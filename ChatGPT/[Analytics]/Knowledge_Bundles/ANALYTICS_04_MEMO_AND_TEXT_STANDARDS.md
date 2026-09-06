# [Analytics] — Memo and Text Standards

## Purpose

Compact upload artifact for [Analytics] covering memo and text standards.

## Source files

- `ChatGPT/[Analytics]/Knowledge/MEMO_PIPELINE.md`
- `ChatGPT/[Analytics]/Knowledge/ANALYTICAL_MEMO_STRUCTURE.md`
- `ChatGPT/[Analytics]/Knowledge/WORD_REPORT_STANDARD.md`
- `ChatGPT/[Analytics]/Knowledge/TEXT_QA_AND_STYLE.md`
- `ChatGPT/[Analytics]/Knowledge/MEMO_RUBRIC.md`
- `ChatGPT/[Analytics]/Knowledge/ANALYTICS_04_MEMO_AND_TEXT_STANDARDS_BUNDLE_SEMANTICS.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[Analytics]`.

## Status

- production_promotion: no, unless explicitly accepted elsewhere
- bundle_type: generated compact upload artifact
- source_of_truth: declared granular source files
- source_fingerprint: sha256:12ade3c5b5b0cd6bd996e9692a81f9a5e26e682157b9211175ab9cfa5bc7a8fb
- generator: scripts/build_knowledge_bundles.py

---

# Content

## From: `ChatGPT/[Analytics]/Knowledge/MEMO_PIPELINE.md`

# Analytical Memo Pipeline
## Purpose
Convert verified analysis into a memo without losing evidence.
## Pipeline
```text
mart_main_full
→ analysis tables
→ insight cards
→ evidence cards
→ mart_main_tz / compact
→ management synthesis when material and management-facing
→ LLM context package, if needed
→ draft memo
→ deterministic memo QA
→ LLM Judge according to the canonical [LLM] memo gate
→ revision only from explicit findings
→ final report
```
`[Analytics]` owns verified inputs and deterministic memo QA. `[LLM]` owns Judge/revise triggers in `ChatGPT/[LLM]/Knowledge/MEMO_GENERATION_WORKFLOW.md`; this pipeline references that contract rather than redefining it.
This pipeline is the Gate 3 (narrative) checkpoint (`ANALYTICAL_REASONING_STANDARD.md` §14): it controls that memo wording is no stronger than the verified claim from Gate 2. A headline conclusion with `allowed_in_executive = no` (missing Claim/Evidence Registry lineage, or `analytical_depth = material/decision_critical` without a resolved `METRIC_DEFINITION_CARD`) does not enter the memo/executive layer; state the limitation instead.
## Memo structure
1. Executive summary.
2. Key numbers.
3. Main drivers.
4. Exceptions / anomalies.
5. Risks.
6. Management implication / decision or action if any.
7. Limitations.
8. Appendix / evidence.
### Management implication section (P1-B, issue #449, standard, active)
For `analytical_depth = material / decision_critical`, the management
implication section (item 6) reads the `ANALYTICAL_REASONING_STANDARD.md`
§16 controls rather than redefining them:
- `recommendation_status` (supported / pilot_candidate / hypothesis) from
  `RECOMMENDATION_EVIDENCE` (§16.2) governs the strength of the wording used;
  a `pilot_candidate` or `hypothesis` recommendation is worded as such, not
  as a settled management decision.
- `what_would_change_the_view` (§16.6) is stated as one compact line when a
  material evidence gap exists (§16.2–§16.5, `FINAL_EVIDENCE_SUFFICIENCY`, or
  unresolved `CONTRADICTING_EVIDENCE`); it is omitted when no such gap
  exists.
Routine/quick output does not instantiate these fields absent a material
trigger (§9 runtime collapse).
## Audience split
### Executive memo
For CFO / COO / руководители:
- verdict;
- headline numbers;
- where the money is;
- main risks;
- decisions or actions if supported;
- limitations.
Uses:
```text
mart_main_tz / mart_main_compact
```
### Finance working package
For Sergey / Finance Team / deep review:
- full evidence;
- DQ;
- timing notes;
- INOUT checks if valid;
- baseline;
- cards;
- backlog;
- reconciliation.
Uses:
```text
mart_main_full
```
## Evidence rule
Every important sentence must be backed by:
- metric;
- table/mart;
- period;
- evidence card;
- or explicitly marked as interpretation.
## Memo QA
- [ ] Executive summary is materially shorter than supporting evidence and does not exceed it.
- [ ] Key numbers trace to mart.
- [ ] Drivers are ranked by impact.
- [ ] Risks have `risk_basis`.
- [ ] Actions have owner / due date / status.
- [ ] Limitations visible.
- [ ] Hypotheses are not presented as confirmed causes.
- [ ] No headline claim with `allowed_in_executive = no` appears in the
  executive body.
