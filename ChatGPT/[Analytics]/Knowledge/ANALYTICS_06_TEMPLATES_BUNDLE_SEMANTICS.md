# Migrated Bundle Semantics

Canonical source created during Issue #285 provenance migration.
Legacy bundle provenance: `ChatGPT/[Analytics]/Knowledge_Bundles/ANALYTICS_06_TEMPLATES.md`.

## Legacy section: `ChatGPT/[Analytics]/Templates/ANALYTICS_CONTEXT_PACK_TEMPLATE.md`

Data contract:
Method:
Verified facts:
QA:
- Data contract, grain, period, filters, and exclusions explicit.
- Numeric calculations performed by deterministic tool; LLM arithmetic not used.
- Findings trace to verified facts, source mart, and evidence.
Limitations:
Acceptance:

## Legacy section: `ChatGPT/[Analytics]/Templates/VARIANCE_ANALYSIS_PACK_TEMPLATE.md`

Data contract:
Materiality absolute/relative/zero-plan/contribution rules:
Selected/excluded population and selection coverage:
Method:
Source formula/sign; economic direction rule; raw variance:
Normalized management variance and resolution status:
Variance table with primary attribution and non-additive attributes:
Gross adverse/favorable/net bridge and reconciliation:
Economic/timing/data-mapping/unresolved attribution and residual:
Gross classification population, denominator, classified/unclassified movement, coverage, row counts:
Drivers:
Generalization scope/evidence:
Reported view; adjusted view with explicit polarity and reconciliation:
QA:
- Plan and fact sources identified.
- Period, grain, filters, and exclusions match across plan and fact.
- Variance calculations performed by deterministic tool; LLM arithmetic not used.
- Raw/source and normalized management signs are explicit and not mixed.
- Gross/net and primary attribution reconcile; favorable offset is explicit when driver exceeds net.
- Coverage uses eligible gross absolute movement, not net variance.
- Unsupported controllability/recurrence/generalization remain unknown/not established.
- Reported result remains visible and adjusted polarity is explicit.
Limitations:
Acceptance:

## Legacy section: `ChatGPT/[Analytics]/Templates/AUDIT_ANOMALY_IO_TEMPLATE.md`

Data contract:
Method:
Output:
QA:
- Expected behavior, period, grain, filters, and threshold explicit.
- Detection calculations performed by deterministic tool; LLM arithmetic not used.
- Finding separated from likely cause and hypothesis.
Limitations:
Acceptance:

## Legacy section: `ChatGPT/[Analytics]/Templates/FINANCE_MEMO_QA_CHECKLIST.md`

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

## Legacy section: `ChatGPT/[Analytics]/Templates/AP_P2P_CONTEXT_PACK.md`

Scope:
Data contract:
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

## Legacy section: `ChatGPT/[Analytics]/Templates/AP_P2P_RISK_LIBRARY.md`

Usage rules:
Risk scenario register:
Areas:
- Vendor master
- Invoice
- PO / receipt / invoice / payment
- Payment
QA:
- Each risk scenario has source tables, key fields, deterministic checks, false-positive checks, cautious wording, QA status, confidence, and limitations.
Human acceptance:

## Legacy section: `ChatGPT/[Analytics]/Templates/AP_P2P_EXCEPTION_REGISTER_TEMPLATE.md`

Scope:
Data contract:
Exception register:
Evidence fields:
Exception status values:
QA:
- Facts are separated from assumptions and hypotheses.
- Confidence and limitations are visible.
Human acceptance:

## Legacy section: `ChatGPT/[Analytics]/Templates/AP_P2P_AUDIT_FINDING_TEMPLATE.md`

Finding header:
Scope:
Data contract:
Method:
Facts:
Interpretation:
Limitations:
Recommended action:
Wording guardrail:
Human acceptance:

## Legacy section: `ChatGPT/[Analytics]/Templates/AP_P2P_QA_CHECKLIST.md`

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

## Legacy section: `ChatGPT/[Analytics]/Templates/CLAIM_EVIDENCE_REGISTRY_TEMPLATE.md`

- `formula_or_method` does not replace `method_execution_id`.
- Lineage: claim → executed method → source mart/table/slice → metric/period/grain/filter/baseline → evidence.
- Blocked/planned/not-needed executions cannot support a claim requiring a method result.
- `confidence`, `claim_support`, and `causal_status` are independent; claim strength cannot exceed evidence sufficiency.
- Scope/evidence is required before one-period evidence is generalized as systemic, non-systemic, structural, persistent, recurring, isolated, or one-off.
