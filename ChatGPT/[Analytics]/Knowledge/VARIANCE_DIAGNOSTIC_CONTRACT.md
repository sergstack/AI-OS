# Variance Diagnostic Contract

## Purpose and ownership

This file is the canonical `[Analytics]` runtime/output contract for material Plan/Fact and variance diagnostics. It is a thin extension of `ANALYTICAL_REASONING_STANDARD.md` and reuses the 22 methods owned by `ANALYTICAL_TECHNIQUES.md`; it creates no method, registry, framework, or independent workflow.

Apply the full contract only when `analytical_depth = material / decision_critical` or variance risk makes reconciliation, classification, or evidence controls material. Routine/quick cases collapse to the verified reported result, explicit direction rule, compact reconciliation/QA, and answer.

```text
reported result
→ normalized management variance
→ gross bridge
→ reconciled primary attribution
→ classification coverage
→ materiality
→ secondary management attributes
→ claim calibration
→ management synthesis
```

Deterministic calculations and classifications precede LLM narrative. The Writer receives verified, partial, hypothesis, or unknown fields; it does not calculate or infer them.

## 1. Variance sign convention

```text
VARIANCE_SIGN_CONVENTION

source_value:
source_formula:
source_sign_convention:

raw_variance:
raw_variance_formula:

economic_direction:
  higher_is: favorable / adverse / context_dependent

normalized_management_variance:
  amount:
  convention: positive = adverse; negative = favorable
  status: resolved / unresolved
```

```text
raw mathematical variance != management direction
```

- Expense: `Actual > Plan` is adverse when higher expense is adverse.
- Revenue: `Actual < Plan` is adverse when higher revenue is favorable.
- Preserve the native source/raw sign and formula for traceability.
- Use only normalized management direction inside a management bridge or attribution reconciliation.
- Never mix raw and normalized signs inside one bridge.
- `context_dependent` requires an explicit business rule. Without it, normalization status is `unresolved` and no normalized classification is published.
- Do not impose one universal `actual - plan` management formula across metrics.

## 2. Diagnostic runtime

```text
VARIANCE_DIAGNOSTIC

reported_result:
  plan:
  actual:
  source_variance:
  source_sign_convention:

normalized_result:
  normalized_management_variance:
  economic_direction_rule:
  normalization_status:

gross_bridge:
  gross_adverse:
  gross_favorable:
  net_management_variance:
  reconciliation_residual:
  reconciliation_status:

primary_attribution:
  economic_variance:
  timing_or_cutoff:
  data_or_mapping_effect:
  unresolved:
  reconciliation_residual:
  reconciliation_status:
```

The reported result remains canonical. The normalized result is a management-direction view, not a replacement for the source result.

### Gross bridge

For a material case disclose gross adverse movement, gross favorable movement, and normalized net management variance.

```text
gross adverse + gross favorable = normalized net management variance
```

Both use the normalized sign convention: adverse is positive and favorable is negative. If a material adverse driver exceeds the net adverse variance, the compensating favorable movement must be explicit.

Reuse `contribution_analysis`, `bridge_analysis`, `factor_reconciliation`, and `unexplained_residual` as applicable. Do not add a method.

### Primary attribution reconciliation

Primary attribution categories are mutually exclusive within one row/effect, collectively exhaustive within the declared scope, and deterministically reconciled.

```text
NET_ATTRIBUTION_RECONCILIATION

normalized_management_variance:
economic_effect:
timing_effect:
data_mapping_effect:
unresolved_effect:
reconciliation_residual:
status: pass / fail
```

```text
economic_effect
+ timing_effect
+ data_mapping_effect
+ unresolved_effect
= normalized_management_variance
```

If the residual is outside the declared deterministic tolerance, `status = fail`. The management narrative must then keep the residual visible and must not present attribution as complete.

## 3. Classification coverage

Net reconciliation and classification coverage answer different questions and must remain separate.

```text
ABSOLUTE_CLASSIFICATION_COVERAGE

population_basis: all_rows / material_rows / selected_rows
eligible_gross_movement:
classified_gross_movement:
unclassified_gross_movement:
coverage_pct:

row_count_total:
row_count_classified:
row_count_unknown:

classification_dimensions:
categories_mutually_exclusive: yes / no / not_applicable
```

Default deterministic definition:

```text
coverage_pct
= classified gross absolute movement
/ eligible gross absolute movement
```

Any alternative definition requires an explicit numerator, denominator, and population. A classification aggregate without declared population and coverage is not a complete explanation. Never use small net variance as the denominator for gross classification coverage.

## 4. Materiality and selection

Declare materiality before narrative generation; do not hardcode universal thresholds.

