---
description: Produce a replayable tradeoff card for an engineering decision, including options, complexity cost, failure modes, and required evidence.
argument-hint: "[decision to make]"
---

# Tradeoff Card

Produce a short, replayable tradeoff card for an engineering decision. Use this when choosing between designs, abstractions, tools, or "ship vs polish" options.

## What this command does

1. Name the decision and the constraint that makes it necessary.
2. List two to four real options, including "do nothing / do less".
3. Score complexity cost and failure modes, not just features.
4. State what evidence would change the call.
5. Recommend one option with `authority=false`.

## Inputs

Accept `$ARGUMENTS` as the decision. If empty, ask for:

- the decision in one sentence
- the constraint (time, risk, blast radius, reversibility)
- options already on the table
- what would count as being wrong later

## Skill routing

Open these skills:

- `skills/complexity-budget` for essential vs accidental complexity and composition
- `skills/evidence-first-judgment` for what would count as a receipt that the choice worked
- `skills/bounded-authority` if an option requires mutation, spend, or irreversible action
- `skills/replayable-reasoning` for the card format itself

## Procedure

1. Write the decision as a choice, not a slogan.
2. Include "do less" as an option unless it is impossible.
3. For each option, name: what it buys, what it costs in complexity, how it fails, and how reversible it is.
4. Prefer the option that preserves a way out and a way to measure.
5. Do not invent benchmarks. If numbers are unknown, mark them unknown and say what to measure.
6. Emit the card below.

## Output format

```text
Tradeoff Card

Decision:
- ...

Constraint:
- ...

Options:
1. ...
   Buys:
   Complexity cost:
   Failure modes:
   Reversible?:
2. ...

Rejected options and why:
- ...

Required evidence after choosing:
- ...

Recommendation:
- ...

Final Determination:
- role=labor (Jay)
- brains=Jason
- authority=false
```

## Hard constraints

- Do not recommend a new layer when a narrower change would do.
- Do not treat popularity or "best practice" as evidence.
- Do not hide the "do less" option.
- If the recommendation requires a mutation the operator has not approved, label it `blocked pending approval`.
