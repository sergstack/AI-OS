# AES Analytics Pilot — Results (Phase 4)

Status: executed. This is the Phase 4 run of the pilot specified in
`docs/pilots/AES_ANALYTICS_PILOT.md`, per
`docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md` Section 19 (adoption phases) and
`docs/standards/AUTONOMOUS_EXECUTION_EXTENSION_CONTRACT.md` Section 5.2 (`[Analytics]`
extension expectations).

## Scope deviation (read first)

`AES_ANALYTICS_PILOT.md`'s constraints say: "Use a real or realistic
Analytics dataset already governed by an existing data contract; do not
invent a new financial dataset for the pilot alone."

This repository has **no real Analytics data infrastructure** — no RAW
data files, no mart-building code, no real business dataset governed by
`ChatGPT/[Analytics]/Knowledge/DATA_CONTRACTS.md`. Running this pilot
against real business data was out of scope and forbidden (source
mutation / business-data risk). Instead, this run built a small, clearly
labeled **synthetic** pilot fixture (invented numbers, fictional
"Widget A/B/C" products, fictional "North/South" regions) and walked it
through the full methodology end to end. This is a deliberate, documented
deviation from the pilot spec's dataset constraint, made because the
spec's precondition (an existing real dataset) does not hold in this
repository. No business formula, metric definition, or financial control
belonging to the real `[Analytics]` project was read, changed, or
referenced beyond the vocabulary check in
`ChatGPT/[Analytics]/Knowledge_Bundles/ANALYTICS_02_DATA_CONTRACTS_AND_MARTS.md`
and `ChatGPT/[Analytics]/Knowledge/ANALYTICS_WORKFLOW.md`.

Formal authoring of the `[Analytics]` execution extension itself
(`docs/standards/AUTONOMOUS_EXECUTION_EXTENSION_CONTRACT.md` Section 5.2, deliverable 1
of `AES_ANALYTICS_PILOT.md`) and resolution of the `accepted: yes/no` ->
`overall_delivery` open question (deliverable 2) were **not** part of
this concrete pilot-run task and remain follow-up work; the execution
record's `project_extension` field records illustrative subtype names
only (`data_or_mapping_fix`, `calculation_or_logic_fix`), not a ratified
extension.

## 1. Data contract

`docs/autonomous_execution/pilot_fixtures/analytics/DATA_CONTRACT.md`.

| Field | Value |
|---|---|
| Entity | synthetic sales order line |
| Grain (RAW/STAGE) | one row per `order_id` |
| Grain (MART) | one row per `(quarter, region, product)` |
| Keys | `order_id` (RAW/STAGE); `(quarter, region, product)` (MART) |
| Period | fictional Q1 / Q2 |
| Currency/unit | synthetic USD (`unit_price_usd`, derived `revenue_usd`); `units` = raw count |

## 2. RAW fixture

`docs/autonomous_execution/pilot_fixtures/analytics/raw_sales.csv` — 16
synthetic order rows (14 `completed`, 2 `cancelled`), fictional company
and product names, clearly commented as synthetic.

## 3. Build script

`scripts/pilot_analytics_build_mart.py` — deterministic, no randomness.
Reads RAW, writes `stage_sales.csv` (STAGE), `mart_sales_by_quarter.csv`
/ `.json` (MART), and `reconciliation_report.json`. Formula:
`revenue_usd = units * unit_price_usd` (completed orders only);
`growth_pct = (Q2_total - Q1_total) / Q1_total * 100`.

## 4. Defect found and fixed (corrective loop)

**Defect (def-001)**, classification `contract` / subtype
`data_or_mapping_fix`: the first version of `build_mart()` omitted the
`status == "completed"` filter required by the contract's
`metric_rules`, so cancelled-order revenue leaked into the MART
aggregation.

### Before (FAIL) — first run, command output

