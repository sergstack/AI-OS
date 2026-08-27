# Router Workflow

Reference material. Active routing behavior is defined by `ROUTING_RULES.md`,
`THINGS_OUTPUT_SCHEMA.md`, `HANDOFF_PROTOCOL.md`, and
`SMOKE_QA_FOR_INBOX_ROUTER.md`.

Core boundary:

Router routes.
Router clarifies.
Router packages.
Router does not solve.

## Operating Flow

Capture → Classify → Clarify if needed → Route → Next Action / Handoff → Review

1. Capture the raw input as given.
2. Classify the input type.
3. Ask clarification only when the destination or action is unclear.
4. Route to the best destination.
5. Create one next action or a project handoff.
6. Review that the Router did not solve the target task.

## Classification Types

- action
- project
- decision
- research
- context / note
- prompt / LLM workflow
- data / calculation
- code / implementation
- AI concept / AI pattern
- thinker corpus / author artifact
- calendar event
- waiting item
- someday
- trash

## Things Gate

В Things отправлять только то, что можно выполнить физическим или цифровым
действием.

Проверка:

1. Есть ли глагол действия?
2. Понятно ли, где или в каком инструменте делать?
3. Понятно ли, когда задача готова?

Если нет — это не task, а context, idea, decision или project draft.

## Review Checklist

- Destination is explicit.
- Confidence is honest.
- Clarification is limited to 1–3 questions.
- One next step is provided.
- Handoff is used for project work.
- Router does not solve the target task.
