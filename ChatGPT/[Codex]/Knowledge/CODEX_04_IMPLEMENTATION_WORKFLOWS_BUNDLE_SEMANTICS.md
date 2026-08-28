# Migrated Bundle Semantics

Canonical source created during Issue #285 provenance migration.
Legacy bundle provenance: `ChatGPT/[Codex]/Knowledge_Bundles/CODEX_04_IMPLEMENTATION_WORKFLOWS.md`.

## Legacy section: `ChatGPT/[AI OS]/Knowledge/ANALYTICAL_MEMO_FACTORY_CODEX_APP_WORKFLOW.md`

`[Codex]` is the task package design layer. Codex APP is the executor layer.

## Legacy section: `docs/standards/EXISTING_SCRIPT_CONTROLLED_REFACTOR_STANDARD.md`

Engineering / Codex standard for cleaning or refactoring an existing working script or pipeline without losing useful behavior.
Use when an existing script, CLI, notebook-exported script, or pipeline already runs or has known useful output and Sergey asks for cleanup, controlled refactor, modularization, simplification, or removal of obsolete internal code.
Do not use for greenfield implementation, bug recovery, Analytics methodology, business definition work, output-contract changes without acceptance, production deploys, migrations, source mutation, or real provider/API execution without separate approval.
Core rule:
For large or risky refactors, use `Parent / Child Issue Gate Standard` from `docs/standards/PARENT_CHILD_ISSUE_GATE_STANDARD.md` by reference.
