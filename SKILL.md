---
name: agent-context-foundation
description: Use at the start and throughout repository coding, review, bugfix, feature, test, or agent-instruction tasks, even when not named. Ensure the target repo has a standing AGENTS.md bridge to Agent/ context, record confirmed agent errors including user corrections, and validate changes/regressions with actual evidence and screenshots for visual work.
---

# Agent Context Foundation

## Purpose

Provide a lightweight, repeatable start-of-task discipline: find the project's instructions, preserve its boundaries, make the smallest complete change, verify effects, and retain useful error memory.

This skill is a decision engine, not a universal manual. Its discovery metadata improves implicit selection but cannot force loading: for every-session reliability, use a short standing AGENTS.md bridge in the host project (documented in README).

## Standing Project Entry Point (Required For Writable Repository Tasks)

This skill repository's own root `AGENTS.md` **does not apply to other projects**. For each target repository where code or instruction edits are authorized, establish its **root `AGENTS.md` file** as the persistent entry point. `AGENTS.md` is a *file*, not a folder; `Agent/` is the project-context folder. Check existing root/scoped `AGENTS.md` and project instructions first; **merge a short foundation bridge**, never overwrite or duplicate local instructions. The bridge must tell the agent to read the applicable `Agent/README.md` and `Agent/INDEX.md` (or established equivalent), route to relevant rules, use `agent-context-foundation` when installed, record confirmed errors, and validate actual changes before closure. Use `references/templates/codex-customization.md` as the canonical bridge.

- **At project startup or the first writable engineering task:** if no root `AGENTS.md` exists, create it with the standing bridge before modifying product code. If it exists without an effective foundation route, add only the missing bridge, retaining all existing rules and generated sections. If there is no usable `Agent/` context or equivalent, establish only `Agent/README.md` and `Agent/INDEX.md` with real routing; never manufacture empty modules. This is a required initialization check, **not** a reason to scan all project issues or documents.
- **At every subsequent task:** read the applicable standing instructions and relevant `Agent/` routing, then use only task-matching context. Recheck before final completion; do not assume prior session memory remains active.
- **Read-only, unavailable filesystem, restrictive project policy or absent installation:** do not claim the bridge was created or the skill loaded. Report the missing entry point and exact blocker. Do independent permitted work while keeping the bootstrap pending.
- **Actual activation limit:** metadata and a project's `AGENTS.md` can request this skill but cannot force an unsupported agent host to select or install it. Verify in a **fresh target-agent session**. An update to GitHub does not update local installed copies.

## Operational Application

Apply relevant rules directly when authorized; do not merely recommend them. Load only the needed module or source. Ask for approval only at a genuine authority, security, scope, or project-policy boundary. Document a blocker and its next action rather than claiming success.

## Core Invariants

- Preserve existing root/scoped `AGENTS.md` or `Agent/` instructions; do not invent a competing standard or universal Git/review policy.
- Prefer current user intent, existing context, local instructions and narrow source evidence. **Issue reading is conditional, never routine orientation.**
- Keep a single canonical owner for each rule, fact or contract; load by pointer, not duplicated histories. Add modules only when verified evidence justifies their cost.
- Distinguish app login, permission to view/use a feature, authorization of external services, execution safety, and persistence. A restriction in one dimension must not silently disable another.
- Track confirmed agent mistakes, including **mistakes identified by the user** (missed checks, ignored constraints, unjustified assumptions, defects and regressions), in one issue with cause, fix and actual validation, then keep a one-line `Agent/error-memory/INDEX.md` pointer. Do not blame the user or skip recording an oversight because the user discovered it. Avoid duplicate issue narratives and harmless transient-error noise.
- Keep reusable memory verified and retire stale guidance; preserve precise code/test anchors, project language/encoding, and security boundaries. Never store secrets in agent context.
- Follow project policy for tests, branches and deployment. Disposable QA/debug artifacts belong in the project's existing temporary workspace, or `.agent-temp/` if needed.

Detailed principles: `references/foundation-principles.md`.

## Default Startup And Smallest Complete Change

When selected for any repository task (including a simple fix or review):

1. **Read standing project instructions at the start of every task:** follow root/scoped `AGENTS.md`, then the project's `Agent/README.md` and `Agent/INDEX.md` or their existing equivalent to find relevant rules; read matching rules rather than every document. Do not confuse project `Agent/` (context), skill `agents/openai.yaml` (metadata), and Codex `.agents/skills/` (installation).
2. **Repair missing standing route:** on a writable repository task, create/merge the root `AGENTS.md` bridge if absent and, if no equivalent exists, the minimal `Agent/README.md` + `Agent/INDEX.md` context route. Preserve local/generated instructions. In read-only or blocked environments, report the missing route and keep it pending without obstructing independent work.
3. **Ponytail-compatible minimalism:** prefer no new code when existing behavior suffices; otherwise reuse existing components/contracts and choose the **smallest complete fix**, not merely the fewest edited lines. Follow affected callers, integration points and tests only as needed. Reject speculative abstractions, dependencies, migrations and unrelated features.
4. **Validate before demos and closeout:** re-read the resulting diff and user acceptance criteria, check requested behavior, adjacent regressions and security/data effects, and present **actual** test evidence. For visual UI work, capture and share screenshots of the observed state when tools permit. Never present an unverified example or simulation as a successful execution. Keep error issues and memory references current; do not reread context on every micro-step.

If the skill was not selected, standing `AGENTS.md` rules are the minimal fallback; do not claim the skill was executed merely because similar guidance was followed.

## Context Budget And Task Boundary Gate

