# StreamDeck v2.8 MCP Actions Pilot

Status: pilot passed / candidate-only
Profile targeted: `AI OS StreamDeck v2.8 Candidate`
Safety mode: supervised only
Promotion status: candidate only

## Observed Workflow

Sergey wrote a message.

ChatGPT used the StreamDeck MCP action `AIOS_HOME_JUDGE`.

ChatGPT then used the StreamDeck MCP action `AIOS_HOME_REVISOR`.

The flow produced a reviewed and revised output for human acceptance.

Workflow:

```text
Draft -> Judge -> Revisor -> human acceptance
```

## Pilot Result

| Item | Result |
|---|---|
| MCP available | yes |
| Actions visible | yes |
| Actions executed | `AIOS_HOME_JUDGE`, `AIOS_HOME_REVISOR` |
| Workflow verdict | pass |
| Safety mode | supervised only |
| Destructive actions | none |
| Auto-send | no |
| Merge / publish / deploy | no |
| v2.8 status | candidate-only |
| v2.7 status | untouched |

## Safety Boundaries

- The pilot used supervised MCP actions only.
- No destructive actions were executed.
- No auto-send action was used.
- No merge, publish, or deploy action was used.
- v2.8 remains candidate-only.
- v2.7 was not modified.
- Human acceptance remains required before treating the output as final.

## Residual Risks

- The pilot confirms this two-action workflow only, not the full v2.8 action set.
- Physical StreamDeck device behavior, timing, focus state, and text insertion context may still vary by active application.
- MCP action descriptions and button mappings can drift from the repository records if changed manually in the Stream Deck app.
- Supervised-only safety depends on keeping auto-send, destructive, merge, publish, deploy, and secret-handling actions out of the MCP Actions profile.
- v2.8 must remain candidate-only until broader smoke QA and Sergey acceptance are recorded.

## Next Step

Expand the pilot to 5-7 safe actions while preserving supervised-only behavior, no auto-send, no destructive actions, no merge, no publish, no deploy, v2.8 candidate-only status, and v2.7 untouched status.
