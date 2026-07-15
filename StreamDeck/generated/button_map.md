# AI-OS StreamDeck v3.0 — generated button map

> Generated from canonical JSON by `tools/generate_v3.py`; do not edit manually.

## AIOS-CONTROL

| Key | Label | Target profile | Device binding |
|---|---|---|---|
| K1 | DAILY | `B00_DAILY` | `manual_serial_neutral` |
| K2 | ROUTE | `B10_ROUTE` | `manual_serial_neutral` |
| K3 | AI OS | `B20_AI_OS` | `manual_serial_neutral` |
| K4 | THINKING | `B30_THINKING` | `manual_serial_neutral` |
| K5 | ANALYTICS | `B40_ANALYTICS` | `manual_serial_neutral` |
| K6 | LLM | `B50_LLM` | `manual_serial_neutral` |
| K7 | CODEX | `B60_CODEX` | `manual_serial_neutral` |
| K8 | JUDGE | `B70_JUDGE` | `manual_serial_neutral` |
| K9 | REVISOR | `B80_REVISOR` | `manual_serial_neutral` |
| K10 | MEMO | `B90_MEMO` | `manual_serial_neutral` |
| K11 | LOCAL AI | `BA0_LOCAL_AI` | `manual_serial_neutral` |
| K12 | PILOTS | `BB0_PILOTS` | `manual_serial_neutral` |
| K13 | KB | `BC0_KB` | `manual_serial_neutral` |
| K14 | MCP | `BD0_MCP` | `manual_serial_neutral` |
| K15 | DECK QA | `BE0_DECK_QA` | `manual_serial_neutral` |

## DAILY (`B00_DAILY`)

| Key | Label | Prompt ID | Owner | Insertion method | Next pass |
|---|---|---|---|---|---|
| K1 | INBOX | `b00_daily_inbox` | [Inbox Router] | `clipboard_paste` | `final_acceptance_gate` |
| K2 | AI TREND | `ai_trend` | [AI OS] | `clipboard_paste` | `final_acceptance_gate` |
| K3 | DECISION | `thinking_decision` | [Thinking] | `clipboard_paste` | `final_acceptance_gate` |
| K4 | DATA CONTRACT | `analytics_data_contract` | [Analytics] | `clipboard_paste` | `final_acceptance_gate` |
| K5 | GOAL→PR | `codex_goal_to_pr` | [Codex] | `clipboard_paste` | `final_acceptance_gate` |
| K6 | FIN MEMO | `b00_daily_fin_memo` | [LLM] / Memo | `clipboard_paste` | `final_acceptance_gate` |
| K7 | PROMPT | `llm_prompt_review` | [LLM] | `clipboard_paste` | `final_acceptance_gate` |
| K8 | CONTEXT | `b00_daily_context` | [LLM] | `clipboard_paste` | `final_acceptance_gate` |
| K9 | SYNC | `codex_sync` | [Codex] | `clipboard_paste` | `final_acceptance_gate` |
| K10 | KB EVIDENCE | `b00_daily_kb_evidence` | [AI OS] | `clipboard_paste` | `final_acceptance_gate` |
| K11 | BLOCKER | `blocker_review` | [Thinking] | `clipboard_paste` | `final_acceptance_gate` |
| K12 | HANDOFF | `handoff_prepare` | [Inbox Router] | `clipboard_paste` | `final_acceptance_gate` |
| K13 | JUDGE | `judge_universal` | [LLM] / Judge | `clipboard_paste` | `final_acceptance_gate` |
| K14 | REVISOR | `revisor_apply_notes` | [LLM] / Revisor | `clipboard_paste` | `final_acceptance_gate` |
| K15 | FINAL GATE | `final_acceptance_gate` | [LLM] / Judge | `clipboard_paste` | `owner_acceptance` |

## ROUTE (`B10_ROUTE`)

