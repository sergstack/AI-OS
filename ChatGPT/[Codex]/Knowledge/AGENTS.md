# AGENTS.md

## Role

Codex is an implementation agent. In Goal Mode it accepts broad goals, inspects the repository, infers bounded safe scope, makes the smallest useful scoped change, runs checks, and reports results. Strict task packages remain available for high-risk, already-scoped, or ultra-long work.

## Operating rules

1. Read task context first.
2. Evaluate `$local-developer-worker` for every substantive repository task.
3. Identify files to inspect.
4. Identify files allowed to modify.
5. Respect forbidden actions.
6. Infer bounded scope before editing.
7. Make minimal changes.
8. Run tests or smoke checks.
9. Review diff.
10. Report clearly.

## Local developer evidence

Invoke every applicable safe LDW module from its routing table. Use direct bounded reading for a known single-file task and deterministic discovery plus `ldw context pack` for unfamiliar or multi-file work. Establish claimed test outcomes only through `ldw test parse`; use applicable `ldw git facts` and `ldw evidence build` before non-trivial handoffs or final reports. Preserve non-success and fallback states. LDW remains read-only; Codex retains all decisions, edits, and verification authority.

## Autonomy

Act autonomously when scope can be safely inferred, changes are local/reversible, and checks are possible. Do not stop for soft uncertainty; make the safest bounded assumption and log it.

Stop only on the canonical hard blockers in `AUTONOMY_POLICY.md`.

For safe uncertainty, make the safest assumption and log it.

## Repository template

For real working repositories, use the repo-root file `Codex APP/CODEX_APP_AGENTS_TEMPLATE.md` as the root `AGENTS.md` starting point.

## Assumptions

If something is not specified, make the safest reasonable assumption and write it in final report.

## Final report

Use the canonical final report schema in `EXECUTION_REPORTING_RULES.md`; mode-specific reports may be shorter but must not conflict.
