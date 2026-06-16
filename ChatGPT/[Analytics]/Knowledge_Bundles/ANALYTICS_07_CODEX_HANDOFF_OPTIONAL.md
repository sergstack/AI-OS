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

## Upload target

ChatGPT Project Sources / Knowledge for `[Analytics]`.

## Status

- bundle_type: compact upload artifact
- source_of_truth: granular files listed above
- production_promotion: no, unless explicitly accepted elsewhere

---

# Content

## From: `ChatGPT/[AI OS]/Knowledge/ANALYTICAL_MEMO_FACTORY_CODEX_APP_WORKFLOW.md`

# Analytical Memo Factory via Codex APP
## Routing rule
If the user asks to create an analytical memo as an executable artifact, the default route is:
```text
[Analytics] for analytical task framing
-> [Codex] for ultra-long Codex APP task package
-> Codex APP for execution
```
`[Analytics]` remains the analytical methodology layer. `[Codex]` prepares the task package. Codex APP executes locally. Python calculates; LLM writes only from Python/evidence outputs; Judge/QA checks; Human accepts.

## From: `ChatGPT/[Analytics]/Knowledge/CODEX_TASK_PACKETS.md`

# Codex Task Packets
## Purpose
## Important rule
## Input
```text
json compact + json full
or only json compact
```
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
- [ ] `[Analytics]` still solves analytical tasks directly.
- [ ] Handoff is only for implementation.
- [ ] Main files standard added.
- [ ] QA and acceptance updated.
- [ ] Smoke QA updated.
## 2. Stage packet
- [ ] `stage_main_full` required.
- [ ] No metrics/classifiers in stage.
- [ ] Portability to DB / BI / Excel stated.
- [ ] Stage slices allowed only after main stage file.
## 3. Mart packet
- [ ] `mart_main_full` required.
- [ ] `mart_main_tz/compact` required.
- [ ] Slices derive from `mart_main_full`.
- [ ] Metrics/formulas/classifiers/risk/confidence fields in mart layer.
## 4. Charts packet
- [ ] Each chart has source_mart.
- [ ] Each chart has metric, grain, period.
- [ ] Caption does not exceed evidence.
- [ ] Chart slices derive from `mart_main_full`.
## 5. Insights packet
- [ ] DQ status included.
- [ ] Plan / Fact / Delta / ABS Delta included when relevant.
- [ ] Top deviations ranked.
- [ ] Risk has basis.
- [ ] Confidence has rationale.
- [ ] Cause vs hypothesis separated.
- [ ] Action has owner / due date.
## 6. Word packet
- [ ] Executive summary from compact mart.
- [ ] Appendix/evidence from full mart.
- [ ] Charts sourced from mart slices.
- [ ] Limitations visible.
## 7. Text QA packet
Objective: text and formatting QA.
- [ ] No unsupported claims.
- [ ] Low Confidence not written as fact.
- [ ] Risk/action rules followed.
- [ ] Formatting preserves meaning.
## 8. QA packet
Objective: run smoke QA and record acceptance.
- [ ] Smoke questions pass/fail recorded.
- [ ] Changed files listed.
- [ ] Residual risks listed.
- [ ] Rollback notes provided.


## From: `ChatGPT/[Analytics]/Templates/CODEX_HANDOFF_TEMPLATE.md`

# Handoff to Codex
Forbidden actions:
## Analytics context already resolved
QA:
## Do not change
- Do not remove in-project analysis mode.
- Do not remove main files requirement.
- Do not route all analytics tasks to Codex.
- Do not treat smoke QA as production readiness.


## From: `ChatGPT/[Analytics]/Codex_Tasks/00_OVERVIEW.md`

# Codex Task 00 — Overview
## Objective
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
