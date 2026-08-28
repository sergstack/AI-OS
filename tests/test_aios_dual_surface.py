from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = REPO_ROOT / "PROJECT_CAPABILITIES.yaml"
SKILLS_ROOT = REPO_ROOT / ".agents" / "skills"

EXPECTED_PROJECTS = {
    "ai_os": "ChatGPT/[AI OS]",
    "thinking": "ChatGPT/[Thinking]",
    "analytics": "ChatGPT/[Analytics]",
    "llm": "ChatGPT/[LLM]",
    "codex": "ChatGPT/[Codex]",
    "inbox_router": "ChatGPT/[Inbox Router]",
    "thinkers_os": "ChatGPT/[Thinkers OS]",
}


def load_registry() -> dict:
    # JSON is a YAML 1.2 subset and keeps this registry dependency-free.
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))


def registry_matches(registry: dict, routed_destination: str) -> list[str]:
    capabilities = registry["capabilities"]
    if routed_destination in capabilities:
        return [routed_destination]
    return sorted(
        capability_id
        for capability_id, capability in capabilities.items()
        if Path(capability["canonical_path"]).name == routed_destination
    )


def test_registry_is_location_resolver_only() -> None:
    registry = load_registry()

    assert registry["schema_version"] == 2
    assert set(registry) == {"schema_version", "capabilities"}
    assert set(registry["capabilities"]) == set(EXPECTED_PROJECTS)

    for capability_id, canonical_path in EXPECTED_PROJECTS.items():
        capability = registry["capabilities"][capability_id]
        assert set(capability) == {"canonical_path", "context_entrypoints"}
        assert capability["canonical_path"] == canonical_path


def test_context_entrypoints_exist_and_stay_within_canonical_project() -> None:
    registry = load_registry()

    for capability in registry["capabilities"].values():
        project = REPO_ROOT / capability["canonical_path"]
        entrypoints = capability["context_entrypoints"]
        assert entrypoints[0] == "PROJECT_INSTRUCTIONS.md"
        for relative_path in entrypoints:
            assert not Path(relative_path).is_absolute()
            resolved = (project / relative_path).resolve()
            assert resolved.is_relative_to(project.resolve())
            assert resolved.is_file()


def test_orchestrator_and_generic_project_context_are_the_only_skills() -> None:
    skill_files = sorted(
        path.relative_to(SKILLS_ROOT).as_posix()
        for path in SKILLS_ROOT.glob("*/SKILL.md")
    )
    assert skill_files == [
        "ai-os-orchestrator/SKILL.md",
        "project-context/SKILL.md",
    ]

    context = (SKILLS_ROOT / "project-context" / "SKILL.md").read_text(
        encoding="utf-8"
    )
    assert "does not classify the request or define domain methodology" in context
    assert "included files with selection reasons" in context
    assert "excluded candidates with reasons" in context
    assert "reject paths that escape it" in context


def test_orchestrator_is_thin_default_and_fails_closed() -> None:
    orchestrator = (
        SKILLS_ROOT / "ai-os-orchestrator" / "SKILL.md"
    ).read_text(encoding="utf-8")

    for canonical_reference in (
        "ROUTING_RULES.md",
        "PROJECT_CAPABILITIES.yaml",
        ".agents/skills/project-context/SKILL.md",
        "ChatGPT/[AI OS]/Knowledge/HANDOFF_PROTOCOL.md",
        "GOAL_MODE.md",
        "HANDOFF_STYLE_STANDARD.md",
        "AUTONOMOUS_EXECUTION_STANDARD.md",
    ):
        assert canonical_reference in orchestrator

    assert "exactly one primary owner capability" in orchestrator
    assert "Invoke or follow `project-context` only after" in orchestrator
    assert "Add capabilities only by handoff" in orchestrator
    assert "without a hardcoded label map" in orchestrator
    assert "zero or multiple registry matches are `blocked`" in orchestrator
    assert "do not invoke `project-context`" in orchestrator
    assert "Do not guess an owner" in orchestrator
    assert "load all projects" in orchestrator
    assert "status `blocked`" in orchestrator


