# Thinkers Synthesis Patterns

- synthesis_status_source: `ChatGPT/[Thinkers OS]/Knowledge/SYNTHESIS_AND_EXPORT.md`
- status_write_policy: statuses below are read-only mirrors; `[Thinking]` cannot promote or revise them
- deployment_status: repository_candidate_not_uploaded
- owner_acceptance: pending
- production_status: NOT AUTHORIZED

## SYN-001-REPEATED-FAILURE-DIAGNOSIS — Repeated Failure Diagnosis

- problem type: `repeated_process_failure`
- source authors: Deming, Forrester, Clausewitz
- source patterns: `THINKERS-DEMING-PATTERN-001`, `THINKERS-FORRESTER-PATTERN-001`, `THINKERS-CLAUSEWITZ-PATTERN-001`
- use: recurring failure persists after local fixes or may involve system feedback, delay, or unresolved dependencies.
- do not use: one-off direct violation is evidenced or urgent containment cannot wait.
- workflow: separate signal/requirement; map recurrence, scope, feedback, delay, and dependencies; classify cause; assign bounded action; define verification and rollback.
- output: bounded diagnosis with cause class, loop/dependency hypotheses, owners, verification trigger, and rollback.
- risks: unsupported statistical labels; accountability dilution; qualitative loops presented as proof.
- QA: facts, requirements, hypotheses, feedback assumptions, owners, and overturning evidence are distinguishable.
- rollback: revert the corrective change if verification contradicts the diagnosis; retain and reclassify the incident.
- confidence: medium-low
- status: `active_provisional`
- evidence: Judge-pass author patterns; cross-author synthesis Judge pass.

## SYN-002-DECISION-UNDER-FRICTION — Decision Under Friction

- problem type: `consequential_decision_under_uncertainty`
- source authors: Clausewitz, Kahneman, Forrester
- source patterns: `THINKERS-CLAUSEWITZ-PATTERN-001`, `THINKERS-KAHNEMAN-PATTERN-001`, `THINKERS-FORRESTER-PATTERN-001`
- use: consequential decision combines uncertainty, material dependencies, frame sensitivity, or delayed system effects.
- do not use: routine reversible work with no material dependency, framing, or feedback risk.
- workflow: state objective/dependencies; record baseline and frames; map evidenced feedback; choose review depth/action; declare monitoring and rollback.
- output: decision record with evidence, frame test, dependencies, model requirement, action, and revisit trigger.
- risks: militarized framing; bias labels without evidence; false model precision.
- QA: review depth traces to impact, reversibility, evidence, and plausible feedback.
- rollback: return to the last reversible decision state when a declared assumption fails.
- confidence: medium-low
- status: `active_provisional`
- evidence: Judge-pass author patterns; cross-author synthesis Judge pass.

## SYN-003-OWNERSHIP-AND-SYSTEM-CHECK — Ownership and System Check

- problem type: `unclear_ownership_or_governance`
- source authors: Deming, Ostrom, Lenin
- source patterns: `THINKERS-DEMING-PATTERN-001`, `THINKERS-OSTROM-PATTERN-001`, `THINKERS-LENIN-PATTERN-001`
- use: failure involves ambiguous ownership, interacting rules, concentrated permissions, or multiple decision centers.
- do not use: ownership is clear and a direct violation can be handled without structural change.
- workflow: separate signal/cause/accountability; map owners/rules; test concentration/local autonomy; assign action; define safeguards and rollback.
- output: ownership/system map with mandates, hypotheses, monitoring, escalation, safeguards, and rollback owner.
- risks: accountability dilution; governance sprawl; coercive or ideological transfer.
- QA: every mandate and structural claim has evidence, challenge, monitoring, and rollback.
- rollback: restore the prior ownership map if coordination or safeguards worsen; retain history.
- confidence: medium-low
- status: `active_provisional`
- evidence: Judge-pass author patterns; cross-author synthesis Judge pass.

## SYN-004-BIAS-AWARE-DECISION-REVIEW — Bias-Aware Decision Review

- problem type: `bias_aware_decision_review`
- source authors: Kahneman, Clausewitz
- source patterns: `THINKERS-KAHNEMAN-PATTERN-001`, `THINKERS-CLAUSEWITZ-PATTERN-001`
- use: high-impact decision may change with baseline, equivalent framing, or unverified dependency assumptions.
- do not use: retrospective diagnosis of a person, substitution for domain evidence, or delay on routine reversible work.
- workflow: predeclare threshold/baseline; capture initial judgment; restate equivalent frames; check material evidence; document reversal/revisit trigger.
- output: prospective decision-hygiene record without personal bias labels.
- risks: hindsight accusation; post-hoc baseline; slow review assumed superior.
- QA: baseline, frames, evidence, initial judgment, reversal, and disagreement are explicit.
- rollback: remove the gate from low-value classes if logged reasoning quality does not improve; preserve records.
- confidence: medium-low
- status: `active_provisional`
- evidence: Judge-pass author patterns; cross-author synthesis Judge pass.

## SYN-005-REVERSIBLE-INTERVENTION-GATE — Reversible Intervention Gate

- problem type: `policy_with_feedback_or_delay`
- source authors: Forrester, Ostrom, Lenin, Deming
- source patterns: `THINKERS-FORRESTER-PATTERN-001`, `THINKERS-OSTROM-PATTERN-001`, `THINKERS-LENIN-PATTERN-001`, `THINKERS-DEMING-PATTERN-001`
- use: structural or policy intervention has uncertain feedback, multiple owners, concentrated dependencies, or costly reversal.
- do not use: urgent containment or small reversible change where modeling/governance add no decision value.
- workflow: define outcome/evidence; map feedback/governance; route quantitative claims to the smallest reproducible Python/SQL test; run bounded pilot; predeclare stop/rollback.
- output: pilot contract with assumptions, governance, safeguards, monitored thresholds, and rollback.
- risks: false precision; governance overbuild; coercive transfer; unsupported system labels.
- QA: inputs, periods, units, assumptions, mandates, evidence, stop threshold, rollback owner, and history are inspectable.
- rollback: disable at the threshold, restore the previous configuration, and preserve model, decisions, and observations.
- confidence: medium-low
- status: `active_provisional`
- evidence: Judge-pass author patterns; cross-author synthesis Judge pass.

## Excluded from active synthesis

- Isolated Judge-pass author patterns for Boyd, Drucker, Munger, and Ohno are not part of these five cross-author patterns.
- Candidate pilot revisions, candidate Conflict Map additions, candidate/revise/blocked/restricted/deprecated/archival artifacts, and raw source payloads are excluded.
- Exclusion does not reject an author pattern; it prevents unreviewed or irrelevant material from controlling a case.
