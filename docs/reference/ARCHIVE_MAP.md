# Archive Map — AI OS Project Settings v05

```text
AI_OS_Project_Settings_v05/
├── docs/
│   └── reference/
│       └── ARCHIVE_MAP.md
├── MANIFEST.json
├── MANIFEST.md
├── UPLOAD_GUIDE.md
└── ChatGPT/
    └── [AI OS]/
        ├── README.md
        ├── PROJECT_INSTRUCTIONS.md
        └── Knowledge/
            ├── AI_OS_PROJECT_FILES_INDEX.md
            ├── PROJECT_ROUTING.md
            ├── KB_USAGE_RULES.md
            ├── GOVERNANCE_RULES.md
            ├── AI_OS_WORKFLOW.md
            ├── HANDOFF_PROTOCOL.md
            ├── SMOKE_QA_FOR_AI_OS.md
            └── ANTI_PATTERNS.md
```

## Назначение

Пакет предназначен только для существующей папки `[AI OS]`, где уже загружена governed KB.

## Два индекса

| Индекс | Где находится | Роль |
|---|---|---|
| `KB__00_INDEX.md` | уже в Project Knowledge | Индекс базы знаний |
| `AI_OS_PROJECT_FILES_INDEX.md` | в этом пакете | Индекс новых рабочих файлов |

## Upload policy

Загрузить в Project Knowledge только файлы из `Knowledge/`.
`README.md` хранить локально как инструкцию по установке.
`PROJECT_INSTRUCTIONS.md` скопировать в поле Project Instructions.

## Validation policy

Every `PROJECT_INSTRUCTIONS.md` file must be <= 8000 characters.
If a file exceeds the limit, move supporting content into `Knowledge/`.
