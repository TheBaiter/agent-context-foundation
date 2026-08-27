# Planning Module

Read only when the repository has durable planning conventions that differ from generic task planning.

## Boundary

Per-task plans and progress belong in the authoritative task record.

`Agent/planning/` is only for reusable project conventions such as:

- required phases,
- review gates,
- approval points defined by the project,
- expected plan granularity,
- project-specific validation sequencing,
- handoff conventions.

Do not store the current task plan here.

Do not invent approval or Git policies. Follow the project's existing process.

Use `references/templates/planning.md` only when durable planning conventions actually exist.
