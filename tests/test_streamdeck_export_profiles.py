from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import zipfile


REPO_ROOT = Path(__file__).resolve().parents[1]
STREAMDECK = REPO_ROOT / "StreamDeck"
EXPORTER = STREAMDECK / "tools" / "export_profiles.py"
APPROVED_REGISTRY_SHA256 = "d85df305d8a537df3b15eeeec0510607c8b1d84c28f47560ab9ce888fa22da82"


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


def test_export_is_deterministic_and_prompt_contracts_are_exact(tmp_path: Path) -> None:
    first = run_export(tmp_path)
    assert first.returncode == 0, first.stderr
    first_hashes = hashes(tmp_path)
    assert len(first_hashes) == 16

    second = run_export(tmp_path)
    assert second.returncode == 0, second.stderr
    assert hashes(tmp_path) == first_hashes

    registry_path = STREAMDECK / "prompts" / "prompt_registry.json"
    assert hashlib.sha256(registry_path.read_bytes()).hexdigest() == APPROVED_REGISTRY_SHA256
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    config = json.loads((STREAMDECK / "config" / "action_profiles.json").read_text(encoding="utf-8"))
    qa = json.loads((STREAMDECK / "qa" / "prompt_qa_matrix.json").read_text(encoding="utf-8"))

    assert registry["version"] == config["version"] == qa["version"] == "3.1.2"
    assert registry["prompt_count"] == len(registry["prompts"]) == 140
    assert len({item["prompt_id"] for item in registry["prompts"]}) == 140
    assert len(config["buttons"]) == 225
    assert all(item["insertion_method"] == "clipboard_paste" for item in config["buttons"])
    assert all(item["auto_send"] is False for item in config["buttons"])

    registry_by_id = {item["prompt_id"]: item for item in registry["prompts"]}
    qa_by_id = {item["prompt_id"]: item for item in qa["rows"]}
    refs_by_id: dict[str, list[str]] = {prompt_id: [] for prompt_id in registry_by_id}
    for row in config["buttons"]:
        prompt = registry_by_id[row["prompt_id"]]
        refs_by_id[row["prompt_id"]].append(f"{row['profile_id']}/{row['button']}")
        assert row["prompt_version"] == prompt["prompt_version"]
        assert row["owner_project"] == prompt["owner_project"]
        assert row["icon"] == f"assets/icons/action_{prompt['task_type']}.svg"

    for prompt_id, prompt in registry_by_id.items():
        assert hashlib.sha256(prompt["body"].encode()).hexdigest() == prompt["prompt_hash"]
        assert prompt["button_refs"] == refs_by_id[prompt_id]
        assert qa_by_id[prompt_id]["prompt_version"] == prompt["prompt_version"]
        assert qa_by_id[prompt_id]["prompt_hash"] == prompt["prompt_hash"]
        assert qa_by_id[prompt_id]["button_refs"] == prompt["button_refs"]

    expected_bodies = Counter(
        registry_by_id[row["prompt_id"]]["body"] for row in config["buttons"]
    )
    exported_bodies = []
    for path in sorted(tmp_path.glob("B*.streamDeckProfile")):
        with zipfile.ZipFile(path) as archive:
            assert all(info.date_time == (1980, 1, 1, 0, 0, 0) for info in archive.infolist())
            for action in page_actions(archive).values():
                assert action["Settings"]["isSendingEnter"] is False
                assert action["Settings"]["isTypingMode"] is False
                exported_bodies.append(action["Settings"]["pastedText"])
    assert len(exported_bodies) == 225
    assert Counter(exported_bodies) == expected_bodies


def test_controller_export_is_serial_neutral(tmp_path: Path) -> None:
    result = run_export(tmp_path)
    assert result.returncode == 0, result.stderr
    with zipfile.ZipFile(tmp_path / "A00_CONTROL.streamDeckProfile") as archive:
        root_name = next(
            name for name in archive.namelist()
            if name.count("/") == 1 and name.endswith("manifest.json")
        )
        root = json.loads(archive.read(root_name))
        assert root["Device"]["UUID"] == ""
        actions = page_actions(archive)
        assert len(actions) == 15
        assert all(action["Settings"]["DeviceUUID"] == "" for action in actions.values())
        assert all(action["Settings"]["ProfileUUID"] for action in actions.values())
