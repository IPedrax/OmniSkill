---
name: marketing
description: This skill should be used when the user needs the OmniSkill Marketing crew — auditing on-page SEO, generating programmatic SEO pages from data, ranking inside AI answers, lifting page and form conversion, scaling ad creative variations, or applying behavioral psychology to copy. Triggers on "/omniskill:marketing", "SEO audit", "why isn't this page ranking", "improve conversion", "write ad variations", "landing page isn't converting".
when_to_use: Use for acquisition and conversion work — search visibility, ad creative, and turning traffic into signups.
allowed-tools: Read Glob
---

# 03 — Marketing

> Copy, SEO and ads that convert. **Your growth engine.**

## Pick the specialist

| Skill | Use when |
|---|---|
| `seo-audit` | Diagnosing why a page underperforms in search |
| `programmatic-seo` | Generating many pages from a dataset |
| `ai-seo` | Being cited inside AI assistant answers |
| `cro` | Traffic arrives but does not convert |
| `ad-creative` | Producing and scaling ad variations for testing |
| `mktg-psychology` | Sharpening any of the above with behavioral triggers |

## Load it

Read `${CLAUDE_SKILL_DIR}/../<skill>/SKILL.md` and follow it.

## Routing notes

Diagnose before prescribing. A page that ranks but does not convert is a `cro` problem; a page nothing finds is a `seo-audit` problem. Treating the second as the first wastes the whole effort.

`mktg-psychology` is a multiplier, not a standalone — layer it onto copy the other five produce.
