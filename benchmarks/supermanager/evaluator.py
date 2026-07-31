#!/usr/bin/env python3
"""Immutable deterministic evaluator for the Supermanager Level A benchmark."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path


def _text(repo_root: Path, paths: list[str]) -> tuple[str, list[str]]:
    chunks: list[str] = []
    missing: list[str] = []
    for relative in paths:
        path = repo_root / relative
        if not path.is_file():
            missing.append(relative)
            continue
        chunks.append(path.read_text(encoding="utf-8"))
    return "\n".join(chunks), missing


def _evaluate_terms(case: dict, content_root: Path) -> tuple[bool, dict]:
    content, missing = _text(content_root, case["paths"])
    required_all = case.get("required_all", [])
    required_any = case.get("required_any", [])
    forbidden = case.get("forbidden", [])
    absent = [term for term in required_all if term not in content]
    any_ok = not required_any or any(term in content for term in required_any)
    present_forbidden = [term for term in forbidden if term in content]
    passed = not missing and not absent and any_ok and not present_forbidden
    return passed, {
        "missing_files": missing,
        "missing_required_terms": absent,
        "required_any_satisfied": any_ok,
        "present_forbidden_terms": present_forbidden,
    }


def _evaluate_command(case: dict, repo_root: Path) -> tuple[bool, dict]:
    completed = subprocess.run(
        case["argv"], cwd=repo_root, text=True, capture_output=True, check=False
    )
    return completed.returncode == 0, {
        "argv": case["argv"],
        "returncode": completed.returncode,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
    }


def _evaluate_registry(repo_root: Path) -> tuple[bool, dict]:
    instructions = sorted(repo_root.glob("ChatGPT/*/PROJECT_INSTRUCTIONS.md"))
    registry = (repo_root / "PROJECT_REGISTRY.md").read_text(encoding="utf-8")
    missing = [
        path.parent.name
        for path in instructions
        if f"`{path.parent.name}`" not in registry
        or f"`{path.parent.relative_to(repo_root)}`" not in registry
    ]
    return not missing, {"project_count": len(instructions), "missing_registry_entries": missing}


def evaluate_case(case: dict, repo_root: Path) -> dict:
    assertion = case["assertion"]
    if assertion == "terms":
        passed, evidence = _evaluate_terms(case, repo_root)
    elif assertion == "definition_terms":
        passed, evidence = _evaluate_terms(case, Path(__file__).resolve().parent)
    elif assertion == "command":
        passed, evidence = _evaluate_command(case, repo_root)
    elif assertion == "registry_matches":
        passed, evidence = _evaluate_registry(repo_root)
    elif assertion == "path_reference":
        source = repo_root / case["source_path"]
        target = repo_root / case["reference"]
        source_text = source.read_text(encoding="utf-8") if source.is_file() else ""
        passed = source.is_file() and case["reference"] in source_text and target.is_file()
        evidence = {
            "source_exists": source.is_file(),
            "reference_declared": case["reference"] in source_text,
            "target_exists": target.is_file(),
        }
    else:
        raise ValueError(f"Unsupported assertion: {assertion}")
    return {
        "id": case["id"],
        "set": case["set"],
        "project": case["project"],
        "route": case["route"],
        "category": case["category"],
        "hard_fail_class": case.get("hard_fail_class"),
        "passed": passed,
        "score": 100 if passed else 0,
        "evidence": evidence,
    }


def load_cases(path: Path) -> list[dict]:
    return json.loads(path.read_text(encoding="utf-8"))["cases"]
