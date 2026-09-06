# Governance and Anti-Patterns

## Governance principles

- Deterministic calculations before LLM narrative.
- Traceability before automation.
- Main files before slices.
- Evidence before conclusions.
- Acceptance before production readiness.
- Analysis inside `[Analytics]` before handoff.
- Method eligibility and triggers follow `ANALYTICAL_TECHNIQUES.md`; the LLM cannot silently override the registry.
- Reasoning cannot substitute for deterministic execution or missing prerequisites.
- Claim strength cannot exceed final evidence sufficiency.
- Every material / decision-critical analytical conclusion passes an explicit post-findings Analytical Judge gate (`ANALYTICAL_REASONING_STANDARD.md` §8) before narrative packaging; the gate orchestrates existing controls and adds no second QA framework.
- `docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md` remains canonical execution governance; `ANALYTICS_EXTENSION.md` supplies domain-specific constraints without creating a second execution framework.
- A formula alone is not a sufficient metric definition; material/flagship/ratio-like metrics require an approved `METRIC_DEFINITION_CARD` (`ANALYTICAL_REASONING_STANDARD.md` §11).
- Canonical `VALUE_STATE` distinctions (`DATA_CONTRACTS.md`) are not collapsed into a generic null where doing so could change denominator, population, reconciliation, classification coverage, metric result, claim strength, or management conclusion (§12).
- Every headline claim for `analytical_depth = material / decision_critical` has complete Claim/Evidence Registry lineage; missing lineage sets `allowed_in_executive = no` (§13).
- `GATE 1 (data/calculation)`, `GATE 2 (analytical claim)`, and `GATE 3 (narrative)` remain distinct: `DATA VALID != CLAIM SUPPORTED != NARRATIVE ACCEPTABLE` (§14).

## Evidence labels

Use:

```text
DATA FACT
CALCULATION RESULT
INTERPRETATION
RECOMMENDATION
HYPOTHESIS
LIMITATION
BLOCKER
```

## Blockers

Do not publish final management conclusion when:

- data contract missing;
- grain missing;
- DQ Fail;
- unreconciled totals;
- missing metric formula;
- unsupported cause;
- risk without basis;
- action without owner/due date;
- no main mart for a mart-based conclusion;
- the Analytical Judge gate returns `blocked`;
- a material/flagship/ratio-like metric has no approved `METRIC_DEFINITION_CARD`;
- a headline claim lacks complete Claim/Evidence Registry lineage (`allowed_in_executive = no`).

## Anti-patterns

| Anti-pattern | Why bad | Correct action |
|---|---|---|
| Handoff to Codex too early | Analytics loses its role | Analyze first, handoff implementation only |
| Slices before main files | Inconsistent outputs | Build `stage_main_full`, then `mart_main_full`, then slices |
| Raw-to-memo | Unsupported conclusions | Use mart/evidence |
| LLM as calculation source | Non-deterministic truth | Calculate deterministically |
| Hidden business logic | Cannot audit | Document formulas/classifiers |
| Pretty memo before QA | Looks right, may be wrong | QA first |
| Low Confidence as fact | Misleading | Label hypothesis |
| Risk without basis | Decorative risk | Add `risk_basis` or remove |
| Action without owner/date | Not actionable | Add owner/due date/status |

## P0 analytical reasoning failure modes

Apply these controls through `ANALYTICAL_REASONING_STANDARD.md` and the existing Analysis QA; do not create a competing governance or QA framework.

