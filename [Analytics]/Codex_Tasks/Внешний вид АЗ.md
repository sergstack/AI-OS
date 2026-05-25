# Codex Task: Analytical Memo Visual QA Gate v1

## Mode

read-only first / deterministic QA / professional DOCX-PDF appearance gate

## Context

We generate professional analytical memos as DOCX/PDF artifacts for CFO / risk / operations users.

Existing QA already checks:
- LLM quality;
- routing;
- report generation;
- DOCX render diagnostics;
- artifact publication hygiene.

Now we need a deterministic visual-quality gate so analytical notes look professional, readable, and release-ready.

KB review context:
- KB checked: yes
- Sources reviewed:
  - `Аудит внешнего вида АЗ.md`
  - `PROJECT_DESCRIPTION_REPORT.md`
  - `Структура папок фабрики.txt`
  - `KB__03_WORKFLOWS_TRACEABILITY.md`
- KB finding: partial
- Confidence: medium
- Evidence: mixed
- Interpretation: DOCX/render QA is supported; visual-quality gate requires formalization.

## Objective

Create a deterministic visual QA standard and read-only diagnostic gate for analytical memo DOCX/PDF outputs.

This task is NOT a business-logic task.  
This task is NOT a generator-fix task.  
This task is NOT a live pipeline run.

The goal is to add a governed diagnostic layer that separates:

- render correctness;
- visual layout quality;
- executive readability;
- publishing hygiene.

## Inputs

Use the existing repository structure and current DOCX/report QA conventions.

Relevant conceptual inputs:
- existing DOCX LibreOffice diagnostic logic;
- existing report QA checks;
- existing analytical memo generation pipeline;
- existing artifact validation patterns;
- current DOCX/PDF analytical memo outputs as diagnostic targets only.

Expected current diagnostic areas to reuse where available:

- LibreOffice availability;
- DOCX package inspection;
- DOCX to PDF render;
- PDF to PNG page render;
- page-level visual diagnostics;
- table diagnostics;
- chart/image diagnostics;
- metadata and publishing hygiene;
- content sanity checks.

## Files To Inspect

Inspect existing project conventions before creating files:

- existing DOCX / LibreOffice diagnostic scripts;
- existing report QA scripts;
- existing tests around DOCX/report artifacts;
- existing docs/report QA documentation;
- project README / AGENTS / RUNBOOK if present;
- existing config conventions;
- existing artifact diagnostics folder conventions;
- existing pytest patterns.

Do not edit during the first inspection step.

## Files Allowed To Modify

Create or update only the following files, unless the project has a clearly different convention for docs/config/scripts/tests:

```text
docs/ANALYTICAL_MEMO_VISUAL_STANDARD.md
docs/DOCX_VISUAL_QA_GATE.md
config/docx_style_contract.yml
scripts/diagnose_docx_visual_quality.py
tests/test_docx_visual_quality_contract.py
```

If the project uses different equivalent locations, follow the existing project structure and explain the chosen paths in the final report.

## Forbidden Actions

Do not:

- change business calculations;
- change mart logic;
- change risk scoring;
- change metric formulas;
- change LLM prompts unless explicitly required by a later separate task;
- change `.env`, secrets, credentials, Kestra config, flow files, or scheduler settings;
- run live Kestra;
- modify existing report artifacts;
- auto-fix DOCX files;
- rewrite conclusions;
- alter numeric values;
- remove evidence markers;
- hide exceptions or risks;
- weaken existing QA gates;
- remove existing validation checks;
- broaden scope into generator redesign;
- add unrelated dependencies;
- commit, push, deploy, or publish anything.

This task must be read-only against existing DOCX/PDF/report artifacts.

## Required Subagent Roles

Use subagent-style decomposition where useful:

- planner: inspect repository conventions and confirm scope;
- implementation engineer: create docs/config/script/test files;
- test engineer: run contract tests and CLI smoke checks;
- reviewer: check scope, forbidden actions, output contracts, and residual risks.

