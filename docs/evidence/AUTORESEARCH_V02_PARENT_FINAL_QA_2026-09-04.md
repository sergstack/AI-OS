# AIOS AutoResearch v0.2 — Parent Final QA (re-run after live session) — 2026-09-04

Parent: [#409](https://github.com/sergstack/AI-OS/issues/409) ([Goal] AIOS AutoResearch v0.2 —
live behavioral autotuning loop).
Child: [#419](https://github.com/sergstack/AI-OS/issues/419) ([Thinking/AI OS][AutoResearch v0.2
10/10] Live holdout, adversarial review, and parent final QA).

This is the **final parent acceptance gate** for AutoResearch v0.2, re-run after the coordinated
live session of 2026-09-04. It **does not promote or apply any candidate**; there is none.

No holdout content was accessed. No credential value was read, printed, or transmitted.

---

## 0. What changed since the point-in-time draft

An earlier revision of this document (same date) recorded parent gate **`blocked`** because the
live-execution children were unbuilt. They have since been implemented and the live session was
run. This revision supersedes that draft on the same branch; the git history preserves it.

---

## 1. Dependency / evidence completeness

| Child | Title | Delivery | Evidence |
|---|---|---|---|
| #410 | Audit v0.1 reuse & live-transport feasibility | merged (PR #420) | `AUTORESEARCH_V02_BASELINE_TRANSPORT_AUDIT_2026-09-03.md` |
| #411 | Freeze live-execution/privacy/budget/authority/evidence contract | merged (PR #421) | `AUTORESEARCH_V02_LIVE_CONTRACT.md`, authority matrix, batch-config schema |
| #412 | Deterministic AI-OS context-pack compiler | merged (PR #422) | `autoresearch_context_pack_compiler.py`, `autoresearch_context_manifest.schema.json` |
| #413 | Playwright MCP browser-session live transport + smoke | merged (PR #423); **smoke executed** | `AUTORESEARCH_V02_LIVE_BROWSER_SMOKE_2026-09-04.md` (§ "Update — 2026-09-04") — 1 real `gpt-5-6-thinking` call, `response_hash b2539ec2…`, model `ui_observed`; smoke facts recorded inline, no standalone JSON record committed |
| #414 | Live blind A/B semantic Judge + de-blinding | PR #425 (review) | `AUTORESEARCH_V02_LIVE_JUDGE_CALIBRATION_2026-09-04.md`; live blind Judge exercised in #417 |
| #415 | Real failure intake, attribution, bounded Researcher proposal | PR #426 (review) | `AUTORESEARCH_V02_RESEARCHER_SMOKE_2026-09-04.md`; no failure candidate arose to route through it |
| #416 | Matched live runs, hard gates, ledger, stable CLI | PR #427 (review) | `AUTORESEARCH_V02_CLI_CONTROLLER_2026-09-04.md`; 9-verb CLI, dry-run, resume, cleanup |
| #417 | Phase 0 live calibration & discovery gate | PR #428 (review); **executed live** | `AUTORESEARCH_V02_PHASE0_LIVE_2026-09-04.md` + `autoresearch_v02_phase0_records_2026-09-04.json` |
| #418 | Phase 1 bounded live autotuning pilot | **blocked** — see §3 | — |

**Result:** every implementation/calibration child #410–#417 is delivered (#410–#412 merged,
#413–#417 implemented, tested, and in owner review as PRs #425–#428; #413 already merged as
PR #423). #418 is legitimately `blocked` on #417's output, not skipped. Dependency verdict:
**satisfied** for a parent-gate decision.

---

## 2. Live architecture actually exercised

Real, not synthetic. All calls were `gpt-5-6-thinking` in the owner's ChatGPT Pro account
through the #413 `playwright_mcp` transport (dedicated persistent Playwright profile, owner
signed in interactively).

