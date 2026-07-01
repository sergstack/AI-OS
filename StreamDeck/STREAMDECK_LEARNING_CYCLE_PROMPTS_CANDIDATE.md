# Candidate Full Prompt Set — Stream Deck Learning Cycle

Status: **candidate / ready for Stream Deck pilot**
Owner project: **[LLM]**
Use: кнопки Stream Deck для изучения материала, проверки, доработки и сохранения карточек
Promotion status: **not permanent standard**
Evidence status: **practical recommendation / needs 3–5 real runs**

Основной экран:

```text
[Daily]      [Master]     [Hardcore]   [Judge]
[Revisor]   [QA]         [Save Mini]  [Save Full]
```

## Как пользоваться

```text
Daily → Save Mini
Master → Judge → Revisor → Save Full
Hardcore → Judge → Revisor → QA → Save Full
```

Если результат нужно передать в другой проект — использовать отдельную кнопку `Handoff` на Router / AI Operator экране.

## Self-check vs external Judge

`Master` и `Hardcore` содержат встроенный `Self-Judge`. Это внутренняя самопроверка результата.

Внешняя кнопка `Judge` остаётся отдельным quality gate:

* после `Master` — recommended, если есть reusable output;
* после `Hardcore` — required;
* перед `Save Full` для high-value материалов — recommended / required по риску;
* перед permanent standard — required.

## Source coverage rule

`Source coverage` означает:

```text
достаточно ли покрыты ключевые элементы исходника для intended use
```

Это **не** означает полный пересказ исходника. Примеры, учебные детали и неиспользуемые блоки можно оставить как reference, если они не нужны для текущей цели.

## Global rules for all buttons

```text
- Используй последнее содержательное сообщение, вложения и контекст текущего project folder.
- Не проси вставлять материал вручную, если он уже есть в контексте.
- Не выдумывай факты, источники, цифры, даты, файлы, repo paths, tests или approvals.
- Отделяй facts / interpretation / hypothesis / recommendation.
- Помечай unsupported claims и weak evidence.
- Не превращай weak evidence в supported fact.
- Не делай production-ready claims без evidence и acceptance.
- Для high-stakes тем указывай необходимость source verification.
- Не копируй raw dumps, full transcripts, private client data или sensitive data.
- Если задача выходит за рамки текущего проекта — верни route / handoff.
```

## Do not claim / Do not do

```text
- Не утверждать, что Learning Card = verified AI OS KB evidence.
- Не утверждать, что prompt set является permanent standard.
- Не запускать automation.
- Не делать расчёты эффекта без [Analytics].
- Не делать implementation / repo changes без [Codex].
- Не утверждать юридическую / data безопасность без review.
- Не сохранять Save Mini как reusable asset без Judge / QA.
- Не использовать Save Full как полноценную Process Card без заполнения по конкретному процессу.
```

---

# 1. Daily

```text
# LEARNING CYCLE — DAILY

Изучи последний предоставленный материал: сообщение выше, вложения, заметки или контекст текущего project folder.

Не проси вставлять тему или контекст вручную.
Если тема явно не названа, определи её из материала.
Если данных мало, сделай best effort и отметь missing inputs.

Цель:
Быстро понять материал за 5–10 минут и получить одно практическое действие.

Правила:
- Не выдумывай факты.
- Отделяй facts / interpretation / hypothesis.
- Unsupported claims помечай.
- Если evidence слабое, прямо скажи.
- Не делай production-ready выводов.
- Для high-stakes выводов укажи, что нужна source verification.
- Если материал требует расчётов → route to [Analytics].
- Если требует кода / файлов / repo → route to [Codex].
- Если требует KB evidence → route to [AI OS].
- Если требует стратегии / решения → route to [Thinking].
- Если это prompts / LLM workflow / model routing / quality → [LLM].
- Не сохраняй результат автоматически: если вывод полезен, следующим шагом предложи Save Mini.

Верни:

Mode:
Daily

Topic detected:

Mini-frame:
- что это:
- зачем полезно:
- границы применимости:

Mini-map:
- 3–5 ключевых элементов:

One useful insight:

One action:
- что сделать за 10–20 минут:

Risk check:
- что можно неправильно понять:
- что требует проверки:

Reusable mini-output:
- checklist / question / prompt / decision aid:

Confidence:
low / medium / high

Next safe step:
```

---

# 2. Master

