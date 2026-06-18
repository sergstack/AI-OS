# AI OS Stream Deck — русская инструкция настройки v2.6

Статус: безопасная ручная настройка.
Навигация: один профиль и вложенные папки.
Изменение v2.6: сохранены QA v2.2, Capture v2.3, Research v2.4 и Memo v2.5; обновлён только экран `ПРОГОНЫ`: дублирующиеся generic pilot-промпты заменены на staged pilot workflow Brief → Hypothesis → Test case → Run log → Result → QA → Lessons → Decision. Обновлён индекс документации. Остальные экраны и кнопки сохранены.
Имена продуктов и технические команды не переводятся: Stream Deck, ChatGPT, GitHub, Codex, Gemini, Perplexity, YouTube, Obsidian, Things, README, URL, `.env`, `python3`, `git`.

## Главное правило

Кнопка должна вставлять полный русский текст, а не внутренний код.

```text
Название кнопки: Анализ
Действие: System → Text
Текст: полный русский запрос
```

## Правила безопасности

- Внутри каждой папки K1 — `⬆ НАЗАД`.
- Текстовые кнопки только вставляют текст. Автоматическую отправку выключить.
- Команды терминала вставляются текстом и запускаются вручную.
- Не добавлять удаление, отправку, слияние, публикацию или другие разрушительные действия.
- Для AI OS сначала routing/evidence, затем reasoning и next step.

## Координаты

```text
K1  K2  K3  K4  K5
K6  K7  K8  K9  K10
K11 K12 K13 K14 K15
```

# Экраны и кнопки

## Экран: `ДОМ`

```text
┌────────────┬────────────┬────────────┬────────────┬────────────┐
│ 🧭 МАРШРУТ  │ 🧠 AI OS    │ ♟ РЕШЕНИЯ  │ 📊 АНАЛИЗ   │ ✍ ЗАПРОСЫ  │
├────────────┼────────────┼────────────┼────────────┼────────────┤
│ 🛠 CODEX    │ ⚖ ПРОВЕРКА │ 📥 ВХОД     │ 📝 ЗАПИСКА  │ 🔎 ПОИСК    │
├────────────┼────────────┼────────────┼────────────┼────────────┤
│ 🗂 РЕПО     │ 🚦 ПРОГОНЫ  │ 📚 БАЗА     │ ⚙ СИСТЕМА  │ ⛔ СТОП     │
└────────────┴────────────┴────────────┴────────────┴────────────┘
```

### K1 — `🧭 МАРШРУТ`

- **Действие:** `Folder`

- **Заметка:** Главный маршрутизатор задач

- **Создать папку с таким названием.**

### K2 — `🧠 AI OS`

- **Действие:** `Folder`

- **Заметка:** AI-concepts, evidence, use cases

- **Создать папку с таким названием.**

### K3 — `♟ РЕШЕНИЯ`

- **Действие:** `Folder`

- **Заметка:** Решения, сценарии, риски

- **Создать папку с таким названием.**

### K4 — `📊 АНАЛИЗ`

- **Действие:** `Folder`

- **Заметка:** Метрики, dashboard, данные

- **Создать папку с таким названием.**

### K5 — `✍ ЗАПРОСЫ`

- **Действие:** `Folder`

- **Заметка:** Prompts, model routing, eval

- **Создать папку с таким названием.**

### K6 — `🛠 CODEX`

- **Действие:** `Folder`

- **Заметка:** Codex task package factory

- **Создать папку с таким названием.**

### K7 — `⚖ ПРОВЕРКА`

- **Действие:** `Folder`

- **Заметка:** Judge, evidence, quality gates

- **Создать папку с таким названием.**

### K8 — `📥 ВХОД`

- **Действие:** `Folder`

- **Заметка:** Быстрый захват

- **Создать папку с таким названием.**

### K9 — `📝 ЗАПИСКА`

- **Действие:** `Folder`

- **Заметка:** Фабрика записок

- **Создать папку с таким названием.**

### K10 — `🔎 ПОИСК`

- **Действие:** `Folder`

- **Заметка:** Источник, hype filter

- **Создать папку с таким названием.**

### K11 — `🗂 РЕПО`

- **Действие:** `Folder`

- **Заметка:** GitHub/validation

- **Создать папку с таким названием.**

### K12 — `🚦 ПРОГОНЫ`

- **Действие:** `Folder`

- **Заметка:** Pilot cases

- **Создать папку с таким названием.**

### K13 — `📚 БАЗА`

- **Действие:** `Folder`

- **Заметка:** Knowledge base

- **Создать папку с таким названием.**

### K14 — `⚙ СИСТЕМА`

- **Действие:** `Folder`

- **Заметка:** Системные утилиты

- **Создать папку с таким названием.**

### K15 — `⛔ СТОП`

- **Действие:** `Multi Action`

- **Заметка:** Не удалять, не закрывать критичные приложения

- **Настроить вручную:**

```text
Esc → switch/open AI OS HOME
```

- **Не добавлять разрушительные действия.**

## Экран: `МАРШРУТ`

```text
┌────────────┬────────────┬────────────┬────────────┬────────────┐
│ ⬆ НАЗАД    │ Raw→Route  │ Things?    │ Calendar?  │ Notes?     │
├────────────┼────────────┼────────────┼────────────┼────────────┤
│ AI OS?     │ Thinking?  │ Analytics? │ LLM?       │ Codex?     │
├────────────┼────────────┼────────────┼────────────┼────────────┤
│ Codex APP? │ Handoff    │ Clarify    │ QA route   │ Open proj  │
└────────────┴────────────┴────────────┴────────────┴────────────┘
```

### K1 — `⬆ НАЗАД`

- **Действие:** `штатный возврат из папки`

- **Заметка:** Не перепрограммировать

- **Оставить штатную кнопку возврата из папки.**

### K2 — `Raw → Route`

- **Действие:** `System → Text`

- **Заметка:** Главный triage: route first, solve never

- **Вставить в поле текста:**

```text
# ROUTER — RAW → ROUTE

Исходный запрос:
[вставить]

Задача:
Работай как [Inbox Router]. Не решай целевую задачу. Нужно только классифицировать вход, выбрать маршрут, назвать риски и подготовить следующий шаг / handoff.

Фокус кнопки:
Общий вход без предварительной классификации. Найди лучший destination и один безопасный следующий шаг.

Сначала определи лучший маршрут, не подгоняй под название кнопки.

Правила маршрутизации:
- Things — конкретное физическое или цифровое действие.
- Calendar — встреча, дедлайн или жёсткий слот времени.
- Notes / Obsidian — контекст, идея, reference material, длинная заметка.
- [AI OS] — AI concept, AI use case, AI pattern, evidence, governance.
- [Thinking] — решение, стратегия, варианты, сценарии, риски.
- [Analytics] — данные, метрики, расчёты, сверки, dashboards, marts.
- [LLM] — prompt, GPT instructions, workflow, model routing, eval.
- [Codex] — код, implementation, tests, refactor, automation task package.
- Codex APP — сверхдолгая работа Codex / ultra-long run package.
- User — если без уточнения есть высокий риск неверного маршрута.


Проверка перед ответом:
- не решай задачу внутри Router;
- не отправляй не-actionable контекст в Things;
- не отправляй расчёты в [AI OS];
- не отправляй код в [Thinking];
- не отправляй в [Codex] без constraints, acceptance criteria и rollback;
- если маршрут unclear, задай максимум 1–3 вопроса.

Верни строго:

## Решение по маршруту
Куда:
Почему:
Уверенность: strong / medium / weak
Статус: direct / clarify / handoff / park / trash

## Классификация
Тип:
Можно действовать сейчас: да / нет
Нужно уточнение: да / нет

## Факты / допущения / пробелы
Факты:
Допущения:
Чего не хватает:
Риски:

## Следующее действие
Задача:
Area / Project:
Tag:
Готово, когда:

## Передача в проект
From:
To:
Task type:
Objective:
Context:
Inputs:
Constraints:
Expected output:
Acceptance criteria:
Risks:
Open questions:
Suggested first step:
```

### K3 — `Things?`

- **Действие:** `System → Text`

- **Заметка:** Проверка: можно ли сделать task в Things

- **Вставить в поле текста:**

```text
# ROUTER — THINGS GATE

Исходный запрос:
[вставить]

Задача:
Работай как [Inbox Router]. Не решай целевую задачу. Нужно только классифицировать вход, выбрать маршрут, назвать риски и подготовить следующий шаг / handoff.

Фокус кнопки:
Проверь, является ли вход конкретным действием для Things.

Предпочтительный маршрут для проверки: Things.

Правила маршрутизации:
- Things — конкретное физическое или цифровое действие.
- Calendar — встреча, дедлайн или жёсткий слот времени.
- Notes / Obsidian — контекст, идея, reference material, длинная заметка.
- [AI OS] — AI concept, AI use case, AI pattern, evidence, governance.
- [Thinking] — решение, стратегия, варианты, сценарии, риски.
- [Analytics] — данные, метрики, расчёты, сверки, dashboards, marts.
- [LLM] — prompt, GPT instructions, workflow, model routing, eval.
- [Codex] — код, implementation, tests, refactor, automation task package.
- Codex APP — сверхдолгая работа Codex / ultra-long run package.
- User — если без уточнения есть высокий риск неверного маршрута.
Things gate:
1. Есть ли глагол действия?
2. Понятно ли, где / в каком инструменте делать?
3. Понятно ли, когда задача готова?
Если хотя бы один ответ «нет» — не отправляй в Things, предложи уточнение или Notes / Obsidian.

Проверка перед ответом:
- не решай задачу внутри Router;
- не отправляй не-actionable контекст в Things;
- не отправляй расчёты в [AI OS];
- не отправляй код в [Thinking];
- не отправляй в [Codex] без constraints, acceptance criteria и rollback;
- если маршрут unclear, задай максимум 1–3 вопроса.

Верни строго:

## Решение по маршруту
Куда:
Почему:
Уверенность: strong / medium / weak
Статус: direct / clarify / handoff / park / trash

## Классификация
Тип:
Можно действовать сейчас: да / нет
Нужно уточнение: да / нет

## Факты / допущения / пробелы
Факты:
Допущения:
Чего не хватает:
Риски:

## Следующее действие
Задача:
Area / Project:
Tag:
Готово, когда:

## Передача в проект
From:
To:
Task type:
Objective:
Context:
Inputs:
Constraints:
Expected output:
Acceptance criteria:
Risks:
Open questions:
Suggested first step:
```

### K4 — `Calendar?`

- **Действие:** `System → Text`

- **Заметка:** Проверка: календарь или задача

- **Вставить в поле текста:**

```text
# ROUTER — CALENDAR GATE

Исходный запрос:
[вставить]

Задача:
Работай как [Inbox Router]. Не решай целевую задачу. Нужно только классифицировать вход, выбрать маршрут, назвать риски и подготовить следующий шаг / handoff.

Фокус кнопки:
Проверь, является ли вход событием, дедлайном или жёстким временным слотом.

Предпочтительный маршрут для проверки: Calendar.

Правила маршрутизации:
- Things — конкретное физическое или цифровое действие.
- Calendar — встреча, дедлайн или жёсткий слот времени.
- Notes / Obsidian — контекст, идея, reference material, длинная заметка.
- [AI OS] — AI concept, AI use case, AI pattern, evidence, governance.
- [Thinking] — решение, стратегия, варианты, сценарии, риски.
- [Analytics] — данные, метрики, расчёты, сверки, dashboards, marts.
- [LLM] — prompt, GPT instructions, workflow, model routing, eval.
- [Codex] — код, implementation, tests, refactor, automation task package.
- Codex APP — сверхдолгая работа Codex / ultra-long run package.
- User — если без уточнения есть высокий риск неверного маршрута.
Calendar gate:
- Есть дата YYYY-MM-DD или её можно надёжно вывести?
- Есть время / дедлайн / событие?
- Нужен ли участник, место, длительность?
Если времени нет, но есть действие — вероятно Things, не Calendar.

Проверка перед ответом:
- не решай задачу внутри Router;
- не отправляй не-actionable контекст в Things;
- не отправляй расчёты в [AI OS];
- не отправляй код в [Thinking];
- не отправляй в [Codex] без constraints, acceptance criteria и rollback;
- если маршрут unclear, задай максимум 1–3 вопроса.

Верни строго:

## Решение по маршруту
Куда:
Почему:
Уверенность: strong / medium / weak
Статус: direct / clarify / handoff / park / trash

## Классификация
Тип:
Можно действовать сейчас: да / нет
Нужно уточнение: да / нет

## Факты / допущения / пробелы
Факты:
Допущения:
Чего не хватает:
Риски:

## Следующее действие
Задача:
Area / Project:
Tag:
Готово, когда:

## Передача в проект
From:
To:
Task type:
Objective:
Context:
Inputs:
Constraints:
Expected output:
Acceptance criteria:
Risks:
Open questions:
Suggested first step:
```

### K5 — `Notes?`

- **Действие:** `System → Text`

- **Заметка:** Проверка: контекст не превращать в задачу

- **Вставить в поле текста:**

```text
# ROUTER — NOTES / OBSIDIAN GATE

Исходный запрос:
[вставить]

Задача:
Работай как [Inbox Router]. Не решай целевую задачу. Нужно только классифицировать вход, выбрать маршрут, назвать риски и подготовить следующий шаг / handoff.

Фокус кнопки:
Проверь, является ли вход контекстом, идеей, reference material или длинной заметкой.

Предпочтительный маршрут для проверки: Notes / Obsidian.

Правила маршрутизации:
- Things — конкретное физическое или цифровое действие.
- Calendar — встреча, дедлайн или жёсткий слот времени.
- Notes / Obsidian — контекст, идея, reference material, длинная заметка.
- [AI OS] — AI concept, AI use case, AI pattern, evidence, governance.
- [Thinking] — решение, стратегия, варианты, сценарии, риски.
- [Analytics] — данные, метрики, расчёты, сверки, dashboards, marts.
- [LLM] — prompt, GPT instructions, workflow, model routing, eval.
- [Codex] — код, implementation, tests, refactor, automation task package.
- Codex APP — сверхдолгая работа Codex / ultra-long run package.
- User — если без уточнения есть высокий риск неверного маршрута.
Notes gate:
- Это знание, контекст, идея или материал без немедленного действия?
- Есть ли смысл сохранить как reference?
- Если есть конкретный следующий шаг — выдели его отдельно для Things.

Проверка перед ответом:
- не решай задачу внутри Router;
- не отправляй не-actionable контекст в Things;
- не отправляй расчёты в [AI OS];
- не отправляй код в [Thinking];
- не отправляй в [Codex] без constraints, acceptance criteria и rollback;
- если маршрут unclear, задай максимум 1–3 вопроса.

Верни строго:

## Решение по маршруту
Куда:
Почему:
Уверенность: strong / medium / weak
Статус: direct / clarify / handoff / park / trash

## Классификация
Тип:
Можно действовать сейчас: да / нет
Нужно уточнение: да / нет

## Факты / допущения / пробелы
Факты:
Допущения:
Чего не хватает:
Риски:

## Следующее действие
Задача:
Area / Project:
Tag:
Готово, когда:

## Передача в проект
From:
To:
Task type:
Objective:
Context:
Inputs:
Constraints:
Expected output:
Acceptance criteria:
Risks:
Open questions:
Suggested first step:
```

### K6 — `AI OS?`

- **Действие:** `System → Text`

- **Заметка:** AI concept / evidence / governance

- **Вставить в поле текста:**

```text
# ROUTER — AI OS GATE

Исходный запрос:
[вставить]

Задача:
Работай как [Inbox Router]. Не решай целевую задачу. Нужно только классифицировать вход, выбрать маршрут, назвать риски и подготовить следующий шаг / handoff.

Фокус кнопки:
Проверь, относится ли вход к AI concepts, AI use cases, AI patterns, evidence или governance.

Предпочтительный маршрут для проверки: [AI OS].

Правила маршрутизации:
- Things — конкретное физическое или цифровое действие.
- Calendar — встреча, дедлайн или жёсткий слот времени.
- Notes / Obsidian — контекст, идея, reference material, длинная заметка.
- [AI OS] — AI concept, AI use case, AI pattern, evidence, governance.
- [Thinking] — решение, стратегия, варианты, сценарии, риски.
- [Analytics] — данные, метрики, расчёты, сверки, dashboards, marts.
- [LLM] — prompt, GPT instructions, workflow, model routing, eval.
- [Codex] — код, implementation, tests, refactor, automation task package.
- Codex APP — сверхдолгая работа Codex / ultra-long run package.
- User — если без уточнения есть высокий риск неверного маршрута.
AI OS gate:
- Не делай расчёты.
- Не проектируй prompts вместо [LLM].
- Не пиши код вместо [Codex].
- Требуй evidence / KB / governance check, если идея будет использоваться дальше.

Проверка перед ответом:
- не решай задачу внутри Router;
- не отправляй не-actionable контекст в Things;
- не отправляй расчёты в [AI OS];
- не отправляй код в [Thinking];
- не отправляй в [Codex] без constraints, acceptance criteria и rollback;
- если маршрут unclear, задай максимум 1–3 вопроса.

Верни строго:

## Решение по маршруту
Куда:
Почему:
Уверенность: strong / medium / weak
Статус: direct / clarify / handoff / park / trash

## Классификация
Тип:
Можно действовать сейчас: да / нет
Нужно уточнение: да / нет

## Факты / допущения / пробелы
Факты:
Допущения:
Чего не хватает:
Риски:

## Следующее действие
Задача:
Area / Project:
Tag:
Готово, когда:

## Передача в проект
From:
To:
Task type:
Objective:
Context:
Inputs:
Constraints:
Expected output:
Acceptance criteria:
Risks:
Open questions:
Suggested first step:
```

### K7 — `Thinking?`

- **Действие:** `System → Text`

- **Заметка:** Decision / strategy / risk

- **Вставить в поле текста:**

```text
# ROUTER — THINKING GATE

Исходный запрос:
[вставить]

Задача:
Работай как [Inbox Router]. Не решай целевую задачу. Нужно только классифицировать вход, выбрать маршрут, назвать риски и подготовить следующий шаг / handoff.

Фокус кнопки:
Проверь, является ли вход решением, стратегией, выбором вариантов, сценарием или risk review.

Предпочтительный маршрут для проверки: [Thinking].

Правила маршрутизации:
- Things — конкретное физическое или цифровое действие.
- Calendar — встреча, дедлайн или жёсткий слот времени.
- Notes / Obsidian — контекст, идея, reference material, длинная заметка.
- [AI OS] — AI concept, AI use case, AI pattern, evidence, governance.
- [Thinking] — решение, стратегия, варианты, сценарии, риски.
- [Analytics] — данные, метрики, расчёты, сверки, dashboards, marts.
- [LLM] — prompt, GPT instructions, workflow, model routing, eval.
- [Codex] — код, implementation, tests, refactor, automation task package.
- Codex APP — сверхдолгая работа Codex / ultra-long run package.
- User — если без уточнения есть высокий риск неверного маршрута.
Thinking gate:
- Если нужны числа, расчёты или проверка данных — handoff в [Analytics].
- Если нужно писать prompt/workflow — handoff в [LLM].
- Если нужно реализовать код — handoff в [Codex] только после принятого решения.

Проверка перед ответом:
- не решай задачу внутри Router;
- не отправляй не-actionable контекст в Things;
- не отправляй расчёты в [AI OS];
- не отправляй код в [Thinking];
- не отправляй в [Codex] без constraints, acceptance criteria и rollback;
- если маршрут unclear, задай максимум 1–3 вопроса.

Верни строго:

## Решение по маршруту
Куда:
Почему:
Уверенность: strong / medium / weak
Статус: direct / clarify / handoff / park / trash

## Классификация
Тип:
Можно действовать сейчас: да / нет
Нужно уточнение: да / нет

## Факты / допущения / пробелы
Факты:
Допущения:
Чего не хватает:
Риски:

## Следующее действие
Задача:
Area / Project:
Tag:
Готово, когда:

## Передача в проект
From:
To:
Task type:
Objective:
Context:
Inputs:
Constraints:
Expected output:
Acceptance criteria:
Risks:
Open questions:
Suggested first step:
```

### K8 — `Analytics?`

- **Действие:** `System → Text`

- **Заметка:** Data / metrics / calculations

- **Вставить в поле текста:**

```text
# ROUTER — ANALYTICS GATE

Исходный запрос:
[вставить]

Задача:
Работай как [Inbox Router]. Не решай целевую задачу. Нужно только классифицировать вход, выбрать маршрут, назвать риски и подготовить следующий шаг / handoff.

Фокус кнопки:
Проверь, относится ли вход к данным, метрикам, расчётам, сверкам, dashboard, marts или data quality.

Предпочтительный маршрут для проверки: [Analytics].

Правила маршрутизации:
- Things — конкретное физическое или цифровое действие.
- Calendar — встреча, дедлайн или жёсткий слот времени.
- Notes / Obsidian — контекст, идея, reference material, длинная заметка.
- [AI OS] — AI concept, AI use case, AI pattern, evidence, governance.
- [Thinking] — решение, стратегия, варианты, сценарии, риски.
- [Analytics] — данные, метрики, расчёты, сверки, dashboards, marts.
- [LLM] — prompt, GPT instructions, workflow, model routing, eval.
- [Codex] — код, implementation, tests, refactor, automation task package.
- Codex APP — сверхдолгая работа Codex / ultra-long run package.
- User — если без уточнения есть высокий риск неверного маршрута.
Analytics gate:
- Зафиксируй period, grain, metric, source, currency / units, если они известны.
- Не делай вывод сильнее данных.
- Если нужна реализация pipeline — сначала analytics spec, потом handoff в [Codex].

Проверка перед ответом:
- не решай задачу внутри Router;
- не отправляй не-actionable контекст в Things;
- не отправляй расчёты в [AI OS];
- не отправляй код в [Thinking];
- не отправляй в [Codex] без constraints, acceptance criteria и rollback;
- если маршрут unclear, задай максимум 1–3 вопроса.

Верни строго:

## Решение по маршруту
Куда:
Почему:
Уверенность: strong / medium / weak
Статус: direct / clarify / handoff / park / trash

## Классификация
Тип:
Можно действовать сейчас: да / нет
Нужно уточнение: да / нет

## Факты / допущения / пробелы
Факты:
Допущения:
Чего не хватает:
Риски:

## Следующее действие
Задача:
Area / Project:
Tag:
Готово, когда:

## Передача в проект
From:
To:
Task type:
Objective:
Context:
Inputs:
Constraints:
Expected output:
Acceptance criteria:
Risks:
Open questions:
Suggested first step:
```

### K9 — `LLM?`

- **Действие:** `System → Text`

- **Заметка:** Prompt / workflow / model routing

- **Вставить в поле текста:**

