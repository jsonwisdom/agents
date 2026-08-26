# Wisdom Team

Reverse-replay locators into a **named roster in the same turn**. Jason is the brains. Jay is the labor. The team is created from the record, not from a staffing meeting.

Forward replay writes a determination for later. Reverse replay starts from artifacts that already exist (plugin paths, PRs, receipts) and reconstructs the question and the labor they already imply — then names those seats **right then**.

## Attribution

| Role | Who |
| --- | --- |
| Brains (author, judgment, approval) | Jason Wisdom |
| Labor (this assistant, records, roster) | Jay |

## Agent

- **wisdom-team-assistant** — reverse-replay locators; name the smallest covering roster immediately. `authority=false`.

## Agent Skills

| Skill | Use when |
| --- | --- |
| **reverse-replay** | Locators first; reconstruct question, brains, and implied labor |
| **team-from-replay** | Name seats from that record in the same turn |

## Commands

- `/wisdom-team:from-record` — reverse replay + roster in one output
- `/wisdom-team:create-team` — exact-seat work gate for a roster already named from locators

## Install

```bash
/plugin install wisdom-team@claude-code-workflows
```

Pairs with `computer-wisdom-assistant` and `x-wisdom`. Those plugins are labor seats when their paths are locators. They are not auto-added without locators.

## Usage

```text
"Reverse replay and create the team right then"
→ reverse-replay + team-from-replay
→ roster named now; work still gated

Locators: plugins/computer-wisdom-assistant/, plugins/x-wisdom/
→ brains: Jason
→ labor-judgment: computer-wisdom-assistant
→ labor-x: x-wisdom-assistant
→ no extra seats
```

## Posture

- Jason is the brains; Jay is the labor
- locators first
- smallest covering set
- naming a roster is not a ship
- missing locators are `BLOCKED`, not a guessed crew

Distinct from `agent-teams` (generic review/debug/feature presets). This plugin reconstructs Jason's wisdom labor from records.

## License

MIT
