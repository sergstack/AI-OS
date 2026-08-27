# Migrated Bundle Semantics

Canonical source created during Issue #285 provenance migration.
Legacy bundle provenance: `ChatGPT/[Analytics]/Knowledge_Bundles/ANALYTICS_01_CORE_WORKFLOW.md`.

## Legacy section: `ChatGPT/[Analytics]/Knowledge/ANALYTICS_WORKFLOW.md`

If mode = `quick`, collapse to: question → minimal inputs → grain / period / filters → calculation or reasoning → compact result → QA note → limitation.
`analytical_depth` and `output_mode` are independent. Use conditional reasoning depth from `ANALYTICAL_REASONING_STANDARD.md`; `quick` does not become a full reasoning artifact without a material trigger.
## Parent / Child Issue Gate
For large or risky analytics tasks involving data contracts, stage/mart layers, workbook/report contracts, reconciliation, manual review, provider evidence, duplicate/anomaly candidates, or final QA, use `Parent / Child Issue Gate Standard` by reference.
Analytics should define parent scope, child issue sequence, source/output layers, grain, formulas, QA, limitations, and acceptance gates before Codex implementation. Do not use this pattern for simple one-step Goal Mode tasks.
## Workflow steps
1. Question / scope: business question, decision context, audience, period, grain, metrics, filters, owner, expected output; classify analytical intent and create `TASK_PROFILE` unless eligible for the compact routine path.
2. Inputs: available files, missing files, compact/full JSON, source systems, refresh date, required joins, directories/mappings, limitations.
3. Data contract: no calculation without grain; no memo without method; no mart without expected output.
4. RAW: original input only; no business logic, classifications, interpretations, or memo conclusions.
5. `stage_main_full`: cleaned, normalized, typed, identity/mapping joins only, no metrics/classifiers.
6. `mart_main_full`: complete analysis-ready table with metrics, formulas, flags, risk/confidence, QA and evidence fields.
7. `mart_main_tz` / compact: shortened mart for task, audience or executive memo.
8. Slices: derive all slices from `mart_main_full`.
9. Analysis: select the deterministic-first minimum sufficient method set from the registry, apply prerequisites, then use the preliminary evidence check, explanation challenge and claim calibration only to required depth. `blocked != executed`, `driver != root cause`, and material method conflict is not silently reconciled.
10. Charts: source from `mart_main_full` or a documented derived slice.
11. Memo: use verified analysis, not raw assumptions. For material or decision-critical management-facing output, compress verified findings into the smallest sufficient executive synthesis: supported business meaning, business effect versus data/control artefact where relevant, management implication and decision/action if any, material uncertainty, and what changes the view. Do not create evidence or infer controllability or persistence without support. Keep routine output compact; strategic choices remain with `[Thinking]`.
12. QA and acceptance: preserve existing QA/Judge/acceptance; `manual_review_required = yes` blocks automatic final publication until review resolution is recorded.

## Legacy section: `ChatGPT/[Analytics]/Knowledge/IN_PROJECT_ANALYSIS_MODE.md`

## Routing boundaries
Передавать в Codex только если нужно изменить файлы репозитория, написать Python/SQL/DAX/Power Query, создать тесты, автоматизировать pipeline, сгенерировать DOCX/PDF/PPTX программно, построить production-ready ETL, изменить структуру пакета документов или выполнить diff/release/rollback.
Передавать в LLM только если нужны prompt library, model routing, LLM evaluation, orchestration, generation workflow, or long-form narrative polish after verified numbers.
Передавать в Thinking только если нужно стратегическое решение, сценарий, decision memo, trade-off analysis or risk appetite.
Передавать в AI OS только если нужны AI pattern, AI governance, evidence/confidence по AI-концепции, новые модели/tools/use cases.

## Legacy section: `ChatGPT/[Analytics]/Knowledge/MAIN_FILES_STANDARD.md`

Correct flow:
Wrong flow:
`stage_main_full` is the cleaned, normalized and typed data array without business metrics or analytical classifiers.
Contains source metadata, period, date fields, entity keys, normalized dimensions, mapped IDs, currency/unit, technical lineage and row status for technical issues.
Does not contain business metrics, classification labels, materiality flags, risk labels, confidence labels, interpretation, memo text, or management conclusions.
Required:
`mart_main_full` is the full analysis-ready table for Sergey, Finance Team, deep conclusions and evidence. It contains metrics, formulas, dimensions, grain/keys, classification/materiality/variance/driver/timing/risk/confidence/action/QA/evidence/source lineage fields.
`mart_main_tz` / `mart_main_compact` is a shortened management-ready mart for the task, audience or executive memo. It does not replace `mart_main_full`.
A correct analytical result can be compact if key numbers are traceable, formulas are documented, limitations are visible, and full evidence can be produced if requested.
Rule: full mart is evidence layer, not default user interface.
All slices must be derived from `mart_main_full` and state source, filter logic, grain, metrics, purpose, and use.
When compact and full are both provided: compact defines executive requirements and short output; full defines full data/method/evidence requirements.
When only compact is provided: define a minimal data contract, required main files, missing fields, unsupported claims and assumptions register.
