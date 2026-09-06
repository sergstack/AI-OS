# [Analytics] EDA-to-Claim Calibration Review — issue #451

Status: **regression/calibration review, not a new controls framework**.
`owner review required` before any promotion, merge, deployment, or Project
sync. This document records a structured written (paper-trace) evaluation
against the existing `ANALYTICAL_REASONING_STANDARD.md`, templates, QA, and
governance text — reasoning through each observed WineMag wording pattern and
each of the ten acceptance-criteria scenarios named in issue #451 against the
current contract. It is **not** a live LLM execution run; no live model, no
wine dataset, and no wine model were built or run as part of this review.
That limitation is stated explicitly wherever it affects a recommendation,
following the same honesty style as `P1_PILOT_EVIDENCE_2026-09-06.md` and
`P1_449_PILOT_EVIDENCE_2026-09-06.md`.

Per issue #451's own review correction: the underlying WineMag dataset,
execution trace, code, calculations, and exact externally loaded project
context were **not independently verified**. This review does not label the
supplied numbers false, does not claim a proven recurring runtime defect,
and does not assert that `PROJECT_INSTRUCTIONS.md` or any specific existing
rule caused the wording in the supplied answer. Attribution remains
uncertain; this review closes the gap between "a rule exists on paper" and
"the rule is traceable to a concrete, worded example," which is what the
paper-trace below actually demonstrates.

## 1. Scope and changed files

All changes are inside `ChatGPT/[Analytics]/**`; `docs/knowledge_bundle_provenance_audit.{json,md}`
were mechanically regenerated (byte-count/fingerprint sync only), same
pattern as PR #447/#450's own provenance-sync commits. No file outside these
paths was modified.

Changed:

- `ChatGPT/[Analytics]/Knowledge/GOVERNANCE_AND_ANTI_PATTERNS.md` — new
  "EDA-to-claim calibration additions (issue #451)" section, 7 rows added to
  the existing P0 failure-mode table pattern. No new table structure, no new
  taxonomy.
- `ChatGPT/[Analytics]/Knowledge/SMOKE_QA_FOR_ANALYTICS.md` — new case 15 (9
  scenarios: 15.1–15.9) covering the ten acceptance-criteria rows from issue
  #451.
- `ChatGPT/[Analytics]/package_manifest.json` — added
  `Templates/METRIC_DEFINITION_CARD_TEMPLATE.md` (the discrepancy issue #451
  named) plus three more files with the identical gap
  (`Knowledge/AUTORESEARCH_STOCHASTICITY_NONINFERIORITY_METHOD.md`,
  `Knowledge/P1_PILOT_EVIDENCE_2026-09-06.md`,
  `Knowledge/P1_449_PILOT_EVIDENCE_2026-09-06.md`) and this review's own new
  file. See §6 for the verification trail.
- `ChatGPT/[Analytics]/Knowledge/CHANGELOG.md` — new dated entry.
- `ChatGPT/[Analytics]/Knowledge/ANALYTICS_PROJECT_FILES_INDEX.md` — index
  row for this file.
- `ChatGPT/[Analytics]/Knowledge/EDA_CLAIM_CALIBRATION_REVIEW_2026-09-06.md`
  — this file (new).
- `docs/knowledge_bundle_provenance_audit.json` and
  `docs/knowledge_bundle_provenance_audit.md` — mechanically regenerated via
  `scripts/audit_bundle_provenance.py --write`.

Not changed: `ChatGPT/[Analytics]/Knowledge/ANALYTICAL_TECHNIQUES.md` (see
§4, zero diff), `ANALYSIS_CONTINUATION_GATE` (§15.3 of
`ANALYTICAL_REASONING_STANDARD.md`, left exactly as issue #445/#449 left
it — deferred, not activated), `ChatGPT/[Analytics]/PROJECT_INSTRUCTIONS.md`
(near its 8000-char ceiling; no content added there per this issue's own
warning), `confidence: high/medium/low` and every other existing Analytics
enum, `Codex_Tasks/**`, and the 22-method registry. Bundle *outputs* are
regenerated deterministically via `scripts/build_knowledge_bundles.py
--write`, which only rewrites files already declared as generated outputs in
`knowledge_bundle_manifest.json` — that manifest's `sources` lists were not
edited (they were already correct; see §6).

## 2. R1 — baseline and defect attribution mapping