```text
# ROUTER — LLM GATE

Исходный запрос:
[вставить]

Задача:
Работай как [Inbox Router]. Не решай целевую задачу. Нужно только классифицировать вход, выбрать маршрут, назвать риски и подготовить следующий шаг / handoff.

Фокус кнопки:
Проверь, относится ли вход к prompt, GPT instructions, context package, workflow, model routing или eval.

Предпочтительный маршрут для проверки: [LLM].

Правила маршрутизации:
- Things — конкретное физическое или цифровое действие.
- Calendar — встреча, дедлайн или жёсткий слот времени.
- Notes / Obsidian — контекст, идея, reference material, длинная заметка.
- [AI OS] — AI concept, AI use case, AI pattern, evidence, governance.
- [Thinking] — решение, стратегия, варианты, сценарии, риски.
- [Analytics] — данные, метрики, расчёты, сверки, dashboards, marts.
- [LLM] — prompt, GPT instructions, workflow, model routing, eval.
- [Codex] — код, implementation, tests, refactor, automation task package.
- Codex APP — сверхдолгая работа Codex / ultra-long run package.
- User — если без уточнения есть высокий риск неверного маршрута.
LLM gate:
- Не передавай raw dump как context package.
- Не hardcode конкретную модель как постоянную истину.
- Для цен, лимитов, API, release status нужен fresh check.

Проверка перед ответом:
- не решай задачу внутри Router;
- не отправляй не-actionable контекст в Things;
- не отправляй расчёты в [AI OS];
- не отправляй код в [Thinking];
- не отправляй в [Codex] без constraints, acceptance criteria и rollback;
- если маршрут unclear, задай максимум 1–3 вопроса.

Верни строго:

## Решение по маршруту
Куда:
Почему:
Уверенность: strong / medium / weak
Статус: direct / clarify / handoff / park / trash

## Классификация
Тип:
Можно действовать сейчас: да / нет
Нужно уточнение: да / нет

## Факты / допущения / пробелы
Факты:
Допущения:
Чего не хватает:
Риски:

## Следующее действие
Задача:
Area / Project:
Tag:
Готово, когда:

## Передача в проект
From:
To:
Task type:
Objective:
Context:
Inputs:
Constraints:
Expected output:
Acceptance criteria:
Risks:
Open questions:
Suggested first step:
```

### K10 — `Codex?`

- **Действие:** `System → Text`

- **Заметка:** Code / repo / tests / automation

- **Вставить в поле текста:**

```text
# ROUTER — CODEX GATE

Исходный запрос:
[вставить]

Задача:
Работай как [Inbox Router]. Не решай целевую задачу. Нужно только классифицировать вход, выбрать маршрут, назвать риски и подготовить следующий шаг / handoff.

Фокус кнопки:
Проверь, является ли вход задачей на код, tests, refactor, repo changes или automation task package.

Предпочтительный маршрут для проверки: [Codex].

Правила маршрутизации:
- Things — конкретное физическое или цифровое действие.
- Calendar — встреча, дедлайн или жёсткий слот времени.
- Notes / Obsidian — контекст, идея, reference material, длинная заметка.
- [AI OS] — AI concept, AI use case, AI pattern, evidence, governance.
- [Thinking] — решение, стратегия, варианты, сценарии, риски.
- [Analytics] — данные, метрики, расчёты, сверки, dashboards, marts.
- [LLM] — prompt, GPT instructions, workflow, model routing, eval.
- [Codex] — код, implementation, tests, refactor, automation task package.
- Codex APP — сверхдолгая работа Codex / ultra-long run package.
- User — если без уточнения есть высокий риск неверного маршрута.
Codex gate:
- Нужны repo, files to inspect, files to change, forbidden actions, checks, acceptance criteria, rollback.
- Не отправляй в Codex, если решение ещё не принято или аналитическая логика не определена.
- Не разрешай merge / push / destructive actions без явного gate.

Проверка перед ответом:
- не решай задачу внутри Router;
- не отправляй не-actionable контекст в Things;
- не отправляй расчёты в [AI OS];
- не отправляй код в [Thinking];
- не отправляй в [Codex] без constraints, acceptance criteria и rollback;
- если маршрут unclear, задай максимум 1–3 вопроса.

Верни строго:

## Решение по маршруту
Куда:
Почему:
Уверенность: strong / medium / weak
Статус: direct / clarify / handoff / park / trash

## Классификация
Тип:
Можно действовать сейчас: да / нет
Нужно уточнение: да / нет

## Факты / допущения / пробелы
Факты:
Допущения:
Чего не хватает:
Риски:

## Следующее действие
Задача:
Area / Project:
Tag:
Готово, когда:

## Передача в проект
From:
To:
Task type:
Objective:
Context:
Inputs:
Constraints:
Expected output:
Acceptance criteria:
Risks:
Open questions:
Suggested first step:
```

### K11 — `Codex APP?`

- **Действие:** `System → Text`

- **Заметка:** Ultra-long Codex routing

- **Вставить в поле текста:**

```text
# ROUTER — CODEX APP / ULTRA-LONG GATE

Исходный запрос:
[вставить]

Задача:
Работай как [Inbox Router]. Не решай целевую задачу. Нужно только классифицировать вход, выбрать маршрут, назвать риски и подготовить следующий шаг / handoff.

Фокус кнопки:
Проверь, нужна ли сверхдолгая работа Codex: много файлов, PR, checks, staged batches, long local execution.

Предпочтительный маршрут для проверки: Codex APP.

Правила маршрутизации:
- Things — конкретное физическое или цифровое действие.
- Calendar — встреча, дедлайн или жёсткий слот времени.
- Notes / Obsidian — контекст, идея, reference material, длинная заметка.
- [AI OS] — AI concept, AI use case, AI pattern, evidence, governance.
- [Thinking] — решение, стратегия, варианты, сценарии, риски.
- [Analytics] — данные, метрики, расчёты, сверки, dashboards, marts.
- [LLM] — prompt, GPT instructions, workflow, model routing, eval.
- [Codex] — код, implementation, tests, refactor, automation task package.
- Codex APP — сверхдолгая работа Codex / ultra-long run package.
- User — если без уточнения есть высокий риск неверного маршрута.
Codex APP gate:
- Использовать для ultra-long-local / long repo task package.
- Требуются batches, allowed scope, forbidden actions, checks, final report contract.
- Если задача маленькая — обычный [Codex], не Codex APP.

Проверка перед ответом:
- не решай задачу внутри Router;
- не отправляй не-actionable контекст в Things;
- не отправляй расчёты в [AI OS];
- не отправляй код в [Thinking];
- не отправляй в [Codex] без constraints, acceptance criteria и rollback;
- если маршрут unclear, задай максимум 1–3 вопроса.

Верни строго:

## Решение по маршруту
Куда:
Почему:
Уверенность: strong / medium / weak
Статус: direct / clarify / handoff / park / trash

## Классификация
Тип:
Можно действовать сейчас: да / нет
Нужно уточнение: да / нет

## Факты / допущения / пробелы
Факты:
Допущения:
Чего не хватает:
Риски:

## Следующее действие
Задача:
Area / Project:
Tag:
Готово, когда:

## Передача в проект
From:
To:
Task type:
Objective:
Context:
Inputs:
Constraints:
Expected output:
Acceptance criteria:
Risks:
Open questions:
Suggested first step:
```

### K12 — `Handoff`

- **Действие:** `System → Text`

- **Заметка:** Строгий handoff вместо пустого бланка

- **Вставить в поле текста:**

```text
# ROUTER — PROJECT HANDOFF PACKAGE

Исходный запрос:
[вставить]

Задача:
Подготовь пакет передачи из [Inbox Router] в целевой проект. Не решай задачу. Не добавляй неподтверждённые факты. Если destination неясен — сначала укажи clarify и максимум 1–3 вопроса.

Destination rules:
- [AI OS] — AI concept / evidence / governance.
- [Thinking] — decision / options / risks.
- [Analytics] — data / metrics / calculations / reconciliation / dashboards.
- [LLM] — prompts / workflows / model routing / eval.
- [Codex] — code / tests / repo changes / automation.
- Codex APP — ultra-long Codex run.

Верни строго:
Destination:
Task type:
Objective:
Context:
Inputs:
Constraints:
Expected output:
Acceptance criteria:
Risks:
Evidence / confidence:
Open questions:
Suggested first step:

Если Destination = [Codex] или Codex APP, дополнительно:
Repository:
Files to inspect:
Files allowed to change:
Forbidden actions:
Checks / smoke tests:
Rollback / stop condition:
```

### K13 — `Clarify`

- **Действие:** `System → Text`

- **Заметка:** Когда без уточнения нельзя

- **Вставить в поле текста:**

```text
# ROUTER — CLARIFICATION REQUIRED

Исходный запрос:
[вставить]

Задача:
Определи, почему маршрут нельзя выбрать безопасно. Не задавай широкое интервью. Сформулируй максимум 1–3 критических вопроса, без которых высок риск неправильного routing.

Верни строго:
Предварительный маршрут:
Почему не хватает данных:
Риск неверного маршрута:
Критические вопросы: максимум 3
Что можно сделать без уточнения:
Что заблокировано до ответа:
Следующий шаг:
```

### K14 — `QA route`

- **Действие:** `System → Text`

- **Заметка:** Быстрая проверка маршрута

- **Вставить в поле текста:**

```text
# ROUTER — ROUTE QA / JUDGE

Маршрут или handoff для проверки:
[вставить]

Задача:
Проверь как @judge, корректен ли routing. Router не должен решать целевую задачу.

Проверь:
- destination explicit;
- confidence honest;
- facts / assumptions / risks separated;
- missing data visible;
- one next step provided;
- handoff used for project work;
- no calculations routed to [AI OS];
- no code routed to [Thinking];
- no vague context routed to Things;
- no Codex without constraints / acceptance / rollback.

Верни строго:
QA verdict: pass / revise / blocked
Wrong routing:
Missing constraints:
Unsupported assumptions:
Main risk:
Required fix:
Corrected route:
Approved next step:
```

### K15 — `Open project`

- **Действие:** `System → Text`

- **Заметка:** Второй шаг после handoff, не первый

- **Вставить в поле текста:**

```text
# ROUTER — OPEN TARGET PROJECT

Принятый маршрут:
[вставить destination]

Действие:
Открой соответствующий ChatGPT Project вручную и вставь подготовленный handoff.

Карта открытия:
- [AI OS] → <CHATGPT_AI_OS_PROJECT_URL>
- [Thinking] → <CHATGPT_THINKING_PROJECT_URL>
- [Analytics] → <CHATGPT_ANALYTICS_PROJECT_URL>
- [LLM] → <CHATGPT_LLM_PROJECT_URL>
- [Codex] → <CHATGPT_CODEX_PROJECT_URL>
- Codex APP → <CHATGPT_CODEX_APP_PROJECT_URL>

Не открывай проект до route QA, если confidence = weak или status = clarify / blocked.
```

## Экран: `AI OS`

```text
┌────────────┬────────────┬────────────┬────────────┬────────────┐
│ ⬆ НАЗАД    │ Анализ     │ Применить  │ Подтв.     │ Ловушки    │
├────────────┼────────────┼────────────┼────────────┼────────────┤
│ На проверк │ Свежесть   │ В LLM      │ В Codex    │ Правила    │
├────────────┼────────────┼────────────┼────────────┼────────────┤
│ Приём      │ Сбои       │ Статус БЗ  │ Источники  │ Практика   │
└────────────┴────────────┴────────────┴────────────┴────────────┘
```

### K1 — `⬆ НАЗАД`

- **Действие:** `штатный возврат из папки`

- **Оставить штатную кнопку возврата из папки.**

### K2 — `Анализ`

- **Действие:** `System → Text`

- **Заметка:** Grounded AI OS analysis

- **Вставить в поле текста:**

```text
# AI OS — АНАЛИЗ

Тема или идея:
[вставить]

Режим:
concept / use case / comparison / next step / routing

Задача:
Сделай grounded-разбор внутри [AI OS]. Сначала определи routing, затем проверь KB и только после этого формулируй вывод.

Проверь по порядку:
1. Есть ли релевантные KB-файлы / Gold cards.
2. Что подтверждено, слабо подтверждено, смешано, не подтверждено или не найдено.
3. Требуется ли свежая внешняя проверка: AI-релизы, модели, API, pricing, лимиты, benchmark, market facts.
4. Как это применимо к работе Сергея: аудит, аналитика, governance, AI-workflows.
5. Нужен ли handoff в [Thinking] / [Analytics] / [LLM] / [Codex].

Раздели:
- FACT:
- INTERPRETATION:
- RECOMMENDATION:
- HYPOTHESIS:
- BLOCKER:

Верни строго:
KB проверен: да / нет
Источники: [...]
Найдено в KB: да / нет / частично
Fresh external check: не нужен / нужен / выполнен
Confidence: strong / medium / weak
Evidence: supported / weak / mixed / unsupported / not found

Суть:
Как это работает:
Применение для Сергея:
Риски и ограничения:
Routing:
Итог:
Next step:
```

### K3 — `Применить`

- **Действие:** `System → Text`

- **Заметка:** Use case for Sergey

- **Вставить в поле текста:**

```text
# AI OS — ПРИМЕНИТЬ К РАБОТЕ СЕРГЕЯ

Тема, AI-паттерн или инструмент:
[вставить]

Задача:
Найди практическое применение для работы Сергея внутри [AI OS]. Не делай стратегическое решение вместо [Thinking], расчёты вместо [Analytics], prompt-orchestration вместо [LLM] и код вместо [Codex].

Сначала проверь:
- что уже есть в KB;
- evidence status: supported / weak / mixed / unsupported / not found;
- какие ограничения и gates есть;
- что требует свежей проверки;
- какие use cases реально подходят финансовому аудитору / стратег-аналитику.

Собери 3–5 use cases, затем выбери топ-2 по критериям:
- польза для аудита / аналитики;
- скорость внедрения;
- риск;
- evidence strength;
- зависимость от других проектов;
- обратимость.

Верни:
KB проверен:
Источники:
Evidence:
Use cases table:
| Use case | Value for Sergey | Evidence | Risk | Owner project | First safe step |
|---|---|---|---|---|---|
Топ-2 рекомендации:
Что НЕ делать сейчас:
Review item, если evidence weak/mixed/unsupported:
Routing:
Next step:
```

### K4 — `Подтв.`

- **Действие:** `System → Text`

- **Заметка:** Evidence verdict / confirmation

- **Вставить в поле текста:**

```text
# AI OS — ПОДТВЕРЖДЕНИЕ / EVIDENCE CHECK

Утверждение, идея или рекомендация:
[вставить]

Задача:
Проверь, можно ли считать это подтверждённым внутри [AI OS]. Отвечай как evidence judge: не усиливай вывод выше источников.

Порядок проверки:
1. Найди релевантные KB-файлы / cards.
2. Проверь support_status, confidence, evidence_count, limitations, review queue.
3. Отдели KB knowledge от fresh external check.
4. Определи статус: supported / weak / mixed / unsupported / not found.
5. Если weak / mixed / unsupported / not found — оформи review item.

Раздели:
- FACT:
- INTERPRETATION:
- RECOMMENDATION:
- HYPOTHESIS:
- BLOCKER:

Верни строго:
KB проверен: да / нет
Источники:
Найдено в KB: да / нет / частично
Confidence: strong / medium / weak
Evidence: supported / weak / mixed / unsupported / not found
Verdict: подтверждено / частично / не подтверждено / не найдено
What can be safely claimed:
What must NOT be claimed:
Review item:
- claim:
- source files checked:
- evidence status:
- risk if used:
- recommended action:
- owner project:
Routing:
Next step:
```

### K5 — `Ловушки`

- **Действие:** `System → Text`

- **Заметка:** Hype / anti-pattern / risk scan

- **Вставить в поле текста:**

```text
# AI OS — ЛОВУШКИ / ANTI-PATTERN CHECK

Тема, идея, AI-инструмент или workflow:
[вставить]

Задача:
Проверь как @judge: где здесь hype, слабое evidence, неправильный routing или преждевременная автоматизация.

Ищи:
- unsupported claims;
- weak evidence, выдаваемое как fact;
- hidden assumptions;
- missing limitations;
- wrong project routing;
- premature Codex / production execution;
- blocked promotion items: embeddings, semantic search, vector DB, web UI, agentic workflows, autonomous retrieval;
- raw dumps / chunks / logs / secrets as knowledge source;
- отсутствие acceptance criteria.

Верни:
KB проверен:
Источники:
Evidence:
Main trap:
Risk level: low / medium / high
Failure modes:
| Trap | Why risky | Evidence status | Detection check | Safer alternative |
|---|---|---|---|---|
What not to claim:
What to defer:
Review item, если нужен:
Routing:
Next step:
```

### K6 — `На проверку`

- **Действие:** `System → Text`

- **Заметка:** Review queue item

- **Вставить в поле текста:**

```text
# AI OS — ЗАПИСЬ НА ПРОВЕРКУ / REVIEW ITEM

Утверждение или решение-кандидат:
[вставить]

Задача:
Оформи review item для AI OS. Используй, если evidence weak / mixed / unsupported / not found, либо если есть риск premature implementation.

Заполни строго:
- claim:
- source files checked:
- evidence status: weak / mixed / unsupported / not found
- confidence: strong / medium / weak
- risk if used:
- what can be safely said now:
- what must not be claimed:
- recommended action:
- owner project: [AI OS] / [Thinking] / [Analytics] / [LLM] / [Codex]
- acceptance condition:
- next review trigger:
- next step:
```

### K7 — `Свежесть`

- **Действие:** `System → Text`

- **Заметка:** Freshness / external check decision

- **Вставить в поле текста:**

```text
# AI OS — СВЕЖЕСТЬ / FRESHNESS CHECK

Тема, инструмент, модель, API, benchmark, pricing или правило:
[вставить]

Задача:
Определи, что можно взять из KB, а что требует свежей внешней проверки. Не отвечай устаревшими фактами как текущими.

Проверь:
- относится ли тема к текущим AI-релизам, моделям, API, pricing, лимитам, benchmark, market facts, законам, продуктовым правилам;
- есть ли в KB стабильное знание;
- какие утверждения могут измениться после даты KB;
- нужен ли web-check перед рекомендацией;
- можно ли сейчас дать только предварительный вывод.

Верни:
KB проверен:
KB knowledge:
Fresh external check: нужен / не нужен / уже выполнен
Claims requiring freshness:
| Claim | Why freshness matters | Risk if stale | Source to check |
|---|---|---|---|
Safe interim answer:
Blocked claims until fresh check:
Routing:
Next step:
```

### K8 — `В LLM`

- **Действие:** `System → Text`

- **Заметка:** AI OS → LLM handoff

- **Вставить в поле текста:**

```text
# AI OS → [LLM] HANDOFF

Тема или задача:
[вставить]

Задача:
Подготовь handoff из [AI OS] в [LLM] для prompt/workflow/model routing/context package. Не передавай raw dumps и не превращай weak evidence в facts.

Собери curated context:
- цель;
- verified facts;
- interpretations clearly marked;
- unsupported / weak claims clearly marked;
- constraints;
- risks;
- expected output;
- acceptance criteria.

Не передавать:
- raw transcripts;
- source-card dumps;
- chunks / embeddings / vector DB;
- secrets / API keys / `.env`;
- неподтверждённые claims как facts;
- production-ready claims без acceptance.

Верни строго:
Handoff to: [LLM]
Task type: prompt / workflow / model routing / context package / revisor
Goal:
Context from AI OS:
KB evidence used:
Confidence:
Inputs required:
Expected output:
Constraints:
Risks:
Acceptance criteria:
What not to claim:
Suggested first step:
```

### K9 — `В Codex`

- **Действие:** `System → Text`

- **Заметка:** AI OS → Codex gated handoff

- **Вставить в поле текста:**

```text
# AI OS → [Codex] HANDOFF / GATED

Задача или идея для реализации:
[вставить]

ВНИМАНИЕ:
Использовать только если есть accepted / recommended decision или явная задача на repository docs / tests / tooling. Если evidence weak или решение не принято — сначала вернуть в [AI OS] / [Thinking] / [LLM].

Перед handoff проверь:
- KB evidence used;
- confidence;
- decision status;
- allowed files;
- forbidden changes;
- acceptance criteria;
- checks to run;
- rollback / stop condition.

Запрещено:
- менять business logic без acceptance;
- добавлять secrets / API keys / `.env`;
- мержить автоматически;
- расширять scope;
- реализовывать blocked promotion items без gate;
- выдавать weak evidence как requirement.

Верни строго:
Handoff to: [Codex]
Task type: docs / implementation / tests / tooling / QA
Proceed gate: pass / blocked / needs [Thinking] / needs [LLM]
Goal:
Accepted context:
KB evidence used:
Confidence:
Allowed files:
Forbidden changes:
Expected output:
Checks to run:
Acceptance criteria:
Rollback / stop condition:
Risks:
Suggested first step:
```

### K10 — `Правила`

- **Действие:** `System → Website`

- **Адрес или цель:**

```text
https://github.com/sergstack/AI-OS/blob/main/ChatGPT/%5BAI%20OS%5D/Knowledge/GOVERNANCE_RULES.md
```

### K11 — `Приём`

- **Действие:** `System → Text`

- **Заметка:** Acceptance / promotion gate

- **Вставить в поле текста:**

```text
# AI OS — ПРИЁМ / ACCEPTANCE GATE

Результат, вывод, KB-update или workflow:
[вставить]

Задача:
Проверь, можно ли принять результат как рабочий для [AI OS], или его нужно доработать / заблокировать / передать в другой проект.

Проверь acceptance checklist:
- KB files checked;
- evidence listed;
- confidence label set;
- weak / unsupported claims separated;
- routing clear;
- risks named;
- limitations visible;
- next step concrete;
- no blocked promotion items recommended as current implementation;
- smoke QA не назван production readiness.

Верни:
KB проверен:
Источники:
Acceptance status: pass / revise / blocked
Evidence:
Missing items:
Residual risks:
What must change before acceptance:
What not to claim:
Owner project:
Next step:
```

### K12 — `Сбои`

- **Действие:** `System → Text`

- **Заметка:** AI OS failure modes

- **Вставить в поле текста:**

```text
# AI OS — СБОИ / FAILURE MODES

Ответ, workflow, KB-идея или handoff:
[вставить]

Задача:
Найди, как это может сломаться внутри [AI OS]. Проверяй не содержание ради содержания, а failure modes governance/evidence/routing.

Проверь сбои:
- ответ без KB grounding;
- нет source_id / card_id / evidence references, если нужны;
- weak evidence стало fact;
- unsupported claim не помечен;
- свежий факт дан без fresh check;
- route выбран неверно;
- handoff без constraints / acceptance criteria;
- blocked promotion item предложен как текущая реализация;
- raw dump предложен как knowledge source;
- вывод сильнее данных.

Верни:
Failure status: pass / revise / blocked
Failure modes table:
| Failure mode | Severity | Trigger | Detection check | Required fix | Owner project |
|---|---|---|---|---|---|
Main blocker:
Safer version:
Routing:
Next step:
```

### K13 — `Статус БЗ`

- **Действие:** `System → Text`

- **Заметка:** KB coverage / status check

- **Вставить в поле текста:**

```text
# AI OS — СТАТУС БЗ / KB COVERAGE CHECK

Тема, область или вопрос:
[вставить]

Задача:
Проверь, что именно покрыто в KB по этой теме, а что отсутствует или требует review. Не заполняй пробелы догадками.

Проверь:
- релевантные KB-файлы / Gold cards;
- support_status;
- confidence;
- evidence_count;
- limitations;
- review queue;
- release / promotion status;
- есть ли blocked items.

Верни:
KB проверен:
Источники:
Coverage status: strong / partial / weak / not found
Supported items:
Weak or missing items:
Limitations:
Review queue impact:
Promotion / acceptance status:
What can be answered now:
What cannot be answered from KB:
Routing:
Next step:
```

### K14 — `Источники`

- **Действие:** `System → Text`

- **Заметка:** Source map / evidence inventory

- **Вставить в поле текста:**

