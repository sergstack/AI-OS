# Analytical Reasoning Standard — P0

## Purpose and boundary

This standard adds a bounded reasoning-control layer to the existing `[Analytics]` workflow. It does not replace or redefine the Data Contract, RAW, `stage_main_full`, `mart_main_full`, `mart_main_tz` / `mart_main_compact`, deterministic calculations, chart sourcing, memo pipeline, QA / Judge, acceptance, or Codex handoff boundary.

Execution remains governed by the canonical repo-root `AUTONOMOUS_EXECUTION_STANDARD.md`. `docs/autonomous_execution/extensions/ANALYTICS_EXTENSION.md` remains authoritative for Analytics-specific AES requirements. This standard structures analytical reasoning and method selection only; it does not fork, weaken, or duplicate AES execution states, corrective-loop limits, stop conditions, rollback, acceptance, or external-action authority.

```text
reasoning-control loop != autonomous execution framework
adaptive reasoning != autonomous agent
adaptive reasoning does not create an independent retry/self-improvement loop
```

```text
business question
→ task profile and analytical intent
→ deterministic-first minimum sufficient method set
→ prerequisite gate
→ existing Analytics execution
→ preliminary evidence check
→ explanation challenge when material
→ claim calibration and final evidence sufficiency
→ existing QA / Judge / acceptance
```

`mart_main_full` remains the evidence and reuse layer. Management-facing marts remain `mart_main_tz` / `mart_main_compact`. Calculations, slices, and chart sources continue to use verified analytical layers.

Explicit boundary:

```text
LLM reasoning != deterministic execution
```

The LLM may classify ambiguous intent, evaluate bounded judgment or hybrid triggers, challenge explanations, and calibrate wording. It cannot replace deterministic arithmetic, formulas, reconciliation, variance, driver or exposure calculations, deterministic classification, or a deterministically executable forecast. Missing deterministic prerequisites cannot be compensated by reasoning.

## 1. `TASK_PROFILE` and derived controls

Create the profile before method selection when the case is not eligible for the compact routine path:

```text
TASK_PROFILE

question:
decision_user:

materiality: low / medium / high
uncertainty: low / medium / high
reversibility: easy / medium / difficult
evidence_state: unknown / weak / mixed / strong
evidence_state_basis:

analytical_depth: routine / material / decision_critical
output_mode: quick / standard / full
expected_output:

challenge_level: minimal / standard / enhanced
robustness_required: yes / no
manual_review_required: yes / no
thinking_handoff_possible: yes / no
```

Do not create a numerical score. `analytical_depth` controls reasoning depth; `output_mode` controls artifact size. They are independent.

Base mapping:

| analytical_depth | challenge_level | Derived control |
|---|---|---|
| `routine` | `minimal` | Use compact reasoning unless a material trigger appears. |
| `material` | `standard` | Apply the standard challenge and relevant robustness controls. |
| `decision_critical` | `enhanced` | Consider robustness and record explicit final evidence sufficiency. |

Set `robustness_required = yes` when a declared baseline, subgroup, or sensitivity robustness trigger is satisfied; otherwise `no`. Set `thinking_handoff_possible = yes` when the unresolved question crosses the stop/escalation boundary into alternatives, trade-offs, risk appetite, or decision; otherwise `no`.

Set `manual_review_required = yes` when at least one materially relevant condition holds:

- the final claim uses causal or root-cause language;
- material contradictory evidence remains unresolved;
- a decision-critical conclusion has weak or partial evidence;
- a judgment or hybrid method materially affects the final claim;
- the Analytics conclusion requires escalation or handoff to `[Thinking]`.

When set to `yes`, the analysis cannot pass final publication automatically: record the reviewer or review owner, review status, and resolution in the existing Analysis QA / acceptance path. In other cases, use the existing governance and risk context without inventing a scoring model.

## 2. Analytical intents

P0 activates only:

```text
validate_data
diagnose_variance
explain_drivers
test_explanation
project_forward
```

Candidate intents are deferred and must not be routed as active P0 intents without pilot evidence:

```text
locate_concentration
detect_anomalies
analyze_structure
analyze_trend
prepare_decision_evidence
evaluate_control
```

Classify the business question to the narrowest active intent that can answer it. When several intents are required, record each one and its distinct question; do not expand the taxonomy.

## 3. Deterministic-first method selection

`ANALYTICAL_TECHNIQUES.md` is the source of truth for method eligibility, registry metadata, intent mapping, and method triggers.

```text
INTENT
↓
INTENT × METHOD MAPPING
↓
CORE METHODS
↓
DETERMINISTIC TRIGGERS
↓
TRIGGERED METHODS
↓
JUDGMENT / HYBRID TRIGGERS
↓
BOUNDED LLM REVIEW
↓
OPTIONAL / MATERIAL OMISSION CHECK
```

