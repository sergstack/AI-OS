# Scope Lock — AI OS Dual Surface Phase 1 Simplification

## Allowed files

- `AGENTS.md`
- `PROJECT_CAPABILITIES.yaml`
- `.agents/skills/aios-router/**`
- `.agents/skills/project-context/**`
- `.agents/skills/aios-evidence/**`
- `.agents/skills/analytics/**`
- `.agents/skills/thinking/**`
- `.agents/skills/llm/**`
- `tests/test_aios_dual_surface.py`
- `docs/aios_dual_surface_phase1/**`

## Allowed actions

- Remove redundant Phase 1 Skills after dependency and uniqueness checks.
- Reduce the registry to location resolution.
- Keep one generic bounded context loader.
- Update only related tests and compact Phase 1 evidence.
- Run local tests, validators, Git facts, and behavioral context checks.

## Forbidden files and actions

- No edits, moves, or renames under `ChatGPT/**` or `Codex APP/**`.
- No edits to unrelated user work, baseline `.codex/worktrees`, business logic, formulas, schemas, public APIs, validation scripts, secrets, runtime, deployment, or production state.
- No replacement router, classifier, governance framework, dependencies, commit, push, PR, merge, publish, or deploy.

## Public behavior rule

Canonical project behavior and paths remain unchanged. Codex adds only location resolution and bounded canonical context loading.
