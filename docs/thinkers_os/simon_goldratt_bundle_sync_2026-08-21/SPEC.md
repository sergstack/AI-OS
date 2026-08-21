# SPEC

## Goal

Synchronize the Judge-pass Herbert A. Simon and Eliyahu M. Goldratt packages into the canonical AI-OS Thinkers OS and Thinking upload bundles, then publish the change through a dedicated worktree and pull request.

## Current state

- Operational Thinkers OS records both authors as complete P0/P1 packages with Judge pass.
- The canonical AI-OS bundles do not mention Simon, Goldratt, Bounded Decision Design, or Constraint-First Flow Review.
- The five active provisional synthesis patterns must remain unchanged.

## Requirements

- Update the Thinkers OS portfolio snapshot from 10 to 12 registered authors, from 8 to 10 complete packages, and from 10 to 12 Judge-pass packages.
- Register Simon and Goldratt as isolated Judge-pass author patterns pending a separate synthesis refresh.
- Project the two isolated patterns into the Thinking synthesis bundle without adding them to the active Lens Router or five-pattern synthesis set.
- Refresh every affected bundle source fingerprint and the Thinkers OS upload-list fingerprints.
- Validate bundles and focused integration contracts.
- Commit and publish the dedicated branch, then open a non-draft PR for the deterministic Merge Gate.

## Constraints

- Do not include books, normalized text, excerpts, source manifests, logs, or local absolute paths.
- Do not modify Project Instructions, active synthesis pattern status, Lens Router, Conflict Map, schemas, scripts, or tests.
- Keep `owner_acceptance: pending`, `canonical_status: false`, and `production_status: NOT AUTHORIZED`.
- Codex must not manually merge the pull request.

## Acceptance criteria

- Both names and both pattern titles occur in the appropriate canonical granular and bundle files.
- The active synthesis set remains exactly five patterns.
- Source fingerprints match the current listed sources.
- Knowledge-bundle, Thinkers OS integration, Thinking integration, and public-safety checks pass.
- The worktree is clean after commit, the branch is pushed, and a non-draft PR targets `main`.
- Merge status is reported from the GitHub Merge Gate without a manual Codex merge.

## Risks

- A content-only bundle change could accidentally imply synthesis promotion.
- Fingerprints will be stale if granular sources and bundles are not updated together.
- GitHub auto-merge depends on repository-side checks and settings outside local control.
