# AIOS AutoResearch v0.2 — Live Blind A/B Judge & De-blinding Boundary — 2026-09-04

Parent: [#409](https://github.com/sergstack/AI-OS/issues/409).
Child: [#414](https://github.com/sergstack/AI-OS/issues/414) (Implement live blind A/B Judge and
de-blinding boundary).

Status: **implementation + automated checks complete; the live calibration proof is `blocked`**
pending the coordinated live session (owner sign-in to the dedicated Playwright profile) that
also covers the #413 smoke and #417 Phase 0. Per #414's Stop/blocker rule, hand-authored Judge
findings cannot satisfy the calibration proof and the child is not accepted as complete until
actual Judge calls have run.

No live model/provider/Judge call was made in producing this document.

---

## Owner authorization envelope

Same envelope as `AUTORESEARCH_V02_LIVE_BROWSER_SMOKE_2026-09-04.md` (owner instruction
2026-09-04, Option 1): dedicated persistent Playwright profile; **~40** Phase-0 live calls total
(subject **and Judge** calls share this ceiling — live-contract §6); **$0 / plan-included**.
This authorizes Phase 0 scope only; not candidate acceptance, active-config, merge, or
production.

---

## Final response format (per #414)

```text
Parent:                     #409. Child #414.
Dependencies:               #411 controlling; #412 Judge-role context boundary available; #413 transport in review (PR #423); #394 contract + finding schema reused unchanged.
Judge transport/model:      #413 PlaywrightMcpBrowserTransport via lba.invoke(); model class pinned "judge"; model identity not_observable in a browser UI; independence recorded per run (independent_model | limited_same_model_class | unknown).
Evaluator version/hash:     docs/standards/autoresearch_v02_evaluator_config.json — evaluator_version_hash 8d62446047a808c2d4392e39ad5b71861b96d0e9af315d937e742331fde8ae0d (sha256 over {prompt_family_text, rubric_blocks_by_case_family, model_class_pin, finding_schema_version}, #394 §10). Drift is rejected by EvaluatorConfig.load().
Blinding/order protocol:    A/B via autoresearch_shadow_runner.alternation_order(experiment_id, seed) (reused unchanged); mandatory reversed second pass; presentation_order_hash per pass; de-blinding only after BOTH orders produce schema-valid findings, and only in the evidence layer (never in prompt or finding).
Live Judge calls:           0 so far — BLOCKED. Predeclared calibration = 4 pairs x 2 orders + <= 1 bounded retry per order (<= ~10 Judge calls), all inside the shared 40-call Phase-0 ceiling; exact count re-frozen at session start.
Calibration results:        pending — see "Predeclared live calibration" below.
Disagreements/order effects: mechanism implemented + tested (order_consistent | judge_disagreement); material disagreement contributes `inconclusive`, never averaged.
Deterministic override proof: implemented + tested — a `discard`-consequence precheck returns consistency `deterministic_bypass`, contributes `blocked`, Judge call count 0.
Budget/usage:               each Judge call routes through lba.invoke and consumes the shared BudgetState (test-proven); usage/cost = not_observable / $0 for a browser session.
Checks run:                 19 focused #414 tests; full suite 550 passed (531 + 19); check_manifest_paths 189/189; check_repo_public_safety PASS; check_index_coverage 9/9; new finding schema valid draft-07. No live network call in any test.
Acceptance status:          BLOCKED. Artifact/code acceptance met; business acceptance (actual blinded live findings, incl. one obvious and one ambiguous pair) not met until the live calibration runs.
Residual bias/limitations: browser-UI Judge cannot expose model identity -> independence likely `limited_same_model_class` unless a distinct authorized Judge model is available in budget; treat Judge agreement as NOT independent corroboration in that case and require an independent adversarial/human gate before any promotion (#414 "Model independence").
Rollback:                   remove scripts/autoresearch_live_judge.py, schemas/autoresearch_live_semantic_finding.schema.json, docs/standards/autoresearch_v02_evaluator_config.json, tests/test_autoresearch_live_judge.py, this doc, and the README line. No v0.1 file, #394 schema, Project config, or active behaviour touched.
```

---

## What was built

- **`scripts/autoresearch_live_judge.py`**
  - `EvaluatorConfig` — frozen evaluator identity; `frozen_hash()` is #394 §10's content hash,
    not a second mechanism; `load()` rejects declared-vs-computed drift.
  - `primary_assignment` / `reversed_assignment` — reuse
    `autoresearch_shadow_runner.alternation_order` unchanged; `presentation_order_hash` per pass.
  - `build_judge_prompt` — fills the #394 §2 prompt family; **fail-closed leakage guard** over
    the case/pipeline-injected text (`frozen_input`, deterministic findings) for
    baseline/candidate identity, hypothesis, expected winner, prior decision, owner preference,
    authority/merge/production tokens. The frozen boilerplate and rubric — which legitimately
    *name* those concepts to tell the Judge to ignore them — are exempt; the two subject outputs
    are anonymised positionally.
  - `FakeJudgeModel` (deterministic, no I/O) and `BrowserJudgeModel` (routes each call through
    `lba.invoke` on the #413 transport, sharing the batch `BudgetState`).
  - `parse_judge_findings` — extracts the JSON array; `None` on empty/unparseable → bounded
    retry, never a PASS.
  - `validate_live_finding` — schema-validates each finding and rejects any forbidden
    authority/identity/score field.
  - `run_blind_ab` — the #414 required sequence: deterministic precheck → primary order → live
    call #1 → validate → reversed order → live call #2 → validate → consistency compare →
    privileged de-blinding *after* both validate → `CaseSemanticEvidence`
    (`order_consistent | judge_disagreement | deterministic_bypass`; `contributes`
    `pass|revise|blocked|inconclusive`).
- **`schemas/autoresearch_live_semantic_finding.schema.json`** — additive; the frozen #394
  schema is not modified. Reuses its verdict/severity/confidence vocabularies; adds only live
  provenance fields; `additionalProperties:false` plus an explicit `not/anyOf` block keep
  authority/identity/score fields structurally impossible.
- **`docs/standards/autoresearch_v02_evaluator_config.json`** — the frozen evaluator config with
  its self-consistent `evaluator_version_hash`.
- **`tests/test_autoresearch_live_judge.py`** — 19 tests.

---

## Predeclared live calibration (to run in the coordinated session)

Per #414 "Live calibration proof", exactly these, with the count re-frozen at session start:

1. **one obvious good/bad behavioral pair** (a clearly rule-following output vs a clearly
   rule-violating one) — expect a material `revise`/`blocked` verdict favouring the compliant
   side, stable across both orders → `order_consistent`.
2. **the same pair, A/B reversed** — expect the same substantive verdict; a reversal without a
   rubric-grounded reason is itself a `judge_disagreement` event.
3. **one ambiguous pair** expected to preserve uncertainty → `revise`/`blocked` with explicit
   `limitations`, or a `judge_disagreement` mapping to `inconclusive`.
4. **one deterministic-hard-fail case** — proves the Judge is not invoked and cannot override it
   (`deterministic_bypass`, 0 Judge calls).

Hand-authored Judge findings are explicitly **not** acceptable for this proof.

---

## Blockers

1. Owner sign-in to the dedicated Playwright MCP profile (shared with #413 / #417).
2. A live `mcp_call` binding for `PlaywrightMcpBrowserTransport`.
3. A frozen Judge-role context pack from `scripts/autoresearch_context_pack_compiler.py`
   (`role: semantic_judge`) for each calibration case.
4. An owner decision on whether a Judge model distinct from the subject model is available
   within the $0 / plan-included envelope; if not, `evaluator_independence:
   limited_same_model_class` is recorded and self-preference risk disclosed.

Until items 1–4 are done and real Judge invocation IDs + response hashes exist, #414 stays
`blocked`.

---

## Rollback

Remove the five child-owned files listed above plus the one `docs/evidence/README.md` index
line. No v0.1 artifact, the frozen #394 schema, Project configuration, or active AI-OS behaviour
is touched.

---

## Checks run

```bash
python3 -m pytest tests/test_autoresearch_live_judge.py -q                    # 19 passed
python3 -m pytest tests/ -q                                                   # 550 passed
python3 -m json.tool schemas/autoresearch_live_semantic_finding.schema.json   # parses
python3 scripts/check_manifest_paths.py                                       # 189/189
python3 scripts/check_repo_public_safety.py                                   # PASS
python3 scripts/check_index_coverage.py                                       # 9/9
```

This document was scanned for secrets, raw credentials, personal data, hidden reasoning, and
unsupported live-run claims before commit: none found. No live Judge call has occurred.