```text
# LEARNING CYCLE — MASTER

Изучи последний предоставленный материал: сообщение выше, вложения, заметки или контекст текущего project folder.

Не проси вставлять тему, цель или project context вручную.
Определи тему, цель и контекст применения автоматически из материала.
Если чего-то не хватает, не блокируй работу: сделай best effort и явно отметь missing inputs.

Цель:
Превратить материал в понятный reusable output: checklist / prompt / memo skeleton / QA-gate / routing card / decision aid / process card.

Цикл:
Frame → Map → Learn → Apply → Self-Judge → Revisor → QA-gate → Result

Правила:
- Не выдумывай факты.
- Отделяй facts / interpretation / hypothesis / recommendation.
- Unsupported claims помечай.
- Не превращай weak evidence в supported fact.
- Не делай production-ready claims.
- Не используй learning output как source of truth для high-stakes решений.
- Для high-stakes тем требуй source verification.
- Расчёты / метрики / data QA → [Analytics].
- Код / repo / files / tests / implementation → [Codex].
- KB evidence / governance / supported pattern → [AI OS].
- Strategy / trade-off / decision → [Thinking].
- Prompts / LLM workflow / model routing / quality → [LLM].
- Self-Judge внутри этого prompt не заменяет внешнюю кнопку Judge для reusable output.
- Если результат нужно сохранить как asset, следующим шагом предложи external Judge / Revisor / Save Full.

Верни:

Mode:
Master

Topic detected:

Frame:
- learning goal:
- known facts:
- assumptions:
- missing inputs:

Map:
- 5–9 ключевых блоков:

Learn:
- краткое объяснение:
- важные детали:
- типовые ошибки:

Apply:
- применение к моей работе:
- reusable output:

Если материал относится к бизнес-процессу / AI-аудиту / внедрению ИИ / process card, обязательно проверь, нужны ли в reusable output следующие блоки:

1. Discovery / выявление задач:
   - кто участвует;
   - как собираем список задач: созвон / чат / опрос / документы;
   - что фиксируем: что делают / как часто / сколько времени / какая боль;
   - как группируем задачи: daily / weekly / monthly / complex;
   - какая задача выбрана первой.

2. As-Is:
   - текущий процесс;
   - входы;
   - системы / источники;
   - шаги;
   - решения;
   - выход;
   - частота;
   - объём;
   - текущие ошибки / задержки / quality issues.

3. To-Be / proposed implementation:
   - будущий процесс;
   - что делает человек;
   - что делает ИИ;
   - что ИИ не должен делать;
   - CJM / BPMN / Flow / UserStory needed: yes/no.

4. Adoption / change risk:
   - риск сопротивления сотрудников;
   - страх замещения;
   - обучение нужно: yes/no;
   - коммуникация нужна: yes/no;
   - owner adoption.

5. Route maturity:
   - Audit;
   - Audit/R&D;
   - R&D;
   - Development;
   - почему выбран этот уровень зрелости.

Self-Judge:
- unsupported claims:
- weak evidence:
- risks:
- blockers:
- routing issues:
- source coverage gaps for intended use:
  - какие важные элементы исходника были сжаты или потеряны;
  - какие детали нужно оставить как reference, а не тащить в карточку;
  - какие элементы нужно добавить в reusable output.

Revised result:
- исправленная версия без новых фактов:

QA-gate:
- learning goal clear: yes/no
- topic map exists: yes/no
- application exists: yes/no
- reusable output exists: yes/no
- risks visible: yes/no
- routing correct: yes/no
- confidence not overstated: yes/no
- source coverage sufficient for intended use: yes/no

Final result:
- итог:
- что можно использовать:
- что нельзя считать доказанным:
- что требует отдельной проверки:
- что из исходника сохранено для intended use:
- что из исходника сознательно не переносим:
- next safe step:
- confidence: low / medium / high
```

---

# 3. Hardcore

