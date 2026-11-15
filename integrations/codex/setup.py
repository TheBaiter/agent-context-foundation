#!/usr/bin/env python3
"""Non-destructive Codex project integration installer and diagnostic.

Run from an installed source checkout with: python integrations/codex/setup.py --project PATH --install
Never silently replaces existing user instructions or unrelated hooks.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
HOOK_SOURCE = ROOT / 'integrations/codex/agent_context_hook.py'
HOOK_NAME = 'agent_context_hook.py'
MARK_START = '<!-- agent-context-foundation:begin v3 -->'
MARK_END = '<!-- agent-context-foundation:end -->'
EVENTS = ('SessionStart', 'UserPromptSubmit', 'SubagentStart', 'Stop')
BRIDGE = '''\n{start}
## Agent Context Foundation (project lifecycle)
On every repository task, read the applicable root/scoped `AGENTS.md` and `Agent/README.md`,
then `Agent/INDEX.md`; consult the compact error-memory index and pending notes for
relevant lessons. Use `agent-context-foundation` when available. If not selected,
follow these standing rules without claiming the skill was loaded.

For a meaningful agent mistake, including a user correction, record a short fact
and next check in project-owned `Agent/error-memory/PENDING.md` during work. Before
closing, verify the actual change and regressions, consolidate only proven
prevention in `Agent/error-memory/INDEX.md`, and leave unverified work pending.
No fabricated tests/screenshots. Do not change Git/ignore policy automatically;
project memory may be Git tracked or local/ignored by project policy.
{end}
'''.format(start=MARK_START, end=MARK_END)


def paths(project: Path) -> dict[str, Path]:
    return {
        'agents': project / 'AGENTS.md',
        'index': project / 'Agent/INDEX.md',
        'readme': project / 'Agent/README.md',
        'errors': project / 'Agent/error-memory/INDEX.md',
        'hook_script': project / '.codex/hooks/agent_context_hook.py',
        'hooks': project / '.codex/hooks.json',
    }


def managed_hook(script: str) -> dict:
    return {'type': 'command',
            'command': f'python3 "$(git rev-parse --show-toplevel)/{script}"',
            'commandWindows': (
                'powershell -NoProfile -Command '
                '"$root = git rev-parse --show-toplevel; '
                f'py -3 (Join-Path $root \'{script}\')"'),
            'timeout': 10,
            'additionalContextLimit': 1000}


def is_managed(hook: object) -> bool:
    return isinstance(hook, dict) and HOOK_NAME in str(hook.get('command', ''))


def merge_hooks(existing: dict, installed: bool) -> dict:
    """Change ONLY our hook handlers; preserve third-party events/matchers."""
    if not isinstance(existing, dict):
        raise ValueError('hooks.json root must be an object')
    doc = json.loads(json.dumps(existing))
    hooks = doc.setdefault('hooks', {})
    if not isinstance(hooks, dict):
        raise ValueError('hooks must be an object')
    for event, groups in list(hooks.items()):
        if not isinstance(groups, list):
            raise ValueError(f'hooks.{event} must be an array')
        retained = []
        for group in groups:
            if not isinstance(group, dict) or not isinstance(group.get('hooks'), list):
                raise ValueError(f'Unexpected hooks.{event} group; refusing to overwrite')
            other = [h for h in group['hooks'] if not is_managed(h)]
            if other:
                retained.append({**group, 'hooks': other})
        if retained:
            hooks[event] = retained
        else:
            del hooks[event]
    if installed:
        script = '.codex/hooks/agent_context_hook.py'
        for event in EVENTS:
            group = {'hooks': [managed_hook(script)]}
            if event == 'SessionStart':
                group['matcher'] = 'startup|resume|clear|compact|fork'
            hooks.setdefault(event, []).append(group)
    return doc


def load_hooks(filename: Path) -> dict:
    if not filename.exists():
        return {}
    if filename.is_symlink():
        raise ValueError(f'Refusing to follow symlink: {filename}')
    return json.loads(filename.read_text(encoding='utf-8'))


def write_if_changed(path: Path, content: str, dry: bool, changes: list[str]):
    if any(ancestor.is_symlink() for ancestor in (path, *path.parents)):
        raise ValueError(f'Refusing to follow symlink: {path}')
    if path.exists() and path.read_text(encoding='utf-8') == content:
        return
    changes.append(str(path))
    if not dry:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding='utf-8', newline='\n')


def install(project: Path, *, dry: bool) -> list[str]:
    p = paths(project)
    if not HOOK_SOURCE.is_file():
        raise ValueError(f'Missing source hook: {HOOK_SOURCE}')
    if not project.is_dir():
        raise ValueError(f'Not a directory: {project}')
    changes = []
    # Preflight every managed output before first write to avoid partial installs.
    for destination in p.values():
        if any(parent.is_symlink() for parent in (destination, *destination.parents)):
            raise ValueError(f'Refusing symlink destination: {destination}')
    existing = load_hooks(p['hooks'])
    merged = merge_hooks(existing, installed=True)
    if p['hook_script'].exists() and p['hook_script'].read_text(encoding='utf-8') != HOOK_SOURCE.read_text(encoding='utf-8'):
        raise ValueError('Existing hook script differs; review changes before replacing (remove the old script explicitly to upgrade)')
    agents = p['agents'].read_text(encoding='utf-8') if p['agents'].exists() else ''
    if p['agents'].is_symlink():
        raise ValueError('AGENTS.md is a symlink')
    if MARK_START in agents or MARK_END in agents:
        if agents.count(MARK_START) != 1 or agents.count(MARK_END) != 1:
            raise ValueError('Ambiguous managed AGENTS.md markers')
        before, middle = agents.split(MARK_START, 1)
        _, after = middle.split(MARK_END, 1)
        agents = before + BRIDGE.strip('\n') + after
    elif 'Agent Context Foundation' not in agents:
        agents = agents + ('\n' if agents else '') + BRIDGE.strip('\n') + '\n'
    # Unmanaged existing guidance is respected; do not duplicate it.
    if agents:
        write_if_changed(p['agents'], agents, dry, changes)
    initial = {
        'readme': '# Agent context\n\nFollow the root AGENTS.md; use [INDEX.md](INDEX.md) to locate project knowledge.\n',
        'index': '# Agent context index\n\n- [Error memory](error-memory/INDEX.md) (when present)\n- `error-memory/PENDING.md`: unresolved user/agent corrections (when present)\n',
        'errors': '# Verified error memory\n\nIndex verified lessons by source issue/task. Keep unresolved errors in PENDING.md.\n',
    }
    for key, initial_text in initial.items():
        if not p[key].exists():
            write_if_changed(p[key], initial_text, dry, changes)
    write_if_changed(p['hooks'], json.dumps(merged, indent=2, ensure_ascii=False) + '\n', dry, changes)
    write_if_changed(p['hook_script'], HOOK_SOURCE.read_text(encoding='utf-8'), dry, changes)
    return changes


def uninstall(project: Path, *, dry: bool) -> list[str]:
    p = paths(project)
    changes = []
    for dest in p.values():
        if any(parent.is_symlink() for parent in (dest, *dest.parents)):
            raise ValueError(f'Refusing symlink destination: {dest}')
    current = load_hooks(p['hooks'])
    merged = merge_hooks(current, installed=False)
    if p['agents'].exists():
        if p['agents'].is_symlink():
            raise ValueError('AGENTS.md is a symlink')
        agents = p['agents'].read_text(encoding='utf-8')
        if MARK_START in agents or MARK_END in agents:
            if agents.count(MARK_START) != 1 or agents.count(MARK_END) != 1:
                raise ValueError('Ambiguous managed AGENTS.md markers')
            before, suffix = agents.split(MARK_START, 1)
            _, after = suffix.split(MARK_END, 1)
            write_if_changed(p['agents'], before[:-1] + after[1:] if before.endswith('\n') and after.startswith('\n') else (after[1:] if not before and after.startswith('\n') else before + after), dry, changes)
    if merged != current:
        write_if_changed(p['hooks'], json.dumps(merged, indent=2, ensure_ascii=False) + '\n', dry, changes)
    # Delete only our own known script. Preserve all Agent/ memory and skill files.
    if p['hook_script'].exists():
        if p['hook_script'].is_symlink():
            raise ValueError('Hook script is a symlink')
        if p['hook_script'].read_text(encoding='utf-8') == HOOK_SOURCE.read_text(encoding='utf-8'):
            changes.append(str(p['hook_script']))
            if not dry:
                p['hook_script'].unlink()
    return changes


def diagnose(project: Path) -> dict:
    p = paths(project)
    agents = p['agents'].read_text(encoding='utf-8') if p['agents'].is_file() and not p['agents'].is_symlink() else ''
    try:
        conf = load_hooks(p['hooks'])
        handlers = conf.get('hooks', {})
        events = {
            e: sum(1 for g in handlers.get(e, []) for h in g.get('hooks', []) if is_managed(h))
            for e in EVENTS
        }
        errors = []
    except (ValueError, json.JSONDecodeError, TypeError, KeyError) as exc:
        events = {}
        errors = [str(exc)]
    source = HOOK_SOURCE.read_text(encoding='utf-8') if HOOK_SOURCE.exists() else ''
    script_ok = p['hook_script'].is_file() and not p['hook_script'].is_symlink() and p['hook_script'].read_text(encoding='utf-8') == source
    return {
        'project': str(project),
        'standing_instructions': bool(agents),
        'managed_bridge': MARK_START in agents and MARK_END in agents,
        'agent_index': p['index'].is_file(),
        'memory_index': p['errors'].is_file(),
        'script_matches_source': script_ok,
        'skill_project_copy_present': (project / '.agents/skills/agent-context-foundation/SKILL.md').is_file(),
        'skill_global_copy': 'NOT_VERIFIED',
        'hooks_per_event': events,
        'configured': bool(agents) and p['index'].is_file() and script_ok and all(events.get(e) == 1 for e in EVENTS),
        'runtime_trusted': 'NOT_VERIFIED',
        'skill_loaded': 'NOT_VERIFIED',
        'errors': errors,
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--project', required=True, help='Existing target repository directory')
    modes = ap.add_mutually_exclusive_group(required=True)
    modes.add_argument('--install', action='store_true')
    modes.add_argument('--check', action='store_true')
    modes.add_argument('--uninstall', action='store_true')
    ap.add_argument('--dry-run', action='store_true', help='Show planned files without modifying them')
    args = ap.parse_args(argv)
    project = Path(args.project).resolve()
    if not project.is_dir():
        ap.error(f'Project directory does not exist: {project}')
    try:
        changes = install(project, dry=args.dry_run) if args.install else (uninstall(project, dry=args.dry_run) if args.uninstall else [])
        result = diagnose(project)
        result['changes'] = changes
        result['dry_run'] = args.dry_run
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0 if args.install or args.uninstall or result['configured'] else 1
    except (OSError, ValueError, UnicodeError) as exc:
        print(json.dumps({'error': str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
