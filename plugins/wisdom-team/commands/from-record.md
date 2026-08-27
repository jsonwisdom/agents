---
description: Reverse-replay locators into a reconstructed determination and name the wisdom team roster in the same turn.
argument-hint: "[plugin paths, PR URL, SHA, or other locators]"
---

# From Record

Reverse-replay existing locators, then name the team **in this output**. This command does not put seats to work and does not publish.

## Inputs

Accept `$ARGUMENTS` as locators. If empty, use the wisdom plugins in this workspace if they exist:

- `plugins/computer-wisdom-assistant/`
- `plugins/x-wisdom/`

Ask only when those paths are missing and no other locator was given.

## Skill routing

Open `skills/reverse-replay`, then `skills/team-from-replay` in the same turn. Do not stop after reconstruction.

## Procedure

1. List locators before conclusions.
2. Reconstruct the question those artifacts already answer.
3. Name brains and labor from the record, not from preference.
4. Emit the smallest covering roster immediately.
5. Status `BLOCKED` if locators cannot be inspected. Do not staff from chat memory.

## Output format

```text
From Record

Status: READY / PASS_WITH_NOTES / BLOCKED

Locators:
- ...

Reconstructed question:
- ...

Roster (named this turn):
- brains: Jason Wisdom
- labor-...: ...

Why these seats:
- ...

Seats refused:
- ...

Final determination:
- role=labor (Jay)
- brains=Jason
- authority=false
```