| Key | Label | Prompt ID | Owner | Insertion method | Next pass |
|---|---|---|---|---|---|
| K1 | RAW→ROUTE | `b10_route_raw_to_route` | [Inbox Router] | `clipboard_paste` | `final_acceptance_gate` |
| K2 | THINGS? | `b10_route_things` | [Inbox Router] | `clipboard_paste` | `final_acceptance_gate` |
| K3 | CALENDAR? | `b10_route_calendar` | [Inbox Router] | `clipboard_paste` | `final_acceptance_gate` |
| K4 | NOTES? | `b10_route_notes` | [Inbox Router] | `clipboard_paste` | `final_acceptance_gate` |
| K5 | AI OS? | `b10_route_ai_os` | [Inbox Router] | `clipboard_paste` | `final_acceptance_gate` |
| K6 | THINKING? | `b10_route_thinking` | [Inbox Router] | `clipboard_paste` | `final_acceptance_gate` |
| K7 | ANALYTICS? | `b10_route_analytics` | [Inbox Router] | `clipboard_paste` | `final_acceptance_gate` |
| K8 | LLM? | `b10_route_llm` | [Inbox Router] | `clipboard_paste` | `final_acceptance_gate` |
| K9 | CODEX? | `b10_route_codex` | [Inbox Router] | `clipboard_paste` | `final_acceptance_gate` |
| K10 | CODEX APP? | `b10_route_codex_app` | [Inbox Router] | `clipboard_paste` | `final_acceptance_gate` |
| K11 | BLOCKER | `blocker_review` | [Thinking] | `clipboard_paste` | `final_acceptance_gate` |
| K12 | HANDOFF | `handoff_prepare` | [Inbox Router] | `clipboard_paste` | `final_acceptance_gate` |
| K13 | JUDGE | `judge_universal` | [LLM] / Judge | `clipboard_paste` | `final_acceptance_gate` |
| K14 | REVISOR | `revisor_apply_notes` | [LLM] / Revisor | `clipboard_paste` | `final_acceptance_gate` |
| K15 | FINAL GATE | `final_acceptance_gate` | [LLM] / Judge | `clipboard_paste` | `owner_acceptance` |

## AI OS (`B20_AI_OS`)

| Key | Label | Prompt ID | Owner | Insertion method | Next pass |
|---|---|---|---|---|---|
| K1 | AI TREND | `ai_trend` | [AI OS] | `clipboard_paste` | `final_acceptance_gate` |
| K2 | PATTERN | `b20_ai_os_pattern` | [AI OS] | `clipboard_paste` | `final_acceptance_gate` |
| K3 | USE CASE | `b20_ai_os_use_case` | [AI OS] | `clipboard_paste` | `final_acceptance_gate` |
| K4 | EVIDENCE | `evidence_check` | [AI OS] | `clipboard_paste` | `final_acceptance_gate` |
| K5 | GOVERNANCE | `b20_ai_os_governance` | [AI OS] | `clipboard_paste` | `final_acceptance_gate` |
| K6 | FRESH CHECK | `b20_ai_os_fresh_check` | [AI OS] | `clipboard_paste` | `final_acceptance_gate` |
| K7 | SOURCE TRUTH | `kb_source_truth` | [AI OS] | `clipboard_paste` | `final_acceptance_gate` |
| K8 | LOOP DESIGN | `b20_ai_os_loop_design` | [AI OS] | `clipboard_paste` | `final_acceptance_gate` |
| K9 | PROMPT QA | `b20_ai_os_prompt_qa` | [LLM] / Judge | `clipboard_paste` | `final_acceptance_gate` |
| K10 | STREAMDECK | `b20_ai_os_streamdeck` | [AI OS] | `clipboard_paste` | `final_acceptance_gate` |
| K11 | BLOCKER | `blocker_review` | [Thinking] | `clipboard_paste` | `final_acceptance_gate` |
| K12 | HANDOFF | `handoff_prepare` | [Inbox Router] | `clipboard_paste` | `final_acceptance_gate` |
| K13 | JUDGE | `judge_universal` | [LLM] / Judge | `clipboard_paste` | `final_acceptance_gate` |
| K14 | REVISOR | `revisor_apply_notes` | [LLM] / Revisor | `clipboard_paste` | `final_acceptance_gate` |
| K15 | FINAL GATE | `final_acceptance_gate` | [LLM] / Judge | `clipboard_paste` | `owner_acceptance` |

## THINKING (`B30_THINKING`)

