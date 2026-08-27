# Foundation Principles

Read when designing, auditing, or changing the repository's agent-context architecture.

Do not load this reference for ordinary feature work.

## Goal

Minimize the total cost of completing work correctly:

`reading + discovery + correction + verification + recovery + handoff`

The smallest document is not automatically the best document. Preserve compact anchors that prevent expensive rediscovery.

## Minimum Viable Context

Persist information only when removing it would materially increase the chance of:

- choosing the wrong owner,
- violating a non-obvious rule,
- repeating expensive discovery,
- repeating a known verified failure,
- missing required verification,
- losing task continuity.

Do not persist information that source code, configuration, tooling, or obvious repository structure already exposes cheaply and reliably.

## Progressive Disclosure

Use:

`entrypoint -> router -> owner -> supporting reference`

Each layer should answer a decision the previous layer could not.

A router points; it does not duplicate the destination.

Splitting a large file into many files is not progressive disclosure if agents still load all of them.

## Canonical Ownership

One durable truth has one owner.

Typical ownership:

- source/configuration: implementation truth,
- global/local instruction files: operating rules,
- project map: localization,
- project rules: cross-project constraints,
- planning docs: durable planning conventions,
- task system: task chronology and current execution state,
- error memory: verified reusable failures,
- summaries: cross-cutting expensive rediscovery,
- tools: reusable procedures.

When duplicates exist, choose the owner and replace copies with pointers.

## Evidence-Based Growth

A supported module is not a required module.

Create a module only when evidence shows it reduces future cost or risk, such as repeated rediscovery, recurring mistakes, non-obvious ownership, durable constraints, or repeated fragile procedures.

No evidence means no module.

## Scope

Preserve existing agent standards when valid.

Global guidance should contain only global rules. Put subtree-specific guidance close to the owning subtree.

More specific local guidance should not be copied into global docs.

## Knowledge Classes

Distinguish:

- durable guidance,
- current state,
- task history,
- observations,
- recurring error knowledge.

Do not promote task chronology or hypotheses into durable docs.

## Promotion And Retirement

Use:

`discovered -> candidate -> verified -> durable`

Promote only with evidence such as source inspection, reproducible behavior, exact tests, authoritative documentation, or explicit project decisions.

When durable knowledge becomes unreliable:

`durable -> challenged -> superseded or retired`

Do not keep contradictory guidance active.

## Staleness

Use compact source anchors when correctness depends on changing implementation:

- paths,
- symbols,
- test names,
- commands,
- schema/config identifiers,
- decision or issue identifiers.

When an anchor changes materially, reverify dependent guidance before using it for high-impact decisions.

Do not add metadata mechanically when it has no maintenance value.

## Context Health

Diagnose before adding documentation:

- distraction: too much irrelevant default context,
- confusion: unclear route or owner,
- clash: contradictory active rules,
- poisoning: stale context still influencing work,
- lost critical context: compaction removed paths, symbols, verification, or handoff anchors.

Fix the failure mode rather than layering more context on top.

## Language And Encoding

Preserve the repository's established language and encoding.

Default to UTF-8 when no explicit constraint exists.

Use ASCII-only only when an actual toolchain, terminal, integration, or portability requirement justifies it.

## Verification

Verification guidance is valuable only when exact.

Prefer:

- exact command or check,
- affected package/workspace,
- relevant test/suite,
- prerequisite,
- what success proves,
- what remains unverified.

Never invent a command to make documentation look complete.

## External Material

Ideas may be adapted. Executable material must be reviewed before import.

Inspect scripts, hooks, commands, network behavior, writes, dependencies, permissions, and secret handling before adoption.

## Review Questions

Before adding durable context, ask:

1. What future decision will this improve?
2. Is it expensive or risky to rediscover?
3. Does an owner already exist?
4. Can a pointer replace copied prose?
5. Is it verified?
6. Is it durable knowledge or task history?
7. What would make it stale?
8. Does it belong globally or locally?
9. Would no new documentation be better?
