# [Analytics] — Codex Handoff Optional

## Purpose

Compact upload artifact for [Analytics] covering codex handoff optional.

## Source files

- `ChatGPT/[Analytics]/Knowledge/CODEX_TASK_PACKETS.md`
- `ChatGPT/[Analytics]/Templates/CODEX_HANDOFF_TEMPLATE.md`
- `ChatGPT/[Analytics]/Codex_Tasks/00_OVERVIEW.md`
- `ChatGPT/[Analytics]/Codex_Tasks/01_STAGE.md`
- `ChatGPT/[Analytics]/Codex_Tasks/02_MART.md`
- `ChatGPT/[Analytics]/Codex_Tasks/03_CHARTS.md`
- `ChatGPT/[Analytics]/Codex_Tasks/04_INSIGHTS.md`
- `ChatGPT/[Analytics]/Codex_Tasks/05_WORD.md`
- `ChatGPT/[Analytics]/Codex_Tasks/06_TEXT_QA.md`
- `ChatGPT/[Analytics]/Codex_Tasks/07_SMOKE_QA.md`
- `ChatGPT/[AI OS]/Knowledge/ANALYTICAL_MEMO_FACTORY_CODEX_APP_WORKFLOW.md`
- `ChatGPT/[Analytics]/Knowledge/ANALYTICS_07_CODEX_HANDOFF_OPTIONAL_BUNDLE_SEMANTICS.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[Analytics]`.

## Status

- production_promotion: no, unless explicitly accepted elsewhere
- bundle_type: generated compact upload artifact
- source_of_truth: declared granular source files
- source_fingerprint: sha256:729544d90b1a582454e5296afa690117484e41109ad9b8674da61abcc1e2e62d
- generator: scripts/build_knowledge_bundles.py

---

# Content

## From: `ChatGPT/[Analytics]/Knowledge/CODEX_TASK_PACKETS.md`

# Codex Task Packets
## Purpose
Когда нужно изменить документы, код или автоматизацию, `[Analytics]` выдаёт ТЗ для `[Codex]` частями, чтобы изменения были управляемыми.
## Important rule
Codex task packets are for implementation. Analytical logic stays in `[Analytics]` first.
For analytical memo production, `[Codex]` prepares the ultra-long Codex APP task package and Codex APP executes it locally. Python calculates metrics, deltas, shares, rankings, totals, charts, and evidence tables. LLM narrative must write only from Python/evidence outputs.
## Input
```text
json compact + json full
or only json compact
```
Use:
- compact for scope, audience, expected outputs;
- full for detailed rules, files, schemas, acceptance.
## Output packet set
1. Общий обзор ТЗ для передачи Codex.
2. ТЗ для формирования Stage.
3. ТЗ для формирования Mart.
4. ТЗ для подбора графиков.
5. ТЗ для создания выводов на основе структуры аналитических записок.
6. ТЗ для подготовки аналитических записок в Word.
7. ТЗ для отладки текстов и оформления аналитических записок.
8. QA / smoke / acceptance packet.
## Packet template
```markdown
# Codex Task Packet — <name>
From: [Analytics]
To: [Codex]
Task type:
Objective:
Context:
Files to inspect:
Files to change:
Inputs:
Constraints:
Forbidden actions:
Expected outputs:
Tests / checks:
Acceptance criteria:
Risks:
Rollback notes:
```
## 1. Overview packet
Objective: update or create the Analytics package without breaking in-project analysis mode.
Acceptance:
- [ ] `[Analytics]` still solves analytical tasks directly.
- [ ] Handoff is only for implementation.
- [ ] Main files standard added.
- [ ] QA and acceptance updated.
- [ ] Smoke QA updated.
## 2. Stage packet
Objective: enforce `stage_main_full` before stage slices.
Acceptance:
- [ ] `stage_main_full` required.
- [ ] No metrics/classifiers in stage.
- [ ] Portability to DB / BI / Excel stated.
- [ ] Stage slices allowed only after main stage file.
## 3. Mart packet
Objective: enforce `mart_main_full` and `mart_main_tz/compact`.
Acceptance:
- [ ] `mart_main_full` required.
- [ ] `mart_main_tz/compact` required.
- [ ] Slices derive from `mart_main_full`.
- [ ] Metrics/formulas/classifiers/risk/confidence fields in mart layer.
## 4. Charts packet
Objective: chart selection from mart sources only.
Acceptance:
- [ ] Each chart has source_mart.
- [ ] Each chart has metric, grain, period.
- [ ] Caption does not exceed evidence.
- [ ] Chart slices derive from `mart_main_full`.
## 5. Insights packet
Objective: create conclusions using memo structure.
Acceptance:
- [ ] DQ status included.
- [ ] Plan / Fact / Delta / ABS Delta included when relevant.
- [ ] Top deviations ranked.
- [ ] Risk has basis.
- [ ] Confidence has rationale.
- [ ] Cause vs hypothesis separated.
- [ ] Action has owner / due date.
## 6. Word packet
Objective: prepare Word/DOCX memo standard.
Acceptance:
- [ ] Executive summary from compact mart.
- [ ] Appendix/evidence from full mart.
- [ ] Charts sourced from mart slices.
- [ ] Limitations visible.
## 7. Text QA packet
Objective: text and formatting QA.
Acceptance:
- [ ] No unsupported claims.
- [ ] Low Confidence not written as fact.
- [ ] Risk/action rules followed.
- [ ] Formatting preserves meaning.
## 8. QA packet
Objective: run smoke QA and record acceptance.
Acceptance:
- [ ] Smoke questions pass/fail recorded.
- [ ] Changed files listed.
- [ ] Residual risks listed.
- [ ] Rollback notes provided.

