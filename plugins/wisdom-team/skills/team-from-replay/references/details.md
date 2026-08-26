# Seat bounds and the work gate

Load this file when a covering-set choice is close, or when the operator asked to start work.

## Seat bounds

Each named labor seat may observe and recommend inside its class. None may approve, merge, post, or spend.

| Seat | In | Out |
|---|---|---|
| labor-judgment | claims, tradeoffs, bounds | shipping as Jason |
| labor-x | read X, draft posts | send without exact-text yes |
| labor-witness | PR files, checks, diffs | review submissions |
| labor-receipts | CI/receipt locators | certifying merge |
| labor-public-record | source-visible records | legal conclusions |
| labor-onchain | tx / contract locators | signing |
| labor-fork | bounded read-only side tasks | expanding the bound |

Specialist names for those seats live in the plugin tree: computer-wisdom-assistant, x-wisdom-assistant, github-pr-witness, receipt-auditor, alms-public-record-verifier, base-zora-receipt-agent, and the side-task clerk under `plugins/agent-fork-coordinator/`.

## Work gate

Naming is free. Starting work is not.

```text
Approval Gate

Seats to put to work:
- ...

Bound:
- ...

Stop:
- ...

Brains decision:
- approve exact seats and bound / deny / drop seats
```

A previous yes to a different roster is not this yes.

## Size

Two labor seats plus brains is enough when locators are the wisdom plugins. A third labor seat needs a third locator class. Four or more is usually a covering-set failure, not scale.
