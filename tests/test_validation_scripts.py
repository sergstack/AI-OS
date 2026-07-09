from __future__ import annotations

import importlib.util
from pathlib import Path
import subprocess
import sys
import textwrap


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = REPO_ROOT / "scripts"


def run_script(script_name: str, cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPTS_DIR / script_name)],
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def init_git_repo(path: Path) -> None:
    subprocess.run(["git", "init", "-q"], cwd=path, check=True)


def git_add(path: Path, *files: str) -> None:
    subprocess.run(["git", "add", *files], cwd=path, check=True)


def load_script_module(script_name: str):
    module_path = SCRIPTS_DIR / script_name
    spec = importlib.util.spec_from_file_location(module_path.stem, module_path)
    assert spec is not None
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[module_path.stem] = module
    spec.loader.exec_module(module)
    return module


def write_valid_upload_list(project_dir: Path, bundle_name: str) -> None:
    (project_dir / "Knowledge_Bundles" / "UPLOAD_LIST.md").write_text(
        textwrap.dedent(
            f"""\
            # Upload List

            ## Required upload files

            - `{bundle_name}`

            ## Optional upload files

            - `none`

            ## Do not upload

            - `PROJECT_INSTRUCTIONS.md` — paste into Project Instructions instead.

            ## File count

            Required: 1
            Optional: 0
            Total: 1
            Limit: 40
            Status: pass
            """
        ),
        encoding="utf-8",
    )


def write_bundle(
    project_dir: Path,
    bundle_name: str,
    source_path: str,
    source_fingerprint: str | None = None,
) -> None:
    fingerprint_line = (
        f"- source_fingerprint: {source_fingerprint}\n" if source_fingerprint else ""
    )
    (project_dir / "Knowledge_Bundles" / bundle_name).write_text(
        textwrap.dedent(
            f"""\
            # Test Bundle

            ## Purpose

            Minimal fixture.

            ## Source files

            - `{source_path}`

            ## Upload target

            Test project Knowledge.

            ## Status

            Test fixture only.
            {fingerprint_line}

            # Content

            Safe bundled content.
            """
        ),
        encoding="utf-8",
    )


def make_bundle_project(tmp_path: Path, bundle_name: str = "TEST_BUNDLE.md") -> tuple[Path, Path]:
    project_dir = tmp_path / "ChatGPT" / "[Test]"
    (project_dir / "Knowledge").mkdir(parents=True)
    (project_dir / "Knowledge_Bundles").mkdir()
    (project_dir / "Knowledge_Bundles" / "README.md").write_text(
        "Test bundle folder.\n", encoding="utf-8"
    )
    write_valid_upload_list(project_dir, bundle_name)
    return tmp_path, project_dir


def test_public_safety_flags_tracked_zip_archive(tmp_path: Path) -> None:
    init_git_repo(tmp_path)
    (tmp_path / "fixture.zip").write_bytes(b"PK\x03\x04")
    git_add(tmp_path, "fixture.zip")

    result = run_script("check_repo_public_safety.py", tmp_path)

    assert result.returncode == 1
    assert "Forbidden tracked zip archive: fixture.zip" in result.stdout


def test_public_safety_flags_files_inside_forbidden_vector_dirs(tmp_path: Path) -> None:
    init_git_repo(tmp_path)
    (tmp_path / "embeddings").mkdir()
    (tmp_path / "embeddings" / "notes.md").write_text("Safe text.\n", encoding="utf-8")
    git_add(tmp_path, "embeddings/notes.md")

    result = run_script("check_repo_public_safety.py", tmp_path)

    assert result.returncode == 1
    assert "Forbidden vector/embedding directory: embeddings/notes.md" in result.stdout


def test_public_safety_ignores_untracked_ignored_folders(tmp_path: Path) -> None:
    init_git_repo(tmp_path)
    (tmp_path / ".gitignore").write_text("local/\n", encoding="utf-8")
    (tmp_path / "safe.md").write_text("Safe markdown content.\n", encoding="utf-8")
    (tmp_path / "local").mkdir()
    (tmp_path / "local" / "ignored.zip").write_bytes(b"PK\x03\x04")
    git_add(tmp_path, ".gitignore", "safe.md")

    result = run_script("check_repo_public_safety.py", tmp_path)

    assert result.returncode == 0
    assert "Public safety check passed." in result.stdout


