# Analytics QA Checklist

## Data QA

- [ ] Required files exist.
- [ ] Required columns exist.
- [ ] Data types valid.
- [ ] Dates parsed correctly.
- [ ] Currency / units normalized.
- [ ] Null policy applied.
- [ ] Duplicate policy applied.
- [ ] Freshness checked.
- [ ] Mapping tables checked.
- [ ] Unmatched rows listed.
- [ ] `VALUE_STATE` distinctions (`KNOWN`/`UNKNOWN`/`NOT_REPORTED`/
  `NOT_APPLICABLE`/`PARSE_FAILED`/`MISSING_SOURCE`/`UNMATCHED`/`BLOCKED`) are
  not collapsed into a generic null where material.

## Main files QA

- [ ] `stage_main_full` exists or is designed.
- [ ] `stage_main_full` has no business metrics.
- [ ] `stage_main_full` has no analytical classifiers.
- [ ] `stage_main_full` is portable to DB / BI / Excel.
- [ ] `mart_main_full` exists or is designed.
- [ ] `mart_main_full` contains metrics and formulas.
- [ ] Material/flagship/ratio-like metrics have a `METRIC_DEFINITION_CARD`
  with `status: approved`, or the conclusion is limited/blocked.
- [ ] `mart_main_tz` or `mart_main_compact` exists or is designed.
- [ ] Mart slices are derived from `mart_main_full`.

## Calculation QA

- [ ] RAW totals reconciled.
- [ ] STAGE totals reconciled.
- [ ] MART totals reconciled.
- [ ] Metric formulas documented.
- [ ] Edge cases tested or listed.
- [ ] Outliers reviewed.
- [ ] Thresholds explicit.
- [ ] Grain explicit.
- [ ] Period explicit.

## Quantitative sanity gate

For a published quantitative report with a `flagship_metric`, apply
`QUANTITATIVE_SANITY_GATE.md` before publication:

- [ ] Gate applicability is stated; unpublished scratch/exploratory work is
  not treated as a published result.
- [ ] Every flagship metric has a complete read-back-verifiable source locator
  and an independent source-level locator.
- [ ] Representation, plausibility, method applicability, population state,
  censoring, independent recalculation, tolerance, evidence, and resolution
  are recorded.
- [ ] Duration/time-to-event metrics have storage semantics and censoring
  checked when applicable.
- [ ] `quantitative_sanity_gate_status` is `pass`, or publication is stopped
  with `revise` / `blocked` and the required remediation.

This is an extension of existing Analysis QA, not a second QA framework. Keep
the record internal or in evidence/appendix so `quick` output remains compact.

## Analysis QA

