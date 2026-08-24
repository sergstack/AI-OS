# Plan

## Missing inputs

- None.

## Scope assumptions

- Issue #268 is the executable task contract.
- A closure-aware record declares `standard_version: 1.1.0`; historical `1.0.0` records retain their existing structural validity.

## Affected files / areas

- Canonical AES, extension/status/adoption/acceptance documentation, schema, examples, validator, and tests.
- Project registry, seven registered bundles and upload/sync manifests.
- Issue-specific evidence and rollback/acceptance records.

## Steps

1. Record compatibility and scope gates, then define the closure-review contract in canonical AES and extension/status documentation.
2. Add the additive closure record to the schema, closure-aware examples, and semantic rules/tests for successful terminal records.
3. Add deterministic AC1–AC10 coverage and the PR #4 retrospective mapping.
4. Update seven thin bundle exposures, registry references, fingerprints/manifests, and honest sync statuses.
5. Run focused tests and repository checks; repair in-scope defects and re-run affected validation.
6. Perform final acceptance and closure review, record rollback/evidence, commit, push, and open a non-merged PR.

## Dependencies

- Step 2 depends on Step 1.
- Step 3 depends on Step 2.
- Step 4 depends on Step 1.
- Step 5 depends on Steps 2–4.
- Step 6 depends on Step 5.

## Risks

- See `SPEC.md`.

## Validation strategy

- JSON Schema validation, focused validator tests, existing repository checks, bundle/manifest checks, and final acceptance mapping.

## Parallel work

- None; shared canonical contract requires ordered changes.
