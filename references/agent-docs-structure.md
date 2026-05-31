# Agent Documentation Structure

Use this reference when creating or refactoring agent-facing documentation.

## Goal

Make documentation task-routed so agents do not read irrelevant context.

## Entry Files

### Root README.md

Purpose:

- tell human readers that the main README is human-facing,
- tell LLMs where agent-specific docs live,
- prevent agents from searching randomly for instructions.

Recommended notice near the top:

```md
> This `README.md` is aimed at human developers.
> If you are an LLM, read `Agent/README.md` before acting in this repo and load only task-relevant documents listed there.
```

Keep this notice short. Do not duplicate the full agent guide in the root README.

### README.md

Purpose:

- first file agents read inside the docs folder,
- short operating rules,
- ASCII policy,
- pointer to `INDEX.md`.

Keep it short. Do not put full project details here.

Required content:

- minimal reading flow,
- rule against reading the whole docs folder,
- rule against reading broad docs for trivial known-file changes,
- English and ASCII-only policy,
- task checklist,
- where to add new documentation.

### INDEX.md

Purpose:

- main router,
- map task areas to documents,
- prevent bulk reading,
- define where future guidance belongs.

Required content:

- global rules,
- core document table,
- specialized document table,
- error memory routing,
- adding-new-guidance policy.

### Agent.md

Use only when compatibility is useful.

If created, keep it short and make it point to:

- `README.md`,
- `INDEX.md`,
- `core/README.md`.

Do not keep a long `Agent.md` as the primary guide.

### recommended-codex-customization.md

Purpose:

- provide copy-ready text for Codex personalization,
- make future sessions start with the same routing rules,
- tell agents to read the root README, `Agent/README.md`, and `Agent/INDEX.md`,
- enforce English and ASCII-only documentation rules,
- enforce scoped reading and error-memory routing.

Do not wrap it in commentary. It should be directly copyable into a Codex customization field.

It should include a new-repository rule:

- if `Agent/README.md` or `Agent/INDEX.md` is missing, use `$agent-context-foundation` when installed,
- canonical install source: `TheBaiter/agent-context-foundation`,
- if it is not installed, install it with `npx skills add TheBaiter/agent-context-foundation` when possible,
- if direct install is not possible, use `$find-skills` and search for `agent-context-foundation` by `TheBaiter`,
- if no skill is available, create only the smallest entry and router first.

### Local Access Or QA Access Docs

Use a local access document when visual QA, browser tests, smokes, or authenticated test flows need reusable test credentials.

Rules:

- ask the user before writing any credential value,
- store only local, demo, QA, or test credentials the user explicitly allows,
- never store production credentials, customer credentials, service-role secrets, API keys, tokens, or refresh tokens,
- if permission is unclear, document how to configure credentials instead of storing values,
- include environment, scope, username, password only when allowed, last verified date, and reset notes.

For public repositories, prefer placeholders or environment variable names.

### Tools Docs

Use `tools/README.md` for reusable scripts, local tools, and learned procedures.

Read it only when:

- the task involves mojibake, encoding, generated files, fragile transformations, or bulk mechanical edits,
- an existing script/tool may already solve the task,
- the agent is about to create a repeatable helper script.

Required rule:

- create a script/tool for fragile repeated fixes,
- run it,
- inspect the result,
- fix the script until it works,
- document it only if it is reusable.

### Skill Coverage Checklist

Use `skill-coverage-checklist.md` only for maintaining the reusable skill or comparing it with the local `Agent/` structure.

Do not route normal implementation tasks to that file.

## Core Folder

Use `core/` for broad reusable guidance.

Add `core/README.md` so agents can see the local map without reading every core file.

Recommended files:

- `project-overview.md` - product scope, stack, repo layout, source-of-truth files.
- `routing-auth-access.md` - routes, auth, sessions, proxy, organizations, permissions.
- `business-domain.md` - domain semantics and product behavior.
- `data-model-and-data-layer.md` - schema, migrations, RLS, RPC, repository layer.
- `ui-and-forms.md` - frontend UI, forms, fields, tables, CRUD screens.
- `env-scripts-quality.md` - env vars, scripts, tests, typecheck, build, verification.
- `security-and-agent-roles.md` - secrets, restrictions, deploy notes, task-agent routing.

Each task-specific file should include:

- purpose,
- when to read,
- when not to read,
- concrete source files or folders,
- rules for future updates.

## Specialized Docs

Keep narrow docs outside `core/` when they are used only for specific workflows.

Examples:

- forms,
- datatables,
- workflow events,
- visual QA,
- local access,
- QA or test access,
- reusable tools and scripts,
- skill coverage audits,
- closing checklist,
- entity conventions.

Link each specialized doc from `INDEX.md`.

## Task Checklist

Add a compact checklist to the entry docs:

1. Identify whether the task is trivial, narrow, or domain-specific.
2. For trivial tasks, read only the entry router and the named source file.
3. For domain tasks, read only documents routed by `INDEX.md`.
4. Decide whether error memory is relevant.
5. If error memory is not relevant, do not read it.
6. If error memory is relevant, route through `error-memory/errors/INDEX.md`.
7. Update docs only when reusable knowledge changed.

Examples of trivial tasks:

- add a temporary `console.log`,
- fix a typo,
- adjust formatting in one named file,
- answer a simple question.

These tasks should not trigger reading all docs or all error files.

## Adding New Documentation

Add a new file only when it prevents repeated context loading or captures a reusable rule.

Before adding:

1. Check whether an existing document owns the topic.
2. Choose `core/` for broad reusable guidance.
3. Choose a specialized doc for narrow workflow rules.
4. Choose `error-memory/` for error patterns.
5. Choose local access docs only for approved non-production QA/test credentials.
6. Choose `tools/README.md` for reusable scripts, tools, and learned procedures.
7. Update `INDEX.md`.
8. Keep the file English and ASCII-only.
