# Local Model Eval Matrix

## Purpose

Evaluate local model usefulness with lightweight checklist evals.

This matrix is for pilots, not benchmark infrastructure. It does not add SWE-Bench, RAGAS, vector DB, embeddings, semantic search, autonomous eval agents, or production automation.

## Matrix

| Eval area | Check | Pass | Revise | Blocked |
|---|---|---|---|---|
| Context discipline | Uses curated excerpts | sources named and no raw dump | context needs trimming | requires forbidden inputs |
| Draft quality | Produces usable draft | clear draft with limitations | style or structure needs revision | unsupported claims dominate |
| Retrieval pilot | Finds relevant excerpts | excerpts trace to source | misses some evidence | treats retrieval as final truth |
| Judge/revise | Supports review loop | unsupported claims listed | judge criteria unclear | no review path |
| Security | Respects boundary | no secrets or production data | unclear data classification | secrets, `.env`, credentials, API keys, raw logs, or runtime artifacts needed |
| Analytics boundary | Does not calculate truth | routes calculations to `[Analytics]` | wording overstates numbers | performs unverified calculations |
| Production boundary | Stays experimental | no production automation | promotion criteria unclear | production workflow requested |

## Model Record

```text
model_or_surface:
use_case:
context_type:
sample_task:
result:
limitations:
security_status:
judge_verdict:
next_step:
```

## Comparison Rules

- Compare local models by task class, not by hype.
- Use the same curated context for each model.
- Keep outputs short enough to review.
- Treat results as candidate evidence only.
- Use judge/revise before reuse.
- State limitations every time.

## Hardware Notes

Hardware choices, including RTX 3090, home server budget, power/noise tradeoffs, and upgrade timing, belong in `[Thinking]` as a decision memo.

Do not embed hardware purchase decisions as main AI-OS setup or production architecture.
