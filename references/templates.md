# Templates

Use these templates when creating a new foundation.

## Root README.md LLM Notice

Place this near the top of the repository root `README.md`:

```md
> This `README.md` is aimed at human developers.
> If you are an LLM, read `Agent/README.md` before acting in this repo and load only task-relevant documents listed there.
```

## Agent README.md

```md
# Agent Operational Entry

This folder contains task-routed operational memory for agents working in this repository.

## Minimal Reading Rule

Do not read the whole `Agent/` folder by default.

Default flow:

1. Read this file.
2. Read `INDEX.md`.
3. Select only the documents that match the current task.
4. Read source code before editing.
5. Update only the documentation that changed in meaning.

## Trivial Task Rule

For small known-file tasks, do not load broad project docs or error history.

Examples:

- add a temporary `console.log`,
- fix a typo,
- format one named file,
- answer a simple question,
- change one small line in a file the user already named.

Read only this entry, `INDEX.md`, and the target source file unless the change exposes a real domain, security, data, or error-memory risk.

## Task Checklist

Before implementation:

1. Classify the task as trivial, narrow, or domain-specific.
2. Identify the source files likely to change.
3. Use `INDEX.md` only if extra documentation is needed.
4. Decide whether error memory is relevant.
5. If error memory is not relevant, do not read it.

Before finishing:

1. Run the checks that match the change.
2. Update docs only if reusable guidance changed.
3. Update error memory only if a meaningful new error pattern was found.

## ASCII Rule

All new or updated documentation in `Agent/` should use English and ASCII-only text.

Avoid accents, emojis, smart quotes, em dashes, and special punctuation.

## Main Router

Use `INDEX.md` to decide what to read.
```

## Agent INDEX.md

```md
# Agent Documentation Index

Use this file as the router for `Agent/`.

Do not read every document. Pick the smallest relevant set for the task.

## Global Rules

- Keep context small.
- Read only documents that match the files or behavior being changed.
- Do not read broad docs for trivial known-file tasks.
- Do not read error memory unless the current task makes it relevant.
- Prefer source code over stale documentation when there is a conflict.
- Keep all new or updated documentation English and ASCII-only.
- If adding new guidance, update this index.

## Core Documents

| Task area | Read |
| --- | --- |
| Broad project orientation, repo layout, route map | `core/project-overview.md` |
| Routes, login, sessions, organizations, permissions | `core/routing-auth-access.md` |
| Business domain behavior | `core/business-domain.md` |
| Schema, migrations, RPC, repository layer | `core/data-model-and-data-layer.md` |
| UI, forms, tables, CRUD screens | `core/ui-and-forms.md` |
| Env vars, scripts, tests, build, verification | `core/env-scripts-quality.md` |
| Secrets, security, deploy, process rules | `core/security-and-agent-roles.md` |
| Manual setup of Codex instructions on another PC or agent profile | `recommended-codex-customization.md` |
| Local, demo, or QA test credentials approved by the user | `acceso-local.md` or `local-access.md` |
| Reusable scripts, local tools, encoding fixes, or learned procedures | `tools/README.md` |
| Coverage comparison between local Agent docs and the reusable skill | `skill-coverage-checklist.md` |

## Error Memory

Use `error-memory/` only when the task relates to a known or likely error category.

Start with `error-memory/errors/INDEX.md`.
Do not read all error files by default.
```

## Recommended Codex Customization

Write this as `Agent/recommended-codex-customization.md` with no wrapper text:

```md
Before any change in this repo:

1. Read `README.md`.
2. Read `Agent/README.md`.
3. Read `Agent/INDEX.md`.
4. From that index, read only the documents that apply to the concrete task.

Do not read the whole `Agent/` folder by default.
Do not read every file in `Agent/core/` by default.
Keep context small and route by task impact.

Documentation rules:

- All documentation added or updated inside `Agent/` for agent usage must be written in English and ASCII-only text.
- Avoid accents, emojis, smart quotes, em dashes, and special punctuation.
- If adding new guidance, update `Agent/INDEX.md`.
- If a document is task-specific, include when to read it and when not to read it.

New repository or missing agent docs:

- If the repo has no `Agent/README.md` or `Agent/INDEX.md`, do not overthink a custom structure from scratch.
- If `$agent-context-foundation` is installed, use it to create the agent documentation foundation.
- If it is not installed, use `$find-skills` or search for an agent context/documentation foundation skill before inventing a new layout.
- If no skill is available, create the smallest `Agent/README.md` and `Agent/INDEX.md` first, then add only task-relevant docs.

Tooling and encoding repairs:

- For mojibake, encoding repairs, bulk mechanical edits, repeated formatting, or fragile transformations, create a script/tool instead of doing manual one-off edits.
- Run the script, inspect the result, and fix the script until it works.
- Document reusable scripts, tools, and learned procedures in `Agent/tools/` or the most relevant routed document.
- If the tool prevents a meaningful recurring error, update `Agent/error-memory/` at the end of the task.

Error memory:

- Use `Agent/error-memory/`.
- Always start with `Agent/error-memory/errors/INDEX.md`.
- Do not read all error files by default.
- Search only the relevant category file with `rg -n`.
- Read the smallest useful section.
- Update error memory only at the end of meaningful work.
- Store root cause and final fix, not raw logs.
- Never store secrets, tokens, passwords, or credentials.

QA and test credentials:

- Ask the user before writing any credential value.
- Store only local, demo, QA, or test credentials that the user explicitly allows.
- Never store production credentials, customer credentials, API keys, service-role secrets, access tokens, or refresh tokens.
- If permission is unclear, document how to configure credentials instead of writing values.

Implementation rules:

- Read source code before editing.
- Use the owner folder for each domain.
- Do not create generic abstractions when an existing local pattern is enough.
- If a task touches routes, auth, data contracts, forms, entities, workflow, deployment, scripts, or verification, read the matching document from `Agent/INDEX.md`.
```