```text
# AI OS — ИСТОЧНИКИ / SOURCE MAP

Тема или утверждение:
[вставить]

Задача:
Собери карту источников и evidence inventory. Не делай большой пересказ; покажи, на чём можно строить ответ.

Проверь и раздели:
- governed KB files;
- working project files;
- release / manifest / confidence files;
- review queue;
- fresh external sources, если нужны;
- missing sources.

Верни:
KB проверен:
Source map:
| Source | Type | What it supports | Evidence status | Limitation |
|---|---|---|---|---|
Strongest evidence:
Weak / missing evidence:
Conflicts or gaps:
Fresh check needed:
Safe claims:
Unsafe claims:
Routing:
Next step:
```

### K15 — `Практика`

- **Действие:** `System → Text`

- **Заметка:** Next safe action / practical step

- **Вставить в поле текста:**

```text
# AI OS — ПРАКТИКА / NEXT SAFE ACTION

Тема, вывод или предыдущий ответ:
[вставить]

Задача:
Сформулируй один следующий безопасный практический шаг. Не строй большую стратегию и не уходи в реализацию без gate.

Проверь:
- что уже подтверждено в KB;
- какой evidence status;
- есть ли blocker;
- нужен ли fresh check;
- какой owner project;
- какие acceptance criteria;
- что нельзя делать сейчас.

Верни:
KB проверен:
Current status: draft / supported / weak / blocked / needs handoff
Best next step:
Why this step:
Owner project:
Inputs required:
Acceptance criteria:
Risk if skipped:
What not to do now:
Routing:
Итог:
Next step:
```

## Экран: `РЕШЕНИЯ`

```text
┌────────────┬────────────┬────────────┬────────────┬────────────┐
│ ⬆ НАЗАД    │ Решение    │ Варианты   │ Риски      │ Допущения  │
├────────────┼────────────┼────────────┼────────────┼────────────┤
│ Сценарии   │ Критерии   │ Пересмотр  │ В Анализ   │ В LLM      │
├────────────┼────────────┼────────────┼────────────┼────────────┤
│ В Codex    │ Участники  │ Остановка  │ Итог       │ Проект     │
└────────────┴────────────┴────────────┴────────────┴────────────┘
```

### K1 — `⬆ НАЗАД`

- **Действие:** `штатный возврат из папки`

- **Оставить штатную кнопку возврата из папки.**

### K2 — `Решение`

- **Действие:** `System → Text`

- **Заметка:** Decision memo / итоговое решение

- **Вставить в поле текста:**

```text
# РЕШЕНИЯ — DECISION MEMO

Вопрос:
[описать]

Режим:
FAST / STANDARD / DEEP

Задача:
Подготовь decision memo в [Thinking]. Не делай расчёты вместо [Analytics], не проектируй код вместо [Codex], не оформляй финальный текст вместо [LLM], если нужен отдельный handoff.

Собери:
1. Frame:
- какой вопрос решаем;
- какой результат нужен;
- кто пользователь решения;
- цена ошибки;
- обратимость решения.

2. Facts / Assumptions / Unknowns:
- FACT:
- ASSUMPTION:
- HYPOTHESIS:
- UNKNOWN:
- BLOCKER:

3. Options:
Сравни 2–4 варианта, включая «ничего не делать».

4. Criteria:
- риск;
- скорость;
- стоимость;
- обратимость;
- evidence strength;
- operational complexity;
- dependency on [Analytics] / [LLM] / [Codex] / [AI OS].

5. Risk review:
- downside;
- hidden assumptions;
- failure modes;
- detection checks;
- mitigations.

6. Decision:
- recommendation;
- why now;
- what not to do;
- what to defer.

Верни:
- decision:
- status: черновик / кандидат решения / рекомендовано / заблокировано / нужна передача / принято / устарело
- confidence: X/10
- why not 10/10:
- acceptance criteria:
- revisit trigger:
- next review:
- handoff / next step:

```

### K3 — `Варианты`

- **Действие:** `System → Text`

- **Заметка:** Options matrix with trade-offs

- **Вставить в поле текста:**

```text
# РЕШЕНИЯ — OPTIONS MATRIX

Вопрос:
[описать]

Контекст:
[факты / ограничения / цель]

Задача:
Собери 2–4 реалистичных варианта решения в [Thinking]. Обязательно включи вариант «ничего не делать».

Для каждого варианта определи:
- что означает вариант;
- когда он уместен;
- плюсы;
- минусы;
- риск;
- стоимость / трудозатраты, если известно;
- обратимость;
- evidence strength;
- зависимости от других проектов.

Сравни по критериям:
- скорость;
- качество;
- стоимость;
- риск;
- доказательность;
- сложность;
- обратимость.

Верни:
1. Decision question:
2. Options table:
| Option | What it means | Best when | Pros | Cons | Risk | Cost | Reversibility | Evidence |
|---|---|---|---|---|---|---|---|---|
3. Comparison table:
4. Recommended option:
5. Why not the alternatives:
6. Critical assumptions:
7. Status:
8. Confidence:
9. Next step:

```

### K4 — `Риски`

- **Действие:** `System → Text`

- **Заметка:** Judge-style risk review

- **Вставить в поле текста:**

```text
# РЕШЕНИЯ — RISK REVIEW

Решение / идея / план:
[описать]

Проверь как @judge в [Thinking]:
- unsupported claims;
- weak evidence;
- hidden assumptions;
- missing alternatives;
- ignored downside;
- wrong project routing;
- premature automation;
- missing acceptance criteria.

Раздели:
- FACT:
- ASSUMPTION:
- HYPOTHESIS:
- BLOCKER:

Оцени риски:
| Risk | Severity | Trigger | Impact | Detection check | Mitigation | Owner | Reversibility |
|---|---|---|---|---|---|---|---|

Верни:
- risk level: low / medium / high
- main blocker:
- weak assumptions:
- what would make this fail:
- safer next step:
- decision: proceed / revise / stop / handoff
- status:
- confidence:

```

### K5 — `Допущения`

- **Действие:** `System → Text`

- **Заметка:** Assumption audit / blockers

- **Вставить в поле текста:**

```text
# РЕШЕНИЯ — ASSUMPTION AUDIT

Вопрос / решение:
[описать]

Задача:
Проведи аудит допущений в [Thinking]. Не превращай гипотезы в факты.

Раздели входной контекст:
- FACT: подтверждено входными данными / источниками;
- ASSUMPTION: принято для рассуждения, но не доказано;
- HYPOTHESIS: полезная версия, которую надо проверить;
- UNKNOWN: неизвестно;
- BLOCKER: без этого нельзя принимать решение.

Для каждого допущения оцени:
| Assumption | Why needed | Evidence | Risk if false | How to verify | Owner | Deadline | Decision impact |
|---|---|---|---|---|---|---|---|

Верни:
1. Critical assumptions:
2. Weak assumptions:
3. Blockers:
4. What can be decided now:
5. What cannot be decided yet:
6. Required verification:
7. Status:
8. Confidence:
9. Next step:

```

### K6 — `Сценарии`

- **Действие:** `System → Text`

- **Заметка:** Base / optimistic / downside

- **Вставить в поле текста:**

```text
# РЕШЕНИЯ — SCENARIO ANALYSIS

Вопрос:
[описать]

Контекст решения:
[описать]

Задача:
Построй сценарный анализ в [Thinking]. Не выдумывай числа. Если нужны расчёты, sensitivity или финансовый эффект — отметь handoff в [Analytics].

Построй 3 сценария:
1. Base
2. Optimistic
3. Downside

Для каждого сценария определи:
- что происходит;
- ключевые допущения;
- trigger;
- leading indicators;
- downside;
- reversibility;
- decision implication.

Верни:
| Scenario | What happens | Key assumptions | Trigger | Leading indicators | Downside | Reversibility | Decision implication |
|---|---|---|---|---|---|---|---|

Дополнительно:
- cross-scenario risks:
- what would change the decision:
- handoff required: [Analytics] / [LLM] / [Codex] / [AI OS] / none
- recommendation:
- status:
- confidence:
- next step:

```

### K7 — `Критерии`

- **Действие:** `System → Text`

- **Заметка:** Weighted criteria / decision rules

- **Вставить в поле текста:**

```text
# РЕШЕНИЯ — CRITERIA / DECISION RULES

Вопрос:
[описать]

Варианты, если уже есть:
[вставить]

Задача:
Определи критерии выбора в [Thinking] и проверь, какое решение будет рациональным при текущих ограничениях.

Собери критерии:
- speed;
- quality;
- cost;
- risk;
- reversibility;
- evidence strength;
- operational complexity;
- dependency on other projects;
- personal / stakeholder impact, если применимо.

Для каждого критерия укажи:
| Criterion | Weight 1–5 | Why it matters | Measurement / signal | Deal-breaker threshold |
|---|---:|---|---|---|

Верни:
1. Decision criteria:
2. Deal-breakers:
3. Trade-offs:
4. Which option wins under current criteria:
5. What changes the decision:
6. Missing evidence:
7. Status:
8. Confidence:
9. Next step:

```

### K8 — `Пересмотр`

- **Действие:** `System → Text`

- **Заметка:** Revisit trigger / next review

- **Вставить в поле текста:**

```text
# РЕШЕНИЯ — REVISIT TRIGGER

Решение / кандидат решения:
[описать]

Текущий статус:
черновик / кандидат решения / рекомендовано / заблокировано / нужна передача / принято / устарело

Задача:
Определи условия пересмотра решения в [Thinking]. Решение не должно жить вечно без проверки.

Проверь возможные triggers:
- появились новые данные;
- изменились cost / risk / timing / scope;
- QA fail;
- допущение оказалось неверным;
- implementation feedback из [Analytics] / [LLM] / [Codex] противоречит решению;
- owner rejects hypothesis;
- решение становится трудно обратимым.

Верни:
1. Decision:
2. Current status:
3. Revisit triggers:
4. Leading indicators:
5. Next review date / condition:
6. Owner:
7. What to monitor:
8. What would force rollback / pause:
9. Confidence:
10. Next step:

```

### K9 — `В Анализ`

- **Действие:** `System → Text`

- **Заметка:** Thinking → Analytics handoff

- **Вставить в поле текста:**

```text
# ПЕРЕДАЧА ИЗ [Thinking] В [Analytics]

От: [Thinking]
Кому: [Analytics]

Тип задачи:
[calculation / scenario quantification / metric check / budget impact / plan-fact / data validation]

Decision context:
- вопрос решения:
- варианты для проверки:
- период:
- метрики:
- единицы / валюта:
- допущения:
- что нужно посчитать:
- что нельзя считать без данных:

Expected analytical output:
- таблица / расчёт / sensitivity / dashboard / data quality check

Acceptance criteria:
- формулы видны;
- источники указаны;
- assumptions отделены от facts;
- limitations указаны;
- выводы не сильнее данных.

Risks:
Evidence / confidence:
Open questions:
Next step:

```

### K10 — `В LLM`

- **Действие:** `System → Text`

- **Заметка:** Thinking → LLM handoff

- **Вставить в поле текста:**

```text
# ПЕРЕДАЧА ИЗ [Thinking] В [LLM]

От: [Thinking]
Кому: [LLM]

Тип задачи:
[memo rewrite / narrative / prompt / context package / revisor]

Decision context:
- вопрос:
- recommended decision:
- status:
- audience:
- desired tone:

Передавать только curated context:
- verified facts;
- assumptions clearly marked;
- options considered;
- risks;
- limitations;
- confidence;
- accepted terminology.

Не передавать:
- raw dump;
- secrets / API keys / .env;
- неподтверждённые claims как facts;
- приватные данные без разрешения.

Expected output:
[описать]

Acceptance criteria:
- facts / interpretation / recommendation разделены;
- unsupported claims помечены или удалены;
- confidence и limitations сохранены;
- стиль стал яснее, но смысл не усилен;
- revisor не добавляет новые факты.

Risks:
Open questions:
Next step:

```

### K11 — `В Codex`

- **Действие:** `System → Text`

- **Заметка:** Thinking → Codex after accepted decision

- **Вставить в поле текста:**

```text
# ПЕРЕДАЧА ИЗ [Thinking] В [Codex]

ВНИМАНИЕ:
Использовать только если решение уже имеет статус «рекомендовано» или «принято».
Если решение не принято — сначала вернуть в [Thinking] / [Analytics].

От: [Thinking]
Кому: [Codex]

Тип задачи:
[implementation / automation / tests / file generation]

Accepted decision:
- decision:
- status:
- owner:
- acceptance criteria:
- constraints:
- what not to change:

Files to inspect:
-

Files to change:
-

Forbidden actions:
- не менять business logic без acceptance;
- не добавлять secrets / API keys / .env;
- не править main branch напрямую;
- не сливать автоматически;
- не расширять scope без согласования.

Expected outputs:
-

Tests / checks:
-

Rollback:
-

Residual risks:
Open questions:
Next step:

```

### K12 — `Участники`

- **Действие:** `System → Text`

- **Заметка:** Stakeholder / incentives map

- **Вставить в поле текста:**

```text
# РЕШЕНИЯ — STAKEHOLDER MAP

Решение / ситуация:
[описать]

Участники:
[кто вовлечён]

Задача:
Разобрать участников, интересы, сопротивление и коммуникационные риски в [Thinking].

Для каждого участника определи:
| Stakeholder | Role | Interest | Incentive | Concern | Influence | Support / resist / neutral | Needed action |
|---|---|---|---|---|---|---|---|

Проверь:
- кто принимает решение;
- кто влияет неформально;
- кто несёт последствия;
- где конфликт интересов;
- где скрытое сопротивление;
- где нужно согласование;
- где решение может сломаться из-за коммуникации.

Верни:
1. Stakeholder map:
2. Main alignment risk:
3. Communication risks:
4. Required approvals:
5. Safer framing:
6. What not to say / not to promise:
7. Status:
8. Confidence:
9. Next step:

```

### K13 — `Остановка`

- **Действие:** `System → Text`

- **Заметка:** Stop / pause / rollback

- **Вставить в поле текста:**

```text
# РЕШЕНИЯ — STOP / PAUSE / ROLLBACK

Решение / план:
[описать]

Задача:
Определи условия остановки, паузы и отката в [Thinking].

Раздели:
- STOP: когда продолжать нельзя;
- PAUSE: когда нужно остановиться и собрать данные;
- ROLLBACK: когда нужно вернуться к предыдущему состоянию;
- ESCALATE: когда нужно передать выше / в другой проект.

Проверь stop conditions:
- нет ключевых данных;
- цена ошибки выше ожидаемой;
- риск стал необратимым;
- QA fail;
- владелец не подтверждён;
- acceptance criteria не определены;
- появились новые blockers;
- решение требует [Analytics] / [LLM] / [Codex], но handoff не сделан.

Верни:
| Condition | Type: stop/pause/rollback/escalate | Trigger | Detection check | Owner | Action |
|---|---|---|---|---|---|

Итог:
- current verdict: proceed / pause / stop / rollback / handoff
- main blocker:
- minimum safe next step:
- confidence:

```

### K14 — `Итог`

- **Действие:** `System → Text`

- **Заметка:** Final decision record

- **Вставить в поле текста:**

```text
# РЕШЕНИЯ — FINAL DECISION RECORD

Вопрос:
[описать]

Черновик решения / обсуждение:
[вставить]

Задача:
Собери финальную запись решения в [Thinking]. Не усиливай выводы выше evidence.

Проверь перед финалом:
- вопрос сформулирован;
- facts отделены от assumptions;
- рассмотрены 2–4 варианта;
- вариант «ничего не делать» рассмотрен;
- критерии выбора указаны;
- риски и blockers видны;
- acceptance criteria есть;
- revisit trigger есть;
- handoff нужен / не нужен;
- owner указан.

Верни:
1. Decision:
2. Status: черновик / кандидат решения / рекомендовано / заблокировано / нужна передача / принято / устарело
3. Owner:
4. Date:
5. Context:
6. Facts:
7. Assumptions:
8. Options considered:
9. Recommendation:
10. Why not alternatives:
11. Risks / blockers:
12. Acceptance criteria:
13. Revisit trigger:
14. Next review:
15. Handoff:
16. Confidence:
17. What not to claim:
18. Next step:

```

### K15 — `Проект`

- **Действие:** `System → Website`

- **Адрес или цель:**

```text
<CHATGPT_THINKING_PROJECT_URL>
```

## Экран: `АНАЛИЗ`

```text
┌────────────┬────────────┬────────────┬────────────┬────────────┐
│ ⬆ НАЗАД    │ Панель     │ Показатель │ Исх→Слой   │ План/Факт  │
├────────────┼────────────┼────────────┼────────────┼────────────┤
│ Кач.данн.  │ Витрина    │ Отклон.    │ Источник   │ Огранич.   │
├────────────┼────────────┼────────────┼────────────┼────────────┤
│ В LLM      │ В Codex    │ Вопросы    │ Для рук.   │ Проект     │
└────────────┴────────────┴────────────┴────────────┴────────────┘
```

### K1 — `⬆ НАЗАД`

- **Действие:** `штатный возврат из папки`

- **Оставить штатную кнопку возврата из папки.**

### K2 — `Панель`

- **Действие:** `System → Text`

- **Заметка:** Analytics dashboard / executive panel

- **Вставить в поле текста:**

```text
# АНАЛИЗ — ПАНЕЛЬ / DASHBOARD

Бизнес-вопрос:
[описать]

Контекст:
- аудитория:
- решение, для которого нужна панель:
- период:
- валюта / единицы:
- доступные данные:
- отсутствующие данные:

Задача:
Спроектируй аналитическую панель внутри [Analytics]. Не передавай в Codex, если не требуется реализация, код или автоматизация.

Обязательно определи:
- KPI / показатели;
- grain;
- period;
- filters / slicers;
- formulas;
- source mart;
- QA checks;
- limitations.

Главные файлы:
- stage_main_full: создать / спроектировать; без метрик, классификаторов и выводов;
- mart_main_full: источник показателей, flags, QA, evidence и confidence;
- mart_main_tz / mart_main_compact: управленческая версия для панели;
- dashboard slices: только из mart_main_full.

Верни:
1. Question / scope:
2. Audience / decision:
3. Data available / missing:
4. Data contract status:
5. Main files:
6. KPI catalog:
7. Dashboard structure:
8. Filters / slicers:
9. Chart specs:
   - chart_name:
   - purpose:
   - source_mart:
   - metric:
   - period:
   - grain:
   - filter:
   - caption_claim:
   - limitation:
10. QA:
11. What cannot be claimed:
12. Acceptance status:
13. Next step:
```

### K3 — `Показатель`

- **Действие:** `System → Text`

- **Заметка:** Metric definition card

- **Вставить в поле текста:**

```text
# АНАЛИЗ — ПОКАЗАТЕЛЬ / METRIC CARD

Показатель или бизнес-вопрос:
[описать]

Контекст:
- аудитория:
- период:
- валюта / единицы:
- источники данных:
- известные ограничения:

Задача:
Сформируй Definition Card для показателя в [Analytics]. Расчётная логика должна быть deterministic, без скрытой LLM-интерпретации.

Определи:
- business meaning;
- formula;
- numerator / denominator, если применимо;
- grain;
- period logic;
- filters / exclusions;
- source fields;
- required mappings;
- null / duplicate / currency policy;
- reconciliation checks.

Главные файлы:
- stage_main_full: какие поля нужны без метрик и классификаторов;
- mart_main_full: где живёт формула и QA fields;
- mart_main_tz / mart_main_compact: как показатель показывать руководителю.

Верни:
1. Metric name:
2. Business purpose:
3. Formula:
4. Grain / period / filters:
5. Required source columns:
6. Stage requirements:
7. Mart requirements:
8. QA checks:
9. Edge cases:
10. Limitations:
11. Forbidden claims:
12. Confidence:
13. Next step:
```

### K4 — `Исх→Слой`

- **Действие:** `System → Text`

- **Заметка:** RAW → stage_main_full

- **Вставить в поле текста:**

```text
# АНАЛИЗ — ИСХОДНИКИ → STAGE_MAIN_FULL

Бизнес-вопрос:
[описать]

Входные данные:
[файлы / таблицы / поля / период]

Задача:
Спроектируй слой RAW → stage_main_full для аналитического кейса в [Analytics].

Правила:
- RAW не изменять смыслово: только inventory, source metadata, raw totals, raw column list.
- stage_main_full должен быть очищенным, нормализованным и типизированным.
- В stage_main_full запрещены бизнес-метрики, классификаторы, risk labels, confidence labels, интерпретации и memo-текст.
- Stage slices можно проектировать только после stage_main_full.
- Если данных мало, явно зафиксируй gaps и assumptions.

Верни:
1. Question / scope:
2. Input inventory:
3. Data contract draft:
   - dataset:
   - owner:
   - source:
   - period:
   - grain:
   - primary keys:
   - required columns:
   - column types:
   - date logic:
   - currency / units:
   - null policy:
   - duplicate policy:
   - freshness rule:
   - mapping rules:
4. RAW checks:
5. stage_main_full spec:
   - grain:
   - required columns:
   - transformations:
   - lineage fields:
   - QA fields:
6. Reconciliation checks:
7. Data risks:
8. BLOCKERS:
9. Next step:
```

### K5 — `План/Факт`

- **Действие:** `System → Text`

- **Заметка:** Plan / fact variance analysis

- **Вставить в поле текста:**

```text
# АНАЛИЗ — ПЛАН / ФАКТ

Бизнес-вопрос:
[описать]

Данные:
[план, факт, период, разрезы, валюта]

Задача:
Подготовь план-факт анализ внутри [Analytics] с проверяемой логикой расчёта.

Обязательно:
- зафиксируй grain, period, filters и currency / units;
- определи formulas: Plan, Fact, Delta, Delta %, ABS Delta, share_of_total;
- отдели real variance, timing, data issue, mapping issue и hypothesis;
- ранжируй отклонения по ABS Delta / materiality;
- не называй причину подтверждённой без evidence.

Главные файлы:
- stage_main_full: входные поля без бизнес-метрик;
- mart_main_full: все расчёты, row_type, timing_status, risk_basis, confidence;
- mart_main_tz / mart_main_compact: top deviations и управленческий вывод.

Верни:
1. Scope:
2. Data contract status:
3. Calculation method:
4. Mart fields required:
5. Top deviations logic:
6. Findings:
   - DATA FACT:
   - CALCULATION RESULT:
   - INTERPRETATION:
   - HYPOTHESIS:
   - RECOMMENDATION:
7. Risks with risk_basis:
8. Actions with owner / due date / status, если применимо:
9. QA / reconciliation:
10. Limitations:
11. What cannot be claimed:
12. Acceptance status:
13. Next step:
```

### K6 — `Кач.данн.`

- **Действие:** `System → Text`

- **Заметка:** Data quality gate

- **Вставить в поле текста:**

```text
# АНАЛИЗ — КАЧЕСТВО ДАННЫХ / DQ GATE

Данные или кейс:
[описать / вставить]

Задача:
Проверь качество данных для аналитического кейса в [Analytics] до выводов, графиков и memo.

Проверь:
- required files exist;
- required columns exist;
- data types valid;
- dates parsed correctly;
- currency / units normalized;
- null policy applied;
- duplicate policy applied;
- freshness checked;
- mapping tables checked;
- unmatched rows listed;
- RAW total = STAGE total, если применимо;
- STAGE total = MART total, если применимо.

Главные файлы:
- stage_main_full exists or designed;
- stage_main_full has no metrics / classifiers;
- mart_main_full exists or designed;
- mart_main_tz / compact exists or designed;
- slices are derived from mart_main_full.

Верни:
1. DQ status: pass / fail / blocked
2. Data contract gaps:
3. Required checks:
4. Nulls:
5. Duplicates:
6. Unmatched rows:
7. Freshness issues:
8. Reconciliation status:
9. Impact on analysis:
10. BLOCKERS:
11. Allowed conclusions:
12. Forbidden conclusions:
13. Next step:
```

