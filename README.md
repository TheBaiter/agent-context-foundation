# Agent Context Foundation

[![Skill](https://img.shields.io/badge/skill-agent--context--foundation-blue)](https://github.com/TheBaiter/agent-context-foundation)

A lightweight agent skill for ordinary repository coding tasks and agent-context maintenance. Its job is to guide the smallest complete safe change while preserving scoped instructions, regression checks and a compact error trail.

Its job is not to impose one universal agent workflow. Its job is to help agents discover the right context, load only what matters, preserve reusable knowledge, and leave meaningful work traceable.

## Activation: Skill Discovery Is Not Automatic Execution

**Two distinct layers are required for consistent startup behavior:**

- **Standing guidance:** Codex automatically reads active global and repository `AGENTS.md` instructions. This is where the short mandatory baseline belongs.
- **On-demand skill:** Codex initially sees skill name/description and may select the full `SKILL.md` for matching tasks. A positive `allow_implicit_invocation` flag permits selection; it does not itself start or force the skill. `agents/openai.yaml` is launcher metadata, not a startup hook.

The updated description now matches normal tasks such as `fix the bug`, `implement this feature`, `refactor` and `review this code`, without requiring a literal skill mention. Installing only in one repository does **not** expose the skill in every other repository.

### Codex installation and update

```bash
# Make this skill visible in Codex across repositories
npx skills add TheBaiter/agent-context-foundation -g -a codex
npx skills ls -g -a codex

# Check/update installed copies when the repository changes
npx skills check
npx skills update agent-context-foundation -g

# For an installation scoped only to the current repository:
npx skills add TheBaiter/agent-context-foundation -a codex
npx skills update agent-context-foundation -p
```

Merge the short [Codex standing bridge](references/templates/codex-customization.md) into the existing `~/.codex/AGENTS.md` or the target repository `AGENTS.md`, without replacing other rules or an effective `AGENTS.override.md`. A global file affects Codex sessions on that machine; a repository file affects that project. Use a **new session** to check that both the standing instructions and the updated skill are visible. A GitHub update alone does not update any user's installation.

For other coding agents, use their supported persistent-instruction files and skill installation scope; behavior varies by host. **No skill text alone can guarantee implicit activation in every agent.**

### Project instruction layout

- `AGENTS.md`: startup instructions recognized by Codex (root/scoped or global).
- `Agent/README.md` and `Agent/INDEX.md`: optional project-specific routing and durable context.
- `Agent/error-memory/INDEX.md`: short pointers to verified agent mistakes, with the issue as owner of detail.
- `agents/openai.yaml` in **this skill repo**: optional skill UI metadata, not your project's instruction folder.
- `.agents/skills/`: one recognized repository-level skill installation location.

Check existing conventions first. If a needed `Agent/` foundation is absent, create a tiny route when repository edits are authorized, otherwise request permission. Do not create competing folders or bulk-load an entire agent history.

### Smallest complete change and Ponytail

For repository code, prefer reusing an existing implementation, changing the least necessary surface, and including affected callers/tests/security boundaries. Minimal diff is not an excuse to leave a half-working feature. This aligns with [Ponytail](https://github.com/DietrichGebert/ponytail), a separate optional skill; it is **not a dependency** of Agent Context Foundation.

```bash
# Optional: install Ponytail independently for Codex
npx skills add DietrichGebert/ponytail -g -a codex --skill ponytail
```

### Trigger and behavior checks

See `evals/activation-cases.csv` for prompts that should select the skill and negative controls for unrelated tasks. Evaluate in fresh installed-agent sessions: distinguish *skill listed*, *skill actually loaded*, and *behavior followed*. Static metadata checks **cannot prove** runtime activation; if selection fails, keep the standing `AGENTS.md` baseline and report the miss rather than claiming success.

## Core Model

```text
SKILL.md
  -> decide what the task needs
  -> establish the task boundary from the request and minimum relevant source
  -> read a specific issue only if a trigger exists
  -> load a relevant module only if needed
  -> load one specific template only if output must be generated
  -> apply the minimum coherent change
  -> validate
  -> update task trace
```

The skill follows these principles:

- minimum viable context,
- progressive disclosure,
- canonical ownership,
- evidence-based module creation,
- scoped/local instructions,
- verified memory promotion,
- staleness and retirement,
- exact verification anchors,
- durable task traceability,
- task-boundary checks without routine issue-history retrieval,
- separation of capability access from authentication and persistence,
- positive/negative/regression checks across modes and integrations,
- issue-based correction and closure for confirmed meaningful agent errors,
- active problem history owned by the authoritative task instead of repository context,
- staged diagnosis/planning/implementation/revalidation for non-trivial fixes,
- no universal Git/review policy,
- repository language/encoding preservation,
- one temporary workspace for disposable QA/visual/debug artifacts.

## Operational By Default

When the skill applies, its relevant rules are meant to be executed.

An optional module is optional only until repository evidence makes it relevant. Once activated, its applicable rules are operational defaults.

The agent should not turn executable rules into "recommendations" or "things to consider" when it has authority to apply them directly. Recommendations are reserved for genuinely optional improvements or real user/project decision boundaries.

The final report should describe what was applied, skipped, blocked, or not applicable.

## Why

Agent documentation often grows into a second codebase: large entry files, duplicated rules, stale memory, generic checklists, and historical logs that every future task pays to read.

This skill tries to prevent that.

A supported capability is not automatically generated. A module exists only when repository evidence shows that it reduces future risk, confusion, or rediscovery.

The correct result may be no documentation change.

## Minimum Foundation

Preserve an existing valid agent instruction standard such as root or nested `AGENTS.md`.

If a new routed `Agent/` foundation is actually needed, start with only:

```text
Agent/
  README.md
  INDEX.md
```

Everything else is optional.

Examples:

```text
project-map.md   -> owner or entrypoint discovery is repeatedly expensive
error-memory/    -> verified reusable failure knowledge exists
tools/           -> a repeated procedure is fragile or mechanical
summaries/       -> a complex area is repeatedly reconstructed
planning/        -> durable project-specific planning conventions exist
project-rules.md -> project-wide non-obvious constraints exist
checklists/      -> specialized recurring verification is needed
```

Do not create empty folders, hypothetical error categories, or documentation merely because a template exists.

## Context Budget And Task Boundaries

The default is the current request + relevant local agent instructions + narrow code/contract owner. Do not automatically read issues, their comments, linked tasks, every module or an entire repository. **Only consult a specific issue when directly named, needed to resolve a real contradiction/dependency, or relevant to a confirmed error.** Stop context retrieval once the requested behavior, owner and validation route are clear.

For complex cross-mode work, use `references/task-boundaries.md` selectively. Keep access distinct from login, external authorization and data persistence: a guest mode without cloud saving can still allow catalog browsing or safely scoped temporary integration when the actual contract permits it. Verify allowed and denied behavior plus adjacent regressions.

## Errors, Traceability And Memory

When an agent causes a meaningful error or regression, create or reuse one issue in the project's existing tracker and record: **what happened, why it failed (if known), how it was corrected, what tests were run and the preventive rule**. After a fresh successful validation, close the issue. If validation is blocked, leave it open with the exact pending check; do not report an unverified fix as complete.

Write one compact pointer to `Agent/error-memory/INDEX.md` or the existing canonical equivalent:

`#123 — disabled guest catalog due to cloud-save assumption — check access and persistence separately`

That line remains useful even after the issue is closed, while detail stays in the issue. A future agent reads only a relevant pointer and opens the full issue when it cannot resolve a recurring case. No duplicate issue body, long timeline, universal issue preflight or blanket scan. A more detailed reusable memory case is optional, subject to evidence and maintenance value.

Ordinary work does not require a new issue or routine issue reading. The project's own task/commit conventions still apply. See `references/task-traceability.md` and `references/modules/error-memory.md` only when needed.

## Repository Architecture

```text
SKILL.md
agents/
  openai.yaml

references/
  foundation-principles.md
  task-traceability.md
  task-boundaries.md

  modules/
    foundation.md
    project-map.md
    error-memory.md
    tools.md
    summaries.md
    planning.md
    project-rules.md
    checklists.md
    migration.md
    codex-customization.md
    temporary-workspace.md

  templates/
    base-readme.md
    base-index.md
    project-map.md
    error-memory-readme.md
    error-memory-index.md
    error-case.md
    planning.md
    project-rules.md
    checklists-index.md
    codex-customization.md
```

## Progressive Loading

`SKILL.md` is the decision engine.

It should be enough to determine which module, if any, applies.

Examples:

- creating or repairing the base route -> read `references/modules/foundation.md` (only if routing is actually defective),
- recurring failure knowledge -> read `references/modules/error-memory.md`,
- migration/compaction -> read `references/modules/migration.md`,
- project-specific planning conventions -> read `references/modules/planning.md`,
- uncertain feature boundaries crossing guest/auth/API/persistence modes -> read `references/task-boundaries.md` only if necessary.

Only after the module decides that output is needed should the agent load the corresponding template.

Do not load every reference or template up front.

## Temporary Agent Workspace

Reuse the repository's existing temporary workspace when one already exists. Otherwise use a single root:

```text
.agent-temp/
```

Put disposable screenshots, visual QA captures, temporary reports, logs, scratch files, exports, and intermediate artifacts there instead of scattering them across the repository.

Task planning and traceability do not belong there. If a temporary artifact becomes durable, move it to its canonical project location before closing the task.

## Error Memory

Use an existing `Agent/error-memory/INDEX.md` or equivalent for one-line references to confirmed agent errors, with issue number, short cause and prevention. Create it when the first meaningful agent error warrants a pointer; do not create empty category trees. Keep the full repair narrative in its issue, close only on verified repair, and preserve the short pointer after closure while useful. Long reusable cases are evidence-driven and optional; do not preload them.

## Language And Encoding

Preserve the repository's established language and encoding.

Use UTF-8 when no explicit portability constraint exists.

Use ASCII-only only when a real toolchain, terminal, integration, or portability requirement justifies it.

## Git And Project Policy

The skill does not impose a universal branch, draft PR, merge, review, approval, credential, or deployment workflow.

Those rules belong to the repository or to an evidence-backed project-rules module.

## Manual invocation

The canonical skill name is `$agent-context-foundation`. Explicit invocation remains available when implicit matching misses; the persistent bridge is the primary way to request it on every repository task.

## Self-Audit

The skill should apply its own principles to itself.

A healthy version should have:

- a compact `SKILL.md`,
- focused modules,
- small templates,
- no duplicated policy ownership,
- no obsolete active routes,
- no hypothetical module structure,
- no universal project-specific rules,
- task history separated from durable memory,
- active problem history stored in the authoritative task rather than duplicated into repository context,
- closed error issues referenced by short Agent error-memory pointers,
- no systematic issue reading for ordinary work.

The skill should become easier to extend by adding a module without making `SKILL.md` grow into a manual again.
