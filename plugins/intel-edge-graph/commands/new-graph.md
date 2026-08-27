---
description: Scaffold an empty INTEL_EDGE_GRAPH_V0_1 instance with locked invariants. Does not populate a story.
argument-hint: "[optional graph_id]"
---

# New Intel Edge Graph

Scaffold a rigor-safe empty intel graph. Copy the empty instance, fill identifiers, leave nodes and edges empty unless `$ARGUMENTS` is only a `graph_id`.

## What this command does

1. Load `skills/intel-edge-graph/references/INTEL_EDGE_GRAPH_EMPTY_V0_1.json`.
2. Load `skills/intel-edge-graph/references/INTEL_EDGE_GRAPH_V0_1.schema.json`.
3. If `$ARGUMENTS` is a graph id, set `graph_id` to that value. Otherwise keep `INTEL_EDGE_GRAPH_EMPTY_V0_1`.
4. Set `created_at` to the current UTC timestamp.
5. Keep `nodes: []` and `edges: []`.
6. Keep invariants locked.

## Hard constraints

- Do not add story nodes.
- Do not bind FAMILY node ids.
- Do not invent `receipt_sha256`.
- Do not set `status` to `VERIFIED`.
- Do not set `authority_created` to true.
- Do not write the JSON to a git path unless the operator names the path in `$ARGUMENTS` after `WRITE_TO:`.

## Expected output

```text
Intel Edge Graph

Status: READY
graph_id: ...
edges: 0 (DECLARED=0 HOLD=0 VERIFIED=0)
family_bind: false
facts_promoted: 0
edges_inferred: 0
silent_inference: BLOCKED
authority_created: false
```

Then print the JSON instance.
