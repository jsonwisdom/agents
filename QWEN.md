# Qwen Code — setup guide

> The canonical context file is [`AGENTS.md`](AGENTS.md) at the repo root. Qwen Code
> reads it via `qwen-extension.json` (`contextFileName`). This guide covers Qwen-specific
> setup only. Do not point `contextFileName` at this file — it would be injected every prompt.

## Install

Generated trees live under `.qwen/` (gitignored) so they never overwrite Gemini's
extension-root `skills/`, `agents/`, and `commands/`. Clone, generate, then install locally:

```bash
gh repo clone wshobson/agents ~/agents && cd ~/agents
make generate HARNESS=qwen
qwen extensions install .
# restart Qwen Code
```

During development, `qwen extensions link .` symlinks the clone so you don't reinstall
after regenerating. In-repo, Qwen also loads `.qwen/skills` and `.qwen/agents` as project
skills/agents once generated.

## What you get

Counts live in [`AGENTS.md`](AGENTS.md). After generate:

- **Skills** at `.qwen/skills/<plugin>__<skill>/SKILL.md` — describe a task to activate
- **Subagents** at `.qwen/agents/<plugin>__<agent>.md` — invoke with `@<agent>` or `/agents`
- **Slash commands** at `/<plugin>` and `/<plugin>:<command>` — Markdown with `{{args}}`

## Qwen-specific differences

| Capability | Claude Code | Qwen Code |
|---|---|---|
| Plugin installation | `/plugin install` | `qwen extensions install <path-or-url>` |
| Context file | `CLAUDE.md` (symlink to `AGENTS.md`) | `qwen-extension.json` → `AGENTS.md` |
| Per-agent tool allowlist | `tools:` (Claude names) | `tools:` remapped to Qwen names (`read_file`, …) |
| Skill / agent discovery | native | native under `.qwen/` (and via the extension) |
| Model assignment | per-agent aliases | `inherit` (default) / `fast` (haiku) |
| Commands | Markdown + `$ARGUMENTS` | Markdown + `{{args}}` (TOML deprecated) |
| `TodoWrite` tool | yes | `todo` equivalent, not a 1:1 port |

## Regenerating

```bash
make generate HARNESS=qwen                            # all plugins
make generate HARNESS=qwen PLUGIN=javascript-typescript   # one plugin
make clean-generated HARNESS=qwen                     # remove `.qwen/` output
```

`qwen-extension.json` is committed and rewritten by `emit_global`. Do not hand-edit it.

## See also

- [`AGENTS.md`](AGENTS.md) — canonical context (cross-harness conventions)
- [`docs/harnesses.md`](docs/harnesses.md) — full capability matrix
- [`docs/round-trip-results.md`](docs/round-trip-results.md) — round-trip verification recipes
