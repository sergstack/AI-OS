# Upload Guide — [AI OS]

## 1. Project Instructions

Скопируй весь текст из:

```text
ChatGPT/[AI OS]/PROJECT_INSTRUCTIONS.md
```

в поле **Project Instructions** существующего ChatGPT Project `[AI OS]`.

Before pasting, verify that every `PROJECT_INSTRUCTIONS.md` file is <= 8000 characters:

```bash
python3 scripts/check_project_instructions_length.py
```

If a Project Instructions file is longer than 8000 characters, do not paste it into ChatGPT Project Settings. Move supporting content into `Knowledge/` and keep Project Instructions as a compact behavior kernel.

## 2. Project Knowledge

Загрузи только эти файлы:

```text
ChatGPT/[AI OS]/Knowledge/AI_OS_PROJECT_FILES_INDEX.md
ChatGPT/[AI OS]/Knowledge/PROJECT_ROUTING.md
ChatGPT/[AI OS]/Knowledge/KB_USAGE_RULES.md
ChatGPT/[AI OS]/Knowledge/GOVERNANCE_RULES.md
ChatGPT/[AI OS]/Knowledge/AI_OS_WORKFLOW.md
ChatGPT/[AI OS]/Knowledge/HANDOFF_PROTOCOL.md
ChatGPT/[AI OS]/Knowledge/GITHUB_ISSUE_DRIVEN_HANDOFF.md
ChatGPT/[AI OS]/Knowledge/SMOKE_QA_FOR_AI_OS.md
ChatGPT/[AI OS]/Knowledge/ANTI_PATTERNS.md
```

## 3. Не загружать

Не загружай повторно весь KB package, если он уже есть.
Не загружай:

```text
zip archives
raw transcripts
source-card dumps
clean-note dumps
chunks
temp files
logs
runtime artifacts
embeddings
vector DB
secrets
.env
```

`README.md` remains local / repo guidance and is not uploaded as Project Knowledge unless explicitly intended.

## 4. После загрузки

Задай smoke questions из:

```text
SMOKE_QA_FOR_AI_OS.md
```

Минимально проверить:

1. Проект различает `KB__00_INDEX.md` и `AI_OS_PROJECT_FILES_INDEX.md`.
2. Проект маршрутизирует задачи в правильные папки.
3. Проект не выдаёт weak evidence как supported.
4. Проект не рекомендует blocked promotion items.

## 5. Статус

Этот пакет не делает `[AI OS]` production-promoted. Он только обновляет project behavior и operational memory.

## 6. Operational verification

After manual sync, record status in `CHATGPT_PROJECT_SYNC_CHECKLIST.md`, run smoke QA from `SMOKE_QA_REFRESH_PLAN.md`, and complete the relevant pilot in `PILOT_CASES.md`.

## 7. Compact Knowledge bundles

Use `ChatGPT/[Project]/Knowledge_Bundles/UPLOAD_LIST.md` when uploading compact bundle files into ChatGPT Sources.

Granular `Knowledge/` files remain the source of truth. Upload bundles OR granular files, not both, unless debugging a sync issue.

For analytical memo production, upload bundle files that include the `Analytical Memo Factory via Codex APP` workflow. Do not upload granular and bundle files together unless debugging.
