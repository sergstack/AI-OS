# [Analytics] — Templates

## Purpose

Compact upload artifact for [Analytics] covering templates.

## Source files

- `ChatGPT/[Analytics]/Templates/ANALYSIS_RESPONSE_TEMPLATE.md`
- `ChatGPT/[Analytics]/Templates/DATA_CONTRACT_TEMPLATE.md`
- `ChatGPT/[Analytics]/Templates/MART_SPEC_TEMPLATE.md`
- `ChatGPT/[Analytics]/Templates/MEMO_TEMPLATE.md`
- `ChatGPT/[Analytics]/Templates/ANALYTICS_CONTEXT_PACK_TEMPLATE.md`
- `ChatGPT/[Analytics]/Templates/VARIANCE_ANALYSIS_PACK_TEMPLATE.md`
- `ChatGPT/[Analytics]/Templates/AUDIT_ANOMALY_IO_TEMPLATE.md`
- `ChatGPT/[Analytics]/Templates/FINANCE_MEMO_QA_CHECKLIST.md`
- `ChatGPT/[Analytics]/Templates/AP_P2P_CONTEXT_PACK.md`
- `ChatGPT/[Analytics]/Templates/AP_P2P_RISK_LIBRARY.md`
- `ChatGPT/[Analytics]/Templates/AP_P2P_EXCEPTION_REGISTER_TEMPLATE.md`
- `ChatGPT/[Analytics]/Templates/AP_P2P_AUDIT_FINDING_TEMPLATE.md`
- `ChatGPT/[Analytics]/Templates/AP_P2P_QA_CHECKLIST.md`
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


## From: `ChatGPT/[Analytics]/Templates/ANALYTICS_CONTEXT_PACK_TEMPLATE.md`

# Analytics Context Pack Template
Question:
Decision context:
Audience:
Data contract:
Grain:
Period:
Comparison period:
Filters:
Method:
Calculation tool:
Verified facts:
QA:
- Data contract, grain, period, filters, and exclusions explicit.
- Numeric calculations performed by deterministic tool; LLM arithmetic not used.
- Findings trace to verified facts, source mart, and evidence.
Limitations:
Acceptance:


## From: `ChatGPT/[Analytics]/Templates/VARIANCE_ANALYSIS_PACK_TEMPLATE.md`

# Variance Analysis Pack Template
Question:
Decision context:
Data contract:
Plan / baseline source:
Fact source:
Grain:
Period:
Comparison period:
Filters:
Method:
Calculation tool:
Variance table:
Drivers:
QA:
- Plan and fact sources identified.
- Period, grain, filters, and exclusions match across plan and fact.
- Variance calculations performed by deterministic tool; LLM arithmetic not used.
Limitations:
Acceptance:


## From: `ChatGPT/[Analytics]/Templates/AUDIT_ANOMALY_IO_TEMPLATE.md`

# Audit Anomaly Input / Output Template
Anomaly ID:
Question:
Decision context:
Data contract:
Expected behavior:
Grain:
Period:
Filters:
Anomaly threshold:
Method:
Calculation tool:
Output:
Finding:
Evidence:
Likely cause:
Risk:
Recommended action:
QA:
- Expected behavior, period, grain, filters, and threshold explicit.
- Detection calculations performed by deterministic tool; LLM arithmetic not used.
- Finding separated from likely cause and hypothesis.
Limitations:
Acceptance:


## From: `ChatGPT/[Analytics]/Templates/FINANCE_MEMO_QA_CHECKLIST.md`

# Finance Memo QA Checklist
Data contract:
- Source datasets, owner, refresh timestamp, required columns, metric rules, currency / units, and source mart listed.
Grain / period / filters:
- Grain, period, comparison period, filters, exclusions, and segment scope explicit.
Method:
- Method, source layer, output layer, and formula references stated.
- Numeric calculations performed by deterministic tool; LLM arithmetic not used.
Memo facts:
- Key numbers and deviations trace to verified Analytics facts.
- Risks have `risk_basis`; actions have owner, due date, and status.
QA:
- Totals, reconciliations, data quality status, and confidence visible.
Limitations:
Acceptance:
- Memo narrative is based only on verified Analytics facts.


