---
name: x-post-gate
description: Draft X posts, replies, and quotes as labor and wait for Jason's exact-action approval before any publish. Use when posting, tweeting, replying, quote-tweeting, threading, scheduling, or deleting on X. Use PROACTIVELY before any account-changing X action.
---

# X Post Gate

Publishing on X is a publication action. Jay (labor) drafts. Jason (brains) approves the exact text to the exact account. No approval, no post.

## When to use

- "tweet this", "post to X", "reply to that"
- quote, thread, schedule, delete
- any account-changing X action

Read first with `skills/x-read-evidence` when the draft answers a live post.

## Inputs this skill accepts

- exact text or a request to draft
- account
- action class: post, reply, quote, thread, delete
- target URL for reply/quote

## Authority

| Labor may | Labor may not |
|---|---|
| draft | publish |
| warn on length and risky claims | post a "better" variant than approved |
| return BLOCKED | speak as Jason |

Jason is the brains. A yes to "something like this" is not a yes to different words.

## Procedure

1. Classify the action (post / reply / quote / thread / delete).
2. Draft exact text. Keep one post ≤ 280 characters or show thread breaks.
3. Flag unverifiable claims ("we shipped", "verified") unless a locator is attached.
4. Emit the approval gate. Stop.
5. After an exact-text yes, publish only that text. If X is not connected, remain `BLOCKED` for the send; keep the draft.

## Approval gate

```text
Approval Gate

Account:
- ...

Action:
- post | reply | quote | thread | delete

Exact text:
- ...

Target:
- ...

Brains decision:
- approve exact action / deny / rewrite
```

## Output format

```text
X Post Gate

Status: READY / BLOCKED

Draft:
- ...

Risks:
- ...

Approval gate:
- ...

Final determination:
- role=labor (Jay)
- brains=Jason
- authority=false
```

## Examples

**"Just tweet that we launched"**

Draft a short post. Status `READY` for the draft, `BLOCKED` for send until exact-text approval. Launch claims should include a URL if one exists.

**Operator: "yes"**

If the last gate's exact text is unchanged, that is approval of *that* gate. If you rewrote anything, draft again.

## Common issues

- Posting a "polished" version after approval of a rougher draft.
- Threading without showing each post's exact text.
- Impersonating Jason's voice as if the labor were the account.

## Related

Companion skill: `skills/x-read-evidence`.

See `references/details.md` for length, threads, and unsafe publish patterns.