| Failure mode | Required control |
|---|---|
| Driver presented as root cause; correlation presented as causation | Use the claim ladder, `claim_support`, `causal_status`, and causal evidence gate. |
| Premature explanation | Run the preliminary evidence check and stop when explanatory analysis is infeasible. |
| Baseline dependence | State baseline/rationale and run required baseline robustness for material cases. |
| Aggregation bias; selection/exclusion bias | Check materially relevant segmentation, exclusions, and subgroup robustness. |
| Population or denominator change | Explain population/denominator and quantify scope change before interpreting ratios. |
| Timing or cut-off effect | State cut-off and test timing/trend when the declared trigger is satisfied. |
| False precision | Constrain precision and claim strength to data quality and evidence sufficiency. |
| Silent exclusions | Record materially plausible excluded methods and data exclusions. |
| Narrative stronger than evidence | Enforce `claim strength <= final evidence sufficiency`. |
| Method bloat | Use the minimum sufficient method set and stop conditions. |
| Confidence mistaken for causality | Preserve `confidence != claim_support != causal_status`. |
| Numerical magnitude mistaken for business materiality | Assess decision context and materiality separately; do not use a numerical reasoning score. |
| Reasoning substituted for deterministic execution | Enforce `LLM reasoning != deterministic execution`. |
| LLM silently overrides method registry | Record candidate omission and route it to existing QA/review. |
| Subjective or undefined method trigger | Require `trigger_type`, `trigger_rule`, and `trigger_evidence_required`. |
| Blocked method treated as evidence | Enforce `blocked != executed` and reject blocked/planned/not-needed lineage. |
| Method execution lineage loss | Require unique `method_execution_id` and claim-to-evidence lineage. |
| Conflicting methods silently reconciled | Preserve conflicting results, record contradictory evidence, constrain claim strength, and escalate if material. |
| Full reasoning runtime applied to a routine case without trigger | Use the compact path and do not instantiate unused full reasoning records. |
| Anomaly mistaken for control exception | Distinguish unusual observations from explicit rule/control violations. |
| Aggregate reconciliation used instead of entity-level unmatched analysis | Use unmatched-elements analysis when concrete one-sided populations are material. |
| Driver decomposition accepted without factor reconciliation | Reconcile summed factor effects to observed delta whenever mathematically applicable. |
| Timing shift interpreted as economic effect | Run timing validation when cut-off or recognition timing could change interpretation. |
| Transformation artifact interpreted as source/business effect | Trace `REPORT → MART → STAGE → RAW` and identify the first verified layer where the effect appears. |
| Leading indicator treated as proven causal predictor | Use calibrated signal/association/risk language unless causal evidence exists. |
| Method catalog inflated by converting controls into methods | Require a distinct question, execution procedure, and material analytical effect before adding a method. |
| Decision methods leak from `[Thinking]` into `[Analytics]` | Keep trade-offs, reversibility, premortem, risk appetite, choice, and decision in `[Thinking]`. |
| Reasoning-control loop mistaken for an autonomous execution loop | Keep reasoning/method selection inside the AES-governed scope, checks, bounded correction, stop, rollback, acceptance, and authority boundaries. |
| Analytical conclusion reaches memo without an explicit post-findings challenge | Run the Analytical Judge gate after findings; record `ANALYTICAL_JUDGE` `pass / revise / blocked` for material / decision-critical cases. |
| Analytical Judge treated as an autonomous retry loop | Allow only `Judge finding → one bounded correction or deterministic rerun → Judge re-check`; no silent self-retry, no unrestricted iteration; AES limits and the `[Codex]` one-fix limit are unchanged. |
| Analytical Judge used as a second QA framework or a new taxonomy | The gate only orchestrates `PRELIMINARY_EVIDENCE_CHECK`, explanation challenge, `FINAL_EVIDENCE_SUFFICIENCY`, `CLAIM_EVIDENCE_REGISTRY`, Analysis QA, and variance diagnostic QA; it defines no new field. |
| `blocked` method converted into evidence at the Judge step | Enforce `blocked != executed`; a `blocked` prerequisite forces Judge `blocked`, not a weaker `pass`. |
| Formula treated as a sufficient metric definition (ambiguous ratio/rate published as flagship) | Require `METRIC_DEFINITION_CARD` with numerator/denominator/aggregation/population before a material conclusion; block or limit if unresolved. |
| Materially different missing/uncertainty states collapsed into one null | Preserve `VALUE_STATE` (`UNKNOWN`/`NOT_REPORTED`/`PARSE_FAILED`/`MISSING_SOURCE`/`UNMATCHED`/`BLOCKED`); reflect coverage/denominator impact before claiming `SUPPORTED`. |
| Headline claim published without method/evidence lineage | Require complete Claim/Evidence Registry lineage; set `allowed_in_executive = no` and route to Analytical Judge `revise`/`blocked` when missing. |
| Data/calculation correctness treated as license for a stronger claim or narrative | Keep `GATE 1 (data/calculation)`, `GATE 2 (analytical claim)`, `GATE 3 (narrative)` distinct; `DATA VALID != CLAIM SUPPORTED != NARRATIVE ACCEPTABLE`. |

