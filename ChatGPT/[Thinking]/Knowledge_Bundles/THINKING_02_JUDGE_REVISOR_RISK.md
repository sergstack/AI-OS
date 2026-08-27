# [Thinking] — Judge Revisor Risk

## Purpose

Compact upload artifact for [Thinking] covering judge revisor risk.

## Source files

- `ChatGPT/[Thinking]/Knowledge/JUDGE_REVIEW.md`
- `ChatGPT/[Thinking]/Knowledge/REVISOR_REWRITE.md`
- `ChatGPT/[Thinking]/Knowledge/RISK_REVIEW.md`
- `ChatGPT/[Thinking]/Knowledge/STRATEGY_OPTIONS_TEMPLATE.md`
- `ChatGPT/[Thinking]/Knowledge/THINKING_02_JUDGE_REVISOR_RISK_BUNDLE_SEMANTICS.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[Thinking]`.

## Status

- production_promotion: no, unless explicitly accepted elsewhere
- bundle_type: generated compact upload artifact
- source_of_truth: declared granular source files
- source_fingerprint: sha256:93039eb8844a2dbd1537459179bae4e783026168fd22f7f663b747ce77f48593
- generator: scripts/build_knowledge_bundles.py

---

# Content

## From: `ChatGPT/[Thinking]/Knowledge/JUDGE_REVIEW.md`

# Judge Review
## Role
`@judge` — критик результата. Не переписывает красиво, а ищет слабые места.
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
10. no rollback.
## Karpathy minimality check
Before verdict, check:
1. Is the proposal creating a new layer to fight complexity?
2. Can the workflow fit on one page?
3. Is there one clear input, one transformation, one QA check, and one output?
4. Are facts, assumptions, hypotheses, weak claims, and unsupported claims separated?
5. Are acceptance criteria defined?
6. Is rollback / deletion rule defined?
7. Has the workflow passed 3 pilot cases?
8. Is routing correct:
   - prompts / LLM workflow → [LLM]
   - strategy / risks → [Thinking]
   - data / deterministic calculations → [Analytics]
   - implementation / tests → [Codex]
   - AI OS pattern / evidence → [AI OS]
Verdict rule:
- If a proposal adds a new mode, automation, folder, dashboard, agentic workflow, or broad repo change before pilot evidence, verdict must be `revise` or `blocked`.
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
Define `@revisor` as a rewrite role after judge review.
## Rule
Revisor rewrites the result without adding new facts.
## Required behavior
- does not add new facts;
- preserves supported / weak / unsupported distinctions;
- preserves risks and confidence;
- makes output shorter and decision-ready;
- flags missing evidence instead of hiding it.
## Output discipline
Revisor may:
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
| Area | Questions |
|---|---|
| Assumptions | Что мы считаем правдой без проверки? |
| Evidence | Какие выводы supported, weak, unsupported? |
| Reversibility | Можно ли откатить решение? |
| Blast radius | Что сломается при ошибке? |
| Dependencies | От кого/чего зависит успех? |
| Timing | Почему сейчас? Что изменится позже? |
| QA | Как понять, что решение сработало? |
| Stop conditions | Когда остановиться? |
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
## Open assumptions
## Next step
```

## From: `ChatGPT/[Thinking]/Knowledge/THINKING_02_JUDGE_REVISOR_RISK_BUNDLE_SEMANTICS.md`

# Migrated Bundle Semantics
Canonical source created during Issue #285 provenance migration.
Legacy bundle provenance: `ChatGPT/[Thinking]/Knowledge_Bundles/THINKING_02_JUDGE_REVISOR_RISK.md`.
## Legacy section: `ChatGPT/[Thinking]/Knowledge/JUDGE_REVIEW.md`
Verdict rule: if a proposal adds a new mode, automation, folder, dashboard, agentic workflow, or broad repo change before pilot evidence, verdict must be `revise` or `blocked`.
