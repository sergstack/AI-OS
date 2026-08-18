# Security Policy

## Supported scope

Security reports are accepted for the current `main` branch and its repository
workflows, validation scripts, prompt-execution helpers, and published
configuration artifacts.

Historical files under archive paths, unmerged branches, candidate physical
Stream Deck setups, and external ChatGPT Project configuration are not supported
versions. They may still be relevant evidence when a current vulnerability can
be reproduced from them.

This support statement does not claim production readiness or deployment.

## Report a vulnerability privately

Do not open a public issue for a suspected vulnerability. Use GitHub's
[private vulnerability reporting](https://github.com/sergstack/AI-OS/security/advisories/new).

Include only the minimum information needed to reproduce and assess the issue:

- affected path, workflow, or component;
- impact and realistic attack scenario;
- bounded reproduction steps;
- affected commit or branch;
- suggested mitigation, if known.

Do not submit credentials, API keys, `.env` contents, client data, raw financial
data, private ChatGPT content, browser storage, or unrelated personal data.
Sanitize examples before attaching them.

## Handling

The repository owner will review the report, request clarification when needed,
and coordinate disclosure through the private advisory. No response or repair
service-level agreement is promised.

Repository fixes remain subject to the normal branch, validation, owner-review,
and merge gates. A security report does not authorize external access,
deployment, credential rotation, or production changes by Codex.
