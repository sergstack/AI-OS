#!/usr/bin/env python3
"""Validate the canonical AI-OS StreamDeck v3.0 package."""

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
        require(row["prompt_version"] == prompt_by_id[row["prompt_id"]]["prompt_version"], f"button/registry version mismatch: {row['prompt_id']}")
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

    specialized_markers = (
        "\n\nSubject logic:\n", "\n\nFreshness:\n", "\n\nNumeric boundary:\n",
        "\n\nRevision boundary:\n", "\n\nGoal Mode boundary:\n", "\n\nJudge rule:\n", "\n\nMemo boundary:\n",
    )
    boilerplate_only = [p["prompt_id"] for p in prompts if not any(marker in p["body"] for marker in specialized_markers)]
    require(len(boilerplate_only) == 61, f"expected 61 boilerplate-only prompts after ROUTE batch, found {len(boilerplate_only)}")
    route_batch_ids = {
        row["prompt_id"] for row in rows
        if row["profile_id"] == "B10_ROUTE" and int(row["button"][1:]) <= 12
    }
    require(all(prompt_by_id[prompt_id]["prompt_version"] == "1.1.0" for prompt_id in route_batch_ids), "ROUTE batch versions must be 1.1.0")
    require(all("\n\nSubject logic:\n" in prompt_by_id[prompt_id]["body"] for prompt_id in route_batch_ids), "ROUTE batch subject logic missing")
    owner_projects = ("[Inbox Router]", "[AI OS]", "[Thinking]", "[Analytics]", "[LLM]", "[Codex]")
    b10_router_ids = {
        row["prompt_id"] for row in rows
        if row["profile_id"] == "B10_ROUTE" and int(row["button"][1:]) <= 10
    }
    require(all(all(owner in prompt_by_id[prompt_id]["body"] for owner in owner_projects) for prompt_id in b10_router_ids), "B10 ROUTE prompts must list all allowed owner projects")

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
        require(row["prompt_version"] == prompt_by_id[row["prompt_id"]]["prompt_version"], f"QA/registry version mismatch: {row['prompt_id']}")
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