```text
$ python3 scripts/pilot_analytics_build_mart.py
=== AES Phase 4 Analytics pilot: RAW -> STAGE -> MART reconciliation ===
RAW rows: 16, STAGE rows: 16
contract_expected_revenue_usd (RAW, completed-only): 2130.0
stage_completed_revenue_usd:                          2130.0
mart_total_revenue_usd:                                2440.0
  [PASS] raw_row_count_equals_stage_row_count
  [PASS] contract_expected_revenue_equals_stage_completed_revenue
  [FAIL] stage_completed_revenue_equals_mart_total_revenue
  [FAIL] contract_expected_revenue_equals_mart_total_revenue
  [FAIL] mart_units_equal_raw_completed_units_no_double_counting
Q1 total revenue (mart): 1110.0
Q2 total revenue (mart): 1330.0
QoQ growth_pct: 19.82
RECONCILIATION: FAIL
EXIT CODE: 1
```

Cancelled-order revenue ($160 in Q1 + $150 in Q2 = $310) leaked into the
MART totals, inflating both quarters and distorting the growth figure
(19.82% instead of the correct number).

### Fix applied

In `build_mart()`, added the missing filter:

```python
for row in stage_rows:
    if row["status"] != "completed":
        continue
    ...
```

### After (PASS) — corrected run, command output

```text
$ python3 scripts/pilot_analytics_build_mart.py
=== AES Phase 4 Analytics pilot: RAW -> STAGE -> MART reconciliation ===
RAW rows: 16, STAGE rows: 16
contract_expected_revenue_usd (RAW, completed-only): 2130.0
stage_completed_revenue_usd:                          2130.0
mart_total_revenue_usd:                                2130.0
  [PASS] raw_row_count_equals_stage_row_count
  [PASS] contract_expected_revenue_equals_stage_completed_revenue
  [PASS] stage_completed_revenue_equals_mart_total_revenue
  [PASS] contract_expected_revenue_equals_mart_total_revenue
  [PASS] mart_units_equal_raw_completed_units_no_double_counting
Q1 total revenue (mart): 950.0
Q2 total revenue (mart): 1180.0
QoQ growth_pct: 24.21
RECONCILIATION: PASS
EXIT CODE: 0
```

### Reconciliation before/after summary

| Metric | Before (defective) | After (fixed) |
|---|---|---|
| contract_expected_revenue_usd (RAW) | 2130.00 | 2130.00 |
| mart_total_revenue_usd | 2440.00 (wrong) | 2130.00 (matches) |
| QoQ growth_pct | 19.82% (wrong) | 24.21% (correct) |
| Reconciliation checks passing | 2 / 5 | 5 / 5 |

## 5. Findings memo

`docs/autonomous_execution/pilot_fixtures/analytics/PILOT_MEMO.md` —
finding: synthetic completed-order revenue grew +24.21% QoQ ($950 ->
$1,180), with an explicit "fictional pilot data, not a real business
claim" disclaimer at the top and confidence/limitations section.

## 6. Judge-style self-review checklist

Checked against the Analytics extension's expected blockers
(`docs/standards/AUTONOMOUS_EXECUTION_EXTENSION_CONTRACT.md` Section 5.2 vocabulary /
`ChatGPT/[Analytics]/Knowledge/QA_CHECKLIST.md`):

| Check | Outcome |
|---|---|
| Entity defined | Pass — synthetic sales order line, `DATA_CONTRACT.md` |
| Grain defined (RAW/STAGE and MART) | Pass — order-line grain and quarter x region x product grain, both stated |
| Keys defined | Pass — `order_id`; `(quarter, region, product)` |
| Period defined | Pass — fictional Q1/Q2 |
| Currency/unit defined | Pass — synthetic USD, unit count |
| RAW/STAGE/MART reconciliation passes | Pass — 5/5 checks, `reconciliation_report.json`, `overall_pass: true` |
| No conclusion drawn without a mart + reconciliation | Pass — memo number is read from the post-fix `mart_sales_by_quarter.json`, after `overall_pass: true` |
| No unsupported claims | Pass — memo states method, formula, confidence, and limitations; explicitly disclaims real-business relevance |
| Risk basis stated | Pass — synthetic-data risk and scope-deviation rationale stated in this document's "Scope deviation" section and in `DATA_CONTRACT.md` |
| Memo not stale relative to final mart revision | Pass — memo's numbers (950 / 1,180 / 24.21%) match the final, corrected `mart_sales_by_quarter.json` `formula` block exactly |
| Claim/evidence traceability | Pass — memo's numbers trace to `reconciliation_report.json` and `mart_sales_by_quarter.json`; execution record `req-001`/`def-001` link to `val-001`/`val-002` |

