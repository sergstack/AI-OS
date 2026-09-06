# [Analytics] P1 Pilot Evidence — issue #445

Status: **bounded pilot evidence only**. `owner review required` before any
promotion, merge, deployment, or Project sync. This document records a
structured written (paper-trace) evaluation: reasoning through each scenario
against the OLD (P0-only) contract text and the NEW (P1-activated) contract
text and recording what each would output/allow per the field lists in issue
#445. It is **not** a live LLM execution run; no live model was invoked as
part of this pilot. That limitation is stated explicitly wherever it affects
a recommendation, per this document's own held-out lane (`HELD_OUT_TRANSFER_EVAL`
requires eventual live comparative evidence before promotion — see
Residual limitations).

## 1. Scope and changed files

All changes are inside `ChatGPT/[Analytics]/**`. No file outside this path
was modified.

Changed:

- `ChatGPT/[Analytics]/Knowledge/ANALYTICAL_REASONING_STANDARD.md` — §15
  rewritten from "P1 extension points (design only)" to "P1 activated
  controls (bounded pilot)"; §15.1/§15.2/§15.3 add the three full contracts;
  "P1 pilot status" section replaces "P1 and P2 status".
- `ChatGPT/[Analytics]/Templates/METRIC_DEFINITION_CARD_TEMPLATE.md` — P1
  extension-point note flipped to "activated" with a pointer to §15.1 (fields
  not duplicated, to avoid drift).
- `ChatGPT/[Analytics]/Knowledge/DATA_CONTRACTS.md` — added a short
  cross-reference from `UNMATCHED` `VALUE_STATE` to the activated
  `RECONCILIATION_CONTRACT` (§15.2); no field duplication.
