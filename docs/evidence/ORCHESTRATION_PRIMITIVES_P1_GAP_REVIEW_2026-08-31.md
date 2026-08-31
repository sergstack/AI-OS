# Orchestration Primitives P1 Gap Review — 2026-08-31

- Issue: [#344](https://github.com/sergstack/AI-OS/issues/344)
- Review scope: P1.1–P1.4 only
- Semantic owner: `[AI OS]`
- Implementation owner: `[Codex]`
- Baseline: `origin/main` at `abd2346`
- Decision status: Judge-ready gap review; owner review pending

## Decision

Only P1.3 exposes a current contract gap, and that gap is partial rather than
material. The existing effect boundary protects authority, intent consistency,
and post-commit verification, but it does not state whether an action can be
safely replayed or how duplicate commits are prevented. No recorded duplicate
effect has been observed, so this review does not authorize implementation.

P1.1, P1.2, and P1.4 do not justify a contract change under current evidence.
P2 and P3 remain outside this task. No framework, runtime, dependency, deploy,
or production promotion is authorized.

## Classification matrix

Each primitive has exactly one classification from the issue taxonomy.

| Primitive | Classification | Current coverage | Evidence-based finding | Smallest next change |
| --- | --- | --- | --- | --- |
| P1.1 Execution journal contract | `not needed` | AES already records ordered iterations, requirement status history, validation runs, external actions, handoffs, continuation route trace, and evidence references with timestamps/revisions. | No recorded case shows that an execution could not be reconstructed from the AES record. Adding a second journal now would duplicate canonical state without an observed recovery or chronology defect. | None. Revisit only after an observed reconstruction ambiguity, lost transition, or recovery failure that the AES record cannot explain. |
| P1.2 Explicit WAIT/RESUME contract | `already sufficient` | The continuation envelope preserves the original goal and acceptance criteria, owner, `resume_stage`, record/scope/routing references, source revision, hashes, authority provenance, progress, route trace, and guards. Warm resume requires compatibility checks; owner review pending is distinct from a stopped execution. | Current evidence includes a successful cross-project resume and no observed durable-wait failure inside an authorized machine-callable boundary. A new generic `WAIT` state would currently mirror existing stopped/owner-review/continuation semantics rather than close an evidenced gap. | None. Revisit when a real wait case needs a named external signal or deadline that cannot be represented by the present continuation and authority fields. |
| P1.3 Idempotency contract for side effects | `partial gap` | Every declared side effect follows `PLAN -> PREVIEW EFFECT -> AUTHORITY CHECK -> COMMIT -> VERIFY`; the schema records an intent fingerprint, commit state, authority recheck, and verification evidence; SEM-015 enforces those boundaries. | The contract has no stable idempotency key, provider/action replay capability, attempt identity, or rule that blocks a second commit after an already completed action. This is a real semantic omission, but no duplicate effect or unsafe replay has been observed, so it is not a material gap. | Open a separate strict, owner-approved P1.3 contract task. Do not implement it in this review. |
| P1.4 Workflow logic vs effectful activity separation | `already sufficient` | The continuation controller routes and records but does not execute or validate domain work. `execute`, `validate`, and `decide` are explicitly separate. Side effects are declared as `external_actions` behind an effect boundary and explicit authority. | No evidence shows control logic silently performing an undeclared effect or an effectful worker redefining acceptance or authority. A new “activity” abstraction would add terminology without changing the enforced boundary. | None. Revisit only after an observed boundary violation that the current controller/external-action separation cannot prevent or represent. |

## Evidence inspected

- `docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md`: state machine,
  requirements/status history, validation freshness, external authority,
  effect-boundary invariant, rollback, and resume rules.
- `docs/standards/AUTONOMOUS_EXECUTION_CONTINUATION_CONTROL_PLANE_CONTRACT.md`:
  controller boundary, separate execute/validate/decide operations, route trace,
  progress, evidence deltas, and guards.
- `schemas/autonomous_execution_record.schema.json`: continuation and
  `external_action.effect_boundary` machine-readable shapes.
- `scripts/validate_autonomous_execution_record.py` and
  `tests/test_autonomous_execution_validator.py`: SEM-015 authority,
  preview/commit-intent, and verification enforcement.
- `docs/autonomous_execution/AUTONOMOUS_EXECUTION_ACCEPTANCE_CASES.md` and
  `tests/test_autonomous_execution_schema.py`: current structural and semantic
  acceptance surface.
- `docs/evidence/DURABLE_RUNTIME_GAP_PHASE0_2026-08-31.md`: no observed crash
  state loss, duplicate effects, invalid closure, or lost retry state; P3 is
  therefore not authorized.
- `CURRENT_STATUS.md`: three Dual Surface live routes required zero manual
  orchestration and one cross-project case preserved continuity.

Repository statements are contract evidence, not proof of external runtime
behavior. Dated live-test records are bounded observations, not universal
reliability claims.

## Bounded P1.3 follow-up candidate

This is a proposed scope for a later owner-approved task, not an implementation
authorization.

Allowed files:

- `docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md`
- `schemas/autonomous_execution_record.schema.json`
- `scripts/validate_autonomous_execution_record.py`
- `docs/autonomous_execution/AUTONOMOUS_EXECUTION_ACCEPTANCE_CASES.md`
- `tests/test_autonomous_execution_schema.py`
- `tests/test_autonomous_execution_validator.py`

Required design decision by `[AI OS]`: whether replay metadata is required for
all declared side effects or only actions with a replay-capable provider, and
whether attempts belong inside one action record or in a separate bounded
attempt list. The design must preserve compatibility for existing non-replayed
records and must not imply that every provider supports idempotency.

Minimum acceptance cases:

1. `test_external_action_replay_contract_is_additive`: a replay-capable action
   records a stable key tied to the approved intent, while existing
   non-replayed records remain compatible under the accepted migration policy.
2. `test_completed_action_replay_key_cannot_commit_twice`: a completed action
   cannot produce a second commit from the same replay key.
3. `test_changed_intent_requires_new_key_and_authority_check`: a materially
   changed intent requires a new authority check and replay key.
4. `test_unsupported_replay_is_explicitly_blocked`: an action/provider without
   replay protection is explicitly replay-blocked, not reported as safely
   idempotent.

Rollback for that future task must be a scoped revert of the contract, schema,
validator, acceptance cases, and tests. It must not depend on a runtime service
or data migration.

## Scope and adoption gates

- P1.3 implementation: `not_authorized`; owner decision required.
- P2 adoption: `not_planned` in this issue stage.
- P3 durable runtime: `blocked` by the Phase 0 evidence gate.
- Framework/dependency adoption: `not_authorized`.
- Merge: owner review pending.
- Production: not authorized.

## Judge-ready verdict

`pass` for completeness of the requested P1 gap review, not for adoption of the
four primitives. The matrix assigns one permitted classification to every P1
item, identifies the only bounded follow-up candidate, names its exact files
and acceptance cases, preserves rollback, and leaves all higher phases closed.
