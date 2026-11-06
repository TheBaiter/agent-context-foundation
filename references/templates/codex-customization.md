# Standing Codex Bridge (copy selectively)

Install the skill globally or in the target repository, then **merge**, do not overwrite, the short block below into:
- `~/.codex/AGENTS.md` (all Codex workspaces; unless the effective global override replaces it); or
- the repository's root `AGENTS.md` (that repo only).

Codex reads this standing file at session start. A skill's `SKILL.md` is **not** a standing file: it is loaded only after selection. Instructions may request skill use, but cannot guarantee host support or selection. Keep the bridge short to protect context budget.

```md
## Agent Context Foundation — standing repository rules
At the start of **every repository coding, review, fix, test, documentation or maintenance task**, read this root/scoped AGENTS.md and the relevant project Agent/README.md and Agent/INDEX.md (or an established equivalent); follow their applicable rules. Route selectively; do not preload all issue histories.

Use the installed `agent-context-foundation` skill for these tasks even when not explicitly named. If the skill is not available, obey this baseline and report the activation limitation; never claim to have loaded it.

If this project is writable and lacks an effective root AGENTS.md bridge or an Agent/ route (or equivalent), create/merge the minimal missing files while preserving existing rules. Do not overwrite generated/scoped instructions.

Choose the smallest **complete** change. Validate the resulting diff, actual behavior and regressions before showing an example or declaring completion. For UI/visual results, inspect the running application and share genuine screenshots of the observed state/tests when capture is available; if unavailable, mark visual verification pending. Report actual tests and skipped checks distinctly.

For every confirmed meaningful agent mistake **including corrections discovered by the user**, create or reuse a focused issue: failure, missed check/cause, fix, actual validation and preventive rule. Keep one short pointer in `Agent/error-memory/INDEX.md` or the project's canonical equivalent. Close the issue only after required verification succeeds. Do not create issues for harmless transient retries.

Follow local security and Git policies. Do not execute GitHub Actions for testing where prohibited. 
```

Do not install the full skill text in `AGENTS.md`, add an untested auto-run hook, or make every task perform a context audit. Existing `AGENTS.override.md` and more local instructions may supersede the bridge.

For a target repository without a root `AGENTS.md`, the code block above can be its initial file. If a root file exists, **append only the missing contract**, preserving generated blocks, project-specific restrictions, and scoped/override instructions. Create `Agent/README.md` and `Agent/INDEX.md` only when there is no existing equivalent, and use those files as concise routers to actual project documents.

Verify in a **fresh Codex session** that the effective instructions were loaded and the agent actually selected `SKILL.md` for an ordinary coding request that did not name the skill. Check a user-correction case and a visual screenshot case separately. Observe a trivial task too: it should stay lightweight. A new GitHub commit or installed skill alone cannot rewrite downstream repositories or global Codex instructions.
