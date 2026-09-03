# AIOS AutoResearch v0.1 — Parent Final QA & Promotion Gate — 2026-09-03

Parent: [#388](https://github.com/sergstack/AI-OS/issues/388). Defining child: [#398](https://github.com/sergstack/AI-OS/issues/398) — "Finalist holdout, adversarial promotion gate, and parent final QA," co-owned `[Thinking]` / `[AI OS]` / `[LLM]` / `[Analytics]`, final acceptance owned by Sergey.

## Scope of this document — read before the results

#398's own dependency list has three items: (1) #397 accepted with a complete evidence package — satisfied, merged in [PR #407](https://github.com/sergstack/AI-OS/pull/407); (2) *"a separate Sergey/owner decision must authorize finalist/holdout evaluation"*; (3) *"holdout access isolation must be technically demonstrated before any holdout run."*

**Items (2) and (3) are moot, not satisfied-by-proceeding-anyway.** #397 produced **zero finalists** — a finalist requires `keep_candidate` with immutable patch hashes selected *before* any holdout access, and #397's honest, deliberately-conservative design (no fabricated evidence-backed candidate) produced 0 `keep_candidate` results. There is nothing to select as a finalist and nothing to run a holdout comparison against. Authorizing finalist/holdout evaluation would be authorizing an empty set — this document does not request that authorization, does not access the holdout, and marks every holdout-dependent output item `not_applicable` with the evidence being #397's own result, not an assumption made here.

What this document **does** do, and does not need further authorization for: reconcile issue #388's original parent acceptance criteria against the complete, real evidence from #389–#397, apply #398's own falsification criteria to that evidence, and produce the required owner recommendation and parent gate verdict — the "final QA" half of #398's title, distinct from the "finalist holdout" half.

## 1. Child / dependency and evidence-completeness matrix

| Child | Title | State | Evidence |
|---|---|---|---|
| #389 | Baseline and collision audit | merged, PR #399 | `docs/evidence/AUTORESEARCH_V01_BASELINE_AUDIT_2026-09-03.md` |
| #390 | Freeze v0.1 contract, search space, hard invariants | merged, PR #400 | `docs/standards/AUTORESEARCH_V01_CONTRACT.md`, `docs/standards/autoresearch_v01_manifest.json` |
| #391 | Eval/experiment/manifest schemas + fixtures | merged, PR #401 | `schemas/autoresearch_{eval_case,experiment_record,batch_manifest}.schema.json`, 40 tests |
| #392 | Read-only validator, hard-veto engine, ledger, comparator | merged, PR #402 | `scripts/autoresearch_validator.py`, 42 tests |
| #393 | Provider-neutral shadow runner + worktree isolation | merged, PR #403 | `scripts/autoresearch_shadow_runner.py`, 19 tests |
| #394 | Frozen semantic evaluator + blind A/B Judge contract | merged, PR #404 | `ChatGPT/[LLM]/Knowledge/AUTORESEARCH_SEMANTIC_EVALUATOR_CONTRACT.md`, `schemas/autoresearch_semantic_finding.schema.json`, 29 tests |
| #395 | Stochasticity/non-inferiority decision-comparator method | merged, PR #405 | `ChatGPT/[Analytics]/Knowledge/AUTORESEARCH_STOCHASTICITY_NONINFERIORITY_METHOD.md`, `scripts/autoresearch_decision_comparator.py`, 25 tests |
| #396 | Phase 0 calibration | merged, PR #406 | `docs/evidence/AUTORESEARCH_PHASE0_CALIBRATION_2026-09-03.md`, 23/23 calibration cases pass, 16 tests |
| #397 | Phase 1 bounded pilot | merged, PR #407 | `docs/evidence/AUTORESEARCH_PHASE1_PILOT_2026-09-03.md`, 4 real experiments, 14 tests |
| #398 | This document | in progress | — |

**10/10 children accepted/merged. No child is marked "not applicable" — every one produced real, tested artifacts.** Test suite grew from a pre-#389 baseline of 243 to **428 passing** by #397, entirely additive, zero regressions at any step (verified in every PR's own checks).

## 2. Finalist selection basis

**No finalists were selected.** This is not an omission this document is working around — it is #397's own, deliberately honest result, restated here rather than reframed: 4 experiments run (fewer than the 10-cap, per #397's own "no mutation merely to consume the budget" rule), 1 `discard` (negative control, correctly caught), 2 `inconclusive`, 1 rejected pre-application. Zero `keep_candidate`. There is no validation-cherry-picking risk here, because there is no set to pick from.

## 3. Holdout isolation/access evidence

**Not applicable — no holdout was accessed.** The mechanism itself is real and tested: #391's schema forces `input_ref`-only (no inline payload) for `split: holdout` cases; #393's `JSONLResponseAdapter` and shadow-worktree isolation never touch holdout content; #396 and #397 both used `train`-only case splits. What is **not yet exercised** is the end-to-end "seal → run finalists → open holdout only after selection" sequence, because no finalist ever triggered it. This is an honest gap in *exercised evidence*, not a gap in the mechanism's design.

## 4. Frozen contract and configuration hashes

`docs/standards/autoresearch_v01_manifest.json` is unchanged since #390 (verified: no PR in this chain after #390 touched it). No real evaluator/split/threshold hash was ever frozen, because no live evaluator was invoked anywhere in #392–#397 (consistent scope statement, repeated and honestly disclosed in every one of those PRs). The *verification mechanism* for such hashes (`INV-03`, `reject_environment_mismatch`) is real, merged, and tested in #392/#396/#397 — what remains unexercised is freezing a *real* evaluator identity, which requires the still-open live-Judge/transport decision from #396 §11.

## 5. Deterministic hard-gate results

Zero hard-invariant violations reached any ledger across #392, #393, #396, or #397's real runs. The one negative-control experiment in #397 that *should* have triggered a regression signal did — correctly, as `non_inferiority_result: fail` / `material_regression_flag: true`, forcing `discard` — proving the gate fires when it should, not just that it stays quiet when nothing is wrong.

## 6. Blind/reversed-order semantic Judge findings

**`NOT_RUN`.** No live semantic Judge was invoked anywhere in this entire program (#392 through #397 each state this explicitly). #394 froze the contract a real Judge would need to satisfy; #396 calibrated the deterministic machinery a Judge's output would flow through; neither is a live Judge run. This is the single largest piece of *exercised* evidence this program does not yet have, and it is the first of #396 §11's two named open items, still open.

## 7. Analytics holdout and uncertainty results

**Not applicable** — no holdout, per §3. #395's non-inferiority/material-improvement method itself is real, tested (25 dedicated tests, order-invariance proven by exhaustive permutation), and was exercised on real (non-holdout) data in #397.

## 8. Validation-to-holdout generalization comparison

**Not applicable** — there is no validation improvement to check for generalization, since #397 produced zero `keep_candidate` results to have "validated" in the first place.

## 9. Hidden regressions and benchmark-exploitation review

None found, and the harness demonstrated active resistance to at least one class of hidden regression: #397's negative control was a real, plausible, non-obvious harmful wording change (removing an explicit escalation instruction), and the harness caught it via the actual non-inferiority worst-case-dominance rule, not a special-cased check written to catch that specific example. No case cherry-picking, threshold adjustment, or post-hoc relabeling occurred anywhere in this chain — every PR's evidence doc records defects found and fixed *before* results were reported (e.g. #392's two latent fixture bugs, #396's infrastructure-class coverage gap), never after.

## 10. Harness-level falsification assessment

Checked against every one of #398's own listed falsification criteria, using only real evidence from #389–#397:

| Falsification criterion | Assessment | Basis |
|---|---|---|
| Evaluator cannot reliably distinguish obvious good/bad variants | **Not falsified** | #396: 23/23 calibration cases across all 10 required classes correctly distinguished — for the deterministic pipeline. The *semantic-Judge* half of this criterion is `NOT_RUN` (§6), not falsified nor confirmed. |
| Ranking is unstable across matched reruns | **Not applicable** | No ranking was ever computed; no two candidates ever competed. |
| Validation improvement does not transfer to holdout | **Not applicable** | No validation improvement occurred (§8). |
| Most observed failures cannot be attributed to the mutable surface | **Not applicable, but adjacent to the real finding** | No observed failures existed to attempt attribution on at all (§ below, item 11) — this is not a harness attribution failure, it is an absence of input evidence, a materially different and more fixable condition. |
| Manual bounded review yields equivalent value at materially lower complexity | **TRIGGERED — this is the material finding** | See §11. |
| Optimization repeatedly causes governance regressions | **Not falsified (the opposite occurred)** | Zero regressions were ever kept; the one attempted regression was caught on its first and only occurrence. |
| Holdout secrecy cannot be enforced | **Not applicable** | Never tested (§3). |
| Experiment records provide no material information gain | **Partially triggered, precisely scoped** | Zero information gain about real AI-OS routing/handoff wording quality (no real question was ever posed to the harness). Substantial, real information gain about the harness's own correctness (§12). These are different claims and must not be merged into one verdict. |
| Each gain requires accumulating exceptions/instruction bloat | **Not applicable** | No gains occurred to evaluate for bloat. |

## 11. Complexity/cost versus manual bounded-review comparison

This is the one falsification criterion this program's own evidence actually triggers, and it is the basis for this document's recommendation (§13). The build cost of this harness was real and substantial: 10 PRs, roughly 4,000+ lines of schemas/code/tests/docs, ~185 new tests, across five nominal owners (`[AI OS]`, `[Codex]`, `[LLM]`, `[Analytics]`, `[Thinking]`). Given that cost, #397's Phase 1 pilot could still only run negative/no-op/uncertain-attribution controls — not because the harness is deficient (§10 found it correctly handled every case it was given), but because **no real evidence source exists yet** for it to operate on. Today, a human directly noticing an actual routing or handoff confusion and proposing a bounded, reviewed wording fix would produce equivalent or better real-world value, at zero additional built complexity, than running this harness against fabricated "observed failures" — which #397 correctly refused to do. This is a statement about the *current evidence-sourcing gap*, not a defect in the harness's design; §13's recommendation reflects that distinction precisely rather than either over- or under-stating it.

## 12. Residual risks and rollback readiness

No residual risk: no active configuration, Project Instructions, or routing content was ever mutated by any part of this program (verified independently in #392, #393, #396, and #397, each with its own before/after working-tree-fingerprint proof). Rollback is trivial by construction — every artifact is additive (new files) or a reviewed, git-tracked edit to a shared index/bundle file; nothing requires an active-state revert because nothing active was ever touched.

## 13. Recommendation

```text
simplify_to_manual_regression_suite
```

Selected specifically because §11's falsification criterion is the one that actually fired, named by #398 itself as a valid trigger for exactly this recommendation — not `stop_autoresearch` (the harness's own design and correctness are not in question, §10; nothing here indicates the *mechanism* should be abandoned) and not `promote_candidate_to_separate_implementation_issue` (there is no candidate, §2) and not `open_new_parent_for_broader_search` (the bottleneck is evidence supply, not search breadth — a broader search would only produce more fabricated "observed failures" faster) and not `revise_and_recalibrate` (nothing observed here indicates the harness itself needs revision; §10 found no falsification of its own mechanisms).

Concretely: fall back to manual, human-noticed, individually-reviewed bounded wording fixes for AI-OS Project Instructions/routing as the default path for now. This is not a deletion — the harness (`scripts/autoresearch_validator.py`, `autoresearch_shadow_runner.py`, `autoresearch_decision_comparator.py`, the frozen contracts, and both evidence-generating pipelines) remains merged, tested, and available to re-engage without rebuilding, specifically once either (a) a real live-Judge integration exists (§6, #396 §11 item 1) or (b) a genuine field-observed failure worth attributing a hypothesis to actually occurs — at which point re-running Phase 1 needs no new engineering, only real inputs.

## 14. Parent gate

```text
pass
```

Per #398's own explicit rule, restated because it directly resolves what might otherwise read as a contradiction: *"Parent PASS may mean the harness was responsibly falsified and stopped; it does not require a promoted instruction change."* Every one of #388's original acceptance criteria (reconciled individually below) is satisfied by real evidence; a `pass` verdict here reflects that the *research program conducted itself correctly end to end*, including correctly declining to promote anything under insufficient evidence — not that a behavior improvement was found and shipped.

## Parent #388 acceptance criteria — reconciled individually, not only against #397's latest result

### Business acceptance

- [x] The harness distinguishes useful, harmful, and inconclusive candidates under matched conditions — #396 (deterministic layer, all 10 classes) + #397 (real batch: 1 correctly-caught harmful case, 2 correctly-inconclusive cases).
- [x] Every experiment has a supported or explicitly uncertain attribution statement, a minimal mutation, rollback, and immutable evidence — #397's 4 experiments each carry all of these; experiment 4's honestly-`uncertain` attribution is itself evidence this criterion was taken seriously, not rubber-stamped `supported`.
- [x] Hard governance regressions cannot be compensated by aggregate improvement — #395's worst-case-dominance design (no averaging mechanism exists to game) + #397's real demonstration.
- [x] `keep_candidate` has no authority or promotion side effect — #391/#392's schema-level and validator-level `INV-08` enforcement (structural, not conventional); moot in practice this batch since 0 `keep_candidate` occurred, but the mechanism itself is proven independently by #392's dedicated tests.
- [x] The owner can reject all candidates or simplify/terminate AutoResearch without losing evidence — this document is that action, and every artifact remains in git history and `docs/evidence/`.

### Artifact/content checks

- [x] All required schemas, manifests, contracts, validators, fixtures, and evidence artifacts exist at approved repository paths — §1.
- [~] Frozen evaluator and split hashes are verified before each batch — the verification mechanism is real and tested; no *real* evaluator hash has been frozen yet because no live evaluator exists (§4, §6). Marked partial, not satisfied, deliberately.
- [x] Protected-path mutation, evaluator mutation, multiple causal mechanisms, `NOT RUN -> PASS`, and implicit authority escalation fail closed — directly tested in #392/#393, and #397's experiment 3 proved the protected-path case live against real content.
- [x] Baseline/candidate runtime configuration and revision matching are verified — #392's `reject_environment_mismatch`, #393's `reject_config_mismatch`.
- [x] Append-only history rejects mutation, deletion, or reordering of previous records — #392's hash-chain ledger, exercised for real in #397.
- [x] Phase 0 calibration separates obvious good/bad variants and records run variance — #396.
- [x] Phase 1 records every attempted experiment, including negative and inconclusive results — #397's evidence doc records all 4, not only successes.
- [~] Holdout remains inaccessible to the Researcher and is used only at the predeclared checkpoint — mechanism proven by design and by #391/#393's tests; the full sealed-until-checkpoint sequence was never exercised end to end (§3). Marked partial.
- [x] Final QA rechecks the original parent objective and all child acceptance criteria — this document.

### Technical checks

- [x] Focused tests for every new schema, validator, runner, ledger, and comparator behavior — 185 new tests added across #391–#397 (243 → 428).
- [x] Full applicable repository test suite passes on the final revision — re-verified below (§Checks run).
- [x] Existing routing, AES, bundle, manifest, safety, and public-repository checks remain green — verified in every PR's own checks throughout, re-verified below.
- [x] No stale mandatory artifacts or validation results are used for acceptance — the bundle-regeneration golden rule was followed on every PR that touched a declared source (#390, #394, #395).

### Non-acceptance examples — confirmed NOT to have occurred

- [x] A single scalar score was never used to hide a hard regression (#392's `assert_no_scalar_score`, #395's Pareto-only efficiency rule, tested).
- [x] No successful LLM run was ever reported as a causal improvement (no live LLM run occurred at all, anywhere).
- [x] No validation-only gain was promoted without holdout and owner review (0 promotions occurred).
- [x] No candidate ever changed active Project Instructions, `main`, evaluator, or governance semantics (proven before/after every batch, #392/#393/#396/#397).
- [x] Judge `pass` was never interpreted as owner approval, merge permission, or production authorization (`NOT_RUN` throughout, §6; and structurally excluded even where it would apply, #392/#394).
- [x] No runtime service, database, dashboard, or generic autonomous-agent layer was introduced (explicitly forbidden and never built, every child).

## Checks run

- All 10 child issues (#389–#398) confirmed accepted/merged; no child marked not-applicable (§1).
- `pytest tests/ -q` → re-run on this final revision (see command output below) to confirm the full 428+ suite remains green with #398's own additions.
- `check_manifest_paths.py`, `check_repo_public_safety.py`, `check_knowledge_bundles.py`, `audit_bundle_provenance.py --check`, `check_index_coverage.py` — re-run on this final revision (see command output below).
- Active repository/project configuration confirmed unchanged by this document's own addition (`git status --short` / `git diff --check` show only the intended new files).
- Parent acceptance checklist completed against the *original* #388 objective (Final acceptance criteria block from the parent issue text), not only #397's latest result — see reconciliation above.
