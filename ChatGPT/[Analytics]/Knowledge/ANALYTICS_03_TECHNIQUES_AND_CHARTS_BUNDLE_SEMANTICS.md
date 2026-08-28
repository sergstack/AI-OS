# Migrated Bundle Semantics

Canonical source created during Issue #285 provenance migration.
Legacy bundle provenance: `ChatGPT/[Analytics]/Knowledge_Bundles/ANALYTICS_03_TECHNIQUES_AND_CHARTS.md`.

## Legacy section: `ChatGPT/[Analytics]/Knowledge/ANALYTICAL_TECHNIQUES.md`

Registry is the source of truth for eligibility; registration is not execution. Each method records `METHOD_ID`, name, purpose, role, requirements, input grain, required metrics, output, execution owner/mode, validation owner, limitation, and failure mode. Mixed execution also records deterministic and reasoning components.
For P0, `NAME` is the stable registry label represented by `METHOD_ID`; display formatting cannot change identity.
`P0 METHOD COUNT = 22`. Capability groups (`DECOMPOSE`, `LOCATE`, `VALIDATE`, `CHALLENGE`, `FORWARD`) are readability aids only, not runtime taxonomy or routing.
Material Plan/Fact uses `VARIANCE_DIAGNOSTIC_CONTRACT.md` to configure existing methods. `variance_analysis` preserves raw/source formula and normalizes management direction from an explicit KPI rule; contribution exposes gross movement and coverage; bridge/factor reconciliation use one normalized sign; residual keeps incomplete attribution visible. Controllability, recurrence, budget status, materiality, coverage, and accountability are controls/attributes, not methods.
| METHOD_ID | Role / mode | Purpose and required boundary |
| `variance_analysis` | analytical / deterministic | Comparable actual/baseline at aligned grain → variance. |
| `contribution_analysis` | analytical / deterministic | Reconciled additive components → ranked contribution. |
| `bridge_analysis` | analytical / deterministic | Non-overlapping start/end movements → bridge. |
| `driver_decomposition` | analytical / mixed | Deterministic decomposition plus bounded interpretation → driver candidates/residual, not causal proof. |
| `mix_analysis` | analytical / deterministic | Stable categories/weights → mix effect. |
| `segmentation` | analytical / deterministic | Valid groups and sufficient observations → segment comparison. |
| `trend_analysis` | analytical / deterministic | Comparable ordered periods → trend/inflection evidence. |
| `cohort_analysis` | analytical / deterministic | Common anchor/windows → cohort comparison. |
| `anomaly_analysis` | validation / deterministic | Explicit expected range/distribution → unusual-observation candidates. |
| `exception_analysis` | validation / mixed | Approved rule/control and declared population → explicit violation candidates; never infer a missing rule. |
| `unmatched_elements_analysis` | validation / deterministic | Comparable populations and approved match rule → concrete one-sided/matched elements. |
| `reconciliation` | validation / deterministic | Comparable totals/keys → match/mismatch. |
| `factor_reconciliation` | validation / deterministic | Observed delta and executed factor effects → completeness gap/status. |
| `unexplained_residual` | validation / deterministic | Reconciled total/components → residual. |
| `data_layer_check` | validation / deterministic | Traceable `REPORT → MART → STAGE → RAW` lineage → first-appearance layer. |
| `timing_validation` | validation / mixed | Approved dates/cut-off definition → quantified timing/cross-period effect. |
| `alternative_explanation_test` | mixed / mixed | Deterministic discriminating tests plus bounded comparison → supported/rejected/unresolved explanations. |
| `robustness_to_baseline` | validation / deterministic | Defensible comparable baselines → conclusion stability. |
| `subgroup_robustness` | validation / deterministic | Sufficient material subgroups → stable/heterogeneous result. |
| `sensitivity_analysis` | validation / deterministic | Explicit plausible assumption range and model → range/breakpoints. |
| `forecast_to_period_end` | analytical / deterministic | Defined cut-off/method and adequate history → forecast with limitations. |
| `leading_indicator_analysis` | analytical / mixed | Defined target/precursor, temporal ordering and evidence basis → leading signal/association/risk, not causal prediction. |
Capability distinctions:
| `validate_data` | reconciliation, data-layer | anomaly, exception, unmatched, timing, segmentation, subgroup robustness | — |
| `diagnose_variance` | variance, contribution, unexplained residual, factor reconciliation | bridge, mix, unmatched, segmentation, trend, timing | baseline robustness |
| `explain_drivers` | driver decomposition, unexplained residual, factor reconciliation | alternative test, segmentation, trend, timing, data-layer | baseline robustness, sensitivity |
| `test_explanation` | alternative explanation test | baseline/subgroup robustness, sensitivity, timing, data-layer | cohort |
| `project_forward` | forecast to period end | sensitivity, leading indicator | trend, baseline robustness |
Every non-CORE selection requires `trigger_type`, a concrete `trigger_rule`, `trigger_evidence_required`, and deterministic mapping-level `priority`. Priority is non-numeric: CORE first; deterministic triggers before judgment/hybrid triggers; OPTIONAL last. Missing evidence cannot silently activate a method; a plausible omission is recorded for QA. Minimum sufficient set: include only methods capable of materially changing finding, confidence, risk, recommendation, limitation, or evidence assurance.
Trigger rules by intent:
- `validate_data`: reconciliation and data-layer are CORE; exception requires approved rule/population/fields/scope; unmatched requires comparable populations and approved match rule; timing requires dates/boundary/approved definition and material cut-off candidate.
- `diagnose_variance`: factor reconciliation is CORE; unmatched activates when additions/removals may explain variance; timing activates when cut-off may explain variance.
- `explain_drivers`: factor reconciliation is CORE; timing or data-layer activates when the candidate driver may reflect cut-off or transformation.
- `test_explanation`: timing/data-layer only when either is a materially plausible competing explanation.
- `project_forward`: leading indicator only when a defined precursor/target, temporal ordering, relevant history, and evidence basis can materially change outlook interpretation.
Every new non-CORE method uses the existing `trigger_type`, `trigger_rule`, `trigger_evidence_required`, `trigger_evidence`, and `priority` contract and the existing prerequisite gate.
- “Почему отклонение?” → `diagnose_variance`; add `explain_drivers` only for an explanatory question with prerequisites.
`driver_decomposition` produces driver candidates, not root cause.

