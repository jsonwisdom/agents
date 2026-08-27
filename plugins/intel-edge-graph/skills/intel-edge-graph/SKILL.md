---
name: intel-edge-graph
description: Instantiate and classify INTEL_EDGE_GRAPH_V0_1 for intel stories without binding the FAMILY graph. Use when recording outlet claims, official quotes, state-entity events, or document edges; when a news story needs a rigor-safe graph; or when an agent is about to mix family nodes with intel nodes. Use PROACTIVELY before promoting any intel edge past DECLARED.
---

# Intel Edge Graph v0.1

A foreign graph for intel stories. Mirrors FAMILY edge-graph rigor. Never joins the family graph.

Load `references/details.md` before classifying an edge. Load `references/INTEL_EDGE_GRAPH_V0_1.schema.json` before writing JSON. Start from `references/INTEL_EDGE_GRAPH_EMPTY_V0_1.json`.

## When to Use

- Recording what an outlet claims about an official, state entity, event, document, or location
- Keeping a news or intel story off the FAMILY graph
- Deciding whether an edge is `DECLARED`, `HOLD`, `DISPUTED`, `REJECTED`, or `VERIFIED`
- An operator asks for Path A / intel edge graph / foreign-graph lab

## Hard membrane

```text
INTEL_GRAPH != FAMILY_GRAPH
STORY_FORM != EVIDENCE
CLAIMS != GUILT
PRESS_SUMMARY != OFFICIAL_TRANSCRIPT
ANONYMOUS_SOURCE != VERIFIED
ATTRIBUTES_MOTIVE != VERIFIED
CONFIDENCE != PROMOTION
MISSING_RECEIPT_SHA256 => status in {DECLARED, HOLD}
SILENCE IS A VALID GRAPH STATE
HOLD != INVITATION TO GUESS
```

Forbidden node kinds: `PERSON` (use `OFFICIAL` only for a public role), `FAMILY_MEMBER`, `WALLET`, `COIN`.

Forbidden `node_id` values: any FAMILY graph id (`DADDY_JAY`, `HEIDEE`, …). See `forbidden_node_ids` on the empty instance.

## Default invariants

```text
authority_created = false
facts_promoted    = 0
edges_inferred    = 0
silent_inference  = BLOCKED
family_bind       = false
```

Only Jason may set `authority_created=true`. A `VERIFIED` edge does not flip it.

## Edge status

| Status | Allowed when |
|---|---|
| `HOLD` | Missing source, missing hash, or operator hold |
| `DECLARED` | Operator or document declared the claim; no receipt hash yet |
| `DISPUTED` | A second bound source contradicts the first |
| `REJECTED` | Operator rejects the edge |
| `VERIFIED` | `receipt_sha256` is a 64-char hex digest **and** `evidence_type` is not `ANONYMOUS_SOURCE` or `PRESS_SUMMARY` **and** predicate is not `ATTRIBUTES_MOTIVE` |

New edges default to `DECLARED` if origin is `USER_DECLARED` or `DOCUMENT_SOURCE_BOUND` without a hash. Otherwise `HOLD`.

Forbidden origins for asserted edges: `MACHINE_GENERATED`, `ADJACENCY_DERIVED`, `STORY_FORM_DERIVED`, `FAMILY_INHERITED`, `SOCIAL_EXPECTATION_DERIVED`.

## Procedure

1. Copy the empty instance. Fill `graph_id`, `version`, `created_at`.
2. Add nodes from the allowed kinds only.
3. Add edges with `origin`, `predicate`, `evidence.evidence_type`, and `status`.
4. Leave `receipt_sha256` absent until a real hash exists. Do not invent one.
5. Classify. Do not infer a missing edge from two neighboring edges.
6. Return the JSON plus a one-line invariant block. Stop.

Do not populate a named story (including CIA/Moscow/Ratcliffe) unless the operator asks for that instance in this turn.

## Output

```text
Intel Edge Graph

Status: READY / HOLD / BLOCKED
graph_id: ...
edges: N (DECLARED=x HOLD=y VERIFIED=z)
family_bind: false
facts_promoted: 0
edges_inferred: 0
silent_inference: BLOCKED
authority_created: false
```

Then print the JSON. Do not write it to a git repo unless the operator names the path.

## Related

Companion: `computer-wisdom-assistant` skills `bounded-authority` and `evidence-first-judgment`.
See `references/details.md` for FAMILY-mirror rules, promotion gates, and the empty instance.
