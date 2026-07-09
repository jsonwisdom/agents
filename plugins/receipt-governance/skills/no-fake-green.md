# No Fake Green

Use this skill when reviewing claims of success, passing tests, deployment, verification, ownership, or completion.

## Rule

A green claim is admissible only when it is tied to observable evidence.

Acceptable evidence includes:

- CI workflow run tied to the relevant commit
- test command with visible output
- receipt file with artifact path and digest
- sha256 or equivalent content digest
- CID for reachable content-addressed artifacts
- transaction hash or block reference for on-chain claims
- reproducible verification steps

## Unsafe green signals

Flag these as insufficient:

- "It works"
- "Tests pass" without observed output
- "Verified" without verifier output
- "Deployed" without deployment receipt
- "Merged-ready" without current branch comparison
- "Wallet controlled" from address alone
- "CID created" without actual CID
- "Hash confirmed" without digest

## Safer language

Use:

- observed
- reported
- pending verification
- evidence not present
- documentation-only
- replayable if artifacts are reachable
- authority=false

## Output behavior

When evidence is missing, do not soften the result.

Use:

`BLOCKED: claimed success lacks observed evidence.`

Never use:

`PASS`

unless the evidence is visible, reachable, and tied to the reviewed artifact.
