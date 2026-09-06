# Claim / Evidence Registry Template

| claim_id | hypothesis_id | claim_text | claim_type | method_execution_id | method_status | source_mart | source_table_or_slice | metric | period | grain | filter | baseline | formula_or_method | evidence_id | alternative_explanations | contradicting_evidence | discriminating_evidence | falsification_test | generalization_scope | generalization_evidence | qa_status | confidence | claim_support | causal_status | limitation | allowed_in_executive | review_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

## Claim types

- DATA FACT
- CALCULATION RESULT
- INTERPRETATION
- RECOMMENDATION
- HYPOTHESIS
- LIMITATION
- BLOCKER

## Rules

- No management conclusion without evidence_id.
- No risk without risk_basis.
- No action without owner / due date / status.
- Low confidence cannot be presented as confirmed cause.
- Executive claims must trace to `mart_main_tz` / `mart_main_compact`.
- Deep claims must trace to `mart_main_full`.
- `formula_or_method` is human-readable and does not replace `method_execution_id`.
- Required lineage is claim → `method_execution_id` → executed method → source mart/table/slice → metric/period/grain/filter/baseline → evidence.
- A claim requiring an actual method result cannot use `method_status = blocked / planned / not_needed` as supporting evidence.
- `confidence` (`high / medium / low`), `claim_support` (`SUPPORTED / PARTIALLY_SUPPORTED / HYPOTHESIS / UNSUPPORTED`), and `causal_status` (`not_applicable / association_only / explanation_supported / causal_evidence`) are independent.
- Claim strength must not exceed final evidence sufficiency. Driver evidence alone does not establish root cause.
- `generalization_scope` states the observed and claimed period/population boundary. `generalization_evidence` is required before one-period evidence is generalized as systemic, non-systemic, structural, persistent, recurring, isolated, or one-off.

## Mandatory Headline Claim Gate

For `analytical_depth = material / decision_critical`, every headline claim
requires a registry row with complete lineage: headline claim -> claim
registry row -> `method_execution_id` -> `method_status = executed` (aligned
with `ANALYTICAL_REASONING_STANDARD.md` `METHOD_PLAN.execution_status`) ->
source mart/table/slice -> metric/period/grain/filter/baseline ->
`evidence_id` -> `claim_support` -> `causal_status` -> `confidence` ->
`generalization_scope` -> `qa_status`.

```text
lineage missing -> allowed_in_executive = no
```

Do not promote a claim beyond its evidence:

- `observation -> cause` requires causal evidence, not association alone.
- `contribution -> supported explanation` may rely on discriminating /
  alternative-explanation evidence (competing explanations tested and
  ruled out); a quantified contribution alone, with no discriminating
  evidence, supports at most "main quantified contributor within observed
  scope".
- `supported explanation -> root cause` requires causal evidence or a
  causal-capable analytical design (`causal_status = causal_evidence`) —
  alternative-explanation evidence alone does not reach `root cause`.
- `association -> causation` requires `causal_status = causal_evidence`.
- `single-period -> systemic / recurring / persistent` requires
  `generalization_evidence`.

`method_status = blocked / planned / not_needed` can never support a claim
(`blocked != executed`). Narrative claim strength (memo/executive wording)
must not exceed `FINAL_EVIDENCE_SUFFICIENCY.maximum_claim_strength`. This
gate is the claim-level (Gate 2) checkpoint; it does not replace Gate 1
(data/calculation correctness) or Gate 3 (narrative wording), and it is read,
not reimplemented, by the Analytical Judge (`ANALYTICAL_REASONING_STANDARD.md`
§8) and the memo/narrative QA (`MEMO_PIPELINE.md`, `MEMO_RUBRIC.md`).

## `RECOMMENDATION` row evidence (P1-B, issue #449, standard, active — promoted 2026-09-06, see `docs/evidence/ANALYTICS_P1_PROMOTION_2026-09-06.md`)

A registry row with `claim_type = RECOMMENDATION` for `analytical_depth =
material / decision_critical` links to a `RECOMMENDATION_EVIDENCE` record
(`ANALYTICAL_REASONING_STANDARD.md` §16.2) via `claim_id`; no new column is
added to this template. `claim_support` for such a row cannot be
`SUPPORTED` while `RECOMMENDATION_EVIDENCE.recommendation_status` is
`pilot_candidate` or `hypothesis` —

```text
diagnostic evidence != intervention evidence
```

— a proven `problem_evidence` does not raise `claim_support` for the
`RECOMMENDATION` row above the recorded `recommendation_status`. Where the
recommendation proposes a targeted (entity-specific) intervention,
`generalization_scope` / `generalization_evidence` for that row must reflect
the §16.3 `stability_check` result (rotating Top-N does not support a
targeted-entity `generalization_scope`). Where the recommendation proposes a
forecasting/planning-method change, `evidence_id` must reference the §16.4
`FORECAST_METHOD_COMPARISON`, not the diagnostic finding alone. Promoted to
standard, active status 2026-09-06 (owner-authorized); see
`docs/evidence/ANALYTICS_P1_PROMOTION_2026-09-06.md`.
