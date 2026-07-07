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
