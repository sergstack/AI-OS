# AES Codex Corrective-Loop Pilot Fixture

Status: **pilot evidence, not real functionality.**

This directory exists solely to provide durable, isolated evidence for the
Phase 2 Codex corrective-loop pilot specified in
`docs/pilots/AES_CODEX_PILOT.md` and executed under
`docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md` Section 9.5 (defect registration ->
bounded fix -> affected check rerun -> regression -> revalidation).

Nothing in this directory is imported by, or affects, any production code
path. `pilot_helper.py` is a small standalone module written specifically
for this pilot, deliberately shaped like a realistic utility function so the
corrective loop has something real to exercise, but it is not used anywhere
outside this fixture.

Files:
- `pilot_helper.py` - the fixture module under test. Ships in its
  **corrected** (post-pilot) state; see `docs/pilots/AES_CODEX_PILOT_RESULTS.md`
  and the execution record at
  `docs/autonomous_execution/examples/pilot_evidence/codex_corrective_loop_pilot.json`
  for the seeded defect and the exact before/after diff.
- `test_pilot_helper.py` - the focused regression test that caught the
  seeded defect (red) and now passes against the fix (green). It is part of
  the permanent pilot evidence and is safe to keep running in the normal
  `pytest tests/` baseline indefinitely.

Do not delete these files - they are the durable record that the corrective
loop was actually run, not merely described.
