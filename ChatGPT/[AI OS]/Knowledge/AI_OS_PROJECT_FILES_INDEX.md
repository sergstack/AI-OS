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
| `WEEKLY_AI_OS_REVIEW_TEMPLATE.md` | candidate template | Лёгкий weekly review: inputs, open loops, repo/sync/Stream Deck risks и один next action | Когда нужно выбрать одно следующее улучшение без task-manager слоя |
| `ARCHIVE_SUPERSEDED_RULE.md` | candidate rule | Traceability rule для archive / superseded статусов без auto-delete | Когда нужно убрать элемент из active layer с причиной, replacement/status и следом |
| `SMOKE_QA_FOR_AI_OS.md` | QA | Проверка, что проект отвечает по KB, а не из воздуха | После загрузки/обновления файлов |
| `ANTI_PATTERNS.md` | anti-patterns | Что нельзя делать в `[AI OS]` | Перед спорными или рискованными задачами |
| `AGENT_LOOP_PLAYBOOK.md` | loop governance | Supervised agent loops без autonomous agents и production agentic workflows | Когда нужно спроектировать или проверить bounded supervised loop |
| `AI_EVAL_REGISTRY.md` | eval registry | Лёгкий реестр AI evals по AI-OS проектам | Когда нужно выбрать eval status, verdict, owner project и pass/revise/blocked criteria |
| `AUTO_RESEARCH_BACKLOG.md` | backlog | Future research-loop ideas вне текущих production workflows | Когда AutoResearch или Karpathy-style loops обсуждаются как backlog или pilot candidates |
| `CROSS_PROJECT_EVAL_PLAYBOOK.md` | eval routing | Маршрутизация AI evals к правильному проекту и judge/check | Когда нужно оценить output между AI OS, LLM, Analytics, Codex, Thinking или loop design |
| `ACT_OR_ABSTAIN_EVAL_GATE.md` | eval gate | Проверяет, когда supervised workflow должен действовать или остановиться | Перед execution, change или supervised-loop continuation |
| `GOAL_CONSISTENCY_CLOSURE_CHECK.md` | closure eval | Проверяет исходную цель, acceptance и owner boundary поверх AES Closure Review | Перед terminal closure candidate result |
| `FAILURE_REGISTRY.md` | failure lifecycle | Фиксирует подтверждённый сбой и условную передачу в regression case | После observed workflow failure |
| `GOLDEN_EVAL_CASES.md` | eval cases | Reusable manual smoke QA cases для prompt, model или workflow changes | Когда нужно проверить eval behavior или judge drift |
| `JUDGE_CALIBRATION.md` | judge rules | Как AI-OS использует LLM-as-a-Judge, не считая judge output объективной истиной | Перед использованием или изменением judge workflows |
| `LOOP_ACCEPTANCE_CHECKLIST.md` | loop QA | Checklist для решения, безопасен ли supervised loop к запуску | Перед запуском или acceptance supervised loop |
| `SKILLS_HOOKS_MCP_DECISION_MATRIX.md` | tooling governance | Decision matrix для skills, hooks, MCP tools и sub-agents как workflow aids | Когда нужно решить, добавлять или использовать workflow tooling |
| `EXISTING_SCRIPT_CONTROLLED_REFACTOR_STANDARD.md` | engineering / Codex standard | Controlled cleanup/refactor of existing working scripts without behavior loss | Когда рабочий скрипт надо почистить: сначала baseline, output contract, safety tests, затем refactor |

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

## Bundle semantic migration sources

- `AIOS_01_ROUTING_AND_WORKFLOW_BUNDLE_SEMANTICS.md`
- `AIOS_02_GOVERNANCE_AND_EVIDENCE_BUNDLE_SEMANTICS.md`
- `AIOS_03_HANDOFF_AND_SMOKE_QA_BUNDLE_SEMANTICS.md`
- `AIOS_04_GOAL_PACKS_AND_COMMAND_SURFACE_BUNDLE_SEMANTICS.md`
