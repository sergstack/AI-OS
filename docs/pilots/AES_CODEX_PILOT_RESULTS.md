# AES Codex Corrective-Loop Pilot — Results

Status: **executed (Phase 2 pilot)**. This supersedes the "not executed"
status note in `docs/pilots/AES_CODEX_PILOT.md` for the pilot run itself;
that file remains the governing spec and is unchanged.

Execution record:
`docs/autonomous_execution/examples/pilot_evidence/codex_corrective_loop_pilot.json`
(`execution_id: exec-aes-codex-pilot-001`, `parent_execution_id: null` — no
prior execution record exists for Phase 1, which shipped as a docs/schema
package rather than a recorded execution).

## Scope

Per the pilot spec's constraint to use "a safe, local defect ... never an
artificially introduced defect in shipped code," a new, clearly-labeled
fixture was created rather than sabotaging any real file:

- `tests/fixtures/aes_pilot/README.md` — marks the directory as pilot
  evidence only, not real functionality.
- `tests/fixtures/aes_pilot/pilot_helper.py` — a small standalone utility,
  `clamp_percentage(value)`, shaped like a realistic small function
  (clamping a score/progress value into `[0, 100]`) but not imported by any
  production code path.
- `tests/fixtures/aes_pilot/test_pilot_helper.py` — three focused tests,
  loaded via the same `importlib`-by-path convention already used in
  `tests/test_validation_scripts.py`.

Nothing outside `tests/fixtures/aes_pilot/` was modified.

## Defect

- **ID:** `def-pilot-001`
- **Classification:** `implementation`
- **Severity:** `recoverable`
- **Root cause:** `clamp_percentage` clamped only the upper bound
  (`min(value, 100)`), so a negative input (e.g. `-10`) passed through
  unclamped instead of being floored at `0`.
- **Detected by:** `test_clamp_percentage_clamps_lower_bound`, one of the
  three focused tests written alongside the fixture, run *before* any fix
  was applied.
- **Registered:** committed to the branch in its defective (red) state
  first (commit `76b64561`), so the defect is on record before the
  correction exists — not fixed silently.

## Fix (bounded, one-fix policy)

Single minimal corrective iteration, per Codex's
`max_corrective_fixes_per_failed_check: 1` policy
(`AUTONOMOUS_EXECUTION_STANDARD.md` Section 9.7):

```diff
-    return min(value, 100)
+    return max(0, min(value, 100))
```

