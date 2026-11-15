# Codex lifecycle adapter (opt-in pilot)

**Purpose:** give Agent Context Foundation a deterministic opportunity to run at session start, each user prompt and subagent start, and a bounded closeout review when project Git state changes. This is an **adapter for local Codex**, not a replacement for project AGENTS.md, and not proof that an LLM actually understood or followed every rule.

Official Codex documentation: https://learn.chatgpt.com/docs/hooks

## Install in one trusted test repository

1. Keep existing AGENTS.md, Agent/README.md, Agent/INDEX.md, and project error-memory files. Install/update the skill into .agents/skills/agent-context-foundation/ first.
2. Review agent_context_hook.py and hooks.json.example. The hook runs Python on your machine; **do not enable code you have not reviewed**.
3. Copy agent_context_hook.py to <repo>/.codex/hooks/agent_context_hook.py. Copy hooks.json.example to <repo>/.codex/hooks.json **only if that file does not already exist**. Otherwise merge its four event groups; never overwrite other hooks or install this adapter twice.
4. Python 3 and Git must be available. On Windows, py -3 and PowerShell must work; elsewhere, python3 must work. Launch Codex from within the repository. No network service or third-party Python package is required.
5. In the Codex CLI, use /hooks to review and trust the hook definition. The project .codex/ config also must be trusted. Restart Codex and confirm hooks run. A Git commit does not silently enable or trust project hooks.
6. Test a fresh unnamed bugfix, a user correction, a no-change prompt, plan/read-only mode, a subagent and a new session. Confirm actual Agent/ file updates and tests. Do not infer runtime PASS from this adapter's unit tests.

### Behavior and limits

- SessionStart / UserPromptSubmit / SubagentStart inject a short project-context reminder. They never claim the skill was selected.
- UserPromptSubmit creates an advisory Git snapshot at .agent-temp/agent-context-foundation/<opaque-id>.json. It stores **no prompt, transcript, token or customer data**. Stop removes the snapshot on first closeout.
- If Git state differs at Stop, the hook asks the agent **once** to recheck the diff, tests and error-memory closeout. A second stop proceeds without looping.
- No matching repo AGENTS/Agent route, no Git, missing turn ID, or plan mode: no enforcement. Pre-existing changes can cause false positives; edits that leave Git state unchanged can cause false negatives. A hook does not detect every semantic mistake or prove that tests ran.
- A disabled/untrusted hook, unsupported host or timeout cannot enforce anything. A session interrupted before Stop can leave one small local snapshot; clean stale adapter-owned snapshots when no session uses them. Project owners decide whether to ignore .agent-temp in Git.
- Do not enable across all projects until the pilot is evaluated. Claude Code uses a different host-specific hook format.

## Unit tests

From this skill repository's root, run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s integrations/codex/tests -v
```

The unit tests use isolated repositories created **inside** the skill project and removed after execution. They do not emulate Codex itself or test Windows PowerShell.