Do not use subagents for complexity theatre. Keep the task atomic.

## Required Verdicts

The diagnostic output must produce separate verdicts:

```yaml
docx_render_status: pass | revise | blocked
visual_layout_status: pass | revise | blocked
executive_readability_status: pass | revise | blocked
publishing_hygiene_status: pass | revise | blocked
overall_visual_release_status: pass | revise | blocked
```

Rules:

- `blocked` means the artifact must not be released.
- `revise` means the artifact renders but needs generator/style improvement.
- `pass` means no material visual/publishing defects were detected.

## Severity Matrix

Every defect must have severity:

```yaml
severity: blocker | high | medium | low
```

Minimum classification:

| Defect | Severity |
|---|---|
| DOCX cannot render to PDF | blocker |
| PDF cannot render to PNG pages | blocker |
| Key table unreadable | blocker |
| Required chart missing | blocker |
| Required chart blank | blocker |
| Text clipped or outside page | blocker/high |
| Table outside margins | high |
| Main report and appendix mixed | high |
| Missing executive summary | high |
| Chart caption orphaned from chart | high |
| Required table missing | high |
| Tracked changes present | blocker |
| Comments present | blocker/high |
| Debug/local paths present | blocker/high |
| English technical chart titles in Russian report | medium/high |
| Inconsistent fonts or heading hierarchy | medium |
| Overdense page with no visual grouping | medium |
| Minor spacing/alignment inconsistency | low |

## Machine-Readable Style Contract

Create:

```text
config/docx_style_contract.yml
```

Minimum required fields:

```yaml
page:
  size: A4
  margins_cm:
    top: 1.8
    bottom: 1.8
    left: 1.8
    right: 1.8

fonts:
  body:
    min_size_pt: 10
    preferred_size_pt: 10.5
  table:
    min_size_pt: 8.5
  h1:
    min_size_pt: 15
    bold: true
  h2:
    min_size_pt: 12
    bold: true

tables:
  max_columns_main_body: 6
  repeat_header_rows_required: true
  numeric_alignment: right
  text_alignment: left
  require_readable_headers: true
  wide_tables_to_appendix: true

charts:
  min_width_cm: 13
  min_dpi: 150
  require_caption: true
  require_nearby_interpretation: true
  forbid_blank_charts: true
  forbid_default_technical_titles: true

language:
  report_language: ru
  forbid_english_technical_titles: true

appendix:
  require_clean_page_break: true
  require_appendix_heading: true
  forbid_mixing_with_main_report: true

publishing_hygiene:
  forbid_tracked_changes: true
  forbid_comments: true
  forbid_debug_paths: true
  forbid_local_temp_paths: true
  forbid_excessive_custom_metadata: true
```

The test file must validate that the YAML exists, is parseable, and contains all required top-level keys.

## Diagnostic Script Requirements

Create:

```text
scripts/diagnose_docx_visual_quality.py
```

The script must support:

```bash
python3 scripts/diagnose_docx_visual_quality.py \
  --docx artifacts/report/<target>.docx \
  --out artifacts/diagnostics/docx_visual_<timestamp>/
```

Required behavior:

1. Verify DOCX exists.
2. Capture file size and metadata.
3. Inspect DOCX package read-only.
4. Detect comments, tracked changes, suspicious metadata, local/debug paths.
5. Check LibreOffice or soffice availability.
6. Convert DOCX to PDF headlessly.
7. Convert PDF pages to PNG images.
8. Preserve stdout/stderr logs.
9. Produce page-level diagnostics.
10. Produce table diagnostics.
11. Produce chart diagnostics.
12. Produce publishing hygiene diagnostics.
13. Produce JSON defect report.
14. Produce Markdown diagnostic report.
15. Exit non-zero if any `blocker` exists.

The script must not modify the source DOCX.

## Required Diagnostic Artifacts

The diagnostics folder must contain:

