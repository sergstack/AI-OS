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
