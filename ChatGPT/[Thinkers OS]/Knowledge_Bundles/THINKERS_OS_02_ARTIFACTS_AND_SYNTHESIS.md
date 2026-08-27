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
- source_fingerprint: sha256:c1e98fd04870879f42ac0ac95a6191024c4c5f274b4afec91bac388744df6a06

---

# Content

## From: `ChatGPT/[Thinkers OS]/Knowledge/ARTIFACT_CONTRACTS.md`

# Artifact Contracts

## Traceable excerpt

Each excerpt identifies excerpt ID, source ID, author, work, normalized location, short paraphrase or compliant quotation, reason, target card, and confidence. Avoid long copyrighted quotation and ornamental excerpts.

## Author Card

Separate `FACT`, `INTERPRETATION`, `HYPOTHESIS`, `RECOMMENDATION`, `BLOCKER`, core problem, concepts, next extraction, and confidence. Partial coverage remains explicit.

## Idea Card

One source-backed idea per card with evidence reference, concrete application, anti-pattern, transfer risk, confidence, and bounded candidate status. Missing evidence, risk, or confidence blocks the card.

## Applied Pattern

Required fields:

- source ideas;
- input;
- workflow;
- output;
- QA check;
- rollback;
- failure modes;
- transfer risk;
- confidence;
- export status.

Do not create a pattern from an unsupported idea.

## Judge

Review unsupported claims, evidence strength, hidden assumptions, corpus completeness, transfer risk, routing, QA, rollback, and premature automation. Verdict is `pass`, `revise`, or `blocked`. Non-pass blocks export.

## Revisor

Run only after `revise`. Fix only Judge-required defects; do not add facts, upgrade evidence, or erase limitations, risks, blockers, or confidence.

## Export candidate

Export only after Judge pass. Required state:

- `owner_acceptance: pending`;
- `execution_status: not run` unless observed otherwise;
- `production_status: NOT AUTHORIZED`;
- `contains_raw_source_text: false`;
- evidence and transfer risk explicit.

Export one functionally relevant bounded output to one receiving project. Never export books, normalized text, excerpt dumps, source manifests, blocked/rejected artifacts, or local paths.

## From: `ChatGPT/[Thinkers OS]/Knowledge/SYNTHESIS_AND_EXPORT.md`

# Synthesis and Export

## Portfolio snapshot — 2026-08-21

| Author | Coverage | Artifact/Judge state | Cross-author state |
|---|---|---|---|
| Peter Drucker | complete | Judge pass, export ready | isolated author pattern |
| W. Edwards Deming | complete | Judge pass, export ready | active synthesis lens |
| Daniel Kahneman | complete | Judge pass, export ready | active synthesis lens |
| Vladimir Lenin | complete | Judge pass, export ready | active synthesis lens |
| John Boyd | complete | Judge pass, export ready | isolated author pattern pending synthesis refresh |
| Elinor Ostrom | partial — two P1 gaps | bounded Judge pass, export ready | active synthesis lens with partial evidence |
| Taiichi Ohno | partial — one P1 gap | bounded Judge pass, export ready | isolated author pattern pending synthesis refresh |
| Jay Forrester | complete | Judge pass, export ready | active synthesis lens |
| Carl von Clausewitz | complete | Judge pass, export ready | active synthesis lens |
| Charlie Munger | complete | Judge pass, export ready | isolated author pattern pending synthesis refresh |
| Herbert A. Simon | complete | Judge pass, export ready | isolated author pattern pending synthesis refresh |
| Eliyahu M. Goldratt | complete | Judge pass, export ready | isolated author pattern pending synthesis refresh |
| Richard P. Rumelt | partial — one P1 gap | bounded Judge pass, export ready | isolated author pattern pending synthesis refresh |
| Everett M. Rogers | partial — two P1 gaps | bounded Judge pass, export ready | isolated author pattern pending synthesis refresh |
| Donald A. Norman | complete | Judge pass, export ready | isolated author pattern pending synthesis refresh |

Owner acceptance remains pending. Production status is `NOT AUTHORIZED`.

