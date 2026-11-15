# V3 real-host acceptance (not yet executed)

Run in a fresh, trusted Codex session on the feature branch. Record OS/host version, effective AGENTS route, actual hook invocation, skill load, files read/written, executed tests and blockers. Redact sensitive content and keep temporary files inside the project. No GitHub Actions.

| Scenario | Evidence needed |
| --- | --- |
| Ordinary bugfix without naming skill | Hook firing vs selected SKILL.md vs observed task/QA |
| Correction from user | During-task PENDING write; verified repair; unresolved notes retained |
| Next session | Agent recovers relevant INDEX/PENDING without old chat |
| Compaction/subagent | Effective routes and memory recovered; no duplicate ownership |
| Existing dirty file edited again | One closeout request and no infinite Stop loop |
| Plan/read-only/no-change | No unauthorized write, no fabricated test results |
| Pre-existing hooks | Non-managed handlers preserved; no duplicated installation |
| Native Windows | PowerShell/py/git command actually executed and parsed |
| Host trust disabled | Explicit fallback and no false promise of enforcement |
| Visual UI | Genuine runtime screenshot or unverified status |

Report distinct STATIC, UNIT, HOST HOOK, SKILL SELECTED, BEHAVIOR, CROSS-SESSION evidence, with observed counts including failures. Benchmark key positive/negative prompts repeatedly before marking epic #13 done.
