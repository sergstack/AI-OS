#!/usr/bin/env python3
"""Verify immutable live benchmark definition hashes."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    manifest = json.loads((HERE / "freeze_manifest.json").read_text(encoding="utf-8"))
    actual = {relative: sha((HERE / relative).resolve()) for relative in manifest["file_hashes"]}
    if actual != manifest["file_hashes"]:
        missing = [relative for relative in actual if actual[relative] != manifest["file_hashes"][relative]]
        raise SystemExit(f"freeze mismatch: {missing}")
    serialized = "".join(f"{relative}\0{digest}\n" for relative, digest in sorted(actual.items()))
    serialized += f"sealed_holdout\0{manifest['sealed_holdout_sha256']}\n"
    benchmark_hash = hashlib.sha256(serialized.encode()).hexdigest()
    if benchmark_hash != manifest["benchmark_hash"]:
        raise SystemExit("benchmark hash mismatch")
    cases = json.loads((HERE / "cases.json").read_text(encoding="utf-8"))
    if [case["case_id"] for case in cases] != manifest["public_case_ids"]:
        raise SystemExit("case ID order mismatch")
    print(f"PASS benchmark_version={manifest['benchmark_version']} benchmark_hash={benchmark_hash}")


if __name__ == "__main__":
    main()
