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

## Main files QA

- [ ] `stage_main_full` exists or is designed.
- [ ] `stage_main_full` has no business metrics.
- [ ] `stage_main_full` has no analytical classifiers.
- [ ] `stage_main_full` is portable to DB / BI / Excel.
- [ ] `mart_main_full` exists or is designed.
- [ ] `mart_main_full` contains metrics and formulas.
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
- [ ] `material_method_disagreement_recorded?`
- [ ] `unresolved_method_conflict_reflected_in_claim_strength?`
- [ ] `claim_support_correct?`
- [ ] `causal_status_correct?`
- [ ] `confidence_confused_with_causality?`
- [ ] `manual_review_required_correctly_set?` If `yes`, reviewer/owner, status, and resolution are recorded before final publication.
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

Use `ANALYTICAL_REASONING_STANDARD.md` for field semantics. These checks extend the existing Analysis QA; they do not create a separate QA framework.

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

## Handoff QA

- [ ] Handoff only if another project is needed.
- [ ] Expected output clear.
- [ ] Acceptance criteria clear.
- [ ] Inputs listed.
- [ ] Risks listed.
- [ ] No unresolved analysis hidden in Codex task.
