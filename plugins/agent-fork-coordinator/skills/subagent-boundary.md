# Subagent Boundary

Use this skill when coordinating background subagents, forked research tasks, debugging branches, PR witness tasks, MCP tool use, or specialist delegation.

## Boundary model

A subagent is allowed to observe, analyze, summarize, and recommend.

A subagent is not allowed to mutate state unless the operator approves the exact action.

## Required fork fields

| Field | Purpose |
|---|---|
| task name | stable handle for the fork |
| objective | what the fork is trying to learn or resolve |
| scope | what is inside and outside the task |
| allowed tools | read-only tools or approved MCP surfaces |
| disallowed actions | mutations, approvals, deployments, signing, spending |
| expected evidence | citations, logs, receipts, hashes, diffs, tx references |
| stop condition | when the fork must return |
| return format | bounded report shape |

## Unsafe delegation patterns

- vague task with no stop condition
- broad repo mutation authority
- wallet or signing authority
- deployment authority
- approval or merge authority
- unstated tool permissions
- hidden assumptions from main context
- specialist output promoted as fact without evidence

## MCP permission boundary

Classify tools before use:

- read-only
- write-capable
- destructive
- financial/signing
- identity/authentication
- external-publication

Write-capable, destructive, financial, signing, identity, or publication actions require explicit operator approval.

## Safe return language

Use:

- observed
- reported
- evidence found
- evidence missing
- blocked pending approval
- requires operator decision
- authority=false

## Rule

Parallelism is allowed. Unbounded authority is not.

If a fork cannot state its scope, evidence requirement, and stop condition, it must not start.
