---
name: replayable-reasoning
description: Write determinations another session can replay from artifacts, not from chat memory. Use when recording a review, tradeoff, incident note, or "why we decided this", when a conclusion must survive a new conversation, or when a claim should be tied to a commit, log, hash, or receipt. Use PROACTIVELY whenever the answer will be cited later as a decision.
---

# Replayable Reasoning

A wise determination can be replayed. This skill records the minimum structure so a later reader can reach the same status from the same artifacts, or see exactly why they cannot.

## When to use

- Wisdom reviews and tradeoff cards
- Incident or debug notes that will outlive this chat
- Handoffs between sessions or people
- Any conclusion that might be quoted as "we verified"
- Writing a receipt-shaped paragraph instead of a story

Load `skills/evidence-first-judgment` for what counts as an artifact. Load `skills/bounded-authority` if the record authorizes later action (it should not). Load `skills/complexity-budget` when the decision is about adding or refusing structure.

## Inputs this skill accepts

- question
- artifacts inspected (paths, SHAs, run IDs)
- method (what was compared or measured)
- status
- unknowns

## Replay test

A record passes the replay test if a stranger with the same locators can:

1. Find the artifacts.
2. Repeat the comparison or measurement.
3. Agree the status follows, or point to a missing locator.

If the record requires "being in the room", it is not replayable. Mark it `documentation-only` or `BLOCKED`.

## Record fields

| Field | Rule |
|---|---|
| question | one sentence |
| locators | commit, path, URL, run ID, digest — not "the latest" |
| method | what was compared or run |
| observed | what those locators showed |
| inferred | labeled separately |
| unknowns | named, not implied |
| status | READY / PASS_WITH_NOTES / BLOCKED |
| authority | false |

## Procedure

1. Write the question as something artifacts can answer.
2. List locators before conclusions.
3. Describe the method in verbs a later session can execute ("diff these two SHAs", "read this log line").
4. Split observed from inferred.
5. End with status and `authority=false`.
6. If a locator is missing, the status cannot be `PASS`.

## Output format

```text
Replayable Record

Question:
- ...

Locators:
- ...

Method:
- ...

Observed:
- ...

Inferred:
- ...

Unknowns:
- ...

Status:
- READY / PASS_WITH_NOTES / BLOCKED

Final determination:
- authority=false
```

Keep the record short enough to paste. Detail belongs in the locators, not in atmosphere.

## Examples

**Replayable**

```text
Question: Did validate.yml succeed on abc123?
Locators: GitHub Actions run 555, commit abc123
Method: read job conclusions on that run
Observed: validate job success; smoke-test skipped
Status: PASS_WITH_NOTES
authority=false
```

**Not replayable**

```text
Question: Is the migration safe?
Locators: none
Method: "looks like other migrations"
Observed: none
Status: BLOCKED
```

**Chat memory leak**

A previous turn said tests passed. This record does not inherit that. Either attach the output locator or treat it as unknown.

## Common issues

- Dating a conclusion "today" without a timestamp and SHA.
- Pointing at a directory instead of a file and revision.
- Mixing a recommendation into Observed. Recommendations go after status.
- Writing a narrative that cannot be executed as a method.

## Related

Companion skills: `skills/evidence-first-judgment`, `skills/bounded-authority`, `skills/complexity-budget`.

See `references/details.md` for locator patterns, anti-patterns, and a compact receipt template.
