# Standing Codex Bridge (copy selectively)

Install the skill globally or in the target repository, then **merge**, do not overwrite, the short block below into:
- `~/.codex/AGENTS.md` (all Codex workspaces; unless the effective global override replaces it); or
- the repository's root `AGENTS.md` (that repo only).

Codex reads this standing file at session start. A skill's `SKILL.md` is **not** a standing file: it is loaded only after selection. Instructions may request skill use, but cannot guarantee host support or selection. Keep the bridge short to protect context budget.

```md
## Repository engineering baseline
At the start of each repository coding/review task, use the installed `agent-context-foundation` skill when available, even when the user does not name it. Read only the active scoped AGENTS.md and the relevant project Agent/README.md or established equivalent; use Agent/INDEX.md to route details selectively. Do not preload all issues or history.

If the project has no usable context route, add a minimal compatible entrypoint only when file edits are authorized and durable guidance is warranted; otherwise ask or report the blocker without stopping independent work.

Choose the smallest **complete** safe change: reuse existing behavior, respect request scope, account for affected callers/API/integrations, avoid speculative code, and check relevant tests/regressions. No new ticket for trivial work. For a confirmed material agent-caused mistake, create/reuse a focused issue, record failure/cause/fix/verification, close only after verified repair, and retain a one-line issue pointer in the project's canonical Agent error-memory index.

If the skill is unavailable or not selected, follow this compact baseline directly. Obey more specific local policies and do not claim that you loaded an unavailable skill.
```

Do not install the full skill text in `AGENTS.md`, add an untested auto-run hook, or make every task perform a context audit. Existing `AGENTS.override.md` and more local instructions may supersede the bridge.

Verify in a **fresh Codex session** by checking the instruction sources loaded and whether the agent actually reads `SKILL.md` on an ordinary request that does not name the skill. Observe a trivial task too: it should remain lightweight. No repository-only change can alter a user's global Codex instructions.
