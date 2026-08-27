# Base Agent README Template

Use only when the repository needs an `Agent/README.md`.

```md
# Agent Context

## Core Rules

- Use `INDEX.md` to load only context relevant to the current task.
- Apply relevant agent rules directly when authorized. Do not reduce applicable rules to recommendations or suggestions.
- Do not read the entire agent documentation tree by default.
- Prefer canonical owners and pointers over duplicated guidance.
- Preserve the repository's language and encoding; use UTF-8 unless a project constraint requires otherwise.
- For meaningful work, use the project's authoritative task system and keep its status, decisions, verification, blockers, and handoff current.
- Promote only verified reusable knowledge into durable agent docs.
- Never store secrets or private data in reusable agent documentation.
- Put disposable screenshots, QA captures, logs, scratch files, and intermediate artifacts in the repository's single temporary workspace. Reuse the existing one; otherwise use `.agent-temp/`.

## Routing

Read `INDEX.md` and select the smallest relevant route.

## Local Scope

Follow more specific repository instructions when a subtree has its own applicable guidance.
```
