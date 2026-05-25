# Decision Status and Revisit Trigger

## Purpose

Define the standard for decision status tracking and revisit conditions.

## Decision statuses

- `draft`
- `candidate decision`
- `recommended`
- `blocked`
- `handoff required`
- `accepted`
- `deprecated`

## Revisit triggers

- new data;
- changed cost, risk, timing, or scope;
- QA fail;
- assumption invalidated;
- implementation feedback contradicts decision;
- owner rejects hypothesis;
- decision becomes irreversible.

## Requirement

Require status plus revisit trigger for:

- strategic decisions;
- budget or process decisions;
- handoff tasks;
- anything saved as a reusable decision record.

## Minimum record

Every reusable decision record should state:

- decision;
- status;
- confidence;
- owner;
- revisit trigger;
- next review;
- handoff;
- link or source.