| Key | Label | Prompt ID | Owner | Insertion method | Next pass |
|---|---|---|---|---|---|
| K1 | DECISION | `thinking_decision` | [Thinking] | `clipboard_paste` | `final_acceptance_gate` |
| K2 | OPTIONS | `b30_thinking_options` | [Thinking] | `clipboard_paste` | `final_acceptance_gate` |
| K3 | RISKS | `thinking_risks` | [Thinking] | `clipboard_paste` | `final_acceptance_gate` |
| K4 | ASSUMPTIONS | `b30_thinking_assumptions` | [Thinking] | `clipboard_paste` | `final_acceptance_gate` |
| K5 | REVERSIBLE? | `b30_thinking_reversible` | [Inbox Router] | `clipboard_paste` | `final_acceptance_gate` |
| K6 | SCENARIO | `b30_thinking_scenario` | [Thinking] | `clipboard_paste` | `final_acceptance_gate` |
| K7 | PREMORTEM | `b30_thinking_premortem` | [Thinking] | `clipboard_paste` | `final_acceptance_gate` |
| K8 | CRITERIA | `b30_thinking_criteria` | [Thinking] | `clipboard_paste` | `final_acceptance_gate` |
| K9 | TRADE-OFFS | `b30_thinking_trade_offs` | [Thinking] | `clipboard_paste` | `final_acceptance_gate` |
| K10 | NEXT STEP | `b30_thinking_next_step` | [Thinking] | `clipboard_paste` | `final_acceptance_gate` |
| K11 | BLOCKER | `blocker_review` | [Thinking] | `clipboard_paste` | `final_acceptance_gate` |
| K12 | HANDOFF | `handoff_prepare` | [Inbox Router] | `clipboard_paste` | `final_acceptance_gate` |
| K13 | JUDGE | `judge_universal` | [LLM] / Judge | `clipboard_paste` | `final_acceptance_gate` |
| K14 | REVISOR | `revisor_apply_notes` | [LLM] / Revisor | `clipboard_paste` | `final_acceptance_gate` |
| K15 | FINAL GATE | `final_acceptance_gate` | [LLM] / Judge | `clipboard_paste` | `owner_acceptance` |

## ANALYTICS (`B40_ANALYTICS`)

| Key | Label | Prompt ID | Owner | Insertion method | Next pass |
|---|---|---|---|---|---|
| K1 | DATA CONTRACT | `analytics_data_contract` | [Analytics] | `clipboard_paste` | `final_acceptance_gate` |
| K2 | DATA QUALITY | `b40_analytics_data_quality` | [Analytics] | `clipboard_paste` | `final_acceptance_gate` |
| K3 | VARIANCE | `b40_analytics_variance` | [Analytics] | `clipboard_paste` | `final_acceptance_gate` |
| K4 | RECONCILE | `b40_analytics_reconcile` | [Analytics] | `clipboard_paste` | `final_acceptance_gate` |
| K5 | ANOMALY | `b40_analytics_anomaly` | [Analytics] | `clipboard_paste` | `final_acceptance_gate` |
| K6 | MART SPEC | `b40_analytics_mart_spec` | [Analytics] | `clipboard_paste` | `final_acceptance_gate` |
| K7 | FORMULA | `b40_analytics_formula` | [Analytics] | `clipboard_paste` | `final_acceptance_gate` |
| K8 | QA CHECKS | `b40_analytics_qa_checks` | [Analytics] | `clipboard_paste` | `final_acceptance_gate` |
| K9 | ANALYTICS LOOP | `b40_analytics_analytics_loop` | [Analytics] | `clipboard_paste` | `final_acceptance_gate` |
| K10 | MEMO FACTS | `b40_analytics_memo_facts` | [Analytics] | `clipboard_paste` | `final_acceptance_gate` |
| K11 | BLOCKER | `blocker_review` | [Thinking] | `clipboard_paste` | `final_acceptance_gate` |
| K12 | HANDOFF | `handoff_prepare` | [Inbox Router] | `clipboard_paste` | `final_acceptance_gate` |
| K13 | JUDGE | `judge_universal` | [LLM] / Judge | `clipboard_paste` | `final_acceptance_gate` |
| K14 | REVISOR | `revisor_apply_notes` | [LLM] / Revisor | `clipboard_paste` | `final_acceptance_gate` |
| K15 | FINAL GATE | `final_acceptance_gate` | [LLM] / Judge | `clipboard_paste` | `owner_acceptance` |

## LLM (`B50_LLM`)

