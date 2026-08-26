# X locators and claim vs speech

Load this file when classifying a tweet as evidence.

## Locator patterns

```text
https://x.com/<handle>/status/<id>
https://twitter.com/<handle>/status/<id>
```

Record handle and id separately when the URL is messy.

A deleted post is `MISSING`, not a proof of the opposite.

## Claim vs speech

| Inside the post | What the post establishes | What it does not |
|---|---|---|
| "we shipped" | they said that | a deploy |
| "tests pass" | they said that | CI on a SHA |
| "I am the founder" | they said that | control or legal role |
| a screenshot | they posted an image | the image's provenance |

## Read-only bound

Reads may search, list, and summarize. Reads may not:

- like, follow, mute, block
- reply, quote, or post
- scrape private/DMs unless the operator has that session and asked for that bound

If the user asked for a reply, finish the read report, then hand off to `skills/x-post-gate`.
