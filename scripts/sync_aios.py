#!/usr/bin/env python3
"""Run local AI-OS sync readiness checks and print sync guidance."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys


CHECKS = [
    "scripts/check_project_instructions_length.py",
    "scripts/check_repo_public_safety.py",
    "scripts/check_codex_goal_mode_defaults.py",
    "scripts/check_manifest_paths.py",
    "scripts/check_knowledge_bundles.py",
    "scripts/check_index_coverage.py",
]


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def run_check(root: Path, rel: str) -> int:
    path = root / rel
    if not path.exists():
        print(f"SKIP missing check script: {rel}")
        return 0

    print(f"RUN python3 {rel}")
    completed = subprocess.run([sys.executable, rel], cwd=root, check=False)
    if completed.returncode == 0:
        print(f"PASS {rel}")
    else:
        print(f"FAIL {rel} exit={completed.returncode}")
    return completed.returncode


def print_guidance() -> None:
    print()
    print("Sync readiness guidance:")
    print("- GitHub is the current source of truth.")
    print("- ChatGPT Project Knowledge upload is needed only for baseline or bundle changes.")
    print("- Codex uses AGENTS.md plus repository files for fresh state.")
    print("- This helper validates repository consistency but does not upload to ChatGPT or push to GitHub.")
    print("- This helper does not perform external sync or modify remote systems.")


def main() -> int:
    root = repo_root()
    failures = 0
    for rel in CHECKS:
        failures += 1 if run_check(root, rel) else 0

    print_guidance()
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
