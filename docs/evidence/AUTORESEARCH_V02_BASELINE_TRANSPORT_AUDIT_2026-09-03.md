# AIOS AutoResearch v0.2 — Baseline Reuse & Live-Transport Feasibility Audit — 2026-09-03

Parent: [#409](https://github.com/sergstack/AI-OS/issues/409) ([Goal] AIOS AutoResearch v0.2 — live behavioral autotuning loop).
Child: [#410](https://github.com/sergstack/AI-OS/issues/410) (Audit v0.1 reuse and live-transport feasibility) — mandatory baseline gate, no dependencies.

This is a **read-only feasibility map**, not an implementation. No live model/provider/Judge call was made. No credential value was read, printed, or transmitted — only credential-source **class** (env var name presence, keychain entry presence, package presence) was checked, per this issue's own explicit boundary.

## 0. Source revision and observed environment

- Baseline revision: `28cfb1e` (`origin/main`, observed 2026-09-03), the exact commit that merged #398/PR #408.
- `git status --short`: clean at audit start.
- Execution environment: Claude Code CLI `2.1.247`, Claude Agent SDK `0.3.258`, Node.js `v22.19.0`, `npx` `10.9.3`, macOS (Darwin 25.5.0), authenticated via OAuth session in the macOS Keychain (`Claude Code-credentials` entry present; `CLAUDE_CODE_OAUTH_SCOPES` env var present) — not a raw `ANTHROPIC_API_KEY`.

## Owner instruction directly steering this audit's transport conclusion

Recorded verbatim, `owner_instruction`-class authority (AES canonical classes), received live during this audit's own execution, 2026-09-03: **"Мы будем делать лив прогон в браузерной сессии. А не по API. Учти это"** ("We will do the live run in a browser session. Not via API. Take this into account.")

This directly resolves §4/§7 below in favor of a browser-automation transport over an API/SDK transport, and is treated as decisive, not merely one candidate among several — consistent with #409's own text: *"Sergey/owner: live-call/cost authority where required"* and *"transport and credential source class"* being one of the items #411 must freeze under explicit owner authorization. This audit still records the API-transport candidates it inspected, for completeness and so #411 has the full comparison on record, but does not recommend them as the primary path given this instruction.

## 1. v0.1 reuse / extend / replace / protected matrix

| v0.1 component | Path | Classification | Basis |
|---|---|---|---|
| Frozen contract | `docs/standards/AUTORESEARCH_V01_CONTRACT.md` | **protected** | #390; v0.2 adds a stricter additive layer per #409's own safety boundary, never edits this file directly |
| Protected/mutable-surface manifest | `docs/standards/autoresearch_v01_manifest.json` | **reuse unchanged** | Search-space scope (Project Instructions/routing/ambiguity/handoff/context-loading wording) is identical between v0.1 and v0.2's stated Scope |
| Eval case / experiment record / batch manifest schemas | `schemas/autoresearch_{eval_case,experiment_record,batch_manifest}.schema.json` | **reuse unchanged** | #391; no field in any of the three needs a v0.2-specific addition observed so far — `model_provider_runtime_hash`/`evaluator_version_hash` fields already exist and already anticipate a real (not synthetic) identity |
| Observation-row schema | `schemas/autoresearch_observation_row.schema.json` | **reuse unchanged** | #395; already carries `missingness_reason`, config-hash fields needed for live-run bookkeeping |
| Semantic-finding schema | `schemas/autoresearch_semantic_finding.schema.json` | **reuse unchanged** | #394; the schema itself has no notion of "how the finding was produced" — live vs. hand-authored is a provenance fact carried elsewhere (ledger/evidence doc), not a schema field, so no schema change is needed to start using it for real Judge output |
| Deterministic validator + hard-veto engine + ledger + comparator | `scripts/autoresearch_validator.py` | **reuse unchanged for validation logic; extend for provenance** | #392; every `reject_*`/`INV-*` function operates on already-structured records regardless of how they were produced. Needs one small addition (§2) to record/enforce a `provenance: live \| hand_authored \| synthetic_fixture` marker so a v0.2 batch can be validated as containing real live evidence, not just structurally-valid evidence |
| Shadow runner + worktree isolation + patch-scope/anchor enforcement | `scripts/autoresearch_shadow_runner.py` | **reuse unchanged** | #393; `create_shadow_worktree`/`reject_patch_scope`/`verify_anchor_scope`/`reject_config_mismatch` are all provenance-agnostic — they operate on a patch and a worktree, not on how the observation was obtained. The `AdapterCallable` contract (`(experiment_id, condition, case_id) -> dict \| None`) is exactly the seam a browser-transport adapter plugs into (§2) |
| `JSONLResponseAdapter` | `scripts/autoresearch_shadow_runner.py` | **reuse as the offline/replay path; extend with a live sibling adapter** | Stays valid for replaying a previously-captured live transcript deterministically (a `field_reproduction`, §5); a new adapter class implementing the same `AdapterCallable` contract but backed by a live browser session is additive, not a replacement |
| Decision comparator (non-inferiority, worst-case dominance, escalation ceiling) | `scripts/autoresearch_decision_comparator.py` | **reuse unchanged** | #395; operates purely on `CaseObservation` verdict sequences, agnostic to whether those verdicts came from a live or synthetic Judge |
| Phase 0 calibration runner | `scripts/autoresearch_phase0_calibration.py` | **extend, not replace** | #396; its 10 calibration classes and their real-code exercise pattern are the right shape for a v0.2 Phase 0 too — needs one additive input source (live-Judge-produced findings instead of/alongside hand-authored ones) rather than a rewrite |
| Phase 1 pilot runner | `scripts/autoresearch_phase1_pilot.py` | **replace the observation-source half; reuse the orchestration half** | See §3 — this is the exact file #409's Context section names as the current blocker |
| Semantic evaluator contract | `ChatGPT/[LLM]/Knowledge/AUTORESEARCH_SEMANTIC_EVALUATOR_CONTRACT.md` | **reuse unchanged** | #394; already specifies the blind A/B prompt family, order-reversal protocol, and finding schema a live Judge must satisfy — it was frozen in anticipation of exactly this |
| Stochasticity/non-inferiority method | `ChatGPT/[Analytics]/Knowledge/AUTORESEARCH_STOCHASTICITY_NONINFERIORITY_METHOD.md` | **reuse unchanged** | #395; explicitly designed for N=3–5 discrete Judge verdicts regardless of their source |
| Failure registry | `ChatGPT/[AI OS]/Knowledge/FAILURE_REGISTRY.md` | **reuse unchanged** | Already the correct causal-attribution contract (`attribution_status: attributable \| uncertain \| ineligible`); v0.2's "field observation intake" (#415) is a new *producer* of failure records, not a new registry |
| `benchmarks/live_behavioral/` | `benchmarks/live_behavioral/` (README, `benchmark_spec.json`, `freeze_manifest.json`, `HOLDOUT_MANIFEST.json`, `evaluate_live.py`, `verify_freeze.py`) | **extend — this is the closest existing prior art for the now-decided browser transport** | Its own README already documents a **manual, browser-based** live workflow: freeze → sync Instructions/Knowledge into the actual Project → run every public case three times in a fresh Project chat → capture prompt/response/URL/config hash/model condition → evaluate → open sealed holdout only after selection → frozen final gate. This is structurally the *same* workflow #409 wants, currently executed by a human clicking through a browser rather than an MCP browser tool driving it. v0.2's live adapter (#413) should be framed as **automating this existing, already-accepted workflow**, not inventing a new one. |
| `scripts/live_project_verifier.py` | `scripts/live_project_verifier.py` | **reuse unchanged, directly relevant precedent** | Already states the exact constraint this audit reconfirms: *"The script never invokes, edits, or synchronizes a Project. A controlled browser or manual operator performs the actual invocation and supplies a local capture."* This is the transport-neutral capture-binding pattern a browser-driven adapter should follow for *evidence capture*, even though the *invocation* itself can now be MCP-automated rather than fully manual. |
| AES, `ROUTING_RULES.md`, `HANDOFF_STYLE_STANDARD.md`, Prompt QA Factory, `REGRESSION_GATE.md`, authority-separation rules | various | **protected** | Same protected status as under v0.1; v0.2 adds no new authority path around these |

## 2. Required extensions (not replacements)

1. **Provenance marker on experiment/observation records.** Add one field (recommend `provenance: "live" | "hand_authored" | "synthetic_fixture"`, plus for `"live"` a `capture_method: "browser_automation" | "browser_manual" | "api"`) to `schemas/autoresearch_experiment_record.schema.json` and `schemas/autoresearch_observation_row.schema.json`. Without this, nothing in the existing validator can *structurally* distinguish a real live batch from a repeat of #397's hand-authored one — #409's own Non-acceptance example ("Re-running `scripts/autoresearch_phase1_pilot.py` with different hard-coded responses") is exactly the failure mode this field closes off deterministically rather than by convention/trust.
2. **A live browser adapter implementing `AdapterCallable`.** `scripts/autoresearch_shadow_runner.py`'s `AdapterCallable` contract (`(experiment_id, condition, case_id) -> dict | None`) is already the right seam (§1). A new adapter class — call it `LiveBrowserAdapter` — would, per case: drive a browser MCP tool to open/reuse the target ChatGPT Project chat, type the case prompt, wait for and capture the response, and return the same observation-row shape `JSONLResponseAdapter` already returns (`response`, `runtime_model_configuration`, plus the new provenance fields from item 1). This is additive: `JSONLResponseAdapter` keeps working unchanged for replay of a previously captured transcript.
3. **Model-identity verification step before each case.** `benchmarks/live_behavioral/`'s own evidence (cited in this session's memory of prior Qwen Studio work, structurally identical class of failure) shows a real, recurring failure mode: a chat UI can silently default to the wrong model unless explicitly reselected/verified before each run. A browser-driven adapter needs an explicit "read the selected model from the UI and assert it matches the frozen `model_provider_runtime_hash` identity" step, or the run is not evidence of anything — this is a genuinely new piece of logic, not present in v0.1 (which never touched a live UI at all).
4. **Live-Judge invocation using the same browser transport**, satisfying #394's already-frozen blind A/B + order-reversal contract — the contract itself needs no change; only a caller that actually performs two blinded, order-varied browser conversations per case and feeds the resulting text into `validate_semantic_finding` (already built, #394) needs to be added.

No wholesale rewrite is indicated anywhere in the v0.1 stack. Every extension above is additive to an existing seam.

## 3. What exactly prevents `autoresearch_phase1_pilot.py` from consuming real model outputs today

Read directly from the file at this revision: its `_JsonlAdapterFactory`/observation-construction helpers hand-author literal Python string constants as "baseline response" / "candidate response" text for each of its 4 experiments, then wrap them in `JSONLResponseAdapter`-compatible rows and hand them to `run_shadow_experiment`. There is no code path in this file that opens a browser, calls an API, or reads any external system at all — every observation is authored by whoever wrote the file, before the run, with the answer already known. This is not a bug; #393/#397 state this scope explicitly and honestly throughout. The blocker is precisely and only the absence of a `LiveBrowserAdapter` (§2 item 2) plumbed into the same `run_shadow_experiment(..., adapter=...)` call the file already makes — the orchestration, worktree isolation, patch-scope checks, and hand-off to the comparator are all already real and require no change.

## 4. Transport candidate matrix

Every field below is from directly observed environment evidence at this revision, not memory or inference from a product name (per this issue's own rule).

| Field | `browser_mcp_playwright` | `browser_mcp_claude_in_chrome` | `browser_pane_claude_browser` | `api_claude_code_print_mode` | `api_openai_sdk` |
|---|---|---|---|---|---|
| `transport_id` | Official Microsoft `@playwright/mcp@latest`, installed and registered this session | Real-Chrome MCP extension (existing logged-in browser sessions) | Claude Code's own built-in in-app "Browser pane" MCP tools | `claude -p` / `--print` CLI mode | `openai` Python SDK |
| `availability` | **observed** — `claude mcp list` → `✔ Connected`; smoke-tested this session (navigated to a real page, added a real item, confirmed in a fresh snapshot) | **observed** — tool schemas registered and loadable via `ToolSearch("claude-in-chrome")`; live connection/session status not separately verified in this audit (would require an actual browser action, out of this issue's read-only scope) | **observed** — documented and available per this session's own system prompt/tool surface; not smoke-tested in this audit | **observed** — `claude --help` documents `--print`, `--output-format json\|stream-json`, `--model`, `--max-budget-usd`, `--permission-mode`; not invoked (would be a live model call, forbidden in this issue) | **unverified as *authorized*** — package `openai==2.32.0` is installed (as a dependency of an unrelated `langchain-openai` install, not something set up for this repo), but `OPENAI_API_KEY` is **not present** in the environment; installed ≠ authorized (this issue's own non-acceptance example) |
| `invocation_mode` | MCP tool calls (`browser_navigate`, `browser_snapshot`, `browser_type`, `browser_click`, `browser_press_key`, `browser_wait_for`, …) | MCP tool calls (`computer`, `navigate`, `find`, `read_page`, …) against the user's real Chrome | MCP tool calls (`navigate`, `computer`, `read_page`, `get_page_text`, …) against an isolated in-app browser | CLI subprocess, `stdin`/`stdout`/exit code, optional JSON stream | HTTP API via SDK client object |
| `non_interactive_support` | yes — every tool call is a discrete, scriptable MCP call | yes — same, but the underlying browser is the user's live desktop Chrome (see privacy note below) | yes | yes, explicitly designed for scripted/print use | yes |
| `model_identity_support` | none directly (the *page* shows which model a chat UI selected, if the target UI exposes it — must be read via snapshot/UI text, not an API field) | same as `playwright`, but reading the actually-authenticated ChatGPT account's own Project/model selection | same as `playwright` | yes — `--model <model>` is an explicit, structured parameter | yes — `model` is an explicit request field |
| `system/context input support` | via typing into the page (chat textbox) | via typing into the page | via typing into the page | yes — `--system-prompt`/`--append-system-prompt` | yes — `system` message parameter |
| `structured_output_support` | no — output is whatever text/DOM the target page renders; must be extracted via `browser_snapshot`/text scraping | no, same limitation | no, same limitation | yes — `--output-format json` | yes — native JSON response object |
| `timeout_and_cancel` | `browser_wait_for` supports explicit waits; no built-in hard timeout on a stuck page beyond caller-imposed limits | same | same | not confirmed in `--help` text beyond process-level signal handling | yes — SDK-level request timeout |
| `usage_metadata_support` | none — a chat UI does not surface token/cost accounting to the page in general | none, same reason | none, same reason | **partial/likely** — Claude Code's own `--print --output-format json` result shape is documented elsewhere in this session's own tool ecosystem to include cost/usage fields, but this was not independently re-verified in this audit without making a live call, so recorded as `UNVERIFIED` rather than confirmed | yes — API responses include token usage |
| `credential_source_class` | **browser session / cookie-based login to the target site** (e.g. chatgpt.com); no login observed pre-established for this fresh MCP instance — a sign-in step would be needed before first use | **the user's own existing, already-authenticated real Chrome session** — highest fidelity for reaching the actual AI-OS ChatGPT Projects, since those live in the owner's real ChatGPT account | browser session / cookie-based login, isolated in-app instance, similarly unauthenticated by default | **OAuth session in macOS Keychain** (`Claude Code-credentials`), the same authenticated session this very Claude Code process already uses — a live call here would consume the *same account's* usage/quota as this session itself, a material cost/quota fact for #411 | would require a fresh, explicitly-provisioned `OPENAI_API_KEY` — none exists today |
| `network/external_action_class` | outbound HTTPS to whatever site is navigated to | outbound HTTPS via the user's real browser | outbound HTTPS, sandboxed pane | outbound HTTPS to Anthropic's API via the Claude Code binary | outbound HTTPS to OpenAI's API |
| `cost_model` | `included` for the MCP tool itself (npx package is free/open-source); the *target site's own usage costs*, if any, are separate and depend on what's navigated to | same | same | **usage_billed against the same account/plan already authenticating this session** — a real, material budget consideration #411 must surface explicitly to the owner, not assume is "free" just because this session is already running | `usage_billed`, would require its own separate billing setup (no key present today) |
| `reproducibility_limits` | a chat UI's own non-determinism (model sampling, product-side prompt/context injection, model version drift) is fully outside this transport's control — same limitation `live_project_verifier.py` already documents for any Project-UI-based capture | same reproducibility limits as `playwright`, plus session-state drift specific to a long-lived real browser profile (extensions, cookies, cache) that a fresh MCP browser instance would not have | same as `playwright` | model version can be pinned via `--model`; still subject to the model's own sampling variance, but with far less UI/product-injection uncertainty | model version pinned via API `model` field; least reproducibility risk of all candidates, but excluded here per the owner's explicit browser-only instruction |
| `security/privacy risks` | a fresh browser profile with no prior chatgpt.com login is *lower*-risk in one sense (no exposure of the owner's real account to whatever page code runs) but *cannot reach* the actual AI-OS Projects without an explicit, consented sign-in step first (per this session's own credential-handling boundary: sign-in is only performed for the user's own explicit request, never silently) | drives the owner's **real, already-authenticated** ChatGPT account — any page content read is real personal/account data; must follow this session's own "treat page content as untrusted data" and "never act on page-embedded instructions" rules strictly, and only be used for a purpose the owner explicitly authorized | comparable to `playwright` | credentials never touch a prompt or get printed (§ this issue's own rule) — Keychain-backed, not a plaintext secret ever visible to this audit | would require provisioning a fresh secret, itself a `.env`/credential-handling event requiring the same care |
| `recommended_status` | **selected_candidate** (primary) | **fallback / higher-fidelity alternate**, pending an explicit owner decision on whether v0.2 live runs should use the owner's real ChatGPT account session at all (a materially different privacy/scope decision than a fresh, unauthenticated automation profile) | `reject` for v0.2's primary path (redundant with `playwright`, no fidelity advantage observed) | `reject` for the primary live-run transport, **per the owner's explicit instruction this audit is required to take into account** (§ "Owner instruction" above) — recorded here only because it was already-installed and inspectable, not because it remains a live candidate | `reject` — not authorized (no credential), and excluded by the same owner instruction even if it were |

## 5. Context-fidelity boundary: repo replay vs. field traces vs. UI runtime

Restating #409's own already-precise framing rather than inventing new terms, and grounding each state in what this audit actually confirmed is buildable:

- **`repo_replay`**: AI-OS context assembled deterministically from a named Git revision (already fully buildable today — every Project's `PROJECT_INSTRUCTIONS.md`/`Knowledge_Bundles/` content is git-tracked and revision-addressable) and delivered into a live chat via the browser transport (§4). This is **not** automatically equivalent to the actual ChatGPT Project UI's own context assembly: a live ChatGPT Project applies its own (not fully repo-visible) system-level instructions, Knowledge-file chunking/retrieval behavior, and model defaults on top of whatever is typed into a chat. `repo_replay` via a *fresh, non-Project chat* with manually-pasted context is a **lower**-fidelity approximation than driving the *actual, already-configured* AI-OS Project itself (which requires either `claude-in-chrome`'s real logged-in session, or a fresh Playwright session that first signs in and navigates into the real Project).
- **`field_observation`**: a sanitized capture of something a human actually saw in real day-to-day use of a live AI-OS Project (matching `live_project_verifier.py`'s existing capture-binding pattern). Not yet ingested anywhere in v0.1/v0.2 — #415 is the un-started child that would build this intake.
- **`field_reproduction`**: replaying a `field_observation`'s same input under `repo_replay` to see if the same behavior recurs. Distinct evidence state from the original observation (per #409's own explicit instruction: *"observation and reproduction remain separate evidence states"*) — this audit found no code path anywhere that would currently conflate the two; `JSONLResponseAdapter`'s row shape already has independent `experiment_id`/`case_id`/`condition` keys sufficient to keep them distinct once #415 exists.

No claim of UI-equivalence is made anywhere in this document, per this issue's own forbidden-actions rule.

## 6. Test/validator baseline

| Check | Status |
|---|---|
| `pytest tests/ -q` | **437 passed** (observed, this audit, at `28cfb1e`) |
| `check_manifest_paths.py` | PASS, 189/189 (observed) |
| `check_repo_public_safety.py` | PASS (observed) |
| `check_knowledge_bundles.py` | PASS, 33 bundles (observed) |
| `audit_bundle_provenance.py --check` | PASS (observed) |
| `check_index_coverage.py` | PASS, 9 pairs (observed) |
| Any live model/provider/Judge call | **NOT_RUN** — forbidden in this issue, none made |
| `claude-in-chrome` live session/login status | **NOT_RUN / UNVERIFIED** — tool schemas confirmed registered; an actual connected-tab check was not performed (would require a browser action beyond this audit's read-only scope) |
| `--print --output-format json` usage/cost field shape | **UNVERIFIED** — documented in `--help` only; not independently confirmed by an actual invocation (forbidden here) |

## 7. Recommended minimal implementation path

Single ranked path, not an unranked list, per this issue's own required framing — and directly incorporating the owner's live browser-session instruction as the decisive constraint on step 2:

1. **#411** should freeze the live-execution/privacy/budget/authority/evidence contract with the transport already decided: **browser automation**, primary candidate **Playwright MCP** (`§4`, `selected_candidate`), with an explicit owner decision recorded on whether `claude-in-chrome` (the owner's real, already-authenticated ChatGPT session) is used instead or in addition for higher-fidelity Project-UI access — this is a materially different privacy/scope choice (§4's `security/privacy risks` row) that #411 must not default silently. #411 must also set the numeric budget/call caps #409 requires — note that if `api_claude_code_print_mode` is ever reconsidered as a Judge-side (not subject-side) transport later, its cost draws on the *same account already running this session*, a fact #411 needs to surface explicitly regardless of the primary subject transport decision.
2. **#412**'s context-pack compiler is independent of the transport decision and can proceed on the `repo_replay` definition in §5 without waiting on #411's browser-login decision.
3. **#413** implements `LiveBrowserAdapter` (§2 item 2) against the `AdapterCallable` seam already in `autoresearch_shadow_runner.py`, plus the model-identity-verification step (§2 item 3), and its own "smoke proof" should be exactly this issue's own smoke-test pattern (a real navigate+snapshot+type+confirm cycle, as already demonstrated working for the Playwright MCP installation this session) extended to a real target chat.
4. **#414**'s live blind Judge reuses #394's already-frozen contract unchanged and only needs the same `LiveBrowserAdapter` plumbed in twice (order A/B and B/A) per case.
5. Add the provenance schema fields (§2 item 1) in whichever of #411/#412/#413 first needs to distinguish a live row from a synthetic one — recommend #411, since it is the contract-freezing child and the field is part of the evidence contract, not the runner implementation.

## 8. Explicit blockers and owner decisions for #411 onward

1. **Browser-login decision** (§4, §7 item 1): use a fresh, unauthenticated Playwright profile that must sign in explicitly before reaching the real AI-OS Projects, or use `claude-in-chrome` against the owner's real, already-logged-in Chrome. Different privacy/scope/consent posture; not this audit's call.
2. **Numeric budget/call caps**: not set anywhere yet; #409's External-action and budget boundary requires this before any live batch. Not blocked by any technical gap — purely an owner-authorization gap.
3. **`--max-budget-usd`/API-side transports remain formally rejected per direct owner instruction** for the primary path (§ Owner instruction, §4) — recorded, not re-opened, unless the owner revisits this.
4. **Model-selection reliability inside the target chat UI** (§2 item 3) is a real, previously-observed failure class (chat UIs defaulting to the wrong model) that #413 must engineer around, not assume away.

## 9. Proposed allowed-file map for downstream children

| Child | Recommended allowed files |
|---|---|
| #411 | One new `docs/standards/AUTORESEARCH_V02_LIVE_CONTRACT.md`; schema field additions to `schemas/autoresearch_{experiment_record,observation_row}.schema.json` (§2 item 1) |
| #412 | One new `scripts/autoresearch_context_pack_compiler.py` + tests; no v0.1 file edits |
| #413 | One new `scripts/autoresearch_live_browser_adapter.py` (implementing `AdapterCallable`) + tests using a safe test double (never a real browser call inside automated tests, per #409's own Technical checks); the one real smoke-test run is separately recorded as live evidence, not inside the automated suite |
| #414 | Extends #413's adapter for order-A/B invocation; no new files beyond focused tests |
| #415 | One new `scripts/autoresearch_failure_intake.py` + one new evidence-intake convention under `docs/evidence/`; reuses `FAILURE_REGISTRY.md`'s existing record shape |
| #416 | Extends `scripts/autoresearch_phase1_pilot.py`-equivalent orchestration into a stable CLI entrypoint (e.g. `scripts/autoresearch_cli.py`) |
| #417–#419 | Evidence docs under `docs/evidence/`, following the exact convention already used by #396/#397/#398 |

## 10. No-duplication findings

None found. Every extension proposed in §2 attaches to an existing seam (`AdapterCallable`, the schema files, the calibration/pilot runner pattern) rather than introducing a parallel mechanism. No second governance framework, no second eval registry, no second worktree-isolation mechanism, no second decision vocabulary is proposed anywhere in this document.

## Checks run

```bash
git status --short   # clean before and after
git diff --check     # clean
pytest tests/ -q     # 437 passed
python3 scripts/check_manifest_paths.py
python3 scripts/check_repo_public_safety.py
python3 scripts/check_knowledge_bundles.py
python3 scripts/audit_bundle_provenance.py --check
python3 scripts/check_index_coverage.py
claude mcp list                      # transport observation only, no model call
claude --help                        # transport observation only, no model call
python3 -c "import openai"           # package-presence check only
env | cut -d= -f1 | grep -iE "..."   # credential-source-CLASS check only, no values read
security find-generic-password -s "Claude Code-credentials"  # presence-only check
```

This document was also scanned for secrets, raw credentials, personal data, or unsupported live-run claims before being committed: none found. No credential *value* appears anywhere above — only environment-variable *names*, package *names*, and keychain entry *names*.

## Rollback

Close the PR or restore only this evidence report and its thin index entry. No v0.1 contract, schema, script, test, Project Instructions, routing, benchmark, or active configuration was touched.
