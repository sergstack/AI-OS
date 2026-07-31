# Plan

## Missing inputs

- None for repository implementation. External ChatGPT upload and behavioral smoke remain manual.

## Scope assumptions

- The active status source is `ChatGPT/[Thinkers OS]/Knowledge/SYNTHESIS_AND_EXPORT.md`; upstream registry/Judge records are inspection evidence, not files to copy.
- All five current active provisional patterns are included; isolated author patterns and pilot candidate revisions are excluded.

## Affected files / areas

- `ChatGPT/[Thinking]/PROJECT_INSTRUCTIONS.md`, status, setup, smoke, Knowledge index, four Thinkers artifacts, bundle README, bundles 01/04, and upload list.
- `tests/test_thinking_thinkers_integration.py`.
- `docs/thinkers_thinking_integration/`.

## Steps

1. Lock scope and pass the implementation guard.
2. Add the four granular Thinking artifacts from bounded Judge-pass synthesis evidence.
3. Add bundle 04 and make the router operational in Thinking instructions/guidance without changing ownership.
4. Update the upload list, Knowledge index, existing bundle 01 mirror, and all affected fingerprints.
5. Add smoke/regression tests for routing, precedence, anti-bloat, conflict review, logging, provenance, and content safety.
6. Run targeted and full repository validation; record report-judge, second-opinion, and acceptance evidence.
7. Inspect and stage only scoped files, commit, and push the feature branch without merge.

## Dependencies

- Step 2 depends on Step 1.
- Step 3 depends on Step 2.
- Step 4 depends on Steps 2–3 because fingerprints cover final source bytes.
- Step 5 depends on Steps 2–4.
- Step 6 depends on Step 5.
- Step 7 depends on a passing Step 6 acceptance audit.

## Risks

- Bundle/source drift if fingerprints are calculated before final documentation edits.
- Ownership drift if `[Thinking]` appears to maintain corpus or synthesis status.
- Static smoke evidence can be mistaken for external Project execution.

## Validation strategy

- Run all six repository validators, targeted integration tests, full pytest, and sync readiness.
- Verify exact bundle sources/fingerprints, exact upload-list inclusion, empty application history, forbidden-content boundaries, and feature-branch scope.

## Parallel work

- None; source projection, index mirrors, and fingerprints require ordered execution.