## From: `ChatGPT/[Analytics]/Templates/CODEX_HANDOFF_TEMPLATE.md`

# Handoff to Codex
From: [Analytics]
To: [Codex]
Task type:
Objective:
Context:
Files to inspect:
Files to change:
Inputs:
Constraints:
Forbidden actions:
Expected outputs:
Tests / checks:
Acceptance criteria:
Risks:
Rollback notes:
## Analytics context already resolved
Question:
Data contract:
Main files standard:
Metrics:
QA:
Limitations:
## Do not change
- Do not remove in-project analysis mode.
- Do not remove main files requirement.
- Do not route all analytics tasks to Codex.
- Do not treat smoke QA as production readiness.

## From: `ChatGPT/[Analytics]/Codex_Tasks/00_OVERVIEW.md`

# Codex Task 00 — Overview
From: [Analytics]
To: [Codex]
Task type: documentation / project settings update
## Objective
Update the `[Analytics]` project package so it keeps direct in-project analytics capability while adding the universal main files standard.
## Expected outputs
- Updated `PROJECT_INSTRUCTIONS.md`.
- Updated Knowledge files.
- New main files standard.
- Updated QA and acceptance.
- Smoke QA result.
## Acceptance criteria
- [x] Analytics still performs analysis directly.
- [x] Handoff only for implementation/prompt orchestration/strategy/AI evidence.
- [x] `stage_main_full` required.
- [x] `mart_main_full` required.
- [x] `mart_main_tz/compact` required.
- [x] Slices derive from `mart_main_full`.
- [x] Smoke QA created.

## From: `ChatGPT/[Analytics]/Codex_Tasks/01_STAGE.md`

# Codex Task 01 — Stage
## Objective
Add and enforce the `stage_main_full` standard.
## Requirements
- `stage_main_full` is required before any stage slices.
- It contains cleaned/normalized/typed fields.
- It contains no metrics and no analytical classifiers.
- It is portable to DB / dashboard / Excel / BI.
## Acceptance criteria
- [x] Stage rule documented.
- [x] Forbidden stage content documented.
- [x] Stage slice rule documented.
- [x] QA checklist updated.

## From: `ChatGPT/[Analytics]/Codex_Tasks/02_MART.md`

# Codex Task 02 — Mart
## Objective
Add and enforce `mart_main_full` and `mart_main_tz/compact`.
## Requirements
- `mart_main_full` is the complete analysis-ready mart.
- `mart_main_tz/compact` is the shortened executive/TZ version.
- Slices, charts and memo derive from `mart_main_full`.
- Metrics, classifiers, risks and confidence live in mart layer.
## Acceptance criteria
- [x] Full mart rule documented.
- [x] Compact mart rule documented.
- [x] Slice derivation documented.
- [x] Mart QA updated.

## From: `ChatGPT/[Analytics]/Codex_Tasks/03_CHARTS.md`

