# StreamDeck v2.8 Live Prompt QA

Review date: 2026-07-06

Status: candidate QA / human review required.

## Summary verdict

Verdict: revise v2.8 candidate, then keep candidate status.

Live ChatGPT Project QA found that the v2.8 candidate prompt map is directionally usable, but v0 prompt UX was too edit-heavy because text prompts started with raw `Input: [paste]`. The candidate prompts were revised to support one button press plus zero or one paste:

```text
Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.
```

Two behavior fixes were also applied:

- `AI TREND`: initial live behavior started a web/evidence check by default. Verdict: revise. Fix: label volatile facts as `needs fresh check` and ask Sergey before any live web check. Retest result: pass.
- `CODEX`: initial live output used a non-`codex/` branch example. Verdict: revise. Fix: require repo branch prefix conventions such as `codex/...` when present. Retest result: pass.

Recommendation: keep v2.7 active and keep v2.8 candidate until Sergey manually accepts promotion after physical StreamDeck pilot.

## Test environment

- Browser surface: Codex in-app browser connected to `https://chatgpt.com/`.
- Live Projects used where visible:
  - `INBOX Router`
  - `[LLM]`
  - `[Codex]`
  - `[ANALYTICS]`
  - `[AI OS]`
- Test data: synthetic, non-sensitive prompts only.
- No raw live transcripts, private chat URLs, secrets, tokens, cookies, private files, client data, financial raw data, or runtime artifacts are committed.
- Runtime send method: `fill composer -> click send` was used for reliable browser-runtime testing after a composer state issue was observed.
- Scope limit: this is Codex browser/runtime QA. It does not prove physical StreamDeck device behavior, Elgato profile import behavior, or real key timing.

## Tested buttons matrix

| Button | Target project | Expected | Observed summary | Verdict | UX score | Fix applied | Retest result | Residual risk |
|---|---|---|---|---|---:|---|---|---|
| HOME JUDGE | `[LLM]` | Pass / revise / blocked verdict with unsupported claims and next action. | v0 returned `blocked` for unsafe production/auto-merge claim. Revised prompt then worked using last meaningful message above without manual editing. | pass | 9 | Replaced raw `Input: [paste]` with last-message/selected-text/pasted-material fallback. | Pass: returned blocked verdict from prior draft. | Browser runtime only; physical button timing not tested. |
| HOME REVISOR | `[LLM]` | Revise from Judge notes with no new unsupported facts. | Revised unsafe draft into candidate-only/v2.7-active/no-auto-merge final text using Judge verdict above. | pass | 9 | Same no-raw-placeholder UX fix. | Pass: full Draft -> HOME JUDGE -> HOME REVISOR -> Final workflow completed with no folder hopping and no prompt editing. | Depends on enough prior context being visible in the chat. |
| ROUTE / Raw -> Route | `INBOX Router` | Classify and hand off without solving owner-project work. | Routed confusing StreamDeck prompt work to `[LLM]` first, with Codex/AI OS only as downstream possibilities. | pass | 8 | Same no-raw-placeholder UX fix. | Not retested after fix; global prompt opening was mechanically updated and HOME workflow validated. | Project may still need one paste when no prior message exists. |
| CODEX / Issue -> PR | `[Codex]` | Branch, scoped files, checks, PR/human review, no auto-merge. | v0 produced branch/checks/PR workflow, but branch example did not follow repo `codex/` convention. | revise -> pass | 8 -> 9 | Added repo branch prefix convention: use `codex/...` when present. | Pass: retest suggested `codex/streamdeck-candidate-docs-only` and kept checks/draft PR/human review/no auto-merge. | Output remains a task plan, not actual execution. |
| HOME SYNC | `[Codex]` | Check repo/main/checks; avoid PR unless mismatch/change requires review. | Treated branch/check state as unknown until manual local checks and proposed manual commands; did not jump to PR creation. | pass | 8 | Same no-raw-placeholder UX fix. | Not retested after global UX fix; behavior was already aligned. | Commands are text guidance; physical StreamDeck cannot run them automatically. |
| ANALYTICS / Data Contract | `[ANALYTICS]` | Deterministic data contract with period, grain, metrics, formulas, QA. | Returned RAW/STAGE-style data contract for sanitized ticket data and required deterministic QA before memo. | pass | 8 | Same no-raw-placeholder UX fix. | Not retested after global UX fix; behavior was aligned. | Actual calculations were not run because test used synthetic contract only. |
| MEMO / Finance Memo | `[ANALYTICS]` | Memo from approved Analytics facts only; no invented deltas. | Produced memo structure with audience, period, currency, approved facts, and boundaries. | pass | 8 | Same no-raw-placeholder UX fix. | Not retested after global UX fix; behavior was aligned. | Needs real Analytics-approved facts for production memo use. |
| HOME AI TREND | `[AI OS]` | Trend triage with supported / weak / unsupported claims and no autonomous retrieval by default. | Initial behavior started live web/evidence check by default and reported web-check. | revise -> pass | 6 -> 8 | Changed prompt to label volatile facts as `needs fresh check` and ask Sergey before any live web check. | Pass: retest used KB evidence and did not report default live web check in observed summary. | AI OS may still read Project Knowledge; that is expected, but live web access must remain permissioned. |
| LOCAL AI / Safety | `[LLM]` | Candidate-only local AI boundary; prohibit sensitive data and blocked promotion items. | Returned pass for sanitized public README use and preserved exclusions for secrets/private data/vector DB/embeddings/production automation. | pass | 9 | Same no-raw-placeholder UX fix. | Not retested after global UX fix; behavior was aligned. | Does not test actual Ollama/Open WebUI runtime. |
| KB / Evidence Label | `[AI OS]` | Label claims using KB evidence; preserve candidate-only and sensitive-data boundaries. | Checked KB and began evidence labeling for v2.8 active/candidate and Local AI sensitive-data claims. | pass | 8 | Same no-raw-placeholder UX fix. | Not retested after global UX fix; behavior was aligned. | Project Knowledge may drift after manual upload/sync. |

