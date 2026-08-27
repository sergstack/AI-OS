# [AI OS] — Routing and Workflow

## Purpose

Compact upload artifact for [AI OS] covering routing, workflow, and engineering/Codex standards discoverability.

## Source files

- `ChatGPT/[AI OS]/Knowledge/AI_OS_PROJECT_FILES_INDEX.md`
- `ChatGPT/[AI OS]/Knowledge/PROJECT_ROUTING.md`
- `ChatGPT/[AI OS]/Knowledge/AI_OS_WORKFLOW.md`
- `ChatGPT/[AI OS]/Knowledge/KB_USAGE_RULES.md`
- `ChatGPT/[AI OS]/Knowledge/ANALYTICAL_MEMO_FACTORY_CODEX_APP_WORKFLOW.md`
- `EXISTING_SCRIPT_CONTROLLED_REFACTOR_STANDARD.md`
- `ChatGPT/[AI OS]/Knowledge/AIOS_01_ROUTING_AND_WORKFLOW_BUNDLE_SEMANTICS.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[AI OS]`.

## Status

- production_promotion: no, unless explicitly accepted elsewhere
- bundle_type: generated compact upload artifact
- source_of_truth: declared granular source files
- source_fingerprint: sha256:94da7cde082b00946d33ac4c2bfaa64bb1765e45902dfd040193bb4cca504d45
- generator: scripts/build_knowledge_bundles.py

---

# Content

## From: `ChatGPT/[AI OS]/Knowledge/AI_OS_PROJECT_FILES_INDEX.md`

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
| `REGRESSION_GATE.md` | comparison eval | Сравнивает accepted baseline и candidate без aggregate-score обхода hard regressions | Перед owner acceptance изменения workflow |
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

## From: `ChatGPT/[AI OS]/Knowledge/PROJECT_ROUTING.md`

# Project Routing
Назначение: определить, в каком ChatGPT Project должна решаться задача.
Scope note: this file is the `[AI OS]` project routing and handoff reference.
Canonical front-door routing lives in `ROUTING_RULES.md`. This file owns only
the `[AI OS]` scope; it does not define destination rows or handoff fields.
## Что делает [AI OS]
[AI OS] отвечает на вопросы:
1. Что это такое и как работает?
2. Какие паттерны уже проверены?
3. Как применить к работе Сергея?
4. Что в KB supported, weak, mixed, unsupported или not found?
5. Какой проект должен решать следующую часть задачи?
## Что [AI OS] не делает
- Не выполняет финансовый анализ.
- Не пишет и не меняет код.
- Не запускает pipeline.
- Не делает production execution.
- Не принимает стратегическое решение вместо `[Thinking]`.
- Не заменяет `[LLM]` как операционный оркестратор.
- Не заменяет `[Thinkers OS]` как владельца author corpus, source provenance и thinker artifacts.
Правило владения `[LLM]`: для reusable prompt, выбора model class, LLM workflow,
orchestration или eval design направь задачу в `[LLM]` с фокусным, исполнимым
handoff. Сохрани релевантные evidence/governance context, запрошенный результат,
критерии приёмки и следующий шаг; не убирай сведения, нужные для продолжения
работы. `[AI OS]` может уточнить границы и evidence, но не выбирает модель, не
пишет prompt и не проектирует LLM workflow.
## Handoff rule
Use the canonical template in `HANDOFF_STYLE_STANDARD.md`; retain the relevant
evidence, constraints, acceptance checks, and next step.

## From: `ChatGPT/[AI OS]/Knowledge/AI_OS_WORKFLOW.md`

