---
name: context7
description: Pulls live, version-exact docs. OmniSkill Developers crew — Context7 MCP server, with self-setup when it is not connected.
disable-model-invocation: true
---

# Context7

> Pulls live, version-exact docs · OmniSkill Developers crew

An **MCP server**, not skill content — so unlike the rest of the workforce it cannot be bundled into this plugin. It has to be connected to the session.

## Use it

Two tools, in order:

1. `mcp__context7__resolve-library-id` — turn a library name into a Context7 id.
2. `mcp__context7__query-docs` — query that id for the specific API, config, or migration detail.

Reach for this on **any** library, framework, SDK, or CLI question — including ones that feel familiar. Training data goes stale; these docs do not. Answering a version-specific question from memory is how wrong code gets written confidently.

## If the tools are not available

**Set it up rather than falling back to memory.** Check first — the tools may be present but deferred, so search before concluding they are missing.

If they genuinely are not connected, offer to install it and, on approval, run:

```bash
claude mcp add context7 --scope user -- npx -y @upstash/context7-mcp@latest
```

Then tell the user to restart Claude Code, since MCP servers connect at session start.

The plugin form works too, if they prefer managing it that way:

```bash
claude plugin install context7@claude-plugins-official
```

Do not install without asking — it adds a server that runs whenever Claude Code is open.

**Until it is connected**, say plainly that the answer is coming from training data and may be out of date for the version in use. Never present a remembered API as verified.

## Attribution

Context7 is by [Upstash](https://context7.com). Distributed as an MCP server; nothing is vendored here.
