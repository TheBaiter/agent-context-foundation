# Pending agent failures and verification

Keep this file short. Entries are unresolved observations, not proof of a completed fix. Revisit at task start; consolidate verified prevention to INDEX.md and the linked issue.

- 2026-11-14 | [#12](https://github.com/TheBaiter/agent-context-foundation/issues/12) | **Implicit activation / installation drift**: user reports ignored Agent/ rules and unrecorded corrections. Source inspection found outdated vendored copies in Document-design and Imagine-IT (same old SKILL.md blob), while Mini-ERP's skills-lock.json does not list this skill. The central skill and target-project standing AGENTS bridges were improved. **Still pending**: update/verify installed skill packages and global Codex scope, then run fresh-session implicit-selection, user-correction persistence, cross-session retrieval and closeout tests in a real agent host. Do not call this runtime-verified.