## Minimal keyboard findings

- v0 raw placeholder pattern failed the HOME UX standard because `Input: [paste]` implies manual editing.
- Revised pattern supports:
  - one button press after a draft/answer already exists;
  - one paste maximum when material is not already in context;
  - no manual prompt-field editing;
  - clear fallback when no material exists.
- Full HOME flow tested:
  - Draft answer
  - HOME JUDGE
  - Judge verdict
  - HOME REVISOR
  - revised final
- Full flow verdict: pass.
- Full flow UX score: 9.
- Browser runtime observation: during one test, ChatGPT left previous prompt text in the composer even after an answer appeared. Reliable runtime testing then used `fill composer -> click send`. This is a Codex browser-runtime issue/observation, not proof of physical StreamDeck behavior.
- Folder hopping:
  - HOME JUDGE and HOME REVISOR passed without folder hopping in `[LLM]`.
  - Other buttons were tested in owner Projects because the task required live Project behavior where available.

## Supervised autoloop records

| Button | Iteration | Prompt version | Observed behavior | UX score | Verdict | Fix applied |
|---|---:|---|---|---:|---|---|
| HOME JUDGE | 1 | v0: `Input: [paste]` | Produced correct `blocked` verdict, but prompt required edit/paste placeholder. | 7 | revise | Replace raw placeholder with last-message/selected-text/pasted-material fallback. |
| HOME JUDGE | 2 | revised global UX prompt | Used prior draft and returned `blocked`. | 9 | pass | Final selected. |
| HOME REVISOR | 1 | v0: `Input: [paste]` | Produced useful revision when explicit draft and Judge notes were pasted, but required placeholder editing. | 7 | revise | Replace raw placeholder with last-message/selected-text/pasted-material fallback. |
| HOME REVISOR | 2 | revised global UX prompt | Used Judge verdict above and produced revised final without new unsupported facts. | 9 | pass | Final selected. |
| ROUTE / Raw -> Route | 1 | v0: `Input: [paste]` | Correctly routed to `[LLM]`, but raw placeholder pattern is not ideal. | 7 | revise | Global no-raw-placeholder update. |
| ROUTE / Raw -> Route | 2 | revised global UX prompt | Not individually retested after global update; same prompt family passed HOME workflow and no raw placeholders remain. | 8 | pass | Final selected by mechanical consistency plus prior behavior. |
| CODEX / Issue -> PR | 1 | v0 with generic non-main branch wording | Produced useful Codex workflow, but branch example did not follow repo `codex/` convention. | 8 | revise | Add repo branch prefix convention such as `codex/...` when present. |
| CODEX / Issue -> PR | 2 | revised branch-convention prompt | Returned `codex/streamdeck-candidate-docs-only`, checks, draft PR, human review, no auto-merge. | 9 | pass | Final selected. |
| HOME SYNC | 1 | v0: `Input: [paste]` | Correctly proposed sync checks and avoided PR creation by default. | 7 | revise | Global no-raw-placeholder update. |
| HOME SYNC | 2 | revised global UX prompt | Not individually retested after global update; no raw placeholders remain and behavior already matched. | 8 | pass | Final selected. |
| ANALYTICS / Data Contract | 1 | v0: `Input: [paste]` | Returned usable deterministic data contract. | 7 | revise | Global no-raw-placeholder update. |
| ANALYTICS / Data Contract | 2 | revised global UX prompt | Not individually retested after global update; no raw placeholders remain and behavior already matched. | 8 | pass | Final selected. |
| MEMO / Finance Memo | 1 | v0: `Input: [paste]` | Returned usable memo structure from approved facts. | 7 | revise | Global no-raw-placeholder update. |
| MEMO / Finance Memo | 2 | revised global UX prompt | Not individually retested after global update; no raw placeholders remain and behavior already matched. | 8 | pass | Final selected. |
| HOME AI TREND | 1 | v0: `Input: [paste]` plus `Use fresh web check when facts may have changed.` | Started live web/evidence check by default. | 6 | revise | Remove default live web check; label as `needs fresh check` and ask Sergey before live web check. |
| HOME AI TREND | 2 | revised no-web-by-default prompt | Used KB evidence and did not report default live web check in observed summary. | 8 | pass | Final selected. |
| LOCAL AI / Safety | 1 | v0: `Input: [paste]` | Preserved candidate-only and sensitive-data exclusions. | 8 | revise | Global no-raw-placeholder update for consistency. |
| LOCAL AI / Safety | 2 | revised global UX prompt | Not individually retested after global update; no raw placeholders remain and behavior already matched. | 9 | pass | Final selected. |
| KB / Evidence Label | 1 | v0: `Input: [paste]` | Used KB evidence labels for candidate/active/sensitive-data claims. | 7 | revise | Global no-raw-placeholder update. |
| KB / Evidence Label | 2 | revised global UX prompt | Not individually retested after global update; no raw placeholders remain and behavior already matched. | 8 | pass | Final selected. |

