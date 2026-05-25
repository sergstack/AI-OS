# [Codex] Project Setup

## Что это

`[Codex]` — engineering command center для Codex / Claude Code: task packages, coding workflows, tests, smoke QA, acceptance, release и rollback.

## Что копировать в Project Instructions

Скопируй содержимое:

```text
ChatGPT/[Codex]/PROJECT_INSTRUCTIONS.md
```

## Что загружать в Knowledge

Загрузи все файлы из:

```text
ChatGPT/[Codex]/Knowledge/
```

## Файлы Knowledge

- `ACCEPTANCE_CRITERIA.md`
- `AGENTS.md`
- `AI_OS_REFERENCE.md`
- `ANALYTICAL_MEMO_AUTOMATION_WORKFLOW.md`
- `ANALYTICAL_TECHNIQUES_FOR_CODEX.md`
- `BUGFIX_WORKFLOW.md`
- `CLAUDE.md`
- `CLAUDE_CODE_HANDOFF.md`
- `CODEX_HANDOFF_WORKFLOW.md`
- `DATA_PIPELINE_IMPLEMENTATION_WORKFLOW.md`
- `DONE_DEFINITION.md`
- `FAILURE_MODES.md`
- `KESTRA_AUTOMATION_STANDARD_REFERENCE.md`
- `PROJECT_CONTEXT.md`
- `PROMPT_LIBRARY_CODEX.md`
- `REFACTORING_WORKFLOW.md`
- `RELEASE_CHECKLIST.md`
- `REVIEW_CHECKLIST.md`
- `SMOKE_QA_CHECKLIST.md`
- `SUBAGENT_DECOMPOSITION.md`
- `TASK_TEMPLATE.md`
- `TESTING_WORKFLOW.md`

## What not to upload to ChatGPT Project Knowledge

Do not upload:

- `Codex_App/`
- `.gitkeep`
- secrets / `.env` / credentials
- raw transcripts
- source cards
- chunks
- temp files
- logs
- embeddings
- vector DB
- web UI artifacts

## Codex APP compatibility

Task packages produced in this ChatGPT Project should be executable by `Codex APP`.
Use `Codex APP/CODEX_APP_TASK_PACKAGE_CONTRACT.md` and `Codex APP/CODEX_APP_INTAKE_GATE.md` as the receiving-side contract.

## Что не делать

Не давать Codex размытые задачи. Не разрешать изменения без scope, tests и acceptance criteria.
