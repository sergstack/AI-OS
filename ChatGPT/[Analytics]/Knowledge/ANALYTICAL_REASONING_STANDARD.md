# Analytical Reasoning Standard — P0

## Purpose and boundary

This standard adds a bounded reasoning-control layer to the existing `[Analytics]` workflow. It does not replace or redefine the Data Contract, RAW, `stage_main_full`, `mart_main_full`, `mart_main_tz` / `mart_main_compact`, deterministic calculations, chart sourcing, memo pipeline, QA / Judge, acceptance, or Codex handoff boundary.

Execution remains governed by the canonical repo-root `docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md`. `docs/autonomous_execution/extensions/ANALYTICS_EXTENSION.md` remains authoritative for Analytics-specific AES requirements. This standard structures analytical reasoning and method selection only; it does not fork, weaken, or duplicate AES execution states, corrective-loop limits, stop conditions, rollback, acceptance, or external-action authority.

New AES execution records use the canonical v2 contract and its required
Closure Review. Historical v1 records remain read-only evidence, not a path
for new successful Analytics work.

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

### Material Plan/Fact and variance diagnostics

`VARIANCE_DIAGNOSTIC_CONTRACT.md` owns the bounded runtime/output controls for material Plan/Fact cases: source-sign preservation, explicit management-direction normalization, gross bridge, reconciled primary attribution, separate gross classification coverage, declared materiality, evidence-constrained secondary attributes, reported-versus-adjusted views, and CFO synthesis order.

It reuses the existing `diagnose_variance` mapping and approved methods. It does not add an intent, method, registry, or workflow. Activate the full diagnostic only for material/decision-critical cases or a material variance risk; routine/quick cases keep the compact path.

```text
raw/source variance != normalized management direction
net attribution reconciliation != absolute classification coverage
primary attribution is additive; secondary management attributes are not
driver/effect != controllability != accountability
single-period evidence != systemic / non-systemic evidence
reported result != adjusted management view
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

Discriminating alternative-explanation evidence (competing explanations tested and narrowed, per §6's `EXPLANATION CHALLENGE`) may promote a claim to `SUPPORTED EXPLANATION`; it does not by itself reach `ROOT CAUSE`. Promotion to `ROOT CAUSE` additionally requires causal evidence or a causal-capable analytical design (`causal_status: causal_evidence`) — for example a controlled comparison, natural experiment, or a registry method able to isolate cause from association. Absent that, the maximum claim strength stops at `SUPPORTED EXPLANATION` / driver candidate, even when alternative explanations have been ruled out.

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

## 8. Analytical Judge gate

An explicit, bounded orchestration checkpoint that runs **after deterministic findings and before narrative packaging** (memo / report). It challenges the analytical conclusion itself. It does not add a QA framework, taxonomy, method, intent, or execution state: it reads the controls already defined in §4–§7 and the existing Analytics QA, and returns one visible result.

```text
deterministic calculation
→ findings
→ ANALYTICAL JUDGE
→ pass / revise / blocked
→ revise or rerun when required
→ final findings
→ memo / report
→ existing Memo QA / Judge
→ acceptance
```

### Seven checks (semantic, over existing controls — no new definitions)

| # | Judge check | Reads |
|---|---|---|
| 1 | Question fit — did the analysis answer the declared business question and scope? | `TASK_PROFILE.question`, active intent classification (§1–§2), `expected_output` |
| 2 | Method adequacy — were the selected methods sufficient, and was every supporting method actually executed with prerequisites met? | `METHOD_PLAN` (`status`, `prerequisites_met`, `execution_status`), the registry and triggers in `ANALYTICAL_TECHNIQUES.md`, `blocked != executed` (§4) |
| 3 | Evidence lineage — can every headline conclusion be traced executed method → source mart / table / slice → metric → period → grain → filter / baseline → evidence? | the lineage in §7 and `CLAIM_EVIDENCE_REGISTRY_TEMPLATE.md` |
| 4 | Alternative explanations — is a materially plausible alternative untested or not kept visible? | `COMPETING_EXPLANATIONS[]`, `DISCRIMINATING_EVIDENCE`, `FALSIFICATION_TEST` (§6) |
| 5 | Contradicting evidence — does evidence or method disagreement materially weaken the conclusion? | `CONTRADICTING_EVIDENCE`, `RESIDUAL_UNCERTAINTY`, the method-disagreement rule (§6) |
| 6 | Claim calibration — is any conclusion stronger than `FINAL_EVIDENCE_SUFFICIENCY` (driver → root cause, association → causation, single-period → systemic)? | claim ladder, `claim_support`, `causal_status`, `FINAL_EVIDENCE_SUFFICIENCY`, `claim strength <= final evidence sufficiency` (§7); `VARIANCE_DIAGNOSTIC_CONTRACT.md` for material Plan/Fact |
| 7 | Decision proportionality — does any recommendation, risk statement, or management implication exceed the verified evidence? | the material management synthesis rule (`ANALYTICS_WORKFLOW.md` Step 11) and its acceptance criteria |

The Judge introduces no competing definition for any concept it reads. It reuses `PRELIMINARY_EVIDENCE_CHECK`, the explanation-challenge record, `FINAL_EVIDENCE_SUFFICIENCY`, `CLAIM_EVIDENCE_REGISTRY_TEMPLATE.md`, Analysis QA, and the material variance diagnostic QA where applicable.

### Output

```text
ANALYTICAL_JUDGE
status: pass / revise / blocked
failed_checks:
material_findings:
required_action:
rerun_required: yes / no
manual_review_required: yes / no
maximum_claim_strength:
```

- **pass** — every material conclusion is supported at its stated claim strength; no material unresolved contradiction or missing analytical check remains.
- **revise** — the conclusion or its wording can be corrected from existing evidence, or a bounded additional deterministic check / rerun is available.
- **blocked** — a required prerequisite, reconciliation, grain, validation path, or discriminating evidence is unavailable; the final management conclusion must not be published.

`maximum_claim_strength` cannot exceed `FINAL_EVIDENCE_SUFFICIENCY.maximum_claim_strength`. `manual_review_required` is the value set by §1; the Judge surfaces it and does not redefine it.

### Bounded revise / rerun

Allowed:

```text
Judge finding
→ one explicit bounded correction or deterministic rerun
→ Judge re-check
```

Forbidden: silent self-retry; unrestricted iterative analysis; adding a method without registry / trigger support; reasoning around a missing deterministic prerequisite; treating a `blocked` method as evidence. Correction count, stop conditions, and rollback remain those of the canonical `docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md` and the `[Codex]` one-fix limit where applicable; this gate does not widen them.

### Runtime collapse

`routine` + low uncertainty + no material trigger: collapse the Judge to the existing compact QA note on the compact path (Runtime collapse, §9). Do not instantiate the seven-question `ANALYTICAL_JUDGE` record.

`material` / `decision_critical`: the explicit gate is mandatory. A recorded `ANALYTICAL_JUDGE` with `status: pass` — or a `revise` resolved by one bounded correction and a passing re-check — is required before final findings are handed to memo / report generation. A `blocked` status stops publication of the final management conclusion.

## 9. Runtime collapse

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
→ ANALYTICAL JUDGE (pass / revise / blocked) → FINAL FINDINGS
→ FULL QA
```