- [ ] Ambiguous or unresolved metric definitions (no `METRIC_DEFINITION_CARD`)
  are not presented as flagship conclusions.
- [ ] A management recommendation is not presented as `supported` when
  `RECOMMENDATION_EVIDENCE.recommendation_status` is `pilot_candidate` or
  `hypothesis` (§16.2, standard/active, issue #449; promoted 2026-09-06, see
  `docs/evidence/ANALYTICS_P1_PROMOTION_2026-09-06.md`).
- [ ] `what_would_change_the_view` is present when a material evidence gap
  exists for material/decision-critical output, and absent otherwise (§16.6).

## From: `ChatGPT/[Analytics]/Knowledge/ANALYTICAL_MEMO_STRUCTURE.md`

# Analytical Memo Structure
## Purpose
Структура аналитической записки, которая отделяет обязательный управленческий слой от рабочего evidence-пакета.
## Executive layer for material management analysis
For `analytical_depth = material / decision_critical` and management-facing output, open with a compressed executive layer:
1. Executive verdict answering the business question.
2. Smallest sufficient set of material conclusions, usually 1–3 but never as a quota.
3. Supported business meaning and affected performance dimension.
4. Business effect versus data/control artefact where relevant.
5. Management implication and decision/action required, if any.
6. Material uncertainty and what would change the view.
7. Material limitations.
Rank by the business criterion relevant to the question, not mechanically by `ABS Delta`. Do not collapse materially different performance dimensions. State controllability or persistence only when supported; otherwise mark them unknown or omit them. The executive layer must be materially shorter than the supporting evidence. Routine output remains compact and does not instantiate this layer.
If DQ or reconciliation prevents reliable interpretation, that limitation becomes the executive verdict. Otherwise keep methodology and reconciliation in the evidence layer.
## Supporting evidence layer
Preserve the verified analytical detail:
1. DQ status.
2. Plan / Fact / Delta / ABS Delta where applicable.
3. Material deviations and their ranking criterion.
4. Row type.
5. Timing status.
6. Planning risk + risk basis.
7. Confidence + why not higher.
8. Confirmed cause vs hypothesis.
9. Supported action + owner + due date, if an action is asserted.
10. Limitations / open questions.
## Must / Should / Conditional / Optional
| Block | Status | Notes |
|---|---|---|
| DQ status | Must | Без DQ нельзя публиковать сильный вывод |
| Plan / Fact / Delta / ABS Delta | Must | Базовый слой отклонений |
| Top deviations | Must | Ранжировать по явному business criterion; `ABS Delta` не является универсальным критерием |
| Row type | Must | Например: real variance / timing / data issue / mapping issue |
| Timing status | Must when relevant | candidate / confirmed / partial / not timing |
| Risk + risk basis | Must for management memo | Risk без basis не публиковать |
| Confidence + rationale | Must | Low Confidence не финальная причина |
| Confirmed cause vs hypothesis | Must | Не смешивать |
| Action + owner + due date | Must only when an action is supported | Иначе это observation / monitoring / validation gap |
| INOUT | Conditional | Только при Definition Card |
| Forecast | Optional | Если вопрос про будущее решение |
| Scenario analysis | Optional / advanced | Если нужен выбор сценария |
| ML anomaly detection | Advanced | Не MVP по умолчанию |
| Methodology backlog | Should | Для улучшения системы |
## Stop conditions
| Condition | Action |
|---|---|
| DQ Fail | Do not publish management conclusion |
| No single currency/unit logic | Stop materiality conclusion |
| Low Confidence | Mark as hypothesis / not final cause |
| Timing only candidate | Do not call confirmed timing |
| Risk without basis | Do not publish risk |
| Action without owner/due date | Do not call management action |
| INOUT undefined | Do not use INOUT as explanation |
## Output template
```text
Verdict:
Material conclusions + why they matter:
Key numbers:
Top deviations:
Main driver / hypothesis:
Risk:
Confidence:
Management implication / decision or action if any:
What changes the view:
Limitations:
Evidence:
```

## From: `ChatGPT/[Analytics]/Knowledge/WORD_REPORT_STANDARD.md`

