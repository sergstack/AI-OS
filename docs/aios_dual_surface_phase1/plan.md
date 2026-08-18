# Plan

## Scope

- `AGENTS.md`
- `PROJECT_CAPABILITIES.yaml`
- `.agents/skills/`
- `tests/test_aios_dual_surface.py`
- `docs/aios_dual_surface_phase1/`

Canonical `ChatGPT/**`, unrelated user changes, baseline worktrees, remote systems, and production state are excluded.

## Steps

1. Confirm branch, baseline tests, validators, and Skill dependencies.
2. Remove registry routing/governance semantics.
3. Retain and simplify only generic `project-context`.
4. Remove redundant router, evidence, Analytics, Thinking, and LLM Skills.
5. Replace tests of the duplicate routing framework with resolver, containment, canonical-routing ownership, and protected-path tests.
6. Rerun raw-input behavioral cases with context provenance.
7. Run targeted/full tests and canonical validators after the final change.
8. Complete acceptance, adversarial review, and rollback evidence.

## Validation strategy

- Parse the JSON-compatible YAML registry with the standard library.
- Verify relative entrypoints cannot escape their canonical project.
- Verify canonical routing remains in Inbox Router rather than the registry.
- Verify `project-context` is the only repository-local AI-OS Skill.
- Treat behavioral traces, not unit tests, as routing/context evidence.
