# Foundation Principles

Read this reference when designing, auditing, compacting, or extending the repository's agent-facing context architecture.

Do not load it for a trivial known-file edit unless the task is specifically about agent documentation or context quality.

## Core Model

The foundation exists to minimize the total context cost of completing work correctly.

The goal is not to create the smallest possible documentation set and not to create the most complete possible documentation set.

The goal is to preserve the smallest amount of durable context that materially improves future decisions, routing, verification, or recovery.

## Minimum Viable Context

Every persistent instruction, summary, rule, memory entry, router entry, and generated document must justify its context cost.

Keep an item only when removing it would make a future agent materially more likely to:

- choose the wrong file or owner,
- violate a non-obvious project rule,
- repeat an expensive discovery step,
- repeat a known failure,
- miss a required verification step,
- misunderstand a stable contract or decision,
- lose meaningful task continuity.

Do not persist information that is cheap and reliable to infer from:

- source code,
- package metadata,
- formatter or linter configuration,
- obvious folder names,
- generated files,
- standard language or framework behavior,
- commands that are already discoverable from the repository without ambiguity.

When in doubt, prefer a pointer to the source of truth over a copied explanation.

## Progressive Disclosure

Context must be loaded in layers.

Preferred flow:

1. Read the active entrypoint.
2. Use the smallest router that can classify the task.
3. Load only the matching owner document.
4. Load supporting references only when the current phase requires them.
5. Read source code before implementation.
6. Load history or error memory only when evidence makes it relevant.

Routers route. They should not restate the documents they route to.

References should be one hop away from the document that names them when possible. Avoid chains where one router opens another router that opens another router without adding decision value.

Each optional document should make its load condition clear:

- when to read,
- when not to read,
- what question it answers,
- what document or source owns the detailed truth.

Splitting one large file into many files is not progressive disclosure if agents are still instructed to read all of them.

## Canonical Ownership

One durable fact, rule, contract, decision, or procedure should have one authoritative owner.

Other documents may point to that owner but should not copy the same detailed content.

Use this model:

- entrypoints establish global reading behavior,
- routers point to owners,
- owner documents explain one topic,
- source code owns implementation truth,
- project configuration owns machine-enforced rules,
- task records own work history,
- durable memory owns reusable verified learning.

When the same guidance exists in multiple places:

1. choose the authoritative owner,
2. keep the full rule there,
3. replace duplicates with short pointers,
4. remove stale copies.

Do not use duplicated prose as a synchronization strategy.

## Evidence-Based Structure Growth

Do not create a document, folder, memory category, checklist, summary, or tool merely because the template supports it.

Create it only when there is evidence that it reduces future cost or risk.

Evidence may include:

- repeated rediscovery,
- recurring mistakes,
- non-obvious ownership,
- repeated task routing,
- complex verification,
- stable project-specific constraints,
- a complex area that future work revisits,
- a recurring mechanical procedure,
- a meaningful durable decision,
- repeated handoff failures.

No evidence means no new module.

The correct foundation change may be to create nothing.

## Standard Entrypoints And Local Scope

Respect the repository's existing agent-instruction conventions before creating a new one.

If the repository uses `AGENTS.md`, nested `AGENTS.md` files, local README files, or another established agent entrypoint:

- preserve the established standard when it is valid,
- do not create a competing source of truth,
- use the root entrypoint for truly global guidance,
- use local scoped instructions for behavior that applies only to a subtree,
- treat the closest applicable scoped instruction as more specific than broad guidance unless the repository explicitly defines another precedence rule,
- use `Agent/` as routed supporting context when it adds value, not as a mandatory replacement for existing standards.

Global docs should not contain local exceptions that can live safely with the owning subtree.

## Context Budgets

Use context budgets as health signals, not universal hard limits.

Entry documents and routers should stay small enough to read frequently.

Topic documents may be larger when the topic genuinely requires it, but growth should trigger review.

A context audit should ask:

- Is this file still a router or has it become a manual?
- Are repeated headings or explanations consuming space without changing decisions?
- Can stable detail move behind a pointer?
- Would splitting the file reduce normal task cost?
- Would splitting it create excessive routing overhead?
- Is the content still current?
- Does another document already own the same truth?

A large file is not automatically wrong. A large default-read file requires strong justification.

## Knowledge Classes

Do not treat all repository knowledge as the same kind of memory.

Distinguish at least:

### Durable guidance

Stable project rules, contracts, ownership, verified procedures, and reusable decisions.

### Current state

Where ongoing work currently stands, temporary migration state, active rollout status, or current operational state.

### Task history

What a specific task attempted, decided, changed, verified, failed, or left incomplete.

### Observations

Unverified discoveries, hypotheses, suspicions, and one-time anomalies.

### Error knowledge

Verified recurring failure patterns, root causes, fixes, and prevention guidance.

Task history belongs in the project's work-tracking system. It must not be copied into durable memory merely because it happened.

## Knowledge Promotion

New information should move through explicit confidence states.

Recommended lifecycle:

`discovered -> candidate -> verified -> durable`

Use these meanings:

