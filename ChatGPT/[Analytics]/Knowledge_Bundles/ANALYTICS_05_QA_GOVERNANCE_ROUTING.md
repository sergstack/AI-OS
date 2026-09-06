# [Analytics] — QA Governance Routing

## Purpose

Compact upload artifact for [Analytics] covering qa governance routing.

## Source files

- `ChatGPT/[Analytics]/Knowledge/QA_CHECKLIST.md`
- `ChatGPT/[Analytics]/Knowledge/QUANTITATIVE_SANITY_GATE.md`
- `ChatGPT/[Analytics]/Knowledge/ACCEPTANCE_CRITERIA.md`
- `ChatGPT/[Analytics]/Knowledge/ROUTING_AND_HANDOFF.md`
- `ChatGPT/[Analytics]/Knowledge/AI_OS_REFERENCE.md`
- `ChatGPT/[Analytics]/Knowledge/GOVERNANCE_AND_ANTI_PATTERNS.md`
- `ChatGPT/[Analytics]/Knowledge/SMOKE_QA_FOR_ANALYTICS.md`
- `ChatGPT/[Analytics]/Knowledge/ANALYTICS_05_QA_GOVERNANCE_ROUTING_BUNDLE_SEMANTICS.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[Analytics]`.

## Status

- production_promotion: no, unless explicitly accepted elsewhere
- bundle_type: generated compact upload artifact
- source_of_truth: declared granular source files
- source_fingerprint: sha256:0a4f203db260ddbf5895c0248a40e6fac5bb3008d80a1053045489c1b8603076
- generator: scripts/build_knowledge_bundles.py

---

# Content

## From: `ChatGPT/[Analytics]/Knowledge/QA_CHECKLIST.md`

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

## From: `ChatGPT/[Analytics]/Knowledge/QUANTITATIVE_SANITY_GATE.md`

# Quantitative Sanity Gate
## Purpose and boundary
`quantitative_sanity_gate` is the mandatory pre-publish control for a
quantitative Analytics report. It proves that a decision-bearing number is
plausible, correctly represented, precisely traceable, method-appropriate,
and independently reproducible. It is an extension of existing Analytics QA
and acceptance; it does not replace QA, Judge, reconciliation, or AES.
The gate is required only when a report is being published or presented as a
publishable management-facing result and contains one or more
`flagship_metric`s. A `flagship_metric` is a number shown in an executive
summary, heading, key finding, decision/recommendation basis, or otherwise
used to determine the report conclusion.
Do not create a gate record for private scratch calculations, exploratory
work, or an unpublished draft that is explicitly not offered as a result. If
such material becomes publishable, assess the gate before publication. A
report with no quantitative conclusion records `quantitative_sanity_gate_status:
not_applicable` with its reason.
Gate records are evidence artifacts or an appendix, not required executive
output. `quick` and routine compact reports retain their existing visible
format; publication still requires the internal gate evidence when they make a
quantitative decision-bearing claim.
## Canonical gate record
Create one record for every `flagship_metric`:
```text
metric_id:
metric_name:
reported_value:
unit:
population:
period:
grain:
filters:
source_locator:
representation_check:
plausibility_expectation:
plausibility_result: pass / fail / blocked
method:
method_applicability:
censoring_status: none / present / unknown
independent_source_locator:
independent_recalculation_method:
independent_recalculated_value:
tolerance:
reproduction_result: pass / fail / blocked
reviewer_or_execution_id:
evidence_reference:
resolution:
```
`source_locator` identifies where the reported metric is read back.
`independent_source_locator` identifies the source-level fields/evidence used
by the independent recalculation; it must not point only to the same derived
cells, formula output, copied aggregate, or calculated metric column.
Both locators must be read-back-verifiable:
- spreadsheet: file/workbook, sheet, and cell/range or structured table/column;
- database: dataset/schema/table, fields, and query/filter reference;
- mart: exact mart, row/key/filter, and metric/formula field; the independent
  locator still names the source-level inputs;
- another source: an equivalently precise, readable location.
General names such as `source workbook`, `raw data`, or `mart_main_full` are
not locators by themselves.
## Gate rules
- Check order of magnitude, sign, units, feasible range, and relevant
  cross-field/domain invariants.
- Validate storage semantics for duration metrics. When raw timestamps exist,
  cross-check the derived duration against their difference. Excel time-of-day
  values must not silently represent elapsed durations above 24 hours.
- For time-to-event metrics, state whether observations are open, closed, or
  right-censored. A closed-only percentile is not a complete-population
  duration when censoring is material. Use an appropriate survival method such
  as Kaplan–Meier, or mark the metric limited/blocked with the method gap.
- Independent reproduction starts from the `independent_source_locator`, uses
  an explicit path and tolerance, and cannot reuse the reported derived result.
- Taxonomy, formatting, arithmetic consistency, or reconciliation alone never
  prove gate passage.
## Aggregate status
```text
quantitative_sanity_gate_status: pass / revise / blocked / not_applicable
```
- `pass`: every flagship record has both checks passing, complete evidence and
  locators, an applicable method, and an explicit reproduction within tolerance.
- `revise`: one or more records fail, but a bounded remediation path is known;
  publication is prohibited until the affected records pass.
- `blocked`: required evidence, a read-back locator, source-level reproduction,
  or an applicable method is unavailable or unresolved; publication is
  prohibited.
