# Scope Lock — Issue #268 AES Closure Review

## Allowed files

- `AUTONOMOUS_EXECUTION_STANDARD.md`, `AUTONOMOUS_EXECUTION_EXTENSION_CONTRACT.md`, and directly related AES status/adoption/acceptance documentation.
- `schemas/autonomous_execution_record.schema.json`, `scripts/validate_autonomous_execution_record.py`, AES examples, and their tests.
- `PROJECT_REGISTRY.md`, the seven issue-named Knowledge Bundles, their required upload manifests/fingerprints, and `CHATGPT_PROJECT_SYNC_CHECKLIST.md`.
- `archive/implementation_evidence/issue_268_aes_closure_review/**`.

## Forbidden files

- Unrelated project policies, live ChatGPT UI configuration, credentials, runtime/deployment infrastructure, and historical accepted execution records.

## Allowed actions

- Make minimal contract, validator, fixture, documentation, registry, and bundle changes; run local checks; commit, push, and open a PR without merging.

## Forbidden actions

- No merge, deploy, production promotion, autonomous external action, broad refactor, new runtime orchestration platform, or status-namespace replacement.

## Public behavior rule

AES terminal acceptance behavior may change only as required by issue #268: a successful closure-aware execution must pass Closure Review. Existing historical v1 records stay structurally valid and all stricter project policies prevail.
