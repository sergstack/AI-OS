#!/usr/bin/env python3
"""Validate the canonical AI-OS StreamDeck v3.1.2 package."""

from __future__ import annotations

import hashlib
import json
import re
import sys
import zipfile
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ACTIVE = ROOT
ERRORS: list[str] = []
VERSION = "3.1.2"
APPROVED_REGISTRY_SHA256 = "d85df305d8a537df3b15eeeec0510607c8b1d84c28f47560ab9ce888fa22da82"


def load(relative: str):
    try:
        return json.loads((ACTIVE / relative).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        ERRORS.append(f"{relative}: {exc}")
        return {}


def require(condition: bool, message: str) -> None:
    if not condition:
        ERRORS.append(message)


def validate_exports(controller_rows, rows, prompt_by_id) -> None:
    export_dir = ACTIVE / "exports"
    paths = sorted(export_dir.glob("*.streamDeckProfile"))
    expected_ids = {"A00_CONTROL"} | {row["profile_id"] for row in rows}
    require({path.stem for path in paths} == expected_ids, "exports must contain exactly the 16 expected profiles")
    if {path.stem for path in paths} != expected_ids:
        return

    parsed = {}
    for path in paths:
        try:
            with zipfile.ZipFile(path) as archive:
                require(archive.testzip() is None, f"{path.name}: corrupt zip member")
                require(
                    all(info.date_time == (1980, 1, 1, 0, 0, 0) for info in archive.infolist()),
                    f"{path.name}: zip timestamps are not deterministic",
                )
                root_names = [
                    name for name in archive.namelist()
                    if name.endswith(".sdProfile/manifest.json") and name.count("/") == 1
                ]
                require(len(root_names) == 1, f"{path.name}: expected one root manifest")
                if len(root_names) != 1:
                    continue
                root_name = root_names[0]
                root = json.loads(archive.read(root_name))
                root_dir = root_name.removesuffix("/manifest.json")
                pages = root.get("Pages", {}).get("Pages", [])
                require(len(pages) == 1, f"{path.name}: expected one content page")
                if len(pages) != 1:
                    continue
                page_name = f"{root_dir}/Profiles/{pages[0].upper()}/manifest.json"
                default_name = f"{root_dir}/Profiles/{root['Pages']['Default'].upper()}/manifest.json"
                require(page_name in archive.namelist(), f"{path.name}: content page manifest missing")
                require(default_name in archive.namelist(), f"{path.name}: default page manifest missing")
                if page_name not in archive.namelist() or default_name not in archive.namelist():
                    continue
                page = json.loads(archive.read(page_name))
                actions = page["Controllers"][0]["Actions"]
                parsed[path.stem] = (path, root_dir.removesuffix(".sdProfile"), root, page_name, actions)
        except (OSError, KeyError, json.JSONDecodeError, zipfile.BadZipFile) as exc:
            ERRORS.append(f"{path.name}: {exc}")

    if set(parsed) != expected_ids:
        return
    profile_uuids = {profile_id: value[1] for profile_id, value in parsed.items()}
    source_rows = {"A00_CONTROL": controller_rows}
    for row in rows:
        source_rows.setdefault(row["profile_id"], []).append(row)
    secret = re.compile(r"(ghp_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16})")
    private_path = re.compile(r"/(Users|home)/[^/\s]+/")

    for profile_id, (path, _, root, page_name, actions) in parsed.items():
        require(root.get("Version") == "3.0", f"{path.name}: profile format version must be 3.0")
        require(root.get("Device", {}).get("UUID") == "", f"{path.name}: Device.UUID must be serial-neutral")
        require(len(actions) == 15, f"{path.name}: expected 15 actions")
        require(
            set(actions) == {f"{index % 5},{index // 5}" for index in range(15)},
            f"{path.name}: expected a complete 5x3 action grid",
        )
        rows_by_coordinate = {
            f"{(int(row['button'][1:]) - 1) % 5},{(int(row['button'][1:]) - 1) // 5}": row
            for row in source_rows[profile_id]
        }
        with zipfile.ZipFile(path) as archive:
            for coordinate, action in actions.items():
                row = rows_by_coordinate[coordinate]
                image = action["States"][0]["Image"]
                image_member = f"{page_name.removesuffix('manifest.json')}{image}"
                require(image_member in archive.namelist(), f"{path.name}/{coordinate}: embedded icon missing")
                if image_member in archive.namelist():
                    require(
                        archive.read(image_member) == (ACTIVE / row["icon"]).read_bytes(),
                        f"{path.name}/{coordinate}: embedded icon differs from icon map source",
                    )
                if profile_id == "A00_CONTROL":
                    require(action["UUID"] == "com.elgato.streamdeck.profile.rotate", f"{path.name}/{coordinate}: not Switch Profile")
                    require(action["Settings"].get("DeviceUUID") == "", f"{path.name}/{coordinate}: controller binding is not serial-neutral")
                    require(
                        action["Settings"].get("ProfileUUID") == profile_uuids[row["target_profile_id"]],
                        f"{path.name}/{coordinate}: target profile UUID mismatch",
                    )
                else:
                    prompt = prompt_by_id[row["prompt_id"]]
                    body = action["Settings"].get("pastedText")
                    require(action["UUID"] == "com.elgato.streamdeck.system.text", f"{path.name}/{coordinate}: not System > Text")
                    require(action["Settings"].get("isSendingEnter") is False, f"{path.name}/{coordinate}: auto-send is enabled")
                    require(row.get("insertion_method") == "clipboard_paste", f"{path.name}/{coordinate}: source insertion method is not clipboard_paste")
                    require(action["Settings"].get("isTypingMode") is False, f"{path.name}/{coordinate}: typed-text mode is enabled")
                    require(body == prompt["body"], f"{path.name}/{coordinate}: prompt body mismatch")
                    if isinstance(body, str):
                        require(hashlib.sha256(body.encode()).hexdigest() == prompt["prompt_hash"], f"{path.name}/{coordinate}: prompt hash mismatch")
            manifest_text = json.dumps(root, ensure_ascii=False) + json.dumps(actions, ensure_ascii=False)
            require(not secret.search(manifest_text), f"{path.name}: secret-like token in manifests")
            require(not private_path.search(manifest_text), f"{path.name}: private path in manifests")


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

    require(
        hashlib.sha256((ACTIVE / "prompts" / "prompt_registry.json").read_bytes()).hexdigest()
        == APPROVED_REGISTRY_SHA256,
        "prompt registry differs from the approved PR #216 v3.1.2 source",
    )
    for name, value in (
        ("controller map", controller),
        ("action profiles", actions),
        ("prompt registry", registry),
        ("QA matrix", qa),
        ("icon map", icons),
        ("migration manifest", migration),
        ("MCP registry", mcp),
    ):
        require(value.get("version") == VERSION, f"{name} version must be {VERSION}")

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
    require(all(r.get("insertion_method") == "clipboard_paste" for r in rows), "all 225 action buttons must use insertion_method=clipboard_paste")

    prompt_ids = [p["prompt_id"] for p in prompts]
    require(len(prompt_ids) == len(set(prompt_ids)) == 140, "registry must contain 140 unique prompt IDs")
    prompt_by_id = {p["prompt_id"]: p for p in prompts}
    require(registry["prompt_count"] == len(prompts), "prompt registry count mismatch")
    require({r["prompt_id"] for r in rows} == set(prompt_by_id), "button and registry prompt sets differ")
    valid_next = set(prompt_by_id) | {"owner_acceptance"}
    for row in rows:
        require(row["prompt_id"] in prompt_by_id, f"missing prompt: {row['prompt_id']}")
        for field in ("next_on_pass", "next_on_revise", "next_on_blocked"):
            require(row[field] in valid_next, f"{row['profile_id']}/{row['button']}: invalid {field}")
        require(row["owner_project"] == prompt_by_id[row["prompt_id"]]["owner_project"], f"route mismatch: {row['prompt_id']}")
        require(row["prompt_version"] == prompt_by_id[row["prompt_id"]]["prompt_version"], f"button/registry version mismatch: {row['prompt_id']}")
        require(row["icon"] == f"assets/icons/action_{prompt_by_id[row['prompt_id']]['task_type']}.svg", f"task type/icon mismatch: {row['prompt_id']}")
        require(not Path(row["icon"]).is_absolute() and (ACTIVE / row["icon"]).is_file(), f"missing/absolute icon: {row['icon']}")

    refs_by_prompt: dict[str, list[str]] = {prompt_id: [] for prompt_id in prompt_by_id}
    for row in rows:
        refs_by_prompt[row["prompt_id"]].append(f"{row['profile_id']}/{row['button']}")

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

    required_prompt_fields = {
        "prompt_id", "prompt_version", "task_type", "purpose", "owner_project",
        "button_refs", "input_requirements", "material_selection_rule", "execution_mode",
        "body", "output_schema", "evidence_policy", "freshness_policy",
        "execution_truth_policy", "quality_gate", "known_failure_modes", "qa_status",
        "ux_score_1_5", "prompt_gate_10_of_10", "last_reviewed",
        "owner_acceptance", "prompt_hash",
    }
    valid_task_types = {
        "analytics", "blocked", "draft", "execution_request", "handoff",
        "judge", "memo", "narrative", "revise", "route",
    }
    valid_owners = {
        "[AI OS]", "[Analytics]", "[Codex]", "[Inbox Router]", "[LLM]",
        "[LLM] / Judge", "[LLM] / Local AI", "[LLM] / Memo",
        "[LLM] / Revisor", "[Thinking]",
    }
    for prompt in prompts:
        prompt_id = prompt["prompt_id"]
        require(set(prompt) == required_prompt_fields, f"prompt contract fields mismatch: {prompt_id}")
        require(bool(re.fullmatch(r"\d+\.\d+\.\d+", prompt["prompt_version"])), f"invalid prompt version: {prompt_id}")
        require(prompt["task_type"] in valid_task_types, f"invalid task type: {prompt_id}")
        require(prompt["owner_project"] in valid_owners, f"invalid owner route: {prompt_id}")
        require(prompt["button_refs"] == refs_by_prompt[prompt_id], f"button_refs mismatch: {prompt_id}")
        require(prompt["execution_mode"] == "generate", f"invalid execution mode: {prompt_id}")
        require(prompt["qa_status"] == "not_run", f"unearned prompt QA status: {prompt_id}")
        require(prompt["body"].startswith("# ") and prompt["owner_project"] in prompt["body"].splitlines()[0], f"prompt header/owner mismatch: {prompt_id}")
        require(all(f"- {field}" in prompt["body"] for field in prompt["output_schema"]), f"body/output schema mismatch: {prompt_id}")

    qa_rows = qa["rows"]
    require(len(qa_rows) == qa["prompt_count"] == len(prompts), "QA matrix must have one row per unique prompt")
    require({r["prompt_id"] for r in qa_rows} == set(prompt_by_id), "QA matrix prompt set mismatch")
    executed_cases = 0
    live_run_count = 0
    for row in qa_rows:
        prompt = prompt_by_id[row["prompt_id"]]
        require(row["prompt_version"] == prompt["prompt_version"], f"QA/registry version mismatch: {row['prompt_id']}")
        require(row.get("prompt_hash") == prompt["prompt_hash"], f"QA/registry hash mismatch: {row['prompt_id']}")
        require(row["button_refs"] == prompt["button_refs"], f"QA/registry button_refs mismatch: {row['prompt_id']}")
        require({case["case"] for case in row["test_cases"]} == {"normal", "missing_context_or_evidence", "unsafe_or_ambiguous"}, f"representative cases missing: {row['prompt_id']}")
        for case in row["test_cases"]:
            require(case["status"] in {"NOT RUN", "EXECUTED"}, f"invalid QA execution status: {row['prompt_id']}/{case['case']}")
            forbidden_result_fields = {"response", "raw_response", "request", "request_text", "api_key"}
            require(not (forbidden_result_fields & set(case)), f"raw/private QA result field: {row['prompt_id']}/{case['case']}")
            live_runs = case.get("live_runs", [])
            require(isinstance(live_runs, list), f"invalid live_runs: {row['prompt_id']}/{case['case']}")
            live_run_count += len(live_runs)
            for live_run in live_runs:
                require(not (forbidden_result_fields & set(live_run)), f"raw/private live QA field: {row['prompt_id']}/{case['case']}")
                required_live_fields = {"provider", "model_id", "executed_at", "response_sha256", "response_chars", "deterministic_checks", "observed_verdict"}
                require(set(live_run) == required_live_fields, f"invalid live QA fields: {row['prompt_id']}/{case['case']}")
                require(live_run.get("provider") == "chatgpt_web", f"invalid live QA provider: {row['prompt_id']}/{case['case']}")
                require(isinstance(live_run.get("model_id"), str) and bool(live_run["model_id"]), f"missing live QA model id: {row['prompt_id']}/{case['case']}")
                require(bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", live_run.get("executed_at", ""))), f"invalid live QA execution date: {row['prompt_id']}/{case['case']}")
                require(live_run.get("observed_verdict") in {"pass", "revise"}, f"invalid live QA verdict: {row['prompt_id']}/{case['case']}")
                checks = live_run.get("deterministic_checks", {})
                required_checks = {"schema_fit", "missing_sections", "material_selection", "blocked_or_not_run", "unsafe_action_claim_free", "expected_behavior"}
                require(set(checks) == required_checks, f"invalid live deterministic checks: {row['prompt_id']}/{case['case']}")
                require(bool(re.fullmatch(r"[0-9a-f]{64}", live_run.get("response_sha256", ""))), f"invalid live response hash: {row['prompt_id']}/{case['case']}")
                require(isinstance(live_run.get("response_chars"), int) and live_run["response_chars"] > 0, f"invalid live response length: {row['prompt_id']}/{case['case']}")
            if case["status"] == "EXECUTED":
                executed_cases += 1
                require(case.get("provider") in {"openai", "anthropic", "google"}, f"invalid QA provider: {row['prompt_id']}/{case['case']}")
                require(isinstance(case.get("model_id"), str) and bool(case["model_id"]), f"missing QA model id: {row['prompt_id']}/{case['case']}")
                require(bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", case.get("executed_at", ""))), f"invalid QA execution date: {row['prompt_id']}/{case['case']}")
                require(case.get("observed_verdict") in {"pass", "revise"}, f"invalid QA verdict: {row['prompt_id']}/{case['case']}")
                checks = case.get("deterministic_checks", {})
                required_checks = {"schema_fit", "missing_sections", "material_selection", "blocked_or_not_run", "unsafe_action_claim_free", "expected_behavior"}
                require(set(checks) == required_checks, f"invalid deterministic QA checks: {row['prompt_id']}/{case['case']}")
                require(checks.get("schema_fit") in {"pass", "fail"}, f"invalid schema-fit result: {row['prompt_id']}/{case['case']}")
                require(isinstance(checks.get("missing_sections"), list), f"invalid missing-sections result: {row['prompt_id']}/{case['case']}")
                require(all(checks.get(name) in {"pass", "fail", "not_applicable"} for name in required_checks - {"schema_fit", "missing_sections"}), f"invalid deterministic result value: {row['prompt_id']}/{case['case']}")
                require(bool(re.fullmatch(r"[0-9a-f]{64}", case.get("response_sha256", ""))), f"invalid response hash: {row['prompt_id']}/{case['case']}")
                require(isinstance(case.get("response_chars"), int) and case["response_chars"] > 0, f"invalid response length: {row['prompt_id']}/{case['case']}")
                require(all(isinstance(value, int) and value >= 0 for value in case.get("usage", {}).values()), f"invalid QA usage: {row['prompt_id']}/{case['case']}")
        require(len(row["gate_criteria"]) == 10 and row["criteria_passed"] == 9, f"gate accounting mismatch: {row['prompt_id']}")
        require(row["judge_verdict"] == "blocked", f"unearned Prompt QA pass: {row['prompt_id']}")
        require(row["owner_acceptance"] == "pending" and row["formal_gate_status"] == "blocked - not 10/10", f"unearned QA acceptance: {row['prompt_id']}")
    if executed_cases:
        require(qa["status"] == "repo static QA complete; model executions recorded; physical QA and owner acceptance pending", "executed QA matrix status mismatch")
    require(qa.get("live_run_count") == live_run_count, "live QA run count mismatch")

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
    require("import NOT RUN" in migration["binary_exports"], "binary export import gate must remain NOT RUN")
    require(migration["physical_switch"].startswith("NOT RUN"), "physical switch must remain NOT RUN")

    validate_exports(controller_rows, rows, prompt_by_id)

    archive_checksums = json.loads((ROOT / "archive" / "checksums.json").read_text(encoding="utf-8"))
    for item in archive_checksums["files"]:
        path = ROOT / item["path"]
        require(path.is_file(), f"archive file missing: {item['path']}")
        if path.is_file():
            require(hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"], f"archive checksum mismatch: {item['path']}")

    generated = (ACTIVE / "generated" / "button_map.md").read_text(encoding="utf-8")
    for row in controller_rows + rows:
        require(row["label"] in generated, f"generated map missing label: {row['label']}")
    for row in rows:
        require(
            f"| `{row['prompt_id']}` | `{row['prompt_version']}` |" in generated,
            f"generated map missing prompt/version: {row['prompt_id']} {row['prompt_version']}",
        )
    return report(controller_rows, rows, prompts, qa_rows)


def report(controller=None, rows=None, prompts=None, qa_rows=None) -> int:
    if ERRORS:
        for error in ERRORS:
            print(f"FAIL: {error}")
        print(f"FAIL: {len(ERRORS)} validation error(s)")
        return 1
    print(f"PASS: controller_buttons={len(controller)} action_profiles=15 action_buttons={len(rows)} prompts={len(prompts)} qa_rows={len(qa_rows)}")
    print("PASS: references, routing, hashes, assets, exports, MCP counts, checksums, safety and NOT RUN gates")
    return 0


if __name__ == "__main__":
    sys.exit(main())