# AI OS Workflow
Назначение: минимальный рабочий процесс ответа внутри `[AI OS]`.
## Workflow: grounded AI trend / tool / pattern answer
| Step | Действие | Output |
|---|---|---|
| 1 | Определи тип вопроса | concept / use case / comparison / next step / routing |
| 2 | Проверь KB по приоритету | список файлов и найденных фрагментов |
| 3 | Раздели evidence | supported / weak / mixed / unsupported / not found |
| 4 | Сформулируй ответ | объяснение, применение, риски |
| 5 | Привяжи к работе Сергея | практический use case или ограничение |
| 6 | Определи routing | остаться в `[AI OS]` или передать дальше |
| 7 | Дай next step | одно конкретное действие |
## Шаблон ответа
```text
KB проверен: да
Источники: [...]
Найдено в KB: да / нет / частично
Confidence: strong / medium / weak
Evidence: supported / weak / mixed / not found
Суть:
...
Как это работает:
...
Применение для Сергея:
...
Риски и ограничения:
...
Routing:
...
Итог:
...
Next step:
...
```
## Режимы работы
| Режим | Когда использовать | Результат |
|---|---|---|
| `@analyst` | нужно разобраться в концепции, фактах, данных, вариантах | structured analysis |
| `@judge` | нужно проверить слабые места, evidence, риски | critique / risk list |
| `@revisor` | нужно улучшить формулировку или упаковать ответ | revised output |
| `@ai_operator` | нужно упаковать результат в файлы, инструкции, checklist | file-ready package |
## Engineering / Codex standards
`Existing Script Controlled Refactor Standard` is an engineering/Codex standard for cleaning an existing working script or pipeline without behavior loss.
Use it only when current output is useful and must be preserved. Required order: baseline current behavior, define output contract, add safety tests, then clean/refactor and compare before/after output.
Do not treat this as Analytics material. `[Analytics]` defines analytical methodology, metrics, formulas, marts, and business definitions; Codex applies engineering safety around implementation and refactor work.
## Важное ограничение
[AI OS] не выполняет операционные действия. Если нужен code execution, пайплайн, аналитический расчёт или production task — подготовь handoff в правильный проект.

## From: `ChatGPT/[AI OS]/Knowledge/KB_USAGE_RULES.md`

# KB Usage Rules
Назначение: правила использования governed KB внутри `[AI OS]`.
## 1. С чего начинать
Для любого содержательного ответа сначала проверь KB.
Приоритет:
```text
1. KB__08_USE_CASES_FOR_SERGEY.md
2. KB__07_PATTERNS_AND_FAILURES.md
3. KB__06_OPERATIONAL_FRAMEWORKS.md
4. KB__05_CANONICAL_CONCEPTS.md
5. KB__03_WORKFLOWS_TRACEABILITY.md
6. KB__USE_CASE_ROUTING.md
7. KB__CONFIDENCE_RULES.md
8. KB__REVIEW_QUEUE.md
9. KB__RELEASE_MANIFEST.md
10. KB__00_INDEX.md
```
Для настройки проекта используй также:
```text
AI_OS_PROJECT_FILES_INDEX.md
PROJECT_ROUTING.md
GOVERNANCE_RULES.md
AI_OS_WORKFLOW.md
HANDOFF_PROTOCOL.md
```
## 2. Стандартная шапка ответа
```text
KB проверен: да / нет
Источники: [список файлов]
Найдено в KB: да / нет / частично
Confidence: strong / medium / weak
Evidence: supported / weak / mixed / not found
```
## 3. Evidence labels
| Label | Значение | Как использовать |
|---|---|---|
| supported | подтверждено KB | Можно использовать уверенно |
| weak | слабое evidence / интерпретация | Отмечать как гипотезу или осторожную рекомендацию |
| mixed | источники дают разные сигналы | Показать варианты и риск |
| unsupported | не найдено в KB | Не использовать как факт |
| not found | KB не содержит данных | Сказать прямо, не придумывать |
## 4. Facts vs interpretation
Разделяй:
```text
FACT — подтверждено KB или предоставленными файлами.
INTERPRETATION — логический вывод из фактов.
RECOMMENDATION — практический совет.
HYPOTHESIS — полезная идея без достаточного evidence.
BLOCKER — что нельзя внедрять без проверки.
```
## 5. Когда использовать web
Используй web-проверку, если вопрос касается:
- текущих релизов моделей;
- актуальных API, pricing, limits;
- новых AI-инструментов;
- текущих возможностей OpenAI/Anthropic/Google/Meta/Mistral/etc.;
- свежих benchmark или market facts;
- любых фактов, которые могли измениться.
Отделяй:
```text
KB knowledge: ...
Fresh external check: ...
```
## 6. Что нельзя делать
- Не придумывать факты, если KB пустая.
- Не превращать weak evidence в supported.
- Не скрывать review queue.
- Не игнорировать release manifest.
- Не смешивать source fact, QA recommendation и собственную гипотезу.
- Не рекомендовать blocked promotion items до gates.
## 7. Финальный блок
```text
Итог:
[короткий вывод]
Next step:
[одно конкретное действие]
```

