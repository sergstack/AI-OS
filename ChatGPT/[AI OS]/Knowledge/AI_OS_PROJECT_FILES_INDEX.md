# AI OS Project Files Index

Назначение: второй индекс для `[AI OS]`, только по рабочим файлам, которые добавляются этим пакетом.

## Два индекса в проекте

| Индекс | Статус | Для чего использовать |
|---|---|---|
| `KB__00_INDEX.md` | уже загруженный индекс governed KB | Поиск знаний, концепций, паттернов, workflows, evidence |
| `AI_OS_PROJECT_FILES_INDEX.md` | новый рабочий индекс | Настройки проекта, routing, usage rules, handoff, smoke QA |

## Новые файлы этого пакета

| Файл | Тип | Назначение | Когда использовать |
|---|---|---|---|
| `AI_OS_PROJECT_FILES_INDEX.md` | project index | Навигация по рабочим файлам пакета | Всегда, если вопрос про настройку проекта |
| `PROJECT_ROUTING.md` | routing rules | Маршрутизация между `[AI OS]`, `[Thinking]`, `[Analytics]`, `[LLM]`, `[Codex]` | Когда нужно определить, где решать задачу |
| `KB_USAGE_RULES.md` | KB usage | Как пользоваться KB, как отвечать с evidence/confidence | Перед любым grounded-ответом |
| `GOVERNANCE_RULES.md` | governance | Acceptance, promotion gates, review queue, blocked items | Когда вопрос касается статуса, готовности, promotion |
| `AI_OS_WORKFLOW.md` | workflow | Минимальный workflow ответа в `[AI OS]` | Для регулярной работы с вопросами |
| `HANDOFF_PROTOCOL.md` | handoff | Как передавать задачи в другие проекты | Когда результат должен уйти в Thinking/Analytics/LLM/Codex |
| `GITHUB_ISSUE_DRIVEN_HANDOFF.md` | handoff | Как оформлять handoff в GitHub Issue для `Codex` | Когда нужно передать repository work через issue-driven task package |
| `ANALYTICAL_MEMO_FACTORY_CODEX_APP_WORKFLOW.md` | workflow | Канонический путь создания аналитических записок через `[Analytics]` -> `[Codex]` -> Codex APP | Когда memo должен быть произведён как executable artifact |
| `SMOKE_QA_FOR_AI_OS.md` | QA | Проверка, что проект отвечает по KB, а не из воздуха | После загрузки/обновления файлов |
| `ANTI_PATTERNS.md` | anti-patterns | Что нельзя делать в `[AI OS]` | Перед спорными или рискованными задачами |

## Существующие KB-файлы, которые должны остаться основой

Минимальный ожидаемый набор уже загруженной KB:

```text
KB__00_INDEX.md
KB__01_NAVIGATION.md
KB__02_CONTENT.md
KB__03_WORKFLOWS_TRACEABILITY.md
KB__04_SMOKE_QA.md
KB__05_CANONICAL_CONCEPTS.md
KB__06_OPERATIONAL_FRAMEWORKS.md
KB__07_PATTERNS_AND_FAILURES.md
KB__08_USE_CASES_FOR_SERGEY.md
KB__CARD_SCHEMA.md
KB__CONFIDENCE_RULES.md
KB__PROMOTION_GATES.md
KB__RETRIEVAL_QA.md
KB__REVIEW_QUEUE.md
KB__RELEASE_MANIFEST.md
KB__USE_CASE_ROUTING.md
KB__DEDUPLICATION.md
KB__CHANGELOG.md
MANIFEST.md
SYNTHESIS_MANIFEST.md
README.md
```

## Правило приоритета

1. Для знаний и фактов сначала используй KB-файлы.
2. Для поведения проекта, routing и формата ответа используй рабочие файлы этого пакета.
3. Если есть конфликт: KB governance выше, чем рабочие настройки.
4. Если evidence weak/unsupported — не превращай вывод в факт.

## Статус пакета

- status: active project setting
- production promotion: no
- intended use: настройка поведения `[AI OS]`
- not intended use: замена governed KB