### K7 — `Витрина`

- **Действие:** `System → Text`

- **Заметка:** mart_main_full + compact mart design

- **Вставить в поле текста:**

```text
# АНАЛИЗ — ВИТРИНА / MART DESIGN

Бизнес-вопрос:
[описать]

Данные:
[что доступно]

Задача:
Спроектируй mart layer для анализа в [Analytics].

Обязательно:
- mart_main_full — полный источник истины для анализа, slices, charts и evidence;
- mart_main_tz / mart_main_compact — короткая версия для руководителя / ТЗ;
- все slices строятся только из mart_main_full;
- формулы метрик не скрывать в тексте prompt;
- не делать isolated mini-marts из raw slices.

Верни:
1. mart_main_full:
   - business purpose:
   - audience:
   - grain:
   - period:
   - keys:
   - source stage files:
   - metrics:
   - formulas:
   - dimensions:
   - classifiers:
   - filters:
   - QA totals:
   - evidence fields:
   - limitations:
2. mart_main_tz / mart_main_compact:
   - audience:
   - shortened field list:
   - headline metrics:
   - risk / confidence fields:
   - reference back to mart_main_full:
3. Required slices:
   - used_for:
   - source_mart:
   - metric:
   - grain:
   - filter:
4. QA:
   - STAGE total = MART total:
   - formulas documented:
   - unmatched rows:
   - limitations:
5. Acceptance status:
6. Next step:
```

### K8 — `Отклон.`

- **Действие:** `System → Text`

- **Заметка:** Deviation / driver analysis

- **Вставить в поле текста:**

```text
# АНАЛИЗ — ОТКЛОНЕНИЯ / DRIVER ANALYSIS

Бизнес-вопрос:
[описать]

Данные:
[период, факт/план/база, разрезы]

Задача:
Найди и объясни отклонения внутри [Analytics] через variance / driver / contribution logic.

Обязательно:
- зафиксируй metric, grain, period, filters;
- используй mart_main_full или спроектируй его перед анализом;
- ранжируй отклонения по ABS Delta / materiality;
- отдели confirmed driver от hypothesis;
- timing candidate не называй confirmed timing;
- risk указывай только с risk_basis;
- action указывай только с owner / due date / status.

Верни:
1. Question / scope:
2. Source mart / required mart:
3. Method:
4. Top deviations table spec:
   - item:
   - plan / baseline:
   - fact:
   - delta:
   - abs_delta:
   - share_of_total:
   - row_type:
   - driver_candidate:
   - driver_confirmed:
   - confidence:
5. Findings:
6. Hypotheses to verify:
7. Risks:
8. Recommended actions:
9. QA:
10. Limitations:
11. What cannot be claimed:
12. Next step:
```

### K9 — `Источник`

- **Действие:** `System → Text`

- **Заметка:** Source / data contract review

- **Вставить в поле текста:**

```text
# АНАЛИЗ — ИСТОЧНИК / DATA CONTRACT REVIEW

Источник или набор данных:
[описать]

Задача:
Проверь пригодность источника для аналитического кейса в [Analytics] и собери data contract.

Определи:
- source system / file;
- owner / business owner / technical owner;
- refresh frequency;
- load timestamp;
- period;
- grain;
- primary keys;
- foreign keys;
- required columns;
- optional columns;
- column types;
- allowed values;
- date logic;
- currency / units;
- null policy;
- duplicate policy;
- freshness rule;
- mapping rules.

Проверь связь с главными файлами:
- какие поля идут в stage_main_full;
- какие расчётные поля появятся только в mart_main_full;
- что попадёт в mart_main_tz / compact;
- какие slices допустимы только после mart_main_full.

Верни:
1. Source inventory:
2. Data contract status: complete / partial / blocked
3. Missing fields:
4. Mapping risks:
5. Reconciliation approach:
6. DQ checks:
7. Analysis allowed:
8. Analysis blocked:
9. Next step:
```

### K10 — `Огранич.`

- **Действие:** `System → Text`

- **Заметка:** Limitations / stop conditions

- **Вставить в поле текста:**

```text
# АНАЛИЗ — ОГРАНИЧЕНИЯ / STOP CONDITIONS

Кейс, вывод или расчёт:
[вставить]

Задача:
Проверь, какие выводы можно и нельзя делать в [Analytics].

Стоп-условия для управленческого вывода:
- нет data contract;
- grain не определён;
- DQ status = Fail;
- totals не reconciled;
- metric formula missing;
- currency / units mixed;
- Low Confidence подаётся как финальная причина;
- timing candidate подаётся как confirmed timing;
- risk указан без risk_basis;
- action указан без owner / due date / status;
- INOUT используется без Definition Card;
- chart caption сильнее данных;
- нет mart_main_full для mart-based conclusion.

Верни:
1. Verdict: allowed / revise / blocked
2. BLOCKERS:
3. LIMITATIONS:
4. Unsupported claims:
5. Claims allowed as DATA FACT:
6. Claims allowed as CALCULATION RESULT:
7. Claims allowed only as HYPOTHESIS:
8. Required QA before publication:
9. Required data / fields:
10. Next step:
```

### K11 — `В LLM`

- **Действие:** `System → Text`

- **Заметка:** Analytics → LLM handoff with verified facts only

- **Вставить в поле текста:**

```text
# ПЕРЕДАЧА ИЗ [Analytics] В [LLM]

От: [Analytics]
Кому: [LLM]
Тип задачи:
[редактура / narrative / prompt / context package / judge]

Цель:
[описать]

Контекст:
[коротко]

Передавать только curated context:
- verified facts;
- reconciled metrics;
- source mart / table references;
- compact tables;
- limitations;
- confidence;
- desired tone / output format.

Не передавать:
- raw dump;
- неподтверждённые claims как facts;
- secrets / API keys / .env;
- сырые логи;
- chunks / embeddings / vector DB;
- private client data без явного разрешения.

Аналитическая база:
- stage_main_full:
- mart_main_full:
- mart_main_tz / compact:
- QA status:
- reconciliation status:

Ожидаемый результат:
[описать]

Критерии приёмки:
- facts и interpretation разделены;
- unsupported claims удалены или помечены;
- limitations видны;
- confidence указан;
- текст не сильнее evidence.

Риски:
Открытые вопросы:
Next step:
```

### K12 — `В Codex`

- **Действие:** `System → Text`

- **Заметка:** Analytics → Codex implementation handoff

- **Вставить в поле текста:**

```text
# ПЕРЕДАЧА ИЗ [Analytics] В [Codex]

От: [Analytics]
Кому: [Codex]
Тип задачи:
[implementation / automation / file generation / tests / pipeline]

Цель:
[описать]

Контекст, уже решённый в [Analytics]:
- business question:
- period:
- grain:
- metrics:
- formulas:
- data contract status:
- stage_main_full spec:
- mart_main_full spec:
- mart_main_tz / compact spec:
- QA requirements:

Files to inspect:
-

Files to change:
-

Constraints:
- не менять business logic без acceptance;
- не строить mini-marts из raw slices;
- не скрывать unresolved analysis в кодовой задаче;
- не добавлять secrets / API keys / .env;
- не править main branch напрямую;
- не сливать изменения автоматически;
- не расширять scope без согласования.

Expected outputs:
-

Tests / checks:
-

Acceptance criteria:
- stage_main_full создан / обновлён согласно spec;
- mart_main_full создан / обновлён согласно formulas;
- compact mart создан из full mart;
- slices derived from mart_main_full;
- reconciliation checks passed or failed with explanation;
- residual risks listed;
- rollback notes provided.

Риски:
Открытые вопросы:
Next step:
```

### K13 — `Вопросы`

- **Действие:** `System → Text`

- **Заметка:** Missing data / clarification checklist

- **Вставить в поле текста:**

```text
# АНАЛИЗ — ВОПРОСЫ / GAP CHECK

Бизнес-вопрос:
[описать]

Доступный контекст:
[что известно]

Задача:
Определи, каких данных и решений не хватает для корректного анализа в [Analytics]. Не придумывай недостающий full context.

Проверь gaps по блокам:
- scope;
- audience;
- decision context;
- period;
- grain;
- filters;
- metrics;
- formulas;
- source files;
- required columns;
- mappings;
- currency / units;
- null / duplicate policy;
- reconciliation;
- stage_main_full;
- mart_main_full;
- mart_main_tz / compact;
- QA / acceptance.

Верни:
1. Known facts:
2. Assumptions:
3. Missing data:
4. Blocking questions: максимум 7
5. Non-blocking questions:
6. What can be designed now:
7. What cannot be concluded yet:
8. Suggested next step:
```

### K14 — `Для рук.`

- **Действие:** `System → Text`

- **Заметка:** Executive memo from compact mart

- **Вставить в поле текста:**

```text
# АНАЛИЗ — ДЛЯ РУКОВОДИТЕЛЯ / EXECUTIVE MEMO

Бизнес-вопрос:
[описать]

Проверенные данные / расчёты:
[вставить]

Задача:
Подготовь структуру управленческого вывода в [Analytics] на основе verified evidence. Не делай сильный вывод без QA и source mart.

Источник для executive layer:
- mart_main_tz / mart_main_compact для headline numbers;
- mart_main_full для appendix / evidence;
- charts только из slices derived from mart_main_full.

Структура:
1. Executive summary:
2. Key numbers:
   - metric:
   - value:
   - period:
   - source mart:
   - QA status:
3. Main deviations:
4. Main driver / confirmed cause / hypothesis:
5. Risks with risk_basis:
6. Confidence and why not higher:
7. Recommended actions:
   - action:
   - owner:
   - due date:
   - status:
8. Limitations:
9. Appendix / evidence references:

Правила:
- numbers before adjectives;
- hypothesis is not cause;
- observation is not action;
- risk without basis is not publishable;
- action without owner / due date / status is observation;
- visible report language: Russian business-readable;
- technical IDs only in appendix / evidence.

Верни:
- memo_draft:
- evidence_registry_needed:
- unsupported_claims:
- QA status:
- acceptance status:
- next step:
```

### K15 — `Проект`

- **Действие:** `System → Website`

- **Адрес или цель:**

```text
<CHATGPT_ANALYTICS_PROJECT_URL>
```

## Экран: `ЗАПРОСЫ`

```text
┌────────────┬────────────┬────────────┬────────────┬────────────┐
│ ⬆ НАЗАД    │ Реестр     │ Проверка   │ Доработка  │ Контекст   │
├────────────┼────────────┼────────────┼────────────┼────────────┤
│ Модель     │ Качество   │ Внешн.ИИ   │ В Codex    │ Порядок    │
├────────────┼────────────┼────────────┼────────────┼────────────┤
│ Черн→Пров  │ Сбои       │ Структура  │ Финал QA   │ Проект     │
└────────────┴────────────┴────────────┴────────────┴────────────┘
```

### K1 — `⬆ НАЗАД`

- **Действие:** `штатный возврат из папки`

- **Оставить штатную кнопку возврата из папки.**

### K2 — `Реестр`

- **Действие:** `System → Text`

- **Заметка:** Prompt registry entry

- **Вставить в поле текста:**

```text
# ЗАПРОСЫ — РЕЕСТР PROMPT

Задача или prompt:
[описать / вставить]

Оформи reusable prompt как запись реестра [LLM].

Заполни:
- prompt_id:
- task_type: draft / summarize / judge / revise / classify / extract / synthesize / orchestrate / route / eval
- purpose:
- input_requirements:
- output_schema:
- model_class: fast / reasoning / high-reasoning / local / judge
- quality_gate:
- known_failure_modes:
- owner_project:
- status: draft / active / deprecated / needs_review

Правила:
- не добавляй неподтверждённые факты;
- не называй конкретную модель как постоянную истину;
- отделяй факты от интерпретаций;
- если данных мало, отметь missing evidence.

Верни:
- registry_item:
- риски:
- что проверить перед reuse:
- следующий шаг:
```

### K3 — `Проверка`

- **Действие:** `System → Text`

- **Заметка:** Judge review / hallucination check

- **Вставить в поле текста:**

```text
# ЗАПРОСЫ — JUDGE-ПРОВЕРКА

Текст, prompt, workflow или результат:
[вставить]

Проверь как [LLM] judge:
- отвечает ли исходной задаче;
- отделены ли факты от интерпретаций;
- есть ли hallucinations или unsupported claims;
- не перепутан ли маршрут: [AI OS] / [Thinking] / [Analytics] / [LLM] / [Codex];
- хватает ли входных данных, ограничений и output schema;
- видны ли confidence, limitations и next step;
- нужен ли revise.

Верни строго:
- verdict: pass / revise / blocked
- reason:
- unsupported_claims:
- weak_evidence:
- wrong_routing:
- missing_constraints:
- required_fixes:
- final_quality_status:
```

### K4 — `Доработка`

- **Действие:** `System → Text`

- **Заметка:** Revise without new facts

- **Вставить в поле текста:**

```text
# ЗАПРОСЫ — ДОРАБОТКА PROMPT / OUTPUT

Исходный текст:
[вставить]

Задача:
Перепиши яснее, короче и структурнее, сохранив смысл.

Правила:
- не добавляй новые факты;
- не усиливай уверенность;
- не превращай гипотезы в факты;
- отметь места, где нужна проверка;
- сохрани routing и ограничения;
- если исходник слабый, явно скажи, что именно слабое.

Верни:
- улучшенная версия:
- что изменено:
- что осталось неподтверждённым:
- риски:
- следующий шаг:
```

### K5 — `Контекст`

- **Действие:** `System → Text`

- **Заметка:** Compact context package

- **Вставить в поле текста:**

```text
# ЗАПРОСЫ — CONTEXT PACKAGE

Задача:
[описать]

Собери compact context package для LLM.

Включи:
- цель;
- task_type;
- проверенные факты;
- релевантные выдержки / таблицы / ограничения;
- assumptions;
- missing evidence;
- forbidden claims;
- desired output format;
- quality gate.

Не включай:
- raw dump;
- секреты, API keys, `.env`;
- сырые логи;
- chunks / embeddings / vector DB;
- неподтверждённые утверждения как факты.

Верни:
- context_package:
- что исключено и почему:
- риски контекста:
- следующий шаг:
```

### K6 — `Модель`

- **Действие:** `System → Text`

- **Заметка:** Model class routing

- **Вставить в поле текста:**

```text
# ЗАПРОСЫ — MODEL ROUTING

Задача:
[описать]

Определи класс модели для выполнения задачи.

Проверь критерии:
- task_type;
- reasoning need;
- context size;
- latency;
- privacy;
- tool access;
- cost sensitivity;
- quality gate;
- need for judge/revise.

Классы:
- fast;
- reasoning;
- high-reasoning;
- local;
- judge.

Правила:
- не hardcode конкретные модели как постоянную истину;
- для актуальных цен, лимитов, API и release status нужна свежая проверка;
- deterministic расчёты маршрутизируй в [Analytics];
- код и repo changes — в [Codex].

Верни:
- recommended_model_class:
- почему:
- альтернативный класс:
- quality_gate:
- handoff_target:
- следующий шаг:
```

### K7 — `Качество`

- **Действие:** `System → Text`

- **Заметка:** LLM eval gate

- **Вставить в поле текста:**

```text
# ЗАПРОСЫ — EVAL GATE

Output для проверки:
[вставить]

Проверь качество LLM-output:
- следует ли requested schema;
- отвечает ли задаче;
- отделены ли facts / interpretation / recommendation / hypothesis;
- перечислены ли unsupported claims;
- есть ли evidence references, если они доступны;
- указаны ли confidence и limitations;
- корректен ли route / handoff;
- результат actionable.

Верни строго:
- quality_status: pass / revise / blocked
- reason:
- schema_mismatches:
- unsupported_claims:
- missing_evidence:
- required_revision:
- revision_applied: yes / no / not_applicable
- next_step:
```

### K8 — `Внешн.ИИ`

- **Действие:** `System → Text`

- **Заметка:** External AI handoff package

- **Вставить в поле текста:**

```text
# ЗАПРОСЫ — EXTERNAL AI HANDOFF

Задача для внешнего AI / инструмента:
[описать]

Собери handoff package.

Заполни:
- goal:
- owner_project:
- context_summary:
- allowed_inputs:
- forbidden_inputs:
- expected_output:
- evidence_rules:
- acceptance_criteria:
- rollback_or_stop_condition:
- QA_gate:

Запрещено передавать:
- secrets / API keys / `.env`;
- raw financial dumps без явного разрешения;
- сырые логи;
- raw transcripts;
- chunks / vector DB / embeddings;
- private client data;
- production credentials.

Верни:
- handoff_package:
- hype / tool-choice risk:
- что проверить после результата:
- следующий шаг:
```

### K9 — `В Codex`

- **Действие:** `System → Text`

- **Вставить в поле текста:**

```text
# ПЕРЕДАЧА ЗАДАЧИ

От:
Кому: [Codex]
Тип задачи:
Цель:
Контекст:
Входные данные:
Ограничения:
Ожидаемый результат:
Критерии приёмки:
Риски:
Подтверждения и уверенность:
Открытые вопросы:
```

### K10 — `Порядок`

- **Действие:** `System → Text`

- **Заметка:** Route → context → prompt → model → generate → judge → revise → final

- **Вставить в поле текста:**

```text
# ЗАПРОСЫ — LLM WORKFLOW ORDER

Задача:
[описать]

Построй порядок работы без новых концепций.

Используй цепочку:
1. route;
2. context package;
3. prompt / template;
4. model routing;
5. generate draft;
6. judge;
7. revise;
8. final;
9. handoff / next step.

Для каждого шага укажи:
- вход;
- выход;
- owner project;
- quality gate;
- stop condition.

Верни:
- recommended_workflow:
- где нужен judge:
- где нужен handoff:
- риски:
- следующий шаг:
```

### K11 — `Черн→Пров`

- **Действие:** `System → Text`

- **Заметка:** Controlled draft → judge → revise loop

- **Вставить в поле текста:**

```text
# ЗАПРОСЫ — ЧЕРНОВИК → ПРОВЕРКА → ДОРАБОТКА

Задача:
[описать]

Сделай controlled LLM loop:

1. Draft:
- подготовь черновик по задаче;
- отдели факты от интерпретаций;
- не добавляй неподтверждённые факты.

2. Judge:
- найди unsupported claims;
- проверь routing, constraints, evidence и limitations;
- дай verdict: pass / revise / blocked.

3. Revise:
- исправь только найденные проблемы;
- не добавляй новые claims;
- явно покажи, что изменено.

Верни:
- draft:
- judge_verdict:
- required_revision:
- revised_final:
- limitations:
- next_step:
```

### K12 — `Сбои`

- **Действие:** `System → Text`

- **Заметка:** Known failure modes

- **Вставить в поле текста:**

```text
# ЗАПРОСЫ — FAILURE MODES

Prompt, workflow или output:
[вставить]

Найди возможные сбои LLM-процесса:
- wrong routing;
- raw dump вместо curated context;
- неподтверждённые claims;
- скрытые assumptions;
- слабый output schema;
- отсутствие acceptance criteria;
- отсутствие judge/revise;
- overconfidence;
- tool chosen before task;
- vague Codex handoff.

Верни:
- failure_modes:
- severity: low / medium / high
- trigger:
- prevention:
- detection_check:
- required_fix:
- next_step:
```

### K13 — `Структура`

- **Действие:** `System → Text`

- **Заметка:** Output schema / contract

- **Вставить в поле текста:**

```text
# ЗАПРОСЫ — OUTPUT SCHEMA / CONTRACT

Задача:
[описать]

Спроектируй структуру ответа / output contract.

Определи:
- task_type;
- required sections;
- fields;
- accepted statuses;
- evidence rules;
- confidence format;
- limitations format;
- handoff format, если нужен;
- acceptance criteria.

Правила:
- структура должна быть проверяемой;
- не добавляй неподтверждённые факты;
- отделяй facts от interpretation;
- укажи, что считается fail.

Верни:
- output_schema:
- validation_rules:
- examples_of_fail:
- quality_gate:
- следующий шаг:
```

### K14 — `Финал QA`

- **Действие:** `System → Text`

- **Заметка:** Final QA before reuse

- **Вставить в поле текста:**

```text
# ЗАПРОСЫ — FINAL QA

Финальный output:
[вставить]

Проверь перед использованием / сохранением / передачей дальше:
- задача выполнена;
- схема соблюдена;
- facts и interpretation разделены;
- unsupported claims удалены или помечены;
- confidence указан;
- limitations видны;
- route / owner project верный;
- handoff содержит acceptance criteria, если нужен;
- next step конкретный.

Верни:
- final_verdict: pass / revise / blocked
- release_notes:
- residual_risks:
- what_not_to_claim:
- approved_next_step:
```

### K15 — `Проект`

- **Действие:** `System → Website`

- **Адрес или цель:**

```text
<CHATGPT_LLM_PROJECT_URL>
```

## Экран: `CODEX`

Назначение экрана: подготовка implementation-ready task packages для Codex / Codex APP / Codex CLI / IDE.

`[Codex]` не принимает бизнес-решения, не считает метрики, не проектирует LLM-workflow и не исполняет изменения. Он получает handoff из `[Thinking]`, `[Analytics]`, `[LLM]`, `[AI OS]`, `[Inbox Router]` или GitHub Issues и превращает его в проверяемое ТЗ.

Главный принцип:

```text
Handoff → Codex Task Package → QA ТЗ → Executor
```

Кнопки `CODEX` выбирают тип task package, а не шаги одного workflow. Для notebook/script → pipeline использовать связку `Inspect → Pipeline → QA ТЗ → Long-run`.

```text
┌────────────┬────────────┬────────────┬────────────┬────────────┐
│ ⬆ НАЗАД    │ ТЗ Codex   │ Long-run   │ QA ТЗ      │ Blocker    │
├────────────┼────────────┼────────────┼────────────┼────────────┤
│ Docs-only  │ Bugfix     │ Refactor   │ Pipeline   │ Tests      │
├────────────┼────────────┼────────────┼────────────┼────────────┤
│ Repo/PR    │ Review     │ Handoff    │ Inspect    │ Проект     │
└────────────┴────────────┴────────────┴────────────┴────────────┘
```
### K1 — `⬆ НАЗАД`

- **Действие:** `штатный возврат из папки`

- **Оставить штатную кнопку возврата из папки.**

### K2 — `ТЗ Codex`

- **Действие:** `System → Text`

- **Заметка:** Universal implementation-ready task package

- **Вставить в поле текста:**

```text
# CODEX — TASK PACKAGE FACTORY

Входной handoff:
[вставить]

Задача:
Собери implementation-ready task package для Codex. Не реализуй задачу. Не редактируй файлы. Не добавляй неподтверждённые требования.

Проверь, что вход содержит или явно помечает:
- context;
- objective;
- repository / local path;
- inputs;
- files to inspect;
- files allowed to modify;
- forbidden actions;
- expected outputs;
- acceptance criteria;
- tests / smoke checks;
- rollback plan;
- autonomy mode.

Если данных не хватает, не выдумывай. Пометь status: revise / blocked.

Верни строго:

# Codex Task

## Context
## Objective
## Autonomy mode
normal / long-run / inspect-only

## Inputs
## Repository / local path
## Files to inspect
## Files allowed to modify
## Forbidden actions
## Expected outputs
## Acceptance criteria
## Tests / smoke checks
## Rollback plan
## Hard blockers
## Assumptions
## Final response format

Summary:
Files changed:
Tests/checks run:
Assumptions:
Risks/limitations:
Rollback:
Acceptance status:
Next step:
```

### K3 — `Long-run`

