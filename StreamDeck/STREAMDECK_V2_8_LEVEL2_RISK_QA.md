# StreamDeck v2.8 Level 2 Risk QA

Review date: 2026-07-06

Status: candidate QA / human review required.

## Summary verdict

Verdict: revise v2.8 candidate, keep candidate status.

This pass intentionally tested only high-risk / high-frequency / high-impact Level 2 prompts. It did not test all 195 button rows.

Overall result:

- Tested target buttons: 27.
- Passed: 26.
- Blocked / human choice needed: 1.
- Prompt fix applied: `REVISOR / Prompt Revise`.
- v2.8 remains candidate-only.
- v2.7 remains active.

Blocked item:

- `REVISOR / Prompt Revise`: live output repeatedly reintroduced raw input placeholders when asked to revise a prompt draft containing that bad pattern. The candidate prompt was strengthened, but live retests still failed. Keep this button candidate / blocked until Sergey accepts a different behavior or the owner Project instructions are tightened.

## Test environment

- Browser surface: Codex in-app browser connected to ChatGPT.
- Runtime method: `fill composer -> click send`, same reliable method recorded in `STREAMDECK_V2_8_LIVE_PROMPT_QA.md`.
- Live Projects used:
  - `[LLM]`
  - `[Codex]`
  - `[ANALYTICS]`
  - `[AI OS]`
- Test data: synthetic, non-sensitive prompts only.
- No raw live transcripts, private chat URLs, secrets, tokens, cookies, private files, client data, financial raw data, or runtime artifacts are committed.
- This is browser/runtime QA, not physical StreamDeck device QA.

## Tested buttons matrix

| Button | Target project | Expected | Observed summary | Verdict | UX score | Fix applied | Retest result | Residual risk |
|---|---|---|---|---|---:|---|---|---|
| JUDGE / PR Judge | `[LLM]` | Block unsafe PR readiness and auto-merge claims. | Returned `blocked`; flagged production-readiness and auto-merge claims. | pass | 9 | none | not needed | Browser runtime only. |
| JUDGE / Analytics | `[LLM]` | Require deterministic calculation evidence. | Returned `blocked`; no source data, period, or deterministic calculation evidence. | pass | 9 | none | not needed | Synthetic data only. |
| JUDGE / Evidence | `[LLM]` | Label supported/unsupported evidence claims. | Returned `blocked`; supported candidate-only claim and blocked sensitive/local-AI and auto-browse claims. | pass | 9 | none | not needed | Summary only, no raw transcript committed. |
| JUDGE / Final Gate | `[LLM]` | Compare acceptance criteria and observed checks. | Returned `pass` for no placeholders, live QA recorded, candidate-only status, and observed checks. | pass | 9 | none | not needed | Depends on truthful supplied check summary. |
| REVISOR / No New Claims | `[LLM]` | Detect and remove unsupported new claims. | Flagged `v2.8 is active` and `production-ready` as unsupported. | pass | 9 | none | not needed | Needs source/Judge context in real use. |
| REVISOR / File-ready | `[LLM]` | Produce file-ready final from approved facts only. | Produced concise file-ready status artifact preserving candidate-only and browser-QA limits. | pass | 8 | none | not needed | Formatting still needs human taste check. |
| REVISOR / Prompt Revise | `[LLM]` | Rewrite unsafe prompt without raw input placeholders. | Initial output reintroduced raw input placeholders. | blocked | 4 | Strengthened prompt to require approved StreamDeck UX opening and block if placeholders remain. | Still reintroduced raw placeholders after 3 revised attempts. | Human choice needed; likely Project-level instruction/rubric issue. |
| CODEX / Goal -> Issue | `[Codex]` | Produce issue-ready brief without atomic burden. | Returned goal, context, allowed scope, forbidden actions, checks, rollback, human review. | pass | 9 | none | not needed | It prepares issue text only. |
| CODEX / Run Checks | `[Codex]` | Manual-only smallest relevant checks. | Returned manual command list including repo status, diff, and checks; no execution/automerge. | pass | 9 | none | not needed | Commands still require manual/Codex execution. |
| CODEX / Branch Pack | `[Codex]` | Bounded branch task pack with `codex/...` convention. | Returned bounded docs-only package using Goal Mode and `codex/...` branch. | pass | 9 | none | not needed | Does not execute package. |
| CODEX / Review Report | `[Codex]` | Factual report only, no invented tests. | Summarized supplied changed files and observed `git diff --check`; did not invent broader results. | pass | 8 | none | not needed | Depends on accurate supplied facts. |
| ANALYTICS / QA Checks | `[ANALYTICS]` | Deterministic QA checks with expected/failure meaning. | Returned schema, period, duplicate, null, and reconciliation checks. | pass | 9 | none | not needed | Synthetic contract only. |
| ANALYTICS / Reconcile | `[ANALYTICS]` | Reconciliation plan with layers and join keys. | Identified RAW/MART layers, join key, counts by product, and exceptions. | pass | 9 | none | not needed | No actual data run. |
| ANALYTICS / Formula Review | `[ANALYTICS]` | Formula QA for denominator, period, grain, SQL/Python. | Reviewed `resolution_rate`, inputs, zero denominator, period, and implementation constraints. | pass | 9 | none | not needed | No actual calculation run. |
| ANALYTICS / Supervised Loop | `[ANALYTICS]` | Stop when QA/data/grain insufficient. | Returned `qa_status: blocked` because data/grain were insufficient. | pass | 9 | none | not needed | Synthetic blocked case only. |
| MEMO / Final Memo | `[ANALYTICS]` | Final memo from approved sections only. | Produced memo limited to approved facts and QA status. | pass | 8 | none | not needed | Human editorial review still useful. |
| MEMO / Judge/Revise | `[ANALYTICS]` | Block unsupported memo claims and revise safely. | Returned `blocked`; removed unsupported cost-doubled and layoffs claims. | pass | 9 | none | not needed | Depends on approved facts. |
| MEMO / Recommend | `[ANALYTICS]` | Recommendations that do not exceed evidence. | Recommended cautious investigate/localize actions, not root-cause claims. | pass | 8 | none | not needed | Needs real business context before use. |
| AI OS / Governance | `[AI OS]` | Block blocked-promotion items. | Checked KB and treated semantic search, embeddings, autonomous retrieval, and production web UI as blocked/not promoted. | pass | 8 | none | not needed | Summary is from browser runtime, not committed transcript. |
| AI OS / Evidence Check | `[AI OS]` | Label active/candidate/physical-test claims. | Checked KB and labeled candidate-only vs active/physical-test claims. | pass | 8 | none | not needed | Project Knowledge can drift. |
| AI OS / Agent Loop | `[AI OS]` | Supervised loop design only. | Checked KB and produced supervised-loop framing with stop/human gates. | pass | 8 | none | not needed | Must remain design-only unless separately implemented. |
| LOCAL AI / No Sensitive | `[LLM]` | Block sensitive/client/API/raw-financial data. | Returned `Allowed: no` and listed sensitive items to remove. | pass | 9 | none | not needed | Does not test real local runtime. |
| LOCAL AI / Record Pilot | `[LLM]` | Record pilot result from observed non-sensitive test only. | Produced pilot result fields with candidate verdict and no private data. | pass | 9 | none | not needed | Synthetic pilot note only. |
| LOCAL AI / Judge Output | `[LLM]` | Judge unsafe local AI output. | Returned `blocked`; flagged private client exports, embeddings/search, and candidate-only boundary. | pass | 9 | none | not needed | Does not test real local runtime. |
| KB / Upload Check | `[AI OS]` | Manual upload/sync checklist. | Checked KB and produced manual sync/check framing; did not claim repo checks prove runtime sync. | pass | 8 | none | not needed | Actual ChatGPT upload sync still manual. |
| KB / Bundle Sync | `[AI OS]` | Minimal source/bundle sync task. | Checked KB and produced minimal sync/check framing. | pass | 8 | none | not needed | Does not perform file sync. |
| KB / Source Truth | `[AI OS]` | Identify source of truth. | Checked KB and identified repository candidate files as source of truth, not live response text. | pass | 8 | none | not needed | Project Knowledge can drift. |

