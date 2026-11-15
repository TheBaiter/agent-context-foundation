#!/usr/bin/env python3
"""Optional Codex lifecycle adapter for Agent Context Foundation.

Use only after reviewing and trusting the project hooks. No prompts, transcripts,
secrets or remote requests are written. Turn snapshots are disposable and local.
"""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

MAX_INPUT_BYTES = 65_536
MAX_CONTEXT_CHARS = 1_200


def project_root(cwd: object) -> Path | None:
    if not isinstance(cwd, str) or not cwd:
        return None
    current = Path(cwd).resolve()
    if not current.is_dir():
        return None
    for candidate in (current, *current.parents):
        if (candidate / "AGENTS.md").is_file() and (candidate / "Agent" / "INDEX.md").is_file():
            return candidate
    return None


def repo_state(root: Path) -> str | None:
    """Git snapshot for advisory change detection, not a proof of correctness."""
    try:
        head = subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=root, text=True,
            capture_output=True, timeout=3, check=True,
        ).stdout.strip()
        status = subprocess.run(
            ["git", "status", "--porcelain=v1", "--untracked-files=normal"],
            cwd=root, text=True, capture_output=True, timeout=5, check=True,
        ).stdout.splitlines()
    except (OSError, subprocess.SubprocessError):
        return None
    # Our own snapshot must never make the worktree appear dirty.
    tracked = [line for line in status if not line[3:].startswith(".agent-temp/")]
    return hashlib.sha256((head + "\n" + "\n".join(tracked)).encode("utf-8")).hexdigest()


def marker_path(root: Path, data: dict) -> Path | None:
    session, turn = data.get("session_id"), data.get("turn_id")
    if not isinstance(session, str) or not isinstance(turn, str) or not session or not turn:
        return None
    token = hashlib.sha256((session + "\x00" + turn).encode("utf-8")).hexdigest()[:32]
    return root / ".agent-temp" / "agent-context-foundation" / (token + ".json")


def context(root: Path) -> str:
    base = (
        "Agent Context Foundation (Codex lifecycle hook): Read the project's "
        "AGENTS.md and Agent/README.md + Agent/INDEX.md before repository work. "
        "Check the short Agent/error-memory/INDEX.md and PENDING.md for relevant "
        "mistakes. On meaningful agent errors, including user corrections, append "
        "a brief project-owned PENDING entry immediately; keep working safely. "
        "At closeout review, verify and consolidate lessons. Do not pretend the "
        "SKILL.md was selected unless it was actually loaded."
    )
    pending = root / "Agent" / "error-memory" / "PENDING.md"
    if pending.is_file():
        base += " Unresolved project memory exists at Agent/error-memory/PENDING.md."
    return base[:MAX_CONTEXT_CHARS]


def run(data: dict) -> dict:
    event = data.get("hook_event_name")
    if event not in {"SessionStart", "UserPromptSubmit", "SubagentStart", "Stop"}:
        return {}
    root = project_root(data.get("cwd"))
    if root is None:
        return {}
    if event in {"SessionStart", "UserPromptSubmit", "SubagentStart"}:
        if event == "UserPromptSubmit" and data.get("permission_mode") != "plan":
            marker = marker_path(root, data)
            state = repo_state(root) if marker else None
            if marker and state is not None:
                try:
                    marker.parent.mkdir(parents=True, exist_ok=True)
                    marker.write_text(json.dumps({"git_state": state}) + "\n", encoding="utf-8")
                except OSError:
                    pass  # Never block the user's prompt due to optional bookkeeping.
        return {"hookSpecificOutput": {"hookEventName": event, "additionalContext": context(root)}}
    if data.get("permission_mode") == "plan" or data.get("stop_hook_active") is True:
        return {}
    marker = marker_path(root, data)
    if marker is None or not marker.is_file():
        return {}
    try:
        baseline = json.loads(marker.read_text(encoding="utf-8")).get("git_state")
        marker.unlink()  # At most one continuation per turn, no infinite Stop loops.
    except (OSError, ValueError, TypeError):
        return {}
    now = repo_state(root)
    if baseline and now and baseline != now:
        return {
            "decision": "block",
            "reason": (
                "Agent Context Foundation closeout gate: repository Git state changed "
                "during this turn. Before finalizing, re-read the diff and task "
                "requirements, run feasible regression checks, and review errors "
                "recorded in project Agent/error-memory/PENDING.md. Persist meaningful "
                "user/agent corrections and consolidate only verified preventive "
                "lessons. Report exact tests and remaining blockers. If already "
                "done, briefly confirm the real evidence and finish."
            ),
        }
    return {}


def main() -> None:
    try:
        raw = sys.stdin.buffer.read(MAX_INPUT_BYTES + 1)
        if len(raw) > MAX_INPUT_BYTES:
            raise ValueError("oversize hook input")
        data = json.loads(raw)
        output = run(data) if isinstance(data, dict) else {}
    except (ValueError, OSError, UnicodeError):
        output = {}  # Fail open; never replace ordinary user work with a hook crash.
    sys.stdout.write(json.dumps(output, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
