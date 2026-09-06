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
- `ChatGPT/[Analytics]/Templates/METRIC_DEFINITION_CARD_TEMPLATE.md`
- `ChatGPT/[Analytics]/Knowledge/ANALYTICS_06_TEMPLATES_BUNDLE_SEMANTICS.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[Analytics]`.

## Status

- production_promotion: no, unless explicitly accepted elsewhere
- bundle_type: generated compact upload artifact
- source_of_truth: declared granular source files
- source_fingerprint: sha256:ef697b66cc31e6fc21c61429b51acfba6f77d82b0d1235acadbefb517eaba47a
- generator: scripts/build_knowledge_bundles.py

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
Dataset:
Owner:
Business owner:
Technical owner:
Source:
Refresh frequency:
Load timestamp:
Period:
Grain:
Primary keys:
Foreign keys:
Required columns:
Optional columns:
Column types:
Allowed values:
Date logic:
Currency / units:
Null policy (use canonical VALUE_STATE: KNOWN/UNKNOWN/NOT_REPORTED/NOT_APPLICABLE/PARSE_FAILED/MISSING_SOURCE/UNMATCHED/BLOCKED):
Duplicate policy:
Freshness rule:
Mapping rules:
Join rules:
Metric rules:
Metric definition cards (material/flagship/ratio-like metrics): see Templates/METRIC_DEFINITION_CARD_TEMPLATE.md
Classification rules:
Validation checks:
Known limitations:
Expected outputs:
## Main files
stage_main_full:
mart_main_full:
mart_main_tz / compact:
## QA
required files:
required columns:
reconciliation:
known blockers:

## From: `ChatGPT/[Analytics]/Templates/MART_SPEC_TEMPLATE.md`

# Mart Spec Template
mart_name:
business purpose:
audience:
grain:
period:
keys:
mode:
field_budget:
visible_columns:
hidden_evidence_columns:
excluded_fields:
reason_for_each_extra_metric:
compact_front_view: yes/no
source stage files:
source stage main file:
metrics:
formulas:
metric_definition_cards (material/flagship/ratio-like): see Templates/METRIC_DEFINITION_CARD_TEMPLATE.md
dimensions:
classifiers:
filters:
QA totals:
evidence fields:
value_state_preserved: yes/no (VALUE_STATE not collapsed to generic null where material)
limitations:
## Required main mart files
mart_main_full:
mart_main_tz / compact:
## Slices
| slice_name | source_mart | filter_logic | grain | metrics | purpose |
|---|---|---|---|---|---|
| | mart_main_full | | | | |

## From: `ChatGPT/[Analytics]/Templates/MEMO_TEMPLATE.md`

# Analytical Memo Template
## Executive summary
Verdict:
Key numbers:
Decision needed:
## Scope control
Mode:
Why this output size is sufficient:
What is intentionally excluded:
## Key numbers
| Metric | Value | Period | Source mart | QA status |
|---|---:|---|---|---|
## Main deviations
| Item | Plan | Fact | Delta | ABS Delta | Row type | Confidence |
|---|---:|---:|---:|---:|---|---|
## Drivers / causes
Confirmed causes:
Hypotheses:
## Risks
| Risk | Risk basis | Confidence | Action |
|---|---|---|---|
## Actions
| Action | Owner | Due date | Status | Evidence |
|---|---|---|---|---|
## Limitations
## Appendix / evidence
source_mart_full:
source_mart_compact:
charts:

## From: `ChatGPT/[Analytics]/Templates/ANALYTICS_CONTEXT_PACK_TEMPLATE.md`