| Key | Label | Prompt ID | Owner | Insertion method | Next pass |
|---|---|---|---|---|---|
| K1 | PROMPT BUILD | `b50_llm_prompt_build` | [LLM] | `clipboard_paste` | `final_acceptance_gate` |
| K2 | CONTEXT PACK | `b50_llm_context_pack` | [LLM] | `clipboard_paste` | `final_acceptance_gate` |
| K3 | MODEL ROUTE | `b50_llm_model_route` | [LLM] | `clipboard_paste` | `final_acceptance_gate` |
| K4 | WORKFLOW | `b50_llm_workflow` | [LLM] | `clipboard_paste` | `final_acceptance_gate` |
| K5 | EVAL RUBRIC | `b50_llm_eval_rubric` | [LLM] | `clipboard_paste` | `final_acceptance_gate` |
| K6 | SUMMARIZE | `b50_llm_summarize` | [LLM] | `clipboard_paste` | `final_acceptance_gate` |
| K7 | EXTRACT | `b50_llm_extract` | [LLM] | `clipboard_paste` | `final_acceptance_gate` |
| K8 | SYNTHESIZE | `b50_llm_synthesize` | [LLM] | `clipboard_paste` | `final_acceptance_gate` |
| K9 | LOCAL PROMPT | `b50_llm_local_prompt` | [LLM] / Local AI | `clipboard_paste` | `final_acceptance_gate` |
| K10 | GOAL→CODEX PACK | `b50_llm_goal_to_codex_pack` | [LLM] | `clipboard_paste` | `final_acceptance_gate` |
| K11 | BLOCKER | `blocker_review` | [Thinking] | `clipboard_paste` | `final_acceptance_gate` |
| K12 | HANDOFF | `handoff_prepare` | [Inbox Router] | `clipboard_paste` | `final_acceptance_gate` |
| K13 | JUDGE | `judge_universal` | [LLM] / Judge | `clipboard_paste` | `final_acceptance_gate` |
| K14 | REVISOR | `revisor_apply_notes` | [LLM] / Revisor | `clipboard_paste` | `final_acceptance_gate` |
| K15 | FINAL GATE | `final_acceptance_gate` | [LLM] / Judge | `clipboard_paste` | `owner_acceptance` |

## CODEX (`B60_CODEX`)

| Key | Label | Prompt ID | Owner | Insertion method | Next pass |
|---|---|---|---|---|---|
| K1 | GOAL→PR | `codex_goal_to_pr` | [Codex] | `clipboard_paste` | `final_acceptance_gate` |
| K2 | BUILD FIRST | `b60_codex_build_first` | [Codex] | `clipboard_paste` | `final_acceptance_gate` |
| K3 | INSPECT | `b60_codex_inspect` | [Codex] | `clipboard_paste` | `final_acceptance_gate` |
| K4 | RUN CHECKS | `b60_codex_run_checks` | [Codex] | `clipboard_paste` | `final_acceptance_gate` |
| K5 | FIX IN SCOPE | `b60_codex_fix_in_scope` | [Codex] | `clipboard_paste` | `final_acceptance_gate` |
| K6 | SYNC | `codex_sync` | [Codex] | `clipboard_paste` | `final_acceptance_gate` |
| K7 | PR JUDGE | `b60_codex_pr_judge` | [LLM] / Judge | `clipboard_paste` | `final_acceptance_gate` |
| K8 | FIX CI | `b60_codex_fix_ci` | [Codex] | `clipboard_paste` | `final_acceptance_gate` |
| K9 | REVIEW COMMENTS | `b60_codex_review_comments` | [Codex] | `clipboard_paste` | `final_acceptance_gate` |
| K10 | RELEASE NOTES | `b60_codex_release_notes` | [Codex] | `clipboard_paste` | `final_acceptance_gate` |
| K11 | BLOCKER | `blocker_review` | [Thinking] | `clipboard_paste` | `final_acceptance_gate` |
| K12 | HANDOFF | `handoff_prepare` | [Inbox Router] | `clipboard_paste` | `final_acceptance_gate` |
| K13 | JUDGE | `judge_universal` | [LLM] / Judge | `clipboard_paste` | `final_acceptance_gate` |
| K14 | REVISOR | `revisor_apply_notes` | [LLM] / Revisor | `clipboard_paste` | `final_acceptance_gate` |
| K15 | FINAL GATE | `final_acceptance_gate` | [LLM] / Judge | `clipboard_paste` | `owner_acceptance` |

## JUDGE (`B70_JUDGE`)

