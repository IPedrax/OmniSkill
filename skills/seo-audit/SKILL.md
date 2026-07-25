---
name: seo-audit
description: On-page and technical SEO audit. OmniSkill Marketing crew — diagnoses why a page underperforms in search across crawl, index, content, and Core Web Vitals.
disable-model-invocation: true
---

# SEO Audit

> Diagnoses on-page SEO · OmniSkill Marketing crew

## Diagnose in order

The order matters. A page that cannot be crawled will not be fixed by better copy, and a page that ranks fine but does not convert is a `/omniskill:cro` problem, not this one.

**1 — Can it be crawled?**
`robots.txt` rules, `noindex` meta or header, canonical pointing elsewhere, orphan page with no internal links, blocked by authentication, or a `nofollow` path to it.

**2 — Is it indexed?**
Check `site:` in the search engine and Search Console coverage. Common causes of exclusion: duplicate content with a canonical elsewhere, thin content, soft 404, or crawl budget exhausted on faceted URLs.

**3 — Does it match intent?**
Search the target query and read the top ten results. If they are all comparison lists and the page is a product page, the page is the wrong *format* — no amount of optimisation fixes an intent mismatch. Classify intent as informational, commercial, transactional, or navigational, and match it.

**4 — Is the on-page work done?**
- **Title** — 50–60 characters, primary keyword near the front, and genuinely compelling. It is the click decision.
- **Meta description** — 140–160 characters. Not a ranking factor; is a click-through factor.
- **One H1** matching the page topic; H2/H3 in a real hierarchy.
- **URL** — short, readable, hyphenated, stable.
- **Content depth** relative to what ranks. Compare against the top results rather than a word-count target.
- **Internal links** in from relevant pages, with descriptive anchor text. This is the most under-used lever on most sites.
- **Images** — descriptive `alt`, compressed, explicit `width`/`height`.
- **Schema** — Article, Product, FAQ, Breadcrumb as applicable; validate it.

**5 — Are Core Web Vitals passing?**
LCP under 2.5s, INP under 200ms, CLS under 0.1. Use field data (CrUX) over lab data where available — lab data on a fast machine hides what real users experience.

Common causes: unoptimised hero image (LCP), heavy third-party JavaScript (INP), images and ads without reserved space (CLS).

**6 — Is the technical foundation sound?**
HTTPS throughout, mobile usability, no redirect chains, XML sitemap current and submitted, hreflang correct if multilingual, 404s handled, pagination sane.

## Prioritise

Rank fixes by impact × effort. A title rewrite is minutes and moves click-through; a full migration is months. Lead with the three changes that matter most and state the expected effect of each.

Be explicit when the answer is "this page is fine, the problem is elsewhere". Sites lose more time to optimising already-adequate pages than to any technical fault.

## Verify

Use `/omniskill:webapp-testing` to render the page as a crawler would and confirm content appears without JavaScript where that matters. Client-rendered content that only appears after hydration is a recurring and invisible cause of ranking failure.

## Output

A table: issue, category, severity, evidence, fix, expected impact. Then the top three actions in priority order.

## Checks before delivering

- Crawl and index status verified, not assumed.
- Intent match checked against actual SERP results.
- Core Web Vitals from field data where available.
- Recommendations ranked by impact, with the top three called out.
