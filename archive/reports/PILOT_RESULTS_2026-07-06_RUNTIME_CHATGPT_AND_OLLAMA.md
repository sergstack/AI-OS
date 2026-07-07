# Runtime Pilot Results — ChatGPT Projects and Ollama/Open WebUI

Review date: 2026-07-06

Issue: GitHub #68

Branch: `codex/issue-68-runtime-pilot`

Base dependency: this branch was created from `codex/issue-66-project-folder-pilot-qa` because issue #68 depends on the pilot metadata/template work from PR #67.

Method: live ChatGPT Project smoke prompts were sent through the in-app browser. Ollama/Open WebUI checks used local non-sensitive API/HTTP probes only. No secrets, private files, credentials, production data, financial raw data, autonomous retrieval, vector DB, semantic search index, web UI production setup, uncontrolled agents, or background automation were used.

Limitation: live ChatGPT chat URLs are private browser state and are not committed to this public repository. Results below summarize observed behavior.

## Questions Asked Metric

Target: approximately 0 questions from the agent for reversible in-scope work.

| Pilot scope | Questions asked by agent | Hard blocker? | Instruction gap | Change made / issue |
|---|---:|---|---|---|
| Live ChatGPT Project smoke QA + Ollama/Open WebUI pilot | 0 | no | none observed | none |

Interpretation: this pilot run did not expose an ask-less instruction gap. Future
pilot results should record any agent question here, classify whether it was a
true hard blocker, and link the resulting instruction update or issue.

## Live ChatGPT Project Smoke QA

### `[AI OS]`

Pilot ID: `PILOT-AIOS-001`
Date: 2026-07-06
Project: `[AI OS]`
Owner project: `[AI OS]`
Pilot status: candidate
Manifest/upload status: ChatGPT Project runtime available in browser; repository settings source remains `ChatGPT/[AI OS]/PROJECT_INSTRUCTIONS.md` and Knowledge bundles.
Owner: Sergey
Input: universal runtime smoke prompt from issue #68.
Expected behavior: checks KB/evidence and routes calculations, prompts, decisions, and implementation to owner projects.
Observed behavior: identified itself as AI expert/research advisor for AI trends, patterns, governance, KB evidence, and practical use cases; routed decisions to `[Thinking]`, deterministic finance to `[Analytics]`, prompts/workflows/model routing to `[LLM]`, and repo/code/PR work to `[Codex]`; blocked embeddings, semantic search, vector DB, web UI, and autonomous retrieval as current implementation until acceptance/promotion gate.
Evidence: live ChatGPT response observed in `[AI OS]` project runtime.
Checks run: live smoke prompt submitted through in-app browser.
Verdict: pass
Required fixes: none
Residual risks: live response references current Project runtime state only; future manual upload/sync can drift.
Next step: keep candidate status until human review and periodic live smoke QA.

### `[Thinking]`

Pilot ID: `PILOT-THINKING-001`
Date: 2026-07-06
Project: `[Thinking]`
Owner project: `[Thinking]`
Pilot status: candidate
Manifest/upload status: ChatGPT Project runtime available in browser; repository settings source remains `ChatGPT/[Thinking]/PROJECT_INSTRUCTIONS.md` and Knowledge bundles.
Owner: Sergey
Input: universal runtime smoke prompt from issue #68.
Expected behavior: handles decision framing, assumptions, options, downside, reversibility, and revisit triggers.
Observed behavior: identified strategy/options/risks/decision memo/judge-revisor role; routed calculations to `[Analytics]`, prompts/model routing/LLM quality to `[LLM]`, implementation/tests/release to `[Codex]`, and AI concepts/supported KB patterns to `[AI OS]`; blocked premature automation and production promotion without pilot evidence.
Evidence: live ChatGPT response observed in `[Thinking]` project runtime.
Checks run: live smoke prompt submitted through in-app browser.
Verdict: pass
Required fixes: none
Residual risks: live response references current Project runtime state only; future manual upload/sync can drift.
Next step: keep candidate status until human review and periodic live smoke QA.

### `[Analytics]`

