# [Analytics] — Techniques and Charts

## Purpose

Compact upload artifact for [Analytics] covering techniques and charts.

## Source files

- `ChatGPT/[Analytics]/Knowledge/ANALYTICAL_TECHNIQUES.md`
- `ChatGPT/[Analytics]/Knowledge/ANALYTICAL_REASONING_STANDARD.md`
- `ChatGPT/[Analytics]/Knowledge/VARIANCE_DIAGNOSTIC_CONTRACT.md`
- `ChatGPT/[Analytics]/Knowledge/CHART_SELECTION_STANDARD.md`
- `ChatGPT/[Analytics]/Knowledge/ANALYTICS_03_TECHNIQUES_AND_CHARTS_BUNDLE_SEMANTICS.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[Analytics]`.

## Status

- production_promotion: no, unless explicitly accepted elsewhere
- bundle_type: generated compact upload artifact
- source_of_truth: declared granular source files
- source_fingerprint: sha256:66442553fd94874649fe2973c84d0404624493a0ed0d15cbb3176f85df477675
- generator: scripts/build_knowledge_bundles.py

---

# Content

## From: `ChatGPT/[Analytics]/Knowledge/ANALYTICAL_TECHNIQUES.md`

# Analytical Techniques
## P0 method registry
This registry is the source of truth for method eligibility. Selection follows `ANALYTICAL_REASONING_STANDARD.md`; registry entries do not mean a method has been executed.
For P0, `NAME` is the stable registry label represented by `METHOD_ID`; a display label may replace underscores with spaces but cannot change method identity.
Required registry schema:
```text
METHOD_ID
NAME
PURPOSE
METHOD_ROLE: analytical / validation / mixed
REQUIRES
INPUT_GRAIN
REQUIRED_METRICS
OUTPUT
EXECUTION_OWNER
EXECUTION_MODE: deterministic / reasoning / mixed
VALIDATION_OWNER
LIMITATION
FAILURE_MODE
```
For `EXECUTION_MODE = mixed`, also record `deterministic_component` and `reasoning_component`.
Canonical active P0 scope:
```text
P0 METHOD COUNT = 22
```
For material Plan/Fact cases, `VARIANCE_DIAGNOSTIC_CONTRACT.md` configures the existing methods; it does not create a new `METHOD_ID`. `variance_analysis` preserves the declared source/raw formula and separately normalizes management direction from an explicit KPI rule. `contribution_analysis` exposes gross adverse/favorable movement and declared gross coverage. `bridge_analysis` and `factor_reconciliation` use one normalized sign convention and non-overlapping effects. `unexplained_residual` keeps incomplete attribution visible. Controllability, recurrence, budget status, materiality, coverage, and accountability are runtime attributes or controls, not methods.
Capability groups are a readability aid only and do not create runtime taxonomy or routing:
```text
DECOMPOSE: variance_analysis, contribution_analysis, bridge_analysis, driver_decomposition, mix_analysis
LOCATE: segmentation, cohort_analysis, anomaly_analysis, exception_analysis, unmatched_elements_analysis
VALIDATE: reconciliation, factor_reconciliation, unexplained_residual, data_layer_check, timing_validation
CHALLENGE: alternative_explanation_test, robustness_to_baseline, subgroup_robustness, sensitivity_analysis
FORWARD: trend_analysis, forecast_to_period_end, leading_indicator_analysis
```
| METHOD_ID | PURPOSE | METHOD_ROLE / EXECUTION_MODE | REQUIRES; INPUT_GRAIN; REQUIRED_METRICS | OUTPUT | EXECUTION_OWNER / VALIDATION_OWNER | LIMITATION / FAILURE_MODE |
|---|---|---|---|---|---|---|
| `variance_analysis` | Quantify change against a baseline | analytical / deterministic | Comparable actual and baseline; aligned analytical grain; actual and baseline metric | Absolute/relative variance | deterministic Analytics executor / Calculation QA | Baseline-sensitive; misaligned periods or grain |
| `contribution_analysis` | Rank contributions to a total movement | analytical / deterministic | Reconciled total and additive components; component grain; component delta | Ranked contribution and coverage | deterministic Analytics executor / Calculation QA | Non-additive metrics; contributions do not reconcile |
| `bridge_analysis` | Reconcile start-to-end movement through components | analytical / deterministic | Start, end, and additive movements; bridge-component grain; start/end/change metrics | Reconciled bridge | deterministic Analytics executor / Calculation QA | Overlapping or missing bridge components |
| `driver_decomposition` | Quantify candidate drivers of an outcome | analytical / mixed | Defined driver model and verified measures; driver grain; outcome and driver metrics | Quantified driver candidates and residual | deterministic executor plus bounded reasoning / Analysis QA | Decomposition is not causal proof; omitted or collinear drivers |
| `mix_analysis` | Separate composition effects | analytical / deterministic | Stable category definitions and weights; component/population grain; value and weight metrics | Mix effect | deterministic Analytics executor / Calculation QA | Population or denominator changes hidden |
| `segmentation` | Compare materially different groups | analytical / deterministic | Valid segment definition and sufficient subgroup data; segment grain; target metric | Segment comparison | deterministic Analytics executor / Analysis QA | Selection bias or sparse groups |
| `trend_analysis` | Evaluate direction and inflection over time | analytical / deterministic | Comparable ordered periods; time × analytical grain; target metric | Trend and inflection evidence | deterministic Analytics executor / Analysis QA | Seasonality, cut-off, or short history |
| `cohort_analysis` | Compare populations anchored to a common event/time | analytical / deterministic | Cohort key, anchor, and comparable observation windows; cohort × age grain; target rate/count | Cohort curves or comparison | deterministic Analytics executor / Analysis QA | Immature cohorts or changing definitions |
| `anomaly_analysis` | Identify observations unusual relative to an explicit expected range or distribution | validation / deterministic | Expected range/distribution and verified inputs; event/entity grain; tested metric and threshold | Anomaly candidates | deterministic Analytics executor / Data QA | Threshold dependence and false positives |
| `exception_analysis` | Identify violations of an explicit rule, control condition, process requirement, policy threshold, or required state | validation / mixed | Approved exception/control rule, relevant population, required fields, and scope/filter; entity/transaction grain; rule inputs | Rule-violation candidates and rule result | deterministic detection plus bounded reasoning / Data QA | Missing/ambiguous rule blocks execution; inferred rules or interpretation drift |
| `unmatched_elements_analysis` | Identify concrete elements present on only one side of a comparison | validation / deterministic | Two comparable populations, approved matching key/rule, defined scope, duplicate treatment; entity/key grain; presence/match fields | `only_in_left`, `only_in_right`, `matched` populations | deterministic Analytics executor / Data QA | Invalid keys, duplicate ambiguity, or unapproved fuzzy matching |
| `reconciliation` | Test integrity across layers or totals | validation / deterministic | Comparable source and target totals/keys; reconciliation grain; control totals | Match, mismatch, and unexplained difference | deterministic Analytics executor / Data QA | Incomparable scope or hidden exclusions |
| `factor_reconciliation` | Validate mathematical completeness of factor/driver decomposition | validation / deterministic | Observed total delta, executed decomposition, calculated effects, consistent scope/period/baseline; decomposition grain; total delta and factor effects | Total delta, summed effects, gap, and status | deterministic Analytics executor / Calculation QA | Inconsistent scope or incomplete/overlapping factor effects |
| `unexplained_residual` | Quantify movement not explained by selected components | validation / deterministic | Reconciled total and explained components; total/component grain; total and contributions | Residual value/share | deterministic Analytics executor / Calculation QA | Residual inherits upstream errors |
| `data_layer_check` | Locate the verified RAW/STAGE/MART/report layer where an effect first appears | validation / deterministic | Traceable lineage, comparable grain or explicit aggregation bridge, mapping/transformation definitions; lineage grain; layer values/classifications | First-appearance layer and layer comparison | deterministic Analytics executor / Data QA | Missing lineage or incomparable layers; does not repair pipeline logic |
| `timing_validation` | Test whether an effect is a timing, recognition, posting, settlement, accrual, or cut-off artifact | validation / mixed | Event/transaction and posting/recognition dates, period boundary, entity grain, approved timing definition; timing grain; dated amount/status | Timing classification and quantified cross-period effect | deterministic comparison plus bounded reasoning / Analysis QA | Missing cut-off evidence, ambiguous timing definition, or cross-period incomparability |
| `alternative_explanation_test` | Compare a leading explanation with plausible alternatives | mixed / mixed | Explicit explanations and discriminating observable evidence; claim-relevant grain; test metrics | Supported/rejected/unresolved explanations | deterministic test plus bounded reasoning / Analysis QA | Unobserved confounding or non-discriminating test |
| `robustness_to_baseline` | Test conclusion under reasonable baselines | validation / deterministic | At least two defensible baselines; same analytical grain; target metric by baseline | Stability/change of conclusion | deterministic Analytics executor / Analysis QA | Arbitrary or incomparable alternatives |
| `subgroup_robustness` | Test whether a conclusion holds across relevant groups | validation / deterministic | Material subgroup definition and sufficient data; subgroup grain; claim metric | Stable/heterogeneous subgroup result | deterministic Analytics executor / Analysis QA | Sparse or selected subgroups |
| `sensitivity_analysis` | Test response to plausible assumptions | validation / deterministic | Explicit assumption range and deterministic model; scenario × analytical grain; outcome metric | Sensitivity range and breakpoints | deterministic Analytics executor / Analysis QA | Implausible range or interacting assumptions omitted |
| `forecast_to_period_end` | Project a metric to period end | analytical / deterministic | Defined cut-off, deterministic forecast method, and adequate history; time × analytical grain; actual and forecast driver metrics | Forecast and uncertainty/limitations | deterministic Analytics executor / Calculation QA | Structural break, incomplete period, false precision |
| `leading_indicator_analysis` | Evaluate verified precursor metrics that may alter forward interpretation before the target metric changes | analytical / mixed | Defined target and indicator, temporal ordering, sufficient history where relevant, approved relationship/evidence basis; time grain; indicator and target metrics | Leading signal, association, and forward-risk evidence | deterministic temporal/association analysis plus bounded reasoning / Analysis QA | Spurious association, insufficient history, or causal overstatement |
Mixed-component contract:
| METHOD_ID | deterministic_component | reasoning_component |
|---|---|---|
| `driver_decomposition` | Execute the declared decomposition and residual calculation. | Interpret quantified outputs as driver candidates, not root causes. |
| `alternative_explanation_test` | Execute declared discriminating tests where deterministic evidence is available. | Compare explanations, contradictions, and residual uncertainty without inventing evidence. |
| `exception_analysis` | Apply the approved rule to the declared population and return violations. | Interpret only approved rule ambiguity/material relevance; never infer a missing rule. |
| `timing_validation` | Compare approved dates/cut-offs and quantify cross-period movement. | Interpret timing classification only where the approved definition requires bounded judgment. |
| `leading_indicator_analysis` | Establish temporal ordering and calculate the declared indicator/target relationship. | Calibrate forward relevance as signal/association/risk, never causal prediction without evidence. |
## Capability distinctions
```text
anomaly_analysis != exception_analysis
reconciliation != unmatched_elements_analysis
factor_reconciliation != unexplained_residual
trend_analysis != timing_validation
reconciliation != data_layer_check
forecast_to_period_end != leading_indicator_analysis
```
- Anomaly analysis finds unusual observations; exception analysis tests explicit rule/control violations.
- Reconciliation tests totals/balances; unmatched analysis identifies concrete one-sided elements.
- Factor reconciliation validates decomposition completeness; unexplained residual quantifies what remains.
- Trend analysis describes movement over time; timing validation tests whether movement is a cut-off artifact.
- Reconciliation can pass while mapping/transformation logic is wrong; data-layer check locates first appearance across `REPORT → MART → STAGE → RAW`.
- Forecast estimates the target outcome; leading-indicator analysis evaluates verified precursor signals and cannot present them as causal predictors without supporting evidence.
## Active intent × method mapping
| Intent | CORE | TRIGGERED | OPTIONAL |
|---|---|---|---|
| `validate_data` | `reconciliation`, `data_layer_check` | `anomaly_analysis`, `exception_analysis`, `unmatched_elements_analysis`, `timing_validation`, `segmentation`, `subgroup_robustness` | — |
| `diagnose_variance` | `variance_analysis`, `contribution_analysis`, `unexplained_residual`, `factor_reconciliation` | `bridge_analysis`, `mix_analysis`, `unmatched_elements_analysis`, `segmentation`, `trend_analysis`, `timing_validation` | `robustness_to_baseline` |
| `explain_drivers` | `driver_decomposition`, `unexplained_residual`, `factor_reconciliation` | `alternative_explanation_test`, `segmentation`, `trend_analysis`, `timing_validation`, `data_layer_check` | `robustness_to_baseline`, `sensitivity_analysis` |
| `test_explanation` | `alternative_explanation_test` | `robustness_to_baseline`, `subgroup_robustness`, `sensitivity_analysis`, `timing_validation`, `data_layer_check` | `cohort_analysis` |
| `project_forward` | `forecast_to_period_end` | `sensitivity_analysis`, `leading_indicator_analysis` | `trend_analysis`, `robustness_to_baseline` |
## Trigger contracts for non-CORE methods
Every `INTENT × METHOD` entry has a non-numeric `priority` derived deterministically from status and trigger type:
```text
CORE → core_first
TRIGGERED + deterministic → deterministic_trigger_first
TRIGGERED + judgment / hybrid → judgment_hybrid_after_deterministic
OPTIONAL → optional_last
```
This precedence is the mapping-level `PRIORITY` contract. It orders eligibility evaluation; it is not a quality score and cannot bypass prerequisites or trigger evidence.
| Intent / method | trigger_type | trigger_rule | trigger_evidence_required |
|---|---|---|---|
| `validate_data` / `anomaly_analysis` | deterministic | A declared validation rule or threshold is breached in verified inputs. | Rule/threshold, tested field, and breach result. |
| `validate_data` / `exception_analysis` | hybrid | An approved rule/control condition exists and testing violations is material to data/process validity. | Explicit rule, population, required fields, scope/filter, and evidence of rule applicability. |
| `validate_data` / `unmatched_elements_analysis` | deterministic | Two populations are expected to align and entity-level mismatch may explain the issue. | Comparable populations, approved matching key/rule, scope, and duplicate treatment. |
| `validate_data` / `timing_validation` | hybrid | Period cut-off or timing shift could materially affect validity or interpretation. | Relevant dates, period boundary, entity grain, approved timing definition, and timing candidate evidence. |
| `validate_data` / `segmentation` | hybrid | Mismatch/anomaly candidates span a declared segment dimension and segment comparison could localize a material integrity issue. | Candidate records, valid segment field, and segment counts/coverage. |
| `validate_data` / `subgroup_robustness` | hybrid | A validation conclusion may differ across a materially relevant subgroup. | Overall result plus sufficient subgroup observations. |
| `diagnose_variance` / `bridge_analysis` | deterministic | Start-to-end delta has additive, non-overlapping components that must reconcile. | Start/end totals and component mapping. |
| `diagnose_variance` / `mix_analysis` | hybrid | Verified population/category weights changed and the change could materially affect the total variance. | Period weights, category definitions, and target metric. |
| `diagnose_variance` / `segmentation` | hybrid | Aggregate variance contains materially heterogeneous eligible groups. | Aggregate result and comparable segment-level inputs. |
| `diagnose_variance` / `trend_analysis` | deterministic | Three or more comparable ordered periods are available and timing can change interpretation. | Comparable time series and cut-off metadata. |
| `diagnose_variance` / `unmatched_elements_analysis` | deterministic | Population additions/removals may materially explain the variance. | Comparable period populations, matching rule, duplicate treatment, and variance scope. |
| `diagnose_variance` / `timing_validation` | hybrid | Cut-off, posting, recognition, or cross-period movement may materially explain variance. | Relevant dates, boundary, approved timing definition, and variance candidate. |
| `diagnose_variance` / `robustness_to_baseline` | judgment | A reasonable alternative baseline could materially change a material/decision-critical conclusion. | Current baseline, alternative baseline rationale, and comparable inputs. |
| `explain_drivers` / `alternative_explanation_test` | judgment | At least one materially plausible competing explanation has observable distinguishing evidence. | Leading/competing explanations and proposed discriminating evidence. |
| `explain_drivers` / `segmentation` | hybrid | Quantified driver candidates may differ across a materially relevant segment. | Driver result plus comparable segment inputs. |
| `explain_drivers` / `trend_analysis` | deterministic | Comparable time observations exist and sequence/timing can distinguish explanations. | Ordered time series and event/cut-off metadata. |
| `explain_drivers` / `robustness_to_baseline` | judgment | A reasonable baseline alternative could change driver ranking or claim strength. | Baseline alternatives and comparable driver inputs. |
| `explain_drivers` / `sensitivity_analysis` | hybrid | A quantified driver claim depends materially on an explicit uncertain assumption. | Deterministic model, assumption, plausible range, and target output. |
| `explain_drivers` / `timing_validation` | hybrid | A candidate driver may reflect timing/cut-off rather than economic change. | Driver result, relevant dates/boundary, approved timing definition, and candidate timing evidence. |
| `explain_drivers` / `data_layer_check` | hybrid | A candidate driver may originate from transformation/mapping rather than source data. | Driver result, traceable layers, comparable grain/bridge, and relevant transformation definitions. |
| `test_explanation` / `robustness_to_baseline` | judgment | The explanation depends on a baseline choice with a reasonable alternative. | Explanation, current/alternative baselines, and comparable data. |
| `test_explanation` / `subgroup_robustness` | hybrid | The explanation could fail in a materially relevant subgroup with sufficient data. | Overall evidence and eligible subgroup data. |
| `test_explanation` / `sensitivity_analysis` | hybrid | The explanation changes under a plausible range of an explicit assumption. | Deterministic test model and justified range. |
| `test_explanation` / `cohort_analysis` | hybrid | Cohort timing/population could distinguish plausible explanations and observation windows are comparable. | Cohort key, anchor, windows, and sufficient observations. |
| `test_explanation` / `timing_validation` | hybrid | Timing/cut-off is a materially plausible competing explanation. | Current explanation, relevant dates/boundary, approved timing definition, and discriminating timing evidence. |
| `test_explanation` / `data_layer_check` | hybrid | Mapping/transformation artifact is a materially plausible competing explanation. | Current explanation, traceable layers, comparable grain/bridge, and transformation definitions. |
| `project_forward` / `sensitivity_analysis` | deterministic | The forecast contains an explicit uncertain input whose plausible range materially changes the output. | Forecast model, input range, and scenario outputs. |
| `project_forward` / `trend_analysis` | deterministic | Comparable history is available and trend evidence informs method or limitation. | Ordered history with stable metric definition. |
| `project_forward` / `robustness_to_baseline` | judgment | A reasonable alternative forecast baseline could materially change the projected conclusion. | Current and alternative baselines with rationale. |
| `project_forward` / `leading_indicator_analysis` | hybrid | Verified precursor metrics exist and could materially change interpretation of the forward outlook. | Defined indicator and target, temporal ordering, history where relevant, and evidence basis for relevance. |
Absent required trigger evidence means the method does not become `TRIGGERED`. Record a materially plausible omission for Analysis QA instead of silently changing the mapping.
## Output rule
For each technique state:
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
Techniques should run on:
```text
mart_main_full
or documented mart slices derived from mart_main_full
```
Do not run final conclusions directly on raw/stage unless the task is explicitly a data QA task.
## Technique selection guide
- “Почему отклонение?” → `diagnose_variance`; use `explain_drivers` only when an explanatory question and prerequisites exist.
- “Что изменилось от начала к концу?” → bridge.
- “Где самые большие проблемы?” → contribution + segmentation.
- “Это ошибка или реальное событие?” → reconciliation + anomaly.
- “Какая динамика?” → trend.
- “Какие группы ведут себя по-разному?” → cohort / segmentation.
- “Можно ли доверять данным?” → reconciliation + DQ checks.
Use only the minimum sufficient method set. A method must be able to materially change a finding, confidence, risk, recommendation, limitation, or evidence assurance. `driver_decomposition` produces driver candidates; it does not by itself establish root cause.

