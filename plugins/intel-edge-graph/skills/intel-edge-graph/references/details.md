# Intel edge graph — FAMILY-mirror rules

This file is the long form. The skill body is the fence. Schema: `INTEL_EDGE_GRAPH_V0_1.schema.json`. Scaffold: `INTEL_EDGE_GRAPH_EMPTY_V0_1.json`.

## Why a foreign graph

The JOY FAMILY graph (`FAMILY/graph/FAMILY_EDGE_GRAPH_V1_1.json`) records kinship with sealed local promotion. Intel stories (outlet claims, official travel, documents) must not inherit those edges.

```text
FAMILY_EDGE_GRAPH  = kinship, origin-gated, silence valid
INTEL_EDGE_GRAPH   = claims about public objects, origin-gated, silence valid
CROSSWALK          = FORBIDDEN
```

`family_bind` is a schema `const: false`. Node IDs must match `^INTEL_[A-Z0-9_]+$`. The empty instance lists current FAMILY `node_id` values under `forbidden_node_ids`.

## Mirror of FAMILY sealed rules

| FAMILY rule | Intel equivalent |
|---|---|
| `EVIDENCE_CLASS_NE_RELATIONSHIP_STATE` | `evidence_type` is not `status` |
| `KNOWN_NODE_NE_KNOWN_EDGE` | A node can exist with zero edges |
| `KNOWN_EDGE_NE_ADJACENT_EDGE` | Neighboring intel edges do not create a third |
| `SHARED_OBJECT_NE_RELATIONSHIP_BETWEEN_SUBJECTS` | Two outlets quoting the same official does not bind the outlets |
| `EVIDENCE_FOR_EDGE_A_NE_EVIDENCE_FOR_EDGE_B` | One hash, one edge |
| `SILENCE_IS_VALID_GRAPH_STATE` | Empty `edges` is valid |
| `HOLD_UNSPECIFIED_NE_INVITATION_TO_GUESS` | `HOLD` is not a prompt to fill |
| `EDGE_PROMOTION_IS_LOCAL_ONLY` | `VERIFIED` does not promote neighbors or `authority_created` |

FAMILY origin allow-list for asserted edges: `USER_DECLARED`, `DOCUMENT_SOURCE_BOUND`, `PERSON_CONFIRMED`.

Intel origin allow-list:

- `USER_DECLARED` — Jason named the claim
- `DOCUMENT_SOURCE_BOUND` — a cited document bytes exist
- `ON_RECORD_QUOTE_BOUND` — an on-record quote with a locator
- `EXPLICIT_HOLD` — required when `status=HOLD`

Forbidden origins (not in the enum, so they cannot be stored):

- `MACHINE_GENERATED`
- `ADJACENCY_DERIVED`
- `STORY_FORM_DERIVED`
- `FAMILY_INHERITED`
- `SOCIAL_EXPECTATION_DERIVED`

## Node kinds

Allowed: `OUTLET`, `OFFICIAL`, `STATE_ENTITY`, `EVENT`, `DOCUMENT`, `LOCATION`.

`OFFICIAL` is a public-role story node (title, office, named public figure as reported). It is not a family person and must not reuse a FAMILY `node_id`.

Do not add `PERSON`, `FAMILY_MEMBER`, `WALLET`, or `COIN`.

## Promotion gate

`status=VERIFIED` is valid in the schema only when all of these hold:

1. `evidence.receipt_sha256` matches `^[a-f0-9]{64}$`
2. `evidence.source_ref` is present
3. `evidence.evidence_type` is not `ANONYMOUS_SOURCE` or `PRESS_SUMMARY`
4. `predicate` is not `ATTRIBUTES_MOTIVE`
5. `origin` is `DOCUMENT_SOURCE_BOUND` or `ON_RECORD_QUOTE_BOUND`

Until those are true, use `DECLARED` or `HOLD`.

`confidence` is advisory. A `1.0` confidence with no hash stays `DECLARED`.

`facts_promoted` counts promotions Jason accepts. The empty scaffold starts at `0`. Do not increment it because an edge became `VERIFIED`. Jason increments it.

`authority_created` stays `false` unless Jason sets it on the graph. Edge-level `authority_created` is schema-const `false`.

## What not to do

- Do not copy FAMILY nodes into this graph.
- Do not infer motive, guilt, or fraud from a missing file.
- Do not treat a press summary as a transcript.
- Do not treat an anonymous source as verified.
- Do not invent `receipt_sha256`.
- Do not populate a named story instance unless the operator asks for that instance in the current turn.
- Do not write the JSON into a git repository unless the operator names the path.

## Empty scaffold

`INTEL_EDGE_GRAPH_EMPTY_V0_1.json` has zero nodes and zero edges. That is a valid graph. Copy it, then add objects.

## Next instance

A concrete story graph (for example a CIA/Moscow trip) is a **later operator turn**. This schema and empty instance are Path A. Path A does not pre-load story nodes.
