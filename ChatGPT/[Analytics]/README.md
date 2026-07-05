# [Analytics] Project Settings Package

Назначение: полный пакет настройки папки `[Analytics]`, чтобы проект мог:

1. проводить анализ внутри проекта;
2. строить data contracts, stage, marts, QA и аналитические записки;
3. использовать обязательные главные файлы `stage_main_full`, `mart_main_full`, `mart_main_tz/compact`;
4. передавать задачи в `[Codex]`, `[LLM]`, `[Thinking]` или `[AI OS]` только когда это действительно нужно.

## Canonical GitHub path

Canonical project path:

`ChatGPT/[Analytics]`

The root-level path `/[Analytics]` is not the active source unless it is explicitly created later.

## Как загрузить

1. Скопируй содержимое `PROJECT_INSTRUCTIONS.md` в Project Instructions проекта `[Analytics]`.
2. Загрузи все файлы из папки `Knowledge/` в knowledge area проекта `[Analytics]`.
3. Файлы из `Templates/` можно загрузить как knowledge или держать как рабочие шаблоны.
4. Файлы из `Codex_Tasks/` используй для передачи задач в `[Codex]`, когда нужно изменить код/документы/автоматизацию.

ZIP — только транспортный архив. Не загружай ZIP как единственный knowledge source, если можно загрузить отдельные `.md` файлы.

## Главное поведение проекта

```text
Default: solve in [Analytics].
Handoff only when implementation, prompt orchestration, strategy decision, or AI OS evidence check is needed.
```

`[Analytics]` is the Analytics Factory for the full loop: question → data contract → stage → mart → deterministic calculation → findings → memo → judge/QA → revise/rerun → acceptance → next run.

## Upload order

1. `PROJECT_INSTRUCTIONS.md`
2. `Knowledge/ANALYTICS_PROJECT_FILES_INDEX.md`
3. `Knowledge/ANALYTICS_WORKFLOW.md`
4. `Knowledge/IN_PROJECT_ANALYSIS_MODE.md`
5. `Knowledge/MAIN_FILES_STANDARD.md`
6. Остальные файлы `Knowledge/`
7. `Templates/`
8. `Codex_Tasks/`

## What not to upload to ChatGPT Project Knowledge

Do not upload:

- `Codex_Tasks/`
- `.DS_Store`
- secrets / `.env` / credentials
- raw transcripts
- source cards
- chunks
- temp files
- logs
- embeddings
- vector DB
- web UI artifacts

## Package status

```text
status: ready_to_upload
production_readiness: not claimed
smoke_qa_status: repo_checks_passed / chatgpt_project_smoke_qa_pending
requires_pilot_case: yes
```
