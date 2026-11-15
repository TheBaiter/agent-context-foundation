# Agent Context Foundation repository instructions

For **every** repository engineering, review, documentation, skill or maintenance task in this repository:
1. Read this root `AGENTS.md` and the relevant `SKILL.md` rules before changes. Read `Agent/README.md` and `Agent/INDEX.md` to locate only task-relevant project context; skim the compact `Agent/error-memory/INDEX.md` and `PENDING.md` (if present) once; open matching details only.
2. Follow existing instructions and choose the smallest **complete** safe change. Do not replace scoped rules or invent a universal Git policy.
3. Briefly record meaningful mistakes, including user corrections, in project-owned `Agent/error-memory/PENDING.md` when they happen. Continue safe work; before closing review all pending errors, validate fixes, consolidate verified prevention into the short `INDEX.md`, and link appropriate issue/task evidence. Keep unverified errors pending.
4. Before demonstrating, claiming success or closing: re-read the affected change and acceptance criteria, verify actual behavior and adjacent regressions, and report exact tests and results. For visual/runtime work, provide genuine screenshots of the observed output/tests when capture is available; otherwise state what could not be visually checked. Never fabricate evidence or claim unrun tests passed.
5. Keep screenshots and disposable artifacts in the project's temporary workspace, not arbitrary directories; keep durable issue/commit evidence in its canonical owner. Respect the project's choice of Git-tracked or gitignored local memory; never alter `.gitignore` automatically. Do not use GitHub Actions.

If a required check cannot run, leave that verification explicitly pending and do not represent it as passed.