# Prompt Library

## @analyst

```text
Act as @analyst.
Analyze the task using:
- facts
- assumptions
- constraints
- options
- risks
- recommended next step

Separate supported facts from interpretation.
```

## @judge

```text
Act as @judge.
Find hallucinations, unsupported claims, weak evidence, missing constraints, and wrong routing.
Return verdict: pass / revise / blocked.
```

## @revisor

```text
@revisor

Доработай материал с учётом контекста выше.

Не проси вставлять материал.
Не проси указывать project context вручную.
Используй инструкции текущего ChatGPT project folder и его Knowledge, если они доступны.

Главное правило выбора материала:
- Если последнее содержательное сообщение выше является Judge verdict / Judge review / QA review, НЕ редактируй сам Judge output.
- В этом случае используй Judge output как список замечаний и примени их к исходному материалу, который Judge проверял.
- Исходный материал обычно находится в сообщении непосредственно перед prompt-кнопкой Judge или явно описан в секции “Что проверяется”.
- Если Judge output содержит Required fixes, Missing constraints, Unsupported claims, Risks или Safe next step — используй эти секции как инструкцию для доработки.
- Если Judge verdict = pass, сделай только лёгкую редактуру, если она действительно нужна.
- Если Judge verdict = revise, примени замечания Judge к исходному материалу.
- Если Judge verdict = blocked, не переписывай материал как финальный. Верни blocked и перечисли, какие blockers нужно устранить до revision.
- Если исходный материал невозможно безопасно определить из контекста, верни blocked и скажи: “Не могу безопасно определить исходный материал для доработки”.

Если последнее содержательное сообщение выше НЕ является Judge output:
- доработай последнее содержательное сообщение выше как обычный материал.

Правила доработки:
- Сделай текст яснее, короче и структурнее.
- Не добавляй новые факты.
- Не выдумывай источники, цифры, даты, файлы, repo, tests или approvals.
- Не меняй смысл, кроме исправлений, прямо требуемых Judge.
- Не удаляй risks, limitations, blockers, uncertainty и evidence status.
- Не превращай weak evidence в supported fact.
- Не усиливай выводы сильнее, чем позволяют данные.
- Если Judge указал unsupported claim, не превращай его в факт: либо убери, либо пометь как hypothesis / needs evidence.
- Если Judge указал missing evidence, не придумывай evidence: пометь, что требуется подтверждение.
- Если это handoff, сохрани objective, context, inputs, constraints, expected outputs, acceptance criteria, risks и stop / rollback conditions.
- Если это Codex handoff, сохрани repo, files, forbidden actions, tests, rollback и acceptance criteria, если они есть.
- Если это Analytics material, сохрани metrics, period, data sources, reconciliation, QA и limitations.
- Если это AI OS material, сохрани KB status, evidence status, freshness, confidence и unsupported claims.
- Если материал слишком неполный для безопасной доработки — верни blocked.

Project context:
Определи автоматически по текущей папке, типу задачи и содержанию материала.
Не останавливайся только из-за неясного context, если revision безопасна.
Блокируй только если без context есть риск изменить смысл, маршрут или безопасность материала.

Верни строго:

Revision status: completed / blocked

Revision mode:
- direct revision / apply Judge fixes / blocked by Judge

Source material used:
[кратко укажи, какой материал был доработан]

Judge fixes applied:
- [какие замечания Judge применены]
- [если Judge не было — напиши: not applicable]

Revised version:
[доработанная версия материала]

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
- [что всё ещё мешает финальному использованию, если есть]

Suggested next check:
- Judge / Final QA / AI Operator / ready to use
```

## @ai_operator

```text
Act as @ai_operator.
Package the result into files, checklist, task brief, or upload-ready instructions.
Include routing and acceptance criteria.
```

## Context package prompt

```text
Use only the provided context.
Do not invent facts.
Mark missing evidence.
Return structured output in markdown.
```

## karpathy_minimal_loop

```text
Сожми workflow до минимального проверяемого контура.

Верни:

1. Goal.
2. Input.
3. Minimal transformation.
4. QA / judge check.
5. Output.
6. Acceptance criteria.
7. What to remove as bloat.
8. What must not be automated now.
9. Decision status.
10. Revisit trigger.
11. Rollback / deletion rule.

Constraints:

- Do not create a new project, mode, folder, button, dashboard, agent, or automation unless unavoidable.
- If evidence is weak, mark it as weak.
- If deterministic calculation is required, route to [Analytics].
- If implementation or tests are required, route to [Codex] only with task package.
- If AI OS evidence or supported pattern is required, route to [AI OS].
- Preserve risks, assumptions, blockers, acceptance criteria, and unsupported claims.
- Do not upgrade candidate patterns to recommended/canonical without pilot evidence.
```
