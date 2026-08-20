# Tasks

## Preparation

- [x] Read canonical repository instructions, registry, project-context, command surface, routing, handoff, Goal Mode, and merge policy.
- [x] Create an isolated branch and worktree from current `origin/main`.
- [x] Run LDW doctor, inventory, and bounded context selection.

## Scope lock

- [x] Allow only the files listed in `SCOPE_LOCK.md` and preserve the capability registry as a location resolver.

## Implementation

- [x] Add `.agents/skills/ai-os-orchestrator/SKILL.md`.
- [x] Make the orchestrator the default AI-OS goal entry in canonical instructions and command surface.
- [x] Align reusable global-entry documentation with the new skill.
- [x] Update routing-contract tests.

## Validation

- [x] Run focused routing-contract tests.
- [x] Run the full repository test and canonical check set.
- [x] Parse every claimed test outcome through LDW.
- [x] Run independent Judge review and address correctable in-scope defects.

## Acceptance mapping

- [x] Verify every SPEC requirement against changed files and observed checks.
- [ ] Record risks, rollback, acceptance, and branch/PR status.

## Forbidden actions

- Do not change domain routing semantics outside the canonical Inbox Router rules.
- Do not add the orchestrator as a domain capability in `PROJECT_CAPABILITIES.yaml`.
- Do not load or duplicate complete Knowledge trees.
- Do not modify user-local Codex configuration, deploy, promote, or merge.

## Documentation

- [x] Keep default entry documentation concise and reference-based.
