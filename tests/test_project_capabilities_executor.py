"""Deterministic invariants for the PROJECT_CAPABILITIES executor block.

Covers the bounded "Supervised AI-OS subagent dispatch (pilot)" runtime
binding and the two hardened structural blockers:
  - DEF-001: every dispatch runs in an isolated git worktree;
  - no nested delegation: executors use agent types whose built-in tool set
    excludes the Agent tool, so a child cannot spawn a sub-agent and cannot
    write to the repository.

These are structural contract checks only; they do not spawn agents.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = REPO_ROOT / "PROJECT_CAPABILITIES.yaml"

# The only executor backend the pilot verified on the Claude Code surface.
ALLOWED_BACKENDS = {"claude_code_subagent"}
# Built-in Claude Code agent types whose tool set excludes the `Agent` tool
# (and `Write`/`Edit`): a child of one of these types is structurally unable to
# spawn a sub-agent or mutate the repo. This is the enforcement for
# `child_dispatch: forbidden` and `write_capable: false`.
NON_NESTING_AGENT_TYPES = {"Plan", "Explore"}
ALLOWED_WORKSPACES = {"isolated_worktree"}
EXECUTOR_KEYS = {
    "backend",
    "agent_type",
    "context_loader",
    "workspace",
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
        assert executor["agent_type"] in NON_NESTING_AGENT_TYPES
        assert executor["context_loader"] == "project-context"
        assert executor["workspace"] in ALLOWED_WORKSPACES
        assert isinstance(executor["write_capable"], bool)


def test_def_001_every_dispatch_is_workspace_isolated() -> None:
    """DEF-001 regression: no executor may run in the shared parent tree."""
    for capability_id, capability in capabilities().items():
        assert (
            capability["executor"]["workspace"] == "isolated_worktree"
        ), f"{capability_id} must dispatch into an isolated worktree"


def test_no_nested_delegation_is_structural_not_prompt_level() -> None:
    for capability_id, capability in capabilities().items():
        executor = capability["executor"]
        assert executor["child_dispatch"] == "forbidden"
        # The agent type itself must be one that cannot hold the Agent tool.
        assert executor["agent_type"] in NON_NESTING_AGENT_TYPES, (
            f"{capability_id}: child_dispatch:forbidden must be backed by a "
            f"non-nesting agent type, got {executor['agent_type']}"
        )


def test_no_child_is_write_capable() -> None:
    """The hardened pilot has no write-capable child; an implementation slice
    returns a patch and the root applies it."""
    write_capable = {
        capability_id
        for capability_id, capability in capabilities().items()
        if capability["executor"]["write_capable"]
    }
    assert write_capable == set(), (
        "no dispatched child may be write_capable; "
        f"got {sorted(write_capable)}"
    )


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
    must not be treated as executable. Guards against a future edit that adds
    an aspirational backend value."""
    caps = capabilities()
    executable = {
        capability_id
        for capability_id, capability in caps.items()
        if capability["executor"]["backend"] in ALLOWED_BACKENDS
    }
    assert executable == set(caps)

    tampered = json.loads(json.dumps(caps))
    tampered["analytics"]["executor"]["backend"] = "imaginary_runtime"
    still_executable = {
        capability_id
        for capability_id, capability in tampered.items()
        if capability["executor"]["backend"] in ALLOWED_BACKENDS
    }
    assert "analytics" not in still_executable


def test_agent_loop_playbook_declares_the_hardened_bounds() -> None:
    playbook = (
        REPO_ROOT / "ChatGPT/[AI OS]/Knowledge/AGENT_LOOP_PLAYBOOK.md"
    ).read_text(encoding="utf-8")
    assert "Supervised AI-OS Subagent Dispatch (Pilot)" in playbook
    assert "hub-and-spoke only: `root -> child -> root`" in playbook
    assert "excludes the `Agent` tool" in playbook
    assert 'every dispatch uses `isolation: "worktree"`' in playbook
    assert "one AES `execution_id` for the whole user goal" in playbook


def test_orchestrator_skill_binds_dispatch_to_isolation_and_root_only() -> None:
    raw = (
        REPO_ROOT / ".agents/skills/ai-os-orchestrator/SKILL.md"
    ).read_text(encoding="utf-8")
    skill = " ".join(raw.split())  # collapse line wrapping
    assert "Native subagent dispatch (pilot)" in skill
    assert "backend: claude_code_subagent" in skill
    assert 'with `isolation: "worktree"`' in skill
    assert "spawn a further sub-agent" in skill
    assert "root applies the patch and runs the validation" in skill
    assert "The root is the only writer." in skill
    assert "continuation.route_trace" in skill
    assert "repeat_route_refused_missing_evidence_delta" in skill
