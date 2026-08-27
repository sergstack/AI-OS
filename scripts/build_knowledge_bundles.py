#!/usr/bin/env python3
"""Deterministically render declared Knowledge bundle outputs."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


FORBIDDEN_PARTS = {".env", "archive", "logs", "runtime", "embeddings", "vector", "zip"}


def normalized(text: str) -> str:
    return "\n".join(line.rstrip() for line in text.splitlines() if line.strip()) + "\n"


def render(root: Path, item: dict[str, object]) -> str:
    sources = item["sources"]
    assert isinstance(sources, list) and sources
    digest = hashlib.sha256()
    sections = []
    for source in sources:
        assert isinstance(source, str)
        path = root / source
        if not path.is_file() or any(part.lower() in FORBIDDEN_PARTS for part in path.parts):
            raise ValueError(f"forbidden or missing source: {source}")
        text = normalized(path.read_text(encoding="utf-8"))
        digest.update(source.encode() + b"\0" + text.encode() + b"\0")
        sections.append(f"## From: `{source}`\n\n{text}")
    fingerprint = f"sha256:{digest.hexdigest()}"
    return ("# Generated Knowledge Bundle\n\n"
            "## Status\n\n"
            "- bundle_type: generated compact upload artifact\n"
            "- source_of_truth: declared granular source files\n"
            f"- source_fingerprint: {fingerprint}\n"
            "- generator: scripts/build_knowledge_bundles.py\n\n---\n\n# Content\n\n" + "\n".join(sections))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    if args.check == args.write:
        parser.error("choose exactly one of --check or --write")
    root = Path(__file__).resolve().parents[1]
    manifest = json.loads((root / "knowledge_bundle_manifest.json").read_text(encoding="utf-8"))
    if manifest.get("status") != "ready":
        raise SystemExit("BLOCKED: provenance audit is not ready; bundle writes are forbidden")
    stale = []
    for item in manifest["bundles"]:
        output = root / item["output"]
        expected = render(root, item)
        if args.check and output.read_text(encoding="utf-8") != expected:
            stale.append(str(item["output"]))
        elif args.write:
            output.write_text(expected, encoding="utf-8")
    if stale:
        print("STALE:\n" + "\n".join(stale))
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