```text
# LEARNING CYCLE — HARDCORE

Глубоко разбери последний предоставленный материал: сообщение выше, вложения, заметки или контекст текущего project folder.

Не проси вставлять тему, цель или project context вручную.
Определи тему, цель, критичность и контекст применения автоматически.
Если данных недостаточно, продолжай best effort и явно отметь missing inputs / blockers.

Цель:
Получить глубокое понимание, риски, ограничения, применимость и reusable artifact.

Цикл:
Frame → Map → Learn → Apply → Self-Judge → Revisor → QA-gate → Result

Правила:
- Не выдумывай источники, цифры, исследования, approvals, repo paths или tests.
- Не подменяй source verification красивым объяснением.
- Не делай production-ready claims.
- Не усиливай выводы сильнее, чем позволяют данные.
- Для актуальных / high-stakes / финансовых / юридических / медицинских / технических тем укажи, где нужна свежая проверка источников.
- Расчёты / метрики → [Analytics].
- Код / repo / implementation → [Codex].
- KB-backed evidence → [AI OS].
- Strategy / decision → [Thinking].
- Prompt / LLM workflow → [LLM].
- Self-Judge внутри этого prompt не заменяет внешнюю кнопку Judge.
- Для high-value / high-stakes / reusable output внешний Judge обязателен.
- Для сохранения как asset использовать latest revised / approved version.

Верни:

Mode:
Hardcore

Topic detected:

Criticality inferred:
low / medium / high

Frame:
- главный вопрос:
- практический результат:
- known facts:
- assumptions:
- missing inputs:
- blockers:

Topic map:
- core concepts:
- mechanisms:
- use cases:
- risks:
- failure modes:
- quality checks:
- routing implications:
- open questions:

Source coverage map:
- какие основные блоки исходника выявлены:
- какие блоки критичны для intended use:
- какие блоки можно сжать:
- какие блоки нельзя потерять:
- какие блоки являются примерами, а не правилами:
- какие claims требуют source verification:

Если материал относится к бизнес-процессу / AI-аудиту / внедрению ИИ, отдельно проверь наличие:
- Discovery / выявление задач;
- приоритизация задач;
- As-Is;
- To-Be;
- CJM / BPMN / Flow / UserStory;
- Audit / Audit-R&D / R&D / Development;
- business effect / baseline / ROI route to [Analytics];
- data / legal constraints;
- old process vs new process;
- reverse prompt engineering / восстановление методологии;
- adoption / change risks;
- training / communication / external expert / market research.

Structured learning:
- executive summary:
- ключевая логика:
- детали, которые нельзя потерять:
- ловушки и ошибки:

Application design:
A. безопасное минимальное применение:
- input:
- transformation:
- output:
- QA check:
- stop condition:

B. более сильное применение с рисками:
- input:
- transformation:
- output:
- QA check:
- stop condition:

Reusable artifact:
Создай один reusable artifact:
- checklist / prompt / routing card / QA-gate / memo skeleton / decision template / process card.

Если artifact = process card / AI pre-pilot card, он должен включать:
0. Discovery / выявление задач
1. Process
2. As-Is
3. Evidence status
4. AI fit
5. Route maturity: Audit / Audit-R&D / R&D / Development
6. Route options: training / ready software / R&D / custom development
7. Data / legal constraints
8. Business effect, with route to [Analytics] if calculation is needed
9. QA-gate
10. To-Be / proposed implementation
11. Adoption / change risk
12. Decision

Self-Judge review:
- unsupported claims:
- weak evidence:
- missing evidence:
- overconfidence:
- wrong routing:
- blockers:
- source coverage gaps for intended use:
- where fresh source check is required:
- what not to claim:

Revised result:
- исправленная версия без добавления новых фактов:

QA-gate:
- learning goal clear: yes/no
- topic map exists: yes/no
- application exists: yes/no
- reusable output exists: yes/no
- risks and blockers explicit: yes/no
- routing correct: yes/no
- unsupported claims marked: yes/no
- confidence not overstated: yes/no
- source coverage sufficient for intended use: yes/no
- next step clear: yes/no

Final result:
- итоговое понимание:
- применимость к работе:
- reusable output:
- source coverage for intended use:
  - retained:
  - compressed:
  - not included intentionally:
  - missing / needs evidence:
- риски:
- blockers:
- next safe action:
- confidence:
```

---

# 4. Judge

