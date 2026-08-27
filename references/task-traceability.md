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

For trivial local edits, keep traceability proportionate and reuse existing task or commit context when sufficient.

## Before Substantial Work

Record:

- goal,
- status,
- scope,
- success criteria,
- initial plan,
- known constraints or assumptions.

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

## Compact Fallback Template

Use the project's own template first. If none exists:

```md
## Goal
...

## Status
Planned | In progress | Blocked | Ready for review | Complete

## Scope / success criteria
- ...

## Plan
- [ ] ...

## Decisions
- Decision:
- Reason:
- Evidence:
- Consequence:

## Changes / verification
- ...

## Blockers / failures
- ...

## Handoff
- Current point:
- Remaining:
- Next action:
- Risk:
```

Delete unused sections instead of preserving empty ceremony.
