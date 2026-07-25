---
name: mcp-builder
description: Wire Claude to any tool. OmniSkill Developers crew — bundled copy of the MCP Builder skill.
disable-model-invocation: true
---

# MCP Builder

> Wire Claude to any tool · OmniSkill Developers crew

**Bundled — nothing to install.** The full MCP Builder skill ships inside this plugin.

## Use it

Read `${CLAUDE_SKILL_DIR}/vendor/SKILL.md` and follow it. That file is the authority for this capability; the notes below are the OmniSkill house rules layered on top.

Its supporting files (scripts, references, assets) sit alongside it under `${CLAUDE_SKILL_DIR}/vendor/`. Resolve any relative path in that skill against `${CLAUDE_SKILL_DIR}/vendor/`, not the working directory.

## House rules

Use it to expose an external API or internal tool to Claude as an MCP server. Prefer an MCP server over a bespoke script when the capability will be reused across sessions.

## Attribution

Vendored verbatim from [anthropics/skills](https://github.com/anthropics/skills), licensed **Apache-2.0**. The upstream license ships at `${CLAUDE_SKILL_DIR}/vendor/LICENSE.txt`. Unmodified — upstream is the place to send fixes.
