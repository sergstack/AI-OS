# Communication QA Checklist

Status: candidate / ready for human review.
Purpose: QA checklist for executive, finance, audit, chart, and decision communication after Analytics QA.

## Source and scope

- [ ] Main message exists.
- [ ] Source exists.
- [ ] Period exists.
- [ ] Scope / population exists.
- [ ] Metric / amount / fact exists where applicable.
- [ ] Currency / units are visible where applicable.
- [ ] Evidence cards, source mart, or accepted source references are listed.

## Evidence and claims

- [ ] Facts are separated from interpretation.
- [ ] Limitations are visible.
- [ ] Confidence is visible.
- [ ] Unsupported claims are removed or marked.
- [ ] Root cause is evidenced or marked `requires management confirmation`.
- [ ] Recommendation traces to verified facts.
- [ ] Recommendation is actionable.
- [ ] Owner / next step is visible.

## Analytics-first guardrails

- [ ] Analytics facts came before LLM narrative.
- [ ] Deterministic checks came before narrative.
- [ ] LLM arithmetic was not used.
- [ ] LLM variance, driver, exposure, or root-cause calculation was not used.
- [ ] No new facts, metrics, causes, or recommendations were invented.

## Output safety

- [ ] No private/client/vendor/employee/bank/invoice/payment/tax ID/personal data.
- [ ] No secrets or credentials.
- [ ] No raw dumps or runtime artifacts.
- [ ] No production reporting automation is implied.
- [ ] No deck generator or raw-data-to-deck workflow is implied.

## Verdict

QA verdict: pass / revise / blocked
Reason:
Unsupported claims:
Missing evidence:
Overclaimed root cause:
Weak recommendation:
Required revision:
Approved next step:
