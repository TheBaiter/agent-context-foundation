---
name: agent-context-foundation
description: Keep coding-agent context focused, prevent task-boundary drift, and trace confirmed agent mistakes with minimal issue and error-memory pointers. Use for substantive repository changes, debugging, regressions or agent-context maintenance; load issues and detailed references only when evidence requires them.
---

# Agent Context Foundation

## Purpose

Make repository context cheaper to load, easier to route, safer to maintain, and easier to resume.

This skill is a decision engine. It should not become the repository's universal operating manual.

## Operational Application

Apply relevant rules directly when authorized; do not merely recommend them. Load only the needed module or source. Ask for approval only at a genuine authority, security, scope, or project-policy boundary. Document a blocker and its next action rather than claiming success.

## Core Invariants

- Preserve existing root/scoped `AGENTS.md` or `Agent/` instructions; do not invent a competing standard or universal Git/review policy.
- Prefer current user intent, existing context, local instructions and narrow source evidence. **Issue reading is conditional, never routine orientation.**
- Keep a single canonical owner for each rule, fact or contract; load by pointer, not duplicated histories. Add modules only when verified evidence justifies their cost.
- Distinguish app login, permission to view/use a feature, authorization of external services, execution safety, and persistence. A restriction in one dimension must not silently disable another.
- Track material agent-caused errors in one issue with cause, fix and actual validation, then keep a one-line `Agent/error-memory/INDEX.md` pointer while preventive. Do not duplicate issue narratives.
- Keep reusable memory verified and retire stale guidance; preserve precise code/test anchors, project language/encoding, and security boundaries. Never store secrets in agent context.
- Follow project policy for tests, branches and deployment. Disposable QA/debug artifacts belong in the project's existing temporary workspace, or `.agent-temp/` if needed.

Detailed principles: `references/foundation-principles.md`.

## Context Budget And Task Boundary Gate

**Default: do the task, not an exhaustive context audit.** Use the current request and context already in the session. Read the relevant existing agent instruction entrypoint (`AGENTS.md`, `Agent/README.md` or actual equivalent) and the narrowest code/contract owner. Do **not** preload every issue, recent comment, linked issue, module, repository directory, or error history.

1. **Cheap boundary:** state the requested outcome; distinguish what stays allowed, forbidden, unchanged, or deferred. Check only the dimensions that matter (identity, authorization, external integration, read/write, persistence, feature flag). Never infer that lack of login or cloud saving forbids unrelated catalogs, offline editing, or explicitly authorized temporary connections.
2. **Issue-read triggers, not a default:** consult the *specific* issue only when the request names it; a matching short error-memory pointer is relevant; the change depends on an unresolved earlier decision/contract; available context conflicts; or a confirmed error needs to be recorded. If the current request plus source resolves the task, **read zero issues**. Follow linked dependencies only if they actually block a decision. Do not search/list all issues for orientation.
3. **Progressive escalation:** begin with the minimum relevant files. Expand to API/integration/security owners or `references/task-boundaries.md` only when the observed behavior or risk requires them. Stop gathering context when the desired boundary, code owner, and relevant verification are clear. A high-risk cross-mode change merits deeper checks; a local edit does not need a full matrix.
4. **Check the outcome:** validate permitted behavior (positive), restricted effects (negative), adjacent modes (regression) in proportion to the change. Revisit the user-requested boundary on material corrections or contradictions, not on every micro-step. Tests authored, passed, and unrun must be distinguished.

**If the agent makes a meaningful mistake:** use the correction-and-memory procedure below. Never replace a requested implementation with lengthy analysis of issues.

## Error Correction, Issue Lifecycle And Short Memory

When the agent introduces a defect, regression, wrong assumption, avoidable tool misuse, or incorrect restriction with material impact:

