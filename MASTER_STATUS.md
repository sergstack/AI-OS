# Master Status

## Repository Governance

- status: governance-validation-added
- last_checked: 2026-06-15
- production_promotion: no

## Validation Gates

- Project instructions length: <= 8000 chars
- Public safety scan: required
- No raw absolute local paths: required
- Manifest/path consistency: required
- Smoke QA: required
- Pilot case: required before production promotion

## Project Instructions Rule

`PROJECT_INSTRUCTIONS.md` is the compact behavior kernel for each ChatGPT Project.

Use `Knowledge/` for supporting policies, templates, examples, checklists, and detailed workflows.

If `PROJECT_INSTRUCTIONS.md` exceeds 8000 characters, do not paste it into ChatGPT Project Settings. Split supporting content into `Knowledge/` and keep only routing, scope, evidence, output, and critical safety rules in Project Instructions.
