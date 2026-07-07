# Chart Commentary Standard

Status: candidate / ready for human review.
Purpose: concise chart commentary based only on verified Analytics chart data and QA.

## Required inputs

Chart ID:
Chart source:
Source mart / slice:
Period:
Scope / population:
Metric / amount / fact:
Grain:
Filters:
QA status:
Limitations:

## Commentary structure

What it shows:
What changed:
Why it matters:
What to do next:

## Evidence

Source:
Period:
Scope / population:
Metric / amount / fact:
Confidence:

## Guardrails

- Do not infer unsupported causes from visual shape.
- Do not calculate variance, exposure, driver impact, or root cause by LLM.
- If cause is not evidenced, write `requires management confirmation`.
- Recommendation must trace to verified chart facts or accepted Analytics findings.
- Keep limitations visible.
