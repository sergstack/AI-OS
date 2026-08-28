# Migrated Bundle Semantics

Canonical source created during Issue #285 provenance migration.
Legacy bundle provenance: `ChatGPT/[AI OS]/Knowledge_Bundles/AIOS_01_ROUTING_AND_WORKFLOW.md`.

## Legacy section: `ChatGPT/[AI OS]/Knowledge/PROJECT_ROUTING.md`

`ChatGPT/[Inbox Router]/Knowledge/ROUTING_RULES.md`.
If raw-input triage and AI OS scoped routing differ, use Inbox Router for
triage and this file for AI OS evidence/governance scope.

## Legacy section: `docs/standards/EXISTING_SCRIPT_CONTROLLED_REFACTOR_STANDARD.md`

This is an engineering/Codex standard, not Analytics methodology. It does not define business logic, metrics, formulas, or analytical conclusions.
Use `Existing Script Controlled Refactor Standard` when an existing script, CLI, notebook-exported script, or pipeline already runs or has known useful output, and Sergey wants cleanup, controlled refactor, modularization, simplification, or removal of obsolete internal code without behavior loss.
Do not use this standard for greenfield implementation, broken-script recovery, requested behavior/schema/metric/formula/API/provider/output-contract changes, production deploy, migration, source mutation, Safe Apply, real provider/API execution without approval, or cases where current behavior cannot be baselined.
Capture current command or entrypoint, representative input fixture/sample/dry-run path, output files/stdout/stderr, exit codes, filenames and locations, schema/columns/order/formatting, row counts or reconciliation totals, accepted warnings, known quirks, current tests, and before-refactor golden output where applicable.
Define filenames, locations, formats, schema, column names and order, deterministic formatting, CLI arguments/defaults, exit codes, stdout/stderr behavior, generated artifact policy, accepted warning/error behavior, and what counts as behavior change.
Any output contract change requires separate explicit acceptance.
Use the smallest meaningful safety checks: existing tests, focused regression tests, golden-output comparison, smoke run/dry-run, schema check, row-count or reconciliation-total check, CLI help/entrypoint check, artifact validation, `git diff --check`, or repo-specific validation scripts.
Allowed only after baseline, output contract, and safety checks exist: extract functions, split internal modules, rename internal helpers, isolate CLI/config/IO/transform/validate/report layers, remove truly dead or obsolete code, remove debug-only branches outside accepted behavior, replace duplicated internal logic with an equivalent helper, clarify comments/docstrings, and add focused tests around preserved behavior.
Forbidden without separate explicit acceptance: behavior changes, output contract changes, schema/column/file-format/file-location changes, metric/formula/business-rule/financial-control changes, dependency additions, provider/API behavior changes, real provider/API execution, migrations, production/runtime/deploy changes, broad rewrite, deleting tests/QA/validation, source data mutation, runtime artifacts outside accepted fixture policy, autonomous loops, embeddings, semantic search, vector DB, or web UI.
For large or risky refactors, use `Parent / Child Issue Gate Standard` from `docs/standards/PARENT_CHILD_ISSUE_GATE_STANDARD.md`. Do not duplicate the full parent/child standard.
Typical child issues: baseline and output contract; safety tests or golden checks; dead-code cleanup; module extraction; final before/after comparison. Do not start downstream cleanup/refactor child issues until baseline and safety-test child issues are accepted or merged.
Pass only when baseline behavior is captured, output contract is explicit, safety tests or comparison checks exist and run, cleanup stays in scope, before/after output is compared, output contract is preserved unless separately accepted, forbidden changes are absent, and final report lists changed files, checks, risks, rollback, and acceptance status.
Stop when current behavior cannot be run/inspected/baselined, output contract cannot be inferred safely, no meaningful safety test/comparison path exists, required input data is missing and no safe fixture can be used, the task requires secrets/local absolute paths/production systems/real provider/API/source mutation, preserving behavior conflicts with requested cleanup, or the requested change would alter schema, metrics, formulas, business rules, APIs, file formats, column order, or output locations without separate acceptance.
