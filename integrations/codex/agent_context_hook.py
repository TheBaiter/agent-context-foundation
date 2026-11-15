#!/usr/bin/env python3
"""Optional Codex lifecycle hook. No network, no transcript or prompt persistence.

Output is advisory. Hook installation/trust and model compliance require host tests.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys

MAX_INPUT_BYTES = 65536
MAX_CONTEXT_CHARS = 1100
MAX_DIRTY_FILES = 128
# Heuristic only: may miss corrections or match an ordinary task. Never persist text.
CORRECTION = re.compile(
    r'\b(?:lo que hiciste|te equivocaste|rompiste|volviste a|se te olvid[oó]|'
    r'no respetaste|antes dijiste|me dijiste|your (?:last|previous) (?:change|answer)|'
    r'you (?:broke|forgot|missed)|again,? you)\b', re.IGNORECASE)


def project_root(cwd: object) -> Path | None:
    if not isinstance(cwd, str) or not cwd:
        return None
    path = Path(cwd).resolve()
    if not path.is_dir():
        return None
    for candidate in (path, *path.parents):
        if (candidate / 'AGENTS.md').is_file() and (candidate / 'Agent/INDEX.md').is_file():
            return candidate
    return None


def git_snapshot(root: Path) -> str | None:
    """Advisory working tree fingerprint; captures repeated edits to already-dirty files."""
    try:
        head = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=root,
                              capture_output=True, timeout=4, check=True).stdout.strip()
        raw = subprocess.run(['git', 'status', '--porcelain=v1', '-z',
                              '--untracked-files=normal'], cwd=root,
                             capture_output=True, timeout=6, check=True).stdout
    except (OSError, subprocess.SubprocessError):
        return None
    parts = [p for p in raw.split(b'\0') if p and not p[3:].startswith(b'.agent-temp/')]
    digest = hashlib.sha256(head)
    # Hash working-tree metadata as well as status, bounded for predictable cost.
    for part in parts:
        digest.update(part)
    count = 0
    for part in parts:
        if len(part) < 4 or part[:2] == b'??' and part[3:].endswith(b'/'):
            continue
        rel = os.fsdecode(part[3:])
        if rel.startswith('.agent-temp/'):
            continue
        if count >= MAX_DIRTY_FILES:
            break
        count += 1
        path = root / rel
        try:
            stat = path.lstat()
            digest.update(f'{rel}:{stat.st_size}:{stat.st_mtime_ns}:{stat.st_mode}'.encode('utf-8', 'replace'))
        except OSError:
            digest.update(f'{rel}:missing'.encode())
    return digest.hexdigest()


def pending_fingerprint(root: Path) -> str:
    pending = root / 'Agent/error-memory/PENDING.md'
    try:
        return hashlib.sha256(pending.read_bytes()).hexdigest() if pending.is_file() else 'missing'
    except OSError:
        return 'unavailable'


def marker_path(root: Path, data: dict) -> Path | None:
    session, turn = data.get('session_id'), data.get('turn_id')
    if not isinstance(session, str) or not isinstance(turn, str) or not session or not turn:
        return None
    key = hashlib.sha256((session + '\0' + turn).encode('utf-8')).hexdigest()[:32]
    return root / '.agent-temp/agent-context-foundation' / (key + '.json')


def context(event: str, root: Path, correction: bool = False) -> dict:
    message = (
        'Agent Context Foundation: before repository work, read effective AGENTS.md, '
        'Agent/README.md and Agent/INDEX.md. Skim the short error-memory INDEX '
        'and PENDING, open only relevant details. Use the installed skill if selected. '
        'For meaningful agent errors including user corrections, record a short '
        'project-owned PENDING entry during the task. Before handoff validate changes '
        'and regressions, consolidate only verified prevention, disclose missing QA. '
        'Never claim the skill loaded or tests ran without evidence.'
    )
    if (root / 'Agent/error-memory/PENDING.md').is_file():
        message += ' Existing pending lessons: Agent/error-memory/PENDING.md.'
    if correction:
        message += ' This prompt may correct earlier agent work: evaluate and record any confirmed mistake now.'
    return {'hookSpecificOutput': {'hookEventName': event, 'additionalContext': message[:MAX_CONTEXT_CHARS]}}


def run(data: dict) -> dict:
    event = data.get('hook_event_name')
    if event not in {'SessionStart', 'UserPromptSubmit', 'SubagentStart', 'Stop'}:
        return {}
    root = project_root(data.get('cwd'))
    if root is None:
        return {}
    if event in {'SessionStart', 'SubagentStart'}:
        return context(event, root)
    if event == 'UserPromptSubmit':
        prompt = data.get('prompt')
        likely_correction = isinstance(prompt, str) and bool(CORRECTION.search(prompt[:8192]))
        if data.get('permission_mode') != 'plan':
            marker = marker_path(root, data)
            snapshot = git_snapshot(root) if marker is not None else None
            if marker is not None:
                record = {'git': snapshot, 'pending': pending_fingerprint(root),
                          'likely_correction': likely_correction}
                try:
                    marker.parent.mkdir(parents=True, exist_ok=True)
                    if marker.is_symlink():
                        return context(event, root, likely_correction)
                    marker.write_text(json.dumps(record) + '\n', encoding='utf-8')
                except OSError:
                    pass
        return context(event, root, likely_correction)
    if data.get('permission_mode') == 'plan' or data.get('stop_hook_active') is True:
        return {}
    marker = marker_path(root, data)
    if marker is None or not marker.is_file() or marker.is_symlink():
        return {}
    try:
        record = json.loads(marker.read_text(encoding='utf-8'))
        marker.unlink()  # One review continuation at most, even if model fails.
    except (OSError, ValueError, TypeError):
        return {}
    now = git_snapshot(root)
    changed = bool(record.get('git') and now and record['git'] != now)
    correction_missing = bool(record.get('likely_correction') and
                              record.get('pending') == pending_fingerprint(root))
    if not changed and not correction_missing:
        return {}
    reasons = []
    if changed:
        reasons.append('Repository files changed; inspect the actual diff and run feasible regression checks.')
    if correction_missing:
        reasons.append('A possible user correction was detected but the project PENDING ledger was unchanged. Determine whether this is a meaningful agent mistake; if confirmed, write a short, non-sensitive entry now.')
    reasons.append('Review task errors and leave unverified lessons pending; report exactly which tests and visual checks ran. Do not invent evidence. Then finish without another Stop continuation.')
    return {'decision': 'block', 'reason': ' Agent Context Foundation closeout review: ' + ' '.join(reasons)}


def main() -> None:
    try:
        raw = sys.stdin.buffer.read(MAX_INPUT_BYTES + 1)
        if len(raw) > MAX_INPUT_BYTES:
            raise ValueError('oversized hook input')
        data = json.loads(raw)
        result = run(data) if isinstance(data, dict) else {}
    except (ValueError, OSError, UnicodeError):
        result = {}  # Optional hook must never stall normal user work.
    sys.stdout.write(json.dumps(result, ensure_ascii=False) + '\n')


if __name__ == '__main__':
    main()