# Codex Task 03 — Charts
## Objective
Add chart selection standard.
## Requirements
Each chart must have source mart/slice, metric, period, grain, filter, purpose and limitation.
## Acceptance criteria
- [x] Chart source rule documented.
- [x] Chart types mapped to analytical needs.
- [x] Chart QA checklist added.
- [x] Captions cannot exceed evidence.
## Visual and language standard for executive memo
- Все видимые элементы управленческой записки должны быть на русском языке.
- Technical IDs допускаются только в appendix / evidence layer и не должны перегружать основной текст записки.
- Графики для executive memo используют спокойную управленческую палитру: приглушённые, благородные цвета без ярких и кислотных оттенков.
- Technical values such as `fact_only`, `plan_only`, `p_fact_adjusted`, `refund_only`, `source_mix`, `slice_*`, `mart_*`, `EV-*`, `CH_EXEC_*` must not appear in the main executive body unless placed in appendix / evidence context.
- Chart labels, legends, axes, titles and captions must use Russian business-readable labels.
- Captions must not exceed evidence.
- Executive memo body must stay management-readable; evidence detail belongs to appendix / evidence layer.
- Appendix / evidence must be clearly separated from the executive memo.
## Additional chart QA checks
- [ ] Visible report language is Russian.
- [ ] Chart labels are Russian / business-readable.
- [ ] Legends, axes, titles and captions are Russian / business-readable.
- [ ] Executive chart palette uses muted executive colors.
- [ ] No technical IDs in executive body.
- [ ] Technical IDs appear only in appendix / evidence.

## From: `ChatGPT/[Analytics]/Codex_Tasks/04_INSIGHTS.md`

# Codex Task 04 — Insights
## Objective
Add analytical memo insight structure.
## Requirements
Insights must separate facts, calculations, interpretation, recommendation, hypothesis and limitations.
## Acceptance criteria
- [x] MVP memo blocks documented.
- [x] Must/Should/Conditional/Optional layers documented.
- [x] Stop conditions documented.
- [x] Cause vs hypothesis rule documented.

## From: `ChatGPT/[Analytics]/Codex_Tasks/05_WORD.md`

# Codex Task 05 — Word / DOCX
## Objective
Add Word/DOCX report standard.
## Requirements
- Executive content from `mart_main_tz/compact`.
- Appendix/evidence from `mart_main_full`.
- Charts from mart slices.
- Limitations visible.
## Acceptance criteria
- [x] Word structure documented.
- [x] Metadata documented.
- [x] DOCX QA documented.
- [x] Handoff to Codex only for automated generation.
## Visual and language standard for executive memo
- Все видимые элементы управленческой записки должны быть на русском языке.
- Technical IDs допускаются только в appendix / evidence layer и не должны перегружать основной текст записки.
- Графики для executive memo используют спокойную управленческую палитру: приглушённые, благородные цвета без ярких и кислотных оттенков.
- Technical values such as `fact_only`, `plan_only`, `p_fact_adjusted`, `refund_only`, `source_mix`, `slice_*`, `mart_*`, `EV-*`, `CH_EXEC_*` must not appear in the main executive body unless placed in appendix / evidence context.
- Chart labels, legends, axes, titles and captions must use Russian business-readable labels.
- Captions must not exceed evidence.
- Executive memo body must stay management-readable; evidence detail belongs to appendix / evidence layer.
- Appendix / evidence must be clearly separated from the executive memo.
## Additional DOCX QA checks
- [ ] Visible report language is Russian.
- [ ] No technical IDs in executive body.
- [ ] Technical IDs appear only in appendix / evidence.
- [ ] Chart labels and captions are Russian / business-readable.
- [ ] Executive chart palette uses muted executive colors.
- [ ] Appendix is clearly separated from executive memo.

## From: `ChatGPT/[Analytics]/Codex_Tasks/06_TEXT_QA.md`

# Codex Task 06 — Text QA
## Objective
Add text and formatting QA standard.
## Acceptance criteria
- [x] Unsupported claims blocked.
- [x] Low Confidence not written as fact.
- [x] Risk/action rules documented.
- [x] Formatting QA documented.

## From: `ChatGPT/[Analytics]/Codex_Tasks/07_SMOKE_QA.md`

# Codex Task 07 — Smoke QA
## Objective
Run smoke QA after package update.
## Acceptance criteria
- [x] Scope/routing question passes.
- [x] Main files question passes.
- [x] Compact/full question passes.
- [x] Charts question passes.
- [x] Memo question passes.
- [x] Stop conditions question passes.
- [x] Acceptance question passes.
- [x] Residual risks recorded.

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

## From: `ChatGPT/[Analytics]/Knowledge/ANALYTICS_07_CODEX_HANDOFF_OPTIONAL_BUNDLE_SEMANTICS.md`

# Migrated Bundle Semantics
Canonical source created during Issue #285 provenance migration.
Legacy bundle provenance: `ChatGPT/[Analytics]/Knowledge_Bundles/ANALYTICS_07_CODEX_HANDOFF_OPTIONAL.md`.
## Legacy section: `ChatGPT/[AI OS]/Knowledge/ANALYTICAL_MEMO_FACTORY_CODEX_APP_WORKFLOW.md`
`[Analytics]` remains the analytical methodology layer. `[Codex]` prepares the task package. Codex APP executes locally. Python calculates; LLM writes only from Python/evidence outputs; Judge/QA checks; Human accepts.