- `not_applicable`: no published quantitative conclusion is present; state the
  reason. It is not a substitute for a failed or missing flagship record.
For `revise` or `blocked`, name each failed metric, evidence, owner/reviewer,
required remediation, and publication status in `resolution`.
## Non-acceptance
- A generic “sanity checked” item without the record and stop behavior.
- A report-level `pass` when any flagship metric is failed, blocked, missing
  evidence, or has an unresolved locator.
- Successful reconciliation presented as proof of correct units or duration
  representation.
- Recalculation from the same erroneous calculated cells or derived column.
- Kaplan–Meier mentioned as optional prose while a materially censored
  closed-only percentile passes.
- Copying this full contract into global system instructions or a second
  Analytics QA framework.
## Integration
`QA_CHECKLIST.md` owns the operational checklist, `ACCEPTANCE_CRITERIA.md`
owns result acceptance, and `DATA_CONTRACTS.md` owns source/evidence inputs.
Those files reference this contract rather than duplicate it. Method registry
ownership remains in `ANALYTICAL_TECHNIQUES.md`; this gate adds no method ID.

## From: `ChatGPT/[Analytics]/Knowledge/ACCEPTANCE_CRITERIA.md`

# Analytics Acceptance Criteria
A result is accepted when:
1. Question and scope are clear.
2. Inputs are listed.
3. Data contract exists or missing fields are explicit.
4. Grain, period and filters are documented.
5. Stage and mart main files are created or designed.
6. Calculation method is documented.
7. QA checks passed or failed with explanation.
8. Findings are traceable to data.
9. Limitations are explicit.
10. Handoff package is complete if another project is needed.
11. Before publication, every flagship metric in a quantitative report passes
    `QUANTITATIVE_SANITY_GATE.md`; otherwise the result is `revise` or
    `blocked` and is not published as a final quantitative conclusion.
12. For `analytical_depth = material / decision_critical`, the Analytical Judge
    gate (`ANALYTICAL_REASONING_STANDARD.md` §8) ran after findings and before
    memo / report generation, and an `ANALYTICAL_JUDGE` result is recorded with
    `status: pass` (or a `revise` resolved by one bounded correction and a
    passing re-check). A `blocked` Judge status means the final management
    conclusion is not published. `maximum_claim_strength` does not exceed
    `FINAL_EVIDENCE_SUFFICIENCY`; `driver != root cause` and
    `correlation != causation` hold. Routine / no-trigger cases satisfy this
    through the compact QA note without a full Judge record.
13. Material/flagship/ratio-like metrics have an approved
    `METRIC_DEFINITION_CARD` (`ANALYTICAL_REASONING_STANDARD.md` §11); an
    unresolved material metric definition blocks a strong management
    conclusion.
14. `VALUE_STATE` distinctions are not collapsed into a generic null where
    material (§12); a claim built on unresolved material uncertainty coverage
    is at most `PARTIALLY_SUPPORTED`, unless the uncertainty is quantified and
    demonstrably does not change the conclusion.
15. For `analytical_depth = material / decision_critical`, every headline
    claim has complete Claim/Evidence Registry lineage (§13); missing
    lineage sets `allowed_in_executive = no` and the claim does not appear
    in the executive layer.
## Main file acceptance
```text
stage_main_full: pass/fail/blocked/not_applicable
mart_main_full: pass/fail/blocked/not_applicable
mart_main_tz_or_compact: pass/fail/blocked/not_applicable
slices_from_mart_main_full: pass/fail/blocked/not_applicable
```
## Acceptance status
```text
accepted: yes/no
qa_status: pass/fail/blocked
quantitative_sanity_gate_status: pass/revise/blocked/not_applicable
analytical_judge_status: pass/revise/blocked/not_applicable
metric_definition_status: approved/provisional/blocked/not_applicable
value_state_coverage_status: pass/revise/blocked/not_applicable
headline_claim_gate_status: pass/blocked/not_applicable
confidence: high/medium/low
residual_risks:
known_limitations:
next_step:
```
## Usability acceptance
A result is not accepted if it is technically complete but unusable for the requested task.
For `quick` mode:
- max 1 user-facing table;
- max 5 metrics;
- max 12 visible columns;
- no workbook unless explicitly requested;
- no hidden expansion into `full` package.
For `standard` mode:
- compact front view required;
- no more than 3-5 sheets unless justified;
- every extra sheet must have a business purpose.
For `full` mode:
- workbook may be large, but must include:
  - README / index;
  - compact front sheet;
  - data dictionary;
  - field groups;
  - evidence appendix.
