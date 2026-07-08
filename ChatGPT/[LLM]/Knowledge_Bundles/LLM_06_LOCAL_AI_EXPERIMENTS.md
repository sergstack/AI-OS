# [LLM] — Local AI Experiments

## Purpose

Compact upload artifact for `[LLM]` covering local AI, Ollama, Open WebUI, local model evals, and security boundaries as controlled experiments.

## Source files

- `ChatGPT/[LLM]/Knowledge/LOCAL_LLM_WORKFLOW.md`
- `ChatGPT/[LLM]/Knowledge/LOCAL_AI_EXPERIMENT_PLAYBOOK.md`
- `ChatGPT/[LLM]/Knowledge/OLLAMA_OPENWEBUI_PILOT.md`
- `ChatGPT/[LLM]/Knowledge/LOCAL_MODEL_EVAL_MATRIX.md`
- `ChatGPT/[LLM]/Knowledge/LOCAL_AI_SECURITY_BOUNDARY.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[LLM]`.

## Status

- bundle_type: compact upload artifact
- source_of_truth: granular files listed above
- production_promotion: no, unless explicitly accepted elsewhere
- source_fingerprint: sha256:48c271e649950953a816d0989974c45e82969a609f116122586865cd0f877edf
- local_ai_status: experiment / pilot only

---

# Content

## Local AI Experiment Playbook

Local AI is for private drafts, local context exploration, retrieval pilots, prompt tests, and non-critical generation. It is not production truth, not a production backbone, and not a replacement for AI-OS governance, Analytics calculations, or Codex implementation checks.

Workflow:

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

Rules:

- local retrieval is not final truth;
- local model output is draft until checked;
- use curated excerpts, not raw dumps;
- run judge/revise before using output in memo, decision, handoff, or repo task;
- state limitations for local model output;
- route hardware and RTX 3090 decisions to `[Thinking]` as decision memo.

## Ollama / Open WebUI Pilot

Owner project: `[LLM]`

Pilot status: `candidate`

Manifest/upload status: source file is `ChatGPT/[LLM]/Knowledge/OLLAMA_OPENWEBUI_PILOT.md`.

Residual risk: repository-file guidance only; local tool behavior still needs a recorded pilot result.

Ollama and Open WebUI are allowed as local experiment surfaces for draft generation, local model comparison, and curated excerpt exploration.

They are not production systems and do not replace source review, judge/revise, Analytics QA, or AI-OS evidence checks.

Pilot loop:

```text
prepare curated context
-> run local draft / retrieval pilot
-> keep relevant excerpts only
-> compare against source context
-> judge / revise
-> state limitations
-> decide pass / revise / blocked
```

Stop if output becomes final truth, sources are not traceable, forbidden inputs are needed, or the workflow requires autonomous retrieval, vector DB, embeddings, semantic search, MCP tools, or production automation.

## Local Model Eval Matrix

Evaluate local models with lightweight checks:

- context discipline;
- draft quality;
- retrieval pilot relevance;
- judge/revise support;
- security boundary;
- Analytics boundary;
- production boundary.

Use the same curated context for comparisons. Treat results as candidate evidence only. State limitations every time.

## Security Boundary

Do not send to local models or local AI tools:

- secrets;
- `.env`;
- credentials;
- API keys;
- production data;
- raw financial dumps without explicit approval;
- raw logs;
- runtime artifacts;
- production credentials;
- private client data unless explicitly approved and minimized;
- source-card dumps;
- raw transcripts unless explicitly scoped and sanitized;
- chunks;
- vector DB files;
- embedding stores;
- semantic search indexes.

Do not add:

- autonomous retrieval;
- vector DB;
- embeddings;
- semantic search;
- web UI production workflow;
- MCP tools;
- production automation;
- unattended agent loops;
- runtime artifact stores.

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
