# Ship Guy — Miami Page Update (July 2026)

Only one file changed: **`car-shipping-miami-fl.html`**
Everything else in this zip is your original site, untouched. Deploy the whole
folder, or replace just that one page.

Target keyword: **Auto Transport Miami Florida**

---

## What changed

| # | Change | Why |
|---|--------|-----|
| 1 | **Title & meta description** rewritten to lead with "Auto Transport Miami, FL" and include price + pickup speed | Keyword match in title; CTR lift from concrete numbers in the SERP snippet |
| 2 | **Quick-answer box** added under the intro (cost range, pickup timing, snowbird swing) | Targets the featured snippet and Google AI Overviews, which extract short direct answers |
| 3 | **Est. open rate column** added to all 8 rows of the route table + dated footnote | Turns the page from an article into a tool; unique data Google's scaled-content policy rewards |
| 4 | **New section: "What Shapes Your Miami Auto Transport Price"** with two seasonal-direction cards | Original local expertise (E-E-A-T); captures "cheapest time to ship car to Florida" queries |
| 5 | **Two new local callouts**: condo/high-rise delivery, hurricane season + PortMiami export | First-hand operational knowledge no competitor template has |
| 6 | **FAQ expanded 6 → 9** (personal items, presence at pickup, insurance) and the cost answer given real ranges | Matches high-volume People Also Ask queries |
| 7 | **JSON-LD schema updated**: FAQPage mirrors on-page text word-for-word, 3 new questions, Offer pricing, MC/USDOT identifiers on the provider | Rich results eligibility; mismatched schema vs. on-page text is a violation |
| 8 | **E-E-A-T byline** above the footer: license numbers, FMCSA SAFER verify link, reviewer credit, last-updated date | The strongest trust signal available for a YMYL-adjacent money transaction |

Preserved exactly as-is: header, nav, mobile menu, footer, brand tokens
(`--brand:#0b34c0`), Plus Jakarta Sans / Inter, hero image, reveal animations,
and the **berocker quote widget iframe** in the hero (`#quoteForm`).

---

## Before you publish — required

1. **Replace `[XXXXXX]` license placeholders.** They appear in two places:
   - the E-E-A-T byline near the bottom of the page
   - the JSON-LD `identifier` block in `<head>`

   The byline links to the FMCSA SAFER database and invites visitors to verify
   you. Publishing fake or blank numbers there is worse than omitting the
   section entirely.

2. **Replace `[Full Name]`, `[Title]`, `[X] years`** in the byline with a real
   person on your team. Ideally link it to a bio page.

3. **Swap the rate estimates for your own data.** The figures are realistic
   market ranges, but your quote history is better — and it's the thing
   competitors can't copy. The footnote promises a quarterly refresh; keep that
   promise or remove the date.

## After you publish

- Submit the URL in Google Search Console → URL Inspection → Request Indexing.
- Validate the schema at `search.google.com/test/rich-results`.
- Watch Search Console for 4–8 weeks. Track **long-tail** impressions
  ("cheapest time to ship car to Florida", "enclosed transport Brickell",
  "Miami to New York car shipping cost") — not just the head term, which is a
  12–18 month climb against Montway and Sherpa and depends on backlinks and
  reviews more than on-page content.
- Add real customer reviews to the page when you have Miami-specific ones, then
  (and only then) add `AggregateRating` schema. Never mark up reviews you
  haven't collected.

---

## Using this as the template for more city pages

The four blocks below are what make this page rank rather than read as
boilerplate. Each must carry **genuinely city-specific** data, or the page set
trips Google's scaled-content-abuse policy:

1. **Quick-answer box** — city-specific price floor, pickup window, seasonal note
2. **Priced lane table** — real rates for that city's actual top routes
3. **Seasonal cards** — the direction and months that matter *there*
   (Miami's snowbird flow is not Phoenix's, is not Chicago's)
4. **Local callouts** — the operational quirks of that market (ports, HOA/gated
   access, weather windows, dealer districts)

Test for any new city page: swap the city name out and ask how much of the page
would still be true. If the answer is "most of it," the page isn't ready.
