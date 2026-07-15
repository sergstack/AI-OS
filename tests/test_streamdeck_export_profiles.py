from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import zipfile


REPO_ROOT = Path(__file__).resolve().parents[1]
STREAMDECK = REPO_ROOT / "StreamDeck"
EXPORTER = STREAMDECK / "tools" / "export_profiles.py"


def run_export(output_dir: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(EXPORTER), "--output-dir", str(output_dir)],
        cwd=REPO_ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def hashes(output_dir: Path) -> dict[str, str]:
    return {
        path.name: hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(output_dir.glob("*.streamDeckProfile"))
    }


def page_actions(archive: zipfile.ZipFile) -> dict:
    manifests = [name for name in archive.namelist() if name.endswith("/manifest.json")]
    for name in manifests:
        value = json.loads(archive.read(name))
        controllers = value.get("Controllers")
        if controllers and controllers[0].get("Actions"):
            return controllers[0]["Actions"]
    raise AssertionError("content page manifest not found")


def test_export_is_deterministic_and_prompt_bodies_are_exact(tmp_path: Path) -> None:
    first = run_export(tmp_path)
    assert first.returncode == 0, first.stderr
    first_hashes = hashes(tmp_path)
    assert len(first_hashes) == 16

    second = run_export(tmp_path)
    assert second.returncode == 0, second.stderr
    assert hashes(tmp_path) == first_hashes

    registry = json.loads((STREAMDECK / "prompts" / "prompt_registry.json").read_text(encoding="utf-8"))
    config = json.loads((STREAMDECK / "config" / "action_profiles.json").read_text(encoding="utf-8"))
    qa = json.loads((STREAMDECK / "qa" / "prompt_qa_matrix.json").read_text(encoding="utf-8"))
    assert len(config["buttons"]) == 225
    assert all(item.get("insertion_method") == "clipboard_paste" for item in config["buttons"])
    registry_by_id = {item["prompt_id"]: item for item in registry["prompts"]}
    qa_by_id = {item["prompt_id"]: item for item in qa["rows"]}
    route_batch_ids = {
        item["prompt_id"] for item in config["buttons"]
        if item["profile_id"] == "B10_ROUTE" and int(item["button"][1:]) <= 12
    }
    assert len(route_batch_ids) == 12
    assert all(registry_by_id[prompt_id]["prompt_version"] == "1.1.0" for prompt_id in route_batch_ids)
    assert all(qa_by_id[prompt_id]["prompt_version"] == "1.1.0" for prompt_id in route_batch_ids)
    assert all("\n\nSubject logic:\n" in registry_by_id[prompt_id]["body"] for prompt_id in route_batch_ids)
    judge_batch_ids = {
        item["prompt_id"] for item in config["buttons"]
        if item["profile_id"] == "B70_JUDGE" and int(item["button"][1:]) <= 10
    } | {"final_acceptance_gate"}
    assert len(judge_batch_ids) == 11
    assert all(registry_by_id[prompt_id]["prompt_version"] == "1.1.0" for prompt_id in judge_batch_ids)
    assert all(qa_by_id[prompt_id]["prompt_version"] == "1.1.0" for prompt_id in judge_batch_ids)
    assert all("\n\nSubject logic:\n" in registry_by_id[prompt_id]["body"] for prompt_id in judge_batch_ids)
    analytics_batch_ids = {
        item["prompt_id"] for item in config["buttons"]
        if item["profile_id"] == "B40_ANALYTICS" and int(item["button"][1:]) <= 10
    }
    assert len(analytics_batch_ids) == 10
    assert all(registry_by_id[prompt_id]["prompt_version"] == "1.1.0" for prompt_id in analytics_batch_ids)
    assert all(qa_by_id[prompt_id]["prompt_version"] == "1.1.0" for prompt_id in analytics_batch_ids)
    assert all("\n\nSubject logic:\n" in registry_by_id[prompt_id]["body"] for prompt_id in analytics_batch_ids)
    deck_qa_batch_ids = {
        "be0_deck_qa_device_target", "be0_deck_qa_text_insert", "be0_deck_qa_auto_send_off",
        "be0_deck_qa_placeholder", "be0_deck_qa_duplicates", "be0_deck_qa_prompt_hash",
        "be0_deck_qa_export_backup",
    }
    assert all(registry_by_id[prompt_id]["prompt_version"] == "1.1.0" for prompt_id in deck_qa_batch_ids)
    assert all(qa_by_id[prompt_id]["prompt_version"] == "1.1.0" for prompt_id in deck_qa_batch_ids)
    assert all("\n\nSubject logic:\n" in registry_by_id[prompt_id]["body"] for prompt_id in deck_qa_batch_ids)
    aios_kb_pilots_batch_ids = {
        "b20_ai_os_governance", "b20_ai_os_loop_design", "b20_ai_os_pattern",
        "b20_ai_os_streamdeck", "b20_ai_os_use_case",
        "bb0_pilots_pilot_plan", "bb0_pilots_pilot_result", "bb0_pilots_residual_risk",
        "bb0_pilots_rollback", "bb0_pilots_run_record", "bb0_pilots_status_note",
        "bc0_kb_bundle_sync", "bc0_kb_evidence_label", "bc0_kb_kb_search",
        "bc0_kb_manifest", "bc0_kb_review_item", "bc0_kb_support_mix",
    }
    assert all(registry_by_id[prompt_id]["prompt_version"] == "1.1.0" for prompt_id in aios_kb_pilots_batch_ids)
    assert all(qa_by_id[prompt_id]["prompt_version"] == "1.1.0" for prompt_id in aios_kb_pilots_batch_ids)
    assert all("\n\nSubject logic:\n" in registry_by_id[prompt_id]["body"] for prompt_id in aios_kb_pilots_batch_ids)
    expected_bodies = {item["body"] for item in registry["prompts"]}
    exported_bodies = []
    for path in sorted(tmp_path.glob("B*.streamDeckProfile")):
        with zipfile.ZipFile(path) as archive:
            assert all(info.date_time == (1980, 1, 1, 0, 0, 0) for info in archive.infolist())
            for action in page_actions(archive).values():
                assert action["Settings"]["isSendingEnter"] is False
                assert action["Settings"]["isTypingMode"] is False
                exported_bodies.append(action["Settings"]["pastedText"])
    assert len(exported_bodies) == 225
    assert set(exported_bodies) == expected_bodies


def test_controller_export_is_serial_neutral(tmp_path: Path) -> None:
    result = run_export(tmp_path)
    assert result.returncode == 0, result.stderr
    with zipfile.ZipFile(tmp_path / "A00_CONTROL.streamDeckProfile") as archive:
        root_name = next(name for name in archive.namelist() if name.count("/") == 1 and name.endswith("manifest.json"))
        root = json.loads(archive.read(root_name))
        assert root["Device"]["UUID"] == ""
        actions = page_actions(archive)
        assert len(actions) == 15
        assert all(action["Settings"]["DeviceUUID"] == "" for action in actions.values())
        assert all(action["Settings"]["ProfileUUID"] for action in actions.values())
