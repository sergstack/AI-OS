# Prompt QA Factory

Prompt QA Factory is the AI-OS standard for turning reusable prompts into accepted prompt assets.

It applies to StreamDeck prompts, ChatGPT Project prompts, Codex prompts, Judge/Revisor prompts, and Analytics memo prompts.

## Core Loop

```text
candidate -> test -> judge -> revise -> selected
```

The loop is supervised only. A prompt is not selected until a human accepts the final version.

## Statuses

| Status | Meaning |
|---|---|
| `candidate` | Draft prompt proposed for a repeated use case. It may be useful, but it is not accepted yet. |
| `test` | Candidate is run against small, representative cases. |
| `judge` | Output is reviewed against explicit criteria and risks. |
| `revise` | Prompt is changed only to address observed test or judge findings. |
| `selected` | Final prompt is accepted for reuse by the owner reviewer. |

## How To Test

Use the smallest representative set of cases that shows whether the prompt is useful in real work.

Each test should record:

- input context;
- expected output shape;
- actual output or observed behavior;
- friction points;
- unsupported claims or missing constraints;
- whether the prompt stayed inside the allowed scope.

For Analytics memo prompts, deterministic calculations must happen in Python or SQL before the prompt writes or reviews narrative.

## How To Judge

Judge against the intended workflow, not against whether the prompt sounds polished.

Minimum criteria:

- goal fit;
- output schema fit;
- source discipline;
- low-friction UX;
- no invented facts;
- no hidden automation;
- no sensitive data exposure;
- residual risks visible.

## Revision Rule

Revise only from observed evidence:

- failed or weak test case;
- judge finding;
- user friction;
- missing acceptance requirement;
- unsafe or unsupported behavior.

Do not broaden the prompt into a general agent, autonomous workflow, retrieval system, or production automation.

## Selection Rule

A prompt can be marked `selected` only when:

- test cases are recorded;
- judge criteria are recorded;
- UX score is recorded;
- residual risks are recorded;
- owner acceptance status is `accepted`;
- no blocked item is required.

## Supervision Boundary

Prompt QA Factory follows AI-OS supervised loop governance.

Allowed:

- local prompt drafting and revision;
- human-reviewed test cases;
- judge/revisor review;
- repository documentation or PR diffs;
- candidate / ready-for-human-review status before acceptance.

Forbidden:

- production automation;
- sensitive data;
- autonomous retrieval;
- vector DB, embeddings, or semantic search;
- auto-merge;
- claiming production readiness.

## UX Score

Record UX score as `1` to `5`.

| Score | Meaning |
|---|---|
| `1` | Confusing or high-friction. |
| `2` | Usable only with extra explanation. |
| `3` | Works for the narrow case but has visible friction. |
| `4` | Reusable with minor residual risks. |
| `5` | Low-friction, clear, and ready for accepted reuse. |

## Prompt QA Record

```markdown
# Prompt QA Record

## Prompt name

## Owner project

## Use case

## Candidate prompt

## Test cases

## Judge criteria

## Iterations

## Final selected prompt

## UX score

## Residual risks

## Acceptance status
```

## Use By Prompt Type

| Prompt type | Owner | Typical test |
|---|---|---|
| StreamDeck prompts | `[LLM]` / `[Codex]` | Button command produces the intended low-friction result. |
| ChatGPT Project prompts | Owner project | Project follows source, routing, and output rules. |
| Codex prompts | `[Codex]` | Repo task stays bounded, reversible, and verifiable. |
| Judge/Revisor prompts | `[Thinking]` / `[LLM]` | Judge finds unsupported claims; Revisor improves without adding claims. |
| Analytics memo prompts | `[Analytics]` / `[LLM]` | Narrative uses deterministic results and shows assumptions, periods, currencies, and risks. |

## Done Criteria

The prompt record is complete, the final prompt is selected or explicitly left as a candidate, residual risks are visible, and owner acceptance is recorded.
