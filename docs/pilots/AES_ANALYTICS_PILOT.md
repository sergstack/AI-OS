# AES Analytics Pilot (Phase 4 — not executed)

Status: specification only. This pilot is not executed by this Phase 1
task and is not authorized by Phase 1 completion
(`docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md` Section 20).

## Goal

Run the full Analytics flow under AES tracking:

```text
data contract -> mapping -> reconciliation -> mart -> findings -> memo
-> Judge -> correction -> rebuild -> final acceptance
```

## Must verify

- entity, grain, period, currency/unit, per
  `ChatGPT/[Analytics]/Knowledge/DATA_CONTRACTS.md`;
- formulas;
- RAW/STAGE/MART reconciliation;
- claim/evidence traceability;
- chart and memo freshness (artifact-freshness contract, standard Section
  11.3).

## Constraints

- Use a real or realistic Analytics dataset already governed by an
  existing data contract; do not invent a new financial dataset for the
  pilot alone.
- No business formula, metric definition, or financial control may be
  changed as part of running this pilot — the pilot demonstrates AES
  tracking around existing Analytics methodology, it does not modify that
  methodology.

## Deliverables (Phase 4, separate issue/PR)

1. A `[Analytics]` execution extension defining domain defect subtypes,
   required evidence, and acceptance-scope additions
   (`docs/standards/AUTONOMOUS_EXECUTION_EXTENSION_CONTRACT.md` Section 5.2).
2. Resolution of the `accepted: yes/no` -> `overall_delivery` open question
   left in `docs/AUTONOMOUS_EXECUTION_STATUS_MAPPING.md` Section 4: which
   domain conditions must hold before `accepted: yes` may be reflected as
   `overall_delivery: pass`.
3. One real execution record covering the full flow above, including at
   least one registered defect and correction cycle (e.g. a reconciliation
   mismatch found and fixed).

## Acceptance for the pilot itself

- No conclusion is drawn from raw data without a mart and reconciliation,
  per `ChatGPT/[Analytics]/Knowledge/DATA_CONTRACTS.md` rules.
- Judge findings on the memo are traceable to specific requirement/defect
  IDs in the execution record.
- `overall_delivery: pass` is not asserted while the memo artifact is
  stale relative to the final mart revision.
