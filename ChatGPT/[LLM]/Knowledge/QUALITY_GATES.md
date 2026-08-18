# LLM Quality Gates

## Output QA

- [ ] Does the output answer the task?
- [ ] Are facts separated from interpretations?
- [ ] Are unsupported claims marked?
- [ ] Is confidence stated?
- [ ] Are sources/evidence referenced when available?
- [ ] Are limitations visible?
- [ ] Is routing correct?
- [ ] Is the output actionable?

## Hallucination checks

1. Ask: what claims are not supported?
2. Remove or mark them.
3. Check against AI OS or source context when needed.
4. For memo generation, apply the Judge triggers and no-Judge acceptance rule in `MEMO_GENERATION_WORKFLOW.md`.
5. Revise only from explicit findings; a `pass` result does not trigger a rewrite.

## Verdict

```text
quality_status: pass / revise / blocked
reason:
unsupported_claims:
required_revision:
```
