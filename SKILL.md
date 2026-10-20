---
name: agent-context-foundation
description: Use proactively for multi-step repository bug fixes, substantial feature implementation, refactors, migrations, and reviews to discover project instructions, follow issue/task history, preserve traceability, and avoid repeat errors. Also create, repair, compact, or audit AGENTS.md and Agent/ guidance. Skip trivial isolated edits and general questions.
---

# Agent Context Foundation

## Purpose

Make repository context cheaper to load, easier to route, safer to maintain, and easier to resume.

This skill is a decision engine. It should not become the repository's universal operating manual.


## Activation Boundary

The skill may be selected **implicitly**, without the user naming it, when the actual repository task needs an instruction route, authoritative work trace, verified recurring-error knowledge, or maintenance of reusable agent context.

- Typical matches: a multi-step bug fix, risky refactor or migration, substantial feature with handoff, investigation requiring a task record, or repair of `AGENTS.md`/`Agent/` guidance.
- Non-matches: general programming explanations, brainstorming without repository access, cosmetic or trivial isolated edits, and unrelated tasks.
- Do not infer activation merely from the words "code", "repository", "test", or "agent". Apply the task-specific boundary above.
- On a coding task, **do the requested coding work**. Load only applicable context/traceability rules; do not turn every task into a full context-health audit or generate new documentation without evidence.
- Do not claim the skill automatically executes in every session: selection depends on the host exposing this skill and the agent matching the task to its metadata.


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
- For meaningful discovered bugs, regressions, defects, or implementation problems, create or reuse the project's authoritative issue/task before fixing them when a tracker is available; keep discovery, plan, implementation, verification, and closure evidence in that record.
- Keep active problem state, investigation chronology, temporary hypotheses, repair progress, and validation history in the authoritative issue/task instead of duplicating them into reusable repository context. When repository-local discoverability is useful, keep only a compact pointer to the authoritative record and remove it when it becomes stale.
- Keep non-trivial discovery, diagnosis, repair planning, implementation, and revalidation as distinct checkpoints. Prefer independent final validation when practical; otherwise perform a fresh validation pass separated from implementation.
- Keep disposable QA, visual, debugging, and intermediate artifacts in one repository temporary workspace. Reuse the project's existing temporary root; otherwise use `.agent-temp/`.
- The correct result may be no documentation change.

Detailed context principles are owned by `references/foundation-principles.md`.

## Task Traceability

For meaningful work, use the project's authoritative issue, ticket, task, work item, plan, or equivalent record.

Before substantial edits, record the goal, scope, success criteria, status, initial plan, and known constraints.

If investigation discovers a concrete problem that merits a meaningful change, create or reuse its authoritative task record before implementing the repair. Prefer one issue/task for the problem lifecycle rather than splitting discovery, diagnosis, fix, and validation across unrelated records.

Do not copy that active problem history into `AGENTS.md`, `Agent/` docs, planning files, summaries, error memory, or other reusable context merely to remember it. If agents need a repository-local signal that the problem exists, store only the smallest useful pointer to the authoritative task record.

Update the record when scope, important decisions, evidence, failures, blockers, verification, or handoff changes.

Do not close a discovered-problem record merely because code was written. Close it only after the intended change is applied, required verification succeeds, and remaining risk or follow-up is recorded.

Task history stays in the task record. Promote only verified reusable conclusions into durable agent context.

For trivial local work, keep traceability proportionate and reuse existing task or commit context when sufficient.

Detailed traceability rules are owned by `references/task-traceability.md`.

## Workflow Selection

Choose the route according to the **work actually requested**. An engineering task is not automatically a context-health audit.

### A. Engineering work: fix, implement, refactor, migrate, or review

1. Follow the active repository instructions, including any applicable `AGENTS.md` and project `Agent/README.md` route. Locate the authoritative tracker, source owners, and exact verification commands.
2. For meaningful work, find/reuse the existing issue or task record; record the goal, scope, success criteria, relevant constraints, and initial plan. When discovering a concrete defect that warrants a meaningful repair, create or reuse its record **before** implementation if a tracker is available.
3. For a non-trivial defect, keep **confirmation -> diagnosis -> plan and scope review -> implementation -> fresh revalidation -> closure or handoff** as distinguishable checkpoints in that one task record. Read `references/task-traceability.md` for their operational contract.
4. Perform the requested code/review work, applying only the relevant project constraints. Record material decisions, failures, scope changes, and evidence in the task record as they occur, not reconstructed from memory afterward.
5. Recheck the original failure and likely regressions, use the relevant tests/checks, and inspect the resulting diff. Independent validation is preferred when practical; otherwise conduct a distinct fresh review pass.
6. Update the authoritative task with the actual result, tests run or skipped, remaining risk, commit/PR anchor, and next action. Close only after its verification/closure gate passes; otherwise leave it open with an explicit handoff.
7. Promote a **verified reusable lesson** to error memory or other canonical durable context only when it will help future work. Do not copy the issue's active chronology into `Agent/`.

**Error classification:** A reproducible product bug, regression, defect, or meaningful implementation mistake belongs in the authoritative task/issue lifecycle. A failed command, denied permission, transient tooling error, or unsuccessful attempt belongs in that task's trace **when it materially affects the decision, next action, or verification**, not in a separate issue by default. Only verified, reusable lessons belong in durable `Agent/error-memory/`. Do not equate "document errors" with appending every console error to a growing memory file.

If the tracker is inaccessible, preserve the available evidence in the smallest project-authorized handoff and report the blocker. Do not claim an issue was created. For tiny isolated edits, keep the process proportionate and do not manufacture an issue.

### B. Agent-context foundation work: create, repair, compact, or audit instructions

1. Inspect active root/local agent instructions, existing `Agent/` routes, source structure, and the project's tracking system.
2. Identify canonical owners and classify problems as irrelevant default reads, duplication, contradictory ownership, stale memory, or missing high-value anchors.
3. Decide the smallest evidence-backed action: no change, compact, repair routing, migrate, or add one justified module.
4. Load only the applicable module from the router below and a template only when generating a file.
5. Apply the change, preserving project conventions, language, verification anchors, and task-trace ownership.
6. Validate the final instruction route and verify that no contradictory active paths or duplicated task chronology remain. Update the authoritative task record and any verified durable knowledge; leave an explicit handoff if incomplete.

When a task genuinely combines both routes, perform the requested engineering work first; adjust the foundation only for a demonstrated reusable gap. Do not run a full context audit by default.

## Module Router

Read a module only when its condition is true.

| Need | Read |
| --- | --- |
| Meaningful issue/task trace, discovered defects, or final revalidation | `references/task-traceability.md` |
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
- task system for current work history and active problem state,
- error memory for verified reusable failures after the active issue lifecycle,
- local README for owner-local reusable knowledge,
- summaries for cross-cutting expensive rediscovery,
- tools for reusable deterministic procedures,
- the repository's single temporary workspace for disposable QA/visual/debug artifacts.

A repository-local active-problem entry, when justified, should be a routing pointer to the authoritative task rather than a second copy of its investigation or status.

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
- Do meaningful discovered problems have an authoritative task record before repair, without duplicate issue creation?
- Is active problem history kept out of reusable repository context, with only a compact task pointer when local routing actually needs one?
- Are stale active-problem pointers removed after resolution unless they still have durable routing value?
- Were non-trivial discovery, diagnosis, planning, implementation, and revalidation kept as distinct checkpoints instead of one monolithic pass?
- Was final validation independent when practical, or at least performed as a fresh pass separated from implementation?
- Are discovered-problem records closed only after implementation and required verification are complete?
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