## Active provisional synthesis

MVP limits: 5 active patterns, preferably 2–3 lenses per case, maximum 4. Current patterns:

| Pattern | When to use | Key boundary |
|---|---|---|
| `SYN-001-REPEATED-FAILURE-DIAGNOSIS` | recurring failure after local fixes | do not erase direct accountability or present qualitative loops as proof |
| `SYN-002-DECISION-UNDER-FRICTION` | consequential decision with uncertainty, framing, dependencies, or delay | do not militarize routine work or add modeling without decision value |
| `SYN-003-OWNERSHIP-AND-SYSTEM-CHECK` | ambiguous ownership, rules, permissions, or multiple decision centers | do not centralize away local fit or hide coercive transfer |
| `SYN-004-BIAS-AWARE-DECISION-REVIEW` | prospective high-impact judgment sensitive to baseline/frame | do not label people retrospectively or replace domain evidence |
| `SYN-005-REVERSIBLE-INTERVENTION-GATE` | structural intervention with feedback, multiple owners, or costly reversal | quantitative claims require `[Analytics]`; pilot needs stop and rollback owners |

All five remain `active_provisional`, not validated/canonical. Application count does not promote them.

## Lens Router

| Problem type | Primary lenses | Optional lens | Route |
|---|---|---|---|
| repeated process failure | Deming; Forrester | Clausewitz for material dependency | `[Thinking]`; `[Analytics]` for model claims |
| consequential decision under uncertainty | Clausewitz; Kahneman | Forrester for delayed/nonlinear effects | `[Thinking]` |
| unclear ownership or governance | Ostrom; Deming | Lenin for rules/concentrated permissions | `[Thinking]`; reusable rule candidate to `[AI OS]` |
| structural change or concentration | Lenin; Ostrom | Deming for unresolved cause class | `[Thinking]` |
| policy with feedback or delay | Forrester; Deming | Ostrom for multiple owners | `[Analytics]` plus bounded `[Thinking]` record |
| bias-aware decision review | Kahneman; Clausewitz | none | `[Thinking]` |

Drucker, Boyd, Munger, Ohno, Simon, Goldratt, Rumelt, Rogers, and Norman remain isolated Judge-pass patterns until a separate synthesis refresh explicitly merges, replaces, or rejects them under duplicate/conflict rules.

## Available isolated Judge-pass patterns

These patterns are available for bounded `[Thinking]` use at precedence level 6. They are not active synthesis patterns, do not change the Lens Router, and must not be selected without a matching case trigger.

### `THINKERS-SIMON-PATTERN-001` — Bounded Decision Design

- use: decisions overloaded by alternatives, unclear premises, limited attention, or a disputed problem representation;
- workflow: define mandatory constraints and aspiration thresholds, separate facts from values and guesses, test the problem representation, search a bounded option set, choose a reversible sufficient action, and reopen when feedback violates a threshold;
- boundary: satisficing cannot lower safety, legal, ethical, rights, evidence, or irreversible-downside constraints;
- evidence: complete P0/P1 corpus, four traceable excerpts, Judge pass;
- status: isolated `active_provisional`; owner acceptance pending; production not authorized.

### `THINKERS-GOLDRATT-PATTERN-001` — Constraint-First Flow Review

- use: recurring flow delay, too many concurrent initiatives, suspected bottlenecks, project multitasking, or persistent operational conflict;
- workflow: define the system and guardrails, verify the current constraint, exploit before elevating, subordinate release, limit multitasking, monitor buffers, test conflict assumptions, and rediagnose after change;
- boundary: the constraint lens cannot override safety, quality, rights, governance, demand evidence, or multiple legitimate system goals;
- evidence: complete P0/P1 corpus, four traceable excerpts, Judge pass;
- status: isolated `active_provisional`; owner acceptance pending; production not authorized.

### `THINKERS-RUMELT-PATTERN-001` — Strategy Kernel and Crux Review

