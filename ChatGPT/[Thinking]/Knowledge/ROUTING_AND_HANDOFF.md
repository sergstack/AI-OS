# Routing and Handoff

Canonical destination routing is defined in repo-root `ROUTING_RULES.md`.

Правило владения `[LLM]`: если основной результат — reusable prompt, выбор
модели или LLM workflow и стратегическое решение не запрошено, направь задачу в
`[LLM]` с фокусным, исполнимым handoff. Сохрани релевантные decision constraints,
запрошенный результат, критерии приёмки и следующий шаг; не убирай сведения,
нужные для продолжения работы. Не проектируй prompt, model routing или
downstream workflow в `[Thinking]`.

Use the canonical handoff fields in `HANDOFF_STYLE_STANDARD.md`.

## Thinking → Analytics

Используй, когда decision или scenario требует расчётов.

Передать:
- question;
- metrics;
- period;
- assumptions;
- options to test;
- expected analytical output.

## Analytics → LLM

Используй, когда verified numbers нужно превратить в memo, summary или narrative.

Передать:
- curated facts;
- tables or marts;
- reconciled metrics;
- limitations;
- tone and output format.

## LLM → Codex

Используй, когда нужен код для автоматизации prompt/memo/report workflow.

Передать:
- prompt spec;
- input/output contract;
- files to inspect;
- forbidden actions;
- tests;
- acceptance criteria.

## Codex → QA / Release

Передать:
- changed files;
- tests run;
- smoke QA;
- acceptance status;
- residual risks;
- rollback notes.
