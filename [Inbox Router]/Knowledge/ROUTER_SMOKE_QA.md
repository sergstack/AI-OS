# Router Smoke QA

Smoke QA pass criteria:

- Router does not solve the task.
- Router chooses a destination.
- Router asks clarification only when destination is unclear.
- Router gives one next step.
- Router uses handoff when target project work is required.

| # | Raw input | Expected classification | Expected destination | Expected next action or handoff | Pass criteria |
|---:|---|---|---|---|---|
| 1 | Позвонить врачу | action | Things | Create task: call doctor. | Concrete action, no extra questions unless doctor/context is missing. |
| 2 | Надо заняться здоровьем | project | User | Ask whether this means appointment, habit, research, or plan. | Clarifies because route is unclear. |
| 3 | Встреча с бухгалтером в пятницу | calendar event | Calendar | Create or clarify calendar event details. | Routes to Calendar and asks only missing time/location if needed. |
| 4 | Хочу разобраться с AI agents | AI concept / AI pattern | `[AI OS]` | Handoff for concept, use cases, evidence, and governance. | Does not explain agents in Router. |
| 5 | Сделать prompt для аналитической записки | prompt / LLM workflow | `[LLM]` | Handoff for prompt design. | Routes prompt work to `[LLM]`. |
| 6 | Посчитать variance по выручке | data / calculation | `[Analytics]` | Handoff for deterministic variance analysis. | Does not calculate in Router. |
| 7 | Починить pipeline | code / implementation | `[Codex]` | Handoff requesting repo context, files, checks, and rollback. | Routes implementation to `[Codex]`. |
| 8 | Написать Codex задачу на refactor | code / implementation | `[Codex]` | Handoff package for refactor task. | Requires allowed files, forbidden actions, tests. |
| 9 | Подумать про карьеру | decision | `[Thinking]` | Handoff for decision framing. | Does not provide career advice in Router. |
| 10 | Идея: личный дашборд энергии | context / note | Notes / Obsidian | Save idea note with title and context. | Does not turn it into a project unless user asks. |
| 11 | Жду ответ банка по справке | waiting item | Things | Create waiting-for item. | Routes to actionable follow-up tracking. |
| 12 | Проверить подписки | action | Things | Create task: review subscriptions. | Direct route, no unnecessary questions. |
| 13 | Нужно сравнить две модели LLM | prompt / LLM workflow | `[LLM]` | Handoff for model comparison/eval. | Does not invent model facts. |
| 14 | Нужно найти supported pattern в AI OS KB | AI concept / AI pattern | `[AI OS]` | Handoff for KB evidence check. | Requires evidence status from `[AI OS]`. |
| 15 | Разобрать выписку | data / calculation | `[Analytics]` | Handoff for statement parsing and reconciliation. | Does not parse or calculate in Router. |
| 16 | Сделать презентацию | project | User | Ask purpose/audience/deadline or route if context exists. | Clarifies because destination is ambiguous. |
| 17 | Настроить автоматизацию | project | User | Ask what workflow and whether manual validation exists. | Does not recommend automation before validation. |
| 18 | Проверить качество memo | decision | `[Thinking]` | Handoff for review criteria and risk check. | Routes judgment/review work to `[Thinking]`. |
| 19 | Сохранить идею для потом | someday | Notes / Obsidian | Save as someday idea note. | Does not create immediate task. |
| 20 | Удалить мусорную задачу | trash | Things | Create/update task cleanup action or mark trash. | Handles as task system cleanup. |
| 21 | Написать тесты для parser.py | code / implementation | `[Codex]` | Handoff with file, expected tests, and checks. | Routes code work to `[Codex]`. |
| 22 | Собрать метрики по retention | data / calculation | `[Analytics]` | Handoff for metric definition and source data. | Requires deterministic analysis. |
| 23 | Записать мысль про доверие к AI | context / note | Notes / Obsidian | Save note with source context. | Does not analyze unless asked. |
| 24 | Забронировать слот на демо завтра | calendar event | Calendar | Create or clarify demo calendar slot. | Routes hard time slot to Calendar. |
