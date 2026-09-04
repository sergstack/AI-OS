# AIOS AutoResearch — MD-2 Cross-Project Decision Package — 2026-09-05

Runtime: `main`@`3b81126cb754a3b4021fa16666b418e62eda5c90`.

Status: **decision package for `[LLM]` / `[Analytics]` / `[AI OS]`. No
directional mapping is implemented here. `[Codex]` is not the eligible
decision-maker for this gap** — issue #433's own `run_experiment` docstring
already names MD-2 as an owner ruling scoped to "minimal-for-C1," explicitly
not the general reusable semantics, and the pre-merge method review of PR
#434 already flagged MD-2 as the one item that could not be resolved inside
that PR (see "Prior review already on record" below).

## 1. Exact current data flow

```
lj.run_blind_ab(...)                              [autoresearch_live_judge.py]
  -> two Judge calls (primary order, reversed order), each producing
     validated finding objects against schemas/autoresearch_live_semantic_finding.schema.json
  -> per-order _material(records) -> (worst_verdict, worst_severity)
  -> order-consistency check: v0==v1 and s0==s1 ?
       yes -> contributes = aggregate ("pass"|"revise"|"blocked", never "fail")
       no  -> contributes = "inconclusive"  (order disagreement -> never averaged)
  -> returns CaseSemanticEvidence(contributes=...)

cli._contributes_to_pair(contributes)             [autoresearch_cli.py, MD-2]
  contributes == "pass"        -> (baseline_verdict="pass", candidate_verdict="pass")
  anything else                -> (None, None)

cli.Controller.run_experiment  per matched rerun k:
  per_case[cid]["baseline_verdicts"].append(bv)
  per_case[cid]["candidate_verdicts"].append(cv)

adc.CaseObservation(
  baseline_verdicts=tuple(...),      # from the list above, across 3 reruns
  candidate_verdicts=tuple(...),
)

adc.evaluate_case_material_improvement(obs)        [autoresearch_decision_comparator.py]
  matched = [(b,c) for b,c in zip(baseline_verdicts, candidate_verdicts) if b is not None and c is not None]
  if len(matched) < MIN_MATCHED_RERUNS(3): return "inconclusive", "no_observation"
  if group_has_variance(baseline_side): return "inconclusive", "evaluator_disagreement_unresolved"
  all_improved = all(severity(c) < severity(b) for b, c in matched)
  return ("keep" if all_improved else "inconclusive"), None
```

