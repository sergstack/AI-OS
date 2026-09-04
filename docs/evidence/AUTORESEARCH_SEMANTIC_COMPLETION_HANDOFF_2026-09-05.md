# AIOS AutoResearch — Semantic-Completion Handoff to [LLM] / [Analytics] / [AI OS] — 2026-09-05

Parent: [#409](https://github.com/sergstack/AI-OS/issues/409). Runtime:
`main`@`3b81126cb754a3b4021fa16666b418e62eda5c90` (PR #434, issue #433).

From: `[Codex]`. To: `[LLM]`, `[Analytics]`, `[AI OS]`. Status: **decision
request. No code, schema, evaluator, or comparator change made. No live
call made. No merge/promotion. STOP at this gate — do not resume
implementation without an explicit acceptance below.**

Trigger: a `[Thinking]`-authored candidate task package
(`AUTORESEARCH_SEMANTIC_COMPLETION_REVIEWED_V2.md`, reviewed-v2,
2026-09-05) asked `[Codex]` to preflight AutoResearch's measurement contour
and produce a bounded plan rather than execute. This document is that
plan's terminal deliverable: everything past this point requires an
owner/cross-project decision `[Codex]` is not eligible to make alone.

## Objective of this decision gate

Reach an accepted semantic-observation contract after which `[Codex]` can
implement and test an end-to-end path capable of distinguishing beneficial
/ harmful / no-op / mixed candidates — not to declare AutoResearch v0.2
"done," and not to run any further live call in the meantime.

## 1. Observed facts

1. **MD-2's mapping structurally forecloses ever detecting improvement.**
   `scripts/autoresearch_cli.py::_contributes_to_pair` maps a Judge's
   comparative `contributes` value to `(pass, pass)` when unambiguous, or
   `(None, None)` otherwise. `scripts/autoresearch_decision_comparator.py::evaluate_case_material_improvement`
   requires `severity(candidate) < severity(baseline)` in every matched
   pair. Equal values can never satisfy a strict `<`; excluded pairs never
   reach the check. Verified by direct reading of both functions on this
   revision, not inferred from one run's data — see
   `AUTORESEARCH_MD2_DECISION_PACKAGE_2026-09-05.md` §2 for the full
   derivation.
2. **This was already flagged, pre-merge, as an open item**, not a new
   discovery. `docs/evidence/AUTORESEARCH_V02_LIVE_LOOP_WIRING_2026-09-04.md`'s
   "Formal method review" scored MD-2 `blocked` and listed four candidate
   resolutions; the owner's actual ruling for PR #434 picked the most
   conservative one ("keep only the unambiguous step") explicitly as a
   narrow, non-general "minimal-for-C1" scope, explicitly deferring the
   rest.
3. **The subject never receives the literal mutated text.**
   `scripts/autoresearch_cli.py::_case_payload` sends
   `cpc.render_summary(ctx)` (a per-file manifest: path, source class, byte
   count, purpose) plus the frozen task text — never file contents. C1-R1's
   own captured payloads show only a 3-byte difference (`2596 bytes` vs.
   `2593 bytes`) as the sole trace of the mutation reaching the subject
   prompt. See `AUTORESEARCH_SUBJECT_CONTENT_PROPAGATION_MEMO_2026-09-05.md`.
4. **The live Judge's raw output was schema-noncompliant on 5 of 6 real
   attempts in the C1-R1 run** — unescaped quotes inside a JSON string
   value (3 cases), `evidence` supplied as an object instead of the
   required string (2 cases). These are genuine live-model formatting
   failures, not parsing bugs on the harness side: reproduced as
   regression fixtures in `tests/test_autoresearch_c1r1_regression.py`
   (`test_c1r1_unescaped_quote_json_is_rejected_not_crashed`,
   `test_c1r1_evidence_as_object_fails_schema_not_silently_coerced`,
   `test_c1r1_wrong_shape_verdict_tie_fails_schema`), all three correctly
   rejected by the existing fail-closed parsing/validation.
5. **Retry-exhaustion degrades gracefully today, but only through one
   specific code path.** `lj.run_blind_ab`'s bounded retry, when it
   ultimately fails, returns `contributes: "inconclusive"` — never a crash,
   never a fabricated pass (`test_retry_exhaustion_degrades_to_inconclusive_never_pass`).
   However, this graceful behavior depends on the `JudgeModel.evaluate()`
   implementation **never raising** — the real `BrowserJudgeModel.evaluate()`
   is safe because it routes through `lba.invoke()`, which internally
   catches `LiveTransportError`; a `JudgeModel` that raises directly (as an
   incorrect implementation might) will crash `run_blind_ab` instead of
   degrading. This is an implicit, undocumented part of the `JudgeModel`
   protocol contract, found while writing the regression test above — worth
   `[LLM]`/`[AI OS]` making explicit in the contract doc, independent of the
   MD-2 decision.
6. **`run_blind_ab` returns on the first order's failure without ever
   evaluating the second order.** Confirmed both in the C1-R1 live run's
   own `judge_invocation_ids` (2 of 3 reruns show two attempts of the SAME
   order, never reaching `:rev`) and in
   `test_first_order_failure_short_circuits_second_order`. Relevant for
   anyone reasoning about "how many Judge calls were actually consumed" in
   any future batch preview math.
7. **The evaluator contract's own governance status is `candidate`, not
   `active`** (`ChatGPT/[LLM]/Knowledge/AUTORESEARCH_SEMANTIC_EVALUATOR_CONTRACT.md`,
   header). No batch may use it until an owner accepts a specific frozen
   version/hash under `PROMPT_LIFECYCLE_STANDARD.md`'s promotion gate — a
   standing fact independent of MD-2, worth `[AI OS]`/`[LLM]` confirming is
   still intentionally the case given live batches have already run against
   it under separate per-instance authorizations.
8. **Fresh, full verification on this exact revision** (not reused from
   any prior session): `pytest tests/ -q` → 613 passed pre-handoff, 620
   passed with the 7 new regression tests added; `check_manifest_paths`
   189/189; `check_repo_public_safety` PASS; `check_index_coverage` 9/9;
   `check_knowledge_bundles` 0 failed. See
   `AUTORESEARCH_PREFLIGHT_2026-09-05.md` for exact commands/output.
9. **The C1-R1 freeze package and its evidence were, until this handoff,
   sitting on a branch (`codex/chatgpt-project-live-optimization-source`)
   that does not descend from the merged AutoResearch runtime at all.**
   Copied here, onto `codex/autoresearch-md2-handoff` (cut from
   `origin/main`@`3b81126`), with byte-hashes re-verified after the copy.
   The original location has not been deleted pending your review of this
   copy.

## 2. Exact source refs

- `scripts/autoresearch_cli.py` — `_contributes_to_pair`, `_case_payload`,
  `ManualCandidateSpec`, `Controller.run_experiment`.
- `scripts/autoresearch_decision_comparator.py` — `evaluate_case_material_improvement`,
  `evaluate_case_non_inferiority`, `aggregate_decision`, `MIN_MATCHED_RERUNS`/`MAX_MATCHED_RERUNS`.
- `scripts/autoresearch_live_judge.py` — `run_blind_ab`, `build_judge_prompt`,
  `primary_assignment`/`reversed_assignment`, `parse_judge_findings`,
  `validate_live_finding`, `BrowserJudgeModel`.
- `scripts/autoresearch_context_pack_compiler.py` — `render_summary`,
  `compile_subject_baseline`/`compile_subject_candidate`, `equivalence_report`.
- `scripts/autoresearch_shadow_runner.py` — `mutable_surface_line_ranges`
  (the existing anchor-excerpting mechanism the subject-content memo's
  recommended option would reuse).
- `schemas/autoresearch_live_semantic_finding.schema.json` — the frozen
  finding shape any Option A schema change would extend.
- `ChatGPT/[LLM]/Knowledge/AUTORESEARCH_SEMANTIC_EVALUATOR_CONTRACT.md` §§2,
  6, 9, 10, 11 — prompt family, finding schema, disagreement handling,
  versioning/content-hash contract, anti-leakage rules.
- `ChatGPT/[Analytics]/Knowledge/AUTORESEARCH_STOCHASTICITY_NONINFERIORITY_METHOD.md`
  §§7, 8 — material-improvement logic, 3→5 escalation (not implemented in
  the current minimal-for-C1 scope; separately deferred, not part of this
  handoff).
- `docs/evidence/AUTORESEARCH_V02_LIVE_LOOP_WIRING_2026-09-04.md` — the
  pre-merge method review that first scored MD-2 `blocked` and listed the
  four resolution options this handoff's Option A/B/C map onto.
- `docs/standards/autoresearch_v01_manifest.json` — the four declared
  mutable surfaces (`MUT-ROUTING-TIEBREAK`, `MUT-AIOS-CONTEXT-PRIORITY`,
  `MUT-AIOS-HANDOFF-WORDING`, `MUT-HANDOFF-PROJECT-ADDITIONS`), unchanged,
  not a candidate surface for this decision.
- `docs/evidence/autoresearch_c1r1_freeze/AUTORESEARCH_C1R1_LIVE_RUN_2026-09-04.md` —
  the source of the 5/6 malformed-Judge-output and manifest-only-context
  facts above.

## 3. Competing options

Full detail, tradeoffs, and required-change tables in the two companion
documents. Summary:

**MD-2 (Judge→observation→comparator gap)** —
`AUTORESEARCH_MD2_DECISION_PACKAGE_2026-09-05.md`:
- **A** — directional Judge extension, blind A/B preserved (schema-additive; `[LLM]`-owned; comparator untouched).
- **B** — per-side absolute scoring (new `[LLM]`-owned prompt mode; comparator untouched; call-budget impact needs explicit owner sign-off).
- **C** — comparator-side redefinition of "improvement" (`[Analytics]`-owned; touches the frozen §7 method itself; highest risk).
- **D** — rescope to regression/no-op detection only; no code change; conflicts with the stated program objective unless that objective is explicitly narrowed.

**Subject-content propagation** —
`AUTORESEARCH_SUBJECT_CONTENT_PROPAGATION_MEMO_2026-09-05.md`:
- **1** — full file content inline (contradicts issue #412's anti-dump rule as currently worded; largest prompt-size/cost impact).
- **2** — bounded excerpt of just the declared mutable surface, reusing `mutable_surface_line_ranges` (smallest change; produces a mechanically checkable equivalence proof).
- **3** — structured mutated-surface diff (risks smuggling hypothesis-shaped framing into the subject prompt; not recommended as a first choice).

## 4. Recommendation

- MD-2: **Option A**, conditional on `[LLM]` budgeting a Judge-output
  reliability pass first, given the 5/6 malformed-output rate observed
  live under the *current*, simpler schema. **Option B** as the fallback if
  `[LLM]` judges that reliability risk as dominant over the blind-A/B
  anti-bias property Option A preserves. **Option C** only if `[Analytics]`
  independently finds the frozen §7 predicate wrong on its own terms.
  **Option D** named explicitly as the "stop here" baseline, since it is in
  fact the value already demonstrated live (Phase 0's correctly-caught
  harmful mutation).
- Subject content: **Option 2**, for the reasons in the memo (smallest
  change, reuses audited code, produces the exact equivalence proof the
  program objective already asks for).

Neither recommendation is implemented. Both are `[Codex]`'s best-effort
read of the tradeoffs for the actual decision-makers, not a default to fall
back on absent a response.

## 5. Risks

- Picking MD-2 Option A or B without a prior reliability calibration risks
  repeating C1-R1's outcome for a different reason (Judge format failure
  rather than symmetric-mapping blindness) — indistinguishable from
  "inconclusive because no signal exists" without deliberately designed
  calibration fixtures (per the original ТЗ's own §4 calibration
  requirements, out of scope for this handoff).
- Picking Option C without full `[Analytics]` re-derivation risks silently
  weakening the one already-validated conservative property (`AUTORESEARCH_STOCHASTICITY_NONINFERIORITY_METHOD.md`
  §7's "one successful run is never evidence of improvement") that the
  whole method was built to guarantee.
- Picking subject-content Option 1 without revisiting issue #412's anti-dump
  rule risks a governance inconsistency (a rule cited by the same module
  that would now violate it) more than a technical risk.
- Not deciding at all indefinitely defers the stated program objective
  while consuming no further owner time — a legitimate but silent form of
  Option D that should be a conscious choice, not a default by inaction.

## 6. Acceptance criteria (for whichever option(s) are chosen)

- The chosen MD-2 option's evaluator-contract change (if any) is frozen
  under `PROMPT_LIFECYCLE_STANDARD.md`'s existing promotion gate with a new
  `evaluator_contract_version` and recomputed content hash — no second
  hashing mechanism.
- The chosen subject-content option's equivalence proof is mechanically
  checkable (e.g., excerpt diff == declared patch hunks), not just
  eyeballed.
- `evaluate_case_non_inferiority`'s existing regression-catching behavior
  (already proven live in Phase 0) is unchanged by any MD-2 option unless
  Option C's re-derivation explicitly revisits it too.
- `pytest tests/ -q` plus the applicable manifest/safety/index/bundle
  checks pass fresh on the implementation revision before any live use is
  considered.
- A new calibration batch (per the original ТЗ's controlled-defect/
  controlled-degradation/null-control/mixed-control cases) is run and
  accepted *before* any real-candidate pilot, with its own separate,
  numbered-in-advance batch envelope.

## 7. Forbidden actions (unchanged from every gate this whole program has held to)

- No live call of any kind on the basis of this handoff alone.
- No change to `evaluate_case_non_inferiority`, `aggregate_decision`'s
  hard-veto ordering, or any frozen schema without the specific owner
  acceptance this handoff is requesting.
- No merge, promotion, or `keep_candidate`-shaped outcome from anything in
  this handoff.
- No claim that AutoResearch v0.2's semantic-optimization objective is
  complete, satisfied, or "ready" — this handoff exists precisely because
  it is not yet, and closes no acceptance question by itself.
- No expansion of the four declared mutable surfaces, no access to the
  sealed holdout, no touching `benchmarks/*/freeze_manifest.json` or ledger
  history.

## 8. First safe implementation step after a decision

Once `[LLM]`/`[Analytics]`/`[AI OS]` accept an MD-2 option and a
subject-content option (independently — they don't have to land together):
`[Codex]` implements exactly the accepted option(s), re-derives the
evaluator content hash if the contract changed, updates or removes the
regression tests in `tests/test_autoresearch_c1r1_regression.py` that the
new behavior intentionally supersedes (`test_md2_mapping_can_never_yield_material_improvement`
and/or `test_case_payload_does_not_currently_include_mutated_row_text`),
adds new tests proving the accepted option actually closes the gap it was
chosen to close, and returns to a preflight-and-plan posture (not
execution) for the calibration-batch stage — per the original ТЗ's own §4,
still gated on its own separate authorization.
