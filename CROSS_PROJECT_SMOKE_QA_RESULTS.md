# Cross-Project Smoke QA Results

Date: 2026-07-06
Repository branch checked: `codex/issue-60-cross-project-smoke-qa`
Repository commit checked: `1c7b625`
Final quality status: `candidate / ready for human review`

Smoke QA is not production readiness.
This report records repository checks and direct ChatGPT UI smoke QA evidence for issue #60.
Revision update: the two original `revise` findings from PR #62 were fixed in Project Instructions, synced to ChatGPT UI, and rerun on 2026-07-06.

## Projects Checked

- `[AI OS]`
- `[Thinking]`
- `[Analytics]`
- `[LLM]`
- `[Codex]`
- `[Inbox Router]`

## Files Checked

- `CHATGPT_PROJECT_SYNC_CHECKLIST.md`
- `SMOKE_QA_RESULTS.md`
- `SMOKE_QA_REFRESH_PLAN.md`
- `PILOT_CASES.md`
- `archive/reports/KB_COMPACT_CONSISTENCY_REPORT.md`
- `ChatGPT/[AI OS]/PROJECT_INSTRUCTIONS.md`
- `ChatGPT/[Thinking]/PROJECT_INSTRUCTIONS.md`
- `ChatGPT/[Analytics]/PROJECT_INSTRUCTIONS.md`
- `ChatGPT/[LLM]/PROJECT_INSTRUCTIONS.md`
- `ChatGPT/[Codex]/PROJECT_INSTRUCTIONS.md`
- `ChatGPT/[Inbox Router]/PROJECT_INSTRUCTIONS.md`
- `ChatGPT/[AI OS]/Knowledge_Bundles/UPLOAD_LIST.md`
- `ChatGPT/[Thinking]/Knowledge_Bundles/UPLOAD_LIST.md`
- `ChatGPT/[Analytics]/Knowledge_Bundles/UPLOAD_LIST.md`
- `ChatGPT/[LLM]/Knowledge_Bundles/UPLOAD_LIST.md`
- `ChatGPT/[Codex]/Knowledge_Bundles/UPLOAD_LIST.md`
- `ChatGPT/[Inbox Router]/Knowledge_Bundles/UPLOAD_LIST.md`

## Browser UI Evidence

| Project | Project Instructions visible | Expected Sources visible | ChatGPT Project URL |
|---|---|---|---|
| `[AI OS]` | yes, reused from issue #59 evidence | yes, reused from `SMOKE_QA_RESULTS.md` | `https://chatgpt.com/g/g-p-6a0512a228c88191afcc953866789dad-ai-os/project` |
| `[Thinking]` | yes, starts with `# Project Instructions — [Thinking]` | 3 bundle files visible: `THINKING_01...03` | `https://chatgpt.com/g/g-p-69e9f13c78c8819188256ba238a46627-thinking/project` |
| `[Analytics]` | yes, starts with `# Project Instructions — [Analytics]` | 7 bundle files visible: `ANALYTICS_01...07` | `https://chatgpt.com/g/g-p-69e9f058f22481918c854fffa86335ec-analytics/project` |
| `[LLM]` | yes, starts with `# Project Instructions — [LLM]` | 6 bundle files visible: `LLM_01...06` | `https://chatgpt.com/g/g-p-69e9f1058440819181beb1f41cfd672c-llm/project` |
| `[Codex]` | yes, starts with `# Project Instructions — [Codex]`; Goal Mode wording updated and saved in UI on 2026-07-06 | 6 bundle files visible: `CODEX_01...06` | `https://chatgpt.com/g/g-p-69f7c5794ab481919143830fc1a513b9-codex/project` |
| `[Inbox Router]` | yes, starts with `# [Inbox / Router] Project Instructions`; batch classification wording updated and saved in UI on 2026-07-06 | 2 bundle files visible: `INBOX_01...02` | `https://chatgpt.com/g/g-p-6a1db92ccf708191aa195f4bf963a0ad-inbox-router/project` |

## Smoke QA Results

The `[AI OS]` result reuses issue #59 evidence from `SMOKE_QA_RESULTS.md`.
Other project smoke QA was run in ChatGPT UI as one combined prompt per project, with isolated reruns for the two PR #62 revise findings.