| Key | Label | Prompt ID | Owner | Insertion method | Next pass |
|---|---|---|---|---|---|
| K1 | UNIVERSAL | `judge_universal` | [LLM] / Judge | `clipboard_paste` | `final_acceptance_gate` |
| K2 | EVIDENCE | `judge_evidence` | [LLM] / Judge | `clipboard_paste` | `final_acceptance_gate` |
| K3 | ROUTE | `judge_route` | [LLM] / Judge | `clipboard_paste` | `final_acceptance_gate` |
| K4 | RISK | `judge_risk` | [LLM] / Judge | `clipboard_paste` | `final_acceptance_gate` |
| K5 | FRESHNESS | `judge_freshness` | [LLM] / Judge | `clipboard_paste` | `final_acceptance_gate` |
| K6 | ANALYTICS | `judge_analytics` | [LLM] / Judge | `clipboard_paste` | `final_acceptance_gate` |
| K7 | MEMO | `judge_memo` | [LLM] / Judge | `clipboard_paste` | `final_acceptance_gate` |
| K8 | PROMPT | `judge_prompt` | [LLM] / Judge | `clipboard_paste` | `final_acceptance_gate` |
| K9 | PR | `judge_pr` | [LLM] / Judge | `clipboard_paste` | `final_acceptance_gate` |
| K10 | LOCAL AI | `judge_local_ai` | [LLM] / Judge | `clipboard_paste` | `final_acceptance_gate` |
| K11 | BLOCKER | `blocker_review` | [Thinking] | `clipboard_paste` | `final_acceptance_gate` |
| K12 | HANDOFF | `handoff_prepare` | [Inbox Router] | `clipboard_paste` | `final_acceptance_gate` |
| K13 | JUDGE | `judge_universal` | [LLM] / Judge | `clipboard_paste` | `final_acceptance_gate` |
| K14 | REVISOR | `revisor_apply_notes` | [LLM] / Revisor | `clipboard_paste` | `final_acceptance_gate` |
| K15 | FINAL GATE | `final_acceptance_gate` | [LLM] / Judge | `clipboard_paste` | `owner_acceptance` |

## REVISOR (`B80_REVISOR`)

| Key | Label | Prompt ID | Owner | Insertion method | Next pass |
|---|---|---|---|---|---|
| K1 | APPLY NOTES | `revisor_apply_notes` | [LLM] / Revisor | `clipboard_paste` | `final_acceptance_gate` |
| K2 | SHORTEN | `revisor_shorten` | [LLM] / Revisor | `clipboard_paste` | `final_acceptance_gate` |
| K3 | CLEARER | `revisor_clearer` | [LLM] / Revisor | `clipboard_paste` | `final_acceptance_gate` |
| K4 | EXEC VERSION | `revisor_exec_version` | [LLM] / Revisor | `clipboard_paste` | `final_acceptance_gate` |
| K5 | FILE-READY | `revisor_file_ready` | [LLM] / Revisor | `clipboard_paste` | `final_acceptance_gate` |
| K6 | MEMO | `revisor_memo` | [LLM] / Revisor | `clipboard_paste` | `final_acceptance_gate` |
| K7 | DECISION | `revisor_decision` | [LLM] / Revisor | `clipboard_paste` | `final_acceptance_gate` |
| K8 | STRUCTURE | `revisor_structure` | [LLM] / Revisor | `clipboard_paste` | `final_acceptance_gate` |
| K9 | TONE | `revisor_tone` | [LLM] / Revisor | `clipboard_paste` | `final_acceptance_gate` |
| K10 | SOURCE-PRESERVE | `revisor_source_preserve` | [LLM] / Revisor | `clipboard_paste` | `final_acceptance_gate` |
| K11 | BLOCKER | `blocker_review` | [Thinking] | `clipboard_paste` | `final_acceptance_gate` |
| K12 | HANDOFF | `handoff_prepare` | [Inbox Router] | `clipboard_paste` | `final_acceptance_gate` |
| K13 | JUDGE | `judge_universal` | [LLM] / Judge | `clipboard_paste` | `final_acceptance_gate` |
| K14 | REVISOR | `revisor_apply_notes` | [LLM] / Revisor | `clipboard_paste` | `final_acceptance_gate` |
| K15 | FINAL GATE | `final_acceptance_gate` | [LLM] / Judge | `clipboard_paste` | `owner_acceptance` |

## MEMO (`B90_MEMO`)

