# Migrated Bundle Semantics

Canonical source created during Issue #285 provenance migration.
Legacy bundle provenance: `ChatGPT/[Analytics]/Knowledge_Bundles/ANALYTICS_05_QA_GOVERNANCE_ROUTING.md`.

## Legacy section: `ChatGPT/[Analytics]/Knowledge/QA_CHECKLIST.md`

- [ ] Method selection adequate; no material omission or method bloat.
- [ ] Registry mapping followed; deterministic trigger, trigger priority, and trigger contract/evidence checked; no silent LLM override.
- [ ] Selected prerequisites met; reasoning did not replace a deterministic claim.
- [ ] Claim lineage is complete and references an executed method.
- [ ] Baseline explicit; required baseline robustness assessed.
- [ ] Population/denominator explained and scope change quantified.
- [ ] Preliminary evidence sufficient to continue.
- [ ] Alternative explanation, contradicting/discriminating evidence, and material falsification test assessed.
- [ ] Material method disagreement recorded and unresolved conflict constrains claim strength.
- [ ] Claim support, causal status, and confidence are not confused.
- [ ] `manual_review_required` correctly set; when `yes`, review owner/status/resolution recorded before publication.
- [ ] Final evidence sufficient for the claim; conclusion is not stronger than evidence.
- [ ] Stop/escalation assessed; routine collapse applied; no unnecessary full reasoning record.
- [ ] Exception and anomaly distinguished.
- [ ] Unmatched analysis used when population mismatch is material.
- [ ] Factor decomposition reconciled when applicable.
- [ ] Timing/cut-off checked when material.
- [ ] Data-layer artifact considered when material.
- [ ] Leading-indicator relationship supported and not presented as causal without evidence.
- [ ] New-method trigger contract and prerequisites satisfied.
- [ ] New method added only for a distinct capability.
- [ ] AES remains canonical execution governance; the Analytics extension is applied without duplication.
- [ ] Reasoning control is not treated as an autonomous execution or independent retry loop.
Use `ANALYTICAL_REASONING_STANDARD.md` for field semantics. This extends existing Analysis QA and creates no separate QA framework.
Use `VARIANCE_DIAGNOSTIC_CONTRACT.md` only for material/decision-critical Plan/Fact or material variance risk:
- [ ] Raw/source and normalized management signs are explicit/non-mixed; unresolved direction blocks normalization.
- [ ] Gross adverse/favorable and net reconcile; primary economic/timing/data-mapping/unresolved effects are non-overlapping and scope-complete.
- [ ] Coverage declares gross population/denominator, classified/unclassified movement and row counts separately from net reconciliation.
- [ ] Materiality basis, denominator, selected/excluded population, and selection coverage precede narrative.
- [ ] Secondary attributes are non-additive; unsupported controllability/recurrence remain unknown.
- [ ] Single-period evidence is not systemic/non-systemic; driver/owner does not imply root cause/accountability.
- [ ] Reported result remains canonical; adjusted view reconciles with explicit polarity.

## Legacy section: `ChatGPT/[Analytics]/Knowledge/ACCEPTANCE_CRITERIA.md`

- workbook may be large, but must include README / index, compact front sheet, data dictionary, field groups and evidence appendix.
For `VARIANCE_DIAGNOSTIC_CONTRACT.md` cases:
- reported/raw and normalized views are traceable and signs are explicit/non-mixed;
- gross/net bridge and primary attribution reconcile deterministically;
- gross coverage declares population, denominator, classified/unclassified movement and unknown rows separately;
- materiality basis/population are explicit;
- controllability, recurrence, generalization, and accountability have evidence or remain unknown/not established;
- adjusted view is supplementary, reconciled, and uses explicit polarity;
- management synthesis follows the semantic contract without expanding routine output.

## Legacy section: `ChatGPT/[Analytics]/Knowledge/GOVERNANCE_AND_ANTI_PATTERNS.md`

- Registry and trigger contracts govern method eligibility; no silent LLM override.
- Reasoning cannot replace deterministic execution or missing prerequisites.
- AES remains canonical execution governance; the Analytics extension adds domain constraints without creating a second execution framework.
- Driver/root-cause and correlation/causation confusion → claim ladder and causal evidence gate.
- Premature explanation → preliminary evidence stop gate.
- Baseline, aggregation, selection/exclusion, population, denominator, timing/cut-off bias → explicit controls and triggered robustness tests.
- False precision and narrative stronger than evidence → final evidence sufficiency cap.
- Method bloat → minimum sufficient set and stop rules.
- Confidence mistaken for causality → `confidence != claim_support != causal_status`.
- Numerical magnitude mistaken for business materiality → separate task profile; no numerical reasoning score.
- Reasoning substituted for deterministic execution → enforce deterministic boundary.
- Silent registry override or undefined trigger → require trigger type/rule/evidence and existing QA review.
- Blocked method used as evidence or execution lineage lost → `blocked != executed` and unique `method_execution_id`.
- Conflicting methods silently reconciled → preserve contradiction, constrain claim, escalate if material.
- Full reasoning applied to routine work without trigger → compact runtime collapse.
- Anomaly mistaken for control exception → distinguish unusual observation from explicit rule violation.
- Aggregate reconciliation replacing entity-level unmatched analysis → identify concrete one-sided elements when material.
- Driver decomposition accepted without factor reconciliation → reconcile factor effects when applicable.
- Timing shift interpreted as economic effect → run timing validation for material cut-off candidates.
- Transformation artifact interpreted as source/business effect → trace `REPORT → MART → STAGE → RAW`.
- Leading indicator treated as causal predictor → use signal/association/risk language without causal evidence.
- Method catalog inflated by controls → require distinct question, execution, and material effect.
- Decision methods leaking from `[Thinking]` → keep trade-offs, reversibility, premortem, risk appetite, choice, and decision in `[Thinking]`.
- Reasoning-control loop mistaken for autonomous execution → keep it inside AES-governed scope, checks, bounded correction, stop, rollback, acceptance, and authority boundaries.
## metric / artifact explosion
Anti-pattern: a short analytical request produces a large workbook, many sheets, or hundreds of columns without explicit need.

## Legacy section: `ChatGPT/[Analytics]/Knowledge/SMOKE_QA_FOR_ANALYTICS.md`

## 8. short task / anti-bloat test
