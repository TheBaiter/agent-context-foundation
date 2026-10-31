# Task Traceability

Read for confirmed agent mistakes, genuine task handoffs, or meaningful tracking policy. Do not load this reference for every ordinary code edit.

This file owns execution-trace rules. It does not own durable project knowledge.

## Principle

Every meaningful task should leave enough durable trace for another person or agent to understand:

- what was attempted,
- accepted scope and success criteria (including positive and negative capability boundaries),
- current plan,
- important decisions and reasons,
- relevant evidence,
- what changed,
- what was verified,
- failures or blockers that affect continuation,
- where the task stopped,
- next action.

Traceability makes work inspectable and resumable.

## Use The Existing System

Prefer the project's authoritative:

- GitHub Issue,
- Jira/Linear/Azure/GitLab work item,
- planning/task file,
- ADR-linked task,
- equivalent tracker.

Do not create a parallel tracking system when one already owns task state.

If an error needs tracking but no issue system exists, use the smallest durable task record allowed by project conventions; do not invent a new service.

## When Required

Do not require a new issue or a search through existing issues merely because work is multi-step. Reuse a task/issue when supplied by the user, required by project process, or needed to resume a substantial tracked effort.

When the **agent makes a confirmed meaningful error** (wrong implementation, regression, invalid assumption with product impact, or avoidable procedural mistake), create a focused issue in the existing tracker unless one already owns that same error. Document the error and correction through verified closure. Concrete defects discovered while working should likewise use the project's issue convention; avoid tickets for harmless transient retries or unrelated hypotheticals.

For trivial local edits, rely on the change and concise completion notes; no ceremony.

## Discovered Problem Workflow

A confirmed meaningful agent-caused problem should have one authoritative issue/task from discovery through validated closure, but need not force a history search when the issue identifier is already known.

Reuse an existing record when it already owns the same problem. Do not create duplicate issues just to satisfy process.

The record should preserve, either in the initial body or through staged updates/comments:

- problem statement,
- how and where the problem was discovered,
- evidence that confirms the problem,
- affected surface and known boundaries,
- scope and success criteria,
- diagnosis or current cause hypothesis,
- repair plan,
- review of whether the proposed repair is the smallest coherent fix,
- implementation progress and important deviations from plan,
- verification and regression evidence,
- final outcome and relevant commit/PR/change identifier,
- remaining risk, follow-up, or explicitly none.

Prefer one issue/task with progressive updates over separate records for discovery, diagnosis, implementation, and validation unless those stages become genuinely independent scopes.

Do not wait until after the code change to reconstruct why the issue existed.

## Active Problem Context Boundary

The authoritative issue/task owns the active problem state and its execution history.

Do not copy unresolved bugs, regressions, defects, investigation chronology, temporary hypotheses, failed approaches, repair progress, changing status, or validation history into reusable repository context merely so future agents know the problem exists.

This applies to agent instruction files, `Agent/` documentation, planning files, project summaries, project rules, local READMEs, error memory, and similar durable context unless the content has independently become verified reusable knowledge.

Keeping the active history in the task system avoids:

- duplicated ownership,
- larger default context,
- stale status copied into files,
- conflicting versions of the same investigation,
- repeated context cost for transient information.

If repository-local discoverability is genuinely useful, keep only the smallest routing pointer needed to reach the authoritative record. A useful pointer normally contains no more than:

- issue/task identifier or direct route,
- a short neutral problem label,
- an owner/surface only when needed for routing.

Do not mirror the issue body, diagnosis, plan, progress log, or validation history next to the pointer.

After validated resolution, keep a **single-line pointer** to an agent-caused confirmed error in the canonical `Agent/error-memory/INDEX.md` (or existing equivalent) while it helps avoid repeating the mistake: issue ID, brief symptom/cause and prevention. The detailed resolution remains in the closed issue. Remove obsolete pointers and merge duplicates rather than appending indefinitely.

A full standalone error-memory case is optional; promote it only for verified reusable lessons. The one-line index pointer is not a second issue log and must not contain status histories or long narratives.

## Staged Investigation And Repair

For non-trivial problems, do not collapse the entire lifecycle into one reasoning pass.

Use distinct checkpoints with one concrete objective at a time:

1. **Confirm** — reproduce or otherwise confirm the problem and capture evidence.
2. **Diagnose** — identify the cause or narrow the cause hypothesis, affected owners, and boundaries.
3. **Plan** — define the smallest coherent repair, success criteria, regression risks, and verification route.
4. **Scope review** — challenge whether the plan is too broad, too narrow, speculative, or missing adjacent impact.
5. **Implement** — apply the repair against the recorded boundary and plan, including UI and API/integration consequences, and note material deviations.
6. **Revalidate** — perform a fresh verification pass against the original problem, success criteria, and likely regressions.
7. **Close or hand off** — close only when implementation and required verification are complete; otherwise leave the record open with the exact next action.

These checkpoints may happen in one working session and in one issue, but they should remain distinguishable in the trace.

Do not treat a single monolithic analysis followed immediately by self-approval as equivalent to staged review for a non-trivial problem.

## Independent Revalidation

Prefer final validation by a different agent, reviewer, role, or person when one is available and the cost is reasonable.

The validator should assess the implemented result against the issue's problem statement, scope, success criteria, evidence, and regression risks rather than merely agreeing with the implementation narrative.

When independent validation is unavailable, the implementing agent must perform a fresh validation pass separated from implementation. Re-read the issue criteria, inspect the resulting change as a reviewer would, rerun the relevant verification, and actively look for false closure, missing scope, regressions, or unsupported assumptions.

Record who or what performed the revalidation and the evidence used.