- **#413 transport smoke** — 1 subject call; repo-derived AI-OS context (`context_hash
  c5a1c5b0…` over `ROUTING_RULES.md` + `HANDOFF_STYLE_STANDARD.md` at `662686e…`); a real
  607-char answer with `response_hash b2539ec2…`; model identity `ui_observed`
  (`data-message-model-slug`).
- **#417 Phase 0** — 12 calls (10 subject, 2 blind A/B Judge, 0 Researcher), $0 /
  plan-included, 0 retries / timeouts / invalid outputs.

`repo_replay` via a fresh non-Project chat is a **lower-fidelity** approximation of the real
configured AI-OS Project runtime — no UI-equivalence claim is made anywhere.

---

## 3. Final response format (per #419)

```text
Parent:                         #409. Re-run after the 2026-09-04 live session.
Dependencies/evidence completeness: SATISFIED for a parent-gate decision. #410–#417 delivered (PRs #420–#428); #413 merged + smoke executed; #418 blocked on #417's output (not skipped).
Live architecture actually exercised: #413 transport smoke (1 subject call) + #417 Phase 0 (12 calls) — real gpt-5-6-thinking, $0, model ui_observed on every call.
CLI/operator result:            #416 delivers one documented 9-verb CLI (doctor/context/baseline/reproduce/propose/experiment/batch/report/cleanup) with a no-network --dry-run, bounded resume, and scoped cleanup. Assessed by test + dry-run, not just code existence; a real batch stays blocked (exit 4) without a wired live transport, by design.
Calls/budget reconciliation:    13 live calls total across #413 + #417 (11 subject, 2 Judge, 0 Researcher). $0 (Pro plan quota). token/cost usage not_observable (never estimated). 0 retries, 0 timeouts, 0 invalid outputs, 0 missing observations.
Failures and attribution:       0 baseline failures found in Phase 0. 0 field observations ingested. Nothing routed through #415. Attribution: n/a.
Experiments/decisions:          0 autotuning experiments (Phase 1 not run). Phase 0 control calibration: CAL-1 pass, CAL-2 masked (control-design lesson), CAL-4b pass, CAL-2b regressed-as-designed.
Finalists:                      0. Nothing frozen. finalist/holdout evaluation not_applicable (Branch B — Phase 0 executed and produced no finalist to test).
Holdout isolation/results:      NOT ACCESSED (correct). not_applicable — no finalist set, and #418 did not run. Integrity contract not violated.
Hard-gate result:               deterministic dominance proven in code (deterministic_bypass → 0 Judge calls; preflight rejects protected/multi-file/out-of-anchor before any call). Live semantic results cannot override a deterministic discard.
Behavioral/efficiency/uncertainty result: live blind A/B Judge on CAL-4b vs CAL-2b, both orders → order_consistent on verdict (harmful=revise, baseline=pass, regardless of A/B position); minor within-rubric severity wobble (critical↔high), not a reversal. Analytics comparator not invoked (no candidate).
Adversarial findings:           (1) live Judge reliably distinguished an obvious harmful routing violation from a correct one — the "Judge cannot distinguish / is order-biased" falsification criterion did NOT fire; (2) the mutable surface is demonstrably load-bearing (CAL-2b vs CAL-4b); (3) control-design pitfall (CAL-2): a deep-rule mutation can be masked by a higher-priority rule — a calibration lesson for any future Phase 1, not a harness defect; (4) subject and Judge share a model class (limited_same_model_class) → Judge agreement is not independent corroboration.
Privacy/leakage review:         clean. No credential read/typed/exported; no cookie/storage/profile export; no other-tab inspection; captured answers scanned for secret-shaped content (none); no raw_restricted trace. 13 transient chat URLs recorded for audit only.
Falsification assessment:       no whole-program falsification criterion fired. One v0.1 condition — "no genuine field-observed failure exists yet" — still holds. The v0.1 "no working live Judge" condition is now DISCHARGED: a live blind Judge demonstrably works and is order-consistent on an obvious case.
Manual alternative comparison:  manual bounded regression review still delivers the realized decision value: Phase 0 produced 0 promotable findings. The live loop's incremental value remains prospective — it becomes decision-relevant only once a real field failure exists to autotune against.
Options considered:             (1) parent pass + keep the harness available, defer Phase 1 [SELECTED by owner 2026-09-04]; (2) parent pass + formally retire the live-autotuning ambition; (3) hold at revise for a fuller repeated-run Phase 0.
Recommendation:                 KEEP THE HARNESS AVAILABLE, DEFER PHASE 1. The v0.2 live loop is built and calibrated against real model output; it correctly found no baseline failure and correctly declined to promote anything. Re-engage only when a genuine field-observed failure appears. Manual bounded regression review remains sufficient until then. This mirrors v0.1's #398 outcome.
Parent gate:                    pass
Authority/merge/production status: candidate_acceptance = owner_only / nothing to accept. merge_authority = not_granted (the #414–#417 PRs are in normal owner review). production_authority = not_granted. No candidate exists; no active Project configuration, routing, or main was changed by any live run.
Residual risks:                 §5.
Rollback:                       §6.
Owner decision required:        YES (light) — accept this parent gate `pass` and decide whether to close #409 now (harness available, Phase 1 deferred) or leave #409 open pending a field failure. Also: normal owner review + merge of PRs #425–#428.
```

---

## 4. Whole-program falsification assessment

| Criterion | Status on v0.2 |
|---|---|
| No authorized/reproducible live transport can be sustained | **Cleared** — 13 real calls, 0 failures, $0, model identity observable every time |
| Repo replay lacks useful fidelity for the relevant behaviour | Not fired — Phase 0 controls behaved coherently under repo_replay; fidelity limitation is disclosed, not disqualifying |
| Live Judge cannot distinguish obvious cases / is materially order-biased | **Did not fire** — order-consistent verdicts on an obvious harmful-vs-correct pair |
| Candidate rankings unstable across matched reruns | n/a — no candidates |
| No real/reproducible failure can be found or attributed | **Still holds** — Phase 0 found no baseline failure; carried over from v0.1 |
| Researcher proposals repeatedly fail one-mechanism/protected-scope gates | n/a — no Researcher runs |
| Validation improvements do not transfer to holdout | n/a — no holdout run |
| Automation repeatedly produces hard governance regressions | Not observed — no active state changed |
| Live evidence/usage/cost cannot be audited | Not fired — per-call conversation URLs + hashes recorded; cost $0/plan-included; token usage honestly `not_observable` |

**Net:** v0.2 was **executed responsibly**. The live idea is technically real (transport + Judge
work), and it correctly produced **no promotable result** because no genuine failure exists to
autotune against — exactly the honest outcome v0.1's #398 anticipated.

---

## 5. Residual risks

- **Fidelity**: `repo_replay` via a fresh chat ≠ the real configured Project runtime; every
  downstream evidence doc carries this.
- **Judge independence**: subject and Judge are the same model class; Judge agreement is not
  independent corroboration — an independent adversarial/human gate is required before any
  future promotion.
- **Phase 0 depth**: Part B used a single run per family; repeated-run discrimination (per #395)
  was demonstrated only on the CAL-4b/CAL-2b pair. A fuller Phase 0 would be needed before any
  Phase 1.
- **Re-freeze on review changes**: Phase 0 ran on the #413–#416 branch code while those PRs are
  in review. A material change in review requires a re-frozen Phase 0 re-run (the batch is
  append-only, never overwritten).
- **Momentum**: "keep the harness available" must not drift into running Phase 1 without a real
  failure and a fresh owner budget grant.

---

## 6. Rollback

No active AI-OS behaviour, Project configuration, routing, `main`, or v0.1/prior-v0.2 record was
changed by any live run. No candidate exists. Rollback of this gate is: restore only this
evidence document and its one `docs/evidence/README.md` index line. The #414–#417 PRs roll back
by normal PR closure. The owner may delete the 13 transient chat conversations at will; their
URLs are retained purely for audit. A compromised or superseded Phase 0 batch is versioned, not
overwritten.

---

## 7. Checks run

```bash
python3 -m pytest tests/ -q                     # 592 passed (on the #416 branch base this stack rebases onto)
python3 scripts/check_manifest_paths.py         # 189/189
python3 scripts/check_repo_public_safety.py     # PASS
python3 scripts/check_index_coverage.py         # 9/9
gh pr view 420..428 / gh issue view 409..419    # state reconciliation, no model call
```

No live model/provider/Judge call was made in producing this document. It was scanned for
secrets, raw restricted traces, personal data, and unsupported robustness/causal claims before
commit: none found.