```text
MATERIALITY_CONTRACT

absolute_threshold:
relative_threshold:
zero_plan_rule:

top_contribution_rule:
  contribution_basis: gross_adverse / gross_favorable / gross_absolute
  threshold:

qualitative_override:
selected_population:
excluded_population:
selection_coverage:
```

An item may be material when it passes a declared absolute threshold; passes a declared relative threshold with a meaningful denominator; has actual activity with zero plan under the declared rule; belongs to contributors covering a declared share of gross movement; or satisfies a declared qualitative control/compliance/risk trigger. Every run identifies the basis, denominator, population, and exclusions.

## 5. Secondary management attributes

Secondary attributes describe different analytical dimensions and remain outside the additive bridge.

```text
budget_status: planned / underplanned / unbudgeted / unknown
controllability: controllable / partially_controllable / non_controllable / unknown
recurrence: recurring / one_off / unknown
evidence_status: supported / partial / hypothesis / unknown
```

A row may simultaneously be `economic_variance + unbudgeted + controllable + one_off`; only the primary effect participates in additive attribution. Secondary attributes must never be summed as independent causes of normalized variance.

### Controllability

```text
CONTROLLABILITY_CLASSIFICATION

classification: controllable / partially_controllable / non_controllable / unknown
approved_rule_or_business_definition:
evidence_source:
classification_basis:
review_status:
```

Insufficient business/evidence basis means `controllability = unknown`. Amount, zero-plan status, budget ownership, management ownership, and driver status do not establish controllability. Valid evidence may include approved policy, contract terms, tax/regulatory nature, process rules, delegation/authority rules, or another traceable approved business definition.

### Recurrence and generalization

```text
RECURRENCE_CLASSIFICATION

classification: recurring / one_off / unknown
recurrence_basis: historical_pattern / contractual_schedule / confirmed_event_specific / process_rule / other_verified_basis
evidence_source:
```

One observation alone establishes neither `recurring` nor `one_off` unless independent event-specific evidence supports it. Otherwise use `unknown`.

```text
single-period evidence != systemic / non-systemic evidence
```

Claims such as `systemic`, `non-systemic`, `structural`, `persistent`, `recurring`, `isolated`, or `one-off` require explicit generalization evidence such as comparable multi-period history, process/control evidence, contractual recurrence, or confirmed event-specific evidence. One period may support only period-bounded concentration language.

### Accountability boundary

```text
driver/effect != controllability != accountability
management_owner != responsible_for_cause
```

Do not infer responsibility, mismanagement, budget violation, or control failure solely from amount, ownership, zero-plan status, or driver status. Accountability claims require separate criteria and evidence.

## 6. Reported and adjusted views

```text
REPORTED_VIEW

official_plan:
official_actual:
official_variance:
source_sign_convention:
normalized_management_variance:
```

```text
ADJUSTED_MANAGEMENT_VIEW

adjustment_id:
adjustment_amount:
adjustment_direction: increases_adverse / reduces_adverse
adjustment_type:
reason:
evidence:
expected_reversal_or_normalization:
approved_rule:
included_in_adjusted_view:
```

```text
reported_management_variance
+ adverse_increasing_adjustments
- adverse_reducing_adjustments
= adjusted_management_variance
```

The adjusted view is supplementary and never replaces the reported result. No silent exclusion or ambiguous unsigned adjustment polarity is allowed.

## 7. CFO / management synthesis

For material Plan/Fact analysis, compress the verified diagnostic in this semantic order:

1. reported result;
2. normalized management effect;
3. primary driver/effect at supported claim strength;
4. gross favorable/adverse offset and net bridge;
5. economic, timing, data/mapping, and unresolved attribution;
6. budget quality;
7. controllability;
8. classification coverage and unknown population;
9. what is supported;
10. what is not established;
11. action or next discriminating evidence.

This is a semantic contract, not a mandatory verbose template. Show the smallest sufficient management synthesis and keep the supporting diagnostic in the evidence layer. Routine cases must not instantiate the full structure.

Management synthesis cannot create analytical evidence. A driver remains below root-cause level unless causal evidence permits escalation. Controllability, recurrence, systemic status, and accountability remain `unknown` or `not established` when their evidence contracts are unmet.

## 8. Claim, method, QA, and stop gates

Claims trace through the existing `CLAIM_EVIDENCE_REGISTRY_TEMPLATE.md`. Use its generalization fields when language extends beyond the observed period/scope.

```text
claim strength <= final evidence sufficiency
driver != root cause
reported result != adjusted management view
net attribution reconciliation != absolute classification coverage
```

Stop or constrain publication when sign normalization is unresolved; the gross or attribution bridge fails; coverage population/denominator is missing; materiality basis is absent; adjusted polarity is ambiguous; or a secondary/generalized claim lacks required evidence.