- discovered: observed during work but not yet trusted,
- candidate: potentially reusable and worth checking,
- verified: supported by source, test, reproducible behavior, user decision, or another authoritative anchor,
- durable: stable enough to guide future work.

Do not promote a hypothesis, failed attempt, temporary workaround, or unfinished implementation into durable guidance.

When durable knowledge stops being valid, move it through:

`durable -> challenged -> superseded or retired`

Do not silently leave contradictory guidance active.

## Consolidation And Forgetting

Memory must be maintained by consolidation, not accumulation.

When new verified knowledge overlaps existing memory:

- merge duplicate lessons,
- update the canonical owner,
- mark replaced guidance as superseded or remove it,
- preserve only the historical pointer needed to understand a relevant migration or decision,
- delete stale detail that no longer improves future decisions.

A memory system that only appends will eventually become a context problem.

## Staleness And Reverification

Durable knowledge should include source anchors when its correctness depends on files, symbols, commands, schemas, configuration, or external contracts.

Useful anchors include:

- file paths,
- symbols,
- schema names,
- configuration keys,
- exact commands,
- issue or decision identifiers,
- test names.

Use a `last reviewed` or equivalent marker only when it adds real maintenance value.

When the anchored source changes materially, treat dependent memory as potentially stale and reverify it before using it for a high-impact decision.

Do not add metadata fields mechanically to every note. Metadata must pay for itself.

## Optimize Total Task Cost

Do not optimize only for the number of tokens in the initial read.

Over-compression can remove the anchors an agent needs and force repeated repository discovery.

Preserve compact, high-value anchors that prevent expensive rediscovery, especially:

- owner paths,
- entrypoints,
- important symbols,
- exact verification commands,
- stable contracts,
- unresolved risks,
- current handoff point for active work.

Evaluate context by total cost to complete the task correctly:

`reading + discovery + corrections + verification + recovery`

A slightly larger document can be cheaper overall when it prevents repeated exploration or mistakes.

## Project Maps Should Localize Work

A project map should help an agent answer:

- Where does this behavior enter the system?
- Which file or component owns it?
- Which boundaries or dependencies matter?
- Where should a change normally be made?
- What should not be modified for this task?
- What verification surface belongs to this area?

Do not turn `project-map.md` into a copied source tree.

Prefer owners, entrypoints, boundaries, and high-value anchors.

## Exact Verification Guidance

Verification instructions are high-value context only when they are exact.

Prefer:

- exact command,
- affected package or workspace,
- relevant test file or suite,
- environment or prerequisite,
- what success proves,
- what remains unverified.

Avoid generic guidance such as "run tests" when the repository can provide a more precise route.

Never invent a verification command to make documentation look complete.

## Context Degradation Audit

Audit the foundation for these failure modes:

### Distraction

Too much irrelevant context is loaded for common tasks.

Signals:

- large mandatory reads,
- giant templates,
- broad manuals,
- unrelated error history.

### Confusion

The agent cannot tell which route or owner applies.

Signals:

- too many overlapping routers,
- vague "read when" rules,
- ambiguous ownership,
- excessive nesting.

### Clash

Two active documents give different instructions about the same thing.

Signals:

- duplicated rules,
- incompatible commands,
- different owners claiming authority.

### Poisoning

Stale or incorrect context continues influencing work.

Signals:

- old paths,
- retired architecture,
- superseded fixes,
- obsolete commands,
- temporary workarounds presented as durable rules.

### Lost Critical Context

Compaction removed the details required to resume or act correctly.

Signals:

- missing owner paths,
- missing symbols,
- missing verification,
- missing current task state,
- repeated rediscovery after handoff.

A context-health review should identify the failure mode before adding more documentation.

## Local Knowledge Placement

Put reusable knowledge as close as practical to the owner that benefits from it.

Use:

- local `AGENTS.md` or equivalent for scoped operating instructions,
- local `README.md` for human-and-agent knowledge that belongs with a component or folder,
- `Agent/summaries/` for cross-cutting agent-only summaries,
- `Agent/tools/` for reusable procedures and scripts,
- `Agent/error-memory/` for verified recurring failures,
- project rules for truly project-wide operating constraints,
- task tracking for work history.

Do not move local knowledge into a global document merely because the global file is easier to find.

## External Material And Imported Patterns

Concepts may be adapted into the foundation, but external executable material must be reviewed before use.

Before importing scripts, hooks, commands, templates with executable behavior, or automation:

- inspect what it reads and writes,
- inspect shell or network actions,
- check secret and credential handling,
- check dependency and supply-chain risk,
- remove instructions that do not belong to the local project.

Import ideas deliberately. Do not inherit behavior blindly.

## Foundation Review Questions

Before adding durable context, ask:

1. What future decision will this improve?
2. Is the information expensive or risky to rediscover?
3. Is there already a canonical owner?
4. Can a pointer replace copied prose?
5. Is the knowledge verified?
6. Is it durable, current state, task history, or only an observation?
7. What source anchors support it?
8. What would make it stale?
9. Does it belong globally or closer to a local owner?
10. Is creating no new document the better result?
