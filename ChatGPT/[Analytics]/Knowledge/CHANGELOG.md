# Changelog

## 2026-09-06 — analytics-eda-claim-calibration (issue #451)

Regression/calibration review, not a new controls framework. `owner review
required` before any promotion decision; this entry does not itself
authorize production adoption, merge, deployment, or Project sync.

Added:

- `GOVERNANCE_AND_ANTI_PATTERNS.md`: "EDA-to-claim calibration additions
  (issue #451)" — 7 new rows in the existing P0 failure-mode table naming
  narrow, previously-ambiguous instances of existing controls (observed
  rating != quality/preference; model residual != market
  inefficiency/fair-value; definition != manufactured evidence; selected
  reviews/volume != guarantee/expertise; listed price != current
  price/availability; reviewer confound requires common-support check
  before normalization; in-sample association != measured predictive
  performance). No new field, taxonomy, method, or gate.
- `SMOKE_QA_FOR_ANALYTICS.md`: new case 15 (9 scenarios) covering the 10-row
  acceptance-criteria table from issue #451 across three fixture families
  (WineMag wording, a CFO/audit transfer variant reusing case 14 scenario
  C's pattern, and a routine positive-control/routing fixture). Paper-trace
  scenarios only; no live model run.
- `package_manifest.json`: repaired a genuine completeness gap —
  `Templates/METRIC_DEFINITION_CARD_TEMPLATE.md` (present in `Knowledge/MANIFEST.md`
  and the canonical `knowledge_bundle_manifest.json` bundle sources since
  issue #439, but missing from this project's own file list) plus three
  more recently-added files that had the same gap
  (`AUTORESEARCH_STOCHASTICITY_NONINFERIORITY_METHOD.md`,
  `P1_PILOT_EVIDENCE_2026-09-06.md`, `P1_449_PILOT_EVIDENCE_2026-09-06.md`)
  and this review's own new evidence file.
- Evidence packet: `EDA_CLAIM_CALIBRATION_REVIEW_2026-09-06.md` — R1–R6
  mapping table (observed failure pattern -> existing owning rule ->
  reproduction/trace evidence -> smallest justified correction -> required
  regression check), 10-scenario paper-trace result, and the manifest
  finding.

Not changed: `ANALYTICAL_TECHNIQUES.md` (byte-identical to `origin/main`),
`ANALYSIS_CONTINUATION_GATE` (§15.3, untouched, remains deferred), the
22-method registry, `confidence: high/medium/low`, any Analytics enum, and
`PROJECT_INSTRUCTIONS.md` (near its length ceiling; all additions placed in
`Knowledge/`).

## 2026-09-06 — analytics-p1-recommendation-evidence (issue #449)

Bounded pilot only. `owner review required` before any promotion decision;
this entry does not itself authorize production adoption, merge, deployment,
or Project sync.

Added:

- Strengthened material Explanation Challenge (`ANALYTICAL_REASONING_STANDARD.md`
  §16.1) — a material explanatory/intervention-oriented statement requires a
  recorded `DISCRIMINATING_TEST_STATUS: executed / blocked / unavailable`;
  contribution + recurrence alone cannot support it. Reuses existing
  `alternative_explanation_test`, `CONTRADICTING_EVIDENCE`,
  `DISCRIMINATING_EVIDENCE`, `FALSIFICATION_TEST`, `FINAL_EVIDENCE_SUFFICIENCY`.
- `RECOMMENDATION_EVIDENCE` (§16.2, CONTROL, not a method) — compact record
  for material management recommendations; required invariant `diagnostic
  evidence != intervention evidence`; an untested intervention caps
  `recommendation_status <= pilot_candidate`. Read by the Analytical Judge
  (§8 check 7) and `MEMO_PIPELINE.md`'s management-implication section.
- Material stability/persistence check (`stability_check`, §16.3) — extends
  `generalization_scope` / `generalization_evidence` and
  `RECURRENCE_CLASSIFICATION`; distinguishes stable from rotating
  concentration before a targeted-redesign recommendation.
- Out-of-sample validation for forecasting/planning-method change
  recommendations (`FORECAST_METHOD_COMPARISON`, §16.4) — requires an
  out-of-sample, comparable-scope, same-metric-definition comparison with a
  monetary-error metric and a frequency/corridor-accuracy metric where
  applicable, before a strong method-change recommendation. Reuses
  `forecast_to_period_end`, `sensitivity_analysis`, `robustness_to_baseline`,
  and existing backtesting logic; no `backtest` `METHOD_ID` created.
- Economic vs process diagnosis boundary — `effect_type` classification
  (§16.5, `VARIANCE_DIAGNOSTIC_CONTRACT.md` Accountability boundary) — names
  the rule `a financial pattern alone cannot establish a process failure`;
  `process_control` requires process evidence, not a financial pattern
  alone. Reuses existing primary-attribution categories, `data_layer_check`,
  `timing_validation`, `exception_analysis`.
- `what_would_change_the_view` (§16.6) — compact named field for material
  executive output, formalizing the existing `ACCEPTANCE_CRITERIA.md` /
  `QA_CHECKLIST.md` prose criterion.
- QA_CHECKLIST.md: new "Recommendation evidence, stability, and
  out-of-sample validation (P1-B, issue #449, bounded pilot)" section (8
  checklist items). SMOKE_QA_FOR_ANALYTICS.md: new case 14 with the five
  scenarios (A–E) from issue #449.
- Pilot evidence packet: 5-scenario OLD-vs-NEW result matrix, per-element
  recommendation with differentiated confidence, incremental catches, false
  blocks, regressions, rollback status
  (`Knowledge/P1_449_PILOT_EVIDENCE_2026-09-06.md`).

Constraints preserved:

- 22-method registry not expanded; no new `METHOD_ID`; no new analytical
  intent (`ANALYTICAL_TECHNIQUES.md` unchanged, verified by diff against
  `origin/main`).
- All six elements stay CONTROL/field-level additions, not methods; none
  appears in the registry table.
- No second Judge, no second QA framework, no autonomous retry/
  self-improvement loop introduced.
- `ANALYSIS_CONTINUATION_GATE` (§15.3, issue #445) is untouched and remains
  **deferred, not activated** — this issue's scope explicitly forbids
  reviving it without new pilot evidence, and none was introduced.
- `blocked != executed` is not weakened.
- Active analytical intents are unchanged.
- Routine/quick path (§9) is unaffected; all six elements carry an explicit
  material activation trigger and do not instantiate without it (smoke QA
  case 14, scenario E).
- All changes stayed inside `ChatGPT/[Analytics]/**`.

Status:

```text
production_ready: not claimed
promotion: owner review required (not decided by this pilot)
gate_verdict: see Knowledge/P1_449_PILOT_EVIDENCE_2026-09-06.md
```

## 2026-09-06 — analytics-p1-comparative-integrity (issue #445)

Bounded pilot only. `owner review required` before any promotion decision;
this entry does not itself authorize production adoption, merge, deployment,
or Project sync.

Added:

- Activated `POPULATION_CONTRACT` (CONTROL/CONTRACT) — full field list and
  required behavior (`ANALYTICAL_REASONING_STANDARD.md` §15.1,
  `Templates/METRIC_DEFINITION_CARD_TEMPLATE.md`). Extends, does not replace,
  §5's `population_constant_or_explained?` /
  `denominator_constant_or_explained?` / `scope_change_quantified?`.
- Activated `RECONCILIATION_CONTRACT` (CONTROL/CONTRACT) — full field list
  distinguishing amount/row-count/matched-population/identity-mapping/
  classification-coverage integrity dimensions
  (`ANALYTICAL_REASONING_STANDARD.md` §15.2, `DATA_CONTRACTS.md`). Wraps
  existing `reconciliation` / `unmatched_elements_analysis` /
  `factor_reconciliation` / `unexplained_residual` methods; no new
  `METHOD_ID`.
- `ANALYSIS_CONTINUATION_GATE` (ROUTING/WORKFLOW CONTROL) evaluated and
  **deferred, not activated** — the pilot found no incremental catch over
  §10's existing stop/escalation rules on any traced scenario
  (`ANALYTICAL_REASONING_STANDARD.md` §15.3). The CONTINUE/STOP/BLOCK/HANDOFF
  field design is retained as a documented extension point only; §10 alone
  remains the live continuation/stopping control.
- `HELD_OUT_TRANSFER_EVAL` (QA/EVAL only, not a method) — six required lanes:
  `known_regression_cases`, `held_out_cases`, `shifted_domain_cases`,
  `boundary_cases`, `contradictory_evidence_cases`,
  `old_p0_regression_cases` (`QA_CHECKLIST.md`). New smoke QA case 13
  (`SMOKE_QA_FOR_ANALYTICS.md`) covering held-out population semantics
  shift, held-out reconciliation semantics shift, and old-P0 compact
  regression protection.
- Pilot evidence packet: 10-scenario P0-baseline-vs-P1-candidate result
  matrix, known-vs-held-out results reported separately, per-element
  recommendation, rollback status
  (`Knowledge/P1_PILOT_EVIDENCE_2026-09-06.md`).

Constraints preserved:

- 22-method registry not expanded; no new `METHOD_ID`; no new analytical
  intent (`ANALYTICAL_TECHNIQUES.md` unchanged, verified by diff against
  `origin/main`).
- `POPULATION_CONTRACT` / `RECONCILIATION_CONTRACT` stay CONTROL/CONTRACT and
  are the only P1 controls activated by this pilot; `ANALYSIS_CONTINUATION_GATE`
  stays classified ROUTING/WORKFLOW CONTROL but is deferred/not activated;
  `HELD_OUT_TRANSFER_EVAL` stays QA/EVAL.
- Analytical Judge (§8), deterministic-first boundary, `blocked != executed`,
  and §9 compact runtime collapse remain authoritative and unchanged.
- All changes stayed inside `ChatGPT/[Analytics]/**`.

Status:

```text
production_ready: not claimed
promotion: owner review required (not decided by this pilot)
gate_verdict: see Knowledge/P1_PILOT_EVIDENCE_2026-09-06.md
```

## 2026-09-05 — analytics-p0-semantic-contracts (issue #439)

Added:

- `METRIC_DEFINITION_CARD` — canonical semantic definition card for
  material/flagship/ratio-like metrics (`Templates/METRIC_DEFINITION_CARD_TEMPLATE.md`,
  referenced from `DATA_CONTRACTS.md`, `ANALYTICAL_REASONING_STANDARD.md` §11,
  `MAIN_FILES_STANDARD.md`, `QA_CHECKLIST.md`, `ACCEPTANCE_CRITERIA.md`). A
  formula alone is not a sufficient metric definition; an unresolved material
  metric definition blocks a strong management conclusion.
- Canonical `VALUE_STATE` vocabulary (`KNOWN`/`UNKNOWN`/`NOT_REPORTED`/
  `NOT_APPLICABLE`/`PARSE_FAILED`/`MISSING_SOURCE`/`UNMATCHED`/`BLOCKED`) with
  its invariants, defined in `DATA_CONTRACTS.md` and referenced from
  `MAIN_FILES_STANDARD.md`, `ANALYTICAL_REASONING_STANDARD.md` §12,
  `DATA_CONTRACT_TEMPLATE.md`, `MART_SPEC_TEMPLATE.md`,
  `EVIDENCE_CARD_TEMPLATE.md`, `QA_CHECKLIST.md`, and `ACCEPTANCE_CRITERIA.md`.
  `RAW -> STAGE -> MART` must not collapse materially different states into a
  generic null.
- Mandatory Headline Claim Gate (`ANALYTICAL_REASONING_STANDARD.md` §13,
  `CLAIM_EVIDENCE_REGISTRY_TEMPLATE.md`): for `analytical_depth = material /
  decision_critical`, every headline claim requires complete registry
  lineage or `allowed_in_executive = no`. Enforces
  `observation -> cause`, `contribution -> root cause`,
  `association -> causation`, and `single-period -> systemic / recurring /
  persistent` are never promoted without the required evidence level.
- Explicit "Three control gates" documentation (`ANALYTICAL_REASONING_STANDARD.md`
  §14, `GOVERNANCE_AND_ANTI_PATTERNS.md`): Gate 1 (data/calculation), Gate 2
  (analytical claim), Gate 3 (narrative) named as already-implemented,
  distinct mechanics; `DATA VALID != CLAIM SUPPORTED != NARRATIVE ACCEPTABLE`.
- P1 design-only extension-point notes (not implemented in this version):
  `POPULATION_CONTRACT`, `RECONCILIATION_CONTRACT`,
  `ANALYSIS_CONTINUATION_GATE` (`ANALYTICAL_REASONING_STANDARD.md` §15,
  `METRIC_DEFINITION_CARD_TEMPLATE.md`).
- Smoke QA case 12 covering the five P0 failure modes: ambiguous metric,
  uncertainty collapse, contribution vs root cause, single-period
  generalization, headline without lineage (`SMOKE_QA_FOR_ANALYTICS.md`).

Updated:

- `MEMO_PIPELINE.md` and `MEMO_RUBRIC.md` to tie the narrative gate to the
  Headline Claim Gate (`allowed_in_executive`).
- `Templates/DATA_CONTRACT_TEMPLATE.md`, `Templates/MART_SPEC_TEMPLATE.md`,
  `Templates/EVIDENCE_CARD_TEMPLATE.md` with `VALUE_STATE` /
  `METRIC_DEFINITION_CARD` reference fields.
- `MANIFEST.md` and `knowledge_bundle_manifest.json` to register
  `Templates/METRIC_DEFINITION_CARD_TEMPLATE.md`; `Knowledge_Bundles/`
  rebuilt only via `scripts/build_knowledge_bundles.py --write`.

Constraints preserved:

- 22-method registry not expanded; no new `METHOD_ID`.
- No new/parallel QA framework; existing Analytical Judge and Quantitative
  Sanity Gate semantics unchanged.
- `driver != root cause` and `claim strength <= final evidence sufficiency`
  strengthened, not weakened.
- `quick`-mode runtime collapse unchanged.
- `[Analytics]` / `[Thinking]` boundary unchanged (trade-offs, risk appetite
  stay in `[Thinking]`).

Status:

```text
production_ready: not claimed
pilot_case_required: yes
smoke_qa_status: pass (new case 12 added; full suite not independently re-run as human pilot)
```

## 2026-09-02 — analytical-judge-gate (issue #357)

Added:

- Explicit `Analytical Judge` gate as `ANALYTICAL_REASONING_STANDARD.md` §8: a
  compact post-findings orchestration checkpoint (`findings → Analytical Judge
  → pass / revise / blocked → final findings → memo`). Seven semantic checks
  mapped to existing controls; compact `ANALYTICAL_JUDGE` output record;
  bounded revise/rerun rule; `quick` runtime collapse. No new QA framework,
  taxonomy, method, or intent; §8→§9, §9→§10 renumbered.

Updated:

- `ANALYTICS_WORKFLOW.md` canonical workflow and Step 9 to make the gate
  explicit before memo/report.
- `QA_CHECKLIST.md` with a post-findings Analytical Judge gate block
  (orchestration, not a second framework).
- `ACCEPTANCE_CRITERIA.md` with criterion 12, `analytical_judge_status`, and a
  blocked-status entry.
- `GOVERNANCE_AND_ANTI_PATTERNS.md` with the gate principle, a blocker entry,
  and anti-pattern rows (no autonomous retry loop, no second framework,
  `blocked != executed`).
- `SMOKE_QA_FOR_ANALYTICS.md` with a case forcing a plausible over-strong
  "root cause" claim to `revise`, plus a `quick`-mode collapse case.

Status:

```text
production_ready: not claimed
pilot_case_required: yes
smoke_qa_status: pass
```

## 2026-05-25 — analytics-project-settings-minor-fix

Added:

- Canonical GitHub path note in README.
- Do-not-upload guidance for ChatGPT project knowledge.
- Claim / evidence registry template.
- Evidence card template.
- Memo rubric.

Updated:

- Knowledge manifest to include the rubric and new templates.
- package manifest to match the documented package inventory.
- Smoke QA result note to reflect the minor-fix pass.

Status:

```text
production_ready: not claimed
pilot_case_required: yes
```

## 2026-05-21 — analytics-project-settings-full-v1

Added:

- In-project analysis mode.
- Main files standard.
- Mandatory `stage_main_full`.
- Mandatory `mart_main_full`.
- Mandatory `mart_main_tz/compact`.
- Rule that mart slices derive from `mart_main_full`.
- Compact/full JSON input logic.
- Chart selection standard.
- Analytical memo MVP structure.
- Word/DOCX report standard.
- Text QA and style standard.
- Codex task packets by controlled parts.
- Smoke QA for Analytics.
- Smoke QA result recorded.

Updated:

- Routing to prevent premature handoff.
- Acceptance criteria with main file checks.
- QA checklist with main file and chart checks.

Status:

```text
ready_to_upload: yes
production_ready: not claimed
smoke_qa_status: pass
requires_pilot_case: yes
```