Committed as `cba47c4` ("AES Codex pilot iter-002: fix def-pilot-001
(bounded, one-fix policy)"). The fix passed on the first attempt, so no
second corrective iteration or residual-risk report was needed.

## Commands run and actual output

1. **Red (defect present, before fix), commit `76b64561`:**

   ```
   $ python3 -m pytest tests/fixtures/aes_pilot/test_pilot_helper.py -q
   ..F                                                                      [100%]
   =================================== FAILURES ===================================
   ___________________ test_clamp_percentage_clamps_lower_bound ___________________
   >       assert clamp_percentage(-10) == 0
   E       assert -10 == 0
   E        +  where -10 = clamp_percentage(-10)
   1 failed, 2 passed in 0.03s
   ```

2. **Fix applied**, then **green, commit `cba47c4`:**

   ```
   $ python3 -m pytest tests/fixtures/aes_pilot/test_pilot_helper.py -q
   ...                                                                      [100%]
   3 passed in 0.01s
   ```

3. **Regression — full repo test suite, against `cba47c4` (final revision):**

   ```
   $ python3 -m pytest tests/ -q
   ........................................................................ [ 93%]
   .....                                                                    [100%]
   77 passed in 1.30s
   ```

   (74 pre-existing tests + 3 new fixture tests, all passing — zero
   collateral damage.)

4. **Regression — existing governance/validation scripts, against `cba47c4`:**

   ```
   $ python3 scripts/check_project_instructions_length.py   # exit 0, 7/7 PASS
   $ python3 scripts/check_repo_public_safety.py             # exit 0, PASS
   $ python3 scripts/check_codex_goal_mode_defaults.py        # exit 0, 21 occurrences, 0 failed
   $ python3 scripts/check_manifest_paths.py                  # exit 0, 122/122 PASS
   $ python3 scripts/check_knowledge_bundles.py                # exit 0, 33 bundles, 0 failed
   $ python3 scripts/check_index_coverage.py                  # exit 0, 9 pairs, 0 failed
   ```

5. **Execution record structural validation:**

   ```
   $ python3 -c "import json, jsonschema; \
       schema = json.load(open('schemas/autonomous_execution_record.schema.json')); \
       data = json.load(open('docs/autonomous_execution/examples/pilot_evidence/codex_corrective_loop_pilot.json')); \
       jsonschema.validate(instance=data, schema=schema); print('SCHEMA VALID')"
   SCHEMA VALID
   ```

## Pass/fail outcome

**Pass.** The full loop was observed end to end:

```
defect registration (iter-001, commit 76b64561, red test)
  -> bounded fix (iter-002, commit cba47c4, one minimal change)
  -> affected check rerun (val-pilot-002: focused test, green)
  -> regression (val-pilot-003/004: full pytest suite + all six scripts, all pass)
  -> revalidation (execution record acceptance_scopes.corrective_loop: pass)
```

## Scope-acceptance verdict

`overall_delivery: pass` (a corrective iteration was required and
completed — `pass_no_corrective_iteration_required` does not apply here,
per the pilot spec).

## Lineage update (adoption cleanup)

`parent_execution_id` in
`docs/autonomous_execution/examples/pilot_evidence/codex_corrective_loop_pilot.json`
was added retroactively during pre-merge adoption cleanup of the AES PR
stack (#225-#230), pointing to `exec-aes-crossproject-pilot-001` (the
Phase 5 cross-project handoff pilot's root execution). The Phase 5 pilot
report had flagged that this record's parent link only existed in the
Phase 5 handoff record, not reciprocally here. Since no PR in the stack is
merged yet, this is an additive field change to unfrozen evidence, not a
rewrite of any test result, defect description, hash, or command output.

## Gaps / notes for the canonical standard

- No gaps found in the corrective-loop contract itself; the acceptance
  criteria in `docs/pilots/AES_CODEX_PILOT.md` ("Acceptance for the pilot
  itself") were all directly checkable against this run.
- The schema's `parent_execution_id` convention for "no real prior
  execution recorded" (`null`) worked cleanly and matches the convention
  already used in the Phase 1 illustrative examples.
- This pilot run did not need to exercise the "same check fails twice ->
  stop and report residual risk" path, since the single fix succeeded.
  That path remains validated only by the normative spec text
  (`AUTONOMOUS_EXECUTION_STANDARD.md` Section 9.7), not by an observed
  run, and would need a second, separate pilot fixture to exercise for
  real if that evidence gap matters later.

## Governance note

This is a **Phase 2 pilot**, governed by
`AUTONOMOUS_EXECUTION_STANDARD.md` Section 19 ("Adoption phases": Phase 1
normative package -> Phase 2 Codex pilot -> ...) and Section 20 ("Next
owner": completion of Phase 1 "does not authorize: pilot execution,
semantic enforcement, CI blocking, merge, deploy, or production
adoption" — this pilot is the separate Phase 2 execution that section
anticipates). It demonstrates the corrective-loop contract on an
isolated fixture; it does **not** authorize semantic enforcement, CI
blocking, or any change to `.github/workflows/*`.

Note: the task brief that requested this pilot referenced
"spec Section 45.1" for this governance claim. No Section 45.1 exists in
`AUTONOMOUS_EXECUTION_STANDARD.md` (the document has 20 sections) — the
correct citations are Sections 19 and 20 above, used in this report and
the PR description instead.