Each observed WineMag wording transition, mapped to the rule that should
already govern it, with an honest verdict on whether it is already covered
or needed a narrow addition.

| # | Observed failure pattern | Existing owning rule | Reproduction/trace evidence | Verdict | Correction |
|---|---|---|---|---|---|
| 1 | "undervalued by the market" from high score + moderate listed price | Claim ladder (§6/§7), `causal_status`, `METRIC_DEFINITION_CARD.forbidden_interpretations` | Traced: the existing text states `causal_status: not_applicable / association_only / explanation_supported / causal_evidence` and requires evidence before promotion, but no example ties an in-sample score/price association to a "market inefficiency" reading specifically — an unguided application of the existing rule could plausibly still let "undervalued" through as a plausible-sounding `INTERPRETATION` without a discriminating check. | **genuine narrow gap** | Added row 2 in `GOVERNANCE_AND_ANTI_PATTERNS.md` (model-implied value != market inefficiency); smoke QA 15.2. |
| 2 | model-implied price difference -> "fair price" / "overpayment" | Same as #1, plus units/log-transform explicitness | Same trace as #1; additionally the existing text has no explicit reminder to keep units/transform explicit for a model-conditional residual. | **genuine narrow gap** (same rule family as #1) | Same added row; smoke QA 15.4. |
| 3 | selected producer reviews -> "almost impossible to buy a bad wine" | `generalization_scope` / `generalization_evidence` (`CLAIM_EVIDENCE_REGISTRY_TEMPLATE.md`) | Traced: the existing `generalization_evidence` rule explicitly covers *temporal* generalization ("single-period -> systemic/recurring/persistent") but its worked example does not cover *selection-based* generalization (a hand-picked or top-N subset of reviews standing in for the whole producer/population). Applying the existing rule by analogy would likely still catch this, but the wording gap is real enough that an ambiguous application could miss it. | **genuine narrow gap** | Added row 4 (selected reviews/volume != guarantee/expertise); smoke QA 15.4. |
| 4 | observed reviewer averages -> "strict/generous critics" | §5 population/denominator controls, `POPULATION_CONTRACT` (§15.1) | Traced: §5's population/denominator machinery targets ratio/rate/share metrics with a *known* population definition; it does not by itself prompt an overlap/common-support check between a *rater identity* and *what that rater happens to review* (region/style/product mix). This confound-detection step is not named anywhere in the existing text. | **genuine narrow gap** | Added row 6 (reviewer confound requires common-support check); smoke QA 15.5. |
| 5 | in-sample text association -> expected predictive capability | `causal_status: association_only`, `FINAL_EVIDENCE_SUFFICIENCY` | Traced: the existing claim ladder and `causal_status` enum correctly block an *causal* promotion from association, but predictive-performance is a distinct axis from causal_status that the existing text does not explicitly name — nothing currently requires a held-out split/baseline/leakage check before a *predictive* (as opposed to causal) claim from an association. `ANALYTICAL_TECHNIQUES.md`'s registry has no text/NLP method at all (confirmed by grep), so this pattern falls outside the registry entirely and was governed only by the general association/causal rule, which is a partial but not full fit. | **genuine narrow gap** | Added row 7 (in-sample association != measured predictive performance); smoke QA 15.6. |
| 6 | exploratory regional/sort rankings -> purchase-oriented recommendations | `RECOMMENDATION_EVIDENCE` (§16.2, issue #449) | Traced: §16.2 already states `diagnostic evidence != intervention evidence` and caps `recommendation_status <= pilot_candidate` when `test_or_backtest_performed = no`. This generalizes directly to "ranking observed -> should buy these wines" (an untested intervention/action recommendation) without modification — the rule text ("management recommendation", "intervention") is domain-general, not corporate-specific wording that would need re-scoping. | **already covered** | No rule change. Regression check: smoke QA 15.7 exercises the untested-recommendation cap on a non-corporate (purchase-recommendation) fixture to confirm the existing wording transfers. |

Five of six patterns needed a narrow, localized addition (all placed as new
rows in the existing `GOVERNANCE_AND_ANTI_PATTERNS.md` failure-mode table,
reusing its exact existing format — no new table, no new section type, no
new field). One pattern (exploratory rankings -> recommendations) was
already adequately covered by the #449 `RECOMMENDATION_EVIDENCE` control and
required only a regression smoke-QA case, not a text change. This matches
the issue's own framing that most of R1–R5 would likely be "already
covered," with narrow additions where genuinely ambiguous — five of six
here needed a small addition, one did not.

## 3. R2 — claim-specific calibration through existing fields

The five bullet examples in issue #451's R2 map one-to-one onto four of the
six rows above (points != quality is new; residual != market-inefficiency
overlaps row 1/2's addition; definition != evidence is new; selected-reviews
!= guarantee overlaps row 3's addition; listed-price != current-price is
new). All five were placed as rows in the existing
`GOVERNANCE_AND_ANTI_PATTERNS.md` failure-mode table rather than a new `§17`
in `ANALYTICAL_REASONING_STANDARD.md`, per the issue's own steer. No keyword
blacklist was implemented for "quality" / "best" / "fair" — the added rows
name the *asserted meaning and evidence gap*, not a forbidden word list, and
existing legitimate terminology (e.g. "main quantified contributor",
"supported explanation") is unaffected.

| R2 bullet | Placement | Verdict |
|---|---|---|
| `points` is observed rating, not objective quality/preference | `GOVERNANCE_AND_ANTI_PATTERNS.md` row 1 | narrow_example_added |
| expected price/residual is model-conditional, not market inefficiency/fair value | `GOVERNANCE_AND_ANTI_PATTERNS.md` row 2 | narrow_example_added |
| a definition/owner decision cannot manufacture missing evidence | `GOVERNANCE_AND_ANTI_PATTERNS.md` row 3 | narrow_example_added |
| selected high-score reviews / review volume do not guarantee future purchases or expertise | `GOVERNANCE_AND_ANTI_PATTERNS.md` row 4 | narrow_example_added |
| dataset-listed price does not establish current price/availability/purchase suitability | `GOVERNANCE_AND_ANTI_PATTERNS.md` row 5 | narrow_example_added |

## 4. R3 — population, denominators, deduplication, and metric semantics

The joint-vs-conditional regression target
(`P(score>=90 AND price<=20 | country) != P(score>=90 | price<=20, country)`)
was checked against `METRIC_DEFINITION_CARD_TEMPLATE.md`'s `population` /
`numerator` / `denominator` fields and the activated `POPULATION_CONTRACT`
(§15.1, issue #445, `numerator_population` / `denominator_population` as
distinct required fields). Traced: the existing card and contract *already
force* an explicit, separately-stated numerator population and denominator
population — a correctly completed card cannot silently collapse the two
probabilities into one field, because `numerator_population` and
`denominator_population` are already separate required entries. This is
**already covered as a mechanism**; what was missing was a concrete worked
example demonstrating the exact joint-vs-conditional confusion pattern named
by the issue. That gap is closed by smoke QA 15.3, not a text change.

Deduplication grain (exact-content duplicates vs. unique bottle/SKU/vintage)
is already addressed by `RECONCILIATION_CONTRACT`'s (§15.2) `matched_population`
/ `identity_mapping_status` fields and the existing `DATA_CONTRACTS.md`
`VALUE_STATE.UNMATCHED` semantics; no change needed.

Undefined composite score ("price/quality value") handling is already
addressed by `METRIC_DEFINITION_CARD_TEMPLATE.md`'s `status: provisional`
path ("may still be shown with an explicit limitation but cannot anchor a
strong conclusion") — this permits a scoped partial answer without blocking
the whole task. Smoke QA 15.7 exercises this directly as a regression case
since it was not previously scenario-tested for this specific "undefined
value metric, useful partial answer" shape.

**Verdict: already_covered (mechanism); smoke_qa_added (regression example).**
No change to `METRIC_DEFINITION_CARD_TEMPLATE.md`, `POPULATION_CONTRACT`, or
`RECONCILIATION_CONTRACT` field lists.

## 5. R4 — proportionate robustness and realistic model prerequisites

Checked whether the existing "minimum sufficient method set" philosophy
(§3 of `ANALYTICAL_REASONING_STANDARD.md`: "Include a method only if it can
materially change at least one of: finding, confidence, risk, recommendation,
limitation, evidence assurance… Stop adding methods when none is likely to
change those outputs") already implements "smallest applicable check, not
every check universally." Traced: yes — this is precisely the existing
rule; no global sample-size/significance threshold exists anywhere in the
standard (confirmed by reading §§1–16 in full), consistent with the issue's
instruction not to invent one.

The reviewer-adjustment / common-support prerequisite named in R4 is the one
genuinely new element (see §2 row 4 above; added as a `GOVERNANCE_AND_ANTI_PATTERNS.md`
row, exercised by smoke QA 15.5). The NLP baseline/split/leakage prerequisite
is the other genuinely new element (§2 row 5; smoke QA 15.6). Both were
already counted as narrow additions in §2/§3 above and are not duplicated
here.

**Verdict: already_covered (minimum-sufficient-method-set philosophy, §3);
the two concrete robustness gaps it under-specified (reviewer confound, NLP
validation) are counted once, in §2/§3, not as separate R4 rules.**

## 6. R5 — preserve analytical usefulness and routing

Checked `ROUTING_AND_HANDOFF.md` and `PROJECT_INSTRUCTIONS.md`'s handoff
section. Traced: `ROUTING_AND_HANDOFF.md` already states "Analytics default:
for metrics, marts, data contracts, QA, calculations, deviations, charts and
analytical memo structure: stay in `[Analytics]`" and "Handoff to Codex" /
"Thinking -> Analytics" sections that keep bounded recommendations,
methodology, and acceptance criteria inside `[Analytics]`, routing out only
implementation (`[Codex]`), narrative/model routing (`[LLM]`), or genuine
strategy/decision (`[Thinking]`). `PROJECT_INSTRUCTIONS.md`'s "Handoff out
only when the task leaves analytics scope" list is consistent with this.
Nothing in either file routes an in-scope interpretation, bounded
recommendation, or exploratory idea out of `[Analytics]` by default.

**Verdict: already_covered, no change.** Regression protection: smoke QA
15.9 (positive control / routing) confirms a routine result stays in
`[Analytics]` and only a genuinely strategic decision (e.g. "which churn
strategy to pursue") routes to `[Thinking]`, per the existing rule text
verbatim.

## 7. R6 — delivery and effective-context check (manifest finding)

Two distinct manifest-like files exist for `[Analytics]`:

1. Root canonical `knowledge_bundle_manifest.json` — the generator input for
   `Knowledge_Bundles/*`. Verified via direct inspection: the
   `ANALYTICS_06_TEMPLATES.md` bundle entry's `sources` list **already
   includes** `ChatGPT/[Analytics]/Templates/METRIC_DEFINITION_CARD_TEMPLATE.md`,
   and the rendered bundle file contains the template's content (confirmed
   by `grep -n METRIC_DEFINITION_CARD_TEMPLATE`, 4 hits including a `## From:`
   heading at line 834). **This file was already correct; issue #451's
   premise, read against this specific file, is stale — no fix needed here.**
2. `ChatGPT/[Analytics]/package_manifest.json` — a separate, independently
   maintained "analytics_project_settings_full" file list. Verified via
   direct set-difference against the actual `Knowledge/`/`Templates/`
   directory contents: `Templates/METRIC_DEFINITION_CARD_TEMPLATE.md` **was
   genuinely absent** from this file's list, along with three more
   recently-added files with the identical gap
   (`Knowledge/AUTORESEARCH_STOCHASTICITY_NONINFERIORITY_METHOD.md`,
   `Knowledge/P1_PILOT_EVIDENCE_2026-09-06.md`,
   `Knowledge/P1_449_PILOT_EVIDENCE_2026-09-06.md`). This matches a prior,
   independent finding: `docs/evidence/PROJECT_WIDE_REVISION_REVIEW_2026-09-03.md`
   already flagged "`[Analytics]`: two package manifests (`Knowledge/MANIFEST.md`,
   root `package_manifest.json`), both stale, neither enforced by any check
   script" as a high-severity theme-3 finding three days before this issue.
   `Knowledge/MANIFEST.md` was independently confirmed to already list
   `Templates/METRIC_DEFINITION_CARD_TEMPLATE.md` correctly (line 65) — only
   `package_manifest.json` had the gap.

**Verdict: genuine_bug_fixed.** All four missing entries (plus this review's
own new file) were added to `package_manifest.json.files` (§1). No script in
`scripts/` currently enforces this file's completeness — that remains a
known, pre-existing gap (documented in the 2026-09-03 review) and is out of
this issue's bounded scope to close with a new validation script; the fix
here is the file-content repair the issue explicitly authorizes, not a new
check-script project.

`UPLOAD_LIST.md` (`Knowledge_Bundles/`) requires Project Instructions to be
pasted separately and lists 6 required + 1 optional bundle; this review
changed the *source* files for bundle 05 (`GOVERNANCE_AND_ANTI_PATTERNS.md`,
`SMOKE_QA_FOR_ANALYTICS.md`) and bundle 01 (`ANALYTICS_PROJECT_FILES_INDEX.md`
index row only). Both were regenerated via
`scripts/build_knowledge_bundles.py --write` (see §8). Repository
regeneration is **not** evidence of external ChatGPT Project upload; external
synchronization and any post-sync smoke QA remain `NOT RUN` / owner-gated
(see §9).

## 8. Ten-scenario acceptance table (paper-trace only)

All 10 rows from issue #451's acceptance-criteria table, implemented as
`SMOKE_QA_FOR_ANALYTICS.md` case 15 (scenarios 15.1–15.9; rows 3 and the
denominator check share scenario 15.3, and rows for "valid description +
invalid generalization" / "model residual + producer/reviewer claims" are
scenarios 15.2/15.4 respectively — see the case file for exact mapping).

| Acceptance row | Scenario | Baseline (pre-#451 contract) | Candidate (post-#451 contract) | Result |
|---|---|---|---|---|
| Execution honesty | 15.1 | No explicit rule forbidding upgrading a user's "I calculated" claim to verified `executed` status, beyond the general `blocked != executed` lineage rule (§4). | Same lineage rule applies directly; no new field needed — `method_execution_id` / `execution_status` already require actual execution evidence, not user assertion. | **pass** (already covered; no candidate change; regression case added) |
| Valid description + invalid generalization | 15.2 | General claim-ladder/`causal_status` rule exists but no worked example ties it to "undervalued by market." | New `GOVERNANCE_AND_ANTI_PATTERNS.md` row makes the exact pattern explicit. | **pass** (narrow_example_added closes the wording gap) |
| Joint vs conditional denominator | 15.3 | `POPULATION_CONTRACT`/metric card already force separate numerator/denominator population fields. | No text change; new worked example. | **pass** (already covered; smoke_qa_added) |
| Model residual + producer/reviewer claims | 15.4 | Same gap as row 2, plus `generalization_evidence` gap for selection-based generalization. | New rows 2 and 4 in `GOVERNANCE_AND_ANTI_PATTERNS.md`. | **pass** (narrow_example_added) |
| Confounded ranking | 15.5 | No explicit overlap/common-support prerequisite for reviewer normalization. | New row 6. | **pass** (narrow_example_added) |
| Predictive statement | 15.6 | `causal_status: association_only` exists but no predictive-performance-specific baseline/split/leakage requirement. | New row 7. | **pass** (narrow_example_added) |
| Undefined metric, useful partial answer | 15.7 | `METRIC_DEFINITION_CARD.status: provisional` path already permits a scoped partial answer with limitation. | No text change; new worked example. | **pass** (already covered; smoke_qa_added) |
| CFO transfer | 15.8 | `RECURRENCE_CLASSIFICATION` + Accountability boundary rule (`VARIANCE_DIAGNOSTIC_CONTRACT.md` §5, `effect_type` §16.5) already forbid inferring process failure/fraud from a financial pattern alone. | No text change; new worked example reusing #449 scenario C's pattern. | **pass** (already covered; smoke_qa_added) |
| Positive control / routing | 15.9 | `ROUTING_AND_HANDOFF.md` + §9 runtime collapse already route a routine result directly and a strategic decision to `[Thinking]`. | No text change; new worked example. | **pass** (already covered; smoke_qa_added) |
| Delivery / status honesty | §7 (this document) + §9 below | N/A | Repository source/contract checks, paper-traced case review, and external sync are reported as three separate states, not blended (see §9). | **pass** |

No scenario required manufacturing a failing baseline to justify a new
gate. Five of nine WineMag/CFO/positive-control scenarios (15.1, 15.3, 15.7,
15.8, 15.9) show the existing contract already passes the case
("already_covered"); four (15.2, 15.4, 15.5, 15.6) needed the narrow text
additions in §2/§3 above to make the existing rule's application to this
exact wording pattern unambiguous, rather than relying on an unguided
analogy.

## 9. Regressions and false-block check

None identified. `ANALYTICAL_TECHNIQUES.md` is byte-identical to
`origin/main` (§4/§10 confirm no diff). `ANALYSIS_CONTINUATION_GATE` (§15.3)
was not touched and remains deferred, not activated. No existing method,
intent, Analytical Judge check, claim-ladder rule, `POPULATION_CONTRACT`,
`RECONCILIATION_CONTRACT`, `RECOMMENDATION_EVIDENCE`, enum, or gate was
weakened, replaced, or duplicated as a competing source of truth. No
keyword blacklist was added. Scenario 15.7 and 15.9 specifically confirm
that the additions do not block routine exploration or force a full
statistical model before any finding is reported.

## 10. Delivery and validation states (kept separate)

1. **Source/contract and generated-artifact validation**: `pytest tests/ -q`,
   `check_project_instructions_length.py`, `check_repo_public_safety.py`,
   `check_codex_goal_mode_defaults.py`, `check_manifest_paths.py`,
   `check_knowledge_bundles.py`, `check_index_coverage.py`,
   `build_knowledge_bundles.py --check`, `audit_bundle_provenance.py
   --check` — real results recorded in the PR description / handoff, not
   fabricated here.
2. **Case-based semantic review**: this document (§2–§8) — paper-trace /
   static review only, explicitly not a live behavioral run. No live LLM
   was invoked; no wine model was built; no real Top-50 was calculated.
3. **Authorized external Project-sync verification and post-sync smoke**:
   **NOT RUN**. Repository regeneration is not evidence of ChatGPT Project
   upload or behavior change. Next step: an owner-authorized upload of the
   regenerated `ANALYTICS_01_CORE_WORKFLOW.md` and
   `ANALYTICS_05_QA_GOVERNANCE_ROUTING.md` bundles plus a live smoke-QA pass
   against `SMOKE_QA_FOR_ANALYTICS.md` case 15, when the owner chooses to
   perform it.

## 11. Rollback

Revert `GOVERNANCE_AND_ANTI_PATTERNS.md`'s new section, `SMOKE_QA_FOR_ANALYTICS.md`'s
case 15, and the `package_manifest.json` additions; regenerate
`Knowledge_Bundles/ANALYTICS_01_CORE_WORKFLOW.md` and
`ANALYTICS_05_QA_GOVERNANCE_ROUTING.md` via
`scripts/build_knowledge_bundles.py --write` and
`docs/knowledge_bundle_provenance_audit.{json,md}` via
`scripts/audit_bundle_provenance.py --write`. No method-registry migration,
enum change, or `ANALYSIS_CONTINUATION_GATE` status change is involved in
rollback — none of those were touched.

## 12. Residual limitations

- The WineMag dataset, execution trace, code, and exact externally loaded
  project context that produced the original supplied answer were not
  available to this review; attribution of the original wording to a
  specific instruction gap, an unclear example, an existing-but-unapplied
  rule, source/bundle delivery drift, or unavailable execution evidence
  remains **uncertain**. This review closes a wording-ambiguity gap it can
  verify from the contract text itself, not a confirmed root cause of the
  original incident.
- No live model was run for any of the nine scenarios; all results are
  paper-traced against contract text, per this issue's explicit instruction
  that a paper walkthrough is not a live model run.
- `check_manifest_paths.py`, `check_knowledge_bundles.py`, and other
  existing validation scripts do not enforce `package_manifest.json`
  completeness (confirmed by grep — no script references this file). This
  review repairs the file's content but does not add a new enforcement
  script, per the issue's explicit prohibition on new dashboards/services/
  checks beyond the bounded scope; this residual gap is documented, not
  silently left unmentioned.

## 13. Explicit statement

This review adds **no new finding-status taxonomy, method ID, intent,
registry, Judge, execution mode, permanent evaluation corpus, dashboard,
service, agent, or repo-wide routing redesign**. `confidence: high / medium
/ low` and every other existing Analytics enum are unchanged.
`ANALYSIS_CONTINUATION_GATE` (§15.3) remains deferred, not activated, and was
not revisited. The bounded pilots from #445 and #449 remain bounded-pilot,
owner-review-pending; this issue does not promote them.

## 14. Final verdict

```text
R1: 5/6 patterns needed a narrow example addition; 1/6 already covered.
R2: all 5 bullets placed as narrow examples in the existing failure-mode table.
R3: already covered (mechanism); regression example added.
R4: already covered (minimum-sufficient-method-set philosophy).
R5: already covered, no change.
R6: genuine packaging bug found and fixed (package_manifest.json only;
    knowledge_bundle_manifest.json was already correct).
Regressions: none identified.
New taxonomy/gate/framework added: none.
```
