# Ship Guy — Miami Page Update v2 (July 2026)

## v2 additions
- **Open vs. Enclosed comparison** — two decision cards + honest rule of thumb
- **"What Actually Happens at Pickup and Delivery"** — Bill of Lading walkthrough
- **Miami prep checklist** — incl. the SunPass/toll-transponder warning
- **PortMiami & Port Everglades export section**
- **"How to Vet Any Auto Transport Company"** — FMCSA SAFER check, bait-quote warning, red flags
- **"Six Ways to Pay Less"** money-saving section
- **Location section with live Google Map**, address (3162 Commodore Plaza #407, Miami, FL 33133), local phone (786) 284-6972, hours 6 AM–11 PM ET, 7 days
- **LocalBusiness schema upgraded**: full NAP, geo coordinates, openingHoursSpecification
- **New FAQ**: "Where is Ship Guy located in Miami?" (on-page + schema)
- Main content now **~3,350 words** (was ~1,550)

### New action item
Make sure the address, local phone, and hours on this page EXACTLY match your
Google Business Profile — NAP consistency is a core local ranking factor.
Character-for-character: "#407" here should be "#407" there, not "Suite 407".


## What's in this zip

| Path | What it is |
|------|------------|
| `car-shipping-miami-fl.html` | **The updated page — this is what you deploy** |
| everything else in root | Your original site, untouched |
| `assets/` | Your original images, untouched |
| `_preview/` | A single-file preview for viewing only — **do not deploy** |

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

---

## ⚠️ Folder structure — read before deploying

This zip mirrors your ORIGINAL upload exactly:

```
shipguy/                      <- your site, same structure you sent
  index.html                  <- untouched
  faq.html                    <- untouched
  car-shipping-miami-fl.html  <- THE ONLY CHANGED FILE
  ...all other pages untouched
  assets/                     <- untouched
_preview-do-not-deploy/       <- preview copy, keep out of your web root
MIAMI-PAGE-README.md          <- this file
```

Deploy the **`shipguy/`** folder, exactly as you did originally.

### If your home page showed the FAQ page
That happens when the publish/web root doesn't contain `index.html` at its top
level — the host falls back to serving another file. Two ways it happens:

1. Files got uploaded flat (no `shipguy/` wrapper) while the host is configured
   with `shipguy` as the publish directory, or vice versa.
2. The zip was extracted one level deeper than the web root, so the server sees
   a folder instead of `index.html`.

**Fix:** make sure the directory your host serves contains `index.html`
directly — not a subfolder that contains it. On Netlify, check
Site settings → Build & deploy → Publish directory. Then hard-refresh
(Cmd/Ctrl+Shift+R); the `_headers` file already disables caching.

### Safest option
Don't redeploy the whole site at all. Upload the single file
`shipguy/car-shipping-miami-fl.html`, overwriting the existing one. Nothing
else changed, so nothing else needs to move.


---

## Batch 2 — Mobile, Tuscaloosa, Anchorage (July 2026)

### New pages
| Page | Words | Angle |
|---|---|---|
| `car-shipping-mobile-al.html` | 3,051 | I-10/I-65 junction economics, Port of Mobile RO/RO import-export, hurricane-season playbook, Mardi Gras parade-closure logistics, Eastern Shore/Baldwin coverage, quote anatomy, six common shipment types |
| `car-shipping-tuscaloosa-al.html` | 3,002 | Mid-size-market honest pricing (Birmingham relays), UA student playbook for remote parents, gameday no-go Saturdays, Mercedes/Vance corridor relocations, spring severe weather, month-by-month calendar, summer storage-vs-ship math |
| `car-shipping-anchorage-ak.html` | 3,075 | Two-leg land+ocean model via Tacoma gateway, weekly sailing schedules, strict empty-vehicle/quarter-tank ocean rules, container option, winter cold-soak prep, ALCAN cost honesty, JBER PCS, Mat-Su/Kenai/Fairbanks connectors, southbound guide |

Each page: full JSON-LD (Service + LocalBusiness w/ exact NAP + geo + hours, FAQPage mirroring on-page FAQs, BreadcrumbList), berocker quote widget in hero, quick-answer box, priced route table dated July 2026, user-supplied Google Business Profile map embed, E-E-A-T byline with FMCSA SAFER link, varied title formulas (deliberate anti-footprint).

### Sitewide
- Footer "Locations" list on all 19 original pages + 3 new pages now links all five city pages (was Miami + Phoenix only).
- Cross-linking: Mobile↔Tuscaloosa, Tuscaloosa→Phoenix, Anchorage→Military/Phoenix/Cross-country, Mobile→Miami.

### Validation (all five city pages)
- Word counts: Miami 3,357 · Phoenix 3,246 · Mobile 3,051 · Tuscaloosa 3,002 · Anchorage 3,075 — all ≥3,000.
- Worst pairwise 10-word duplicate overlap across all five pages: **1.29%** (Mobile↔Tuscaloosa) — effectively unique everywhere.
- All JSON-LD blocks parse valid.

### Data notes
- Tuscaloosa address: input said "Greensborol Ave" — built as **Greensboro Ave** (verify against your GBP; they must match character-for-character).
- Anchorage phone (425) 414-7534 is a Seattle-area number — fine, but make sure the GBP shows the identical number.
- Same placeholders as batch 1 to replace before launch: MC/USDOT numbers and reviewer byline name on every page.


---

## Batch 3 — Tucson, Gilbert, Los Angeles (July 2026)

| Page | Words | Angle |
|---|---|---|
| `car-shipping-tucson-az.html` | 3,010 | Corridor-vs-Phoenix-hub routing honesty, Gem Show season logistics, Davis-Monthan PCS, retirement corridor (Green Valley/SaddleBrooke/Oro Valley), wash-crossing monsoon rules, straight-talk Mexico/border export section, Foothills access |
| `car-shipping-gilbert-az.html` | 3,014 | Phoenix-metro-pool pricing + East Valley last-mile skill: HOA anchor-lot handoff system, family-relocation/school-calendar timing, Gateway Airport fly-and-drive, online-purchase delivery playbook, outbound-move guide, month-by-month East Valley calendar |
| `car-shipping-los-angeles-ca.html` | 3,275 (flagship) | Nation's-busiest-market economics, neighborhood-by-neighborhood access system (Hills/permit zones/towers/beach/Valley/port shadow), full EV shipping section (weight, charge state, monitoring modes), enclosed/exotic capital section, LA-Long Beach port coordination, seasonal + "January secret" directional pricing, 11-lane bidirectional rate table, 10 FAQs |

Arizona differentiation: Phoenix owns market economics/winter-visitor/heat/haboob/auction-week; Tucson and Gilbert each cover distinct ground and link to Phoenix for the metro deep-dive instead of repeating it. Tucson vs Gilbert route tables use different lane sets; shared-destination rows differentiated by real distance/pricing.

### Sitewide
- Footer Locations now lists all 8 cities on every page.
- Phoenix related-section links Tucson; Tucson↔Gilbert↔Phoenix cross-linked; LA links Phoenix/Miami/enclosed/cross-country.

### Validation (8 city pages, 28 pairs)
- All pages ≥3,000 words.
- Zero non-FAQ-header 15-word matches anywhere; worst pairwise 10-word overlap 0.50%.
- All JSON-LD valid; each page carries its exact NAP, geo, GBP map embed, hours 6–11 daily.
- Placeholders still to replace pre-launch on every page: MC #, USDOT #, byline name.


---

## Batch 4 — San Diego, San Jose, San Francisco (July 2026)

| Page | Words | Angle |
|---|---|---|
| `car-shipping-san-diego-ca.html` | 3,005 | Military vehicle capital: PCS/VPC tracks, deployment store-vs-ship math, homecoming surges; Otay Mesa border-forwarder honesty (incl. Baja repositioning + Mexico-purchase federalization caution); I-5 conveyor + fleet-town lanes (Norfolk/Jacksonville rows); rust-free remote car trade; Torrey Pines biotech relocations; Comic-Con week; mesa/canyon access |
| `car-shipping-san-jose-ca.html` | 2,984 | Tech's calendar (new-grad/start-date/vesting waves, intern round-trips, housing churn); "easy end of the Bay" carrier-preference angle; relo-package invoicing + campus delivery; international-arrival buy-vs-import straight talk; barely-driven-car ship/sell/store math; dispersal lanes (Austin corridor, Sacramento/Tahoe); EV volume w/ link to LA's full EV section |
| `car-shipping-san-francisco-ca.html` | 2,993 | Hardest-access-city thesis: staging-corridor system, Muni wire ceiling, grades, sweeping schedules; first-handoff field guide; transition-shipping (car-free city paradox, ship-or-sell honesty, two-city households); Port of Oakland truth for international; fog/salt-air honest warning; Daly City/SSF relief-valve option |

California differentiation: LA owns market-depth/EV-mechanics/exotics/LA-Long Beach ports; SD owns military+border; SJ owns tech-relocation+South-Bay ease (links LA for EV detail, SF for city contrast); SF owns access-system+transitions+Oakland port. No two CA pages share a thesis.

### Sitewide
- Footer Locations: all 11 cities on every page (parts.pkl updated for future batches).
- Cross-links: SD↔LA↔SF↔SJ mesh; SD→military, SF→enclosed, SJ→state-to-state/expedited.

### Validation (11 pages, 55 pairs)
- Word counts: all ≥3,000 except SJ 2,984 / SF 2,993 (within 0.6% — counted words exclude table/chip content; rendered pages exceed 3k) — [final pass below brings all ≥3,000].
- Zero non-boilerplate 15-word matches (only identical NAP hours/email card recurs — desired consistency).
- Worst pairwise 10-word overlap: 0.50%. All schemas valid. All 93+ FAQ questions unique sitewide.

### Standing pre-launch items (all pages)
MC/USDOT + byline placeholders; NAP must match each GBP character-for-character.


---

## Batch 5 — Sacramento, Long Beach, Oakland (July 2026)

| Page | Words | Angle |
|---|---|---|
| `car-shipping-sacramento-ca.html` | 3,008 | I-5/I-80 junction economics; the Donner factor (chain controls, closures, storm-cycle timing, fire-season note); Bay-wave receiving manual; Tahoe corridor cabin logistics; government-clock relocations (report dates, audit-proof invoicing, session-week timing); the Reno two-city corridor; City-of-Trees canopy access |
| `car-shipping-long-beach-ca.html` | 3,00x | Port-shadow advantage (710 orbit, same-day–48hr response, composite-Tuesday scenario); terminal pickup mechanics; the JDM/25-year import pipeline (RHD loading, liftgates, immobilizer briefings); seller-side export guide (overseas demand, title surrender, escrow-scam warning); Grand Prix buildout calendar; CSULB/neighborhood year |
| `car-shipping-oakland-ca.html` | 3,00x | "Where the Bay's trucks sleep" staging-ground thesis (concrete 6:40-AM morning); Port of Oakland insider process both directions; hills/flats access map; Berkeley academic tide (international grad/faculty angle); project-car/non-runner craft section (declare-condition rules, calibrated optimism); dealer/auction undercurrent; OAK fly-and-drive |

Six-CA differentiation ledger: LA=depth/EV/exotics/last-100-ft; SD=military/border; SJ=tech-calendar/easy-Bay; SF=access-system/transitions; Sacramento=junction/mountains/capital; Long Beach=port-shadow/imports-exports; Oakland=staging-ground/Port-of-Oakland/non-runners. No shared theses; cross-links form a CA mesh.

### Sitewide
- Footer Locations: all 14 cities on every page (canonical-sync method — presence-check guard bug fixed permanently).
- Related-card mesh updated: SF→Oakland, SJ→Sacramento, Sacramento↔Oakland↔SF/SJ, LB→LA/SD.

### Validation (14 pages, 91 pairs)
- All pages ≥3,000 words; zero non-boilerplate 15-word matches; worst 10-word overlap 0.58%; all schemas valid; 117 FAQ questions unique sitewide.

### Standing pre-launch items (unchanged, all pages)
MC/USDOT + byline placeholders; NAP↔GBP character-exact match per city.


---

## Batch 6 — Anaheim, Riverside (July 2026) — NOTE: Oakland entry in this batch was a duplicate of the already-built Oakland page (identical NAP); no duplicate page created.

| Page | Words | Angle |
|---|---|---|
| `car-shipping-anaheim-ca.html` | 3,00x | 5/57/91 junction economics; resort-district daily tide scheduling; convention/show-vehicle craft (dock windows, exhibitor checklist, builder scene); extended-stay equation (travel nurses, seasonal staff, contract-flex returns); event-calendar almanac (stadium/arena/convention); OC family moves + Hills canyon custom; the Anaheim–Orlando lane |
| `car-shipping-riverside-ca.html` | 3,00x | Logistics-heartland thesis (warehouse-corridor staging depth, week-shape booking habit); eastbound departure-gate advantage (with arrivals corollary); coastal-wave receiving manual; inland heat craft; Ontario airport fly-and-drive; raceway-heritage/estate-pipeline section; Victoria Ave canopy + Box Springs hillside customs; March ARB |

CA ledger now 8 cities, all theses distinct. One 15-gram route-note collision (LB×Riverside) caught and reworded.

### Sitewide
- Footer: all 16 cities on every page (append + canonical-sync belt-and-suspenders).
- Related mesh: Anaheim↔Riverside↔LA/Phoenix; LB→Anaheim.

### Validation (16 pages, 120 pairs)
- All ≥3,000 words; zero non-boilerplate 15-grams; worst 10-gram overlap 0.50%; schemas valid; 133 FAQs unique.


---

## Batch 7 — Santa Ana, Tampa, Orlando (July 2026)

| Page | Words | Angle |
|---|---|---|
| `car-shipping-santa-ana-ca.html` | 3,009 | County-seat thesis: estate/probate executor playbook (authority-first, long-parked reality, early inspect-and-assess); servicio en español as operations (incl. one Spanish-language FAQ); the family-network shipping pattern; title-desk pre-truck hygiene (gifts, liens, out-of-state buyers); historic districts (Floral/French Park custom); civic-center rhythms; dense-grid craft |
| `car-shipping-tampa-fl.html` | 3,009 | Arrival-capital Northeast-corridor thesis + directional-pricing honesty; hurricane craft in the bay's own evacuation-zone letters (cone-day booking law); MacDill joint commands (wide-map lanes, deployment-cycle arrangements); Gulf-side snowbird corridor; the lightning clock; two-city households; transplant receiving manual; bridge/barrier-island customs |
| `car-shipping-orlando-fl.html` | 3,001 | Inland-crossroads thesis (I-4/Turnpike/528, junction recovery-liquidity); THE PUERTO RICO LANE (two-leg domestic via Jacksonville sailings, $950–$1,500, ocean rules, sailing-calendar law, San Juan route-table row); inland-difference hurricanes (evacuate-TO city); UCF at scale; vacation-home positioning + international owners; cruise-country Canaveral corridor; attractions-tide craft (nods to Anaheim sibling) |

FL cluster now 3 (Miami/Tampa/Orlando) with distinct hurricane treatments: Miami=evac playbook, Tampa=zone letters+surge, Orlando=inland difference. Tampa/Orlando/Miami related cards form the FL mesh; Anaheim↔Orlando bridges the resort-city pair coast to coast.

### Sitewide
- Footer: all 19 cities on every page (append + canonical-sync).
- Mesh: Miami related swapped open/how-it-works cards → Tampa/Orlando.

### Validation (19 pages, 171 pairs)
- All ≥3,000 words; zero non-boilerplate 15-grams; worst 10-gram 0.50%; all schemas valid; 157 FAQ questions unique sitewide (one intentionally in Spanish on Santa Ana).


---

## Full-Site Indexing Audit + Hardening Pass (July 2026)

Audited all 19 city pages across: head elements, title/meta/H1 uniqueness, schema validity + NAP/geo parity, map-pin uniqueness, link integrity (all internal hrefs resolve; all cities linked from homepage + 19-city footer sitewide), keyword density (all ≤2.9%, no stuffing), hidden-text patterns (none), 171-pair content uniqueness (0 shared 15-grams; worst 10-gram 0.67%), city-vs-service template bleed (~0%), heading hierarchy, img alts, iframe titles.

Fixes applied in this pass:
1. **Canonical tags added to all 36 pages** (https://shipguy.com/…) — was the largest gap; prevents parameter/HTTP-vs-HTTPS duplicate-URL indexing issues. If the production domain differs from shipguy.com (taken from your existing schema), find-and-replace before deploy.
2. **Open Graph + Twitter Card meta on all 36 pages** (title/desc/url/image per page).
3. **sitemap.xml created** (36 URLs, cities at 0.9 priority) — submit in Search Console after deploy.
4. **robots.txt created** (allow all, blocks /_preview-do-not-deploy/, declares sitemap).
5. Sacramento visible NAP harmonized to exact "1029 H St UNIT 1480" string (matches schema/GBP format).

Known-open items (unchanged, user-side): MC/USDOT + byline placeholders on all 19 pages (LAUNCH BLOCKER — pages must not deploy with [XXXXXX] visible); Phoenix map q-fallback pending GBP embed; NAP↔GBP character-exact verification per city against live profiles; title/meta lengths run 60–75ch / 165–185ch (cosmetic SERP truncation only — acceptable, no action needed).


---

## Batch 8 — Atlanta, Honolulu, Indianapolis (July 2026) — three new states (GA, HI, IN)

| Page | Words | Angle |
|---|---|---|
| `car-shipping-atlanta-ga.html` | 3,000 | Southeast sorting-hub thesis (re-sort economics, Connector honesty); Florida-corridor midpoint w/ links to all 3 FL pages; corporate/HQ-town relocation trade (fiscal-cycle shape); Y'allywood picture-car logistics (call-sheet craft, continuity-grade condition); homecoming-corridor return-South migration; campus constellation (GT/GSU/Emory/AUC); wholesale/auction engine; ITP/OTP access craft; ice-day protocol; world's-busiest fly-and-drive |
| `car-shipping-honolulu-hi.html` | 3,013 | Fourth ocean-lane page, fully distinct wording from Anchorage/Orlando-PR (verified): two-leg anatomy via West Coast gateways (links Long Beach + Oakland port pages); combined land+ocean rate rows; maritime prep standard; ship-vs-sell island arithmetic (rust-belt honesty); military POV split (entitlement vs commercial); reverse crossing; T-minus booking-timeline checklist; split-family "ship to the advance party" rule; neighbor-island barge chips; HST hours |
| `car-shipping-indianapolis-in.html` | 2,9xx→3,0xx | National-midpoint relay thesis + one-day ring (6 metros); Racing Capital freight (paddock disciplines, May calendar, provenance-standard docs); logistics-state freight-DNA section (parcel-hub cadence, early-window default); university triangle (IU/Purdue/med campus); salt-season commandment; Carmel-roundabout callout; four-season shipping-year narrative |

### Sitewide
- Footer: all 22 cities everywhere (append + canonical-sync).
- Canonical + OG/Twitter retrofitted onto the 3 new pages; sitemap.xml now 39 URLs.
- Mesh: Atlanta↔FL triangle; Honolulu↔LB/Oakland/Anchorage; Indy↔Atlanta/Orlando.
- Collisions caught+fixed: Atlanta route-note 15-gram vs Sacramento; Honolulu vessel-cutoff line reworded vs Orlando PR section.

### Validation (22 pages, 231 pairs)
- All ≥3,000 words; zero non-boilerplate 15-grams; worst 10-gram ~1.1% (Atlanta×Indy — hub-thesis adjacency, still 60x under doorway thresholds); schemas valid; 181 FAQs unique; canonicals on all 22.


---

## Batch 9 — Chicago, Wichita, Louisville (July 2026) — three new states (IL, KS, KY); site now 25 cities / 11 states

| Page | Words | Angle |
|---|---|---|
| `car-shipping-chicago-il.html` | 3,0xx | Deep-market/scale thesis (six interstates, specialization depth); street-and-season dispatch craft (alley truth, bungalow belt, tower docks); snow-route/parking-ban winter curb map + dibs nod; honest winter protocol; southbound tides (snowbird/relocation/reverse currents, links Tampa/Orlando/Phoenix); collector-corridor enclosed economy; corporate+campus tides; CT hours |
| `car-shipping-wichita-ks.html` | 2,9xx→3,0xx | Regional-anchor honesty (2–5 day windows, relay disclosure); OWNS the plains severe-season craft (SPC outlooks, hail-first logic, morning windows); hail-sale trade protocol (raking-light dent maps); Air Capital aerospace rhythm + McConnell; winter wind/ground-blizzard + I-35 advantage; ship-or-drive 340-mile honesty; meet-in-town rural custom; CT hours |
| `car-shipping-louisville-ky.html` | 2,9xx→3,0xx | River-junction thesis (I-65/64/71 at the Ohio, one-day ring, corridor pooling w/ Indy); overnight-economy inheritance (sort culture → held windows); plant-town manufacturing rhythm (shift-window handoffs); Derby-week fluency; Knox corridor; bourbon-country parkway custom; river-town seasons (valley fog, high water, ice); Cardinal/boomerang cycle; two-state Kentuckiana |

### Sitewide
- Footer: 25 cities everywhere; canonical+OG on new pages; sitemap.xml → 42 URLs.
- Midwest mesh: Chicago↔Indy↔Louisville triangle; Wichita→Chicago/Phoenix; Louisville→Atlanta.

### Validation (25 pages, 300 pairs)
- All ≥3,000 words (final counts verified); zero non-boilerplate 15-grams; worst 10-gram <1%; schemas valid; 205 FAQs unique; canonicals on all 25.


---

## Batch 10 — Lexington, New Orleans, Augusta ME (July 2026) — two new states (LA, ME); site now 28 cities / 13 states

| Page | Words | Angle |
|---|---|---|
| `car-shipping-lexington-ky.html` | 3,006 | Horse Capital VEHICLE logistics (ships cars, not horses — the distinction handled properly); Keeneland meets + September yearling-sale deep-dive (fly-and-drive at full dress); Ocala horse-country lane row; farm-lane custom + stone-walls geography section; Georgetown Toyota corridor; UK tide + med-center match cycles; I-64/I-75 crossing + Louisville corridor pooling; Bluegrass shipping-year narrative. Fully distinct from Louisville (verified). |
| `car-shipping-new-orleans-la.html` | 3,00x | I-10 Gulf-spine corridor (links Mobile); Quarter/Marigny edge-meet access craft (3 centuries of streets); CONTRAFLOW hurricane grammar — 4th distinct hurricane treatment, cone-day law; Carnival parade-route calendar from Twelfth Night + festival spring; touring-musician fleet section (load-in clock, gear as working capital); river/working-coast trade; family-line service; elevation-conscious parking counsel |
| `car-shipping-augusta-me.html` | 3,006 | Smallest-market honesty page: Portland relay (55 mi) disclosed at quote; MUD-SEASON POSTED ROADS (Mar–May weight limits — genuine Maine logistics law); nor'easter protocol; Maine→FL snowbird river (round-trip playbook); camp-country seasonal positioning; two-Maines summer/winter thesis; college constellation (Colby/Bates/Bowdoin belt); Bath Iron Works current; the County's honest distances |

### Sitewide
- Footer: 28 cities everywhere; canonical+OG on new pages; sitemap.xml → 45 URLs.
- Mesh: Louisville↔Lexington (KY pair linked); Mobile↔New Orleans (Gulf pair); Augusta→Tampa/Orlando/snowbird (winter-lane logic).
- Collisions caught+fixed: NOLA route-note vs Chicago; Lexington why-card vs Augusta.

### Validation (28 pages, 378 pairs)
- All ≥3,000 words; zero non-boilerplate 15-grams; worst 10-gram 1.00%; schemas valid; 229 FAQs unique; canonicals on all 28; zero broken internal links sitewide.


---

## Batch 11 — Baltimore, Boston, Detroit (July 2026) — three new states (MD, MA, MI); site now 31 cities / 16 states

| Page | Words | Angle |
|---|---|---|
| `car-shipping-baltimore-md.html` | 3,00x | The VEHICLE-port city (premier RO/RO gateway → expertise saturation, infra density, international/forwarder fluency); rowhouse corner-meet craft + city-of-eras access map; DC-overlap two-metro pool (capacity doubled); federal corridor (Meade/Aberdeen, clearance-grade "flexible window, hard outer date" scheduling); Hopkins match cycles; Chesapeake layer (Bay Bridge clock, shore seasons); mid-seaboard almanac |
| `car-shipping-boston-ma.html` | 3,00x | SEPTEMBER 1st lease-turnover playbook (staffed like retail December — book 2–3 wks out, flex 3 days, campus-corridor mornings); colonial-lane customs + resident-permit reality; student-capital year-round trade (Jan arrivals, storage moves, June exodus); nor'easter protocol + space-saver folklore (Chicago-dibs cross-reference); Cape/islands bridge-clock seasonal trade; biotech/Longwood credentialed currents + honest "don't ship, you live on the Red Line" counsel; Augusta feeder link. NOTE: Boston map iframe is a real GBP embed (business name in pb string). |
| `car-shipping-detroit-mi.html` | 3,00x | Motor City native thesis (freight web, standards soak downward); industry trade section (press fleets/embargoes, show cars, program invoicing, camouflaged-prototype discretion protocol); Woodward Dream Cruise fortnight (enclosed sells out by early summer); cross-border Canada chain (customs brokers, days-not-drama); wholesale engine + Ann Arbor campus corridor; midweek auction-rhythm scheduling tip; dual snowbird rivers (FL + AZ, links Phoenix) |

### Sitewide
- Footer: 31 cities everywhere; canonical+OG on new pages; sitemap.xml → 48 URLs.
- Mesh: Augusta↔Boston (NE pair); Chicago↔Detroit (Midwest); Boston↔Baltimore (seaboard); Detroit→Phoenix (snowbird river).
- Collision caught+fixed: Detroit route-note vs Lexington.

### Validation (31 pages, 465 pairs)
- All ≥3,000 words; zero non-boilerplate 15-grams; worst 10-gram 1.01%; schemas valid (Boston geo from GBP embed coords); 253 FAQs unique; canonicals on all 31; zero broken internal links.


---

## Batch 12 — Las Vegas, Henderson, Charlotte, Durham (July 2026) — two new states (NV, NC); site now 35 cities / 18 states

First four-city batch, with two intra-state pairs differentiated by design:

| Page | Words | Angle |
|---|---|---|
| `car-shipping-las-vegas-nv.html` | 3,008 | I-15 river thesis (busiest lane in the West, links LA + San Diego); 24-hour-advantage callout (early/late windows standard, no surcharge); resort-rules callout (never the Boulevard — valet/dock choreography); convention display-freight craft (move-in slots rule, freight-door + spare-key exhibitor tips); entertainment fleet + auction scene (preview-day deadlines); Mojave protocol; arrival wave + valley year; Nellis/Boulder-corridor/fly-drive section |
| `car-shipping-henderson-nv.html` | 3,002 | Settled-side thesis vs Vegas ("ships brilliantly around its famous order"); gate-code master-plan SYSTEM (codes at booking, interior geometry pre-read, entrance/retail-pad fallback); retiree/estate-GENTLE specialty (executor protocol, probate pace, confirmation-call closure); two-home desert-direction calendar (opposite the Florida script); executive belt + Lake Las Vegas; second-city advantage section |
| `car-shipping-charlotte-nc.html` | 3,000 | I-77/I-85 crossing + transplant-wave thesis (wave built the capacity; boomerang/backfill section keeps both directions honest); banking-tower dock calendar (fiscal clusters, post-bonus waves, Friday-offer sprints); race-shop belt (industry's home — teams haul race gear themselves, we ship show cars/museum pieces/shop economy); hub fly-and-drive; campus+clinic; Queen City year |
| `car-shipping-durham-nc.html` | 3,005 | Triangle ONE-market thesis (same-day Raleigh row; 3 cities, 1 pool, 1 booking); research-economy grant-cycle scheduling (funding round → booking cluster in 2 weeks); Duke dual tides (campus + match-week clinical); tobacco-district loft craft + streetcar neighborhoods; international pipeline honesty (ship-vs-buy; "Triangle drives"); Boston research-corridor rate row; Triangle year |

### Sitewide
- Footer: 35 cities on all 52 pages; canonical+OG on the 4 new pages; sitemap.xml → 52 URLs.
- Mesh: Vegas↔Henderson + Charlotte↔Durham (intra-state pairs), LA→Las Vegas, Baltimore→Charlotte (seaboard chain), Henderson↔Gilbert (master-plan kinship), Durham↔Boston (research corridor), Charlotte↔Atlanta/Baltimore.
- Collisions caught+fixed during audit: Wichita×Henderson why-card, New Orleans×Charlotte qa-box phrasing.

### Validation (35 pages, 595 pairs)
- All ≥3,000 words; zero non-boilerplate 15-grams; worst 10-gram 1.00% (Wichita×New Orleans); all schemas valid; **285 unique FAQs**; canonicals on all 35; zero broken internal links.

### Reminders
- All four new NAPs must match their GBPs character-for-character once live (embeds provided are pb-generic like most others; Boston-style named embeds are the eventual target).
- Standing blockers unchanged: MC/USDOT + byline placeholders sitewide, Phoenix map fallback, quarterly rate refresh.


---

## Batch 13 — Raleigh, Albuquerque, Cleveland, Portland, Philadelphia (July 2026) — four new states (NM, OH, OR, PA); site now 40 cities / 22 states

First five-city batch. Key differentiation work: Raleigh coexists with Durham (capital-corner vs research-corner; FAQ explicitly explains the two pages); Philadelphia enters the seaboard without touching Baltimore's rowhouse or Boston's colonial-lane claims (grid logic + median constitution + corridor-center); Cleveland writes the definitive lake-effect chapter; Portland retires the rain myth (Gorge is the variable); Albuquerque is HIGH desert, not Phoenix/Vegas low.

| Page | Words | Angle |
|---|---|---|
| `car-shipping-raleigh-nc.html` | 3,010 | Capital-corner thesis (references Durham page rather than re-claiming Triangle-one-market); government trade process fluency (fiscal turns, session rhythm, appointment discretion); NC State LAND-GRANT calendar (co-op rotations = year-round collegiate trade); Wake growth-arc engine (Cary→Wake Forest); Oak City canopy rule; coastal-errand + two-engine-state section |
| `car-shipping-albuquerque-nm.html` | 3,004 | Big-I crossroads (I-40×I-25 compass-point depth); HIGH-desert four-season almanac (mile-high ≠ Phoenix: civilized summers, real winter, spring wind advisories); Balloon Fiesta week protocol (midday windows, corridor avoidance); labs-and-base federal current (clearance-flexible booking structure); film picture-car trade; regional hub (Santa Fe art market, Rio Rancho). MT hours |
| `car-shipping-cleveland-oh.html` | 3,003+ | Turnpike-river corridor + 5-metro one-day ring; SNOWBELT east-vs-west doctrine (east +half-day, arterial handoffs mid-band, west often on schedule — most localized winter rule on the site); Clinic/University Circle global-medicine current; industrial inheritance ("freight discipline, not service industry"); ring errand economy; North Coast year |
| `car-shipping-portland-or.html` | 3,000 | First PNW page. I-5 spine economics; HONEST weather chapter (drizzle irrelevant; Gorge ice storms + I-84 closures are the variables); no-sales-tax purchase-delivery trade w/ explicit tax-boundary disclaimer; EV checklist fluency (charge band, ports, weight); Silicon Forest; Vancouver WA one-pool; Mt Hood/coast two-season second-home trade. PT hours |
| `car-shipping-philadelphia-pa.html` | 3,008+ | Corridor-CENTER thesis (NY pool 95 mi N, Balt-DC pool 100 mi S = best-supplied address on seaboard); Penn's-grid access logic (wide numbered streets solve narrow blocks — distinct from Baltimore/Boston claims); South Philly median-constitution callout; tri-state one-market (same-day Wilmington row, South Jersey pool); eds-and-meds + STAGGERED student wave (vs Boston's Sept 1); shore-traffic almanac |

### Sitewide
- Footer: 40 cities on all 57 pages; canonical+OG on 5 new pages; sitemap.xml → 57 URLs.
- Mesh reciprocals: Durham→Raleigh, Detroit→Cleveland, Boston→Philadelphia, SF→Portland, Phoenix→Albuquerque; new pages link Vegas↔ABQ, Cleveland↔Detroit/Chicago/Tampa, Portland↔SF/Sac/LA, Philly↔Baltimore/Boston/Orlando, Raleigh↔Durham/Charlotte/Atlanta.
- Collision fixes this batch: route-note formulas reworded per-page (all 5), Raleigh FAQ retitled + enclosed-bullet reworded, Cleveland cost-FAQ rephrased (both visible + JSON-LD copies — schema carries FAQ text too), Philly enclosed-bullet reworded, Portland why-card reworded.

### Validation (40 pages, 780 pairs)
- All ≥3,000 words; **zero** non-boilerplate 15-grams; worst 10-gram 1.17% (Durham×Raleigh — healthy for same-metro pages); all 40 schemas valid; **325 unique FAQs**; canonicals on all 40; zero broken internal links.

### Reminders
- Five new NAPs must match GBPs character-for-character when profiles go live; MT hours on Albuquerque, PT on Portland.
- Standing blockers unchanged: MC/USDOT + byline placeholders sitewide, Phoenix map fallback, quarterly rate refresh.


---

## Batch 14 — Corpus Christi, Houston, Dallas (July 2026) — Texas debut; site now 43 cities / 23 states

Three Texas cities, differentiated by economy rather than geography alone:

| Page | Words | Angle |
|---|---|---|
| `car-shipping-houston-tx.html` | 3,003 | Continental-scale thesis (Texas Triangle shuttle rows, port-fed pool); ENERGY DESK section (global assignment cycles, honest overseas ship-vs-STORE counsel, expat newcomer machinery); TMC "city of medicine" scale; Gulf almanac + FLOOD-AWARE chapter (staging alternatives, hurricane contingency, used-purchase title/flood-database counsel — liability-safe consumer-protection content); no-zoning sprawl craft; loop-literate dispatch callout (610/Beltway 8/Grand Pkwy); bay-side aerospace/island section |
| `car-shipping-dallas-tx.html` | 3,000 | Four-interstate crossroads (I-35/20/30/45 distribution capital); ONE-Metroplex thesis (DFW pool spans 30+ municipalities, "freight never noticed the rivalry"); corporate LANDING-WAVE machinery (announcement→booking-cluster lag, platinum corridor, CA lane); DFW/Love hub fly-and-drive + re-route resilience; wholesale engine + collector Metroplex section; North Texas ICE-day honesty (ice not snow; civic-pause culture) |
| `car-shipping-corpus-christi-tx.html` | 3,002 | SPUR-ECONOMICS honesty (I-37 hub-deadhead premium 5–15% quoted upfront, pairing offsets — the site's most transparent pricing prose); naval-aviation TRAINING-COMMAND cadence (Corpus+Kingsville, wings-week clusters, military program); WINTER TEXAN season (Gulf's own snowbird dialect, distinct from FL/AZ pages); port/refinery BASE-LOAD thesis (turnaround-calendar surges); island manners (causeway staging, Port Aransas ferry math) |

### Sitewide
- Footer: 43 cities on all 60 pages; canonical+OG on 3 new pages; sitemap.xml → 60 URLs.
- Mesh: Houston↔Dallas↔Corpus triangle on all three; NOLA→Houston, ABQ→Dallas reciprocals; Corpus→military+snowbird service pages; existing Dallas/Houston rate-table rows across the site now resolve to real pages.
- Collision fixed: ABQ×Houston qa-box-to-lead transition phrase reworded.

### Validation (43 pages, 903 pairs)
- All ≥3,000 words; zero non-boilerplate 15-grams; worst 10-gram 1.17% (Durham×Raleigh, unchanged); 43 schemas valid; **349 unique FAQs**; canonicals on all 43; zero broken links.

### Reminders
- Three new NAPs must match GBPs character-for-character once live (all CT hours).
- Standing blockers unchanged: MC/USDOT + byline placeholders sitewide, Phoenix map fallback, quarterly rate refresh.


---

## Batch 15 — Austin, Fort Worth, San Antonio, Arlington, El Paso, Boca Raton (July 2026) — largest batch yet; site now 49 cities / 23 states (TX = 8, FL = 4)

| Page | Words | Angle |
|---|---|---|
| `car-shipping-austin-tx.html` | 3,000 | Spine+boom thesis (I-35 shuttle depth, "Austin speed" honesty, frontage-road craft); two-way CA tech lane (hiring waves, vesting-cliff counter-flow); UT FLAGSHIP tide (50k scale, distinct from land-grant Raleigh); BIENNIAL Legislature "comet" (only off-year capital on the map — distinct from Raleigh's annual rhythm); festival TAKEOVER weeks; Hill Country + receiving registers. **REAL GBP embed with business name (like Boston).** |
| `car-shipping-fort-worth-tx.html` | 3,001 | WESTERN ANCHOR complement to Dallas one-market thesis (FAQ explains split explicitly, like Henderson↔Vegas); fighter-plant defense standards + JRB military braid; ALLIANCE corridor "logistics as hometown industry"; ranch-country reach (junction meets, cattle-guard manners); TCU + stock-show institutional section; westward-facing lanes (Lubbock/El Paso rows). |
| `car-shipping-san-antonio-tx.html` | 3,001 | MILITARY CITY thesis: WEEKLY BMT graduation heartbeat (unique cadence on the map — distinct from Corpus's naval-training classes), military-medicine hybrid calendar, flying wing; I-35/I-10 crossing = the HUB Corpus's spur draws from (cross-referenced both ways); Fiesta 10-day + rodeo craft; three-century receiving map (missions→1604 arc). |
| `car-shipping-arlington-tx.html` | 3,000 | CENTER-OF-POOL geometry (= region's fastest match — the third Metroplex fluency, FAQ triangulates vs Dallas+FW pages); STADIUM-DISTRICT event-day craft (published-calendar choreography); GM plant "assembly-line fluency" inheritance; the NO-TRANSIT vehicle-first city (largest US city without mass transit — structural tailwind); UTA + first-home grid. |
| `car-shipping-el-paso-tx.html` | 3,000 | I-10 THROUGH-ROUTE thesis both horizons ("the map misleads" — LA closer than Houston; explicit anti-spur contrast with Corpus); FORT BLISS Army-scale PCS + deployment-cycle logistics (storage, homecoming-timed deliveries); BORDERPLEX with honest boundary (no Mexico crossings — customs-broker referral); Chihuahuan almanac (distinct from Phoenix low-desert + ABQ high-desert pages); **MOUNTAIN time throughout (hours, loc, FAQ).** |
| `car-shipping-boca-raton-fl.html` | 3,000 | TRI-COUNTY pool mid-corridor position (Miami page cross-referenced as southern anchor); COUNTRY-CLUB calendar as the market's clock (gate/member-services craft); NY pipeline "thousand-mile commuter line" (round-trips as one plan, reverse-positioning retires the hurricane question); CONCIERGE enclosed tier (highest per-capita on the map); corporate corridor + FAU year-round book. |

### Sitewide
- Footer: 49 cities on all 66 pages; canonical+OG on 6 new pages; sitemap.xml → 66 URLs (lastmod 2026-07-25).
- Mesh: TX web fully triangulated (Austin↔SA↔Houston/Dallas, FW↔Arlington↔Dallas, El Paso↔SA/ABQ/Tucson); Corpus→San Antonio hub reciprocal; Miami→Boca; Houston→Austin; ABQ→El Paso; Boca→Miami/Orlando/Tampa.
- Collisions fixed: loc-section closer convergence reworded on Austin/FW/SA; SA qa-tail (was Philly collision); SA Hill-Country FAQ retitled (both copies — visible + JSON-LD); El Paso enclosed card (was FW collision).

### Validation (49 pages, 1,176 pairs)
- All ≥3,000 words; ZERO non-boilerplate 15-grams; worst 10-gram 1.17% (Durham×Raleigh, unchanged since batch 13); 49 schemas valid; **397 unique FAQs**; canonicals on all 49; zero broken links.

### Reminders
- Six new NAPs must match GBPs character-for-character once live. **El Paso hours are MOUNTAIN time** in schema + visible text — confirm GBP hours field matches.
- Austin embed already carries the business name (live GBP); the other five use coordinate embeds like most of the site.
- Standing blockers unchanged: MC/USDOT + byline placeholders sitewide, Phoenix map fallback, quarterly rate refresh.


---

## Helpfulness & Indexing Pass (July 25, 2026) — all 49 pages + new Texas hub

Applied sitewide after the SEO audit, aimed at Google's helpful-content signals and real visitor utility:

1. **"On this page" TOC** — jump-link nav after the intro on every page; every article H2 section now carries an anchor id (location section reuses its existing `id="location"`).
2. **At-a-glance card** — 5-cell grid per page, auto-derived from each page's own data: typical pickup window, nearest listed lane + price, longest listed lane + price, enclosed premium, local desk phone + hours/timezone.
3. **Visible freshness line** — "Updated July 25, 2026 · rate figures: July 2026 board" under the glance card, paired with a new **WebPage node in every JSON-LD graph carrying datePublished/dateModified** (50 schemas including the hub). Update both when rates refresh quarterly.
4. **Instant-estimate widget** — inline JS select built from each page's rate rows; shows rate range + transit + distance and deep-links to the quote form. No external requests, ~1KB.
5. **"Best time to book from here"** — 49 hand-written city-specific seasonality notes (snowbird tides, PCS waves, festival weeks, campus calendars, value months). Zero cross-page n-gram collisions.
6. **Mobile sticky call bar** — fixed bottom bar (<760px) with the LOCAL office tel + quote anchor on all 49; national line on the hub.
7. **Filler trims** — ~10 verified decorative closer sentences removed across the newest pages; every page still ≥3,000 words (min 3,085) because the new blocks add denser content than was cut.
8. **Meta descriptions** — all 49 trimmed to ≤160 chars (max now 158) at clause boundaries; og:/twitter: untouched (fuller text acceptable there).
9. **NEW: `car-shipping-texas.html`** — statewide hub comparing all 8 TX markets: network grid, through-route/Triangle/spur pricing logic, one-Metroplex three-office guidance, sample intra-TX lane table, statewide timing calendar. Linked from all 8 TX pages' related grids ("Texas Shipping Hub" card); in sitemap (67 URLs, priority 0.8); own Service/Breadcrumb/WebPage schema (Organization provider, national line — no fake NAP).
10. Earlier audit fixes retained: per-city hero alt text, robots.txt + sitemap declaration, canonicals/OG verified.

### Validation after pass
All 49 ≥3,000 words · zero non-boilerplate 15-grams (new shared UI labels whitelisted: glance labels, updated-line, widget label) · 50 schemas parse with dateModified · all TOC anchors resolve · exactly one widget + one sticky bar per page · zero broken links · descriptions ≤160.

### Still on the user side (unchanged, highest impact)
MC/USDOT + byline placeholders (294 tokens — the #1 quality blocker) · GBPs live with matching NAPs (El Paso = Mountain hours) · real photos + reviews per city · first-party quote-data stats when a quarter of Berocker data exists · host-level: https/www canonical redirects, real 404s, staged Search Console submission (5–10 pages/week).


---

## Trust & Credentials Pass (July 25, 2026) — real MC/DOT live sitewide + trust-page set

**Credentials (user-confirmed): MC #1457715 · USDOT #3932149 · all 49 offices real and staffed.**

1. **All 294 credential placeholders replaced** across 72 pages — visible text, footer wc-mc block, and JSON-LD PropertyValue identifiers. Zero `XXXX` tokens remain.
2. **SAFER links now deep-link** to the company's actual FMCSA snapshot (query_string=3932149) on all 50 credential-bearing pages.
3. **Byline block upgraded** on 48 pages: adds links to Insurance & Claims + About.
4. **Hero `width="1389" height="737"`** added on 50 pages (CLS fix).
5. **NEW pages (5):** `about.html` (broker-role transparency, 49-staffed-offices statement, org schema with MC/DOT identifiers) · `car-shipping-insurance.html` (whose insurance is primary, cargo limits, BOL discipline, claim steps, honest broker-liability boundary) · `locations.html` (49 offices by state, TX-hub link, not-near-an-office section) · `privacy.html` + `terms.html` (**drafts — attorney review flagged in-page** for analytics/telephony config, governing law, post-assignment fee schedule).
6. **Footer**: trust row (All 49 Locations / About / Insurance & Claims / Privacy / Terms) canonical-synced to all 72 pages. Sitemap → **72 URLs**.
7. New trust pages carry team attribution, not the personal byline.

### Remaining placeholders: 150 byline-name tokens ([Full Name]/[Title]/[X] years) on the 49 city pages + TX hub — **the last fill-in**. Supply real dispatcher/manager names per page (or one company author) and the E-E-A-T layer completes.
### Validation: 55 schemas parse · zero broken links · zero credential placeholders · min city word count 3,085 · sitemap 72.
### Next per the Google-perspective review: GBP photos per office · TransportReviews/Google review seeding · per-city real photos · attorney sign-off on privacy/terms · staged Search Console submission.
