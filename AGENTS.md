# Agent Context Foundation repository instructions

For **every** repository engineering, review, documentation, skill or maintenance task in this repository:
1. Read this root `AGENTS.md` and the relevant `SKILL.md` rules before changes. Read `Agent/README.md` and `Agent/INDEX.md` to locate only task-relevant project context; consult matching error-memory pointers, not all issues or histories.
2. Follow existing instructions and choose the smallest **complete** safe change. Do not replace scoped rules or invent a universal Git policy.
3. Treat confirmed agent mistakes (including user-discovered oversights, unsupported assumptions and regressions) as errors to correct and trace: one focused issue for the failure and one short preventive pointer in `Agent/error-memory/INDEX.md`.
4. Before demonstrating, claiming success or closing: re-read the affected change and acceptance criteria, verify actual behavior and adjacent regressions, and report exact tests and results. For visual/runtime work, provide genuine screenshots of the observed output/tests when capture is available; otherwise state what could not be visually checked. Never fabricate evidence or claim unrun tests passed.
5. Keep screenshots and disposable artifacts in the project's temporary workspace, not arbitrary directories; keep durable issue/commit evidence in its canonical owner. Do not use GitHub Actions.

If a required check cannot run, leave that verification explicitly pending and do not represent it as passed.