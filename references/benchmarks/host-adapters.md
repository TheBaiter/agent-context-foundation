# Lessons adapted from other agent systems

Scope: [epic #13](https://github.com/TheBaiter/agent-context-foundation/issues/13). Read only while working on host integration or memory workflows.

| Project | Documented difference | Adaptation | Not adopted |
| --- | --- | --- | --- |
| [Superpowers](https://github.com/obra/superpowers) | Host startup hooks inject skill router | Codex-specific bootstrap and compact context | Copying their launcher or all skills verbatim |
| [Beads](https://github.com/gastownhall/beads/blob/main/docs/getting-started/ide-setup.md) | CLI setup, check, prime and durable memory | Idempotent project integration and doctor | Replacing GitHub issues or requiring its database |
| [Claude-Mem](https://github.com/thedotmack/claude-mem/blob/main/docs/public/architecture/hooks.mdx) | Capture→processing→recall at session lifecycle events | Project PENDING → verified INDEX → relevant next-session retrieval | Raw transcripts, local worker, SQLite by default |
| [Everything Claude Code](https://github.com/affaan-m/ECC) | Hooks plus learning from observed patterns | Promote only evidenced preventive checks and retire stale knowledge | Auto-promote speculative rules |
| [Codex Hooks](https://learn.chatgpt.com/docs/hooks) | Trust and lifecycle event/output schemas | Match official SessionStart/UserPromptSubmit/SubagentStart/Stop | Claiming all hosts share the same API |

These comparisons identify **mechanisms, not proven success rates**. A trusted hook can inject context; semantic obedience and actual skill selection require host-level tests. No host-independent promise of automatic invocation.
