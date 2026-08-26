# Composition tests, YAGNI checks, and worked tradeoffs

Use this file when the options are close or the proposal is a new platform.

## Composition tests

Ask, for the proposed piece:

1. Can another program use this through a boring interface (files, stdin, HTTP with a small schema)?
2. Can we delete it without rewriting callers' business rules?
3. Does it fail loudly with a locator we can put in a receipt?
4. Does it do one job, or several "while we're here" jobs?

If the answers are no, the piece is likely accidental complexity.

## YAGNI checks

YAGNI is not an excuse to be sloppy. It is a check on *inventory*:

- Unused extension points
- Unused configuration dimensions
- Unused compatibility shims
- Unused "enterprise" layers

Keep the design easy to *extend later* by staying small and explicit, not by pre-building the extension.

```text
YAGNI pass: we can add a flag later because the function is one file.
YAGNI fail: we added a plugin system so we would not have to edit that file.
```

## Cost units

Score options with the same units:

| Unit | Meaning |
|---|---|
| concepts | names a newcomer must learn |
| moving parts | processes, stores, queues, build graphs |
| failure modes | new ways to be down or wrong |
| calendar | time to reverse |

Do not mix "feels cleaner" into these units. Clean is a claim; put it under Inferred until a measurement exists.

## Worked tradeoff: cache

```text
Problem: p95 read latency is 900ms on endpoint X
Observed pain: traces show a repeated expensive query
Option 0: fix the query / index
Option 1: in-process memo with TTL
Option 2: shared cache cluster
Complexity: 0 < 1 << 2
Reversibility: index change and memo are easy; cluster is an ops surface
Recommendation: option 0 or 1 with a locator (trace ID, p95 before/after)
authority=false
```

A cluster is not wiser because it is more "real". It is wiser only if option 0/1 fail an observed test.

## Worked tradeoff: microservices

Splitting a module into a service adds failure modes (network, auth, versioning, local-dev). Pay that tax when the *operational* boundary is already real (separate SLOs, separate deploy cadence, separate data lifetime). Team-chart cosmetics are not an operational boundary.

## Pairing with other skills

- Pain must be Observed: `skills/evidence-first-judgment`.
- Implementing the winner is a mutation: `skills/bounded-authority`.
- Keep the card replayable: `skills/replayable-reasoning`.