- **Действие:** `System → Text`

- **Заметка:** Ultra-long / Codex APP task package

- **Вставить в поле текста:**

```text
# CODEX — LONG-RUN TASK PACKAGE

Входной handoff:
[вставить]

Задача:
Собери ultra-long / Codex APP task package. Не исполняй задачу. Не редактируй файлы.

Использовать только если:
- задача scoped;
- изменения локальные и обратимые;
- allowed files понятны;
- есть checks / smoke checks;
- можно продолжать без микровопросов до hard blocker.

Добавь:
- execution mode;
- batches;
- allowed scope;
- forbidden actions;
- retry policy;
- stop conditions;
- final report contract.

Верни:

# Codex APP Long-run Task

## Context
## Objective
## Execution mode
ultra-long-local / long-run / inspect-only

## Inputs
## Repository / local path
## Allowed files
## Forbidden files/actions
## Batch plan
## Checks per batch
## Acceptance criteria
## Stop conditions
## Rollback plan
## Final report format
```

### K4 — `QA ТЗ`

- **Действие:** `System → Text`

- **Заметка:** Judge check before executor handoff

- **Вставить в поле текста:**

```text
# CODEX — TASK PACKAGE QA / JUDGE

Codex task package:
[вставить]

Задача:
Проверь как @judge, готово ли ТЗ к передаче исполнителю Codex. Не реализуй задачу.

Проверь:
- objective один и проверяемый;
- context достаточный;
- repository / local path указан;
- files to inspect указаны;
- files allowed to modify указаны;
- forbidden actions указаны;
- expected outputs проверяемы;
- acceptance criteria можно отметить pass/fail;
- tests / smoke checks соответствуют риску;
- rollback plan есть;
- hard blockers видны;
- scope не расширен;
- нет business logic / formulas / schemas / output contracts без explicit acceptance;
- нет secrets / `.env` / credentials;
- нет production/deploy/runtime mutation.

Верни строго:
QA verdict: pass / revise / blocked
Missing fields:
Scope risks:
Forbidden-action risks:
Unsupported assumptions:
Hard blockers:
Required fixes:
Approved task type:
Ready for Codex: yes / no
```

### K5 — `Blocker`

- **Действие:** `System → Text`

- **Заметка:** Why the task cannot safely proceed

- **Вставить в поле текста:**

```text
# CODEX — BLOCKER REPORT

Входная задача / handoff:
[вставить]

Задача:
Определи, почему задачу нельзя безопасно передать в Codex сейчас. Не реализуй. Не придумывай недостающие данные.

Проверь blocker categories:
- нет objective;
- нет repository / local path;
- нет allowed files;
- нет forbidden actions;
- нет acceptance criteria;
- нет tests / smoke checks;
- нет rollback;
- нужны secrets / `.env` / credentials;
- затрагивается production/deploy/runtime;
- меняются business logic / formulas / schemas / APIs / output contracts;
- требуется destructive action;
- невозможно проверить результат.

Верни:
blocked_reason:
missing_input:
risk_if_continue:
safe_next_step:
what can be prepared now:
what is blocked:
```

### K6 — `Docs-only`

- **Действие:** `System → Text`

- **Заметка:** Safe documentation/settings task package

- **Вставить в поле текста:**

```text
# CODEX — DOCS-ONLY TASK PACKAGE

Входной handoff:
[вставить]

Задача:
Собери task package для безопасной docs-only задачи. Не реализуй.

Разрешённый scope:
- README;
- setup docs;
- manifest;
- upload guide;
- project settings;
- documentation consistency.

Запрещено:
- менять business logic;
- менять governed KB content без explicit scope;
- менять source cards / raw transcripts / chunks / embeddings / vector DB;
- добавлять web UI / semantic search / agentic workflow;
- трогать secrets / `.env`.

Верни полный Codex Task Package с:
- allowed files;
- forbidden files/actions;
- docs-only checks;
- acceptance criteria;
- rollback plan.
```

### K7 — `Bugfix`

- **Действие:** `System → Text`

- **Заметка:** Bugfix package: reproduce/root cause/test

- **Вставить в поле текста:**

```text
# CODEX — BUGFIX TASK PACKAGE

Описание ошибки:
[вставить]

Задача:
Собери task package на bugfix. Не исправляй ошибку.

Обязательно включи:
- observed behavior;
- expected behavior;
- reproduction steps or evidence;
- likely files to inspect;
- files allowed to modify;
- forbidden actions;
- minimal fix principle;
- regression test / smoke check;
- acceptance criteria;
- rollback plan.

Верни Codex Task Package.
```

### K8 — `Refactor`

- **Действие:** `System → Text`

- **Заметка:** Refactor package without behavior changes

- **Вставить в поле текста:**

```text
# CODEX — REFACTOR TASK PACKAGE

Входной handoff:
[вставить]

Задача:
Собери task package на безопасный refactor. Не реализуй.

Обязательные условия:
- behavior must be preserved;
- output contracts must be preserved;
- no business logic changes;
- no schema/API/column changes unless explicitly accepted;
- regression/golden checks required where possible.

Верни Codex Task Package.
```

### K9 — `Pipeline`

- **Действие:** `System → Text`

- **Заметка:** Notebook/script to RAW-STAGE-MART-GRAPHICS-LLM-MEMO package

- **Вставить в поле текста:**

```text
# CODEX — NOTEBOOK / SCRIPT TO PIPELINE TASK PACKAGE

Входной handoff из [Analytics] или текущего проекта:
[вставить]

Задача:
Собери task package на перевод Python notebooks / scripts в воспроизводимый pipeline. Не реализуй.

Целевая архитектура:
RAW → STAGE → MART → GRAPHICS → LLM PACKAGE → MEMO → QA

Проверь, что уже определено:
- repository / local path;
- notebooks / scripts to inspect;
- source input files;
- current outputs / baseline artifacts;
- business question;
- period;
- grain;
- metrics;
- formulas;
- data contract;
- RAW inventory rules;
- STAGE normalization rules;
- MART metrics and dimensions;
- GRAPHICS list and source mart/slices;
- LLM PACKAGE evidence / context rules;
- MEMO structure;
- QA / reconciliation requirements.

Если formulas, grain, output contracts или business definitions не определены — status: blocked / needs [Analytics].

Обязательные ограничения:
- не менять формулы без explicit acceptance;
- не менять schemas / column names / output contracts без explicit acceptance;
- не строить graphics напрямую из raw, только из mart/slices;
- deterministic расчёты отделить от LLM narrative;
- LLM MEMO писать только из evidence / context package;
- не трогать raw/private files;
- не добавлять secrets / `.env`;
- не добавлять web UI / vector DB / agentic workflow без отдельного gate.

Expected outputs:
- raw loader;
- stage builder;
- mart builder;
- graphics generator;
- LLM context/evidence package builder;
- memo draft generator or memo package;
- QA / validation checks;
- README / run instructions;
- tests / smoke checks.

Acceptance criteria:
- baseline воспроизводится или явно зафиксирован как unavailable;
- RAW totals = STAGE totals, где применимо;
- STAGE totals = MART totals, где применимо;
- output contract сохранён;
- graphics generated from mart/slices;
- LLM package contains verified facts only;
- tests / smoke checks defined;
- rollback plan provided.

Верни Codex Task Package.
```

### K10 — `Tests`

- **Действие:** `System → Text`

- **Заметка:** Tests / smoke / regression package

- **Вставить в поле текста:**

```text
# CODEX — TESTS / SMOKE CHECKS TASK PACKAGE

Входная задача:
[вставить]

Задача:
Собери task package на tests / smoke checks. Не запускай проверки.

Определи:
- risk level;
- smallest meaningful checks;
- existing tests to run;
- tests to add, если нужно;
- contract checks;
- smoke checks;
- golden/regression checks;
- artifact validation;
- pass/fail criteria.

Верни Codex Task Package.
```

### K11 — `Repo/PR`

- **Действие:** `System → Text`

- **Заметка:** Repository branch / PR workflow package

- **Вставить в поле текста:**

```text
# CODEX — REPO / PR TASK PACKAGE

Входная задача:
[вставить]

Задача:
Собери task package для local repo → branch → commit → push → PR workflow. Не выполняй git-команды.

Включи:
- repository / local path;
- expected branch name;
- allowed files;
- forbidden files;
- checks before commit;
- commit message type;
- PR summary requirements;
- merge restrictions;
- cleanup expectations;
- rollback plan.

Запрещено:
- direct commit to main;
- force push;
- merge without explicit approval;
- broad unrelated changes.

Верни Codex Task Package.
```

### K12 — `Review`

- **Действие:** `System → Text`

- **Заметка:** Review Codex result / diff / report before acceptance

- **Вставить в поле текста:**

```text
# CODEX — RESULT / DIFF REVIEW

Результат Codex, diff, PR summary или final report:
[вставить]

Исходное ТЗ / acceptance criteria:
[вставить, если есть]

Задача:
Проверь как @judge, можно ли принимать результат. Не добавляй новые требования и не исправляй код.

Проверь:
- objective выполнен;
- изменения остались в allowed files;
- forbidden actions не выполнены;
- business logic / formulas / schemas / output contracts не изменены без explicit acceptance;
- tests / smoke checks реально указаны;
- failing checks не скрыты;
- rollback path понятен;
- residual risks названы;
- final report содержит Summary, Files changed, Tests/checks, Assumptions, Risks, Acceptance status, Next step.

Верни строго:
Review verdict: pass / revise / blocked
What passed:
What failed:
Scope issues:
Contract / schema risks:
Missing tests:
Unsupported claims:
Required fix:
Acceptance status:
Safe next step:
```

### K13 — `Handoff`

- **Действие:** `System → Text`

- **Заметка:** Return to source project or executor handoff

- **Вставить в поле текста:**

```text
# CODEX — HANDOFF BACK / NEXT PROJECT

Codex task / result / blocker:
[вставить]

Задача:
Определи, нужно ли вернуть задачу в [Thinking], [Analytics], [LLM], [AI OS] или можно передавать executor-layer.

Верни:
Current status:
Best destination:
Reason:
What is ready:
What is missing:
Risks:
Next handoff package:
```

### K14 — `Inspect`

- **Действие:** `System → Text`

- **Заметка:** Inspect-only project structure package

- **Вставить в поле текста:**

```text
# CODEX — INSPECT-ONLY PROJECT STRUCTURE PACKAGE

Задача / репозиторий:
[вставить]

Задача:
Собери inspect-only task package для получения структуры проекта. Не реализуй, не редактируй файлы.

Цель inspect:
- понять архитектуру проекта;
- найти ключевые папки;
- найти notebooks / scripts / entrypoints;
- найти tests / configs / docs;
- найти input/output/artifact locations;
- выявить private/sensitive зоны;
- подготовить следующий safe handoff для Refactor / Pipeline / Tests / Long-run.

Autonomy mode:
inspect-only

Files allowed to modify:
none

Forbidden actions:
- не менять файлы;
- не делать commit / push / merge;
- не удалять файлы;
- не трогать secrets / `.env` / credentials;
- не запускать destructive commands;
- не менять business logic / formulas / output contracts.

Expected output:
- project tree на 2–3 уровня;
- назначение ключевых папок;
- main entrypoints;
- notebooks / scripts inventory;
- data / artifacts / generated outputs inventory;
- tests/checks available;
- configs / environment notes;
- private/sensitive areas;
- risks / blockers;
- recommended next step.

Верни Codex Task Package.
```

### K15 — `Проект`

- **Действие:** `System → Website`

- **Адрес или цель:**

```text
<CHATGPT_CODEX_PROJECT_URL>
```

## Экран: `ПРОВЕРКА`

Назначение экрана: универсальный judge-контур для проверки результата перед сохранением, передачей или использованием. Экран не заменяет специализированные проверки в `МАРШРУТ`, `AI OS`, `ЗАПРОСЫ`, `АНАЛИЗ` и `CODEX`, а служит быстрым аварийным QA-пультом.

Главный принцип:

```text
Draft / Handoff / Output → Judge Gate → pass / revise / blocked → Approved next step
```

```text
┌────────────┬────────────┬────────────┬────────────┬────────────┐
│ ⬆ НАЗАД    │ Quick QA   │ Evidence   │ Факт/Толк  │ Schema QA  │
├────────────┼────────────┼────────────┼────────────┼────────────┤
│ Fix brief  │ Blocker    │ Status     │ Risk QA    │ Accept     │
├────────────┼────────────┼────────────┼────────────┼────────────┤
│ Halluc.    │ Route QA   │ Handoff    │ Final QA   │ Fast Pass  │
└────────────┴────────────┴────────────┴────────────┴────────────┘
```

### K1 — `⬆ НАЗАД`

- **Действие:** `штатный возврат из папки`

- **Заметка:** Не перепрограммировать

- **Оставить штатную кнопку возврата из папки.**


### K2 — `Quick QA`

- **Действие:** `System → Text`

- **Заметка:** Universal 30-second judge gate

- **Вставить в поле текста:**

```text
# ПРОВЕРКА — QUICK QA

Материал для проверки:
[вставить]

Intended use:
черновик / handoff / memo / prompt / Codex task / KB / руководитель / другое

Задача:
Проверь как @judge. Не переписывай материал и не решай исходную задачу. Дай короткий verdict и один безопасный следующий шаг.

Проверь:
- отвечает ли материал исходной задаче;
- есть ли unsupported claims;
- разделены ли FACT / INTERPRETATION / HYPOTHESIS / RECOMMENDATION;
- видны ли missing evidence, confidence и limitations;
- верен ли routing / owner project;
- есть ли actionable next step.

Верни строго:
QA verdict: pass / revise / blocked
Reason:
Unsupported claims:
Missing evidence:
Wrong routing:
Main risk:
Required revision:
Approved next step:
```


### K3 — `Evidence`

- **Действие:** `System → Text`

- **Заметка:** Evidence / unsupported claims check

- **Вставить в поле текста:**

```text
# ПРОВЕРКА — EVIDENCE QA

Материал для проверки:
[вставить]

Claim context / intended use:
[черновик / memo / KB / handoff / руководитель / другое]

Задача:
Проверь только доказательность. Не улучшай стиль и не расширяй содержание. Главный вопрос: какие утверждения нельзя безопасно использовать как facts.

Раздели claims:
- SUPPORTED FACT: подтверждено входным контекстом / источниками;
- WEAK CLAIM: есть слабая опора или неполный контекст;
- UNSUPPORTED CLAIM: нет подтверждения;
- FRESHNESS REQUIRED: нужен свежий web/API/pricing/release/legal check;
- INTERPRETATION: допустимое толкование, но не факт;
- HYPOTHESIS: версия для проверки.

Верни строго:
Evidence verdict: pass / revise / blocked
Supported claims:
Weak claims:
Unsupported claims:
Freshness-required claims:
What must not be claimed:
Required evidence:
Safe wording:
Owner project for verification:
Next step:
```


### K4 — `Факт/Толк`

- **Действие:** `System → Text`

- **Заметка:** Facts vs interpretation splitter

- **Вставить в поле текста:**

```text
# ПРОВЕРКА — FACT / INTERPRETATION SPLIT

Материал для проверки:
[вставить]

Задача:
Раздели материал на факты, расчётные результаты, интерпретации, гипотезы, рекомендации и blockers. Не добавляй новые факты.

Классифицируй каждое значимое утверждение:
- DATA FACT: прямо дано во входе / источнике;
- CALCULATION RESULT: следует из формулы или расчёта;
- INTERPRETATION: вывод из фактов;
- HYPOTHESIS: версия, требующая проверки;
- RECOMMENDATION: действие / совет;
- BLOCKER: то, без чего нельзя принять вывод;
- UNSUPPORTED: не подтверждено входом.

Проверь:
- не поданы ли гипотезы как факты;
- не названа ли причина подтверждённой без evidence;
- не сильнее ли рекомендация, чем данные;
- есть ли confidence и limitations.

Верни строго:
Split verdict: pass / revise / blocked
DATA FACT:
CALCULATION RESULT:
INTERPRETATION:
HYPOTHESIS:
RECOMMENDATION:
BLOCKER:
UNSUPPORTED:
Required rewrite rules:
Safe final wording:
Next step:
```


### K5 — `Schema QA`

- **Действие:** `System → Text`

- **Заметка:** Output schema / contract check

- **Вставить в поле текста:**

```text
# ПРОВЕРКА — SCHEMA / OUTPUT CONTRACT QA

Материал для проверки:
[вставить]

Expected schema / output contract:
[вставить, если есть]

Задача:
Проверь, соблюдена ли требуемая структура ответа. Не оценивай красоту текста, оценивай проверяемость и полноту contract.

Проверь:
- есть ли все обязательные разделы;
- заполнены ли обязательные поля;
- статусы из допустимого набора;
- facts / assumptions / risks / limitations разделены;
- output можно проверить pass/fail;
- next step конкретный;
- handoff содержит objective, inputs, constraints, expected output, acceptance criteria, risks;
- нет лишних неподтверждённых разделов.

Верни строго:
Schema verdict: pass / revise / blocked
Missing required sections:
Missing required fields:
Invalid statuses / labels:
Ambiguous fields:
Extra risky content:
Required schema fixes:
Corrected output skeleton:
Next step:
```


### K6 — `Fix brief`

- **Действие:** `System → Text`

- **Заметка:** Revision brief without rewriting everything

- **Вставить в поле текста:**

```text
# ПРОВЕРКА — REVISION BRIEF

Материал для доработки:
[вставить]

Исходная задача / intended use:
[вставить]

Задача:
Не переписывай весь материал. Составь точный brief на доработку: что исправить, удалить, смягчить, подтвердить или передать в другой проект.

Проверь:
- unsupported claims;
- missing evidence;
- wrong routing;
- overconfidence;
- missing constraints;
- нарушенную структуру;
- слабый next step;
- риск использования без acceptance.

Верни строго:
Revision verdict: revise / blocked / no revision needed
Must delete:
Must mark as hypothesis:
Must support with evidence:
Must soften wording:
Must add:
Must route / handoff:
Do not change:
Patch plan:
Acceptance check after revision:
Next step:
```


### K7 — `Blocker`

- **Действие:** `System → Text`

- **Заметка:** Stop / pause / blocked gate

- **Вставить в поле текста:**

```text
# ПРОВЕРКА — BLOCKER GATE

Материал / решение / handoff:
[вставить]

Задача:
Определи, можно ли продолжать, или есть stop / pause / blocked condition. Не решай задачу вместо владельца.

Проверь blockers:
- нет исходной задачи / objective;
- нет owner project;
- нет ключевых данных / источников;
- вывод сильнее evidence;
- route неясен;
- handoff без constraints / acceptance criteria;
- Codex-задача без files / tests / rollback;
- аналитический вывод без data contract / QA;
- есть destructive action без явного gate;
- есть secrets / `.env` / private data risk;
- нужен fresh check, но он не выполнен.

Верни строго:
Blocker verdict: proceed / pause / blocked / escalate
Main blocker:
Stop conditions:
Pause conditions:
What is safe to do now:
What is blocked:
Owner project:
Required fix to unblock:
Minimum safe next step:
```


### K8 — `Status`

- **Действие:** `System → Text`

- **Заметка:** Artifact / decision / output status classification

- **Вставить в поле текста:**

```text
# ПРОВЕРКА — STATUS CLASSIFIER

Материал / prompt / решение / handoff / output:
[вставить]

Задача:
Определи рабочий статус материала. Не улучшай текст. Не повышай статус без evidence и acceptance.

Допустимые статусы:
- raw_capture: сырой вход;
- draft: черновик;
- candidate: можно обсуждать, но не использовать как финал;
- revise_required: нужна доработка;
- blocked: нельзя использовать до исправления blocker;
- accepted: можно использовать в указанном intended use;
- deprecated: устарело;
- needs_handoff: нужно передать в другой проект.

Проверь:
- intended use;
- evidence status;
- completeness;
- routing;
- acceptance criteria;
- residual risks;
- next review trigger.

Верни строго:
Status:
Why:
Allowed use:
Forbidden use:
Evidence status:
Acceptance status: pass / revise / blocked
Residual risks:
Revisit trigger:
Owner project:
Next step:
```


### K9 — `Risk QA`

- **Действие:** `System → Text`

- **Заметка:** Risk / hidden assumptions / failure modes

- **Вставить в поле текста:**

```text
# ПРОВЕРКА — RISK QA

Материал / решение / план:
[вставить]

Задача:
Проверь как @judge риски, скрытые assumptions и failure modes. Не спорь ради спора: ищи реальные условия поломки.

Проверь:
- hidden assumptions;
- weak evidence;
- overconfidence;
- ignored downside;
- wrong routing;
- premature automation;
- missing owner / acceptance / rollback;
- риск использования результата не по назначению;
- что будет, если главный assumption ложный.

Верни строго:
Risk verdict: low / medium / high / blocked
Top risks table:
| Risk | Severity | Trigger | Impact | Detection check | Mitigation | Owner |
|---|---|---|---|---|---|---|
Critical assumptions:
Failure modes:
What would make this unsafe:
Required safeguards:
Safer next step:
Confidence:
```


### K10 — `Accept`

- **Действие:** `System → Text`

- **Заметка:** Acceptance / save / handoff gate

- **Вставить в поле текста:**

```text
# ПРОВЕРКА — ACCEPTANCE GATE

Материал для приёмки:
[вставить]

Intended use:
сохранить / передать / использовать в memo / использовать в KB / отправить в Codex / показать руководителю / другое

Acceptance criteria:
[вставить, если есть]

Задача:
Проверь, можно ли принять материал для указанного intended use. Не принимай черновик как финал только потому, что он выглядит убедительно.

Проверь:
- задача выполнена;
- output schema соблюдена;
- evidence / sources / limitations видны;
- unsupported claims удалены или помечены;
- routing / owner project корректен;
- acceptance criteria проверяемы;
- residual risks перечислены;
- next step конкретный;
- для Codex есть constraints, tests, rollback;
- для KB есть confidence и what_not_to_claim.

Верни строго:
Acceptance verdict: pass / revise / blocked
Accepted for intended use: да / нет
Missing acceptance criteria:
Required fixes before acceptance:
Residual risks:
What not to claim:
Save / handoff allowed: да / нет
Approved next step:
```


### K11 — `Halluc.`

- **Действие:** `System → Text`

- **Заметка:** Hallucination / overclaiming check

- **Вставить в поле текста:**

```text
# ПРОВЕРКА — HALLUCINATION / OVERCLAIM QA

Материал для проверки:
[вставить]

Known source context, если есть:
[вставить]

Задача:
Найди возможные hallucinations, overclaiming и факты, которые могли устареть. Не добавляй новые факты и не ищи оправдания слабым claims.

Проверь:
- конкретные факты без источника;
- имена, даты, версии, цены, лимиты, API, законы, релизы, benchmark claims;
- причинно-следственные утверждения без evidence;
- “лучший / самый / всегда / доказано” без основания;
- выводы, которые сильнее входных данных;
- invented sources / invented file references;
- скрытое смешение факта и интерпретации.

Верни строго:
Hallucination verdict: pass / revise / blocked
Likely hallucinations:
Overclaimed statements:
Freshness required:
Unsupported causality:
Invented or missing sources:
Safe replacements:
Claims to remove:
Next step:
```


### K12 — `Route QA`

- **Действие:** `System → Text`

- **Заметка:** Cross-project routing judge

- **Вставить в поле текста:**

