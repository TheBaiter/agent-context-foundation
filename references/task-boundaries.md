# Task Boundaries And Scope Re-Anchoring

Load this only when multiple modes, permissions, integrations, or data lifetimes create a real ambiguity or regression risk. The default lightweight gate is in `SKILL.md`. Do not spend more context reconstructing the project than the task requires.

## 1. Recover only the missing decision

Start from the current user request, session context and directly affected source/contracts. Read local agent instructions through the project's existing short entrypoint, not every instruction file.

Read an issue **only when** the user cites its number, a relevant error-memory line points to it and details are needed, an unresolved contract depends on it, or evidence conflicts. Fetch the one known issue first. Read its most relevant decision/comment only if needed; follow related issues selectively. Do not browse all issues, full histories or unrelated branches as a preflight.

Classify an important statement as current explicit requirement, observed behavior, superseded decision, proposal, or assumption. Source truth confirms implementation, not always intended behavior; explicit current user requirements can supersede older issue decisions. If the task is clear without an issue, proceed.

Keep the essential scope/owner/evidence in the existing task or a compact working note; do not produce a standing matrix or new issue for a straightforward modification.

## 2. Build a small boundary contract

For a genuinely cross-mode change, use a compact matrix in the existing task record or working context, only for affected surfaces:

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

For material tracked changes, keep the decisive trade-off in the existing authoritative task. Create an error issue only when a concrete agent mistake or defect needs correction, not for every alternative considered.

## 5. Prove both permission and prohibition

At least four kinds of checks belong in non-trivial acceptance criteria:

1. **Positive:** every explicitly permitted operation still works in its intended mode, even when no app session or product DB exists, if that is the contract.
2. **Negative:** forbidden persistence, login enforcement, private access, unsafe remote methods and unauthorized side effects do not occur.
3. **Regression:** flag OFF / signed-in / legacy / adjacent workflows retain their prior behavior. Test server enforcement as well as UI affordances when relevant.
4. **State/lifecycle:** restart, reload, stale cookies, switching origin, loading saved files, failed query, missing dependency and feature status do not accidentally persist sensitive data or turn a planned integration into a false success.

Tests must distinguish **written**, **executed**, **passed**, and **not executed**. A locally unavailable test should be authored where possible, anchored in the issue with exact command and expected result, and marked for manual execution if required by the project. Do not use GitHub Actions when project policy prohibits them. Never claim production readiness based on source review alone.

Recheck the requested boundary and inspect the final diff; challenge over-restrictions and missing adjacent surfaces. For a confirmed agent-caused regression, create/reuse its issue, record root cause and fix/verification, close only after validation, and leave a one-line `Agent/error-memory/INDEX.md` reference. A detailed memory case is optional and must be verified, not copied from issue history.

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

If an issue is involved, leave its decision/verification/handoff concise and accurate; otherwise report the essential result without creating a tracker entry. An incomplete security or PC-test gate blocks only claims/phases that depend on it. Never store active issue histories in reusable agent context; a one-line error pointer is enough.
