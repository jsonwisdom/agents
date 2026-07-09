# check-onchain-claim

Review an on-chain claim using receipt-first evidence boundaries.

## Behavior

Inspect claims involving Base, Zora, ENS, Basename, EAS, token contracts, mints, transfers, payments, deployments, attestations, or wallet addresses.

Return a boundary report that separates observed chain evidence from unsupported claims.

## Hard constraints

- Do not infer wallet control from an address alone.
- Do not infer deployment from a repository, screenshot, or social post alone.
- Do not infer token ownership from a profile page alone.
- Do not infer payment, mint, sale, transfer, or attestation without transaction evidence.
- If transaction hash, block context, or explorer reference is missing, return BLOCKED for the affected claim.

## Expected output

```text
Base Zora Receipt Agent Review

Status: PASS / PASS_WITH_NOTES / BLOCKED

Observed On-Chain Evidence:
- ...

Missing Evidence:
- ...

Unsafe Claims:
- ...

Safe Rewrite:
- ...

Final Determination:
- authority=false
- witness-only
```