```text
# ПРОВЕРКА — ROUTE QA

Маршрут / ответ / handoff для проверки:
[вставить]

Задача:
Проверь как @judge, корректен ли routing между проектами. Не решай целевую задачу.

Проверь:
- destination explicit;
- task type корректный;
- confidence honest;
- facts / assumptions / risks разделены;
- missing data visible;
- one next step provided;
- handoff used for project work;
- нет расчётов в [AI OS];
- нет кода в [Thinking];
- нет prompt/workflow в [Analytics];
- нет vague context в Things;
- нет Codex без constraints / acceptance / rollback.

Верни строго:
Route verdict: pass / revise / blocked
Wrong routing:
Correct destination:
Missing constraints:
Unsupported assumptions:
Main risk:
Required fix:
Corrected handoff skeleton:
Approved next step:
```


### K13 — `Handoff`

- **Действие:** `System → Text`

- **Заметка:** Handoff completeness and safety QA

- **Вставить в поле текста:**

```text
# ПРОВЕРКА — HANDOFF QA

Handoff для проверки:
[вставить]

Задача:
Проверь, готов ли handoff к передаче в целевой проект. Не выполняй handoff и не решай задачу.

Проверь обязательные поля:
- From;
- To;
- Task type;
- Objective;
- Context;
- Inputs;
- Constraints;
- Expected output;
- Acceptance criteria;
- Risks;
- Evidence / confidence;
- Open questions;
- Suggested first step.

Дополнительно для [Codex] / Codex APP:
- repository / local path;
- files to inspect;
- files allowed to change;
- forbidden actions;
- checks / smoke tests;
- rollback / stop condition;
- final report format.

Верни строго:
Handoff verdict: pass / revise / blocked
Missing fields:
Ambiguous scope:
Wrong destination:
Unsupported claims inside handoff:
Missing acceptance criteria:
Missing rollback / stop condition:
Required fixes:
Approved handoff summary:
Next step:
```


### K14 — `Final QA`

- **Действие:** `System → Text`

- **Заметка:** Final gate before save / share / reuse

- **Вставить в поле текста:**

```text
# ПРОВЕРКА — FINAL QA

Финальный материал:
[вставить]

Intended final use:
сохранить в Knowledge / отправить в проект / использовать в memo / показать руководителю / передать в Codex / другое

Задача:
Проверь материал перед финальным использованием. Не переписывай его полностью; дай verdict, release notes и обязательные исправления.

Проверь:
- исходная задача выполнена;
- output schema соблюдена;
- facts / interpretation / hypothesis / recommendation разделены;
- unsupported claims удалены или помечены;
- confidence и limitations видны;
- route / owner project верный;
- handoff содержит acceptance criteria, если нужен;
- next step конкретный;
- residual risks честно указаны;
- материал не обещает production readiness без acceptance.

Верни строго:
Final verdict: pass / revise / blocked
Release notes:
Unsupported claims:
Required final fixes:
Residual risks:
What not to claim:
Approved use:
Save / share allowed: да / нет
Approved next step:
```


### K15 — `Fast Pass`

- **Действие:** `System → Text`

- **Заметка:** Ultra-short QA verdict

- **Вставить в поле текста:**

```text
# ПРОВЕРКА — FAST PASS

Материал:
[вставить]

Задача:
Дай ультракороткую QA-проверку. Не делай полный аудит. Используй только для низкорисковых черновиков.

Проверь за один проход:
- задача выполнена;
- нет очевидных unsupported claims;
- маршрут не выглядит ошибочным;
- есть понятный next step.

Верни строго:
Verdict: pass / revise / blocked
One-line reason:
Biggest risk:
One required fix:
Approved next step:
```

## Экран: `ВХОД`

```text
┌────────────┬────────────┬────────────┬────────────┬────────────┐
│ ⬆ НАЗАД    │ Inbox      │ Idea       │ Problem    │ Task       │
├────────────┼────────────┼────────────┼────────────┼────────────┤
│ Meeting    │ Metric     │ Bug        │ Risk       │ Memo seed  │
├────────────┼────────────┼────────────┼────────────┼────────────┤
│ Research   │ Prompt     │ Decision   │ Route later│ Obsidian   │
└────────────┴────────────┴────────────┴────────────┴────────────┘
```

### Роль папки `ВХОД`

`ВХОД` — это быстрый intake-контур. Он не решает задачу, не делает финальный routing, не проводит QA и не создаёт project handoff. Его задача — быстро нормализовать сырой материал и подготовить его к последующему маршруту через `МАРШРУТ`.

Правило:

```text
Capture → normalize → route later
```

Не делать внутри Capture:
- не превращать каждую мысль в Things;
- не принимать решения;
- не отправлять в Codex;
- не делать расчёты;
- не писать финальную записку;
- не считать гипотезу фактом.

### K1 — `⬆ НАЗАД`

- **Действие:** `штатный возврат из папки`

- **Заметка:** Не перепрограммировать

- **Оставить штатную кнопку возврата из папки.**


### K2 — `Inbox`

- **Действие:** `System → Text`

- **Заметка:** Universal fast capture / normalize only

- **Вставить в поле текста:**

```text
# CAPTURE — INBOX / БЫСТРЫЙ ВХОД

Raw input:
[вставить]

Задача:
Нормализуй входящий материал для последующей обработки. Не решай задачу, не делай глубокий анализ, не создавай финальный routing и не превращай всё подряд в Things.

Extract only:
- capture_title:
- raw_summary:
- type_candidate: idea / problem / task / meeting / metric / bug / risk / memo_seed / research_seed / prompt_seed / decision_seed / unclear
- facts_given:
- missing_details:
- capture_status: raw / normalized / route_needed / ready_for_project
- routing_needed: yes / no
- urgency: none / today / dated / unclear
- next_safe_action: route later / ask / save to notes / create Things / create Calendar / handoff candidate
- note_for_later:

Rules:
- не придумывай недостающие факты;
- если тип неясен, ставь unclear;
- максимум один следующий безопасный шаг;
- QA и project routing выполняются позже.
```


### K3 — `Idea`

- **Действие:** `System → Text`

- **Заметка:** Idea / hypothesis intake

- **Вставить в поле текста:**

```text
# CAPTURE — IDEA / ГИПОТЕЗА

Raw input:
[вставить]

Задача:
Зафиксируй идею как сырой кандидат. Не оценивай её глубоко и не превращай в решение.

Extract only:
- idea:
- trigger / why it appeared:
- possible use:
- known facts:
- assumptions:
- related area / project candidate:
- evidence_needed:
- not_decided:
- capture_status: raw / normalized / route_needed
- next_safe_action:

Rules:
- гипотезу не называй фактом;
- не обещай реализацию;
- если идея требует проверки AI / инструмента / модели / pricing, пометь freshness_needed.
```


### K4 — `Problem`

- **Действие:** `System → Text`

- **Заметка:** Problem / friction intake

- **Вставить в поле текста:**

```text
# CAPTURE — PROBLEM / БОЛЬ

Raw input:
[вставить]

Задача:
Зафиксируй проблему без поиска виноватых и без преждевременного решения.

Extract only:
- problem:
- context:
- affected area:
- observed symptom:
- evidence_given:
- missing_details:
- possible impact:
- severity: low / medium / high / unclear
- owner_project_candidate:
- capture_status: raw / normalized / route_needed
- next_safe_action:

Rules:
- не назначай root cause, если он не указан;
- не предлагай Codex, пока не определены scope и acceptance;
- если проблема про данные, пометь candidate_owner: [Analytics].
```


### K5 — `Task`

- **Действие:** `System → Text`

- **Заметка:** Action intake for Things or project

- **Вставить в поле текста:**

```text
# CAPTURE — TASK / ДЕЙСТВИЕ

Raw input:
[вставить]

Задача:
Проверь, является ли вход конкретным действием. Не выполняй задачу.

Extract only:
- action:
- object:
- where / tool:
- due date / time, if any:
- done when:
- blocker:
- route_candidate: Things / Calendar / Project / unclear
- project_candidate, if any:
- capture_status: ready_for_task / route_needed / unclear
- next_safe_action:

Rules:
- если нет глагола действия, не отправляй в Things;
- если есть жёсткая дата/время, пометь Calendar candidate;
- если задача проектная, нужен later handoff.
```


### K6 — `Meeting`

- **Действие:** `System → Text`

- **Заметка:** Calendar intake

- **Вставить в поле текста:**

```text
# CAPTURE — MEETING / CALENDAR

Raw input:
[вставить]

Задача:
Вытащи только данные для потенциального календарного события. Не создавай событие.

Extract only:
- event:
- date:
- time:
- duration:
- participants:
- location / link:
- preparation_needed:
- deadline_or_event: deadline / meeting / reminder / unclear
- calendar_readiness: ready / missing_details / unclear
- missing_details:
- next_safe_action:

Rules:
- если нет даты или времени, не называй событие готовым;
- если это действие без жёсткого времени, пометь Things candidate;
- используй даты в формате YYYY-MM-DD, если дата известна.
```


### K7 — `Metric`

- **Действие:** `System → Text`

- **Заметка:** Analytics metric intake

- **Вставить в поле текста:**

```text
# CAPTURE — METRIC / KPI

Raw input:
[вставить]

Задача:
Зафиксируй показатель или аналитический вопрос для [Analytics]. Не считай и не придумывай формулу.

Extract only:
- metric_name:
- business_question:
- period:
- grain:
- formula_if_known:
- source_if_known:
- currency / units:
- required_dimensions:
- owner_project: [Analytics]
- missing_data:
- capture_status: raw / normalized / route_needed
- next_safe_action:

Rules:
- deterministic calculation позже в [Analytics];
- если формула неизвестна, пиши formula_missing;
- не делай выводы без data contract.
```


### K8 — `Bug`

- **Действие:** `System → Text`

- **Заметка:** Bug / incident intake

- **Вставить в поле текста:**

```text
# CAPTURE — BUG / ERROR

Raw input:
[вставить]

Задача:
Зафиксируй ошибку или сбой. Не исправляй и не назначай root cause без evidence.

Extract only:
- what_failed:
- expected_behavior:
- actual_behavior:
- where_it_happened:
- steps_to_reproduce:
- impact:
- severity: low / medium / high / blocker / unclear
- likely_owner_project:
- logs_or_files_mentioned:
- missing_details:
- next_safe_action:

Rules:
- не проси raw logs/secrets в общий prompt;
- если нужен Codex, позже потребуется repo, files, checks, rollback;
- если severity blocker, пометь stop_or_escalate_candidate.
```


### K9 — `Risk`

- **Действие:** `System → Text`

- **Заметка:** Risk / weak signal intake

- **Вставить в поле текста:**

```text
# CAPTURE — RISK / WEAK SIGNAL

Raw input:
[вставить]

Задача:
Зафиксируй риск или слабый сигнал. Не превращай его в подтверждённую проблему без evidence.

Extract only:
- risk_signal:
- source / context:
- affected_area:
- possible_trigger:
- possible_impact:
- evidence_given:
- assumptions:
- severity: low / medium / high / unclear
- owner_project_candidate:
- monitoring_signal:
- next_safe_action:

Rules:
- risk != fact;
- не усиливай вероятность без данных;
- если требуется decision review, пометь owner_project_candidate: [Thinking].
```


### K10 — `Memo seed`

- **Действие:** `System → Text`

- **Заметка:** Memo seed intake

- **Вставить в поле текста:**

```text
# CAPTURE — MEMO SEED

Raw input:
[вставить]

Задача:
Зафиксируй заготовку будущей записки. Не пиши записку сейчас.

Extract only:
- memo_topic:
- audience:
- decision_or_question:
- period:
- key_facts_given:
- sections_needed:
- evidence_needed:
- limitations:
- owner_project_candidate: [Analytics] / [LLM] / [Thinking] / unclear
- capture_status: raw / normalized / route_needed
- next_safe_action:

Rules:
- memo без evidence остаётся seed;
- числа и таблицы должны прийти из [Analytics];
- стиль и финальная упаковка позже в [LLM].
```


### K11 — `Research`

- **Действие:** `System → Text`

- **Заметка:** Research topic intake

- **Вставить в поле текста:**

```text
# CAPTURE — RESEARCH SEED

Raw input:
[вставить]

Задача:
Зафиксируй тему исследования и границы. Не проводи исследование сейчас.

Extract only:
- research_topic:
- research_question:
- scope:
- freshness_needed: yes / no / unclear
- source_types_needed:
- avoid_list:
- expected_output:
- relevance_for_Sergey:
- owner_project_candidate: [AI OS] / [LLM] / [Thinking] / unclear
- missing_details:
- next_safe_action:

Rules:
- если тема про AI-релизы, модели, API, pricing, benchmark или market facts — freshness_needed: yes;
- не делай web claims внутри capture;
- сохраняй как seed для последующего routing.
```


### K12 — `Prompt seed`

- **Действие:** `System → Text`

- **Заметка:** Prompt / LLM workflow intake

- **Вставить в поле текста:**

```text
# CAPTURE — PROMPT SEED / LLM WORKFLOW

Raw input:
[вставить]

Задача:
Зафиксируй идею prompt, workflow или model routing для [LLM]. Не делай финальный prompt без quality gate.

Extract only:
- prompt_or_workflow_goal:
- task_type_candidate: draft / summarize / judge / revise / classify / extract / synthesize / orchestrate / route / eval / unclear
- input_requirements:
- desired_output:
- constraints:
- model_class_candidate: fast / reasoning / high-reasoning / local / judge / unclear
- quality_gate_needed:
- known_risks:
- owner_project: [LLM]
- next_safe_action:

Rules:
- не hardcode конкретную модель как постоянную истину;
- reusable prompt требует registry item;
- unsupported claims пометить как missing evidence.
```


### K13 — `Decision seed`

- **Действие:** `System → Text`

- **Заметка:** Candidate decision intake

- **Вставить в поле текста:**

```text
# CAPTURE — DECISION SEED / РЕШЕНИЕ-КАНДИДАТ

Raw input:
[вставить]

Задача:
Зафиксируй кандидат решения. Не отмечай его как принятое решение.

Extract only:
- decision_question:
- candidate_option:
- current_status: idea / candidate / discussed / unclear
- facts_given:
- assumptions:
- unknowns:
- blockers:
- owner_project: [Thinking]
- decision_readiness: not_ready / needs_options / needs_data / ready_for_review
- next_safe_action:

Rules:
- accepted decision может появиться только после review;
- если нужны числа или сценарии, пометь handoff_candidate: [Analytics];
- если нужна реализация, Codex только после accepted decision.
```


### K14 — `Route later`

- **Действие:** `System → Text`

- **Заметка:** Prepare material for later routing

- **Вставить в поле текста:**

```text
# CAPTURE — ROUTE LATER / TRIAGE PREP

Raw input:
[вставить]

Задача:
Подготовь материал к последующей маршрутизации. Не решай целевую задачу и не делай финальный handoff.

Extract only:
- normalized_summary:
- type_candidate:
- possible_destinations:
- why_unclear:
- blocking_questions: максимум 3
- facts_given:
- missing_details:
- capture_status: route_needed / ready_for_router / unclear
- suggested_router_button: Raw → Route / Things? / Calendar? / Analytics? / LLM? / Codex? / Clarify
- next_safe_action:

Rules:
- если route confidence weak, не открывай project;
- project handoff выполняется в папке МАРШРУТ;
- QA выполняется позже, если материал пойдёт в project / Codex / memo / KB.
```


### K15 — `Obsidian`

- **Действие:** `System → Website / Open`

- **Заметка:** Open Obsidian Inbox / AI OS capture note

- **Адрес или цель:**

```text
<OBSIDIAN_INBOX_URI>
```


## Экран: `ЗАПИСКА`
```text
┌────────────┬────────────┬────────────┬────────────┬────────────┐
│ ⬆ НАЗАД    │ Brief      │ Context    │ Facts      │ Structure  │
├────────────┼────────────┼────────────┼────────────┼────────────┤
│ Draft      │ Exec sum.  │ Risks      │ Actions    │ Limit.     │
├────────────┼────────────┼────────────┼────────────┼────────────┤
│ Evidence   │ To LLM     │ Memo QA    │ Final      │ Project    │
└────────────┴────────────┴────────────┴────────────┴────────────┘
```

Роль экрана: фабрика записок. Экран не делает расчёты и не придумывает факты. Правильный поток: `Brief → Context → Facts → Structure → Draft → Memo QA → Final`.

### K1 — `⬆ НАЗАД`

- **Действие:** `Navigation Back`

- **Заметка:** Не перепрограммировать

- **Оставить штатную кнопку возврата из папки.**

### K2 — `Brief`

- **Действие:** `System → Text`

- **Заметка:** Memo brief / постановка записки

- **Вставить в поле текста:**

```text
# ЗАПИСКА — BRIEF

Тема:
[указать]

Аудитория:
[руководитель / CFO / команда / личная база / другое]

Цель записки:
[решение / информирование / контроль / объяснение отклонений / предложение действий]

Период:
[YYYY-MM-DD / месяц / квартал / год / не применимо]

Источник контекста:
[Analytics / Thinking / AI OS / Research / другое]

Входные материалы:
[вставить кратко]

Ожидаемый output:
[executive memo / analytical memo / decision memo / status memo / QA note]

Ограничения:
- не придумывать факты;
- не усиливать вывод выше evidence;
- отделять факты, расчёт, интерпретацию, гипотезу и рекомендацию;
- если данных не хватает — указать missing evidence;
- не делать deterministic расчёты внутри memo;
- если нужны расчёты — handoff в [Analytics].

Верни строго:
- memo_type:
- audience:
- intended_use:
- decision/use:
- required_sections:
- required_inputs:
- missing_inputs:
- owner_project:
- routing_needed: yes / no
- next_step:
```

### K3 — `Context`

- **Действие:** `System → Text`

- **Заметка:** Curated context package

- **Вставить в поле текста:**

```text
# ЗАПИСКА — CONTEXT PACKAGE

Материалы:
[вставить]

Задача:
Собери compact context package для записки. Не пиши финальный memo. Не передавай raw dump дальше.

Раздели:
- DATA FACT:
- CALCULATION RESULT:
- INTERPRETATION:
- HYPOTHESIS:
- RECOMMENDATION:
- LIMITATION:
- MISSING EVIDENCE:
- UNSUPPORTED CLAIM:

Проверь:
- есть ли период у чисел;
- есть ли source / mart / file reference;
- не смешаны ли разные периоды;
- не названы ли гипотезы подтверждёнными причинами;
- какие claims нельзя использовать в memo.

Верни строго:
1. Memo question:
2. Audience:
3. Verified facts:
4. Reconciled numbers:
5. Source / mart / file references:
6. Open assumptions:
7. Unsupported claims:
8. What cannot be claimed:
9. Recommended memo structure:
10. Handoff needed:
11. Next step:
```

### K4 — `Facts`

- **Действие:** `System → Text`

- **Заметка:** Fact table / evidence inventory

- **Вставить в поле текста:**

```text
# ЗАПИСКА — FACT TABLE

Контекст / данные:
[вставить]

Задача:
Собери только проверенные факты для записки. Не делай выводы, причины и рекомендации.

Верни таблицу:
| Fact | Period | Source | Evidence status | Confidence | Limitation |
|---|---|---|---|---|---|

Отдельно:
- calculation_results:
- assumptions:
- hypotheses:
- unsupported_claims:
- facts_not_usable_yet:
- missing_sources:
- what_must_not_be_claimed:
```

### K5 — `Structure`

- **Действие:** `System → Text`

- **Заметка:** Memo structure / outline

- **Вставить в поле текста:**

```text
# ЗАПИСКА — STRUCTURE

Memo brief:
[вставить]

Curated context / facts:
[вставить]

Задача:
Спроектируй структуру записки под цель и аудиторию. Не пиши полный текст и не добавляй новые факты.

Выбери тип:
- executive memo;
- analytical memo;
- decision memo;
- status memo;
- QA note.

Собери структуру:
1. Title
2. Executive summary
3. Key facts
4. Analysis / interpretation
5. Risks
6. Recommendations / actions
7. Limitations
8. Evidence appendix

Для каждого раздела укажи:
| Section | Purpose | Inputs needed | Evidence required | What not to include |
|---|---|---|---|---|

Верни:
- memo_type:
- outline:
- required evidence:
- missing inputs:
- sections to omit:
- next step:
```

### K6 — `Draft`

- **Действие:** `System → Text`

- **Заметка:** First memo draft from curated context

- **Вставить в поле текста:**

```text
# ЗАПИСКА — DRAFT

Memo brief:
[вставить]

Curated context:
[вставить]

Задача:
Напиши черновик записки на основе только предоставленного context.

Структура:
1. Executive summary
2. Key facts
3. Analysis
4. Risks
5. Recommendations
6. Limitations
7. Evidence appendix

Правила:
- не добавляй новые факты;
- числа показывай с периодом и источником;
- причины называй гипотезами, если они не подтверждены;
- рекомендации делай только из facts / calculation results;
- риски указывай только с risk_basis;
- ограничения показывай явно;
- если evidence слабое — помечай это в тексте.

Верни строго:
- memo_draft:
- unsupported_claims:
- missing_evidence:
- weak_points:
- confidence:
- next_step:
```

### K7 — `Exec summary`

- **Действие:** `System → Text`

- **Заметка:** Executive summary from memo/facts

- **Вставить в поле текста:**

```text
# ЗАПИСКА — EXECUTIVE SUMMARY

Memo draft / facts:
[вставить]

Аудитория:
[указать]

Задача:
Собери короткое executive summary. Не добавляй новые факты, числа или причины.

Правила:
- сначала вывод, потом 2–4 ключевых факта;
- numbers before adjectives;
- причина = hypothesis, если не подтверждена;
- не обещай action без owner / due date / status;
- явно покажи limitation, если вывод неполный.

Верни:
1. Executive summary: 3–6 предложений
2. Key numbers:
3. Main risk:
4. Recommended action, if supported:
5. Limitation:
6. Confidence:
7. What not to claim:
```

### K8 — `Risks`

- **Действие:** `System → Text`

- **Заметка:** Memo risk section with basis

- **Вставить в поле текста:**

```text
# ЗАПИСКА — RISKS SECTION

Memo context / draft:
[вставить]

Задача:
Собери блок рисков для записки. Не добавляй риски без основания.

Для каждого риска укажи:
| Risk | Risk basis | Trigger | Impact | Evidence | Severity | Mitigation | Owner |
|---|---|---|---|---|---|---|---|

Проверь:
- риск подтверждён данными или это гипотеза;
- есть ли trigger;
- не перепутан ли риск с проблемой;
- не перепутана ли рекомендация с наблюдением.

Верни:
- publishable_risks:
- hypothesis_risks:
- unsupported_risks_to_remove:
- main_risk:
- mitigation_needed:
- confidence:
```

### K9 — `Actions`

- **Действие:** `System → Text`

- **Заметка:** Recommendations / action register

- **Вставить в поле текста:**

```text
# ЗАПИСКА — ACTIONS / RECOMMENDATIONS

Memo context / findings:
[вставить]

Задача:
Собери рекомендации и action register для записки. Не превращай наблюдения в действия.

Правила:
- action должен иметь owner / due date / status или быть помечен как proposed;
- recommendation должна следовать из facts / calculation results;
- не добавляй инициативы без evidence;
- если данных мало — предложи verification action.

Верни таблицу:
| Action | Why needed | Evidence | Owner | Due date | Status | Risk if skipped | Next check |
|---|---|---|---|---|---|---|---|

Отдельно:
- recommendations_supported:
- recommendations_to_defer:
- observations_not_actions:
- missing_owners:
- confidence:
```

### K10 — `Limitations`

- **Действие:** `System → Text`

- **Заметка:** Limitations and forbidden claims

- **Вставить в поле текста:**

