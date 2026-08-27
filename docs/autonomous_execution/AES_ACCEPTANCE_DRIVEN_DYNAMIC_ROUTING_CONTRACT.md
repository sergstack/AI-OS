# AES Acceptance-Driven Dynamic Routing Contract

Status: contract only; not-yet-schema.  Canonical owner: `[AI OS]`.

## Control plane and ownership

AES is the one control-plane hub for a multi-owner continuation. It preserves
the original goal, acceptance state, route trace, progress, and guards; it is
not a `ChatGPT/[...]` project. `[Thinking]`, `[Analytics]`, `[LLM]`, and
`[Codex]` remain owners of their domain work.

The controller separates `execute`, `validate`, and `decide`: an executor does
not make a material owner decision, a validator does not change acceptance or
implement a remedy, and a decision owner does not recompute domain work merely
to decide. `[Thinking]` is invoked only for a decision between alternatives,
evidence conflict, changed downside, owner decision required, strategic
interpretation of a downstream result, or restatement of the original problem.
Completion of another owner's work is not a trigger.

## Acceptance-driven dynamic routing

The route is derived at execution time, never fixed at intake or inferred from
the prior owner:

```text
current state + remaining acceptance criteria + new evidence
+ routing rules (ownership) + governance constraints -> next owner
```

`current state` includes the durable AES record, prior route trace and guard
observations. `remaining acceptance criteria` are the original criteria not
yet satisfied with current evidence. `new evidence` is a named evidence delta.
`routing rules` are the ownership rows in `ROUTING_RULES.md`; `governance
constraints` include authority, scope, safety, and stricter domain limits.

The output must be an owner assigned by that mapping: calculation to
`[Analytics]`, strategic decision to `[Thinking]`, prompt/LLM workflow to
`[LLM]`, and implementation to `[Codex]`. Skipping an owner is normal when no
remaining criterion maps to its work. A pre-planned sequence is an execution
artifact, never routing input.

When several remaining criteria map to different valid owners, choose the
owner for the criterion that blocks the largest number of other remaining
criteria; break ties by the earliest unresolved dependency recorded in the
acceptance state, then by the smallest stable criterion identifier. Record the
candidate criteria and tie-break evidence in the trace. `ROUTING_RULES.md`
resolves one-input ownership; this rule resolves multi-criterion priority.

When no remaining criterion maps to a registered capability, use the existing
`external`, `internal_non_capability`, or `owner_escalation` class in
`ROUTING_RULES.md`. Do not choose the nearest project. Preserve the unresolved
criterion and resulting terminal or owner-decision handoff.

## Five-entity conceptual model

Exactly five top-level conceptual entities exist: `goal`, `acceptance`,
`trace`, `progress`, and `guards`. `trace` contains current owner/stage,
ordered routes, signatures, deltas and refusals. `goal` contains terminal
disposition. This is conceptual and not-yet-schema; it must later remain
additive and optional.

Progress partitions original criteria into satisfied and remaining criteria;
a disk change is neither necessary nor sufficient. A repeat route requires one
or more of `new_evidence`, `changed_assumption`, `failed_validation`,
`changed_acceptance_interpretation`, `new_owner_instruction`, or
`implementation_feedback`. Otherwise refuse it and record
`repeat_route_refused_missing_evidence_delta`.

## Bounds, scope, and mapping

Named but unset parameters govern hop budget, per-owner retry limit,
no-progress counter, and route-signature cycle detection. If multiple guards
trip, precedence is cycle, per-owner retry, no-progress, then hop budget.
They do not weaken the Codex one-correction limit. Calibrate only after 3--5
real multi-project executions.

Acceptance is monotonic: no owner may silently widen, narrow, or reinterpret
the original criteria. A need beyond scope is a proposal that stops for owner
decision before execution.

| Condition | Existing AES handling |
| --- | --- |
| budget exhausted | `stopped` / `iteration_limit_reached`; owner-decision report, not blocker |
| no authorized route | `hard_blocker`, or `required_external_action_not_authorized` where applicable |
| validation failed | normal failed requirement/corrective loop; `validation_unavailable` only when it cannot run |
| partial closure | `overall_delivery: partial` |
| scope widening | `stopped` / `scope_boundary_violation` |

No-progress is a genuine gap: `repeated_defect_limit_reached` is about one
recurring defect, not stalled acceptance. The downstream `[Codex]` handoff may
add `continuation_no_progress_limit_reached` only after schema compatibility,
validator coverage, and focused tests are approved.

Budget exhaustion produces an owner-decision report with completed and
remaining criteria, trace, last real progress, proposed next route, and risk
of continuing. It is distinguishable from no path. This contract changes no
AES schema, validator, test, status enum, pilot, smoke, or promotion state.

## Downstream handoff

`[Codex]` may implement this accepted contract in a separate strict task:
optional additive schema fields, advisory validation, focused compatibility
tests, and rollback by reverting that bounded commit. No threshold values are
authorized by this contract.