- `ChatGPT/[Analytics]/Knowledge/QA_CHECKLIST.md` — added "Held-out transfer
  eval (P1 QA/EVAL, issue #445)" section defining `HELD_OUT_TRANSFER_EVAL`
  and its six required lanes.
- `ChatGPT/[Analytics]/Knowledge/SMOKE_QA_FOR_ANALYTICS.md` — added smoke QA
  case 13 with the held-out population-semantics-shift, held-out
  reconciliation-semantics-shift, and old-P0-compact-regression questions.
- `ChatGPT/[Analytics]/Knowledge/CHANGELOG.md` — new dated entry.
- `ChatGPT/[Analytics]/Knowledge/P1_PILOT_EVIDENCE_2026-09-06.md` — this file
  (new).

Not changed: `ChatGPT/[Analytics]/Knowledge/ANALYTICAL_TECHNIQUES.md` (see
§2, zero diff), `Codex_Tasks/**`, `Knowledge_Bundles/**` source content
(bundle *outputs* are regenerated deterministically via
`scripts/build_knowledge_bundles.py --write`, which only rewrites files
already declared as generated outputs in the existing
`knowledge_bundle_manifest.json` — that manifest itself was not edited).

## 2. P0 baseline description

`Question/Scope → Inputs → Data Contract → RAW → stage_main_full →
mart_main_full → mart_main_tz/compact → deterministic calculation →
findings → evidence challenge/claim calibration when required → Analytical
Judge → memo/report → QA → acceptance`, with:

- §5 population/denominator checks (`population_constant_or_explained?` /
  `denominator_constant_or_explained?` / `scope_change_quantified?`), binary,
  capping `claim_support <= PARTIALLY_SUPPORTED` when unresolved.
- Reconciliation via separate existing methods: `reconciliation`,
  `unmatched_elements_analysis`, `factor_reconciliation`,
  `unexplained_residual`, plus the existing anti-pattern note ("aggregate
  reconciliation used instead of entity-level unmatched analysis" —
  `GOVERNANCE_AND_ANTI_PATTERNS.md`), all trigger-gated (§3 "Trigger contracts
  for non-CORE methods" — `unmatched_elements_analysis` is TRIGGERED, not
  CORE, for `validate_data`/`diagnose_variance`).
- §10 stop/escalation rules (prose rules, not a recorded per-case decision
  object).
- §8 Analytical Judge, §13 Headline Claim Gate, §12 `VALUE_STATE`, §9 runtime
  collapse — unchanged, remain authoritative.

## 3. P1 candidate description

Same architecture, extended by:

- `POPULATION_CONTRACT` (§15.1, CONTROL/CONTRACT) — structured
  population/denominator comparability record with `comparability_status`
  (4-state) and mandatory `scope_change_amount`/`scope_change_pct` fields,
  activated for material/decision-critical population-dependent metrics.
- `RECONCILIATION_CONTRACT` (§15.2, CONTROL/CONTRACT) — structured record
  separating `amount_reconciliation` / `row_count_reconciliation` /
  `matched_population` / `identity_mapping_status` / `classification_coverage`
  / `unexplained_residual`, wrapping the same existing methods.
- `ANALYSIS_CONTINUATION_GATE` (§15.3, ROUTING/WORKFLOW CONTROL) — structured
  CONTINUE/STOP/BLOCK/HANDOFF decision record restating §10.
- `HELD_OUT_TRANSFER_EVAL` (`QA_CHECKLIST.md`, QA/EVAL) — six-lane transfer
  evaluation scaffold, not a method.

All four collapse to the existing P0 compact/routine path when there is no
material trigger (§9 unchanged).

## 4. 22-method registry check

```text
$ diff <(git show origin/main:"ChatGPT/[Analytics]/Knowledge/ANALYTICAL_TECHNIQUES.md") \
       "ChatGPT/[Analytics]/Knowledge/ANALYTICAL_TECHNIQUES.md"
(zero output — files identical)
```

- P0 method count before: 22. After: 22 (file untouched; verified by diff,
  see §"Validation" in the PR for the literal command output).
- No new `METHOD_ID`. No new analytical intent (`Active intent × method
  mapping` table unchanged).
- `POPULATION_CONTRACT` / `RECONCILIATION_CONTRACT` classified
  CONTROL/CONTRACT; `ANALYSIS_CONTINUATION_GATE` classified ROUTING/WORKFLOW
  CONTROL; `HELD_OUT_TRANSFER_EVAL` classified QA/EVAL — none is a method,
  none appears in the registry table.

## 5. 10-scenario result matrix (P0 baseline vs. P1 candidate)

Lane classification per `QA_CHECKLIST.md`: scenarios 1–7 are
`known_regression_cases` (development-designed adversarial cases directly
targeting Gaps 1–3); scenario 7 also exercises `contradictory_evidence_cases`;
scenarios 8–9 are `held_out_cases` / `shifted_domain_cases` (explicitly
different domain/wording per issue #445); scenario 10 is
`old_p0_regression_cases`. `boundary_cases` (e.g. exact-tolerance,
zero-denominator) are not separately populated in this pilot — see Residual
limitations.

| # | Scenario | P0 baseline (paper trace) | P1 candidate (paper trace) | Incremental catch? |
|---|---|---|---|---|
| 1 | Population shift, apparent efficiency gain (loss-making entities leave population) | §5: `population_constant_or_explained? = no`; if `scope_change_quantified?` unmet → `claim_support <= PARTIALLY_SUPPORTED`. Correct outcome, but the binary field can be marked `no`/`yes` without ever recording a number. | `POPULATION_CONTRACT`: `population_changed_vs_baseline: yes`, `comparability_status: unresolved` until `scope_change_amount`/`scope_change_pct` are actually filled in; `interpretation_allowed != yes` enforced by the same cap. | **Weak.** Same final gate outcome as P0. The only difference is that the quantification fields are mandatory to fill in (or explicitly marked unresolved), closing a "assert yes without evidence" loophole. Not a new detection rule. |
| 2 | Mix shift, unchanged component performance | `mix_analysis` (existing CORE/TRIGGERED method for `diagnose_variance`) already isolates the composition effect; §5 population/denominator checks do not fire because the population itself is unchanged. Correct: max claim = quantified mix-driven aggregate change. | `POPULATION_CONTRACT` does not apply (population/denominator unchanged); no new field is instantiated. Same outcome via `mix_analysis`. | **None.** P0 and P1 identical; `POPULATION_CONTRACT` is out of scope for a pure mix effect by design. |
| 3 | Amount reconciliation PASS, population FAIL (offsetting unmatched rows) | Existing anti-pattern already named ("aggregate reconciliation used instead of entity-level unmatched analysis" — `GOVERNANCE_AND_ANTI_PATTERNS.md`), but `unmatched_elements_analysis` is TRIGGERED-not-CORE: its trigger rule ("entity-level mismatch may explain the issue") may not fire when the amount total already reconciles cleanly and nothing looks wrong. Realistic failure mode: P0 declares "reconciled" from the amount pass alone. | `RECONCILIATION_CONTRACT` makes `matched_population` / `only_in_left` / `only_in_right` **mandatory fields to declare** (even as "not tested") whenever a reconciliation-based claim is published, independent of whether a mismatch was already suspected. `overall_interpretation` cannot claim population integrity while `matched_population != pass`. | **Real.** Forces the population-matching question to be asked even when amount reconciliation alone gives no reason to suspect a problem — this is the concrete gap the existing anti-pattern warns about but does not itself force. |
| 4 | Row count + amount PASS, identity mapping FAIL (entities swapped) | No existing named control for "identity mapping" as a distinct dimension. P0 could plausibly conclude "dataset reconciled" from amount+count alone; a swapped-entity error is not addressed by `reconciliation`, `unmatched_elements_analysis` (nothing is unmatched — every row still matches something), or `factor_reconciliation`. Confirmed by search: no prior `[Analytics]` doc names "identity mapping" as a checked dimension. | `RECONCILIATION_CONTRACT` names `identity_mapping_status` as a separate, mandatory field; `overall_interpretation` invariant explicitly forbids inferring identity integrity from amount/row-count passes alone. | **Real, and the clearest incremental catch of the four elements.** This is a genuinely new named dimension; P0 has no equivalent control. |
| 5 | Premature stop (dominant contributor found, material timing question remains, data available) | §6 (`explanation challenge`, material case) + §10 escalation rule ("competing explanations remain materially plausible") already require continuing to the discriminating timing check before a final claim; §8 Analytical Judge would flag a premature `SUPPORTED`/`ROOT CAUSE` claim. Correct outcome already. | `ANALYSIS_CONTINUATION_GATE`: `decision: CONTINUE`, `next_method_candidate: timing_validation`, `what_can_it_change` stated explicitly. Same outcome, now as a recorded object. | **None identified.** Outcome identical to §10+§6+§8. The gate adds an explicit, named next-method field; it does not change what is permitted. |
| 6 | Method bloat (routine variance reconciled, stable conclusion, several methods technically eligible) | §10 stop rule ("added complexity provides no decision value") already applies; §9 runtime collapse already keeps routine cases compact. Correct outcome already. | `ANALYSIS_CONTINUATION_GATE`: `decision: STOP`, `reason` cites no material unresolved question. Same outcome, now recorded. | **None identified.** Duplicates §10 without a new substantive rule; value (if any) is a recording/enforcement discipline, unverified without live testing. |
| 7 | Discriminating evidence unavailable, causal interpretation requested | §10 escalation rule ("causal language is requested without causal evidence") plus §4 `blocked != executed` and §6 claim ladder already stop causal promotion and require the lower supported claim strength. Correct outcome already. | `ANALYSIS_CONTINUATION_GATE`: `decision: BLOCK`, `required_evidence_available: no`. Same outcome, now recorded as a `BLOCK` rather than an implicit stop. | **Weak.** Same substantive outcome; the gate makes "why we didn't proceed" explicit and auditable rather than leaving it as an unrecorded application of §10. |
| 8 | Held-out: population semantics shift (cost per resolved ticket; ticket-closure policy changed) | §5's `denominator_constant_or_explained?` is domain-agnostic in wording and *should* generalize, but nothing in P0 forces recognizing "ticket-closure policy changed" as a denominator-population event rather than an efficiency gain — it depends entirely on the executor's own generalization, with no structural prompt. | `POPULATION_CONTRACT`'s field list (`denominator_population`, `denominator_changed_vs_baseline`) is the same generic structure as §5, just more granular; it does not add a domain-transfer mechanism either — transfer still depends on the executor recognizing "ticket-closure policy" as a `denominator_population` change. | **Unproven, not clearly better.** Paper trace cannot show P1 transfers better than P0 here; both rely on the same underlying generalization capability. This is exactly the kind of "held-out deterioration/no-clear-outperformance" case the issue asks to flag honestly rather than force-adopt. |
| 9 | Held-out: reconciliation semantics shift (equal aggregate customer count, material entrant/exit churn) | `unmatched_elements_analysis` (existing method) is capable of producing `only_in_left`/`only_in_right`, but nothing in P0 forces asking the question when the *aggregate count itself is unchanged* — an aggregate-count match is a weaker prior for suspecting mismatch than a reconciliation-amount pass, so the P0 trigger is even less likely to fire here than in scenario 3. | `RECONCILIATION_CONTRACT`'s `matched_population`/`only_in_left`/`only_in_right` fields are mandatory regardless of domain (financial amounts or customer cohorts) and regardless of whether the aggregate figure itself looks stable. | **Real and transfers.** Because the contract's fields are declared independent of domain-specific triggers, this is the one held-out case where the P1 structure plausibly transfers better than P0's trigger-dependent method activation. |
| 10 | Old P0 compact regression (simple quick Plan/Fact, stable population, reconciled data, no material trigger) | Compact path per §9: `QUESTION → INTENT → CORE/TRIGGERED METHOD → DETERMINISTIC RESULT → COMPACT QA → ANSWER`. No full population/reconciliation/continuation record. | All three P1 controls carry an explicit "activation trigger" clause requiring a material/decision-critical case; none is instantiated for this routine case. Output stays on the existing compact path — same as P0. | **No regression** (this is the point of the test): P1 additions do not leak into the routine/quick path. |

## 6. Known-case vs. held-out/shifted result, reported separately

- **Known cases (1–7):** 2 of 7 show a clear, real incremental catch not
  present in P0 (scenarios 3, 4 — both `RECONCILIATION_CONTRACT`). 1 of 7
  (scenario 1, `POPULATION_CONTRACT`) shows a weak/evidentiary-only catch.
  2 of 7 (scenarios 5, 7 — `ANALYSIS_CONTINUATION_GATE`) show the same
  outcome as P0 with a recording/traceability difference only. 1 of 7
  (scenario 6, `ANALYSIS_CONTINUATION_GATE`) shows no identified incremental
  value. 1 of 7 (scenario 2) is out of scope for the P1 additions and
  correctly unaffected.
- **Held-out / shifted cases (8–9):** 1 of 2 (`RECONCILIATION_CONTRACT`,
  scenario 9) plausibly transfers better than P0 because its fields are
  triggered by declaration, not by domain-specific suspicion. 1 of 2
  (`POPULATION_CONTRACT`, scenario 8) does **not** show a clear transfer
  advantage over P0 in this paper trace — flagged honestly rather than
  claimed as a win.
- **Old-P0-regression case (10):** No regression; compact path preserved for
  all four elements.
- Per the promotion gate: a known-suite win combined with held-out
  deterioration/non-improvement would be a promotion failure. Here,
  `RECONCILIATION_CONTRACT`'s known-case catches (3, 4) are corroborated,
  not contradicted, by its held-out case (9) — supporting adoption for owner
  review. `POPULATION_CONTRACT`'s known-case catch (1) is weak and its
  held-out case (8) shows no clear transfer advantage — this does not meet
  the bar for a strong incremental-catch claim, and is reported as such.

## 7. Incremental catches (explicit)

- `RECONCILIATION_CONTRACT`: identity-mapping-failure (scenario 4) has no
  prior named control anywhere in `[Analytics]` documentation — genuinely new
  coverage. Population-vs-amount reconciliation conflation (scenario 3, 9)
  is named as an anti-pattern today but not structurally forced; the
  contract forces it via mandatory fields, including in a held-out domain.
- `POPULATION_CONTRACT`: closes a "quantification asserted, not shown"
  loophole in §5's binary fields (scenario 1). Modest; does not change the
  final claim-strength outcome versus P0.
- `ANALYSIS_CONTINUATION_GATE`: no incremental catch identified in this
  paper-trace pilot (scenarios 5–7 identical outcome to §10 alone); value, if
  any, is enforcement/auditability of an explicit decision record, unverified
  without live comparative execution.
- `HELD_OUT_TRANSFER_EVAL`: not itself a detection control; its value is
  making the known-vs-held-out separation in §6 possible at all. This pilot
  populates the lane definitions and scenario set; it does not yet run them
  against live model output.

## 8. Regressions

None identified. `ANALYTICAL_TECHNIQUES.md` is byte-identical to
`origin/main` (§4). Scenario 10 confirms the compact/routine path is
unaffected by any of the four additions. No existing method, intent,
Analytical Judge check, or claim-ladder rule was weakened, replaced, or
duplicated as a competing source of truth.

## 9. Complexity / false-block observations

- No false blocks identified: all four additions are written as
  activation-gated (material/decision-critical trigger required) and
  explicitly instructed not to instantiate for routine/quick cases (scenario
  10).
- Bloat risk is structurally bounded for `ANALYSIS_CONTINUATION_GATE` by its
  "activation trigger" clause, but this pilot cannot verify in a live run
  that an executor actually respects the collapse instruction rather than
  instantiating the full record defensively "just in case" — flagged as a
  residual limitation, not asserted as safe.

## 10. Per-element recommendation

- `POPULATION_CONTRACT`: **ADOPT_FOR_OWNER_REVIEW**, with an explicit caveat
  that the paper-trace incremental catch is modest (evidentiary rigor, not a
  new outcome) and the held-out transfer case (8) did not show a clear
  advantage over P0. Owner review should weigh this as a lower-confidence
  adopt than `RECONCILIATION_CONTRACT`.
- `RECONCILIATION_CONTRACT`: **ADOPT_FOR_OWNER_REVIEW**. Clearest incremental
  catch of the four (identity-mapping dimension, scenario 4), corroborated by
  a held-out case (scenario 9) that plausibly transfers better than P0's
  trigger-dependent mechanism.
- `ANALYSIS_CONTINUATION_GATE`: **DEFER**. No incremental catch identified
  against the paper-traced scenarios (5–7 produce identical outcomes to
  existing §10 rules); the concept is not harmful (no regression, no bloat in
  the traced scenarios) but its value is unproven without live comparative
  execution showing it prevents a silent premature stop or bloat episode that
  §10 alone would have missed. Recommend deferring adoption until such
  live-execution evidence exists, rather than adopting on documentation
  completeness alone.
- `HELD_OUT_TRANSFER_EVAL`: **ADOPT_FOR_OWNER_REVIEW** as a QA/EVAL
  scaffold only (lane definitions + initial scenario set). Flagged limitation:
  this pilot did not execute the lanes against live model output; that
  execution is required before the lane can support a real promotion
  decision for any of the other three elements.

## 11. Rollback status

Documented and structurally trivial for all four (see
`ANALYTICAL_REASONING_STANDARD.md` §"P1 pilot status" and `QA_CHECKLIST.md`):

- `POPULATION_CONTRACT` → §5's bare population checks.
- `RECONCILIATION_CONTRACT` → existing separate
  reconciliation/unmatched/factor-reconciliation/residual/coverage controls,
  wrapper removed.
- `ANALYSIS_CONTINUATION_GATE` → §10 stop/escalation rules alone.
- `HELD_OUT_TRANSFER_EVAL` → delete the QA_CHECKLIST section and smoke QA
  case 13; analytical runtime unaffected.

No method-registry migration is required for any rollback.

## 12. Residual limitations

- This is a documentation/design pilot: a structured written walkthrough, not
  a live LLM execution comparison. All "P0 baseline vs. P1 candidate"
  outcomes above are reasoned from the contract text, not observed from an
  actual run. Per the issue's own promotion gate, this is sufficient for
  "target-specific bounded-pilot evidence for a separate owner decision," not
  for promotion itself.
- `boundary_cases` (exact tolerance, zero-denominator, fully-matched-at-100%)
  are not separately populated with dedicated scenarios in this pilot; only
  the six lane definitions exist in `QA_CHECKLIST.md`.
- `ANALYSIS_CONTINUATION_GATE`'s recommended DEFER should be revisited with
  live comparative evidence rather than being read as a permanent rejection.
- Held-out transfer claims (§6, §10) are themselves reasoned qualitatively
  (trigger-dependent vs. declaration-mandatory), not measured against an
  actual held-out execution run.

## 13. Explicit statement

**Owner review is required before any promotion, merge, deployment, or
Project sync of any of the four elements. Nothing in this pilot authorizes
production adoption.**

## 14. Final gate verdict

```text
PASS_FOR_OWNER_REVIEW
```

Rationale: all bounded-pilot acceptance criteria in issue #445 are met —
scope stayed inside `ChatGPT/[Analytics]/**`; all four elements evaluated as
one coherent package; 22-method registry unchanged (verified by diff); no
new `METHOD_ID`/analytical intent; `HELD_OUT_TRANSFER_EVAL` stays QA/EVAL
only; all 10 scenarios recorded with baseline-vs-candidate outcomes;
known/held-out results reported separately; incremental catches, false
blocks, and regressions stated explicitly; each element has one of the four
required recommendations (three `ADOPT_FOR_OWNER_REVIEW`, one `DEFER` — not
forced adoption across the board); rollback documented; residual limitations
stated; `owner review required` is the terminal state.
