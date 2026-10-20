# Codex Customization Template

Use this when the user wants **standing Codex behavior without manually naming the skill each day**.

Keep the project's existing instructions. The global example below is an **excerpt to merge**, not a file to overwrite blindly. Install the skill separately; `AGENTS.md` cannot install it by itself.

## Codex global instructions (`~/.codex/AGENTS.md` or `$CODEX_HOME/AGENTS.md`)

```md
## Repository engineering traceability

For substantive repository debugging, fixes, feature work, migrations, refactors,
or reviews, use the installed `$agent-context-foundation` skill when relevant
without requiring me to mention it. Apply its engineering workflow, not a full
agent-document audit. Follow active project instructions and project-specific
approval, security, and Git conventions.

Even if that skill is unavailable:
- Read the applicable repository instructions and project Agent/README.md route,
  when they exist; use only context relevant to the task.
- For a meaningful discovered defect, reuse an existing authoritative issue/task
  or create one before implementing its repair when tracking is available.
- Record the problem, evidence, plan, important decisions, material failed
  attempts, verification, remaining risk, and handoff in that record.
- Do not claim a fix is complete until the original failure and relevant
  regressions are rechecked. If verification is blocked, state that explicitly.
- Keep active issue history in the task system; promote to agent error memory
  only verified lessons likely to help future tasks.
- Skip extra issue ceremony for trivial, isolated, or transient failures, unless
  a more specific project rule requires it.
```

Use the same concise excerpt in the **existing repository root `AGENTS.md`** rather than globally when these expectations should apply to just that project.

## Verification after adding the instructions

1. Confirm the skill appears in the current agent's installed skill list. A GitHub repository URL by itself is not proof of installation.
2. Restart or start a new Codex session so global/project `AGENTS.md` is reloaded.
3. Ask Codex to list its loaded instruction sources. It should identify the correct global and project scopes.
4. Give it a **natural** repair request without `$agent-context-foundation`, and inspect whether it actually loads the skill and produces the expected issue, implementation, and verification evidence.
5. Try a trivial request to confirm it does not invent unnecessary issue or memory work.

A project `AGENTS.override.md` can take precedence over its same-directory `AGENTS.md`. Respect existing instruction scope instead of creating a competing entrypoint.
