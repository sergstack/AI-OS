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