## From: `ChatGPT/[Analytics]/Knowledge/ANALYTICAL_REASONING_STANDARD.md`

# Analytical Reasoning Standard — P0
## Purpose and boundary
This standard adds a bounded reasoning-control layer to the existing `[Analytics]` workflow. It does not replace or redefine the Data Contract, RAW, `stage_main_full`, `mart_main_full`, `mart_main_tz` / `mart_main_compact`, deterministic calculations, chart sourcing, memo pipeline, QA / Judge, acceptance, or Codex handoff boundary.
Execution remains governed by the canonical repo-root `docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md`. `docs/autonomous_execution/extensions/ANALYTICS_EXTENSION.md` remains authoritative for Analytics-specific AES requirements. This standard structures analytical reasoning and method selection only; it does not fork, weaken, or duplicate AES execution states, corrective-loop limits, stop conditions, rollback, acceptance, or external-action authority.
New AES execution records use the canonical v2 contract and its required
Closure Review. Historical v1 records remain read-only evidence, not a path
for new successful Analytics work.
```text
reasoning-control loop != autonomous execution framework
adaptive reasoning != autonomous agent
adaptive reasoning does not create an independent retry/self-improvement loop
```
```text
business question
→ task profile and analytical intent
→ deterministic-first minimum sufficient method set
→ prerequisite gate
→ existing Analytics execution
→ preliminary evidence check
→ explanation challenge when material
→ claim calibration and final evidence sufficiency
→ existing QA / Judge / acceptance
```
`mart_main_full` remains the evidence and reuse layer. Management-facing marts remain `mart_main_tz` / `mart_main_compact`. Calculations, slices, and chart sources continue to use verified analytical layers.
Explicit boundary:
```text
LLM reasoning != deterministic execution
```
The LLM may classify ambiguous intent, evaluate bounded judgment or hybrid triggers, challenge explanations, and calibrate wording. It cannot replace deterministic arithmetic, formulas, reconciliation, variance, driver or exposure calculations, deterministic classification, or a deterministically executable forecast. Missing deterministic prerequisites cannot be compensated by reasoning.
## 1. `TASK_PROFILE` and derived controls
Create the profile before method selection when the case is not eligible for the compact routine path:
```text
TASK_PROFILE
question:
decision_user:
materiality: low / medium / high
uncertainty: low / medium / high
reversibility: easy / medium / difficult
evidence_state: unknown / weak / mixed / strong
evidence_state_basis:
analytical_depth: routine / material / decision_critical
output_mode: quick / standard / full
expected_output:
challenge_level: minimal / standard / enhanced
robustness_required: yes / no
manual_review_required: yes / no
thinking_handoff_possible: yes / no
```
Do not create a numerical score. `analytical_depth` controls reasoning depth; `output_mode` controls artifact size. They are independent.
Base mapping:
| analytical_depth | challenge_level | Derived control |
|---|---|---|
| `routine` | `minimal` | Use compact reasoning unless a material trigger appears. |
| `material` | `standard` | Apply the standard challenge and relevant robustness controls. |
| `decision_critical` | `enhanced` | Consider robustness and record explicit final evidence sufficiency. |
Set `robustness_required = yes` when a declared baseline, subgroup, or sensitivity robustness trigger is satisfied; otherwise `no`. Set `thinking_handoff_possible = yes` when the unresolved question crosses the stop/escalation boundary into alternatives, trade-offs, risk appetite, or decision; otherwise `no`.
Set `manual_review_required = yes` when at least one materially relevant condition holds:
- the final claim uses causal or root-cause language;
- material contradictory evidence remains unresolved;
- a decision-critical conclusion has weak or partial evidence;
- a judgment or hybrid method materially affects the final claim;
- the Analytics conclusion requires escalation or handoff to `[Thinking]`.
When set to `yes`, the analysis cannot pass final publication automatically: record the reviewer or review owner, review status, and resolution in the existing Analysis QA / acceptance path. In other cases, use the existing governance and risk context without inventing a scoring model.
## 2. Analytical intents
P0 activates only:
```text
validate_data
diagnose_variance
explain_drivers
test_explanation
project_forward
```
Candidate intents are deferred and must not be routed as active P0 intents without pilot evidence:
```text
locate_concentration
detect_anomalies
analyze_structure
analyze_trend
prepare_decision_evidence
evaluate_control
```
Classify the business question to the narrowest active intent that can answer it. When several intents are required, record each one and its distinct question; do not expand the taxonomy.
## 3. Deterministic-first method selection
`ANALYTICAL_TECHNIQUES.md` is the source of truth for method eligibility, registry metadata, intent mapping, and method triggers.
```text
INTENT
↓
INTENT × METHOD MAPPING
↓
CORE METHODS
↓
DETERMINISTIC TRIGGERS
↓
TRIGGERED METHODS
↓
JUDGMENT / HYBRID TRIGGERS
↓
BOUNDED LLM REVIEW
↓
OPTIONAL / MATERIAL OMISSION CHECK
```
Method status semantics:
- `CORE`: selected for the intent, subject to prerequisites.
- `TRIGGERED`: selected only when its declared trigger contract is satisfied.
- `OPTIONAL`: considered only when materially plausible and capable of changing the analytical outcome.
For every non-CORE selection that depends on a trigger, the mapping must define:
```text
trigger_type: deterministic / judgment / hybrid
trigger_rule:
trigger_evidence_required:
priority:
```
- `deterministic`: verified inputs satisfy an unambiguous calculation or rule.
- `judgment`: bounded analytical reasoning is required.
- `hybrid`: deterministic evidence creates a candidate trigger; bounded reasoning determines material relevance.
Absent trigger evidence cannot silently activate a method. The LLM cannot silently override the registry. A materially plausible omitted method is recorded as `candidate_omission` with rationale and sent to existing QA / review; it is not silently included.
### Minimum sufficient method set
Include a method only if it can materially change at least one of:
```text
finding
confidence
risk
recommendation
limitation
evidence assurance
```
Stop adding methods when none is likely to change those outputs. Method count is not evidence strength.
### Canonical P0 registry scope
The active P0 registry contains exactly 22 approved methods. The six capability-gap additions are `exception_analysis`, `unmatched_elements_analysis`, `factor_reconciliation`, `timing_validation`, `data_layer_check`, and `leading_indicator_analysis`. `ANALYTICAL_TECHNIQUES.md` owns their schema, eligibility, prerequisites, execution boundary, and triggers.
Capability completeness must not inflate the registry. Do not create additional `METHOD_ID` values for contradicting/discriminating evidence, falsification, hypothesis/claim ladders, numerator/denominator/population controls, stop conditions, largest-variance ranking, time lens, detail checks, or structure-of-change configurations. These remain reasoning, QA, governance, or configurations of existing methods.
Decision methods such as robust/no-regret/conditional action, premortem, decision reversibility, and trade-off analysis remain owned by `[Thinking]`. `[Analytics]` provides forecast, sensitivity, verified evidence/uncertainty, downside, and leading indicators without making the strategic choice.
Any registry expansion beyond 22 requires P1/pilot evidence or separate explicit acceptance. Do not add methods merely to reproduce a mixed 45-technique catalog.
## 4. Method plan and prerequisite gate
For every concrete planned application, record:
```text
METHOD_PLAN
method:
intent:
status: CORE / TRIGGERED / OPTIONAL
why_selected:
question_answered:
trigger:
trigger_type:
trigger_rule:
trigger_evidence_required:
trigger_evidence:
priority:
execution_owner:
execution_mode: deterministic / reasoning / mixed
prerequisites_met: yes / no / not_applicable
execution_status: planned / executed / blocked / not_needed
missing_requirement:
method_execution_id:
```
Prerequisite semantics:
- `yes`: all required prerequisites exist and are satisfied;
- `no`: a required prerequisite exists but is unavailable or unmet;
- `not_applicable`: the method has no prerequisite of the relevant type.
`not_applicable` cannot bypass a real missing prerequisite.
```text
blocked != executed
blocked method != supporting evidence
```
`method_execution_id` uniquely identifies one application within the analysis. Repeated applications with a different period, grain, filter, baseline, population, or scenario require separate IDs. `WHY_EXCLUDED` is required only for materially plausible excluded methods.
## 5. Baseline, population, and denominator controls
For baseline-dependent analysis record:
```text
baseline:
  type:
  period:
  rationale:
alternative_baseline_material: yes / no
```
For a material or decision-critical case, if a reasonable alternative baseline could materially change the conclusion, `robustness_to_baseline` is required, subject to its prerequisites.
For ratios, averages, rates, margins, productivity, conversion, mix, and analogous measures, record:
```text
population_constant_or_explained?:
denominator_constant_or_explained?:
scope_change_quantified?:
```
Check additions, removals, filter changes, entity changes, cut-off changes, and denominator-definition changes.
```text
ratio interpretation requires numerator + denominator + population
```
```text
population/denominator materially unexplained -> claim_support <= PARTIALLY_SUPPORTED
```
If `population_constant_or_explained?` or `denominator_constant_or_explained?` is `no` and the underlying change is material and not quantified (`scope_change_quantified?` not satisfied), the ratio/rate/margin/mix claim cannot be recorded as `SUPPORTED`; a headline or management conclusion built on it is capped at `claim_support <= PARTIALLY_SUPPORTED` until the population/denominator shift is quantified and shown not to change the conclusion. Once so quantified, the cap does not apply.
### Material Plan/Fact and variance diagnostics
`VARIANCE_DIAGNOSTIC_CONTRACT.md` owns the bounded runtime/output controls for material Plan/Fact cases: source-sign preservation, explicit management-direction normalization, gross bridge, reconciled primary attribution, separate gross classification coverage, declared materiality, evidence-constrained secondary attributes, reported-versus-adjusted views, and CFO synthesis order.
It reuses the existing `diagnose_variance` mapping and approved methods. It does not add an intent, method, registry, or workflow. Activate the full diagnostic only for material/decision-critical cases or a material variance risk; routine/quick cases keep the compact path.
```text
raw/source variance != normalized management direction
net attribution reconciliation != absolute classification coverage
primary attribution is additive; secondary management attributes are not
driver/effect != controllability != accountability
single-period evidence != systemic / non-systemic evidence
reported result != adjusted management view
```
## 6. Preliminary evidence and explanation challenge
After deterministic findings and before explanation, record when the analysis is material or decision-critical:
```text
PRELIMINARY_EVIDENCE_CHECK
finding_supported: yes / partial / no
explanatory_analysis_feasible: yes / no
critical_evidence_gap:
next_step: continue / stop / collect evidence
```
If explanatory analysis is not feasible, stop, state the limitation, and do not fabricate an explanation.
For material and decision-critical cases ask:
1. What else could explain this?
2. What evidence contradicts the current explanation?
3. What test could materially change the conclusion?
4. What observable evidence distinguishes the leading explanations?
Runtime record:
```text
CURRENT_EXPLANATION:
COMPETING_EXPLANATIONS[]:
CONTRADICTING_EVIDENCE:
DISCRIMINATING_EVIDENCE:
FALSIFICATION_TEST:
TEST_RESULT:
RESIDUAL_UNCERTAINTY:
```
Claim ladder:
```text
OBSERVATION
→ CALCULATED EFFECT
→ DRIVER CANDIDATE
→ SUPPORTED EXPLANATION
→ ROOT CAUSE
```
```text
driver != root cause
correlation != causation
```
`ROOT CAUSE` is allowed only when the evidence and analytical design support causal language.
Discriminating alternative-explanation evidence (competing explanations tested and narrowed, per §6's `EXPLANATION CHALLENGE`) may promote a claim to `SUPPORTED EXPLANATION`; it does not by itself reach `ROOT CAUSE`. Promotion to `ROOT CAUSE` additionally requires causal evidence or a causal-capable analytical design (`causal_status: causal_evidence`) — for example a controlled comparison, natural experiment, or a registry method able to isolate cause from association. Absent that, the maximum claim strength stops at `SUPPORTED EXPLANATION` / driver candidate, even when alternative explanations have been ruled out.
### Method disagreement
When materially relevant methods produce incompatible interpretations or conclusions:
```text
material method disagreement
→ record as contradictory evidence
→ preserve conflicting results
→ no silent LLM reconciliation
→ do not average incompatible conclusions
→ constrain maximum claim strength
→ escalate when the conflict remains material
```
Unresolved disagreement remains visible in `CONTRADICTING_EVIDENCE`, `RESIDUAL_UNCERTAINTY`, and `FINAL_EVIDENCE_SUFFICIENCY`.
## 7. Claim and evidence calibration
Preserve the existing confidence taxonomy:
```text
confidence: high / medium / low
```
Add independent dimensions:
```text
claim_support: SUPPORTED / PARTIALLY_SUPPORTED / HYPOTHESIS / UNSUPPORTED
causal_status: not_applicable / association_only / explanation_supported / causal_evidence
```
Invariant:
```text
confidence != claim_support != causal_status
```
For material and decision-critical final claims record:
```text
FINAL_EVIDENCE_SUFFICIENCY
sufficient_for:
- observation
- calculated_effect
- driver_candidate
- supported_explanation
- causal_claim
status: sufficient / partial / insufficient
missing_discriminating_evidence:
contradictory_evidence_remaining:
maximum_claim_strength:
```
```text
claim strength <= final evidence sufficiency
```
LLM confidence, management expectation, expert intuition, method count, and narrative fluency cannot strengthen a claim beyond the evidence.
The existing `CLAIM_EVIDENCE_REGISTRY_TEMPLATE.md` owns claim-level fields. Required lineage is:
```text
claim
→ method_execution_id
→ executed method
→ source mart / table / slice
→ metric / period / grain / filter / baseline
→ evidence
```
`formula_or_method` remains a human-readable description and does not replace `method_execution_id`. A claim that requires an actual method result cannot use an execution with status `blocked`, `planned`, or `not_needed` as supporting evidence.
## 8. Analytical Judge gate
An explicit, bounded orchestration checkpoint that runs **after deterministic findings and before narrative packaging** (memo / report). It challenges the analytical conclusion itself. It does not add a QA framework, taxonomy, method, intent, or execution state: it reads the controls already defined in §4–§7 and the existing Analytics QA, and returns one visible result.
```text
deterministic calculation
→ findings
→ ANALYTICAL JUDGE
→ pass / revise / blocked
→ revise or rerun when required
→ final findings
→ memo / report
→ existing Memo QA / Judge
→ acceptance
```
### Seven checks (semantic, over existing controls — no new definitions)
| # | Judge check | Reads |
|---|---|---|
| 1 | Question fit — did the analysis answer the declared business question and scope? | `TASK_PROFILE.question`, active intent classification (§1–§2), `expected_output` |
| 2 | Method adequacy — were the selected methods sufficient, and was every supporting method actually executed with prerequisites met? | `METHOD_PLAN` (`status`, `prerequisites_met`, `execution_status`), the registry and triggers in `ANALYTICAL_TECHNIQUES.md`, `blocked != executed` (§4) |
| 3 | Evidence lineage — can every headline conclusion be traced executed method → source mart / table / slice → metric → period → grain → filter / baseline → evidence? | the lineage in §7 and `CLAIM_EVIDENCE_REGISTRY_TEMPLATE.md` |
| 4 | Alternative explanations — is a materially plausible alternative untested or not kept visible? | `COMPETING_EXPLANATIONS[]`, `DISCRIMINATING_EVIDENCE`, `FALSIFICATION_TEST` (§6) |
| 5 | Contradicting evidence — does evidence or method disagreement materially weaken the conclusion? | `CONTRADICTING_EVIDENCE`, `RESIDUAL_UNCERTAINTY`, the method-disagreement rule (§6) |
| 6 | Claim calibration — is any conclusion stronger than `FINAL_EVIDENCE_SUFFICIENCY` (driver → root cause, association → causation, single-period → systemic)? | claim ladder, `claim_support`, `causal_status`, `FINAL_EVIDENCE_SUFFICIENCY`, `claim strength <= final evidence sufficiency` (§7); `VARIANCE_DIAGNOSTIC_CONTRACT.md` for material Plan/Fact |
| 7 | Decision proportionality — does any recommendation, risk statement, or management implication exceed the verified evidence? | the material management synthesis rule (`ANALYTICS_WORKFLOW.md` Step 11) and its acceptance criteria |
The Judge introduces no competing definition for any concept it reads. It reuses `PRELIMINARY_EVIDENCE_CHECK`, the explanation-challenge record, `FINAL_EVIDENCE_SUFFICIENCY`, `CLAIM_EVIDENCE_REGISTRY_TEMPLATE.md`, Analysis QA, and the material variance diagnostic QA where applicable.
### Output
```text
ANALYTICAL_JUDGE
status: pass / revise / blocked
failed_checks:
material_findings:
required_action:
rerun_required: yes / no
manual_review_required: yes / no
maximum_claim_strength:
```
- **pass** — every material conclusion is supported at its stated claim strength; no material unresolved contradiction or missing analytical check remains.
- **revise** — the conclusion or its wording can be corrected from existing evidence, or a bounded additional deterministic check / rerun is available.
- **blocked** — a required prerequisite, reconciliation, grain, validation path, or discriminating evidence is unavailable; the final management conclusion must not be published.
`maximum_claim_strength` cannot exceed `FINAL_EVIDENCE_SUFFICIENCY.maximum_claim_strength`. `manual_review_required` is the value set by §1; the Judge surfaces it and does not redefine it.
### Bounded revise / rerun
Allowed:
```text
Judge finding
→ one explicit bounded correction or deterministic rerun
→ Judge re-check
```
Forbidden: silent self-retry; unrestricted iterative analysis; adding a method without registry / trigger support; reasoning around a missing deterministic prerequisite; treating a `blocked` method as evidence. Correction count, stop conditions, and rollback remain those of the canonical `docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md` and the `[Codex]` one-fix limit where applicable; this gate does not widen them.
### Runtime collapse
`routine` + low uncertainty + no material trigger: collapse the Judge to the existing compact QA note on the compact path (Runtime collapse, §9). Do not instantiate the seven-question `ANALYTICAL_JUDGE` record.
`material` / `decision_critical`: the explicit gate is mandatory. A recorded `ANALYTICAL_JUDGE` with `status: pass` — or a `revise` resolved by one bounded correction and a passing re-check — is required before final findings are handed to memo / report generation. A `blocked` status stops publication of the final management conclusion.
## 9. Runtime collapse
P0 is one workflow with conditional depth, not two independent workflows.
Eligible compact path:
```text
routine + low uncertainty + no material trigger
→ QUESTION
→ INTENT
→ CORE / TRIGGERED METHOD
→ DETERMINISTIC RESULT
→ COMPACT QA
→ ANSWER
```
Full path:
```text
TASK PROFILE
→ METHOD PLAN
→ ANALYSIS
→ PRELIMINARY EVIDENCE CHECK
→ EXPLANATION CHALLENGE
→ CLAIM CALIBRATION
→ FINAL EVIDENCE SUFFICIENCY
→ ANALYTICAL JUDGE (pass / revise / blocked) → FINAL FINDINGS
→ FULL QA
```
Without a material trigger, do not instantiate an unnecessary full Explanation Challenge, competing-explanations structure, falsification structure, expanded claim-registry state, full evidence-sufficiency record, or the seven-question `ANALYTICAL_JUDGE` record. `quick` retains the existing quick-mode artifact and context budget and does not become a full governance artifact by default.
## 10. Stop and escalation rules
Stop analytical deepening when:
- another method is unlikely to materially change finding, confidence, risk, recommendation, limitation, or evidence assurance;
- required discriminating evidence is unavailable;
- further precision exceeds data quality;
- the conclusion is robust to plausible uncertainty;
- the next unresolved question is strategic;
- added complexity provides no decision value.
Escalate through the existing routing and review path when:
- competing explanations remain materially plausible;
- material contradictory evidence remains unresolved;
- material method disagreement remains unresolved;
- the conclusion depends on an unsupported assumption;
- causal language is requested without causal evidence;
- required evidence lies outside Analytics ownership.
Preserve the decision boundary:
```text
[Analytics]: verified quantitative evidence
↓
[Thinking]: alternatives / trade-offs / risk appetite / decision
```
`thinking_handoff_possible = yes` identifies a possible boundary; it does not silently transfer ownership. `manual_review_required = yes` applies when the escalation materially affects the conclusion.
## 11. Metric semantics gate
A formula alone is not a sufficient metric definition. For material,
flagship, or ratio-like metrics, use
`../Templates/METRIC_DEFINITION_CARD_TEMPLATE.md` (`METRIC_DEFINITION_CARD`)
to fix numerator, denominator, aggregation semantics, population,
units/currency, sign/direction, zero-denominator behavior, allowed
comparison scope, and forbidden interpretations before a material
conclusion. `METRIC_DEFINITION_CARD.status: provisional / blocked`, or a
required field left undefined, still permits reporting the underlying
`DATA FACT` / `CALCULATION RESULT` with an explicit limitation attached; it
blocks a strong `INTERPRETATION` / `RECOMMENDATION` or flagship management
conclusion built on that metric. The interpretive layer is limited to
`HYPOTHESIS` / `LIMITATION` at most until the card reaches
`status: approved`. This gate does not add a metric to the 22-method
registry and does not redefine any business metric; it fixes the
definition-card mechanism only.
## 12. Canonical `VALUE_STATE` and claim strength
`DATA_CONTRACTS.md` owns the canonical `VALUE_STATE` vocabulary (`KNOWN`,
`UNKNOWN`, `NOT_REPORTED`, `NOT_APPLICABLE`, `PARSE_FAILED`,
`MISSING_SOURCE`, `UNMATCHED`, `BLOCKED`) and its invariants (`UNKNOWN != 0`,
`UNKNOWN != NOT_REPORTED`, `PARSE_FAILED != MISSING_SOURCE`,
`NOT_APPLICABLE != FALSE`). `RAW -> STAGE -> MART` must not collapse
materially different states into one generic null when that could change
denominator, population, reconciliation, classification coverage, metric
result, claim strength, or management conclusion.
```text
unresolved material uncertainty coverage -> claim_support <= PARTIALLY_SUPPORTED
```
A claim built on a mart where a material share of the relevant population
carries `UNKNOWN`, `PARSE_FAILED`, `MISSING_SOURCE`, or `UNMATCHED` cannot be
recorded as `SUPPORTED` with `confidence: high` unless the uncertainty
coverage is itself declared and quantified, and that quantification
demonstrably does not change the conclusion. Once resolved this way, the
uncertainty is no longer "unresolved" and the `<= PARTIALLY_SUPPORTED` cap
does not apply.
## 13. Mandatory Headline Claim Gate
For `analytical_depth = material / decision_critical`, every headline claim
requires a `CLAIM_EVIDENCE_REGISTRY_TEMPLATE.md` row with complete lineage:
```text
headline claim
-> claim registry row
-> method_execution_id
-> execution_status = executed
-> source mart/table/slice
-> metric/period/grain/filter/baseline
-> evidence_id
-> claim_support
-> causal_status
-> confidence
-> generalization_scope
-> qa_status
```
```text
lineage missing -> allowed_in_executive = no
```
This restates and enforces, at the headline-claim level, rules already
present in §4 (`blocked != executed`), §6 (claim ladder,
`driver != root cause`), and §7 (`claim strength <= final evidence
sufficiency`); it adds no new taxonomy. `manual_review_required` (§1) and the
Analytical Judge (§8, check 3 and 6) read this gate; they do not duplicate
it.
## 14. Three control gates
`[Analytics]` separates three gates. They are already implemented by
existing mechanics; this section names them so they are not conflated.
```text
GATE 1 - DATA / CALCULATION
Are the data, formulas, units, grain, and reconciliation correct?
Owned by: Data Contract, stage/mart QA, Contract QA, Calculation QA.
GATE 2 - ANALYTICAL CLAIM
What does the executed evidence permit asserting?
Owned by: METHOD_PLAN, PRELIMINARY_EVIDENCE_CHECK, claim ladder,
FINAL_EVIDENCE_SUFFICIENCY, CLAIM_EVIDENCE_REGISTRY, Analytical Judge (§8).
GATE 3 - NARRATIVE
Is the memo/executive wording no stronger than the verified claim?
Owned by: MEMO_PIPELINE.md, MEMO_RUBRIC.md, and the canonical [LLM] memo
Judge/QA gate.
```
Invariant:
```text
DATA VALID != CLAIM SUPPORTED != NARRATIVE ACCEPTABLE
```
Passing Gate 1 does not authorize a claim; passing Gate 2 does not authorize
narrative wording stronger than `maximum_claim_strength`. The Analytical
Judge remains the post-findings Gate 2 checkpoint; Memo QA / the `[LLM]`
Judge remains the Gate 3 checkpoint. Neither gate is redefined or
duplicated by this section.
## 15. P1 activated controls (bounded pilot, issue #445)
Status: bounded pilot activation only. `owner review required` before any
promotion decision; this section does not authorize production adoption,
merge, deployment, or Project-sync of the pilot. These three controls extend
the existing P0 mechanics named below; they do not fork, replace, or
duplicate them, add a new `METHOD_ID`, add a new analytical intent, or change
the 22-method registry in `ANALYTICAL_TECHNIQUES.md`.
### 15.1 `POPULATION_CONTRACT` (CONTROL/CONTRACT)
Activated extension of §5's `population_constant_or_explained?` /
`denominator_constant_or_explained?` / `scope_change_quantified?` and of
`../Templates/METRIC_DEFINITION_CARD_TEMPLATE.md`'s `population` field, for
ratio/rate/share/average/margin/conversion/productivity/frequency and
analogous denominator-sensitive metrics. It does not replace either.
```text
POPULATION_CONTRACT
population_definition:
numerator_population:
denominator_population:
period:
grain:
filters:
exclusions:
population_changed_vs_baseline:
denominator_changed_vs_baseline:
scope_change_amount:
scope_change_pct:
comparability_status: comparable / comparable_with_adjustment / not_comparable / unresolved
interpretation_allowed: yes / limited / no
limitation:
```
Required behavior: the reported metric may remain visible when
`comparability_status = unresolved`, but a strong comparative interpretation
(`interpretation_allowed = yes`) must not be published when a material
population/denominator/scope change is unresolved or unquantified. This is
the same §5 cap restated with explicit fields:
```text
comparability_status: unresolved or not_comparable
  and scope_change_quantified? = no
  -> interpretation_allowed != yes
  -> claim_support <= PARTIALLY_SUPPORTED
```
Activation trigger: instantiate for `analytical_depth = material /
decision_critical` cases involving a ratio/rate/share/average/margin/
conversion/productivity/frequency metric with a comparison across periods or
segments. Routine/quick cases with no material population/denominator
trigger keep the existing §5 one-line check and do not instantiate the full
contract (§9 runtime collapse still applies).
### 15.2 `RECONCILIATION_CONTRACT` (CONTROL/CONTRACT)
Activated wrapper over existing, unchanged methods and QA
(`reconciliation`, `unmatched_elements_analysis`, `factor_reconciliation`,
`unexplained_residual`, classification-coverage QA, `data_layer_check`).
No second `reconciliation` method and no new `METHOD_ID` are created; the
contract only makes explicit which integrity dimension each existing result
covers, so a pass on one dimension is not read as proof of another.
```text
RECONCILIATION_CONTRACT
scope:
period:
grain:
tolerance:
amount_reconciliation:
row_count_reconciliation:
matched_population:
only_in_left:
only_in_right:
identity_mapping_status:
classification_coverage:
unexplained_residual:
overall_interpretation:
limitations:
```
Required invariant:
```text
amount_reconciliation != row_count_reconciliation != matched_population
  != identity_mapping_status != classification_coverage != factor_reconciliation
```
`overall_interpretation` may only claim the integrity dimensions that were
actually tested; a pass on `amount_reconciliation` alone does not authorize
"fully reconciled" language covering `matched_population`,
`identity_mapping_status`, or `classification_coverage` when those were not
separately tested or were tested and failed.
Activation trigger: instantiate for material/decision-critical cases where a
reconciliation-based claim (e.g. "dataset reconciles", "fully matched") would
be published; routine/quick cases keep the existing single-line
reconciliation QA result (§9 runtime collapse still applies).
### 15.3 `ANALYSIS_CONTINUATION_GATE` (ROUTING / WORKFLOW CONTROL)
Activated, explicit restatement of §10's stop/escalation rules as a
recorded decision for material/decision-critical cases. It is not an
autonomous loop: it cannot silently add methods, cannot silently retry,
cannot reason around a missing deterministic prerequisite, must preserve the
Analytical Judge (§8) and §10 as authoritative, and must collapse to the
existing compact path for routine/quick cases without a material trigger
(§9 runtime collapse still applies).
```text
ANALYSIS_CONTINUATION_GATE
current_question_answered:
current_claim_strength:
remaining_uncertainty:
material_unresolved_question:
next_method_candidate:
what_can_it_change:
required_evidence_available:
expected_decision_value:
decision: CONTINUE / STOP / BLOCK / HANDOFF
reason:
```
Decision semantics:
- `CONTINUE` only when `next_method_candidate` is an already-registered
  method (§3 registry) that can materially change finding, claim strength,
  confidence, risk, recommendation, limitation, or evidence assurance
  (`what_can_it_change` non-empty and material).
- `STOP` when no eligible next method can materially change the
  decision-relevant result (restates §10's stop rules).
- `BLOCK` when `required_evidence_available = no` for the discriminating
  check (restates `blocked != executed`, §4).
- `HANDOFF` only when the remaining unresolved question leaves Analytics
  ownership (restates §10's escalation/decision-boundary rules); it does not
  silently transfer ownership.
Activation trigger: instantiate for material/decision-critical cases at a
point where continuation is genuinely in question (after a dominant finding,
before a final claim, or when multiple methods are technically eligible).
Do not instantiate for routine/quick cases with no material trigger.
## P1 pilot status (issue #445)
`POPULATION_CONTRACT`, `RECONCILIATION_CONTRACT`, and
`ANALYSIS_CONTINUATION_GATE` are activated for a bounded pilot only, per
issue #445. Pilot evidence, the 10-scenario baseline-vs-candidate matrix, and
per-element recommendations are recorded in
`../Knowledge/P1_PILOT_EVIDENCE_2026-09-06.md`. `owner review required`
before any promotion decision; passing the pilot does not itself authorize
production adoption. `HELD_OUT_TRANSFER_EVAL` (QA/EVAL, not a method) is
defined in `QA_CHECKLIST.md` and exercised via `SMOKE_QA_FOR_ANALYTICS.md`.
Rollback: `POPULATION_CONTRACT` rolls back to the bare §5 population checks;
`RECONCILIATION_CONTRACT` rolls back to the existing separate
reconciliation/unmatched/factor-reconciliation/residual/coverage controls
without the wrapper; `ANALYSIS_CONTINUATION_GATE` rolls back to §10's
minimum-sufficient-method/stop/escalation rules alone. No method-registry
migration is required for rollback in any case.
P2 remains deferred. Do not implement expanded taxonomies, reusable pattern
promotion, autonomous learning, automatic promotion or downgrade, or agentic
analytical orchestration.

## From: `ChatGPT/[Analytics]/Knowledge/VARIANCE_DIAGNOSTIC_CONTRACT.md`

# Variance Diagnostic Contract
## Purpose and ownership
This file is the canonical `[Analytics]` runtime/output contract for material Plan/Fact and variance diagnostics. It is a thin extension of `ANALYTICAL_REASONING_STANDARD.md` and reuses the 22 methods owned by `ANALYTICAL_TECHNIQUES.md`; it creates no method, registry, framework, or independent workflow.
Apply the full contract only when `analytical_depth = material / decision_critical` or variance risk makes reconciliation, classification, or evidence controls material. Routine/quick cases collapse to the verified reported result, explicit direction rule, compact reconciliation/QA, and answer.
```text
reported result
→ normalized management variance
→ gross bridge
→ reconciled primary attribution
→ classification coverage
→ materiality
→ secondary management attributes
→ claim calibration
→ management synthesis
```
Deterministic calculations and classifications precede LLM narrative. The Writer receives verified, partial, hypothesis, or unknown fields; it does not calculate or infer them.
## 1. Variance sign convention
```text
VARIANCE_SIGN_CONVENTION
source_value:
source_formula:
source_sign_convention:
raw_variance:
raw_variance_formula:
economic_direction:
  higher_is: favorable / adverse / context_dependent
normalized_management_variance:
  amount:
  convention: positive = adverse; negative = favorable
  status: resolved / unresolved
```
```text
raw mathematical variance != management direction
```
- Expense: `Actual > Plan` is adverse when higher expense is adverse.
- Revenue: `Actual < Plan` is adverse when higher revenue is favorable.
- Preserve the native source/raw sign and formula for traceability.
- Use only normalized management direction inside a management bridge or attribution reconciliation.
- Never mix raw and normalized signs inside one bridge.
- `context_dependent` requires an explicit business rule. Without it, normalization status is `unresolved` and no normalized classification is published.
- Do not impose one universal `actual - plan` management formula across metrics.
## 2. Diagnostic runtime
```text
VARIANCE_DIAGNOSTIC
reported_result:
  plan:
  actual:
  source_variance:
  source_sign_convention:
normalized_result:
  normalized_management_variance:
  economic_direction_rule:
  normalization_status:
gross_bridge:
  gross_adverse:
  gross_favorable:
  net_management_variance:
  reconciliation_residual:
  reconciliation_status:
primary_attribution:
  economic_variance:
  timing_or_cutoff:
  data_or_mapping_effect:
  unresolved:
  reconciliation_residual:
  reconciliation_status:
```
The reported result remains canonical. The normalized result is a management-direction view, not a replacement for the source result.
### Gross bridge
For a material case disclose gross adverse movement, gross favorable movement, and normalized net management variance.
```text
gross adverse + gross favorable = normalized net management variance
```
Both use the normalized sign convention: adverse is positive and favorable is negative. If a material adverse driver exceeds the net adverse variance, the compensating favorable movement must be explicit.
Reuse `contribution_analysis`, `bridge_analysis`, `factor_reconciliation`, and `unexplained_residual` as applicable. Do not add a method.
### Primary attribution reconciliation
Primary attribution categories are mutually exclusive within one row/effect, collectively exhaustive within the declared scope, and deterministically reconciled.
```text
NET_ATTRIBUTION_RECONCILIATION
normalized_management_variance:
economic_effect:
timing_effect:
data_mapping_effect:
unresolved_effect:
reconciliation_residual:
status: pass / fail
```
```text
economic_effect
+ timing_effect
+ data_mapping_effect
+ unresolved_effect
= normalized_management_variance
```
If the residual is outside the declared deterministic tolerance, `status = fail`. The management narrative must then keep the residual visible and must not present attribution as complete.
## 3. Classification coverage
Net reconciliation and classification coverage answer different questions and must remain separate.
```text
ABSOLUTE_CLASSIFICATION_COVERAGE
population_basis: all_rows / material_rows / selected_rows
eligible_gross_movement:
classified_gross_movement:
unclassified_gross_movement:
coverage_pct:
row_count_total:
row_count_classified:
row_count_unknown:
classification_dimensions:
categories_mutually_exclusive: yes / no / not_applicable
```
Default deterministic definition:
```text
coverage_pct
= classified gross absolute movement
/ eligible gross absolute movement
```
Any alternative definition requires an explicit numerator, denominator, and population. A classification aggregate without declared population and coverage is not a complete explanation. Never use small net variance as the denominator for gross classification coverage.
## 4. Materiality and selection
Declare materiality before narrative generation; do not hardcode universal thresholds.
```text
MATERIALITY_CONTRACT
absolute_threshold:
relative_threshold:
zero_plan_rule:
top_contribution_rule:
  contribution_basis: gross_adverse / gross_favorable / gross_absolute
  threshold:
qualitative_override:
selected_population:
excluded_population:
selection_coverage:
```
An item may be material when it passes a declared absolute threshold; passes a declared relative threshold with a meaningful denominator; has actual activity with zero plan under the declared rule; belongs to contributors covering a declared share of gross movement; or satisfies a declared qualitative control/compliance/risk trigger. Every run identifies the basis, denominator, population, and exclusions.
## 5. Secondary management attributes
Secondary attributes describe different analytical dimensions and remain outside the additive bridge.
```text
budget_status: planned / underplanned / unbudgeted / unknown
controllability: controllable / partially_controllable / non_controllable / unknown
recurrence: recurring / one_off / unknown
evidence_status: supported / partial / hypothesis / unknown
```
A row may simultaneously be `economic_variance + unbudgeted + controllable + one_off`; only the primary effect participates in additive attribution. Secondary attributes must never be summed as independent causes of normalized variance.
### Controllability
```text
CONTROLLABILITY_CLASSIFICATION
classification: controllable / partially_controllable / non_controllable / unknown
approved_rule_or_business_definition:
evidence_source:
classification_basis:
review_status:
```
Insufficient business/evidence basis means `controllability = unknown`. Amount, zero-plan status, budget ownership, management ownership, and driver status do not establish controllability. Valid evidence may include approved policy, contract terms, tax/regulatory nature, process rules, delegation/authority rules, or another traceable approved business definition.
### Recurrence and generalization
```text
RECURRENCE_CLASSIFICATION
classification: recurring / one_off / unknown
recurrence_basis: historical_pattern / contractual_schedule / confirmed_event_specific / process_rule / other_verified_basis
evidence_source:
```
One observation alone establishes neither `recurring` nor `one_off` unless independent event-specific evidence supports it. Otherwise use `unknown`.
```text
single-period evidence != systemic / non-systemic evidence
```
Claims such as `systemic`, `non-systemic`, `structural`, `persistent`, `recurring`, `isolated`, or `one-off` require explicit generalization evidence such as comparable multi-period history, process/control evidence, contractual recurrence, or confirmed event-specific evidence. One period may support only period-bounded concentration language.
### Accountability boundary
```text
driver/effect != controllability != accountability
management_owner != responsible_for_cause
```
Do not infer responsibility, mismanagement, budget violation, or control failure solely from amount, ownership, zero-plan status, or driver status. Accountability claims require separate criteria and evidence.
## 6. Reported and adjusted views
```text
REPORTED_VIEW
official_plan:
official_actual:
official_variance:
source_sign_convention:
normalized_management_variance:
```
```text
ADJUSTED_MANAGEMENT_VIEW
adjustment_id:
adjustment_amount:
adjustment_direction: increases_adverse / reduces_adverse
adjustment_type:
reason:
evidence:
expected_reversal_or_normalization:
approved_rule:
included_in_adjusted_view:
```
```text
reported_management_variance
+ adverse_increasing_adjustments
- adverse_reducing_adjustments
= adjusted_management_variance
```
The adjusted view is supplementary and never replaces the reported result. No silent exclusion or ambiguous unsigned adjustment polarity is allowed.
## 7. CFO / management synthesis
For material Plan/Fact analysis, compress the verified diagnostic in this semantic order:
1. reported result;
2. normalized management effect;
3. primary driver/effect at supported claim strength;
4. gross favorable/adverse offset and net bridge;
5. economic, timing, data/mapping, and unresolved attribution;
6. budget quality;
7. controllability;
8. classification coverage and unknown population;
9. what is supported;
10. what is not established;
11. action or next discriminating evidence.
This is a semantic contract, not a mandatory verbose template. Show the smallest sufficient management synthesis and keep the supporting diagnostic in the evidence layer. Routine cases must not instantiate the full structure.
Management synthesis cannot create analytical evidence. A driver remains below root-cause level unless causal evidence permits escalation. Controllability, recurrence, systemic status, and accountability remain `unknown` or `not established` when their evidence contracts are unmet.
## 8. Claim, method, QA, and stop gates
Claims trace through the existing `CLAIM_EVIDENCE_REGISTRY_TEMPLATE.md`. Use its generalization fields when language extends beyond the observed period/scope.
```text
claim strength <= final evidence sufficiency
driver != root cause
reported result != adjusted management view
net attribution reconciliation != absolute classification coverage
```
Stop or constrain publication when sign normalization is unresolved; the gross or attribution bridge fails; coverage population/denominator is missing; materiality basis is absent; adjusted polarity is ambiguous; or a secondary/generalized claim lacks required evidence.

## From: `ChatGPT/[Analytics]/Knowledge/CHART_SELECTION_STANDARD.md`

# Chart Selection Standard
## Purpose
Подбирать графики только после определения метрики, grain, периода, аудитории и source mart.
## Source rule
Каждый график должен иметь:
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
| Analytical need | Recommended chart |
|---|---|
| Plan vs fact by period | Line chart or grouped bar |
| Top deviations | Bar chart sorted by ABS Delta |
| Structure / composition | Stacked bar or 100% stacked bar |
| Movement explanation | Bridge / waterfall |
| Trend over time | Line chart |
| Distribution / outliers | Box plot or histogram |
| Segment comparison | Bar chart / small multiples |
| Risk matrix | Heatmap or matrix |
| Flow | Sankey only if flow data is reliable |
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

## From: `ChatGPT/[Analytics]/Knowledge/ANALYTICS_03_TECHNIQUES_AND_CHARTS_BUNDLE_SEMANTICS.md`

# Migrated Bundle Semantics
Canonical source created during Issue #285 provenance migration.
Legacy bundle provenance: `ChatGPT/[Analytics]/Knowledge_Bundles/ANALYTICS_03_TECHNIQUES_AND_CHARTS.md`.
## Legacy section: `ChatGPT/[Analytics]/Knowledge/ANALYTICAL_TECHNIQUES.md`
Registry is the source of truth for eligibility; registration is not execution. Each method records `METHOD_ID`, name, purpose, role, requirements, input grain, required metrics, output, execution owner/mode, validation owner, limitation, and failure mode. Mixed execution also records deterministic and reasoning components.
For P0, `NAME` is the stable registry label represented by `METHOD_ID`; display formatting cannot change identity.
`P0 METHOD COUNT = 22`. Capability groups (`DECOMPOSE`, `LOCATE`, `VALIDATE`, `CHALLENGE`, `FORWARD`) are readability aids only, not runtime taxonomy or routing.
Material Plan/Fact uses `VARIANCE_DIAGNOSTIC_CONTRACT.md` to configure existing methods. `variance_analysis` preserves raw/source formula and normalizes management direction from an explicit KPI rule; contribution exposes gross movement and coverage; bridge/factor reconciliation use one normalized sign; residual keeps incomplete attribution visible. Controllability, recurrence, budget status, materiality, coverage, and accountability are controls/attributes, not methods.
| METHOD_ID | Role / mode | Purpose and required boundary |
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
- “Почему отклонение?” → `diagnose_variance`; add `explain_drivers` only for an explanatory question with prerequisites.
`driver_decomposition` produces driver candidates, not root cause.
## Legacy section: `ChatGPT/[Analytics]/Knowledge/ANALYTICAL_REASONING_STANDARD.md`
## Boundary and flow
This is a bounded reasoning-control extension; it does not replace Data Contract, RAW, STAGE, MART, deterministic calculations, chart sourcing, memo, QA/Judge, acceptance, or handoff. `mart_main_full` remains evidence/reuse; compact marts remain management-facing.
Execution remains governed by repo-root `docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md`; `docs/autonomous_execution/extensions/ANALYTICS_EXTENSION.md` remains authoritative for Analytics-specific AES requirements. Reasoning control structures method selection only; it does not fork AES states, correction limits, stop/rollback/acceptance, or external authority. It is not an autonomous agent or an independent retry/self-improvement loop. Closure Review uses existing Data/Analysis/Output Judge, reconciliation, unsupported-conclusion, and artifact-freshness controls; the Analytics extension remains authoritative for domain detail.
LLM reasoning != deterministic execution
TASK PROFILE → INTENT → deterministic-first minimum methods → prerequisite gate
→ existing execution → preliminary evidence → explanation challenge when material
→ claim calibration → final evidence sufficiency → existing QA/Judge
LLM may classify ambiguous intent and bounded judgment/hybrid triggers, challenge explanations, and calibrate wording. It cannot replace deterministic arithmetic, formulas, reconciliation, variance/driver/exposure calculations, classification, or a deterministically executable forecast. Missing prerequisites cannot be reasoned away.
## Task profile
question; decision_user
evidence_state_basis
expected_output
No numerical scoring. Analytical depth and output mode are independent. Routine → minimal; material → standard; decision-critical → enhanced plus robustness consideration and explicit evidence sufficiency.
Set `robustness_required = yes` only when a declared baseline, subgroup, or sensitivity trigger is satisfied. Set `thinking_handoff_possible = yes` only when the unresolved question crosses into alternatives, trade-offs, risk appetite, or decision.
Set `manual_review_required = yes` for causal/root-cause final language, unresolved material contradictory evidence, decision-critical weak/partial evidence, material judgment/hybrid influence, or required `[Thinking]` escalation. Record review owner/status/resolution before publication.
P0 active intents: `validate_data`, `diagnose_variance`, `explain_drivers`, `test_explanation`, `project_forward`. Deferred candidates: `locate_concentration`, `detect_anomalies`, `analyze_structure`, `analyze_trend`, `prepare_decision_evidence`, `evaluate_control`.
Canonical P0 registry contains exactly 22 methods, including `exception_analysis`, `unmatched_elements_analysis`, `factor_reconciliation`, `timing_validation`, `data_layer_check`, and `leading_indicator_analysis`. Controls remain controls; numerator/denominator/population, contradiction/discrimination/falsification, claim ladder, and stop conditions do not become methods. Trade-offs, premortem, reversibility, risk appetite, choice, and decision remain in `[Thinking]`. Expansion beyond 22 requires P1/pilot evidence or separate acceptance.
## Method plan and prerequisites
method; intent; status: CORE / TRIGGERED / OPTIONAL
why_selected; question_answered
trigger; trigger_type; trigger_rule; trigger_evidence_required; trigger_evidence; priority
execution_owner; execution_mode
missing_requirement; method_execution_id
`yes` means all requirements satisfied; `no` means a real requirement is unmet; `not_applicable` means no such requirement exists and cannot bypass one. `blocked != executed`; blocked is not evidence. Each period/grain/filter/baseline/population/scenario application needs a distinct `method_execution_id`. Explain exclusion only for materially plausible methods.
## Baseline and ratio controls
Record baseline type/period/rationale and whether an alternative is material. For material/decision-critical cases, a reasonable alternative capable of changing the conclusion requires `robustness_to_baseline`. Ratios require numerator + denominator + population; explain population/denominator and quantify additions, removals, filters, entities, cut-offs, and definition changes.
## Material Plan/Fact controls
`VARIANCE_DIAGNOSTIC_CONTRACT.md` owns source-sign preservation, management-direction normalization, gross bridge, primary attribution, gross coverage, declared materiality, evidence-constrained secondary attributes, reported/adjusted separation, and CFO synthesis order. It adds no intent, method, registry, or workflow; full diagnostics activate only for material/decision-critical cases or material variance risk.
primary attribution is additive; secondary attributes are not
## Explanation challenge
Preliminary check records finding support (`yes / partial / no`), explanatory feasibility, critical gap, and next step (`continue / stop / collect evidence`). If infeasible: stop, state limitation, do not fabricate.
Material/decision-critical cases record current and competing explanations, contradicting and discriminating evidence, falsification test/result, and residual uncertainty. Ask what else explains the finding, what contradicts it, what test changes it, and what evidence distinguishes explanations.
OBSERVATION → CALCULATED EFFECT → DRIVER CANDIDATE → SUPPORTED EXPLANATION → ROOT CAUSE
Material method disagreement remains contradictory evidence; preserve conflict, do not silently reconcile or average incompatible conclusions, constrain claim strength, and escalate if unresolved/material.
## Claim calibration
Preserve `confidence: high / medium / low`. Add independent `claim_support: SUPPORTED / PARTIALLY_SUPPORTED / HYPOTHESIS / UNSUPPORTED` and `causal_status: not_applicable / association_only / explanation_supported / causal_evidence`.
For material/decision-critical claims, `FINAL_EVIDENCE_SUFFICIENCY` states what is sufficient for observation, calculated effect, driver candidate, supported explanation, and causal claim; status; missing discriminating evidence; remaining contradictions; maximum claim strength. LLM confidence, expectations, intuition, method count, and fluency cannot strengthen evidence.
Lineage: claim → `method_execution_id` → executed method → source mart/table/slice → metric/period/grain/filter/baseline → evidence. Blocked/planned/not-needed executions cannot support claims requiring results.
## Runtime, stop, escalation
Routine + low uncertainty + no material trigger uses question → intent → core/triggered method → deterministic result → compact QA → answer. Do not instantiate full challenge, competing explanations, falsification, expanded registry, or evidence-sufficiency records without a trigger; preserve quick-mode budget.
Stop when added methods cannot materially change the outcome, discriminating evidence is unavailable, precision exceeds data quality, conclusion is robust, the remaining question is strategic, or complexity adds no decision value. Escalate for materially plausible competing explanations, unresolved contradictory/method conflict, unsupported assumptions, causal language without causal evidence, or evidence outside Analytics ownership. `[Analytics]` owns verified evidence; `[Thinking]` owns alternatives/trade-offs/risk appetite/decision.
P1 pilot calibration and P2 expanded/autonomous taxonomies remain deferred; do not claim them implemented.
## Legacy section: `ChatGPT/[Analytics]/Knowledge/VARIANCE_DIAGNOSTIC_CONTRACT.md`
## Boundary and activation
Canonical material Plan/Fact runtime/output contract; thin extension of the existing reasoning standard and 22-method registry. Full structure activates only for material/decision-critical cases or material variance risk; routine/quick cases collapse to verified result, direction rule, compact reconciliation/QA, and answer. Deterministic calculation/classification precedes LLM narrative.
## Sign and reported result
Record source value/formula/sign, raw variance, explicit `higher_is: favorable / adverse / context_dependent`, and normalized management variance where positive is adverse and negative favorable. Raw math is not management direction. Preserve native source sign; use one normalized sign inside management bridges. Context-dependent KPI without an approved business rule remains unresolved. Reported result stays canonical.
## Gross bridge and primary attribution
Material cases show gross adverse, gross favorable, normalized net, residual, and status. A driver above net requires explicit favorable offset. Reuse contribution, bridge, factor reconciliation, and residual methods.
Primary `economic + timing + data/mapping + unresolved` effects are non-overlapping within a row, exhaustive within scope, and reconcile to normalized net variance. Failed residual remains visible and blocks a complete-explanation narrative.
## Coverage and materiality
Net attribution reconciliation is separate from absolute classification coverage. Coverage declares population, eligible/classified/unclassified gross absolute movement, row counts, dimensions, and exclusivity. Default denominator is eligible gross absolute movement, never small net variance.
Materiality declares absolute/relative thresholds, meaningful denominator, zero-plan rule, gross contribution basis/threshold, qualitative override, selected/excluded population, and selection coverage. No universal threshold.
## Secondary attributes and evidence
Budget status, controllability, recurrence, and evidence status are non-additive attributes. Amount, zero-plan/driver/owner status does not prove controllability or accountability. Insufficient approved business evidence means controllability `unknown`. One observation does not prove recurring/one-off; single-period evidence does not prove systemic/non-systemic. Generalization requires traceable multi-period, process/control, contractual, or event-specific evidence.
## Adjusted view and synthesis
Adjusted management view is supplementary: explicit adjustment ID, amount, `increases_adverse / reduces_adverse` polarity, type, reason, evidence, normalization/reversal, approved rule, and inclusion. It reconciles from reported management variance and never replaces reported Plan/Fact.
CFO synthesis order: reported result; normalized effect; supported driver; gross offset/bridge; primary nature; budget quality; controllability; coverage/unknown; supported; not established; action/next evidence. This is semantic order, not a verbose mandatory template. Claim strength stays within evidence; driver stays below root cause.
