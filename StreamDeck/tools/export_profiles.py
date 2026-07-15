#!/usr/bin/env python3
"""Export deterministic candidate Stream Deck profiles from the v3 sources."""

from __future__ import annotations

import argparse
import json
import uuid
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "exports"
DEVICE_MODEL = "20GAA9901"  # Stream Deck 15-key; owner hardware import is NOT RUN.
ZIP_TIMESTAMP = (1980, 1, 1, 0, 0, 0)
NAMESPACE = uuid.UUID("af0d88d1-7e7d-5d70-998c-145a2369371c")


def load(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def stable_uuid(kind: str, value: str) -> uuid.UUID:
    return uuid.uuid5(NAMESPACE, f"ai-os-streamdeck-v3/{kind}/{value}")


def profile_uuid(profile_id: str) -> str:
    return str(stable_uuid("profile", profile_id)).upper()


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()


def coordinate(button: str) -> str:
    index = int(button.removeprefix("K")) - 1
    return f"{index % 5},{index // 5}"


def state(label: str, image_name: str) -> dict:
    return {
        "FontFamily": "",
        "FontSize": 9,
        "FontStyle": "",
        "FontUnderline": False,
        "Image": f"Images/{image_name}",
        "OutlineThickness": 2,
        "ShowTitle": True,
        "Title": f"{label}\n",
        "TitleAlignment": "bottom",
        "TitleColor": "#ffffff",
    }


def text_action(row: dict, prompt: dict, image_name: str) -> dict:
    if row.get("insertion_method") != "clipboard_paste":
        raise ValueError(f"unsupported insertion_method: {row.get('insertion_method')!r}")
    action_uuid = "com.elgato.streamdeck.system.text"
    return {
        "ActionID": str(stable_uuid("action", f"{row['profile_id']}/{row['button']}")),
        "LinkedTitle": True,
        "Name": "Text",
        "Plugin": {"Name": "Text", "UUID": action_uuid, "Version": "1.0"},
        "Resources": None,
        "Settings": {
            "Hotkey": {"KeyModifiers": 0, "QTKeyCode": 33554431, "VKeyCode": -1},
            "isSendingEnter": False,
            "isTypingMode": False,
            "pastedText": prompt["body"],
        },
        "State": 0,
        "States": [state(row["label"], image_name)],
        "UUID": action_uuid,
    }


def switch_action(row: dict, image_name: str) -> dict:
    action_uuid = "com.elgato.streamdeck.profile.rotate"
    return {
        "ActionID": str(stable_uuid("action", f"{row['profile_id']}/{row['button']}")),
        "LinkedTitle": True,
        "Name": "Switch Profile",
        "Plugin": {"Name": "Switch Profile", "UUID": action_uuid, "Version": "1.0"},
        "Resources": None,
        "Settings": {
            "DeviceUUID": "",
            "PageIndex": 0,
            "ProfileUUID": profile_uuid(row["target_profile_id"]),
        },
        "State": 0,
        "States": [state(row["label"], image_name)],
        "UUID": action_uuid,
    }


def archive_entries(profile_id: str, name: str, rows: list[dict], prompts: dict[str, dict]) -> dict[str, bytes]:
    root_id = profile_uuid(profile_id)
    page_id = str(stable_uuid("page", profile_id))
    default_id = str(stable_uuid("default-page", profile_id))
    root_dir = f"{root_id}.sdProfile"
    page_dir = f"{root_dir}/Profiles/{page_id.upper()}"
    default_dir = f"{root_dir}/Profiles/{default_id.upper()}"
    actions: dict[str, dict] = {}
    entries: dict[str, bytes] = {}

    for row in sorted(rows, key=lambda item: int(item["button"][1:])):
        icon_path = Path(row["icon"])
        image_name = icon_path.name
        source = ROOT / icon_path
        entries[f"{page_dir}/Images/{image_name}"] = source.read_bytes()
        if profile_id == "A00_CONTROL":
            actions[coordinate(row["button"])] = switch_action(row, image_name)
        else:
            actions[coordinate(row["button"])] = text_action(row, prompts[row["prompt_id"]], image_name)

    entries[f"{root_dir}/manifest.json"] = json_bytes({
        "Device": {"Model": DEVICE_MODEL, "UUID": ""},
        "Name": name,
        "Pages": {"Current": page_id, "Default": default_id, "Pages": [page_id]},
        "Version": "3.0",
    })
    entries[f"{page_dir}/manifest.json"] = json_bytes({
        "Controllers": [{"Actions": actions, "Type": "Keypad"}],
        "Icon": "",
        "Name": name,
    })
    entries[f"{default_dir}/manifest.json"] = json_bytes({
        "Controllers": [{"Actions": {}, "Type": "Keypad"}],
        "Icon": "",
        "Name": "",
    })
    return entries


def write_archive(path: Path, entries: dict[str, bytes]) -> None:
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name in sorted(entries):
            info = zipfile.ZipInfo(name, ZIP_TIMESTAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, entries[name], compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


def export_profiles(output_dir: Path) -> list[Path]:
    controller = load("config/controller_map.json")["buttons"]
    action_rows = load("config/action_profiles.json")["buttons"]
    registry = load("prompts/prompt_registry.json")["prompts"]
    icon_paths = {item["path"] for item in load("config/icon_map.json")["icons"]}
    prompts = {item["prompt_id"]: item for item in registry}
    rows_by_profile: dict[str, list[dict]] = {"A00_CONTROL": controller}
    names = {"A00_CONTROL": "AIOS-CONTROL"}

    for row in action_rows:
        rows_by_profile.setdefault(row["profile_id"], []).append(row)
        names[row["profile_id"]] = row["profile_name"]
    referenced_icons = {row["icon"] for row in controller + action_rows}
    if referenced_icons != icon_paths:
        raise ValueError("button icon references do not match config/icon_map.json")

    output_dir.mkdir(parents=True, exist_ok=True)
    outputs = []
    for profile_id in sorted(rows_by_profile):
        path = output_dir / f"{profile_id}.streamDeckProfile"
        write_archive(path, archive_entries(profile_id, names[profile_id], rows_by_profile[profile_id], prompts))
        outputs.append(path)
    return outputs


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    outputs = export_profiles(args.output_dir)
    print(f"EXPORTED: {len(outputs)} candidate profiles to {args.output_dir}")
    print("IMPORT NOT RUN: owner must import and bind controller actions to the physical Deck B")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