# Analytics Context Pack Template
## Scope
Question:
Decision context:
Audience:
Owner:
Expected output:
## Data contract
Source datasets:
Source owner:
Refresh timestamp:
Required columns:
Primary keys:
Join keys:
Currency / units:
Metric rules:
## Grain / period / filters
Grain:
Period:
Comparison period:
Filters:
Exclusions:
Segmentation:
## Method
Workflow step:
Source layer:
Output layer:
Calculation tool:
Method summary:
Formula references:
## Verified facts
| fact_id | fact | metric | period | grain | source_mart | evidence_id | QA status |
|---|---|---|---|---|---|---|---|
## QA
- [ ] Data contract is complete enough for the requested output.
- [ ] Grain, period, filters, and exclusions are explicit.
- [ ] Numeric calculations were performed by Python, SQL, spreadsheet formulas, or another deterministic project-standard tool.
- [ ] LLM arithmetic was not used.
- [ ] Findings trace to verified facts, source mart, and evidence.
## Limitations
Known blockers:
Coverage gaps:
Data quality notes:
Assumptions:
## Acceptance
- [ ] Context pack can support the requested analysis or memo.
- [ ] Unsupported claims are marked as assumptions, hypotheses, limitations, or blockers.
- [ ] Next run trigger is clear.

## From: `ChatGPT/[Analytics]/Templates/VARIANCE_ANALYSIS_PACK_TEMPLATE.md`

# Variance Analysis Pack Template
## Scope
Question:
Decision context:
Audience:
Owner:
Expected output:
## Data contract
Source datasets:
Source owner:
Refresh timestamp:
Required columns:
Metric rules:
Plan / baseline source:
Fact source:
Currency / units:
## Grain / period / filters
Grain:
Period:
Comparison period:
Filters:
Exclusions:
Materiality threshold:
Relative threshold and denominator:
Zero-plan rule:
Contribution basis and threshold:
Selected / excluded population:
Selection coverage:
## Method
Source layer:
Output layer:
Variance method:
Ranking method:
Calculation tool:
Formula references:
## Sign convention
Source variance formula:
Source sign convention:
Economic direction rule (`higher_is`):
Raw variance:
Normalized management variance (`positive = adverse`, `negative = favorable`):
Normalization status (`resolved / unresolved`):
## Variance table
| item | plan | fact | source_variance | normalized_management_variance | abs_movement | delta_pct | primary_attribution | budget_status | controllability | recurrence | evidence_status | period | grain | source_mart | QA status |
|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|---|---|---|---|
## Gross bridge and attribution
Gross adverse movement:
Gross favorable movement:
Normalized net management variance:
Economic effect:
Timing / cutoff effect:
Data / mapping effect:
Unresolved effect:
Reconciliation residual:
Reconciliation status:
## Classification coverage
Population basis:
Eligible gross movement:
Classified gross movement:
Unclassified gross movement:
Coverage percentage:
Total / classified / unknown row counts:
## Drivers
Confirmed drivers:
Hypotheses:
Unexplained variance:
Generalization scope and evidence:
## Reported / adjusted view
Official Plan / Fact / variance:
Reported normalized management variance:
Adjustments with explicit `increases_adverse / reduces_adverse` direction:
Adjusted management variance:
## QA
- [ ] Plan and fact sources are identified.
- [ ] Period, grain, filters, and exclusions match across plan and fact.
- [ ] Totals reconcile before variance interpretation.
- [ ] Variance, absolute variance, and percentage variance were calculated by Python, SQL, spreadsheet formulas, or another deterministic project-standard tool.
- [ ] LLM arithmetic was not used.
- [ ] Confirmed drivers are separated from hypotheses.
- [ ] Source/raw sign and normalized management direction are explicit and not mixed.
- [ ] Gross adverse plus gross favorable reconciles to normalized net variance.
- [ ] Primary attribution is mutually exclusive, exhaustive within scope, and reconciled.
- [ ] Classification coverage uses eligible gross absolute movement, not net variance.
- [ ] Controllability and recurrence have traceable evidence or remain `unknown`.
- [ ] Single-period evidence is not generalized as systemic/non-systemic.
- [ ] Reported result remains visible; adjusted polarity is explicit.
## Limitations
Known blockers:
Coverage gaps:
Timing issues:
Mapping issues:
Assumptions:
## Acceptance
- [ ] Top deviations are ranked by materiality.
- [ ] Every driver or risk has evidence.
- [ ] Recommendations do not exceed verified variance facts.
- [ ] Secondary management attributes are not summed as causes.
- [ ] A material driver exceeding net variance has an explicit favorable offset.

