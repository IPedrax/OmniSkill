---
name: local-leads
description: Prospect lists of local businesses from Google Maps. OmniSkill Marketing crew. Drives gosom/google-maps-scraper with telemetry forced off: turns "clients like X in city Y" into queries, scrapes name, category, phone, site, rating and emails to CSV, then dedupes, scores and splits the list by the gap you can sell into.
disable-model-invocation: true
---

# local-leads

> Who to call on Monday · OmniSkill Marketing crew

The rest of this crew works on traffic that already exists. This one finds the businesses before they have heard of you: every pet shop in a city, every dental clinic in a neighbourhood, with phone, website, rating and review count, in one CSV.

Not bundled. It is a Go binary, [gosom/google-maps-scraper](https://github.com/gosom/google-maps-scraper) (MIT).

## Install once

Take the Linux release binary instead of building, which needs Go 1.27:

```bash
mkdir -p ~/tools/google-maps-scraper
curl -L -o ~/tools/google-maps-scraper/google-maps-scraper \
  https://github.com/gosom/google-maps-scraper/releases/latest/download/google_maps_scraper-$(curl -s https://api.github.com/repos/gosom/google-maps-scraper/releases/latest | jq -r .tag_name | tr -d v)-linux-amd64
chmod +x ~/tools/google-maps-scraper/google-maps-scraper
```

Then put a wrapper named `gmaps-scraper` on the PATH that exports `DISABLE_TELEMETRY=1` and `exec`s the binary. **Always call the wrapper, never the binary.** Upstream sends PostHog events by default and derives the machine ID from your external IP (`runner/runner.go`, `tlmt/`); only the exact value `1` turns that off. The first run downloads its own Playwright driver and Chromium into `~/.cache/ms-playwright-go`.

Do not install upstream's agent skill. Its `ensure-latest.sh` runs `npx --yes skills update` on every start, and it tells the agent to run Docker without asking.

## Run it

1. **Turn the ask into queries**, one per line, in the language of the market: `pet shop em Curitiba`, `clínica odontológica Batel Curitiba`. One category and one place per line. A single Maps search runs dry well before a big city does, so split it by neighbourhood instead of hoping `-depth` digs deeper. Tag a line with `#!#<id>` to carry your own id into the `input_id` column.
2. **Start small, then widen:**

```bash
gmaps-scraper -input queries.txt -results leads.csv -lang pt -depth 1 -email -exit-on-inactivity 3m
```

`-depth 1` returns about 15 to 20 places per query, which is enough to check the queries are right. Raise it to 5 or 10 for the real run. `-email` visits each business's own website to find addresses, so it is slower and touches third-party sites. For "within 3 km of here", add `-geo 'lat,lng' -radius 3000` and post-filter by `latitude`/`longitude`, because Maps does not respect the radius strictly. `-resume` continues a run that was interrupted. Keep `-c` at 1 or 2 without proxies, because higher concurrency gets blocked sooner.

3. **Clean before you show it.** Dedupe on `place_id` (overlapping neighbourhoods repeat places), drop places whose `status` says closed, and keep the columns that sell: `title`, `category`, `phone`, `website`, `emails`, `review_count`, `review_rating`, `complete_address`, `link`. Write a short Python script for this, not a spreadsheet by hand.

## Score by the gap you can sell into

A raw list is a phone book. Before handing it over, ask what is being sold and split the list by the signal that shows the need:

| Selling | The signal | Column |
|---|---|---|
| Websites | No site, or a site that is only a social profile | `website` empty or an Instagram/Facebook URL |
| Reputation, reviews | Plenty of reviews, a weak rating | `review_count` high, `review_rating` under 4.2 |
| Google profile, local SEO | Few reviews, no hours, no photos | `review_count` low, `open_hours` empty |
| Booking, ordering | A busy place with no online booking | `reservations` / `order_online` empty or `null`, high reviews |

Hand over the top 20 to 50 per segment, each with the one-line reason it is on the list. That reason is the opening line of the call. From there, `mktg-psychology` and Social & Content's `copywriting` write the outreach, and `cro` fixes the landing page they get sent to.

## House rules

**Business contact data, not people.** Collect what a business publishes as its own contact. When a phone or email is clearly a person's own (a self-employed professional's mobile, a name@gmail), it is personal data under LGPD (or GDPR). The outreach then needs a legitimate-interest basis, a clear way to opt out, and the list must not be resold. Say this once whenever the list will be used for contact.

**One person writing, not a blast.** Mass WhatsApp sends break WhatsApp's terms and get the number banned, and bulk cold email from a fresh domain lands in spam and damages that domain. Suggest a few dozen personal messages a day over any automation.

**Scraping Maps is against Google's terms.** Keep runs modest, never log into a Google account in the scraper, and don't promise the user an always-on pipeline. A blocked IP means slowing down, not adding proxies by reflex.

## Where it sits in the crew

Upstream of everything else in Marketing: this produces the audience, the others work on what it sees. For one company's footprint (who owns it, what else they run), that is the OSINT side, not this.

## Source

[google-maps-scraper](https://github.com/gosom/google-maps-scraper) by gosom · **MIT**. Nothing is vendored here; the binary installs from its GitHub release.