- [ ] Method stated.
- [ ] Source mart stated.
- [ ] Top deviations ranked by materiality / ABS Delta.
- [ ] Driver logic documented.
- [ ] Timing status not overstated.
- [ ] Confirmed cause separated from hypothesis.
- [ ] Confidence rationale stated.
- [ ] `method_selection_adequate?`
- [ ] `material_method_omitted?`
- [ ] `unnecessary_method_bloat?`
- [ ] `registry_mapping_followed?`
- [ ] `deterministic_trigger_applied?`
- [ ] `trigger_contract_defined?`
- [ ] `trigger_priority_followed?`
- [ ] `trigger_evidence_sufficient?`
- [ ] `llm_silent_override_detected?`
- [ ] `selected_method_prerequisites_met?`
- [ ] `reasoning_used_for_deterministic_claim?`
- [ ] `claim_method_lineage_complete?`
- [ ] `claim_references_executed_method?`
- [ ] `baseline_explicit?`
- [ ] `baseline_robustness_required?`
- [ ] `population_constant_or_explained?`
- [ ] `denominator_constant_or_explained?`
- [ ] `scope_change_quantified?`
- [ ] `preliminary_evidence_sufficient_to_continue?`
- [ ] `alternative_explanation_considered?`
- [ ] `contradicting_evidence_checked?`
- [ ] `discriminating_evidence_defined?`
- [ ] `falsification_test_defined_if_material?`
- [ ] `material_method_disagreement_resolved_or_visible?`
- [ ] `unresolved_method_conflict_reflected_in_claim_strength?`
- [ ] `claim_support_correct?`
- [ ] `causal_status_correct?`
- [ ] `confidence_confused_with_causality?`
- [ ] `manual_review_required_assessed?` If `yes`, reviewer/owner, status, and resolution are recorded before final publication.
- [ ] `final_evidence_sufficient_for_claim?`
- [ ] `conclusion_stronger_than_evidence?`
- [ ] `stop_condition_assessed?`
- [ ] `thinking_escalation_required?`
- [ ] `routine_collapse_applied_when_eligible?`
- [ ] `unnecessary_full_reasoning_record_created?`
- [ ] `exception_vs_anomaly_distinguished?`
- [ ] `unmatched_analysis_used_when_population_mismatch_material?`
- [ ] `factor_decomposition_reconciled_when_applicable?`
- [ ] `timing_cutoff_checked_when_material?`
- [ ] `data_layer_artifact_considered_when_material?`
- [ ] `leading_indicator_relationship_supported?`
- [ ] `leading_indicator_not_presented_as_causal_without_evidence?`
- [ ] `new_method_trigger_contract_followed?`
- [ ] `new_method_prerequisites_met?`
- [ ] `new_method_added_only_if_distinct_capability?`
- [ ] `aes_execution_governance_preserved?`
- [ ] `analytics_extension_applied_without_duplication?`
- [ ] `reasoning_control_not_treated_as_autonomous_execution_loop?`
- [ ] `material_metric_definition_card_resolved?` — material/flagship/
  ratio-like metric has an approved `METRIC_DEFINITION_CARD`, or the
  conclusion is limited/blocked (`ANALYTICAL_REASONING_STANDARD.md` §11).
- [ ] `value_state_not_collapsed?` — `VALUE_STATE` distinctions are preserved
  where material; uncertainty coverage is reflected in denominator/coverage
  before a claim is `SUPPORTED` (§12).
- [ ] `headline_claim_lineage_complete?` — every headline claim for
  `analytical_depth = material/decision_critical` has a complete registry
  lineage (§13); missing lineage sets `allowed_in_executive = no`.
- [ ] `promotion_not_exceeding_evidence?` — `observation -> cause`,
  `contribution -> root cause`, `association -> causation`, and
  `single-period -> systemic/recurring/persistent` are not asserted without
  the required evidence level.
- [ ] `three_gates_not_conflated?` — Gate 1 (data/calculation), Gate 2
  (analytical claim), and Gate 3 (narrative) are kept distinct (§14);
  `DATA VALID != CLAIM SUPPORTED != NARRATIVE ACCEPTABLE`.

Use `ANALYTICAL_REASONING_STANDARD.md` for field semantics. These checks extend the existing Analysis QA; they do not create a separate QA framework.

### Analytical Judge gate (post-findings)

Explicit checkpoint after findings and before memo / report — an orchestration
pass over the controls above, not a second QA framework. For
`analytical_depth = material / decision_critical`, record an `ANALYTICAL_JUDGE`
result; routine / no-trigger cases collapse to the compact QA note. See
`ANALYTICAL_REASONING_STANDARD.md` §8.

- [ ] `question_fit?` — analysis answered the declared business question and scope.
- [ ] `method_adequacy?` — selected methods sufficient; every supporting method `execution_status: executed` with `prerequisites_met`.
- [ ] `evidence_lineage_complete?` — each headline conclusion traces executed method → source mart/table/slice → metric/period/grain/filter/baseline → evidence.
- [ ] `alternative_explanation_tested_or_visible?`
- [ ] `contradicting_evidence_or_method_disagreement_not_silently_passed?`
- [ ] `claim_strength <= final_evidence_sufficiency?` — including `driver != root cause`, `correlation != causation`, single-period != systemic.
- [ ] `recommendation_risk_implication_within_verified_evidence?`
- [ ] `ANALYTICAL_JUDGE` status recorded: `pass` / `revise` / `blocked`; `revise` resolved by one bounded correction + passing re-check; `blocked` stops publication.
- [ ] `judge_did_not_become_autonomous_retry_loop?` — no silent self-retry; no method added without registry/trigger support; `blocked != executed`.