## From: `ChatGPT/[AI OS]/Knowledge/ANALYTICAL_MEMO_FACTORY_CODEX_APP_WORKFLOW.md`

# Analytical Memo Factory via Codex APP
## Purpose
Canonical workflow for producing analytical memos as executable artifacts through Codex APP while keeping project roles separate.
Use this workflow when the user wants a memo, charts, QA, and final artifacts produced from data with deterministic calculations.
## Terminology
- Analyst: task owner / analytical requester.
- `[Analytics]`: analytical methodology and framing layer.
- `[Codex]`: task package design layer.
- Codex APP: executor layer.
- Python: calculation layer.
- LLM: narrative layer.
- Judge/QA: quality layer.
- Human: acceptance layer.
## End-to-end workflow
```text
Analyst defines the analytical task
-> [Analytics] structures analytical methodology
-> [Codex] prepares an ultra-long Codex APP task package
-> Codex APP executes the task package
-> Python calculates
-> LLM writes from evidence
-> Judge/QA checks
-> Human accepts the result
```
## 1. Analyst defines the task
The Analyst provides:
- business question;
- data sources;
- period;
- expected memo type;
- constraints;
- audience;
- acceptance expectations.
## 2. [Analytics] structures the analytical methodology
`[Analytics]` owns analytical framing and methodology. It should define:
- `RAW -> STAGE -> MART -> EVIDENCE -> MEMO -> QA`;
- `stage_main_full` requirement;
- `mart_main_full` requirement;
- `mart_main_tz` / compact requirement;
- chart and evidence requirements;
- limitations and QA criteria.
`[Analytics]` is not reduced to Codex routing. It remains the place for analytical reasoning, methodology, data contracts, assumptions, limitations, and acceptance criteria.
## 3. [Codex] prepares an ultra-long task package
`[Codex]` designs the task package for Codex APP. It is not the local executor in this workflow.
The task package should include:
- objective;
- inputs;
- files to inspect;
- files allowed to modify;
- forbidden actions;
- expected outputs;
- tests / smoke checks;
- acceptance criteria;
- rollback;
- final response format.
## 4. Codex APP executes
Codex APP executes the task package locally. It should:
- inspect repository and data;
- write Python;
- build stage, mart, evidence, and charts;
- generate memo artifacts;
- run QA / smoke checks;
- report acceptance status.
## 5. Python calculates
Python is the calculation layer for:
- metrics;
- deltas;
- shares;
- rankings;
- totals;
- charts;
- evidence tables.
LLM must not perform these calculations mentally.
## 6. LLM writes
LLM is the narrative layer. It writes:
- memo narrative only from Python outputs and evidence;
- no unsupported calculations;
- no invented facts;
- no hidden assumptions.
## 7. Judge/QA checks
Judge/QA checks:
- unsupported claims;
- evidence coverage;
- limitations;
- data contracts;
- chart captions;
- memo quality;
- acceptance criteria.
## 8. Human accepts
Human review accepts or rejects:
- final memo;
- residual risks;
- limitations;
- next actions.
## Modes
### Mode A - Interactive Analytics
Use when the user wants to reason, explore, discuss methodology, or manually inspect outputs.
```text
User <-> [Analytics]
```
### Mode B - Analytical Memo Factory via Codex APP
Use when the user wants the memo produced as an artifact/work package with Python calculations, charts, QA, and final report.
```text
User -> [Analytics] -> [Codex] -> Codex APP
```
## Routing rule
If the user asks to create an analytical memo as an executable artifact, the default route is:
```text
[Analytics] for analytical task framing
-> [Codex] for ultra-long Codex APP task package
-> Codex APP for execution
```
Do not force the user into a manual loop where `[Analytics]` asks for Python outputs back and forth, unless the user explicitly wants interactive analysis.
## Boundaries
- Do not change metric definitions without explicit analytical approval.
- Do not invent schemas, formulas, facts, or business rules.
- Do not let LLM narrative exceed Python/evidence outputs.
- Do not claim production readiness without human acceptance.
- Do not treat Codex APP execution as ChatGPT Project sync evidence.
## Status
- status: canonical workflow pattern
- production_promotion: no
- source_of_truth: this file plus the granular Analytics and Codex workflow files

