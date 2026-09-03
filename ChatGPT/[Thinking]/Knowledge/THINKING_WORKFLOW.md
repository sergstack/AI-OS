# Thinking Workflow

Status: candidate reference (see `CURRENT_STATUS.md`), not the governing
workflow. For a material complex case, `PROJECT_INSTRUCTIONS.md`'s "Базовый
workflow" is canonical — it adds a Lens gate (`THINKERS_LENS_ROUTER.md`),
Conflict check (`THINKERS_CONFLICT_MAP.md`), and an application-Log step that
this simplified 7-step version omits. Use this file only for the general
shape; use `PROJECT_INSTRUCTIONS.md` for anything thinker-pattern-related.

## Purpose

Использовать для сложных решений, стратегии, рисков и выбора маршрута.

## Workflow

1. **Frame**
   - Какой вопрос решаем?
   - Какой decision/output нужен?
   - Кто пользователь результата?

2. **Facts**
   - Что известно?
   - Какие источники есть?
   - Что подтверждено, а что предположение?

3. **Options**
   - 2–4 варианта.
   - Для каждого: upside, downside, cost, reversibility.

4. **Criteria**
   - speed;
   - risk;
   - cost;
   - evidence strength;
   - operational complexity;
   - dependency on other projects.

5. **Risk review**
   - hidden assumptions;
   - failure modes;
   - what can go wrong;
   - how to detect failure.

6. **Decision**
   - recommendation;
   - why now;
   - what not to do;
   - what to defer.

7. **Handoff**
   - Analytics for calculations.
   - LLM for prompts/memo generation.
   - Codex for implementation.
   - AI OS for supported KB pattern.

## Output format

```text
Decision:
Reason:
Options considered:
Risks:
Assumptions:
Confidence:
Next step:
```
