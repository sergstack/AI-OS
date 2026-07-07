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


def write_bundle(project_dir: Path, bundle_name: str, source_path: str) -> None:
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
    write_bundle(project_dir, "TEST_BUNDLE.md", source)

    report = module.check_project(root, "[Test]", Path("ChatGPT/[Test]"))

    assert report.failures == []
    assert report.total_upload_files == 1
    assert report.source_paths is True


def test_knowledge_bundles_detects_missing_referenced_source(tmp_path: Path) -> None:
    module = load_script_module("check_knowledge_bundles.py")
    root, project_dir = make_bundle_project(tmp_path)
    missing_source = "ChatGPT/[Test]/Knowledge/missing.md"
    write_bundle(project_dir, "TEST_BUNDLE.md", missing_source)

    report = module.check_project(root, "[Test]", Path("ChatGPT/[Test]"))

    assert any("source file missing" in failure for failure in report.failures)
    assert report.source_paths is False
