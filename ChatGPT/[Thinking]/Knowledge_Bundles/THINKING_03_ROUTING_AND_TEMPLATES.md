# [Thinking] — Routing and Templates

## Purpose

Compact upload artifact for [Thinking] covering routing and templates.

## Source files

- `ChatGPT/[Thinking]/Knowledge/ROUTING_AND_HANDOFF.md`
- `ChatGPT/[Thinking]/Knowledge/AI_OS_REFERENCE.md`
- `ChatGPT/[Thinking]/Knowledge/SCENARIO_ANALYSIS_TEMPLATE.md`
- `ChatGPT/[Thinking]/CURRENT_STATUS.md`
- `ChatGPT/[Thinking]/SMOKE_QA_RESULTS.md`
- `ChatGPT/[Thinking]/Knowledge/THINKING_03_ROUTING_AND_TEMPLATES_BUNDLE_SEMANTICS.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[Thinking]`.

## Status

- production_promotion: no, unless explicitly accepted elsewhere
- bundle_type: generated compact upload artifact
- source_of_truth: declared granular source files
- source_fingerprint: sha256:42845a00da415bfd8f1513c18bf4ee7aba1ca6728f4fda8557a89e95b6c8c1ee
- generator: scripts/build_knowledge_bundles.py

---

# Content

## From: `ChatGPT/[Thinking]/Knowledge/ROUTING_AND_HANDOFF.md`

# Routing and Handoff
Canonical destination routing is defined in repo-root `ROUTING_RULES.md`.
Правило владения `[LLM]`: если основной результат — reusable prompt, выбор
модели или LLM workflow и стратегическое решение не запрошено, направь задачу в
`[LLM]` с фокусным, исполнимым handoff. Сохрани релевантные decision constraints,
запрошенный результат, критерии приёмки и следующий шаг; не убирай сведения,
нужные для продолжения работы. Не проектируй prompt, model routing или
downstream workflow в `[Thinking]`.
Use the canonical handoff fields in `HANDOFF_STYLE_STANDARD.md`.
## Thinking → Analytics
Используй, когда decision или scenario требует расчётов.
Передать:
- question;
- metrics;
- period;
- assumptions;
- options to test;
- expected analytical output.
## Analytics → LLM
Используй, когда verified numbers нужно превратить в memo, summary или narrative.
Передать:
- curated facts;
- tables or marts;
- reconciled metrics;
- limitations;
- tone and output format.
## LLM → Codex
Используй, когда нужен код для автоматизации prompt/memo/report workflow.
Передать:
- prompt spec;
- input/output contract;
- files to inspect;
- forbidden actions;
- tests;
- acceptance criteria.
## Codex → QA / Release
Передать:
- changed files;
- tests run;
- smoke QA;
- acceptance status;
- residual risks;
- rollback notes.

## From: `ChatGPT/[Thinking]/Knowledge/AI_OS_REFERENCE.md`

# AI OS Reference
## Purpose
Этот проект не содержит полную AI OS KB. `[AI OS]` уже существует и хранит governed knowledge base.
Используй `[AI OS]`, когда нужно:
- понять новую AI-концепцию;
- найти supported pattern;
- проверить confidence / evidence;
- связать AI-тренд с работой Сергея;
- найти governance rule;
- отличить supported / weak / unsupported claim.
## Не копировать
Не копировать в этот проект:
- весь compact KB package;
- raw transcripts;
- source cards;
- chunks;
- temp files;
- logs;
- embeddings;
- vector DB;
- web UI artifacts.
## Как ссылаться
Когда нужен KB-backed вывод, формулируй handoff в `[AI OS]` так:
```text
Используй AI OS KB. Найди supported/weak/unsupported evidence по теме:
<topic>
Верни:
- найдено в KB: да/нет/частично
- sources
- confidence
- supported claims
- weak/unsupported claims
- practical use for Sergey
```
## Rule
AI OS даёт evidence и patterns. Текущий проект применяет их в своей области, не смешивая роли.

## From: `ChatGPT/[Thinking]/Knowledge/SCENARIO_ANALYSIS_TEMPLATE.md`

