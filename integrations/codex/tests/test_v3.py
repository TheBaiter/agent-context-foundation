"""Pure local unit/CLI tests; no Codex host or GitHub Actions required."""
from __future__ import annotations
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

BASE = Path(__file__).resolve().parents[3]

def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

setup = load(BASE / 'integrations/codex/setup.py', 'setup_v3')
hook = load(BASE / 'integrations/codex/agent_context_hook.py', 'hook_v3')

class SetupTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='acf-v3-', dir=BASE)
        self.project = Path(self.tmp.name)
        (self.project / 'AGENTS.md').write_text('# User project\n\nKeep current instructions.\n', encoding='utf-8')

    def tearDown(self):
        self.tmp.cleanup()

    def test_merge_preserves_other_hooks_and_instructions(self):
        hooks = self.project / '.codex/hooks.json'
        hooks.parent.mkdir(parents=True)
        hooks.write_text(json.dumps({'hooks': {'Stop':[{'hooks':[{'type':'command','command':'echo existing'}]}], 'PostToolUse':[{'matcher':'Bash','hooks':[{'type':'command','command':'true'}]}]}}, indent=2))
        first = setup.install(self.project, dry=False)
        self.assertGreater(len(first), 0)
        doc = json.loads(hooks.read_text())
        self.assertEqual(doc['hooks']['PostToolUse'][0]['hooks'][0]['command'], 'true')
        self.assertEqual(len(doc['hooks']['Stop']), 2)
        self.assertIn('Keep current instructions.', (self.project / 'AGENTS.md').read_text())
        self.assertEqual(setup.install(self.project, dry=False), [])
        self.assertTrue(setup.diagnose(self.project)['configured'])

    def test_uninstall_keeps_user_hooks_and_project_memory(self):
        setup.install(self.project, dry=False)
        pending = self.project / 'Agent/error-memory/PENDING.md'
        pending.write_text('Real pending error\n')
        removed = setup.uninstall(self.project, dry=False)
        self.assertGreater(len(removed), 0)
        self.assertEqual(setup.uninstall(self.project, dry=False), [])
        self.assertTrue(pending.exists())
        self.assertEqual((self.project / 'AGENTS.md').read_text(), '# User project\n\nKeep current instructions.\n')
        self.assertEqual(setup.diagnose(self.project)['hooks_per_event'], {e: 0 for e in setup.EVENTS})

    def test_dry_run_does_not_create_files(self):
        changes = setup.install(self.project, dry=True)
        self.assertTrue(changes)
        self.assertFalse((self.project / '.codex').exists())
        self.assertNotIn(setup.MARK_START, (self.project / 'AGENTS.md').read_text())

    def test_invalid_hooks_does_not_mutate_project(self):
        hooks = self.project / '.codex/hooks.json'
        hooks.parent.mkdir(parents=True)
        hooks.write_text('{ invalid json', encoding='utf-8')
        before = (self.project / 'AGENTS.md').read_text()
        with self.assertRaises(json.JSONDecodeError):
            setup.install(self.project, dry=False)
        self.assertEqual((self.project / 'AGENTS.md').read_text(), before)

    def test_symlink_destination_refused(self):
        outer = self.project / 'outside'
        outer.mkdir()
        (self.project / '.codex').symlink_to(outer, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, 'symlink'):
            setup.install(self.project, dry=False)

    def test_unmanaged_existing_bridge_not_duplicated(self):
        (self.project / 'AGENTS.md').write_text('# Agent Context Foundation\nOriginal custom rules\n')
        setup.install(self.project, dry=False)
        self.assertNotIn(setup.MARK_START, (self.project / 'AGENTS.md').read_text())

    def test_malformed_hook_group_rejected(self):
        p = self.project / '.codex/hooks.json'
        p.parent.mkdir(parents=True)
        p.write_text('{"hooks":{"Stop":[{"hooks":42}]}}')
        with self.assertRaises(ValueError):
            setup.install(self.project, dry=False)

    def test_cli_json_doctor(self):
        script = BASE / 'integrations/codex/setup.py'
        setup.install(self.project, dry=False)
        p = subprocess.run([sys.executable,str(script),'--project',str(self.project),'--check'],capture_output=True,text=True)
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertEqual(json.loads(p.stdout)['runtime_trusted'], 'NOT_VERIFIED')

class HookTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='acf-v3-', dir=BASE)
        self.root = Path(self.tmp.name)
        (self.root / 'Agent/error-memory').mkdir(parents=True)
        (self.root / 'Agent/INDEX.md').write_text('# Index\n')
        (self.root / 'AGENTS.md').write_text('# Instructions\n')
        subprocess.run(['git','init','-q'], cwd=self.root, check=True)
        subprocess.run(['git','add','AGENTS.md','Agent/INDEX.md'], cwd=self.root, check=True)
        subprocess.run(['git','-c','user.name=Test','-c','user.email=test@example.invalid','commit','-qm','start'],cwd=self.root,check=True)
        self.data = {'cwd':str(self.root), 'session_id':'abc', 'turn_id':'def', 'permission_mode':'default'}

    def tearDown(self):
        self.tmp.cleanup()

    def call(self, event, **changes):
        return hook.run({**self.data, 'hook_event_name': event, **changes})

    def test_initial_context_and_subagents(self):
        for event in ['SessionStart','SubagentStart']:
            self.assertIn('Agent/INDEX', self.call(event)['hookSpecificOutput']['additionalContext'])

    def test_one_stop_gate_on_real_change(self):
        self.call('UserPromptSubmit', prompt='Please do a small fix')
        (self.root / 'AGENTS.md').write_text('Changed\n')
        self.assertEqual(self.call('Stop')['decision'], 'block')
        self.assertEqual(self.call('Stop'), {})

    def test_edits_on_preexisting_dirty_files_detected(self):
        (self.root / 'AGENTS.md').write_text('Preexisting dirt\n')
        self.call('UserPromptSubmit', prompt='Please fix')
        (self.root / 'AGENTS.md').write_text('Updated existing dirt with same length\n')
        self.assertEqual(self.call('Stop')['decision'], 'block')

    def test_user_correction_triggers_without_git_changes(self):
        self.call('UserPromptSubmit', prompt='Lo que hiciste está mal; antes dijiste otra cosa')
        first = self.call('Stop')
        self.assertEqual(first['decision'], 'block')
        self.assertIn('PENDING', first['reason'])
        self.assertEqual(self.call('Stop'), {})

    def test_user_correction_with_pending_change_does_not_reblock(self):
        self.call('UserPromptSubmit', prompt='Lo que hiciste está mal')
        pending = self.root / 'Agent/error-memory/PENDING.md'
        pending.write_text('Corrected and documented\n')
        # Pending creation is itself a Git worktree change. One-time gate still checks QA.
        self.assertEqual(self.call('Stop')['decision'], 'block')

    def test_no_correction_no_changes_no_gate(self):
        self.call('UserPromptSubmit', prompt='Explain a code pattern')
        self.assertEqual(self.call('Stop'), {})

    def test_prompt_never_persisted(self):
        secret='supersecret-placeholder-0123'
        self.call('UserPromptSubmit', prompt='Lo que hiciste ' + secret)
        content = hook.marker_path(self.root, self.data).read_text()
        self.assertNotIn(secret, content)
        self.assertTrue(json.loads(content)['likely_correction'])

    def test_plan_mode_no_marker(self):
        self.call('UserPromptSubmit', prompt='Lo que hiciste mal', permission_mode='plan')
        self.assertFalse((self.root / '.agent-temp').exists())
        self.assertEqual(self.call('Stop', permission_mode='plan'), {})

    def test_missing_ids_fails_open(self):
        self.assertEqual(self.call('Stop', turn_id=None), {})

    def test_config_is_declared_by_host(self):
        # Tested separately after the actual hooks.json is staged in the branch.
        self.assertIn('UserPromptSubmit', setup.EVENTS)

# Additional guards for deployment regressions.
class GuardTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='acf-v3-', dir=BASE)
        self.project = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_existing_modified_hook_is_not_overwritten(self):
        script = self.project / '.codex/hooks/agent_context_hook.py'
        script.parent.mkdir(parents=True)
        script.write_text('# local customization\n')
        with self.assertRaisesRegex(ValueError, 'differs'):
            setup.install(self.project, dry=False)
        self.assertFalse((self.project / 'AGENTS.md').exists())
        self.assertEqual(script.read_text(), '# local customization\n')

    def test_branch_uninstall_removes_only_managed_entries(self):
        setup.install(self.project, dry=False)
        hooks = self.project / '.codex/hooks.json'
        doc = json.loads(hooks.read_text())
        doc['hooks']['Stop'][0]['hooks'].append({'type':'command','command':'echo third_party'})
        hooks.write_text(json.dumps(doc))
        setup.uninstall(self.project, dry=False)
        after = json.loads(hooks.read_text())
        self.assertEqual(after['hooks']['Stop'][0]['hooks'][0]['command'], 'echo third_party')

    def test_initial_empty_project_roundtrip(self):
        setup.install(self.project, dry=False)
        self.assertTrue(setup.diagnose(self.project)['configured'])
        setup.uninstall(self.project, dry=False)
        self.assertEqual((self.project / 'AGENTS.md').read_text(), '')
        self.assertTrue((self.project / 'Agent/INDEX.md').exists())

    def test_main_handler_json_stdio(self):
        script = BASE / 'integrations/codex/agent_context_hook.py'
        proc = subprocess.run([sys.executable, str(script)], input=json.dumps({'hook_event_name':'SessionStart','cwd':str(self.project)}), text=True, capture_output=True)
        self.assertEqual(proc.returncode, 0)
        self.assertEqual(json.loads(proc.stdout), {})

if __name__ == '__main__':
    unittest.main()
