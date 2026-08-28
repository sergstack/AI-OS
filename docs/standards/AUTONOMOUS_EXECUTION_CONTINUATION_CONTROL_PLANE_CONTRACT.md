# AES Continuation Control Plane Contract

Status: normative continuation semantics; implementation is additive and
optional for existing AES records.

Canonical owner: `[AI OS]`.  Implementation owner: `[Codex]`.

## Boundary

AES is the control-plane hub for an active multi-owner execution. `[Thinking]`,
`[Analytics]`, `[LLM]`, and `[Codex]` retain domain ownership. The controller
routes, records, and terminates; it does not execute domain work, validate its
own work, or make owner decisions.

`[Thinking]` is invoked only for: a decision between alternatives, evidence
conflict, changed downside, owner decision required, strategic interpretation
of downstream results, or restatement of the original problem. Completing an
upstream owner's work is not a trigger and no owner is a mandatory transit.

## Conceptual model

The continuation envelope has exactly five conceptual entities:

1. `goal` — immutable original goal, scope reference, and terminal
   disposition;
2. `acceptance` — immutable original criteria and their hash;
3. `trace` — current owner/stage, ordered route trace, signatures, deltas,
   and refusals;
4. `progress` — satisfied and remaining original criteria plus last real
   progress; and
5. `guards` — named limits, observations, tripped guard, and stop report.

Current owner/stage belong to `trace`; terminal disposition belongs to `goal`
and is referenced by `guards`. They are not additional entities.

## Routing and operations

After every hop, select the next route from remaining original acceptance
criteria, required evidence, and authorized ownership—not owner adjacency.
`execute`, `validate`, and `decide` are separate: an executor does not make a
material decision, a validator does not alter criteria or implement a remedy,
and a decision owner does not recompute domain work merely to decide.

Acceptance is monotonic. A downstream owner cannot silently widen, narrow, or
reinterpret the original criteria. Work beyond them becomes a scope-change
proposal and stops for owner decision before execution.

## Repeat routes and guards

A repeat route requires a named `evidence_delta`: `new_evidence`,
`changed_assumption`, `failed_validation`, `changed_acceptance_interpretation`,
`new_owner_instruction`, or `implementation_feedback`. Without one, record
`repeat_route_refused_missing_evidence_delta`; choose another authorized route
or stop using the existing AES terminal mapping.

Four independent guards have named, initially unset parameters:
`max_continuation_hops`, `max_retries_per_owner`, `max_no_progress_hops`, and
`route_signature_history_window`. Their semantics are respectively hop count,
repeat visits per owner, consecutive non-progress against original criteria,
and cyclic route signatures. A disk change alone is not progress.

When multiple guards trip together, record all. Precedence is route-signature
cycle, per-owner retry limit, no-progress counter, then hop budget. Guards do
not authorize extra corrections or weaken Codex's one-correction limit.
Calibrate values only after 3--5 real multi-project executions, recording the
population, false stops/refusals, proposed values, and owner decision.

## AES mapping

All machine-readable values remain lowercase `snake_case`; this contract does
not change the existing execution, requirement, acceptance-scope, or delivery
enums.

| Continuation condition | AES handling |
| --- | --- |
| Hop budget exhausted | `stopped` / `iteration_limit_reached`, with `overall_delivery: partial` when criteria remain and an owner-decision report. |
| No acceptance progress | `stopped` / `continuation_no_progress_limit_reached`. This additive terminal reason is required because a repeated defect is not the same condition. |
| No authorized route | `stopped` / `hard_blocker`, or `required_external_action_not_authorized` for that specific case. |
| Failed validation | Existing failed requirement/acceptance path and corrective loop; use `validation_unavailable` only when validation cannot run. |
| Partial acceptance | Existing `overall_delivery: partial`. |
| Scope widening | `stopped` / `scope_boundary_violation` with `authority_status: owner_review_pending`. |

A guard stop records completed and remaining criteria, route trace, last real
progress, proposed next route, guard observations, evidence deltas/refusals,
and risk of continuing. Budget exhaustion is an autonomy boundary, not a
blocker. Closure requires all original mandatory criteria with current AES
evidence; an intermediate handoff or check cannot close the goal.
