# Temporary Workspace Module

Read when the agent generates disposable QA, visual, debugging, inspection, export, or intermediate artifacts.

## Rule

Reuse the repository's existing temporary workspace when one is already established.

Otherwise use one repository-level folder:

```text
.agent-temp/
```

Do not create a hierarchy by task unless the repository already requires one.

## Put Here

Examples:

- screenshots and visual QA captures,
- temporary reports,
- debugging logs,
- scratch notes,
- inspection dumps,
- temporary exports,
- intermediate generated files.

Do not scatter these artifacts across the repository root or source folders.

## Boundary

The temporary workspace is disposable working state.

Do not store authoritative task planning or traceability there. Meaningful task history belongs in the project's issue, ticket, task, plan, or equivalent tracker.

If an artifact becomes durable, move it to its canonical project location before task completion.

When repository policy permits, ignore the temporary workspace as one unit instead of maintaining scattered ignore rules.
