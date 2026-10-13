---
name: startup-council
description: A board meeting for a business idea, grounded in numbers. OmniSkill Finance crew. Runs the unit economics and a simulated buyer panel first, then puts the idea to seven advisors on a mix of models (the Offers, Monopoly and Product lenses, a CFO, the Customer, a Contrarian, an Executor), has them peer-review each other anonymously, and ends in one verdict (fund, fund if, pass) with conditions. Bundles the full founder pack for everything after the verdict.
disable-model-invocation: true
---

# startup-council

> Argue over the margins, not the vibe · OmniSkill Finance crew

One model asked "is this a good business?" gives one confident answer. This runs the question the way a council does: several advisors who each see it from a different angle, on different models so they genuinely disagree, critiquing each other without knowing who wrote what, and a chair who has to reconcile them. And before anyone gives an opinion, the CFO math and a buyer panel put real numbers on the table.

Bundled: the eleven-skill [founder pack](https://github.com/Jakeschincariol/founder-skill) lives in `${CLAUDE_SKILL_DIR}/vendor/founder-*/`. A path inside one of those files that starts with the CLAUDE_SKILL_DIR placeholder means that file's own folder, for example `${CLAUDE_SKILL_DIR}/vendor/founder-cfo/`. Write the full path into every command. Python 3.8+, nothing to install.

Everything is written to `founder/` in the user's project, which is where the pack's other skills look.

## Model mix

Every sub-agent below gets an explicit `model` on the Agent call, so the council is several models arguing, not one model in seven hats:

| Role | Model |
|---|---|
| Offers lens · CFO | `opus` |
| Monopoly lens · Contrarian | `sonnet` |
| Product lens · Executor | `fable` |
| The Customer | `haiku` |
| Reviewers A, B, C | `opus`, `sonnet`, `fable` |
| Buyer panel (and supply panel) | rotate by panelist number: `sonnet`, `haiku`, `fable`, `opus` |
| Chair | you, in this session |

When the bundled founder skills run on their own (`founder-board`'s three members, `founder-consumer`'s buyers), use the same assignment. If the Agent tool here rejects the `model` parameter, run everything on the default model and say once that the council ran single-model, so its agreement is weaker evidence.

Different models still share a lot of training. The mix catches one model's quirks; it does not turn simulated opinions into market evidence.

## 1. The idea

Follow Step 0 of `vendor/founder-board/SKILL.md`: write `founder/idea.md`, asking at most three questions for anything missing (name, customer, product, price). Never invent a budget, a market size or a competitor.

## 2. Numbers first

Tell the user up front: this step is about 20 sub-agent calls plus a few questions about costs.

- **Buyers.** Follow `vendor/founder-consumer/SKILL.md` steps 1 to 3 with `--n 20`, applying the model rotation. Write `founder/panel/models.json` mapping each buyer id to its model, then report the buy rate per model next to the headline. A model that buys far more readily than the rest is an artifact to discount; say so.
- **Localize the panel.** `panel.py` deals English names and prints income in `$`. Outside an English-speaking dollar market, run `${CLAUDE_SKILL_DIR}/scripts/localize.py` on the panel folder: with `--names` (local first names, at least one per panelist) right after `init`, and with `--currency` (e.g. `R$`) after `prompts` and again after `tally`. Write `customer.json` incomes in the local currency.
- **Both sides of a marketplace.** If the business only works when a second group shows up (drivers, hosts, sellers, tutors, restaurants), run a second panel for that side: its own `founder/customer-supply.json` and `founder/pitch-supply.md` (what they earn, what they pay the platform, what is asked of them), `--dir founder/panel-supply --n 10`, same model rotation and localization. A demand-only panel hides the side most marketplaces die on.
- **Unit economics.** Follow `vendor/founder-cfo/SKILL.md` steps 1 and 2: `founder/numbers.json` from the user's real quotes where they have them, estimates marked as estimates in `founder/cfo-sources.md`, and the ramp checked against the panel's first-month purchases. Run `unit_economics.py`.

If the user cannot give costs yet, run the council on the panel alone and record "CFO: inputs missing" as the first open question; don't make up a rent.

## 3. The brief

Write `founder/council/brief.md`, the only thing every advisor sees: `idea.md`, the panel headline with its top three reasons to pass in buyers' words (and the supply panel's, if one ran), the CFO results (contribution per sale, margin, break-even per day against capacity, cash needed, payback), and what is still unknown.