Without a material trigger, do not instantiate an unnecessary full Explanation Challenge, competing-explanations structure, falsification structure, expanded claim-registry state, full evidence-sufficiency record, or the seven-question `ANALYTICAL_JUDGE` record. `quick` retains the existing quick-mode artifact and context budget and does not become a full governance artifact by default.

## 10. Stop and escalation rules

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

## 11. Metric semantics gate

A formula alone is not a sufficient metric definition. For material,
flagship, or ratio-like metrics, use
`../Templates/METRIC_DEFINITION_CARD_TEMPLATE.md` (`METRIC_DEFINITION_CARD`)
to fix numerator, denominator, aggregation semantics, population,
units/currency, sign/direction, zero-denominator behavior, allowed
comparison scope, and forbidden interpretations before a material
conclusion. `METRIC_DEFINITION_CARD.status: provisional / blocked`, or a
required field left undefined, still permits reporting the underlying
`DATA FACT` / `CALCULATION RESULT` with an explicit limitation attached; it
blocks a strong `INTERPRETATION` / `RECOMMENDATION` or flagship management
conclusion built on that metric. The interpretive layer is limited to
`HYPOTHESIS` / `LIMITATION` at most until the card reaches
`status: approved`. This gate does not add a metric to the 22-method
registry and does not redefine any business metric; it fixes the
definition-card mechanism only.

## 12. Canonical `VALUE_STATE` and claim strength

`DATA_CONTRACTS.md` owns the canonical `VALUE_STATE` vocabulary (`KNOWN`,
`UNKNOWN`, `NOT_REPORTED`, `NOT_APPLICABLE`, `PARSE_FAILED`,
`MISSING_SOURCE`, `UNMATCHED`, `BLOCKED`) and its invariants (`UNKNOWN != 0`,
`UNKNOWN != NOT_REPORTED`, `PARSE_FAILED != MISSING_SOURCE`,
`NOT_APPLICABLE != FALSE`). `RAW -> STAGE -> MART` must not collapse
materially different states into one generic null when that could change
denominator, population, reconciliation, classification coverage, metric
result, claim strength, or management conclusion.

```text
unresolved material uncertainty coverage -> claim_support <= PARTIALLY_SUPPORTED
```

