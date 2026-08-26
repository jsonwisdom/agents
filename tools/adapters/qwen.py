"""Qwen Code adapter.

Qwen Code (`@qwen-code/qwen-code`) is a Gemini CLI fork with native SKILL.md skills,
markdown subagents, and markdown slash commands (TOML is deprecated). Generated trees
live under `.qwen/` so they never collide with Gemini's extension-root `skills/`,
`agents/`, and `commands/` output.

1. `.qwen/skills/<plugin>__<skill>/SKILL.md` — namespaced SKILL.md (Qwen allows `_`).
2. `.qwen/agents/<plugin>__<agent>.md` — markdown subagents; models map to
   `inherit` / `fast`.
3. `.qwen/commands/<plugin>/<command>.md` — nested markdown commands become
   `/<plugin>:<command>`; plugin entry at `.qwen/commands/<plugin>.md` is `/<plugin>`.
4. Committed `qwen-extension.json` at repo root (`contextFileName: AGENTS.md`).
   `QWEN.md` is a hand-authored setup guide and is not generated.

Install: `make generate HARNESS=qwen && qwen extensions install .`
In-repo, Qwen also loads `.qwen/skills` and `.qwen/agents` as project skills/agents.
"""

from __future__ import annotations

import json
from pathlib import Path

from tools.adapters.base import (
    WORKTREE,
    AgentSource,
    CommandSource,
    EmitResult,
    HarnessAdapter,
    PluginSource,
    SkillSource,
)
from tools.adapters.capabilities import TOOL_NAME_MAPS, resolve_model


def _qwen_frontmatter(fm: dict) -> str:
    lines = ["---"]
    for k, v in fm.items():
        if isinstance(v, list):
            value = ", ".join(str(x) for x in v)
            lines.append(f"{k}: [{value}]")
        elif isinstance(v, bool):
            lines.append(f"{k}: {'true' if v else 'false'}")
        elif v is None:
            continue
        else:
            value = str(v).replace("\n", " ").strip()
            lines.append(f"{k}: {value}")
    lines.append("---")
    return "\n".join(lines)


def _rewrite_body_qwen_tools(body: str) -> str:
    """Rewrite backticked Claude tool names to Qwen's native identifiers."""
    out = body
    for camel, native in TOOL_NAME_MAPS["qwen"].items():
        out = out.replace(f"`{camel}`", f"`{native}`")
    return out


