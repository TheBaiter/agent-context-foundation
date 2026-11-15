# Pending agent failures and verification

Keep this file short. Entries are unresolved observations, not proof of a completed fix. Revisit at task start; consolidate verified prevention to INDEX.md and the linked issue.

- 2026-11-14 | [#12](https://github.com/TheBaiter/agent-context-foundation/issues/12) | **Activation still not runtime-verified**: source contract and all three project standing bridges improved; vendored skill packages in Document-design and Imagine-IT updated, and package added to Mini-ERP. All three contain the same 27 source blobs and corresponding v1 lock hash (static PASS). **Pending**: user's actual local/global Codex installations or checked-out workspaces may still be stale; test a fresh real host session for implicit activation, immediate user-correction capture, cross-session retrieval and end-of-task consolidation. Host selection is not enforceable by SKILL.md alone; do not claim E2E PASS.

## Codex native hooks pilot — 2026-11-15

- [#12](https://github.com/TheBaiter/agent-context-foundation/issues/12): Codex lifecycle adapter and **local repo pilot config** added to main; 11 local Python unit tests passed. Hook script blob matches tested local source. Official Codex hooks require project trust and separate `/hooks` trust. **Unverified**: actual Windows/PowerShell command, Codex hook execution, implicit skill selection and real agent corrections across sessions. Do not sync this pilot to downstream projects or close the issue until host checks pass.
