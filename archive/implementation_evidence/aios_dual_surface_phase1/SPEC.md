# SPEC

## Goal

Keep one canonical AI-OS source of truth plus the smallest Codex integration layer: canonical routing, location resolution, bounded project-context loading, explicit handoff, and validation.

## Current state

- Seven `ChatGPT/[Project]` folders remain the canonical domain sources.
- Canonical routing is instruction-driven and owned by Inbox Router and project contracts.
- `PROJECT_CAPABILITIES.yaml` resolves capability IDs to canonical locations and context entrypoints.
- `project-context` is the only repository-local AI-OS skill and provides bounded loading with included/excluded provenance.
- The baseline manifest validator has 14 failures caused by existing nested `.codex/worktrees`.

## Requirements

- Preserve all seven canonical ChatGPT paths and methodology.
- Keep the registry location-only: no task taxonomy, governance blocks, domain methodology, or duplicated owner matrix.
- Keep `project-context` generic and limited to bounded context loading and provenance.
- Do not add a replacement router, classifier, governance layer, or domain skills.
- Preserve canonical ownership and explicit cross-project handoffs.
- Validate raw-input behavioral cases separately from static repository tests.

## Constraints

- Do not edit, move, or rename canonical `ChatGPT/**` files.
- Do not change business, financial, metric, schema, formula, API, or production behavior.
- Do not add dependencies, services, retrieval, vector, web, autonomous, secret, deployment, or external-write capabilities.
- Do not claim an independent classifier, technical routing enforcement, or production readiness.

## Acceptance criteria

1. All seven canonical paths and Project Instructions remain present.
2. The registry contains only schema, canonical paths, and relative context entrypoints.
3. Only generic `project-context` remains under `.agents/skills/`.
4. `project-context` does not classify requests or define domain methodology.
5. Five raw-input cases resolve to expected canonical projects with included/excluded provenance.
6. Thinking → Codex uses an explicit bounded handoff before implementation.
7. Targeted and full tests pass after the final relevant change.
8. Canonical validators pass or unchanged baseline failures are reported separately.
9. Rollback is local; production promotion remains no.

## Risks

- Natural-language routing remains an instruction-following judgment, not an independent classifier.
- Static tests can validate contracts and paths but cannot prove every future routing decision.
- Bounded context loading is procedural rather than a technical sandbox.