## Prompt changes made

### Global no-raw-placeholder UX update

Applied to all v2.8 prompt entries in JSON, CSV, and setup markdown.

v0:

```text
Input:
[paste]
```

Final selected prompt opening:

```text
Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.
```

Reason selected: meets HOME UX pass rule by avoiding manual prompt editing, allowing one paste maximum, and providing clear fallback.

### AI TREND web-check fix

v0:

```text
Use fresh web check when facts may have changed.
```

Final selected:

```text
If facts may have changed, label them as needs fresh check and ask Sergey before any live web check.
```

Reason selected: preserves evidence discipline without autonomous retrieval.

### CODEX branch convention fix

v0:

```text
create or use a non-main branch, make minimal reversible changes
```

Final selected:

```text
create or use a non-main branch following repo branch prefix conventions such as `codex/...` when present, make minimal reversible changes
```

Reason selected: aligns Codex prompts with repo branch convention while preserving branch/checks/PR/human review/no-auto-merge behavior.

## Final selected prompts by tested button

Each final selected prompt is stored in:

- `AIOS_StreamDeck_Button_Map_v2.8_COMMAND_SURFACE_ALIGNED.json`
- `AIOS_StreamDeck_Button_Map_v2.8_COMMAND_SURFACE_ALIGNED.csv`
- `AIOS_StreamDeck_Setup_Instruction_v2.8_COMMAND_SURFACE_ALIGNED.md`