# Scenario Analysis Template
## Question
## Decision context
## Scenarios
| Scenario | What happens | Key assumptions | Trigger | Leading indicators | Downside | Reversibility | Decision implication |
|---|---|---|---|---|---|---|---|
| Base | | | | | | | |
| Optimistic | | | | | | | |
| Downside | | | | | | | |
## Cross-scenario risks
## What would change the decision
## Handoff required?
- Analytics:
- LLM:
- Codex:
- AI OS:
## Recommendation
## Confidence
## Next step

## From: `ChatGPT/[Thinking]/CURRENT_STATUS.md`

# [Thinking] Current Status
Status: active
Owner: Sergey / Thinking Lead
Last updated: 2026-09-03
Last smoke QA: 2026-07-31 — repository contract pass; external behavior pass after 2 targeted reruns
Last pilot: `PILOT-THINKING-001` (2026-08-27) — one live decision memo, recorded `candidate` / `medium` confidence in root `docs/evidence/PILOT_RESULTS_2026-08-27_THINKING.md`; next step is owner review, then a further bounded pilot (see root `docs/operations/PILOT_CASES.md`)
- status_scope: ChatGPT/[Thinking]
- status_verified_revision: cddceb1f738191e67d03459e73dfa6c6a99db559
## Active canonical files
| File | Status | Purpose |
|---|---|---|
| `PROJECT_INSTRUCTIONS.md` | active | core project instructions |
| `README.md` | active | project setup and loading guidance |
| `CURRENT_STATUS.md` | active | live status tracking |
| `SMOKE_QA_RESULTS.md` | active | smoke QA record |
| `DECISION_LOG.md` | active | reusable decision record |
| `Knowledge/INDEX.md` | active | canonical file index |
| `Knowledge/REVISOR_REWRITE.md` | active | rewrite standard |
| `Knowledge/DECISION_STATUS_AND_REVISIT.md` | active | decision status standard |
| `Knowledge/THINKERS_LENS_ROUTER.md` | active | bounded lens selection for real decisions |
| `Knowledge/THINKERS_CONFLICT_MAP.md` | active | provisional cross-author conflict boundaries |
| `Knowledge/THINKERS_SYNTHESIS_PATTERNS.md` | active | five active provisional synthesis patterns mirrored from Thinkers OS |
| `Knowledge/THINKERS_APPLICATION_LOG.md` | active | empty append-only real-case logging schema |
## Candidate files
| File | Status | Why candidate |
|---|---|---|
| `Knowledge/THINKING_WORKFLOW.md` | candidate | workflow reference, not status source |
| `Knowledge/DECISION_MEMO_TEMPLATE.md` | candidate | template, not policy |
| `Knowledge/RISK_REVIEW.md` | candidate | supporting review guidance |
| `Knowledge/JUDGE_REVIEW.md` | candidate | supporting review guidance |
| `Knowledge/STRATEGY_OPTIONS_TEMPLATE.md` | candidate | supporting template |
| `Knowledge/ROUTING_AND_HANDOFF.md` | candidate | routing reference |
| `Knowledge/AI_OS_REFERENCE.md` | candidate | external reference |
## Deprecated / do not load as core
| File | Reason |
|---|---|
| none | no deprecated core files identified |
## Recently resolved gaps
- Dedicated decision log added.
- Smoke QA results file added.
- Explicit status/revisit standard added in a standalone canonical file.
- README now points to the canonical index file.
- Scenario analysis template exists and is covered by `THINKING_03_ROUTING_AND_TEMPLATES.md` (moved here 2026-09-03 — was miscategorized under "Current gaps" despite reading as already resolved).
## Current gaps
- Smoke QA remains documentation-level and does not replace a pilot case.
- Root path decision remains canonicalized to `ChatGPT/[Thinking]`.
- External ChatGPT sync is complete for Project Instructions and all four authoritative bundles.
- External behavioral smoke initially found two missing explicit fields; the Project Instructions gate was clarified and both targeted reruns passed.
- One prospective `[Thinking]` application pilot ran 2026-08-27 (`PILOT-THINKING-001`, see "Last pilot" above) with `candidate`/`medium`-confidence result; broader application effectiveness beyond this one pilot remains unverified.
## Thinkers synthesis status
- repository bundle: synchronized to external `[Thinking]`; follow-up instruction fix verified
- pattern count: 5 active provisional read-only mirrors
- isolated patterns excluded: Drucker, Boyd, Munger, Ohno, Simon, Goldratt, Rumelt, Rogers, Norman (corrected 2026-09-03 to match `[Thinkers OS]`'s current portfolio — Rumelt/Rogers/Norman were added there 2026-08-21 and this list had not been updated; see `docs/evidence/PROJECT_WIDE_REVISION_REVIEW_2026-09-03.md`)
- pilot candidate revisions: excluded pending separate Judge authorization
- owner acceptance: pending
- production status: NOT AUTHORIZED
## Next review trigger
- new project instructions change;
- routing conflict;
- judge/revisor failure;
- decision status missing in important outputs;
- handoff confusion;
- smoke QA fail.

## From: `ChatGPT/[Thinking]/SMOKE_QA_RESULTS.md`

# [Thinking] Smoke QA Results
Date: 2026-07-31
Repository contract verdict: pass
External behavioral verdict: pass after targeted remediation
| Test | Prompt / Input | Expected behavior | Actual behavior | Status | Fix required |
|---|---|---|---|---|---|
| Routing calculation to [Analytics] | Ask for deterministic calculation or metric math | Route to `[Analytics]`, not `[Thinking]` | Route rules and evidence guidance point to `[Analytics]` | pass | no |
| Routing code implementation to [Codex] | Ask for code changes, tests, or repo edits | Route to `[Codex]` | Handoff guidance points code work to `[Codex]` | pass | no |
| Unsupported claim flagged by `@judge` | Present weak claim with missing evidence | Mark unsupported claim and note evidence gap | Evidence rules require unsupported / blocker classification | pass | no |
| `@revisor` does not add new facts | Ask for rewrite of judged memo | Keep support status, no new facts | Revisor standard forbids new facts | pass | no |
| Scenario analysis uses 3 scenarios and does not invent numbers | Provide scenario template use case | Use base / optimistic / downside and avoid fabricated values | Scenario template added with empty numeric slots | pass | no |
| Decision memo includes status and revisit trigger | Create reusable decision record | Include status and revisit trigger | Decision status standard requires both | pass | no |
| AI OS evidence request is handed off, not copied into [Thinking] | Ask for KB-backed evidence | Hand off to `[AI OS]` instead of duplicating KB | Routing / handoff rules point to `[AI OS]` | pass | no |
| Thinker problem classification | Present a material complex decision | Classify one primary problem type before lens selection | `THINKERS_LENS_ROUTER.md` requires one primary problem type | pass | no |
| Thinker lens anti-bloat | Present a case with several plausible authors | Prefer 2–3 lenses and never exceed 4 | Router sets two primaries, optional third, and written reason for fourth | pass | no |
| Thinker conflict review | Select lenses that have a mapped tension | Check the applicable Conflict Map boundary | Router output requires `conflict_map_check`; Conflict Map defines the check rule | pass | no |
| Case evidence precedence | Present a pattern that conflicts with direct case evidence | Case evidence wins | Precedence ranks case facts and direct evidence first | pass | no |
| Irrelevant authors excluded | Present a narrow problem | Do not enumerate unrelated authors | Anti-bloat rule requires only selected and materially plausible excluded lenses | pass | no |
| Simple task remains simple | Present routine reversible work | Skip synthesis activation | Router explicitly skips conceptual activation for simple routine reversible tasks | pass | no |
| Analytics / LLM / Codex routing preserved | Request calculation, prompt workflow, or repository implementation | Route to the owning project | Router output and bundle preserve all three routes | pass | no |
## Issues found
- none
## Required fixes
- none
## Acceptance status
pass
Repository evidence: `python3 -m pytest -q tests/test_thinking_thinkers_integration.py tests/test_validation_scripts.py tests/test_thinkers_os_integration.py` — 52 passed. This command is static repository-contract evidence only; external behavior is recorded separately below.
## External behavioral smoke
Environment: cloud ChatGPT Project `[Thinking]` after Project Instructions refresh and upload of the four authoritative bundles from `Knowledge_Bundles/UPLOAD_LIST.md`.
| Case | Observed behavior | Status | Fix required |
|---|---|---|---|
| Primary problem classification | Produced a bounded pilot recommendation but did not output `primary_problem_type` | revise | require the explicit complex-case field in Project Instructions |
| Lens anti-bloat | Selected exactly two lenses (Clausewitz and Kahneman), explained why additional lenses were unnecessary | pass | no |
| Conflict Map review | Reconciled speed versus recurring-defect diagnosis through a contained pilot, QA gate, and rollback, but did not output `conflict_map_check` | revise | require the explicit complex-case field in Project Instructions |
| Case evidence precedence | Explicitly stated that direct 4-of-5 pilot failures override the general automation pattern and blocked scaling | pass | no |
| Irrelevant authors excluded | Returned a narrow second-reviewer recommendation without enumerating authors | pass | no |
| Simple task remains simple | Returned only the requested short title; no synthesis activation | pass | no |
| Analytics / LLM / Codex routing preserved | Routed calculation to `[Analytics]`, prompt workflow to `[LLM]`, and repository code/tests to `[Codex]` without doing the tasks | pass | no |
External result: 5 pass, 2 revise. The two revisions concern missing explicit observability fields, not the substantive recommendations.
## External issues found
- `primary_problem_type` was not emitted for a material complex case.
- `conflict_map_check` was not emitted for a mapped speed-versus-quality tension.
## External remediation and targeted rerun
- Project Instructions now require `primary_problem_type`, `selected_lenses`, `conflict_map_check`, and `precedence_check` in material complex outputs.
- The material-complex gate now explicitly includes competing objectives, recurring defects, material downside, weak or conflicting evidence, cross-functional conflict, and low reversibility.
| Rerun | Observed behavior | Status |
|---|---|---|
| Primary problem classification | Emitted all four required fields and a bounded pilot recommendation | pass |
| Conflict Map review | Emitted all four required fields and reconciled speed versus quality through an explicit boundary | pass |
Targeted rerun result: 2 pass, 0 revise.
## External acceptance status
pass

## From: `ChatGPT/[Thinking]/Knowledge/THINKING_03_ROUTING_AND_TEMPLATES_BUNDLE_SEMANTICS.md`

# Migrated Bundle Semantics
Canonical source created during Issue #285 provenance migration.
Legacy bundle provenance: `ChatGPT/[Thinking]/Knowledge_Bundles/THINKING_03_ROUTING_AND_TEMPLATES.md`.
## Legacy section: `ChatGPT/[Thinking]/CURRENT_STATUS.md`
| `Knowledge/THINKERS_SYNTHESIS_PATTERNS.md` | active | five active provisional patterns mirrored from Thinkers OS |
## Legacy section: `ChatGPT/[Thinking]/SMOKE_QA_RESULTS.md`
| Primary problem classification | Bounded pilot recommendation; missing `primary_problem_type` | revise | require explicit complex-case field |
| Lens anti-bloat | Exactly two lenses; additional lenses explicitly excluded | pass | no |
| Conflict Map review | Contained pilot resolved the tension; missing `conflict_map_check` | revise | require explicit complex-case field |
| Case evidence precedence | Direct 4-of-5 pilot failures overrode the general automation pattern | pass | no |
| Irrelevant authors excluded | Narrow recommendation without author enumeration | pass | no |
| Simple task remains simple | Only the requested short title | pass | no |
| Analytics / LLM / Codex routing preserved | Correct three-way routing without task execution | pass | no |
External result: 5 pass, 2 revise.
- Require `primary_problem_type`, `selected_lenses`, `conflict_map_check`, and `precedence_check` for material complex cases.
- Clarify the material-complex gate for competing objectives, recurring defects, material downside, weak or conflicting evidence, cross-functional conflict, and low reversibility.
- Primary problem classification rerun: pass.
- Conflict Map review rerun: pass.
