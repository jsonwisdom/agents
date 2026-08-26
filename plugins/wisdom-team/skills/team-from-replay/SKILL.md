---
name: team-from-replay
description: Name a wisdom team roster from a reverse-replay record in the same turn, using the smallest covering set. Use when creating the team, staffing seats, or when reverse replay just reconstructed locators. Use PROACTIVELY so the roster is named immediately rather than deferred.
---

# Team From Replay

The team is created when the reverse-replay record is written, not later. This skill names the smallest covering roster from that record. Extra seats are a complexity spend and need a locator.

Jason is brains. Named specialists are labor. This skill does not grant authority.

## When to use

- "create the team" / "right then" / "who's on it"
- immediately after `skills/reverse-replay`
- when a roster is about to be invented without locators (stop and reverse-replay first)

If reverse replay has not run this turn, load `skills/reverse-replay` first.

## Inputs this skill accepts

- reverse-replay record (locators, reconstructed question, implied brains/labor)
- optional extra locators that would justify another seat

## Covering set

Pick the smallest seats that cover the reconstructed question.

| Locator class | Seat to name | Specialist |
|---|---|---|
| judgment / claims / tradeoffs | labor-judgment | computer-wisdom-assistant |
| X posts, reads, drafts | labor-x | x-wisdom-assistant |
| GitHub PR bytes | labor-witness | github-pr-witness |
| CI / ship receipts | labor-receipts | receipt-auditor |
| public-record claims | labor-public-record | alms-public-record-verifier |
| chain / Base / Zora | labor-onchain | base-zora-receipt-agent |
| bounded side research | labor-fork | side-task clerk |

Name in every covering set:

| Seat | Who |
|---|---|
| brains | Jason Wisdom |

Do not name a seat whose locator class is absent. Do not name Jay as brains.

## Right then

"Right then" means the roster appears in the same output as the reverse replay. It does not mean work has started. Putting seats to work is a publication-shaped action: exact seats, exact bound, brains yes.

## Procedure

1. Read implied labor from the reverse-replay record.
2. Map each implied labor item to one seat. Collapse duplicates.
3. Refuse seats that are "useful later".
4. Emit the roster now.
5. If the operator asked to start work, emit an approval gate and wait.

## Output format

```text
Team From Replay

Status: READY / BLOCKED

Roster:
- brains: Jason Wisdom
- labor-...: <specialist>

Covering:
- ...

Refused seats:
- ... (locator missing)

Approval gate:
- none | exact seats + bound for work

Final determination:
- role=labor (Jay)
- brains=Jason
- authority=false
```

## Examples

**Judgment + X plugins observed**

Roster: brains Jason; labor-judgment computer-wisdom-assistant; labor-x x-wisdom-assistant.
Refused: witness, receipts, on-chain (no locator).

**"Add a debug crew while we're here"**

Refuse. No debug locator. Status stays `READY` for the covering set only.

## Common issues

- Copying the full governance catalog into every roster.
- Naming this assistant as team lead of record.
- Treating roster publication as Jason's voice.

## Related

Companion skill: `skills/reverse-replay`.

See `references/details.md` for seat bounds and the work gate.
