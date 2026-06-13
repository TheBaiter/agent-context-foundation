# Agent Context Foundation

[![Skill](https://img.shields.io/badge/skill-agent--context--foundation-blue)](https://github.com/TheBaiter/agent-context-foundation)

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
- internal summaries for recurring pages, flows, components, scripts, and topics,
- project-specific planning guidance that captures the user's planning style,
- local README or summary guidance for complex components, scripts, flows, and folders,
- non-secret project operating rules,
- intent-based and topic-based closing checklists,
- copy-ready Codex customization text.

The goal is not to reduce quality. The goal is to preserve useful context while making agents read only what is relevant.

## When To Use This Skill

Use this skill when a repository needs a clear place for agent instructions and the existing guidance is missing, too large, duplicated, or hard to route.

It is a good fit when agents keep rereading the same broad docs, repeating the same mistakes, losing useful setup knowledge, or mixing project rules with raw logs and one-off notes. It is also useful when a repo needs a small `Agent/README.md`, a task router, indexed error memory, reusable tool notes, safe credential rules, or copy-ready Codex customization text.

It can also help when a project has complex components, scripts, workflows, integrations, or generated-file processes that future agents keep rediscovering from source. In those cases, the skill should recommend a short local `README.md`, an `Agent/summaries/` note, or an `Agent/tools/README.md` entry instead of forcing every future agent to reread the whole implementation.

It can also preserve planning preferences. If the user or project has a specific way to plan work, the skill can add `Agent/planning/README.md` so generic planning skills know the local style before producing broad plans.

Use it when the goal is to make future agents read less but act with more reliable context.

## When Not To Use This Skill

Do not use this skill for ordinary feature work, one-file edits, bug fixes that do not change agent guidance, product documentation for end users, or business requirements that are not meant for agents.

Do not use it to archive every failed attempt or every terminal log. Error memory should be grouped by recurring root cause and final fix, not stored as a raw history.

Do not use it to store secrets, production credentials, API keys, tokens, passwords, private customer data, or sensitive raw logs.

## First Install Behavior

If an agent installs or selects this skill by itself because a repository has missing or weak agent docs, it should first explain the foundation in plain language.

That explanation should cover:

- what the skill does,
- which files it may create or update,
- the golden rules future agents must follow,
- the normal operating rules future agents should follow,
- the no-secrets policy,
- the English and ASCII-only rule for generated `Agent/` docs,
- whether the generated `Agent/` folder should be committed to Git or added to `.gitignore`.

Generated `Agent/README.md` files should put "Golden Rules" immediately after the title, followed by compact "What This Does" and "Normal Rules" sections so users can understand and configure the foundation without reading every generated document.

Generated `Agent/README.md` files should also include a short "Foundation Identity" section naming `agent-context-foundation`, the canonical source `TheBaiter/agent-context-foundation`, and the purpose of the generated `Agent/` folder. This makes the folder self-identifying for other project users and future agents.

Generated Codex customization text should also start with the same golden rules.

The agent should not modify `.gitignore` for `Agent/` unless the user explicitly chooses local-only agent docs. If the user does not answer, `.gitignore` should remain unchanged and the final response should say the Git tracking decision is pending.

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
  closing-checklists.md
  project-rules.md
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
  planning/
    README.md
  summaries/
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
- Creating `Agent/summaries/README.md` for short reusable context on pages, flows, components, scripts, and recurring topics.
- Creating `Agent/planning/README.md` for project-specific planning preferences when the user's planning style or project planning gates need to be preserved.
- Recommending local README or summary files for complex source areas when they would reduce repeated rereading.
- Creating `Agent/project-rules.md` for non-secret operating constraints such as allowed environments, safe probes, and approval gates.
- Creating `Agent/closing-checklists.md` so agents close work with the matching intent-based or topic-based checklist and report verification clearly.
- Creating `Agent/recommended-codex-customization.md` for copy-ready Codex personalization.
- Adding safe rules for local, demo, QA, or test credentials with explicit user permission.

## What It Does Not Do

- It does not replace source-code inspection.
- It does not create user-facing product documentation.
- It does not store production secrets, tokens, API keys, passwords, or customer data.
- It does not turn error memory into a generic log archive.
- It does not force agents to read all generated documents.
- It does not solve every repo process problem by adding more docs.
- It does not store production credentials, customer data, raw logs, or project-specific secrets in reusable templates.

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

Canonical skill name: `$agent-context-foundation`.
Canonical install source: `TheBaiter/agent-context-foundation`.

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
