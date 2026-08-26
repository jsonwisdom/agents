---
name: x-read-evidence
description: Read X (Twitter) posts, threads, profiles, and search results as observed claims with locators, not as proof of the world. Use when the user asks what someone posted, to search X, to summarize a timeline or thread, or when a tweet is offered as evidence. Use PROACTIVELY before treating an X post as a fact.
---

# X Read Evidence

An X post is a public speech act. It is evidence that *that account posted those bytes at that locator*. It is not evidence that the claim inside the post is true.

## When to use

- "What did @handle tweet?"
- Search, mentions, timeline, thread, profile
- A tweet URL offered as proof of a ship, a bug, or a deal
- Before drafting a reply (read first)

Load `skills/x-post-gate` if the next step is to publish. Do not publish from this skill.

## Inputs this skill accepts

- handle, post URL, search phrase, or thread
- time window if known
- whether live X access is available

## Locators

| Strong | Weak |
|---|---|
| post URL or numeric post ID + handle | "that tweet" |
| visible timestamp | "today" |
| exact quoted text | a paraphrase |

If you cannot name a locator, the read is `BLOCKED` or documentation-only.

## Procedure

1. State the question.
2. Fetch public posts if X is connected. If not, `BLOCKED` for live data — do not invent.
3. Quote or closely paraphrase with a locator per item.
4. Split **observed** (bytes on X) from **inferred** (motive, truth of the claim, "everyone thinks").
5. If the post claims "shipped / verified / paid", note that X is not the receipt for those claims.

## Output format

```text
X Read Evidence

Status: READY / PASS_WITH_NOTES / BLOCKED

Question:
- ...

Locators:
- ...

Observed:
- ...

Inferred:
- ...

Not established by this post:
- ...

Final determination:
- role=labor (Jay)
- brains=Jason
- authority=false
```

## Examples

**Thread as proof of a deploy**

Observed: @example wrote "it's live" at a post URL.
Not established: production deploy. Need a deploy receipt, not a tweet.

**Search with no connection**

Status: `BLOCKED`. Live search requires a connected X session. Do not fabricate hits.

## Common issues

- Treating likes/reposts as agreement with the claim.
- Collapsing a quote-tweet into the original author's words.
- Using a screenshot of X as a live locator (documentation-only unless the URL can be fetched).

## Related

Companion skill: `skills/x-post-gate`.

See `references/details.md` for locator patterns and claim-vs-speech tables.