## From: `EXISTING_SCRIPT_CONTROLLED_REFACTOR_STANDARD.md`

# Existing Script Controlled Refactor Standard
## Purpose
Define a safe reusable workflow for cleaning or refactoring an existing working script or pipeline without losing useful behavior.
Use this standard when a script already produces valuable output but has messy internals, mixed responsibilities, obsolete code, debug fragments, local assumptions, old tests, or an unclear contract.
The standard is an engineering / Codex standard. It is not Analytics methodology and does not define business logic, metrics, formulas, or analytical conclusions.
## Use when
Use `Existing Script Controlled Refactor Standard` when all of these are true:
- an existing script, CLI, notebook-exported script, or pipeline already runs or has a known useful output;
- the user wants cleanup, controlled refactor, modularization, simplification, or removal of obsolete internal code;
- behavior preservation matters more than redesign;
- a baseline and at least one meaningful safety check can be created or identified;
- changes can be made locally and reviewed in a bounded PR.
## Do not use when
Do not use this standard when:
- the task is greenfield implementation;
- the script is not known to work and the goal is bugfix or recovery;
- the user explicitly requests behavior, schema, metric, formula, API, provider-routing, or output-contract changes;
- the task requires production deploy, migration, source data mutation, Safe Apply, or real provider/API execution without separate approval;
- there is no meaningful way to baseline current behavior or compare before/after output;
- the correct next step is Analytics framing, business definition work, or evidence review rather than engineering refactor.
## Core rule
Baseline, contract, and safety tests come before cleanup.
```text
baseline current behavior
-> define output contract
-> add safety tests
-> remove dead/obsolete code
-> refactor structure without behavior change
-> compare before/after output
-> acceptance
```
Codex must not start cleanup or restructuring until current behavior is captured, the output contract is explicit, and a safety test or comparison path exists.
## Baseline requirements
Before refactor, capture the smallest useful baseline that makes behavior observable.
Include where applicable:
- current command or entrypoint;
- representative input fixture, sample, or dry-run path;
- current output files, stdout, stderr, and exit code behavior;
- output filenames and locations;
- schema, columns, ordering, formatting, row counts, and reconciliation totals;
- accepted warnings, known quirks, and intentional legacy behavior;
- current tests or smoke checks;
- before-refactor golden output or comparison artifact.
Do not commit generated runtime artifacts unless repo policy explicitly allows them as fixtures or golden files.
## Output contract
Define what must remain unchanged unless separately accepted.
The output contract should state:
- output filenames and locations;
- file formats;
- schema, column names, column order, and deterministic formatting;
- expected row counts or reconciliation totals where applicable;
- CLI arguments and defaults;
- exit codes;
- stdout / stderr behavior when relevant;
- generated artifact policy;
- accepted warning and error behavior;
- what counts as a behavior change.
Any change to the output contract requires separate explicit acceptance.
## Safety tests before cleanup
Before removing code or restructuring modules, add or identify the smallest meaningful safety checks.
Use one or more of:
- existing tests;
- focused regression tests;
- golden-output comparison;
- smoke run or dry-run;
- schema check;
- row-count or reconciliation-total check;
- CLI help / entrypoint check;
- artifact validation;
- `git diff --check`;
- repo-specific validation scripts.
If no safety check is possible, stop and report a blocker instead of refactoring by intuition.
## Allowed refactor
Allowed only after baseline, output contract, and safety checks exist:
- extract functions;
- split internal modules;
- rename internal helpers;
- isolate CLI parsing from business logic;
- isolate IO from transformation logic;
- isolate validation and reporting;
- remove truly dead, obsolete, or unreachable code;
- remove debug-only branches that are not part of the accepted behavior;
- replace duplicated internal logic with an equivalent helper;
- improve comments and docstrings that clarify the preserved contract;
- add focused tests around preserved behavior.
Keep the diff minimal and reversible.
## Forbidden without separate acceptance
Do not do any of the following without separate explicit acceptance:
- behavior changes;
- output contract changes;
- schema, column, file-format, or file-location changes;
- metric, formula, business-rule, or financial-control changes;
- dependency additions;
- provider/API behavior changes;
- real provider/API execution;
- migrations;
- production/runtime/deploy changes;
- broad rewrite;
- deleting tests, QA, validation, or safety checks;
- source data mutation;
- committing generated runtime artifacts outside accepted fixture policy;
- adding autonomous loops, embeddings, semantic search, vector DB, or web UI.
## Recommended module split
When useful, split the script into clear internal layers:
```text
cli / entrypoint
-> config
-> io
-> transform
-> validate
-> report
-> tests
-> fixtures / golden outputs, only where repo policy allows
```
This split is recommended, not mandatory. Use the smallest structure that makes behavior safer and clearer.
## Parent/child decomposition for large risky refactors
For large or risky refactors, use `Parent / Child Issue Gate Standard` from `PARENT_CHILD_ISSUE_GATE_STANDARD.md`.
Do not duplicate the full parent/child standard here.
A large refactor should usually be split into child issues such as:
1. baseline and output contract;
2. safety tests or golden checks;
3. dead-code cleanup;
4. module extraction;
5. final before/after comparison.
Do not start downstream cleanup/refactor child issues until the baseline and safety-test child issues are accepted or merged.
## Acceptance criteria
Pass only when:
- baseline behavior is captured;
- output contract is explicit;
- safety tests or comparison checks exist and run;
- cleanup stays inside the accepted scope;
- before/after output is compared;
- output contract is preserved unless separately accepted;
- no forbidden runtime, schema, business-logic, provider, dependency, or artifact changes are included;
- final report lists changed files, checks, risks, rollback, and acceptance status.
## Required final response
For tasks using this standard, Codex must report:
```text
Summary:
Branch:
Files inspected:
Files changed:
Baseline captured:
Output contract:
Safety tests:
Before/after comparison:
Behavior changes:
Checks run:
Risks:
Rollback:
PR:
Acceptance status:
```
If behavior changed, acceptance status cannot be `pass` unless the behavior change was separately accepted.
## Blockers
Stop and report a blocker when:
- current behavior cannot be run, inspected, or baselined;
- output contract cannot be inferred safely;
- no meaningful safety test or comparison path exists;
- required input data is missing and no safe fixture can be used;
- the task requires secrets, local absolute paths, production systems, real provider/API execution, or source data mutation;
- preserving behavior conflicts with requested cleanup;
- the requested change would alter schema, metrics, formulas, business rules, APIs, file formats, column order, or output locations without separate acceptance.
## Key principle
Do not clean a working script by memory, taste, or vibes. First pin down what it does, then make it safer to change, then refactor only what the baseline can protect.