# Word / DOCX Report Standard
## Purpose
Стандарт подготовки аналитических записок в Word без потери evidence.
## Source rule
DOCX must be based on verified data:
```text
executive memo content ← mart_main_tz / mart_main_compact
appendix / evidence ← mart_main_full
charts ← slices derived from mart_main_full
```
## Recommended document structure
1. Title.
2. Date / period / owner.
3. Executive summary.
4. Key numbers table.
5. Main deviations and drivers.
6. Risks and confidence.
7. Recommended actions.
8. Charts.
9. Limitations.
10. Appendix / evidence.
## Required metadata
```text
report_name:
period:
audience:
owner:
source_mart_full:
source_mart_compact:
qa_status:
accepted:
version:
```
## Word formatting principles
- Use short executive summary.
- Put numbers in tables, not only prose.
- Put limitations before appendix, not hidden at the end.
- Use chart captions that state the exact metric and period.
- Separate confirmed causes from hypotheses.
- Avoid decorative language.
## Executive language and evidence layer
- Все видимые элементы управленческой записки должны быть на русском языке.
- Executive memo body must stay management-readable; detailed evidence belongs to appendix / evidence layer.
- Technical IDs допускаются только в appendix / evidence layer.
- Technical values such as `fact_only`, `plan_only`, `p_fact_adjusted`, `refund_only`, `source_mix`, `slice_*`, `mart_*`, `EV-*`, `CH_EXEC_*` must not appear in the main executive body unless placed in appendix / evidence context.
- Chart titles, labels, legends, axes and captions must use Russian business-readable labels.
- Appendix / evidence must be clearly separated from the executive memo body.
## DOCX acceptance
- [ ] Executive summary present.
- [ ] Key numbers trace to `mart_main_tz/compact`.
- [ ] Deep claims trace to `mart_main_full`.
- [ ] Charts have source and caption.
- [ ] Limitations visible.
- [ ] Confidence stated.
- [ ] No unsupported claims.
- [ ] Formatting does not change analytical meaning.
- [ ] Visible report language is Russian.
- [ ] No technical IDs in executive body.
- [ ] Technical IDs only in appendix / evidence.
- [ ] Appendix is clearly separated from executive memo.
## Handoff to Codex
Only handoff DOCX generation to Codex if the task requires:
- automated `.docx` creation;
- template rendering;
- file conversion;
- reproducible report generator;
- tests or CI.
Otherwise, structure and content can be prepared inside `[Analytics]`.

## From: `ChatGPT/[Analytics]/Knowledge/TEXT_QA_AND_STYLE.md`

# Text QA and Style
## Purpose
Отладка текстов и оформления аналитических записок так, чтобы текст не становился сильнее данных.
## Style principles
- Concrete over decorative.
- Numbers before adjectives.
- Evidence before recommendation.
- Limitation before confidence inflation.
- Hypothesis is not cause.
- Observation is not action.
## Language rules
Use:
```text
Данные показывают...
Расчёт по mart_main_full показывает...
Отклонение составляет...
Вероятная причина, требующая проверки...
Ограничение анализа...
```
Avoid:
```text
Очевидно...
Бесспорно...
Компания должна...
Причина точно в...
Данные полностью подтверждают...
```
unless QA and evidence support it.
## Executive report language standard
- Все видимые элементы управленческой записки должны быть на русском языке.
- Executive memo body must stay management-readable; evidence detail belongs to appendix / evidence layer.
- Technical IDs допускаются только в appendix / evidence layer.
- Technical values such as `fact_only`, `plan_only`, `p_fact_adjusted`, `refund_only`, `source_mix`, `slice_*`, `mart_*`, `EV-*`, `CH_EXEC_*` must not appear in the main executive body unless placed in appendix / evidence context.
- Chart labels, legends, axes, titles and captions must use Russian business-readable labels.
- Captions must not exceed evidence.
## Text QA checklist
- [ ] No unsupported claims.
- [ ] Every key conclusion has evidence.
- [ ] Low Confidence is not written as fact.
- [ ] Hypotheses are labeled.
- [ ] Risk has `risk_basis`.
- [ ] Action has owner / due date / status.
- [ ] INOUT not used without Definition Card.
- [ ] Chart captions not stronger than data.
- [ ] Limitations visible.
- [ ] Executive wording matches compact mart.
- [ ] Deep conclusions reference full mart/evidence.
- [ ] Visible report language is Russian.
- [ ] No technical IDs in executive body.
- [ ] Technical IDs appear only in appendix / evidence.
## Formatting QA
- [ ] Headings reflect analytical structure.
- [ ] Tables are readable.
- [ ] Period and units visible.
- [ ] Numbers have consistent formatting.
- [ ] Same metric has same name everywhere.
- [ ] Appendix is clearly separated from executive memo.
- [ ] No hidden methodological caveats.
- [ ] Executive memo body is not overloaded with evidence detail.