Exact source: `_contributes_to_pair` in `scripts/autoresearch_cli.py`
(comment block immediately above it is headed `# --- METHOD DECISION MD-2
(owner ruling, issue #433 -- MINIMAL-FOR-C1 scope) ---`);
`evaluate_case_material_improvement` in
`scripts/autoresearch_decision_comparator.py`, lines ~122-148 on this
revision; the strict-improvement requirement is also stated in prose at
`ChatGPT/[Analytics]/Knowledge/AUTORESEARCH_STOCHASTICITY_NONINFERIORITY_METHOD.md`
§7: "every matched candidate rerun for that case has a strictly better
`normalized_behavior_result` than its paired baseline rerun (reproducible
across all available reruns — 'one successful run is never evidence of
improvement,' reused verbatim as the Required rule)."

## 2. Why strict improvement is currently unreachable

`severity(...)` maps `{"pass": 0, "revise": 1, "blocked": 2}`
(`av.VERDICT_PRECEDENCE`, reused unchanged by the comparator). Under MD-2,
every matched pair is `(pass, pass)` — `severity(b) == severity(c) == 0` —
by construction, because `_contributes_to_pair` maps the ONLY unambiguous
Judge outcome (`contributes == "pass"`, meaning the Judge found A and B
equivalent) to an *identical* baseline/candidate pair, and maps every case
where the Judge found some difference (`revise`, `blocked`,
`inconclusive`) to `(None, None)` — excluded from `matched` entirely, never
attributed to either side.

`all(severity(c) < severity(b) for b, c in matched)` therefore has exactly
two possible outcomes:
- `matched` is non-empty and every pair is `(0, 0)` → `0 < 0` is `False` for
  every pair → `all_improved = False`.
- `matched` has fewer than 3 non-null pairs → short-circuits to
  `"inconclusive"`/`"no_observation"` before `all_improved` is even
  computed.

There is no code path by which `all_improved` can be `True`. This is a
structural property of the two functions composed together, verified by
direct reading, not an empirical observation from one run's data. C1-R1's
`inconclusive` result is consistent with this but does not by itself prove
it — the proof is in the composition of `_contributes_to_pair` and
`evaluate_case_material_improvement`, independent of any particular Judge
output.

Root cause, one level up: `lj.run_blind_ab` produces one **relative**
signal (does B differ materially from A, and in which direction of
severity) that has already been collapsed to a single aggregate
`contributes` value shared by both sides. The comparator's
`evaluate_case_material_improvement` wants two **independent absolute**
per-side severities. MD-2 is the (deliberately conservative, owner-ruled)
bridge between these two shapes, and it was scoped, in the #433 PR
docstring's own words, to avoid "directional per-side guessing about which
side a revise/blocked verdict belongs to" — i.e., it trades the ability to
ever detect improvement for the guarantee of never fabricating a direction
it wasn't given.

## 3. Prior review already on record

The pre-merge method review of PR #434 (`docs/evidence/AUTORESEARCH_V02_LIVE_LOOP_WIRING_2026-09-04.md`,
"Formal method review" section) already scored MD-2 `blocked` for exactly
this reason, and listed four candidate resolutions verbatim:

> (a) keep only the unambiguous step — order-consistent `pass` ->
> (pass,pass); every other `contributes` -> (None,None) [no fabricated
> direction; a Judge-found regression then maps to inconclusive, not
> reject]; OR
> (b) [LLM]/#394: add a directional-attribution field to the finding
> schema / evaluator contract so a finding names the worse side; OR
> (c) [LLM]/#414: run the Judge in a per-side absolute-scoring mode
> instead of (or alongside) blind A/B; OR
> (d) [Analytics]/#395: define canonically how a comparative finding maps
> to per-side `normalized_behavior_result`.

The owner's actual ruling for PR #434 selected **(a)** — explicitly and
narrowly, as a "minimal-for-C1" scope, explicitly **not** the general
reusable semantics, explicitly deferring (b)/(c)/(d) to a follow-up. This
decision package is that follow-up. Options A/B/C below map directly onto
(b)/(c)/(d) above; Option D is new (not in the original four), added
because the program's own objective statement should be checked against
the possibility that no directional extension is wanted yet.

## 4. Options

### Option A — directional Judge extension, blind A/B preserved (≈ prior option b)