### Material variance diagnostic QA

Apply `VARIANCE_DIAGNOSTIC_CONTRACT.md` only to material/decision-critical Plan/Fact cases or a material variance risk:

- [ ] Source/raw formula and sign convention remain distinct from normalized management direction; unresolved KPI direction blocks normalization.
- [ ] Gross adverse/favorable movement and normalized net variance reconcile using one normalized sign convention.
- [ ] Primary economic/timing/data-mapping/unresolved effects are non-overlapping, scope-complete, and reconciled; failed residual remains visible.
- [ ] Classification population, eligible gross movement, classified/unclassified movement, row counts, and coverage denominator are explicit and separate from net reconciliation.
- [ ] Materiality basis, denominator, selected/excluded population, and selection coverage are declared before narrative.
- [ ] Budget status, controllability, recurrence, and evidence status remain non-additive; unsupported controllability/recurrence remain `unknown`.
- [ ] Single-period evidence is not generalized as systemic/non-systemic; driver/ownership does not imply root cause or accountability.
- [ ] Reported result remains canonical; adjusted view reconciles separately with explicit adjustment polarity.

## Chart QA

- [ ] Chart source mart/slice listed.
- [ ] Metric listed.
- [ ] Grain listed.
- [ ] Period listed.
- [ ] Caption does not exceed data.
- [ ] Chart adds insight.
- [ ] Chart labels, legends, axes, titles and captions are Russian / business-readable.
- [ ] Executive chart palette uses muted executive colors.
- [ ] Technical IDs are absent from executive chart body unless the chart is appendix / evidence.

## Memo QA

- [ ] No unsupported claims.
- [ ] Every key conclusion has evidence.
- [ ] Limitations visible.
- [ ] Recommendations do not exceed data.
- [ ] Confidence stated.
- [ ] Risk has `risk_basis`.
- [ ] Action has owner / due date / status.
- [ ] Visible report language is Russian.
- [ ] No technical IDs in executive body.
- [ ] Technical values such as `fact_only`, `plan_only`, `p_fact_adjusted`, `refund_only`, `source_mix`, `slice_*`, `mart_*`, `EV-*`, `CH_EXEC_*` appear only in appendix / evidence context.
- [ ] Appendix is clearly separated from executive memo.

### Material management synthesis QA

Apply only to material / decision-critical management-facing output:

- [ ] Business question is answered by an executive verdict; material findings are prioritized by business relevance rather than catalogued.
- [ ] Supported business meaning is stated, or the evidence gap is explicit; any “main” issue has a supported criterion.
- [ ] Material performance dimensions remain distinct; business effect and data/control artefact are separated where relevant.
- [ ] Management implication and decision/action if any are evidence-constrained; material uncertainty remains visible.
- [ ] What would materially change the conclusion is stated when relevant, and strategic choice is routed to `[Thinking]`.
- [ ] Executive synthesis is materially shorter than supporting evidence; routine compact output is not expanded.

## Handoff QA

- [ ] Handoff only if another project is needed.
- [ ] Expected output clear.
- [ ] Acceptance criteria clear.
- [ ] Inputs listed.
- [ ] Risks listed.
- [ ] No unresolved analysis hidden in Codex task.

## Recommendation evidence, stability, and out-of-sample validation (P1-B, issue #449, bounded pilot)

Bounded pilot only. `owner review required` before any promotion decision.
Reads `ANALYTICAL_REASONING_STANDARD.md` §16 controls; adds no method, no
second Judge, and no second QA framework.

- [ ] `material_explanatory_statement_has_discriminating_test_status?` — a
  material explanatory/intervention-oriented conclusion (§16.1) records
  `DISCRIMINATING_TEST_STATUS: executed / blocked / unavailable`; contribution
  + recurrence alone does not support it.
