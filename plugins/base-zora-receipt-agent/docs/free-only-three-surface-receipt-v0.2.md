# FREE_ONLY_THREE_SURFACE_RECEIPT_V0_2

## Purpose

`FREE_ONLY_THREE_SURFACE_RECEIPT_V0_2` is a governed receipt primitive for free-only replay evidence.

It binds a transaction to three independently observed public-data surfaces without using trace APIs, paid RPC assumptions, wallet-control claims, creator-identity claims, token-authenticity claims, sale/payment proof claims, or legal ownership claims.

## Primitive ID

```text
FREE_ONLY_THREE_SURFACE_RECEIPT_V0_2
```

## Required surfaces

A valid primitive instance contains all three surfaces:

1. `TX_RECEIPT_SURFACE`
2. `LOG_SURFACE`
3. `STATE_READ_SURFACE`

If any surface is absent, the receipt MUST NOT be labeled `FREE_ONLY_THREE_SURFACE_RECEIPT_V0_2`.

## Boundary lock

Every receipt of this type MUST carry:

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

## Rule 1 — Admission to pipeline

A replay pipeline MAY attach a transaction to this primitive only if all conditions are satisfied:

- A `TX_RECEIPT_SURFACE` is obtained using `eth_getTransactionReceipt` or equivalent public transaction-receipt evidence.
- Logs are present and classified into a `LOG_SURFACE`.
- At least one selector-explicit `eth_call` is executed and recorded for `STATE_READ_SURFACE`.

If any condition fails, the pipeline MUST NOT label the result as `FREE_ONLY_THREE_SURFACE_RECEIPT_V0_2`.

## Rule 2 — Required boundary fields

Every valid receipt MUST explicitly preserve the boundary lock.

The primitive is invalid if it omits, weakens, or contradicts any of these fields:

- `authority=false`
- `free_only=true`
- `no_fake_green=true`
- `debug_traceTransaction="not_used"`
- `internal_calls_observed=false`
- `wallet_control_claim=false`
- `creator_identity_claim=false`
- `token_authenticity_claim=false`
- `payment_or_sale_claim=false`

## Rule 3 — Claim discipline

Pipelines MAY assert only directly observed surface facts, such as:

- transaction receipt observed
- logs observed and classified
- selector-explicit state read observed
- free RPC replay path executed

Pipelines MUST NOT assert:

- wallet control
- legal ownership
- token authenticity
- creator identity
- sale/payment semantics
- internal call structure
- trace semantics

unless separate admissible evidence explicitly supports that claim outside this primitive.

## CI / governance enforcement targets

A pre-merge or receipt-governance check SHOULD reject a candidate receipt if:

- `receipt_type` equals `FREE_ONLY_THREE_SURFACE_RECEIPT_V0_2` but one of the three surfaces is missing.
- `authority` is not `false`.
- `free_only` is not `true`.
- `no_fake_green` is not `true`.
- `debug_traceTransaction` is anything other than `not_used`.
- `internal_calls_observed` is not `false`.
- wallet, creator, authenticity, ownership, payment, sale, or trace claims appear inside the primitive.

## Witness completeness gate

A run MAY be marked `FREE_ONLY_THREE_SURFACE_RECEIPT_V0_2` only after all three surfaces are present:

```text
TX_RECEIPT_SURFACE=observed
LOG_SURFACE=observed
STATE_READ_SURFACE=observed
```

A run MUST NOT be marked replay-verified under this primitive if any of those surfaces are missing.

## Example sealed chain

The first observed chain sealed in this repository is:

```text
source_tx=0xc4b8d203688a0bf1b04345a65719d02d4feef3e9354f7e49f4291a1a8da24178
contract=0x5795735950fd48211a31d8aeccb1de91b210a0b9
surfaces=TX_RECEIPT_SURFACE -> LOG_SURFACE_ERC20_STYLE -> ERC20_STATE_READ_SURFACE
trace_surface=not_observed
```

That example demonstrates the primitive pattern but does not elevate the transaction into trace, ownership, authenticity, creator, sale, payment, or legal semantics.

## Final boundary

```text
authority=false
free_only=true
no_fake_green=true
```
