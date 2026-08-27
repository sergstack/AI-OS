# Migrated Bundle Semantics

Canonical source created during Issue #285 provenance migration.
Legacy bundle provenance: `ChatGPT/[AI OS]/Knowledge_Bundles/AIOS_03_HANDOFF_AND_SMOKE_QA.md`.

## Legacy section: `ChatGPT/[AI OS]/Knowledge/HANDOFF_PROTOCOL.md`

- `Objective` сохраняет исходную цель; `Expected output` описывает текущий этап; `Acceptance criteria` не теряет исходную приёмку.
- Если owner capability доступна, reversible, policy-permitted и authorized, вызови её, проверь результат и верни его текущему владельцу.
- Если capability недоступна, верни terminal handoff с точной причиной; не считай подготовку handoff completion.
- Не авторизуй owner-frozen policy, merge, deploy, production promotion или другое действие с material downside/низкой обратимостью.
- Destination вне `PROJECT_CAPABILITIES.yaml` обрабатывается по class в `ROUTING_RULES.md`: `external` остаётся explicit terminal handoff; `internal_non_capability` продолжает только названную границу; `owner_escalation` требует owner decision.

## Canonical compact field set

The sole field-set owner is `HANDOFF_STYLE_STANDARD.md`. This migrated bundle
semantics file references that standard and does not repeat its fields or mode
rules.

## Legacy section: `ChatGPT/[AI OS]/Knowledge/GITHUB_ISSUE_DRIVEN_HANDOFF.md`

- Acceptance criteria

## Legacy section: `ChatGPT/[AI OS]/Knowledge/SMOKE_QA_FOR_AI_OS.md`

- подготовленный, но неисполненный handoff не даёт `COMPLETED`;
- original goal и acceptance criteria сохраняются.
- owner-frozen policy, merge или deploy без approval не выполняются;
- возвращается `OWNER_DECISION_REQUIRED` с точным decision/approval.
- дефект регистрируется и маршрутизируется к владельцу;
- выполняется permitted minimal correction и повторяется тот же affected check;
- для Codex сохраняется предел одной коррекции.
- destination вне `PROJECT_CAPABILITIES.yaml` даёт explicit terminal handoff;
- capability не изобретается, `project-context` не вызывается, authority не расширяется.
