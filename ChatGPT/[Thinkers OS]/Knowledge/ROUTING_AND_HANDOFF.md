# Routing and Handoff

Canonical destination routing is defined in repo-root `ROUTING_RULES.md`.
`[Thinkers OS]` prepares bounded handoffs; it does not absorb the receiving project's work.
For the local boundary: source request/intake remains corpus work here; a real
decision routes to `[Thinking]`; an extraction prompt routes to `[LLM]`;
repository implementation routes to `[Codex]`; quantitative validation routes
to `[Analytics]`.

## Handoff contract

Use one receiving project and the canonical fields in `HANDOFF_STYLE_STANDARD.md`.

Add author/corpus coverage, source artifact, Judge status, and transfer risk when the handoff uses thinker evidence.

## Handoff gates

- No Judge-pass pattern: do not export.
- Partial corpus: label the handoff bounded/partial and name the missing P1 gap.
- Quantitative claim: require `[Analytics]` evidence.
- Repository mutation: require `[Codex]` scope, checks, rollback, and acceptance.
- External Project sync: manual owner action unless explicitly authorized.

Forbidden inputs include secrets, raw/normalized books, excerpt dumps, source manifests, logs, local paths, and blocked/rejected artifacts.
