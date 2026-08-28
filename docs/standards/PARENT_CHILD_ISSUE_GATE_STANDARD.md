# Parent / Child Issue Gate Standard

This standard defines when and how to split a complex analytics or implementation goal into a parent issue, sequenced child issues, PR gates, and final QA.

Use this pattern when a goal is too large or risky for one Codex pass, especially when it changes data contracts, workbook/report contracts, marts, formulas, provider logic, safety boundaries, or acceptance criteria.

## Core pattern

```text
Parent issue = goal / scope / safety / final acceptance
Child issue = one executable layer
PR = evidence for one child issue
Gate = accept / revise / blocked
Final QA = parent acceptance
```

Recommended execution flow:

```text
Parent
  -> baseline / data contract
  -> stage layer
  -> mart / output contract
  -> calculation or classification logic
  -> review / UX / exception layer
  -> duplicate / anomaly / evidence layer if needed
  -> final QA / acceptance
```

## When to use this standard

Use parent/child issues when at least two or three of these are true:

- multiple files, sheets, tables, or outputs are involved;
- row counts, totals, joins, or reconciliations must be proven;
- a data contract, formula, metric, schema, workbook contract, or output contract changes;
- manual review is required;
- external provider evidence is involved;
- there are safety constraints such as no auto-apply, no merge, no source mutation, no API calls, or no secrets;
- the work must be reviewable through PRs;
- the result will be reused or repeated;
- a mistake can create a wrong business decision.

Do not use this pattern for small one-step tasks such as a short text change, one calculation, one chart, or a single low-risk doc edit. Use Goal Mode directly for those.

## Parent issue contract

A parent issue should define the full outcome, not every implementation detail.

Required sections:

```text
Context
Objective
Source layer / input files
Output layer / expected artifacts
Grain
Period / snapshot date
Filters / scope boundaries
Safety boundaries
Forbidden actions
Child issue order
Final acceptance criteria
Final response format
```

The parent issue should stay open until final QA passes. Do not close the parent only because a baseline or first child PR passed.

## Child issue contract

Each child issue must be small enough for one focused Codex pass.

Required sections:

```text
Parent
Depends on
Objective
Input layer
Output layer
Grain
Required files / sheets / columns
Rules
Forbidden actions
Checks
Acceptance criteria
Final response format
```

A child issue should not silently start downstream work. If a downstream idea appears, create another child issue or add a scoped addendum to the correct existing issue.

## Dependency rule

Codex must respect child issue order.

If a child issue depends on another issue or PR, Codex should:

1. Check the dependency state.
2. Continue only if the dependency is accepted or merged.
3. Stop with a clear blocker if the dependency is still open, draft, unmerged, or rejected.

Blocker format:

```text
Blocked because: <dependency> is not accepted/merged.
Current state: <open/draft/unmerged/etc.>
Next human action: <review/merge/accept/revise>
No code changes made.
```

## PR gate rule

One PR should normally correspond to one child issue.

The PR must report:

```text
Summary
Parent issue
Child issue
Files changed
Artifacts generated, if any
Commands run
Tests / checks
Row counts / reconciliation, if applicable
Safety status
Acceptance status
Remaining blockers
Rollback notes
```

The PR must not claim parent completion unless it is the final QA child issue and all downstream child issues have passed.

## Analytics layer rule

For analytics work, do not jump directly from raw data to memo or recommendations.

Preferred sequence:

```text
question / scope
-> data contract
-> source / raw inventory
-> stage_main_full
-> mart_main_full
-> compact/review mart
-> deterministic calculation
-> findings
-> QA
-> memo / final acceptance
```

Calculations, row counts, joins, totals, percentages, ratios, variances, reconciliations, classification rules, and thresholds must be deterministic through Python, SQL, spreadsheet formulas, or explicit manual control.

LLM may help with wording, structure, labels, explanations, and handoffs. LLM must not be the source of calculation truth.

## Safety boundaries

Default forbidden actions unless explicitly approved:

```text
mutate source data
enable auto-apply
auto-merge records
auto-overwrite identifiers or business fields
claim legal/financial correctness without evidence
run unapproved provider/API calls
commit secrets or .env files
commit runtime/generated artifacts unless explicitly in scope
remove existing QA or safety checks without replacement and migration note
```

If an old contract conflicts with a new contract, do not silently overwrite it. Create a migration note or blocker.

Correct:

```text
old contract + baseline evidence -> contract v2 -> reconciliation -> QA acceptance
```

Incorrect:

```text
new instruction -> delete old contract -> hope tests catch regressions
```

## Baseline gate

For high-risk work, the first child issue should usually be a baseline.

Baseline should answer:

```text
What exists now?
What row counts / totals are reproducible?
Which tests currently pass?
Which historical blockers reproduce?
Which blockers are unreproduced but documented?
What is explicitly out of scope for this baseline?
```

A baseline PR can be accepted as evidence, but it does not close the parent.

## Review / UX gate

If a human must manually review rows, cards, cases, or exceptions, include a review/UX child issue.

The reviewer should be able to answer from the review artifact:

```text
What is this row/card?
What is wrong?
What is proposed?
What evidence supports it?
What is the risk?
Why is auto-apply forbidden?
What is the next action?
What decision did the reviewer make?
```

Keep technical/debug fields in the full mart. Keep the review sheet compact and decision-oriented.

## Candidate vs confirmed rule

For duplicates, anomalies, provider matches, semantic matches, or risk flags:

```text
candidate != confirmed issue
external evidence != source of truth
semantic match != merge decision
provider name != automatic proposal
```

If a record is marked as a duplicate candidate, it must show the linked record IDs or pair IDs. A standalone flag such as `Duplicate = yes` is insufficient.

## Final QA child issue

The final QA child issue must run after all implementation child issues.

It should verify:

```text
row-count reconciliation
required sheets/files/tables
required columns
allowed classifier values
mapping and join integrity
nulls and duplicates
manual-review coverage
safety flags
no source mutation
no secrets/runtime artifacts
limitations documented
parent acceptance criteria satisfied
```

Only final QA may recommend closing the parent issue.

## Standard child issue order template

```text
# Parent — <business / analytics outcome>

# Child 1 — Baseline / current-state reconciliation
# Child 2 — Stage layer / source traceability
# Child 3 — Mart or workbook/output contract
# Child 4 — Business logic / proposal / classification safety
# Child 5 — Review UX / exception registry / manual workflow
# Child 6 — Duplicates / anomaly / evidence relationship layer
# Child 7 — Optional advanced layer, such as semantic candidates
# Child 8 — Final QA / parent acceptance
```

Keep 5-10 child issues per parent when possible. If the scope grows beyond that, split into another parent issue or milestone.

## Final user-facing summary format

After each child PR or gate, report briefly:

```text
What changed:
Checks run:
Evidence:
Acceptance status:
Remaining blockers:
Next issue:
```

Do not include long implementation narratives unless the reviewer asks for them.