def test_public_safety_flags_tracked_unsafe_local_path(tmp_path: Path) -> None:
    init_git_repo(tmp_path)
    unsafe_path = "/" + "Users/alice/private/file.txt"
    (tmp_path / "notes.md").write_text(f"Do not reference {unsafe_path}\n", encoding="utf-8")
    git_add(tmp_path, "notes.md")

    result = run_script("check_repo_public_safety.py", tmp_path)

    assert result.returncode == 1
    assert "Absolute local path reference: notes.md" in result.stdout


def test_public_safety_allows_safe_markdown(tmp_path: Path) -> None:
    init_git_repo(tmp_path)
    (tmp_path / "README.md").write_text(
        "Safe project notes with relative/path.md only.\n", encoding="utf-8"
    )
    git_add(tmp_path, "README.md")

    result = run_script("check_repo_public_safety.py", tmp_path)

    assert result.returncode == 0
    assert "Public safety check passed." in result.stdout


def test_public_safety_flags_fake_token_in_python(tmp_path: Path) -> None:
    init_git_repo(tmp_path)
    fake_token = "ghp_" + "FAKEFAKEFAKEFAKEFAKE1234"
    (tmp_path / "script.py").write_text(
        f"TOKEN = '{fake_token}'\n", encoding="utf-8"
    )
    git_add(tmp_path, "script.py")

    result = run_script("check_repo_public_safety.py", tmp_path)

    assert result.returncode == 1
    assert "Possible secret/token pattern: script.py" in result.stdout


def test_public_safety_flags_fake_token_in_csv(tmp_path: Path) -> None:
    init_git_repo(tmp_path)
    fake_token = "sk-" + "FAKEFAKEFAKEFAKEFAKE1234"
    (tmp_path / "data.csv").write_text(
        f"name,token\nexample,{fake_token}\n", encoding="utf-8"
    )
    git_add(tmp_path, "data.csv")

    result = run_script("check_repo_public_safety.py", tmp_path)

    assert result.returncode == 1
    assert "Possible secret/token pattern: data.csv" in result.stdout


def test_codex_goal_mode_defaults_allows_scoped_strict_task_packages(tmp_path: Path) -> None:
    (tmp_path / "AGENTS.md").write_text(
        textwrap.dedent(
            """\
            Use Goal Mode by default.

            Strict task packages are reserved for high-risk, already-scoped,
            or explicitly requested work, and are not the default user burden.
            """
        ),
        encoding="utf-8",
    )

    result = run_script("check_codex_goal_mode_defaults.py", tmp_path)

    assert result.returncode == 0
    assert "Failed: 0" in result.stdout


def test_codex_goal_mode_defaults_rejects_atomic_task_package_default(tmp_path: Path) -> None:
    (tmp_path / "AGENTS.md").write_text(
        "Codex should work only by atomic task package.\n", encoding="utf-8"
    )

    result = run_script("check_codex_goal_mode_defaults.py", tmp_path)

    assert result.returncode == 1
    assert "forbidden atomic-only wording" in result.stdout


def test_project_instructions_length_passes_below_threshold(tmp_path: Path) -> None:
    (tmp_path / "PROJECT_INSTRUCTIONS.md").write_text("Short instructions.\n", encoding="utf-8")

    result = run_script("check_project_instructions_length.py", tmp_path)

    assert result.returncode == 0
    assert "Passed: 1" in result.stdout
    assert "Failed: 0" in result.stdout


def test_project_instructions_length_fails_above_threshold(tmp_path: Path) -> None:
    (tmp_path / "PROJECT_INSTRUCTIONS.md").write_text("x" * 8001, encoding="utf-8")

    result = run_script("check_project_instructions_length.py", tmp_path)

    assert result.returncode == 1
    assert "Failed: 1" in result.stdout
    assert "over_by=1" in result.stdout