def test_invoke_ai_os_continues_the_original_goal_without_expanding_authority() -> None:
    orchestrator = (
        SKILLS_ROOT / "ai-os-orchestrator" / "SKILL.md"
    ).read_text(encoding="utf-8")
    handoff = (
        REPO_ROOT / "ChatGPT/[AI OS]/Knowledge/HANDOFF_PROTOCOL.md"
    ).read_text(encoding="utf-8")
    smoke_qa = (
        REPO_ROOT / "ChatGPT/[AI OS]/Knowledge/SMOKE_QA_FOR_AI_OS.md"
    ).read_text(encoding="utf-8")

    assert "## Invoke AI-OS continuation mode" in orchestrator
    assert "original_goal" in orchestrator
    assert "original_acceptance_criteria" in orchestrator
    assert "Handoff completion is not goal completion." in orchestrator
    assert "return the result to the current owner" in orchestrator
    assert "reassess the original goal" in orchestrator
    assert "does not expand authority" in orchestrator
    assert "not a runtime service" in orchestrator
    assert "Never weaken acceptance criteria" in orchestrator
    assert "Execution lifecycle and warm resume" in orchestrator
    assert "continuation` envelope" in orchestrator
    assert "not terminate orchestration" in orchestrator
    assert "An unchanged source revision alone never permits warm resume." in orchestrator
    for terminal_outcome in (
        "`COMPLETED`",
        "`OWNER_DECISION_REQUIRED`",
        "`BLOCKED`",
    ):
        assert terminal_outcome in orchestrator

    assert "Handoff completion is not goal completion." in handoff
    assert "Destination вне `PROJECT_CAPABILITIES.yaml`" in handoff
    assert "explicit terminal handoff" in handoff
    assert "owner-frozen policy" in handoff

    root_agents = (REPO_ROOT / "AGENTS.md").read_text(encoding="utf-8")
    assert "local completion does not terminate the orchestration lifecycle" in root_agents

    for scenario in (
        "### 6. Safe continuation",
        "### 7. Handoff is not completion",
        "### 8. Owner authority",
        "### 9. Corrective continuation",
        "### 10. External destination",
    ):
        assert scenario in smoke_qa


def test_orchestrator_references_canonical_routing_instead_of_copying_it() -> None:
    orchestrator = (
        SKILLS_ROOT / "ai-os-orchestrator" / "SKILL.md"
    ).read_text(encoding="utf-8")

    assert "Do not copy their routing tables" in orchestrator
    assert "Calculation / data / metrics" not in orchestrator
    assert "Prompt / model routing / LLM workflow" not in orchestrator
    assert "Implementation / code / tests / release" not in orchestrator


def test_current_repository_passes_sync_readiness_checks() -> None:
    result = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "sync_aios.py")],
        cwd=REPO_ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )

    assert result.returncode == 0, result.stdout + result.stderr
    for check in (
        "scripts/check_project_instructions_length.py",
        "scripts/check_repo_public_safety.py",
        "scripts/check_codex_goal_mode_defaults.py",
        "scripts/check_manifest_paths.py",
        "scripts/check_knowledge_bundles.py",
        "scripts/check_index_coverage.py",
    ):
        assert f"PASS {check}" in result.stdout


def test_registry_derived_resolution_is_unique_and_fail_closed() -> None:
    registry = load_registry()

    assert registry_matches(registry, "thinking") == ["thinking"]
    assert registry_matches(registry, "[Thinking]") == ["thinking"]
    assert registry_matches(registry, "Codex APP") == []
    assert registry_matches(registry, "[Missing]") == []

    ambiguous = json.loads(json.dumps(registry))
    ambiguous["capabilities"]["thinking_duplicate"] = {
        "canonical_path": "Shadow/[Thinking]",
        "context_entrypoints": ["PROJECT_INSTRUCTIONS.md"],
    }
    assert registry_matches(ambiguous, "[Thinking]") == [
        "thinking",
        "thinking_duplicate",
    ]


def test_missing_canonical_path_blocks_before_context_loading(tmp_path: Path) -> None:
    registry = load_registry()
    capability_id = registry_matches(registry, "[Thinking]")[0]
    capability = registry["capabilities"][capability_id]
    missing_root = tmp_path / capability["canonical_path"]

    assert not missing_root.exists()
    assert capability["context_entrypoints"][0] == "PROJECT_INSTRUCTIONS.md"


def test_orchestrator_is_the_default_goal_entrypoint() -> None:
    agents = (REPO_ROOT / "AGENTS.md").read_text(encoding="utf-8")
    goal_mode = (REPO_ROOT / "GOAL_MODE.md").read_text(encoding="utf-8")
    commands = (REPO_ROOT / "docs/standards/COMMAND_SURFACE.md").read_text(encoding="utf-8")

    assert "use `ai-os-orchestrator` as the default entrypoint" in agents
    assert "Simple local, reversible repository work" in agents
    assert "canonical `ai-os-orchestrator` skill" in goal_mode
    assert "`AI-OS Goal` is the default when no route is supplied" in commands


def test_root_routing_rules_own_domain_routing_semantics() -> None:
    routing = (REPO_ROOT / "ROUTING_RULES.md").read_text(encoding="utf-8")

    for destination in (
        "`[AI OS]`",
        "`[Thinkers OS]`",
        "`[Thinking]`",
        "`[Analytics]`",
        "`[LLM]`",
        "`[Codex]`",
        "`[Inbox Router]`",
    ):
        assert destination in routing


def test_handoff_style_standard_is_the_only_field_set_owner() -> None:
    fields = (
        "From:",
        "To:",
        "Task type:",
        "Mode:",
        "Objective:",
        "Context:",
        "Inputs:",
        "Constraints:",
        "Expected output:",
        "Acceptance criteria:",
        "Risks:",
        "Evidence / confidence:",
        "Open questions:",
        "Suggested first step:",
    )
    owners = []
    for path in REPO_ROOT.rglob("*.md"):
        relative = path.relative_to(REPO_ROOT)
        if any(part in {"archive", "Knowledge_Bundles"} for part in relative.parts):
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        if all(field in text for field in fields):
            owners.append(relative.as_posix())

    assert owners == ["HANDOFF_STYLE_STANDARD.md"]


def test_root_agents_uses_canonical_routing_and_bounded_context() -> None:
    agents = (REPO_ROOT / "AGENTS.md").read_text(encoding="utf-8")

    assert "## Domain Capability Discovery" in agents
    assert "classify the request using canonical routing rules" in agents
    assert "use `project-context` only after routing" in agents
    assert agents.count("## Domain Capability Discovery") == 1


def test_protected_chatgpt_architecture_is_present() -> None:
    for canonical_path in EXPECTED_PROJECTS.values():
        project = REPO_ROOT / canonical_path
        assert project.is_dir()
        assert (project / "PROJECT_INSTRUCTIONS.md").is_file()
        assert (project / "Knowledge").is_dir()
        assert (project / "Knowledge_Bundles").is_dir()


def test_phase1_files_pass_existing_public_safety_validator(tmp_path: Path) -> None:
    phase1_files = [
        REPO_ROOT / "AGENTS.md",
        REGISTRY_PATH,
        Path(__file__),
        *(SKILLS_ROOT.rglob("*")),
        *((REPO_ROOT / "archive" / "implementation_evidence" / "aios_dual_surface_phase1").rglob("*")),
    ]

    for source in phase1_files:
        if not source.is_file():
            continue
        relative_path = source.relative_to(REPO_ROOT)
        destination = tmp_path / relative_path
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(source.read_bytes())

    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    subprocess.run(["git", "add", "--all"], cwd=tmp_path, check=True)
    result = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "check_repo_public_safety.py")],
        cwd=tmp_path,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )

    assert result.returncode == 0, result.stdout + result.stderr
    assert "Public safety check passed." in result.stdout
