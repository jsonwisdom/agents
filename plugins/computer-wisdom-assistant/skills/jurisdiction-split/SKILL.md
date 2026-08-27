---
name: jurisdiction-split
description: Keep names, wallets, bills, agencies, and .gov sites as separate objects when they share a brand. Use when a user treats jaywisdom.eth and jaywisdom.base.eth as one name, Coinbase Wallet and Coinbase.com as one custodian, congress.gov and justice.gov as one vault, or the CLARITY Act as a key-recovery or identity-stitching tool. Use PROACTIVELY when "clarity," jurisdiction, digital commodity vs security, or split custody appear.
---

# Jurisdiction Split

Same *shape* of confusion is not the same object. A brand that says Clarity, Coinbase, ENS, or `.gov` can still be split custody. Do not collapse the pile.

Load `skills/evidence-first-judgment` before treating a URL as a record. Load `skills/bounded-authority` before any write, bind, or recovery action. Load `skills/replayable-reasoning` for the determination.

## When to Use

- Two names, labels, wallets, or sites that "feel like one system"
- Digital-asset bills, SEC vs CFTC, "who has jurisdiction over this token"
- Coinbase Wallet vs Coinbase.com, self-custody vs intermediary
- `jaywisdom.eth` vs `jaywisdom.base.eth` vs `*.cb.id`
- congress.gov / whitehouse.gov / justice.gov treated as one vault
- A stalled or passed-House bill offered as a recovery tool for a lost key

## Claim vs record

| Slogan | Record |
|---|---|
| "the CLARITY Act" | bill number, title, chamber, date, vote or action |
| "it's on .gov" | host + path + date; publication surface, not ownership |
| "Coinbase has it" | which product, which address, which published rule |
| "that's my ENS" | which name, which registry, which address, which date |
| "agencies already made it clear" | which instrument, which agency, which date |

A `.gov` URL is a **publication surface**. The record is the bill number, the section, the date, the vote. Same as: the record is the address + the name + the date, not "Coinbase" as a feeling.

## Same shape, not the same object

| Name / custody pile | Market-jurisdiction pile |
|---|---|
| `jaywisdom.eth` vs `jaywisdom.base.eth` vs `*.cb.id` | security vs commodity vs "not either yet" |
| Coinbase Wallet vs Coinbase.com | self-custody vs intermediary |
| three addresses, one human | two agencies, one market |
| name still resolves, key gone | bill passed House, Senate stall, agencies write anyway |

Looks like one system. It is not. Do not merge rows.

## CLARITY Act as a real bill, not a vibe

As of 2026-08-27 this skill treats H.R. 3633, *Digital Asset Market Clarity Act of 2025*, as a **named legislative object**, not as law and not as a recovery tool.

Observed legislative locators (publication surface: congress.gov):

- H.R. 3633, 119th Congress
- House passage 2025-07-17, 294–134
- Senate Banking reported with a substitute; placed on Senate calendar 2026-06-01
- Cloture on the motion to proceed presented 2026-08-08
- Tracker status: passed House; **not law** on 2026-08-27

Three pens can use one word: Congress (bill text), SEC, CFTC. Naming "clarity" does not unify them.

What the bill *tries* to do, in one line: split **digital commodity** (mostly CFTC) from **investment contract / security** (SEC), plus recordkeeping and customer-asset rules — "mature blockchain" vs "issuer still running the show." That is a jurisdiction split, not a key stitch.

See `references/details.md` for the record shape, surface table, and worked refusals.

## Procedure

1. Name each object separately (name, host, product, bill, agency).
2. For each object, ask: path, date, bytes or vote, who can change it.
3. Mark analogy vs identity. "Rhymes with" is not "is."
4. Refuse slogan proof. Demand FRA-shaped locators: number, section, date, vote — or address, name, date.
5. If the ask is to recover a key, bind ENS, rewrite BoxD, or "update entire GitHub," return `BLOCKED` and load `skills/bounded-authority`.

## Must not

```text
CLARITY Act              != law (as of 2026-08-27)
congress.gov             != whitehouse.gov != justice.gov
bill text                != enforcement action
publication surface      != vault ownership
H.R. 3633                != recovery of a lost seed
H.R. 3633                != stitch of five names onto one key
Coinbase Wallet          != Coinbase.com
self-custody rule        != intermediary books
jaywisdom.eth            != jaywisdom.base.eth
MATCH on UTF-8 literal   != ENS ownership
authority_created        = false
```

## Output format

```text
Jurisdiction Split

Status: HOLD / PASS_WITH_NOTES / BLOCKED

Objects named (not merged):
- ...

Same-shape analogy (not identity):
- ...

Publication surfaces:
- ...

Records (number / section / date / vote or address / name / date):
- ...

Missing:
- ...

Refused:
- key recovery from a bill
- .gov host as owner of an ENS name
- collapsing Wallet vs .com
- unbounded GitHub write

Final determination:
- role=labor
- authority=false
```

## Related

Companion skills: `skills/evidence-first-judgment`, `skills/bounded-authority`, `skills/replayable-reasoning`.
