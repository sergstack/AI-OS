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