```text
@judge

Проверь последнее содержательное сообщение выше.

Не проси вставлять материал.
Не проси указывать project context вручную.
Используй инструкции текущего ChatGPT project folder и его Knowledge.

Проверь:
- unsupported claims;
- weak evidence;
- missing constraints;
- wrong routing;
- risks;
- blockers;
- overconfidence;
- source-substitution;
- automation creep;
- source coverage gaps.

Если проверяется Learning Card / Process Card / reusable output по исходному материалу, дополнительно проверь:
- не потеряны ли ключевые блоки исходника для intended use;
- не превращены ли примеры из исходника в универсальные правила;
- не потеряны ли risks / limitations / blockers;
- не потеряны ли legal / data / privacy constraints;
- не потеряны ли As-Is / To-Be / QA / adoption / routing элементы;
- что сознательно сжато и должно остаться только reference.

Если материал относится к AI-аудиту бизнес-процессов, проверь наличие или честное отсутствие:
- Discovery / выявление задач;
- As-Is;
- To-Be / proposed implementation;
- Route maturity: Audit / Audit-R&D / R&D / Development;
- business effect / baseline / Analytics route;
- data / legal constraints;
- old process vs new process;
- adoption / change risk;
- QA-gate;
- stop conditions.

Не переписывай материал.
Не решай целевую задачу.
Не усиливай выводы сильнее, чем позволяют данные.

Routing:
- calculations / metrics / data QA → [Analytics]
- code / repo / files / tests / implementation → [Codex]
- KB evidence / governance / supported pattern → [AI OS]
- prompts / LLM workflow / model routing / quality → [LLM]
- strategy / trade-off / decision / risks → [Thinking]

Верни строго:

Judge verdict: pass / revise / blocked

Unsupported claims:

Missing constraints:

Source coverage gaps:

Risks:

Required fixes:

Stop / blocked conditions:

Safe next step:
```

---

# 5. Revisor

```text
@revisor

Доработай материал с учётом контекста выше.

Не проси вставлять материал.
Не проси указывать project context вручную.
Используй инструкции текущего ChatGPT project folder и его Knowledge, если они доступны.

Главное правило:
- Если последнее содержательное сообщение выше является Judge verdict / QA review, НЕ редактируй сам Judge/QA output.
- Используй Judge/QA output как список замечаний и примени их к исходному материалу.
- Если Judge verdict = pass, сделай только лёгкую редактуру, если она действительно нужна.
- Если Judge verdict = revise, примени замечания.
- Если Judge verdict = blocked, не переписывай как финальный материал; верни blockers.
- Если исходный материал невозможно безопасно определить — верни blocked.

Правила:
- Сделай текст яснее, короче и структурнее.
- Не добавляй новые факты.
- Не выдумывай источники, цифры, даты, файлы, repo, tests или approvals.
- Не удаляй risks, limitations, blockers, uncertainty и evidence status.
- Не превращай weak evidence в supported fact.
- Не усиливай выводы сильнее, чем позволяют данные.
- Сохрани project route и stop conditions.

Верни строго:

Revision status: completed / blocked

Revision mode:
- direct revision / apply Judge fixes / blocked by Judge

Source material used:

Judge fixes applied:

Revised version:

What changed:
- clarity:
- structure:
- wording:
- risk/evidence handling:

What was preserved:
- meaning:
- facts:
- numbers/dates:
- uncertainty:
- project route:
- limitations:

Remaining blockers:

Suggested next check:
- Judge / QA / Handoff / ready to use
```

---

# 6. QA

```text
# FINAL QA

Проверь последнее содержательное сообщение выше перед использованием.

Не переписывай материал.
Не решай целевую задачу.
Не проси указывать intended use вручную: определи его автоматически из контекста.

Intended use:
определи автоматически: сохранить как prompt / использовать как workflow / добавить в Stream Deck / передать в другой проект / использовать в memo / другое

Проверь:
- задача выполнена;
- структура ответа соблюдена;
- facts / interpretation / hypothesis / recommendation разделены;
- unsupported claims удалены или помечены;
- confidence и limitations видны;
- routing корректный;
- high-stakes use требует source verification;
- нет production-ready claims без acceptance;
- нет automation без pilot evidence;
- next step конкретный;
- blockers честно указаны;
- source coverage достаточен для intended use.

Если intended use = save as Learning Card / Process Card / reusable asset:
- карточка сохраняет ключевые элементы исходника, нужные для цели;
- примеры из исходника не выданы за универсальные правила;
- raw material не копируется внутрь карточки;
- source reference сохранён;
- missing evidence явно указано;
- source coverage gaps указаны или исправлены.

Если материал относится к AI-аудиту бизнес-процессов, проверь:
- Discovery / выявление задач;
- As-Is;
- To-Be / proposed implementation;
- Route maturity;
- route options;
- business effect / Analytics handoff;
- data / legal constraints;
- adoption / change risk;
- QA-gate;
- stop conditions.

Верни строго:

Final verdict: pass / revise / blocked

Release notes:

Unsupported claims:

Source coverage:

Required final fixes:

Residual risks:

What not to claim:

Approved use:

Save / share allowed: yes / no

Approved next step:
```

