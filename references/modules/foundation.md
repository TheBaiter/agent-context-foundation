# Foundation Module

Read when creating, repairing, or compacting a repository's agent instruction foundation.

## Decision

Preserve the repository's established instruction standard when it is valid. Root or nested `AGENTS.md`, local instruction files, or another existing convention may already be the correct authority.

Create a new `Agent/` route only when the repository lacks a usable route or when routed supporting context will materially reduce future discovery cost.

## Minimum

When `Agent/` is needed, start with only:

```text
Agent/
  README.md
  INDEX.md
```

Use the templates in `references/templates/base-readme.md` and `references/templates/base-index.md`.

## Rules

- Root guidance contains only truly global behavior.
- Local rules live close to the subtree they govern.
- Routers point to canonical owners instead of repeating them.
- Do not create empty modules.
- Do not copy source-code facts that are cheap to rediscover.
- Preserve repository language and encoding. Default to UTF-8 when no explicit constraint exists.
- Follow the repository's own Git, review, approval, credential, and deployment policies.
- Task execution history belongs in the project task system, not in durable agent docs.

## Add A Module Only With Evidence

Add a module when repeated work shows a durable need:

- project map: owner or entrypoint discovery is expensive,
- error memory: a verified failure pattern is reusable,
- tools: a procedure is fragile or repeatedly performed,
- summaries: a complex area is repeatedly reconstructed,
- planning: the repository has durable planning conventions,
- project rules: non-obvious project-wide constraints exist,
- checklists: specialized verification or closeout is recurring,
- Codex customization: the user wants reusable personalization.

If no module is justified, stop with the minimum or make no documentation change.
