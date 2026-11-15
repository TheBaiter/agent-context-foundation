# Standing Codex Bridge (copy selectively)

Install the skill globally or in the target repository, then **merge**, do not overwrite, the short block below into:
- `~/.codex/AGENTS.md` (all Codex workspaces; unless the effective global override replaces it); or
- the repository's root `AGENTS.md` (that repo only).

Codex reads this standing file at session start. A skill's `SKILL.md` is **not** a standing file: it is loaded only after selection. Instructions may request skill use, but cannot guarantee host support or selection. Keep the bridge short to protect context budget.

```md
## Agent Context Foundation — standing repository rules
At the start of every repository coding, review, test, documentation, automation, delegated, resumed or handoff task, read the applicable root/scoped AGENTS.md and project Agent/README.md + Agent/INDEX.md (or equivalents). Skim the compact project error-memory INDEX and pending entries once, opening only relevant details.

Use the installed `agent-context-foundation` skill even without being named. If unavailable, outdated or not selected, follow this baseline and disclose the limitation; never claim it loaded. Merge a minimal missing root AGENTS/Agent route when authorized, preserving scoped/generated instructions.

Make the smallest complete change; validate actual behavior, contracts and adjacent regressions before closeout. For visual UI work capture real runtime/test screenshots when possible; otherwise mark checks pending.

On any meaningful agent mistake, including a user correction, immediately append a short task/symptom/evidence/next-check note to project-owned `Agent/error-memory/PENDING.md` (or the project's existing equivalent). Continue independent safe work. Before final delivery review this task's pending errors, group duplicates, verify fixes, write reusable prevention to the short `Agent/error-memory/INDEX.md` with a task/issue anchor, and leave unresolved items pending. Do not merely promise to remember in chat.

Project memory may be Git-tracked or Git-ignored/local-only by project choice; do not change ignore rules automatically. Respect project security/Git policy, and do not use GitHub Actions for tests where prohibited.

```

Do not install the full skill text in `AGENTS.md`, add an untested auto-run hook, or make every task perform a context audit. Existing `AGENTS.override.md` and more local instructions may supersede the bridge.

For a target repository without a root `AGENTS.md`, the code block above can be its initial file. If a root file exists, **append only the missing contract**, preserving generated blocks, project-specific restrictions, and scoped/override instructions. Create `Agent/README.md` and `Agent/INDEX.md` only when there is no existing equivalent, and use those files as concise routers to actual project documents.

Verify in a **fresh Codex session** that the effective instructions were loaded and the agent actually selected `SKILL.md` for an ordinary coding request that did not name the skill. Check a user-correction case and a visual screenshot case separately. Observe a trivial task too: it should stay lightweight. A new GitHub commit or installed skill alone cannot rewrite downstream repositories or global Codex instructions.
