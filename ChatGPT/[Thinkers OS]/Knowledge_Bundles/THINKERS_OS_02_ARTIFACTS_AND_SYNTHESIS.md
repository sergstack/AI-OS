# [Thinkers OS] — Artifacts and Synthesis

## Purpose

Compact operational baseline for artifact contracts, Judge/Revisor, active provisional synthesis, Lens Router, Conflict Map, export routing, and rollback.

## Source files

- `ChatGPT/[Thinkers OS]/Knowledge/ARTIFACT_CONTRACTS.md`
- `ChatGPT/[Thinkers OS]/Knowledge/SYNTHESIS_AND_EXPORT.md`
- `ChatGPT/[Thinkers OS]/Knowledge/ROUTING_AND_HANDOFF.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[Thinkers OS]`.

## Status

- bundle_type: compact upload artifact
- source_of_truth: granular files listed above
- generated_date: 2026-08-21
- owner_acceptance: pending
- production_status: NOT AUTHORIZED
- source_fingerprint: sha256:959c23e93208198e0f31e0586e0d1b285d9a91f59508de2d6e90292ddfedebd4

---

# Content

## Artifact chain

- Excerpt: source ID, normalized location, short attributable paraphrase, target card, confidence.
- Author Card: fact, interpretation, hypothesis, recommendation, blocker, concepts, next extraction, confidence.
- Idea Card: one source-backed idea, application, anti-pattern, transfer risk, confidence.
- Applied Pattern: input, workflow, output, QA, rollback, failure modes, transfer risk, confidence.
- Judge: unsupported claims, assumptions, completeness, routing, QA, rollback, automation risk; pass/revise/blocked.
- Revisor: only Judge-required corrections; no new facts or evidence upgrades.
- Export: only after pass; owner acceptance pending, production unauthorized, no raw source text.

## Synthesis gate

Only Judge-pass author patterns can control active synthesis. Candidate, revise, blocked, restricted, deprecated, and archival artifacts are excluded.

Prefer 2–3 lenses per case; maximum 4. MVP maximum is 5 active patterns. Case facts and project governance always outrank thinker patterns.

## Current active provisional patterns

1. Repeated Failure Diagnosis — recurring failure with system, feedback, delay, or dependency questions.
2. Decision Under Friction — consequential uncertainty, framing, dependencies, or delayed effects.
3. Ownership and System Check — ambiguous mandates, rules, permissions, concentration, or multiple decision centers.
4. Bias-Aware Decision Review — prospective baseline/frame sensitivity in high-impact judgment.
5. Reversible Intervention Gate — structural/policy change with feedback, multiple owners, or costly reversal.

All remain `active_provisional`; none is validated/canonical by application count.

## Lens Router

- Repeated process failure: Deming + Forrester; Clausewitz only for material unresolved dependency.
- Consequential uncertainty: Clausewitz + Kahneman; Forrester for delayed/nonlinear effects.
- Unclear governance: Ostrom + Deming; Lenin for rules/concentrated permissions.
- Structural concentration: Lenin + Ostrom; Deming for unresolved cause class.
- Feedback/delay policy: Forrester + Deming; Ostrom for multiple owners.
- Bias-aware review: Kahneman + Clausewitz.

Drucker, Boyd, Munger, Ohno, Simon, and Goldratt are Judge-pass isolated author patterns pending a separate synthesis refresh.

## Available isolated Judge-pass patterns

These are precedence-level-6 author patterns, not additions to the active five-pattern synthesis or Lens Router.

### Bounded Decision Design — Herbert A. Simon

- use: alternatives, premises, attention, or problem representation make a decision difficult to bound;
- workflow: define constraints and aspiration thresholds; separate facts, values, and guesses; test the representation; search a bounded option set; choose a reversible sufficient action; reopen on failed feedback;
- transfer risk: satisficing can rationalize weak evidence or hide material interactions and irreversible downside;
- evidence/status: complete P0/P1 corpus; four traceable excerpts; Judge pass; isolated `active_provisional`; owner acceptance pending.

### Constraint-First Flow Review — Eliyahu M. Goldratt

- use: flow delay, excess concurrent work, bottleneck hypotheses, project multitasking, or persistent operational conflict;
- workflow: define system and guardrails; verify the constraint; exploit before elevating; subordinate release; limit multitasking; monitor buffers; test assumptions; rediagnose after change;
- transfer risk: a single-constraint story can erase plural goals or damage safety, quality, rights, and governance;
- evidence/status: complete P0/P1 corpus; four traceable excerpts; Judge pass; isolated `active_provisional`; owner acceptance pending.

## Conflict Map

- Central redesign vs polycentric fit: change evidenced constraints and preserve bounded local autonomy.
- Act under friction vs model first: match model depth to reversibility and feedback risk.
- System cause vs direct accountability: separate causal classification from containment and accountability.
- Deliberate review vs decision friction: trigger framing review only above a declared materiality threshold.

Never hide Position A/B, dominance conditions, failure mode, evidence status, or source artifact traceability.

## Routing

- maintenance of authors/corpus/intake/artifacts/synthesis → `[Thinkers OS]`.
- application to a real decision → `[Thinking]`.
- extraction prompt/model workflow → `[LLM]`.
- metrics or quantitative validation → `[Analytics]`.
- repository implementation/tests → `[Codex]`.
- general reusable AI governance candidate → `[AI OS]`.

Use one receiving project and the canonical handoff fields from `HANDOFF_STYLE_STANDARD.md`.

## Rollback and safety

Disable the two bundles, remove only bounded routing/registry entries, restore prior upload guidance and validator project sets, and rerun repository checks. Preserve books, source manifests, artifacts, application history, and Judge results.

Never upload or export raw/normalized books, OCR dumps, excerpt dumps, source manifests, execution logs, local absolute paths, secrets, or blocked/rejected artifacts. Owner acceptance remains pending. Production status is `NOT AUTHORIZED`.
