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
