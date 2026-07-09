# On-Chain Evidence Boundary

Use this skill when reviewing claims about wallets, contracts, tokens, mints, transfers, payments, deployments, attestations, ENS names, Basenames, Zora pages, or Base transactions.

## Required evidence by claim

| Claim | Required evidence |
|---|---|
| wallet control | signature, authenticated action, or explicit wallet-originated proof |
| deployment | transaction hash and contract address |
| mint | transaction hash, token/contract address, chain context |
| transfer | transaction hash, sender, recipient, token, chain context |
| payment | transaction hash, asset, amount, sender/recipient, chain context |
| attestation | UID, schema if available, chain context |
| ENS/Basename resolution | name, resolved address, lookup date, source |
| token provenance | contract address, creator/deployer evidence, transaction history |

## Unsafe signals

- address alone
- screenshot alone
- profile page alone
- repo claim alone
- branch name alone
- social post alone
- token title alone
- explorer page without matching claim scope

## Rule

If the evidence does not match the claim scope, return BLOCKED or PASS_WITH_NOTES at best.

Never promote a visible artifact into proof of control, ownership, payment, deployment, or identity without transaction-grade or signature-grade evidence.