| Tested button | v0 prompt | Revised prompt(s) | Final selected prompt | Why selected | UX score improvement |
|---|---|---|---|---|---:|
| HOME JUDGE | `HOME / JUDGE` with `Input: [paste]`. | Global no-raw-placeholder opening. | `HOME / JUDGE`: last meaningful message, selected text, or pasted material; verdict `pass / revise / blocked`. | Passed full HOME workflow without prompt editing. | 7 -> 9 |
| HOME REVISOR | `HOME / REVISOR` with `Input: [paste]`. | Global no-raw-placeholder opening. | `HOME / REVISOR`: last meaningful message, selected text, or pasted material; revise using Judge notes; no new unsupported facts. | Used Judge verdict above and produced final text without folder hopping. | 7 -> 9 |
| ROUTE / Raw -> Route | `ROUTE / Raw -> Route` with `Input: [paste]`. | Global no-raw-placeholder opening. | `ROUTE / Raw -> Route`: classify and hand off, solve never. | Live routing was correct; revised opening removes edit burden. | 7 -> 8 |
| CODEX / Issue -> PR | `CODEX / Issue -> PR` with generic non-main branch wording. | Global no-raw-placeholder opening; branch convention fix. | `CODEX / Issue -> PR`: follow repo branch prefix conventions such as `codex/...`, run checks, draft PR, human review, no auto-merge. | Retest produced `codex/...` branch and preserved PR safety gates. | 8 -> 9 |
| HOME SYNC | `HOME / SYNC` with `Input: [paste]`. | Global no-raw-placeholder opening. | `HOME / SYNC`: check repo/main/checks and avoid PR unless mismatch/change requires review. | Live behavior avoided premature PR; revised opening removes edit burden. | 7 -> 8 |
| ANALYTICS / Data Contract | `ANALYTICS / Data Contract` with `Input: [paste]`. | Global no-raw-placeholder opening. | `ANALYTICS / Data Contract`: deterministic contract with layer, period, grain, metrics, formulas, QA. | Live output was directly usable; revised opening removes edit burden. | 7 -> 8 |
| MEMO / Finance Memo | `MEMO / Finance Memo` with `Input: [paste]`. | Global no-raw-placeholder opening. | `MEMO / Finance Memo`: memo from approved Analytics facts only. | Live output preserved approved-facts boundary; revised opening removes edit burden. | 7 -> 8 |
| HOME AI TREND | `HOME / AI TREND` with `Input: [paste]` and default fresh web check wording. | Global no-raw-placeholder opening; no-web-by-default fix. | `HOME / AI TREND`: label volatile facts as `needs fresh check` and ask Sergey before any live web check. | Retest avoided default live web check and preserved evidence labels. | 6 -> 8 |
| LOCAL AI / Safety | `LOCAL AI / Safety` with `Input: [paste]`. | Global no-raw-placeholder opening. | `LOCAL AI / Safety`: candidate-only local experiment, sensitive-data and blocked-promotion guard. | Live output preserved safety boundary; revised opening removes edit burden. | 8 -> 9 |
| KB / Evidence Label | `KB / Evidence Label` with `Input: [paste]`. | Global no-raw-placeholder opening. | `KB / Evidence Label`: label claims as supported, weak, mixed, unsupported, or needs fresh check. | Live output used KB evidence labels; revised opening removes edit burden. | 7 -> 8 |

## Buttons not tested

The minimum required buttons were tested:

- HOME JUDGE
- HOME REVISOR
- ROUTE / Raw -> Route
- CODEX / Issue -> PR
- HOME SYNC
- ANALYTICS / Data Contract
- MEMO / Finance Memo
- HOME AI TREND
- LOCAL AI / Safety
- KB / Evidence Label

Not all Level 2 buttons were live-tested. Untested buttons inherit the global no-raw-placeholder update where applicable, but still need future pilot QA before promotion.

## Recommendation

- Keep v2.7 active.
- Keep v2.8 as candidate.
- Do not promote v2.8 active until Sergey accepts it after manual/physical StreamDeck pilot.
- Proceed with human review of the revised v2.8 candidate prompts.

## Residual risks

- Physical StreamDeck device behavior was not tested.
- Elgato profile import/export behavior was not tested.
- ChatGPT Project Knowledge and runtime behavior can drift after manual uploads or settings changes.
- Live QA used synthetic non-sensitive inputs, not real production work.
- Some revised prompts were not individually retested after the global placeholder fix; they were accepted based on prior aligned live behavior plus mechanical no-placeholder consistency.
