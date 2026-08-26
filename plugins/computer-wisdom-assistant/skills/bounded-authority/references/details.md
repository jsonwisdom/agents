# Authority fences, stop conditions, and unsafe delegation

Use this file when a task is large, involves MCP, or the operator is about to grant write access.

## Stop-condition recipes

A stop condition is a sentence that, when true, ends the work.

Good:

```text
Stop when the workflow run for SHA abc123 is observed as success, failure, or missing.
Stop after listing the three cheapest measurements, even if none have been run.
Stop if the file does not exist in this workspace.
```

Bad:

```text
Stop when it looks good.
Stop when the user is happy.
Stop after investigating thoroughly.
```

"Thoroughly" is not a fence. Replace it with a countable artifact.

## Unsafe delegation patterns

Do not start a side task that has:

- no stop condition
- broad repo mutation rights
- wallet, signing, or spend rights
- deploy or merge rights
- unstated tool permissions
- hidden assumptions copied from the main thread
- specialist output promoted as fact without evidence

Parallel work is fine. Unbounded authority is not.

## MCP and external tools

Before any external tool:

1. Name the server and tool.
2. State the purpose in one line.
3. Classify permission (read-only through publication).
4. State the risk boundary.
5. State whether this exact call is approved.

Discovery is not permission. Listing tools is read-only. Invoking a write-capable tool is not.

Default transport and scope are the operator's to set. If they are unknown, return `BLOCKED` rather than guessing a privileged default.

## Main thread vs side task

Keep the original question moving. A side task returns a packet:

```text
Side task packet
- name
- bound (copy of Authority Bound)
- observed
- missing
- recommendation
- authority=false
```

Do not merge the packet into "the work is done" without `skills/evidence-first-judgment`.

## Mutation language

The operator approves actions, not vibes.

| Operator said | Bound |
|---|---|
| "you may edit that file" | that path, not the tree |
| "fix tests" | failing tests in scope; no drive-by refactors |
| "ship it" | publication gate still required |
| "use whatever tools you need" | still classify; still gate writes |

If the approval is broader than the objective, narrow it in the bound you write back. The written fence is what later sessions should replay.

## Pairing with other skills

- Evidence of a completed mutation still needs `skills/evidence-first-judgment`.
- The bound itself should be replayable via `skills/replayable-reasoning`.
- A request to "build a platform so this is easier next time" is a complexity question: `skills/complexity-budget`.
