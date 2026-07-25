---
name: context7
description: Pulls live, version-exact docs. OmniSkill Developers crew — adapter that delegates to the Context7 skill.
disable-model-invocation: true
---

# Context7

> Pulls live, version-exact docs · OmniSkill Developers crew

This capability is provided by **Context7**, an optional companion plugin from the official marketplace that runs as an MCP server.

## Use it

Invoke the `mcp__context7__resolve-library-id` and `mcp__context7__query-docs` tools and follow it. That skill is the authority here — this file only routes to it and adds the OmniSkill house rules below.

## House rules

Resolve the library id first, then query. Reach for this on *any* library, framework, or CLI question — including ones that feel familiar. Training data goes stale; these docs do not. Answering a version-specific question from memory is how wrong code gets written confidently.

## If it is missing

Install it with:

```bash
claude plugin install context7@claude-plugins-official
```

OmniSkill does not require it — this adapter is the only skill affected.
