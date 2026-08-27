# Migrated Bundle Semantics

Canonical source created during Issue #285 provenance migration.
Legacy bundle provenance: `ChatGPT/[AI OS]/Knowledge_Bundles/AIOS_03_HANDOFF_AND_SMOKE_QA.md`.

## Legacy section: `ChatGPT/[AI OS]/Knowledge/HANDOFF_PROTOCOL.md`

- `Goal` сохраняет исходную цель; `Expected output` описывает текущий этап; `Acceptance criteria` не теряет исходную приёмку.
- Если owner capability доступна, reversible, policy-permitted и authorized, вызови её, проверь результат и верни его текущему владельцу.
- Если capability недоступна, верни terminal handoff с точной причиной; не считай подготовку handoff completion.
- Не авторизуй owner-frozen policy, merge, deploy, production promotion или другое действие с material downside/низкой обратимостью.
- Destination вне `PROJECT_CAPABILITIES.yaml` остаётся explicit terminal handoff: не изобретай capability, не вызывай `project-context` и не расширяй authority.
## Canonical compact field set
```text
From:
To:
Task type:
Mode: goal / strict
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
```
Use `Mode: goal` for broad repo/workflow/project goals where the receiving project can infer bounded safe scope. Use `Mode: strict` for high-risk, already-scoped, ultra-long, or explicitly requested task packages.

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
