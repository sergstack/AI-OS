# AIOS AutoResearch v0.2 — Live-Execution, Privacy, Budget & Evidence Contract

- Status: `candidate`, `contract_version: "0.2.0"`. Not authorized for any live call on its own — see §10/§15 and `docs/standards/autoresearch_v02_authority_matrix.json`.
- Owner: co-owned `[AI OS]` (governance) / `[Codex]` (implementation), per issue #409's role boundary.
- Parent: [#388](https://github.com/sergstack/AI-OS/issues/388) → v0.1 (closed, `docs/evidence/AUTORESEARCH_PARENT_FINAL_QA_2026-09-03.md`) → [#409](https://github.com/sergstack/AI-OS/issues/409) → v0.2. Defining child: [#411](https://github.com/sergstack/AI-OS/issues/411). Depends on: [#410](https://github.com/sergstack/AI-OS/issues/410) (merged).
- Companions: `schemas/autoresearch_v02_live_batch_config.schema.json` (per-batch machine-readable contract) and `docs/standards/autoresearch_v02_authority_matrix.json` (fixed authority-boundary declaration).

## What this extends, and what it does not replace

This is an **additive v0.2 layer** on top of the accepted v0.1 foundation, not a rewrite. It reuses, unchanged, by direct reference rather than restatement:

- `docs/standards/AUTORESEARCH_V01_CONTRACT.md` and `docs/standards/autoresearch_v01_manifest.json` — the mutable/protected surfaces and hard invariants remain controlling (issue #409's own Safety boundary: *"v0.1 hard invariants remain controlling unless a stricter additive v0.2 rule is accepted"* — no such stricter rule is introduced here).
- `schemas/autoresearch_{eval_case,experiment_record,batch_manifest,observation_row,semantic_finding}.schema.json`, `scripts/autoresearch_{validator,shadow_runner,decision_comparator}.py` — all confirmed reuse-unchanged by #410's audit; this contract does not modify any of them.
- `docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md`'s canonical status namespaces (`execution_state`, `authority_status`, `merge_status`, `production_status`, etc.) — v0.2 does not create a second state machine or status namespace; every enum below either reuses an AES value directly or is a narrowly-scoped addition specific to a live-batch concept AES has no equivalent for (e.g. `transport_authority_status`).
- `ChatGPT/[AI OS]/Knowledge/FAILURE_REGISTRY.md`'s attribution vocabulary (`attributable | uncertain | ineligible`) — reused unchanged for field-observation attribution (§9).

v0.1's own experiment records and evidence documents (#392's ledger, #396's calibration, #397's pilot) remain immutable historical evidence, per this contract's own Core rule below — nothing here retroactively edits or re-scores them.

## 1–3. Evidence states, transport identity, evaluator identity

Reused verbatim from #409/#410 rather than redefined:

- **`repo_replay`**: AI-OS context assembled deterministically from a named Git revision and delivered through an authorized transport. Not automatically equivalent to the ChatGPT Project UI's own context assembly (§12).
- **`field_observation`**: a sanitized capture of something actually observed in live day-to-day AI-OS Project use. Evidence that a response occurred — nothing more.
- **`field_reproduction`**: replaying a `field_observation`'s same input under `repo_replay`. A **separate** evidence state from the original observation, and it may fail to reproduce — that is itself informative, not an error to hide.

**Transport identity** (per-batch, `schemas/autoresearch_v02_live_batch_config.schema.json`): `transport_id`, `transport_version`, `credential_source_class` (`browser_session_cookie | oauth_keychain | api_key_env | none`), `transport_authority_status` (`not_authorized | authorized_pending_budget | authorized`). Per #410's audit, the currently selected candidate is `playwright_mcp` (`credential_source_class: browser_session_cookie`) with `claude_in_chrome` as a fallback pending an owner decision on real-account use (§10) — neither is `authorized` by this contract; both remain `not_authorized` until an owner decision sets a specific batch's `transport_authority_status`.

**Evaluator identity**: `evaluator_contract_hash` (sha256 of the frozen files `ChatGPT/[LLM]/Knowledge/AUTORESEARCH_SEMANTIC_EVALUATOR_CONTRACT.md` — reused unchanged, #394) and `evaluator_model_identity`. The Judge's own model/provider/runtime identity is captured with the same rigor as the subject's (§11's role separation applies to *context*, not to *identity capture completeness*).

## 4. Context-pack identity and source-revision requirements

A `context_manifest_hash` (sha256 over the concatenated, canonically-ordered content of every file a `repo_replay` context pack draws from) is required on every batch, `null` only before the context compiler (#412, not yet built) produces one. This hash is the source-revision identity §11's "same accepted transport/model/runtime/context construction, except the declared mutation" rule checks baseline against candidate with.

## 5. External-action preview/authority/commit/verify sequence

Reuses AES §13.2 verbatim, applied to a live provider call as the "external action" it is: `PLAN -> PREVIEW EFFECT -> AUTHORITY CHECK -> COMMIT -> VERIFY`. Concretely for a live batch: plan the exact call set (case IDs, transport, model, budget envelope) → preview it against `docs/standards/autoresearch_v02_authority_matrix.json`'s `live_call_authority`/`usage_budget_authority` (both `owner_only`) → the owner's explicit authorization for *that specific envelope* is the authority check → only then may a call commit → the call's actual result (not the plan) is what gets verified and recorded. A preview is not authorization, per AES's own rule, reused unchanged.

## 6. Call/token/time/cost budget contract

Every field in `schemas/autoresearch_v02_live_batch_config.schema.json`'s budget block (`max_provider_calls`, `max_input_tokens`, `max_output_tokens`, `max_wall_clock_minutes`, `max_cost_amount`, `max_cost_currency`) is **required to be present in the schema** (so it is always addressable) but **may be `null`** until an owner sets it — `null` is the honest, correct value before authorization, never a fabricated default (Forbidden actions: *"No... default paid budget"*). The validator (§ Checks) enforces the one rule the schema alone cannot express: **`authority_status` may only be `"authorized"` when `max_cost_amount` is a positive number and `max_cost_currency` is set**, for any `credential_source_class` this contract classifies as potentially usage-billed. A browser-session transport (`playwright_mcp`, `claude_in_chrome`) has no *AutoResearch-side* per-call cost today (§10's `cost_model` finding from #410), but the *target site's own* usage (e.g. a rate-limited or metered ChatGPT account) is a real, separate cost the owner's `max_cost_amount` decision must still cover if applicable — this contract does not assume `browser_session_cookie` implies "free."

Every call, **including retries and Judge calls**, consumes budget (Core rule, reused verbatim from issue #411's own text).

## 7. Retry and cancellation policy

`retry_limit` (schema: 0–5, matching this repository's own established corrective-loop ceiling discipline) and `call_timeout_seconds` are both required, per-batch fields. A retry that exhausts the limit, a timeout, a provider error, a missing response, or invalid structured output all map to an explicit `inconclusive`/`missingness_reason`-style outcome (reusing #395's `missingness_reason` enum shape) — **never** to a silent pass, per this contract's own Core rule (*"Timeout, cancellation, provider error, missing response, invalid structured output, or budget exhaustion cannot become PASS"*).

## 8. Privacy, redaction, retention, and forbidden-input rules

Fail-closed field-trace intake policy (issue #411's own text, retained as the canonical statement rather than paraphrased):

- redact secrets, credentials, personal/sensitive business data, and unrelated raw context before any field trace is ever written to a file this contract governs;
- preserve prompt/response provenance and the minimal context needed for reproduction — no more;
- every field trace carries an explicit `field_trace_provenance` value: `none | sanitized | synthetic | raw_restricted`;
- **`raw_restricted` traces are never committed to this public repository** — the schema's own conditional (`allOf`) enforces `raw_payload_retention: not_retained` whenever `field_trace_provenance: raw_restricted`, so a raw-restricted trace cannot simultaneously claim to be retained;
- committed evidence uses hashes, metadata, curated excerpts *within this policy*, or external references — never a raw dump;
- deletion/retention rules never permit rewriting a past experiment's recorded decision (append-only, reusing #392's ledger discipline unchanged).

`redaction_policy_ref` on every batch record is a pointer into this section (`AUTORESEARCH_V02_LIVE_CONTRACT.md#8-privacy-redaction-retention-and-forbidden-input-rules`), not a restatement, so the redaction rule has exactly one canonical location.

## 9. Live versus synthetic evidence labels

`synthetic_evidence_allowed_for` is a closed enum: `unit_test | contract_test | negative_control | calibration_deterministic_layer` — the same four uses v0.1 already legitimately made of hand-authored data throughout #392–#397, named explicitly so a future batch cannot silently expand the list. `live_evidence_required: true` on any batch means every `synthetic`-labeled row in that batch is disqualified from contributing to `keep_candidate`/`discard` — it may still validate the deterministic machinery (exactly as #396's Phase 0 already did), but it cannot stand in for a live Judge or live subject response (issue #411's own non-acceptance example: *"Test-double output satisfies a live gate"*).

Field-observation attribution reuses `FAILURE_REGISTRY.md`'s `attributable | uncertain | ineligible` vocabulary unchanged (§ "What this extends").

## 10. Researcher/evaluator/controller/owner authority boundaries

Formalized in the companion `docs/standards/autoresearch_v02_authority_matrix.json`: `implementation_authority` (`bounded_delegate`), `live_call_authority` (`owner_only`), `usage_budget_authority` (`owner_only`), `candidate_acceptance_authority` (`owner_only`), `active_configuration_authority` (`not_granted`), `merge_authority` (`not_granted`), `production_authority` (`not_granted`). **No implicit conversion is permitted** between these — an available/configured credential does not grant `live_call_authority`; a granted `usage_budget_authority` for one envelope does not extend to a different one. The Researcher role (once #415 exists) may propose one shadow hypothesis/patch; it cannot modify frozen evals, approve itself, alter active configuration, merge, deploy, or advance the batch baseline — reused verbatim from issue #409's own Role and authority boundary text. The Judge never receives candidate identity, hypothesis, preferred result, or promotion authority (blind by construction, reusing #394's contract unchanged) — enforced structurally by `schemas/autoresearch_semantic_finding.schema.json`'s absence of any such field (#394, unchanged, verified again in this issue's own Checks).

**Owner decision recorded from #410, restated here as the concrete first application of this boundary**: whether v0.2's first live batch uses `playwright_mcp` (a fresh, unauthenticated browser profile requiring an explicit sign-in) or `claude_in_chrome` (the owner's real, already-logged-in ChatGPT session — higher fidelity, materially different privacy posture) remains open and is `live_call_authority`/`usage_budget_authority`-gated, not decided by this contract.

## 11. Reproducibility and model/provider drift rules

Baseline and candidate must use the **same** accepted transport/model/runtime/context construction, except the one declared mutation (Core rule, reused verbatim) — enforced at the code level by `autoresearch_shadow_runner.reject_config_mismatch` (#393, reuse-unchanged per #410) and `autoresearch_validator.reject_environment_mismatch` (#392, reuse-unchanged), both already exercised against exactly this class of drift. A model/provider/context/evaluator drift between baseline and candidate yields an invalid comparison, mapped to `inconclusive` — never averaged away or silently corrected (reusing #395's non-inferiority method unchanged).

## 12. Acceptable limitations when exact UI-runtime reproduction is unavailable

Reused from #410 §5 rather than re-derived: `repo_replay` via a transport that is *not* the actual, already-configured AI-OS ChatGPT Project (e.g. a fresh Playwright session pasting context into a new chat) is a **lower**-fidelity approximation than driving the real, already-configured Project itself. No claim of UI-runtime equivalence is made anywhere in this contract, its schema, or any evidence document it governs (Forbidden actions, reused verbatim: *"No claim that repo replay is identical to the ChatGPT Project UI"*). Every evidence document downstream of this contract must carry this same limitation explicitly rather than omit it.

## 13. Hard stop conditions

Reusing #409's own Revisit/stop triggers as this contract's `abort_conditions` vocabulary rather than inventing a parallel list: no authorized reproducible live transport; live Judge cannot distinguish obvious cases or is materially order-biased; repo replay lacks useful fidelity; live calls cannot be bounded/audited; no reproducible failure or supported attribution; Researcher proposals repeatedly violate minimality/protected scope; candidate effects are dominated by variance; validation improvement does not transfer to holdout; governance/privacy/integrity regression; manual review gives equivalent value at materially lower cost/complexity (the exact finding v0.1's own #398 final QA already reached once, §"What this extends"); provider/model/privacy/cost/scope/authority changes. Every batch's `abort_conditions` array (schema, non-empty) must be a subset or superset of this canonical list, not a divergent one.

## 14. Rollback/evidence-preservation ownership

No active behavior is ever changed by any v0.2 batch (Safety boundaries, reused: *"Active ChatGPT Project settings and main are not experiment targets"*). Rollback is therefore always: close the PR, or restore only the new contract/manifest/schema/tests/evidence files this contract or a downstream child added — never edit or delete a v0.1 or prior v0.2 record (append-only, §9). `[Codex]` owns rollback mechanics; `[AI OS]` owns whether a rollback is warranted.

## 15. Phase 0/Phase 1 authorization boundary

Mirrors v0.1's own successful pattern (#396 → #397) rather than inventing a new one: Phase 0 live calibration (#417) may proceed once #412–#416 are each individually accepted/merged, `live_call_authority` and `usage_budget_authority` are both explicitly granted for a *specific, bounded* calibration envelope, and this contract's schema validates that envelope. Phase 1 (#418, capped at 5 experiments per #409's own dependency graph — note this is a **stricter** additive cap than v0.1's Phase 1, which allowed up to 10; consistent with §"What this extends"'s "stricter additive v0.2 rule" allowance) requires a **separate, later** `usage_budget_authority` grant — Phase 0's budget authorization does not implicitly extend to Phase 1 (§10's no-implicit-conversion rule, applied across phases as well as across batches).

## 16. Compatibility map to v0.1 schemas, manifests, and hard invariants

| v0.1 artifact | v0.2 relationship |
|---|---|
| `autoresearch_v01_manifest.json` | Unchanged; v0.2's search-space scope is identical (#409's own Scope section matches #388's verbatim) |
| `schemas/autoresearch_experiment_record.schema.json` | Unchanged in this issue; #410 §2 recommends one additive `provenance`/`capture_method` field, deferred to whichever of #412/#413 first needs to write a live record — not added here to keep this contract's own diff minimal and reviewable |
| `schemas/autoresearch_observation_row.schema.json` | Same deferral as above |
| `scripts/autoresearch_validator.py`, `autoresearch_shadow_runner.py`, `autoresearch_decision_comparator.py` | Unchanged; all three are provenance-agnostic per #410's audit and require no v0.2-specific edit |
| AES `authority_status`/`execution_state`/etc. | Unchanged; this contract's own `authority_status` enum (`owner_review_pending \| authorized \| rejected`) is a narrower, batch-scoped value that maps onto AES's broader vocabulary without redefining it |

## 17. Controlled-L1 subject-context boundary and native-Project transfer (L2)

Additive tightening ([LLM]→[Codex] handoff, 2026-09-05), triggered by a real
session finding: a `repo_replay` batch that pastes its rendered context into
a chat opened *inside* a named, live ChatGPT Project (e.g. `[AI OS]`) is not
a clean baseline/candidate comparison. The Project's own real, already-live
instructions and knowledge apply **on top of** the pasted text for both
arms, so the comparison actually measured `[Project] + pasted-baseline` vs.
`[Project] + pasted-candidate` — a real observation, but not evidence about
the effect of replacing the Project's own instructions, and not something
this contract's §12 fidelity-limitation language alone made clear enough to
prevent.

**Two new required batch-config fields** (`schemas/autoresearch_v02_live_batch_config.schema.json`),
both enforced fail-closed by `Controller.run_experiment` itself (not
expressible in JSON Schema conditionals alone, same pattern as §6's cost
rule):

- `subject_context_scope`: `non_project_controlled | native_project`. A
  `repo_replay` causal comparison MUST declare `non_project_controlled` — a
  neutral transport with no named-Project instructions/knowledge active.
  `native_project` is declared but not runnable by any code path this
  contract version implements; it exists only to name the field's opposite
  value honestly, reserved for a future, separately-authorized L2 contract
  (below). `run_experiment` blocks with zero calls if this is anything but
  `non_project_controlled`.
- `memory_personalization_isolation_status`: `verified_disabled | unverifiable | not_applicable`.
  Account-level ChatGPT memory/personalization/custom-instruction influence
  on the Subject transport must be proven excluded, not merely assumed
  absent because the chat isn't inside a named Project folder. Only
  `verified_disabled` satisfies the precondition; `unverifiable` fails
  closed exactly like an unset budget field does in §6 — it is never
  silently treated as `verified_disabled`.

**Owner revise, 2026-09-05 — a self-declared string is not evidence.** The
first review of this section correctly rejected it: both fields above are
plain batch-config strings anyone could set without anything actually
checking them. Fixed for `subject_context_scope`, honestly flagged as still
open for `memory_personalization_isolation_status`:

- **`subject_context_scope` is now machine-verified per call, not merely
  declared.** `RawCapture.page_url` — the real URL the live transport
  observes via its own `browser_snapshot` at submission time — was already
  being captured but was silently discarded before ever reaching a
  persisted record. It is now threaded through `LiveInvocationResult`
  (`observed_page_url`) into the ledgered invocation record
  (`schemas/autoresearch_live_invocation.schema.json`), and `invoke()`
  cross-checks it: a batch declaring `non_project_controlled` whose
  observed URL matches a named-Project pattern (`/g/g-p-<id>-<slug>/`,
  confirmed from real captures this session) is refused
  (`termination_status: scope_violation`) rather than silently accepted.
  `target_url_prefix` alone (`https://chatgpt.com/`) cannot distinguish a
  bare chat from a named Project — both match it — so this check does not
  rely on that field at all.
- **`memory_personalization_isolation_status` has no implemented
  verification mechanism in this codebase and none is claimed here.**
  Account-level memory/personalization state is not observable from this
  transport's surface without a capability this contract does not yet
  have (e.g. a confirmed technical signature for ChatGPT's own
  "Temporary Chat" mode, not verified live in this session and therefore
  not invented as a check). Every record `Controller.run_experiment`
  produces now carries a mandatory `causal_validity_status` object
  (`schemas/autoresearch_manual_candidate_evaluation.schema.json`) stating
  this split plainly:
  `subject_context_scope_verification: machine_verified_per_call_observed_url`,
  `memory_personalization_isolation_verification: self_declared_not_machine_verified`.
  A clean `pilot_decision` can never be read as proving both preconditions —
  the second is, and remains, an assertion. Designing a real verification
  mechanism for this dimension is separate, not-yet-started work; until it
  lands, no result from this pipeline should be treated as fully
  causally-valid on this axis, consistent with this contract's own original
  rule that an undemonstrated precondition blocks a causal claim rather
  than downgrading to a weaker one.

**Mutation-visibility gate**: a patch existing in Git is not itself
experimental treatment. `Controller.run_experiment` now requires
`equivalence_report(...)`'s `mutable_surface_excerpt.excerpt_differs` to be
`true` (and the excerpt `present`) before any Subject/Judge call — if the
declared mutation is absent from the rendered Subject payload, the batch is
discarded, not silently trusted. Zero calls occur past either new gate or
this one.

**L2 — native `[AI OS]` transfer validation — is named here as a future
contract shape only.** It re-tests whether an L1-qualified candidate's
behavior survives inside the real, native Project once actually applied to
the intended Project Instruction/routing surface, under separate owner
authorization for the temporary mutation, with exact settings read-back and
mandatory rollback. **No code path in this repository implements L2.** It
does not re-estimate causal effect, does not re-open a passed L1 result, and
a transfer failure vetoes promotion even when L1 passed; a transfer
`inconclusive` leaves L1's own evidence intact but blocks any native-adoption
claim. Defining and authorizing L2 is separate, later work.

## Checks

- `python3 -m json.tool schemas/autoresearch_v02_live_batch_config.schema.json` and the authority matrix — both parse.
- `jsonschema.Draft7Validator.check_schema(...)` — schema is a valid draft-07 document.
- `tests/test_autoresearch_v02_live_contract.py` proves, with fixtures, every one of this issue's own "Checks" bullets: a `synthetic`-only batch cannot validate as satisfying `live_evidence_required: true`; an `authorized` batch without a positive `max_cost_amount` fails; a Judge finding (`schemas/autoresearch_semantic_finding.schema.json`, reused unchanged) still structurally cannot carry an authority/merge/production field (re-confirms #394's existing guarantee under the new contract); `raw_restricted` + any `raw_payload_retention` other than `not_retained` fails the schema's own conditional; the authority matrix has exactly the 7 required authorities, each with exactly one of the 3 defined levels, and `merge_authority`/`production_authority`/`active_configuration_authority` are all `not_granted`.
- `tests/test_autoresearch_md2_calibration.py` proves §17's three batch-level gates through the real `Controller.run_experiment`, not by inspection alone: `subject_context_scope: native_project` blocks with zero calls; `memory_personalization_isolation_status` other than `verified_disabled` blocks with zero calls; a declared mutation whose `mutable_surface_excerpt.excerpt_differs` is `false` (patch in Git, absent from the rendered payload) is discarded with zero calls. The same file's existing four-control calibration (beneficial/harmful/no-op/mixed) still passes with the two new required fields present, unchanged in outcome.
- `tests/test_autoresearch_live_browser_adapter.py` proves the per-call transport-scope verification directly against `invoke()`: an observed URL matching the named-Project pattern is refused (`scope_violation`) even though it satisfies `target_url_prefix`; an observed bare-chat URL passes and is persisted in the record via `observed_page_url`; an unknown `subject_context_scope` value is rejected at `TransportPolicy` construction, before any call is possible.
