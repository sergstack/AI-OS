# Changelog

## 2026-09-05 — analytics-p0-semantic-contracts (issue #439)

Added:

- `METRIC_DEFINITION_CARD` — canonical semantic definition card for
  material/flagship/ratio-like metrics (`Templates/METRIC_DEFINITION_CARD_TEMPLATE.md`,
  referenced from `DATA_CONTRACTS.md`, `ANALYTICAL_REASONING_STANDARD.md` §11,
  `MAIN_FILES_STANDARD.md`, `QA_CHECKLIST.md`, `ACCEPTANCE_CRITERIA.md`). A
  formula alone is not a sufficient metric definition; an unresolved material
  metric definition blocks a strong management conclusion.
- Canonical `VALUE_STATE` vocabulary (`KNOWN`/`UNKNOWN`/`NOT_REPORTED`/
  `NOT_APPLICABLE`/`PARSE_FAILED`/`MISSING_SOURCE`/`UNMATCHED`/`BLOCKED`) with
  its invariants, defined in `DATA_CONTRACTS.md` and referenced from
  `MAIN_FILES_STANDARD.md`, `ANALYTICAL_REASONING_STANDARD.md` §12,
  `DATA_CONTRACT_TEMPLATE.md`, `MART_SPEC_TEMPLATE.md`,
  `EVIDENCE_CARD_TEMPLATE.md`, `QA_CHECKLIST.md`, and `ACCEPTANCE_CRITERIA.md`.
  `RAW -> STAGE -> MART` must not collapse materially different states into a
  generic null.
- Mandatory Headline Claim Gate (`ANALYTICAL_REASONING_STANDARD.md` §13,
  `CLAIM_EVIDENCE_REGISTRY_TEMPLATE.md`): for `analytical_depth = material /
  decision_critical`, every headline claim requires complete registry
  lineage or `allowed_in_executive = no`. Enforces
  `observation -> cause`, `contribution -> root cause`,
  `association -> causation`, and `single-period -> systemic / recurring /
  persistent` are never promoted without the required evidence level.
- Explicit "Three control gates" documentation (`ANALYTICAL_REASONING_STANDARD.md`
  §14, `GOVERNANCE_AND_ANTI_PATTERNS.md`): Gate 1 (data/calculation), Gate 2
  (analytical claim), Gate 3 (narrative) named as already-implemented,
  distinct mechanics; `DATA VALID != CLAIM SUPPORTED != NARRATIVE ACCEPTABLE`.
- P1 design-only extension-point notes (not implemented in this version):
  `POPULATION_CONTRACT`, `RECONCILIATION_CONTRACT`,
  `ANALYSIS_CONTINUATION_GATE` (`ANALYTICAL_REASONING_STANDARD.md` §15,
  `METRIC_DEFINITION_CARD_TEMPLATE.md`).
- Smoke QA case 12 covering the five P0 failure modes: ambiguous metric,
  uncertainty collapse, contribution vs root cause, single-period
  generalization, headline without lineage (`SMOKE_QA_FOR_ANALYTICS.md`).

Updated:

- `MEMO_PIPELINE.md` and `MEMO_RUBRIC.md` to tie the narrative gate to the
  Headline Claim Gate (`allowed_in_executive`).
- `Templates/DATA_CONTRACT_TEMPLATE.md`, `Templates/MART_SPEC_TEMPLATE.md`,
  `Templates/EVIDENCE_CARD_TEMPLATE.md` with `VALUE_STATE` /
  `METRIC_DEFINITION_CARD` reference fields.
- `MANIFEST.md` and `knowledge_bundle_manifest.json` to register
  `Templates/METRIC_DEFINITION_CARD_TEMPLATE.md`; `Knowledge_Bundles/`
  rebuilt only via `scripts/build_knowledge_bundles.py --write`.

Constraints preserved:

- 22-method registry not expanded; no new `METHOD_ID`.
- No new/parallel QA framework; existing Analytical Judge and Quantitative
  Sanity Gate semantics unchanged.
- `driver != root cause` and `claim strength <= final evidence sufficiency`
  strengthened, not weakened.
- `quick`-mode runtime collapse unchanged.
- `[Analytics]` / `[Thinking]` boundary unchanged (trade-offs, risk appetite
  stay in `[Thinking]`).

Status:

```text
production_ready: not claimed
pilot_case_required: yes
smoke_qa_status: pass (new case 12 added; full suite not independently re-run as human pilot)
```

## 2026-09-02 — analytical-judge-gate (issue #357)

Added:

- Explicit `Analytical Judge` gate as `ANALYTICAL_REASONING_STANDARD.md` §8: a
  compact post-findings orchestration checkpoint (`findings → Analytical Judge
  → pass / revise / blocked → final findings → memo`). Seven semantic checks
  mapped to existing controls; compact `ANALYTICAL_JUDGE` output record;
  bounded revise/rerun rule; `quick` runtime collapse. No new QA framework,
  taxonomy, method, or intent; §8→§9, §9→§10 renumbered.

Updated:

- `ANALYTICS_WORKFLOW.md` canonical workflow and Step 9 to make the gate
  explicit before memo/report.
- `QA_CHECKLIST.md` with a post-findings Analytical Judge gate block
  (orchestration, not a second framework).
- `ACCEPTANCE_CRITERIA.md` with criterion 12, `analytical_judge_status`, and a
  blocked-status entry.
- `GOVERNANCE_AND_ANTI_PATTERNS.md` with the gate principle, a blocker entry,
  and anti-pattern rows (no autonomous retry loop, no second framework,
  `blocked != executed`).
- `SMOKE_QA_FOR_ANALYTICS.md` with a case forcing a plausible over-strong
  "root cause" claim to `revise`, plus a `quick`-mode collapse case.

Status:

```text
production_ready: not claimed
pilot_case_required: yes
smoke_qa_status: pass
```

## 2026-05-25 — analytics-project-settings-minor-fix

Added:

- Canonical GitHub path note in README.
- Do-not-upload guidance for ChatGPT project knowledge.
- Claim / evidence registry template.
- Evidence card template.
- Memo rubric.

Updated:

- Knowledge manifest to include the rubric and new templates.
- package manifest to match the documented package inventory.
- Smoke QA result note to reflect the minor-fix pass.

Status:

```text
production_ready: not claimed
pilot_case_required: yes
```

## 2026-05-21 — analytics-project-settings-full-v1

Added:

- In-project analysis mode.
- Main files standard.
- Mandatory `stage_main_full`.
- Mandatory `mart_main_full`.
- Mandatory `mart_main_tz/compact`.
- Rule that mart slices derive from `mart_main_full`.
- Compact/full JSON input logic.
- Chart selection standard.
- Analytical memo MVP structure.
- Word/DOCX report standard.
- Text QA and style standard.
- Codex task packets by controlled parts.
- Smoke QA for Analytics.
- Smoke QA result recorded.

Updated:

- Routing to prevent premature handoff.
- Acceptance criteria with main file checks.
- QA checklist with main file and chart checks.

Status:

```text
ready_to_upload: yes
production_ready: not claimed
smoke_qa_status: pass
requires_pilot_case: yes
```
