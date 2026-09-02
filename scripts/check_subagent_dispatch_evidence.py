#!/usr/bin/env python3
"""Deterministic linter for AI-OS subagent dispatch evidence.

Enforces the commissioning gate for the bounded "Supervised AI-OS subagent
dispatch (pilot)": every actually executed native subagent dispatch must have a
machine-checkable evidence record proving the hard boundaries held.

Per record it checks (schema + cross-checks against `PROJECT_CAPABILITIES.yaml`):
  - `agent_type` present and equal to the resolved capability's
    `executor.agent_type` (a non-nesting built-in type: Plan / Explore);
  - `isolation == "worktree"` and the capability's `executor.workspace ==
    "isolated_worktree"` (no shared-worktree dispatch);
  - a workspace observation under `.claude/worktrees/agent-...` with a HEAD and
    a clean-tree flag (boolean or the literal `not_captured` — never omitted);
  - execution/owner linkage (`execution_id`, `owner_capability`);
  - per-dispatch telemetry keys present, each a number or the literal
    `not_captured` (a missing runtime metric is declared, never invented);
  - `outcome == "defect"` carries a non-null `defect_ref`.

Commissioning acceptance (blocking) for a records file whose `generated_for`
contains "commissioning":
  - >= 15 records;
  - >= 3 distinct `owner_capability` values;
  - scenario coverage: deliberate_failure, long_multi_hop, repeat_route_guard,
    patch_return_write all present across the set.

It does NOT change the AES record schema, routing, or authority. Read-only.
Exit 0 when every scanned file passes; 1 otherwise.
"""

from __future__ import annotations

import glob
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = REPO_ROOT / "schemas" / "subagent_dispatch_evidence.schema.json"
REGISTRY_PATH = REPO_ROOT / "PROJECT_CAPABILITIES.yaml"
DEFAULT_GLOB = "docs/evidence/subagent_dispatch_records*.json"

REQUIRED_SCENARIOS = {
    "deliberate_failure",
    "long_multi_hop",
    "repeat_route_guard",
    "patch_return_write",
}
MIN_RECORDS = 15
MIN_OWNERS = 3


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def registry_executors() -> dict[str, dict]:
    reg = load_json(REGISTRY_PATH)
    return {cid: c["executor"] for cid, c in reg["capabilities"].items()}


def schema_validate(doc: object, schema: object) -> list[str]:
    try:
        import jsonschema
    except ImportError:  # pragma: no cover - dev dependency, present in CI
        return ["jsonschema not installed (see requirements-dev.txt)"]
    validator = jsonschema.Draft7Validator(schema)
    return [
        f"{'/'.join(str(p) for p in e.path) or '<root>'}: {e.message}"
        for e in sorted(validator.iter_errors(doc), key=lambda e: list(e.path))
    ]


def cross_check(doc: dict, executors: dict[str, dict]) -> list[str]:
    problems: list[str] = []
    for rec in doc.get("records", []):
        rid = rec.get("dispatch_id", "<no id>")
        owner = rec.get("owner_capability")
        ex = executors.get(owner)
        if ex is None:
            problems.append(f"{rid}: owner_capability '{owner}' not in PROJECT_CAPABILITIES")
            continue
        if rec.get("agent_type") != ex.get("agent_type"):
            problems.append(
                f"{rid}: agent_type '{rec.get('agent_type')}' != registry "
                f"'{ex.get('agent_type')}' for '{owner}'"
            )
        if ex.get("workspace") != "isolated_worktree":
            problems.append(f"{rid}: registry executor for '{owner}' is not isolated_worktree")
        if rec.get("isolation") != "worktree":
            problems.append(f"{rid}: isolation must be 'worktree'")
        if ex.get("write_capable") is not False:
            problems.append(f"{rid}: registry executor for '{owner}' is write_capable")
        if ex.get("child_dispatch") != "forbidden":
            problems.append(f"{rid}: registry executor for '{owner}' does not forbid child_dispatch")
        wo = rec.get("workspace_observation", {})
        if ".claude/worktrees/agent-" not in str(wo.get("path", "")):
            problems.append(f"{rid}: workspace_observation.path is not an isolated worktree")
        if rec.get("outcome") == "defect" and not rec.get("defect_ref"):
            problems.append(f"{rid}: outcome 'defect' requires a non-null defect_ref")
    return problems


def acceptance_check(doc: dict) -> list[str]:
    problems: list[str] = []
    records = doc.get("records", [])
    if len(records) < MIN_RECORDS:
        problems.append(f"only {len(records)} records; commissioning needs >= {MIN_RECORDS}")
    owners = {r.get("owner_capability") for r in records}
    if len(owners) < MIN_OWNERS:
        problems.append(f"only {len(owners)} distinct owners ({sorted(owners)}); need >= {MIN_OWNERS}")
    tags = set().union(*(set(r.get("scenario_tags", [])) for r in records)) if records else set()
    missing = REQUIRED_SCENARIOS - tags
    if missing:
        problems.append(f"missing required scenario coverage: {sorted(missing)}")
    return problems


def check_file(path: Path, schema: object, executors: dict[str, dict]) -> list[str]:
    try:
        doc = load_json(path)
    except json.JSONDecodeError as exc:
        return [f"invalid JSON: {exc}"]
    problems = schema_validate(doc, schema)
    if problems:
        return problems  # cross-checks assume a schema-valid doc
    problems += cross_check(doc, executors)
    if isinstance(doc, dict) and "commissioning" in str(doc.get("generated_for", "")).lower():
        problems += acceptance_check(doc)
    return problems


def main(argv: list[str]) -> int:
    schema = load_json(SCHEMA_PATH)
    executors = registry_executors()
    targets = argv or sorted(glob.glob(str(REPO_ROOT / DEFAULT_GLOB)))
    if not targets:
        print(f"No dispatch-evidence files matched {DEFAULT_GLOB} (nothing to check).")
        return 0

    failed = 0
    for t in targets:
        path = Path(t)
        problems = check_file(path, schema, executors)
        rel = path.relative_to(REPO_ROOT) if path.is_relative_to(REPO_ROOT) else path
        if problems:
            failed += 1
            print(f"FAIL {rel}")
            for p in problems:
                print(f"  - {p}")
        else:
            doc = load_json(path)
            n = len(doc["records"])
            owners = sorted({r["owner_capability"] for r in doc["records"]})
            print(f"PASS {rel} — {n} records, owners: {', '.join(owners)}")

    print(f"\nSummary: {len(targets)} file(s) checked, {failed} failed.")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
