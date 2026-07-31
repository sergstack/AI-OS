# Smoke QA For Inbox Router

Run these tests after updating the ChatGPT Project.

| # | Input | Expected result |
|---:|---|---|
| 1 | Надо разобраться с налогами | Things task with title, area, next action, and no fake deadline. |
| 2 | Нашёл новую AI-фичу, хочу понять, полезна ли она мне | Handoff to `[AI OS]`, not Things-only. |
| 3 | Стоит ли мне покупать mini PC или Raspberry Pi для self-hosted app? | Handoff to `[Thinking]` or decision framing, not Codex. |
| 4 | Нужно посчитать экономию от автоматизации отчёта | Handoff to `[Analytics]` with metrics, period, and inputs. |
| 5 | Нужно поправить скрипт и добавить тесты | Handoff to `[Codex]` with objective, allowed files, checks, and acceptance criteria. |
| 6 | Хочу добавить новую книгу Деминга и обновить межавторский synthesis | Handoff to `[Thinkers OS]`, not `[Thinking]` or `[AI OS]`. |

## Pass condition

- Raw or unclear input routes to `[Inbox Router]` first.
- Things outputs use the Things schema.
- Project work uses the handoff schema.
- Router does not deeply solve, calculate, implement, or create production workflows.
