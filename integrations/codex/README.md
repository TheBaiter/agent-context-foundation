# Agent Context Foundation v3 — Codex integration (opt-in)

This integration translates lessons from Superpowers' host bootstrap, Beads' reproducible setup/diagnosis, Claude-Mem's capture→persist→recall lifecycle and ECC's verified-learning promotion into a **project-owned Markdown memory** design. No external service, session archive, database, network calls, or automatic Git push.

## Install in one trusted repository (do not roll out everywhere yet)

The skill itself must be installed separately through the host's supported skill mechanism. For Codex, while this work remains on the feature branch, **install from that branch's local checkout** rather than the default `main`:

```sh
# From the target repository, point to the source checkout on this branch:
npx skills add /path/to/agent-context-foundation -a codex
npx skills ls -a codex
```

From an **Agent Context Foundation source checkout** (this repository, branch `feat/always-on-agent-context-v3`):

```sh
python3 integrations/codex/setup.py --project /path/to/target --install --dry-run
python3 integrations/codex/setup.py --project /path/to/target --install
python3 integrations/codex/setup.py --project /path/to/target --check
# To remove only the managed bridge/hooks, retaining project memory:
python3 integrations/codex/setup.py --project /path/to/target --uninstall
```

On Windows use `py -3` instead of `python3` for the setup command. The target must be an existing trusted project folder with a Git checkout to use Git change checks. The setup script uses only Python standard library; it **does not install Python or Node**, manage global paths, download dependencies or modify `.gitignore`. Install the skill as shown above before believing the runtime can select it.

**What setup changes:** merges a uniquely marked section into existing `AGENTS.md`, ensures minimal `Agent/README.md`, `Agent/INDEX.md`, `Agent/error-memory/INDEX.md` when absent, installs one script at `.codex/hooks/agent_context_hook.py`, and merges its own handlers into `.codex/hooks.json`. Other instructions, hooks, indexes and pending memory are preserved. Repeat installation is idempotent. A pre-existing modified script, malformed JSON, symlinked destination or ambiguous markers causes a safe failure instead of overwriting. The separate source repo's `.codex/hooks.json` is a **pilot for that repository only**. Don't enable both project and global copies of the same adapter, or duplicate closeout reminders will occur.

After installation, open a **fresh Codex session** in the target repository and inspect `/hooks`. Local hook configuration must be **trusted/enabled**; a file in Git is not automatic authorization to execute code. Doctor output checks local files/handlers, **not** the host's trust state or actual skill selection. Validate an ordinary task without naming the skill. On Windows, verify `py -3`, PowerShell quoting and `git` in a real Windows Codex process (not emulated here).

## Behavior and limits

| Event | Action | Guarantee/limit |
| --- | --- | --- |
| SessionStart (including compact/resume/fork) | Adds a short pointer to project instructions and relevant memory | Context injection only; cannot prove files were actually read |
| UserPromptSubmit | Repeats short context reminder; stores an opaque per-turn snapshot of Git and pending-memory fingerprint | Heuristic identifies certain Spanish/English user-correction phrasing; saves **boolean only**, not prompt text |
| SubagentStart | Injects same short route for delegated agents | Subagent behavior depends on host/permissions |
| Stop | When project changed **or** an apparent user correction was not recorded, requests one bounded follow-up review | Advisory. `stop_hook_active` and one-use marker prevent endless retries; no automatic semantic proof of tests or error capture |

Snapshots are kept inside the project's `.agent-temp/agent-context-foundation/`, not in system-temp or user home. They contain Git fingerprints, pending-file hash and a correction-intent boolean. They do not store user prompts, assistant transcripts, tool outputs, tokens or secrets. A crash before Stop may leave an orphan snapshot; clean stale adapter-owned files when sessions have ended. Treat `.agent-temp` as disposable and choose Git ignore policy intentionally.

**Important:** Git changes are not the same as meaningful mistakes, and no Git changes does not imply no mistakes. The correction heuristic is intentionally conservative: it can miss wording or produce false positives. A `Stop` continuation only asks the agent to review and, if warranted, write memory. If writing is blocked, the agent must disclose the blocker. Nothing in hooks guarantees compliance in untrusted hosts or across every tool path.

## How to verify without GitHub Actions

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s integrations/codex/tests -v
```

Local tests check installer idempotence, hooks coexistence, safe uninstall, symlink/malformed-config refusal, correction prompt privacy, dirty-worktree change detection, bounded continuation, plan mode and stdin/stdout JSON. They are **not** Codex E2E tests. See `../../evals/host-acceptance.md` for session-level acceptance. Do not mark the epic as complete until the real Codex host (including Windows) passes it.

## Source/credit and why not direct code reuse

- [Superpowers](https://github.com/obra/superpowers) supplies the architectural example of host-specific bootstrap and compact skill instruction routing. We adapt the idea rather than copying their launcher.
- [Beads agent/IDE setup](https://github.com/gastownhall/beads/blob/main/docs/getting-started/ide-setup.md) separates reproducible installation and `--check` diagnosis from runtime behavior.
- [Claude-Mem hooks](https://github.com/thedotmack/claude-mem/blob/main/docs/public/architecture/hooks.mdx) demonstrates separate lifecycle capture and next-session retrieval. We deliberately store only project Markdown and no raw conversation or worker database.
- [Everything Claude Code](https://github.com/affaan-m/ECC) describes persistent error/pattern learning; we promote only verified prevention and avoid opaque automatic rules.
- [Codex official hooks](https://learn.chatgpt.com/docs/hooks) govern actual event JSON and trust. Host semantics take precedence over this README.
