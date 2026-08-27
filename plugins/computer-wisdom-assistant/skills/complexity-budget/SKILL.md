---
name: complexity-budget
description: Spend complexity only on essential difficulty, prefer composition, and refuse speculative layers. Use when adding a service, framework, abstraction, or "platform", when choosing ship versus polish, when a design is growing just-in-case branches, or when two options differ mainly in future flexibility. Use PROACTIVELY before recommending new architecture.
---

# Complexity Budget

Essential complexity comes from the problem. Accidental complexity comes from our extra machinery. This skill spends the budget on the former and starves the latter.

## When to use

- New service, queue, framework, or workspace
- Shared library "for later"
- Premature generalization from one example
- Ship vs polish, YAGNI, "we might need"
- Two designs that differ only in hypothetical scale
- Unix-style composition vs a unified platform

Load `skills/evidence-first-judgment` for whether the current pain is observed. Load `skills/bounded-authority` before implementing the winner. Load `skills/replayable-reasoning` for the tradeoff card.

## Inputs this skill accepts

- the problem in one sentence
- the constraint (time, risk, reversibility)
- current pain (observed)
- proposed machinery

## Essential vs accidental

| Essential (pay) | Accidental (tax) |
|---|---|
| the domain's real rules | extra types for a single call site |
| failure modes users already hit | a platform for the next six features |
| an interface another program must consume | a custom framework around one script |
| measured scale | imagined scale |

If the pain is not in Observed, the machinery is probably a tax.

## Composition bias

Prefer programs and modules that:

- do one job
- compose through plain data (text, files, events with boring schemas)
- can be replaced without a rewrite
- fail in a way you can see

A new layer must pay for itself in *this* change, not in a hypothetical portfolio.

## Procedure

1. State the problem and the observed pain.
2. List "do less" as option zero.
3. For each option, name complexity cost (new concepts, moving parts, failure modes) and reversibility.
4. Ask: which option can be undone in a day if we are wrong?
5. Prefer the option that preserves a measurement and a way out.
6. Recommend with `authority=false`. Popularity is not evidence.

## Decision table

| Signal | Lean toward |
|---|---|
| one call site, one team, reversible | do less / local change |
| two independent failure domains | a seam, not a platform |
| observed operational pain | the smallest fence that contains it |
| "we'll need it when we scale" | measure first |
| cannot name a falsifier | do not add the layer |

## Output format

```text
Complexity Budget

Problem:
- ...

Observed pain:
- ...

Option 0 (do less):
- ...

Other options:
- ...

Complexity cost (new parts / concepts / failure modes):
- ...

Reversibility:
- ...

Recommendation:
- ...

Required evidence after choosing:
- ...

Final determination:
- authority=false
```

## Examples

**Shared util from one use**

Proposal: `packages/shared/http.ts` used by one app.
Observed pain: none (copy-paste of 12 lines).
Option 0: keep the copy or extract a function in-tree.
Recommendation: do less. A shared package is a versioning and ownership tax.

**Queue "for reliability"**

Proposal: add a broker because requests might spike.
Observed pain: none in logs.
Recommendation: `BLOCKED` as architecture. Measure queue depth / latency first. A timeout and a retry in the existing path may be the whole budget.

**Two implementations, one interface**

Observed pain: mobile and web drift on the same rule.
A narrow shared module for *that rule* can be essential. A new "domain layer" for everything else is accidental until more pain is observed.

## Common issues

- Solving a feeling of mess with a new taxonomy. Rename and delete first.
- Treating "industry standard" as a requirement. Standards are options with costs.
- Paying the tax up front for an audience that does not exist yet.
- Hiding accidental complexity behind generators. Generated machinery is still machinery.

## Related

Companion skills: `skills/evidence-first-judgment`, `skills/bounded-authority`, `skills/replayable-reasoning`, `skills/pattern-fidelity`.

See `references/details.md` for composition tests, YAGNI checks, and worked tradeoffs.