def test_knowledge_bundles_passes_minimal_valid_fixture(tmp_path: Path) -> None:
    module = load_script_module("check_knowledge_bundles.py")
    root, project_dir = make_bundle_project(tmp_path)
    source = "ChatGPT/[Test]/Knowledge/source.md"
    (root / source).write_text("Source content.\n", encoding="utf-8")
    write_bundle(
        project_dir,
        "TEST_BUNDLE.md",
        source,
        module.source_fingerprint(root, [source]),
    )

    report = module.check_project(root, "[Test]", Path("ChatGPT/[Test]"))

    assert report.failures == []
    assert report.total_upload_files == 1
    assert report.source_paths is True


def test_knowledge_bundles_detects_stale_source_fingerprint(tmp_path: Path) -> None:
    module = load_script_module("check_knowledge_bundles.py")
    root, project_dir = make_bundle_project(tmp_path)
    source = "ChatGPT/[Test]/Knowledge/source.md"
    source_path = root / source
    source_path.write_text("Source content.\n", encoding="utf-8")
    write_bundle(
        project_dir,
        "TEST_BUNDLE.md",
        source,
        module.source_fingerprint(root, [source]),
    )
    source_path.write_text("Changed source content.\n", encoding="utf-8")

    report = module.check_project(root, "[Test]", Path("ChatGPT/[Test]"))

    assert any("source_fingerprint mismatch" in failure for failure in report.failures)
    assert report.source_paths is False


def test_index_coverage_passes_when_all_files_listed(tmp_path: Path) -> None:
    module = load_script_module("check_index_coverage.py")
    knowledge = tmp_path / "Knowledge"
    knowledge.mkdir()
    (knowledge / "LISTED.md").write_text("Content.\n", encoding="utf-8")
    (tmp_path / "INDEX.md").write_text("- `LISTED.md`\n", encoding="utf-8")

    failures = module.missing_from_index(tmp_path, "Knowledge", "INDEX.md")

    assert failures == []


def test_index_coverage_detects_unlisted_file(tmp_path: Path) -> None:
    module = load_script_module("check_index_coverage.py")
    knowledge = tmp_path / "Knowledge"
    knowledge.mkdir()
    (knowledge / "LISTED.md").write_text("Content.\n", encoding="utf-8")
    (knowledge / "MISSING.md").write_text("Content.\n", encoding="utf-8")
    (tmp_path / "INDEX.md").write_text("- `LISTED.md`\n", encoding="utf-8")

    failures = module.missing_from_index(tmp_path, "Knowledge", "INDEX.md")

    assert failures == ["INDEX.md does not list Knowledge/MISSING.md"]


def test_knowledge_bundles_detects_missing_referenced_source(tmp_path: Path) -> None:
    module = load_script_module("check_knowledge_bundles.py")
    root, project_dir = make_bundle_project(tmp_path)
    missing_source = "ChatGPT/[Test]/Knowledge/missing.md"
    write_bundle(project_dir, "TEST_BUNDLE.md", missing_source)

    report = module.check_project(root, "[Test]", Path("ChatGPT/[Test]"))

    assert any("source file missing" in failure for failure in report.failures)
    assert report.source_paths is False


def test_merge_gate_owner_tier_fails_closed() -> None:
    workflow = (REPO_ROOT / ".github" / "workflows" / "auto-merge.yml").read_text(
        encoding="utf-8"
    )

    assert "gh pr merge \"$PR_URL\" --disable-auto" in workflow
    assert "gh pr review \"$PR_URL\" --comment" in workflow
    assert "--request-changes" not in workflow
    assert "::error::Protected paths changed" in workflow
    assert "exit 1" in workflow


