# Local-First Compute P0 Capability Audit — 2026-08-31

- Issue: [#345](https://github.com/sergstack/AI-OS/issues/345)
- AI-OS baseline: `origin/main` at `abd2346`
- AI-OS owner: `[AI OS]`
- Mechanics owner: `sergstack/local-developer-worker`
- Evidence status: repository and observed-tool evidence; no production promotion

## Verdict

Current AI-OS and LDW already provide the core deterministic boundaries for
progressive disclosure, verification, and adaptive routing. The remaining
gaps are partial: there is no general loss-aware semantic compactor, the real
local-first allowlist is empty, and telemetry does not by itself provide the
matched quality/economics evidence required for promotion. No material gap
requires a new worker or runtime.

## Capability matrix

Each capability has exactly one P0 classification.

| Capability | Classification | Current evidence | Gap / decision |
| --- | --- | --- | --- |
| Progressive disclosure | `already sufficient` | `ldw context pack` records selected/excluded paths and byte reduction; bounded expansion requires the previous package plus a reason or deterministic trigger. AI-OS `CONTEXT_PACK_STANDARD.md` preserves goal, facts, authority provenance, constraints, and quality gate. | No new mechanism. Use the existing pack/expand contract. |
| Summarization / context compaction | `partial gap` | LDW can select source context and render facts-only evidence reports. AI-OS already defines source-reference and authority-provenance rules. | No general semantic compactor currently proves preservation of every goal/requirement/defect/authority field. Keep semantic summaries candidate-only; use the preservation contract in the new policy before any later pilot. |
| Local offload | `partial gap` | `ldw ollama advise` is read-only, loopback-verified, schema-bounded, and candidate-only. Its synthetic terminal-triage pilot established a technical shape. | The evidence-backed production allowlist is empty; no representative real-task matched study exists. Do not add another worker. |
| Adaptive model routing | `already sufficient` | `ldw codex run` has policy-owned aliases, deterministic task signals, risk floors, escalation/fallback, and privacy-safe routing telemetry. Offline contracts and controlled read-only smokes exist. | Provider-side model/effort echo remains unverified, and a deployment policy may block execution. These are evidence/deployment limits, not a missing AI-OS router. |
| Deterministic verification | `already sufficient` | LDW has authoritative test parsing, Git facts, schema validation, evidence lineage, portfolio gates, and deterministic terminal-verifier boundaries. | Preserve deterministic authority; do not replace it with model interpretation. |
| Tool/context telemetry | `partial gap` | LDW records privacy-safe status, latency, input/output bytes, fallback, context reduction, routing profile, and observable Codex token counters. | False acceptance, semantic quality, manual attention, local compute burden, and matched task outcome require explicit evaluation records; absent metrics stay unknown. |

## Source evidence

AI-OS sources:

- `docs/standards/CONTEXT_PACK_STANDARD.md`
- `docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md`
- `ChatGPT/[AI OS]/Knowledge/GOVERNANCE_RULES.md`
- `ChatGPT/[AI OS]/Knowledge/AI_EVAL_REGISTRY.md`
- `ChatGPT/[LLM]/Knowledge/LOCAL_AI_SECURITY_BOUNDARY.md`
- `ChatGPT/[LLM]/Knowledge/LOCAL_MODEL_EVAL_MATRIX.md`

LDW sources inspected read-only:

- `README.md`
- `docs/tool-contracts.md`
- `docs/ollama-advisory-effect-study.md`
- `docs/context-efficiency-final-study.md`
- `docs/adaptive-codex-routing/acceptance.md`
- `docs/telemetry.md`
- `src/local_developer_worker/tools.py`

Observed during this execution:

- `ldw doctor`: success, `RUN-b880bf9c37d1e616`.
- Adaptive `ldw codex run`: `policy_blocked`,
  `RUN-8f48f3053d4b7be4`; no child execution occurred.
- AI-OS context pack: success, `RUN-7d96d75ae80fc3b1`, with 30.58%
  byte-based candidate reduction. This is not a token-savings claim.
- File inventory: `partial`, `RUN-040fa2f972d4b6f0`; sensitive/ignored
  candidates were not treated as usable context.

## P1 decision

The policy and machine-readable registry may proceed as candidate governance
artifacts. No class is promoted to `local_first`. The first eligible real
pilot remains high-volume semantic terminal triage with a terminal
deterministic verifier, because LDW already exposes that bounded primitive.

A separate LDW issue should validate the cross-repository registry/handoff and
design an owner-approved matched real-task study. It must not implement a new
worker, weaken verification, or promote a class from synthetic evidence.

The related mechanics handoff already exists as
[`sergstack/local-developer-worker#56`](https://github.com/sergstack/local-developer-worker/issues/56).
Its P0 audit is proposed in
[`sergstack/local-developer-worker#57`](https://github.com/sergstack/local-developer-worker/pull/57);
that PR is open and its GitHub `test` check was observed successful on
2026-08-31. This is candidate cross-repository evidence until owner review and
merge; it does not change the empty AI-OS allowlist.

## Gates and rollback

- P1 policy/registry: candidate, ready for owner review.
- Real allowlist promotion: not authorized.
- Automated policy-assisted routing: not authorized.
- Production: not authorized.
- Rollback: revert the policy/registry/schema/test/evidence commit and rebuild
  generated bundles; LDW mechanics and historical evidence remain unchanged.
