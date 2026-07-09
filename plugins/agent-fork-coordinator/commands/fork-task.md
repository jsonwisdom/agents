# fork-task

Create a bounded witness-only side task for research, debugging, PR analysis, receipt checking, on-chain evidence review, or public-record review.

## Behavior

Define a fork task with clear scope, allowed tools, disallowed actions, expected evidence, and stop conditions.

Return a coordinator report that can be used by a subagent or specialist without losing the main thread's working state.

## Required inputs

- objective
- task type
- scope boundary
- allowed sources or tools
- expected output
- stop condition

## Hard constraints

- Do not create an open-ended task.
- Do not authorize repository, filesystem, wallet, deployment, or API mutations.
- Do not treat MCP tool discovery as permission to execute.
- Do not merge fork findings into the main thread without observed evidence.
- If the task needs write access, return an approval gate instead of acting.

## Expected output

```text
Fork Coordinator Report

Status: READY / PASS_WITH_NOTES / BLOCKED

Fork Task:
- Name:
- Objective:
- Scope:

Assigned Specialist:
- ...

Allowed Tools / MCP Surfaces:
- ...

Disallowed Actions:
- ...

Expected Evidence:
- ...

Stop Condition:
- ...

Main Thread Use:
- ...

Approval Gate:
- ...

Final Determination:
- authority=false
- witness-only
```