## Closure Gate

Writing code is not completion.

Do not close a discovered-problem issue/task until:

- the intended repair is actually applied,
- required tests/checks/verification have succeeded or any skipped verification is explicitly justified,
- the original failure or defect is rechecked where practical,
- relevant regressions have been considered, including whether permitted capabilities remain available and restricted effects remain blocked in each affected mode,
- material deviations from the plan are documented,
- remaining risk and follow-up are recorded,
- the implementation anchor such as commit, PR, or deployed change is linked when practical.

If one of those conditions is not met, keep the record open and state the blocker or next action.

## Before Substantial Work

Begin with the user's current instruction, available context and the minimum relevant source. **Do not read issues by default.** Fetch only an explicitly named issue, one that owns a confirmed error, or a specific decision needed to resolve a conflict. Load `references/task-boundaries.md` only if permissions/integrations truly complicate the boundary.

Record:

- goal,
- status,
- scope,
- success criteria,
- initial plan,
- known constraints or assumptions,
- affected actors/modes and allowed, denied, preserved, deferred capabilities,
- boundary owners (UI, API/server, integration, storage, import/export) and dependency issues,
- evidence for decisions or explicit gaps still under investigation.

For a discovered problem, also record how it was found and the evidence that makes it real enough to act on.

Do not reconstruct this only after implementation.

## Update Checkpoints

Update the task record when one of these materially changes:

- scope or the current user/issue contract (including superseded restrictions),
- plan,
- implementation direction,
- evidence,
- important decision,
- blocker,
- failure affecting continuation,
- verification result,
- handoff state.

For discovered problems, update at the transition between confirmation, diagnosis, planning/scope review, implementation, and revalidation when the result of that phase changes what follows.

Do not log every command or micro-attempt.

## Decision Trace

For an important decision, preserve:

- decision,
- reason,
- evidence/anchor,
- consequence or tradeoff,
- whether it is temporary or a durable candidate.

If it becomes stable project knowledge, promote the conclusion to the canonical owner and leave the task record pointing to it.

## Evidence

Prefer precise anchors:

- file paths,
- symbols,
- test names,
- exact commands,
- commits/PRs,
- schemas/migrations,
- contract/version identifiers.

Summarize large logs instead of pasting them unless raw text is necessary evidence.

## Failures

Record agent mistakes in their dedicated existing/new issue when they have material impact; include symptom, cause (or unknown), fix, verification, prevention and commit. Routine tool retries do not each need their own issue.

Record a failed approach in an existing task only when it:

- changes the next step,
- exposes a constraint,
- explains the current implementation,
- is likely to be repeated,
- leaves cleanup,
- or is the current blocker.

Capture attempt, result, cause if known, learning, and next action.

Keep a one-line issue pointer in `Agent/error-memory/INDEX.md` for a confirmed agent-caused error after resolution while relevant. Promote a detailed failure case only if independently verified and reusable.

## Planning Boundary

A per-task plan belongs in the task record and should evolve with execution.

Durable `Agent/planning/` guidance describes reusable project planning conventions, not the current task plan.

## Git Boundary

Link branches, commits, PRs, or reviews to the task record when practical.

Follow the repository's own Git/review/merge policy.

The foundation must not invent universal draft, merge, or task-switch rules.

Issue-first traceability does not imply GitHub specifically; use the repository's authoritative tracker.

## Memory Boundary

Task trace answers: "What happened in this task, and what is its current state?"

Durable memory answers: "What should future agents continue to know after this task is no longer active?"

Do not use durable memory as a shadow issue tracker. While a problem is active, its chronology, hypotheses, plan, status, and verification belong in the authoritative task record. A repository-local pointer may route to that record, but must not duplicate it.

At validated closure:

1. Complete the issue's symptom/cause/repair/tests/commit and close it; leave unverified errors open with the next check.
2. Update one compact `Agent/error-memory/INDEX.md` pointer for a confirmed agent error, even after closure if still preventive.
3. Promote a longer reusable lesson only when verified and worth its context cost.
4. Retire stale pointers and keep chronology inside the issue.

## Handoff

Before pausing incomplete meaningful work, record:

- current status,
- completed and incomplete phase,
- active owners/files,
- unresolved blocker/question,
- latest verification,
- remaining risk,
- next useful action.

A new agent should not need chat history or commit archaeology merely to continue.

## Completion

Before marking complete, record:

- final outcome,
- key decisions,
- changed surfaces,
- verification,
- skipped verification,
- remaining risk/follow-up,
- relevant commits/PRs,
- durable knowledge promoted, or explicitly none.

For an agent-caused error, confirm the issue states what failed, why (if known), how it was fixed, what was actually tested, and the pointer in Agent error memory. Close only after necessary checks succeed.

## Compact Fallback Template

Use the project's own template first. If none exists:

```md
## Problem / goal
...

## Status
Planned | In progress | Blocked | Ready for validation | Complete

## Discovery / evidence
- Found while:
- Evidence:
- Affected surface:

## Scope / success criteria
- ...

## Diagnosis
- Cause / hypothesis:
- Boundaries:

## Plan / scope review
- [ ] ...
- Smallest coherent fix review:
- Regression risks:
- Verification route:

## Decisions
- Decision:
- Reason:
- Evidence:
- Consequence:

## Changes
- ...

## Revalidation
- Validator / fresh pass:
- Verification performed:
- Result:
- Regressions checked:

## Blockers / failures
- ...

## Handoff / closure
- Current point:
- Remaining:
- Next action:
- Risk / follow-up:
- Commit / PR:
```

Delete unused sections instead of preserving empty ceremony.
