#!/usr/bin/env python3
"""Validate the canonical AI-OS StreamDeck v3.0 package."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
ACTIVE = ROOT / "active" / "v3.0"
ERRORS: list[str] = []


def load(relative: str):
    try:
        return json.loads((ACTIVE / relative).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        ERRORS.append(f"{relative}: {exc}")
        return {}


def require(condition: bool, message: str) -> None:
    if not condition:
        ERRORS.append(message)


def main() -> int:
    controller = load("config/controller_map.json")
    actions = load("config/action_profiles.json")
    registry = load("prompts/prompt_registry.json")
    qa = load("qa/prompt_qa_matrix.json")
    icons = load("config/icon_map.json")
    migration = load("migration/migration_manifest.json")
    mcp = load("migration/mcp_registry.json")
    baseline = load("qa/baseline_audit.json")
    if ERRORS:
        return report()

    controller_rows = controller["buttons"]
    rows = actions["buttons"]
    prompts = registry["prompts"]
    require(len(controller_rows) == controller["count"] == 15, "controller must contain exactly 15 buttons")
    require(len({r["target_profile_id"] for r in controller_rows}) == 15, "controller target profiles must be unique")
    require(all(r["auto_send"] is False for r in controller_rows), "controller auto_send must be false")

    profiles = {r["profile_id"] for r in rows}
    require(len(profiles) == actions["profile_count"] == 15, "action deck must contain exactly 15 profiles")
    require(len(rows) == actions["button_count"] == 225, "action deck must contain exactly 225 buttons")
    for profile in profiles:
        keys = {r["button"] for r in rows if r["profile_id"] == profile}
        require(keys == {f"K{i}" for i in range(1, 16)}, f"{profile}: expected exactly K1-K15")
    require(len({(r["device"], r["profile_id"], r["button"]) for r in rows}) == len(rows), "duplicate device/profile/button")
    require(all(r["auto_send"] is False and r["requires_confirmation"] is True for r in rows), "all action buttons must be supervised and auto_send=false")

    prompt_keys = [(p["prompt_id"], p["prompt_version"]) for p in prompts]
    require(len(prompt_keys) == len(set(prompt_keys)), "prompt_id + prompt_version must be unique")
    prompt_by_id = {p["prompt_id"]: p for p in prompts}
    require(registry["prompt_count"] == len(prompts), "prompt registry count mismatch")
    require({r["prompt_id"] for r in rows} == set(prompt_by_id), "button and registry prompt sets differ")
    valid_next = set(prompt_by_id) | {"owner_acceptance"}
    for row in rows:
        require(row["prompt_id"] in prompt_by_id, f"missing prompt: {row['prompt_id']}")
        for field in ("next_on_pass", "next_on_revise", "next_on_blocked"):
            require(row[field] in valid_next, f"{row['profile_id']}/{row['button']}: invalid {field}")
        require(row["owner_project"] == prompt_by_id[row["prompt_id"]]["owner_project"], f"route mismatch: {row['prompt_id']}")
        require(not Path(row["icon"]).is_absolute() and (ACTIVE / row["icon"]).is_file(), f"missing/absolute icon: {row['icon']}")

    bodies = Counter(p["body"] for p in prompts)
    require(not [body for body, count in bodies.items() if count > 1], "duplicate prompt bodies found")
    forbidden = re.compile(r"\[PASTE[^\]]*\]|\bTODO\b|Summary:\s*\nFacts used:", re.I)
    secret = re.compile(r"(ghp_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16})")
    private_path = re.compile(r"/(Users|home)/[^/\s]+/")
    for prompt in prompts:
        body = prompt["body"]
        require(not forbidden.search(body), f"placeholder/generic schema in {prompt['prompt_id']}")
        require("??" not in body and "!!" not in body, f"double punctuation in {prompt['prompt_id']}")
        require(not secret.search(body), f"secret-like token in {prompt['prompt_id']}")
        require(not private_path.search(body), f"private absolute path in {prompt['prompt_id']}")
        require(hashlib.sha256(body.encode()).hexdigest() == prompt["prompt_hash"], f"prompt hash mismatch: {prompt['prompt_id']}")
        require(prompt["prompt_gate_10_of_10"] is None and prompt["owner_acceptance"] == "pending", f"unearned prompt gate: {prompt['prompt_id']}")
        require(prompt["output_schema"] and prompt["output_schema"] != ["Summary", "Facts used", "Assumptions", "Risks", "Next step"], f"generic output schema: {prompt['prompt_id']}")

    require(prompt_by_id["b50_llm_prompt_build"]["output_schema"] == ["Recommended workflow", "Prompt / template", "Input requirements", "Output schema", "Model class", "Quality gate", "Known failure modes", "Handoff / next action"], "PROMPT BUILD schema mismatch")
    require(prompt_by_id["b50_llm_context_pack"]["output_schema"] == ["Goal", "Decision needed", "Relevant files / sources", "Facts", "Assumptions", "Constraints", "Forbidden", "Open questions", "Expected output", "Quality gate", "Owner project", "Handoff target"], "CONTEXT PACK schema mismatch")
    require("there is no paste placeholder" in prompt_by_id["codex_goal_to_pr"]["body"], "GOAL→PR latest-goal contract missing")
    require("never the verdict itself" in prompt_by_id["revisor_apply_notes"]["body"], "REVISOR source-artifact contract missing")
    require("current official sources" in prompt_by_id["ai_trend"]["body"], "AI TREND freshness contract missing")
    require(all("All calculations and numeric QA must be performed by Python or SQL" in p["body"] for p in prompts if p["task_type"] == "analytics"), "Analytics deterministic boundary missing")
    require(all("Analytics-approved facts" in p["output_schema"] and "requires management confirmation" in p["body"] for p in prompts if p["task_type"] == "memo"), "Memo narrative boundary missing")
    require(all("Return only pass, revise, or blocked" in p["body"] for p in prompts if p["task_type"] == "judge"), "Judge verdict contract missing")
    require(prompt_by_id["b20_ai_os_prompt_qa"]["task_type"] == "judge", "PROMPT QA must be judge-only")

    qa_rows = qa["rows"]
    require(len(qa_rows) == qa["prompt_count"] == len(prompts), "QA matrix must have one row per unique prompt")
    require({r["prompt_id"] for r in qa_rows} == set(prompt_by_id), "QA matrix prompt set mismatch")
    for row in qa_rows:
        require({case["case"] for case in row["test_cases"]} == {"normal", "missing_context_or_evidence", "unsafe_or_ambiguous"}, f"representative cases missing: {row['prompt_id']}")
        require(len(row["gate_criteria"]) == 10 and row["criteria_passed"] == 9, f"gate accounting mismatch: {row['prompt_id']}")
        require(row["judge_verdict"] == "blocked", f"unearned Prompt QA pass: {row['prompt_id']}")

    icon_paths = {item["path"] for item in icons["icons"]}
    require(icon_paths == {r["icon"] for r in controller_rows + rows}, "icon map does not match button maps")
    require(mcp["counts"]["total"] == len(mcp["actions"]) == 7, "MCP registry must contain seven actions")
    require(mcp["counts"]["execution_verified_legacy"] == 2, "legacy MCP evidence count must be computed as two")
    require(baseline["counts"] == {
        "cells": 195, "screens": 13, "text_actions": 118, "empty_cells": 53,
        "folder_actions": 12, "back_actions": 12,
        "texts_with_repeated_safety_boilerplate": 117,
        "repeated_safety_boilerplate_chars_including_heading": 411,
        "texts_with_generic_output_schema": 44, "paste_goal_placeholders": 1,
    }, "v2.9 computed baseline counts differ from issue evidence")

    for item in migration["files"]:
        path = ROOT / item["path"]
        require(path.is_file(), f"manifest file missing: {item['path']}")
        if path.is_file():
            require(hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"], f"manifest checksum mismatch: {item['path']}")
    require(migration["binary_exports"].startswith("NOT RUN"), "binary exports must remain NOT RUN")
    require(migration["physical_switch"].startswith("NOT RUN"), "physical switch must remain NOT RUN")

    archive_checksums = json.loads((ROOT / "archive" / "checksums.json").read_text(encoding="utf-8"))
    for item in archive_checksums["files"]:
        path = ROOT / item["path"]
        require(path.is_file(), f"archive file missing: {item['path']}")
        if path.is_file():
            require(hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"], f"archive checksum mismatch: {item['path']}")

    generated = (ACTIVE / "generated" / "button_map.md").read_text(encoding="utf-8")
    for row in controller_rows + rows:
        require(row["label"] in generated, f"generated map missing label: {row['label']}")
    return report(controller_rows, rows, prompts, qa_rows)


def report(controller=None, rows=None, prompts=None, qa_rows=None) -> int:
    if ERRORS:
        for error in ERRORS:
            print(f"FAIL: {error}")
        print(f"FAIL: {len(ERRORS)} validation error(s)")
        return 1
    print(f"PASS: controller_buttons={len(controller)} action_profiles=15 action_buttons={len(rows)} prompts={len(prompts)} qa_rows={len(qa_rows)}")
    print("PASS: references, routing, hashes, assets, MCP counts, checksums, safety and NOT RUN gates")
    return 0


if __name__ == "__main__":
    sys.exit(main())
