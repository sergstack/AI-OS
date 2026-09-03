# Shared Standards

This directory contains active cross-repository standards and reusable
workflows. They apply across ChatGPT Project packages, Codex execution, and
GitHub delivery; they are not owned by one Project folder or the Codex APP
runtime layer.

Canonical root contracts remain in the repository root when they define the
primary entry flow, routing, or handoff semantics. Use the
[repository map](../REPOSITORY_MAP.md) to find the authoritative document for
each question.

Current cross-project policy standards include:

- `LOCAL_FIRST_COMPUTE_POLICY.md` — AI-OS eligibility, promotion, evidence,
  fallback, provenance, and rollback rules for local-model offload;
- `local_first_task_class_registry.json` — machine-readable initial class
  registry; its production `local_first` allowlist is empty.
- `AUTORESEARCH_V01_CONTRACT.md` — frozen v0.1 research boundary for issue
  [#388](https://github.com/sergstack/AI-OS/issues/388) (AIOS AutoResearch):
  mutable/protected surfaces, hard invariants, decision semantics, and role
  separation. Not authorized for Phase 0 or Phase 1 execution on its own.
- `autoresearch_v01_manifest.json` — its machine-readable protected-surface
  and hard-invariant manifest.
- `AUTORESEARCH_V02_LIVE_CONTRACT.md` — additive v0.2 live-execution,
  privacy, budget, and evidence contract for issue
  [#409](https://github.com/sergstack/AI-OS/issues/409) (AIOS AutoResearch
  v0.2): evidence states, transport/evaluator identity, budget/retry/
  privacy rules, authority boundaries, and hard stop conditions. Extends
  v0.1 without rewriting it; not authorized for any live call on its own.
- `autoresearch_v02_authority_matrix.json` — its fixed authority-boundary
  declaration (`live_call_authority`, `usage_budget_authority`,
  `merge_authority`, etc.), each `owner_only` / `bounded_delegate` /
  `not_granted`.
