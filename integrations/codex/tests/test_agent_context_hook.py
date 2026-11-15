"""Run with: python3 -m unittest discover -s integrations/codex/tests -v"""
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

PROJECT = Path(__file__).resolve().parents[3]
SCRIPT = PROJECT / 'integrations' / 'codex' / 'agent_context_hook.py'
spec = importlib.util.spec_from_file_location('acf_hook', SCRIPT)
acf = importlib.util.module_from_spec(spec)
spec.loader.exec_module(acf)

class HookTests(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix='acf-hook-test-', dir=PROJECT))
        (self.root / 'Agent').mkdir()
        (self.root / 'Agent' / 'INDEX.md').write_text('# Index\n', encoding='utf-8')
        (self.root / 'AGENTS.md').write_text('# Repo rules\n', encoding='utf-8')
        subprocess.run(['git', 'init', '-q'], cwd=self.root, check=True)
        subprocess.run(['git', 'add', 'AGENTS.md', 'Agent/INDEX.md'], cwd=self.root, check=True)
        subprocess.run(['git', '-c', 'user.name=Test', '-c', 'user.email=test@example.invalid', 'commit', '-qm', 'initial'], cwd=self.root, check=True)
        self.event = {'cwd': str(self.root), 'session_id': 'session-1', 'turn_id': 'turn-1', 'permission_mode': 'default'}

    def tearDown(self):
        shutil.rmtree(self.root)

    def invoke(self, event, **kw):
        return acf.run({**self.event, 'hook_event_name': event, **kw})

    def test_start_injects_project_routes_without_writing(self):
        value = self.invoke('SessionStart')
        self.assertIn('Agent/error-memory/', value['hookSpecificOutput']['additionalContext'])
        self.assertFalse((self.root / '.agent-temp').exists())

    def test_correction_prompt_is_not_stored(self):
        secret = 'do-not-store-private-prompt'
        self.invoke('UserPromptSubmit', prompt=secret)
        marker = acf.marker_path(self.root, self.event)
        self.assertTrue(marker.is_file())
        self.assertNotIn(secret, marker.read_text())

    def test_git_edit_triggers_once_then_allows_stop(self):
        self.invoke('UserPromptSubmit')
        (self.root / 'AGENTS.md').write_text('new rule\n', encoding='utf-8')
        first = self.invoke('Stop')
        self.assertEqual(first['decision'], 'block')
        self.assertIn('regression checks', first['reason'])
        self.assertEqual(self.invoke('Stop'), {})
        self.assertFalse(acf.marker_path(self.root, self.event).exists())

    def test_git_commit_triggers_closeout(self):
        self.invoke('UserPromptSubmit')
        (self.root / 'AGENTS.md').write_text('committed new rule\n', encoding='utf-8')
        subprocess.run(['git', 'add', 'AGENTS.md'], cwd=self.root, check=True)
        subprocess.run(['git', '-c', 'user.name=Test', '-c', 'user.email=test@example.invalid', 'commit', '-qm', 'new'], cwd=self.root, check=True)
        self.assertEqual(self.invoke('Stop')['decision'], 'block')

    def test_stop_hook_active_never_loops(self):
        self.invoke('UserPromptSubmit')
        (self.root / 'AGENTS.md').write_text('change\n', encoding='utf-8')
        self.assertEqual(self.invoke('Stop', stop_hook_active=True), {})

    def test_no_change_does_not_block(self):
        self.invoke('UserPromptSubmit')
        self.assertEqual(self.invoke('Stop'), {})

    def test_plan_mode_has_no_marker_and_no_stop_gate(self):
        self.invoke('UserPromptSubmit', permission_mode='plan')
        self.assertFalse((self.root / '.agent-temp').exists())
        self.assertEqual(self.invoke('Stop', permission_mode='plan'), {})

    def test_not_a_project_is_ignored(self):
        shutil.rmtree(self.root / 'Agent')
        self.assertEqual(self.invoke('SessionStart'), {})

    def test_unknown_events_are_ignored(self):
        self.assertEqual(self.invoke('PreToolUse'), {})

    def test_nested_working_directory_finds_root(self):
        nested = self.root / 'src' / 'lib'
        nested.mkdir(parents=True)
        value = self.invoke('SubagentStart', cwd=str(nested))
        self.assertEqual(value['hookSpecificOutput']['hookEventName'], 'SubagentStart')

    def test_config_is_valid_and_contains_supported_events(self):
        config = json.loads((PROJECT / 'integrations' / 'codex' / 'hooks.json.example').read_text(encoding='utf-8'))
        self.assertEqual(set(config['hooks']), {'SessionStart', 'UserPromptSubmit', 'SubagentStart', 'Stop'})
        for groups in config['hooks'].values():
            for group in groups:
                for hook in group['hooks']:
                    self.assertIn('commandWindows', hook)
                    self.assertNotIn('async', hook)

if __name__ == '__main__':
    unittest.main()
