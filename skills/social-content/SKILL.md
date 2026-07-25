---
name: social-content
description: This skill should be used when the user needs the OmniSkill Social & Content crew — writing posts for every platform, rewriting page copy, planning a topic map, scripting and producing video, building hub-and-cluster pillar content, or designing lifecycle email sequences. Triggers on "/omniskill:social-content", "write a LinkedIn post", "rewrite this copy", "content calendar", "video script", "email sequence", "what should I post".
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
| `pillar-content` | Long-form hub pieces with supporting cluster articles |
| `email-sequences` | Lifecycle flows — onboarding, nurture, win-back |

## Load it

Read `${CLAUDE_SKILL_DIR}/../<skill>/SKILL.md` and follow it.

## Routing notes

For a one-off ask, go straight to the specialist. For anything ongoing, run `content-strategy` first — posting without a topic map produces volume, not compounding authority.

`pillar-content` and `social` compose: the pillar is the asset, the posts are the distribution.
