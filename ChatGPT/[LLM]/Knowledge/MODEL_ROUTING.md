# Model Routing

## Routing criteria

| Need | Model style |
|---|---|
| Fast draft | fast model |
| Hard reasoning | reasoning model |
| Long context synthesis | long-context model |
| Local/private draft | local/Ollama |
| Critique | judge model |
| Rewrite | balanced model |
| Code implementation | route to Codex |

## Rule

Model routing is guidance, not a factual claim about current model capabilities. For current prices, limits, API details or release status, verify with fresh sources.

Route by model class rather than permanent model name.

## Primary gates

1. task type;
2. risk / error cost;
3. privacy;
4. verification path.

Use reasoning need, context length, latency, cost, and tool access as secondary factors or tie-breakers. Do not require a numerical scoring matrix.

```text
task type
-> can deterministic/tool verification solve or constrain it?
-> risk / error cost
-> privacy constraint
-> required verification path
-> cheapest suitable model class
-> Judge/escalation when required
```

Routing ownership remains:

- deterministic calculation -> `[Analytics]`;
- implementation and tests -> `[Codex]`;
- AI KB evidence and canonical governance -> `[AI OS]`;
- prompt, context, model-routing, and workflow eval -> `[LLM]`.

## Selection checklist

- task type;
- risk / error cost;
- privacy;
- verification path;
- reasoning need;
- context length;
- latency and cost;
- tool access and quality gate.
