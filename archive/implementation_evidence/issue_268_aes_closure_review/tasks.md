# Tasks

## Preparation

- [x] Read canonical instructions, issue #268, AES sources, registry, and project exposure surfaces.
- [x] Create a branch from `origin/main`.
- [x] Classify schema compatibility as additive and preserve historical v1 records.

## Scope lock

- [x] Use only `SCOPE_LOCK.md` allowed paths; preserve existing stricter project policies.

## Implementation

- [x] Define canonical Closure Review semantics and migration boundary.
- [x] Extend schema, semantic validator, and validator tests.
- [x] Add acceptance-case and retrospective coverage.
- [x] Refresh registry and all seven thin project exposures.

## Validation

- [x] Run focused validator/schema tests via LDW parsing.
- [x] Run applicable repository policy, manifest, bundle, and index checks.
- [ ] Review final diff, freshness, and rollback readiness.

## Acceptance mapping

- [ ] Map AC1–AC10 and Definition of Done to evidence in `ACCEPTANCE_CHECK.md`.

## Forbidden actions

- Do not add a runtime platform, autonomous external action, new competing status namespace, broad project copies of AES, or a merge.
- Do not widen Codex corrective policy or represent repository updates as live UI synchronization.

## Documentation

- [ ] Record final acceptance, changed-file manifest, rollback, and live-sync boundary.
