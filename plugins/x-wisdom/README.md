# X Wisdom

Wisdom-bound agent for **X (Twitter) reads and posts**, with Agent Skills.

**Jason is the brains. Jay is the labor.** Reads are observed locators. Posts are publication: draft, then exact-action approval. The agent does not speak as Jason.

This is not a growth/engagement publisher. It is a judgment-bound X reader and poster: live posts are speech locators, not proof of the world.

## Attribution

| Role | Who |
| --- | --- |
| Brains (author, judgment, approval) | Jason Wisdom |
| Labor (this assistant, execution, records) | Jay |

## Agent

- **x-wisdom-assistant** — read timelines/threads/search; draft posts; never publish without brains approval. `authority=false`.

## Agent Skills

| Skill | Use when |
| --- | --- |
| **x-read-evidence** | Search, timeline, thread, profile, tweet-as-evidence |
| **x-post-gate** | Draft, reply, quote, thread, schedule, delete |

## Commands

- `/x-wisdom:x-read` — evidence report from public X
- `/x-wisdom:x-draft-post` — exact-text draft + approval gate

## Install

```bash
/plugin install x-wisdom@claude-code-workflows
```

Pairs with `computer-wisdom-assistant` if installed.

Live reads and sends need a connected X session in the harness. If X is disconnected, reads of current timelines are `BLOCKED`; drafts still work.

## Usage

```text
"What did @handle tweet about the launch?"
→ x-read-evidence (observed locators, not proof the launch shipped)

"Draft a reply"
→ x-read-evidence first, then x-post-gate (approval gate, no send)

"Just tweet that we launched"
→ x-post-gate (READY draft, BLOCKED send until exact-text approval)
```

## Posture

- Jason is the brains; Jay is the labor
- reads are observed, not true
- posts are publication (exact-action approval)
- no fake green
- no unbounded posting, reply storms, or engagement farming
- if X is not connected, say so and still draft; do not invent live timelines

Distinct from `social-publishing` (multi-platform SocialClaw) and `hermes-tweet` (Hermes + XQUIK). Those publish; this one waits for brains.

## License

MIT
