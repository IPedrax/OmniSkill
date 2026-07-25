---
name: ai-seo
description: Rank inside AI assistant answers. OmniSkill Marketing crew — optimizes for retrieval and citation by AI search, chat assistants, and AI overviews rather than blue links.
disable-model-invocation: true
---

# AI SEO

> Rank inside AI answers · OmniSkill Marketing crew

Being cited when someone asks an AI assistant rather than a search engine. Related to classic SEO but optimising for a different mechanism: retrieval and citation, not ranking and clicking.

## How this differs

Classic SEO wins a position and earns a click. AI search retrieves passages, synthesises an answer, and cites some sources. The unit of value is **the passage**, not the page — and much of the time there is no click at all.

That changes what to optimise:

| Classic SEO | AI SEO |
|---|---|
| Page ranks | Passage gets retrieved |
| Click-through | Citation and mention |
| Keyword targeting | Question and entity coverage |
| Page-level authority | Passage-level extractability |

## 1. Write extractable passages

An AI system retrieves chunks. A chunk that only makes sense with the surrounding page will not be used.

- **Answer the question in the first sentence** under a heading, then elaborate. Inverted pyramid, always.
- **Make each section self-contained.** Repeat the entity name rather than relying on "it" — a chunk starting with "It supports three modes" is unusable on its own.
- **Use question-shaped headings** matching how people actually ask.
- **Keep paragraphs tight** — 2–4 sentences chunk cleanly; a 300-word block does not.
- **Put facts in lists and tables.** Structured data extracts far more reliably than prose.

## 2. Be specific and citable

AI systems favour sources with concrete, verifiable specifics. Numbers, dates, named entities, and stated methodology all raise the odds of citation. Vague marketing prose is unretrievable — there is nothing in it to quote.

State facts plainly and attributably: "As of March 2026, the free tier includes 10,000 requests per month" is citable. "Generous free tier" is not.

## 3. Build entity clarity

These systems reason over entities. Make it unambiguous what the company is, what it does, and how it relates to the category.

- Consistent naming and description everywhere
- Organization and Product schema markup
- A clear, factual About page
- Presence in the sources these systems trust: Wikipedia and Wikidata where genuinely notable, industry directories, review platforms

## 4. Earn third-party mentions

AI answers frequently synthesise from sources *other than* the company's own site. Being described accurately across reviews, comparisons, listicles, and forum discussions matters as much as owned content.

Prioritise: category review sites, community discussions where the category is debated, and comparison content — including comparisons written by others.

## 5. Answer comparison and alternative queries directly

"X vs Y" and "alternatives to X" are heavily used AI prompts. Publish honest comparisons, including where the competitor is the better fit. Balanced comparisons get cited; one-sided ones get skipped, and being cited as the honest source is worth more than winning a page nobody trusts.

## 6. Stay technically retrievable

Content must be in the server-rendered HTML. Many AI crawlers do not execute JavaScript, so client-rendered content is invisible to them.

Decide deliberately on crawler access in `robots.txt` (GPTBot, ClaudeBot, PerplexityBot, Google-Extended). Blocking them removes any possibility of citation — that is a legitimate strategic choice, but make it knowingly rather than by copying a template.

## 7. Measure

Attribution is genuinely hard here. Practical signals: referral traffic from AI assistants, branded search volume, and direct testing — ask the assistants the target questions periodically and record whether the brand appears and how accurately it is described.

Track accuracy, not just presence. Being cited with wrong information is worse than not being cited.

## Checks before delivering

- Every section answers its heading in the first sentence.
- Sections are self-contained with entities named, not pronouns.
- Specific, dated, verifiable facts replace vague claims.
- Content is server-rendered.
- Crawler access decided deliberately.
- Comparison and alternative queries are answered honestly.
