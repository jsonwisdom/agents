---
description: Review a claim, design, diff, or "done" statement against computer-wisdom skills and return an evidence-first determination.
argument-hint: "[claim, path, PR, or decision to review]"
---

# Wisdom Review

Review a technical claim, design, diff, or completion statement using the Computer Wisdom Assistant skills. Produce a determination another engineer can replay.

## What this command does

1. Identify the claim or decision under review.
2. Load the relevant skills.
3. Separate observed evidence from inference.
4. Flag unsafe language and missing receipts.
5. Return a bounded determination with `authority=false`.

## Inputs

Accept `$ARGUMENTS` as the review target. If empty, ask for one of:

- the claim in one sentence
- a file, diff, or PR to inspect
- a design proposal
- a "tests pass / deployed / verified / done" statement

Also capture, if known:

- what would count as success
- what evidence already exists
- whether mutation is in scope

## Skill routing

Open these skills as needed:

- `skills/evidence-first-judgment` for success, proof, verification, deployment, ownership, or completion claims
- `skills/bounded-authority` when the request implies mutation, approval, or unbounded scope
- `skills/replayable-reasoning` for the determination record itself
- `skills/complexity-budget` when the object of review is a new layer, abstraction, or "just in case" design

## Procedure

1. Restate the claim in one sentence.
2. Inspect the workspace (and linked artifacts) for observable evidence. Do not invent run status, hashes, or receipts.
3. Classify each supporting item as observed, inferred, documentation-only, or missing.
4. Check language: flag "proves", "verified", "deployed", "passing", and similar words unless a receipt is visible and tied to the artifact.
5. Name the cheapest next measurement.
6. Emit the report below. If evidence cannot be inspected, status is `BLOCKED`.

## Output format

```text
Wisdom Review

Status: READY / PASS_WITH_NOTES / BLOCKED

Target:
- ...

Claim:
- ...

Skills Applied:
- ...

Observed Evidence:
- ...

Inferred (not evidence):
- ...

Unsafe Language:
- ...

Missing Receipts:
- ...

Next Measurement:
- ...

Final Determination:
- role=labor (Jay)
- brains=Jason
- authority=false
```

## Hard constraints

- Do not mark `PASS` without visible evidence tied to the reviewed artifact.
- Do not treat a title, checklist, screenshot, or branch name as proof by itself.
- Do not mutate the repository, merge, deploy, or publish from this command.
- If the user asked for a mutation, return an approval gate instead of acting.
