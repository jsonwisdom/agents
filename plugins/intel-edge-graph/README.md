# Intel Edge Graph

Foreign-graph lab for intel stories. Same sealed rigor as the JOY FAMILY edge graph, on a **separate namespace**.

**Jason is the brains. Jay is the labor.** This plugin records outlet/official/document claims. It does not bind family nodes, promote story to evidence, or flip `authority_created`.

## What you get

### Agent

- **intel-edge-graph-witness** — witness-only classifier for intel edges. Default `authority=false`.

### Agent Skill

- **intel-edge-graph** — instantiate, classify, and hold `INTEL_EDGE_GRAPH_V0_1` objects. Load `references/INTEL_EDGE_GRAPH_V0_1.schema.json` before writing JSON.

### Command

- `/intel-edge-graph:new-graph` — scaffold the empty instance. Does not populate a story.

## Membrane

```text
INTEL_GRAPH != FAMILY_GRAPH
STORY_FORM != EVIDENCE
CLAIMS != GUILT
PRESS_SUMMARY != OFFICIAL_TRANSCRIPT
ANONYMOUS_SOURCE != VERIFIED
CONFIDENCE != PROMOTION
MISSING_RECEIPT_SHA256 => DECLARED | HOLD
SILENCE IS A VALID GRAPH STATE
```

## Default invariants

```text
authority_created = false
facts_promoted    = 0
edges_inferred    = 0
silent_inference  = BLOCKED
family_bind       = false
```

Do not populate a concrete story graph unless the operator names the instance and accepts `DECLARED` edges.

## Install

```bash
/plugin install intel-edge-graph@claude-code-workflows
```

## License

MIT
