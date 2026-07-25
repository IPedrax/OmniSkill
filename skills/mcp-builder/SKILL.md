---
name: mcp-builder
description: Wire Claude to any tool. OmniSkill Developers crew — adapter that delegates to the MCP Builder skill.
disable-model-invocation: true
---

# MCP Builder

> Wire Claude to any tool · OmniSkill Developers crew

This capability is provided by **MCP Builder**, bundled with Claude Code — nothing to install.

## Use it

Invoke /mcp-builder and follow it. That skill is the authority here — this file only routes to it and adds the OmniSkill house rules below.

## House rules

Use it to expose an external API or internal tool to Claude as an MCP server. Prefer an MCP server over a bespoke script when the capability will be reused across sessions.

## If it is missing

It ships with Claude Code, so absence means bundled skills are disabled. Check the `disableBundledSkills` setting.
