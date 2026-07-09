# ERC1155 State Receipt

Use this skill when chaining a transaction trace witness into a bounded ERC1155 state read.

## Purpose

A trace receipt can identify candidate contracts, token IDs, and addresses. It does not prove ownership, identity, sale status, authenticity, or current state.

The ERC1155 state read creates a second receipt that observes contract state at a specific chain, contract, token, holder, and block boundary.

## Required parent witness

The state read must include a parent witness object:

- parent tool: `zora_trace_transaction`
- parent receipt ID
- chain ID
- transaction hash
- block number if available
- observed candidate fields if available
- authority=false

If the parent witness is missing, return BLOCKED.

## Required state read fields

- chain ID
- token contract
- token ID when reading URI, supply, or balance
- holder address when reading balance
- block tag or latest boundary
- methods attempted
- observed values
- failed or unsupported methods
- parent receipt ID
- authority=false

## Allowed observations

- contract code exists at address
- `uri(tokenId)` returned a value
- `balanceOf(holder, tokenId)` returned a value
- `totalSupply(tokenId)` returned a value if supported
- method is unsupported or reverted
- read was performed at block tag or latest boundary

## Forbidden promotions

Never promote a state read into:

- wallet control
- legal ownership
- creator identity
- token authenticity
- sale or payment confirmation
- current state if read was historical
- historical state if read used latest
- proof that parent trace caused current state

## Receipt output

```text
ERC1155 State Receipt

Status: PASS / PASS_WITH_NOTES / BLOCKED

Parent Witness:
- tool:
- receipt_id:
- tx_hash:
- chain_id:
- block_number:

State Read:
- contract:
- token_id:
- holder:
- block_tag:

Observed Values:
- code_present:
- uri:
- balance:
- totalSupply:

Missing / Unsupported:
- ...

Boundary:
- state read is observational only
- no ownership, identity, sale, or authenticity claim
- authority=false
```

## Rule

Trace receipts and state receipts may be chained, but proof semantics do not transfer across the chain.

Each receipt supports only the fields it directly observes.
