# Agent Context Foundation

[![Skill](https://img.shields.io/badge/skill-agent--context--foundation-blue)](https://github.com/TheBaiter/agent-context-foundation)

A modular agent skill for creating, repairing, compacting, and auditing repository context.

Its job is not to impose one universal agent workflow. Its job is to help agents discover the right context, load only what matters, preserve reusable knowledge, and leave meaningful work traceable.

## Core Model

```text
SKILL.md
  -> decide what the task needs
  -> load one relevant module
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
- issue-first lifecycle for meaningful discovered problems,
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

## Task Traceability

Meaningful work should use the project's existing issue, ticket, task, work item, plan, or equivalent system.

The task record should preserve enough information to resume the work:

- goal and status,
- scope and success criteria,
- plan,
- important decisions and reasons,
- evidence,
- verification,
- relevant failures or blockers,
- current handoff,
- next action.

When an agent discovers a concrete bug, regression, defect, or implementation problem that requires a meaningful change, it should create or reuse the authoritative issue/task before implementing the repair when the project has a tracker.

Prefer one issue/task for the whole lifecycle. It should capture how the problem was found, confirming evidence, affected scope, diagnosis, repair plan, scope review, implementation, revalidation, and final closure evidence.

That active history belongs in the issue/task, not duplicated into `AGENTS.md`, `Agent/` documentation, planning files, summaries, error memory, or other reusable repository context merely to remember the problem. If local discoverability is useful, keep only a compact pointer to the authoritative issue/task.

This keeps transient investigation and status out of default agent context, reduces file growth and stale duplicated state, and preserves one exact route to the current source of truth.

When the issue is resolved, remove stale active-problem pointers unless they still have a justified durable routing purpose. Only verified reusable conclusions should be promoted into durable agent documentation or error memory.

For non-trivial problems, keep confirmation, diagnosis, planning, implementation, and revalidation as separate checkpoints instead of one monolithic reasoning pass. Independent final validation is preferred when practical; otherwise the implementing agent should perform a fresh review pass separated from implementation.

Do not close the issue merely because code exists. Close it only after the intended fix is applied, required verification succeeds, regressions are considered, and remaining risk or follow-up is recorded.

Task history stays in the task record.

Only verified reusable conclusions are promoted into durable agent documentation or error memory.

## Repository Architecture

```text
SKILL.md
agents/
  openai.yaml

references/
  foundation-principles.md
  task-traceability.md

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

- creating or repairing the base route -> read `references/modules/foundation.md`,
- recurring failure knowledge -> read `references/modules/error-memory.md`,
- migration/compaction -> read `references/modules/migration.md`,
- project-specific planning conventions -> read `references/modules/planning.md`.

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

Error memory is evidence-driven.

The minimum structure is:

```text
Agent/error-memory/
  README.md
  errors/
    INDEX.md
```

Categories are created only after real verified cases exist.

Knowledge moves through:

```text
discovered -> candidate -> verified -> durable
```

Stale cases may become challenged, superseded, or retired.

Investigation chronology belongs in task traceability, not in error memory. Active issue state must not be mirrored into error memory; only verified reusable lessons belong there.

## Language And Encoding

Preserve the repository's established language and encoding.

Use UTF-8 when no explicit portability constraint exists.

Use ASCII-only only when a real toolchain, terminal, integration, or portability requirement justifies it.

## Git And Project Policy

The skill does not impose a universal branch, draft PR, merge, review, approval, credential, or deployment workflow.

Those rules belong to the repository or to an evidence-backed project-rules module.

## When It Activates

A compatible agent discovers installed skills from their `name` and `description`. It may select this skill **without an explicit `$agent-context-foundation` request** when a substantive repository task involves existing project instructions, traceability for a meaningful fix or refactor, recurring failure knowledge, or agent-context maintenance.

The skill is **not** a general prerequisite for every code edit. It should stay out of trivial changes, questions without repository context, and unrelated work. When selected during implementation, the agent should perform the requested work while applying only the relevant foundation rules; it should not conduct a full documentation audit by default.

Skill selection is model- and host-dependent; writing a stronger description improves discoverability but cannot guarantee activation. The `agents/openai.yaml` launcher describes a manually selectable prompt. Its `default_prompt` is not an automatic execution hook.

## Install And Verify

The repository is distributed through the Vercel `skills` CLI. The default installation is **project-scoped**, so installing in one repository does not make it available in every other repository.

For Codex **in all projects**:

```bash
npx skills add TheBaiter/agent-context-foundation -g -a codex
npx skills ls -g -a codex
```

For Codex **only in the current project**, run these from that project directory:

```bash
npx skills add TheBaiter/agent-context-foundation -a codex
npx skills ls -a codex
```

Use your target agent's identifier instead of `codex` for other supported clients. After repository updates, check the installed version and update when needed:

```bash
npx skills check
npx skills update agent-context-foundation -g   # global installation
npx skills update agent-context-foundation -p   # project installation
```

Inspect the installed skill list in a **new agent session** and verify that `agent-context-foundation` is exposed to that agent. A skill present on GitHub but absent from the session's discovery list cannot be implicitly selected.

### Persistent Codex instructions: the missing reliability layer

`SKILL.md` is **selected**, not loaded unconditionally. If the goal is consistent error reporting and verification in day-to-day coding, combine skill installation with Codex's **automatically read** `AGENTS.md` instructions.

- For all Codex repositories: merge the concise excerpt from [`references/templates/codex-customization.md`](references/templates/codex-customization.md) into your existing `~/.codex/AGENTS.md` (or `$CODEX_HOME/AGENTS.md`).
- For one repository only: merge it into that repository's existing root `AGENTS.md`.
- Preserve more-specific repository rules and any `AGENTS.override.md`; never overwrite an existing instruction file blindly.
- The excerpt includes a minimal issue/failure/verification baseline **even when the skill is not selected**. More detailed guidance remains in the skill.

Use a **new Codex session** to verify the instruction sources were loaded and that a natural bugfix prompt both consults the relevant skill and produces an authoritative task record. Do not equate a skill being installed with an agent having used it.

There is a third possible failure: the installed version may be outdated, disabled, or not linked to Codex. Confirm the local `SKILL.md` contents and the agent's actual skill list after updating. For a reliable reinstall, use `npx skills add TheBaiter/agent-context-foundation -g -a codex` in the intended scope and inspect the installed files; command success alone is not proof that the active session is using the new instructions.

Canonical skill name: `$agent-context-foundation`.

Direct manual invocation remains supported:

```text
Use $agent-context-foundation to audit this repository's agent context.
```

## Trigger Regression Cases

Test **both** selection and behavior: a fresh agent must actually load the skill when expected, reuse/create an authoritative issue for a meaningful discovered defect, preserve material failure evidence, perform fresh regression checks, and leave the issue open if blocked. Include naturally phrased user requests that do **not** mention issue tracking or the skill.

`evals/activation-cases.csv` covers implicit positive cases, explicit invocation, and negative controls. Test these in a fresh agent session with the skill installed, using an expendable repository/fixture and verifying whether the agent **actually reads `SKILL.md`**. Merely following similar advice does not prove the skill was activated.

Static inspection verifies the metadata and regression fixtures but cannot measure real model selection. Record misses/false positives against the cases, then adjust the description rather than adding broad mandatory instructions.

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
- meaningful discovered problems traced from discovery through validated closure.

The skill should become easier to extend by adding a module without making `SKILL.md` grow into a manual again.
