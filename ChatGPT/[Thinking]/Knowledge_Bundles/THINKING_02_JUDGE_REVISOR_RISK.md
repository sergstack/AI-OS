# [Thinking] — Judge Revisor Risk

## Purpose

Compact upload artifact for [Thinking] covering judge revisor risk.

## Source files

- `ChatGPT/[Thinking]/Knowledge/JUDGE_REVIEW.md`
- `ChatGPT/[Thinking]/Knowledge/REVISOR_REWRITE.md`
- `ChatGPT/[Thinking]/Knowledge/RISK_REVIEW.md`
- `ChatGPT/[Thinking]/Knowledge/STRATEGY_OPTIONS_TEMPLATE.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[Thinking]`.

## Status

- bundle_type: compact upload artifact
- source_of_truth: granular files listed above
- production_promotion: no, unless explicitly accepted elsewhere

---

# Content

## From: `ChatGPT/[Thinking]/Knowledge/JUDGE_REVIEW.md`

# Judge Review
## Role
## What to check
1. unsupported claims;
2. hidden assumptions;
3. missing alternatives;
4. ignored downside;
5. too broad scope;
6. weak evidence;
7. project routing errors;
8. premature automation;
9. no acceptance criteria;
## Judge prompt
```text
Act as @judge.
Review the proposal below.

Check:
- unsupported claims
- weak evidence
- hidden assumptions
- risks
- wrong project routing
- missing acceptance criteria
- premature automation

Return:
1. Verdict: pass / revise / blocked
2. Critical issues
3. Weak evidence
4. Required revisions
5. Safer next step
```
## Verdict rules
- `pass`: usable as is.
- `revise`: useful but needs correction.
- `blocked`: unsafe, unsupported, or wrong project.


## From: `ChatGPT/[Thinking]/Knowledge/REVISOR_REWRITE.md`

# Revisor Rewrite Standard
## Purpose
## Rule
## Required behavior
- does not add new facts;
- preserves supported / weak / unsupported distinctions;
- preserves risks and confidence;
- makes output shorter and decision-ready;
- flags missing evidence instead of hiding it.
## Output discipline
- tighten wording;
- reduce repetition;
- improve structure;
- make handoff clearer;
- preserve the original conclusion status.
Revisor must not:
- upgrade weak evidence to fact;
- delete blockers;
- delete uncertainty;
- invent missing support;
- change the decision without explicit justification.


## From: `ChatGPT/[Thinking]/Knowledge/RISK_REVIEW.md`

# Risk Review
## Use when
- решение дорогое;
- последствия трудно откатить;
- evidence неполный;
- есть operational или reputational risk;
- задача передаётся в Codex.
## Checklist
| Evidence | Какие выводы supported, weak, unsupported? |
| QA | Как понять, что решение сработало? |
## Output
```text
Risk level: low / medium / high
Main blocker:
Weak assumptions:
Mitigations:
Decision: proceed / revise / stop / handoff
```


## From: `ChatGPT/[Thinking]/Knowledge/STRATEGY_OPTIONS_TEMPLATE.md`

# Strategy Options Template
```markdown
# Strategy Options

## Question

## Options

| Option | What it means | Best when | Pros | Cons | Risk | Cost | Reversibility |
|---|---|---|---|---|---|---|---|

## Comparison

| Criterion | Option A | Option B | Option C |
|---|---|---|---|
| Speed | | | |
| Quality | | | |
| Cost | | | |
| Risk | | | |
| Evidence | | | |
| Complexity | | | |

## Recommendation

## Why not the alternatives

```