## Material management synthesis acceptance
For `analytical_depth = material / decision_critical` and management-facing output:
- the business question is answered by an executive verdict;
- the smallest sufficient set of material findings is prioritized by a supported business criterion;
- headline business meaning is supported or its evidence gap is explicit;
- materially different performance dimensions and data/control artefacts remain distinct where relevant;
- management implication and decision/action if any do not exceed verified evidence;
- material uncertainty remains visible, with what would change the view where applicable;
- strategic choice is routed to `[Thinking]` when it depends on trade-offs, risk appetite, or preferences;
- the executive layer is materially shorter than the supporting evidence.
Routine compact tasks are excluded from expanded synthesis acceptance.
## Material Plan/Fact variance acceptance
For cases governed by `VARIANCE_DIAGNOSTIC_CONTRACT.md`:
- reported and normalized management views are both traceable and use explicit, non-mixed sign conventions;
- gross adverse/favorable movement, normalized net variance, and primary attribution reconcile deterministically;
- gross classification coverage declares population, denominator, classified/unclassified movement, and unknown rows separately from net reconciliation;
- materiality basis and selected/excluded population are explicit;
- controllability, recurrence, generalization, and accountability claims have required evidence or remain unknown/not established;
- adjusted view is supplementary, reconciled, and uses explicit adjustment polarity;
- management synthesis follows the contract semantically without expanding routine output.
## Blocked status
Use `blocked` when:
- required data is missing;
- grain is unknown;
- DQ Fail;
- no reconciliation possible;
- metric formulas undefined;
- compact-only input is insufficient for requested conclusion;
- implementation is required before result can be produced.
- a required flagship metric has a blocked quantitative sanity gate.
- the Analytical Judge gate returns `blocked` (required prerequisite,
  reconciliation, grain, validation path, or discriminating evidence
  unavailable).
- a material/flagship/ratio-like metric has no approved
  `METRIC_DEFINITION_CARD` and the conclusion depends on it.
- a headline claim for `analytical_depth = material / decision_critical` has
  no complete Claim/Evidence Registry lineage (`allowed_in_executive = no`).
## Not production-ready rule
Smoke QA or a good memo does not equal production readiness. Production readiness requires implementation evidence, tests, acceptance and rollback/release notes where relevant.

## From: `ChatGPT/[Analytics]/Knowledge/ROUTING_AND_HANDOFF.md`

# Routing and Handoff
Canonical destination routing is defined in repo-root `ROUTING_RULES.md`.
## Analytics default
For metrics, marts, data contracts, QA, calculations, deviations, charts and analytical memo structure: stay in `[Analytics]`.
## Analytical Memo Factory via Codex APP
If the user asks to create an analytical memo as an executable artifact, use:
```text
[Analytics] for analytical task framing
-> [Codex] for ultra-long Codex APP task package
-> Codex APP for execution
```
Keep `[Analytics]` responsible for methodology, data contracts, assumptions, limitations, and acceptance criteria. `[Codex]` designs the task package; Codex APP executes locally.
Do not force an interactive loop where `[Analytics]` asks for Python outputs back and forth unless the user explicitly wants manual exploration.
## Do not hand off too early
Before handoff, provide:
- analytical framing;
- data contract or missing fields;
- main files standard;
- expected metrics;
- QA requirements;
- acceptance criteria.
Use the canonical handoff fields in `HANDOFF_STYLE_STANDARD.md`.
## Thinking → Analytics
Use when decision/scenario requires calculations.
Pass:
- question;
- metrics;
- period;
- assumptions;
- options to test;
- expected analytical output.
## Analytics → LLM
Use when verified numbers need narrative, prompt workflow or model routing.
Pass:
- curated facts;
- tables or marts;
- reconciled metrics;
- limitations;
- tone and output format.
## Analytics → Codex
Use when implementation is needed.
Pass:
- files to inspect/change;
- input/output contract;
- main files rules;
- task packet;
- forbidden actions;
- tests;
- acceptance criteria.
## Codex → QA / Release
Pass:
- changed files;
- tests run;
- smoke QA;
- acceptance status;
- residual risks;
- rollback notes.

## From: `ChatGPT/[Analytics]/Knowledge/AI_OS_REFERENCE.md`

# AI OS Reference
## Purpose
`[Analytics]` does not contain the full AI OS KB. `[AI OS]` already stores governed knowledge about AI concepts, tools, patterns, governance and use cases.
Use `[AI OS]` when needed:
- understand a new AI concept;
- find supported AI pattern;
- check confidence / evidence for AI claims;
- connect AI trend to Sergey’s work;
- find governance rule;
- distinguish supported / weak / unsupported AI claim.
## Do not copy into Analytics
Do not copy:
- full AI OS compact KB package;
- raw transcripts;
- source cards;
- chunks;
- temp files;
- logs;
- embeddings;
- vector DB;
- web UI artifacts.
## How to ask AI OS
```text
Используй AI OS KB. Найди supported/weak/unsupported evidence по теме:
<topic>
Верни:
- найдено в KB: да/нет/частично
- sources
- confidence
- supported claims
- weak/unsupported claims
- practical use for Sergey
```
## Boundary rule
AI OS gives evidence and patterns. `[Analytics]` applies them only when they affect analytics workflow, QA, marts, memo or reporting.

## From: `ChatGPT/[Analytics]/Knowledge/GOVERNANCE_AND_ANTI_PATTERNS.md`