1. Confirm the symptom, check whether an issue already owns **that error**, then create one if needed; do not scan unrelated issues or make duplicates. If the user supplied an issue ID, use it directly.
2. Record **what failed**, **why** (or explicitly unknown), **what changed to fix it**, **how it was verified**, **regression risks**, and a commit/reference. Update only at meaningful checkpoints; keep the detailed history in the issue.
3. Repair and perform a fresh validation pass. **Close the issue when the repair and its required verification are actually complete**; if blocked or untested, leave it open with the exact missing check and next step. Do not claim a pass because a test was merely written.
4. In the existing `Agent/error-memory/INDEX.md` (or the project's canonical error-memory index), add or update **one concise line**: `#issue — symptom/cause — prevention or corrected rule`. Create only this small index if no route exists and the error warrants a durable reminder. Keep this reference after issue closure if it remains useful; remove it when obsolete. **Do not copy issue timelines, logs, or full diagnoses into Agent/**.
5. Read that line when the same area or symptom recurs; fetch the full issue **only** if the line and current source are insufficient. Promote a detailed reusable case through `references/modules/error-memory.md` only when justified.

For ordinary meaningful work, reuse a task record if one is already provided or project policy demands it; **do not open or read issues merely for ceremony**. See `references/task-traceability.md` for the error lifecycle and `references/task-boundaries.md` only for a complex boundary.

## Workflow Routing

- **Product/engineering task:** apply the cheap Context Budget/Boundary Gate; load detailed task trace or boundary references only for confirmed errors, non-trivial cross-mode risks or genuine handoffs. Implement and validate the product request, not an agent-documentation audit.
- **Agent-context maintenance task:** use the foundation workflow below and load only evidence-backed modules. Context maintenance is not the default outcome of an engineering task.
- **Trivial work:** use proportionate checks; no issue, matrix, or module merely for ceremony.

## Context-Maintenance Workflow

Only use this route when the task concerns agent instructions, documentation routing or durable memory; ordinary coding tasks follow the cheap boundary gate instead.

1. Inspect the existing instruction entrypoint and the exact source or problem; read issues only when one of the trigger conditions applies.
2. Identify the canonical owner and classify the failure (irrelevant context, contradictory/stale rule, missing owner/anchor, or a confirmed agent error). Use the issue correction lifecycle for the last case.
3. Choose the minimum solution: no change, correct a pointer, compact stale text, or add one justified module. Do not create directories/templates just because they exist.
4. Change the smallest affected files. Recheck meaning, routing, links, unrelated behavior, encoding, secrets and the actual diff.
5. Record relevant outcome and verification; close an error issue only after required checks pass. Keep one preventive index pointer where useful; do not store the issue's history in docs.

## Module Router

Read a module only when its condition is true.

| Need | Read |
| --- | --- |
| Create or repair the base instruction route | `references/modules/foundation.md` |
| Repository orientation is repeatedly expensive | `references/modules/project-map.md` |
| Verified recurring failure knowledge exists | `references/modules/error-memory.md` |
| A repeated fragile procedure should become a tool | `references/modules/tools.md` |
| A complex cross-cutting area is repeatedly reconstructed | `references/modules/summaries.md` |
| Durable project-specific planning conventions exist | `references/modules/planning.md` |
| Non-obvious project-wide operating constraints exist | `references/modules/project-rules.md` |
| Specialized recurring verification or closeout is needed | `references/modules/checklists.md` |
| Existing agent docs or memory need migration/compaction | `references/modules/migration.md` |
| The user wants reusable Codex personalization | `references/modules/codex-customization.md` |
| Disposable QA/visual/debug artifacts are generated | `references/modules/temporary-workspace.md` |

Do not read every module to decide whether it is needed. The workflow and repository evidence decide first.

## Template Router

Output templates are **optional skeletons**, not policy owners. Only after deciding to create a specific document, load its matching file in `references/templates/` (for example `base-readme.md`, `base-index.md`, `error-case.md`, `project-map.md`, `planning.md`). Never bulk-load templates.

## Minimum Foundation

If the repository already has a valid agent instruction route, preserve it.

If a new routed `Agent/` foundation is actually needed, start with only:

```text
Agent/
  README.md
  INDEX.md
```

Everything else is optional and evidence-backed.

Do not create empty folders, hypothetical error categories, placeholder modules, or documentation merely because a template exists.

## Knowledge Placement

Implementation truth belongs in code; operating rules in scoped instructions; durable conventions in their owning module; active task/error history in the issue; a short error pointer in the project's canonical Agent memory index; detailed reusable lessons only after verification. Use pointers rather than copying content.

## First Run

If context is missing, describe the existing instruction route and smallest justified repair. Do not produce a catalog of modules, demand approvals without a real boundary, or invent Git/security policies.

## Context Health Audit

Correct the actual cause: distracting reads, unclear ownership, contradictory or stale guidance, or lost high-value anchors. Do not fix context overload by adding another layer of mandatory context.

## Self-Audit

Confirm that the default context load is smaller; task boundaries remain correct; no issue is read without a trigger; matching modules and links resolve; no active issue narrative is copied into Agent; confirmed mistakes have verified issue records and concise pointers; permissions/security and existing project conventions are preserved; and no unnecessary files were created.

## Completion

Report the actual change, validation performed, unverified risks, and the issue/commit or next action. Never claim a test or integration was executed when it was only described.

