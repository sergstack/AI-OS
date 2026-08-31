from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft7Validator


ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / "docs/standards/LOCAL_FIRST_COMPUTE_POLICY.md"
REGISTRY = ROOT / "docs/standards/local_first_task_class_registry.json"
SCHEMA = ROOT / "schemas/local_first_task_class_registry.schema.json"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_local_first_registry_conforms_to_schema() -> None:
    errors = sorted(
        Draft7Validator(load_json(SCHEMA)).iter_errors(load_json(REGISTRY)),
        key=lambda error: list(error.path),
    )
    assert errors == []


def test_initial_registry_has_no_unproven_local_first_promotion() -> None:
    task_classes = load_json(REGISTRY)["task_classes"]
    assert len({item["task_class_id"] for item in task_classes}) == len(task_classes)
    assert {item["status"] for item in task_classes} >= {
        "candidate_review",
        "frontier_floor",
        "blocked",
    }
    assert all(
        item["promotion_evidence"] == "owner_accepted"
        for item in task_classes
        if item["status"] == "local_first"
    )
    assert not any(item["status"] == "local_first" for item in task_classes)


def test_blocked_classes_cannot_claim_output_authority() -> None:
    task_classes = load_json(REGISTRY)["task_classes"]
    blocked = [item for item in task_classes if item["status"] == "blocked"]
    assert blocked
    assert all(item["output_authority"] == "none" for item in blocked)


def test_policy_preserves_issue_345_boundaries() -> None:
    policy = POLICY.read_text(encoding="utf-8")
    required_sections = [
        "## Selection order",
        "## Registry statuses",
        "## Promotion contract",
        "## Progressive disclosure",
        "## Loss-aware compaction",
        "## Provenance and authority",
        "## Rollback and revisit",
    ]
    assert all(section in policy for section in required_sections)
    assert "The initial production `local_first` allowlist is empty." in policy
    assert "Frontier review is not owner approval." in policy