## EDA-to-claim calibration additions (issue #451)

These rows name specific instances of the failure modes above (claim ladder,
`causal_status`, `generalization_scope`/`generalization_evidence`, Metric
Definition Card `forbidden_interpretations`) that a 2026-09-06 review found
worded ambiguously enough to warrant an explicit example. No new field,
taxonomy, method, or gate is added; see
`EDA_CLAIM_CALIBRATION_REVIEW_2026-09-06.md` for the full mapping and
paper-trace evidence.

| Failure mode | Required control |
|---|---|
| An observed rating/score (e.g. a critic's `points`) presented as objective quality or personal preference | State the metric is the observed rating (`DATA FACT` / `CALCULATION RESULT`); a quality or preference claim is an `INTERPRETATION` requiring additional evidence, not an automatic reading of the score. |
| A model-implied expected value or residual presented as market inefficiency, realizable savings, or fair value | Treat the expected value/residual as a model-conditional `CALCULATION RESULT` (`causal_status: association_only` unless demonstrated otherwise); keep units and any log-price transform explicit; require additional market/comparability evidence before a value-gap or fair-price claim. |
| A definition/owner decision for an undefined or composite metric mistaken for the missing empirical evidence a claim needs | A definition may fix the intended meaning of a metric (`METRIC_DEFINITION_CARD`); it cannot manufacture evidence — `claim_support` and `status: provisional/approved` remain independent fields. |
| Selected high-scoring reviews, or reviewer/record volume, presented as a purchase or producer-wide reliability guarantee | Selected/filtered records describe those records; require `generalization_scope` / `generalization_evidence` before extending to future purchases or population-wide reliability. Volume states observed coverage, not demonstrated expertise. |
| A dataset-listed price (or other point-in-time attribute) presented as current price, availability, or purchase suitability | State the attribute's observation basis (dataset vintage/snapshot date) explicitly; do not invent an observation date or silently substitute a current-state claim. |
| Reviewer/rater averages treated as a bias-corrected difficulty scale ("strict/generous critics") without checking confounding | Inspect overlap/common support and separability from region/style/product mix before a reviewer-normalized comparison; when the available design cannot separate them, retain the limitation rather than asserting a corrected objective scale. |
| In-sample association (e.g. text/feature separation by outcome) presented as measured predictive performance | Require an explicit target, baseline, held-out split, metric, and leakage/duplicate-entity check before a predictive-performance claim; association alone supports `causal_status: association_only`, not a performance claim. A retrospective/explanatory use (e.g. reconstructing an already-known label) is distinct from an ex-ante predictive use and must be labeled as such. |

## Metric / artifact explosion

Anti-pattern:
A short analytical request produces a large workbook, many sheets, or hundreds of columns without explicit need.

Why bad:

- user cannot inspect the result;
- decision signal is buried;
- QA fields become noise;
- compact task becomes `full` package.

Correct action:

- classify output mode first;
- default to compact view;
- expose only decision-relevant metrics;
- move evidence/QA/lineage to appendix or internal design;
- ask for `full` mode only when needed.

## Production readiness rule

Do not claim production readiness unless:

- implementation exists;
- tests passed;
- smoke QA recorded;
- acceptance criteria passed;
- residual risks listed;
- rollback/release notes exist.
