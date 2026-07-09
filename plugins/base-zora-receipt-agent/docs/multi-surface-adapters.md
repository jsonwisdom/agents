# Multi-Surface Adapter Policy

## Purpose

This document defines how adapters are allowed to touch governed replay surfaces.

Adapters MUST declare the surface level they consume and MUST NOT claim beyond that level.

More surfaces provide more evidence. They do not automatically grant stronger semantics.

## Adapter classes

Governance recognizes three adapter classes.

### TX-only adapters

```text
surface_level=TX_ONLY
input=TX_RECEIPT_SURFACE
```

Allowed claims:

- transaction exists
- transaction status observed
- block number observed
- gas used observed
- log count observed

Forbidden claims:

- log semantics
- token type
- balances
- supply
- wallet control
- ownership
- creator identity
- token authenticity
- payment/sale semantics
- trace/internal call structure

### TX+LOG adapters

```text
surface_level=TX_LOG
input=TX_RECEIPT_SURFACE + LOG_SURFACE
```

Allowed claims:

- transaction receipt observed
- logs observed
- event topic present
- topic surface classified, such as ERC20-style transfer surface, ERC721-adjacent surface, ERC1155-adjacent surface, unknown/custom event surface

Forbidden claims:

- balances
- supply
- wallet control
- ownership
- creator identity
- token authenticity
- payment/sale semantics
- trace/internal call structure

### Three-surface adapters

```text
surface_level=THREE_SURFACE_V0_2
input=TX_RECEIPT_SURFACE + LOG_SURFACE + STATE_READ_SURFACE
receipt_type=FREE_ONLY_THREE_SURFACE_RECEIPT_V0_2
```

Allowed claims:

- transaction receipt observed
- logs observed and classified
- selector-explicit state read observed
- ERC20-adjacent state observed when supported by `eth_call` responses
- name, symbol, decimals, totalSupply, and balanceOf surfaces observed when those calls are executed successfully

Forbidden claims:

- wallet control
- legal ownership
- creator identity
- token authenticity
- payment/sale semantics
- trace/internal call structure

## Adapter declaration invariant

Every adapter MUST declare:

```text
adapter_id=<stable identifier>
surface_level=<TX_ONLY | TX_LOG | THREE_SURFACE_V0_2>
authority=false
free_only=true
no_fake_green=true
```

If `surface_level=THREE_SURFACE_V0_2`, the adapter MUST also declare:

```text
receipt_type=FREE_ONLY_THREE_SURFACE_RECEIPT_V0_2
```

If an adapter touches `STATE_READ_SURFACE` but does not declare `THREE_SURFACE_V0_2`, CI SHOULD reject it.

## Claim matrix

| Surface level | May assert | Must not assert |
|---|---|---|
| `TX_ONLY` | transaction exists; status; blockNumber; gasUsed; logs count | token type; log semantics; balances; supply; ownership; authenticity; payment/sale; creator identity; trace/internal calls |
| `TX_LOG` | log with topic0 observed; topic classification; ERC20-style/ERC721-adjacent/ERC1155-adjacent/unknown surface | balances; supply; ownership; authenticity; payment/sale; creator identity; trace/internal calls |
| `THREE_SURFACE_V0_2` | tx observed; logs classified; selector-explicit state read observed; ERC20-adjacent interface surface observed | wallet control; legal ownership; creator identity; token authenticity; payment/sale semantics; trace/internal calls |

Adapters that violate this matrix are governance-invalid.

## CI enforcement sketch

For each adapter declaration, governance checks SHOULD verify:

### Surface use vs declaration

- If `surface_level=TX_ONLY` and the adapter reads logs, reject.
- If `surface_level=TX_ONLY` and the adapter reads state, reject.
- If `surface_level=TX_LOG` and the adapter reads state, reject.
- If `surface_level=THREE_SURFACE_V0_2` and the adapter references trace, ownership, authenticity, creator identity, payment, sale, or legal ownership claims, reject.

### Boundary lock

Reject if any boundary field is missing or contradicts:

```text
authority=false
free_only=true
no_fake_green=true
```

### Receipt type lock

Reject if:

```text
surface_level=THREE_SURFACE_V0_2
```

and:

```text
receipt_type != FREE_ONLY_THREE_SURFACE_RECEIPT_V0_2
```

## Required adapter declaration example

```text
adapter_id=base-zora-free-only-erc20-state-reader
surface_level=THREE_SURFACE_V0_2
receipt_type=FREE_ONLY_THREE_SURFACE_RECEIPT_V0_2
authority=false
free_only=true
no_fake_green=true
```

## Invalid examples

### Invalid TX-only escalation

```text
surface_level=TX_ONLY
claim="ERC20 transfer occurred"
```

Invalid because TX-only adapters may observe log count but may not classify log semantics.

### Invalid TX+LOG state escalation

```text
surface_level=TX_LOG
claim="holder balance observed"
```

Invalid because balance requires `STATE_READ_SURFACE`.

### Invalid three-surface semantic elevation

```text
surface_level=THREE_SURFACE_V0_2
claim="holder owns the token"
```

Invalid because state-read evidence does not prove wallet control, legal ownership, or authenticity.

## Final boundary

```text
authority=false
free_only=true
no_fake_green=true
```