## From: `ChatGPT/[Analytics]/Templates/AUDIT_ANOMALY_IO_TEMPLATE.md`

# Audit Anomaly Input / Output Template
## Input
Anomaly ID:
Question:
Decision context:
Owner:
Expected output:
## Data contract
Source datasets:
Source owner:
Refresh timestamp:
Required columns:
Primary keys:
Join keys:
Expected behavior:
Metric rules:
Currency / units:
## Grain / period / filters
Grain:
Period:
Comparison period:
Filters:
Exclusions:
Anomaly threshold:
## Method
Source layer:
Output layer:
Detection method:
Comparison method:
Calculation tool:
Formula references:
## Output
Finding:
Evidence:
Likely cause:
Risk:
Recommended action:
Owner:
Due date:
Confidence:
## Anomaly evidence table
| anomaly_id | entity | metric | observed_value | expected_value | delta | period | grain | source_mart | evidence_id | QA status |
|---|---|---|---:|---:|---:|---|---|---|---|---|
## QA
- [ ] Expected behavior is explicit.
- [ ] Period, grain, filters, and threshold are explicit.
- [ ] Detection calculations were performed by Python, SQL, spreadsheet formulas, or another deterministic project-standard tool.
- [ ] LLM arithmetic was not used.
- [ ] Finding is separated from likely cause and hypothesis.
- [ ] Risk has a risk basis and evidence.
## Limitations
Known blockers:
Coverage gaps:
False-positive risks:
Assumptions:
## Acceptance
- [ ] Anomaly output can be traced to source mart, evidence, period, and grain.
- [ ] Unsupported causes remain hypotheses.
- [ ] Recommended action is bounded by verified evidence.

## From: `ChatGPT/[Analytics]/Templates/FINANCE_MEMO_QA_CHECKLIST.md`

# Finance Memo QA Checklist
## Scope
Memo title:
Decision context:
Audience:
Owner:
Expected output:
## Data contract
- [ ] Source datasets are listed.
- [ ] Source owner and refresh timestamp are listed.
- [ ] Required columns and metric rules are listed.
- [ ] Currency / units are explicit.
- [ ] Source mart or compact mart is listed.
## Grain / period / filters
- [ ] Grain is explicit.
- [ ] Period and comparison period are explicit.
- [ ] Filters and exclusions are explicit.
- [ ] Segment or entity scope is explicit.
## Method
- [ ] Method is stated.
- [ ] Source layer and output layer are stated.
- [ ] Formula references are included where relevant.
- [ ] Numeric calculations were performed by Python, SQL, spreadsheet formulas, or another deterministic project-standard tool.
- [ ] LLM arithmetic was not used.
## Memo facts
- [ ] Key numbers trace to verified Analytics facts.
- [ ] Main deviations trace to mart rows, slices, or evidence cards.
- [ ] Drivers are separated into confirmed causes and hypotheses.
- [ ] Risks have `risk_basis`.
- [ ] Actions have owner, due date, and status.
- [ ] Recommendations do not exceed verified facts.
## QA
- [ ] Totals and reconciliations are documented or blockers are listed.
- [ ] Data quality status is visible.
- [ ] Confidence is stated for major claims.
- [ ] Executive language avoids technical IDs outside appendix / evidence.
- [ ] Appendix or evidence section is clearly separated from the memo body.
## Limitations
- [ ] Known blockers are listed.
- [ ] Coverage gaps are listed.
- [ ] Timing, mapping, or data quality issues are listed.
- [ ] Assumptions are labeled.
## Acceptance
- [ ] Memo narrative is based only on verified Analytics facts.
- [ ] Unsupported statements are marked as assumptions, hypotheses, limitations, or blockers.
- [ ] The memo is ready for judge / QA or clearly blocked.

## From: `ChatGPT/[Analytics]/Templates/AP_P2P_CONTEXT_PACK.md`