## From: `ChatGPT/[AI OS]/Knowledge/AIOS_01_ROUTING_AND_WORKFLOW_BUNDLE_SEMANTICS.md`

# Migrated Bundle Semantics
Canonical source created during Issue #285 provenance migration.
Legacy bundle provenance: `ChatGPT/[AI OS]/Knowledge_Bundles/AIOS_01_ROUTING_AND_WORKFLOW.md`.
## Legacy section: `ChatGPT/[AI OS]/Knowledge/PROJECT_ROUTING.md`
`ChatGPT/[Inbox Router]/Knowledge/ROUTING_RULES.md`.
If raw-input triage and AI OS scoped routing differ, use Inbox Router for
triage and this file for AI OS evidence/governance scope.
## Legacy section: `EXISTING_SCRIPT_CONTROLLED_REFACTOR_STANDARD.md`
This is an engineering/Codex standard, not Analytics methodology. It does not define business logic, metrics, formulas, or analytical conclusions.
Use `Existing Script Controlled Refactor Standard` when an existing script, CLI, notebook-exported script, or pipeline already runs or has known useful output, and Sergey wants cleanup, controlled refactor, modularization, simplification, or removal of obsolete internal code without behavior loss.
Do not use this standard for greenfield implementation, broken-script recovery, requested behavior/schema/metric/formula/API/provider/output-contract changes, production deploy, migration, source mutation, Safe Apply, real provider/API execution without approval, or cases where current behavior cannot be baselined.
Capture current command or entrypoint, representative input fixture/sample/dry-run path, output files/stdout/stderr, exit codes, filenames and locations, schema/columns/order/formatting, row counts or reconciliation totals, accepted warnings, known quirks, current tests, and before-refactor golden output where applicable.
Define filenames, locations, formats, schema, column names and order, deterministic formatting, CLI arguments/defaults, exit codes, stdout/stderr behavior, generated artifact policy, accepted warning/error behavior, and what counts as behavior change.
Any output contract change requires separate explicit acceptance.
Use the smallest meaningful safety checks: existing tests, focused regression tests, golden-output comparison, smoke run/dry-run, schema check, row-count or reconciliation-total check, CLI help/entrypoint check, artifact validation, `git diff --check`, or repo-specific validation scripts.
Allowed only after baseline, output contract, and safety checks exist: extract functions, split internal modules, rename internal helpers, isolate CLI/config/IO/transform/validate/report layers, remove truly dead or obsolete code, remove debug-only branches outside accepted behavior, replace duplicated internal logic with an equivalent helper, clarify comments/docstrings, and add focused tests around preserved behavior.
Forbidden without separate explicit acceptance: behavior changes, output contract changes, schema/column/file-format/file-location changes, metric/formula/business-rule/financial-control changes, dependency additions, provider/API behavior changes, real provider/API execution, migrations, production/runtime/deploy changes, broad rewrite, deleting tests/QA/validation, source data mutation, runtime artifacts outside accepted fixture policy, autonomous loops, embeddings, semantic search, vector DB, or web UI.
For large or risky refactors, use `Parent / Child Issue Gate Standard` from `PARENT_CHILD_ISSUE_GATE_STANDARD.md`. Do not duplicate the full parent/child standard.
Typical child issues: baseline and output contract; safety tests or golden checks; dead-code cleanup; module extraction; final before/after comparison. Do not start downstream cleanup/refactor child issues until baseline and safety-test child issues are accepted or merged.
Pass only when baseline behavior is captured, output contract is explicit, safety tests or comparison checks exist and run, cleanup stays in scope, before/after output is compared, output contract is preserved unless separately accepted, forbidden changes are absent, and final report lists changed files, checks, risks, rollback, and acceptance status.
Stop when current behavior cannot be run/inspected/baselined, output contract cannot be inferred safely, no meaningful safety test/comparison path exists, required input data is missing and no safe fixture can be used, the task requires secrets/local absolute paths/production systems/real provider/API/source mutation, preserving behavior conflicts with requested cleanup, or the requested change would alter schema, metrics, formulas, business rules, APIs, file formats, column order, or output locations without separate acceptance.
