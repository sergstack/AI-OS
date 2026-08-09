# [Analytics] — Techniques and Charts

## Purpose

Compact upload artifact for [Analytics] covering techniques and charts.

## Source files

- `ChatGPT/[Analytics]/Knowledge/ANALYTICAL_TECHNIQUES.md`
- `ChatGPT/[Analytics]/Knowledge/ANALYTICAL_REASONING_STANDARD.md`
- `ChatGPT/[Analytics]/Knowledge/CHART_SELECTION_STANDARD.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[Analytics]`.

## Status

- bundle_type: compact upload artifact
- source_of_truth: granular files listed above
- production_promotion: no, unless explicitly accepted elsewhere
- source_fingerprint: sha256:18ceffd6dfce2d8cd13b6084acb251caf9aab9151ebc962c87f8619fcd7938b2

---

# Content

## From: `ChatGPT/[Analytics]/Knowledge/ANALYTICAL_TECHNIQUES.md`

# Analytical Techniques

## P0 method registry

Registry is the source of truth for eligibility; registration is not execution. Each method records `METHOD_ID`, name, purpose, role, requirements, input grain, required metrics, output, execution owner/mode, validation owner, limitation, and failure mode. Mixed execution also records deterministic and reasoning components.

For P0, `NAME` is the stable registry label represented by `METHOD_ID`; display formatting cannot change identity.

`P0 METHOD COUNT = 22`. Capability groups (`DECOMPOSE`, `LOCATE`, `VALIDATE`, `CHALLENGE`, `FORWARD`) are readability aids only, not runtime taxonomy or routing.

| METHOD_ID | Role / mode | Purpose and required boundary |
|---|---|---|
| `variance_analysis` | analytical / deterministic | Comparable actual/baseline at aligned grain → variance. |
| `contribution_analysis` | analytical / deterministic | Reconciled additive components → ranked contribution. |
| `bridge_analysis` | analytical / deterministic | Non-overlapping start/end movements → bridge. |
| `driver_decomposition` | analytical / mixed | Deterministic decomposition plus bounded interpretation → driver candidates/residual, not causal proof. |
| `mix_analysis` | analytical / deterministic | Stable categories/weights → mix effect. |
| `segmentation` | analytical / deterministic | Valid groups and sufficient observations → segment comparison. |
| `trend_analysis` | analytical / deterministic | Comparable ordered periods → trend/inflection evidence. |
| `cohort_analysis` | analytical / deterministic | Common anchor/windows → cohort comparison. |
| `anomaly_analysis` | validation / deterministic | Explicit expected range/distribution → unusual-observation candidates. |
| `exception_analysis` | validation / mixed | Approved rule/control and declared population → explicit violation candidates; never infer a missing rule. |
| `unmatched_elements_analysis` | validation / deterministic | Comparable populations and approved match rule → concrete one-sided/matched elements. |
| `reconciliation` | validation / deterministic | Comparable totals/keys → match/mismatch. |
| `factor_reconciliation` | validation / deterministic | Observed delta and executed factor effects → completeness gap/status. |
| `unexplained_residual` | validation / deterministic | Reconciled total/components → residual. |
| `data_layer_check` | validation / deterministic | Traceable `REPORT → MART → STAGE → RAW` lineage → first-appearance layer. |
| `timing_validation` | validation / mixed | Approved dates/cut-off definition → quantified timing/cross-period effect. |
| `alternative_explanation_test` | mixed / mixed | Deterministic discriminating tests plus bounded comparison → supported/rejected/unresolved explanations. |
| `robustness_to_baseline` | validation / deterministic | Defensible comparable baselines → conclusion stability. |
| `subgroup_robustness` | validation / deterministic | Sufficient material subgroups → stable/heterogeneous result. |
| `sensitivity_analysis` | validation / deterministic | Explicit plausible assumption range and model → range/breakpoints. |
| `forecast_to_period_end` | analytical / deterministic | Defined cut-off/method and adequate history → forecast with limitations. |
| `leading_indicator_analysis` | analytical / mixed | Defined target/precursor, temporal ordering and evidence basis → leading signal/association/risk, not causal prediction. |