# Candidate AP/P2P Context Pack
Status: candidate template / checklist only.
## Scope
Question:
Audit objective:
Decision context:
Audience:
Owner:
Expected output:
## Data contract
Source tables:
Source owner:
Refresh timestamp:
Required columns:
Primary keys:
Join keys:
Currency / units:
Period logic:
Approval threshold source:
## Key fields
Vendor fields:
Invoice fields:
PO fields:
Receipt fields:
Payment fields:
User / approver fields:
Bank account fields:
## Grain / period / filters
Grain:
Period:
Comparison period:
Filters:
Exclusions:
Materiality threshold:
## Risk scenarios
Vendor master:
- duplicate vendor identity
- duplicate tax ID / registration ID
- duplicate bank account
- duplicate address / phone
- inactive vendor with recent payment
- new vendor with large first payment
Invoice:
- same vendor + same invoice number
- same vendor + same amount + close dates
- normalized invoice number match
- invoice just below approval threshold
- invoice without PO
- invoice after payment
PO / receipt / invoice / payment:
- invoice before goods receipt
- invoice amount above tolerance
- payment without receipt
- multiple invoices against same PO line
- closed PO with new invoice
Payment:
- weekend / holiday payment
- urgent / manual payment run
- split payments
- changed bank account before payment
- payment to inactive / blocked vendor
- large one-off payment
## Method
Source layer:
Output layer:
Deterministic check:
False-positive check:
Exception output:
Calculation tool:
## Evidence rules
- Use cautious wording: `exception`, `risk indicator`, `requires review`, `possible duplicate`, `potential control breach`.
- Do not label fraud, misconduct, manipulation, or confirmed duplicate payment without separate evidence and human acceptance.
- DPO benchmark claims: `not found` / `needs evidence` unless separately supported.
- Penalty amount claims: `not found` / `needs evidence` unless separately supported.
- Do not include real client, vendor, employee, bank, invoice, payment, tax ID, or personal data examples.
## QA
- [ ] Data contract is complete enough for the selected AP/P2P checks.
- [ ] Source tables, key fields, period, grain, currency, filters, and exclusions are explicit.
- [ ] Checks are deterministic and reproducible.
- [ ] LLM arithmetic was not used.
- [ ] False-positive checks are listed before findings are accepted.
- [ ] Findings remain candidate exceptions until human review.
## Limitations
Known blockers:
Coverage gaps:
Mapping issues:
Timing issues:
Assumptions:
## Human acceptance
- [ ] Reviewer accepted the data contract and scope.
- [ ] Reviewer accepted the exception wording.
- [ ] Reviewer accepted or rejected each finding.
- [ ] Candidate pack remains non-production unless separately accepted.

## From: `ChatGPT/[Analytics]/Templates/AP_P2P_RISK_LIBRARY.md`

