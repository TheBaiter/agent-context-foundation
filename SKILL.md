---
name: agent-context-foundation
description: Create, repair, compact, or audit repository agent context using minimum viable context, progressive disclosure, canonical ownership, evidence-based modules, durable task traceability, and verified memory. Use when agent instructions are missing, oversized, duplicated, stale, hard to route, or repeatedly cause rediscovery or mistakes.
---

# Agent Context Foundation

## Purpose

Make repository context cheaper to load, easier to route, safer to maintain, and easier to resume.

This skill is a decision engine. It should not become the repository's universal operating manual.

## Operational Application

When this skill applies, treat its applicable rules as actions to perform, not background information to mention.

- Apply every relevant rule by default when the agent has authority to do so.
- Do not downgrade an applicable rule into a recommendation, suggestion, consideration, or future improvement.
- Do not merely tell the user that a rule should be followed when the agent can follow it directly.
- A module being optional means its activation is conditional. Once evidence activates that module, its applicable rules are operational.
- Apply only the relevant subset of the skill. Do not load or execute unrelated modules.
- Use recommendations only for genuinely optional improvements or when a real decision boundary belongs to the user or project.
- Ask for approval only when required by authority, project policy, destructive impact, credentials, unclear scope, or another real decision boundary.
- If a required action cannot be performed, record the blocker and the exact next action instead of presenting the rule as if it were satisfied.
- Final reporting should state what was applied, skipped, blocked, or intentionally not applicable; it should not restate the skill as advice.

## Core Invariants

- Preserve a valid existing instruction standard such as root or nested `AGENTS.md`; do not create a competing authority.
- Load only context relevant to the current task.
- Execute applicable skill rules directly when authorized; do not treat them as passive recommendations.
- Give each durable rule, fact, contract, decision, or procedure one canonical owner.
- Prefer pointers to owners over duplicated prose.
- Create documentation or modules only when evidence shows they reduce future risk, confusion, or rediscovery.
- Keep global rules global and local rules close to the subtree they govern.
- Separate durable guidance, current state, task history, observations, and recurring error knowledge.
- Promote knowledge only after evidence: `discovered -> candidate -> verified -> durable`.
- Consolidate, challenge, supersede, retire, or remove stale memory instead of only appending.
- Preserve high-value anchors such as owner paths, symbols, exact tests, commands, boundaries, and handoff points.
- Never store secrets, production credentials, tokens, or private customer data in reusable agent context.
- Preserve the repository's established language and encoding. Default to UTF-8 when no explicit portability constraint exists.
- Follow the repository's own Git, review, approval, credential, security, and deployment policies.
- Keep disposable QA, visual, debugging, and intermediate artifacts in one repository temporary workspace. Reuse the project's existing temporary root; otherwise use `.agent-temp/`.
- The correct result may be no documentation change.

Detailed context principles are owned by `references/foundation-principles.md`.

## Task Traceability

For meaningful work, use the project's authoritative issue, ticket, task, work item, plan, or equivalent record.

Before substantial edits, record the goal, scope, success criteria, status, initial plan, and known constraints.

Update the record when scope, important decisions, evidence, failures, blockers, verification, or handoff changes.

Task history stays in the task record. Promote only verified reusable conclusions into durable agent context.

For trivial local work, keep traceability proportionate and reuse existing task or commit context when sufficient.

Detailed traceability rules are owned by `references/task-traceability.md`.

## Workflow

1. Locate or create the authoritative task record when the work is meaningful.
2. Inspect the active agent instruction entrypoint, local scoped instructions, source structure, and existing project tracking conventions.
3. Classify the task and load only the context required to make the next correct decision.
4. Identify canonical owners, affected surfaces, constraints, risks, and exact verification routes.
5. Audit for oversized default reads, duplication, ambiguous ownership, contradictions, stale guidance, or missing high-value anchors.
6. Decide the minimum useful action: no change, compact, repair routing, migrate, or add one evidence-backed module.
7. Load only the module reference required for that action.
8. Load only the specific template required for output generation.
9. Apply the smallest coherent change while preserving existing project conventions. Execute applicable rules directly rather than restating them as recommendations.
10. Update the task record during meaningful execution checkpoints.
11. Validate routing, ownership, staleness, secrets, language/encoding preservation, and exact verification guidance.
12. Before finishing or pausing, update the task record with current status, verification, remaining risk, and next action.
13. Promote durable knowledge only when it is verified and reusable.