---

# 7. Save Mini

```text
# SAVE MINI CARD

Преобразуй последний содержательный результат выше в короткую карточку сохранения.

Не проси вставлять материал.
Не проси указывать project context вручную.
Используй последнее сообщение, вложения и контекст текущего project folder.

Правила:
- Структурируй только уже полученный результат.
- Не добавляй новые факты.
- Не создавай новое evidence.
- Не выдумывай источники, ссылки, даты, файлы, approvals, repo paths или tests.
- Если был Judge / Revisor / QA, сохраняй latest revised / approved version.
- Не копируй raw material, full transcript, raw dump или sensitive data.
- Сохраняй summary + reference.
- Если данных нет, укажи not provided / missing evidence.
- Не превращай interpretation или hypothesis в fact.
- Если материал high-stakes без source verification, статус должен быть draft / needs evidence.
- Save Mini не является reusable asset без Judge / QA.

Если материал не даёт practical use, next action, risk/blocker, decision или reusable output — предложи discard / parked.

Верни строго:

# Mini Learning Card — [Topic]

Card ID:
LC_[Project]_[Topic]_YYYY-MM-DD

Status:
draft / reviewed / parked / discarded

Action status:
open / done / parked / discarded

Owner project:
[LLM] / [Thinking] / [Analytics] / [Codex] / [AI OS]

Original material location:
link / file / note / message above / not provided

Source summary:
[краткое содержание без raw dump]

Topic:

Key takeaway:

Practical use:

Reusable output:
short description / none

Risks / limitations:

Evidence status:
supported / weak / practical recommendation / needs evidence / not checked

Review trigger:
[когда пересмотреть / событие / not needed]

Next action:

Decision:
keep / apply / route / archive / discard

Tags:
[#project, #topic, #status, #type]
```

---

# 8. Save Full

