# Repository Paths

## ChatGPT Project Packages

- `ChatGPT/[AI OS]`
- `ChatGPT/[Thinking]`
- `ChatGPT/[Analytics]`
- `ChatGPT/[LLM]`
- `ChatGPT/[Codex]`
- `ChatGPT/[Inbox Router]`

## Executor Layer

- `Codex APP`

## Governance Checks

- `scripts/check_project_instructions_length.py`
- `scripts/check_repo_public_safety.py`
- `.github/workflows/docs-safety.yml`

## Project Instructions Rule

Every `PROJECT_INSTRUCTIONS.md` file must be <= 8000 characters.

## Local Path Placeholders

Do not commit raw machine-specific absolute paths.

- `<LOCAL_AI_OS_ROOT>`: local AI-OS repository root.
- `<LOCAL_REPO_ROOT>`: current local repository root.
- `<LOCAL_CODEX_APP_ROOT>`: local `Codex APP` folder.
- `<LOCAL_ARTIFACTS_ROOT>`: local working artifacts outside this public repository.