## Local Or QA Access Document

Use this only with explicit user permission for local, demo, QA, or test credentials.

```md
# Local Access

Use this file only for local, demo, QA, or test access approved by the user.

Do not store production credentials, customer credentials, API keys, service-role secrets, access tokens, or refresh tokens.

## Credentials

Environment:
<local/demo/qa/test>

Scope:
<what this account can access>

Username:
<username or env var name>

Password:
<password only if the user explicitly allowed storing it; otherwise use env var name>

Last verified:
YYYY-MM-DD

Reset notes:
<how to recreate or rotate this account>
```

## Agent Tools README.md

```md
# Agent Tools Index

Use this file for reusable tools, scripts, and learned procedures that help future agents avoid rereading large source areas.

Do not add one-off notes here. Add only reusable procedures.

## When to read

- a task mentions mojibake, encoding, bulk mechanical edits, generated files, or fragile transformations,
- an existing script/tool might already solve the task,
- the agent is about to create a repeatable helper script,
- the agent needs a known procedure without rereading large code paths.

## When not to read

- the task is a simple source edit in one named file,
- the task has no tooling, script, encoding, or repeated procedure angle,
- the relevant command is already explicit in the user request.

## Tooling rule

For mojibake, encoding repairs, bulk mechanical edits, repeated formatting, or fragile transformations:

1. Create a script/tool instead of doing manual one-off edits.
2. Run it against the intended target.
3. Inspect the result.
4. Fix the script until it works.
5. Keep or document the tool only if it is reusable.
6. If the issue was a meaningful recurring error, update `Agent/error-memory/` at the end of the task.
```

## Core Document Header

```md
# <Title>

## Purpose

This document is part of the split operational memory. Read it only when the task matches its scope.

## When to read

- <task condition>

## When not to read

- <non-task condition>

## Content
```

## Error Memory README.md

```md
# Error Memory Documentation Foundation

This folder defines a compact and task-aware error memory system.

## Core principles

- Route first through `errors/INDEX.md`.
- Do not read all error files by default.
- Read only categories that match the current task.
- Search for exact sections before reading full files.
- Store root causes and fixes, not raw noise.
- Update memory only at the end of meaningful work.
- Prevent duplicate entries.
- Keep everything in English and ASCII.
```

## Error Memory errors/INDEX.md

```md
# Error Memory Router Index

This file is the router for error memory.

Do not read all files by default.
Do not bulk-load the `errors/` directory.
Do not open unrelated categories.

## How to use

1. Decide if the task needs error memory.
2. If needed, read this index first.
3. Select only matching categories.
4. Search selected files for exact sections.
5. Read the smallest useful section only.

## When not to read error memory

- greetings
- simple chat replies
- generic conceptual explanations
- simple formatting tasks
- adding a temporary `console.log`
- changing one small line in a user-named file
- fixing a typo
- unrelated non-technical questions
- tasks with no code, command, config, or debugging work

## Shared write strategy

- Update at the end of meaningful work only.
- Store pattern, root cause, and final fix.
- Avoid raw logs and repeated traces.
- Avoid duplicate entries with the same root cause.

## <Category> errors

File:
`errors/<category>-errors.md`

Read when:

- <task condition>

Do not read when:

- <non-task condition>

Keywords:
<keyword1>, <keyword2>, <keyword3>

Priority:
<High/Medium/Low and when>

Scope notes:
<short scope>
```

## Error Memory errors/TEMPLATE.md

```md
# Error Entry Template

Use this template for new entries.

Create a new ID only when the root cause is meaningfully different.
If root cause is the same, update the existing entry.

## <CATEGORY_CODE><NUMBER> - <short title>

Category:
<category name>

Keywords:
<keyword1>, <keyword2>, <keyword3>

Symptoms:
<what failed from user or runtime perspective>

Context:
<where and when this pattern appears>

Root cause:
<technical cause, concise and specific>

Fix:
<final fix that solved it>

Avoid:
<what not to do next time>

Affected tools or modules:
<tool/module list or N/A>

Related files:
<internal paths only, optional>

Last updated:
YYYY-MM-DD
```