```text
# ЗАПИСКА — LIMITATIONS / WHAT NOT TO CLAIM

Memo draft / context:
[вставить]

Задача:
Определи ограничения записки и claims, которые нельзя публиковать.

Проверь:
- missing evidence;
- mixed periods;
- unreconciled numbers;
- unclear source / mart;
- hypothesis stated as cause;
- risk without risk_basis;
- action without owner / due date / status;
- stale facts requiring fresh check;
- unsupported recommendations.

Верни строго:
1. Limitations:
2. Unsupported claims:
3. Claims allowed as DATA FACT:
4. Claims allowed as CALCULATION RESULT:
5. Claims allowed only as HYPOTHESIS:
6. Claims to remove:
7. Required QA before final:
8. Publication status: allowed / revise / blocked
9. Next step:
```

### K11 — `Evidence`

- **Действие:** `System → Text`

- **Заметка:** Evidence appendix

- **Вставить в поле текста:**

```text
# ЗАПИСКА — EVIDENCE APPENDIX

Memo draft / facts / sources:
[вставить]

Задача:
Собери evidence appendix для записки. Не делай новый анализ.

Верни таблицу:
| Claim in memo | Evidence source | Period | Evidence status | Confidence | Limitation | Appendix note |
|---|---|---|---|---|---|---|

Отдельно:
- claims_without_evidence:
- weak_evidence_claims:
- source_gaps:
- fresh_check_needed:
- what_to_remove_before_final:
- evidence_readiness: pass / revise / blocked:
```

### K12 — `To LLM`

- **Действие:** `System → Text`

- **Заметка:** Memo → [LLM] handoff

- **Вставить в поле текста:**

```text
# ЗАПИСКА → [LLM] HANDOFF

От:
[Analytics / Thinking / AI OS / Research / Memo]

Кому:
[LLM]

Тип задачи:
[memo draft / memo revise / executive summary / style edit / memo QA]

Goal:
[описать]

Curated context:
[только проверенные факты, расчёты, ограничения]

Do not pass:
- raw dump;
- неподтверждённые claims как facts;
- secrets / .env / private data без разрешения;
- расчёты без QA;
- выводы сильнее evidence;
- новые факты без источника.

Expected output:
[описать]

Acceptance criteria:
- facts / interpretation / recommendation separated;
- unsupported claims listed;
- limitations visible;
- style improved but meaning not amplified;
- no new facts added.

Risks:
Evidence / confidence:
Open questions:
Next step:
```

### K13 — `Memo QA`

- **Действие:** `System → Text`

- **Заметка:** Memo-specific judge gate

- **Вставить в поле текста:**

```text
# ЗАПИСКА — MEMO QA / JUDGE

Memo draft:
[вставить]

Brief / intended use:
[вставить]

Проверь:
- отвечает ли memo цели и аудитории;
- есть ли executive summary;
- отделены ли facts / calculation results / interpretation / hypothesis / recommendation;
- есть ли unsupported claims;
- не смешаны ли периоды;
- не названы ли гипотезы подтверждёнными причинами;
- есть ли risk_basis для рисков;
- есть ли owner / due date / status у действий;
- видны ли limitations;
- есть ли evidence appendix;
- можно ли передавать руководителю / сохранять.

Верни строго:
QA verdict: pass / revise / blocked
Reason:
Unsupported claims:
Period issues:
Overclaimed causes:
Missing evidence:
Weak recommendations:
Required revision:
Final readiness:
Approved next step:
```

### K14 — `Final`

- **Действие:** `System → Text`

- **Заметка:** Final memo record

- **Вставить в поле текста:**

```text
# ЗАПИСКА — FINAL MEMO

Revised memo:
[вставить]

QA result:
[вставить]

Задача:
Собери финальную версию записки. Не добавляй новые факты после QA.

Верни строго:
1. Title:
2. Date:
3. Audience:
4. Status: draft / reviewed / approved / blocked
5. Executive summary:
6. Key facts:
7. Analysis:
8. Risks:
9. Recommendations:
10. Limitations:
11. Evidence appendix:
12. Open questions:
13. Next review trigger:
14. Save / handoff recommendation:
15. Confidence:
16. What not to claim:
```

### K15 — `Project`

- **Действие:** `System → Website`

- **Заметка:** Открыть целевой проект для memo / LLM work

- **Адрес или цель:**

```text
<CHATGPT_LLM_PROJECT_URL>
```

## Экран: `ПОИСК`

```text
┌────────────┬────────────┬────────────┬────────────┬────────────┐
│ ⬆ НАЗАД    │ Brief      │ Sources    │ AI tools   │ Workflow   │
├────────────┼────────────┼────────────┼────────────┼────────────┤
│ Compare    │ Hype?      │ Score      │ Gemini DR  │ Perplexity │
├────────────┼────────────┼────────────┼────────────┼────────────┤
│ YouTube    │ GitHub     │ Backlog    │ To AI OS   │ Research QA │
└────────────┴────────────┴────────────┴────────────┴────────────┘
```

Роль экрана: внешний разведчик источников, workflows, AI-инструментов и repos с anti-hype фильтром. Research выдаёт candidate evidence, а не финальную истину. Решения — в `[Thinking]`, расчёты — в `[Analytics]`, prompt/workflow — в `[LLM]`, evidence/KB — в `[AI OS]`, реализация — в `[Codex]` только после gate.

### K1 — `⬆ НАЗАД`

- **Действие:** `штатный возврат из папки`

- **Заметка:** Built-in folder back; не перепрограммировать

- **Оставить штатную кнопку возврата из папки.**

### K2 — `Brief`

- **Действие:** `Text`

- **Заметка:** Research brief: topic, scope, criteria, freshness, output

- **Вставить в поле текста:**

```text
# ПОИСК — RESEARCH BRIEF

Сырая тема / вопрос:
[вставить]

Задача:
Сформулируй исследовательское ТЗ. Не ищи источники и не делай финальный вывод. Нужно подготовить точный brief для внешнего поиска / Gemini / Perplexity / YouTube / GitHub.

Правила:
- не превращай тему в рекомендацию;
- не выдумывай факты, цены, лимиты, даты и benchmarks;
- отделяй known facts от assumptions;
- укажи, какие claims требуют fresh check;
- цель Research — найти candidate evidence / workflows / tools, а не принять решение.

Верни строго:
Research question:
Background / known facts:
Assumptions:
Scope in:
Scope out:
Must-have criteria:
Avoid / reject:
Freshness requirement: needed / not needed / unknown
Source types to search:
Output format:
Scoring rubric:
Owner project candidate: [AI OS] / [Thinking] / [Analytics] / [LLM] / [Codex] / unclear
Success criteria:
Next step:
```

### K3 — `Sources`

- **Действие:** `Text`

- **Заметка:** Source inventory: what supports what, limits, use/verify/reject

- **Вставить в поле текста:**

```text
# ПОИСК — SOURCE MAP / INVENTORY

Тема / research brief / найденные источники:
[вставить]

Задача:
Собери карту источников. Источник — это кандидат на evidence, а не готовый факт.

Проверь:
- тип источника: official docs / paper / repo / demo / article / video / vendor / forum / listicle;
- дату / freshness;
- что именно источник поддерживает;
- ограничения и bias;
- есть ли первоисточник;
- какие claims требуют повторной проверки.

Верни строго:
Source map:
| Source | Type | Date / freshness | What it supports | Evidence strength: strong/medium/weak | Limitation / bias | Action: use/verify/reject |
|---|---|---|---|---|---|---|
Strongest sources:
Weak / risky sources:
Missing source types:
Claims safe to carry forward:
Claims requiring verification:
Claims to reject:
Recommended next search:
Routing:
```

### K4 — `AI tools`

- **Действие:** `Text`

- **Заметка:** AI tool scan with use case, freshness, privacy, integration risk

- **Вставить в поле текста:**

```text
# ПОИСК — AI TOOL SCAN

Инструмент / категория / задача:
[вставить]

Задача:
Оцени AI-инструмент или группу инструментов как candidate для работы Сергея. Не делай покупочную рекомендацию без свежей проверки цен, лимитов, условий и доступности.

Проверь:
- use case;
- кто получает пользу;
- входы / выходы;
- setup complexity;
- data privacy / client data risk;
- vendor lock-in;
- API / pricing / limit freshness;
- альтернативы;
- применимость к аудиту, аналитике, memo, routing, QA или Codex workflow.

Верни строго:
Tool / category:
Primary use case:
Value for Sergey:
Input data needed:
Output artifact:
Setup complexity: low / medium / high
Freshness check needed: yes / no
Privacy / data risk:
Integration risk:
Alternatives to compare:
Evidence found / needed:
Hype risk: low / medium / high
Recommendation status: explore / verify / reject / backlog
Owner project:
Next step:
```

### K5 — `Workflow`

- **Действие:** `Text`

- **Заметка:** Find repeatable workflow, not generic news or opinion

- **Вставить в поле текста:**

```text
# ПОИСК — WORKFLOW HUNT

Тема / задача / источник:
[вставить]

Задача:
Найди или извлеки повторяемый порядок работы. Ценность — не в новости, а в reproducible workflow с входами, шагами, выходом и проверкой качества.

Ищи:
- concrete steps;
- tools used;
- input data / prompt / files;
- output artifact;
- quality check;
- repeatability;
- limitations;
- применимость для Сергея.

Отбраковывай:
- мнения без demo;
- новости без workflow;
- listicles;
- pure promotion;
- claims без source trail.

Верни строго:
Workflow name:
Problem solved:
Inputs:
Steps:
Tools:
Output artifact:
Quality check:
Repeatability: high / medium / low
Evidence/source:
Adaptation for Sergey:
Risks / limits:
Owner project candidate:
Next safe step:
```

### K6 — `Compare`

- **Действие:** `Text`

- **Заметка:** Compare options with criteria and no unsupported winner

- **Вставить в поле текста:**

```text
# ПОИСК — COMPARE OPTIONS

Что сравнить:
[вставить]

Контекст применения:
[вставить]

Задача:
Сравни инструменты, источники, workflows или подходы. Не выбирай победителя сильнее, чем позволяет evidence.

Критерии:
- fit to task;
- evidence quality;
- operational depth;
- freshness;
- privacy / data risk;
- setup complexity;
- repeatability;
- cost / pricing freshness, если применимо;
- Sergey relevance;
- hype risk.

Верни строго:
Comparison scope:
Options compared:
| Option | Best use | Evidence | Freshness | Setup | Risk | Sergey relevance | Hype risk | Verdict |
|---|---|---|---|---|---|---|---|---|
Best option if evidence holds:
Why not alternatives:
What requires fresh check:
Unsupported claims:
Decision status: explore / verify / defer / reject
Handoff target:
Next step:
```

### K7 — `Hype?`

- **Действие:** `Text`

- **Заметка:** Ad, affiliate, sponsored, vague claim, benchmark-without-method detector

- **Вставить в поле текста:**

```text
# ПОИСК — HYPE / AD / BIAS CHECK

Источник / инструмент / claim:
[вставить]

Задача:
Проверь, нет ли рекламы, affiliate bias, vendor bias, hype или неподтверждённых обещаний. Не спорь ради спора; отдели полезное зерно от маркетинговой шелухи.

Red flags:
- sponsored / affiliate / vendor bias;
- vague claims;
- no demo;
- no source trail;
- benchmark without method;
- “10 tools” listicle;
- no limitations;
- cherry-picked examples;
- pricing / availability claims without date;
- “must-have / game changer” without evidence.

Верни строго:
Hype verdict: low / medium / high
Bias type:
Supported parts:
Unsupported / exaggerated claims:
Missing evidence:
What can be reused safely:
What must not be claimed:
Usefulness: use / verify / reject / backlog
Safer source needed:
Routing:
Next step:
```

### K8 — `Score`

- **Действие:** `Text`

- **Заметка:** Research scorecard 1–5 with hype risk and Sergey relevance

- **Вставить в поле текста:**

```text
# ПОИСК — RESEARCH SCORECARD

Источник / инструмент / workflow / repo:
[вставить]

Задача:
Оцени research-кандидата по rubric. Не превращай score в финальное решение; это фильтр, а не verdict истины.

Оцени 1–5:
- signal score;
- operational depth;
- novelty;
- practicality;
- evidence quality;
- freshness;
- repeatability;
- Sergey relevance;
- privacy / security risk, где 5 = безопаснее;
- hype risk, где 5 = низкий hype.

Верни строго:
Scorecard:
| Criterion | Score 1-5 | Reason | Evidence / limitation |
|---|---:|---|---|
Total / interpretation:
Keep / verify / reject:
Main reason:
Main risk:
Missing evidence:
Best owner project:
Next step:
```

### K9 — `Gemini DR`

- **Действие:** `Text`

- **Заметка:** Deep Research package for Gemini: broad source/workflow discovery

- **Вставить в поле текста:**

```text
# ПОИСК — GEMINI DEEP RESEARCH PACKAGE

Тема:
[вставить]

Задача:
Подготовь prompt-пакет для Gemini Deep Research. Цель — найти повторяемые workflows, сильные источники, AI-инструменты, repos или практики, а не собрать generic AI news.

Скопируй и используй как research brief:

Topic:
[вставить]

Research objective:
Find practical, repeatable workflows / tools / sources relevant to Sergey’s work in audit, financial analytics, memo generation, AI governance, prompt workflows, routing, QA, or Codex handoff.

Scope in:
- workflow demos;
- official docs;
- GitHub repos;
- deep articles with reproducible steps;
- comparison with evidence;
- current tools only if date/source is clear.

Scope out:
- generic news;
- pricing-only comparisons;
- shallow “top 10 tools” lists;
- pure opinions;
- clickbait;
- unsupported vendor claims;
- no-demo videos.

Must-have criteria:
- source trail;
- concrete steps;
- input/output artifact;
- quality check;
- repeatability;
- limitations;
- relevance to Sergey.

Scoring rubric:
- signal score;
- operational depth;
- novelty;
- practicality;
- evidence quality;
- hype risk;
- Sergey relevance.

Output schema:
1. Executive summary.
2. Source list with dates and source types.
3. Workflow candidates table.
4. Tool / repo candidates table.
5. Unsupported or weak claims.
6. Anti-patterns / hype detected.
7. Top 3 candidates for AI OS ingestion.
8. What requires fresh verification.
9. Recommended handoff target.

Return:
Gemini prompt:
[готовый текст для копирования]
Expected output:
Acceptance criteria:
How to QA the result:
```

### K10 — `Perplexity`

- **Действие:** `Text`

- **Заметка:** Fast source scout: current sources, dates, claims, verification needs

- **Вставить в поле текста:**

```text
# ПОИСК — PERPLEXITY SOURCE SCOUT

Тема / вопрос:
[вставить]

Задача:
Подготовь короткий prompt для Perplexity как быстрого разведчика источников. Не проси финальную рекомендацию без evidence scoring.

Скопируй и используй:

Find current, credible sources for:
[topic]

Return:
- 5–10 sources;
- source type: official docs / paper / repo / article / video / forum / vendor;
- publication or update date;
- claim each source supports;
- why the source is credible or risky;
- what needs verification;
- conflicts between sources;
- links / source names.

Rules:
- prioritize primary sources;
- mark vendor claims separately;
- do not treat listicles as strong evidence;
- do not provide final recommendation without source scoring;
- flag stale pricing, API limits, model capabilities and benchmarks.

Верни:
Perplexity prompt:
Expected output:
Source quality criteria:
How to route results:
Research QA checklist:
```

### K11 — `YouTube`

- **Действие:** `Text`

- **Заметка:** Find workflow demos, not opinions, news or shallow reviews

- **Вставить в поле текста:**

```text
# ПОИСК — YOUTUBE WORKFLOW DISCOVERY

Тема / workflow:
[вставить]

Задача:
Подготовь запрос для поиска YouTube-роликов, где показывают workflow-demo. Не ищи мнения, новости и поверхностные обзоры.

Ищи видео, где автор показывает:
- конкретный workflow;
- экран / demo;
- входные данные;
- шаги;
- инструменты;
- output artifact;
- quality check;
- repeatability.

Reject:
- opinion videos;
- news;
- shallow reviews;
- no demo;
- pure promotion;
- “top tools” without workflow;
- claims without examples.

Верни строго:
Search query ideas:
Selection criteria:
Reject criteria:
Extraction schema:
| Video / channel | Workflow shown | Inputs | Output artifact | Quality check | Evidence strength | Hype risk | Relevance |
|---|---|---|---|---|---|---|---|
What to capture for AI OS:
What not to claim:
Next step:
```

### K12 — `GitHub`

- **Действие:** `Text`

- **Заметка:** Repo scout: README, activity, tests, examples, security, fit

- **Вставить в поле текста:**

```text
# ПОИСК — GITHUB / REPO SCOUT

Repo / тема / задача:
[вставить]

Задача:
Оцени GitHub repo как candidate source / tool / implementation reference. Stars are signal, not proof.

Проверь:
- purpose;
- last activity;
- README quality;
- install / quickstart;
- examples;
- tests;
- issues / maintenance;
- license;
- security / privacy risks;
- dependency risk;
- fit for Sergey;
- suitability for Codex handoff.

Верни строго:
Repo:
Purpose:
Last activity / freshness:
README / docs quality:
Examples:
Tests / CI:
Maintenance signals:
Security / privacy risks:
License / usage constraints:
Fit for Sergey:
Use as: source / pattern / tool candidate / reject
Need Codex? yes / no / later
Unsupported claims:
Next step:
```

### K13 — `Backlog`

- **Действие:** `Text`

- **Заметка:** Research backlog card: defer without losing signal

- **Вставить в поле текста:**

```text
# ПОИСК — RESEARCH BACKLOG ITEM

Тема / источник / идея:
[вставить]

Задача:
Оформи research backlog item. Используй, когда тема потенциально полезна, но сейчас нет времени, evidence слабое или fresh check нужен позже.

Верни строго:
Backlog item:
Research question:
Why it may matter:
Current evidence: none / weak / mixed / promising
Fresh check needed: yes / no
Potential owner project:
Trigger to revisit:
Minimum sources needed:
Expected output if researched:
Risk if ignored:
Risk if acted on now:
Next safe action:
```

### K14 — `To AI OS`

- **Действие:** `Text`

- **Заметка:** Research → AI OS handoff for evidence/pattern ingestion

- **Вставить в поле текста:**

```text
# ПОИСК → [AI OS] HANDOFF

Research output / sources / workflow candidates:
[вставить]

Задача:
Подготовь handoff в [AI OS] для evidence check, pattern candidate, source map или anti-pattern. Не превращай weak evidence в KB fact.

Передавать только curated context:
- topic;
- source list;
- supported claims;
- weak / unsupported claims;
- workflow candidates;
- anti-patterns;
- freshness status;
- limitations;
- recommended KB action.

Не передавать:
- raw dump;
- long transcript;
- secrets / API keys / .env;
- source-card dumps;
- unsupported claims as facts;
- production-ready recommendation.

Верни строго:
Handoff to: [AI OS]
Task type: evidence / pattern candidate / source map / anti-pattern / review item
Topic:
Candidate sources:
Supported claims:
Weak / unsupported claims:
Workflow candidates:
Anti-patterns / hype detected:
Fresh check status:
Confidence:
What not to claim:
Recommended KB action:
Acceptance criteria for AI OS:
Next step:
```

### K15 — `Research QA`

- **Действие:** `Text`

- **Заметка:** Final gate: research output pass/revise/blocked before handoff

- **Вставить в поле текста:**

```text
# ПОИСК — RESEARCH QA GATE

Research output / source map / comparison:
[вставить]

Intended use:
AI OS ingestion / LLM prompt / Thinking decision / Analytics spec / Codex task / personal backlog / other

Задача:
Проверь research-result как @judge. Research не должен выдавать candidate evidence как final truth.

Проверь:
- есть ли research question;
- источники перечислены;
- source types и dates указаны, где важно;
- supported / weak / unsupported claims разделены;
- hype / vendor bias проверен;
- freshness risks видны;
- recommendations не сильнее evidence;
- routing корректен;
- нет premature Codex / production handoff;
- есть next safe step.

Верни строго:
QA verdict: pass / revise / blocked
Reason:
Unsupported claims:
Weak evidence:
Freshness gaps:
Hype / bias risk:
Wrong routing:
Missing sources:
Required fix:
Approved handoff target:
Approved next step:
```


## Экран: `РЕПО`

```text
┌────────────┬────────────┬────────────┬────────────┬────────────┐
│ ⬆ НАЗАД    │ AI-OS      │ README     │ Манифест   │ Маршрут    │
├────────────┼────────────┼────────────┼────────────┼────────────┤
│ Правила    │ Сверка     │ Проверки   │ Статус     │ Запросы    │
├────────────┼────────────┼────────────┼────────────┼────────────┤
│ Задачи     │ Пакеты     │ Прогоны    │ Пути       │ Безопасн.  │
└────────────┴────────────┴────────────┴────────────┴────────────┘
```

### K1 — `⬆ НАЗАД`

- **Действие:** `штатный возврат из папки`

- **Оставить штатную кнопку возврата из папки.**

### K2 — `AI-OS`

- **Действие:** `System → Website`

- **Адрес или цель:**

```text
https://github.com/sergstack/AI-OS
```

### K3 — `README`

- **Действие:** `System → Website`

- **Адрес или цель:**

```text
https://github.com/sergstack/AI-OS/blob/main/README.md
```

### K4 — `Манифест`

- **Действие:** `System → Website`

- **Адрес или цель:**

```text
https://github.com/sergstack/AI-OS/blob/main/MANIFEST.json
```

### K5 — `Маршрут`

- **Действие:** `System → Website`

- **Адрес или цель:**

```text
https://github.com/sergstack/AI-OS/blob/main/ChatGPT/%5BAI%20OS%5D/Knowledge/PROJECT_ROUTING.md
```

### K6 — `Правила`

- **Действие:** `System → Website`

- **Адрес или цель:**

```text
https://github.com/sergstack/AI-OS/blob/main/ChatGPT/%5BAI%20OS%5D/Knowledge/GOVERNANCE_RULES.md
```

### K7 — `Сверка`

- **Действие:** `System → Website`

- **Адрес или цель:**

```text
https://github.com/sergstack/AI-OS/blob/main/CHATGPT_PROJECT_SYNC_CHECKLIST.md
```

### K8 — `Проверки`

- **Действие:** `System → Text`

- **Заметка:** Вставить в терминал, Enter вручную

- **Вставить в поле текста:**

```bash
cd <LOCAL_AI_OS_ROOT>
python3 scripts/check_project_instructions_length.py
python3 scripts/check_repo_public_safety.py
python3 scripts/check_manifest_paths.py
python3 scripts/check_knowledge_bundles.py
```

### K9 — `Статус`

- **Действие:** `System → Text`

- **Заметка:** Вставить в терминал, Enter вручную

- **Вставить в поле текста:**

```bash
cd <LOCAL_AI_OS_ROOT>
git status --short
git diff --stat
```

### K10 — `Запросы`

- **Действие:** `System → Website`

- **Адрес или цель:**

```text
https://github.com/sergstack/AI-OS/pulls
```

### K11 — `Задачи`

- **Действие:** `System → Website`

- **Адрес или цель:**

```text
https://github.com/sergstack/AI-OS/issues
```

### K12 — `Пакеты`

- **Действие:** `System → Website`

- **Адрес или цель:**

```text
https://github.com/sergstack/AI-OS/tree/main/Knowledge_Bundles
```

### K13 — `Прогоны`

- **Действие:** `System → Website`

- **Адрес или цель:**

```text
https://github.com/sergstack/AI-OS/blob/main/PILOT_CASES.md
```

