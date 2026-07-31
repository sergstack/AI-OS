# Smoke QA Results — [Thinkers OS]

- status_date: 2026-07-31
- repository_contract_smoke: PASS — 12/12 static contract cases
- external_project_smoke: NOT RUN — external Project is not created or modified by repository implementation
- production_status: NOT AUTHORIZED

| Case | Expected repository contract | Observed result | Verdict |
|---|---|---|---|
| Missing author book | Route corpus/source request work to `[Thinkers OS]` | Static contract found in `ROUTING_AND_HANDOFF.md` | PASS |
| Apply thinker ideas to real conflict | Route application to `[Thinking]` | Static contract found in `ROUTING_AND_HANDOFF.md` | PASS |
| Create extraction prompt | Route prompt workflow to `[LLM]` | Static contract found in `ROUTING_AND_HANDOFF.md` | PASS |
| Implement source pipeline | Route repository implementation to `[Codex]` | Static contract found in `ROUTING_AND_HANDOFF.md` | PASS |
| Quantitatively validate a pattern | Route calculations and metrics to `[Analytics]` | Static contract found in `ROUTING_AND_HANDOFF.md` | PASS |
| Missing required source | Produce `BLOCKER`, not invented evidence | Static source gate found in `PROJECT_INSTRUCTIONS.md` | PASS |
| Partial corpus | Do not assign `package_complete` | Static completion gate found in `CORPUS_AND_SOURCE_RULES.md` | PASS |
| Preview or sample | Do not accept as full source | Static source rule found in `CORPUS_AND_SOURCE_RULES.md` | PASS |
| Export safety | Exclude raw and normalized books | Static export rule found in `ARTIFACT_CONTRACTS.md` | PASS |
| Synthesis gate | Exclude candidate and blocked artifacts from active synthesis | Static gate found in `THINKERS_OS_WORKFLOW.md` | PASS |
| Uploaded bundle freshness | Do not treat Project Sources as live repository state | Static precedence rule found in bundle 01 | PASS |
| Handoff contract | Use one receiving project and canonical fields | Static contract found in `ROUTING_AND_HANDOFF.md` | PASS |

Observed by `python3 -m pytest -q tests/test_validation_scripts.py tests/test_thinkers_os_integration.py`: 37 passed, including all twelve parametrized repository contract cases. This verifies repository contracts only; external behavioral smoke remains `NOT RUN` and manual.