# Candidate AP/P2P Risk Library
Status: candidate template / checklist only.
## Usage rules
- Use this library as candidate AP/P2P risk indicators for Analytics review.
- Treat every result as an `exception` or `risk indicator` until human review.
- Do not label fraud, misconduct, manipulation, or confirmed duplicate payment without separate evidence and human acceptance.
- DPO benchmark and penalty amount claims are `not found` / `needs evidence` unless separately supported.
## Risk scenario register
| risk_id | area | risk scenario | source tables | key fields | deterministic check | false-positive check | exception output | QA status | confidence | limitation |
|---|---|---|---|---|---|---|---|---|---|---|
| AP-VEND-001 | Vendor master | duplicate vendor identity | vendor master | vendor name, normalized name, address, phone | match normalized identity fields | verify legal entity, branch, group vendor, and shared service records | possible duplicate vendor identity requires review | not run | low | needs source data |
| AP-VEND-002 | Vendor master | duplicate tax ID / registration ID | vendor master | tax ID, registration ID, country | match normalized tax or registration ID | verify tax group, merged entity, and legitimate shared registration | possible duplicate tax / registration ID requires review | not run | low | needs source data |
| AP-VEND-003 | Vendor master | duplicate bank account | vendor master, bank master | bank account, bank key, vendor ID | match normalized bank account across vendors | verify treasury, factoring, group account, and payment agent setup | possible duplicate bank account requires review | not run | low | needs source data |
| AP-VEND-004 | Vendor master | duplicate address / phone | vendor master | address, phone, vendor ID | match normalized address or phone across vendors | verify shared office, corporate group, and data-entry convention | possible duplicate contact data requires review | not run | low | needs source data |
| AP-VEND-005 | Vendor master | inactive vendor with recent payment | vendor master, payments | vendor status, payment date, payment amount | inactive or blocked status with payment in period | verify status timing, unblock approval, and legacy settlement | potential control breach requires review | not run | low | needs source data |
| AP-VEND-006 | Vendor master | new vendor with large first payment | vendor master, payments | vendor creation date, first payment date, amount | first payment exceeds materiality threshold within new vendor window | verify onboarding approval, contract, and one-time vendor policy | risk indicator requires review | not run | low | needs source data |
| AP-INV-001 | Invoice | same vendor + same invoice number | invoices | vendor ID, invoice number | exact match within vendor | verify credit memo, reversal, corrected invoice, and duplicate entry policy | possible duplicate invoice requires review | not run | low | needs source data |
| AP-INV-002 | Invoice | same vendor + same amount + close dates | invoices | vendor ID, amount, invoice date | same amount within close-date window | verify recurring billing, installments, and scheduled payments | possible duplicate invoice requires review | not run | low | needs source data |
| AP-INV-003 | Invoice | normalized invoice number match | invoices | vendor ID, normalized invoice number | match normalized invoice number after removing spaces, punctuation, and leading zeros | verify vendor numbering convention and reversals | possible duplicate invoice requires review | not run | low | needs source data |
| AP-INV-004 | Invoice | invoice just below approval threshold | invoices, approvals | amount, approval threshold | invoice amount within threshold proximity band | verify legitimate pricing, tax, freight, and split policy | risk indicator requires review | not run | low | needs source data |
| AP-INV-005 | Invoice | invoice without PO | invoices, PO | PO number, invoice type | missing PO where PO is expected | verify non-PO category, approved exception, and policy scope | potential control breach requires review | not run | low | needs source data |
| AP-INV-006 | Invoice | invoice after payment | invoices, payments | invoice date, payment date | payment date before invoice date | verify date fields, prepayment, and data-entry timing | exception requires review | not run | low | needs source data |
| AP-PO-001 | PO / receipt / invoice / payment | invoice before goods receipt | invoices, receipts | invoice date, receipt date | invoice date before receipt date | verify services, accruals, prepayment, and receipt posting lag | exception requires review | not run | low | needs source data |
| AP-PO-002 | PO / receipt / invoice / payment | invoice amount above tolerance | PO, invoices | PO amount, invoice amount, tolerance | invoice amount exceeds PO tolerance | verify approved change order, taxes, freight, and price variance policy | potential control breach requires review | not run | low | needs source data |
| AP-PO-003 | PO / receipt / invoice / payment | payment without receipt | payments, receipts, invoices | payment ID, receipt ID | payment matched to invoice without required receipt | verify non-receipt category and approved exception | potential control breach requires review | not run | low | needs source data |
| AP-PO-004 | PO / receipt / invoice / payment | multiple invoices against same PO line | PO lines, invoices | PO line ID, invoice ID | count invoices per PO line above expected count | verify partial deliveries, milestone billing, and credit memos | exception requires review | not run | low | needs source data |
| AP-PO-005 | PO / receipt / invoice / payment | closed PO with new invoice | PO, invoices | PO status, invoice date | invoice posted after PO close date | verify close/reopen timing and final invoice approval | potential control breach requires review | not run | low | needs source data |
| AP-PAY-001 | Payment | weekend / holiday payment | payments, calendar | payment date | payment date falls on weekend or holiday | verify banking calendar, timezone, and scheduled run | risk indicator requires review | not run | low | needs source data |
| AP-PAY-002 | Payment | urgent / manual payment run | payments | payment run type, urgency flag | manual or urgent payment indicator | verify approved exception and treasury instruction | risk indicator requires review | not run | low | needs source data |
| AP-PAY-003 | Payment | split payments | payments | vendor ID, amount, date | multiple payments near threshold or same obligation | verify installments, payment terms, and partial settlement | risk indicator requires review | not run | low | needs source data |
| AP-PAY-004 | Payment | changed bank account before payment | bank master, payments | bank change date, payment date | bank account changed shortly before payment | verify change approval and callback control | potential control breach requires review | not run | low | needs source data |
| AP-PAY-005 | Payment | payment to inactive / blocked vendor | vendor master, payments | vendor status, payment date | blocked or inactive status at payment date | verify unblock timing and exception approval | potential control breach requires review | not run | low | needs source data |
| AP-PAY-006 | Payment | large one-off payment | payments | vendor ID, amount, frequency | payment exceeds materiality threshold and has no comparable history | verify one-time contract, settlement, or approved exceptional payment | risk indicator requires review | not run | low | needs source data |
## QA
- [ ] Each risk scenario has source tables and key fields.
- [ ] Each risk scenario has deterministic and false-positive checks.
- [ ] Each output uses cautious audit wording.
- [ ] Confidence is not raised without evidence and reviewer acceptance.
## Human acceptance
- [ ] Reviewer selected applicable risk scenarios.
- [ ] Reviewer accepted thresholds and false-positive logic.
- [ ] Reviewer accepted final exception classifications.

