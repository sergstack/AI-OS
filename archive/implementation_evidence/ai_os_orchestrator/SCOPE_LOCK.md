# Scope Lock

## Allowed files

- `.agents/skills/ai-os-orchestrator/SKILL.md`
- `AGENTS.md`
- `GOAL_MODE.md`
- `COMMAND_SURFACE.md`
- `ChatGPT/[AI OS]/Knowledge_Bundles/AIOS_04_GOAL_PACKS_AND_COMMAND_SURFACE.md`
- `docs/CODEX_GLOBAL_AI_OS_ENTRY_POLICY.md`
- `tests/test_aios_dual_surface.py`
- `archive/implementation_evidence/ai_os_orchestrator/*`

## Forbidden files

- `PROJECT_CAPABILITIES.yaml` except read-only validation
- Existing project methodology and granular Knowledge content
- User-local Codex configuration
- Runtime, secret, deploy, provider, and production files

## Allowed actions

- Add one repository skill.
- Make minimal canonical instruction and documentation edits.
- Refresh the one derived bundle whose source fingerprint changes.
- Update contract tests and run read-only validation.
- Commit, push, and open a PR after checks if credentials and repository policy allow it.

## Forbidden actions

- Manual merge or auto-merge decision.
- Production promotion or deployment.
- New routing registry, copied routing table, autonomous agent workflow, or broad refactor.
- Destructive rollback.

## Public behavior

Public behavior may change only to make canonical AI-OS goal intake automatically invoke the new orchestrator. Existing direct routing, strict task packages, owner capabilities, and simple local-only work must remain available.
