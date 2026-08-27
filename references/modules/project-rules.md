# Project Rules Module

Read when non-obvious project-wide operating constraints affect the task.

Examples:

- allowed environments or tenants,
- destructive-action boundaries,
- safe query/probe limits,
- credential handling rules,
- repository-specific Git/review/merge policy,
- deployment constraints,
- exact local verification requirements,
- known risky areas.

Rules must be project-specific and evidence-backed.

Do not use this module to impose universal workflow preferences.

Never store secrets, production credentials, tokens, private customer data, or other sensitive values.

Use `references/templates/project-rules.md`.
