# Smoke QA Results — Inbox Router

| Date | Area | Input | Expected result | Actual result | Verdict | Fix required |
|---|---|---|---|---|---|---|
| 2026-06-15 | Things | Надо разобраться с налогами | Things task with title, area, next action, no fake deadline | not_run | pending | pending_after_run |
| 2026-06-15 | AI OS | Нашёл новую AI-фичу, хочу понять, полезна ли она мне | Handoff to `[AI OS]`, not Things-only | not_run | pending | pending_after_run |
| 2026-06-15 | Thinking | Стоит ли мне покупать mini PC или Raspberry Pi для self-hosted app? | Handoff to `[Thinking]` or decision framing, not Codex | not_run | pending | pending_after_run |
| 2026-06-15 | Analytics | Нужно посчитать экономию от автоматизации отчёта | Handoff to `[Analytics]` with metrics, period, inputs | not_run | pending | pending_after_run |
| 2026-06-15 | Codex | Нужно поправить скрипт и добавить тесты | Handoff to `[Codex]` with objective, allowed files, checks, acceptance criteria | not_run | pending | pending_after_run |
| 2026-07-31 | Thinkers OS | Хочу добавить новую книгу Деминга и обновить межавторский synthesis | Handoff to `[Thinkers OS]`, not `[Thinking]` or `[AI OS]` | Routed to `[Thinkers OS]` with strong confidence and a bounded handoff; Router did not solve the source task | pass | none |
