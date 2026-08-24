# SPEC

## Goal

Implement issue #268: add a universal, bounded AES Closure Review before successful terminal acceptance and expose it thinly to all seven registered ChatGPT projects.

## Current state

- AES v1.0.0 permits `validating` or `revalidating` to reach `completed` directly.
- The v1 schema has no closure record; existing v1 examples are historical evidence.
- An advisory semantic validator enforces SEM-001 through SEM-008.
- All seven projects have registered Knowledge Bundle exposure surfaces.

## Requirements

- Require a Closure Review context, correctable-gap gate, invariant sweep, authority separation, bounded closure iterations, and freshness after closure corrections.
- Preserve current status namespaces and the stricter Codex one-fix rule.
- Use a compatible schema/validator contract, examples, deterministic acceptance cases, and a PR #4 retrospective fixture.
- Update the registry, seven thin bundle exposures, upload manifests when applicable, and the sync checklist without claiming live UI sync.

## Constraints

- AES remains the single canonical semantic owner; extensions remain domain-specific and thin.
- No runtime orchestrator, autonomous merge/deploy, production promotion, historical-record rewrite, or scope expansion.
- Schema compatibility decision: retain valid v1 records with an additive optional `closure_review`; enforce it semantically only for closure-aware successful records.
- Do not merge the PR.

## Acceptance criteria

- Issue #268 AC1–AC10 are represented by deterministic fixtures/tests or documented retrospective evidence as allowed.
- Canonical AES, schema, semantic validator, status/migration docs, examples, registry, all seven bundles, manifests, and sync checklist are consistent.
- Repository checks and relevant tests pass with LDW-parsed evidence.
- Rollback and live-sync boundaries are explicit; merge remains not performed.

## Risks

- An optional additive field can be omitted from a new successful record unless the semantic validator distinguishes closure-aware records.
- Bundle fingerprints may drift when canonical AES changes.
- Repository evidence cannot prove live ChatGPT Project synchronization.
