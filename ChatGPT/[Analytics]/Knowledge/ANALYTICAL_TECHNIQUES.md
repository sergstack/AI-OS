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
| `validate_data` | `reconciliation` | `anomaly_analysis`, `exception_analysis`, `unmatched_elements_analysis`, `data_layer_check`, `timing_validation`, `segmentation`, `subgroup_robustness` | — |
| `diagnose_variance` | `variance_analysis`, `contribution_analysis`, `unexplained_residual` | `bridge_analysis`, `mix_analysis`, `segmentation`, `trend_analysis`, `unmatched_elements_analysis`, `factor_reconciliation`, `timing_validation`, `data_layer_check` | `robustness_to_baseline` |
| `explain_drivers` | `driver_decomposition`, `unexplained_residual` | `alternative_explanation_test`, `segmentation`, `trend_analysis`, `factor_reconciliation`, `timing_validation`, `data_layer_check`, `unmatched_elements_analysis` | `robustness_to_baseline`, `sensitivity_analysis` |
| `test_explanation` | `alternative_explanation_test` | `robustness_to_baseline`, `subgroup_robustness`, `sensitivity_analysis`, `timing_validation`, `data_layer_check` | `cohort_analysis` |
| `project_forward` | `forecast_to_period_end` | `sensitivity_analysis`, `leading_indicator_analysis` | `trend_analysis`, `robustness_to_baseline` |

## Trigger contracts for non-CORE methods

| Intent / method | trigger_type | trigger_rule | trigger_evidence_required |
|---|---|---|---|
| `validate_data` / `anomaly_analysis` | deterministic | A declared validation rule or threshold is breached in verified inputs. | Rule/threshold, tested field, and breach result. |
| `validate_data` / `exception_analysis` | hybrid | An approved rule/control condition exists and testing violations is material to data/process validity. | Explicit rule, population, required fields, scope/filter, and evidence of rule applicability. |
| `validate_data` / `unmatched_elements_analysis` | deterministic | Two populations are expected to align and entity-level mismatch may explain the issue. | Comparable populations, approved matching key/rule, scope, and duplicate treatment. |
| `validate_data` / `data_layer_check` | hybrid | A verified result may plausibly originate from mapping/transformation rather than source economics. | Traceable lineage, comparable grain/bridge, transformation definitions, and observed layer discrepancy candidate. |
| `validate_data` / `timing_validation` | hybrid | Period cut-off or timing shift could materially affect validity or interpretation. | Relevant dates, period boundary, entity grain, approved timing definition, and timing candidate evidence. |
| `validate_data` / `segmentation` | hybrid | Mismatch/anomaly candidates span a declared segment dimension and segment comparison could localize a material integrity issue. | Candidate records, valid segment field, and segment counts/coverage. |
| `validate_data` / `subgroup_robustness` | hybrid | A validation conclusion may differ across a materially relevant subgroup. | Overall result plus sufficient subgroup observations. |
| `diagnose_variance` / `bridge_analysis` | deterministic | Start-to-end delta has additive, non-overlapping components that must reconcile. | Start/end totals and component mapping. |
| `diagnose_variance` / `mix_analysis` | hybrid | Verified population/category weights changed and the change could materially affect the total variance. | Period weights, category definitions, and target metric. |
| `diagnose_variance` / `segmentation` | hybrid | Aggregate variance contains materially heterogeneous eligible groups. | Aggregate result and comparable segment-level inputs. |
| `diagnose_variance` / `trend_analysis` | deterministic | Three or more comparable ordered periods are available and timing can change interpretation. | Comparable time series and cut-off metadata. |
| `diagnose_variance` / `unmatched_elements_analysis` | deterministic | Population additions/removals may materially explain the variance. | Comparable period populations, matching rule, duplicate treatment, and variance scope. |
| `diagnose_variance` / `factor_reconciliation` | deterministic | A multi-factor/driver decomposition has executed and mathematical reconciliation is applicable. | Observed total delta, executed factor effects, and consistent scope/period/baseline. |
| `diagnose_variance` / `timing_validation` | hybrid | Cut-off, posting, recognition, or cross-period movement may materially explain variance. | Relevant dates, boundary, approved timing definition, and variance candidate. |
| `diagnose_variance` / `data_layer_check` | hybrid | Observed variance may first arise from mapping/transformation/classification. | Layer lineage, comparable grain/bridge, transformation definitions, and variance by layer. |
| `diagnose_variance` / `robustness_to_baseline` | judgment | A reasonable alternative baseline could materially change a material/decision-critical conclusion. | Current baseline, alternative baseline rationale, and comparable inputs. |
| `explain_drivers` / `alternative_explanation_test` | judgment | At least one materially plausible competing explanation has observable distinguishing evidence. | Leading/competing explanations and proposed discriminating evidence. |
| `explain_drivers` / `segmentation` | hybrid | Quantified driver candidates may differ across a materially relevant segment. | Driver result plus comparable segment inputs. |
| `explain_drivers` / `trend_analysis` | deterministic | Comparable time observations exist and sequence/timing can distinguish explanations. | Ordered time series and event/cut-off metadata. |
| `explain_drivers` / `robustness_to_baseline` | judgment | A reasonable baseline alternative could change driver ranking or claim strength. | Baseline alternatives and comparable driver inputs. |
| `explain_drivers` / `sensitivity_analysis` | hybrid | A quantified driver claim depends materially on an explicit uncertain assumption. | Deterministic model, assumption, plausible range, and target output. |
| `explain_drivers` / `factor_reconciliation` | deterministic | Executed factor/driver effects require a completeness check against the observed total delta. | Observed delta, executed effects, and consistent scope/period/baseline. |
| `explain_drivers` / `timing_validation` | hybrid | A candidate driver may reflect timing/cut-off rather than economic change. | Driver result, relevant dates/boundary, approved timing definition, and candidate timing evidence. |
| `explain_drivers` / `data_layer_check` | hybrid | A candidate driver may originate from transformation/mapping rather than source data. | Driver result, traceable layers, comparable grain/bridge, and relevant transformation definitions. |
| `explain_drivers` / `unmatched_elements_analysis` | deterministic | Changed population composition may materially explain a driver. | Comparable populations, approved match rule, duplicate treatment, and driver scope. |
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
