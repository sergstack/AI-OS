# AIOS AutoResearch v0.2 — Playwright MCP Browser-Session Live Transport & Smoke — 2026-09-04

Parent: [#409](https://github.com/sergstack/AI-OS/issues/409).
Child: [#413](https://github.com/sergstack/AI-OS/issues/413) (Implement authorized Playwright MCP
browser-session live transport and smoke proof).

Status: **implementation + automated checks complete; the live browser smoke was EXECUTED
2026-09-04** (owner signed in to the dedicated Playwright profile; one real subject-model
submission). Machine-readable result: [`autoresearch_v02_413_smoke_record.json`](autoresearch_v02_413_smoke_record.json).

No credential value was read, typed, printed, exported, or transmitted by the automation. No
cookies, storage state, or browser profile were read or committed. Only the assistant message
text and its `data-message-model-slug` attribute were read from the page.

## Live smoke result (2026-09-04)

- Transport: `playwright_mcp`, `dedicated_persistent_profile` (owner-authenticated), fresh
  non-Project `chatgpt.com` conversation (`repo_replay`, lower fidelity than the real Project).
- Context: `context_hash c5a1c5b0…` over two committed sources (`ROUTING_RULES.md`,
  `HANDOFF_STYLE_STANDARD.md`) at revision `662686e…`; `request_hash 7ac9ed80…`.
- **1** browser submission, **0** retries. `termination_status: completed`.
- **Model identity: `ui_observed`** — `gpt-5-6-thinking` (read from the assistant message's
  `data-message-model-slug`; exact snapshot still `not_observable`).
- **`response_hash b2539ec2…`** — a real, non-placeholder sha256 over the normalised 607-char
  answer. `sanitization_flags: []`.
- Usage/cost: `input_tokens`/`output_tokens`/`usage_metadata_status` = `not_observable`;
  `cost_amount 0.0 USD` (owner's existing ChatGPT Pro plan; within the `$0` / plan-included
  Phase-0 envelope).
- The answer was substantively consistent with the supplied context (routed a pure quantitative
  backtest to `[Analytics]`, required the canonical `HANDOFF_STYLE_STANDARD.md` field set, and
  correctly declined to invent a destination) — recorded as an observation, not as a fidelity
  claim.

A trimmed 2-source pack was used for this bounded smoke; the full 10-source `subject_baseline`
pack is exercised in #417 Phase 0.

---

## Owner authorization envelope (recorded, `owner_instruction` authority)

Verbatim owner instruction, 2026-09-04: **"реши сам. Цель через лив прогон, прогнать настройки
AI OS"** — directional authorization for Option 1 of `AUTORESEARCH_V02_PARENT_FINAL_QA_2026-09-04.md`
(build the live chain), with these three parameters chosen by the owner the same day:

| Parameter | Owner decision |
|---|---|
| Transport connection mode (exactly one for v0.2) | **Dedicated persistent Playwright profile** the owner signs in to interactively. Credentials are never automated. |
| Phase 0 (#417) live-call ceiling | **~40 calls** (subject + blind Judge + A/B order reversal + bounded retries). |
| Monetary cap for usage-billed transport | **$0 / plan-included only.** Abort any call that would require paid overage. |

Scope note: this authorizes Phase 0 scope. Phase 1 (#418) needs a separate later
`usage_budget_authority` grant per `AUTORESEARCH_V02_LIVE_CONTRACT.md` §15. This envelope does
**not** grant candidate-acceptance, active-config, merge, or production authority.

---

## Final response format (per #413)

```text
Parent:                         #409. Child #413.
Dependencies:                   #410 (merged), #411 (merged), #412 (merged) — all satisfied.
Selected transport mode:        dedicated_persistent_profile (Playwright MCP), owner-selected. Exactly one mode implemented.
Browser/session policy:         predeclared TransportPolicy (frozen): target_product openai_chatgpt_ui, target_url_prefix https://chatgpt.com/, session_policy fresh_conversation, browser_session_ref = non-secret profile hash. Untrusted case text cannot mutate it (frozen dataclass; test-proven).
Target UI/product:              OpenAI ChatGPT web UI, dedicated signed-in Playwright profile.
Observed model identity status: gpt-5-6-thinking, ui_observed (from data-message-model-slug); exact snapshot not_observable. Comparator can distinguish verified | ui_observed | not_observable.
Authority/budget evidence:      This document's envelope section is the authority_evidence_ref. invoke() refuses to submit without a non-empty ref, without a numeric call ceiling, or without a cost cap + currency ($0 + USD is a valid authorised cap).
Adapter paths:                  scripts/autoresearch_live_browser_adapter.py (interface + FakeBrowserTransport + PlaywrightMcpBrowserTransport); schemas/autoresearch_live_invocation.schema.json (additive; no v0.1 schema edited); tests/test_autoresearch_live_browser_adapter.py (35 tests).
Live smoke browser submission count: 1 submission, 0 retries (2026-09-04). Conversation https://chatgpt.com/c/6a9a9272-e5c8-83ed-b020-fce204690b0b.
Live response evidence:         one sanitized normalised 607-char answer; response_hash b2539ec297259a36a95ac1c2bf31c72222dfa22620f680ce6ed0c7139c7b85c8 (non-placeholder); context_hash c5a1c5b0…, request_hash 7ac9ed80…, source_revision 662686e…. Full record: autoresearch_v02_413_smoke_record.json.
Usage/cost metadata status:     input_tokens/output_tokens = not_observable (never estimated from length); usage_metadata_status = not_observable; cost_amount = 0.0; cost_currency = USD (plan-included).
Privacy/session/secret checks:  fail-closed sanitization scan on the captured answer (sanitization_flags: []); no credential automation, no cookie/storage/profile export, no unrelated-tab inspection, no environment enumeration.
Automated checks:               35 focused tests pass; full suite 531 passed (496 baseline + 35). check_manifest_paths 189/189, check_repo_public_safety PASS, check_index_coverage 9/9. New schema is valid draft-07. No real browser/network/model call in any test.
Acceptance status:              Artifact/code acceptance met; business acceptance met — one real browser-produced model response entered the pipeline without manual substitution, with a verifiable non-placeholder hash and full transport/context/model-identity record. Owner acceptance of the child remains pending.
Blockers/limitations:           smoke executed; see Limitations below.
Rollback:                       remove scripts/autoresearch_live_browser_adapter.py, schemas/autoresearch_live_invocation.schema.json, tests/test_autoresearch_live_browser_adapter.py, this doc, and the README index line. No v0.1 file, Project config, or browser profile is touched by rollback.
```

---

## What was built

### `scripts/autoresearch_live_browser_adapter.py`

- **One narrow interface**: `invoke(request, policy, budget, transport) -> LiveInvocationResult`,
  running `PLAN -> PREVIEW EFFECT -> AUTHORITY CHECK -> COMMIT -> VERIFY` (AES §13.2 /
  live-contract §5). Every code path returns a `LiveInvocationResult`; a non-`completed`
  `termination_status` is never a PASS and always keeps a sanitized record.
- **Pre-submission gates** (no browser submission on failure): missing/empty
  `authority_evidence_ref`; unauthorised budget (no numeric call ceiling, or missing cost
  cap/currency); wall-clock or call-ceiling exhausted; a paid-cost transport under a `$0` cap;
  missing/mismatched `context_hash`; wrong target page; navigation error; requested-vs-observed
  model-selector mismatch (`selector_unverified`).
- **Post-submission handling**: `timeout`, `session_lost`, `empty_response`, and secret-shaped
  capture (`validation_error`) all return non-pass, consume the reserved call (the provider was
  reached), and preserve evidence.
- **`FakeBrowserTransport`** — deterministic, no I/O, `transport_id = "fake_browser"` /
  `capture_method = "test_double"` fixed so a fake result can never be mistaken for live.
- **`PlaywrightMcpBrowserTransport`** — the one concrete mode (dedicated persistent profile).
  Takes an injected `mcp_call` proxying the real `mcp__playwright__browser_*` tools; with no
  binding it raises rather than fabricating a response. Does not sign in, does not read
  cookies/storage, does not touch other tabs; `close_session` deliberately leaves the owner's
  browser as it found it.
- **Integration seam**: `live_browser_adapter_callable(...)` returns an `AdapterCallable`
  (`(experiment_id, condition, case_id) -> dict | None`) for `run_shadow_experiment`; it returns
  a row only on a passing invocation and `None` otherwise (mapping to the runner's existing
  `MISSING_OBSERVATION -> inconclusive`). `to_observation_row` / `to_live_invocation_record`
  provide the runner-row and schema-record shapes.

### `schemas/autoresearch_live_invocation.schema.json`

Additive v0.2 schema for a live browser-session invocation record. It does **not** modify
`schemas/autoresearch_observation_row.schema.json` or
`schemas/autoresearch_experiment_record.schema.json` (both frozen: `additionalProperties:false`
+ version const). Conditionals enforce: a non-`completed` record carries no response/hash; a
`completed` record carries a real answer + real sha256; `test_double` capture ⇒
`transport_id: fake_browser`; `playwright_mcp` ⇒ `capture_method: browser_automation`.

---

## Blockers (why the live smoke is `blocked`)

1. **Owner sign-in to the dedicated Playwright MCP profile.** The selected mode requires a
   persistent Playwright profile authenticated to the owner's ChatGPT account. Credentials are
   never automated by this implementation (repository rule + #413 Forbidden actions), so the
   owner must complete the interactive sign-in once in that profile before the smoke can reach
   the target UI.
2. **A live `mcp_call` binding.** `PlaywrightMcpBrowserTransport` needs the real
   `mcp__playwright__browser_*` tools wired to its `mcp_call` seam for the single predeclared
   smoke submission. This is deliberately absent from all automated tests.
3. **Predeclared smoke case.** One harmless `repo_replay` context pack (from
   `scripts/autoresearch_context_pack_compiler.py`, `role: subject_baseline`) plus one
   non-sensitive instruction-following question; no candidate mutation; exactly one submission
   with at most one bounded retry.

Until items 1–3 are done and one real browser answer with a non-placeholder hash is captured,
#413 stays `blocked` and must not be accepted as complete. No synthetic substitute is permitted
and there is no silent API/CLI fallback.

---

## Rollback

Remove the four child-owned files listed in the Final response format plus the one
`docs/evidence/README.md` index line. Do not alter the owner's browser profile/session as
rollback. No active AI-OS behaviour, Project configuration, or v0.1 artifact is touched.

---

## Checks run

```bash
python3 -m pytest tests/test_autoresearch_live_browser_adapter.py -q   # 35 passed
python3 -m pytest tests/ -q                                            # 531 passed
python3 -m json.tool schemas/autoresearch_live_invocation.schema.json  # parses
python3 scripts/check_manifest_paths.py                                # 189/189
python3 scripts/check_repo_public_safety.py                            # PASS
python3 scripts/check_index_coverage.py                                # 9/9
```

This document was scanned for secrets, raw credentials, personal data, cookies/storage state,
and unsupported live-run claims before commit: none found. No live browser/model call has
occurred.