## From: `ChatGPT/[Analytics]/Templates/AP_P2P_EXCEPTION_REGISTER_TEMPLATE.md`

# Candidate AP/P2P Exception Register Template
Status: candidate template / checklist only.
## Scope
Question:
Audit objective:
Owner:
Expected output:
## Data contract
Source tables:
Source owner:
Refresh timestamp:
Required columns:
Key fields:
Currency / units:
Period:
Grain:
Filters:
## Exception register
| exception_id | risk_id | risk scenario | entity_id | document_id | amount | currency | period | grain | deterministic check | false-positive check | exception status | QA status | confidence | limitation | reviewer decision |
|---|---|---|---|---|---:|---|---|---|---|---|---|---|---|---|---|
## Evidence fields
Source mart:
Source table or slice:
Evidence ID:
Formula or method:
Threshold:
Reviewer notes:
## Exception status values
- `exception`
- `risk indicator`
- `requires review`
- `possible duplicate`
- `potential control breach`
- `cleared false positive`
- `accepted finding`
## QA
- [ ] Exception rows trace to source mart or source table.
- [ ] Amount, currency, period, grain, and filters are explicit.
- [ ] Deterministic checks were run outside LLM arithmetic.
- [ ] False-positive checks are recorded before reviewer decision.
- [ ] Facts are separated from assumptions and hypotheses.
- [ ] Confidence and limitations are visible.
## Human acceptance
- [ ] Reviewer accepted the exception register scope.
- [ ] Reviewer accepted or cleared each exception.
- [ ] No fraud, misconduct, manipulation, or confirmed duplicate payment language is used without separate evidence and acceptance.

## From: `ChatGPT/[Analytics]/Templates/AP_P2P_AUDIT_FINDING_TEMPLATE.md`

# Candidate AP/P2P Audit Finding Template
Status: candidate template / checklist only.
## Finding header
Finding ID:
Risk scenario:
Area:
Owner:
Reviewer:
Status:
## Scope
Audit objective:
Decision context:
Period:
Grain:
Filters:
Currency / units:
## Data contract
Source tables:
Source owner:
Refresh timestamp:
Required columns:
Key fields:
Source mart:
Evidence IDs:
## Method
Deterministic check:
False-positive check:
Calculation tool:
Threshold:
Reviewer procedure:
## Facts
Observed exception:
Affected entity or document:
Amount:
Period:
Evidence:
QA status:
## Interpretation
Risk indicator:
Potential control breach:
Likely cause:
Assumptions:
Confidence:
## Limitations
Known blockers:
Coverage gaps:
Mapping issues:
Timing issues:
Unsupported claims:
- DPO benchmark: `not found` / `needs evidence`
- Penalty amount: `not found` / `needs evidence`
## Recommended action
Action:
Owner:
Due date:
Acceptance condition:
## Wording guardrail
- Use cautious audit wording.
- Do not label fraud, misconduct, manipulation, or confirmed duplicate payment without separate evidence and human acceptance.
- Keep facts, assumptions, confidence, and limitations separate.
## Human acceptance
- [ ] Reviewer accepted facts and evidence.
- [ ] Reviewer accepted confidence level.
- [ ] Reviewer accepted recommended action.
- [ ] Reviewer accepted final wording.

