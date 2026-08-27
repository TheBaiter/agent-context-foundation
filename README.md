# Agent Context Foundation

[![Skill](https://img.shields.io/badge/skill-agent--context--foundation-blue)](https://github.com/TheBaiter/agent-context-foundation)

Agent Context Foundation is a Codex/agent skill for creating task-routed agent documentation in a repository.

Its purpose is to help agents work with less irrelevant context, fewer repeated mistakes, better long-term memory, and clear task traceability without burning tokens on documentation that does not apply to the current task.

## What It Solves

Many repositories accumulate large agent prompts, long operational manuals, and noisy error logs. Agents often load too much of that material, even for small tasks.

This skill helps create a cleaner structure:

- short entry documents,
- a central routing index,
- a project map for broad orientation without repeated source-tree scans,
- topic-specific core documents,
- specialized docs only when needed,
- indexed error memory with compact category routers and one case file per recurring root cause,
- reusable tool/procedure notes and agent-owned scripts under `Agent/tools/scripts/`,
- internal summaries for recurring pages, flows, components, scripts, and topics,
- project-specific planning guidance that captures the user's planning style,
- local README or summary guidance for complex components, scripts, flows, and folders,
- non-secret project operating rules,
- intent-based and topic-based closing checklists,
- copy-ready Codex customization text.

The goal is not to reduce quality or to minimize files for its own sake. The goal is to minimize the total cost of completing work correctly: reading, discovery, correction, verification, recovery, and handoff.

The foundation follows these rules:

- every persistent line must justify its future context cost,
- entrypoints route and owners explain,
- one durable fact or rule has one canonical owner,
- optional modules are created only when evidence shows they reduce future risk or rediscovery,
- existing standards such as root or nested `AGENTS.md` are preserved when they already own agent instructions,
- durable guidance, current state, task history, observations, and recurring error knowledge are kept distinct,
- new knowledge is promoted only after evidence: `discovered -> candidate -> verified -> durable`,
- stale or contradictory memory is consolidated, superseded, reverified, retired, or removed,
- context health is reviewed for distraction, confusion, clashes, poisoning, and lost critical anchors,
- exact paths, symbols, commands, tests, owners, and handoff points are preserved when they prevent expensive rediscovery,
- the correct result may be to create no new documentation,
- every meaningful task leaves a durable execution trace in the project's existing issue, ticket, plan, or task system.

Task traceability records how work progressed. Durable memory records only what future agents should continue to know after the task is over.

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
- why the skill is being used in this repository,
- the golden rules future agents must follow,
- the normal operating rules future agents should follow,
- the privacy choice for `Agent/`,
- the agent permissions and actions that require explicit user approval,
- prohibited actions and credential handling rules,
- the no-secrets policy,
- the English and ASCII-only rule for generated `Agent/` docs,
- whether the generated `Agent/` folder should be committed to Git or added to `.gitignore`.

Generated `Agent/README.md` files should put "Golden Rules" immediately after the title, followed by compact "What This Does" and "Normal Rules" sections so users can understand and configure the foundation without reading every generated document.

Generated `Agent/README.md` and Codex customization text should also include an initial operating checklist immediately after the golden rules. That checklist tells agents to define scope, plan before editing, use routed docs as evidence, check relevant error memory, choose verification, and avoid blind implementation.

Generated `Agent/README.md` files should also include a short "Foundation Identity" section naming `agent-context-foundation`, the canonical source `TheBaiter/agent-context-foundation`, and the purpose of the generated `Agent/` folder. This makes the folder self-identifying for other project users and future agents.

Generated `Agent/README.md` files should also include first-time setup transparency. If privacy, permissions, prohibited actions, credential handling, or Git tracking are not decided, the generated docs should leave those items as pending decisions and the agent should mention them in the final response.

Generated `Agent/README.md` files should include a skill update check that points to `TheBaiter/agent-context-foundation`. Active repositories should check about once per month, quiet repositories should check at least once per year, and agents should check sooner when repeated mistakes return or the user asks for skill improvements.

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
6. Report any conflict between the task and documented rules before changing files.
7. Establish or reuse the project's task record for meaningful work and update it while decisions, failures, verification, and handoff happen.
8. Update durable documentation and error memory only when reusable verified knowledge changed.

## What The Skill Creates

The skill no longer assumes that every repository needs the same large `Agent/` tree.

If a repository already has a valid agent instruction standard such as `AGENTS.md`, preserve it and add routed supporting context only when needed.

If a new routed foundation is needed, start with the minimum:

```text
Agent/
  README.md
  INDEX.md
```

Then add only evidence-backed modules:

```text
Agent/
  project-map.md
  core/
  error-memory/
  tools/
  summaries/
  planning/
  project-rules.md
  checklists/
  recommended-codex-customization.md
  .generated/
```

A module exists only when it has a demonstrated job. Empty structure and hypothetical knowledge are not a feature.

Task execution history belongs in the project's existing coordination system, not in `Agent/` by default. The foundation teaches agents to maintain that trace during work and to promote only verified reusable conclusions into durable project context.

## What It Covers

- Preserving and improving existing root or nested `AGENTS.md`, `Agent.md`, or similar instruction systems without creating competing sources of truth.
- Creating `Agent/README.md` as a minimal entry point.
- Creating `Agent/INDEX.md` as the main routing document.
- Creating `Agent/project-map.md` when broad orientation would otherwise require repeated scanning.
- Creating `Agent/core/` for broad but task-specific guidance.
- Creating `Agent/error-memory/` as routed, searchable memory with category routers and small case files.
- Creating `Agent/tools/README.md` and `Agent/tools/scripts/` for reusable scripts and learned procedures.
- Creating `Agent/summaries/README.md` for short reusable context on pages, flows, components, scripts, and recurring topics.
- Creating `Agent/planning/README.md` only when project-specific planning preferences need durable guidance.
- Requiring meaningful work to use the project's existing issue, ticket, plan, or task system for execution traceability.
- Recommending local README or summary files for complex source areas when they would reduce repeated rereading.
- Creating `Agent/project-rules.md` for non-secret operating constraints such as allowed environments, safe probes, and approval gates.
- Creating `Agent/checklists/INDEX.md` so agents close work with the matching intent-based or topic-based checklist and report verification clearly.
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
- search category routers or folders with `rg -n`,
- read one matching case file when possible,
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
references/foundation-principles.md
references/task-traceability.md
references/agent-docs-structure.md
references/error-memory-structure.md
references/templates.md
```

`SKILL.md` is the operational entry point. `references/foundation-principles.md` owns the V2 context model, `references/task-traceability.md` owns execution traceability, and the remaining `references/` files are loaded only when their phase or module is relevant.

## Validation

This skill has been validated with the Codex skill validator:

```text
quick_validate.py agent-context-foundation
```

The skill files are intended to stay ASCII-only.
