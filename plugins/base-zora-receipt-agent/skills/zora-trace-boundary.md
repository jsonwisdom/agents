# Zora Trace Boundary

Use this skill when reviewing Base or Zora transaction traces, ERC1155 mints, token transfers, internal calls, reverts, gas behavior, and receipt-linked on-chain evidence.

## Trace methods

Prefer `debug_traceTransaction` with:

- `callTracer` for call tree, internal calls, value movement, reverts, gas, and contract interactions.
- `prestateTracer` for account/storage prestate context when available.

Use archive or trace-enabled RPC providers for full historical trace coverage.

## Required evidence

For each trace receipt, require:

- chain ID
- transaction hash
- block number if available
- RPC provider class or source class
- tracer used
- status
- gas used if available
- calls observed
- revert reason if available
- missing fields
- authority=false

## ERC1155 evidence boundaries

Allowed observations:

- contract code is present
- `uri(tokenId)` returned value
- `balanceOf(address, tokenId)` returned value
- `totalSupply(tokenId)` returned value if supported
- internal mint-like or transfer-like calls were observed in trace

Forbidden promotions:

- balance means wallet control
- token page means creator identity
- factory context means authenticity
- trace observation means legal ownership
- successful transaction means off-chain agreement
- profile presence means provenance

## Error boundaries

Return BLOCKED when:

- transaction hash is malformed
- transaction is not found on selected chain
- RPC does not support `debug_traceTransaction`
- trace result cannot be tied to tx hash and chain ID
- claim exceeds observed trace fields

Return PASS_WITH_NOTES when:

- trace is observed but block context is missing
- token read succeeds but optional metadata methods are unavailable
- GraphQL enrichment is unavailable but raw RPC evidence exists

## Safe language

Use:

- trace observed
- call observed
- contract read observed
- method returned
- evidence missing
- blocked pending trace-enabled RPC
- authority=false

Never use:

- proves ownership
- proves creator identity
- verified provenance
- wallet controlled
- sale confirmed
- production validated

unless independent transaction-grade, signature-grade, or source-grade evidence supports that exact claim.