# Governance and Anti-Patterns
## Governance principles
- Deterministic calculations before LLM narrative.
- Traceability before automation.
- Main files before slices.
- Evidence before conclusions.
- Acceptance before production readiness.
- Analysis inside `[Analytics]` before handoff.
- Method eligibility and triggers follow `ANALYTICAL_TECHNIQUES.md`; the LLM cannot silently override the registry.
- Reasoning cannot substitute for deterministic execution or missing prerequisites.
- Claim strength cannot exceed final evidence sufficiency.
- Every material / decision-critical analytical conclusion passes an explicit post-findings Analytical Judge gate (`ANALYTICAL_REASONING_STANDARD.md` §8) before narrative packaging; the gate orchestrates existing controls and adds no second QA framework.
- `docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md` remains canonical execution governance; `ANALYTICS_EXTENSION.md` supplies domain-specific constraints without creating a second execution framework.
- A formula alone is not a sufficient metric definition; material/flagship/ratio-like metrics require an approved `METRIC_DEFINITION_CARD` (`ANALYTICAL_REASONING_STANDARD.md` §11).
- Canonical `VALUE_STATE` distinctions (`DATA_CONTRACTS.md`) are not collapsed into a generic null where doing so could change denominator, population, reconciliation, classification coverage, metric result, claim strength, or management conclusion (§12).
- Every headline claim for `analytical_depth = material / decision_critical` has complete Claim/Evidence Registry lineage; missing lineage sets `allowed_in_executive = no` (§13).
- `GATE 1 (data/calculation)`, `GATE 2 (analytical claim)`, and `GATE 3 (narrative)` remain distinct: `DATA VALID != CLAIM SUPPORTED != NARRATIVE ACCEPTABLE` (§14).
## Evidence labels
Use:
```text
DATA FACT
CALCULATION RESULT
INTERPRETATION
RECOMMENDATION
HYPOTHESIS
LIMITATION
BLOCKER
```
## Blockers
Do not publish final management conclusion when:
- data contract missing;
- grain missing;
- DQ Fail;
- unreconciled totals;
- missing metric formula;
- unsupported cause;
- risk without basis;
- action without owner/due date;
- no main mart for a mart-based conclusion;
- the Analytical Judge gate returns `blocked`;
- a material/flagship/ratio-like metric has no approved `METRIC_DEFINITION_CARD`;
- a headline claim lacks complete Claim/Evidence Registry lineage (`allowed_in_executive = no`).
## Anti-patterns
| Anti-pattern | Why bad | Correct action |
|---|---|---|
| Handoff to Codex too early | Analytics loses its role | Analyze first, handoff implementation only |
| Slices before main files | Inconsistent outputs | Build `stage_main_full`, then `mart_main_full`, then slices |
| Raw-to-memo | Unsupported conclusions | Use mart/evidence |
| LLM as calculation source | Non-deterministic truth | Calculate deterministically |
| Hidden business logic | Cannot audit | Document formulas/classifiers |
| Pretty memo before QA | Looks right, may be wrong | QA first |
| Low Confidence as fact | Misleading | Label hypothesis |
| Risk without basis | Decorative risk | Add `risk_basis` or remove |
| Action without owner/date | Not actionable | Add owner/due date/status |
## P0 analytical reasoning failure modes
Apply these controls through `ANALYTICAL_REASONING_STANDARD.md` and the existing Analysis QA; do not create a competing governance or QA framework.
| Failure mode | Required control |
|---|---|
| Driver presented as root cause; correlation presented as causation | Use the claim ladder, `claim_support`, `causal_status`, and causal evidence gate. |
| Premature explanation | Run the preliminary evidence check and stop when explanatory analysis is infeasible. |
| Baseline dependence | State baseline/rationale and run required baseline robustness for material cases. |
| Aggregation bias; selection/exclusion bias | Check materially relevant segmentation, exclusions, and subgroup robustness. |
| Population or denominator change | Explain population/denominator and quantify scope change before interpreting ratios. |
| Timing or cut-off effect | State cut-off and test timing/trend when the declared trigger is satisfied. |
| False precision | Constrain precision and claim strength to data quality and evidence sufficiency. |
| Silent exclusions | Record materially plausible excluded methods and data exclusions. |
| Narrative stronger than evidence | Enforce `claim strength <= final evidence sufficiency`. |
| Method bloat | Use the minimum sufficient method set and stop conditions. |
| Confidence mistaken for causality | Preserve `confidence != claim_support != causal_status`. |
| Numerical magnitude mistaken for business materiality | Assess decision context and materiality separately; do not use a numerical reasoning score. |
| Reasoning substituted for deterministic execution | Enforce `LLM reasoning != deterministic execution`. |
| LLM silently overrides method registry | Record candidate omission and route it to existing QA/review. |
| Subjective or undefined method trigger | Require `trigger_type`, `trigger_rule`, and `trigger_evidence_required`. |
| Blocked method treated as evidence | Enforce `blocked != executed` and reject blocked/planned/not-needed lineage. |
| Method execution lineage loss | Require unique `method_execution_id` and claim-to-evidence lineage. |
| Conflicting methods silently reconciled | Preserve conflicting results, record contradictory evidence, constrain claim strength, and escalate if material. |
| Full reasoning runtime applied to a routine case without trigger | Use the compact path and do not instantiate unused full reasoning records. |
| Anomaly mistaken for control exception | Distinguish unusual observations from explicit rule/control violations. |
| Aggregate reconciliation used instead of entity-level unmatched analysis | Use unmatched-elements analysis when concrete one-sided populations are material. |
| Driver decomposition accepted without factor reconciliation | Reconcile summed factor effects to observed delta whenever mathematically applicable. |
| Timing shift interpreted as economic effect | Run timing validation when cut-off or recognition timing could change interpretation. |
| Transformation artifact interpreted as source/business effect | Trace `REPORT → MART → STAGE → RAW` and identify the first verified layer where the effect appears. |
| Leading indicator treated as proven causal predictor | Use calibrated signal/association/risk language unless causal evidence exists. |
| Method catalog inflated by converting controls into methods | Require a distinct question, execution procedure, and material analytical effect before adding a method. |
| Decision methods leak from `[Thinking]` into `[Analytics]` | Keep trade-offs, reversibility, premortem, risk appetite, choice, and decision in `[Thinking]`. |
| Reasoning-control loop mistaken for an autonomous execution loop | Keep reasoning/method selection inside the AES-governed scope, checks, bounded correction, stop, rollback, acceptance, and authority boundaries. |
| Analytical conclusion reaches memo without an explicit post-findings challenge | Run the Analytical Judge gate after findings; record `ANALYTICAL_JUDGE` `pass / revise / blocked` for material / decision-critical cases. |
| Analytical Judge treated as an autonomous retry loop | Allow only `Judge finding → one bounded correction or deterministic rerun → Judge re-check`; no silent self-retry, no unrestricted iteration; AES limits and the `[Codex]` one-fix limit are unchanged. |
| Analytical Judge used as a second QA framework or a new taxonomy | The gate only orchestrates `PRELIMINARY_EVIDENCE_CHECK`, explanation challenge, `FINAL_EVIDENCE_SUFFICIENCY`, `CLAIM_EVIDENCE_REGISTRY`, Analysis QA, and variance diagnostic QA; it defines no new field. |
| `blocked` method converted into evidence at the Judge step | Enforce `blocked != executed`; a `blocked` prerequisite forces Judge `blocked`, not a weaker `pass`. |
| Formula treated as a sufficient metric definition (ambiguous ratio/rate published as flagship) | Require `METRIC_DEFINITION_CARD` with numerator/denominator/aggregation/population before a material conclusion; block or limit if unresolved. |
| Materially different missing/uncertainty states collapsed into one null | Preserve `VALUE_STATE` (`UNKNOWN`/`NOT_REPORTED`/`PARSE_FAILED`/`MISSING_SOURCE`/`UNMATCHED`/`BLOCKED`); reflect coverage/denominator impact before claiming `SUPPORTED`. |
| Headline claim published without method/evidence lineage | Require complete Claim/Evidence Registry lineage; set `allowed_in_executive = no` and route to Analytical Judge `revise`/`blocked` when missing. |
| Data/calculation correctness treated as license for a stronger claim or narrative | Keep `GATE 1 (data/calculation)`, `GATE 2 (analytical claim)`, `GATE 3 (narrative)` distinct; `DATA VALID != CLAIM SUPPORTED != NARRATIVE ACCEPTABLE`. |
## Metric / artifact explosion
Anti-pattern:
A short analytical request produces a large workbook, many sheets, or hundreds of columns without explicit need.
Why bad:
- user cannot inspect the result;
- decision signal is buried;
- QA fields become noise;
- compact task becomes `full` package.
Correct action:
- classify output mode first;
- default to compact view;
- expose only decision-relevant metrics;
- move evidence/QA/lineage to appendix or internal design;
- ask for `full` mode only when needed.
## Production readiness rule
Do not claim production readiness unless:
- implementation exists;
- tests passed;
- smoke QA recorded;
- acceptance criteria passed;
- residual risks listed;
- rollback/release notes exist.

## From: `ChatGPT/[Analytics]/Knowledge/SMOKE_QA_FOR_ANALYTICS.md`

# Smoke QA for Analytics
Назначение: проверить, что `[Analytics]` после загрузки пакета сохраняет способность проводить анализ и правильно использует routing, main files, QA и handoff.
## 1. Scope and routing
Question:
```text
Мне нужно проанализировать отклонения план-факт и подготовить выводы. Ты будешь делать это здесь или отправишь в Codex?
```
Pass condition:
- отвечает, что анализ делается в `[Analytics]`;
- Codex нужен только для реализации/автоматизации;
- называет data contract, stage/mart, QA.
## 2. Main files
Question:
```text
Какие главные файлы должны быть в stage и mart?
```
Pass condition:
- называет `stage_main_full`;
- говорит, что stage без метрик и классификаторов;
- называет `mart_main_full`;
- называет `mart_main_tz` или `mart_main_compact`;
- говорит, что slices строятся из `mart_main_full`.
## 3. Compact/full input
Question:
```text
На входе есть только json compact. Что ты сделаешь?
```
Pass condition:
- использует compact как scope;
- фиксирует assumptions/gaps;
- не придумывает full context;
- всё равно проектирует main files.
## 4. Charts
Question:
```text
Из чего строить графики для аналитической записки?
```
Pass condition:
- отвечает: из `mart_main_full` или slices derived from it;
- требует metric, grain, period, source_mart.
## 5. Memo
Question:
```text
Какие обязательные блоки MVP аналитической записки?
```
Pass condition:
- DQ;
- Plan / Fact / Delta / ABS Delta;
- top deviations;
- row type;
- timing;
- risk + basis;
- confidence;
- cause vs hypothesis;
- action + owner + due date;
- limitations.
## 6. Stop conditions
Question:
```text
Когда нельзя публиковать управленческий вывод?
```
Pass condition:
- DQ Fail;
- no grain;
- no data contract;
- no reconciliation;
- Low Confidence as final cause;
- risk without basis;
- action without owner/date;
- INOUT without Definition Card.
## 7. Acceptance
Question:
```text
Когда результат аналитики считается принятым?
```
Pass condition:
- scope clear;
- inputs listed;
- data contract;
- main files;
- calculation method;
- QA;
- traceable findings;
- limitations;
- handoff complete if needed.
## 8. Short task / anti-bloat test
Question:
```text
Сделай короткий анализ: покажи 3 главных отклонения и вывод.
```
Pass condition:
- mode = `quick`;
- no workbook unless requested;
- no `full` package;
- max 1 table;
- max 5 metrics;
- max 12 visible columns;
- full mart is not generated by default;
- answer includes QA note and limitations;
- result is decision-readable.
## 9. Missing-data compact fast path
Question:
```text
Покажи Top-3 отклонения план-факт и управленческий вывод. Данных, grain, периода и единиц нет. Не задавай лишних вопросов.
```
Pass condition:
- result is `NOT CALCULABLE`;
- no placeholder ranking or empty Top-N table;
- no invented example rows or values;
- minimum required input and one next action are explicit;
- confidence and the material blocker remain visible;
- the same blocker is not repeated across separate QA, limitation, and gate sections.
## 10. Quantitative sanity gate
Question:
```text
Перед публикацией отчёта медиана длительности равна 1,4 ч. В Excel длительности
хранятся как time-of-day, а в исходных timestamps есть многодневные эпизоды.
Ссылка ведёт на другой лист. Можно поставить GATE=pass?
```
Pass condition:
- identifies the Excel modulo-24 representation failure and the wrong
  sheet/range locator;
