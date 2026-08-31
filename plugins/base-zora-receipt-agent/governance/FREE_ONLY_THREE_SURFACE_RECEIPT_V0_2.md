# FREE_ONLY_THREE_SURFACE_RECEIPT_V0_2

## Purpose

This document defines `FREE_ONLY_THREE_SURFACE_RECEIPT_V0_2` as a first-class governance primitive for free-only replay receipts.

The primitive records three independently observed public surfaces:

1. `TX_RECEIPT_SURFACE`
2. `LOG_SURFACE`
3. `STATE_READ_SURFACE`

It governs replay evidence only. It does not create proof of wallet control, token authenticity, creator identity, sale/payment finality, legal ownership, or internal execution.

## Primitive ID

```text
FREE_ONLY_THREE_SURFACE_RECEIPT_V0_2
```

## Required surfaces

### 1. TX_RECEIPT_SURFACE

A transaction receipt surface is admitted only when `eth_getTransactionReceipt` returns a concrete receipt for the target transaction.

Allowed observations include:

- transaction hash
- block number
- status
- gas used
- from / to when present in the receipt payload
- logs array presence

### 2. LOG_SURFACE

A log surface is admitted only when the transaction receipt contains logs and the pipeline classifies those logs by topic surface.

Allowed observations include:

- log index
- emitting contract address
- topic count
- topic0 signature
- data presence or length
- known event-surface classification where deterministic

The log surface may classify observed event shapes. It must not infer hidden internal calls.

### 3. STATE_READ_SURFACE

A state-read surface is admitted only when at least one selector-explicit `eth_call` is executed against a candidate contract derived from the observed receipt/log surface.

Allowed observations include:

- target contract
- calldata selector
- call label
- raw return data
- deterministic ABI decode where selector and return type are known

## Admission rule

A replay pipeline MAY label a result as `FREE_ONLY_THREE_SURFACE_RECEIPT_V0_2` only if all three surfaces are present:

```text
TX_RECEIPT_SURFACE=observed
LOG_SURFACE=observed
STATE_READ_SURFACE=observed
```

If any surface is missing, unavailable, malformed, or blocked, the pipeline MUST NOT label the result as `FREE_ONLY_THREE_SURFACE_RECEIPT_V0_2`.

Permitted non-admitted statuses include:

```text
BLOCKED_NO_TX_RECEIPT
BLOCKED_NO_LOG_SURFACE
BLOCKED_NO_STATE_READ
BLOCKED_RPC_ERROR
PARTIAL_FREE_ONLY_SURFACE
```

## Required boundary fields

Every `FREE_ONLY_THREE_SURFACE_RECEIPT_V0_2` receipt MUST carry:

```text
receipt_type="FREE_ONLY_THREE_SURFACE_RECEIPT_V0_2"
authority=false
free_only=true
no_fake_green=true
debug_traceTransaction="not_used"
internal_calls_observed=false
wallet_control_claim=false
creator_identity_claim=false
token_authenticity_claim=false
payment_or_sale_claim=false
```

Any deviation is a governance violation.

## Claim discipline

Pipelines MAY assert only the surfaces directly observed.

Allowed statements:

```text
tx receipt observed
logs observed and classified
state read observed
free RPC replay path works for the observed surfaces
```

Forbidden statements:

```text
wallet control proven
ownership proven
token authenticity proven
creator identity proven
sale or payment proven
internal calls observed
trace observed
legal status established
```

These forbidden statements remain forbidden unless separate, explicit, admissible evidence is observed and governed by a different primitive.

## CI / governance enforcement

A pre-merge or receipt validation gate SHOULD reject any receipt labeled `FREE_ONLY_THREE_SURFACE_RECEIPT_V0_2` if:

- `receipt_type` is missing or different
- `authority` is not `false`
- `free_only` is not `true`
- `no_fake_green` is not `true`
- `debug_traceTransaction` is not `not_used`
- `internal_calls_observed` is not `false`
- any forbidden claim flag is `true`
- any required surface is missing
- a partial surface is labeled as replay-verified

## Witness completeness gate

A run may be marked three-surface replay-observed only when:

```text
has_tx_receipt_surface=true
has_log_surface=true
has_state_read_surface=true
```

A run MUST NOT be marked replay-verified if it only contains transaction receipt data or log data without a selector-explicit state read.

## Final boundary

```text
authority=false
free_only=true
no_fake_green=true
```

This primitive witnesses public surfaces. It does not elevate them into authority.
