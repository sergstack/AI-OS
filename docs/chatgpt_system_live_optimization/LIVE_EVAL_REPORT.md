# ChatGPT Project System Live Evaluation

- date: 2026-08-21
- owner project: `[AI OS]`
- execution owner: `[Codex]`
- method: live ChatGPT Project responses + local deterministic checks + AES corrective loop
- scope: `[AI OS]`, `[Thinking]`, `[Analytics]`, `[LLM]`, `[Codex]`, `[Inbox Router]`, `[Thinkers OS]`
- production status: `NOT AUTHORIZED`

## Rubric

Each dimension is scored `0` (fail), `1` (partial), or `2` (pass): routing/boundary, evidence/grounding, contract/format, actionability, and calibrated limitations. A critical routing, evidence, safety, or false-execution defect overrides the total and requires `revise` or `blocked`.

## Baseline live results

| Project | Live case | Score | Verdict | Evidence summary |
|---|---|---:|---|---|
| `[AI OS]` | blocked retrieval promotion + Codex handoff | 9/10 | pass | Correctly blocked embeddings, semantic search, and vector DB; separated facts/hypothesis; produced a bounded evidence-review handoff. Explanation was longer than needed but remained traceable. |
| `[Thinking]` | recurring failures: scale or bounded pilot | 9/10 | pass | Emitted all four complex-case observability fields, respected direct case evidence, compared options, and recommended a reversible pilot with revisit triggers. Longer than necessary but decision-ready. |
| `[Analytics]` | quick top-3 plan/fact request without data | 10/10 | pass | Refused to invent numbers, marked the result `NOT CALCULABLE`, exposed missing grain/period/units/reconciliation, and blocked the management conclusion. |
| `[LLM]` | reusable high-risk memo workflow | 8/10 | revise | Routing, Judge/Revisor gates, model-class routing, registry, and limitations were correct. The response expanded to about 13,163 characters and repeated the same constraints across several sections. |
| `[Codex]` | controlled refactor with no repository attached | 8/10 | revise | Correctly returned `PASS FOR INSPECTION / BLOCKED FOR REFACTOR`, did not claim execution, preserved tests/schema/rollback constraints. The missing-input response expanded to about 8,072 characters of hypothetical workflow. |
| `[Inbox Router]` | six-item cross-project batch routing | 10/10 | pass | Routed all six inputs correctly to Things, AI OS, Thinking, Analytics, Codex, and Thinkers OS without solving the target work. |
| `[Thinkers OS]` | preview/sample source-gate case | 10/10 | pass | Fresh post-sync live evidence returned scope-based `REVISE / SCOPE-BLOCKED`, preserved unaffected synthesis, and named owner action/resume stage without invented evidence. |

Baseline total: `64/70` (`9.14/10`). Content and safety gates passed in all seven projects. Two usability defects require corrective iteration.

## Defects and corrective actions

| Defect | Class | Root cause | Before | Corrective action | Rerun scope | Status |
|---|---|---|---|---|---|---|
| `LIVE-LLM-001` | `CONTENT_FIX` | `PROBABLE`: the required six-section format and the request for a template jointly dominate soft brevity guidance | ~13,163 characters with repeated workflow/gate/registry constraints | Two bounded corrections: adaptive depth, then one compact prompt block with a near-4,000-character default | `[LLM]` same live case | `REVISE_LIMIT_REACHED`: ~10,201 characters; semantic quality preserved; 22.5% shorter |
| `LIVE-CODEX-001` | `CONTENT_FIX` | `CONFIRMED`: no fast-path response contract existed for a missing repository/file | ~8,072 characters despite an immediate execution blocker | Two bounded corrections: missing-object fast path, then one-table near-2,500-character contract | `[Codex]` same live case | `PASS_WITH_LIMITATIONS`: ~3,880 characters; one compact table; 51.9% shorter |

## Corrective reruns

| Project | Baseline | First rerun | Final rerun | Semantic regression | Final form verdict |
|---|---:|---:|---:|---|---|
| `[LLM]` | ~13,163 chars | ~12,830 chars | ~10,201 chars | none observed | `REVISE_LIMIT_REACHED` — useful reduction, still above the explicit default target |
| `[Codex]` | ~8,072 chars | ~6,511 chars | ~3,880 chars | none observed | `PASS_WITH_LIMITATIONS` — compact structure achieved, length target exceeded |

The same prompts were used for baseline and reruns. Reruns preserved model-class routing, evidence rules, Judge/Revisor gates, deterministic-calculation handoff, controlled-refactor gate, honest `NOT RUN`, acceptance, and rollback.

## Deterministic validation

Final validation after the accepted edits:

- `python3 -m pytest -q tests/test_validation_scripts.py tests/test_thinking_thinkers_integration.py tests/test_thinkers_os_integration.py`: `53 passed in 0.70s`; independently parsed as passed by Local Developer Worker run `RUN-dc019e6ecef2aa7c` with observed exit code `0` and `command_observed=true`.
- `scripts/check_project_instructions_length.py`: PASS for all 126 instruction files; `[LLM]` is 5,095 characters and `[Codex]` is 7,809 characters.
- `scripts/check_repo_public_safety.py`: PASS.
- `scripts/check_codex_goal_mode_defaults.py`: PASS.
- `scripts/check_knowledge_bundles.py`: PASS for 7 projects and 33 bundles.
- `scripts/check_index_coverage.py`: PASS.
- iteration register JSON parsing: PASS.
- `git diff --check`: PASS.
- `scripts/check_manifest_paths.py`: FAIL with 14 extra `PROJECT_INSTRUCTIONS.md` findings, all under the two pre-existing untracked worktrees `.codex/worktrees/analytics-sms-pr/` and `.codex/worktrees/analytics-variance-contract/`. None is an edited project instruction or report from this task; this remains visible as a repository-level pre-existing limitation.

Final read-only repository facts were captured by Local Developer Worker run `RUN-a444703c24432b88`; the lineage-complete evidence package is `RUN-156c500759bbf136`.

The repository was already dirty and contains unrelated Analytics, LLM lifecycle, Thinkers OS, worktree, script, and test changes. This task did not overwrite, stage, commit, or merge them.

## External state

Baseline prompts were sent once per project. ChatGPT temporarily rate-limited rapid requests after several cases; completed independent cases were not resent. External Project settings synchronization passed read-back after a full project-page reload: `[LLM]` contained the near-4,000-character adaptive-depth rule and `[Codex]` contained the near-2,500-character missing-object fast path.

## Requirements traceability

| Requirement | Implementation location | Evidence | Final status |
|---|---|---|---|
| Use AI-OS methodology | canonical routing/context handoff | one owner resolved to `[AI OS]`; seven project contracts loaded | PASS |
| Run full live test | external ChatGPT Projects | seven baseline cases completed | PASS |
| Evaluate answer quality | this report | five-dimension rubric and 64/70 baseline | PASS |
| Improve observed defects | `[LLM]` and `[Codex]` Project Instructions | two bounded corrective iterations; 22.5% and 51.9% reductions | PASS_WITH_LIMITATIONS |
| Preserve safety/routing | unchanged semantic contracts | no regression observed in affected reruns | PASS |
| Update external instructions | ChatGPT Project settings | post-reload read-back | PASS |
| AES/autoloop | iteration register | baseline → validate → fix → rerun → revalidate | PASS |

## Acceptance

| Scope | Status |
|---|---|
| baseline coverage | PASS |
| routing and safety | PASS |
| evidence and limitations | PASS |
| local corrective instructions | PASS |
| external settings sync | PASS |
| affected live reruns | PASS_WITH_LIMITATIONS |
| rollback readiness | PASS |
| overall delivery | PASS_WITH_LIMITATIONS |

The limitation is non-critical: verbosity remains above the explicit targets, but the responses are materially shorter and the task's safety, routing, evidence, and actionability criteria are satisfied. A third automatic prompt restriction is not applied because AES stops the same recurring defect after two corrective attempts; further reduction would require an explicit product decision to remove or redesign required answer sections.

## LLM-only optimization cycle 2

Sergey explicitly authorized a new LLM-only cycle after the earlier AES stop. The response contract was redesigned without changing evidence, Judge/Revisor, deterministic-calculation, or implementation-routing semantics:

- the mandatory six-section default was replaced by `direct`, `compact asset`, and explicit `expanded` modes;
- a compact asset is limited to one recommendation, one prompt block, one table of at most five rows, one minimal registry record, and at most three closing bullets;
- repetition, process diagrams, field-by-field explanations, and unrequested expansion are forbidden by default.

External `[LLM]` Project Instructions were updated and verified after reload: 5,332 characters, the new `compact asset` contract present, and the old `1. Recommended workflow` contract absent.

The exact high-risk baseline prompt was rerun in the in-app Codex browser. The response decreased from about 10,201 to 3,947 characters (`61.3%`) while preserving `prompt_id`, conditional revise, `[Analytics]` calculation routing, `[Codex]` implementation routing, model-class routing, quality gate, registry candidate status, limitations, and confidence. Verdict: `PASS` for the targeted verbosity defect and semantic regression gate.

A second direct-mode prompt was rerun after the temporary rate limit cleared. The completed response was 702 characters, selected the `fast` model class, supplied exactly one quality gate, stated confidence, and did not expand into a full workflow. Verdict: `PASS` for the direct-mode contract.

Focused validation after this LLM-only edit: `tests/test_validation_scripts.py` — 19 passed, independently parsed by Local Developer Worker run `RUN-190126b390a0e3d1`; instruction length — 126/126 pass; public safety, Knowledge bundles (7 projects / 33 bundles), index coverage, and `git diff --check` — pass. LLM-only cycle status: `PASS`.

Final lineage-complete evidence package: `RUN-7b96eaf71450af8c`, status `success`, with no missing evidence. The interim `RUN-0436948ce1fd5019` was `partial` while the direct-mode case was missing. The earlier `RUN-9d2a2a47ca7e0324` was rejected as `invalid_input` because of a repository-path typo; neither interim run is final acceptance evidence.