### K14 — `Пути`

- **Действие:** `System → Text`

- **Вставить в поле текста:**

```text
В публичных документах нельзя использовать сырые абсолютные локальные пути.

Используй:
<LOCAL_AI_OS_ROOT>
<LOCAL_REPO_ROOT>
<LOCAL_CODEX_APP_ROOT>
<LOCAL_ARTIFACTS_ROOT>
```

### K15 — `Безопасн.`

- **Действие:** `System → Text`

- **Вставить в поле текста:**

```text
# ПРОВЕРКА БЕЗОПАСНОСТИ РЕПОЗИТОРИЯ

Проверь:
- нет .env;
- нет секретов;
- нет ключей доступа;
- нет сырых журналов;
- нет служебных файлов выполнения;
- нет векторной базы;
- нет сырых локальных путей;
- нет архивов как источников знаний.

Вердикт: принято / доработать / заблокировано
```

## Экран: `ПРОГОНЫ`

```text
┌────────────┬────────────┬────────────┬────────────┬────────────┐
│⬆ НАЗАД     │Brief       │Hypothesis  │Test case   │Run log     │
├────────────┼────────────┼────────────┼────────────┼────────────┤
│Result      │QA          │Lessons     │Decision    │Backlog     │
├────────────┼────────────┼────────────┼────────────┼────────────┤
│Scale?      │To Codex    │Card        │Сверка      │Сводка      │
└────────────┴────────────┴────────────┴────────────┴────────────┘
```

Роль экрана: маленькие безопасные проверки workflow перед масштабированием, автоматизацией или добавлением новых кнопок. Pilot не является production-ready доказательством и не заменяет QA / Thinking / Analytics / Codex.

### K1 — `⬆ НАЗАД`

- **Действие:** `штатный возврат из папки`

- **Заметка:** Не перепрограммировать

- **Оставить штатную кнопку возврата из папки.**

### K2 — `Brief`

- **Действие:** `System → Text`

- **Заметка:** Постановка pilot: что проверяем и зачем

- **Вставить в поле текста:**

```text
# ПРОГОНЫ — PILOT BRIEF

Тема / workflow / идея для проверки:
[вставить]

Задача:
Подготовь маленький безопасный pilot. Не решай всю задачу, не строй production-фабрику и не передавай в Codex до результата pilot.

Зафиксируй:
- hypothesis: что хотим проверить;
- owner project: [AI OS] / [Thinking] / [Analytics] / [LLM] / [Codex] / Memo / Research / другое;
- test scope: что входит;
- out of scope: что НЕ проверяем;
- input sample: минимальный вход;
- expected output: что должно получиться;
- success criteria;
- failure criteria;
- timebox / effort limit;
- QA gate after run;
- decision options: adopt / revise / automate / archive / reject.

Верни строго:
Pilot name:
Hypothesis:
Why this pilot matters:
Owner project:
Scope:
Out of scope:
Minimal test case:
Expected output:
Success criteria:
Failure criteria:
Risks:
Stop condition:
Next step:
```

### K3 — `Hypothesis`

- **Действие:** `System → Text`

- **Заметка:** Проверяемая гипотеза перед прогоном

- **Вставить в поле текста:**

```text
# ПРОГОНЫ — HYPOTHESIS

Идея / наблюдение:
[вставить]

Задача:
Преврати идею в проверяемую pilot-гипотезу. Не доказывай её текстом; определи, как её можно проверить маленьким прогоном.

Проверь:
- claim: что предполагаем;
- why it matters;
- assumptions;
- evidence available;
- missing evidence;
- observable signals;
- disconfirming signals: что покажет, что гипотеза неверна;
- decision impact: что изменится после проверки.

Верни строго:
Hypothesis:
Assumptions:
Evidence available:
Missing evidence:
Test signal:
Disconfirming signal:
Risk if false:
Decision after test:
Minimal pilot needed:
Next step:
```

### K4 — `Test case`

- **Действие:** `System → Text`

- **Заметка:** Мини-кейс для проверки workflow

- **Вставить в поле текста:**

```text
# ПРОГОНЫ — TEST CASE

Pilot hypothesis / brief:
[вставить]

Задача:
Спроектируй минимальный test case для pilot. Он должен быть достаточно маленьким, чтобы выполнить руками, но достаточно показательным, чтобы проверить workflow.

Определи:
- input data / prompt / source;
- steps to run;
- expected intermediate outputs;
- expected final output;
- tools / folders to use;
- QA checks;
- stop conditions;
- what not to do.

Верни строго:
Test case name:
Input:
Preconditions:
Steps:
Expected intermediate outputs:
Expected final output:
QA checks:
Stop conditions:
Out of scope:
Run-ready: yes / no
Missing items:
Next step:
```

### K5 — `Run log`

- **Действие:** `System → Text`

- **Заметка:** Фиксация фактического выполнения pilot

- **Вставить в поле текста:**

```text
# ПРОГОНЫ — RUN LOG

Pilot brief / test case:
[вставить]

Фактический прогон:
[вставить что было сделано]

Задача:
Зафиксируй фактический ход pilot. Не улучшай результат задним числом и не исправляй workflow внутри run log.

Раздели:
- planned steps;
- actually performed steps;
- deviations;
- outputs produced;
- errors / friction;
- evidence collected;
- time / effort, если известно;
- notes for QA.

Верни строго:
Pilot name:
Planned steps:
Actual steps:
Deviations:
Outputs:
Errors / friction:
Evidence:
Time / effort:
Immediate observations:
Do not conclude yet:
Next step:
```

### K6 — `Result`

- **Действие:** `System → Text`

- **Заметка:** Результат pilot без преждевременного масштабирования

- **Вставить в поле текста:**

```text
# ПРОГОНЫ — RESULT

Pilot brief:
[вставить]

Run log:
[вставить]

Задача:
Сравни ожидаемый и фактический результат pilot. Не превращай один удачный прогон в production-ready вывод.

Проверь:
- success criteria met / not met;
- failure criteria triggered / not triggered;
- actual output quality;
- evidence strength;
- residual risks;
- whether another run is needed.

Верни строго:
Pilot result: pass / partial / fail / blocked
Expected vs actual:
Success criteria status:
Failure criteria status:
Evidence strength: strong / medium / weak
What worked:
What failed:
Residual risks:
Need another run: yes / no
Recommended decision: adopt / revise / automate / archive / reject
Next step:
```

### K7 — `QA`

- **Действие:** `System → Text`

- **Заметка:** Judge-проверка pilot-output

- **Вставить в поле текста:**

```text
# ПРОГОНЫ — PILOT QA / JUDGE

Pilot result:
[вставить]

Задача:
Проверь как @judge, можно ли доверять результату pilot. Pilot проверяет workflow, а не доказывает production-readiness.

Проверь:
- была ли гипотеза явной;
- был ли test case достаточно маленьким и релевантным;
- не расширился ли scope;
- есть ли evidence результата;
- не сделан ли вывод сильнее одного прогона;
- видны ли failure modes;
- есть ли честный next decision;
- не отправляется ли преждевременно в Codex / production.

Верни строго:
QA verdict: pass / revise / blocked
Reason:
Unsupported conclusions:
Scope creep:
Missing evidence:
Main failure mode:
Required fix:
Approved decision:
Approved next step:
```

### K8 — `Lessons`

- **Действие:** `System → Text`

- **Заметка:** Уроки и улучшения после pilot

- **Вставить в поле текста:**

```text
# ПРОГОНЫ — LESSONS LEARNED

Pilot result / QA:
[вставить]

Задача:
Извлеки уроки из pilot. Не переписывай историю и не усиливай вывод выше evidence.

Верни:
What worked:
What did not work:
What was unnecessary:
What was missing:
Workflow changes needed:
Prompt/button changes needed:
QA changes needed:
Documentation changes needed:
Risks discovered:
Reusable pattern candidate:
Anti-pattern discovered:
Next step:
```

### K9 — `Decision`

- **Действие:** `System → Text`

- **Заметка:** Решение по судьбе pilot

- **Вставить в поле текста:**

```text
# ПРОГОНЫ — PILOT DECISION

Pilot result / QA / lessons:
[вставить]

Задача:
Прими операционное решение по pilot. Не принимай стратегическое решение шире evidence; если нужен выбор вариантов — передай в [Thinking].

Варианты решения:
- adopt: оставить как ручной workflow;
- revise: доработать и прогнать ещё раз;
- automate: готовить gated handoff в [Codex];
- archive: сохранить как опыт, не развивать сейчас;
- reject: отказаться от идеи.

Верни строго:
Decision: adopt / revise / automate / archive / reject
Why:
Evidence used:
Confidence: strong / medium / weak
What changes before reuse:
Owner project:
Acceptance criteria:
Revisit trigger:
Handoff needed: none / [Thinking] / [Analytics] / [LLM] / [Codex] / [AI OS]
Next step:
```

### K10 — `Backlog`

- **Действие:** `System → Text`

- **Заметка:** Отложенный item по результату pilot

- **Вставить в поле текста:**

```text
# ПРОГОНЫ — BACKLOG ITEM

Pilot lesson / decision:
[вставить]

Задача:
Оформи отложенную задачу или улучшение после pilot. Не делай production-задачу без acceptance criteria.

Верни строго:
Backlog item:
Source pilot:
Problem / opportunity:
Proposed change:
Owner project:
Priority: low / medium / high
Evidence strength: strong / medium / weak
Acceptance criteria:
Risks:
Dependencies:
Not now because:
Next review trigger:
Next step:
```

### K11 — `Scale?`

- **Действие:** `System → Text`

- **Заметка:** Проверка: масштабировать, автоматизировать или оставить руками

- **Вставить в поле текста:**

```text
# ПРОГОНЫ — SCALE / AUTOMATE GATE

Pilot decision:
[вставить]

Задача:
Оцени, стоит ли масштабировать pilot в методику, отдельную папку Stream Deck, фабрику или Codex-автоматизацию.

Проверь критерии:
- repeatability: будет ли повторяться;
- frequency: как часто нужно;
- impact: польза;
- risk: цена ошибки;
- manual effort saved;
- complexity of automation;
- evidence strength;
- reversibility;
- owner readiness.

Верни:
Scale verdict: keep manual / revise workflow / create method / create Stream Deck screen / automate with Codex / reject
Rationale:
Criteria table:
Minimum viable next version:
What not to automate:
Required QA before scaling:
Handoff target:
Next step:
```

### K12 — `To Codex`

- **Действие:** `System → Text`

- **Заметка:** Gated handoff в Codex после успешного pilot

- **Вставить в поле текста:**

```text
# ПРОГОНЫ → [Codex] HANDOFF / GATED

Pilot decision:
[вставить]

ВНИМАНИЕ:
Использовать только если pilot decision = automate или есть явно принятое решение на изменение файлов / tooling. Не передавать в Codex слабую гипотезу как requirement.

Подготовь handoff:
Handoff to: [Codex]
Task type: implementation / docs / tests / tooling / automation
Goal:
Accepted pilot evidence:
Scope:
Files to inspect:
Files allowed to change:
Forbidden actions:
Expected output:
Checks / smoke tests:
Acceptance criteria:
Rollback / stop condition:
Residual risks:
Open questions:
Suggested first step:
```

### K13 — `Card`

- **Действие:** `System → Text`

- **Заметка:** Карточка pilot для PILOT_CASES.md / журнала прогонов

- **Вставить в поле текста:**

```text
# ПРОГОНЫ — PILOT CARD / RECORD

Материалы pilot:
[вставить brief, result, QA, decision]

Задача:
Собери компактную карточку pilot для журнала прогонов. Не добавляй новых выводов.

Верни строго:
pilot_id:
date: YYYY-MM-DD
title:
owner_project:
hypothesis:
test_case:
result: pass / partial / fail / blocked
qa_verdict: pass / revise / blocked
decision: adopt / revise / automate / archive / reject
evidence_strength: strong / medium / weak
lessons:
changes_needed:
risks:
next_step:
link_or_location:
```

### K14 — `Сверка`

- **Действие:** `System → Website`

- **Заметка:** Сверка проекта / документации после pilot

- **Адрес или цель:**

```text
https://github.com/sergstack/AI-OS/blob/main/CHATGPT_PROJECT_SYNC_CHECKLIST.md
```

### K15 — `Сводка`

- **Действие:** `System → Website`

- **Заметка:** Журнал pilot cases

- **Адрес или цель:**

```text
https://github.com/sergstack/AI-OS/blob/main/PILOT_CASES.md
```

## Экран: `БАЗА`

```text
┌────────────┬────────────┬────────────┬────────────┬────────────┐
│ ⬆ НАЗАД    │ Индекс     │ Примен.    │ Приёмы     │ Рамки      │
├────────────┼────────────┼────────────┼────────────┼────────────┤
│ Понятия    │ Порядки    │ Маршрут    │ Уверенн.   │ Проверка   │
├────────────┼────────────┼────────────┼────────────┼────────────┤
│ Манифест   │ Поиск      │ Добавить   │ Источник   │ Не найдено │
└────────────┴────────────┴────────────┴────────────┴────────────┘
```

### K1 — `⬆ НАЗАД`

- **Действие:** `штатный возврат из папки`

- **Оставить штатную кнопку возврата из папки.**

### K2 — `Индекс`

- **Действие:** `System → Text`

- **Вставить в поле текста:**

```text
# БАЗА ЗНАНИЙ — ИНДЕКС

Тема:
[указать]

Проверь:
- найдено в базе знаний: да / нет / частично;
- источники;
- подтверждённые утверждения;
- слабые или неподтверждённые утверждения;
- уверенность;
- что отправить на дополнительную проверку;
- следующий шаг.

Не придумывай данные, если в базе не найдено.
```

### K3 — `Примен.`

- **Действие:** `System → Text`

- **Вставить в поле текста:**

```text
# БАЗА ЗНАНИЙ — ПРИМЕН.

Тема:
[указать]

Проверь:
- найдено в базе знаний: да / нет / частично;
- источники;
- подтверждённые утверждения;
- слабые или неподтверждённые утверждения;
- уверенность;
- что отправить на дополнительную проверку;
- следующий шаг.

Не придумывай данные, если в базе не найдено.
```

### K4 — `Приёмы`

- **Действие:** `System → Text`

- **Вставить в поле текста:**

```text
# БАЗА ЗНАНИЙ — ПРИЁМЫ

Тема:
[указать]

Проверь:
- найдено в базе знаний: да / нет / частично;
- источники;
- подтверждённые утверждения;
- слабые или неподтверждённые утверждения;
- уверенность;
- что отправить на дополнительную проверку;
- следующий шаг.

Не придумывай данные, если в базе не найдено.
```

### K5 — `Рамки`

- **Действие:** `System → Text`

- **Вставить в поле текста:**

```text
# БАЗА ЗНАНИЙ — РАМКИ

Тема:
[указать]

Проверь:
- найдено в базе знаний: да / нет / частично;
- источники;
- подтверждённые утверждения;
- слабые или неподтверждённые утверждения;
- уверенность;
- что отправить на дополнительную проверку;
- следующий шаг.

Не придумывай данные, если в базе не найдено.
```

### K6 — `Понятия`

- **Действие:** `System → Text`

- **Вставить в поле текста:**

```text
# БАЗА ЗНАНИЙ — ПОНЯТИЯ

Тема:
[указать]

Проверь:
- найдено в базе знаний: да / нет / частично;
- источники;
- подтверждённые утверждения;
- слабые или неподтверждённые утверждения;
- уверенность;
- что отправить на дополнительную проверку;
- следующий шаг.

Не придумывай данные, если в базе не найдено.
```

### K7 — `Порядки`

- **Действие:** `System → Text`

- **Вставить в поле текста:**

```text
# БАЗА ЗНАНИЙ — ПОРЯДКИ

Тема:
[указать]

Проверь:
- найдено в базе знаний: да / нет / частично;
- источники;
- подтверждённые утверждения;
- слабые или неподтверждённые утверждения;
- уверенность;
- что отправить на дополнительную проверку;
- следующий шаг.

Не придумывай данные, если в базе не найдено.
```

### K8 — `Маршрут`

- **Действие:** `System → Text`

- **Вставить в поле текста:**

```text
# БАЗА ЗНАНИЙ — МАРШРУТ

Тема:
[указать]

Проверь:
- найдено в базе знаний: да / нет / частично;
- источники;
- подтверждённые утверждения;
- слабые или неподтверждённые утверждения;
- уверенность;
- что отправить на дополнительную проверку;
- следующий шаг.

Не придумывай данные, если в базе не найдено.
```

### K9 — `Уверенн.`

- **Действие:** `System → Text`

- **Вставить в поле текста:**

```text
# БАЗА ЗНАНИЙ — УВЕРЕНН.

Тема:
[указать]

Проверь:
- найдено в базе знаний: да / нет / частично;
- источники;
- подтверждённые утверждения;
- слабые или неподтверждённые утверждения;
- уверенность;
- что отправить на дополнительную проверку;
- следующий шаг.

Не придумывай данные, если в базе не найдено.
```

### K10 — `Проверка`

- **Действие:** `System → Text`

- **Вставить в поле текста:**

```text
# БАЗА ЗНАНИЙ — ПРОВЕРКА

Тема:
[указать]

Проверь:
- найдено в базе знаний: да / нет / частично;
- источники;
- подтверждённые утверждения;
- слабые или неподтверждённые утверждения;
- уверенность;
- что отправить на дополнительную проверку;
- следующий шаг.

Не придумывай данные, если в базе не найдено.
```

### K11 — `Манифест`

- **Действие:** `System → Website`

- **Адрес или цель:**

```text
https://github.com/sergstack/AI-OS/blob/main/MANIFEST.json
```

### K12 — `Поиск`

- **Действие:** `System → Text`

- **Вставить в поле текста:**

```text
# БАЗА ЗНАНИЙ — ПОИСК

Тема:
[указать]

Проверь:
- найдено в базе знаний: да / нет / частично;
- источники;
- подтверждённые утверждения;
- слабые или неподтверждённые утверждения;
- уверенность;
- что отправить на дополнительную проверку;
- следующий шаг.

Не придумывай данные, если в базе не найдено.
```

### K13 — `Добавить`

- **Действие:** `System → Text`

- **Вставить в поле текста:**

```text
# БАЗА ЗНАНИЙ — ДОБАВИТЬ

Тема:
[указать]

Проверь:
- найдено в базе знаний: да / нет / частично;
- источники;
- подтверждённые утверждения;
- слабые или неподтверждённые утверждения;
- уверенность;
- что отправить на дополнительную проверку;
- следующий шаг.

Не придумывай данные, если в базе не найдено.
```

### K14 — `Источник`

- **Действие:** `System → Text`

- **Вставить в поле текста:**

```text
# БАЗА ЗНАНИЙ — ИСТОЧНИК

Тема:
[указать]

Проверь:
- найдено в базе знаний: да / нет / частично;
- источники;
- подтверждённые утверждения;
- слабые или неподтверждённые утверждения;
- уверенность;
- что отправить на дополнительную проверку;
- следующий шаг.

Не придумывай данные, если в базе не найдено.
```

### K15 — `Не найдено`

- **Действие:** `System → Text`

- **Вставить в поле текста:**

```text
# БАЗА ЗНАНИЙ — НЕ НАЙДЕНО

Тема:
[указать]

Проверь:
- найдено в базе знаний: да / нет / частично;
- источники;
- подтверждённые утверждения;
- слабые или неподтверждённые утверждения;
- уверенность;
- что отправить на дополнительную проверку;
- следующий шаг.

Не придумывай данные, если в базе не найдено.
```

## Экран: `СИСТЕМА`

```text
┌────────────┬────────────┬────────────┬────────────┬────────────┐
│ ⬆ НАЗАД    │ ChatGPT    │ Obsidian   │ Things     │ Календарь  │
├────────────┼────────────┼────────────┼────────────┼────────────┤
│ Дата       │ Шапка      │ Буфер      │ Окно ←     │ Окно →     │
├────────────┼────────────┼────────────┼────────────┼────────────┤
│ Звук       │ Таймер     │ Корень     │ Помощь     │ СТОП       │
└────────────┴────────────┴────────────┴────────────┴────────────┘
```

### K1 — `⬆ НАЗАД`

- **Действие:** `штатный возврат из папки`

- **Оставить штатную кнопку возврата из папки.**

### K2 — `ChatGPT`

- **Действие:** `System → Website`

- **Адрес или цель:**

```text
https://chatgpt.com
```

### K3 — `Obsidian`

- **Действие:** `System → Website / Open`

### K4 — `Things`

- **Действие:** `System → Website / Open`

### K5 — `Календарь`

- **Действие:** `System → Website`

- **Адрес или цель:**

```text
<GOOGLE_CALENDAR_URL>
```

### K6 — `Дата`

- **Действие:** `System → Text`

- **Заметка:** Можно заменить shortcut-generated date

- **Вставить в поле текста:**

```text
ГГГГ-ММ-ДД
```

### K7 — `Шапка`

- **Действие:** `System → Text`

- **Вставить в поле текста:**

```text
База знаний проверена:
Источники:
Найдено в базе знаний:
Уверенность:
Статус подтверждения:
```

### K8 — `Буфер`

- **Действие:** `System → Hotkey / Script`

- **Заметка:** Только если безопасно

### K9 — `Окно ←`

- **Действие:** `System → Hotkey`

- **Настроить вручную:**

```text
Win + Left / custom macOS shortcut
```

### K10 — `Окно →`

- **Действие:** `System → Hotkey`

- **Настроить вручную:**

```text
Win + Right / custom macOS shortcut
```

### K11 — `Звук`

- **Действие:** `System → Hotkey`

- **Настроить вручную:**

```text
System mute toggle
```

### K12 — `Таймер`

- **Действие:** `Multi Action`

- **Настроить вручную:**

```text
Open timer / start 25 min focus
```

- **Не добавлять разрушительные действия.**

### K13 — `Корень`

- **Действие:** `System → Text`

- **Вставить в поле текста:**

```text
<LOCAL_AI_OS_ROOT>
```

### K14 — `Помощь`

- **Действие:** `System → Text`

- **Вставить в поле текста:**

```text
# ПОМОЩЬ ПО STREAM DECK

Текущий экран:
Задача:
Ожидаемое действие:
Риск:
Нужно ли сначала определить маршрут?
Нужно ли сначала проверить подтверждения?
Нужно ли передать задачу в другой проект?
```

### K15 — `СТОП`

- **Действие:** `Multi Action`

- **Заметка:** Без destructive actions

- **Настроить вручную:**

```text
Esc → switch/open AI OS HOME
```

- **Не добавлять разрушительные действия.**

---

# Проверка после настройки

Проверь цепочку:

1. `ДОМ → AI OS → Анализ`
2. `ДОМ → AI OS → Подтв.`
3. `ДОМ → AI OS → Ловушки`
4. `ДОМ → AI OS → Приём`
5. `ДОМ → AI OS → В LLM`
6. `ДОМ → ПРОВЕРКА → Quick QA`
7. `ДОМ → ПРОВЕРКА → Evidence`
8. `ДОМ → ПРОВЕРКА → Handoff`
9. `ДОМ → ПРОВЕРКА → Final QA`

Ожидаемый результат:
- кнопка вставляет полный русский prompt;
- QA-ответ возвращает `pass / revise / blocked`;
- слабые и неподтверждённые claims не становятся фактами;
- facts / interpretation / hypothesis / recommendation разделены;
- routing в [Thinking] / [Analytics] / [LLM] / [Codex] указан явно;
- handoff содержит acceptance criteria и risks;
- текст не отправляется автоматически;
- опасные действия не выполняются одной кнопкой.