Capability distinctions:

```text
anomaly_analysis != exception_analysis
reconciliation != unmatched_elements_analysis
factor_reconciliation != unexplained_residual
trend_analysis != timing_validation
reconciliation != data_layer_check
forecast_to_period_end != leading_indicator_analysis
```

## Active intent × method mapping

| Intent | CORE | TRIGGERED | OPTIONAL |
|---|---|---|---|
| `validate_data` | reconciliation, data-layer | anomaly, exception, unmatched, timing, segmentation, subgroup robustness | — |
| `diagnose_variance` | variance, contribution, unexplained residual, factor reconciliation | bridge, mix, unmatched, segmentation, trend, timing | baseline robustness |
| `explain_drivers` | driver decomposition, unexplained residual, factor reconciliation | alternative test, segmentation, trend, timing, data-layer | baseline robustness, sensitivity |
| `test_explanation` | alternative explanation test | baseline/subgroup robustness, sensitivity, timing, data-layer | cohort |
| `project_forward` | forecast to period end | sensitivity, leading indicator | trend, baseline robustness |

Every non-CORE selection requires `trigger_type`, a concrete `trigger_rule`, `trigger_evidence_required`, and deterministic mapping-level `priority`. Priority is non-numeric: CORE first; deterministic triggers before judgment/hybrid triggers; OPTIONAL last. Missing evidence cannot silently activate a method; a plausible omission is recorded for QA. Minimum sufficient set: include only methods capable of materially changing finding, confidence, risk, recommendation, limitation, or evidence assurance.

Trigger rules by intent:

- `validate_data`: reconciliation and data-layer are CORE; exception requires approved rule/population/fields/scope; unmatched requires comparable populations and approved match rule; timing requires dates/boundary/approved definition and material cut-off candidate.
- `diagnose_variance`: factor reconciliation is CORE; unmatched activates when additions/removals may explain variance; timing activates when cut-off may explain variance.
- `explain_drivers`: factor reconciliation is CORE; timing or data-layer activates when the candidate driver may reflect cut-off or transformation.
- `test_explanation`: timing/data-layer only when either is a materially plausible competing explanation.
- `project_forward`: leading indicator only when a defined precursor/target, temporal ordering, relevant history, and evidence basis can materially change outlook interpretation.

Every new non-CORE method uses the existing `trigger_type`, `trigger_rule`, `trigger_evidence_required`, `trigger_evidence`, and `priority` contract and the existing prerequisite gate.

## Output rule
```text
method:
metric:
period:
grain:
data source:
source mart:
limitation:
```
## Main file dependency
```text
mart_main_full
or documented mart slices derived from mart_main_full
```
Do not run final conclusions directly on raw/stage unless the task is explicitly a data QA task.
## Technique selection guide
- “Почему отклонение?” → `diagnose_variance`; add `explain_drivers` only for an explanatory question with prerequisites.
- “Что изменилось от начала к концу?” → bridge.
- “Где самые большие проблемы?” → contribution + segmentation.
- “Это ошибка или реальное событие?” → reconciliation + anomaly.
- “Какая динамика?” → trend.
- “Какие группы ведут себя по-разному?” → cohort / segmentation.
- “Можно ли доверять данным?” → reconciliation + DQ checks.

`driver_decomposition` produces driver candidates, not root cause.


## From: `ChatGPT/[Analytics]/Knowledge/ANALYTICAL_REASONING_STANDARD.md`

# Analytical Reasoning Standard — P0

## Boundary and flow

This is a bounded reasoning-control extension; it does not replace Data Contract, RAW, STAGE, MART, deterministic calculations, chart sourcing, memo, QA/Judge, acceptance, or handoff. `mart_main_full` remains evidence/reuse; compact marts remain management-facing.