Extend the finding schema (`schemas/autoresearch_live_semantic_finding.schema.json`,
additive to the frozen v0.1 `autoresearch_semantic_finding.schema.json`,
which stays untouched) with a field that names which of the two
*positionally-blind* labels, `A` or `B`, the finding judges materially
better — never "baseline"/"candidate" (the Judge still never learns which
is which; de-blinding stays in the privileged layer exactly as today, per
`AUTORESEARCH_SEMANTIC_EVALUATOR_CONTRACT.md` §11's anti-leakage rules).
`_contributes_to_pair` is replaced by a real mapping from
(order0 preference, order1 preference, order-consistency) to
`(baseline_severity, candidate_severity)`.

- Evaluator contract change: yes — new field in the frozen finding schema,
  new clause in `AUTORESEARCH_SEMANTIC_EVALUATOR_CONTRACT.md` §6, new
  `evaluator_contract_version` and recomputed `frozen_hash` per §10's
  existing content-hash contract (no new hashing mechanism needed).
- Observation semantics change: yes, in `_contributes_to_pair` only;
  `evaluate_case_material_improvement` itself is untouched.
- Comparator compatibility: full — `CaseObservation`'s shape doesn't
  change, only what feeds `baseline_verdicts`/`candidate_verdicts`.
- Regression risk: **medium**. Blind-comparison anti-bias property is
  preserved (this is the architecturally more conservative option). Risk
  is concentrated in getting the Judge to reliably emit a NEW structured
  field — see the reliability caveat below.
- Backward compatibility: existing findings/records remain schema-valid
  (additive field); historical decisions computed under MD-2 are
  unaffected (they never produced `keep_candidate` in the first place).
- Required schema/code changes: `schemas/autoresearch_live_semantic_finding.schema.json`
  (additive field), `autoresearch_live_judge.py::build_judge_prompt` (ask
  for the field) and `validate_live_finding`, `autoresearch_cli.py::_contributes_to_pair`
  replacement. No `autoresearch_decision_comparator.py` change.

**Reliability caveat (empirical, from C1-R1):** 5 of the 6 real Judge calls
in the C1-R1 live run were schema-noncompliant on their one live attempt —
unescaped quotes inside JSON string values (3 cases) or `evidence` supplied
as an object instead of the required string (2 cases) — under the
*current*, simpler finding schema. Asking the same model for an
*additional* structured field increases the surface for the same class of
formatting failure. This doesn't rule out Option A; it means whoever picks
it should budget for a reliability pass (few-shot examples, stricter
"return ONLY this JSON" framing, or a JSON-repair/re-ask step) before
trusting it live.

### Option B — per-side absolute scoring, alongside or instead of blind A/B (≈ prior option c)

Run the Judge once per side (baseline alone, candidate alone), each scored
independently against the rubric with no comparison and no knowledge the
other side exists, producing its own absolute `verdict`/`severity`
directly. This yields `baseline_verdicts`/`candidate_verdicts` entries with
zero change to `evaluate_case_material_improvement` — the comparator
already expects exactly this shape.

- Evaluator contract change: yes — a new, separate prompt template/mode
  under `[LLM]` ownership (§2's blind A/B prompt family is not modified;
  this is an additional family, or a `#414` mode alongside it).
- Observation semantics change: `_contributes_to_pair` is removed/bypassed
  for this mode; `CaseObservation` is built directly from two independent
  absolute verdicts.
- Comparator compatibility: full, and simpler than Option A — no new
  comparator-facing shape at all.
- Regression risk: **medium-low for the comparator, medium for evaluator
  identity**. Loses the blind-comparison protection against anchoring/
  consistency drift across two separate calls (the Judge's internal notion
  of "what counts as `revise`" must now stay stable call-to-call without a
  side-by-side reference); needs its own calibration cases (§12 analog) to
  establish that stability before trusting it.
- Call-budget impact: doubles the Judge's role in each rerun if run
  *alongside* blind A/B (4 Judge calls per rerun instead of 2), or is
  budget-neutral if it *replaces* blind A/B (still 2 calls per rerun, just
  reframed) — this is itself a decision the owner needs to make explicitly,
  since it changes any future batch's `max_provider_calls` preview math.
- Backward compatibility: additive if run alongside; if it replaces blind
  A/B, every batch preview/test that assumes the current 2-call-per-rerun
  Judge shape needs updating.

Empirically, single-sided prompts are structurally simpler than the current
A/B-with-two-outputs-in-one-prompt shape, so this *may* also improve the
formatting-reliability picture observed in C1-R1 — but that is a hypothesis
to test via calibration, not a given.

### Option C — comparator-side adaptation to the existing relative signal (≈ prior option d)

Instead of changing the Judge, redefine `evaluate_case_material_improvement`
(or add a new comparator predicate) to compute "improvement" directly from
a history of relative `contributes` outcomes across matched reruns —
e.g., "improvement" := every matched rerun's `contributes` is
order-consistently favorable to the anonymized side that de-blinds to
`candidate`, with zero reruns unfavorable or ambiguous. This still requires
de-blinding *something* the Judge said about direction, so it does not
avoid needing more information from the Judge than "pass"/other — in
practice it still needs a directional signal from somewhere (Option A's
schema field, most naturally), it just relocates where "improvement" is
*defined* into `[Analytics]`'s comparator rather than the mapping layer.

- Evaluator contract change: possibly none, if Option A's schema field is
  reused as the sole input; the change here is specifically to
  `evaluate_case_material_improvement`'s definition, not to the Judge.
- Observation semantics change: yes, and the most invasive of the three —
  it changes the **frozen method's own acceptance predicate**
  (`AUTORESEARCH_STOCHASTICITY_NONINFERIORITY_METHOD.md` §7), which issue
  #395 designed and froze deliberately.
- Comparator compatibility: this *is* the comparator change.
- Regression risk: **high**. §7's strict "every matched rerun strictly
  better" rule is the method's core conservatism; loosening or reshaping it
  needs its own `[Analytics]`-owned re-derivation and re-freeze under
  `AUTORESEARCH_STOCHASTICITY_NONINFERIORITY_METHOD.md`'s own governance,
  and arguably needs revalidation against every existing calibration case
  this method was checked against, not just AutoResearch v0.2's cases.
- Backward compatibility: any historical `inconclusive` decided under the
  current §7 predicate stays a valid decision under the old rule; this
  option doesn't retroactively change past outcomes, but it does mean two
  different "improvement" definitions could coexist across method versions
  unless the old one is formally superseded.

### Option D — rescope: accept regression/no-op detection as sufficient for now, defer improvement-detection

Make no code change. Explicitly document that the current wiring is a
**safety net** (catches harmful candidates via `evaluate_case_non_inferiority`,
which is fully directional-signal-independent and already works — this is
exactly what Phase 0 (#417) demonstrated live: a harmful mutation was
correctly caught) rather than an **optimization loop** (finds beneficial
candidates), and that closing the improvement-detection gap is a
deliberately deferred, separately-scoped future decision, not blocking
"AutoResearch v0.2 is working as currently scoped."

- No schema/code change, no regression risk, no new evaluator contract.
- Directly conflicts with the stated program objective ("comparator
  различает improvement, regression и отсутствие достаточных
  доказательств") if that objective is retained as-is — this option only
  makes sense if the owner is willing to narrow the objective instead.
- Cheapest, safest, and the only option requiring zero new owner
  cross-project work — but it is a scope decision, not a technical one, so
  it belongs in this package rather than being assumed.

## 5. Recommendation

**Option A**, conditional on budgeting a Judge-output reliability pass
before any live use, is the recommended default: it preserves the
blind-comparison design that is arguably the architecture's strongest
epistemic property, requires no change to the already-validated,
`[Analytics]`-owned non-inferiority/material-improvement method (§7's rule
stays exactly as frozen), and keeps the live call budget unchanged (still 2
Judge calls per rerun).

That said, this recommendation is **not high-confidence** given C1-R1's own
evidence: a model that gets a *simpler* schema wrong 5 times out of 6 may
do no better, or worse, at a schema with one more required field. If
`[LLM]` judges that reliability risk as dominant, **Option B** is the
reasonable second choice, with the explicit caveat that its call-budget and
calibration implications need to be decided up front, not discovered mid-
batch. **Option C** should be treated as a last resort — it is the only
option that touches the frozen non-inferiority method itself, and should
only be picked if `[Analytics]` independently judges that the comparator's
current improvement predicate is wrong on its own terms, not merely
inconvenient given the Judge's current output shape. **Option D** is
offered as the explicit "do nothing more" baseline for comparison, since
it is in fact the value AutoResearch v0.2 has already demonstrated live
(Phase 0's `no_failure_found` / correctly-caught-harmful-mutation result) —
worth naming so the owner can consciously choose to stop there if that is
sufficient, rather than that being a default nobody decided.

## 6. Explicitly not done here

No directional mapping is implemented. No schema is changed. No evaluator
contract version is bumped. No live call was made to test any option. This
package is inert until `[LLM]` / `[Analytics]` / `[AI OS]` accept one option
(or an alternative none of these four capture).
