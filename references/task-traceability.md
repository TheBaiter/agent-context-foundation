# Task Traceability

Read when defining or auditing how meaningful work is planned, tracked, resumed, or handed off.

This file owns execution-trace rules. It does not own durable project knowledge.

## Principle

Every meaningful task should leave enough durable trace for another person or agent to understand:

- what was attempted,
- accepted scope and success criteria,
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

If no system exists and the work is meaningful, create the smallest durable task record that fits project conventions.

## When Required

Use a durable task record for work that is multi-step, risky, architectural, migratory, investigative, likely to span phases, likely to require handoff, or likely to involve meaningful decisions.

When investigation or implementation discovers a concrete bug, regression, defect, or implementation problem that merits a meaningful change, create or reuse its authoritative task record before implementing the repair when the project has a tracker.

For trivial local edits, keep traceability proportionate and reuse existing task or commit context when sufficient.

## Discovered Problem Workflow

A discovered problem should normally have one authoritative issue/task that follows the problem from discovery through closure.

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

## Staged Investigation And Repair

For non-trivial problems, do not collapse the entire lifecycle into one reasoning pass.

Use distinct checkpoints with one concrete objective at a time:

1. **Confirm** — reproduce or otherwise confirm the problem and capture evidence.
2. **Diagnose** — identify the cause or narrow the cause hypothesis, affected owners, and boundaries.
3. **Plan** — define the smallest coherent repair, success criteria, regression risks, and verification route.
4. **Scope review** — challenge whether the plan is too broad, too narrow, speculative, or missing adjacent impact.
5. **Implement** — apply the repair against the recorded plan and note material deviations.
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
- relevant regressions have been considered,
- material deviations from the plan are documented,
- remaining risk and follow-up are recorded,
- the implementation anchor such as commit, PR, or deployed change is linked when practical.

If one of those conditions is not met, keep the record open and state the blocker or next action.

## Before Substantial Work

Record:

- goal,
- status,
- scope,
- success criteria,
- initial plan,
- known constraints or assumptions.

For a discovered problem, also record how it was found and the evidence that makes it real enough to act on.

Do not reconstruct this only after implementation.

## Update Checkpoints

Update the task record when one of these materially changes:

- scope,
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

Record a failed approach only when it:

- changes the next step,
- exposes a constraint,
- explains the current implementation,
- is likely to be repeated,
- leaves cleanup,
- or is the current blocker.

Capture attempt, result, cause if known, learning, and next action.

Recurring verified failures may later be promoted to error memory.

## Planning Boundary

A per-task plan belongs in the task record and should evolve with execution.

Durable `Agent/planning/` guidance describes reusable project planning conventions, not the current task plan.

## Git Boundary

Link branches, commits, PRs, or reviews to the task record when practical.

Follow the repository's own Git/review/merge policy.

The foundation must not invent universal draft, merge, or task-switch rules.

Issue-first traceability does not imply GitHub specifically; use the repository's authoritative tracker.

## Memory Boundary

Task trace answers: "What happened in this task?"

Durable memory answers: "What should future agents continue to know?"

At close:

1. review what was learned,
2. identify verified reusable conclusions,
3. promote only those conclusions to canonical durable owners,
4. keep chronology and temporary attempts in the task record.

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

For a discovered problem, also confirm that the record contains discovery evidence, diagnosis/boundaries, repair plan, scope review, and a separate revalidation result.

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
