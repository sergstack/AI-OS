# GitHub Foundation v1 — Codex Prompt

## Назначение

Этот файл — готовый prompt для передачи в `[Codex]`, чтобы привести GitHub-репозиторий к базовому инженерному стандарту: README, AGENTS.md, шаблоны Issues/PR, CI, Dependabot и checklist ручных настроек GitHub.

Цель — сделать репозиторий **AI-ready, review-ready и CI-ready**, не меняя бизнес-логику проекта.

---

## Как использовать

1. Открой проект в `[Codex]`.
2. Вставь prompt из блока ниже.
3. Попроси Codex работать через PR / diff, а не “тихо всё переписать”.
4. После выполнения проверь список изменённых файлов, тесты и assumptions.

---

## Prompt для Codex

```text
Task: Create GitHub Foundation v1 for this repository.

Goal:
Turn the repository into a clean, AI-ready and GitHub-ready project without changing business logic.

Context:
This repository should become easier to understand, test, review, and maintain through GitHub-native workflows. The goal is not to rebuild the project, but to add a professional foundation around it: documentation, AI-agent instructions, CI, issue/PR templates, dependency monitoring, and review discipline.

Scope:
1. Inspect the repository structure, dependency manager, existing tests, current files, and generated outputs.
2. Create or update the following files:
   - README.md
   - AGENTS.md
   - CHANGELOG.md
   - CONTRIBUTING.md
   - .github/PULL_REQUEST_TEMPLATE.md
   - .github/ISSUE_TEMPLATE/bug_report.yml
   - .github/ISSUE_TEMPLATE/feature_request.yml
   - .github/workflows/ci.yml
   - .github/dependabot.yml

Important rules:
1. Do not change business logic.
2. Do not refactor application code unless it is strictly necessary for CI/test discovery, and explain it before doing so.
3. Do not modify generated outputs unless documentation explicitly needs to reference their structure.
4. Do not add secrets, tokens, credentials, local machine paths, or private data.
5. Do not assume `requirements.txt` exists. Detect the real dependency manager:
   - requirements.txt
   - pyproject.toml
   - poetry
   - uv
   - pipenv
   - conda
   - or another setup if present
6. CI must match the actual project stack.
7. Do not add semantic search, vector DB, web UI, agentic workflows, autonomous retrieval, or complex multi-agent automation.
8. Keep changes small, reviewable, and easy to revert.

README.md requirements:
- Explain what the project does.
- Explain the problem it solves.
- Provide quickstart instructions.
- Provide setup instructions.
- Provide usage examples.
- Describe project structure.
- Describe development workflow.
- Describe testing.
- Mention current limitations honestly.
- Do not invent features that are not present in the code.

AGENTS.md requirements:
Include concise instructions for AI coding agents:
- project purpose;
- tech stack;
- repository structure;
- install/test/lint commands;
- files or folders that should not be modified casually;
- rules for changing business logic;
- rules for generated outputs;
- definition of done;
- PR/review expectations;
- security constraints.

CI requirements:
- Add a GitHub Actions workflow at `.github/workflows/ci.yml`.
- Trigger on `push` and `pull_request`.
- Install dependencies using the real project setup.
- Run tests if tests exist.
- If tests do not exist, add a safe placeholder check that validates import/package structure where possible and clearly report that test coverage is missing.
- Do not make CI look green by skipping meaningful checks silently.
- Prefer clear failure over fake success.

Dependabot requirements:
- Add `.github/dependabot.yml`.
- Configure it for the detected package ecosystem.
- If the ecosystem is ambiguous, create the safest minimal config and document the assumption.

Templates:
1. Pull request template must ask for:
   - summary;
   - changed files;
   - test evidence;
   - risks;
   - screenshots/logs if relevant;
   - checklist for no secrets and no generated-output drift.
2. Bug report template must ask for:
   - expected behavior;
   - actual behavior;
   - steps to reproduce;
   - environment;
   - logs/error text;
   - affected files if known.
3. Feature request template must ask for:
   - user problem;
   - proposed solution;
   - alternatives;
   - acceptance criteria;
   - risks/constraints.

CHANGELOG.md:
- Create a standard changelog structure.
- Do not invent past releases.
- Add an `Unreleased` section.

CONTRIBUTING.md:
- Explain branch workflow.
- Explain how to install dependencies.
- Explain how to run tests.
- Explain PR expectations.
- Explain commit/PR hygiene.
- Keep it practical and short.

Manual GitHub settings checklist:
Create a section in the final answer listing what must be configured manually in GitHub UI:
- enable branch protection for `main`;
- require pull request before merge;
- require approving review;
- require status checks after first successful CI run;
- enable secret scanning;
- enable Dependabot alerts;
- create GitHub Project board with columns: Backlog, Ready, In progress, Review, Done.

Acceptance criteria:
- README.md is accurate and does not invent unsupported functionality.
- AGENTS.md gives clear project-specific instructions for Codex/AI agents.
- CHANGELOG.md exists with `Unreleased`.
- CONTRIBUTING.md exists and is practical.
- PR and issue templates exist.
- CI workflow exists and matches the actual dependency/test setup.
- Dependabot config exists.
- No business logic is changed.
- No secrets, local paths, or private data are added.
- Final response lists:
  - changed files;
  - why each file was added or changed;
  - detected dependency manager;
  - test/CI commands used;
  - assumptions;
  - blockers;
  - manual GitHub UI steps still required.

Output format:
1. Short summary.
2. Changed files table.
3. Commands run.
4. Test/CI result.
5. Assumptions and blockers.
6. Manual GitHub settings checklist.
7. Recommended next PR/task.
```

---

## Ручной checklist после работы Codex

После того как Codex создаст файлы, в GitHub UI нужно отдельно проверить:

```text
[ ] Branch protection for main enabled
[ ] Pull request before merge required
[ ] At least 1 approving review required
[ ] Status checks required after first successful CI run
[ ] Secret scanning enabled
[ ] Dependabot alerts enabled
[ ] GitHub Project board created
[ ] Repository topics added
[ ] README preview checked manually
[ ] First PR merged only after CI passes
```

---

## Что не входит в GitHub Foundation v1

```text
semantic search
vector DB
web UI
agentic workflows
autonomous retrieval
complex multi-agent automation
automatic Codex review on every PR
large refactoring
business logic rewrite
```

---

## Рекомендуемое название Issue

```text
GitHub Foundation v1: repo docs, AI instructions, CI, templates and security baseline
```

## Рекомендуемое описание Issue

```text
Create a minimal professional GitHub foundation for the repository:
README, AGENTS.md, CHANGELOG, CONTRIBUTING, PR/Issue templates, CI workflow and Dependabot config.
Do not change business logic.
Acceptance: repository becomes easier to understand, test, review and maintain.
```

---

## Короткий итог

Этот prompt должен заставить Codex сделать не “красивый GitHub”, а управляемый инженерный контур: документация, AI-контекст, CI, review discipline и базовая security-гигиена.
