# [Codex] Project Setup

## Что это

`[Codex]` — engineering command center для Codex / Claude Code: task packages, coding workflows, tests, smoke QA, acceptance, release и rollback.

## Что копировать в Project Instructions

Скопируй содержимое:

```text
Project/PROJECT_INSTRUCTIONS.md
```

## Что загружать в Knowledge

Загрузи все файлы из:

```text
Project/Knowledge/
```

## Файлы Knowledge

Основные:
- `AGENTS.md`
- `CLAUDE.md`
- `PROJECT_CONTEXT.md`
- `CODEX_HANDOFF_WORKFLOW.md`
- `TASK_TEMPLATE.md`
- `SUBAGENT_DECOMPOSITION.md`

Implementation:
- `DATA_PIPELINE_IMPLEMENTATION_WORKFLOW.md`
- `ANALYTICAL_MEMO_AUTOMATION_WORKFLOW.md`
- `REFACTORING_WORKFLOW.md`
- `BUGFIX_WORKFLOW.md`
- `TESTING_WORKFLOW.md`

QA / release:
- `SMOKE_QA_CHECKLIST.md`
- `ACCEPTANCE_CRITERIA.md`
- `REVIEW_CHECKLIST.md`
- `RELEASE_CHECKLIST.md`
- `FAILURE_MODES.md`
- `DONE_DEFINITION.md`

## Что не делать

Не давать Codex размытые задачи. Не разрешать изменения без scope, tests и acceptance criteria.