- sets the affected metric and overall gate to `revise` or `blocked`, never
  `pass`;
- requires a source-level independent recomputation rather than reusing the
  derived duration cells.
Question:
```text
Можно ли назвать closed-only percentile полной длительностью популяции, если
есть materially right-censored open cases?
```
Pass condition:
- declares the censoring status and method applicability;
- requires an appropriate survival method such as Kaplan–Meier, or marks the
  metric limited/blocked;
- does not allow the report-level gate to pass.
Question:
```text
Это короткая внутренняя exploratory заметка, которую не публикуют. Нужна ли
полная gate record прямо в ответе?
```
Pass condition:
- does not create a publish gate record for the unpublished exploration;
- preserves the compact `quick` output;
- requires the internal gate evidence before the note becomes publishable and
  contains a flagship metric.
Question:
```text
В опубликованном отчёте две flagship metrics. У первой все проверки и
source-level recomputation проходят, у второй отсутствует independent source
locator. Может ли общий gate быть pass?
```
Pass condition:
- records the first metric as passing and the second as `blocked`;
- sets the aggregate gate to `blocked`, never `pass`;
- names the missing locator and required remediation.
Question:
```text
У опубликованной flagship metric есть exact reported-value locator и separate
source-level locator. Units, feasible range, representation, method
applicability и independent recomputation within tolerance all pass. Каков
статус gate?
```
Pass condition:
- records all required evidence, including both locators and tolerance;
- sets the metric and aggregate gate to `pass`;
- does not add unnecessary executive-facing gate tables.
## 11. Analytical Judge gate
Question:
```text
Deterministic calculation shows category X contributed 70% of a monthly
variance. No causal test, timing validation, or alternative explanation test
was executed. The draft conclusion says: "Category X is the root cause of the
deterioration." Каков результат Analytical Judge?
```
Pass condition:
- `ANALYTICAL_JUDGE status: revise` (not `pass`);
- reason: a 70% contribution supports a driver candidate / calculated effect
  within the observed period, not a root cause;
- `maximum_claim_strength`: "Category X is the main quantified contributor
  within the observed period";
- `required_action`: weaken the claim, or execute the discriminating tests
  (timing validation, alternative explanation, causal test) if prerequisites
  exist;
- no silent self-retry; no method added without registry/trigger support;
- `driver != root cause` and `claim strength <= final evidence sufficiency`
  are cited.
Question:
```text
Routine quick task, low uncertainty, no material trigger. Нужен полный
семиквестионный ANALYTICAL_JUDGE record?
```
Pass condition:
- collapses to the compact QA note;
- does not instantiate the full seven-question `ANALYTICAL_JUDGE` record;
- `quick` output stays compact.
## 12. Metric semantics, VALUE_STATE, and Headline Claim Gate (P0 issue #439)
Question (ambiguous metric):
```text
Отчёт публикует "Planning accuracy = 82%" как flagship-вывод. Numerator,
denominator и aggregation rule не определены. Можно публиковать как
flagship conclusion?
```
Pass condition:
- states the metric definition is incomplete (no `METRIC_DEFINITION_CARD`
  with numerator/denominator/aggregation);
- does not allow `82%` to be published as a flagship conclusion;
- requires either a completed `METRIC_DEFINITION_CARD` (`status: approved`)
  or an explicit limitation/block before publication.
Question (uncertainty collapse):
```text
Источник содержит строки со state KNOWN, UNKNOWN, PARSE_FAILED и
NOT_REPORTED. Можно свести их все к одному null перед расчётом coverage?
```
Pass condition:
- refuses to collapse `KNOWN`/`UNKNOWN`/`PARSE_FAILED`/`NOT_REPORTED` into one
  generic null;
