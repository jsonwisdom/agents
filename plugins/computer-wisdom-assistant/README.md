# Computer Wisdom Assistant

Judgment plugin for technical claims, design tradeoffs, and engineering decisions. This is an assistant **with Agent Skills**: progressive-disclosure `SKILL.md` packages the agent loads on demand, not a single persona prompt.

## What you get

### Agent

- **computer-wisdom-assistant** — specialist for evidence-first review, bounded authority, replayable determinations, and complexity budgets. `authority=false` by default.

### Agent Skills

| Skill | Use when |
| --- | --- |
| **evidence-first-judgment** | Success, proof, verified, deployed, owned, or done claims |
| **bounded-authority** | Scoping work, mutations, MCP/tool permission, stop conditions |
| **replayable-reasoning** | Decisions that another session must be able to replay |
| **complexity-budget** | New layers, abstractions, ship vs polish, YAGNI |

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
```

Or invoke the agent / commands directly.

## Posture

- witness-only unless the operator approves an exact mutation
- no fake green
- no unbounded tasks
- complexity is a budget
- determinations are replayable from locators, not chat memory

Composes with receipt and review plugins; it does not replace CI or cryptographic enforcement.

## License

MIT
