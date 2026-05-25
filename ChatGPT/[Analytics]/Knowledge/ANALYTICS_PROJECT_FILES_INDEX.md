# Analytics Project Files Index

Назначение: навигация по файлам настройки проекта `[Analytics]`.

## Core files

| File | Purpose | Use when |
|---|---|---|
| `PROJECT_INSTRUCTIONS.md` | Главные инструкции проекта | Всегда; вставить в Project Instructions |
| `ANALYTICS_PROJECT_FILES_INDEX.md` | Индекс пакета | Нужно понять, какой файл использовать |
| `ANALYTICS_WORKFLOW.md` | End-to-end workflow | Любая аналитическая задача |
| `IN_PROJECT_ANALYSIS_MODE.md` | Правило “анализ внутри проекта” | Есть риск преждевременного handoff |
| `MAIN_FILES_STANDARD.md` | Стандарт главных stage/mart файлов | Любые данные, marts, slices, BI/Excel |
| `DATA_CONTRACTS.md` | Data contract | Перед расчётами и marts |
| `MARTS_DESIGN.md` | Проектирование marts | Нужны метрики, витрины, cuts, dashboard |
| `ANALYTICAL_TECHNIQUES.md` | Методы анализа | Нужно выбрать variance/driver/bridge/etc. |
| `CHART_SELECTION_STANDARD.md` | Подбор графиков | Нужны графики из mart |
| `MEMO_PIPELINE.md` | Превращение анализа в memo | Нужна аналитическая записка |
| `ANALYTICAL_MEMO_STRUCTURE.md` | Структура записки | Нужно оформить выводы |
| `WORD_REPORT_STANDARD.md` | Word/DOCX стандарт | Нужна аналитическая записка в Word |
| `TEXT_QA_AND_STYLE.md` | Редактура и стиль | Нужно отладить текст и оформление |
| `QA_CHECKLIST.md` | Data/calculation/memo/doc QA | Перед публикацией результата |
| `ACCEPTANCE_CRITERIA.md` | Acceptance | Нужно принять результат |
| `ROUTING_AND_HANDOFF.md` | Routing | Нужно понять, куда передать задачу |
| `CODEX_TASK_PACKETS.md` | Пакетирование ТЗ для Codex | Нужно менять код/документы/автоматизацию |
| `AI_OS_REFERENCE.md` | Связь с AI OS | Нужны AI evidence/patterns |
| `GOVERNANCE_AND_ANTI_PATTERNS.md` | Governance and blockers | Риск unsupported claims |
| `SMOKE_QA_FOR_ANALYTICS.md` | Проверка проекта | После загрузки пакета |
| `CHANGELOG.md` | История изменений | После обновлений |

## Priority rules

1. Для аналитических задач сначала используй `ANALYTICS_WORKFLOW.md`, `IN_PROJECT_ANALYSIS_MODE.md`, `MAIN_FILES_STANDARD.md`.
2. Для данных и расчётов используй `DATA_CONTRACTS.md`, `MARTS_DESIGN.md`, `ANALYTICAL_TECHNIQUES.md`.
3. Для memo/report используй `MEMO_PIPELINE.md`, `ANALYTICAL_MEMO_STRUCTURE.md`, `WORD_REPORT_STANDARD.md`, `TEXT_QA_AND_STYLE.md`.
4. Для QA используй `QA_CHECKLIST.md` и `ACCEPTANCE_CRITERIA.md`.
5. Для передачи в Codex используй `CODEX_TASK_PACKETS.md` и `ROUTING_AND_HANDOFF.md`.

## Non-negotiable rule

Не превращай `[Analytics]` в проект, который только выдаёт ТЗ. Он должен сам проводить анализ, если у него есть данные/контекст и задача не требует implementation.
