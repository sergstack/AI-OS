# Migrated Bundle Semantics

Canonical source created during Issue #285 provenance migration.
Legacy bundle provenance: `ChatGPT/[AI OS]/Knowledge_Bundles/AIOS_02_GOVERNANCE_AND_EVIDENCE.md`.

## Legacy section: `ChatGPT/[AI OS]/Knowledge/GOVERNANCE_RULES.md`

Do not use this pattern to justify autonomous retrieval:
## Autonomous Execution Standard
`[AI OS]` is the canonical owner of the Autonomous Execution Standard (AES).
Execution across all projects now also follows the canonical loop defined in
`AUTONOMOUS_EXECUTION_STANDARD.md` at the repo root: requirements -> execution
-> validation -> defect registration -> corrective action -> affected-scope
rerun -> revalidation -> scope acceptance -> final evidence. It does not
replace Goal Mode, routing, autonomy policy, or the merge policy in
`GOAL_MODE.md`; it connects them into one closed loop, and the stricter rule
wins on any conflict. `[AI OS]` also owns the generic project-extension
interface in `AUTONOMOUS_EXECUTION_EXTENSION_CONTRACT.md`, which a project
implements to add domain-specific defect subtypes, evidence, and acceptance
scopes without restating the canonical state machine or schema.
New AES v2 records require Closure Review: it rechecks original goal, scope,
invariants, final-evidence freshness, rollback, and owner boundary before
terminal acceptance. Historical v1 evidence remains read-only.
For an `Invoke AI-OS` execution, the AES `continuation` envelope is the
canonical durable state: it preserves the original goal and acceptance
criteria, owner, stage, scope/routing references, and freshness hashes. Warm
resume verifies that state; an unchanged source revision alone is insufficient.
The bounded supervised corrective-loop classification does not permit
autonomous agents, generic agentic workflows, or expanded authority.
After routing resolves a primary owner for a material decision or deliverable,
an upstream project may prepare evidence, contradictions, options, risks, and a
bounded handoff, but it must not silently replace that owner. The handoff keeps
the affected decision boundary, requirements, constraints, acceptance, and
first safe step so the receiving owner can continue without re-decomposing the
goal.