Add a **Built-in constraints** section: every limit the product already enforces, read from its code, settings or terms when there are any (minimum and maximum prices, per-km or per-unit floors, caps, fees, who pays the payment processor). Do the arithmetic for the price buyers named: if the floor makes the "bargain" price impossible, say so in the brief. In the RotaHub test run only one advisor noticed that a R$1.20/km floor forbids the R$9.50 seat buyers wanted. No opinion of yours. Sub-agents cannot see this conversation, so it must stand alone.

## 4. Convene: seven advisors, one message

Launch all seven at once (Agent tool, `general-purpose`, the model from the table). Each is told: read `founder/council/brief.md`, apply only your lens, write 150 to 300 words to `founder/council/<lens>.md`, end with `Score: 1-10 | Vote: FUND / FUND IF / PASS` and, for FUND IF, the conditions.

- **Offers, Monopoly, Product:** the three sections of `vendor/founder-board/lenses.md`. Pass the lens text in the prompt. They are published frameworks, not the people: never "Hormozi says".
- **The CFO:** judges only the economics in the brief. Does each sale make money, does break-even fit capacity, how long is the cash runway, which single number moves the outcome most.
- **The Customer:** speaks as the target buyer from `idea.md`, using the panel's objections. Would I pay, what would stop me, what would change my mind.
- **The Contrarian:** assumes a fatal flaw exists and looks for it. In a regulated sector (passenger transport, food, health, finance, education, alcohol, personal data) the prompt also says: check licensing, liability and insurance first, because a business that is illegal as built fails before any margin matters.
- **The Executor:** ignores strategy. What happens Monday morning, and what is the cheapest real test this month?

## 5. Anonymous review

Relabel the seven memos Response A to G in a random order, deleting any line that names the lens ("As the CFO..."), so reviewers judge arguments, not roles. Three reviewers (opus, sonnet, fable) each read all seven and answer in under 200 words: the strongest response and why; the biggest blind spot and whose; what all seven missed.

## 6. The chair's verdict

You, with everything de-anonymized. Write `founder/council.md`:

1. **The vote:** e.g. "4 fund if, 2 pass, 1 fund", the average score, and which way each model leaned.
2. **Where they agree:** points reached independently. Highest confidence.
3. **Where they clash:** both sides, and why reasonable advisors land differently. Don't smooth it over.
4. **What review caught:** blind spots that surfaced only in peer review.
5. **The verdict:** FUND, FUND IF (the merged conditions, as a checklist; in a regulated sector one condition is a legal read through the Legal crew's `legal-risk`) or PASS, in one paragraph, with the strongest version of this business the council can see, even if it isn't what was pitched.
6. **Next:** the one founder skill to run next and why, from `board → competitors → consumer → pricing → offer → cfo → marketing → brand → ops → launch → plan`. Each lives in `vendor/founder-<name>/` and reads what is already in `founder/`.

Then tell the user the vote and verdict in two lines, the top condition, and the next step.

## House rules

**Simulated is not validated.** Say once: the panel and the advisors surface objections and weak numbers well and predict real demand badly, since models lean agreeable. Treat buy rates as an upper bound, and confirm the big calls with real people (a waitlist, a pre-sale, a priced landing page) before money moves. Never present panel quotes as testimonials.

**Score the business, not the founder.** A PASS is a result. Say it plainly.

**Analysis, not advice.** Like the rest of Finance: stated assumptions, not licensed financial or legal advice.

## Where it sits in the crew

Before `3-statements`: the council decides whether there is a business worth modelling. `pricing` goes deeper once the panel's price answers exist; `pitch-deck` comes after a FUND. For a local business the user wants as a client rather than a venture of their own, Marketing's `local-leads` is the door, not this.

## Attribution

Vendored from [Jakeschincariol/founder-skill](https://github.com/Jakeschincariol/founder-skill) @ `fd9385b` (all eleven skills, without tests), licensed **MIT**. License at `${CLAUDE_SKILL_DIR}/vendor/LICENSE`. The council pipeline (independent advisors, anonymous peer review, a chair) follows Andrej Karpathy's LLM Council.
