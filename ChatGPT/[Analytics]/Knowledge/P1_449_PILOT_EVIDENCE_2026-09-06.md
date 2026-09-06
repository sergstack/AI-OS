# [Analytics] P1-B Pilot Evidence — issue #449

Status: **bounded pilot evidence only**. `owner review required` before any
promotion, merge, deployment, or Project sync. This document records a
structured written (paper-trace) evaluation: reasoning through each of the
five scenarios named in issue #449 against the OLD (P0 + issue #445 P1)
contract text and the NEW (P1-B, issue #449) contract text, and recording
what each would output/allow per the field lists in issue #449. It is
**not** a live LLM execution run; no live model was invoked as part of this
pilot. This limitation is stated explicitly wherever it affects a
recommendation (see Residual limitations), following the same style and
honesty standard as `P1_PILOT_EVIDENCE_2026-09-06.md` (issue #445).

## 1. Scope and changed files

All **semantic/content** changes are inside `ChatGPT/[Analytics]/**`. In
addition, `docs/knowledge_bundle_provenance_audit.json` and
`docs/knowledge_bundle_provenance_audit.md` were mechanically regenerated
via `scripts/audit_bundle_provenance.py --write` to keep the repo-wide
provenance snapshot in sync with the regenerated `[Analytics]` bundles — no
manual edits, no content decisions, and no other file under `docs/**` was
touched. Unlike issue #445, this issue's scope does not forbid `docs/**`, so
this regeneration is done in-PR rather than left as a `BLOCKED` item. No
file outside `ChatGPT/[Analytics]/**` and those two provenance files was
modified.

Changed:

- `ChatGPT/[Analytics]/Knowledge/ANALYTICAL_REASONING_STANDARD.md` — new §16
  ("P1-B activated controls, bounded pilot, issue #449") with six
  subsections (§16.1–§16.6), and a new "P1-B pilot status (issue #449)"
  section. `ANALYSIS_CONTINUATION_GATE` (§15.3) is untouched and remains
  deferred, not activated.
- `ChatGPT/[Analytics]/Knowledge/VARIANCE_DIAGNOSTIC_CONTRACT.md` — added
  `effect_type` classification under Accountability boundary (§5), and the
  invariant `a financial pattern alone cannot establish a process failure`
  in the stop/publication gate list (§8).
- `ChatGPT/[Analytics]/Knowledge/QA_CHECKLIST.md` — added "Recommendation
  evidence, stability, and out-of-sample validation (P1-B, issue #449,
  bounded pilot)" section with eight checklist items.
- `ChatGPT/[Analytics]/Knowledge/ACCEPTANCE_CRITERIA.md` — added acceptance
  item 16 (§16 controls) and two new `blocked` triggers.
- `ChatGPT/[Analytics]/Knowledge/MEMO_PIPELINE.md` — added "Management
  implication section (P1-B, issue #449, bounded pilot)" describing how the
  memo reads `recommendation_status` and `what_would_change_the_view`; two
  new Memo QA items.
- `ChatGPT/[Analytics]/Knowledge/MEMO_RUBRIC.md` — added a "Recommendation
  strength" rubric row and a golden-memo criterion.
- `ChatGPT/[Analytics]/Templates/CLAIM_EVIDENCE_REGISTRY_TEMPLATE.md` —
  added a "`RECOMMENDATION` row evidence" section (no new column; links to
  `RECOMMENDATION_EVIDENCE` via `claim_id`).
- `ChatGPT/[Analytics]/Knowledge/SMOKE_QA_FOR_ANALYTICS.md` — added smoke QA
  case 14 with the five scenarios (A–E) from issue #449.
- `ChatGPT/[Analytics]/Knowledge/CHANGELOG.md` — new dated entry.
- `ChatGPT/[Analytics]/Knowledge/ANALYTICS_PROJECT_FILES_INDEX.md` — index
  row for this file.
- `ChatGPT/[Analytics]/Knowledge/P1_449_PILOT_EVIDENCE_2026-09-06.md` — this
  file (new).
- `docs/knowledge_bundle_provenance_audit.json` and
  `docs/knowledge_bundle_provenance_audit.md` — mechanically regenerated via
  `scripts/audit_bundle_provenance.py --write` (byte-count/fingerprint sync
  only, same pattern as PR #447's own provenance-sync commits).

Not changed: `ChatGPT/[Analytics]/Knowledge/ANALYTICAL_TECHNIQUES.md` (see
§2, zero diff), `Codex_Tasks/**`, active analytical intents, and
`ANALYSIS_CONTINUATION_GATE` (§15.3, left exactly as issue #445/PR #447
left it — deferred, not activated). Bundle *outputs* are regenerated
deterministically via `scripts/build_knowledge_bundles.py --write`, which
only rewrites files already declared as generated outputs in the existing
`knowledge_bundle_manifest.json`; that manifest itself was not edited.

## 2. P0 + issue #445 baseline description

`business question → task profile / intent → deterministic-first method set
→ prerequisite gate → execution → preliminary evidence check → explanation
challenge (material) → claim calibration / FINAL_EVIDENCE_SUFFICIENCY →
Analytical Judge (§8, 7 checks incl. check 7 decision proportionality) →
memo/report → QA / acceptance`, plus the issue #445 bounded-pilot additions
(`POPULATION_CONTRACT` §15.1, `RECONCILIATION_CONTRACT` §15.2, both
activated; `ANALYSIS_CONTINUATION_GATE` §15.3, deferred). Relevant existing
controls for this pilot:

- §6 explanation challenge (material/decision-critical): `COMPETING_EXPLANATIONS[]`,
  `CONTRADICTING_EVIDENCE`, `DISCRIMINATING_EVIDENCE`, `FALSIFICATION_TEST`,
  claim ladder (`driver != root cause`).
- §7 `FINAL_EVIDENCE_SUFFICIENCY`, `claim_support`, `causal_status`.
- §8 Analytical Judge check 7: "does any recommendation, risk statement, or
  management implication exceed the verified evidence?" — a general
  proportionality check with no explicit intervention-testing requirement.
- `VARIANCE_DIAGNOSTIC_CONTRACT.md` §5: `RECURRENCE_CLASSIFICATION`,
  Accountability boundary ("do not infer ... control failure solely from
  amount, ownership, zero-plan status, or driver status").
- `CLAIM_EVIDENCE_REGISTRY_TEMPLATE.md`: `generalization_scope` /
  `generalization_evidence` (one-line binary-style fields, not an
  entity-level stability record).
- `ANALYTICAL_TECHNIQUES.md`: `forecast_to_period_end`, `sensitivity_analysis`,
  `robustness_to_baseline` (test a single method's own conclusion; no
  structural requirement to compare a candidate forecasting/planning method
  against the current one out-of-sample before recommending a switch).
- `ACCEPTANCE_CRITERIA.md` / `QA_CHECKLIST.md`: prose acceptance criterion
  "what would materially change the conclusion is stated when relevant" —
  present in prose, not as a named compact field.

## 3. P1-B candidate description

Same architecture, extended by six §16 elements (`ANALYTICAL_REASONING_STANDARD.md`):

- §16.1 strengthened material Explanation Challenge — requires
  `DISCRIMINATING_TEST_STATUS: executed / blocked / unavailable` for a
  material explanatory/intervention-oriented statement; contribution +
  recurrence alone is insufficient.
- §16.2 `RECOMMENDATION_EVIDENCE` (CONTROL) — `diagnostic evidence !=
  intervention evidence`; untested intervention caps `recommendation_status
  <= pilot_candidate`.
- §16.3 stability/persistence check — `stability_check` distinguishes stable
  from rotating concentration before a targeted-redesign recommendation.
- §16.4 out-of-sample validation — `FORECAST_METHOD_COMPARISON` required
  before a strong forecasting/planning-method-change recommendation.
- §16.5 `effect_type` classification — process-control claims require
  process evidence, not a financial pattern alone.
- §16.6 `what_would_change_the_view` — compact named field for material
  executive output with a material evidence gap.

All six carry an explicit activation-trigger clause (material case with the
relevant pattern/proposal) and collapse to the existing §9 compact path
otherwise. None adds a `METHOD_ID`, a second Judge, or a second QA
framework.

## 4. 22-method registry check

```text
$ diff <(git show origin/main:"ChatGPT/[Analytics]/Knowledge/ANALYTICAL_TECHNIQUES.md") \
       "ChatGPT/[Analytics]/Knowledge/ANALYTICAL_TECHNIQUES.md"
(zero output — files identical)
```

- P0 method count before: 22. After: 22 (file untouched; verified by diff;
  see the PR validation section for the literal command output).
- No new `METHOD_ID` (`RECOMMENDATION_EVIDENCE`, `stability_check`,
  `FORECAST_METHOD_COMPARISON`, `effect_type`, `what_would_change_the_view`,
  `DISCRIMINATING_TEST_STATUS` are CONTROL/field-level additions, not
  methods; none appears in the registry table).
- No new analytical intent (`Active intent × method mapping` table
  unchanged).
- No `backtest` `METHOD_ID` was created; §16.4 reuses `forecast_to_period_end`,
  `sensitivity_analysis`, `robustness_to_baseline`, and existing backtesting
  logic (comparing forecast/plan output to realized out-of-sample values).

## 5. 5-scenario result matrix (OLD vs. NEW, per issue #449)

All five scenarios are `known_regression_cases` in the sense of directly
targeting the six §16 elements (development-designed adversarial cases); no
separate held-out/shifted-domain set was additionally constructed for this
pilot beyond scenario wording variation — see Residual limitations.

| # | Scenario | OLD (P0 + #445, paper trace) | NEW (P1-B, paper trace) | Incremental catch? |
|---|---|---|---|---|
| A | Diagnosis proven (category = 60% gross planning error), intervention untested (recommend driver-based planning, no out-of-sample comparison) | §6 explanation challenge could already require a discriminating test for causal claims, but nothing explicitly separates "diagnosis proven" from "proposed intervention validated"; Judge check 7 is a general proportionality prompt with no explicit intervention-testing rule. A confident diagnosis could plausibly be followed directly by "should switch to driver-based planning" without anything structurally blocking it — this is exactly the gap the issue names. | `RECOMMENDATION_EVIDENCE` (§16.2): `problem_evidence: supported`, `mechanism_evidence` may be supported, but `test_or_backtest_performed: no` forces `recommendation_status: pilot_candidate`. §16.4 additionally requires `FORECAST_METHOD_COMPARISON` before a strong "switch the planning model" claim; absent, same cap applies. | **Real.** OLD had no structural rule forcing the diagnosis-vs-intervention separation; §16.2+§16.4 together force it explicitly. This is the core gap named by the issue. |
| B | Stable aggregate Top-10 (~60% of error over 10 months), rotating individual members month to month | `generalization_scope` / `generalization_evidence` and `RECURRENCE_CLASSIFICATION` require evidence before calling a pattern "systemic"/"persistent", but neither forces an entity-level same-membership check; an aggregate "Top-10 = 60%" figure could plausibly be read as naming a stable population worth a targeted redesign without checking whether membership rotates. | `stability_check` (§16.3) makes `same_entities` / `same_ranking` / `persistence_across_periods` explicit, mandatory fields before a targeted-redesign claim; rotating membership routes the claim to a process/system-level observation instead of a named-entity intervention. | **Real.** No prior control specifically forced the entity-level rotation check; the aggregate-level generalization fields do not by themselves catch member-level rotation. |
| C | Recurring `fact_without_plan` in 8 of 10 months; draft wants to call it mapping/owner/budget-process failure | `RECURRENCE_CLASSIFICATION` (existing) already supports "recurring exception" from 8/10 months of historical pattern. The existing Accountability boundary rule ("do not infer ... control failure solely from amount, ownership, zero-plan status, or driver status") already substantially forbids inferring a process/control failure from the recurrence pattern alone — this is not a new prevention. | `effect_type: process_control` (§16.5) names the same rule as an explicit classification field and requires process evidence (owner/mapping confirmation) before `process_control` is assigned; "recurring exception" itself remains supported without change. | **Modest, formalization-leaning.** The Accountability boundary rule already covers most of this case; §16.5's incremental value is naming the dimension explicitly (`effect_type`) and adding "process_control" as one of a fixed classification set, not preventing a new failure mode the old prose rule missed. |
| D | Candidate planning model wins in-sample only; loses on held-out months on monetary error while improving count accuracy | No existing control requires an out-of-sample, monetary-error-inclusive comparison between a candidate and the current forecasting/planning method before recommending a switch; `robustness_to_baseline` / `sensitivity_analysis` test a single method's own conclusion, not a candidate-vs-current comparison. A recommendation could plausibly cite the in-sample / count-accuracy improvement alone. | `FORECAST_METHOD_COMPARISON` (§16.4) requires the out-of-sample period, comparable population/scope, same metric definitions, a monetary-error metric, and a frequency/corridor-accuracy metric; a candidate that worsens the monetary-error metric out-of-sample cannot support a strong replace-the-model recommendation — `recommendation_status` stays `pilot_candidate` or is rejected. | **Real.** This is a genuinely new structural requirement; no prior control named "compare current vs candidate forecasting method out-of-sample with a monetary-error metric" as a gate before a model-change recommendation. |
| E | Quick regression: simple reconciled Plan/Fact, low uncertainty, no material trigger | Compact path per §9: `QUESTION → INTENT → CORE/TRIGGERED METHOD → DETERMINISTIC RESULT → COMPACT QA → ANSWER`. No `RECOMMENDATION_EVIDENCE`, `stability_check`, or `FORECAST_METHOD_COMPARISON` records (none existed before #449). | All six §16 elements carry an explicit activation-trigger clause (material case + a specific pattern/proposal); none is instantiated for this routine case. Output stays on the existing compact path. | **No regression** (this is the point of the test): the six new elements do not leak into the routine/quick path. |

## 6. Known-case result, reported honestly (no held-out/shifted-domain lane populated in this pilot)

- 3 of 5 scenarios (A, B, D) show a **real** incremental catch: each targets
  a gap where the OLD contract had no structural rule forcing the specific
  separation the issue asks for (diagnosis-vs-intervention; aggregate-vs-
  entity-level stability; in-sample-vs-out-of-sample forecast comparison).
- 1 of 5 (C) shows a **modest, formalization-leaning** catch: the OLD
  Accountability boundary rule already substantially covered this case;
  §16.5 mainly names the dimension explicitly rather than closing a gap the
  old rule missed.
- 1 of 5 (E) confirms **no regression**: the routine/quick compact path is
  unaffected by any of the six additions.
- §16.6 (`what_would_change_the_view`) is not separately scenario-tested
  above because it restates an existing prose acceptance criterion
  (`ACCEPTANCE_CRITERIA.md`, `QA_CHECKLIST.md`) as a compact named field; its
  incremental value is naming/consistency, not new blocking behavior — see
  §7.
- §16.1 (strengthened Explanation Challenge) is exercised implicitly in
  scenario A (the diagnosis itself is `supported`, i.e. the discriminating
  test requirement for the *diagnosis* is already satisfied in that
  scenario) and is not separately scenario-tested for a case where the
  *diagnosis itself* lacks a discriminating test; see Residual limitations.

**No held-out or shifted-domain scenario set beyond A–E was constructed for
this pilot.** Issue #449 specified exactly five scenarios and asked that all
five be implemented as smoke QA / pilot-evidence scenarios; this pilot does
that, but does not additionally construct a shifted-domain variant the way
`P1_PILOT_EVIDENCE_2026-09-06.md` did for issue #445. This is stated
honestly as a residual limitation (§12) rather than claimed as covered.

## 7. Incremental catches (explicit)

- `RECOMMENDATION_EVIDENCE` (§16.2) + `FORECAST_METHOD_COMPARISON` (§16.4):
  together close the core gap named by the issue — a correct diagnosis
  proceeding directly to an unvalidated management/method-change
  recommendation (scenarios A, D). No prior named control forced this
  separation.
- `stability_check` (§16.3): closes an entity-level rotation gap not caught
  by the existing aggregate-level `generalization_scope` /
  `generalization_evidence` fields (scenario B).
- `effect_type` / process-control boundary (§16.5): modest — mostly
  formalizes the existing Accountability boundary rule as an explicit
  classification field (scenario C); does not change the final claim-
  strength outcome versus the OLD rule in the traced case.
- `what_would_change_the_view` (§16.6): not itself a detection control; its
  value is consistency/naming of an already-required acceptance criterion,
  not a new blocking behavior.
- Strengthened Explanation Challenge (§16.1): closes a phrase-recognition
  gap (material explanatory/intervention wording not previously
  pattern-matched to a required discriminating-test-status field), but this
  pilot's traced scenarios do not include a case where a *diagnosis itself*
  (not just the intervention) lacks a discriminating test — see Residual
  limitations.

## 8. Regressions

None identified. `ANALYTICAL_TECHNIQUES.md` is byte-identical to
`origin/main` (§4). Scenario E confirms the compact/routine path is
unaffected. No existing method, intent, Analytical Judge check, claim-ladder
rule, `POPULATION_CONTRACT`, `RECONCILIATION_CONTRACT`, or
`ANALYSIS_CONTINUATION_GATE` status was weakened, replaced, or duplicated as
a competing source of truth. `ANALYSIS_CONTINUATION_GATE` (§15.3) was not
touched and remains deferred, not activated.

## 9. Complexity / false-block observations

- No false blocks identified in the traced scenarios: all six §16 elements
  are written as activation-gated (material case + specific pattern/proposal
  required) and explicitly instructed not to instantiate for routine/quick
  cases (scenario E).
- As with the issue #445 pilot, this paper trace cannot verify in a live run
  that an executor actually respects the collapse instruction rather than
  instantiating the full records defensively "just in case" — flagged as a
  residual limitation, not asserted as safe.
- §16.2's `recommendation_status <= pilot_candidate` cap and §16.4's
  out-of-sample requirement both create a real, intended "block" on strong
  wording in scenarios A and D; this is the designed behavior, not a false
  block, per the issue's expected outcomes.

## 10. Per-element recommendation

- §16.1 (strengthened Explanation Challenge): **ADOPT_FOR_OWNER_REVIEW**,
  modest confidence. Closes a phrase-recognition loophole (material
  explanatory/intervention wording not previously required to carry a
  recorded discriminating-test status); this pilot's scenarios do not
  directly exercise a case where the *diagnosis itself* lacks a
  discriminating test, so the catch is reasoned from the contract-text gap,
  not from a scenario-level failure observed in this pilot.
- §16.2 (`RECOMMENDATION_EVIDENCE`): **ADOPT_FOR_OWNER_REVIEW**, high
  confidence. Real incremental catch in scenario A; directly implements the
  issue's core `diagnostic evidence != intervention evidence` requirement.
- §16.3 (stability/persistence check): **ADOPT_FOR_OWNER_REVIEW**, high
  confidence. Real incremental catch in scenario B; closes an entity-level
  gap not covered by existing generalization fields.
- §16.4 (out-of-sample forecast/planning validation): **ADOPT_FOR_OWNER_REVIEW**,
  high confidence. Real incremental catch in scenario D; no prior control
  named this comparison as a gate, and no new `METHOD_ID`/`backtest` was
  created.
- §16.5 (`effect_type` / process-control boundary): **ADOPT_FOR_OWNER_REVIEW**,
  lower confidence than §16.2–§16.4. The paper-trace incremental catch in
  scenario C is modest — the existing Accountability boundary rule already
  substantially covers this case. Owner review should weigh this as a
  formalization/naming improvement more than a new prevention.
- §16.6 (`what_would_change_the_view`): **ADOPT_FOR_OWNER_REVIEW**, weak/
  naming-only confidence. Restates an existing `ACCEPTANCE_CRITERIA.md` /
  `QA_CHECKLIST.md` prose criterion as a compact named field; no new
  blocking behavior identified versus the prior prose rule.

No element is recommended `DEFER` or `REJECT`, and none showed a false block
or a regression — but evidence strength is not uniform, and only three of
the six elements demonstrate an actual incremental catch in the traced
scenarios:

- §16.2, §16.3, §16.4 — **real incremental catches** (scenarios A, B, D
  respectively); the strongest adopts.
- §16.5 — **modest**: mostly formalizes the existing Accountability boundary
  rule (scenario C exercises it, but the rule already substantially covered
  the case beforehand).
- §16.6 — **consistency/naming value, not a detection catch**: no scenario
  shows it catching anything §16.2–§16.5/`FINAL_EVIDENCE_SUFFICIENCY`/
  `CONTRADICTING_EVIDENCE` would have missed on their own.
- §16.1 — **partially scenario-tested**: reasoned from a genuine contract-text
  gap (material explanatory wording not previously tied to a recorded
  discriminating-test status), but no scenario in this pilot isolates the
  case where the diagnosis itself lacks discriminating evidence, independent
  of §16.2–§16.4.

`ADOPT_FOR_OWNER_REVIEW` across all six therefore means "worth the owner's
review, nothing found harmful," not "uniformly demonstrated" — §16.2/§16.3/
§16.4 are evidence-backed adopts; §16.1/§16.5/§16.6 are adopts on
formalization/consistency grounds pending further live evidence.

## 11. Rollback status

Documented and structurally trivial for all six (see
`ANALYTICAL_REASONING_STANDARD.md` "P1-B pilot status" and `QA_CHECKLIST.md`):

- §16.1 → the existing §6 explanation challenge without the pattern-matched
  discriminating-test-status requirement.
- §16.2 → existing `FINAL_EVIDENCE_SUFFICIENCY`, Analytical Judge check 7,
  and `CLAIM_EVIDENCE_REGISTRY_TEMPLATE.md`, without the
  `RECOMMENDATION_EVIDENCE` wrapper.
- §16.3 → existing `generalization_scope` / `generalization_evidence` and
  `RECURRENCE_CLASSIFICATION`, without the `stability_check` wrapper.
- §16.4 → existing `forecast_to_period_end` / `sensitivity_analysis` /
  `robustness_to_baseline`, without the `FORECAST_METHOD_COMPARISON`
  requirement.
- §16.5 → the existing Accountability boundary rule alone, without the
  `effect_type` classification surface.
- §16.6 → the existing `ACCEPTANCE_CRITERIA.md` / `QA_CHECKLIST.md` prose
  criterion, without the compact named field.

No method-registry migration is required for any rollback.

## 12. Residual limitations

- This is a documentation/design pilot: a structured written walkthrough,
  not a live LLM execution comparison. All "OLD vs. NEW" outcomes above are
  reasoned from the contract text, not observed from an actual run.
- Only the five scenarios named in issue #449 (A–E) were traced; no
  additional held-out or shifted-domain variant set was constructed the way
  `P1_PILOT_EVIDENCE_2026-09-06.md` did for issue #445's scenarios 8–9. A
  future pilot revisiting these six elements should add a held-out/
  shifted-domain lane before any promotion decision that relies on transfer
  evidence.
- §16.1's incremental catch is reasoned from the contract-text gap (a
  phrase-recognition loophole), not from a traced scenario where the
  diagnosis itself failed the discriminating-test requirement; this is
  flagged rather than claimed as a demonstrated catch.
- §16.5 and §16.6 are honestly reported as the weakest of the six elements
  (formalization/naming value more than new prevention); this is stated
  explicitly rather than folded into a uniform "all six equally strong"
  claim.
- `boundary_cases` (e.g. exact stability-tolerance thresholds, exactly 50%
  rotation) are not separately populated with dedicated scenarios in this
  pilot.

## 13. Explicit statement

**Owner review is required before any promotion, merge, deployment, or
Project sync of any of the six elements. Nothing in this pilot authorizes
production adoption.**

## 14. Final gate verdict

```text
PASS_FOR_OWNER_REVIEW
```

Rationale: all bounded-pilot acceptance criteria in issue #449 are met —
semantic scope stayed inside `ChatGPT/[Analytics]/**` (plus mechanical
provenance-artifact regeneration under `docs/**`, see §1); all six elements evaluated
against all five named scenarios; 22-method registry unchanged (verified by
diff); no new `METHOD_ID`/analytical intent; `ANALYSIS_CONTINUATION_GATE`
left deferred/not activated; no second Judge or second QA framework
introduced; each element has an honest per-element recommendation with
differentiated confidence (three high-confidence adopts, one modest, two
weak/naming-only — not a uniform "all equally strong" claim); rollback
documented; residual limitations stated, including the absence of a
held-out/shifted-domain lane; `owner review required` is the terminal state.