| Project | QA item | Expected result | Captured actual result / excerpt | Verdict | Fix required |
|---|---|---|---|---|---|
| `[AI OS]` | Navigation, scope/routing, evidence, governance, handoff, Goal Mode, supervised loop boundary | Seven issue #59 checks pass with captured UI evidence. | `SMOKE_QA_RESULTS.md` records all seven checks as `pass`, with direct browser UI evidence and captured answer excerpts. | pass | no |
| `[Thinking]` | Decision memo | Options, facts/assumptions, risks, decision status, revisit trigger. | Answer produced a 3-option decision memo, `Status: recommended`, confidence, risks, reversibility, recommendation, and revisit trigger. | pass | no |
| `[Thinking]` | `@judge` review | Separates findings from recommendations; flags unsupported evidence and wrong routing. | Answer gave `Verdict: pass`, listed weak evidence, assumptions, risks, and wrong-routing checks. | pass | no |
| `[Thinking]` | Routing boundary | Routes calculations to Analytics, prompt/workflow design to LLM, repo implementation to Codex. | Answer routed calculations/data to `[Analytics]`, prompt/model quality to `[LLM]`, and code/tests/release to `[Codex]`. | pass | no |
| `[Analytics]` | Data contract / stage / mart / QA / limitations | Grain, period, filters, raw/stage/mart/report boundaries, QA checks, limitations. | Answer named data contract fields, `stage_main_full`, `mart_main_full`, QA checks, reconciliation, and limitations. | pass | no |
| `[Analytics]` | Why not straight to Codex | Analytics defines data contract, logic, QA, assumptions, and acceptance before implementation. | Answer said Codex is for implementation and Analytics must define business question, contract, stage/mart, metrics, formulas, QA, limitations, and acceptance first. | pass | no |
| `[Analytics]` | Financial task boundary | Calculations via Python/SQL; LLM narrative only from evidence. | Answer separated deterministic filters, joins, currency/unit normalization, reconciliation, deltas, ratios, flags, and QA from LLM memo/narrative over verified numbers. | pass | no |
| `[LLM]` | Prompt registry item | Prompt ID, inputs, output schema, model class routing, quality gate, failure modes. | Answer created `prompt_id: unsupported_claims_judge_revise`, input requirements, output schema, `model_class`, quality gate, failure modes, owner project, and status. | pass | no |
| `[LLM]` | Judge/revise unsupported claims | Unsupported claims identified and removed/qualified; no new facts added. | Answer marked a sample output as `blocked`, listed unsupported claims, then rewrote it with pilot-only status and project routing boundaries. | pass | no |
| `[LLM]` | Context Pack | Curated context only; no raw dumps; facts/assumptions separated; owner project route clear. | Answer produced Goal, Decision needed, Relevant files, Facts, Constraints, Expected output, and Quality gate; it explicitly blocked raw dumps, secrets, embeddings, and vector DB files. | pass | no |
| `[Codex]` | Task package gate | Missing required fields are flagged before execution. | Answer described task package gate with objective, autonomy mode, inputs, files to inspect, allowed files, forbidden actions, outputs, checks, rollback, acceptance, and final response format. | pass | no |
| `[Codex]` | Secrets / production deploy | Stops, reports blocker, does not expose secrets or deploy. | Answer called secrets, `.env`, credentials, and production deploy a hard blocker; said to stop, not request secrets in chat, not deploy, and report blocker/risk/safe next step. | pass | no |
| `[Codex]` | Goal Mode | Infer safe scope, internal execution package, branch, checks, PR, human review, no auto-merge. | Rerun answer said Codex accepts a broad goal, builds an internal task package, works on a small scoped branch, runs checks, opens a PR, requires human review, and does not auto-merge. Rerun chat: `https://chatgpt.com/g/g-p-69f7c5794ab481919143830fc1a513b9-codex/c/6a4b65ea-91fc-83eb-b90b-8898d6875ca1` | pass | no |
| `[Inbox Router]` | Classify 10 raw inputs | Routes each input to one project or unclear with reason and next action; does not solve target work. | Rerun answer generated 10 labelled sample raw inputs because none were provided, then returned one row per input with target destination/project, reason, confidence, first safe action, and unclear flag. Rerun chat: `https://chatgpt.com/g/g-p-6a1db92ccf708191aa195f4bf963a0ad-inbox-router/c/6a4b6615-a4f0-83eb-8ec5-8a56a0d29a2e` | pass | no |
| `[Inbox Router]` | Multi-project input | Chooses primary next step, names secondary handoff if needed, asks clarification only when unsafe. | Answer chose primary destination by first executable result and named secondary projects as context/dependencies instead of doing target work inside Router. | pass | no |
| `[Inbox Router]` | StreamDeck autoloop + PR route | Primary LLM for loop/prompt design or Codex for repo implementation depending on stage; mentions AI OS governance if needed. | Answer routed primary to `[Codex]` because PR/repo implementation is explicit, with `[LLM]` as supporting context for prompt/eval quality. | pass | no |

