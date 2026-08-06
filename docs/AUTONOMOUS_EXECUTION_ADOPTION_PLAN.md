# Autonomous Execution Standard — Adoption Plan

Canonical standard: `AUTONOMOUS_EXECUTION_STANDARD.md`.
Extension contract: `AUTONOMOUS_EXECUTION_EXTENSION_CONTRACT.md`.

## Phase 1 — normative package (this task)

Delivers: canonical standard, state model, status namespaces, declarative
schema, extension contract, migration map, example records, acceptance-case
specification, pilot specifications, this adoption plan, and thin
references from existing canonical entry documents (`GOAL_MODE.md`,
`README.md`, `REPO_PATHS.md`).

Does not deliver: any per-project extension file, any pilot execution, any
semantic validator, any CI enforcement.

Exit criteria: PR opened against `main`, owner review pending, not merged.

## Phase 2 — Codex pilot

Separate issue and PR. Scope: `docs/pilots/AES_CODEX_PILOT.md`. Produces a
real `[Codex]` execution extension (path decided during this phase, per
`AUTONOMOUS_EXECUTION_EXTENSION_CONTRACT.md` Section 6) and one real,
isolated-fixture execution record demonstrating defect registration ->
bounded fix -> affected-check rerun -> regression -> revalidation. Does not
touch production branches or introduce a real defect into working code.

## Phase 3 — artifact pilot

Separate issue and PR. Scope: `docs/pilots/AES_ARTIFACT_PILOT.md`. Produces
one real execution record demonstrating the artifact-freshness contract
(Section 11.3 of the standard) end to end on one deterministic artifact
type (DOCX, XLSX, PDF, or PPTX).

## Phase 4 — Analytics pilot

Separate issue and PR. Scope: `docs/pilots/AES_ANALYTICS_PILOT.md`.
Produces a real `[Analytics]` execution extension and resolves the
`accepted: yes/no` -> `overall_delivery` domain-condition question left
open in `docs/AUTONOMOUS_EXECUTION_STATUS_MAPPING.md` Section 4.

## Phase 5 — cross-project pilot

Separate issue and PR. Scope: `docs/pilots/AES_CROSS_PROJECT_PILOT.md`.
Produces a real multi-hop handoff chain (`[Thinking] -> [Analytics] ->
[Codex] -> Judge`) and verifies that execution ID, parent execution ID,
requirement IDs, defect IDs, iteration count, evidence references,
acceptance scopes, and authority status all survive every hop.

## Phase 6 — semantic enforcement

Requires a separate, explicit owner decision, taken only after Phases 2-5
have produced enough real evidence to justify it. In scope for Phase 6
only: a semantic validator, duplicate-ID checks, cross-field invariants,
stale-artifact enforcement, stale-test enforcement, iteration-limit
enforcement, handoff-ID enforcement, allowed-path enforcement, and
optionally a blocking CI integration. None of this exists yet and none of
it is authorized by Phase 1 completion.

## What Phase 1 completion authorizes

Phase 1 completion authorizes exactly one thing: opening a PR for owner
review of the normative package. It does not authorize pilot execution,
semantic enforcement, CI blocking, merge, deploy, or production adoption
(`AUTONOMOUS_EXECUTION_STANDARD.md` Section 20).

## PR-as-delivery-mechanism statement

```text
The implementation PR is a delivery mechanism.
The Autonomous Execution Standard does not automatically create,
approve, merge or deploy pull requests.
```