Execution remains governed by repo-root `AUTONOMOUS_EXECUTION_STANDARD.md`; `docs/autonomous_execution/extensions/ANALYTICS_EXTENSION.md` remains authoritative for Analytics-specific AES requirements. Reasoning control structures method selection only; it does not fork AES states, correction limits, stop/rollback/acceptance, or external authority. It is not an autonomous agent or an independent retry/self-improvement loop.

```text
LLM reasoning != deterministic execution
TASK PROFILE → INTENT → deterministic-first minimum methods → prerequisite gate
→ existing execution → preliminary evidence → explanation challenge when material
→ claim calibration → final evidence sufficiency → existing QA/Judge
```

LLM may classify ambiguous intent and bounded judgment/hybrid triggers, challenge explanations, and calibrate wording. It cannot replace deterministic arithmetic, formulas, reconciliation, variance/driver/exposure calculations, classification, or a deterministically executable forecast. Missing prerequisites cannot be reasoned away.

## Task profile

```text
question; decision_user
materiality: low / medium / high
uncertainty: low / medium / high
reversibility: easy / medium / difficult
evidence_state: unknown / weak / mixed / strong
evidence_state_basis
analytical_depth: routine / material / decision_critical
output_mode: quick / standard / full
expected_output
challenge_level: minimal / standard / enhanced
robustness_required: yes / no
manual_review_required: yes / no
thinking_handoff_possible: yes / no
```

No numerical scoring. Analytical depth and output mode are independent. Routine → minimal; material → standard; decision-critical → enhanced plus robustness consideration and explicit evidence sufficiency.

Set `robustness_required = yes` only when a declared baseline, subgroup, or sensitivity trigger is satisfied. Set `thinking_handoff_possible = yes` only when the unresolved question crosses into alternatives, trade-offs, risk appetite, or decision.

Set `manual_review_required = yes` for causal/root-cause final language, unresolved material contradictory evidence, decision-critical weak/partial evidence, material judgment/hybrid influence, or required `[Thinking]` escalation. Record review owner/status/resolution before publication.

P0 active intents: `validate_data`, `diagnose_variance`, `explain_drivers`, `test_explanation`, `project_forward`. Deferred candidates: `locate_concentration`, `detect_anomalies`, `analyze_structure`, `analyze_trend`, `prepare_decision_evidence`, `evaluate_control`.

Canonical P0 registry contains exactly 22 methods, including `exception_analysis`, `unmatched_elements_analysis`, `factor_reconciliation`, `timing_validation`, `data_layer_check`, and `leading_indicator_analysis`. Controls remain controls; numerator/denominator/population, contradiction/discrimination/falsification, claim ladder, and stop conditions do not become methods. Trade-offs, premortem, reversibility, risk appetite, choice, and decision remain in `[Thinking]`. Expansion beyond 22 requires P1/pilot evidence or separate acceptance.

## Method plan and prerequisites

```text
method; intent; status: CORE / TRIGGERED / OPTIONAL
why_selected; question_answered
trigger; trigger_type; trigger_rule; trigger_evidence_required; trigger_evidence; priority
execution_owner; execution_mode
prerequisites_met: yes / no / not_applicable
execution_status: planned / executed / blocked / not_needed
missing_requirement; method_execution_id
```

`yes` means all requirements satisfied; `no` means a real requirement is unmet; `not_applicable` means no such requirement exists and cannot bypass one. `blocked != executed`; blocked is not evidence. Each period/grain/filter/baseline/population/scenario application needs a distinct `method_execution_id`. Explain exclusion only for materially plausible methods.

## Baseline and ratio controls

Record baseline type/period/rationale and whether an alternative is material. For material/decision-critical cases, a reasonable alternative capable of changing the conclusion requires `robustness_to_baseline`. Ratios require numerator + denominator + population; explain population/denominator and quantify additions, removals, filters, entities, cut-offs, and definition changes.

## Explanation challenge

Preliminary check records finding support (`yes / partial / no`), explanatory feasibility, critical gap, and next step (`continue / stop / collect evidence`). If infeasible: stop, state limitation, do not fabricate.

