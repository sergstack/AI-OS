# Upload Guide — [AI OS]

## 0. Repo-first sync model

Daily work uses GitHub as the current source of truth. ChatGPT Project Knowledge is a bootloader/cache for stable baseline uploads, not live state for every small repo change.

Manual paste/upload through the ChatGPT Project UI is a formal periodic sync. Do not reupload Knowledge for every small repository change. Use compact bundles only when refreshing a stable baseline.

See `SYNC_CONTRACT.md` before deciding whether a ChatGPT UI upload is needed.

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

Default upload mode: `Knowledge_Bundles`.

Default mode: use the project bundle upload list as the authoritative manual upload list:

```text
ChatGPT/[AI OS]/Knowledge_Bundles/UPLOAD_LIST.md
```

Для default bundle sync загружай только эти файлы: bundle files listed in that project's `Knowledge_Bundles/UPLOAD_LIST.md`.

Granular `Knowledge/` upload from `ChatGPT/[AI OS]/Knowledge/` is advanced/debug mode only. Do not upload both bundles and granular Knowledge files unless debugging a sync issue.

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

Use `ChatGPT/[Project]/Knowledge_Bundles/UPLOAD_LIST.md` when uploading bundle files into ChatGPT Sources.

Granular `Knowledge/` files and the GitHub repository remain the source of truth. `Knowledge_Bundles` is the default upload mode; granular Knowledge upload is advanced/debug mode only. Upload bundles OR granular files, not both, unless debugging a sync issue.

### Replace a changed bundle without duplicate Sources

For a changed bundle, replace only that bundle in the matching ChatGPT Project:

1. identify the canonical filename from `UPLOAD_LIST.md`;
2. remove the older Source with the same semantic filename, including any UI-added
   suffix such as `(1)` or `(2)`;
3. upload the current repository bundle under its canonical filename;
4. read back the Sources list and confirm exactly one file matches that canonical
   filename.

Record the observed replacement and any affected smoke QA in
`CHATGPT_PROJECT_SYNC_CHECKLIST.md`. A replaced filename proves only source
transport; it does not prove behavioural smoke QA, owner acceptance, or
production authorization.

For analytical memo production, upload bundle files that include the `Analytical Memo Factory via Codex APP` workflow. Do not upload granular and bundle files together unless debugging.

For `[Thinkers OS]`, `ChatGPT/[Thinkers OS]/Knowledge_Bundles/UPLOAD_LIST.md` is the sole authoritative manual upload list. Its granular `Knowledge/` files remain repository source of truth and are not part of the standard upload. Do not upload raw or normalized books, OCR dumps, manifests, execution logs, local absolute paths, or blocked/rejected artifacts.
