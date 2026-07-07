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