- states coverage/denominator must reflect the distinct states;
- limits the management conclusion if the uncertainty is material.
Question (contribution vs root cause):
```text
Category X contributed 70% of the monthly variance. No causal test,
timing validation, or alternative-explanation test was executed. Можно
написать "Category X is the root cause"?
```
Pass condition:
- rejects `root cause`;
- sets maximum claim strength to "main quantified contributor within the
  observed scope";
- cites `driver != root cause` and `claim strength <= final evidence
  sufficiency`.
Question (alternative-explanation evidence, still no causal design):
```text
Category X contributed 70% of the monthly variance. An alternative-explanation
test was executed and rules out the two competing explanations (seasonality,
one-off booking error). No causal test or causal-capable design was run.
Можно написать "Category X is the root cause"?
```
Pass condition:
- allows promotion to `SUPPORTED EXPLANATION` given the discriminating
  alternative-explanation evidence;
- still rejects `ROOT CAUSE`, because promotion beyond `SUPPORTED EXPLANATION`
  requires causal evidence or a causal-capable analytical design
  (`causal_status: causal_evidence`), which was not run;
- `maximum_claim_strength`: "Category X is the supported explanation for the
  variance within the observed scope" — not `root cause`.
Question (single-period generalization):
```text
Один месяц показывает концентрацию проблемы в одном канале. Можно
назвать это systemic, recurring или persistent?
```
Pass condition:
- refuses `systemic` / `recurring` / `persistent` / `one-off` without
  `generalization_evidence`;
- states the observed period/population boundary explicitly
  (`generalization_scope`).
Question (headline without lineage):
```text
Executive draft содержит material claim без method_execution_id и
evidence_id. Можно оставить его в исполнительном разделе memo?
```
Pass condition:
- sets `allowed_in_executive = no`;
- Analytical Judge status is `revise` or `blocked` depending on
  recoverability, never `pass`;
- the claim is removed from the executive body or the lineage is completed
  before publication.
## 13. Held-out transfer eval (P1 QA/EVAL, issue #445)
QA/EVAL lane only — see `QA_CHECKLIST.md` for the full lane definition. These
are the `held_out_cases` / `shifted_domain_cases` entries for the bounded
pilot; they are not analytical methods. Full P0-vs-P1 scenario reasoning is
recorded in `P1_PILOT_EVIDENCE_2026-09-06.md`; this section holds the smoke
QA question form only.
Question (held-out population semantics shift):
```text
Cost per resolved ticket falls period over period, but the ticket-closure
policy changed so more low-effort tickets now count as "resolved". Можно
опубликовать вывод, что стоимость обработки снизилась?
```
Pass condition:
- treats "resolved" as a changed denominator/population, not familiar
  terminology from a financial-restructuring example;
- `denominator_changed_vs_baseline = yes` (or equivalent), `interpretation_allowed`
  is not `yes` until the closure-policy effect is quantified;
- does not accept the efficiency conclusion at face value.
Question (held-out reconciliation semantics shift):
```text
Total customer count is equal across two periods, but a material share of
customers entered and exited between periods. Означает ли равное общее
количество, что базы клиентов идентичны?
```
Pass condition:
- distinguishes equal aggregate count from matched-population integrity;
- surfaces `only_in_left` / `only_in_right` entrant/exit populations rather
  than treating equal totals as proof of an unchanged population;
- does not issue a global "populations match" conclusion from the aggregate
  count alone.
Question (old P0 compact regression protection):
```text
Простая быстрая задача Plan/Fact, population стабильна, данные reconciled,
материального триггера нет. Нужен полный POPULATION_CONTRACT /
RECONCILIATION_CONTRACT / ANALYSIS_CONTINUATION_GATE в ответе?
```
Pass condition:
- preserves the existing compact P0 path (§9 runtime collapse);
- does not instantiate a full P1 contract/gate record without a material
  trigger;
- claim calibration and QA note remain as in the pre-#445 compact path.
## Smoke QA output
```text
smoke_qa_status: pass/fail/blocked
failed_questions:
residual_risks:
next_step:
```
Smoke QA is not production readiness.

## From: `ChatGPT/[Analytics]/Knowledge/ANALYTICS_05_QA_GOVERNANCE_ROUTING_BUNDLE_SEMANTICS.md`