## From: `ChatGPT/[Analytics]/Templates/AP_P2P_QA_CHECKLIST.md`

# Candidate AP/P2P QA Checklist
Status: candidate template / checklist only.
## Data contract
- [ ] Source tables are listed.
- [ ] Source owner and refresh timestamp are listed.
- [ ] Required columns and key fields are listed.
- [ ] Currency / units are explicit.
- [ ] Period logic is explicit.
- [ ] Grain is explicit.
- [ ] Filters and exclusions are explicit.
## Source tables and key fields
- [ ] Vendor master fields are available or listed as missing.
- [ ] Invoice fields are available or listed as missing.
- [ ] PO fields are available or listed as missing.
- [ ] Receipt fields are available or listed as missing.
- [ ] Payment fields are available or listed as missing.
- [ ] User / approver fields are available or listed as missing.
- [ ] Bank account fields are available or listed as missing.
## Deterministic checks
- [ ] Selected risk scenarios are listed.
- [ ] Thresholds are explicit.
- [ ] Checks are reproducible by Python, SQL, spreadsheet formulas, or another deterministic project-standard tool.
- [ ] LLM arithmetic was not used.
- [ ] Exception output includes amount, currency, period, grain, risk scenario, QA status, confidence, and limitation.
## False-positive checks
- [ ] Legitimate shared vendor, address, phone, bank, or tax ID cases are considered.
- [ ] Reversals, credit memos, corrections, installments, and recurring billing are considered.
- [ ] PO tolerances, change orders, taxes, freight, and non-PO categories are considered.
- [ ] Treasury, banking calendar, timezone, manual run approvals, and unblock timing are considered.
- [ ] Exceptions are not escalated to findings before reviewer decision.
## Wording
- [ ] Output uses cautious wording: `exception`, `risk indicator`, `requires review`, `possible duplicate`, or `potential control breach`.
- [ ] Output does not label fraud, misconduct, manipulation, or confirmed duplicate payment without separate evidence and human acceptance.
- [ ] DPO benchmark claims are marked `not found` / `needs evidence` unless separately supported.
- [ ] Penalty amount claims are marked `not found` / `needs evidence` unless separately supported.
- [ ] Public repo content contains no real client, vendor, employee, bank, invoice, payment, tax ID, or personal data examples.
## Human acceptance
- [ ] Reviewer accepted the data contract.
- [ ] Reviewer accepted selected risk scenarios and thresholds.
- [ ] Reviewer accepted false-positive logic.
- [ ] Reviewer accepted final exceptions and findings.
- [ ] Candidate pack remains non-production unless separately accepted.

## From: `ChatGPT/[Analytics]/Templates/CLAIM_EVIDENCE_REGISTRY_TEMPLATE.md`

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

## From: `ChatGPT/[Analytics]/Templates/EVIDENCE_CARD_TEMPLATE.md`

# Evidence Card Template
evidence_id:
source_mart:
source_table_or_slice:
source_file:
metric:
value:
period:
grain:
filter:
calculation_method:
formula:
reconciliation_status:
value_state: KNOWN/UNKNOWN/NOT_REPORTED/NOT_APPLICABLE/PARSE_FAILED/MISSING_SOURCE/UNMATCHED/BLOCKED
dq_status:
qa_status:
confidence:
limitation:
used_in_claims:
review_status:

## From: `ChatGPT/[Analytics]/Templates/METRIC_DEFINITION_CARD_TEMPLATE.md`