- use: a consequential strategy has many issues, unclear diagnosis, or actions without a coherent policy;
- workflow: diagnose the challenge, separate evidence from assumptions, state a crux hypothesis, choose a guiding policy, align actions, and reopen on disconfirming signals;
- boundary: a crux is a testable hypothesis, not root-cause proof; quantitative claims require `[Analytics]`;
- evidence: partial P0/P1 corpus, two normalized works, three traceable excerpts, Judge pass; one P1 work missing;
- status: isolated `active_provisional`; owner acceptance pending; production not authorized.

### `THINKERS-ROGERS-PATTERN-001` — Adoption Context Review

- use: a change needs an adoption hypothesis, channel test, or decision-right diagnosis before wider rollout;
- workflow: identify adopters and decision type, test perceived value and channels, run a bounded trial with feedback, then revise or stop;
- boundary: mandated use is not adoption; no adoption-rate claim without observed data;
- evidence: partial P0/P1 corpus, normalized fifth edition, three traceable excerpts, Judge pass; two P1 works missing;
- status: isolated `active_provisional`; owner acceptance pending; production not authorized.

### `THINKERS-NORMAN-PATTERN-001` — Interaction Clarity Review

- use: users must understand an interaction, system state, feedback, constraint, or recovery path;
- workflow: test discoverability, feedback, constraints, error recovery, and visceral/behavioral/reflective experience with representative users;
- boundary: this does not replace user research, accessibility, safety, or context testing;
- evidence: complete selected P0/P1 corpus, three normalized works, three traceable excerpts, Judge pass;
- status: isolated `active_provisional`; owner acceptance pending; production not authorized.

## Conflict Map

- Central redesign vs polycentric fit: change evidenced constraints while preserving bounded local autonomy and conflict paths.
- Act under friction vs model first: match modeling depth to reversibility, impact, and feedback risk.
- System cause vs direct accountability: separate causal classification from accountability design and immediate containment.
- Deliberate review vs decision friction: trigger framing review only above a declared impact, irreversibility, or sensitivity threshold.

Each conflict requires Position A, Position B, synthesis, when each dominates, failure mode, evidence status, and source artifact IDs in the source registry.

## Export routing

- `[Thinking]`: decision/risk/scenario patterns, Lens Router, Conflict Map, synthesis patterns, precedence.
- `[AI OS]`: supported general governance/evidence/confidence/QA candidates only.
- `[LLM]`: prompts, extraction workflows, model routing, Judge/Revisor logic, eval contracts.
- `[Analytics]`: formalizable methods, data requirements, metrics, quantitative checks, limitations.
- `[Codex]`: schemas, validators, tests, bundle generation, rollback requirements.

Never export raw source payloads, normalized books, source manifests, logs, local paths, or non-pass artifacts.

## Rollback

1. Disable the two `[Thinkers OS]` bundles in external Project Sources.
2. Remove only the bounded `[Thinkers OS]` routing and registry entries.
3. Restore previous upload guidance and validator project sets.
4. Preserve the source repository, books, manifests, artifacts, application history, and Judge results.
5. Rerun repository validation before re-enabling a corrected bounded subset.

## From: `ChatGPT/[Thinkers OS]/Knowledge/ROUTING_AND_HANDOFF.md`

# Routing and Handoff

Canonical destination routing is defined in repo-root `ROUTING_RULES.md`.
`[Thinkers OS]` prepares bounded handoffs; it does not absorb the receiving project's work.
## Handoff contract

Use one receiving project and the canonical fields in `HANDOFF_STYLE_STANDARD.md`.

Add author/corpus coverage, source artifact, Judge status, and transfer risk when the handoff uses thinker evidence.

## Handoff gates

- No Judge-pass pattern: do not export.
- Partial corpus: label the handoff bounded/partial and name the missing P1 gap.
- Quantitative claim: require `[Analytics]` evidence.
- Repository mutation: require `[Codex]` scope, checks, rollback, and acceptance.
- External Project sync: manual owner action unless explicitly authorized.

Forbidden inputs include secrets, raw/normalized books, excerpt dumps, source manifests, logs, local paths, and blocked/rejected artifacts.
