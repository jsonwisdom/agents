---
name: evidence-first-judgment
description: Judge technical claims against observable evidence instead of intention, checklists, or confident wording. Use when a user says tests pass, a change is verified, deployed, owned, fixed, secured, or done, when reviewing a PR or design for unwitnessed success language, or when deciding what receipt a claim still needs. Use PROACTIVELY for success and proof statements.
---

# Evidence-First Judgment

A claim is only as strong as the evidence that can be inspected. This skill turns "it works" into a receipt, a gap, or a blocked determination.

## When to use

- Completion, pass, verify, deploy, own, sign, hash, or "fixed" claims
- PR descriptions, READMEs, and commit messages that sound stronger than the diff
- Local test claims with no command output
- On-chain, CID, or hash claims with no digest or explorer reference
- Asking "are we done?"

Load `skills/bounded-authority` if the claim implies a mutation. Load `skills/replayable-reasoning` when writing the determination. Load `skills/complexity-budget` when the claim is that a new layer was necessary.

## Inputs this skill accepts

- A one-sentence claim
- An artifact (diff, log, receipt file, URL, hash, run ID)
- Optional: what the speaker wants the claim to authorize

## Claim vs evidence

| Claim type | Admissible evidence | Not evidence |
|---|---|---|
| tests passed | command output or CI run tied to the commit | "I ran them" |
| CI passed | workflow run ID + commit SHA | green badge in a README mockup |
| deployed | deploy receipt, URL + revision, or run log | branch name `prod` |
| verified | verifier output | the word "verified" |
| fixed | diff + reproduction or failing-then-passing test | issue closed |
| owned / signed | signature, auth flow, or explicit proof | address or username |
| hashed / CID | digest and reachable artifact | "content addressed" |
| done | stop condition met with observed result | checklist ticked by the author |

## Procedure

1. Write the claim in one sentence without marketing words.
2. List every artifact offered as support.
3. For each artifact, classify: `observed`, `inferred`, `documentation-only`, or `missing`.
4. Ask what would falsify the claim. If nothing could, the claim is unbounded — treat as `BLOCKED`.
5. Name the cheapest next measurement.
6. Return status. `PASS` requires visible evidence tied to the reviewed artifact.

## Safer language

Prefer:

```text
observed
reported
pending verification
evidence not present
documentation-only
replayable if artifacts are reachable
authority=false
```

Replace:

```text
proves        -> observed / consistent with
guarantees    -> expected under these conditions
certified     -> signed receipt attached, or omit
production-safe -> not reviewed for production
merged-ready  -> review complete; merge is an operator action
```

## Output format

```text
Evidence Judgment

Status: PASS / PASS_WITH_NOTES / BLOCKED

Claim:
- ...

Observed:
- ...

Inferred:
- ...

Missing receipts:
- ...

Falsifier:
- ...

Next measurement:
- ...

Final determination:
- authority=false
```

A `PASS` line without a tied artifact is itself a defect. Use `BLOCKED` when the claim is strong and the evidence is absent.

## Examples

**Local tests, no output**

Claim: "Tests pass."
Observed: none.
Determination: `BLOCKED: claimed success lacks observed evidence.`
Next measurement: run the test command and keep the output next to the commit.

**CI run present**

Claim: "CI passed on this PR."
Observed: workflow run `123456` on commit `abc123`.
Determination: `PASS_WITH_NOTES` if the run matches the current commit; `BLOCKED` if the run is on an older SHA.

**Deployed from a branch name**

Claim: "This is in production because the branch is `release`."
Observed: branch name only.
Determination: `BLOCKED`. A branch is a pointer, not a deploy receipt.

## Common issues

- Treating a screenshot as a run. A picture is documentation-only unless the run ID can be re-fetched.
- Treating a plan as a result. "Will run CI" is not "CI passed".
- Collapsing "I believe" into "it is". Keep inference in its own list.
- Softening a gap into a pass. Missing evidence is a gap.

## Related

Companion skills: `skills/bounded-authority`, `skills/replayable-reasoning`, `skills/complexity-budget`, `skills/pattern-fidelity`.

See `references/details.md` for the full claim catalog, falsifier prompts, and worked receipt shapes.
