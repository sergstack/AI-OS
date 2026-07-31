# Plan

## Missing inputs

- None for repository implementation. External ChatGPT Project creation and upload remain manual owner actions.

## Scope assumptions

- The inspected Thinkers OS repository state dated 2026-07-31 is the evidence baseline for bounded portfolio and synthesis summaries.
- `MANIFEST.json` remains the package manifest for `[AI OS]`; `PROJECT_REGISTRY.md` is the cross-project registry.

## Affected files / areas

- `ChatGPT/[Thinkers OS]/`
- `PROJECT_REGISTRY.md`, `REPO_PATHS.md`, and `UPLOAD_GUIDE.md`
- Inbox Router and AI OS routing files
- project-enumerating validation scripts and tests
- `docs/thinkers_os_integration/`

## Steps

1. Lock allowed files/actions and confirm implementation readiness.
2. Create the `[Thinkers OS]` behavior kernel, local guidance, status, granular Knowledge, and rollback rules.
3. Create two compact bundles, their authoritative upload list, and source fingerprints.
4. Add bounded entries to project/path registries, upload guidance, Inbox Router routing, and AI OS routing.
5. Extend only validators that enumerate ChatGPT Projects or Knowledge indexes.
6. Add regression tests for the project contract and all twelve smoke cases.
7. Run targeted validators/tests, fix one local in-scope failure if needed, then run the full repository validation suite.
8. Record observed smoke results and complete the acceptance audit.
9. Inspect the final diff, stage only scoped files, commit, and push the non-main branch to `sergstack/AI-OS`.

## Dependencies

- Step 2 depends on Step 1.
- Step 3 depends on Step 2 because fingerprints cover granular source files.
- Step 5 depends on Steps 2 and 4 because validators require the new paths and registry entry.
- Step 6 depends on Steps 2–5.
- Step 7 depends on Step 6.
- Step 8 depends on observed Step 7 results.
- Step 9 depends on a passing Step 8 acceptance audit.

## Risks

- Bundle content and fingerprints may diverge if generated in the wrong order.
- Routing changes may blur maintenance versus real-decision application.
- Repository smoke evidence cannot prove unsynced external Project behavior.

## Validation strategy

- Run project-instruction length, public safety, goal-mode, manifest/path, bundle, and index validators.
- Run targeted Thinkers OS integration tests and the complete pytest suite.
- Check bundles for forbidden source payloads and local paths.
- Map every SPEC acceptance criterion to a file or observed command result.
- Re-run the relevant checks after final documentation changes and before commit/push.

## Parallel work

- None. Bundle fingerprints and acceptance evidence require ordered execution.
