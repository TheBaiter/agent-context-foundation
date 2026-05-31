# Error Memory Structure

Use this reference when creating or migrating error memory.

## Purpose

Create a compact, indexed, task-aware memory system for useful error patterns.

The system must not behave like a generic log archive. It must be routed, searched, summarized, and never bulk-loaded.

## Language And Encoding Policy

All error-memory documentation must be written in English and ASCII-only text.

Use:

- simple hyphens,
- straight quotes,
- lowercase filenames,
- clear English,
- stable technical terms.

Avoid:

- accents,
- emojis,
- smart quotes,
- em dashes,
- non-ASCII symbols,
- mojibake-prone text.

## Required Structure

```text
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
```

Adjust categories to the repository, but keep `errors/INDEX.md` as the router.

## Main Principle

The agent must not read all error documents by default.

Default flow:

1. Understand the current task.
2. Decide whether error memory is relevant.
3. If not relevant, do not read any error memory.
4. If relevant, read only `errors/INDEX.md` first.
5. Use the index as a router.
6. Open or search only the relevant error file.
7. Prefer reading only the exact matching section.
8. Do not read unrelated error files.
9. Do not update error memory until the end of meaningful work.
10. When updating, store patterns and fixes, not raw noise.

## When Not To Read Error Memory

Do not read error memory for:

- greetings,
- simple chat answers,
- generic explanations,
- simple formatting requests,
- adding a temporary `console.log`,
- changing one small line in a user-named file,
- fixing a typo,
- unrelated questions,
- tasks that do not involve code, commands, configuration, debugging, or implementation,
- tasks where no known error category seems relevant.

If no category in `errors/INDEX.md` matches the task, continue without reading category files.

## Exact Section Reading Policy

When a relevant error file is needed:

1. Search inside the relevant file first.
2. Match by keywords from `errors/INDEX.md`.
3. Read only the matching section.
4. If needed, read a small surrounding range.
5. Read the full file only if the file is small or search is insufficient.

Example searches:

```powershell
rg -n "execution policy|npx|quoting" errors/powershell-errors.md
rg -n "refresh token|invalid caller|seller_id" errors/api-errors.md
rg -n "hydration|server component|client component" errors/frontend-errors.md
```

Never:

- use `cat` on all error files,
- open every error document,
- bulk-load the `errors/` directory,
- read unrelated categories.

## Index Design

`errors/INDEX.md` is the most important file.

It must act as a router, not just a list of files.

Each category should include:

- category name,
- file path,
- when to read,
- when not to read,
- keywords,
- priority,
- scope notes.

Example:

```md
## PowerShell errors

File:
`errors/powershell-errors.md`

Read when:

- the task involves PowerShell
- the task involves Windows terminal commands
- the task involves npm, npx, node, or scripts on Windows
- the task involves execution policy
- the task involves command quoting
- the task involves path escaping
- the task involves environment variables in PowerShell

Do not read when:

- the task is about generic JavaScript code
- the task is about Linux-only deployment
- the task is only a conceptual explanation
- the task is trivial and does not require command execution

Keywords:
powershell, pwsh, windows terminal, npm, npx, node, execution policy, env vars, quoting, path, script, command not found

Priority:
High when the task includes Windows shell commands.

Scope notes:
Command syntax and execution behavior in PowerShell.
```

## Error File Design

Each error file should be organized into small sections.

Each section should describe one unique error pattern.

Entry template:

```md
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

## What To Store

Store:

- error category,
- symptoms,
- context,
- root cause,
- final fix,
- what to avoid next time,
- relevant keywords,
- affected tools or modules,
- internal links only when useful,
- short examples when they clarify the pattern.

Do not store:

- repeated stack traces,
- full logs unless essential,
- raw terminal dumps,
- private credentials,
- secrets,
- access tokens,
- refresh tokens,
- API keys,
- passwords,
- unrelated conversation history,
- every failed attempt,
- duplicated errors with the same root cause.

## Deduplication Policy

The agent must not create a new error entry every time an error happens.

Before adding a new entry, check:

1. Does this error already exist?
2. Is this the same root cause with a different message?
3. Is this a meaningful variant?
4. Should an existing entry be updated instead?
5. Is this important enough to store?

If the root cause is the same, update the existing entry.

Create a new entry only when root cause, context, or fix is meaningfully different.

## Writing Policy

Do not update error memory continuously during every small step.

During the task:

- solve the problem,
- observe errors,
- keep temporary notes if needed,
- avoid permanent memory updates too early.

At the end:

1. Review what actually mattered.
2. Identify unique error patterns.
3. Check for duplicates.
4. Update the correct category file.
5. Add concise, useful information only.
6. Update `errors/INDEX.md` only if needed.
7. Do not store noise.

## When To Update INDEX.md

Update `errors/INDEX.md` only when:

- a new error category is created,
- important new keywords are added,
- a category changes scope,
- a file is renamed,
- routing rules change,
- priority changes.

Do not update `errors/INDEX.md` for every new error entry.

## Task-Aware Examples

Task: "Fix this PowerShell command."

Expected behavior:

- read `errors/INDEX.md`,
- match PowerShell category,
- search `errors/powershell-errors.md`,
- read only the relevant section,
- apply the fix.

Do not read:

- `database-errors.md`,
- `frontend-errors.md`,
- `deployment-errors.md`.

Task: "Hello."

Expected behavior:

- do not read error memory,
- answer normally.

Task: "Refactor a React component."

Expected behavior:

- read `errors/INDEX.md` only if previous known frontend errors or risk areas are relevant,
- if relevant, search `frontend-errors.md`,
- otherwise continue without error memory.

Task: "Fix token refresh for Mercado Libre."

Expected behavior:

- read `errors/INDEX.md`,
- match API/auth/token categories,
- search for token, refresh, seller_id, invalid caller, or similar keywords,
- read only relevant sections.

## Migration Rules

When migrating a legacy error log:

- parse entries by section,
- keep only useful patterns,
- normalize to English and ASCII,
- deduplicate by root cause,
- skip noise and repeated failures,
- keep a short migration summary,
- avoid fake project-specific history,
- remove or retire the legacy log only after references are updated.

## Validation Checklist

Before finishing work involving error memory, verify:

- Did the agent read only `errors/INDEX.md` first?
- Did the agent avoid unrelated error files?
- Did the agent search before reading a full file?
- Did the agent read only the smallest useful section?
- Did the agent avoid updating memory during every step?
- Did the agent update memory only at the end?
- Did the agent avoid duplicate entries?
- Did the agent store root cause, not just symptoms?
- Did the agent avoid secrets and raw logs?
- Did the agent update `errors/INDEX.md` only when needed?
- Did the final documentation remain English and ASCII-only?