| Key | Label | Prompt ID | Owner | Insertion method | Next pass |
|---|---|---|---|---|---|
| K1 | FINANCE | `memo_finance` | [LLM] / Memo | `clipboard_paste` | `final_acceptance_gate` |
| K2 | MANAGEMENT | `memo_management` | [LLM] / Memo | `clipboard_paste` | `final_acceptance_gate` |
| K3 | EXEC SUMMARY | `memo_exec_summary` | [LLM] / Memo | `clipboard_paste` | `final_acceptance_gate` |
| K4 | FINDINGS | `memo_findings` | [LLM] / Memo | `clipboard_paste` | `final_acceptance_gate` |
| K5 | RISKS | `memo_risks` | [LLM] / Memo | `clipboard_paste` | `final_acceptance_gate` |
| K6 | RECOMMEND | `memo_recommend` | [LLM] / Memo | `clipboard_paste` | `final_acceptance_gate` |
| K7 | AUDIT FINDING | `memo_audit_finding` | [LLM] / Memo | `clipboard_paste` | `final_acceptance_gate` |
| K8 | CHART COMMENT | `memo_chart_comment` | [LLM] / Memo | `clipboard_paste` | `final_acceptance_gate` |
| K9 | APPENDIX | `memo_appendix` | [LLM] / Memo | `clipboard_paste` | `final_acceptance_gate` |
| K10 | FINAL MEMO | `memo_final_memo` | [LLM] / Memo | `clipboard_paste` | `final_acceptance_gate` |
| K11 | BLOCKER | `blocker_review` | [Thinking] | `clipboard_paste` | `final_acceptance_gate` |
| K12 | HANDOFF | `handoff_prepare` | [Inbox Router] | `clipboard_paste` | `final_acceptance_gate` |
| K13 | JUDGE | `judge_universal` | [LLM] / Judge | `clipboard_paste` | `final_acceptance_gate` |
| K14 | REVISOR | `revisor_apply_notes` | [LLM] / Revisor | `clipboard_paste` | `final_acceptance_gate` |
| K15 | FINAL GATE | `final_acceptance_gate` | [LLM] / Judge | `clipboard_paste` | `owner_acceptance` |

## LOCAL AI (`BA0_LOCAL_AI`)

| Key | Label | Prompt ID | Owner | Insertion method | Next pass |
|---|---|---|---|---|---|
| K1 | SAFETY | `local_ai_safety` | [LLM] / Local AI | `clipboard_paste` | `final_acceptance_gate` |
| K2 | SANITIZE | `ba0_local_ai_sanitize` | [LLM] / Local AI | `clipboard_paste` | `final_acceptance_gate` |
| K3 | DRAFT ONLY | `ba0_local_ai_draft_only` | [LLM] / Local AI | `clipboard_paste` | `final_acceptance_gate` |
| K4 | OLLAMA SMOKE | `ba0_local_ai_ollama_smoke` | [LLM] / Local AI | `clipboard_paste` | `final_acceptance_gate` |
| K5 | OPEN WEBUI | `ba0_local_ai_open_webui` | [LLM] / Local AI | `clipboard_paste` | `final_acceptance_gate` |
| K6 | MODEL COMPARE | `ba0_local_ai_model_compare` | [LLM] / Local AI | `clipboard_paste` | `final_acceptance_gate` |
| K7 | EVAL MATRIX | `ba0_local_ai_eval_matrix` | [LLM] / Local AI | `clipboard_paste` | `final_acceptance_gate` |
| K8 | JUDGE OUTPUT | `ba0_local_ai_judge_output` | [LLM] / Local AI | `clipboard_paste` | `final_acceptance_gate` |
| K9 | RECORD PILOT | `ba0_local_ai_record_pilot` | [LLM] / Local AI | `clipboard_paste` | `final_acceptance_gate` |
| K10 | CANDIDATE? | `ba0_local_ai_candidate` | [Inbox Router] | `clipboard_paste` | `final_acceptance_gate` |
| K11 | BLOCKER | `blocker_review` | [Thinking] | `clipboard_paste` | `final_acceptance_gate` |
| K12 | HANDOFF | `handoff_prepare` | [Inbox Router] | `clipboard_paste` | `final_acceptance_gate` |
| K13 | JUDGE | `judge_universal` | [LLM] / Judge | `clipboard_paste` | `final_acceptance_gate` |
| K14 | REVISOR | `revisor_apply_notes` | [LLM] / Revisor | `clipboard_paste` | `final_acceptance_gate` |
| K15 | FINAL GATE | `final_acceptance_gate` | [LLM] / Judge | `clipboard_paste` | `owner_acceptance` |

## PILOTS (`BB0_PILOTS`)

