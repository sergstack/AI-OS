# Autonomous Execution Standard — Adoption Plan

Canonical standard: `docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md`.
Extension contract: `docs/standards/AUTONOMOUS_EXECUTION_EXTENSION_CONTRACT.md`.

## Current repository state

This is a historical phase plan. The phase descriptions below retain their
original intended deliverables and exit criteria; they are not the current
completion ledger.

Repository evidence at baseline `21526a812e5ea4823c64815b84f6792f10b563dd`
shows that the Phase 1 package and the following follow-up work are merged:

- Phase 2 Codex isolated-fixture pilot — `docs/pilots/AES_CODEX_PILOT_RESULTS.md`;
- Phase 3 artifact-freshness pilot — `docs/pilots/AES_ARTIFACT_PILOT_RESULTS.md`;
- Phase 4 Analytics synthetic-fixture pilot and the single current project
  extension — `docs/autonomous_execution/extensions/ANALYTICS_EXTENSION.md`;
- Phase 5 cross-project handoff pilot — `docs/pilots/AES_CROSS_PROJECT_PILOT_RESULTS.md`;
- scoped advisory Phase 6 semantic validator —
  `scripts/validate_autonomous_execution_record.py`;
- compact bundle exposure for the projects recorded in `PROJECT_REGISTRY.md`.

These are repository/merge facts only. They do not prove current ChatGPT UI
sync, external smoke execution, owner acceptance, production authorization,
or deployment. No separate Codex extension was adopted: the canonical AES
keeps the existing stricter Codex one-fix policy, and current applicability
decisions are recorded in `PROJECT_REGISTRY.md` rather than inferred from
this historical plan.

## Phase 1 — normative package (this task)

Delivers: canonical standard, state model, status namespaces, declarative
schema, extension contract, migration map, example records, acceptance-case
specification, pilot specifications, this adoption plan, and thin
references from existing canonical entry documents (`GOAL_MODE.md`,
`README.md`, `REPO_PATHS.md`).

Historical Phase 1 did not deliver: any per-project extension file, any pilot
execution, a semantic validator, or CI enforcement. This describes the
original package only; it is not a claim about the current repository.

Exit criteria: PR opened against `main`, owner review pending, not merged.

## Phase 2 — Codex pilot

Separate issue and PR. Scope: `docs/pilots/AES_CODEX_PILOT.md`. Produces a
real `[Codex]` execution extension (path decided during this phase, per
`docs/standards/AUTONOMOUS_EXECUTION_EXTENSION_CONTRACT.md` Section 6) and one real,
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

## Phase 6 — semantic enforcement (historical plan; partially delivered)

Originally required a separate, explicit owner decision, taken only after Phases 2-5
have produced enough real evidence to justify it. In scope for Phase 6
only: a semantic validator, duplicate-ID checks, cross-field invariants,
stale-artifact enforcement, stale-test enforcement, iteration-limit
enforcement, handoff-ID enforcement, allowed-path enforcement, and
optionally a blocking CI integration. The read-only advisory validator now
exists and covers SEM-001…011; blocking CI, runtime enforcement, and any
broader semantic coverage remain separately unauthorized.

## What Phase 1 completion authorizes

Phase 1 completion authorizes exactly one thing: opening a PR for owner
review of the normative package. It does not authorize pilot execution,
semantic enforcement, CI blocking, merge, deploy, or production adoption
(`docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md` Section 20).

## PR-as-delivery-mechanism statement

```text
The implementation PR is a delivery mechanism.
The Autonomous Execution Standard does not automatically create,
approve, merge or deploy pull requests.
```