```text
diagnostic_report.md
defects.json
rendered.pdf
pages/
  page_001.png
  page_002.png
  ...
logs/
  libreoffice_stdout.log
  libreoffice_stderr.log
  pdf_render_stdout.log
  pdf_render_stderr.log
```

`defects.json` minimum schema:

```json
{
  "target_docx": "...",
  "created_at": "...",
  "verdicts": {
    "docx_render_status": "pass|revise|blocked",
    "visual_layout_status": "pass|revise|blocked",
    "executive_readability_status": "pass|revise|blocked",
    "publishing_hygiene_status": "pass|revise|blocked",
    "overall_visual_release_status": "pass|revise|blocked"
  },
  "defects": [
    {
      "id": "VQA-001",
      "severity": "blocker|high|medium|low",
      "category": "render|layout|table|chart|appendix|metadata|executive_readability",
      "page": 1,
      "description": "...",
      "evidence": "...",
      "recommended_action": "..."
    }
  ],
  "release_blockers": []
}
```

## Visual Checks

Implement or document checks for the following areas.

### Render

- DOCX converts to PDF.
- PDF converts to PNG pages.
- Page count is greater than zero.
- No blank pages unless explicitly allowed.

### Page Layout

- no clipped text;
- no overlapping visible text;
- no obvious content outside page margins;
- no orphan section heading at page bottom;
- no chart caption separated from chart;
- appendix starts cleanly;
- main report and appendix are visually separated.

### Tables

Check at minimum:

- KPI block;
- jurisdiction risk table;
- point-risk table;
- provider detail table;
- actions/manual checks table;
- appendix top-5 providers;
- status definitions.

For each:

- table fits page width;
- headers readable;
- numeric columns readable;
- currencies visible;
- percentages visible;
- wrapping acceptable;
- no values visually merged;
- repeated headers after page breaks where applicable.

### Charts

Expected charts:

- Проходимость за 7 дней;
- Распределение депозитов;
- Чистый поток за 7 дней;
- Проходимость по юрисдикциям;
- Изменения проходимости к предыдущему дню;
- Риск и стоимость провайдеров;
- Интенсивность отказов.

For each:

- chart exists;
- chart is not blank;
- chart is readable after DOCX/PDF render;
- caption is near the correct chart;
- chart has nearby interpretation or explanation;
- no default technical titles;
- no English technical titles if report is Russian.

### Executive Readability

Check or document:

- executive summary exists;
- first page is not overloaded;
- key findings are limited and readable;
- main conclusions appear before appendices;
- long technical detail is moved to appendix;
- charts/tables support conclusions rather than decorate the report.

### Publishing Hygiene

Check:

- no tracked changes;
- no comments;
- no excessive custom properties;
- no unsuitable personal metadata;
- no embedded debug text;
- no temporary local file paths.

## Markdown Report Format

`diagnostic_report.md` must use this structure:

```md
# Analytical Memo Visual QA Diagnostic Report

## 1. Verdict

docx_render_status:
visual_layout_status:
executive_readability_status:
publishing_hygiene_status:
overall_visual_release_status:

reason:
release_blockers:
must_fix_before_release:
nice_to_have:
requires_live_run: false

## 2. Target

- DOCX:
- File size:
- Created diagnostics folder:

## 3. Commands Run

List all commands.

## 4. Artifacts Created

| Artifact | Path | Exists | Notes |
|---|---|---|---|

## 5. Defects

| ID | Severity | Category | Page | Description | Recommended action |
|---|---|---|---|---|---|

## 6. Table Diagnostics

## 7. Chart Diagnostics

## 8. Appendix Diagnostics

## 9. Metadata / Publishing Hygiene

## 10. Content Sanity Notes

No full business recalculation was performed.

## 11. Final Recommendation

pass / revise / blocked
```

## Documentation Requirements

Create:

```text
docs/ANALYTICAL_MEMO_VISUAL_STANDARD.md
docs/DOCX_VISUAL_QA_GATE.md
```

The docs must explain:

- purpose of the visual QA gate;
- what is checked deterministically;
- what is only documented as heuristic/manual review;
- status meanings: `pass`, `revise`, `blocked`;
- severity meanings: `blocker`, `high`, `medium`, `low`;
- difference between render correctness and visual quality;
- difference between visual QA and business logic QA;
- why this task must not recalculate business formulas;
- why generator fixes must be a separate task;
- how to run the diagnostic script;
- expected diagnostic artifacts;
- release decision logic.

The docs must explicitly prohibit business logic changes.

## Tests

Create:

```text
tests/test_docx_visual_quality_contract.py
```

Minimum tests:

- style contract YAML exists;
- YAML is parseable;
- required top-level sections exist;
- diagnostic script exists;
- diagnostic script has CLI help;
- diagnostic script does not require live Kestra;
- docs files exist;
- docs contain required verdict names;
- docs contain severity matrix;
- docs explicitly prohibit business logic changes.

If an existing test framework is present, integrate with it.  
Otherwise use plain `pytest`.

Suggested smoke commands:

```bash
python3 scripts/diagnose_docx_visual_quality.py --help
pytest tests/test_docx_visual_quality_contract.py -q
```

If the repository uses another Python/test entrypoint, use the existing convention and report the actual commands.

## Expected Outputs

Create or update:

```text
docs/ANALYTICAL_MEMO_VISUAL_STANDARD.md
docs/DOCX_VISUAL_QA_GATE.md
config/docx_style_contract.yml
scripts/diagnose_docx_visual_quality.py
tests/test_docx_visual_quality_contract.py
```

Expected behavior:

- visual QA separates render/layout/editorial/publishing verdicts;
- every defect has severity;
- release blockers are explicit;
- diagnostic script is read-only against source DOCX;
- script exits non-zero on blocker;
- business logic is not changed;
- no live Kestra run is required;
- tests pass.

## Acceptance Criteria

Task is complete only if:

- [ ] `docs/ANALYTICAL_MEMO_VISUAL_STANDARD.md` exists.
- [ ] `docs/DOCX_VISUAL_QA_GATE.md` exists.
- [ ] `config/docx_style_contract.yml` exists and is valid YAML.
- [ ] `scripts/diagnose_docx_visual_quality.py` exists.
- [ ] `tests/test_docx_visual_quality_contract.py` exists.
- [ ] Visual QA separates render/layout/editorial/publishing verdicts.
- [ ] Every defect has severity.
- [ ] Release blockers are explicit.
- [ ] Diagnostic script is read-only against source DOCX.
- [ ] Script exits non-zero on blocker.
- [ ] Business logic is not changed.
- [ ] Existing QA gates are not weakened.
- [ ] No live Kestra run is required.
- [ ] Tests pass.
- [ ] Final report lists files changed, assumptions, risks, tests, and acceptance status.

## Rollback Plan

If the implementation is not accepted:

- delete the newly created docs/config/script/test files;
- do not touch existing report artifacts;
- do not revert unrelated files;
- leave existing pipeline behavior unchanged;
- keep existing QA and report generation behavior unchanged.

For risky or unexpected changes, report the exact files to revert and do not proceed with broader cleanup.

## Final Review Requirements

Before final response, verify:

- diff is limited to allowed files;
- no business logic changed;
- no mart/report generator formulas changed;
- no prompts changed unless explicitly justified;
- no existing QA gates removed or weakened;
- no live Kestra run executed;
- no secrets, local credentials, or `.env` touched;
- tests/checks were run or blocker is clearly stated.

## Expected Final Response From Codex

Return:

```md
# Implementation Summary

## Files Created

## Files Modified

## Commands Run

## Test Results

## Acceptance Checklist

## Assumptions

## Residual Risks

## Acceptance Status

pass / fail / blocked

## Recommended Next Task
```

Recommended next task must be separate:

```text
Codex Task: Fix report generator visual defects based on Visual QA diagnostic report
```

Do not perform that fix in this task.