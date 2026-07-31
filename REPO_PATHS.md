# Repository Paths

## ChatGPT Project Packages

- `ChatGPT/[AI OS]`
- `ChatGPT/[Thinking]`
- `ChatGPT/[Analytics]`
- `ChatGPT/[LLM]`
- `ChatGPT/[Codex]`
- `ChatGPT/[Inbox Router]`
- `ChatGPT/[Thinkers OS]`

## Executor Layer

- `Codex APP`

## Governance Checks

- `scripts/check_project_instructions_length.py`
- `scripts/check_repo_public_safety.py`
- `scripts/check_manifest_paths.py`
- `scripts/check_knowledge_bundles.py`
- `.github/workflows/docs-safety.yml`

## Operational Verification

- `CHATGPT_PROJECT_SYNC_CHECKLIST.md`
- `PROJECT_SYNC_TEMPLATE.md`
- `PILOT_CASES.md`
- `PILOT_RESULTS_TEMPLATE.md`
- `SMOKE_QA_REFRESH_PLAN.md`

## Knowledge Bundle Paths

- `ChatGPT/[AI OS]/Knowledge_Bundles`
- `ChatGPT/[Thinking]/Knowledge_Bundles`
- `ChatGPT/[Analytics]/Knowledge_Bundles`
- `ChatGPT/[LLM]/Knowledge_Bundles`
- `ChatGPT/[Codex]/Knowledge_Bundles`
- `ChatGPT/[Inbox Router]/Knowledge_Bundles`
- `ChatGPT/[Thinkers OS]/Knowledge_Bundles`

## Project Instructions Rule

Every `PROJECT_INSTRUCTIONS.md` file must be <= 8000 characters.

## Local Path Placeholders

Do not commit raw machine-specific absolute paths.

- `<LOCAL_AI_OS_ROOT>`: local AI-OS repository root.
- `<LOCAL_REPO_ROOT>`: current local repository root.
- `<LOCAL_CODEX_APP_ROOT>`: local `Codex APP` folder.
- `<LOCAL_ARTIFACTS_ROOT>`: local working artifacts outside this public repository.