def test_merge_gate_protected_paths_match_codeowners_roots() -> None:
    workflow = (REPO_ROOT / ".github" / "workflows" / "auto-merge.yml").read_text(
        encoding="utf-8"
    )
    codeowners = (REPO_ROOT / ".github" / "CODEOWNERS").read_text(encoding="utf-8")
    codeowners_patterns = {
        line.split()[0]
        for line in codeowners.splitlines()
        if line.strip() and not line.startswith("#")
    }

    protected_paths = [
        ("AGENTS.md", "AGENTS.md"),
        ("CLAUDE.md", "CLAUDE.md"),
        ("GOAL_MODE.md", "GOAL_MODE.md"),
        ("GOAL_PACKS.md", "GOAL_PACKS.md"),
        ("COMMAND_SURFACE.md", "COMMAND_SURFACE.md"),
        ("CONTEXT_PACK_STANDARD.md", "CONTEXT_PACK_STANDARD.md"),
        ("MASTER_STATUS.md", "MASTER_STATUS.md"),
        ("CURRENT_STATUS.md", "CURRENT_STATUS.md"),
        ("SYNC_CONTRACT.md", "SYNC_CONTRACT.md"),
        ("README.md", "README.md"),
        ("MANIFEST.md", "MANIFEST.md"),
        ("MANIFEST.json", "MANIFEST.json"),
        ("PROJECT_REGISTRY.md", "PROJECT_REGISTRY.md"),
        ("PARENT_CHILD_ISSUE_GATE_STANDARD.md", "PARENT_CHILD_ISSUE_GATE_STANDARD.md"),
        ("EXISTING_SCRIPT_CONTROLLED_REFACTOR_STANDARD.md", "EXISTING_SCRIPT_CONTROLLED_REFACTOR_STANDARD.md"),
        ("ARCHIVE_MAP.md", "ARCHIVE_MAP.md"),
        ("UPLOAD_GUIDE.md", "UPLOAD_GUIDE.md"),
        ("REPO_PATHS.md", "REPO_PATHS.md"),
        ("docs/AI_DEVELOPMENT_WORKFLOW.md", "docs/AI_DEVELOPMENT_WORKFLOW.md"),
        ("docs/MERGE_GATE_OWNER_CHECKLIST.md", "docs/MERGE_GATE_OWNER_CHECKLIST.md"),
        ("ChatGPT/[AI OS]/Knowledge/AI_OS_PROJECT_FILES_INDEX.md", "ChatGPT/*/Knowledge/AI_OS_PROJECT_FILES_INDEX.md"),
        ("ChatGPT/[AI OS]/Knowledge/ARCHIVE_SUPERSEDED_RULE.md", "ChatGPT/*/Knowledge/ARCHIVE_SUPERSEDED_RULE.md"),
        ("ChatGPT/[AI OS]/Knowledge/GOVERNANCE_RULES.md", "ChatGPT/*/Knowledge/GOVERNANCE_RULES.md"),
        ("ChatGPT/[AI OS]/Knowledge/HANDOFF_PROTOCOL.md", "ChatGPT/*/Knowledge/HANDOFF_PROTOCOL.md"),
        ("ChatGPT/[AI OS]/Knowledge/KB_USAGE_RULES.md", "ChatGPT/*/Knowledge/KB_USAGE_RULES.md"),
        ("ChatGPT/[AI OS]/Knowledge/PROJECT_ROUTING.md", "ChatGPT/*/Knowledge/PROJECT_ROUTING.md"),
        ("scripts/", "scripts/"),
        ("tests/", "tests/"),
        (".github/", ".github/"),
        ("PROJECT_INSTRUCTIONS.md", "PROJECT_INSTRUCTIONS.md"),
    ]

    expected_codeowners_patterns = {f"/{pattern}" for _, pattern in protected_paths}
    expected_codeowners_patterns.remove("/PROJECT_INSTRUCTIONS.md")
    expected_codeowners_patterns.add("PROJECT_INSTRUCTIONS.md")
    assert codeowners_patterns == expected_codeowners_patterns

    for path, codeowners_pattern in protected_paths:
        workflow_pattern = path.replace(".", r"\.").replace("[", r"\[").replace("]", r"\]")
        assert codeowners_pattern in codeowners
        assert workflow_pattern in workflow or path in workflow
