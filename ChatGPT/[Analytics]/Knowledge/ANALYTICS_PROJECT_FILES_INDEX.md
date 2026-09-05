# Analytics Project Files Index

Назначение: навигация по файлам настройки проекта `[Analytics]`.

## Core files

| File | Purpose | Use when |
|---|---|---|
| `PROJECT_INSTRUCTIONS.md` | Главные инструкции проекта | Всегда; вставить в Project Instructions |
| `ANALYTICS_PROJECT_FILES_INDEX.md` | Индекс пакета | Нужно понять, какой файл использовать |
| `ANALYTICS_WORKFLOW.md` | End-to-end workflow | Любая аналитическая задача |
| `ANALYTICAL_REASONING_STANDARD.md` | P0 reasoning-control layer | Нужны intent, method plan, prerequisites, explanation challenge или claim calibration |
| `VARIANCE_DIAGNOSTIC_CONTRACT.md` | Material Plan/Fact variance runtime/output contract | Нужны sign normalization, gross bridge, attribution, coverage или evidence-constrained CFO synthesis |
| `IN_PROJECT_ANALYSIS_MODE.md` | Правило “анализ внутри проекта” | Есть риск преждевременного handoff |
| `MAIN_FILES_STANDARD.md` | Стандарт главных stage/mart файлов | Любые данные, marts, slices, BI/Excel |
| `DATA_CONTRACTS.md` | Data contract; canonical `VALUE_STATE` and `METRIC_DEFINITION_CARD` reference | Перед расчётами и marts; нужна семантика метрики или value-state |
| `QUANTITATIVE_SANITY_GATE.md` | Mandatory pre-publish quantitative sanity gate | Published quantitative report has a flagship metric |
| `AUTORESEARCH_STOCHASTICITY_NONINFERIORITY_METHOD.md` | AIOS AutoResearch v0.1 (issue #395) stochasticity/non-inferiority/decision-comparator method; candidate, provisional thresholds | Working on AutoResearch batch decision logic |
| `MANIFEST.md` | Package manifest | Когда нужно проверить состав Analytics package |
| `MARTS_DESIGN.md` | Проектирование marts | Нужны метрики, витрины, cuts, dashboard |
| `MEMO_FACTORY_DESIGN_HANDOFF.md` | Memo factory design handoff | Когда memo workflow требует implementation handoff |
| `ANALYTICAL_TECHNIQUES.md` | Методы анализа | Нужно выбрать variance/driver/bridge/etc. |
| `CHART_SELECTION_STANDARD.md` | Подбор графиков | Нужны графики из mart |
| `MEMO_PIPELINE.md` | Превращение анализа в memo | Нужна аналитическая записка |
| `MEMO_RUBRIC.md` | Memo quality rubric | Нужно оценить качество аналитической записки |
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
| `SMOKE_QA_RESULT.md` | Smoke QA result | Когда нужен последний зафиксированный smoke QA результат |
| `CHANGELOG.md` | История изменений | После обновлений |
| `../../../docs/standards/PARENT_CHILD_ISSUE_GATE_STANDARD.md` | Parent / child gate standard | Complex/high-risk analytics work needing sequenced issues, dependency gates, PR gates, final QA |

## Priority rules

1. Для аналитических задач сначала используй `ANALYTICS_WORKFLOW.md`, `IN_PROJECT_ANALYSIS_MODE.md`, `MAIN_FILES_STANDARD.md`.
2. Для данных и расчётов используй `DATA_CONTRACTS.md`, `MARTS_DESIGN.md`, `ANALYTICAL_TECHNIQUES.md`; для adaptive reasoning control — `ANALYTICAL_REASONING_STANDARD.md`; для material Plan/Fact diagnostics — `VARIANCE_DIAGNOSTIC_CONTRACT.md`.
3. Для memo/report используй `MEMO_PIPELINE.md`, `ANALYTICAL_MEMO_STRUCTURE.md`, `WORD_REPORT_STANDARD.md`, `TEXT_QA_AND_STYLE.md`.
4. Для QA используй `QA_CHECKLIST.md` и `ACCEPTANCE_CRITERIA.md`; перед
   публикацией quantitative report с flagship metric — `QUANTITATIVE_SANITY_GATE.md`.
5. Для передачи в Codex используй `CODEX_TASK_PACKETS.md` и `ROUTING_AND_HANDOFF.md`.
6. Для complex/high-risk analytics execution gates cite `Parent / Child Issue Gate Standard`; do not paste the full text.

## Non-negotiable rule

Не превращай `[Analytics]` в проект, который только выдаёт ТЗ. Он должен сам проводить анализ, если у него есть данные/контекст и задача не требует implementation.

## Bundle semantic migration sources

- `ANALYTICS_01_CORE_WORKFLOW_BUNDLE_SEMANTICS.md`
- `ANALYTICS_02_DATA_CONTRACTS_AND_MARTS_BUNDLE_SEMANTICS.md`
- `ANALYTICS_03_TECHNIQUES_AND_CHARTS_BUNDLE_SEMANTICS.md`
- `ANALYTICS_04_MEMO_AND_TEXT_STANDARDS_BUNDLE_SEMANTICS.md`
- `ANALYTICS_05_QA_GOVERNANCE_ROUTING_BUNDLE_SEMANTICS.md`
- `ANALYTICS_06_TEMPLATES_BUNDLE_SEMANTICS.md`
- `ANALYTICS_07_CODEX_HANDOFF_OPTIONAL_BUNDLE_SEMANTICS.md`