# Migrated Bundle Semantics
Canonical source created during Issue #285 provenance migration.
Legacy bundle provenance: `ChatGPT/[Analytics]/Knowledge_Bundles/ANALYTICS_05_QA_GOVERNANCE_ROUTING.md`.
## Legacy section: `ChatGPT/[Analytics]/Knowledge/QA_CHECKLIST.md`
- [ ] Method selection adequate; no material omission or method bloat.
- [ ] Registry mapping followed; deterministic trigger, trigger priority, and trigger contract/evidence checked; no silent LLM override.
- [ ] Selected prerequisites met; reasoning did not replace a deterministic claim.
- [ ] Claim lineage is complete and references an executed method.
- [ ] Baseline explicit; required baseline robustness assessed.
- [ ] Population/denominator explained and scope change quantified.
- [ ] Preliminary evidence sufficient to continue.
- [ ] Alternative explanation, contradicting/discriminating evidence, and material falsification test assessed.
- [ ] Material method disagreement recorded and unresolved conflict constrains claim strength.
- [ ] Claim support, causal status, and confidence are not confused.
- [ ] `manual_review_required` correctly set; when `yes`, review owner/status/resolution recorded before publication.
- [ ] Final evidence sufficient for the claim; conclusion is not stronger than evidence.
- [ ] Stop/escalation assessed; routine collapse applied; no unnecessary full reasoning record.
- [ ] Exception and anomaly distinguished.
- [ ] Unmatched analysis used when population mismatch is material.
- [ ] Factor decomposition reconciled when applicable.
- [ ] Timing/cut-off checked when material.
- [ ] Data-layer artifact considered when material.
- [ ] Leading-indicator relationship supported and not presented as causal without evidence.
- [ ] New-method trigger contract and prerequisites satisfied.
- [ ] New method added only for a distinct capability.
- [ ] AES remains canonical execution governance; the Analytics extension is applied without duplication.
- [ ] Reasoning control is not treated as an autonomous execution or independent retry loop.
Use `ANALYTICAL_REASONING_STANDARD.md` for field semantics. This extends existing Analysis QA and creates no separate QA framework.
Use `VARIANCE_DIAGNOSTIC_CONTRACT.md` only for material/decision-critical Plan/Fact or material variance risk:
- [ ] Raw/source and normalized management signs are explicit/non-mixed; unresolved direction blocks normalization.
- [ ] Gross adverse/favorable and net reconcile; primary economic/timing/data-mapping/unresolved effects are non-overlapping and scope-complete.
- [ ] Coverage declares gross population/denominator, classified/unclassified movement and row counts separately from net reconciliation.
- [ ] Materiality basis, denominator, selected/excluded population, and selection coverage precede narrative.
- [ ] Secondary attributes are non-additive; unsupported controllability/recurrence remain unknown.
- [ ] Single-period evidence is not systemic/non-systemic; driver/owner does not imply root cause/accountability.
- [ ] Reported result remains canonical; adjusted view reconciles with explicit polarity.
## Legacy section: `ChatGPT/[Analytics]/Knowledge/ACCEPTANCE_CRITERIA.md`
- workbook may be large, but must include README / index, compact front sheet, data dictionary, field groups and evidence appendix.
For `VARIANCE_DIAGNOSTIC_CONTRACT.md` cases:
- reported/raw and normalized views are traceable and signs are explicit/non-mixed;
- gross/net bridge and primary attribution reconcile deterministically;
- gross coverage declares population, denominator, classified/unclassified movement and unknown rows separately;
- materiality basis/population are explicit;
- controllability, recurrence, generalization, and accountability have evidence or remain unknown/not established;
- adjusted view is supplementary, reconciled, and uses explicit polarity;
- management synthesis follows the semantic contract without expanding routine output.
## Legacy section: `ChatGPT/[Analytics]/Knowledge/GOVERNANCE_AND_ANTI_PATTERNS.md`
- Registry and trigger contracts govern method eligibility; no silent LLM override.
- Reasoning cannot replace deterministic execution or missing prerequisites.
- AES remains canonical execution governance; the Analytics extension adds domain constraints without creating a second execution framework.
- Driver/root-cause and correlation/causation confusion → claim ladder and causal evidence gate.
- Premature explanation → preliminary evidence stop gate.
- Baseline, aggregation, selection/exclusion, population, denominator, timing/cut-off bias → explicit controls and triggered robustness tests.
- False precision and narrative stronger than evidence → final evidence sufficiency cap.
- Method bloat → minimum sufficient set and stop rules.
- Confidence mistaken for causality → `confidence != claim_support != causal_status`.
- Numerical magnitude mistaken for business materiality → separate task profile; no numerical reasoning score.
- Reasoning substituted for deterministic execution → enforce deterministic boundary.
- Silent registry override or undefined trigger → require trigger type/rule/evidence and existing QA review.
- Blocked method used as evidence or execution lineage lost → `blocked != executed` and unique `method_execution_id`.
- Conflicting methods silently reconciled → preserve contradiction, constrain claim, escalate if material.
- Full reasoning applied to routine work without trigger → compact runtime collapse.
- Anomaly mistaken for control exception → distinguish unusual observation from explicit rule violation.
- Aggregate reconciliation replacing entity-level unmatched analysis → identify concrete one-sided elements when material.
- Driver decomposition accepted without factor reconciliation → reconcile factor effects when applicable.
- Timing shift interpreted as economic effect → run timing validation for material cut-off candidates.
- Transformation artifact interpreted as source/business effect → trace `REPORT → MART → STAGE → RAW`.
- Leading indicator treated as causal predictor → use signal/association/risk language without causal evidence.
- Method catalog inflated by controls → require distinct question, execution, and material effect.
- Decision methods leaking from `[Thinking]` → keep trade-offs, reversibility, premortem, risk appetite, choice, and decision in `[Thinking]`.
- Reasoning-control loop mistaken for autonomous execution → keep it inside AES-governed scope, checks, bounded correction, stop, rollback, acceptance, and authority boundaries.
## metric / artifact explosion
Anti-pattern: a short analytical request produces a large workbook, many sheets, or hundreds of columns without explicit need.
## Legacy section: `ChatGPT/[Analytics]/Knowledge/SMOKE_QA_FOR_ANALYTICS.md`
## 8. short task / anti-bloat test
