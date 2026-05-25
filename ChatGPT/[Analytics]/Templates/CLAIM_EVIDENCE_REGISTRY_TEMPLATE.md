# Claim / Evidence Registry Template

| claim_id | claim_text | claim_type | source_mart | source_table_or_slice | metric | period | grain | filter | formula_or_method | evidence_id | qa_status | confidence | limitation | allowed_in_executive | review_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

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