- [ ] `recommendation_evidence_recorded_when_material_intervention_proposed?`
  — a material management recommendation has a `RECOMMENDATION_EVIDENCE`
  record (§16.2); `diagnostic evidence != intervention evidence` holds.
- [ ] `untested_intervention_capped_at_pilot_candidate?` —
  `test_or_backtest_performed = no` caps `recommendation_status <=
  pilot_candidate`.
- [ ] `stability_check_recorded_before_targeted_redesign_claim?` — a material
  concentration/recurrence/persistent-pattern claim used to justify a
  targeted (entity-specific) intervention has a `stability_check` (§16.3);
  rotating Top-N is not read as a stable targeted population.
- [ ] `forecast_method_change_has_out_of_sample_comparison?` — a
  recommendation to change a forecasting/planning method has a
  `FORECAST_METHOD_COMPARISON` with an out-of-sample period, comparable
  population/scope, same metric definitions, a monetary-error metric, and a
  frequency/corridor-accuracy metric where applicable (§16.4); otherwise
  `recommendation_status <= pilot_candidate`.
- [ ] `process_control_claim_has_process_evidence?` — `effect_type:
  process_control` (§16.5, `VARIANCE_DIAGNOSTIC_CONTRACT.md`) is not inferred
  from a financial/variance pattern alone.
- [ ] `what_would_change_the_view_present_when_material_gap_exists?` — §16.6
  is stated for material/decision-critical management-facing output with a
  material evidence gap, and omitted (not filled with a placeholder) when no
  such gap exists.
- [ ] `p1_b_controls_collapse_on_routine_no_trigger_cases?` — none of the six
  §16 elements is instantiated without its stated material activation
  trigger; the routine/quick §9 compact path is unaffected.

Pilot results for issue #449 are recorded in
`P1_449_PILOT_EVIDENCE_2026-09-06.md`.

## Held-out transfer eval (P1 QA/EVAL, issue #445)

Classification: QA/EVAL only. `HELD_OUT_TRANSFER_EVAL` is not an analytical
method, does not appear in `ANALYTICAL_TECHNIQUES.md`, has no `METHOD_ID`,
and does not change the 22-method registry. It measures whether a reliability
change (e.g. an activated P1 control) transfers beyond development/known
examples, in addition to — not instead of — existing Smoke/adversarial QA
(`SMOKE_QA_FOR_ANALYTICS.md`).

Required lanes, each evaluated for P0 baseline vs. P1 candidate:

- [ ] `known_regression_cases` — existing development/adversarial cases the
  control was designed against.
- [ ] `held_out_cases` — cases not used during design, same domain.
- [ ] `shifted_domain_cases` — different business domain, metric type, grain,
  or denominator semantics than development cases.
- [ ] `boundary_cases` — edge conditions (e.g. exact tolerance, zero
  denominator, fully matched population).
- [ ] `contradictory_evidence_cases` — cases with unresolved conflicting
  evidence, to confirm no invented resolution.
- [ ] `old_p0_regression_cases` — routine/quick P0 cases with no material
  trigger, to confirm compact-path behavior is preserved.

Anti-overfit requirement: `held_out_cases` / `shifted_domain_cases` must not
be direct paraphrases of development examples — vary business domain, metric
type, grain, denominator semantics, population-shift mechanism,
reconciliation-failure mode, timing/evidence structure, wording, and decision
context.

Required comparison and promotion rule: report `known_regression_cases` /
`held_out_cases` / `shifted_domain_cases` / `old_p0_regression_cases` results
separately, not as one blended pass rate. A known-suite win combined with
held-out or old-P0-regression deterioration is a promotion **failure**, not a
partial pass; no promotion follows from development-suite improvement alone.

`owner review required` before any promotion decision based on this eval
lane. Pilot results for issue #445 are recorded in
`P1_PILOT_EVIDENCE_2026-09-06.md`.