Method status semantics:

- `CORE`: selected for the intent, subject to prerequisites.
- `TRIGGERED`: selected only when its declared trigger contract is satisfied.
- `OPTIONAL`: considered only when materially plausible and capable of changing the analytical outcome.

For every non-CORE selection that depends on a trigger, the mapping must define:

```text
trigger_type: deterministic / judgment / hybrid
trigger_rule:
trigger_evidence_required:
priority:
```

- `deterministic`: verified inputs satisfy an unambiguous calculation or rule.
- `judgment`: bounded analytical reasoning is required.
- `hybrid`: deterministic evidence creates a candidate trigger; bounded reasoning determines material relevance.

Absent trigger evidence cannot silently activate a method. The LLM cannot silently override the registry. A materially plausible omitted method is recorded as `candidate_omission` with rationale and sent to existing QA / review; it is not silently included.

### Minimum sufficient method set

Include a method only if it can materially change at least one of:

```text
finding
confidence
risk
recommendation
limitation
evidence assurance
```

Stop adding methods when none is likely to change those outputs. Method count is not evidence strength.

### Canonical P0 registry scope

The active P0 registry contains exactly 22 approved methods. The six capability-gap additions are `exception_analysis`, `unmatched_elements_analysis`, `factor_reconciliation`, `timing_validation`, `data_layer_check`, and `leading_indicator_analysis`. `ANALYTICAL_TECHNIQUES.md` owns their schema, eligibility, prerequisites, execution boundary, and triggers.

Capability completeness must not inflate the registry. Do not create additional `METHOD_ID` values for contradicting/discriminating evidence, falsification, hypothesis/claim ladders, numerator/denominator/population controls, stop conditions, largest-variance ranking, time lens, detail checks, or structure-of-change configurations. These remain reasoning, QA, governance, or configurations of existing methods.

Decision methods such as robust/no-regret/conditional action, premortem, decision reversibility, and trade-off analysis remain owned by `[Thinking]`. `[Analytics]` provides forecast, sensitivity, verified evidence/uncertainty, downside, and leading indicators without making the strategic choice.

Any registry expansion beyond 22 requires P1/pilot evidence or separate explicit acceptance. Do not add methods merely to reproduce a mixed 45-technique catalog.

## 4. Method plan and prerequisite gate

For every concrete planned application, record:

```text
METHOD_PLAN

method:
intent:
status: CORE / TRIGGERED / OPTIONAL

why_selected:
question_answered:

trigger:
trigger_type:
trigger_rule:
trigger_evidence_required:
trigger_evidence:
priority:

execution_owner:
execution_mode: deterministic / reasoning / mixed

prerequisites_met: yes / no / not_applicable
execution_status: planned / executed / blocked / not_needed
missing_requirement:

method_execution_id:
```

Prerequisite semantics:

- `yes`: all required prerequisites exist and are satisfied;
- `no`: a required prerequisite exists but is unavailable or unmet;
- `not_applicable`: the method has no prerequisite of the relevant type.

`not_applicable` cannot bypass a real missing prerequisite.

```text
blocked != executed
blocked method != supporting evidence
```

`method_execution_id` uniquely identifies one application within the analysis. Repeated applications with a different period, grain, filter, baseline, population, or scenario require separate IDs. `WHY_EXCLUDED` is required only for materially plausible excluded methods.

## 5. Baseline, population, and denominator controls

For baseline-dependent analysis record:

```text
baseline:
  type:
  period:
  rationale:
alternative_baseline_material: yes / no
```

For a material or decision-critical case, if a reasonable alternative baseline could materially change the conclusion, `robustness_to_baseline` is required, subject to its prerequisites.

For ratios, averages, rates, margins, productivity, conversion, mix, and analogous measures, record:

```text
population_constant_or_explained?:
denominator_constant_or_explained?:
scope_change_quantified?:
```

Check additions, removals, filter changes, entity changes, cut-off changes, and denominator-definition changes.

```text
ratio interpretation requires numerator + denominator + population
```

## 6. Preliminary evidence and explanation challenge

After deterministic findings and before explanation, record when the analysis is material or decision-critical:

```text
PRELIMINARY_EVIDENCE_CHECK

finding_supported: yes / partial / no
explanatory_analysis_feasible: yes / no
critical_evidence_gap:
next_step: continue / stop / collect evidence
```

If explanatory analysis is not feasible, stop, state the limitation, and do not fabricate an explanation.

For material and decision-critical cases ask:

1. What else could explain this?
2. What evidence contradicts the current explanation?
3. What test could materially change the conclusion?
4. What observable evidence distinguishes the leading explanations?

Runtime record:

