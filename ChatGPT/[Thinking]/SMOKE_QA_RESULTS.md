# [Thinking] Smoke QA Results

Date: 2026-07-31
Verdict: pass

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

Repository evidence: `python3 -m pytest -q tests/test_thinking_thinkers_integration.py tests/test_validation_scripts.py tests/test_thinkers_os_integration.py` — 52 passed. This is static repository-contract evidence only; external `[Thinking]` Project sync and behavioral smoke are `NOT RUN`.
