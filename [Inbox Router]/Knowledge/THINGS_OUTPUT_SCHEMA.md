# Things Output Schema

Use this schema only when the destination is a concrete Things task.

```text
Destination: Things
Title:
Area:
Project:
Next action:
Status: Today / Anytime / Someday / Waiting / Cancel
Deadline: YYYY-MM-DD / none
Context:
Energy: low / medium / high
Estimated time:
Blocker:
```

## Rules

- Do not use Things as a knowledge base.
- Do not create fake deadlines.
- Do not send implementation work to Things directly without a clear next action.
- If the item is context or reference material, route to Notes / Obsidian.
- If the item needs strategy, calculation, prompt work, or implementation, create a project handoff.