## From: `ChatGPT/[Analytics]/Templates/AP_P2P_CONTEXT_PACK.md`

# Candidate AP/P2P Context Pack
Status: candidate template / checklist only.
Scope:
Data contract:
Source tables:
Key fields:
Grain / period / filters:
Risk scenarios:
- Vendor master: duplicate vendor identity, duplicate tax ID / registration ID, duplicate bank account, duplicate address / phone, inactive vendor with recent payment, new vendor with large first payment.
- Invoice: same vendor + same invoice number, same vendor + same amount + close dates, normalized invoice number match, invoice just below approval threshold, invoice without PO, invoice after payment.
- PO / receipt / invoice / payment: invoice before goods receipt, invoice amount above tolerance, payment without receipt, multiple invoices against same PO line, closed PO with new invoice.
- Payment: weekend / holiday payment, urgent / manual payment run, split payments, changed bank account before payment, payment to inactive / blocked vendor, large one-off payment.
Method:
Evidence rules:
- Use cautious audit wording only.
- DPO benchmark and penalty amount claims are `not found` / `needs evidence` unless separately supported.
- No real client, vendor, employee, bank, invoice, payment, tax ID, or personal data examples.
QA:
- Deterministic checks only; LLM arithmetic not used.
- Findings remain candidate exceptions until human review.
Limitations:
Human acceptance:


## From: `ChatGPT/[Analytics]/Templates/AP_P2P_RISK_LIBRARY.md`

# Candidate AP/P2P Risk Library
Status: candidate template / checklist only.
Usage rules:
- Treat every result as an `exception` or `risk indicator` until human review.
- Do not label fraud, misconduct, manipulation, or confirmed duplicate payment without separate evidence and human acceptance.
Risk scenario register:
| risk_id | area | risk scenario | source tables | key fields | deterministic check | false-positive check | exception output | QA status | confidence | limitation |
Areas:
- Vendor master
- Invoice
- PO / receipt / invoice / payment
- Payment
QA:
- Each risk scenario has source tables, key fields, deterministic checks, false-positive checks, cautious wording, QA status, confidence, and limitations.
Human acceptance:


## From: `ChatGPT/[Analytics]/Templates/AP_P2P_EXCEPTION_REGISTER_TEMPLATE.md`

# Candidate AP/P2P Exception Register Template
Status: candidate template / checklist only.
Scope:
Data contract:
Exception register:
| exception_id | risk_id | risk scenario | entity_id | document_id | amount | currency | period | grain | deterministic check | false-positive check | exception status | QA status | confidence | limitation | reviewer decision |
Evidence fields:
Exception status values:
- `exception`
- `risk indicator`
- `requires review`
- `possible duplicate`
- `potential control breach`
- `cleared false positive`
- `accepted finding`
QA:
- Facts are separated from assumptions and hypotheses.
- Confidence and limitations are visible.
Human acceptance:


## From: `ChatGPT/[Analytics]/Templates/AP_P2P_AUDIT_FINDING_TEMPLATE.md`

# Candidate AP/P2P Audit Finding Template
Status: candidate template / checklist only.
Finding header:
Scope:
Data contract:
Method:
Facts:
Interpretation:
Limitations:
- DPO benchmark: `not found` / `needs evidence`
- Penalty amount: `not found` / `needs evidence`
Recommended action:
Wording guardrail:
- Use cautious audit wording.
- Keep facts, assumptions, confidence, and limitations separate.
Human acceptance:


## From: `ChatGPT/[Analytics]/Templates/AP_P2P_QA_CHECKLIST.md`

# Candidate AP/P2P QA Checklist
Status: candidate template / checklist only.
Data contract:
Source tables and key fields:
Deterministic checks:
- Checks are reproducible by Python, SQL, spreadsheet formulas, or another deterministic project-standard tool.
- LLM arithmetic was not used.
False-positive checks:
Wording:
- Use cautious wording only.
- DPO benchmark and penalty amount claims are `not found` / `needs evidence` unless separately supported.
- No real client, vendor, employee, bank, invoice, payment, tax ID, or personal data examples.
Human acceptance:


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
