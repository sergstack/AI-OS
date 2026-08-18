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


def test_only_generic_project_context_skill_remains() -> None:
    skill_files = sorted(
        path.relative_to(SKILLS_ROOT).as_posix()
        for path in SKILLS_ROOT.glob("*/SKILL.md")
    )
    assert skill_files == ["project-context/SKILL.md"]

    context = (SKILLS_ROOT / "project-context" / "SKILL.md").read_text(
        encoding="utf-8"
    )
    assert "does not classify the request or define domain methodology" in context
    assert "included files with selection reasons" in context
    assert "excluded candidates with reasons" in context
    assert "reject paths that escape it" in context


def test_canonical_inbox_router_owns_domain_routing_semantics() -> None:
    routing = (
        REPO_ROOT / "ChatGPT/[Inbox Router]/Knowledge/ROUTING_RULES.md"
    ).read_text(encoding="utf-8")

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


def test_root_agents_uses_canonical_routing_and_bounded_context() -> None:
    agents = (REPO_ROOT / "AGENTS.md").read_text(encoding="utf-8")

    assert "## Domain Capability Discovery" in agents
    assert "classify the request using canonical routing rules" in agents
    assert "use `project-context` to load only task-relevant canonical files" in agents
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
        *((REPO_ROOT / "docs" / "aios_dual_surface_phase1").rglob("*")),
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