| Key | Label | Prompt ID | Owner | Insertion method | Next pass |
|---|---|---|---|---|---|
| K1 | PILOT PLAN | `bb0_pilots_pilot_plan` | [AI OS] | `clipboard_paste` | `final_acceptance_gate` |
| K2 | TEST CASES | `bb0_pilots_test_cases` | [AI OS] | `clipboard_paste` | `final_acceptance_gate` |
| K3 | RUN RECORD | `bb0_pilots_run_record` | [AI OS] | `clipboard_paste` | `final_acceptance_gate` |
| K4 | PILOT RESULT | `bb0_pilots_pilot_result` | [AI OS] | `clipboard_paste` | `final_acceptance_gate` |
| K5 | ACCEPTANCE | `bb0_pilots_acceptance` | [AI OS] | `clipboard_paste` | `final_acceptance_gate` |
| K6 | RESIDUAL RISK | `bb0_pilots_residual_risk` | [AI OS] | `clipboard_paste` | `final_acceptance_gate` |
| K7 | ROLLBACK | `bb0_pilots_rollback` | [AI OS] | `clipboard_paste` | `final_acceptance_gate` |
| K8 | REGISTRY | `registry_review` | [AI OS] | `clipboard_paste` | `final_acceptance_gate` |
| K9 | STATUS NOTE | `bb0_pilots_status_note` | [AI OS] | `clipboard_paste` | `final_acceptance_gate` |
| K10 | REVISIT | `bb0_pilots_revisit` | [AI OS] | `clipboard_paste` | `final_acceptance_gate` |
| K11 | BLOCKER | `blocker_review` | [Thinking] | `clipboard_paste` | `final_acceptance_gate` |
| K12 | HANDOFF | `handoff_prepare` | [Inbox Router] | `clipboard_paste` | `final_acceptance_gate` |
| K13 | JUDGE | `judge_universal` | [LLM] / Judge | `clipboard_paste` | `final_acceptance_gate` |
| K14 | REVISOR | `revisor_apply_notes` | [LLM] / Revisor | `clipboard_paste` | `final_acceptance_gate` |
| K15 | FINAL GATE | `final_acceptance_gate` | [LLM] / Judge | `clipboard_paste` | `owner_acceptance` |

## KB (`BC0_KB`)

| Key | Label | Prompt ID | Owner | Insertion method | Next pass |
|---|---|---|---|---|---|
| K1 | KB SEARCH | `bc0_kb_kb_search` | [AI OS] | `clipboard_paste` | `final_acceptance_gate` |
| K2 | EVIDENCE LABEL | `bc0_kb_evidence_label` | [AI OS] | `clipboard_paste` | `final_acceptance_gate` |
| K3 | REVIEW ITEM | `bc0_kb_review_item` | [AI OS] | `clipboard_paste` | `final_acceptance_gate` |
| K4 | SUPPORT MIX | `bc0_kb_support_mix` | [AI OS] | `clipboard_paste` | `final_acceptance_gate` |
| K5 | SOURCE TRUTH | `kb_source_truth` | [AI OS] | `clipboard_paste` | `final_acceptance_gate` |
| K6 | MANIFEST | `bc0_kb_manifest` | [AI OS] | `clipboard_paste` | `final_acceptance_gate` |
| K7 | BUNDLE SYNC | `bc0_kb_bundle_sync` | [AI OS] | `clipboard_paste` | `final_acceptance_gate` |
| K8 | UPLOAD CHECK | `bc0_kb_upload_check` | [AI OS] | `clipboard_paste` | `final_acceptance_gate` |
| K9 | FRESHNESS | `freshness_check` | [AI OS] | `clipboard_paste` | `final_acceptance_gate` |
| K10 | CONFLICT CHECK | `bc0_kb_conflict_check` | [AI OS] | `clipboard_paste` | `final_acceptance_gate` |
| K11 | BLOCKER | `blocker_review` | [Thinking] | `clipboard_paste` | `final_acceptance_gate` |
| K12 | HANDOFF | `handoff_prepare` | [Inbox Router] | `clipboard_paste` | `final_acceptance_gate` |
| K13 | JUDGE | `judge_universal` | [LLM] / Judge | `clipboard_paste` | `final_acceptance_gate` |
| K14 | REVISOR | `revisor_apply_notes` | [LLM] / Revisor | `clipboard_paste` | `final_acceptance_gate` |
| K15 | FINAL GATE | `final_acceptance_gate` | [LLM] / Judge | `clipboard_paste` | `owner_acceptance` |

## MCP (`BD0_MCP`)