**Default: do the task, not an exhaustive context audit.** Use the current request and context already in the session. Read the relevant existing agent instruction entrypoint (`AGENTS.md`, `Agent/README.md` or actual equivalent) and the narrowest code/contract owner. Do **not** preload every issue, recent comment, linked issue, module, repository directory, or error history.

1. **Cheap boundary:** state the requested outcome; distinguish what stays allowed, forbidden, unchanged, or deferred. Check only the dimensions that matter (identity, authorization, external integration, read/write, persistence, feature flag). Never infer that lack of login or cloud saving forbids unrelated catalogs, offline editing, or explicitly authorized temporary connections.
2. **Issue-read triggers, not a default:** consult the *specific* issue only when the request names it; a matching short error-memory pointer is relevant; the change depends on an unresolved earlier decision/contract; available context conflicts; or a confirmed error needs to be recorded. If the current request plus source resolves the task, **read zero issues**. Follow linked dependencies only if they actually block a decision. Do not search/list all issues for orientation.
3. **Progressive escalation:** begin with the minimum relevant files. Expand to API/integration/security owners or `references/task-boundaries.md` only when the observed behavior or risk requires them. Stop gathering context when the desired boundary, code owner, and relevant verification are clear. A high-risk cross-mode change merits deeper checks; a local edit does not need a full matrix.
4. **Check the outcome:** validate permitted behavior (positive), restricted effects (negative), adjacent modes (regression) in proportion to the change. Revisit the user-requested boundary on material corrections or contradictions, not on every micro-step. Tests authored, passed, and unrun must be distinguished.

**If the agent makes a meaningful mistake:** use the correction-and-memory procedure below. Never replace a requested implementation with lengthy analysis of issues.

## Error Correction, Issue Lifecycle And Short Memory

When an agent makes a confirmed meaningful mistake — including a regression, a missed user requirement, a wrong assumption, an unchecked claim, or a correction discovered/reported by the **user** that the agent should have caught — record it as the agent's error. Do not exclude user-provided corrections. A changed preference or harmless transient retry is not automatically a defect:

1. Confirm the symptom, check whether an issue already owns **that error**, then create one if needed; do not scan unrelated issues or make duplicates. If the user supplied an issue ID, use it directly.
2. Record **what failed**, **who/how detected it (including user correction)**, **why the agent missed it** (or explicitly unknown), **what changed to fix it**, **how it was verified**, **regression risks**, and a commit/reference. Update only at meaningful checkpoints; keep the detailed history in the issue.
3. Repair and perform a fresh validation pass. **Close the issue when the repair and its required verification are actually complete**; if blocked or untested, leave it open with the exact missing check and next step. Do not claim a pass because a test was merely written.
4. In the existing `Agent/error-memory/INDEX.md` (or the project's canonical error-memory index), add or update **one concise line**: `#issue — symptom/cause — prevention or corrected rule`. Create only this small index if no route exists and the error warrants a durable reminder. Keep this reference after issue closure if it remains useful; remove it when obsolete. **Do not copy issue timelines, logs, or full diagnoses into Agent/**.
5. Read that line when the same area or symptom recurs; fetch the full issue **only** if the line and current source are insufficient. Promote a detailed reusable case through `references/modules/error-memory.md` only when justified.

For ordinary meaningful work, reuse a task record if one is already provided or project policy demands it; **do not open or read issues merely for ceremony**. See `references/task-traceability.md` for the error lifecycle and `references/task-boundaries.md` only for a complex boundary.

## Workflow Routing

- **Product/engineering task:** apply the cheap Context Budget/Boundary Gate; load detailed task trace or boundary references only for confirmed errors, non-trivial cross-mode risks or genuine handoffs. Implement and validate the product request, not an agent-documentation audit.
- **Agent-context maintenance task:** use the foundation workflow below and load only evidence-backed modules. Context maintenance is not the default outcome of an engineering task.
- **Trivial repository work:** follow the startup and minimal-change rules briefly; no issue, matrix, or module merely for ceremony. **Non-repository questions:** the skill does not apply.

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

## Evidence And Completion Gate

**Never mark a task or example as fully validated based only on code edits, a plausibility argument, or written tests.** On every task, after implementation:

1. Re-read the applicable root/scoped `AGENTS.md`, the requested success criteria, changed files and relevant contracts. Compare actual diff to intended scope and inspect for omissions, regressions, duplicated effects, security risks and stale instructions.
2. Run the tests or manual checks actually available for the changed surface, including a positive behavior check, a negative restriction check where applicable, and adjacent regression checks. Record exact command/check, observed result, and what remains unrun. **No GitHub Actions** as a substitute for local/manual verification where forbidden by project policy.
3. **When presenting a UI, screenshot, visual demo, interaction or example:** actually launch/inspect the result and **capture a genuine screenshot** of what the agent observed, with the relevant tested state and, when useful, the test result. Share a path/link or attached evidence when the host supports it. Do not substitute mockups, generated images, repository screenshots, source code, or claimed appearances for actual runtime proof. For CLI/backend/document-only changes, preserve precise command output/commit evidence; also screenshot tested output if the user requires it and capture is supported.
4. If GUI/runtime access, screenshot capture, test execution, or other required evidence is unavailable, name the missing check, reason, residual risk, and next action. **Do not claim visual/E2E success, attach a fake screenshot, or close an issue whose necessary validation is outstanding.** Other successfully performed static checks may be reported as such.
5. Before the final response, ensure any confirmed agent mistake (including user correction of the agent's oversight) has its focused issue and one-line `Agent/error-memory/INDEX.md` prevention pointer. Keep open issues open when full verification is pending.

## Completion

Report the actual change, checks performed **with observed evidence**, screenshots where the applicable requirement was actually met, unverified risks, and issue/commit or next action. Never claim a test, screenshot, integration, or fresh-agent activation was executed when it was only described.

