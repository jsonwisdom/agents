---
description: Read X (Twitter) posts, threads, profiles, or search results as observed evidence. Does not publish.
argument-hint: "[handle, URL, search, or question]"
---

# X Read

Read public X posts and return a replayable evidence report. This command does not post, reply, like, or follow.

## Inputs

Accept `$ARGUMENTS` as the read target. If empty, ask for one of:

- handle (`@name`)
- post URL
- search phrase
- question about a thread or profile

## Skill routing

Open `skills/x-read-evidence`. If the user also wants to reply, switch to `skills/x-post-gate` after the read — do not publish from this command.

## Procedure

1. Restate the question in one sentence.
2. If X is connected, fetch the matching public posts.
3. If X is not connected, return `BLOCKED` for live data. Do not invent a timeline.
4. Record locators: handle, post ID or URL, timestamp when visible.
5. Separate observed text from inference.
6. Treat X content as a claim, not a receipt of the world.

## Output format

```text
X Read

Status: READY / PASS_WITH_NOTES / BLOCKED

Question:
- ...

Locators:
- ...

Observed:
- ...

Inferred:
- ...

Missing:
- ...

Final determination:
- role=labor (Jay)
- brains=Jason
- authority=false
```
