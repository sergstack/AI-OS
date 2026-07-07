# Router Smoke QA

Reference material. Active smoke QA behavior is defined by
`SMOKE_QA_FOR_INBOX_ROUTER.md`.

Быстрая проверка считается пройденной, если:

- Router does not solve the task.
- Router chooses a destination.
- Router asks clarification only when destination is unclear.
- Router gives one next step.
- Router uses handoff when target project work is required.

| # | Raw input | Expected classification | Expected destination | Expected next action or handoff | Pass criteria |
|---:|---|---|---|---|---|
| 1 | Позвонить врачу | action | Things | Задача: Позвонить врачу. | Конкретное действие; без лишних вопросов, если врач и контекст понятны. |
| 2 | Надо заняться здоровьем | project | User | Уточнить, это запись к врачу, привычка, исследование или план. | Уточняет, потому что маршрут неясен. |
| 3 | Встреча с бухгалтером в пятницу | calendar event | Calendar | Событие: встреча с бухгалтером; уточнить время/место, если их нет. | Маршрут в Calendar; спрашивает только недостающие детали. |
| 4 | Хочу разобраться с AI agents | AI concept / AI pattern | `[AI OS]` | Передача в AI OS для разбора концепта, use cases, evidence и governance. | Не объясняет agents внутри Router. |
| 5 | Сделать prompt для аналитической записки | prompt / LLM workflow | `[LLM]` | Передача в LLM для prompt design. | Направляет prompt work в `[LLM]`. |
| 6 | Посчитать variance по выручке | data / calculation | `[Analytics]` | Передача в Analytics для расчета variance по данным. | Не считает внутри Router. |
| 7 | Починить pipeline | code / implementation | `[Codex]` | Передача в Codex с repo context, files to inspect, checks and rollback. | Направляет implementation в `[Codex]`. |
| 8 | Написать Codex задачу на refactor | code / implementation | `[Codex]` | Пакет передачи в Codex для refactor task. | Для strict task указывает allowed files, forbidden actions и tests; для broad goal использует Goal Mode. |
| 9 | Подумать про карьеру | decision | `[Thinking]` | Передача в Thinking для рамки решения. | Не дает карьерный совет внутри Router. |
| 10 | Идея: личный дашборд энергии | context / note | Notes / Obsidian | Заметка: сохранить идею с названием и контекстом. | Не превращает в проект без запроса пользователя. |
| 11 | Жду ответ банка по справке | waiting item | Things | Ожидание: Жду банк — справку — дата запроса. | Направляет в отслеживаемое ожидание. |
| 12 | Проверить подписки | action | Things | Задача: Проверить активные подписки. | Прямой маршрут, без лишних вопросов. |
| 13 | Нужно сравнить две модели LLM | prompt / LLM workflow | `[LLM]` | Передача в LLM для model comparison / eval. | Не придумывает факты о моделях. |
| 14 | Нужно найти supported pattern в AI OS KB | AI concept / AI pattern | `[AI OS]` | Передача в AI OS для KB evidence check. | Требует evidence status из `[AI OS]`. |
| 15 | Разобрать выписку | data / calculation | `[Analytics]` | Передача в Analytics для parsing и reconciliation выписки. | Не парсит и не считает внутри Router. |
| 16 | Сделать презентацию | project | User | Уточнить цель, аудиторию и срок или направить по контексту. | Уточняет, потому что destination неоднозначен. |
| 17 | Настроить автоматизацию | project | User | Уточнить workflow и есть ли manual validation. | Не рекомендует automation до проверки ручного процесса. |
| 18 | Проверить качество memo | decision | `[Thinking]` | Передача в Thinking для критериев review и risk check. | Направляет judgment / review work в `[Thinking]`. |
| 19 | Сохранить идею для потом | someday | Notes / Obsidian | Заметка: сохранить как someday idea. | Не создает немедленную задачу. |
| 20 | Удалить мусорную задачу | trash | Things | Задача: очистить или пометить trash в Things. | Обрабатывает как cleanup в task system. |
| 21 | Написать тесты для parser.py | code / implementation | `[Codex]` | Передача в Codex с файлом, expected tests и checks. | Направляет code work в `[Codex]`. |
| 22 | Собрать метрики по retention | data / calculation | `[Analytics]` | Передача в Analytics для metric definition и source data. | Требует deterministic analysis. |
| 23 | Записать мысль про доверие к AI | context / note | Notes / Obsidian | Заметка: сохранить мысль с исходным контекстом. | Не анализирует, если пользователь не попросил. |
| 24 | Забронировать слот на демо завтра | calendar event | Calendar | Событие: забронировать слот на демо; уточнить время, если его нет. | Направляет hard time slot в Calendar. |