Pilot ID: `PILOT-ANALYTICS-001`
Date: 2026-07-06
Project: `[Analytics]`
Owner project: `[Analytics]`
Pilot status: candidate
Manifest/upload status: ChatGPT Project runtime available in browser; repository settings source remains `ChatGPT/[Analytics]/PROJECT_INSTRUCTIONS.md`, `package_manifest.json`, and Knowledge bundles.
Owner: Sergey
Input: universal runtime smoke prompt from issue #68.
Expected behavior: requires deterministic data contract, period, grain, metrics, formulas, QA, and does not use LLM arithmetic as source of truth.
Observed behavior: identified Analytics Factory flow from question to data contract, stage, mart, deterministic calculation, findings, memo, QA, and acceptance; routed implementation to `[Codex]`, strategy to `[Thinking]`, prompt/model workflow to `[LLM]`, and AI evidence/patterns to `[AI OS]`; required deterministic calculations before memo and blocked unsupported management conclusions.
Evidence: live ChatGPT response observed in `[Analytics]` project runtime.
Checks run: live smoke prompt submitted through in-app browser.
Verdict: pass
Required fixes: none
Residual risks: live response references current Project runtime state only; future manual upload/sync can drift.
Next step: keep candidate status until human review and periodic live smoke QA.

### `[LLM]`

Pilot ID: `PILOT-LLM-001`
Date: 2026-07-06
Project: `[LLM]`
Owner project: `[LLM]`
Pilot status: candidate
Manifest/upload status: ChatGPT Project runtime available in browser; repository settings source remains `ChatGPT/[LLM]/PROJECT_INSTRUCTIONS.md` and Knowledge bundles.
Owner: Sergey
Input: universal runtime smoke prompt from issue #68.
Expected behavior: owns prompts, context packs, workflow orchestration, model routing, judge/revisor flow, and routes calculations/implementation away.
Observed behavior: identified prompt/context/model routing/LLM quality/judge-revise/Codex-safe handoff role; routed AI concepts to `[AI OS]`, deterministic finance to `[Analytics]`, decisions to `[Thinking]`, and code/repo implementation to `[Codex]`; blocked embeddings, vector DB, semantic search indexes, web UI production workflow, autonomous retrieval, production automation, runtime artifact stores, secrets, raw logs, and full dumps.
Evidence: live ChatGPT response observed in `[LLM]` project runtime.
Checks run: live smoke prompt submitted through in-app browser.
Verdict: pass
Required fixes: none
Residual risks: live response references current Project runtime state only; future manual upload/sync can drift.
Next step: keep candidate status until human review and periodic live smoke QA.

### `[Codex]`

Pilot ID: `PILOT-CODEX-001`
Date: 2026-07-06
Project: `[Codex]`
Owner project: `[Codex]`
Pilot status: candidate
Manifest/upload status: ChatGPT Project runtime available in browser; repository settings source remains `ChatGPT/[Codex]/PROJECT_INSTRUCTIONS.md` and Knowledge bundles.
Owner: Sergey
Input: universal runtime smoke prompt from issue #68.
Expected behavior: requires goal/scope/allowed files/checks/rollback/PR/human review and does not auto-merge.
Observed behavior: identified implementation/refactor/bugfix/tests/smoke QA/acceptance/release-rollback role; routed strategy to `[Thinking]`, data/metrics/calculations to `[Analytics]`, AI concepts/evidence/governance to `[AI OS]`, and prompts/workflows/model routing/evals to `[LLM]`; required scoped branch, remote/status verification, allowed-path edits, checks, commit/push/PR only when requested, no direct main merge, and human review.
Evidence: live ChatGPT response observed in `[Codex]` project runtime.
Checks run: live smoke prompt submitted through in-app browser.
Verdict: pass
Required fixes: none
Residual risks: live response references current Project runtime state only; future manual upload/sync can drift.
Next step: keep candidate status until human review and periodic live smoke QA.

### `INBOX Router`

