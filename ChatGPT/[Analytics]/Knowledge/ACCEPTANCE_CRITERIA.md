# Analytics Acceptance Criteria

A result is accepted when:

1. Question and scope are clear.
2. Inputs are listed.
3. Data contract exists or missing fields are explicit.
4. Grain, period and filters are documented.
5. Stage and mart main files are created or designed.
6. Calculation method is documented.
7. QA checks passed or failed with explanation.
8. Findings are traceable to data.
9. Limitations are explicit.
10. Handoff package is complete if another project is needed.

## Main file acceptance

```text
stage_main_full: pass/fail/blocked/not_applicable
mart_main_full: pass/fail/blocked/not_applicable
mart_main_tz_or_compact: pass/fail/blocked/not_applicable
slices_from_mart_main_full: pass/fail/blocked/not_applicable
```

## Acceptance status

```text
accepted: yes/no
qa_status: pass/fail/blocked
confidence: high/medium/low
residual_risks:
known_limitations:
next_step:
```

## Usability acceptance

A result is not accepted if it is technically complete but unusable for the requested task.

For `quick` mode:

- max 1 user-facing table;
- max 5 metrics;
- max 12 visible columns;
- no workbook unless explicitly requested;
- no hidden expansion into full audit package.

For `standard` mode:

- compact front view required;
- no more than 3-5 sheets unless justified;
- every extra sheet must have a business purpose.

For `full_traceable_analysis` mode (`full_audit` alias):

- workbook may be large, but must include:
  - README / index;
  - compact front sheet;
  - data dictionary;
  - field groups;
  - evidence appendix.

## Blocked status

Use `blocked` when:

- required data is missing;
- grain is unknown;
- DQ Fail;
- no reconciliation possible;
- metric formulas undefined;
- compact-only input is insufficient for requested conclusion;
- implementation is required before result can be produced.

## Not production-ready rule

Smoke QA or a good memo does not equal production readiness. Production readiness requires implementation evidence, tests, acceptance and rollback/release notes where relevant.
