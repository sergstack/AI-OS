# LLM Routing

## Task types

| Need | Route |
|---|---|
| Draft text | draft workflow |
| Critique | judge workflow |
| Improve | revise workflow |
| Summarize | summarize workflow |
| Extract structured facts | extraction workflow |
| Build memo | memo generation workflow |
| Choose model | model routing |
| Check output | quality gates |

## Routing rule

Before prompting, decide:
1. task type;
2. input context;
3. output format;
4. quality gate;
5. handoff target.

## Do not use LLM for

- source-of-truth calculations;
- secrets handling;
- unsupported factual claims;
- production implementation without Codex.
