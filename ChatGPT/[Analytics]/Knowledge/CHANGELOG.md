# Changelog

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
