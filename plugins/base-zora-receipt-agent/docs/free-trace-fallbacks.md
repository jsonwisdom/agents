# Free-Only Trace Fallbacks

## Constraint

Free solutions only.

Do not require paid RPC tiers, cloud archive nodes, or bill-risk infrastructure.

## Observed blocker

- Chain: Base mainnet / `8453`
- Target tx: `0xc4b8d203688a0bf1b04345a65719d02d4feef3e9354f7e49f4291a1a8da24178`
- Requested method: `debug_traceTransaction`
- Tracer: `callTracer`
- Observed blocker: Alchemy authenticated successfully, but `debug_traceTransaction` is unavailable on the Free tier.
- Receipt: `plugins/base-zora-receipt-agent/receipts/blocked-trace-rpc-tier-limit.json`

## Current admissible state

```text
Status: BLOCKED_TIER_LIMIT
Trace observed: false
State read executed: false
Runtime validation: false
authority=false
```

The blocker receipt is valid evidence of the failure mode. It is not a trace receipt.

## Free-only strategy

### 1. Public explorer fallback

Use public explorer-visible fields:

- transaction hash
- block number
- from / to
- status
- gas used
- logs if visible
- decoded token transfer events if visible

Boundary: explorer evidence can support only observed transaction/log fields. It cannot replace internal execution tracing.

### 2. Standard JSON-RPC fallback

Use free standard RPC methods where available:

- `eth_getTransactionByHash`
- `eth_getTransactionReceipt`
- `eth_getLogs`
- `eth_getCode`
- `eth_call`

Boundary: standard RPC can support receipt/log/state evidence, but not full internal call-tree evidence.

### 3. ERC1155 state fallback

If contract and token ID can be identified from logs or explorer data, run read-only state checks:

- `eth_getCode`
- `uri(uint256)`
- `balanceOf(address,uint256)`
- `totalSupply(uint256)` if supported

Boundary: state reads are observational only. They do not prove wallet control, legal ownership, creator identity, token authenticity, sale, or payment.

### 4. No Cloud Shell archive node

Do not run Erigon/Base archive inside Google Cloud Shell.

Cloud Shell is ephemeral and not suitable for persistent archive-node operation. This would create bill and reliability risk.

## Next admissible free evidence

- Standard transaction receipt from `eth_getTransactionReceipt`
- Logs from the transaction receipt
- Explorer-visible token transfer events
- ERC1155 state read from identified contract/token ID

## Forbidden claims

Do not claim:

- trace observed
- internal calls observed
- wallet control
- legal ownership
- creator identity
- token authenticity
- sale/payment confirmation
- production validation

unless the exact evidence is observed and recorded.

## Final boundary

```text
authority=false
no_fake_green=true
free_only=true
```
