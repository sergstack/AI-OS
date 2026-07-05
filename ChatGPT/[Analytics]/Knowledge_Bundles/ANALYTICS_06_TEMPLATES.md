# [Analytics] — Templates

## Purpose

Compact upload artifact for [Analytics] covering templates.

## Source files

- `ChatGPT/[Analytics]/Templates/ANALYSIS_RESPONSE_TEMPLATE.md`
- `ChatGPT/[Analytics]/Templates/DATA_CONTRACT_TEMPLATE.md`
- `ChatGPT/[Analytics]/Templates/MART_SPEC_TEMPLATE.md`
- `ChatGPT/[Analytics]/Templates/MEMO_TEMPLATE.md`
- `ChatGPT/[Analytics]/Templates/CLAIM_EVIDENCE_REGISTRY_TEMPLATE.md`
- `ChatGPT/[Analytics]/Templates/EVIDENCE_CARD_TEMPLATE.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[Analytics]`.

## Status

- bundle_type: compact upload artifact
- source_of_truth: granular files listed above
- production_promotion: no, unless explicitly accepted elsewhere

---

# Content

## From: `ChatGPT/[Analytics]/Templates/ANALYSIS_RESPONSE_TEMPLATE.md`

# Analysis Response Template
```text
Mode:
Question / scope:
Data status:
Grain / period / filters:
Method:
Findings:
QA:
Limitations:
Decision / recommendation:
Next step:
```


## From: `ChatGPT/[Analytics]/Templates/DATA_CONTRACT_TEMPLATE.md`

# Data Contract Template
Owner:
Business owner:
Technical owner:
Required columns:
## Main files
## QA
required files:
required columns:


## From: `ChatGPT/[Analytics]/Templates/MART_SPEC_TEMPLATE.md`

# Mart Spec Template
mode:
field_budget:
visible_columns:
hidden_evidence_columns:
excluded_fields:
reason_for_each_extra_metric:
compact_front_view: yes/no
QA totals:
evidence fields:
## Required main mart files
## Slices


## From: `ChatGPT/[Analytics]/Templates/MEMO_TEMPLATE.md`

# Analytical Memo Template
## Executive summary
## Scope control
Mode:
Why this output size is sufficient:
What is intentionally excluded:
## Key numbers
| Metric | Value | Period | Source mart | QA status |
## Main deviations
| Item | Plan | Fact | Delta | ABS Delta | Row type | Confidence |
## Drivers / causes
## Risks
| Risk | Risk basis | Confidence | Action |
## Actions
| Action | Owner | Due date | Status | Evidence |
## Limitations
## Appendix / evidence


## From: `ChatGPT/[Analytics]/Templates/CLAIM_EVIDENCE_REGISTRY_TEMPLATE.md`

# Claim / Evidence Registry Template
| claim_id | claim_text | claim_type | source_mart | source_table_or_slice | metric | period | grain | filter | formula_or_method | evidence_id | qa_status | confidence | limitation | allowed_in_executive | review_status |
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


## From: `ChatGPT/[Analytics]/Templates/EVIDENCE_CARD_TEMPLATE.md`

# Evidence Card Template
evidence_id:
reconciliation_status:
dq_status:
qa_status:
confidence:
review_status:
