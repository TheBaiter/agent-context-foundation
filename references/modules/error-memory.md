# Error Memory Module

Read only to add/revisit a confirmed error pointer, or when a reusable failure requires more than the short index entry. Do not preload the index or cases for unrelated work.

## Minimum Structure

```text
Agent/error-memory/
  INDEX.md             # one-line issue pointers (small default)
  errors/              # only if a justified detailed case exists
    <verified-case>.md
```

Reuse the project's existing canonical error-memory route when present. Otherwise create only the small `Agent/error-memory/INDEX.md` after a confirmed meaningful agent error; detailed case files and categories remain optional. Do not pre-create empty structures.

Optional templates for justified detailed memory: `references/templates/error-memory-readme.md`, `references/templates/error-memory-index.md`, `references/templates/error-case.md`. A one-line pointer needs no template.

## Promotion Gate

Use:

`discovered -> candidate -> verified -> durable`

Keep attempts, hypotheses and temporary findings in the issue. As soon as a meaningful agent mistake is confirmed, including an oversight pointed out by the user, create/reuse its issue and a **short preventive pointer** (`#issue — symptom/cause — preventive rule`) without creating a long case; keep the issue open until the repair is actually verified. The pointer must never assert an unverified fix or contain the issue history. Promote a detailed case only when root cause/fix are verified and the lesson is reusable.

A single case may qualify when it is expensive, dangerous, non-obvious, or likely to recur.

## Case Lifecycle

Use status only when needed:

- active,
- challenged,
- superseded.

Do not keep contradictory cases active.

## Reading

Use the index as a tiny routing aid **only when a matching symptom/surface appears**. Read just the matching line; fetch that issue or case only when the one-line reminder cannot resolve the decision. Never bulk-load issue history.

## Writing

For a short pointer: issue ID/link + brief failure/cause + preventive rule in one line. Update rather than duplicate. For a detailed verified case: store root cause, verified fix, applicability and anchors; no raw session history, secrets, large logs or every failed attempt. Retire obsolete pointers.
