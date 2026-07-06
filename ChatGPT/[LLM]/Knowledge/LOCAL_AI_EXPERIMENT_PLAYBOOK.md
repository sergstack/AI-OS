# Local AI Experiment Playbook

## Purpose

Define controlled use of local models, Ollama, Open WebUI, and a home AI server as an experiment layer.

Local AI is for private drafts, local context exploration, retrieval pilots, prompt tests, and non-critical generation. It is not production truth, not a production backbone, and not a replacement for AI-OS governance, Analytics calculations, or Codex implementation checks.

## Ownership

- `[LLM]` owns local model prompting, context preparation, model-class routing, judge/revise, and limitations.
- `[AI OS]` owns AI evidence, governance, supported / weak / unsupported labels, and promotion gates.
- `[Analytics]` owns data, marts, deterministic calculations, reconciliations, formulas, and analytical QA.
- `[Thinking]` owns hardware buying decisions, RTX 3090 tradeoffs, cost/risk memos, and scenario decisions.
- `[Codex]` owns repo changes, scripts, tests, checks, branches, and PRs.

## Allowed Uses

- private draft generation;
- summarization over curated excerpts;
- prompt experiments;
- local retrieval pilot with reviewed source excerpts;
- memo wording from verified facts;
- model comparison using lightweight examples;
- offline/private exploration when sensitive context is approved for local use.

## Workflow

```text
goal
-> decide owner project
-> prepare compact context
-> remove forbidden inputs
-> run local draft or retrieval pilot
-> copy only relevant retrieved excerpts
-> judge / revise
-> record limitations
-> decide next step
```

## Rules

- Local retrieval is not final truth.
- Local model output is draft until checked.
- Use curated excerpts, not raw dumps.
- Run judge/revise before using output in memo, decision, handoff, or repo task.
- State limitations for local model output.
- Route calculations, reconciliation, formulas, and metric logic to `[Analytics]`.
- Route implementation and repo changes to `[Codex]`.
- Route hardware and RTX 3090 purchase/setup decisions to `[Thinking]`.

## Forbidden

Do not add or recommend:

- production automation;
- autonomous retrieval;
- vector DB;
- embeddings;
- semantic search;
- web UI production workflow;
- MCP tools;
- production agentic workflow;
- runtime artifact stores.

Do not send as local model input:

- secrets;
- `.env`;
- credentials;
- API keys;
- production data;
- raw financial dumps without explicit approval;
- raw logs;
- runtime artifacts.

## Output Format

```text
Local AI status:
Use case:
Model / surface:
Context used:
Checks:
Judge / revise:
Limitations:
Security notes:
Next step:
```
