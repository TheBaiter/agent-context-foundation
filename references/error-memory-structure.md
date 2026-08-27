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
    powershell/
      <case>.md
    node-npm-errors.md
    node-npm/
      <case>.md
    git-errors.md
    git/
      <case>.md
    database-errors.md
    database/
      <case>.md
    api-errors.md
    api/
      <case>.md
    frontend-errors.md
    frontend/
      <case>.md
    deployment-errors.md
    deployment/
      <case>.md
    performance-errors.md
    performance/
      <case>.md
```

Adjust categories to the repository, but keep `errors/INDEX.md` as the router.

## Main Principle

The agent must not read all error documents by default.

Error memory must be grouped by category and recurring root cause. Do not organize it by date, by chat session, by agent name, or by raw terminal output.

Use this structure:

- `errors/INDEX.md` routes every category.
- `errors/<category>-errors.md` is a compact router for one category.
- `errors/<category>/<case>.md` stores one root cause and final fix when the category has more than one meaningful case.
- Small repositories may keep a tiny category file only until it becomes too large.
- New category files are created only when a meaningful recurring error class exists.
- `errors/INDEX.md` is updated only when category routing changes.

Default flow:

1. Understand the current task.
2. Decide whether error memory is relevant.
3. If not relevant, do not read any error memory.
4. If relevant, read only `errors/INDEX.md` first.
5. Use the index as a router.
6. Open or search only the relevant category router or category folder.
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

Each case file should describe one unique verified root cause or one high-value recurring failure pattern.

Task investigation history does not belong here. Keep attempts, hypotheses, and temporary observations in the task record until the lesson is verified and reusable.

Keep category router files short. They should route to case files and define category scope, not store every detail.

Case file template:

```md
Pattern:
<when this case applies>

Read when:
<task or symptom conditions>

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

Evidence / anchors:
<paths, symbols, tests, commands, issue/decision ids, optional>

Status:
active | challenged | superseded

Supersedes:
<case path or N/A, optional>

Last verified:
YYYY-MM-DD
```

Avoid repeating the case title inside the file when the filename already carries it.

## Promotion Gate

Do not write an error-memory case merely because an error occurred.

Use this lifecycle:

`discovered -> candidate -> verified -> durable`

During investigation:

- keep raw symptoms, attempts, hypotheses, and partial findings in the task record,
- mark a reusable lesson as a candidate only when it may matter beyond the current step,
- verify the root cause and fix through reproducible behavior, source inspection, exact tests, authoritative documentation, or an explicit project decision,
- promote the case to durable error memory only when the lesson is stable enough to guide future work.

A one-off anomaly with no verified reusable lesson should stay in task history.

A single occurrence may still justify durable memory when the root cause is verified and the failure is expensive, dangerous, non-obvious, or likely to recur.

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
- evidence or source anchors when they help future re-verification,
- status when a case is challenged or superseded,
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
- unverified hypotheses,
- transient task chronology,
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

## Staleness And Superseding

Error memory must not remain active merely because it was once correct.

When a case depends on specific files, symbols, configuration, commands, schemas, or external contracts, keep compact anchors that make re-verification possible.

Treat a case as potentially stale when:

- anchored source changes materially,
- the owning architecture changes,
- a command or dependency is replaced,
- a new verified fix contradicts the old one,
- the documented symptom no longer reproduces.

Use these states when needed:

- `active` - currently verified and applicable,
- `challenged` - evidence suggests it may no longer be reliable; reverify before high-impact use,
- `superseded` - replaced by a newer verified case or rule.

Do not keep two contradictory cases active.

When a new case replaces an old one:

1. update the canonical active case,
2. mark or remove the old case,
3. keep only the historical pointer needed to understand the transition,
4. update routers only if routing changed.

## Writing Policy

Do not update error memory continuously during every small step.

During the task:

- solve the problem,
- observe errors,
- keep attempts, hypotheses, and temporary findings in the authoritative task record when they affect continuation,
- identify candidate reusable lessons,
- avoid permanent memory updates before the root cause and fix are verified.

At the end:

1. Review what actually mattered.
2. Identify candidate reusable error patterns.
3. Verify the root cause, fix, and applicability.
4. Check for duplicates, stale cases, and contradictions.
5. Promote only verified reusable lessons.
6. Update the canonical category router or case file.
7. Supersede or retire conflicting old guidance when needed.
8. Update `errors/INDEX.md` only if routing changed.
9. Keep task chronology in the task record.
10. Do not store noise.

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
- distinguish verified reusable cases from historical task noise,
- create one case file per unique verified root cause when a legacy category has multiple useful entries,
- keep the legacy category file as a router after migration,
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
- Did the agent keep investigation history in the task record instead of durable error memory?
- Did the agent avoid updating memory before verification?
- Did the agent promote only verified reusable lessons?
- Did the agent avoid duplicate entries?
- Did the agent check for stale, challenged, superseded, or contradictory cases?
- Did the agent store root cause and evidence, not just symptoms?
- Did the agent avoid secrets and raw logs?
- Did the agent update `errors/INDEX.md` only when needed?
- Did the final documentation remain English and ASCII-only?
