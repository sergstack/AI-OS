# Migrated Bundle Semantics

Canonical source created during Issue #285 provenance migration.
Legacy bundle provenance: `ChatGPT/[Codex]/Knowledge_Bundles/CODEX_02_EXECUTION_AUTONOMY_REPORTING.md`.

## Legacy section: `ChatGPT/[Codex]/Knowledge/AUTONOMY_POLICY.md`

For normal bounded repo work, use `Goal Mode Contract` in `GOAL_MODE.md` as the named reusable standard for autonomy, execution order, forbidden actions, reporting, PR/merge-gate posture, and no-deletion-without-quarantine rules.
If the same validation target still fails, the one-fix budget is exhausted for
that target and the independently evidenced defect it represents. Stop further
file-changing corrections for that target and report:

## Legacy section: `ChatGPT/[Codex]/Knowledge/EXECUTION_REPORTING_RULES.md`

## Autonomous Execution Standard
Execution in `[Codex]` now also follows the canonical Autonomous Execution
Standard defined in `docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md` at the repo root
(canonical owner: `[AI OS]`). It sits above `AUTONOMY_POLICY.md`,
`CODEX_LONG_RUN_PLAYBOOK.md`, and `EXECUTION_REPORTING_RULES.md` as a shared
loop — requirements, execution, validation, defect registration, corrective
action, revalidation, and scope acceptance — without replacing any of them or
the merge policy in `GOAL_MODE.md`. The `[Codex]` AES extension at
`docs/autonomous_execution/extensions/CODEX_EXTENSION.md` adds only
Codex-specific evidence, validation, acceptance, freshness, and authority
detail; it does not expand authority or numeric limits. New v2 Closure Review
rechecks repository trust boundaries, regression coverage, diff/freshness, and
rollback; its ceiling never widens `max_corrective_fixes_per_failed_check: 1`.
For an `Invoke AI-OS` continuation, the canonical AES envelope preserves the
original goal, acceptance criteria, resolved owner, stage, and freshness state;
it does not turn a local completed step into terminal acceptance.
Once routing resolves a material decision or deliverable owner, `[Codex]`
keeps that boundary: it may execute a bounded handoff and preserve its
evidence, contradictions, constraints, acceptance, and first safe step, but it
must not silently replace the resolved owner's judgment.