Pilot ID: `PILOT-INBOX-001`
Date: 2026-07-06
Project: `INBOX Router`
Owner project: `[Inbox Router]`
Pilot status: candidate
Manifest/upload status: ChatGPT Project runtime available in browser; repository settings source remains `ChatGPT/[Inbox Router]/PROJECT_INSTRUCTIONS.md` and Knowledge bundles.
Owner: Sergey
Input: universal runtime smoke prompt from issue #68.
Expected behavior: classifies/routes quickly and does not over-solve owner-project work.
Observed behavior: identified capture/classify/clarify/route/next-action role; routed AI concepts to `[AI OS]`, decisions to `[Thinking]`, data/metrics/reconciliations to `[Analytics]`, prompts/workflows/evals to `[LLM]`, code/tests/repo changes to `[Codex]`, hard time slots to Calendar, and concrete actions to Things; stated it must not calculate or write owner-project outputs.
Evidence: live ChatGPT response observed in `INBOX Router` project runtime.
Checks run: live smoke prompt submitted through in-app browser.
Verdict: pass
Required fixes: none
Residual risks: live response references current Project runtime state only; future manual upload/sync can drift.
Next step: keep candidate status until human review and periodic live smoke QA.

## Ollama / Open WebUI Pilot

Pilot ID: `PILOT-LLM-OLLAMA-001`
Date: 2026-07-06
Project: Ollama / Open WebUI
Owner project: `[LLM]`
Pilot status: candidate
Manifest/upload status: source guidance is `ChatGPT/[LLM]/Knowledge/OLLAMA_OPENWEBUI_PILOT.md`; upload bundle excerpt is `ChatGPT/[LLM]/Knowledge_Bundles/LLM_06_LOCAL_AI_EXPERIMENTS.md`.
Owner: Sergey
Input: non-sensitive local prompt: "Safe local pilot. In one sentence, say whether local models should be treated as draft/candidate output until reviewed."
Expected behavior: confirms local models are draft/candidate until reviewed; no private data required; no production automation introduced.
Observed behavior:
- Ollama API reachable at `http://127.0.0.1:11434`; `/api/version` returned `0.30.10`.
- `ollama` CLI was not found in shell `PATH`, but the API was available.
- `/api/tags` listed local completion models including `qwen2.5:7b-instruct`, `phi4:latest`, `mistral-small:latest`, `qwen2.5-coder:32b`, `deepseek-r1:32b`, plus embedding/reranker models.
- `qwen2.5:7b-instruct` responded that local models should be treated as draft/candidate output until reviewed for accuracy and safety.
- `phi4:latest` responded that local models should be treated as draft/candidate outputs until thoroughly reviewed and validated.
- Open WebUI reachable at `http://127.0.0.1:8080/ui/`; HTTP status `200`, content type `text/html`.
Evidence: observed command/API outputs from local checks.
Checks run:
- `command -v ollama && ollama --version && ollama list`
- `curl -sS --max-time 5 http://127.0.0.1:11434/api/version`
- `curl -sS --max-time 5 http://127.0.0.1:11434/api/tags`
- `curl -sS --max-time 60 http://127.0.0.1:11434/api/generate` with `qwen2.5:7b-instruct`
- `curl -sS --max-time 60 http://127.0.0.1:11434/api/generate` with `phi4:latest`
- `curl -sS -L --max-time 10 http://127.0.0.1:8080/ui/`
Verdict: pass
Required fixes: none
Residual risks:
- CLI is not in `PATH`; API access works.
- Open WebUI page was checked by HTTP only, not manually exercised in the browser UI.
- Embedding/reranker models are installed, but this pilot did not use embeddings, vector DB, semantic search, or retrieval.
- Candidate status remains appropriate; this does not promote local AI to production capability.
Next step: keep as candidate local experiment surface; require reviewed source context, judge/revise, and explicit human acceptance before any stronger status.

## Acceptance Status

Status: pass

All six live ChatGPT Project folders were accessible and produced role/routing/safety responses consistent with the repository QA baseline. Ollama and Open WebUI were safely checked with non-sensitive prompts and remain candidate local experiment surfaces, not production capabilities.

## Next Step

Open a draft PR for human review. Do not merge automatically.
