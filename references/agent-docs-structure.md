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

The top of this file should help a user understand the installed foundation without reading the whole folder.

Recommended first sections:

- `Golden Rules` - first section after the H1 title. These rules should almost never be bypassed: route by task, do not read everything, do not store secrets, keep docs ASCII-only, update memory only for reusable knowledge, and ask before deciding whether first-time `Agent/` docs are committed or ignored.
- `Initial Operating Checklist` - second section. It should force scope, plan, routed documentation, error-memory relevance, risk, verification, and checklist decisions before editing.
- `Foundation Identity` - short self-reference naming `agent-context-foundation`, canonical source `TheBaiter/agent-context-foundation`, and the purpose of the generated `Agent/` folder.
- `First-Time Setup Transparency` - short setup contract explaining that first-time creation must disclose the skill goal, likely files, privacy choice, permissions, prohibited actions, credential rules, and Git tracking decision.
- `Skill Update Check` - short maintenance note telling future agents to periodically check `TheBaiter/agent-context-foundation` for relevant updates.
- `What This Does` - one short explanation of the foundation and the optional files it may create.
- `Normal Rules` - everyday operating rules: read source before editing, use owner folders, prefer local patterns, use tools for fragile transformations, run matching checks, and report verification.

Required content:

- brief "what this does" explanation for users and future agents,
- golden rules that are always true and placed immediately after the H1 title,
- initial operating checklist placed immediately after golden rules,
- foundation identity that states which skill generated or maintains the folder,
- first-time setup transparency for privacy, permissions, prohibited actions, credential rules, and Git tracking,
- periodic skill update check guidance,
- normal rules that apply after routing is understood,
- first-time `Agent/` Git tracking decision rule,
- minimal reading flow,
- rule against reading the whole docs folder,
- rule against reading broad docs for trivial known-file changes,
- English and ASCII-only policy,
- task checklist,
- closing checklist rule,
- routes for summaries, tools, project rules, and error memory when relevant,
- guidance for grouping reusable knowledge in local README files, summaries, tools, or existing routed docs,
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
- summary, tool, project-rule, and closing-checklist routes when present,
- planning route when the repository has project-specific planning preferences,
- error memory routing,
- derived project bootstrap routing when the repo contains reusable templates or starter flows,
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
- put golden rules at the very beginning,
- put the initial operating checklist immediately after golden rules,
- include first-time setup transparency rules,
- include periodic skill update check rules,
- include the first-time `Agent/` Git tracking decision rule,
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

### Closing Checklists

Use `closing-checklists.md` when the repository benefits from intent-based closeout checks.

Read it only when:

- the task changes behavior, UI, API contracts, data, deploy, auth, scripts, dependencies, or operational documentation,
- there was a failed verification, wrong assumption, or recurring error,
- the work creates reusable knowledge for future agents.

Do not read it for trivial file-local edits, pure chat answers, or analysis with no changes.

At minimum, require agents to state in the final response:

- which route or checklist was used,
- what was verified,
- what remains risky, unverified, or intentionally skipped,
- whether summaries, project rules, tools, or error memory were updated.
- whether first-time `Agent/` Git tracking was confirmed or remains pending.

Include topic-based sections when the repository needs them:

- trivial change,
- implementation change,
- documentation change,
- UI or frontend change,
- API, data, or contract change,
- auth, security, or credentials change,
- deployment, environment, or dependency change,
- tooling or mechanical repair,
- project rules,
- internal summaries,
- error memory.

The documentation checklist should include a first-time `Agent/` Git tracking check:

- ask whether `Agent/` should be committed to Git or added to `.gitignore`,
- explain committed docs versus local-only docs briefly,
- change `.gitignore` only with explicit user confirmation,
- leave `.gitignore` unchanged if the user does not answer.

The documentation checklist should also include first-time setup transparency:

- explain what `agent-context-foundation` does before creating broad `Agent/` docs,
- explain why it is being used and which files or folders may change,
- ask or record pending decisions for privacy, permissions, prohibited actions, credential handling, Git tracking, and `.gitignore`,
- document pending decisions in `Agent/README.md` and mention them in the final response.

