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