**Judge-style verdict: pass.** No blocker condition is open. (This is a
self-review by the executor, not an independent Judge run — the
execution record's `judge_verdict` field is correctly left `not_run`.)

## 7. Execution record

`docs/autonomous_execution/examples/pilot_evidence/analytics_pilot.json` —
structurally validated against `schemas/autonomous_execution_record.schema.json`
with `jsonschema` 4.26.0:

```text
$ python3 -c "
import json, jsonschema
schema = json.load(open('schemas/autonomous_execution_record.schema.json'))
record = json.load(open('docs/autonomous_execution/examples/pilot_evidence/analytics_pilot.json'))
jsonschema.validate(record, schema)
print('VALID')
"
VALID
```

Covers: requirement `req-001`, defect `def-001` (open -> correcting ->
resolved), two iterations (`iter-001` fail, `iter-002` pass), four
validation runs (`val-001` reconciliation fail, `val-002` reconciliation
pass, `val-003` repo pytest baseline, `val-004` repo governance/baseline
scripts), all seven mandatory acceptance scopes (all `pass`),
`overall_delivery: pass`, `qa_status: not_run`, `judge_verdict: not_run`,
`authority_status: owner_review_pending`.

`source_revision.final_revision` is set to the actual git commit SHA
that lands this pilot (see PR).

**Lineage update (adoption cleanup):** `parent_execution_id` was added
retroactively during pre-merge adoption cleanup of the AES PR stack
(#225-#230), pointing to `exec-aes-crossproject-pilot-001` (the Phase 5
cross-project handoff pilot's root execution). The Phase 5 pilot report
had flagged that this record's parent link only existed in the Phase 5
handoff record, not reciprocally here. Since no PR in the stack is
merged yet, this is an additive field change to unfrozen evidence, not a
rewrite of any test result, defect description, hash, or command output.

## 8. Baseline checks (nothing else broke)

```text
$ python3 -m pytest tests/ -q
........................................................................ [ 97%]
..                                                                       [100%]
74 passed in 1.35s

$ python3 scripts/check_manifest_paths.py
Summary: checked: 122, passed: 122, failed: 0

$ python3 scripts/check_index_coverage.py
Index coverage pairs checked: 9
Failed: 0

$ python3 scripts/check_knowledge_bundles.py
Summary: projects checked: 7, bundles checked: 33, upload files max: 7, failed: 0

$ python3 scripts/check_repo_public_safety.py
Public safety check passed.

$ python3 scripts/check_codex_goal_mode_defaults.py
Codex Goal Mode atomic-default occurrences checked: 21
Failed: 0

$ python3 scripts/check_project_instructions_length.py
Checked PROJECT_INSTRUCTIONS.md files: 7
Passed: 7
Failed: 0
```

All baseline checks pass; no `.github/workflows/*`, `MANIFEST.json`, or
real Knowledge Bundle / `ChatGPT/[Analytics]` governed content was
touched by this pilot — only new, additive files under
`docs/autonomous_execution/pilot_fixtures/analytics/`,
`docs/autonomous_execution/examples/pilot_evidence/`, `docs/pilots/`, and
`scripts/pilot_analytics_build_mart.py`.

## Overall pilot verdict

**Pass.** The full flow — data contract -> mapping -> RAW/STAGE/MART
reconciliation -> formulas -> findings -> memo -> Judge-style review ->
correction -> rebuild -> final acceptance — was demonstrated end to end
against a synthetic fixture, with a genuine defect found (reconciliation
FAIL, evidence captured) and genuinely fixed (reconciliation PASS,
evidence captured), and a structurally valid execution record produced.
This pilot demonstrates AES tracking around Analytics-shaped work; it
does not certify or modify the real `[Analytics]` project's methodology,
and its numeric "finding" carries no real-business weight.