## Prompt changes made

### REVISOR / Prompt Revise

Observed bug:

- The live `[LLM]` response repeatedly reintroduced raw input-placeholder patterns while revising a prompt draft that contained them.

Fix attempted:

- Candidate prompt now says to remove original input-template sections.
- It requires the revised prompt to begin with the approved StreamDeck UX opening.
- It says to return `Verdict: blocked` instead of a revised prompt if placeholders cannot be removed safely.

Retest result:

- Still returned a prompt containing raw input-placeholder patterns after 3 revised attempts.

Final QA verdict:

- `blocked / human choice needed`.

Recommendation:

- Keep `REVISOR / Prompt Revise` in candidate status.
- Do not rely on it for final prompt cleanup until Sergey either accepts the risk or the `[LLM]` Project instructions are tightened.

## Buttons intentionally not tested

This was a risk-based pass. It did not test:

- every Level 2 button;
- every HOME button already covered by `STREAMDECK_V2_8_LIVE_PROMPT_QA.md`;
- all 195 JSON/CSV rows;
- physical StreamDeck device behavior.

## Recommendation

- Keep v2.7 active.
- Keep v2.8 candidate.
- Do not promote v2.8 active until Sergey accepts the candidate after manual/physical StreamDeck pilot.
- Treat `REVISOR / Prompt Revise` as blocked or high-risk until resolved.

## Residual risks

- Physical StreamDeck device behavior remains untested.
- Elgato profile import/export behavior remains untested.
- ChatGPT Project runtime behavior can drift after manual Knowledge sync or settings changes.
- Live QA used synthetic, non-sensitive data only.
- Browser summaries are recorded, not raw transcripts.
- One target button remains blocked despite prompt-level fixes.
