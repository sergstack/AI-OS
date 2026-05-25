# Codex Task Packets

## Purpose

Когда нужно изменить документы, код или автоматизацию, `[Analytics]` выдаёт ТЗ для `[Codex]` частями, чтобы изменения были управляемыми.

## Important rule

Codex task packets are for implementation. Analytical logic stays in `[Analytics]` first.

## Input

```text
json compact + json full
or only json compact
```

Use:

- compact for scope, audience, expected outputs;
- full for detailed rules, files, schemas, acceptance.

## Output packet set

1. Общий обзор ТЗ для передачи Codex.
2. ТЗ для формирования Stage.
3. ТЗ для формирования Mart.
4. ТЗ для подбора графиков.
5. ТЗ для создания выводов на основе структуры аналитических записок.
6. ТЗ для подготовки аналитических записок в Word.
7. ТЗ для отладки текстов и оформления аналитических записок.
8. QA / smoke / acceptance packet.

## Packet template

```markdown
# Codex Task Packet — <name>

From: [Analytics]
To: [Codex]
Task type:
Objective:
Context:
Files to inspect:
Files to change:
Inputs:
Constraints:
Forbidden actions:
Expected outputs:
Tests / checks:
Acceptance criteria:
Risks:
Rollback notes:
```

## 1. Overview packet

Objective: update or create the Analytics package without breaking in-project analysis mode.

Acceptance:

- [ ] `[Analytics]` still solves analytical tasks directly.
- [ ] Handoff is only for implementation.
- [ ] Main files standard added.
- [ ] QA and acceptance updated.
- [ ] Smoke QA updated.

## 2. Stage packet

Objective: enforce `stage_main_full` before stage slices.

Acceptance:

- [ ] `stage_main_full` required.
- [ ] No metrics/classifiers in stage.
- [ ] Portability to DB / BI / Excel stated.
- [ ] Stage slices allowed only after main stage file.

## 3. Mart packet

Objective: enforce `mart_main_full` and `mart_main_tz/compact`.

Acceptance:

- [ ] `mart_main_full` required.
- [ ] `mart_main_tz/compact` required.
- [ ] Slices derive from `mart_main_full`.
- [ ] Metrics/formulas/classifiers/risk/confidence fields in mart layer.

## 4. Charts packet

Objective: chart selection from mart sources only.

Acceptance:

- [ ] Each chart has source_mart.
- [ ] Each chart has metric, grain, period.
- [ ] Caption does not exceed evidence.
- [ ] Chart slices derive from `mart_main_full`.

## 5. Insights packet

Objective: create conclusions using memo structure.

Acceptance:

- [ ] DQ status included.
- [ ] Plan / Fact / Delta / ABS Delta included when relevant.
- [ ] Top deviations ranked.
- [ ] Risk has basis.
- [ ] Confidence has rationale.
- [ ] Cause vs hypothesis separated.
- [ ] Action has owner / due date.

## 6. Word packet

Objective: prepare Word/DOCX memo standard.

Acceptance:

- [ ] Executive summary from compact mart.
- [ ] Appendix/evidence from full mart.
- [ ] Charts sourced from mart slices.
- [ ] Limitations visible.

## 7. Text QA packet

Objective: text and formatting QA.

Acceptance:

- [ ] No unsupported claims.
- [ ] Low Confidence not written as fact.
- [ ] Risk/action rules followed.
- [ ] Formatting preserves meaning.

## 8. QA packet

Objective: run smoke QA and record acceptance.

Acceptance:

- [ ] Smoke questions pass/fail recorded.
- [ ] Changed files listed.
- [ ] Residual risks listed.
- [ ] Rollback notes provided.
