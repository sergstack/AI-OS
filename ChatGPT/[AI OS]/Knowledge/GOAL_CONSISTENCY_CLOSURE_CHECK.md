# Goal-Consistency Closure Check

## Purpose

This is a reusable view of the existing AES Closure Review, not a second state
machine or acceptance ledger. It verifies that a candidate result closes the
original goal, not merely its local checks.

## Closure record

```text
closure_check_id:
owner_project:
original_goal_ref:
acceptance_ref:
final_evidence_ref:
deterministic_checks_status: pass | fail | not_run
original_goal_status: satisfied | revise | blocked
acceptance_criteria_status: satisfied | revise | blocked
owner_boundary_status: preserved | violated | unknown
goal_consistency_status: pass | revise | blocked
material_gap:
verdict:
```

## Decision rule

`checks passed` is necessary where checks apply, but never sufficient for
`pass`. A pass requires all of the following: deterministic checks pass,
original goal is satisfied, acceptance criteria are satisfied, and the owner
boundary is preserved. A missing or weakened material requirement is `revise`;
missing acceptance evidence or a hard owner-boundary violation is `blocked`.
Human acceptance remains governed by AES and project rules.

## Smoke scenarios

| Case | Deterministic checks | Goal | Acceptance | Owner boundary | Verdict |
|---|---|---|---|---|---|
| `CLOSURE-001` scoped docs result | pass | satisfied | satisfied | preserved | pass |
| `CLOSURE-002` green checks, goal missed | pass | revise | revise | preserved | revise |
| `CLOSURE-003` missing owner authority | pass or not applicable | blocked | blocked | violated | blocked |

`CLOSURE-002` is mandatory: no local green result may be reported as complete
when it does not satisfy the original goal.

## Boundaries and rollback

This check neither grants authority nor automatically merges, promotes, or
corrects work. A `revise` or `blocked` verdict returns to the existing AES
corrective path or owner boundary. Rollback is the existing revert/manual
review path for the affected result.
