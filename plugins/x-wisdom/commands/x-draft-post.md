---
description: Draft an X post, reply, or quote as labor. Waits for Jason's exact-action approval before any publish.
argument-hint: "[what to say, and to whom]"
---

# X Draft Post

Draft an X post (or reply/quote) with a publication gate. Do not publish from this command.

## Inputs

Accept `$ARGUMENTS` as the intent. Capture:

- exact message (or ask to draft)
- account to post from, if known
- reply/quote target URL if any
- whether media is in scope

## Skill routing

Open `skills/x-post-gate`. For context from X, read first via `skills/x-read-evidence`.

## Procedure

1. Write the draft in the user's voice, not Jay's manifesto, unless asked.
2. Check length (280 for a single post; say when a thread is required).
3. Flag claims that need a locator (URLs, SHAs, "we shipped") before brains would want them public.
4. Emit an approval gate with the **exact** text that would go out.
5. Wait. Do not call a publish action.

## Output format

```text
X Draft

Status: READY / BLOCKED

Account:
- ...

Exact text:
- ...

Action:
- post | reply | quote | thread

Target (if reply/quote):
- ...

Risks:
- ...

Approval gate:
- brains must approve this exact text to this account

Final determination:
- role=labor (Jay)
- brains=Jason
- authority=false
```

If the operator later says yes to this exact text, that is the gate. A different text needs a new draft.
