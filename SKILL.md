---
name: agent-context-foundation
description: Keep coding-agent context focused, prevent task-boundary drift, and trace confirmed agent mistakes with minimal issue and error-memory pointers. Use for substantive repository changes, debugging, regressions or agent-context maintenance; load issues and detailed references only when evidence requires them.
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
- Before substantive implementation, establish the user's current goal and affected boundary from the current request, already available context, applicable local instructions and smallest relevant source; consult issues only on a specific trigger.
- Separate capability access, app authentication, external-provider authorization, execution safety, and data persistence; denying one does not silently deny the others.
- Recheck the accepted task boundary after user corrections, material discoveries, and before final validation; preserve allowed behavior in addition to enforcing restrictions.
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
- When the agent causes or discovers a confirmed meaningful error/regression, create or reuse one issue in the project's existing tracker, record cause/fix/verification, and close it once the repair is genuinely validated; do not invent an issue for every harmless retry.
- Keep investigation and repair history in the issue, not copied into agent files. Preserve a one-line problem/issue reference in the existing canonical Agent error-memory index (or create that small index when needed), including after validated closure when it helps prevent recurrence; open the issue only for matching cases.
- Keep non-trivial discovery, diagnosis, repair planning, implementation, and revalidation as distinct checkpoints. Prefer independent final validation when practical; otherwise perform a fresh validation pass separated from implementation.
- Keep disposable QA, visual, debugging, and intermediate artifacts in one repository temporary workspace. Reuse the project's existing temporary root; otherwise use `.agent-temp/`.
- The correct result may be no documentation change.

Detailed context principles are owned by `references/foundation-principles.md`.

## Context Budget And Task Boundary Gate

**Default: do the task, not an exhaustive context audit.** Use the current request and context already in the session. Read the relevant existing agent instruction entrypoint (`AGENTS.md`, `Agent/README.md` or actual equivalent) and the narrowest code/contract owner. Do **not** preload every issue, recent comment, linked issue, module, repository directory, or error history.

1. **Cheap boundary:** state the requested outcome; distinguish what stays allowed, forbidden, unchanged, or deferred. Check only the dimensions that matter (identity, authorization, external integration, read/write, persistence, feature flag). Never infer that lack of login or cloud saving forbids unrelated catalogs, offline editing, or explicitly authorized temporary connections.
2. **Issue-read triggers, not a default:** consult the *specific* issue only when the request names it; a matching short error-memory pointer is relevant; the change depends on an unresolved earlier decision/contract; available context conflicts; or a confirmed error needs to be recorded. If the current request plus source resolves the task, **read zero issues**. Follow linked dependencies only if they actually block a decision. Do not search/list all issues for orientation.
3. **Progressive escalation:** begin with the minimum relevant files. Expand to API/integration/security owners or `references/task-boundaries.md` only when the observed behavior or risk requires them. Stop gathering context when the desired boundary, code owner, and relevant verification are clear. A high-risk cross-mode change merits deeper checks; a local edit does not need a full matrix.
4. **Check the outcome:** validate permitted behavior (positive), restricted effects (negative), adjacent modes (regression) in proportion to the change. Revisit the user-requested boundary on material corrections or contradictions, not on every micro-step. Tests authored, passed, and unrun must be distinguished.

**If the agent makes a meaningful mistake:** use the correction-and-memory procedure below. Never replace a requested implementation with lengthy analysis of issues.

## Error Correction, Issue Lifecycle And Short Memory

When the agent introduces a defect, regression, wrong assumption, avoidable tool misuse, or incorrect restriction with material impact:

1. Confirm the symptom, check whether an issue already owns **that error**, then create one if needed; do not scan unrelated issues or make duplicates. If the user supplied an issue ID, use it directly.
2. Record **what failed**, **why** (or explicitly unknown), **what changed to fix it**, **how it was verified**, **regression risks**, and a commit/reference. Update only at meaningful checkpoints; keep the detailed history in the issue.
3. Repair and perform a fresh validation pass. **Close the issue when the repair and its required verification are actually complete**; if blocked or untested, leave it open with the exact missing check and next step. Do not claim a pass because a test was merely written.
4. In the existing `Agent/error-memory/INDEX.md` (or the project's canonical error-memory index), add or update **one concise line**: `#issue — symptom/cause — prevention or corrected rule`. Create only this small index if no route exists and the error warrants a durable reminder. Keep this reference after issue closure if it remains useful; remove it when obsolete. **Do not copy issue timelines, logs, or full diagnoses into Agent/**.
5. Read that line when the same area or symptom recurs; fetch the full issue **only** if the line and current source are insufficient. Promote a detailed reusable case through `references/modules/error-memory.md` only when justified.

For ordinary meaningful work, reuse a task record if one is already provided or project policy demands it; **do not open or read issues merely for ceremony**. See `references/task-traceability.md` for the error lifecycle and `references/task-boundaries.md` only for a complex boundary.

## Workflow Routing

- **Product/engineering task:** apply the cheap Context Budget/Boundary Gate; load detailed task trace or boundary references only for confirmed errors, non-trivial cross-mode risks or genuine handoffs. Implement and validate the product request, not an agent-documentation audit.
- **Agent-context maintenance task:** use the foundation workflow below and load only evidence-backed modules. Context maintenance is not the default outcome of an engineering task.
- **Trivial work:** use proportionate checks; no issue, matrix, or module merely for ceremony.

## Context-Maintenance Workflow

1. Establish the task from the current request and minimal relevant project context. Read/create an issue only on the triggers above; for confirmed agent errors, use the correction lifecycle.
2. Inspect the active agent instruction entrypoint, local scoped instructions, source structure, and existing project tracking conventions.
3. Classify the task and load only the context required to make the next correct decision.
4. Identify canonical owners, affected surfaces, constraints, risks, and exact verification routes.
5. Audit for oversized default reads, duplication, ambiguous ownership, contradictions, stale guidance, or missing high-value anchors.
6. For a non-trivial discovered problem, separate confirmation/evidence, diagnosis/boundaries, repair planning/scope review, implementation, and fresh revalidation into distinct checkpoints recorded in the same authoritative task.
7. Keep active error details in the issue; write one compact Agent error-memory index pointer for the confirmed failure, not a mirrored issue history.
8. Decide the minimum useful action: no change, compact, repair routing, migrate, or add one evidence-backed module.
9. Load only the module reference required for that action.
10. Load only the specific template required for output generation.
11. Apply the smallest coherent change while preserving existing project conventions. Execute applicable rules directly rather than restating them as recommendations.
12. Update the task record during meaningful execution checkpoints.
13. Validate routing, ownership, staleness, secrets, language/encoding preservation, and exact verification guidance.
14. Before finishing or pausing, update the task record with current status, verification, remaining risk, and next action.
15. Promote durable knowledge only when it is verified and reusable.
16. Close the confirmed-error issue after the fix and required revalidation, or leave it open with the missing checks. Keep a concise preventive error-memory pointer while relevant; retire obsolete entries.

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
