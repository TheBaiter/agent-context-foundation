# Project-Owned Error Memory

Read for a meaningful mistake, a user correction or relevant recurring failure. **Memory is stored in files in the project**, not a model's chat history. The repository decides whether files are Git-tracked/shared or gitignored/local-only. Never silently alter `.gitignore` or publish private content.

## Minimum On-Disk Structure

```text
Agent/error-memory/
  INDEX.md       # short, verifiable lessons and pointers
  PENDING.md     # optional, created on first unreviewed meaningful mistake
```

Reuse established equivalent routes. No empty categories or duplicated error systems.

## Task-Start Gate

Skim the small `INDEX.md` and `PENDING.md` entries once; retrieve only relevant detailed issues/cases. If the index grows, route by area without preloading all histories. A task started by a different agent/model must be able to find the same guidance.

## During Task (Fast Capture)

For each meaningful agent mistake, including a user-discovered ignored instruction or missed requirement, append one concise note to `PENDING.md`: area/task, observed symptom, detection/evidence, immediate risk, next check. Identify unknown causes as unknown. Do not wait for the final response or assume chat memory will persist. Continue safe work; do not interrupt with issue creation for every incident. Skip harmless transient retries. Redact secrets.

## Mandatory Closeout (Learning)

1. Review the task's pending notes even without a reminder; group duplicates by cause and distinguish errors from changed preferences.
2. Repair and run actual behavior/regression checks where possible. If unavailable, label the fix and verification pending.
3. Promote a **verified reusable** lesson as one short `INDEX.md` line with area, cause/symptom, preventive check and issue/task/test anchor. Maintain detailed evidence in the task/issue. Reuse/create a focused issue when independently actionable or required by project policy; not for every minor error.
4. Mark consolidated entries resolved/remove them only after transfer; retain unresolved notes and next action. Supersede obsolete or phase-expired rules based on current evidence.
5. Report what was persisted, the tests actually observed and what remains open.

Gitignored local memory survives sessions in the same workspace but not a fresh clone; Git-tracked memory becomes cross-project-copy/shared only after appropriate commit/push. If filesystem write is blocked, say so; do not claim a model will remember on its own.
