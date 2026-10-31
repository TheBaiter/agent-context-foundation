# Task Boundaries And Scope Re-Anchoring

Read this reference for substantive tasks whose outcome depends on multiple modes, permissions, integration points, issue decisions, or data lifetime. `SKILL.md` owns the lightweight mandatory gate; this file owns its deeper method. Do not turn this into an indiscriminate checklist for trivial edits.

## 1. Recover the *current* contract, not a remembered one

At task start, after each material user correction, and before final validation:

1. State the requested outcome in one sentence. Identify the authoritative existing task/issue before creating another. Read its current body **and** newest substantive updates/comments, linked dependencies and related work items. Do not use chat continuity, an old plan, or the latest commit alone as proof of product intent.
2. Inspect local active instructions (`AGENTS.md`, scoped instructions, `Agent/README.md` or its actual project equivalent), contracts and the code paths that implement the requested behavior. Read only enough to establish ownership and effects.
3. Classify statements as **explicit current requirement**, **verified current behavior**, **historical/superseded decision**, **proposed solution**, or **unverified assumption**. Compare dates, explicit overrides and issue status. A comment created later is evidence, not automatic authority over a current explicit requirement. If sources conflict, do not silently choose the more restrictive or convenient implementation; record the conflict, resolve through explicit project/user direction where available, and isolate undecidable work.
4. Record the exact issue/commit/source anchors used so a later agent can recheck them. Track related issues as dependencies; reuse the primary issue unless the discovered defect is independently scoped and cannot be tracked there.

Do not interpret an issue as completed, nor a feature as implemented, merely because a plan, prototype, source branch, or comment describes it.

## 2. Build a small boundary contract

Make a compact matrix in the active task record, only for affected surfaces:

| Dimension | Questions to answer |
| --- | --- |
| Actor and mode | Guest, logged-in, admin, test, legacy? Feature flags ON/OFF? |
| Capability and operation | View catalog, edit, connect, execute query, export, save, import, delete? Explicit positive, negative, unchanged, deferred cases? |
| Identity/permission | Does it need **app** login? Different **external provider** credentials? Authorization or ACL per operation? |
| Read/write and effects | Local-only edit, authorized remote GET/SELECT, mutation, backend access, rate-limit cost, third-party logs? |
| Persistence/lifetime | Memory for this operation/tab, local file/browser draft, account cloud DB, vault, telemetry, exported data? |
| Owners/dependencies | UI, API handler, middleware, integration adapter, security control, serializer, relevant issue/test? |
| Phase | Explore, plan, implement, verify, deploy? What gate blocks only a particular phase or surface? |

Require a positive allowance for desired behavior, not only a list of prohibitions. **No app account** does not imply **no external authentication**, **no access to a catalog**, or **no temporary queries**. **No product DB persistence** does not imply **no external reads** or **no network side effects**. Conversely, visibility of a UI option does not authorize a backend operation, bypass ACL, disclose data, or approve an unreviewed proxy.

Record in scope, out of scope, dependencies, safe defaults, and assumptions. When a dependency is missing, distinguish *specification authorized*, *implemented*, *verified*, and *released*.

## 3. Follow the capability through boundaries

Before changing a guard or hiding an action, trace the user-visible operation through:

`UI -> client state -> API/middleware -> authentication/authorization -> integration -> storage/export -> tests`.

Check which step actually requires an identity, persistent storage, external credentials, rate limiting or security isolation. Fix the narrowest owner that violates the requested contract. Do not globally gate a catalog because saving requires a session; do not remove a temporary integration because cloud credentials are unavailable; do not enable private provider endpoints merely to make a guest UI pass.

For guest or public execution, use only explicitly authorized operations and a safely bounded backend: no credential reuse from other accounts, no arbitrary internal network access, no secret persistence, and applicable abuse/egress limits. If safety cannot be demonstrated, leave execution blocked with an explicit tracked dependency while maintaining unrelated permitted UI/offline capabilities.

When there is an option between quick workaround and coherent repair, compare: required capability, security consequence, affected modes, dependency state, regression surface and verification cost. Choose the smallest change that satisfies the **entire** acceptance contract, not simply the easiest guard to edit.

## 4. Challenge the scope before implementing

- **Too narrow:** fixes a button but misses its API, guard, import/export or source adapter.
- **Too broad:** disables a whole feature family, adds account/login or persistence as a side effect, rewrites unrelated contracts or deletes future architecture.
- **Outdated:** follows a superseded comment, already closed phase or obsolete implementation assumption.
- **Premature:** treats planned integration as shipped, test authored as passed, or deploy blocked as a ban on implementing an authorized change.
- **Unsafe:** interprets public UX as permission to bypass server authorization, expose secrets or run arbitrary remote queries.

For material changes, put the selected alternative, rejected alternatives and why in the authoritative issue. Update that decision if the current user instruction or source evidence changes it.

## 5. Prove both permission and prohibition

At least four kinds of checks belong in non-trivial acceptance criteria:

1. **Positive:** every explicitly permitted operation still works in its intended mode, even when no app session or product DB exists, if that is the contract.
2. **Negative:** forbidden persistence, login enforcement, private access, unsafe remote methods and unauthorized side effects do not occur.
3. **Regression:** flag OFF / signed-in / legacy / adjacent workflows retain their prior behavior. Test server enforcement as well as UI affordances when relevant.
4. **State/lifecycle:** restart, reload, stale cookies, switching origin, loading saved files, failed query, missing dependency and feature status do not accidentally persist sensitive data or turn a planned integration into a false success.

Tests must distinguish **written**, **executed**, **passed**, and **not executed**. A locally unavailable test should be authored where possible, anchored in the issue with exact command and expected result, and marked for manual execution if required by the project. Do not use GitHub Actions when project policy prohibits them. Never claim production readiness based on source review alone.

Re-read the task boundary and inspect the final diff in a fresh review pass; challenge over-restrictions and missing adjacent surfaces. If a regression or material failed approach is discovered, preserve evidence and next action in the authoritative issue. Promote to `Agent/error-memory/` only verified, reusable failure patterns after they have independent durability; do not mirror active problem history.

## 6. Example: guest editor with temporary data

**Illustrative boundary, not a universal product requirement:**

| Operation | Guest without app login | Persistence | Required protection |
| --- | --- | --- | --- |
| View editor and available data-source options | Allowed | None | Do not silently hide catalog |
| Edit static document and export local artifact | Allowed | Local/on-demand only | Do not call cloud save |
| Configure/probe an external source | Permitted *only if expressly specified and safe implementation exists* | Ephemeral operation/tab | User-supplied external authorization; server-side safety, quota, no borrowed session |
| Use account library or saved cloud connections | Denied | No product-account writes | Enforce on server, not UI alone |
| Existing authenticated mode | Preserve existing contract | Existing policy | Regression checks |

The error is to infer from *no account or internal DB* that every data catalog, connector and externally authorized request must be disabled. The opposite error is to open existing authenticated provider endpoints to guests without isolation. Either inference violates the boundary.

## Completion and handoff

Leave the authoritative issue with: current allowed/denied/deferred matrix or compact equivalent; decisive issue/source anchors; implementation and dependency state; actual test results versus pending checks; detected regressions or risks; next action. An incomplete security or PC-test gate blocks only the claims/phases that depend on it, never justifies silently changing user requirements or declaring success. Do not keep this active history in reusable agent context.
