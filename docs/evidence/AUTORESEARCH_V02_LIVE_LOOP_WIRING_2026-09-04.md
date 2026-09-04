# AIOS AutoResearch v0.2 — Live Loop Transport-Binding Wiring — 2026-09-04

Issue: [#433](https://github.com/sergstack/AI-OS/issues/433) (follow-up to
[#416](https://github.com/sergstack/AI-OS/issues/416); parent
[#409](https://github.com/sergstack/AI-OS/issues/409), closed).

Status: **implementation only.** No live model / provider / Judge call was
made in producing this change. Automated tests use `FakeBrowserTransport` /
`FakeJudgeModel` and injected `mcp_call` stubs that raise if invoked.

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

## Rollback

Revert `scripts/autoresearch_cli.py`; delete
`scripts/autoresearch_coordinated_session.py`,
`tests/test_autoresearch_coordinated_session.py`, this doc, its
`docs/evidence/README.md` line, and the `AUTORESEARCH_CLI.md` section. The
harness returns to its current fail-closed `EXIT_BLOCKED` state. No baseline,
active config, `main`, `ledger`, or prior evidence is touched at any point.
