---
name: reverse-replay
description: Reconstruct a determination and implied labor from locators that already exist, instead of writing a new story forward. Use when the user says reverse replay, from the record, what already happened, who was labor, or when a PR, plugin path, SHA, or receipt should be read backward into a question. Use PROACTIVELY before staffing a team from memory.
---

# Reverse Replay

Forward replay writes a determination so a later session can follow the locators. Reverse replay starts from locators that already exist and reconstructs the question, the bound, and the labor they already imply.

The reconstruction is the input to `skills/team-from-replay`. Name the roster in the same turn.

## When to use

- "reverse replay"
- "from the record" / "from this PR" / "from these plugins"
- reconstituting who was brains and who was labor
- before creating a team from work that already shipped

Load `skills/team-from-replay` before the turn ends. A reverse replay with no roster is incomplete.

## Inputs this skill accepts

- locators (paths, SHAs, PR URLs, X post URLs, run IDs, receipts)
- whether those locators can be inspected in this workspace
- optional prior forward-replay card to check against

## Reverse vs forward

| Forward (`replayable-reasoning` shape) | Reverse (this skill) |
|---|---|
| question first | locators first |
| then inspect | then reconstruct the question |
| then write status | then name who the artifacts already employed |

If you cannot find the artifacts, status is `BLOCKED`. Chat memory is not a locator.

## Procedure

1. List locators. Refuse "the latest" and "what we just did" unless a SHA, path, or URL is attached.
2. Inspect what is actually there.
3. Reconstruct one question those artifacts can answer.
4. Split observed (bytes at locators) from inferred (motive, "we meant to").
5. Name brains and labor already implied. Jason is brains when the author/operator record says so.
6. Hand the reconstruction to `skills/team-from-replay` in this turn.

## Output format

```text
Reverse Replay

Status: READY / PASS_WITH_NOTES / BLOCKED

Locators:
- ...

Method:
- ...

Observed:
- ...

Inferred:
- ...

Reconstructed question:
- ...

Brains already implied:
- ...

Labor already implied:
- ...

Unknowns:
- ...

Final determination:
- role=labor (Jay)
- brains=Jason
- authority=false
```

## Examples

**Plugins present**

Locators: `plugins/computer-wisdom-assistant/`, `plugins/x-wisdom/`.
Observed: judgment labor and X labor exist, author Jason Wisdom.
Reconstructed question: who is the wisdom labor for claims vs X posts?
Labor already implied: computer-wisdom-assistant, x-wisdom-assistant.

**PR URL with no fetch**

Status: `BLOCKED` for live PR bytes. Path locators in the workspace may still replay.

## Common issues

- Starting from a desired team and hunting for locators that fit. Reverse replay forbids that.
- Treating a README wish as an observed seat.
- Reconstructing a question the artifacts cannot answer.

## Related

Companion skill: `skills/team-from-replay`.

See `references/details.md` for locator tables and reconstruction checks.
