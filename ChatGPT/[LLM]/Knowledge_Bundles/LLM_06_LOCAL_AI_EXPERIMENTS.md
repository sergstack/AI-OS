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

- production_promotion: no, unless explicitly accepted elsewhere
- local_ai_status: experiment / pilot only
- bundle_type: generated compact upload artifact
- source_of_truth: declared granular source files
- source_fingerprint: sha256:48c271e649950953a816d0989974c45e82969a609f116122586865cd0f877edf
- generator: scripts/build_knowledge_bundles.py

---

# Content

## From: `ChatGPT/[LLM]/Knowledge/LOCAL_LLM_WORKFLOW.md`

# Local LLM Workflow
## Purpose
Use local/Ollama/Open WebUI for drafts, retrieval experiments, private context exploration, or non-critical generation.
## Workflow
1. Prepare compact context.
2. Run retrieval or draft locally.
3. Copy relevant retrieved excerpts.
4. Send curated excerpts to ChatGPT for reasoning/synthesis if needed.
5. Judge output.
6. Record limitations.
## Do not
- treat local retrieval as final truth;
- upload secrets;
- rely on raw dump;
- skip source grounding;
- use local output as production fact without QA.

## From: `ChatGPT/[LLM]/Knowledge/LOCAL_AI_EXPERIMENT_PLAYBOOK.md`

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

## From: `ChatGPT/[LLM]/Knowledge/OLLAMA_OPENWEBUI_PILOT.md`

# Ollama / Open WebUI Pilot
## Purpose
Define safe pilot use of Ollama and Open WebUI.
Owner project: `[LLM]`
Pilot status: `candidate`
Manifest/upload status: source file for `ChatGPT/[LLM]/Knowledge_Bundles/LLM_06_LOCAL_AI_EXPERIMENTS.md`.
Residual risk: repository-file guidance only; local tool behavior still needs a recorded pilot result.
Ollama and Open WebUI are allowed as local experiment surfaces for draft generation, local model comparison, and curated excerpt exploration. They are not production systems and do not replace source review, judge/revise, Analytics QA, or AI-OS evidence checks.
## Pilot Scope
Allowed:
- load local model;
- test prompt behavior;
- draft from curated excerpts;
- compare local model outputs;
- explore approved local notes;
- prepare candidate text for `[LLM]` judge/revise.
Not allowed:
- autonomous retrieval;
- vector DB;
- embeddings;
- semantic search;
- web UI production workflow;
- production automation;
- MCP tools;
- unattended agent loop;
- source-of-truth decision without review.
## Input Rule
Use only curated excerpts and compact context.
Do not paste:
- secrets;
- `.env`;
- credentials;
- API keys;
- production data;
- raw financial dumps without explicit approval;
- raw logs;
- runtime artifacts;
- raw transcripts unless explicitly scoped and sanitized;
- source-card dumps;
- chunks.
## Pilot Loop
```text
prepare curated context
-> run local draft / retrieval pilot
-> keep relevant excerpts only
-> compare against source context
-> judge / revise
-> state limitations
-> decide pass / revise / blocked
```
## Acceptance Gate
Pilot output is usable only when:
- source context is named;
- output is marked draft or candidate;
- unsupported claims are listed;
- limitations are visible;
- judge/revise has been applied;
- deterministic claims have been routed to `[Analytics]`;
- production/repo work has been routed to `[Codex]`.
## Stop Conditions
Stop if:
- sources are not traceable;
- local retrieval contradicts source context;
- output is used as final truth;
- forbidden inputs are needed;
- production data or credentials are involved;
- the workflow requires autonomous retrieval, vector DB, embeddings, semantic search, MCP tools, or production automation.

## From: `ChatGPT/[LLM]/Knowledge/LOCAL_MODEL_EVAL_MATRIX.md`

# Local Model Eval Matrix
## Purpose
Evaluate local model usefulness with lightweight checklist evals.
This matrix is for pilots, not benchmark infrastructure. It does not add SWE-Bench, RAGAS, vector DB, embeddings, semantic search, autonomous eval agents, or production automation.
## Matrix
| Eval area | Check | Pass | Revise | Blocked |
|---|---|---|---|---|
| Context discipline | Uses curated excerpts | sources named and no raw dump | context needs trimming | requires forbidden inputs |
| Draft quality | Produces usable draft | clear draft with limitations | style or structure needs revision | unsupported claims dominate |
| Retrieval pilot | Finds relevant excerpts | excerpts trace to source | misses some evidence | treats retrieval as final truth |
| Judge/revise | Supports review loop | unsupported claims listed | judge criteria unclear | no review path |
| Security | Respects boundary | no secrets or production data | unclear data classification | secrets, `.env`, credentials, API keys, raw logs, or runtime artifacts needed |
| Analytics boundary | Does not calculate truth | routes calculations to `[Analytics]` | wording overstates numbers | performs unverified calculations |
| Production boundary | Stays experimental | no production automation | promotion criteria unclear | production workflow requested |
## Model Record
```text
model_or_surface:
use_case:
context_type:
sample_task:
result:
limitations:
security_status:
judge_verdict:
next_step:
```
## Comparison Rules
- Compare local models by task class, not by hype.
- Use the same curated context for each model.
- Keep outputs short enough to review.
- Treat results as candidate evidence only.
- Use judge/revise before reuse.
- State limitations every time.
## Hardware Notes
Hardware choices, including RTX 3090, home server budget, power/noise tradeoffs, and upgrade timing, belong in `[Thinking]` as a decision memo.
Do not embed hardware purchase decisions as main AI-OS setup or production architecture.

## From: `ChatGPT/[LLM]/Knowledge/LOCAL_AI_SECURITY_BOUNDARY.md`

# Local AI Security Boundary
## Purpose
Define the security boundary for local AI experiments.
Local AI can reduce external exposure, but local does not mean safe by default. Treat local models, Ollama, Open WebUI, home AI servers, downloaded models, browser UIs, and plugins as experimental surfaces.
## Forbidden Inputs
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
## Forbidden Capabilities
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
## Allowed Inputs
Allowed when scoped:
- curated excerpts;
- sanitized notes;
- synthetic examples;
- public docs;
- prompt drafts;
- verified Analytics outputs;
- non-sensitive local test data.
## Boundary Checks
Before a local AI run:
- Is the use case experimental?
- Is the context curated?
- Are secrets and credentials excluded?
- Is production data excluded?
- Are raw financial dumps excluded or explicitly approved?
- Is output marked draft/candidate?
- Is judge/revise planned?
- Are limitations required?
## Stop Conditions
Stop and reroute when:
- the task requires production data;
- security classification is unclear;
- source traceability is missing;
- local model output would become final truth;
- autonomous retrieval or production automation is required;
- hardware investment decisions are needed without `[Thinking]` review.
