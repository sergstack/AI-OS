#!/usr/bin/env python3
"""Deterministically render declared Knowledge bundle outputs."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re


FORBIDDEN_PARTS = {".env", "archive", "logs", "runtime", "embeddings", "vector", "zip"}
FINGERPRINT_PATTERN = re.compile(r"source_fingerprint:\s*(sha256:[0-9a-f]{64})")


def normalized(text: str) -> str:
    """Use LF, trim trailing whitespace, and omit blank lines deterministically."""
    return "\n".join(line.rstrip() for line in text.splitlines() if line.strip()) + "\n"


def source_material(root: Path, item: dict[str, object]) -> tuple[list[tuple[str, str]], str]:
    sources = list(item["sources"]) + list(item.get("migration_sources", []))
    assert isinstance(sources, list) and sources
    digest = hashlib.sha256()
    material = []
    for source in sources:
        assert isinstance(source, str)
        path = root / source
        if not path.is_file() or any(part.lower() in FORBIDDEN_PARTS for part in path.parts):
            raise ValueError(f"forbidden or missing source: {source}")
        raw = path.read_text(encoding="utf-8")
        text = normalized(raw)
        digest.update(source.encode() + b"\0" + raw.encode() + b"\0")
        material.append((source, text))
    return material, f"sha256:{digest.hexdigest()}"


def contract_for(item: dict[str, object]) -> dict[str, object]:
    """Return a declarative upload contract, with a safe test-only fallback."""
    contract = item.get("contract")
    if contract is None:
        return {"title": "Generated Knowledge Bundle", "purpose": "Deterministic upload artifact.", "upload_target": "ChatGPT Project Sources / Knowledge.", "status_lines": []}
    if not isinstance(contract, dict):
        raise ValueError("invalid bundle contract")
    for key in ("title", "purpose", "upload_target", "status_lines"):
        if key not in contract:
            raise ValueError(f"bundle contract missing {key}")
    if not all(isinstance(contract[key], str) for key in ("title", "purpose", "upload_target")):
        raise ValueError("bundle contract text fields must be strings")
    if not isinstance(contract["status_lines"], list) or not all(isinstance(line, str) for line in contract["status_lines"]):
        raise ValueError("bundle contract status_lines must be strings")
    return contract


def render(root: Path, item: dict[str, object]) -> str:
    material, fingerprint = source_material(root, item)
    contract = contract_for(item)
    status_lines = "\n".join(f"- {line}" for line in contract["status_lines"])
    stable_status = (status_lines + "\n" if status_lines else "")
    sources = "\n".join(f"- `{source}`" for source, _ in material)
    sections = "\n".join(f"## From: `{source}`\n\n{text}" for source, text in material)
    return (f"# {contract['title']}\n\n"
            f"## Purpose\n\n{contract['purpose']}\n\n"
            f"## Source files\n\n{sources}\n\n"
            f"## Upload target\n\n{contract['upload_target']}\n\n"
            "## Status\n\n"
            f"{stable_status}"
            "- bundle_type: generated compact upload artifact\n"
            "- source_of_truth: declared granular source files\n"
            f"- source_fingerprint: {fingerprint}\n"
            "- generator: scripts/build_knowledge_bundles.py\n\n---\n\n# Content\n\n"
            f"{sections}")


def expected_fingerprint(text: str) -> str | None:
    match = FINGERPRINT_PATTERN.search(text)
    return match.group(1) if match else None


def check(root: Path, manifest: dict[str, object]) -> list[str]:
    """Recompute expected outputs; hashes are evidence, never the only gate."""
    issues = []
    bundles = manifest.get("bundles")
    if not isinstance(bundles, list):
        return ["UNMAPPED_SOURCE: manifest bundles must be a list"]
    declared_outputs = set()
    for item in bundles:
        if not isinstance(item, dict) or not isinstance(item.get("output"), str):
            issues.append("UNMAPPED_SOURCE: manifest item has no output")
            continue
        output_rel = item["output"]
        declared_outputs.add(output_rel)
        try:
            expected = render(root, item)
        except ValueError as exc:
            message = str(exc)
            code = "FORBIDDEN_INPUT" if "forbidden" in message else "MISSING_SOURCE"
            issues.append(f"{code}: {output_rel}: {message}")
            continue
        output = root / output_rel
        if not output.is_file():
            issues.append(f"STALE_BUNDLE: {output_rel}: output is missing")
            continue
        actual = output.read_text(encoding="utf-8")
        if actual != expected:
            actual_fingerprint = expected_fingerprint(actual)
            expected_header_fingerprint = expected_fingerprint(expected)
            if actual_fingerprint != expected_header_fingerprint:
                issues.append(f"HASH_PROVENANCE_MISMATCH: {output_rel}")
            else:
                issues.append(f"STALE_BUNDLE: {output_rel}")
    for bundle_dir in sorted({(root / output).parent for output in declared_outputs}):
        for output in bundle_dir.glob("*.md"):
            relative = str(output.relative_to(root))
            if relative not in declared_outputs and "generator: scripts/build_knowledge_bundles.py" in output.read_text(encoding="utf-8"):
                issues.append(f"UNEXPECTED_GENERATED_OUTPUT: {relative}")
    return issues


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
        raise SystemExit("AUDIT_PENDING: provenance audit is not ready; bundle writes are forbidden")
    if args.check:
        issues = check(root, manifest)
        if issues:
            print("FAIL:\n" + "\n".join(issues))
            return 1
    else:
        for item in manifest["bundles"]:
            output = root / item["output"]
            output.write_text(render(root, item), encoding="utf-8")
    if args.check:
        print("PASS")
    else:
        print("WROTE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