## From: `ChatGPT/[Analytics]/Knowledge/MEMO_RUBRIC.md`

# Analytical Memo Rubric
## Purpose
Define what a good analytical memo means for `[Analytics]`.
## Rubric
| Area | Pass condition | Fail condition |
|---|---|---|
| Executive verdict | Answers the business question | Finding catalogue without a verdict |
| Prioritization | Smallest sufficient set ranked by an explicit business criterion | Mechanical Top-3 or `ABS Delta` treated as universal importance |
| Business meaning | Each headline has supported meaning or an explicit evidence gap | Manufactured “so what” |
| Performance dimensions | Materially different dimensions remain distinct | Unsupported overall good/bad assessment |
| Effect type | Business effect and data/control artefact are separated where relevant | Data exception presented as economic effect without evidence |
| Evidence | Key conclusions trace to mart/evidence | Unsupported claims |
| Claim gate | Headline claim has complete Claim/Evidence Registry lineage (`allowed_in_executive = yes`) | Headline claim published with `allowed_in_executive = no` or no `method_execution_id`/`evidence_id` |
| Metric semantics | Flagship/ratio-like metric has an approved `METRIC_DEFINITION_CARD` | Ambiguous formula (e.g. undefined numerator/denominator) presented as a flagship result |
| Numbers | Key figures have metric, period, grain, source | Numbers without source |
| Drivers | Drivers ranked by relevant business impact | Decorative or mechanically ranked explanation |
| Risk | Risk has `risk_basis` | Risk without basis |
| Management implication | Decision/action is stated only if supported; otherwise monitoring, validation, no action, or uncertainty remains explicit | Decision manufactured from an observation |
| Recommendation strength | Wording matches `RECOMMENDATION_EVIDENCE.recommendation_status` (supported / pilot_candidate / hypothesis); untested interventions read as pilot candidates, not settled decisions (§16.2, standard/active, issue #449, promoted 2026-09-06) | An untested intervention (no `test_or_backtest_performed`) worded as a confirmed management decision |
| Thinking boundary | Analytics provides evidence and implication; strategic trade-offs remain with `[Thinking]` | Analytics chooses a strategic option without supported criteria |
| Compression | Executive layer is materially shorter than supporting evidence | Synthesis becomes a second analytical report |
| Confidence | Confidence and limitations visible | Low confidence as fact |
| Language | Russian, business-readable executive body | Technical IDs in executive body |
| Charts | Source mart, metric, period, grain visible | Caption stronger than data |
## Golden memo criteria
A memo is strong when:
- executive summary is short and evidence-backed;
- numbers are in tables and prose;
- material conclusions are ranked by an explicit business criterion;
- confirmed causes and hypotheses are separated;
- no headline claim appears without complete Claim/Evidence Registry lineage;
- limitations are visible before appendix;
- management implication does not exceed verified evidence;
- a recommendation's stated strength matches `RECOMMENDATION_EVIDENCE.recommendation_status` and `what_would_change_the_view` is present when a material evidence gap exists (§16.2, §16.6, standard/active, issue #449, promoted 2026-09-06);
- executive synthesis is materially shorter than the evidence layer;
- appendix / evidence layer supports deep claims.

## From: `ChatGPT/[Analytics]/Knowledge/ANALYTICS_04_MEMO_AND_TEXT_STANDARDS_BUNDLE_SEMANTICS.md`

# Migrated Bundle Semantics
Canonical source created during Issue #285 provenance migration.
Legacy bundle provenance: `ChatGPT/[Analytics]/Knowledge_Bundles/ANALYTICS_04_MEMO_AND_TEXT_STANDARDS.md`.
## Legacy section: `ChatGPT/[Analytics]/Knowledge/ANALYTICAL_MEMO_STRUCTURE.md`
For `analytical_depth = material / decision_critical` and management-facing output:
Rank by the relevant business criterion, not mechanically by `ABS Delta`; keep different performance dimensions visible. State controllability or persistence only when supported. The executive layer must be materially shorter than supporting evidence; routine output remains compact. If DQ or reconciliation prevents reliable interpretation, that limitation becomes the executive verdict.
Preserve DQ, applicable Plan/Fact/Delta, material deviations and ranking criterion, row/timing status, risk basis, confidence, cause versus hypothesis, supported action details if asserted, and limitations/open questions.
## Legacy section: `ChatGPT/[Analytics]/Knowledge/MEMO_RUBRIC.md`
| Management implication | Decision/action is stated only if supported | Decision manufactured from an observation |
