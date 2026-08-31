# ERC1155 Lattice Migration Tracker

## Purpose

This document tracks the remaining lattice migration gap for `base-zora-erc1155.json`.

It is intentionally a tracker, not a completed migration.

## Target file

```text
plugins/base-zora-receipt-agent/mcp-servers/base-zora-erc1155.json
```

## Current gap

The ERC1155 MCP spec does not yet declare the full adapter lattice fields required by the multi-surface adapter policy:

```text
adapter_id
surface_level
free_only
no_fake_green
```

## Why this is not patched by analogy

The ERC1155 MCP spec currently describes a state-read path chained from a parent trace receipt:

```text
parent_witness_required=true
allowed_parent_tools=zora_trace_transaction
```

Because the free-only three-surface primitive requires:

```text
debug_traceTransaction="not_used"
internal_calls_observed=false
free_only=true
```

it would be unsafe to mark the existing ERC1155 spec as `free_only=true` or `THREE_SURFACE_V0_2` without first deciding whether ERC1155 has:

1. a trace-chained adapter path, or
2. a separate free-only ERC1155 state-read adapter path.

## Current determination

```text
status=BLOCKED_PENDING_ADAPTER_PATH_DECISION
authority=false
no_fake_green=true
```

## Safe next options

### Option A — Trace-chained ERC1155 adapter

Keep the existing ERC1155 parent trace dependency and declare it as a non-free-only adapter.

This would NOT be a `FREE_ONLY_THREE_SURFACE_RECEIPT_V0_2` adapter.

### Option B — Free-only ERC1155 state-read adapter

Create a separate MCP spec for a free-only ERC1155 read path, for example:

```text
plugins/base-zora-receipt-agent/mcp-servers/base-erc1155-state-read.json
```

That spec could declare free-only selector-explicit state reads such as:

```text
uri(uint256)
balanceOf(address,uint256)
totalSupply(uint256)
```

Only this separate path should be considered for:

```text
free_only=true
surface_level=THREE_SURFACE_V0_2
receipt_type=FREE_ONLY_THREE_SURFACE_RECEIPT_V0_2
```

## Definition of done

This tracker is resolved only when one of the following occurs:

1. The existing `base-zora-erc1155.json` is explicitly classified as trace-chained and not free-only, or
2. A separate free-only ERC1155 adapter spec is added and the free-only lattice fields are applied there.

## Non-claims

This tracker does not assert:

- ERC1155 runtime evidence exists.
- ERC1155 three-surface receipt evidence exists.
- ERC1155 trace evidence exists.
- ERC1155 ownership, authenticity, creator identity, payment, or sale semantics.

## Final boundary

```text
authority=false
no_fake_green=true
```
