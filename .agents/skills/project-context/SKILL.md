---
name: project-context
description: Load a bounded context pack after canonical routing resolves an existing AI-OS project.
---

# Project Context

Use after canonical routing resolves one capability. This skill loads context; it does not classify the request or define domain methodology.

When a capability's `executor.context_loader` names this skill, it is also the context entrypoint for a dispatched subagent (`AGENT_LOOP_PLAYBOOK.md`, "Supervised AI-OS Subagent Dispatch"): load only the one resolved capability's bounded pack; the subagent must not load other projects, classify the request, or select the next owner.

## Procedure

1. Read the resolved capability from `PROJECT_CAPABILITIES.yaml` and verify its `canonical_path` exists.
2. Resolve each relative `context_entrypoint` inside that `canonical_path`; reject paths that escape it.
3. Read `PROJECT_INSTRUCTIONS.md` first, then inspect only the listed entrypoints and task-relevant references from them.
4. Prefer project indexes and curated bundles for discovery. Open granular `Knowledge/` files only when they materially answer the task.
5. Keep primary methodology inside the resolved `canonical_path`. Load another project only for an explicit handoff, never as substitute methodology.
6. Verify every selected path exists. Mark a referenced but absent file as `not found`; do not invent or silently substitute it.
7. Stop when there is enough context to act. Do not load all projects, an entire Knowledge tree, raw dumps, or copied project knowledge.

## Context pack

Return: goal; capability id; canonical path; entrypoints inspected; included files with selection reasons; excluded candidates with reasons; missing references; context sufficiency.
