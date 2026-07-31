# Scope Lock — Thinkers OS Integration

## Allowed files

- `ChatGPT/[Thinkers OS]/**`
- `PROJECT_REGISTRY.md`
- `REPO_PATHS.md`
- `UPLOAD_GUIDE.md`
- `ChatGPT/[Inbox Router]/Knowledge/ROUTING_RULES.md`
- `ChatGPT/[AI OS]/Knowledge/PROJECT_ROUTING.md`
- `scripts/check_manifest_paths.py`
- `scripts/check_knowledge_bundles.py`
- `scripts/check_index_coverage.py`
- `tests/test_validation_scripts.py`
- `tests/test_thinkers_os_integration.py`
- `docs/thinkers_os_integration/**`

## Forbidden files

- `MANIFEST.json` and `MANIFEST.md`, which remain scoped to the `[AI OS]` package.
- Existing project files outside the two allowed routing files.
- Raw or normalized Thinkers OS source material and source manifests.
- Secrets, environment files, runtime artifacts, logs, archives, embeddings, and vector databases.
- GitHub workflows, deployment files, and remote/external ChatGPT state.

## Allowed actions

- Create the bounded local `[Thinkers OS]` package and planning/acceptance evidence.
- Add minimal registry, routing, upload-guidance, validator, and test entries.
- Run local read-only validators, tests, hashes, searches, and status checks.
- Make one local in-scope correction after a failed check.
- Stage only scoped files, commit them, and push `agent/thinkers-os-integration` to `origin` after all checks pass.

## Forbidden actions

- Merge, deploy, publish packages, upload Project Sources, or create/modify an external ChatGPT Project.
- Push any branch other than `agent/thinkers-os-integration` or push before validation passes.
- Download or copy copyrighted source payloads into this repository.
- Promote artifacts to validated/canonical or authorize production.
- Broaden existing project responsibilities or refactor unrelated validators.

## Public behavior rule

Public routing may change only by recognizing the bounded `[Thinkers OS]` responsibility and distinguishing maintenance from application. Existing project responsibilities and all production behavior remain unchanged.
