# Tools Module

Read when a repeated procedure is fragile, mechanical, or costly to perform manually.

Create an agent-owned script only when automation reduces repeated risk or effort.

## Rules

- Prefer deterministic scripts for bulk edits, migrations, encoding repair, generated-file work, or repeated validation.
- Keep reusable agent-owned scripts under the repository's chosen agent tools area, commonly `Agent/tools/scripts/`.
- Document the command, inputs, outputs, safety constraints, and verification.
- Do not create a tool for a one-off operation that is simpler and safer to perform directly.
- Do not embed secrets.
- Follow the repository's existing language, package, and tooling conventions.

A tool note should point to the script and explain when to use it; it should not copy the implementation.