Generated `Agent/README.md` should include a skill update check:

- active repositories should check `TheBaiter/agent-context-foundation` about once per month,
- quiet or maintenance-only repositories should check at least once per year,
- agents should check sooner when repeated agent mistakes return or the user asks for improvements,
- broad template updates from a newer skill version require a short explanation and user confirmation.

### Project Rules

Use `project-rules.md` for non-secret operational constraints.

Read it when a task may depend on:

- allowed environments, tenants, schemas, organizations, or accounts,
- safe API probes and query limits,
- local verification commands,
- actions requiring explicit user approval,
- test credential policy,
- known risky areas.

Do not store credentials, tokens, API keys, refresh tokens, passwords, production customer data, or other secrets.

### Planning Guidance

Use `planning/README.md` when generic planning skills need to adapt to this repository or user.

Read it when:

- the task is multi-step, risky, ambiguous, or crosses multiple owners,
- the user asks for a plan, phased execution, roadmap, or review checkpoints,
- previous plans were too generic, too detailed, too vague, or missed project gates,
- the repository has a known preferred planning style.

Do not read it when:

- the task is a trivial edit in one named file,
- the user asks for direct implementation and the change is narrow,
- planning would add ceremony without reducing risk.

The planning file should capture:

- when to plan and when not to,
- preferred plan length and phase size,
- checkpoint and approval style,
- when to ask before continuing,
- required plan contents,
- how to update plans during execution,
- how to close plans with verification evidence,
- how to combine this repository's style with external planning skills.

Do not create planning guidance automatically for every repository. Recommend or create it when the user's planning style is known, planning mistakes repeat, or the project has complex multi-step workflows.

### Internal Summaries

Use `summaries/README.md` when future agents need short reusable context for pages, screens, flows, component groups, scripts, or recurring topics.

Summaries reduce repeated source and documentation loading. They do not replace source inspection or tests.

Read or update summaries when:

- a task touches a page, flow, component group, script, or topic future agents may revisit,
- behavior, contracts, risks, or verification steps changed,
- source exploration produced reusable context worth preserving.

Do not create summaries for trivial one-line edits or one-off topics with no likely reuse.

### Knowledge Grouping

Use knowledge grouping when a complex source area would otherwise force future agents to reread large files.

Recommended locations:

- local `README.md` inside a component, script, workflow, integration, generated-file process, or folder when the knowledge belongs next to that owner,
- `summaries/<topic>.md` when the knowledge is cross-cutting or belongs in agent memory,
- `tools/README.md` when the knowledge is a reusable command, script, or procedure,
- an existing routed `Agent/` document when it already owns the topic.

Do not create a README or summary for every task. Recommend or create one only when the topic is complex, likely to be revisited, or the note prevents repeated context loading or repeated mistakes.

### Derived Project Bootstrap

If a repository provides templates, starter flows, or reusable docs for other projects, include a bootstrap route.

The route should tell agents to:

- create or update the derived project's agent docs first,
- copy only relevant templates, summaries, project rules, and error-memory categories,
- link inherited guidance through the derived project's `Agent/INDEX.md`,
- keep project-specific constraints in `Agent/project-rules.md`,
- avoid importing secrets, raw logs, production credentials, customer data, or unrelated history.

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
7. Decide whether summaries, project rules, tools, or closing checklists apply.
8. Update docs only when reusable knowledge changed.

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
7. Choose `summaries/` for short reusable page, flow, component, script, or topic context.
8. Choose a local source-folder `README.md` when the knowledge belongs next to a complex component, script, workflow, integration, generated-file process, or folder.
9. Choose `planning/README.md` for project-specific planning preferences, phases, gates, and user planning style.
10. Choose `project-rules.md` for non-secret operating constraints.
11. Choose `closing-checklists.md` for intent-based closeout checks.
12. Update `INDEX.md` when the new document is part of the routed Agent foundation.
13. Keep the file English and ASCII-only.