# Metric Definition Card Template
## Purpose
A formula alone is not a sufficient metric definition. Use this card for
material, flagship, or ratio-like metrics before a strong management
conclusion is published. It extends the existing Data Contract / mart
metric-formula rule (`DATA_CONTRACTS.md`, `MAIN_FILES_STANDARD.md`); it is not
a parallel metric framework and does not replace `QUANTITATIVE_SANITY_GATE.md`
or the 22-method registry.
## Card
```text
METRIC_DEFINITION_CARD
metric_id:
metric_name:
business_question:
metric_type: amount / count / ratio / rate / duration / share / index
formula:
numerator:
denominator:
aggregation_rule:
higher_is: favorable / adverse / context_dependent
unit:
currency:
time_basis:
population:
inclusions:
exclusions:
zero_denominator_rule:
null_semantics:
sign_convention:
allowed_comparisons:
forbidden_interpretations:
source_fields:
owner:
status: approved / provisional / blocked
```
## Field notes
- `numerator` / `denominator` are required whenever `metric_type` is `ratio`,
  `rate`, or `share`; otherwise record `not_applicable`.
- `aggregation_rule` states how the metric aggregates across grain (sum,
  weighted average, last value, distinct count, etc.); it is never inferred
  from the formula alone.
- `population` states the entity/record population the metric is computed
  over, consistent with `MAIN_FILES_STANDARD.md` grain and `DATA_CONTRACTS.md`
  scope rules. Population comparability across periods is the responsibility
  of this field, not a separate framework.
- `zero_denominator_rule` and `null_semantics` must use the canonical
  `VALUE_STATE` vocabulary (`DATA_CONTRACTS.md`) where the null/undefined case
  is materially different from zero.
- `allowed_comparisons` states permitted comparison scope (e.g. same
  population, same period type, same denominator definition).
  `forbidden_interpretations` states conclusions the metric must not be used
  to support (e.g. "not a causal driver", "not comparable across the
  population change on <date>").
- `status: approved` is required before the metric supports a material or
  flagship management conclusion. `provisional` or `blocked` metrics may be
  shown with an explicit limitation but cannot anchor a strong conclusion.
## Required behavior
- A formula alone (`formula:` populated, remaining fields empty) is not a
  sufficient metric definition for a material/flagship/ratio-like metric.
- Before any material conclusion, numerator/denominator, aggregation
  semantics, population, units/currency, sign/direction, zero-denominator
  behavior, allowed comparison scope, and forbidden interpretations must be
  defined where applicable to the `metric_type`.
- An unresolved material metric definition (`status: provisional / blocked`,
  or a required field left undefined) blocks a strong management conclusion:
  the claim is limited to `HYPOTHESIS` / `LIMITATION`, not a flagship finding.
## Acceptance
- [ ] Metric semantics documented separately from formula.
- [ ] Aggregation rule explicit.
- [ ] Numerator / denominator explicit when applicable.
- [ ] Population explicit.
- [ ] Zero-denominator rule explicit.
- [ ] Forbidden interpretations stated.
- [ ] Unresolved material metric definition blocks a strong management
  conclusion.
## P1 extension: `POPULATION_CONTRACT` (standard, active, issue #445)
`POPULATION_CONTRACT` is a more detailed population/denominator
comparability contract for ratio/rate/share/average/margin/conversion/
productivity/frequency metrics. It completed a bounded pilot and is
promoted to standard, active status (CONTROL/CONTRACT) per issue #445; the
full field list, required behavior, and activation trigger are defined once
in `ANALYTICAL_REASONING_STANDARD.md` §15.1 — this section does not restate
them to avoid drift. It extends, and does not replace, the `population`,
`inclusions`, `exclusions` fields on this card and the existing
`population_constant_or_explained?` / `denominator_constant_or_explained?` /
`scope_change_quantified?` controls in `ANALYTICAL_REASONING_STANDARD.md` §5,
which remain active for routine/quick cases with no material trigger.
Promoted 2026-09-06 (owner-authorized); see
`docs/evidence/ANALYTICS_P1_PROMOTION_2026-09-06.md` for the promotion
decision and `../Knowledge/P1_PILOT_EVIDENCE_2026-09-06.md` for the original
pilot evidence.

## From: `ChatGPT/[Analytics]/Knowledge/ANALYTICS_06_TEMPLATES_BUNDLE_SEMANTICS.md`

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