Material/decision-critical cases record current and competing explanations, contradicting and discriminating evidence, falsification test/result, and residual uncertainty. Ask what else explains the finding, what contradicts it, what test changes it, and what evidence distinguishes explanations.

```text
OBSERVATION → CALCULATED EFFECT → DRIVER CANDIDATE → SUPPORTED EXPLANATION → ROOT CAUSE
driver != root cause
correlation != causation
```

Material method disagreement remains contradictory evidence; preserve conflict, do not silently reconcile or average incompatible conclusions, constrain claim strength, and escalate if unresolved/material.

## Claim calibration

Preserve `confidence: high / medium / low`. Add independent `claim_support: SUPPORTED / PARTIALLY_SUPPORTED / HYPOTHESIS / UNSUPPORTED` and `causal_status: not_applicable / association_only / explanation_supported / causal_evidence`.

```text
confidence != claim_support != causal_status
claim strength <= final evidence sufficiency
```

For material/decision-critical claims, `FINAL_EVIDENCE_SUFFICIENCY` states what is sufficient for observation, calculated effect, driver candidate, supported explanation, and causal claim; status; missing discriminating evidence; remaining contradictions; maximum claim strength. LLM confidence, expectations, intuition, method count, and fluency cannot strengthen evidence.

Lineage: claim → `method_execution_id` → executed method → source mart/table/slice → metric/period/grain/filter/baseline → evidence. Blocked/planned/not-needed executions cannot support claims requiring results.

## Runtime, stop, escalation

Routine + low uncertainty + no material trigger uses question → intent → core/triggered method → deterministic result → compact QA → answer. Do not instantiate full challenge, competing explanations, falsification, expanded registry, or evidence-sufficiency records without a trigger; preserve quick-mode budget.

Stop when added methods cannot materially change the outcome, discriminating evidence is unavailable, precision exceeds data quality, conclusion is robust, the remaining question is strategic, or complexity adds no decision value. Escalate for materially plausible competing explanations, unresolved contradictory/method conflict, unsupported assumptions, causal language without causal evidence, or evidence outside Analytics ownership. `[Analytics]` owns verified evidence; `[Thinking]` owns alternatives/trade-offs/risk appetite/decision.

P1 pilot calibration and P2 expanded/autonomous taxonomies remain deferred; do not claim them implemented.


## From: `ChatGPT/[Analytics]/Knowledge/CHART_SELECTION_STANDARD.md`

# Chart Selection Standard
## Purpose
## Source rule
```text
chart_name:
purpose:
source_mart:
source_slice:
metric:
period:
grain:
filter:
caption_claim:
limitations:
```
Source must be:
```text
mart_main_full
or mart slice derived from mart_main_full
```
## Recommended chart types
## Do not use chart when
- metric is not defined;
- source mart is missing;
- grain is mixed;
- currency/unit not normalized;
- sample is too small;
- caption is stronger than data;
- chart duplicates table without insight.
## Executive visual and language standard
- Графики для executive memo используют спокойную управленческую палитру.
- Executive chart colors must be muted and business-readable; no neon colors and no default bright matplotlib palette.
- Chart labels, legends, axes, titles and captions must use Russian business-readable labels.
- Technical values such as `fact_only`, `plan_only`, `p_fact_adjusted`, `refund_only`, `source_mix`, `slice_*`, `mart_*`, `EV-*`, `CH_EXEC_*` must not appear in visible executive chart elements unless the chart is explicitly in appendix / evidence context.
- Technical IDs may remain in chart specs, datasets, catalog technical fields and evidence layer.
- Captions must not exceed evidence.
## Chart acceptance
- [ ] Purpose clear.
- [ ] Source mart listed.
- [ ] Metric listed.
- [ ] Grain listed.
- [ ] Period listed.
- [ ] Caption does not exceed evidence.
- [ ] Limitation visible.
- [ ] Executive chart uses compact mart or slice from full mart.
- [ ] Chart labels are Russian / business-readable.
- [ ] Executive chart palette uses muted executive colors.
- [ ] Technical IDs only in appendix / evidence.