## Legacy section: `ChatGPT/[Analytics]/Knowledge/ANALYTICAL_REASONING_STANDARD.md`

## Boundary and flow
This is a bounded reasoning-control extension; it does not replace Data Contract, RAW, STAGE, MART, deterministic calculations, chart sourcing, memo, QA/Judge, acceptance, or handoff. `mart_main_full` remains evidence/reuse; compact marts remain management-facing.
Execution remains governed by repo-root `docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md`; `docs/autonomous_execution/extensions/ANALYTICS_EXTENSION.md` remains authoritative for Analytics-specific AES requirements. Reasoning control structures method selection only; it does not fork AES states, correction limits, stop/rollback/acceptance, or external authority. It is not an autonomous agent or an independent retry/self-improvement loop. Closure Review uses existing Data/Analysis/Output Judge, reconciliation, unsupported-conclusion, and artifact-freshness controls; the Analytics extension remains authoritative for domain detail.
LLM reasoning != deterministic execution
TASK PROFILE → INTENT → deterministic-first minimum methods → prerequisite gate
→ existing execution → preliminary evidence → explanation challenge when material
→ claim calibration → final evidence sufficiency → existing QA/Judge
LLM may classify ambiguous intent and bounded judgment/hybrid triggers, challenge explanations, and calibrate wording. It cannot replace deterministic arithmetic, formulas, reconciliation, variance/driver/exposure calculations, classification, or a deterministically executable forecast. Missing prerequisites cannot be reasoned away.
## Task profile
question; decision_user
evidence_state_basis
expected_output
No numerical scoring. Analytical depth and output mode are independent. Routine → minimal; material → standard; decision-critical → enhanced plus robustness consideration and explicit evidence sufficiency.
Set `robustness_required = yes` only when a declared baseline, subgroup, or sensitivity trigger is satisfied. Set `thinking_handoff_possible = yes` only when the unresolved question crosses into alternatives, trade-offs, risk appetite, or decision.
Set `manual_review_required = yes` for causal/root-cause final language, unresolved material contradictory evidence, decision-critical weak/partial evidence, material judgment/hybrid influence, or required `[Thinking]` escalation. Record review owner/status/resolution before publication.
P0 active intents: `validate_data`, `diagnose_variance`, `explain_drivers`, `test_explanation`, `project_forward`. Deferred candidates: `locate_concentration`, `detect_anomalies`, `analyze_structure`, `analyze_trend`, `prepare_decision_evidence`, `evaluate_control`.
Canonical P0 registry contains exactly 22 methods, including `exception_analysis`, `unmatched_elements_analysis`, `factor_reconciliation`, `timing_validation`, `data_layer_check`, and `leading_indicator_analysis`. Controls remain controls; numerator/denominator/population, contradiction/discrimination/falsification, claim ladder, and stop conditions do not become methods. Trade-offs, premortem, reversibility, risk appetite, choice, and decision remain in `[Thinking]`. Expansion beyond 22 requires P1/pilot evidence or separate acceptance.
## Method plan and prerequisites
method; intent; status: CORE / TRIGGERED / OPTIONAL
why_selected; question_answered
trigger; trigger_type; trigger_rule; trigger_evidence_required; trigger_evidence; priority
execution_owner; execution_mode
missing_requirement; method_execution_id
`yes` means all requirements satisfied; `no` means a real requirement is unmet; `not_applicable` means no such requirement exists and cannot bypass one. `blocked != executed`; blocked is not evidence. Each period/grain/filter/baseline/population/scenario application needs a distinct `method_execution_id`. Explain exclusion only for materially plausible methods.
## Baseline and ratio controls
Record baseline type/period/rationale and whether an alternative is material. For material/decision-critical cases, a reasonable alternative capable of changing the conclusion requires `robustness_to_baseline`. Ratios require numerator + denominator + population; explain population/denominator and quantify additions, removals, filters, entities, cut-offs, and definition changes.
## Material Plan/Fact controls
`VARIANCE_DIAGNOSTIC_CONTRACT.md` owns source-sign preservation, management-direction normalization, gross bridge, primary attribution, gross coverage, declared materiality, evidence-constrained secondary attributes, reported/adjusted separation, and CFO synthesis order. It adds no intent, method, registry, or workflow; full diagnostics activate only for material/decision-critical cases or material variance risk.
primary attribution is additive; secondary attributes are not
## Explanation challenge
Preliminary check records finding support (`yes / partial / no`), explanatory feasibility, critical gap, and next step (`continue / stop / collect evidence`). If infeasible: stop, state limitation, do not fabricate.
Material/decision-critical cases record current and competing explanations, contradicting and discriminating evidence, falsification test/result, and residual uncertainty. Ask what else explains the finding, what contradicts it, what test changes it, and what evidence distinguishes explanations.
OBSERVATION → CALCULATED EFFECT → DRIVER CANDIDATE → SUPPORTED EXPLANATION → ROOT CAUSE
Material method disagreement remains contradictory evidence; preserve conflict, do not silently reconcile or average incompatible conclusions, constrain claim strength, and escalate if unresolved/material.
## Claim calibration
Preserve `confidence: high / medium / low`. Add independent `claim_support: SUPPORTED / PARTIALLY_SUPPORTED / HYPOTHESIS / UNSUPPORTED` and `causal_status: not_applicable / association_only / explanation_supported / causal_evidence`.
For material/decision-critical claims, `FINAL_EVIDENCE_SUFFICIENCY` states what is sufficient for observation, calculated effect, driver candidate, supported explanation, and causal claim; status; missing discriminating evidence; remaining contradictions; maximum claim strength. LLM confidence, expectations, intuition, method count, and fluency cannot strengthen evidence.
Lineage: claim → `method_execution_id` → executed method → source mart/table/slice → metric/period/grain/filter/baseline → evidence. Blocked/planned/not-needed executions cannot support claims requiring results.
## Runtime, stop, escalation
Routine + low uncertainty + no material trigger uses question → intent → core/triggered method → deterministic result → compact QA → answer. Do not instantiate full challenge, competing explanations, falsification, expanded registry, or evidence-sufficiency records without a trigger; preserve quick-mode budget.
Stop when added methods cannot materially change the outcome, discriminating evidence is unavailable, precision exceeds data quality, conclusion is robust, the remaining question is strategic, or complexity adds no decision value. Escalate for materially plausible competing explanations, unresolved contradictory/method conflict, unsupported assumptions, causal language without causal evidence, or evidence outside Analytics ownership. `[Analytics]` owns verified evidence; `[Thinking]` owns alternatives/trade-offs/risk appetite/decision.
P1 pilot calibration and P2 expanded/autonomous taxonomies remain deferred; do not claim them implemented.

