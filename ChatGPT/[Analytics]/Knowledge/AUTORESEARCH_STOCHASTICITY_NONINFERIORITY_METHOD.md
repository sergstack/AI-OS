# AutoResearch v0.1 — Stochasticity, Non-Inferiority & Decision-Comparator Method

- Status: `candidate` method specification, provisional thresholds only (per issue #395's own input-layer rule: "before [Phase 0 calibration], numeric thresholds must remain provisional or unset"). Not authorized for Phase 0/Phase 1 execution on its own.
- Owner: `[Analytics]`. Semantic rubric/model choice remains `[LLM]`/#394's; repository integration remains `[Codex]`'s.
- Parent: [#388](https://github.com/sergstack/AI-OS/issues/388). Defining child: [#395](https://github.com/sergstack/AI-OS/issues/395). Depends on: [#390](https://github.com/sergstack/AI-OS/issues/390) (contract/manifest, merged), [#394](https://github.com/sergstack/AI-OS/issues/394) (evaluator/finding contract, merged), [#392](https://github.com/sergstack/AI-OS/issues/392) (comparator interface, merged).
- Reuses, does not restate: `docs/standards/AUTORESEARCH_V01_CONTRACT.md`, `docs/standards/autoresearch_v01_manifest.json`, `schemas/autoresearch_experiment_record.schema.json`, `schemas/autoresearch_semantic_finding.schema.json`, `scripts/autoresearch_validator.py`'s `VERDICT_PRECEDENCE`/hard-gate vocabulary, `ChatGPT/[Analytics]/Knowledge/QUANTITATIVE_SANITY_GATE.md`'s method-applicability discipline.

## Why this is a rule-based exact method, not inferential statistics

Issue #389's baseline audit found **no existing statistical significance/non-inferiority tooling anywhere in this repository**, and issue #395 explicitly forbids inventing one dishonestly: *"No p-value, confidence interval, or significance claim unless actually computed under an explicit method and assumptions."* Phase 1 runs 3–5 reruns per case (`benchmark_spec.json`'s `runs_per_case` precedent) of a **discrete, ordinal, non-independent** outcome (an LLM Judge verdict: `pass`/`revise`/`blocked`). Asymptotic methods (t-tests, normal-approximation confidence intervals) assume sample sizes and independence this data structurally does not have; using one anyway, on N=3–5, would be exactly the dishonest "statistical significance" claim issue #395 bans.

This method is therefore **exact and rule-based, not asymptotic**: every "non-inferiority," "material improvement," and "inconclusive" determination below is a deterministic function of the *actual observed reruns*, never a projected/estimated population parameter. Where the method cannot honestly distinguish signal from noise at the available sample size, it returns `inconclusive` — that is a designed, frequent, correct output, not a failure mode.

## 1. Matched baseline/candidate run design

One observation row (§13) per `(case_id, run_id, baseline_or_candidate, model_provider_runtime_hash, evaluator_version_hash)` (issue #395 Grain, reused verbatim as the row identity). A comparison is **matched** only when baseline and candidate rows for the same `case_id` share the same `model_provider_runtime_hash` and `evaluator_version_hash` — see §3. Every row's `hard_gate_status` comes from issue #392's `autoresearch_validator` output; this method never re-derives it.

## 2. Repeated baseline sampling

The baseline is resampled the same number of times as the candidate for every case entering the target-family material-improvement rule (§7) — a single baseline run is never treated as ground truth to compare N candidate runs against, because baseline verdict variance (Judge or model stochasticity) would then be misattributed entirely to the candidate. Non-target families (§6) may use a smaller baseline sample only when the non-inferiority rule's worst-case-dominance logic (§6) does not depend on baseline sample count for correctness — stated explicitly per family in the batch manifest, never assumed.

## 3. Provider/model/runtime/configuration changes

Reuses `autoresearch_shadow_runner.reject_config_mismatch` (issue #393) and `autoresearch_validator.reject_environment_mismatch` (issue #392) as the upstream gate — this method does **not** re-implement configuration-mismatch detection. Its own rule, additive to those: **no pooling across rows with different `model_provider_runtime_hash` or `evaluator_version_hash` values** (issue #395 Forbidden actions, reused verbatim). A comparison spanning mixed hashes is not merely down-weighted — it is `missingness_reason: "configuration_changed"`, excluded from the matched set entirely, and forces `non_inferiority_result` / `material_regression_flag` computation for that case to `inconclusive` rather than silently dropping the row from a denominator (Required rule: "Insufficient sample... environment change... -> `inconclusive`").

## 4. Case-level normalization

`normalized_behavior_result` reuses `scripts/autoresearch_validator.py`'s `VERDICT_PRECEDENCE` mapping verbatim (`pass=0 < revise=1 < blocked=2`) rather than inventing a second severity scale. A `missing` observation (no evaluator finding recorded) normalizes to `None`, never silently coerced to `pass` (issue #395 Required rule: missing observation is never dropped or optimistically rounded).

## 5. Observed run variance / disagreement

`run_variance_or_disagreement` for a `(case_id, baseline_or_candidate)` group with N reruns: `true` if the set of `normalized_behavior_result` values across those N runs has more than one distinct value, else `false`. This is an exact set-cardinality check, not a variance formula — appropriate to N≤5 discrete ordinal data, and reused identically by §6 and §7 below rather than each defining its own noise notion.

## 6. Non-inferiority logic for non-target families

**Worst-case dominance**, not an averaged or statistical test: a non-target case family is non-inferior only if, across every matched rerun pair for every case in that family, **the candidate's `normalized_behavior_result` is never strictly worse than the paired baseline's**. One case, one rerun, one regression is sufficient to fail this rule — there is no "mostly fine" aggregate. This directly implements the Required rule "Non-target families must satisfy a predeclared non-inferiority rule" and the Business acceptance criterion "a candidate cannot win by averaging away a material family-level regression": there is no average to hide behind by construction.

`non_inferiority_result` per family: `"pass"` (dominance holds across all matched pairs), `"fail"` (at least one matched pair shows a strict candidate regression — this sets `material_regression_flag`), or `"inconclusive"` (insufficient matched pairs, a configuration mismatch in the family per §3, or unresolved `run_variance_or_disagreement` on a pair where the two runs' verdict sets don't allow an unambiguous worst-case comparison).

## 7. Material-improvement logic for the target family

A target-family case shows material improvement only when **both**:

1. every matched candidate rerun for that case has a strictly better `normalized_behavior_result` than its paired baseline rerun (reproducible across all available reruns — "one successful run is never evidence of improvement," reused verbatim as the Required rule), and
2. the baseline's own reruns for that case are mutually consistent (`run_variance_or_disagreement == false` for the baseline group) — if the baseline itself is noisy on this case, an apparent candidate advantage cannot be distinguished from baseline flakiness at this sample size, and the case contributes `inconclusive`, not a counted improvement.

This is the "empirically observed noise/uncertainty boundary" the Required rules reference: the boundary is *baseline's own observed consistency*, not an assumed distribution.

## 8. Escalation from 3 to a maximum of 5 matched runs

If, at 3 matched reruns, a target-family case's material-improvement determination (§7) is `inconclusive` because of unresolved `run_variance_or_disagreement` on either side, escalate to up to 2 additional reruns (5 total) for that case only — never a blanket re-run of the whole batch. If the case remains `inconclusive` at 5 reruns, it **stays** `inconclusive`; there is no further escalation (a hard ceiling, matching this repository's own corrective-loop-ceiling discipline). This applies per-case, not per-batch: an unrelated case that resolved cleanly at 3 reruns is not re-run just because a different case escalated.

## 9. Mandatory `inconclusive` conditions

Reused verbatim as a checklist (issue #395 Required rules, not restated as new prose): insufficient matched sample for the rule being evaluated; material Judge disagreement (an unresolved `run_variance_or_disagreement` that §7/§8 could not resolve within the 5-run ceiling); a missing observation (`missingness_reason` set, §10); an environment/configuration change (§3); or overlapping uncertainty between baseline and candidate that the exact worst-case rules in §6/§7 cannot separate. None of these ever silently rounds to `keep_candidate` or `discard`.

## 10. Missing-data and evaluator-disagreement treatment

A missing observation row (an expected `(case_id, run_id, baseline_or_candidate)` combination that never arrived — e.g. `autoresearch_shadow_runner`'s `MISSING_OBSERVATION` finding, issue #393) is recorded with `missingness_reason` set to a specific value (`"no_observation"`, `"configuration_changed"`, `"evaluator_disagreement_unresolved"`, or `"hard_gate_violated"`) and is **excluded from the matched-pair count used by §6/§7's dominance rules**, never imputed and never silently omitted from the case's own `decision_contribution` — a missing row always contributes an explicit `inconclusive`-leaning signal for its case, visible in the case's own row, not just absent from an aggregate.

## 11. Separation of behavioral and efficiency vectors

Reuses `autoresearch_validator.build_comparison_artifact`'s existing separation (issue #392) verbatim: `behavioral_vector` and `efficiency_vector` are computed independently and never combined into one field. This method's own rule, additive: **the efficiency vector is only evaluated after §6 and §7 both clear** (non-target non-inferiority `pass` and target-family material improvement not `inconclusive`/regression) — "Efficiency is considered only after behavioral non-inferiority," reused verbatim as the Required rule.

## 12. Pareto / non-domination rule for efficiency

No single weighted efficiency score (Required rule, reused verbatim). A candidate's efficiency result is `"non_dominated"` only if it is not simultaneously worse than baseline on **both** `cost_delta` and `latency_delta` (issue #391 `efficiency_results` fields, reused verbatim) — i.e. it must be better-or-equal on at least one dimension while not worse on the other. `"dominated"` if strictly worse on both. `"not_evaluated"` if §6/§7 did not clear, per §11.

## 13. Deterministic output fields consumed by #392

One observation row per issue #395's own Grain, with exactly the 16 required fields (formalized as `schemas/autoresearch_observation_row.schema.json` in this PR):

```text
case_id
case_family
run_id
baseline_or_candidate
model_provider_runtime_hash
evaluator_version_hash
hard_gate_status
normalized_behavior_result
target_family_flag
paired_delta
run_variance_or_disagreement
non_inferiority_result
material_regression_flag
missingness_reason
decision_contribution
limitations
```

`decision_contribution` is this row's own vote toward the case's final decision (`"keep"`, `"discard"`, `"inconclusive"`, or `"not_applicable"` for a non-decision-bearing row such as a pure efficiency observation) — the batch-level `keep_candidate`/`discard`/`inconclusive` decision (issue #391 `experiment_record.decision`) is the deterministic aggregation of every row's `decision_contribution` (§14), not a separate judgment call layered on top.

## 14. Aggregation to `keep_candidate` / `discard` / `inconclusive`

Order-invariant, hard-veto-first, exactly reusing issue #391/#392's decision vocabulary (no fourth value invented):

1. **Hard-veto dominance** (reused from issue #392's `enforce_hard_veto_dominance`, applied here to the observation-row level): if any row has `hard_gate_status == "violated"`, the batch decision is `discard` regardless of every other row's `decision_contribution` — computed as a `set`/`any()` check, so row order never changes the result.
2. Else, if any non-target family's `non_inferiority_result == "fail"` (a `material_regression_flag`), the batch decision is `discard` — one regression is sufficient (§6), independent of how many rows show improvement elsewhere.
3. Else, if the target family's material-improvement result (§7/§8) is not yet resolved for at least one case (still `inconclusive` after the 5-run ceiling), or any row's `missingness_reason` is set for a case that would otherwise materially affect the decision, or any `run_variance_or_disagreement` remains unresolved, the batch decision is `inconclusive`.
4. Else (all non-target families non-inferior, target family shows reproducible material improvement, no unresolved missingness/disagreement), the batch decision is `keep_candidate` — efficiency (§12) is reported alongside but never changes this behavioral decision, per §11's ordering rule.

Each step is a pure function over the *set* of rows (via `any()`/`all()`/set operations), not a fold sensitive to input order — proven by an order-permutation test (§synthetic checks).

## 15. Limitations and minimum sample requirements

- Minimum 3 matched reruns per case before any material-improvement or non-inferiority determination is attempted; below that, the case contributes `inconclusive` unconditionally.
- This method establishes **reproducibility across observed reruns**, not statistical generalization to unobserved inputs or future model versions — it makes no claim beyond the specific frozen batch's own evidence.
- A method version change (this document's own revision) requires a new batch; old batch results remain immutable evidence under issue #392's append-only ledger, never retroactively re-scored under a newer method.
- Validation-case repeated exposure across successive experiment batches must be recorded as an explicit overfitting risk in `limitations` (Required rule, reused verbatim) — this method does not itself detect overfitting; it only requires the risk to be visible when validation cases repeat.

## 16. Calibration/holdout reporting template

Reused, not duplicated: Phase 0 calibration (`docs/standards/AUTORESEARCH_V01_CONTRACT.md` §10, issue #396) must show this method correctly separates a predeclared obvious-good and obvious-bad synthetic variant using the exact same aggregation in §14 — not a relaxed or manual check. The holdout report template is the same observation-row schema (§13) plus the batch-level decision (§14); no separate holdout-specific schema is introduced. Holdout rows are computed by this method exactly as validation rows are; only the *disclosure timing* differs (per the frozen contract's sealed-holdout rule), never the calculation.

## Synthetic checks (proved by tests, not asserted in prose)

Every bullet in issue #395's "Checks" section has a corresponding fixture and test in `tests/test_autoresearch_decision_comparator.py`: obvious improvement with no regression → `keep_candidate`; target gain inside the baseline's own noise band → `inconclusive`; one non-target material regression → blocks `keep` even alongside a target-family improvement; a missing run or unresolved evaluator disagreement is visible in `missingness_reason`/`run_variance_or_disagreement`, never silently dropped; a changed `model_provider_runtime_hash` prevents a matched comparison; an efficiency-only gain with `non_inferiority_result != "pass"` never reaches `"non_dominated"` evaluation; a hard-gate violation dominates every other row's contribution; and permuting row order before aggregation produces an identical decision.
