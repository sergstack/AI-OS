# AES Codex Corrective-Loop Pilot (Phase 2 — not executed)

Status: specification only. This pilot is not executed by this Phase 1
task and is not authorized by Phase 1 completion
(`AUTONOMOUS_EXECUTION_STANDARD.md` Section 20).

## Goal

Demonstrate the normative corrective-loop contract
(`AUTONOMOUS_EXECUTION_STANDARD.md` Section 9.5) end to end on a real,
isolated Codex fixture:

```text
defect registration -> bounded fix -> affected check rerun -> regression -> revalidation
```

## Constraints

- Use an isolated fixture directory or a dedicated test branch, not the
  production/working branch's real behavior.
- Use a safe, local defect (e.g. a seeded failing unit test in the
  fixture), never an artificially introduced defect in shipped code.
- Use an existing focused test as the primary validation signal.
- Preserve the existing Codex `max_corrective_fixes_per_failed_check: 1`
  policy (`AUTONOMOUS_EXECUTION_STANDARD.md` Section 9.7); the pilot must
  demonstrate stopping and reporting a residual risk if the same check
  fails twice, not looping.
- Rollback must be a scoped `git restore` or a single revertible commit.

## Deliverables (Phase 2, separate issue/PR)

1. A `[Codex]` execution extension (path decided during Phase 2 per
   `AUTONOMOUS_EXECUTION_EXTENSION_CONTRACT.md` Section 6).
2. One real execution record (conforming to
   `schemas/autonomous_execution_record.schema.json`) capturing the actual
   fixture run, including a real defect, a real corrective iteration, and
   real validation-run evidence.
3. A short pilot report: what was fixed, what checks ran, what the
   corrective loop looked like end to end, and any gaps found in the
   canonical standard.

## Acceptance for the pilot itself

- Defect was registered before the fix (not fixed silently).
- Defect was not closed without resolution evidence.
- Affected checks were rerun after the fix, not assumed.
- The one-fix policy was respected; if it needed to be, the pilot honestly
  reports a residual risk rather than iterating further.
- `overall_delivery` for the pilot execution record follows Section 10.2 of
  the standard.
