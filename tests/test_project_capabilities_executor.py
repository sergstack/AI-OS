"""Deterministic invariants for the PROJECT_CAPABILITIES executor block.

Covers the bounded "Supervised AI-OS subagent dispatch (pilot)" runtime
binding. These are structural contract checks only; they do not spawn agents.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = REPO_ROOT / "PROJECT_CAPABILITIES.yaml"

# The only executor backend the pilot verified on the Claude Code surface.
ALLOWED_BACKENDS = {"claude_code_subagent"}
# Built-in Claude Code agent types the pilot is allowed to use. "Plan" is
# read-only and cannot spawn nested agents; "general-purpose" is the only
# built-in that can perform repository writes.
ALLOWED_AGENT_TYPES = {"Plan", "general-purpose"}
WRITE_CAPABLE_AGENT_TYPES = {"general-purpose"}
EXECUTOR_KEYS = {
    "backend",
    "agent_type",
    "context_loader",
    "write_capable",
    "child_dispatch",
}


def load_registry() -> dict:
    # JSON is a YAML 1.2 subset; keeps the registry dependency-free.
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))


def capabilities() -> dict:
    return load_registry()["capabilities"]


def test_every_capability_has_a_well_formed_executor_block() -> None:
    for capability_id, capability in capabilities().items():
        executor = capability.get("executor")
        assert isinstance(executor, dict), f"{capability_id} missing executor"
        assert set(executor) == EXECUTOR_KEYS, f"{capability_id} executor key drift"
        assert executor["backend"] in ALLOWED_BACKENDS
        assert executor["agent_type"] in ALLOWED_AGENT_TYPES
        assert executor["context_loader"] == "project-context"
        assert isinstance(executor["write_capable"], bool)


def test_hub_and_spoke_child_dispatch_is_forbidden_everywhere() -> None:
    for capability_id, capability in capabilities().items():
        assert (
            capability["executor"]["child_dispatch"] == "forbidden"
        ), f"{capability_id} must forbid child->child dispatch"


def test_write_capability_is_minimised_to_implementation_only() -> None:
    write_capable = {
        capability_id
        for capability_id, capability in capabilities().items()
        if capability["executor"]["write_capable"]
    }
    assert write_capable == {"codex"}, (
        "only the implementation capability may hold a write-capable executor; "
        f"got {sorted(write_capable)}"
    )
    for capability_id, capability in capabilities().items():
        executor = capability["executor"]
        if executor["write_capable"]:
            assert executor["agent_type"] in WRITE_CAPABLE_AGENT_TYPES
        else:
            assert executor["agent_type"] not in WRITE_CAPABLE_AGENT_TYPES


def test_unknown_capability_fails_closed() -> None:
    caps = capabilities()
    assert "does_not_exist" not in caps
    with pytest.raises(KeyError):
        _ = caps["does_not_exist"]


def test_canonical_paths_are_bounded_and_unique() -> None:
    caps = capabilities()
    seen: set[str] = set()
    for capability_id, capability in caps.items():
        raw = capability["canonical_path"]
        path = Path(raw)
        assert not path.is_absolute(), f"{capability_id} canonical_path is absolute"
        assert ".." not in path.parts, f"{capability_id} canonical_path escapes root"
        resolved = (REPO_ROOT / path).resolve()
        assert resolved.is_relative_to(REPO_ROOT.resolve())
        assert resolved.is_dir(), f"{capability_id} canonical_path missing"
        assert raw not in seen, f"duplicate canonical_path {raw}"
        seen.add(raw)


def test_executor_without_a_verified_backend_cannot_claim_execution() -> None:
    """A capability whose executor backend is not in the verified allowlist
    must not be treated as executable. This guards against a future edit that
    adds an aspirational backend value."""
    caps = capabilities()
    executable = {
        capability_id
        for capability_id, capability in caps.items()
        if capability["executor"]["backend"] in ALLOWED_BACKENDS
    }
    # Today every capability is bound to the one verified backend.
    assert executable == set(caps)

    tampered = json.loads(json.dumps(caps))
    tampered["analytics"]["executor"]["backend"] = "imaginary_runtime"
    still_executable = {
        capability_id
        for capability_id, capability in tampered.items()
        if capability["executor"]["backend"] in ALLOWED_BACKENDS
    }
    assert "analytics" not in still_executable


def test_agent_loop_playbook_declares_the_pilot_carveout() -> None:
    playbook = (
        REPO_ROOT / "ChatGPT/[AI OS]/Knowledge/AGENT_LOOP_PLAYBOOK.md"
    ).read_text(encoding="utf-8")
    assert "Supervised AI-OS Subagent Dispatch (Pilot)" in playbook
    assert "hub-and-spoke only: `root -> child -> root`" in playbook
    assert "no `child -> child` delegation" in playbook
    assert "one AES `execution_id` for the whole user goal" in playbook


def test_orchestrator_skill_binds_dispatch_to_route_trace_and_root_only() -> None:
    skill = (
        REPO_ROOT / ".agents/skills/ai-os-orchestrator/SKILL.md"
    ).read_text(encoding="utf-8")
    assert "Native subagent dispatch (pilot)" in skill
    assert "backend: claude_code_subagent" in skill
    assert "continuation.route_trace" in skill
    assert "do not choose or invoke the next owner" in skill
    assert "repeat_route_refused_missing_evidence_delta" in skill
