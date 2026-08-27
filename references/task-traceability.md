# Task Traceability

Read this reference when creating or updating the operating rules for planning, issue tracking, task execution, handoff, or work history.

Do not treat this file as durable project memory for individual tasks. It defines how task history should be recorded in the project's coordination system.

## Purpose

Every meaningful task should leave enough durable execution trace for another person or agent to understand:

- what was being attempted,
- what scope was accepted,
- what decisions were made,
- why those decisions were made,
- what evidence was used,
- what changed,
- what was verified,
- what failed or became blocked,
- where the task stopped,
- what should happen next.

Traceability exists to make work inspectable and resumable.

It is not a substitute for source code, tests, durable project documentation, or error memory.

## Use The Existing Coordination System

Prefer the system the project already uses.

Examples:

- GitHub Issues,
- Jira,
- Linear,
- Azure DevOps work items,
- GitLab issues,
- an established planning file,
- an ADR-linked task,
- another project-owned task or ticket system.

Do not create a parallel tracking system when an existing one already owns task status.

When several systems exist, use the one the project identifies as authoritative for the task.

If the project has no task system and the work is meaningful enough to require handoff or multi-step execution, create the smallest durable plan or task record that fits the repository's existing conventions.

## When A Trace Is Required

Create or locate a durable task record before substantial implementation when the work is:

- multi-step,
- expected to span more than one meaningful phase,
- likely to require handoff,
- risky or destructive,
- architectural,
- a migration,
- a broad refactor,
- a bug investigation with uncertain root cause,
- changing contracts, auth, data, deployment, dependencies, or operational behavior,
- likely to involve several decisions,
- likely to be interrupted or resumed later.

For trivial, obvious, file-local changes, reuse an existing issue or commit context when available and keep the trace compact.

Do not turn a one-line safe edit into a heavy planning ceremony.

## Trace Before Implementation

The trace should exist early enough to influence the work.

At minimum, record before substantial edits:

- task goal,
- current status,
- scope,
- success criteria,
- initial plan or phases,
- known constraints,
- important assumptions.

Do not wait until the end and reconstruct the history from memory.

## Update During Work

Update the task record at meaningful checkpoints.

Required checkpoint types:

### Scope change

Record when the accepted scope expands, shrinks, or changes owner.

### Decision

Record a decision that changes implementation direction, architecture, risk, contract, or verification.

### New evidence

Record evidence that invalidates an assumption or materially changes the plan.

### Failure

Record a failed approach when the failure explains the current state, affects the next attempt, or may matter to handoff.

Do not record every command or every failed micro-attempt.

### Blocker

Record what is blocked, why it is blocked, what evidence confirms the blocker, and what would unblock it.

### Verification

Record what was run or inspected and what the result proves.

### Handoff or stop point

Record the exact current state and the next useful action before leaving meaningful work incomplete.

## Decision Trace

For meaningful decisions, capture:

- decision,
- reason,
- evidence or source anchor,
- alternatives considered when relevant,
- consequences or tradeoffs,
- whether the decision is temporary or durable.

Keep decision records concise.

If a decision becomes stable project knowledge, promote the durable conclusion to the canonical project document or ADR and leave the task record pointing to it.

Do not copy the entire durable rule back into the task history.

## Evidence And Anchors

Prefer precise anchors over long pasted context.

Useful anchors include:

- file paths,
- symbols,
- line or section references when stable enough,
- issue or PR links,
- commit SHAs,
- test names,
- exact commands,
- schema or migration identifiers,
- external contract/version identifiers.

Do not paste large raw logs into the task record unless the raw text is necessary evidence.

Summarize the failure and link or attach the detailed artifact when possible.

## Failures And Dead Ends

Traceability should make failure understandable without becoming an archive of noise.

Record a failed approach when at least one is true:

- it explains why the current implementation looks different,
- another agent is likely to repeat it,
- it exposed an important constraint,
- it changed the plan,
- it left partial work that must be cleaned up,
- it is the current blocker.

For each important failure, record:

- attempted approach,
- observed result,
- likely or verified cause,
- what was learned,
- whether it should be retried,
- next action.

Recurring verified failure patterns belong in error memory after the task, not only in the task record.

## Relationship To Planning

A plan is part of the trace, not a separate disposable artifact.

The plan should reflect the current execution state.

Update it when:

- a phase is completed,
- a phase is abandoned,
- the order changes,
- new work is discovered,
- verification changes the next step.

Do not leave an obsolete original plan looking active after execution diverges from it.

## Relationship To Git

When Git is used, connect the work record to the code history when practical.

Useful links include:

- branch name,
- commits,
- pull request,
- review outcome.

A commit message alone is usually not enough trace for a complex task because it does not preserve planning, rejected alternatives, blockers, or handoff state.

A pull request alone is also not enough when important investigation or decisions happened before the PR was opened.

Follow the project's own branch, review, and merge policy. The foundation should not invent a universal Git workflow.

## Relationship To Durable Memory

Task trace answers:

"What happened during this task?"

Durable memory answers:

"What should future agents know regardless of this task?"

Do not promote task activity automatically.

At task close:

1. review what was learned,
2. identify reusable verified knowledge,
3. update the canonical owner only if the knowledge is durable,
4. update error memory only for recurring verified failures,
5. leave transient attempts and task chronology in the task record.

## Handoff Quality

Before stopping incomplete meaningful work, the trace must make the next action obvious.

Include:

- current status,
- completed phases,
- incomplete phase,
- files or owners currently involved,
- unresolved question or blocker,
- latest verification result,
- known risk,
- next recommended action.

Another agent should not need to reconstruct the previous session merely to understand where to continue.

## Completion

Before marking a task complete, record:

- final outcome,
- key decisions,
- changed surfaces,
- verification performed,
- intentionally skipped verification,
- remaining risk or follow-up,
- links to commits/PRs when applicable,
- durable docs or error memory updated as a result.

If no reusable knowledge changed, say so instead of creating unnecessary memory.

## Compact Task Record Template

Use or adapt the project's own template first. If none exists, the following structure is sufficient:

```md
## Goal

<What must be achieved and why?>

## Status

Planned | In progress | Blocked | Ready for review | Complete

## Scope

- In:
- Out:

## Success criteria

- [ ] ...
- [ ] ...

## Plan

- [ ] Phase 1: ...
- [ ] Phase 2: ...
- [ ] Verification: ...

## Decisions

### <decision>

- Reason:
- Evidence:
- Consequence:
- Status: temporary | durable candidate

## Evidence / anchors

- `path/to/file` - why it matters
- `command` - what it verifies
- issue/PR/commit - relation to the task

## Changes

- ...

## Verification

- Command/check:
- Result:
- What it proves:
- Not verified:

## Failures / blockers

- Attempt:
- Result:
- Cause:
- Learning:
- Next action:

## Current handoff

- Current point:
- Remaining work:
- Next action:
- Risk:
```

Delete empty sections rather than keeping boilerplate that adds no value.

## Traceability Health Check

A task record is healthy when:

- its current status is accurate,
- its plan matches the actual path,
- meaningful decisions have reasons,
- evidence is linked rather than vaguely described,
- failures that affect continuation are recorded,
- verification is explicit,
- the next action is visible,
- durable knowledge is promoted to the right owner,
- task history is not duplicated into permanent context.

A task record is unhealthy when another agent must infer where the work stopped from commits, chat history, or partial source changes alone.
