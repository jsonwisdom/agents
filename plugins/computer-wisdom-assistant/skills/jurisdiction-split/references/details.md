# Jurisdiction-split details

Load this file when the navigation in `SKILL.md` is not enough to keep two similarly branded objects apart.

This is teaching. It is not legal advice, not a court finding, and not a grant of recovery power. `authority=false`.

## Record shape for a bill

A usable legislative receipt names:

| Field | Why |
|---|---|
| bill number | H.R. 3633, not "the clarity thing" |
| congress | 119th |
| title | Digital Asset Market Clarity Act of 2025 |
| chamber + action | House passage, committee report, cloture on motion to proceed |
| date | calendar day of that action |
| tally | yeas/nays when a roll call exists |
| status vs law | passed House is not "became law" |
| host | congress.gov is a publication surface for *that* object |

Falsifier: a later action on congress.gov that changes status (Senate passage, veto, public law number). Until then, do not speak as if the statute exists.

White House talking points and DOJ enforcement pages may *mirror* press about the same topic. Mirroring is not ownership of the bill, of an ENS name, or of a wallet.

## Publication surfaces

| Host | What it can be | What it is not |
|---|---|---|
| congress.gov | bill text, CRS summaries, votes, actions | a vault; a key-recovery desk |
| whitehouse.gov | administration statements / signing theater | the statute; an ENS registrar |
| justice.gov | enforcement after the fact (fraud, BSA, unregistered offering) | the naming layer; Coinbase support |
| sec.gov / cftc.gov | that agency's instrument | Congress; each other |

Same HTML blob copied across hosts is still **two publication events** if the hosts differ. Hash the bytes you fetched; do not alias the hosts.

## Market split (teaching, not a ruling)

The House-passed shape of H.R. 3633 is commonly described as:

- **digital commodity** → mostly CFTC
- **investment contract / security** → SEC
- plus recordkeeping and customer-asset rules
- "mature blockchain" vs "issuer still running the show"

Do not promote that one-line summary to a legal classification of any named token in this repo. Classification of a specific asset needs an instrument + date + section, not this skill.

SEC and CFTC can each publish their own "clarity." That is **three pens, one word**. Count pens. Do not merge them.

## Custody split (teaching)

| Product-shaped name | Custody class (until proven otherwise) |
|---|---|
| Coinbase.com / exchange / intermediary | books, account, maybe recovery policy of *that* product |
| Coinbase Wallet / self-custody | if published rule is no seed, no wallet, a bill about intermediary books does not open the wallet |

Do not fetch or invent Coinbase policy in this file. If a session needs the live rule, fetch that product's published page and hash it as its own object.

## Name split (teaching)

| Name | Class until proven |
|---|---|
| `jaywisdom.eth` | ENS mainnet name object (separate hash, separate registry) |
| `jaywisdom.base.eth` | Basename / L2 name object |
| `*.cb.id` | Coinbase-shaped identity product |
| UTF-8 literal SHA-256 of `jaywisdom.eth` | names 13 bytes only; not ownership |

A MATCH on the 13-byte literal does not bind ENS, does not prove resolver, and does not stitch Base or `cb.id`.

## Worked refusals

**"Update entire GitHub, we need control."**

Unbounded write. Status: `BLOCKED`. Name one repo, one path, one mutation. BoxD rewrite stays `HARD_REJECT`. ENS bind stays closed.

**"CLARITY will get my key back for 0x…"**

A jurisdiction bill, even if it later becomes law, argues who keeps books. It does not reconstruct a seed. Status: `BLOCKED` as recovery. Record the address as a locator if supplied; do not treat it as restored control.

**"It's on justice.gov so computerwisdom.base.eth is ours."**

Host ≠ name registry. Status: `BLOCKED`. Need the name, the registry record, the address, the date.

**"House passed it, so it's law."**

House passage is one action. Public law number is another. As of 2026-08-27, H.R. 3633 is not law. Status: `HOLD` or `PASS_WITH_NOTES` with the action table, never "the Act."

## Observed H.R. 3633 action table (this skill's freeze date)

Freeze date: 2026-08-27. Re-fetch congress.gov before promoting a newer status.

| Date | Action (publication surface: congress.gov) |
|---|---|
| 2025-05-29 | Introduced (Rep. Hill) |
| 2025-07-17 | House passed 294–134 (Roll no. 199) |
| 2026-05-14 | Senate Banking committee meeting on the measure |
| 2026-06-01 | Senate Banking reported with an amendment in the nature of a substitute; Calendar No. 423 |
| 2026-08-08 | Motion to proceed; cloture on the motion to proceed presented |

Not in this table: Senate passage, enrollment, presidential signature, public law number.

Cloture *talk* around mid-September 2026 is calendar pressure, not a vote receipt, until congress.gov records the vote.

## Companion posture

```text
facts_promoted     = 0
edges_inferred     = 0
silent_inference   = BLOCKED
authority_created  = false
ens_bind           = false
github_write       = false unless WRITE_TO names one path
BOXD_REWRITE       = HARD_REJECT
```
