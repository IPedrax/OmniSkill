---
name: marketing
description: This skill should be used when the user needs the OmniSkill Marketing crew — finding local clients from Google Maps, auditing on-page SEO, generating programmatic SEO pages from data, ranking inside AI answers, lifting page and form conversion, scaling ad creative variations, or applying behavioral psychology to copy. Triggers on "/omniskill:marketing", "find me clients", "lead list", "prospect businesses in", "SEO audit", "why isn't this page ranking", "improve conversion", "write ad variations", "landing page isn't converting".
when_to_use: Use for acquisition and conversion work — finding prospects, search visibility, ad creative, and turning traffic into signups.
allowed-tools: Read Glob
---

# 03 — Marketing

> Copy, SEO and ads that convert. **Your growth engine.**

## Pick the specialist

| Skill | Use when |
|---|---|
| `local-leads` | Finding clients: local businesses from Google Maps, scored by the gap you sell into |
| `seo-audit` | Diagnosing why a page underperforms in search |
| `programmatic-seo` | Generating many pages from a dataset |
| `ai-seo` | Being cited inside AI assistant answers |
| `cro` | Traffic arrives but does not convert |
| `ad-creative` | Producing and scaling ad variations for testing |
| `mktg-psychology` | Sharpening any of the above with behavioral triggers |

## Load it

Read `${CLAUDE_SKILL_DIR}/../<skill>/SKILL.md` and follow it. Its paths that start with the CLAUDE_SKILL_DIR placeholder mean its own folder, `${CLAUDE_SKILL_DIR}/../<skill>/`: only the invoked skill gets the placeholder filled in, and Bash never sets it, so write that full path into any command it gives you.

## Routing notes

Diagnose before prescribing. A page that ranks but does not convert is a `cro` problem; a page nothing finds is a `seo-audit` problem. Treating the second as the first wastes the whole effort.

`mktg-psychology` is a multiplier, not a standalone. Layer it onto copy the others produce.

`local-leads` is the one that works before there is any traffic: it finds who to approach. Ask what the user sells before scraping, because that decides which gap the list gets scored on.
