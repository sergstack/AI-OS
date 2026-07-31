#!/usr/bin/env python3
"""Runner role: apply the frozen evaluator to a repository worktree."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import subprocess
from pathlib import Path

from evaluator import evaluate


MANDATORY_CHECKS = [
    ["python3", "scripts/sync_aios.py"],
    ["python3", "scripts/check_project_instructions_length.py"],
    ["python3", "scripts/check_repo_public_safety.py"],
    ["python3", "scripts/check_codex_goal_mode_defaults.py"],
    ["python3", "scripts/check_manifest_paths.py"],
    ["python3", "scripts/check_knowledge_bundles.py"],
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    repo_root = args.repo_root.resolve()
    commit = subprocess.run(["git", "rev-parse", "HEAD"], cwd=repo_root, check=True, capture_output=True, text=True).stdout.strip()
    evaluation = evaluate(repo_root)
    checks = []
    for command in MANDATORY_CHECKS:
        completed = subprocess.run(command, cwd=repo_root, capture_output=True, text=True)
        checks.append({
            "command": " ".join(command),
            "exit_code": completed.returncode,
            "stdout_sha256": hashlib.sha256(completed.stdout.encode()).hexdigest(),
            "stderr_sha256": hashlib.sha256(completed.stderr.encode()).hexdigest(),
        })
    payload = {
        "role": "Runner",
        "repo_commit": commit,
        "python": platform.python_version(),
        "evaluation": evaluation,
        "mandatory_checks": checks,
        "mandatory_checks_pass": all(item["exit_code"] == 0 for item in checks),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({
        "repo_commit": commit,
        "score": evaluation["score"],
        "passed": evaluation["passed_count"],
        "total": evaluation["case_count"],
        "hard_failures": evaluation["hard_failures"],
        "mandatory_checks_pass": payload["mandatory_checks_pass"],
        "output_sha256": hashlib.sha256(args.output.read_bytes()).hexdigest(),
    }, ensure_ascii=False))
    return 0 if payload["mandatory_checks_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
