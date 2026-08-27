---
description: Put a reverse-replayed wisdom roster to work only after Jason's exact-action approval. Names seats from the record; does not invent a crew.
argument-hint: "[roster card or locators]"
---

# Create Team

Create the working team from a reverse-replay record. Name seats from locators. Do not add people. Do not start work until brains approves the exact seats and bound.

## Inputs

Accept `$ARGUMENTS` as a prior From Record card, or locators. If only locators are present, run `skills/reverse-replay` first, then this procedure.

## Skill routing

Open `skills/team-from-replay`. If the roster is not yet named this turn, open `skills/reverse-replay` first. Always both, never roster-only from memory.

## Procedure

1. Confirm the roster came from locators in this turn.
2. Write the exact seats, bounds, and stop condition.
3. Emit an approval gate. Stop.
4. After an exact-seat yes, point each labor seat at its specialist by name. Do not speak as those specialists.
5. If the operator said "create the team right then", the roster is named immediately; the *work* still waits on the gate.

## Output format

```text
Create Team

Status: READY / BLOCKED

Roster:
- ...

Bound:
- in:
- out:
- stop:

Approval gate:
- brains must approve these exact seats and this bound

Final determination:
- role=labor (Jay)
- brains=Jason
- authority=false
```

A yes to "something like a team" is not a yes to extra seats.