## Legacy section: `ChatGPT/[Analytics]/Knowledge/VARIANCE_DIAGNOSTIC_CONTRACT.md`

## Boundary and activation
Canonical material Plan/Fact runtime/output contract; thin extension of the existing reasoning standard and 22-method registry. Full structure activates only for material/decision-critical cases or material variance risk; routine/quick cases collapse to verified result, direction rule, compact reconciliation/QA, and answer. Deterministic calculation/classification precedes LLM narrative.
## Sign and reported result
Record source value/formula/sign, raw variance, explicit `higher_is: favorable / adverse / context_dependent`, and normalized management variance where positive is adverse and negative favorable. Raw math is not management direction. Preserve native source sign; use one normalized sign inside management bridges. Context-dependent KPI without an approved business rule remains unresolved. Reported result stays canonical.
## Gross bridge and primary attribution
Material cases show gross adverse, gross favorable, normalized net, residual, and status. A driver above net requires explicit favorable offset. Reuse contribution, bridge, factor reconciliation, and residual methods.
Primary `economic + timing + data/mapping + unresolved` effects are non-overlapping within a row, exhaustive within scope, and reconcile to normalized net variance. Failed residual remains visible and blocks a complete-explanation narrative.
## Coverage and materiality
Net attribution reconciliation is separate from absolute classification coverage. Coverage declares population, eligible/classified/unclassified gross absolute movement, row counts, dimensions, and exclusivity. Default denominator is eligible gross absolute movement, never small net variance.
Materiality declares absolute/relative thresholds, meaningful denominator, zero-plan rule, gross contribution basis/threshold, qualitative override, selected/excluded population, and selection coverage. No universal threshold.
## Secondary attributes and evidence
Budget status, controllability, recurrence, and evidence status are non-additive attributes. Amount, zero-plan/driver/owner status does not prove controllability or accountability. Insufficient approved business evidence means controllability `unknown`. One observation does not prove recurring/one-off; single-period evidence does not prove systemic/non-systemic. Generalization requires traceable multi-period, process/control, contractual, or event-specific evidence.
## Adjusted view and synthesis
Adjusted management view is supplementary: explicit adjustment ID, amount, `increases_adverse / reduces_adverse` polarity, type, reason, evidence, normalization/reversal, approved rule, and inclusion. It reconciles from reported management variance and never replaces reported Plan/Fact.
CFO synthesis order: reported result; normalized effect; supported driver; gross offset/bridge; primary nature; budget quality; controllability; coverage/unknown; supported; not established; action/next evidence. This is semantic order, not a verbose mandatory template. Claim strength stays within evidence; driver stays below root cause.
