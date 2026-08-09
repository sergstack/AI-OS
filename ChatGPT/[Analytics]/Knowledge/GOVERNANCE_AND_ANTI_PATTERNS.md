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
- `AUTONOMOUS_EXECUTION_STANDARD.md` remains canonical execution governance; `ANALYTICS_EXTENSION.md` supplies domain-specific constraints without creating a second execution framework.

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
- no main mart for a mart-based conclusion.

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
