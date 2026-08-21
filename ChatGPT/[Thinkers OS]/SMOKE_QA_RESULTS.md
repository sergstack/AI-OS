# Smoke QA Results — [Thinkers OS]

- status_date: 2026-08-21
- repository_contract_smoke: PASS — 12/12 static contract cases
- external_project_smoke: PASS — optimized instructions and bundle 01 were synchronized, then the focused source-gate case passed in a new external Project chat on 2026-08-21
- external_full_suite: NOT RUN — the complete twelve-case external suite was not rerun
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

## Focused external behavioral smoke — 2026-08-21

| Case | Expected live behavior | Observed behavior | Verdict |
|---|---|---|---|
| Preview/sample with requested active-synthesis refresh | Block request closure, new source-backed claims, and the new synthesis contribution; allow partial registration and unaffected Judge-pass work; name owner action and do not invent evidence | Post-sync `[Thinkers OS]` response returned `REVISE / SCOPE-BLOCKED`, a compact scope table, `NO CHANGE` for active synthesis, `USABLE` for unaffected synthesis, the full-source blocker, owner action, routing, and the safe resume stage | PASS |

The private chat URL is not stored in the repository. Project Instructions were verified after reopening settings and matched the 6,962-character repository file. Refreshed bundle 01 content and unchanged bundle 02 were both visible; ChatGPT applied a numeric suffix to bundle 01 because same-name items remain in Library.

This focused case does not replace the full twelve-case external suite.

Observed after the optimization changes by `python3 -m pytest -q tests/test_thinkers_os_integration.py tests/test_validation_scripts.py`: 38 passed. Static repository checks and the focused external behavioral observation remain separate evidence types.