A claim built on a mart where a material share of the relevant population
carries `UNKNOWN`, `PARSE_FAILED`, `MISSING_SOURCE`, or `UNMATCHED` cannot be
recorded as `SUPPORTED` with `confidence: high` unless the uncertainty
coverage is itself declared and quantified, and that quantification
demonstrably does not change the conclusion. Once resolved this way, the
uncertainty is no longer "unresolved" and the `<= PARTIALLY_SUPPORTED` cap
does not apply.

## 13. Mandatory Headline Claim Gate

For `analytical_depth = material / decision_critical`, every headline claim
requires a `CLAIM_EVIDENCE_REGISTRY_TEMPLATE.md` row with complete lineage:

```text
headline claim
-> claim registry row
-> method_execution_id
-> execution_status = executed
-> source mart/table/slice
-> metric/period/grain/filter/baseline
-> evidence_id
-> claim_support
-> causal_status
-> confidence
-> generalization_scope
-> qa_status
```

```text
lineage missing -> allowed_in_executive = no
```

This restates and enforces, at the headline-claim level, rules already
present in §4 (`blocked != executed`), §6 (claim ladder,
`driver != root cause`), and §7 (`claim strength <= final evidence
sufficiency`); it adds no new taxonomy. `manual_review_required` (§1) and the
Analytical Judge (§8, check 3 and 6) read this gate; they do not duplicate
it.

## 14. Three control gates

`[Analytics]` separates three gates. They are already implemented by
existing mechanics; this section names them so they are not conflated.

```text
GATE 1 - DATA / CALCULATION
Are the data, formulas, units, grain, and reconciliation correct?
Owned by: Data Contract, stage/mart QA, Contract QA, Calculation QA.

GATE 2 - ANALYTICAL CLAIM
What does the executed evidence permit asserting?
Owned by: METHOD_PLAN, PRELIMINARY_EVIDENCE_CHECK, claim ladder,
FINAL_EVIDENCE_SUFFICIENCY, CLAIM_EVIDENCE_REGISTRY, Analytical Judge (§8).

GATE 3 - NARRATIVE
Is the memo/executive wording no stronger than the verified claim?
Owned by: MEMO_PIPELINE.md, MEMO_RUBRIC.md, and the canonical [LLM] memo
Judge/QA gate.
```

Invariant:

```text
DATA VALID != CLAIM SUPPORTED != NARRATIVE ACCEPTABLE
```

Passing Gate 1 does not authorize a claim; passing Gate 2 does not authorize
narrative wording stronger than `maximum_claim_strength`. The Analytical
Judge remains the post-findings Gate 2 checkpoint; Memo QA / the `[LLM]`
Judge remains the Gate 3 checkpoint. Neither gate is redefined or
duplicated by this section.

## 15. P1 extension points (design only, not implemented in this version)

The following are forward-compatible placeholders only. They are not wired
into any active gate, QA check, or acceptance criterion in this version.

- `POPULATION_CONTRACT` - future population/denominator comparability detail
  for ratio/rate/share/average/margin/conversion/productivity/frequency
  metrics (`population_definition`, `numerator_population`,
  `denominator_population`, `period`, `grain`, `filters`, `exclusions`,
  `population_changed_vs_baseline`, `denominator_changed_vs_baseline`,
  `scope_change_amount`, `scope_change_pct`, `interpretation_allowed`). See
  `../Templates/METRIC_DEFINITION_CARD_TEMPLATE.md`. P1, not active in this
  version; §5's `population_constant_or_explained?` /
  `denominator_constant_or_explained?` / `scope_change_quantified?` remain
  the active controls.
- `RECONCILIATION_CONTRACT` - a future contract distinguishing total
  reconciliation, row-count reconciliation, matched population,
  only-left/only-right population, amount reconciliation, classification
  coverage, and residual/tolerance, so that an aggregate total match is not
  read as population integrity. P1, not active in this version; existing
  RAW/STAGE/MART reconciliation and unmatched-row QA remain the active
  controls.
- `ANALYSIS_CONTINUATION_GATE` - a future control on whether to continue,
  stop, block, or hand off further analysis
  (`current_question_answered`, `current_claim_strength`,
  `remaining_uncertainty`, `material_unresolved_question`,
  `next_method_candidate`, `what_can_it_change`,
  `required_evidence_available`, `expected_decision_value`,
  `decision: CONTINUE / STOP / BLOCK / HANDOFF`). P1, not active in this
  version; §10 stop/escalation rules remain the active controls. This is not
  an autonomous loop and must not be implemented as one.

## P1 and P2 status

P1 is deferred. Do not create fake pilot evidence. Future work may evaluate 5–10 materially different pilot cases, golden and adversarial cases, method and robustness-trigger calibration, confidence-taxonomy migration, and candidate-intent promotion.

P2 is deferred. Do not implement expanded taxonomies, reusable pattern promotion, autonomous learning, automatic promotion or downgrade, or agentic analytical orchestration.