| Key | Label | Prompt ID | Owner | Insertion method | Next pass |
|---|---|---|---|---|---|
| K1 | LIST ACTIONS | `bd0_mcp_list_actions` | [AI OS] | `clipboard_paste` | `final_acceptance_gate` |
| K2 | REGISTRY | `registry_review` | [AI OS] | `clipboard_paste` | `final_acceptance_gate` |
| K3 | VISIBILITY | `bd0_mcp_visibility` | [AI OS] | `clipboard_paste` | `final_acceptance_gate` |
| K4 | JUDGE | `judge_universal` | [LLM] / Judge | `clipboard_paste` | `final_acceptance_gate` |
| K5 | REVISOR | `revisor_apply_notes` | [LLM] / Revisor | `clipboard_paste` | `final_acceptance_gate` |
| K6 | SYNC | `codex_sync` | [Codex] | `clipboard_paste` | `final_acceptance_gate` |
| K7 | AI TREND | `ai_trend` | [AI OS] | `clipboard_paste` | `final_acceptance_gate` |
| K8 | KB SOURCE | `kb_source_truth` | [AI OS] | `clipboard_paste` | `final_acceptance_gate` |
| K9 | LOCAL SAFETY | `bd0_mcp_local_safety` | [LLM] / Local AI | `clipboard_paste` | `final_acceptance_gate` |
| K10 | GOAL→PR | `codex_goal_to_pr` | [Codex] | `clipboard_paste` | `final_acceptance_gate` |
| K11 | BLOCKER | `blocker_review` | [Thinking] | `clipboard_paste` | `final_acceptance_gate` |
| K12 | HANDOFF | `handoff_prepare` | [Inbox Router] | `clipboard_paste` | `final_acceptance_gate` |
| K13 | JUDGE | `judge_universal` | [LLM] / Judge | `clipboard_paste` | `final_acceptance_gate` |
| K14 | REVISOR | `revisor_apply_notes` | [LLM] / Revisor | `clipboard_paste` | `final_acceptance_gate` |
| K15 | FINAL GATE | `final_acceptance_gate` | [LLM] / Judge | `clipboard_paste` | `owner_acceptance` |

## DECK QA (`BE0_DECK_QA`)

| Key | Label | Prompt ID | Owner | Insertion method | Next pass |
|---|---|---|---|---|---|
| K1 | SWITCH TEST | `be0_deck_qa_switch_test` | [Codex] | `clipboard_paste` | `final_acceptance_gate` |
| K2 | DEVICE TARGET | `be0_deck_qa_device_target` | [Codex] | `clipboard_paste` | `final_acceptance_gate` |
| K3 | FOCUS TEST | `be0_deck_qa_focus_test` | [Codex] | `clipboard_paste` | `final_acceptance_gate` |
| K4 | TEXT INSERT | `be0_deck_qa_text_insert` | [Codex] | `clipboard_paste` | `final_acceptance_gate` |
| K5 | AUTO-SEND OFF | `be0_deck_qa_auto_send_off` | [Codex] | `clipboard_paste` | `final_acceptance_gate` |
| K6 | PLACEHOLDER | `be0_deck_qa_placeholder` | [Codex] | `clipboard_paste` | `final_acceptance_gate` |
| K7 | DUPLICATES | `be0_deck_qa_duplicates` | [Codex] | `clipboard_paste` | `final_acceptance_gate` |
| K8 | PROMPT HASH | `be0_deck_qa_prompt_hash` | [Codex] | `clipboard_paste` | `final_acceptance_gate` |
| K9 | EXPORT BACKUP | `be0_deck_qa_export_backup` | [Codex] | `clipboard_paste` | `final_acceptance_gate` |
| K10 | IMPORT TEST | `be0_deck_qa_import_test` | [Codex] | `clipboard_paste` | `final_acceptance_gate` |
| K11 | BLOCKER | `blocker_review` | [Thinking] | `clipboard_paste` | `final_acceptance_gate` |
| K12 | HANDOFF | `handoff_prepare` | [Inbox Router] | `clipboard_paste` | `final_acceptance_gate` |
| K13 | JUDGE | `judge_universal` | [LLM] / Judge | `clipboard_paste` | `final_acceptance_gate` |
| K14 | REVISOR | `revisor_apply_notes` | [LLM] / Revisor | `clipboard_paste` | `final_acceptance_gate` |
| K15 | FINAL GATE | `final_acceptance_gate` | [LLM] / Judge | `clipboard_paste` | `owner_acceptance` |
