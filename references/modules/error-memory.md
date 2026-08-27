# Error Memory Module

Read only when the task involves reusable failure knowledge or an existing error-memory route.

## Minimum Structure

```text
Agent/error-memory/
  README.md
  errors/
    INDEX.md
```

Do not pre-create categories such as PowerShell, Node, Git, database, API, frontend, deployment, or performance. Categories appear only after a real verified case exists.

Use:
- `references/templates/error-memory-readme.md`
- `references/templates/error-memory-index.md`
- `references/templates/error-case.md`

## Promotion Gate

Use:

`discovered -> candidate -> verified -> durable`

Keep attempts, hypotheses, and temporary findings in the task record. Promote a case only when the root cause and fix are verified and the lesson is reusable.

A single case may qualify when it is expensive, dangerous, non-obvious, or likely to recur.

## Case Lifecycle

Use status only when needed:

- active,
- challenged,
- superseded.

Do not keep contradictory cases active.

## Reading

Start from `errors/INDEX.md`. Load only the matching category or case. Never bulk-load error history.

## Writing

Store root cause, verified fix, applicability, prevention, and useful anchors. Do not store raw session history, secrets, large logs, or every failed attempt.
