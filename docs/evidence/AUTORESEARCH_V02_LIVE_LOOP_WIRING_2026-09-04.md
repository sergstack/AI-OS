# AIOS AutoResearch v0.2 — Live Loop Transport-Binding Wiring — 2026-09-04

Issue: [#433](https://github.com/sergstack/AI-OS/issues/433) (follow-up to
[#416](https://github.com/sergstack/AI-OS/issues/416); parent
[#409](https://github.com/sergstack/AI-OS/issues/409), closed).

Status: **implementation done; formal method review returned MD-2 `blocked`,
MD-3 `blocked`, MD-1 `revise`, MD-4 `pass` — #434 must NOT merge** until the
accompanying owner / `[Analytics]` / `[LLM]` / `[AI OS]` decisions are made
(see "Formal method review" below). No live model / provider / Judge call was
made. Automated tests use `FakeBrowserTransport` / `FakeJudgeModel` and
injected `mcp_call` stubs that raise if invoked.

This does **not** change #417→#418 admission semantics, the #395 comparator
method, the #394 evaluator contract, any schema's semantics, or the closed
#409 governance decision. It restores runnable plumbing #416's title claims.

---

## What was missing (verified read-only against `main` @ `0b1ce29`)

`autoresearch_cli.py` could not run a live experiment: `Controller` had no
`run_experiment`; the `experiment` verb ran `doctor` + preview and then
unconditionally `return EXIT_BLOCKED`; nothing sequenced
`asr.run_shadow_experiment` + `lj.run_blind_ab` + `adc.aggregate_decision`;
there was no `mcp_call` injection seam. The 2026-09-04 Phase 0 coordinated
driver was never committed (only its output records).

## What changed

| File | Change |
|---|---|
| `scripts/autoresearch_cli.py` | `+ Controller.run_experiment(...)` — a **sequencer** over the frozen components, no new decision logic. `+ ManualCandidateSpec`. `+ _transport_policy / _build_requests / _case_payload / _semantic_to_case_observation (MD-2) / _finalize_pilot (MD-4) / _spec_from_args`. `+ _CONTROLLER_FACTORY` indirection. `main()` uses the factory; the `experiment` branch now: `transport is None` → **unchanged** `EXIT_BLOCKED` (reason points to the coordinated session); transport bound → `run_experiment`. |
| `scripts/autoresearch_coordinated_session.py` | **new**, thin. The one place a real `mcp_call` enters. Builds the existing `PlaywrightMcpBrowserTransport` + `BrowserJudgeModel` + `Controller`, calls `run_experiment`. Performs no I/O; imports no MCP tool. |
| `tests/test_autoresearch_coordinated_session.py` | **new**, 14 tests, fakes only, no network. |
| `docs/guides/AUTORESEARCH_CLI.md` | `+ "Coordinated-session seam"` section. |

Full suite: `pytest tests/ -q` → **606 passed** (592 baseline + 14 new).
`check_manifest_paths` 189/189 · `check_repo_public_safety` PASS ·
`check_index_coverage` 9/9.

## Components reused unchanged

`lba.invoke`, `lba.PlaywrightMcpBrowserTransport`,
`lba.live_browser_adapter_callable`, `lba.to_live_invocation_record`;
`asr.run_shadow_experiment` (isolated worktree, real scope gate,
parent-tree-fingerprint safety); `lj.run_blind_ab`, `lj.BrowserJudgeModel`,
`lj.EvaluatorConfig`; `adc.evaluate_case`, `adc.aggregate_decision`;
`av.load_manifest`, `av.sha256_hex`; `cpc.compile_subject_baseline`,
`cpc.compile_subject_candidate`, `cpc.equivalence_report`,
`cpc.render_summary`. No edits to any of them.

## Fail-closed behaviour (regression-tested both directions)

- bare shell `experiment` (no transport) → `EXIT_BLOCKED`, reason names the
  coordinated session;
- transport bound but `budget.authorized()` false → `blocked`;
- `batch_config.authority_status != "authorized"` → `blocked`;
- missing `authority_evidence_ref` → `blocked`;
- patch outside the declared mutable surface / touching a protected surface →
  deterministic hard gate → `pilot_decision: reject`;
- context drift outside the one declared mutation → `reject`;
- identical baseline/candidate outputs → `inconclusive` (never
  `candidate_for_owner_review`).

## Decision vocabulary

`run_experiment` for a `manual_candidate_evaluation` returns exactly one of
`reject | inconclusive | candidate_for_owner_review`. The raw
`adc.aggregate_decision` value is mapped: `keep_candidate →
candidate_for_owner_review` (**MD-4**), `discard → reject`, `inconclusive →
inconclusive`. `keep_candidate` is never emitted. `candidate_for_owner_review`
is research evidence only — not owner acceptance, merge, or promotion.

## Method decisions requiring [AI OS] / [Analytics] sign-off before any live run

These are glue between real live evidence and the **unchanged** #395
comparator input shape. They are isolated, conservative (bias toward
`inconclusive` / `reject`), and documented inline with `MD-` markers.

- **MD-1 — rerun orchestration.** `run_count` repeats of
  `asr.run_shadow_experiment` against the one immutable baseline revision +
  the one patch; each repeat = 1 baseline + 1 candidate live subject call per
  case. Escalation 3→5 (per #395 §8) is **not** implemented and is deferred to
  the review.
- **MD-2 — `CaseSemanticEvidence` → `CaseObservation`.** `run_blind_ab` yields
  one *relative* A/B verdict (`contributes`); `adc.CaseObservation` wants
  per-side *absolute* verdicts over ≥3 matched reruns. Mapping:
  `contributes == "pass"` → `(pass, pass)`; `contributes ∈ {revise, blocked}`
  → `(pass, <that>)` (material finding attributed to the candidate);
  `contributes == "inconclusive"` → `(None, None)`. The single Judge verdict
  is held constant only across reruns whose subject outputs were present and
  textually stable; a variant/missing rerun → null pair for that index. No
  semantic verdict is ever fabricated.
- **MD-3 — evidence artifact.** A manual pilot writes a sanitized
  evidence-package JSON, **not** a failure-shaped `experiment_record` /
  `av.ledger_append` (the experiment-record schema + `INV-06` are
  failure-driven; a non-failure manual candidate would be force-discarded).
  No schema change.
- **MD-4 — decision label** (above).

The review either ratifies these or replaces them; if a choice is not already
implied by `AUTORESEARCH_STOCHASTICITY_NONINFERIORITY_METHOD.md` /
`AUTORESEARCH_SEMANTIC_EVALUATOR_CONTRACT.md`, it needs an additive,
owner-reviewed amendment there first.

## Unresolved input — `call_timeout_seconds`

The frozen Phase 0 value is **not recoverable** from committed evidence. Per
the owner decision of 2026-09-04, a **new batch identity** fixes
`call_timeout_seconds = 180` for the new runtime revision. This does **not**
inherit or extend the 2026-09-04 Phase 0 live authorization.

## Fidelity limitation (carried on every downstream evidence doc)

Even a correct loop cannot be certified identical to the 2026-09-04 Phase 0
method, because that driver was never committed. `repo_replay` via a fresh
chat is a lower-fidelity approximation of the real configured Project runtime;
subject and Judge share a model class (`limited_same_model_class`).

## Not done here — requires fresh owner authorization

1. `[AI OS]` / `[Analytics]` review of MD-1/MD-2/MD-3, then merge of #433.
2. Fresh per-instance live authorization for the new runtime revision →
   **one bounded live binding smoke**.
3. Separately: fresh authorization → **re-run the already-frozen candidate
   C1** (`ROUTING_RULES.md` → `## Tie-break rules`, "Coding task preparation"
   row, `a prompt or workflow deliverable` → `a prompt/workflow deliverable`;
   patch sha256 `44505534bf2f910e70725a4244f98347324a7cb1d4af00d8120e501e643c3c87`;
   baseline `0b1ce29386342ef4e1884d8a58b574445572575e`). C1 is unchanged.

No Phase 1 (#418) launch. No holdout access. No active Project Instructions /
routing change. No auto PR / merge / deploy / promotion.

## Formal method review of MD-1…MD-4 (pre-merge, 2026-09-04)

Routing: MD-1/MD-2 → `[Analytics]` vs `AUTORESEARCH_STOCHASTICITY_NONINFERIORITY_METHOD.md` / #395;
MD-2 Judge semantics → `[LLM]` / #394; MD-3/MD-4/authority/lineage → `[AI OS]`.

```
MD-1: revise
Evidence:
  - #395 §15: >=3 matched reruns is the mandatory minimum before any
    non-inferiority / material-improvement determination; below it the case is
    inconclusive unconditionally. run_count default 3 satisfies this.
  - #395 §8: the 3->5 escalation is a CONDITIONAL step but, once its trigger
    holds ("at 3 matched reruns, a target-family case's material-improvement
    determination is inconclusive because of unresolved
    run_variance_or_disagreement"), it is mandatory ("escalate to up to 2
    additional reruns ... for that case only"), with a hard ceiling at 5.
  - Controller.run_experiment implements a fixed `for k in range(run_count)`
    loop and NO escalation. A case that would resolve to keep/discard at 5
    reruns instead terminates at inconclusive.
  - For candidate C1 specifically (near-cosmetic punctuation change) the
    trigger cannot fire (no variance-ambiguous target gain), but the harness
    is meant to be reusable and MD-1 would under-power any future
    variance-ambiguous edit. A method-incomplete loop must not merge on the
    accident that the first candidate does not exercise the gap.
Required change:
  Implement the #395 §8 per-case 3->5 escalation (bounded, per-case, hard
  ceiling 5, no further), OR add a tested hard guard that returns
  status="blocked" with an explicit "escalation unimplemented" reason
  whenever a target case hits the escalation trigger, so the harness never
  silently returns an under-powered determination. Preferred: implement the
  escalation (it is bounded and fully specified). Deferred here because the
  correct rerun shape depends on the MD-2 decision below.

MD-2: blocked
Evidence:
  - #394 / autoresearch_v02_evaluator_config.json produce a *comparative*
    blind A/B finding ("compare exactly two anonymized outputs A and B");
    lj.run_blind_ab returns one aggregate `contributes` value
    (pass|revise|blocked|inconclusive) over both orders, NOT a per-side
    absolute verdict, and does not attribute a material finding to
    baseline-vs-candidate.
  - #395 §1/§13 model each SIDE as its own observation row with its own
    absolute `normalized_behavior_result`; §1 explicitly defers "built from
    collected semantic findings" to "issue #392/#393 territory, not this
    issue" -- that bridge was never built.
  - No frozen contract specifies the relative->absolute conversion.
    `_semantic_to_case_observation` invents it: `contributes in
    {revise,blocked}` -> (baseline="pass", candidate=<that>). This assumes the
    material finding is ALWAYS against the candidate. An order-consistent
    `revise` could equally mean the BASELINE is the worse side (candidate is
    an improvement) or that both share the issue -- the mapping would then
    record a candidate regression that does not exist.
  - "Conservative enough" is not the bar: the mapping does not follow from
    the frozen method, so per the review instruction this is not `revise`.
Required change (owner / [LLM] / [Analytics] decision -- NOT chosen here):
  (a) keep only the unambiguous step -- order-consistent `pass` ->
      (pass,pass); every other `contributes` -> (None,None) [no fabricated
      direction; a Judge-found regression then maps to inconclusive, not
      reject]; OR
  (b) [LLM]/#394: add a directional-attribution field to the finding schema /
      evaluator contract so a finding names the worse side; OR
  (c) [LLM]/#414: run the Judge in a per-side absolute-scoring mode instead of
      (or alongside) blind A/B; OR
  (d) [Analytics]/#395: define canonically how a comparative finding maps to
      per-side `normalized_behavior_result`.

MD-3: blocked
Evidence:
  - `manual_candidate_evaluation` is a new experiment class introduced by the
    owner's task instructions; it appears in NO canonical doc
    (AGENTS.md, GOAL_MODE.md, AUTORESEARCH_V0*_CONTRACT.md, #418).
  - The hash-chained ledger (av.ledger_append) provides append-only,
    tamper-evident, duplicate-checked, correction-only traceability. The MD-3
    sanitized JSON package is immutable only by git/convention -- not
    hash-chained, not tamper-evident, not schema-validated on write.
  - It cannot be represented in the canonical `experiment_record` /
    `av.ledger_append` path without a change: the schema requires
    `observed_failure`, `attribution_evidence`, and an `attribution_status`
    in {supported,uncertain,rejected}; a manual pilot has no failure, and
    manifest INV-06 discards a keep_candidate-class record whose attribution
    is uncertain/ineligible and that is "not explicitly framed ... as a
    bounded discriminating experiment".
  - The justification currently lives only in code comments + this doc, not a
    governance rule -- exactly the gap the review flags.
Required change (owner / [AI OS] decision -- NOT chosen here):
  (a) add an additive governance rule (e.g. an AUTORESEARCH_V02_LIVE_CONTRACT
      section) defining `manual_candidate_evaluation` as a distinct
      non-ledgered evidence class, its required package fields, and its
      immutability basis; OR
  (b) also emit a hash-chained ledger entry using a representable `decision`
      (discard | inconclusive only; the candidate_for_owner_review label
      stays in the companion package), so the audit chain is preserved; OR
  (c) require every manual pilot to be reframed as a bounded discriminating
      experiment so the existing schema/ledger apply unchanged.

MD-4: pass
Evidence:
  - `_PILOT_DECISION` is a pure relabel: keep_candidate ->
    candidate_for_owner_review, discard -> reject, inconclusive ->
    inconclusive. The raw adc.aggregate_decision dict is preserved verbatim
    in evidence["comparator"], evidence["raw_decision"], and
    result["raw_decision"]; aggregate_decision runs unchanged.
  - candidate_for_owner_review carries <= the authority of keep_candidate:
    both are "pending owner review", neither grants acceptance / merge /
    active-config / production; the code emits an explicit authority_note to
    that effect and keep_candidate is never surfaced.
  - The pilot vocabulary (reject | inconclusive | candidate_for_owner_review)
    is owner-specified in the task instructions, not agent-invented.
Required change:
  None for MD-4 itself. Note: the reliability of the relabelled value still
  depends on MD-2 (comparator input) being sound -- tracked under MD-2.
```

### Review outcome

MD-2 and MD-3 are `blocked`; MD-1 is `revise` and is entangled with the MD-2
decision. Per the review instruction, no new semantics were chosen here and
**no further code change was made to #434**. An owner / `[Analytics]` /
`[LLM]` / `[AI OS]` decision request accompanies this review (PR #434 thread
and issue #433). #434 must not merge until MD-2 and MD-3 are resolved and
MD-1 is implemented or explicitly waived.

## Rollback

Revert `scripts/autoresearch_cli.py`; delete
`scripts/autoresearch_coordinated_session.py`,
`tests/test_autoresearch_coordinated_session.py`, this doc, its
`docs/evidence/README.md` line, and the `AUTORESEARCH_CLI.md` section. The
harness returns to its current fail-closed `EXIT_BLOCKED` state. No baseline,
active config, `main`, `ledger`, or prior evidence is touched at any point.
