---
name: social-content
description: This skill should be used when the user needs the OmniSkill Social & Content crew — writing posts for every platform, rewriting page copy, planning a topic map, scripting and producing video, rendering a launch video of a project, building hub-and-cluster pillar content, or designing lifecycle email sequences. Triggers on "/omniskill:social-content", "write a LinkedIn post", "rewrite this copy", "content calendar", "video script", "/brag", "make a launch video", "email sequence", "what should I post".
when_to_use: Use for content production and distribution — social posts, copy, video, and email.
allowed-tools: Read Glob
---

# 04 — Social & Content

> Feed the algorithm on autopilot. **Your content machine.**

## Pick the specialist

| Skill | Use when |
|---|---|
| `content-strategy` | Deciding what to make. **Start here for anything ongoing.** |
| `social` | Platform-native posts (X, LinkedIn, Instagram, TikTok, Threads) |
| `copywriting` | Rewriting existing page or product copy |
| `video` | Scripting and producing video |
| `brag` | A rendered 20s launch video of the user's own project or site, plus share copy |
| `pillar-content` | Long-form hub pieces with supporting cluster articles |
| `email-sequences` | Lifecycle flows — onboarding, nurture, win-back |

## Load it

Read `${CLAUDE_SKILL_DIR}/../<skill>/SKILL.md` and follow it. Its paths that start with the CLAUDE_SKILL_DIR placeholder mean its own folder, `${CLAUDE_SKILL_DIR}/../<skill>/`: only the invoked skill gets the placeholder filled in, and Bash never sets it, so write that full path into any command it gives you.

## Routing notes

For a one-off ask, go straight to the specialist. For anything ongoing, run `content-strategy` first — posting without a topic map produces volume, not compounding authority.

`pillar-content` and `social` compose: the pillar is the asset, the posts are the distribution.

`video` and `brag` split on who makes it: `video` writes the script for a person to shoot, `brag` renders the file itself from the product's own UI, for a launch or release. Its share copy goes to `social` next.