```text
# SAVE FULL CARD

Преобразуй последний содержательный результат выше в полную карточку сохранения.

Не проси вставлять материал.
Не проси указывать project context вручную.
Используй последнее сообщение, вложения и контекст текущего project folder.

Важно:
- Save Full только структурирует уже полученный результат.
- Не добавляй новые факты.
- Не создавай новое evidence.
- Не выдумывай источники, ссылки, даты, файлы, approvals, repo paths или tests.
- Если был Judge / Revisor / QA, сохраняй latest revised / approved version.
- Не копируй raw material, full transcript, raw dump или sensitive data.
- Сохраняй summary + reference.
- Если данных нет — укажи not provided / missing evidence.
- Не превращай interpretation или hypothesis в fact.
- Сохрани risks, limitations, blockers, confidence и evidence status.
- Если материал high-stakes и source verification не проведена — можно сохранить только как draft / needs evidence.
- Не сохраняй как verified knowledge, если evidence status = weak / needs evidence.

Определи Card type:
- Learning Card;
- Prompt Registry Candidate;
- Process Card Candidate;
- Handoff Candidate;
- blocked.

Если материал не даёт reusable output, next action, risk/blocker или decision — предложи parked / discard вместо сохранения.

Перед сохранением:
- проверь, есть ли уже карточка по теме;
- если есть, предложи update existing / create linked card / discard duplicate.

Дополнительно проверь source coverage:
- какие ключевые блоки исходника сохранены;
- какие сжаты;
- какие не включены сознательно;
- какие отсутствуют и требуют revision;
- не были ли примеры превращены в универсальные правила;
- не потеряны ли risks, blockers, legal/data constraints, QA, routing.
- source coverage оценивай для intended use, а не как полный пересказ исходника.

Если Card type = Process Card Candidate, обязательно включи или явно пометь missing:
- Discovery / выявление задач;
- As-Is;
- Evidence status;
- AI fit;
- Route maturity: Audit / Audit-R&D / R&D / Development;
- Route options: training / ready software / R&D / custom development;
- Data / legal constraints;
- Business effect / baseline / Analytics handoff;
- QA-gate;
- To-Be / proposed implementation;
- Adoption / change risk;
- Decision.

Важно:
Process Card Candidate не становится полноценной Process Card, пока не заполнен по одному конкретному процессу.

Верни строго:

# Card Save Result

Save status:
save as draft / save as reusable asset / parked / discard / blocked

Card type:
Learning Card / Prompt Registry Candidate / Process Card Candidate / Handoff Candidate / blocked

Reason:

Duplicate check:
new card / update existing / create linked card / possible duplicate

# Learning Card — [Topic]

Card ID:
LC_[Project]_[Topic]_YYYY-MM-DD

Status:
draft / reviewed / applied / archived

Action status:
open / done / parked / discarded

Owner project:
[LLM] / [Thinking] / [Analytics] / [Codex] / [AI OS]

Date:
YYYY-MM-DD

Review date / revisit trigger:
[дата или событие для пересмотра]

Material type:
article / video / book / note / course / prompt / workflow / meeting / other

Original material location:
link / file / note / message above / not provided

Source summary:
[краткое содержание без raw dump]

Source coverage:
- retained:
- compressed:
- not included intentionally:
- missing / needs revision:

Sensitivity / privacy:
public / internal / confidential / contains sensitive data / needs redaction

Source freshness:
stable / may be outdated / current check required / not checked

Tags:
[#project, #topic, #status, #type]

Linked cards / related artifacts:
-

## 1. Topic

Main topic:

Subtopics:
-

## 2. Key facts

DATA FACT:
-

Missing evidence:
-

## 3. Interpretation

INTERPRETATION:
-

HYPOTHESIS:
-

What not to claim:
-

## 4. Practical use

How this can help my work:
-

Best use case:
-

Do not use when:
-

## 5. Reusable output

Reusable asset type:
checklist / prompt / memo skeleton / QA-gate / routing card / process card / handoff / decision aid / none

Reusable output:

If reusable output is prompt / workflow:
next step = Prompt Registry Candidate

If reusable output is business process / AI pre-pilot:
next step = Process Card Candidate

## 6. Process-specific blocks

Заполнять, если Card type = Process Card Candidate. Если не применимо — указать not applicable.

### 6.1 Discovery / выявление задач
- кто участвует:
- как собираем список задач: созвон / чат / опрос / документы:
- что фиксируем: что делают / как часто / сколько времени / какая боль:
- группировка задач: daily / weekly / monthly / complex:
- какая задача выбрана первой:

### 6.2 As-Is
- input:
- systems / sources:
- steps:
- decisions:
- output:
- frequency:
- volume:
- current time / cost:
- current errors / delays / quality issues:

### 6.3 To-Be / proposed implementation
- future process:
- CJM / BPMN / Flow / UserStory needed: yes/no
- what changes for user:
- what remains human-controlled:
- what AI does:
- what AI must not do:

### 6.4 Route maturity
- Audit:
- Audit/R&D:
- R&D:
- Development:
- selected maturity level:
- why:

### 6.5 Route options
- Training:
- Ready software:
- R&D / prompt pilot:
- Custom development:
- Recommended route:
- Why not alternatives:

### 6.6 Data / legal constraints
- personal data:
- client data:
- HR data:
- financial data:
- commercial secrets:
- anonymization required: yes/no
- legal/data review required: yes/no

### 6.7 Business effect
- people involved:
- hours/month:
- cost/hour:
- expected time reduction:
- quality effect:
- financial effect:
- Analytics handoff required: yes/no

### 6.8 QA-gate
- test examples:
- acceptance criteria:
- reviewer:
- minimum quality level:
- stop condition:
- rollback:

### 6.9 Adoption / change risk
- employee resistance risk:
- fear of replacement: low / medium / high
- training needed: yes/no
- communication needed: yes/no
- external expert needed: yes/no
- market / trend research needed: yes/no
- owner of adoption:

## 7. Risks and limitations

Risks:
-

Limitations:
-

Blockers:
-

High-stakes source verification required:
yes / no

## 8. Routing

Primary route:
[LLM] / [Thinking] / [Analytics] / [Codex] / [AI OS]

Possible handoff:
-

## 9. Quality status

Judge verdict:
pass / revise / blocked / not checked

QA status:
pass / revise / blocked / not checked

Confidence:
low / medium / high

Evidence status:
supported / weak / practical recommendation / needs evidence / not checked

## 10. Decision and next action

Next safe action:

Decision:
keep / apply / route / archive / discard

Save decision:
save as draft / save as reusable asset / send to another project / discard / revisit later

Stop / blocked conditions:
-
```
