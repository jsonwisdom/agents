# Evidence catalog and worked receipts

Load this file when the navigation in `SKILL.md` is not enough to classify a claim.

## Falsifier prompts

Ask one of these out loud before grading a claim:

- What observation would make this false?
- If this failed at 3am, which log line would we expect?
- Which commit SHA is this result tied to?
- Can a stranger replay this without Slack context?
- If the speaker were wrong, how long until we would know?

If the answer is "we wouldn't", the claim is not yet a determination.

## Receipt shape

A usable receipt names:

| Field | Why |
|---|---|
| artifact | what was measured |
| locator | path, URI, run ID, tx hash, or commit |
| digest | sha256 or equivalent when the bytes matter |
| timestamp | when it was observed |
| observer | who or what recorded it |
| result | what was seen, not what was hoped |
| authority=false | this is a record, not a grant of power |

Minimal example:

```text
artifact: unit tests
locator: .github/workflows/validate.yml run 98765 on abc123
digest: n/a (log is the artifact)
timestamp: 2026-08-25T23:00:00Z
observer: GitHub Actions
result: all jobs success on abc123
authority=false
```

## Claim catalog

### Tests and CI

- Command output is evidence for *that* invocation, not for a later commit.
- A workflow must name the SHA. "Latest" is not a SHA.
- Skipped jobs are not passing jobs. Record them as skipped.
- Cached green from a different branch is not this change.

### Deploy and runtime

- A container image digest is stronger than a tag.
- A URL without a revision is a location, not a deploy receipt.
- "I restarted the service" needs a command output or runtime event. The event is evidence of a restart, not of health.

### Security and ownership

- An address, account, or username is identity-shaped data, not control.
- "We rotated the key" needs a timestamped action record and a statement of what still holds the old key.
- CVE closed by version bump needs the lockfile or image digest, not a blog post.

### Content addressing

- A CID or hash without the bytes (or a fetch that returns them) is a name, not a receipt.
- Truncated hashes are not hashes. Record the full digest.

### Product and process

- A checked box in a PR template is a reminder, not a test.
- "Reviewed" without who/what/when is documentation-only.
- Issue state is workflow, not correctness.

## Unsafe green phrases

Flag and rewrite:

| Phrase | Why it fails | Safer rewrite |
|---|---|---|
| it works | unspecified observer | observed behavior X in environment Y |
| should be fine | prediction | not yet measured |
| obviously correct | no falsifier | here is the check |
| LGTM as proof | social | review recorded; tests still required |
| verified locally | unverifiable to others | local, unreproducible unless output attached |

## Worked determinations

### PASS_WITH_NOTES

```text
Claim: lint is clean on this branch
Observed: ruff output, 0 errors, captured in CI run 44 on def456
Inferred: none
Missing: type-check job not in this workflow
Falsifier: a new ruff rule firing on def456
Status: PASS_WITH_NOTES
```

### BLOCKED

```text
Claim: payment webhook is production-safe
Observed: unit tests for signature parsing
Inferred: author believes staging matches prod
Missing: staging replay, idempotency receipt, provider test event ID
Falsifier: duplicate delivery or wrong signing secret
Status: BLOCKED
```

## Pairing with other skills

- If the next step is a mutation, stop and apply `skills/bounded-authority`.
- If the determination must survive a new session, copy it through `skills/replayable-reasoning`.
- If the claim is "we needed this platform", apply `skills/complexity-budget` before grading the platform as success.