```text
CURRENT_EXPLANATION:
COMPETING_EXPLANATIONS[]:
CONTRADICTING_EVIDENCE:
DISCRIMINATING_EVIDENCE:
FALSIFICATION_TEST:
TEST_RESULT:
RESIDUAL_UNCERTAINTY:
```

Claim ladder:

```text
OBSERVATION
→ CALCULATED EFFECT
→ DRIVER CANDIDATE
→ SUPPORTED EXPLANATION
→ ROOT CAUSE
```

```text
driver != root cause
correlation != causation
```

`ROOT CAUSE` is allowed only when the evidence and analytical design support causal language.

### Method disagreement

When materially relevant methods produce incompatible interpretations or conclusions:

```text
material method disagreement
→ record as contradictory evidence
→ preserve conflicting results
→ no silent LLM reconciliation
→ do not average incompatible conclusions
→ constrain maximum claim strength
→ escalate when the conflict remains material
```

Unresolved disagreement remains visible in `CONTRADICTING_EVIDENCE`, `RESIDUAL_UNCERTAINTY`, and `FINAL_EVIDENCE_SUFFICIENCY`.

## 7. Claim and evidence calibration

Preserve the existing confidence taxonomy:

```text
confidence: high / medium / low
```

Add independent dimensions:

```text
claim_support: SUPPORTED / PARTIALLY_SUPPORTED / HYPOTHESIS / UNSUPPORTED
causal_status: not_applicable / association_only / explanation_supported / causal_evidence
```

Invariant:

```text
confidence != claim_support != causal_status
```

For material and decision-critical final claims record:

```text
FINAL_EVIDENCE_SUFFICIENCY

sufficient_for:
- observation
- calculated_effect
- driver_candidate
- supported_explanation
- causal_claim

status: sufficient / partial / insufficient
missing_discriminating_evidence:
contradictory_evidence_remaining:
maximum_claim_strength:
```

```text
claim strength <= final evidence sufficiency
```

LLM confidence, management expectation, expert intuition, method count, and narrative fluency cannot strengthen a claim beyond the evidence.

The existing `CLAIM_EVIDENCE_REGISTRY_TEMPLATE.md` owns claim-level fields. Required lineage is:

```text
claim
→ method_execution_id
→ executed method
→ source mart / table / slice
→ metric / period / grain / filter / baseline
→ evidence
```

`formula_or_method` remains a human-readable description and does not replace `method_execution_id`. A claim that requires an actual method result cannot use an execution with status `blocked`, `planned`, or `not_needed` as supporting evidence.

## 8. Runtime collapse

P0 is one workflow with conditional depth, not two independent workflows.

Eligible compact path:

```text
routine + low uncertainty + no material trigger
→ QUESTION
→ INTENT
→ CORE / TRIGGERED METHOD
→ DETERMINISTIC RESULT
→ COMPACT QA
→ ANSWER
```

Full path:

```text
TASK PROFILE
→ METHOD PLAN
→ ANALYSIS
→ PRELIMINARY EVIDENCE CHECK
→ EXPLANATION CHALLENGE
→ CLAIM CALIBRATION
→ FINAL EVIDENCE SUFFICIENCY
→ FULL QA
```

Without a material trigger, do not instantiate an unnecessary full Explanation Challenge, competing-explanations structure, falsification structure, expanded claim-registry state, or full evidence-sufficiency record. `quick` retains the existing quick-mode artifact and context budget and does not become a full governance artifact by default.

## 9. Stop and escalation rules

Stop analytical deepening when:

- another method is unlikely to materially change finding, confidence, risk, recommendation, limitation, or evidence assurance;
- required discriminating evidence is unavailable;
- further precision exceeds data quality;
- the conclusion is robust to plausible uncertainty;
- the next unresolved question is strategic;
- added complexity provides no decision value.

Escalate through the existing routing and review path when:

- competing explanations remain materially plausible;
- material contradictory evidence remains unresolved;
- material method disagreement remains unresolved;
- the conclusion depends on an unsupported assumption;
- causal language is requested without causal evidence;
- required evidence lies outside Analytics ownership.

Preserve the decision boundary:

```text
[Analytics]: verified quantitative evidence
↓
[Thinking]: alternatives / trade-offs / risk appetite / decision
```

`thinking_handoff_possible = yes` identifies a possible boundary; it does not silently transfer ownership. `manual_review_required = yes` applies when the escalation materially affects the conclusion.

## P1 and P2 status

P1 is deferred. Do not create fake pilot evidence. Future work may evaluate 5–10 materially different pilot cases, golden and adversarial cases, method and robustness-trigger calibration, confidence-taxonomy migration, and candidate-intent promotion.

P2 is deferred. Do not implement expanded taxonomies, reusable pattern promotion, autonomous learning, automatic promotion or downgrade, or agentic analytical orchestration.
