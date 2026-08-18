# Scope Lock

## Allowed files

- `ChatGPT/[Thinking]/PROJECT_INSTRUCTIONS.md`
- `ChatGPT/[Thinking]/README.md`
- `ChatGPT/[Thinking]/CURRENT_STATUS.md`
- `ChatGPT/[Thinking]/SMOKE_QA_RESULTS.md`
- `ChatGPT/[Thinking]/Knowledge/INDEX.md`
- `ChatGPT/[Thinking]/Knowledge/THINKERS_LENS_ROUTER.md`
- `ChatGPT/[Thinking]/Knowledge/THINKERS_CONFLICT_MAP.md`
- `ChatGPT/[Thinking]/Knowledge/THINKERS_SYNTHESIS_PATTERNS.md`
- `ChatGPT/[Thinking]/Knowledge/THINKERS_APPLICATION_LOG.md`
- `ChatGPT/[Thinking]/Knowledge_Bundles/README.md`
- `ChatGPT/[Thinking]/Knowledge_Bundles/THINKING_01_WORKFLOW_AND_DECISIONS.md`
- `ChatGPT/[Thinking]/Knowledge_Bundles/THINKING_04_THINKERS_SYNTHESIS.md`
- `ChatGPT/[Thinking]/Knowledge_Bundles/UPLOAD_LIST.md`
- `tests/test_thinking_thinkers_integration.py`
- `docs/thinkers_thinking_integration/**`

## Forbidden files

- `ChatGPT/[Thinkers OS]/**`
- `MANIFEST.md`, `MANIFEST.json`, other project packages, raw/normalized/excerpt/source-manifest data, and external Project state.

## Allowed actions

- Create/update the listed Markdown/test files; compute fingerprints; run local checks; commit and push `agent/thinking-thinkers-synthesis`.

## Forbidden actions

- No main commit, merge, external upload, status promotion, owner acceptance, source discovery/intake, synthesis status change, dependency, runtime, or deployment changes.

## Public behavior rule

`[Thinking]` may add bounded thinker-lens application after case framing, but it must remain the owner of real decision analysis and must not absorb Thinkers OS corpus/source/synthesis maintenance.