class QwenAdapter(HarnessAdapter):
    harness_id = "qwen"

    def emit_plugin(self, plugin: PluginSource) -> EmitResult:
        result = EmitResult()
        for skill in plugin.skills:
            self._emit_skill(plugin, skill, result)
        for agent in plugin.agents:
            self._emit_agent(plugin, agent, result)
        for cmd in plugin.commands:
            self._emit_command(plugin, cmd, result)
        self._emit_plugin_entry(plugin, result)
        return result

    def emit_global(self, plugins: list[PluginSource]) -> EmitResult:
        """Write committed `qwen-extension.json`. Does not generate `QWEN.md`."""
        result = EmitResult()
        name, version, description = self._marketplace_identity()
        payload = {
            "name": name,
            "version": version,
            "description": description,
            "contextFileName": "AGENTS.md",
            "commands": ".qwen/commands",
            "skills": ".qwen/skills",
            "agents": ".qwen/agents",
        }
        content = json.dumps(payload, indent=2) + "\n"
        result.written.append(self.write("qwen-extension.json", content))
        return result

    # ── Internals ──────────────────────────────────────────────────────────

    def _marketplace_identity(self) -> tuple[str, str, str]:
        """Read name/version/description from marketplace.json when present."""
        fallback = (
            "claude-code-workflows",
            "1.0.0",
            "Multi-harness agentic plugin marketplace.",
        )
        for root in (self.output_root, WORKTREE):
            mp = root / ".claude-plugin" / "marketplace.json"
            if not mp.is_file():
                continue
            try:
                data = json.loads(mp.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                continue
            metadata = data.get("metadata") if isinstance(data.get("metadata"), dict) else {}
            name = str(data.get("name") or fallback[0])
            version = str(metadata.get("version") or data.get("version") or fallback[1])
            description = str(
                metadata.get("description") or data.get("description") or fallback[2]
            )
            return name, version, description
        return fallback

    def _emit_skill(self, plugin: PluginSource, skill: SkillSource, result: EmitResult) -> None:
        skill_id = f"{plugin.name}__{skill.name}"
        rel_dir = Path(".qwen") / "skills" / skill_id
        fm = dict(skill.frontmatter)
        fm["name"] = skill_id

        body = _rewrite_body_qwen_tools(skill.body).rstrip() + "\n"
        content = _qwen_frontmatter(fm) + "\n\n" + body
        result.written.append(self.write(rel_dir / "SKILL.md", content))

        if skill.references_dir:
            for ref in sorted(skill.references_dir.rglob("*")):
                if ref.is_file():
                    rel = ref.relative_to(skill.references_dir)
                    result.written.append(self.mirror_file(ref, rel_dir / "references" / rel))

    def _emit_agent(self, plugin: PluginSource, agent: AgentSource, result: EmitResult) -> None:
        agent_id = f"{plugin.name}__{agent.name}"
        rel = Path(".qwen") / "agents" / f"{agent_id}.md"

        model, warning = resolve_model("qwen", agent.model)
        if warning:
            result.warnings.append(f"agent `{agent_id}`: {warning}")
        fm: dict = {
            "name": agent_id,
            "description": agent.description or f"{agent.name} (from {plugin.name})",
            "model": model,
        }
        if agent.tools:
            qwen_map = TOOL_NAME_MAPS["qwen"]
            fm["tools"] = [qwen_map.get(t, t) for t in agent.tools]

        body = _rewrite_body_qwen_tools(agent.body).rstrip() + "\n"
        content = _qwen_frontmatter(fm) + "\n\n" + body
        result.written.append(self.write(rel, content))

    def _emit_command(
        self, plugin: PluginSource, cmd: CommandSource, result: EmitResult
    ) -> None:
        """Emit `.qwen/commands/<plugin>/<command>.md` → `/<plugin>:<command>`."""
        rel = Path(".qwen") / "commands" / plugin.name / f"{cmd.name}.md"
        description = cmd.description or cmd.name.replace("-", " ").title()
        fm = {"description": description}
        prompt = self._command_prompt(plugin, cmd)
        content = _qwen_frontmatter(fm) + "\n\n" + prompt.rstrip() + "\n"
        result.written.append(self.write(rel, content))

    def _emit_plugin_entry(self, plugin: PluginSource, result: EmitResult) -> None:
        """Top-level `.qwen/commands/<plugin>.md` — Qwen exposes this as `/<plugin>`."""
        description = plugin.description or f"{plugin.name.replace('-', ' ').title()} plugin"
        rel = Path(".qwen") / "commands" / f"{plugin.name}.md"

        agent_list = ", ".join(f"`{plugin.name}__{a.name}`" for a in plugin.agents)
        skill_list = ", ".join(f"`{plugin.name}__{s.name}`" for s in plugin.skills)
        command_list = ", ".join(f"`/{plugin.name}:{c.name}`" for c in plugin.commands)

        parts = [description.rstrip(".") + "."]
        parts.append("")
        parts.append(f"This is the entry point for the `{plugin.name}` plugin.")
        if plugin.agents:
            parts.append("")
            parts.append(f"Subagents: {agent_list}. Invoke with `@<agent>` syntax.")
        if plugin.skills:
            parts.append("")
            parts.append(f"Skills: {skill_list}. Describe a matching task to activate.")
        if plugin.commands:
            parts.append("")
            parts.append(f"Commands: {command_list}.")
        parts.append("")
        parts.append("{{args}}")

        content = _qwen_frontmatter({"description": description}) + "\n\n" + "\n".join(parts) + "\n"
        result.written.append(self.write(rel, content))

    def _command_prompt(self, plugin: PluginSource, cmd: CommandSource) -> str:
        body = cmd.body.strip().replace("$ARGUMENTS", "{{args}}")
        lines = [
            f"You are running the `{cmd.name}` command from the `{plugin.name}` plugin.",
            "",
            "## Protocol",
            "",
            body,
            "",
        ]
        if cmd.argument_hint:
            lines.append(f"Arguments: {cmd.argument_hint}")
            lines.append("")
        joined = "\n".join(lines)
        if "{{args}}" not in joined:
            lines.append("{{args}}")
        return "\n".join(lines)