## Module Router

Read a module only when its condition is true.

| Need | Read |
| --- | --- |
| Create or repair the base instruction route | `references/modules/foundation.md` |
| Repository orientation is repeatedly expensive | `references/modules/project-map.md` |
| Verified recurring failure knowledge exists | `references/modules/error-memory.md` |
| A repeated fragile procedure should become a tool | `references/modules/tools.md` |
| A complex cross-cutting area is repeatedly reconstructed | `references/modules/summaries.md` |
| Durable project-specific planning conventions exist | `references/modules/planning.md` |
| Non-obvious project-wide operating constraints exist | `references/modules/project-rules.md` |
| Specialized recurring verification or closeout is needed | `references/modules/checklists.md` |
| Existing agent docs or memory need migration/compaction | `references/modules/migration.md` |
| The user wants reusable Codex personalization | `references/modules/codex-customization.md` |
| Disposable QA/visual/debug artifacts are generated | `references/modules/temporary-workspace.md` |

Do not read every module to decide whether it is needed. The workflow and repository evidence decide first.

## Template Router

Templates contain output skeletons, not policy ownership.

Load only the template needed for the file being generated.

| Output | Template |
| --- | --- |
| `Agent/README.md` | `references/templates/base-readme.md` |
| `Agent/INDEX.md` | `references/templates/base-index.md` |
| project map | `references/templates/project-map.md` |
| error-memory README | `references/templates/error-memory-readme.md` |
| error-memory index | `references/templates/error-memory-index.md` |
| error case | `references/templates/error-case.md` |
| durable planning conventions | `references/templates/planning.md` |
| project-wide rules | `references/templates/project-rules.md` |
| checklist index | `references/templates/checklists-index.md` |
| Codex customization | `references/templates/codex-customization.md` |

## Minimum Foundation

If the repository already has a valid agent instruction route, preserve it.

If a new routed `Agent/` foundation is actually needed, start with only:

```text
Agent/
  README.md
  INDEX.md
```

Everything else is optional and evidence-backed.

Do not create empty folders, hypothetical error categories, placeholder modules, or documentation merely because a template exists.

## Knowledge Placement

Use the smallest canonical owner:

- source code/configuration for implementation truth,
- active root/local agent instruction files for operating rules,
- project map for owner/entrypoint localization,
- project rules for project-wide constraints,
- planning docs for durable planning conventions,
- task system for current work history,
- error memory for verified reusable failures,
- local README for owner-local reusable knowledge,
- summaries for cross-cutting expensive rediscovery,
- tools for reusable deterministic procedures,
- the repository's single temporary workspace for disposable QA/visual/debug artifacts.

## First Run

When the skill is selected because agent context is missing or structurally weak, explain only:

- what existing instruction standard was found,
- what minimum change is proposed,
- what task-tracking system will hold execution trace,
- which user decision is genuinely required before proceeding.

Do not present a long catalog of optional modules.

Do not modify Git tracking, store credentials, or invent approval rules without project/user authority.

## Context Health Audit

When auditing the foundation, classify problems before adding docs:

- distraction: irrelevant default context,
- confusion: unclear routing or ownership,
- clash: contradictory active guidance,
- poisoning: stale guidance influencing work,
- lost critical context: compaction removed anchors needed to act or resume.

Fix the cause rather than adding another layer of documentation.

## Self-Audit

Before finishing a foundation change, verify:

- Is the default read smaller or more focused?
- Were applicable skill rules actually executed rather than merely recommended?
- Does each durable concept have one canonical owner?
- Are routers pointing instead of explaining?
- Is any optional module present without evidence?
- Are any old paths still referenced as active?
- Does a template contain policy that belongs to a module or project rule?
- Are task history and durable memory separated?
- Are error-memory cases verified rather than copied from investigation history?
- Are language and encoding inherited from the repository instead of globally forced?
- Are Git/review/merge rules project-specific instead of universal?
- Can another agent resume meaningful work from the task trace?
- Did the change preserve exact source and verification anchors that prevent rediscovery?
- Are temporary QA/visual/debug artifacts contained in the repository's single temporary workspace instead of scattered across the tree?
- Would creating no additional documentation now be the better result?

If any answer exposes a conflict, fix it before adding more context.

## Completion

Report:

- what was changed,
- what was intentionally not created,
- what canonical owners were established,
- what was verified,
- remaining risk or unverified areas,
- the task record or handoff point,
- whether any durable knowledge was promoted.