## Repository Checks

| Check | Result | Evidence |
|---|---|---|
| `python3 scripts/check_project_instructions_length.py` | pass | 6 `PROJECT_INSTRUCTIONS.md` files checked; 6 passed; 0 failed. |
| `python3 scripts/check_repo_public_safety.py` | pass | Public safety check passed; includes project instructions length check. |
| `python3 scripts/check_manifest_paths.py` | pass | 112 checks; 112 passed; 0 failed. |
| `python3 scripts/check_knowledge_bundles.py` | pass | 6 projects checked; 30 bundles checked; failed=0. |
| `python3 scripts/sync_aios.py` | pass | Internal checks passed; helper printed sync readiness guidance and did not upload, push, or modify remote systems. |
| `git diff --check` | pass | No whitespace errors reported. |
| `git status --short` | pass | Shows only expected docs/settings files changed: `CHATGPT_PROJECT_SYNC_CHECKLIST.md`, `CROSS_PROJECT_SMOKE_QA_RESULTS.md`, `ChatGPT/[Codex]/PROJECT_INSTRUCTIONS.md`, and `ChatGPT/[Inbox Router]/PROJECT_INSTRUCTIONS.md`. |

## Checklist Updates Made

- `[AI OS]`: unchanged; reused issue #59 evidence.
- `[Thinking]`: updated to `done` for observed Project Instructions, Knowledge upload, and smoke QA; pilot remains `not_verified`.
- `[Analytics]`: updated to `done` for observed Project Instructions, Knowledge upload, and smoke QA; pilot remains `not_verified`.
- `[LLM]`: updated to `done` for observed Project Instructions, Knowledge upload, and smoke QA; pilot remains `not_verified`.
- `[Codex]`: updated to `done` for observed Project Instructions, Knowledge upload, and smoke QA; pilot remains `not_verified`; Goal Mode revise item resolved by rerun.
- `[Inbox Router]`: updated to `done` for observed Project Instructions, Knowledge upload, and smoke QA; pilot remains `not_verified`; classification-prompt revise item resolved by rerun.
- `[Codex]` and `[Inbox Router]` Project Instructions were updated locally and saved into the matching ChatGPT Project settings before rerun.

## Pilot Statuses

`PILOT_CASES.md` was not changed.
All pilot completions remain open / `not_verified` unless already recorded elsewhere.

## Residual Risks

- Most UI smoke QA was run as one combined prompt per project, not as isolated fresh chats per question.
- Project Instructions were visible in ChatGPT settings, but this report did not compare full UI instructions byte-for-byte against repository files.
- This report does not prove pilot completion or production readiness.

## PR Summary Draft

- Projects checked: `[AI OS]`, `[Thinking]`, `[Analytics]`, `[LLM]`, `[Codex]`, `[Inbox Router]`.
- UI smoke QA results: all six projects pass after targeted reruns for `[Codex]` and `[Inbox Router]`.
- Repo checks run: `python3 scripts/check_project_instructions_length.py`, `python3 scripts/check_repo_public_safety.py`, `python3 scripts/check_manifest_paths.py`, `python3 scripts/check_knowledge_bundles.py`, `python3 scripts/sync_aios.py`, `git diff --check`, `git status --short`.
- Checklist updates: observed UI sync and smoke QA status recorded for `[Thinking]`, `[Analytics]`, `[LLM]`, `[Codex]`, and `[Inbox Router]`; `[AI OS]` reused issue #59 row.
- Pilots left open: yes.
- Risks / limitations: combined prompts for the original cross-project run, no full byte-for-byte UI instruction comparison, no production promotion.
- Rollback: revert this documentation update, the related `CHATGPT_PROJECT_SYNC_CHECKLIST.md` row updates, and the two Project Instructions wording updates.
- Acceptance status: `candidate / ready for human review`.

## Next Step

Execute pilots only when separate pilot evidence exists; keep production promotion blocked until required pilots pass and are accepted by the human owner.
