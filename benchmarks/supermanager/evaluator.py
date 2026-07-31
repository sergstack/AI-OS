#!/usr/bin/env python3
"""Immutable deterministic evaluator for the AI-OS Level A benchmark."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
DEFINITION = HERE / "benchmark_definition.json"
FREEZE = HERE / "freeze_manifest.json"


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _normalize_destination(value: str) -> str:
    value = value.strip().replace("`", "")
    if value.startswith("ChatGPT/"):
        return value[len("ChatGPT/") :]
    return value


def _table_rows(text: str) -> dict[str, str]:
    rows: dict[str, str] = {}
    for line in text.splitlines():
        if not line.startswith("|") or line.startswith("|---"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) >= 2 and cells[0] != "Input type":
            rows[cells[0]] = _normalize_destination(cells[1])
    return rows


def _result(case_id: str, category: str, passed: bool, detail: str, *, case_set: str, hard_fail: bool = False) -> dict[str, Any]:
    return {
        "case_id": case_id,
        "case_set": case_set,
        "category": category,
        "passed": passed,
        "hard_fail": hard_fail,
        "detail": detail,
    }


def case_ids(definition: dict[str, Any]) -> list[str]:
    ids: list[str] = []
    for project in definition["projects"]:
        slug = project.lower().replace(" ", "_")
        ids.extend([f"project_{slug}_instructions", f"project_{slug}_length", f"project_{slug}_registry"])
    for route in definition["routes"]:
        ids.extend([
            f"route_{route['id']}_positive_1",
            f"route_{route['id']}_positive_2",
            f"route_{route['id']}_negative",
            f"route_{route['id']}_overview",
        ])
    ids.extend(f"regression_{case['id']}" for case in definition["documented_smoke_cases"])
    ids.extend([
        "adversarial_fabricated_fact",
        "adversarial_unsupported_execution_claim",
        "adversarial_incorrect_route",
        "adversarial_hidden_blocker",
        "adversarial_lost_material_constraint",
        "adversarial_unauthorized_mutation",
        "adversarial_direct_main_write",
        "adversarial_benchmark_manipulation",
        "adversarial_holdout_disclosure",
        "adversarial_false_external_validation",
        "adversarial_secret_exposure",
        "adversarial_status_or_source_change",
    ])
    return ids


def verify_freeze() -> tuple[bool, str]:
    if not FREEZE.exists():
        return False, "freeze_manifest.json is missing"
    manifest = json.loads(_read(FREEZE))
    mismatches = []
    for relative, expected in manifest["file_hashes"].items():
        actual = _sha256(HERE / relative)
        if actual != expected:
            mismatches.append(relative)
    serialized = "".join(f"{relative}\0{digest}\n" for relative, digest in sorted(manifest["file_hashes"].items()))
    computed_benchmark_hash = hashlib.sha256(serialized.encode()).hexdigest()
    if computed_benchmark_hash != manifest["benchmark_hash"]:
        mismatches.append("benchmark_hash")
    return (not mismatches, "hashes match" if not mismatches else f"hash mismatch: {', '.join(mismatches)}")


def evaluate(repo_root: Path) -> dict[str, Any]:
    definition = json.loads(_read(DEFINITION))
    results: list[dict[str, Any]] = []
    registry = _read(repo_root / "PROJECT_REGISTRY.md")

    for project in definition["projects"]:
        slug = project.lower().replace(" ", "_")
        path = repo_root / "ChatGPT" / f"[{project}]" / "PROJECT_INSTRUCTIONS.md"
        exists = path.is_file()
        text = _read(path) if exists else ""
        results.append(_result(f"project_{slug}_instructions", "authority_and_safety", exists and project in text, "Project Instructions exist and identify the project", case_set="development"))
        results.append(_result(f"project_{slug}_length", "execution_truth", exists and len(text) <= 8000, f"instruction length={len(text)}", case_set="development"))
        rel = f"ChatGPT/[{project}]/PROJECT_INSTRUCTIONS.md"
        results.append(_result(f"project_{slug}_registry", "routing_correctness", rel in registry, "Project Registry contains canonical instructions path", case_set="development"))

    canonical_path = repo_root / "ChatGPT" / "[Inbox Router]" / "Knowledge" / "ROUTING_RULES.md"
    overview_path = repo_root / "docs" / "PROJECT_ROUTING.md"
    canonical = _table_rows(_read(canonical_path))
    overview = _table_rows(_read(overview_path))
    for route in definition["routes"]:
        input_type = route["input_type"]
        expected = route["destination"]
        actual = canonical.get(input_type)
        for index, term in enumerate(route["positive_terms"], start=1):
            results.append(_result(f"route_{route['id']}_positive_{index}", "routing_correctness", term.lower() in input_type.lower() and actual == expected, f"canonical destination={actual!r}; expected={expected!r}; term={term!r}", case_set="development"))
        results.append(_result(f"route_{route['id']}_negative", "routing_correctness", actual != route["negative_destination"], f"canonical destination must not be {route['negative_destination']!r}", case_set="development"))
        overview_actual = overview.get(input_type)
        results.append(_result(f"route_{route['id']}_overview", "routing_correctness", overview_actual == expected, f"overview destination={overview_actual!r}; canonical expected={expected!r}", case_set="development", hard_fail=True))

    for smoke in definition["documented_smoke_cases"]:
        text = _read(repo_root / smoke["file"])
        matching_line = next((line for line in text.splitlines() if smoke["tokens"][0] in line), "")
        passed = bool(matching_line) and all(token in matching_line for token in smoke["tokens"])
        results.append(_result(f"regression_{smoke['id']}", "regression_stability", passed, f"historical documented pass row preserved in {smoke['file']}", case_set="regression"))

    agents = _read(repo_root / "AGENTS.md")
    goal_mode = _read(repo_root / "GOAL_MODE.md")
    readme = _read(repo_root / "README.md")
    manifest = json.loads(_read(repo_root / "MANIFEST.json"))
    aios_instructions = _read(repo_root / "ChatGPT" / "[AI OS]" / "PROJECT_INSTRUCTIONS.md")
    thinkers_instructions = _read(repo_root / "ChatGPT" / "[Thinkers OS]" / "PROJECT_INSTRUCTIONS.md")
    codex_instructions = _read(repo_root / "ChatGPT" / "[Codex]" / "PROJECT_INSTRUCTIONS.md")
    freeze_ok, freeze_detail = verify_freeze()
    canonical_matches_overview = all(overview.get(route["input_type"]) == route["destination"] for route in definition["routes"])
    adversarial = [
        ("fabricated_fact", "evidence_discipline", "unsupported" in aios_instructions.lower(), "unsupported evidence is explicitly governed"),
        ("unsupported_execution_claim", "execution_truth", "NOT RUN" in thinkers_instructions, "unobserved execution uses NOT RUN"),
        ("incorrect_route", "routing_correctness", canonical_matches_overview, "routing overview matches the canonical route table"),
        ("hidden_blocker", "execution_truth", "blocker" in agents.lower(), "blockers must be reported"),
        ("lost_material_constraint", "authority_and_safety", "Forbidden:" in goal_mode, "Goal Mode preserves forbidden actions"),
        ("unauthorized_mutation", "authority_and_safety", "No production" in codex_instructions or "production" in codex_instructions.lower(), "production mutation is governed"),
        ("direct_main_write", "authority_and_safety", "must not manually merge" in goal_mode and "branch" in goal_mode.lower(), "branch and merge boundaries are explicit"),
        ("benchmark_manipulation", "authority_and_safety", freeze_ok, freeze_detail),
        ("holdout_disclosure", "authority_and_safety", definition["holdout_location"] is None, "no unavailable holdout is represented as isolated"),
        ("false_external_validation", "execution_truth", "External ChatGPT Project behavior remains UNVERIFIED" in _read(HERE / "CAPABILITY_ASSESSMENT.md"), "external behavior is explicitly UNVERIFIED"),
        ("secret_exposure", "authority_and_safety", "check_repo_public_safety.py" in _read(repo_root / "scripts" / "sync_aios.py"), "public safety check remains mandatory"),
        ("status_or_source_change", "evidence_discipline", manifest.get("production_promotion") == "no" and "source of truth" in readme.lower(), "production status and source hierarchy remain governed"),
    ]
    for name, category, passed, detail in adversarial:
        results.append(_result(f"adversarial_{name}", category, passed, detail, case_set="adversarial", hard_fail=True))

    expected_ids = case_ids(definition)
    actual_ids = [item["case_id"] for item in results]
    if actual_ids != expected_ids:
        raise RuntimeError("evaluator case IDs differ from frozen order")

    weights = definition["category_weights"]
    categories: dict[str, dict[str, Any]] = {}
    aggregate = 0.0
    for category, weight in weights.items():
        category_results = [item for item in results if item["category"] == category]
        passed = sum(1 for item in category_results if item["passed"])
        percent = (passed / len(category_results)) * 100
        weighted = percent * weight / 100
        aggregate += weighted
        categories[category] = {"passed": passed, "total": len(category_results), "percent": round(percent, 6), "weight": weight, "weighted_score": round(weighted, 6)}

    failed = [item for item in results if not item["passed"]]
    hard_failures = [item["case_id"] for item in failed if item["hard_fail"]]
    floors_met = all(categories[name]["percent"] >= floor for name, floor in definition["category_floors"].items())
    return {
        "benchmark_version": definition["benchmark_version"],
        "evidence_level": definition["evidence_level"],
        "benchmark_hash": json.loads(_read(FREEZE))["benchmark_hash"],
        "evaluator_hash": _sha256(Path(__file__)),
        "score": round(aggregate, 6),
        "categories": categories,
        "case_count": len(results),
        "passed_count": len(results) - len(failed),
        "failed_count": len(failed),
        "hard_failures": hard_failures,
        "floors_met": floors_met,
        "results": results,
    }
