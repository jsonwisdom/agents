# Computer Wisdom Assistant

Judgment plugin for technical claims, design tradeoffs, and engineering decisions. This is an assistant **with Agent Skills**: progressive-disclosure `SKILL.md` packages the agent loads on demand, not a single persona prompt.

**Jason is the brains. Jay is the labor.** The agent inspects, measures, and recommends. It does not claim Jason's authority.

## Attribution

| Role | Who |
| --- | --- |
| Brains (author, judgment, approval) | Jason Wisdom |
| Labor (this assistant, execution, records) | Jay |

## What you get

### Agent

- **computer-wisdom-assistant** — specialist for evidence-first review, bounded authority, replayable determinations, complexity budgets, and pattern fidelity. `authority=false` by default.

### Agent Skills

| Skill | Use when |
| --- | --- |
| **evidence-first-judgment** | Success, proof, verified, deployed, owned, or done claims |
| **bounded-authority** | Scoping work, mutations, MCP/tool permission, stop conditions |
| **replayable-reasoning** | Decisions that another session must be able to replay |
| **complexity-budget** | New layers, abstractions, ship vs polish, YAGNI |
| **pattern-fidelity** | Self-started work, closed doors, STORY_FORM vs evidence, ENS labels, grand gestures |

### Commands

- `/computer-wisdom-assistant:wisdom-review` — review a claim, diff, or "done" statement
- `/computer-wisdom-assistant:tradeoff-card` — structured options with complexity cost and required evidence

## Install

```bash
/plugin install computer-wisdom-assistant@claude-code-workflows
```

## Usage

Skills activate from the question:

```text
"Are we safe to say tests passed on this PR?"
→ evidence-first-judgment

"Can you just deploy this?"
→ bounded-authority (approval gate, no deploy)

"Why did we choose a queue here?"
→ complexity-budget + replayable-reasoning

"This teaching proves we should bind the wallet and ship a new agent."
→ pattern-fidelity (STORY_FORM is not evidence; no identity bind; small change or BLOCKED)
```

Or invoke the agent / commands directly.

## Posture

- Jason is the brains; Jay is the labor
- witness-only unless the operator (brains) approves an exact mutation
- no fake green; HOLD / BLOCKED is valid
- no unbounded tasks
- complexity is a budget
- determinations are replayable from locators, not chat memory
- STORY_FORM (teaching presentation) is not evidence; declared labels stay unbound

Composes with receipt and review plugins; it does not replace CI or cryptographic enforcement.

## License

MIT
