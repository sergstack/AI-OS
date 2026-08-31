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
