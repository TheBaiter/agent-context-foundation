# Agent Context Foundation

[![skills.sh](https://skills.sh/b/TheBaiter/agent-context-foundation)](https://skills.sh/TheBaiter/agent-context-foundation)

Agent Context Foundation is a Codex/agent skill for creating task-routed agent documentation in a repository.

Its purpose is to help agents work with less irrelevant context, fewer repeated mistakes, and better long-term memory without burning tokens on documents that do not apply to the current task.

## What It Solves

Many repositories accumulate large agent prompts, long operational manuals, and noisy error logs. Agents often load too much of that material, even for small tasks.

This skill helps create a cleaner structure:

- short entry documents,
- a central routing index,
- topic-specific core documents,
- specialized docs only when needed,
- indexed error memory,
- reusable tool/procedure notes,
- copy-ready Codex customization text.

The goal is not to reduce quality. The goal is to preserve useful context while making agents read only what is relevant.

## Main Idea

Agents should not read everything by default.

They should:

1. Read the repository root `README.md`.
2. Follow the LLM notice to `Agent/README.md`.
3. Use `Agent/INDEX.md` as the router.
4. Read only the docs that match the task.
5. Read error memory only when the task is related to a known or likely error category.
6. Update documentation and error memory only when reusable knowledge changed.

## What The Skill Creates

Default foundation:

```text
Agent/
  README.md
  INDEX.md
  Agent.md
  recommended-codex-customization.md
  skill-coverage-checklist.md
  core/
    README.md
    project-overview.md
    routing-auth-access.md
    business-domain.md
    data-model-and-data-layer.md
    ui-and-forms.md
    env-scripts-quality.md
    security-and-agent-roles.md
  error-memory/
    README.md
    migration-summary.md
    errors/
      INDEX.md
      TEMPLATE.md
      powershell-errors.md
      node-npm-errors.md
      git-errors.md
      database-errors.md
      api-errors.md
      frontend-errors.md
      deployment-errors.md
      performance-errors.md
  tools/
    README.md
```

The exact structure can be adapted to the repository, but the routing principle should stay the same.

## What It Covers

- Splitting large `AGENTS.md`, `Agent.md`, or similar files.
- Creating `Agent/README.md` as a minimal entry point.
- Creating `Agent/INDEX.md` as the main routing document.
- Creating `Agent/core/` for broad but task-specific guidance.
- Creating `Agent/error-memory/` as routed, searchable memory.
- Creating `Agent/tools/README.md` for reusable scripts and learned procedures.
- Creating `Agent/recommended-codex-customization.md` for copy-ready Codex personalization.
- Adding safe rules for local, demo, QA, or test credentials with explicit user permission.

## What It Does Not Do

- It does not replace source-code inspection.
- It does not create user-facing product documentation.
- It does not store production secrets, tokens, API keys, passwords, or customer data.
- It does not turn error memory into a generic log archive.
- It does not force agents to read all generated documents.
- It does not solve every repo process problem by adding more docs.

## Error Memory Philosophy

Error memory is treated as expensive context.

Agents should:

- read `error-memory/errors/INDEX.md` first,
- select only matching categories,
- search exact sections with `rg -n`,
- avoid unrelated error files,
- update memory only at the end of meaningful work,
- store root causes and fixes, not raw logs.

This prevents repeated failures without making every task pay for full historical context.

## Documentation Rules

Generated agent-facing documentation should be:

- English,
- ASCII-only,
- routed by task,
- concise,
- explicit about when to read and when not to read.

The ASCII rule is defensive. It keeps files portable across terminals, shells, operating systems, tools, and agents that may handle encoding differently.

## Usage

Install or reference this skill, then ask the agent to use it in a repository that needs an agent documentation foundation.

Install with:

```bash
npx skills add TheBaiter/agent-context-foundation
```

Example:

```text
Use $agent-context-foundation to create a compact Agent documentation foundation with routed core docs, error memory, and Codex customization text for this repo.
```

For a new repository with no agent docs, use the skill before inventing a custom structure.

## Repository Contents

```text
SKILL.md
agents/openai.yaml
references/agent-docs-structure.md
references/error-memory-structure.md
references/templates.md
```

`SKILL.md` is the skill entry point. The `references/` files are loaded only when needed.

## Validation

This skill has been validated with the Codex skill validator:

```text
quick_validate.py agent-context-foundation
```

The skill files are intended to stay ASCII-only.
