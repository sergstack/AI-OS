# Local-First Compute Policy

- Status: candidate policy; ready for owner review
- Canonical owner: `[AI OS]`
- Execution-mechanics owner: `sergstack/local-developer-worker` (LDW)
- Production promotion: not authorized

## Purpose

Use local models when the work is safe, useful, measurable, cheaper than the
frontier path, and cheaply verifiable before it can affect acceptance or an
external side effect. This policy owns eligibility, evidence, promotion,
fallback, provenance, and authority boundaries. LDW owns bounded execution,
local Ollama transport, schema enforcement, telemetry, and escalation
mechanics.

No local output becomes an observed fact, accepted policy, owner instruction,
or authority merely because a local execution completed successfully.

## Selection order

For equivalent outcomes, choose the first applicable path:

1. deterministic local operation;
2. bounded retrieval or search;
3. local-model semantic operation with the required verifier;
4. frontier-model reasoning;
5. human material decision.

Do not use semantic inference for a result that an existing deterministic tool
can establish authoritatively. Test status belongs to the test parser; Git
state belongs to Git facts; calculations and reconciliations belong to their
deterministic owners.

## Eligibility decision

Before frontier reasoning, ask:

> Can this step be locally offloaded and verified cheaply enough that its
> expected error is detected before acceptance, authority, or a side effect?

All of the following must be true for a local route:

- the input is bounded, sanitized, and policy-permitted;
- the output remains candidate inference until its declared verification;
- a failure or uncertain result has an explicit deterministic, frontier, or
  human fallback;
- the verifier is independent of the local model's confidence;
- the route cannot grant authority or perform an undeclared effect;
- the class has the registry status needed for that use.

## Registry statuses

The canonical machine-readable registry is
`docs/standards/local_first_task_class_registry.json`; its schema is
`schemas/local_first_task_class_registry.schema.json`.

| Status | Meaning |
| --- | --- |
| `local_first` | Representative real-task evidence passed, owner promotion is recorded, and the declared verification/fallback remains mandatory. |
| `candidate_review` | Local execution may be piloted or used only as candidate output with the declared stronger review; it is not a promoted route. |
| `frontier_floor` | The task requires frontier reasoning unless a separate evidence-backed policy revision changes the floor; material owner decisions still remain human. |
| `blocked` | Local-model execution is forbidden for this class under the current policy. |

The initial production `local_first` allowlist is empty. Synthetic evidence may
prove containment or technical shape, but cannot promote a real task class.

## Current class boundary

Candidate-review classes include high-volume semantic terminal triage, bounded
text extraction/classification, non-authoritative summarization, repository
candidate ranking, similarity candidates, anomaly candidates, and first-pass
hypotheses or reviews. Each retains the verifier and fallback declared in the
registry.

Material architecture/governance reasoning, Closure Review, acceptance, and
material financial conclusions have a frontier floor or stricter owner gate.
Owner-only decisions, residual-risk acceptance, merge/deploy/production
authorization, and external side-effect authority are blocked from local-model
ownership. Deterministic truth establishment is also blocked from semantic
substitution: use the authoritative deterministic tool instead.

## Promotion contract

A class may move to `local_first` only through an owner-reviewed registry
change backed by a matched evaluation that records:

- a representative real-task corpus and immutable task identifiers;
- the same task, revision, budget, timeout, verifier, and acceptance rule for
  control and candidate arms;
- deterministic or stronger-model acceptance results;
- quality/error comparison, including false accept/reject where applicable;
- end-to-end latency including every review step;
- frontier-provider token use when observable;
- bytes/context presented to the frontier model when observable;
- local compute burden when observable;
- failures, outliers, and fallback/escalation rate;
- privacy/data-boundary assessment;
- an explicit disable/rollback path.

Missing measurements remain `unknown`, never zero. Context-byte reduction is
not token, latency, or task-success evidence. A successful local call is not a
semantic-quality verdict. Telemetry alone cannot promote a class.

## Progressive disclosure

Material Codex work follows:

```text
goal and constraints
-> bounded context pack
-> inspect selected and excluded evidence
-> expand only for a named missing-context reason or deterministic trigger
```

Every pack retains inclusion/exclusion reasons. Expansion is bounded and linked
to the prior package. Do not claim token savings unless provider tokens are
observed in a matched study.

## Loss-aware compaction

Preserve exactly or by durable source reference:

- original goal, scope, constraints, and acceptance criteria;
- requirement/defect IDs and current states;
- current iteration/continuation and authority state when applicable;
- evidence/source references, unresolved unknowns, and blockers;
- attempted actions when repetition could be harmful.

Repetitive discussion, rejected low-value alternatives, and verbose logs
already represented by deterministic evidence may be compressed. A summary is
a candidate representation, not replacement source evidence. Material use must
retain provenance and verification status.

## Provenance and authority

When a local result affects a downstream decision, record the task-class ID,
registry status, model-derived origin, source/evidence references, verifier
result, and fallback/escalation outcome. Preserve the canonical AES authority
classes; local inference is `candidate_research` or
`hypothesis_recommendation` and is never action-eligible by itself.

Frontier review is not owner approval. Verification is not acceptance.
Acceptance is not merge, deploy, production, or side-effect authorization.

## Security and failure behavior

Local inference remains fail-closed. Do not send secrets, credentials, raw
provider payloads, unapproved production/client/financial data, raw dumps, or
runtime artifacts solely for optimization. Do not persist prompts or model
responses unless a separately accepted evidence contract explicitly requires
and permits it.

Invalid schema, unavailable or unverified local endpoint, uncertain data
classification, missing verifier, quality regression, or changed intent causes
the declared fallback or a stop. A fallback must preserve the evidence class;
it must not silently report a frontier result as local or a model inference as
deterministic observation.

## Rollback and revisit

Rollback disables the local route for the affected task-class ID and returns
to its declared deterministic/frontier/human fallback. Canonical AI-OS
semantics, source evidence, and historical evaluation records remain intact;
no data migration or runtime service is required.

Revisit on a material model/hardware change, quality regression, material
frontier cost/latency change, LDW contract change, new deterministic verifier,
or telemetry that identifies a high-volume opportunity. Revisit evidence does
not change registry status without owner review.
