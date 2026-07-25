---
name: programmatic-seo
description: Generate SEO pages at scale from data. OmniSkill Marketing crew — picks a template pattern, validates demand, and builds pages that survive thin-content and doorway-page penalties.
disable-model-invocation: true
---

# Programmatic SEO

> Pages at scale from data · OmniSkill Marketing crew

Generating hundreds or thousands of pages from a dataset and a template. Powerful when the data is genuinely useful, and actively harmful when it is not.

## The rule that decides success

**Every generated page must be independently useful to a human who lands on it.** If the only difference between two pages is a swapped city name, that is a doorway page and it will be penalised — often taking the rest of the site's rankings with it.

Ask honestly: would someone bookmark this page? If no page in the set passes, do not build the set.

## 1. Find the pattern

The winning shape is a head term plus a modifier dimension where real search demand exists per combination:

- `{service} in {city}`
- `{product} vs {competitor}`
- `best {category} for {use case}`
- `{language} to {language} {tool}`
- `how to {task} in {software}`

Two dimensions is usually the practical limit. Three produces combinatorial pages nobody searches for.

## 2. Validate demand before building

Sample 20–30 combinations and check actual search volume. Expect a long tail — most pages will get little traffic, and that is fine if the aggregate works and each page is genuinely useful.

**Kill the combinations with no demand.** Generating the full cross-product because the data allows it is the single most common failure. 500 useful pages beat 50,000 empty ones, and the empty ones actively damage the useful ones.

## 3. Get the data right

The data *is* the product. It must be accurate, reasonably complete, and refreshable.

Pages with missing fields must degrade gracefully — never render "Price: undefined" or an empty section with a heading. Set a minimum-data threshold and skip pages that fall below it.

Plan the refresh cadence up front. Stale programmatic pages decay faster than hand-written ones because nobody notices them rotting.

## 4. Build the template

Each page needs unique, substantive content beyond the swapped variables:

- Real data specific to that combination — numbers, listings, comparisons
- A meaningful amount of unique text, not a spun paragraph
- Genuinely different, useful internal links to related combinations
- Unique title and meta description built from the variables
- Schema markup matching the content type

Include something that only exists on that page: a data table, a computed result, real reviews. That is what separates a useful page from a doorway.

## 5. Technical architecture

- **URLs** — clean, stable, predictable: `/service/plumbers/austin-tx`
- **Rendering** — static generation or SSR. Client-rendered content is a recurring cause of these pages never indexing.
- **Sitemaps** — split at 50,000 URLs, index file on top
- **Internal linking** — hub pages by dimension, plus related links on each page. Orphaned generated pages do not get crawled.
- **Crawl budget** — release in batches and watch indexation. Dumping 50,000 URLs at once gets a fraction indexed and the rest ignored.
- **Pruning** — plan to remove pages that get no impressions after a few months

## 6. Measure and prune

Track indexation rate, impressions per page, and the share of pages getting any traffic at all. A healthy set has most pages indexed and a meaningful minority getting traffic.

If indexation stalls below ~50%, the pages are too thin. Cut the set and deepen what remains — this is a correction, not a failure.

## Checks before delivering

- Every page passes the "independently useful" test.
- Demand validated on a sample before full generation.
- Missing data degrades gracefully.
- Pages are server-rendered or statically generated.
- Internal linking connects every page.
- A refresh and pruning plan exists.

Pair with `/omniskill:seo-audit` for the on-page fundamentals and `/omniskill:content-strategy` for how this fits the wider topic map.
