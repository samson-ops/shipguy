# Ship Guy site — rollout runbook (rebuilt Oct 14, 2026; last batch Oct 16, 2026)

## What happened
The cloud workspace was reset between sessions, so the previous build tree, zips and builder tooling were gone.
The site was restored from the live GitHub repo (`samson-ops/shipguy`, commit a52183b "Add files via upload")
and the page tooling was reconstructed from a finished page plus the builder scripts recovered from the session transcript.

The repo copy was **behind the last zip you received**: it had the CTA button fix and the SMS-consent gate, but
**not the 5-digit ZIP lock** on the pricing tool. The ZIP lock has been re-applied to every tool page in this build.

## Batch 17 — Oklahoma (this delivery)
| City | URL | Phone | Office |
|---|---|---|---|
| Tulsa | /city/auto-transport-tulsa-oklahoma/ | (918) 897-3349 | 1800 S Baltimore Ave Ste 578, Tulsa, OK 74119 |
| Norman | /city/auto-transport-norman-oklahoma/ | (405) 860-4763 | 104 E Main St Ste 498, Norman, OK 73069 |
| Edmond | /city/auto-transport-edmond-oklahoma/ | (405) 780-9279 | 2 E 11th St #522, Edmond, OK 73034 |

Each page: ~1,800–1,900 prose words, broker disclosure in sentence 1–2, all sentences ≤ 18 words, no banned tokens,
FAQPage schema mirroring the on-page FAQ, GTM ×2, one canonical, Google Business Profile map embed on the office card,
nearby-cities block + statewide-guide link, ZIP lock + consent gate on the pricing tool.

Integration done: Oklahoma state page (City Pages block now Edmond / Norman / Oklahoma City / Tulsa + in-section links),
locations hub (Oklahoma block + "Sixty-nine"), nearby chips on Oklahoma City / Wichita / Kansas City / Dallas,
"See all 69 cities" on all 69 city pages, sitemap (137 URLs, lastmod 2026-10-14).

## Batch 18 — New York (same delivery, later the same evening)
| City | URL | Phone | Office |
|---|---|---|---|
| Queens | /city/auto-transport-queens-new-york/ | (929) 560-4543 | 118-35 Queens Blvd #488, Forest Hills, NY 11375 |
| Buffalo | /city/auto-transport-buffalo-new-york/ | (716) 466-5036 | 424 Main St #497, Buffalo, NY 14202 |
| Yonkers | /city/auto-transport-yonkers-new-york/ | (914) 743-3643 | 30 S Broadway #1210, Yonkers, NY 10701 |
| Rochester | /city/auto-transport-rochester-new-york/ | (585) 632-1459 | 46 Rutter St #857, Rochester, NY 14606 |

Content angle per page: Queens = expressway-not-parkway meeting spots, airports, Florida lane, US Open; Buffalo = Thruway,
Peace Bridge (carriers stay on the US side), lake-effect bands/driving bans, medical campus + UB, Bills, Fort Myers lane;
Yonkers = I-87 only, Westchester parkway bans, the hills, Metro-North commuters, Bronxville/Scarsdale; Rochester = I-490/390/590,
Park Avenue + canal villages, medical center + RIT, lake-effect, Lilac/Jazz/Park Ave festivals, Fort Myers lane.
All four: audit CLEAR (sentences ≤ 18 words, disclosure first 2 sentences, no banned tokens), FAQPage schema, GTM ×2,
one canonical, GBP map embed, ZIP lock + consent gate. Overlap 17.5–22.3% (existing range 7–26%).

Integration: New York state page (City Pages block now Buffalo / Manhattan / Queens / Rochester / Yonkers, at-a-glance text,
Thruway and Westchester sections, Fort Totten mention, FAQ answer re-synced in schema), locations hub (New York block +
"Seventy-three"), nearby chips on Manhattan / Boston / Philadelphia / Cleveland / Detroit, "See all 73 cities" on all 73
city pages, sitemap 141 URLs. Site audit clear; Playwright 0 failures on all four (desktop + mobile, ZIP lock, consent,
stubbed quote → booking).

## Batch 19 — New York, part 2
| City | URL | Phone | Office |
|---|---|---|---|
| Syracuse | /city/auto-transport-syracuse-new-york/ | (315) 809-4321 | 250 S Clinton St #473, Syracuse, NY 13202 |
| Albany | /city/auto-transport-albany-new-york/ | (518) 990-2826 | 111 Washington Ave #259, Albany, NY 12210 |
| Brooklyn | /city/auto-transport-brooklyn-new-york/ | (929) 706-1453 | 26 Court St #2216, Brooklyn, NY 11242 |
| Bronx | /city/auto-transport-bronx-new-york/ | (929) 702-1459 | 1250 Waters Pl Suite 477, Bronx, NY 10461 |

Angles: Syracuse = 81/Thruway interchange, the 81 viaduct detour onto the 481 loop, university hill + hospitals, Micron-era
hiring in Clay, Fort Drum second vehicles, state fair + July car show, snowiest-city winter; Albany = Thruway/Northway/I-90
interchange, state workforce + session, Albany Med, Malta chip plant, Saratoga season, Watervliet/Stratton/Fort Drum staging;
Brooklyn = which bridges carry a trailer (Brooklyn Bridge bans it), BQE cantilever, meeting spots (Sunset Park, Red Hook, Navy
Yard, Canarsie), brownstone vs driveway blocks, Fort Hamilton, parade/marathon/Dyker lights; Bronx = Cross Bronx/Deegan/
Bruckner, parkway bans, Hunts Point / Co-op City / Waters Place meeting spots, Yankees game days, hospitals + colleges,
Riverdale and City Island. All four: audit CLEAR, overlap 15–22%.
Integration: NY state page City Pages block now lists all nine NY cities (+ in-text links in the Thruway and military sections,
FAQ re-synced), hub ("Seventy-seven"), neighbor chips on Manhattan / Queens / Yonkers / Buffalo / Rochester / Boston,
"See all 77 cities" everywhere, sitemap 145 URLs. Site audit clear; Playwright 0 failures on all four.

## Batch 20 — Ohio (Oct 15, 2026)
| City | URL | Phone | Office |
|---|---|---|---|
| Cincinnati | /city/auto-transport-cincinnati-ohio/ | (513) 596-6763 | 600 Vine St #748, Cincinnati, OH 45202 |
| Columbus | /city/auto-transport-columbus-ohio/ | (380) 262-1289 | 338 S High St #968, Columbus, OH 43215 |
| Akron | /city/auto-transport-akron-ohio/ | (330) 632-3174 | 3200 W Market St #780, Akron, OH 44333 |
| Dayton | /city/auto-transport-dayton-ohio/ | (937) 806-5751 | 131 N Ludlow St #981, Dayton, OH 45402 |

Angles: Cincinnati = 75/71 and the Brent Spence work zone, the hills, Northern Kentucky + Indiana share the carrier pool, HQ
relocations, UC/hospitals, cargo hubs, river floods, game days; Columbus = the split + Outerbelt, Ohio State move-in and seven
Saturdays, HQ/chip plant/data centers, DSCC + Rickenbacker, German Village brick streets, state fair/Arnold/Memorial; Akron =
77/76 Central Interchange, Turnpike tolls built in, tire/polymer/utility employers, UA + Kent State, Canton enshrinement week,
snow-belt edge; Dayton = 70/75 crossroads, Wright-Patterson PCS and the second vehicle (base lanes to San Antonio / Colorado
Springs / DC / Warner Robins), Oakwood/Oregon District, hospitals + UD/Wright State, Fuyao + Honda plants, tornado corridor,
air show + Hamvention. All four: audit CLEAR, overlap 19–23%.
Integration: Ohio state page City Pages block now lists Akron / Cincinnati / Cleveland / Columbus / Dayton (+ in-text links in the
Columbus, Cincinnati & Dayton, and Plants sections and two FAQ answers; schema re-synced), hub ("Eighty-one"), neighbor chips on
Cleveland / Indianapolis / Louisville / Lexington / Detroit, "See all 81 cities" everywhere, sitemap 149 URLs. Site audit clear;
Playwright 0 failures on all four.

## Batch 21 — Missouri (Oct 15, 2026)
| City | URL | Phone | Office |
|---|---|---|---|
| St. Louis | /city/auto-transport-st-louis-missouri/ | (314) 661-7719 | 1 Memorial Dr #878A, St. Louis, MO 63102 |
| Springfield | /city/auto-transport-springfield-missouri/ | (417) 754-3371 | 313 South Ave Suite 300, Springfield, MO 65806 |
| Columbia | /city/auto-transport-columbia-missouri/ | (573) 498-2555 | 108 Green Meadows Rd #542, Columbia, MO 65203 |
| Independence | /city/auto-transport-independence-missouri/ | (816) 710-2639 | 201 N Forest Ave #336, Independence, MO 64050 |
| Lee’s Summit | /city/auto-transport-lees-summit-missouri/ | (816) 203-0327 | 310 SW Main St #560, Lee’s Summit, MO 64063 |

Angles: St. Louis = the only city where 70/44/55/64 meet, Poplar Street Bridge, brick neighborhoods vs. wide suburbs, WashU/SLU
+ the Central West End medical complex, Boeing/Enterprise/Edward Jones/Bayer/NGA relocations, Metro East + Scott AFB, tornado +
river floods, Cardinals/Blues game nights, Ladue/Clayton enclosed; Springfield = the Interstate 44 trucking lane (Prime's home
yard), Missouri State/Drury/Evangel, CoxHealth/Mercy, Bass Pro/O'Reilly HQs, Branson + the lakes, Fort Leonard Wood, Ozarks ice
storms; Columbia = halfway on 70 between the metros, Mizzou move-in and home Saturdays, the hospitals and insurers, Jefferson City
and the legislative session, True/False + homecoming; Independence = where 70 leaves the metro, the Square vs. the 291 grids,
Lake City ammunition plant expansion, Centerpoint hospital, Whiteman families, the 435 carrier pool; Lee’s Summit = southeast corner
of the 470 loop, US 50 to Whiteman, lake-community gates (Lakewood/Raintree/Lotawana), John Knox Village, GEHA/NNSA relocations,
Downtown Days and hail. All five: audit CLEAR, overlap 16–20% (below the site median).
Integration: Missouri state page City Pages block now lists Columbia / Independence / Kansas City / Lee’s Summit / Springfield /
St. Louis (+ in-text links in the at-a-glance note, The Metros, Columbia & Springfield, and three FAQ answers; schema re-synced),
hub ("Eighty-six"), neighbor chips on Kansas City / Indianapolis / Tulsa / Chicago / Louisville / Wichita, "See all 86 cities"
everywhere, sitemap 154 URLs. Also fixed two over-long sentences I had added to the Ohio state page in Batch 20 (schema re-synced).
Site audit clear; Playwright 0 failures on all five plus the Missouri state page and Kansas City.
New helper: `tools/patches/resync_faq.py page.html` rebuilds a page's FAQPage JSON-LD from its on-page FAQ after a hand edit.

## Batch 22 — Wisconsin (Oct 15, 2026)
| City | URL | Phone | Office |
|---|---|---|---|
| Madison | /city/auto-transport-madison-wisconsin/ | (608) 208-6567 | 345 W Washington Ave #458, Madison, WI 53703 |
| Green Bay | /city/auto-transport-green-bay-wisconsin/ | (920) 981-2245 | 340 N Broadway #522, Green Bay, WI 54303 |
| Kenosha | /city/auto-transport-kenosha-wisconsin/ | (262) 474-3395 | 3535 30th Ave #604A, Kenosha, WI 53144 |
| Milwaukee (already live) | /city/auto-transport-milwaukee-wisconsin/ | (414) 485-9612 | 411 E Wisconsin Ave #548, Milwaukee, WI 53202 |

Milwaukee already carried this phone, address and the same Google Business Profile embed, so it was not rebuilt — it only
got in-text links to the three new pages and a refreshed Nearby block. **Its builder (build_milwaukee_local.py) is stale**
(the live page had a sentence-splitting pass after the builder was recovered); a warning is at the top of the file. Patch
the live page directly rather than rebuilding it.

**Kenosha map:** the iframe sent for Kenosha is the Milwaukee listing (same place id 0x8805196340349981, same coordinates),
so the Kenosha office card uses an address-based Google Maps embed for now. Send the Kenosha GBP embed and it drops into
`map_src=` in build_kenosha_local.py (one-line change, rebuild, re-zip).

Angles: Madison = 39/90/94 on the east side + the Beltline, the isthmus (State Street closed to cars, Square, campus),
mid-August lease turnover, Badger Saturdays, farmers' market, Verona software campus / insurer / hospitals / Capitol,
alternate-side parking and blizzards; Green Bay = 43 + 41 meeting at the bay, Fox River east/west sides (Astor vs.
Broadway), Lambeau game days + training camp, paper mills + Schneider-style trucking yards, hospitals, UWGB/St. Norbert,
Door County, bay squalls; Kenosha = 94 between the two carrier pools, the Illinois tollway, old plant blocks vs. Pleasant
Prairie grids, HarborPark/streetcar, Snap-on/Jockey/Uline + the 94 warehouses, Metra commuters moving up from Illinois,
Great Lakes Navy second vehicles, lake snow, Country Thunder. All three: audit CLEAR, overlap 12–17%.
Integration: Wisconsin state page City Pages block now lists Green Bay / Kenosha / Madison / Milwaukee (+ links in the
quick note, the Corridor, Milwaukee, Madison and Green Bay sections and three FAQ answers; schema re-synced), hub
("Eighty-nine"), neighbor chips on Milwaukee and Chicago, "See all 89 cities" everywhere, sitemap 157 URLs.
Site audit clear; Playwright 0 failures on the three new pages, Milwaukee and the Wisconsin state page.

## Batch 23 — California (Oct 15, 2026)
| City | URL | Phone | Office |
|---|---|---|---|
| Fresno | /city/auto-transport-fresno-california/ | (559) 553-4693 | 7161 N Howard St Ste 731, Fresno, CA 93720 |
| Bakersfield | /city/auto-transport-bakersfield-california/ | (661) 762-3480 | 1603 California Ave #425B, Bakersfield, CA 93304 |
| Stockton | /city/auto-transport-stockton-california/ | (209) 721-8115 | 110 N San Joaquin St #455, Stockton, CA 95202 |
| Irvine | /city/auto-transport-irvine-california/ | (949) 638-5862 | 18952 MacArthur Blvd #457a, Irvine, CA 92612 |

Angles: Fresno = Highway 99 as the valley's interstate, Tower/Old Fig vs. north-Fresno grids and Clovis, Fresno State move-in,
CRMC/Saint Agnes residents, the farm calendar, NAS Lemoore second vehicles, tule fog + summer heat, the Grapevine;
Bakersfield = where the trucks wait for the Grapevine, 58 as the road around LA (Vegas/Arizona), Oleander/Westchester vs.
Seven Oaks/Rosedale, oil-field crews to the Permian, CSUB + Kern Medical, Edwards families, fog/heat/dust/Tehachapi snow;
Stockton = both 5 and 99, the Crosstown, Altamont commuters moving from the Bay Area, gated Brookside/Spanos Park, warehouses
+ the Lathrop battery factory, Pacific, levees and Weston Ranch floods, Travis; Irvine = village associations and gates, the
toll roads (built into the quote), the El Toro Y, Great Park streets not on maps yet, UCI quarters, Business Complex HQs, the
car-company HQs and press/fleet cars (enclosed), Santa Ana winds and fire season, EVs. All four: audit CLEAR, overlap 11–19%.
Integration: California state page City Pages block now lists all fourteen CA cities (+ links in The Regions, Military and
Who Else Ships; schema unchanged), hub ("Ninety-three"), neighbor chips on Sacramento / San Jose / Oakland / San Francisco /
Los Angeles / Riverside / Las Vegas / San Diego / Santa Ana / Anaheim / Long Beach, "See all 93 cities" everywhere, sitemap
161 URLs. Site audit clear; Playwright 0 failures on the four new pages and the California state page.

## Batch 24 — California, part 2 (Oct 15, 2026)
| City | URL | Phone | Office |
|---|---|---|---|
| Chula Vista | /city/auto-transport-chula-vista-california/ | (619) 932-6392 | 2434 Fenton St #487, Chula Vista, CA 91914 |
| Fremont | /city/auto-transport-fremont-california/ | (229) 490-2759 | 45401 Research Ave #425A, Fremont, CA 94539 |
| San Bernardino | /city/auto-transport-san-bernardino-california/ | (909) 316-3408 | 1274 S Waterman Ave #425, San Bernardino, CA 92408 |

Angles: Chula Vista = the Navy calendar (second car to Norfolk/Jacksonville/Pensacola), west side vs. the gated east-side
villages, the 125 toll (built in), the border and customs, the hospitals and Southwestern College, fire season and May gray;
Fremont = the car factory (new cars shipped home, EVs), the five old towns and the Mission San Jose hills, the Dumbarton toll,
tech/visa relocations and the Austin lane, atmospheric rivers; San Bernardino = the Cajon Pass (wind, snow, fire closures),
the warehouses and the cargo hub, Loma Linda residents, CSUSB/Redlands, March + Fort Irwin families, mountain-town handoffs
at the bottom of the hill. All three: audit CLEAR, overlap 13–17%.
Integration: California state page City Pages block now lists all seventeen CA cities (+ links in The Regions, The Passes and
Military), hub ("Ninety-six"), neighbor chips on San Diego / Irvine / Riverside / San Jose / Oakland / San Francisco / Stockton /
Las Vegas / Anaheim, "See all 96 cities" everywhere, sitemap 164 URLs. Site audit clear; Playwright 0 failures on the three
new pages, the California state page and Irvine.
Note: the Fremont number you sent is a (229) area code (Georgia). It is on the page as given — tell me if it should be different.

## Batch 25 — Staten Island (Oct 15, 2026)
| City | URL | Phone | Office |
|---|---|---|---|
| Staten Island | /city/auto-transport-staten-island-new-york/ | (929) 723-2493 | 651 Willowbrook Rd Ste 887, Staten Island, NY 10314 |

Angles: the four bridges and how the tolls work (NJ bridges charge inbound only, the Verrazzano both ways, all built in; meeting
on the NJ side trims it), priced like New Jersey rather than Brooklyn, the four shores (North Shore hills and one-way streets,
East Shore flood blocks, South Shore driveways, West Shore mall/port/warehouses), the Florida retirement lane and the NYPD/FDNY
retirements, the hospitals, Howland Hook and the Bloomfield warehouses, Fort Hamilton + Coast Guard Sector NY, nor'easters and
the Sandy flood zone, the Verrazzano wind ban, the marathon closure. Audit CLEAR, overlap 11.6%.
Integration: New York state page City Pages block now lists ten cities (+ Staten Island in the quick note and the Parkways
toll paragraph), Brooklyn's toll FAQ now links to the Staten Island page (schema re-synced), hub ("Ninety-seven"), neighbor
chips on Brooklyn / Manhattan / Queens / Bronx / Philadelphia, "See all 97 cities" everywhere, sitemap 165 URLs. Also split
one over-long sentence in the New York page's Military section. Site audit clear; Playwright 0 failures on Staten Island, the
New York state page and Brooklyn.

## Batch 26 — Connecticut (Oct 16, 2026)
| City | URL | Phone | Office |
|---|---|---|---|
| Bridgeport | /city/auto-transport-bridgeport-connecticut/ | (475) 260-5825 | 144 Golden Hill St Ste 731, Bridgeport, CT 06604 |
| Stamford | /city/auto-transport-stamford-connecticut/ | (475) 445-3917 | 1100 Summer St #488, Stamford, CT 06905 |
| New Haven | /city/auto-transport-new-haven-connecticut/ | (475) 270-5918 | 157 Church St #558, New Haven, CT 06510 |
| Hartford | /city/auto-transport-hartford-connecticut/ | (860) 590-9072 | 20 Church St Ste 547, Hartford, CT 06103 |
| Waterbury | /city/auto-transport-waterbury-connecticut/ | (475) 377-4756 | 45 Willow St #202, Waterbury, CT 06710 |
| Norwalk | /city/auto-transport-norwalk-connecticut/ | (475) 260-1277 | 719 West Ave #458, Norwalk, CT 06850 |

Angles: Stamford = the worst stretch of 95, the Merritt truck ban, Harbor Point garages, North Stamford/Greenwich estate roads,
HQ relocations, the Palm Beach finance lane, enclosed collector cars; Norwalk = 95 + the Route 7 connector, SoNo and the
Walk Bridge replacement, Rowayton/Westport/Wilton, HQs along the connector, the Naples lane; Bridgeport = 95 meets Route 8,
Steelpointe lots, Black Rock/East Side three-family blocks vs. North End/Trumbull curbside, Sikorsky, the Port Jefferson ferry
option for Long Island; New Haven = 95 meets 91, Yale move-in/commencement, Yale New Haven residents, Long Wharf tide
flooding, biotech labs; Hartford = 84 crosses 91, insurers + Pratt & Whitney, hospitals and UConn Health, UConn/Trinity/CCSU,
snow/ice and the river dikes; Waterbury = the Mixmaster, the hill neighborhoods, Heritage Village (Southbury) and the Florida
lane, the August 2024 valley floods. All six: audit CLEAR after a second pass, overlap 19–22%.
Integration: the Connecticut state page got its FIRST City Pages block (inserted after the intro, listing all six cities), plus
links in the quick note, the Corridor, Gold Coast, and Hartford & New Haven sections; hub now has a Connecticut block
("One hundred three"); neighbor chips on Yonkers / Bronx / Boston / Albany; "See all 103 cities" everywhere; sitemap 171
URLs (lastmod 2026-10-16). Site audit clear; Playwright 0 failures on all six and the Connecticut state page.
Audit tweak: tokenizer now keeps "</a>’s" as one word (a linked name followed by a possessive no longer counts as two).

## Batch 27 — Massachusetts & Arkansas (Oct 16, 2026)
| City | URL | Phone | Office |
|---|---|---|---|
| Worcester | /city/auto-transport-worcester-massachusetts/ | (508) 290-6094 | 446 Main St #321, Worcester, MA 01608 |
| Springfield, MA | /city/auto-transport-springfield-massachusetts/ | (413) 287-7412 | 1380 Main St #481, Springfield, MA 01103 |
| Little Rock | /city/auto-transport-little-rock-arkansas/ | (501) 432-2427 | 1207 Rebsamen Park Rd #354, Little Rock, AR 72202 |
| Fayetteville, AR | /city/auto-transport-fayetteville-arkansas/ | (479) 432-2108 | 3537 N Steele Blvd #558, Fayetteville, AR 72703 |
| Fort Smith | /city/auto-transport-fort-smith-arkansas/ | (479) 552-9711 | 51 S 6th St #321, Fort Smith, AR 72901 |

Angles: Worcester = 290/190/the Pike/Route 146 and Kelley Square, the seven hills, the Canal District and the Grids,
the medical school and nine colleges, the biotech park, the ice storm and snow bans, move-in weekend; Springfield MA =
91 meets the Pike, the river bridges, Forest Park and Sixteen Acres, Westover (PCS FAQ), the insurer, Baystate, the
colleges, the Big E, the tornado; Little Rock = 40 crosses 30 (430/440/630 and the river bridges), Hillcrest and the
Heights, Chenal, the air base in Jacksonville (PCS FAQ), the medical school, state government, ice storms and the
marathon; Fayetteville = the 49 corridor and the Boston Mountains, the campus and Dickson Street, Mount Sequoyah, the
Bentonville/Springdale/Lowell headquarters lane, game days and shareholders week, ice and spring storms; Fort Smith = 40
meets 49/540 and the Alma interchange, Chaffee Crossing and Van Buren, the air base and Fort Chaffee (PCS FAQ), the
trucking headquarters, the Oklahoma side (Pocola, Roland), the rally. All five: audit CLEAR, overlap 21–25%.
Integration: Massachusetts City Pages block now lists Boston, Springfield, and Worcester, with links in the quick note,
the Worcester & Springfield section, and the "do you cover the Berkshires" FAQ (JSON-LD resynced). Arkansas got its FIRST
City Pages block (inserted after the intro) plus links in the quick note, the Little Rock lead, the 40/49 corridor text,
the UA move-in line, and the Fort Chaffee line. Hub now has an Arkansas block (inserted before California) and says
"One hundred eight"; "See all 108 cities" everywhere; sitemap 176 URLs (lastmod 2026-10-16). Site audit clear (only the
known Gilbert "number one" false positive); Playwright 0 failures on all five pages plus both state pages.
Chips: Boston now lists Worcester and drops Queens; Hartford, Albany, Tulsa, Springfield MO, Dallas, and St. Louis each
gained a neighbor. Both Springfields are registered, so chips render as "Springfield, MA" and "Springfield, MO" and the
`_s()` helper needs the full `springfield-massachusetts` / `springfield-missouri` slug to tell them apart.
New tool: `patches/autosplit.py` splits any sentence over 18 words at ", and" / ", but" / ", so" / ", which" when both
halves fit, and skips a candidate when the comma is part of a list (it printed the leftovers for hand repair; a few
list-splits from the first pass were repaired by hand).

## Batch 28 — Delaware (Oct 16, 2026)
| City | URL | Phone | Office |
|---|---|---|---|
| Wilmington | /city/auto-transport-wilmington-delaware/ | (302) 240-4170 | 221 W 10th St #373, Wilmington, DE 19801 |
| Dover | /city/auto-transport-dover-delaware/ | (302) 246-8730 | 223 W Division St #523, Dover, DE 19901 |

Angles: Wilmington = the twenty corridor miles (95 on the rebuilt viaduct, 495 past the port, 295 to the Memorial
Bridge), the toll plaza at the Maryland line, downtown/Riverfront and Christiana Mall handoffs, rowhouse blocks (Trolley
Square, Little Italy, Forty Acres) against Brandywine Hundred/Pike Creek curbside, Greenville/Hockessin estate roads,
the card banks, the chemical and pharma campuses, Chancery, the hospitals, the fruit port, Ida 2021 on the Brandywine,
the Grand Prix / jazz / Italian festival / Point-to-Point calendar, UD move-in; Dover = no interstate (Route 1 toll road
with the Dover and Biddles Corner plazas against the free DuPont Highway), Division Street / Route 8 west to the Amish
farms, the Green and Legislative Hall, the air base gate (PCS FAQ, second car), postwar subdivisions curbside, the bayside
towns (Bowers Beach, Kitts Hummock, Leipsic; Sandy 2012), race weekend at the Monster Mile, the session, Dover Days, the
state fair in Harrington, Delaware State move-in. Both: audit CLEAR first pass, overlap 14.7% (Dover) / 15.2% (Wilmington).
Integration: Delaware got its FIRST City Pages block (inserted after the intro; both cities), plus links in the intro, the
Corridor section, the Wilmington & Newark section, the Dover section, and the Dover AFB FAQ (one added sentence pointing
to the Dover page; JSON-LD resynced). Hub: new Delaware block between Connecticut and Florida, "One hundred ten", and the
intro H2 — which had said "fifty-seven local pages" since the hub was first built — now reads "one hundred ten local pages".
Neighbor chips: Philadelphia gained Wilmington; Baltimore gained Wilmington and Dover (both 7 chips). "See all 110
cities" everywhere; sitemap 178 URLs (lastmod 2026-10-16). Site audit clear (only the Gilbert note); Playwright 0
failures on Wilmington, Dover, the Delaware state page, locations.html, Philadelphia and Baltimore.
Note for later batches: the hub count lives in four places now — the meta description (×3 occurrences) and the lead
paragraph ("One hundred ten …") plus the intro H2 ("one hundred ten local pages", lower case). Update all of them.

## Batch 29 — Colorado (Oct 16, 2026)
| City | URL | Phone | Office |
|---|---|---|---|
| Denver | /city/auto-transport-denver-colorado/ | (983) 212-2105 | 1401 Lawrence St #1688, Denver, CO 80202 |
| Colorado Springs | /city/auto-transport-colorado-springs-colorado/ | (719) 800-4804 | 559 E Pikes Peak Ave Ste 487, Colorado Springs, CO 80903 |
| Aurora | /city/auto-transport-aurora-colorado/ | (720) 893-9478 | 2675 S Abilene St Ste 598, Aurora, CO 80014 |

(983 is the newer Denver overlay code alongside 303/720 — nothing to flag.) Hours shown as MT.
Angles: Denver = the Mousetrap (25 × 70), the lowered 70 through Elyria, 76/225/270, C-470 vs the E-470 toll, Peña and the
airport fly-and-ship, Brighton Boulevard / Quebec / Speer / Hampden meeting spots, Capitol Hill and Highlands vs Central
Park and suburban curbside, the Tech Center and aerospace plants, hospitals, Auraria/DU/CU move-in, hail, the 2019 and
2021 March blizzards, the stock show, altitude, the traction-law FAQ ("not in the city"); Colorado Springs = 25 and
Monument Hill, US 24 / Ute Pass, Powers and Academy, Fort Carson / Peterson / Schriever / Cheyenne Mountain / the Academy
(PCS and cadet FAQs, gate handoffs along Powers and Highway 115), Old North End / Manitou / Broadmoor vs Briargate and
the Powers corridor, the 2016 hail, the 2012 and 2013 fires, graduation week, the hill climb; Aurora = 225 as the spine,
70 and E-470, Colfax, the Anschutz campus (residents FAQ), Buckley (PCS FAQ), Heather Gardens gate, the gated southeast
(gate-code FAQ), airport fly-and-ship, the 2018 hail, tornado warnings. All three: audit CLEAR after sentence splits,
overlap 18.3% (Aurora) / 20.7% (Colorado Springs) / 22.3% (Denver) after a diversification pass on the shared hail,
checklist, non-running, "what do you need", blizzard and CTA wording.
Integration: Colorado got its FIRST City Pages block (after the intro; all three cities), plus links in the intro, the
Front Range section (Denver hub line, Colorado Springs line, Aurora in the suburbs line), the Military section (two), the
Who Ships Here campuses line, and two FAQs (Fort Carson/Peterson → Colorado Springs page; hail → Denver and Aurora pages;
JSON-LD resynced). Hub: Colorado block inserted before Connecticut, counts "One hundred thirteen" (×4) and the intro H2.
Chips: Albuquerque, Salt Lake City, Kansas City and Wichita each gained Denver (SLC and Wichita now carry 9 chips — they
wrap cleanly on mobile, Playwright checked). "See all 113 cities" everywhere; sitemap 181 URLs (lastmod 2026-10-16).
Site audit clear (only the Gilbert note); Playwright 0 failures on the three new pages, the Colorado state page, SLC,
Wichita and locations.html.

## Batch 30 — Georgia beyond Atlanta (Oct 16, 2026)
| City | URL | Phone | Office |
|---|---|---|---|
| Columbus, GA | /city/auto-transport-columbus-georgia/ | (706) 813-8084 | 18 9th St #574, Columbus, GA 31901 |
| Augusta, GA | /city/auto-transport-augusta-georgia/ | (706) 749-6343 | 1143 Laney Walker Blvd #625, Augusta, GA 30901 |
| Macon | /city/auto-transport-macon-georgia/ | (478) 331-3289 | 2960 Riverside Dr Ste 458, Macon, GA 31204 |
| Savannah | /city/auto-transport-savannah-georgia/ | (912) 455-2132 | 49 Park of Commerce Way #445, Savannah, GA 31405 |
| Athens | /city/auto-transport-athens-georgia/ | (706) 890-6131 | 2500 Daniells Bridge Rd #578, Athens, GA 30606 |

Augusta and Columbus now exist in two states each (Augusta ME, Columbus OH), so chips print "Augusta, GA" / "Augusta, ME"
and `_s()` needs the full `-georgia` slugs — same pattern as the two Springfields. Hours shown as ET.
Angles: Columbus = 185 ending at the Fort Moore gate (PCS and graduation-week FAQs, Victory Drive handoffs), the J.R. Allen
bypass, Uptown/Lakebottom vs North Columbus curbside, the Alabama side (Phenix City prices the same), the insurer and the
payments campus, Michael 2018; Augusta = 20 and the Bobby Jones loop, Fort Eisenhower cyber/signal moves (Gordon Highway
gates), the Hill/Olde Town vs Evans and South Augusta, the medical district (office is in it), the nuclear site and the
Burke County plant, Masters week (FAQ), Helene 2024, the 2014 ice; Macon = the 75/16 fork and the interchange rebuild
(FAQ), 475 for through trucks, Robins AFB (PCS FAQ, Watson/Russell handoffs), Vineville/Ingleside vs north Macon, the
insurer on Riverside, the cherry blossoms (FAQ), Helene, the 1994/1998 floods, the state fair; Savannah = the 16/95
interchange, 516 to the port, the squares (truck-restricted FAQ), Ardsley oaks, Tybee/Skidaway (FAQ), the port release
FAQ, Hunter/Stewart PCS, the jet plant, the new EV plant (FAQ), SCAD September move-in, Matthew/Irma/Debby, contraflow
evacuations, king tides, the 2018 and 2025 snows; Athens = no interstate (316 and 441 off 85, the Loop), UGA move-in
(second week of August) and move-out, the seven home Saturdays (never inside the Loop on a game day), Five Points/downtown
vs Westside and Oconee, student-complex gates (FAQ), the hospital, the 2014 ice and 2017 snow, Helene.
All five: audit CLEAR after sentence splits; overlap 19.6–21.8% after a diversification pass (Columbus had started at 31%
against Colorado Springs and Macon at 28% — the shared military-town Basics / Why Ship Guy / tornado paragraph / "what do
you need" wording was rewritten on both, plus Augusta and Athens).
Integration: the Georgia state page's existing City Pages block (Atlanta only) was regenerated to all six cities, with
links in the intro (Augusta, Savannah), the Corridors section (Macon, Columbus), the Coast lead (Savannah), the Military
section (Columbus, Augusta), the Calendars section (Athens, Augusta) and four FAQs (Masters → Augusta; historic district →
Savannah; UGA → Athens; PCS → Columbus and Augusta); JSON-LD resynced. Hub Georgia block regenerated (6 cities), counts
"One hundred eighteen" (×4) and the intro H2. Chips: Atlanta re-cut to Athens, Macon, Augusta, Columbus, Charlotte,
Tuscaloosa, Jacksonville, Orlando (Louisville and Mobile dropped as the farthest); Jacksonville gained Savannah, Tallahassee
and Tuscaloosa gained Columbus, Charlotte gained Augusta. "See all 118 cities" everywhere; sitemap 186 URLs (lastmod
2026-10-16). Site audit clear (only the Gilbert note); Playwright 0 failures on all five, the Georgia state page, Atlanta
and locations.html.
Gotcha fixed this batch: the hub's Georgia block carried a `<a class="state-link">` after the chips (only Alabama, Alaska,
Arizona, California, Florida and Georgia have one), so a non-greedy regex ending at `</div></div>` ran on into the Hawaii
block and deleted it. `audit_site.py` flagged `hub-missing-city honolulu`; Hawaii and the Georgia state-link were restored
from the previous zip. When regenerating a hub block, anchor the regex on the NEXT state's `<h3>`, not on `</div></div>`.

## Batch 31 — Alabama & Arizona (Oct 16, 2026)
| City | URL | Phone | Office |
|---|---|---|---|
| Huntsville | /city/auto-transport-huntsville-alabama/ | (256) 988-7539 | 102 Clinton Ave W #477, Huntsville, AL 35801 |
| Montgomery | /city/auto-transport-montgomery-alabama/ | (334) 542-4055 | 335 Kershaw Industrial Blvd #522, Montgomery, AL 36117 |
| Mesa | /city/auto-transport-mesa-arizona/ | (928) 447-6589 | 225 E Main St #144B, Mesa, AZ 85201 |
| Chandler | /city/auto-transport-chandler-arizona/ | (928) 612-3715 | 3075 W Ray Rd #525, Chandler, AZ 85226 |
| Glendale | /city/auto-transport-glendale-arizona/ | (928) 564-8665 | 6751 N Sunset Blvd #225, Glendale, AZ 85305 |

OWNER CHECK: the three Arizona numbers are 928, the northern/western Arizona code (Flagstaff, Yuma, Prescott). The
Phoenix-metro codes are 480 (Mesa, Chandler) and 623 (Glendale). Used exactly as supplied, like Fremont's 229. Alabama
hours show CT; Arizona hours show MST (no daylight time).
Angles: Huntsville = 565 as the spur off 65, the Parkway overpasses, Redstone (PCS/agency FAQ, Research Park Boulevard
gate), the space center and contractors, the new plants west of town, Twickenham/Monte Sano vs South Huntsville/Madison,
the new subdivisions "not on the carrier maps yet" FAQ, the 2011 outbreak and tornado season; Montgomery = the 65/85
interchange, the Eastern Boulevard, Maxwell's school-year calendar and the Gunter annex (PCS FAQ), the Korean plant's
car carriers (why pickups are fast), Garden District/Old Cloverdale vs Dalraida and the gated east side, Prattville prices
the same, the legislative session, Zeta 2020; Mesa = US 60 and the 202, RV resorts and 55+ communities (gate FAQ),
Lehi dirt roads, Las Sendas gates, Eastmark curbside, the snowbird tide both ways (lead-time FAQ), Canadian visitors
(domestic leg only), the helicopter plant and data centers, spring training at Riverview, the monsoon; Chandler = 10
plus the Price and Santan loops, the chip plants and Oregon/NorCal/New Mexico transfers (FAQ), the Price corridor
handoffs, Ocotillo/Fulton Ranch/Sun Lakes gates, Ahwatukee and the reservation, the dust off the Casa Grande farms,
the ostrich festival; Glendale = the 101 through Westgate (office is there), Grand Avenue as the Las Vegas road,
Luke (PCS FAQ, Litchfield Road gates), football Sundays/bowl game/concerts (event-day FAQ), the March stadium auction
(FAQ), Camelback Ranch, Arrowhead gates vs Sun City curbside with golf carts.
All five: audit CLEAR after sentence splits. Overlap needed TWO diversification passes: the first pass reused the Batch 30
alternates verbatim (Montgomery hit 26.5% with 372 shingles against Columbus GA; Chandler 29.8%), so every standard
block got a third wording. Final: Huntsville 21.0%, Montgomery 20.1%, Mesa 16.2%, Chandler 16.8%, Glendale 15.8%.
LESSON: each batch needs its OWN wording for the Basics paragraph, Why Ship Guy, checklist, the non-running and
"what do you need" FAQs, the dust/storm FAQ and the table footnote — alternates from an earlier batch are already taken.
Integration: both state pages' City Pages blocks regenerated (Alabama now 4 cities, Arizona 6) with links in the Alabama
Metros and Military sections and two FAQs (PCS → Huntsville and Montgomery; plant carriers → Montgomery, Huntsville), and
in the Arizona Corridors (Chandler), Season (Mesa, Glendale) and Military (Luke "in Glendale") sections plus two FAQs
(auctions and Luke → Glendale); JSON-LD resynced. Hub Alabama and Arizona blocks regenerated with the regex anchored on
the next state's `<h3>` (state-links preserved), counts "One hundred twenty-three" (×4) and the intro H2. Chips: Phoenix
re-cut to Mesa, Chandler, Glendale, Gilbert, Tucson, Las Vegas, Albuquerque, San Diego (Henderson dropped); Gilbert
gained the three metro pages (8 chips), Tucson gained Mesa and Chandler, Tuscaloosa gained Huntsville and Montgomery,
Mobile gained Montgomery. "See all 123 cities" everywhere; sitemap 191 URLs (lastmod 2026-10-16). Site audit clear
(only the Gilbert note); Playwright 0 failures on all five, both state pages, Phoenix, Gilbert, Tucson and locations.html.

## Batch 32 — Hawaii neighbor islands & Idaho (Oct 17, 2026)
| City | URL | Phone | Office |
|---|---|---|---|
| Hilo | /city/auto-transport-hilo-hawaii/ | (808) 824-5278 | 688 Kinoole St #405, Hilo, HI 96720 |
| Kahului | /city/auto-transport-kahului-hawaii/ | (808) 468-3952 | 400 Hana Hwy #225A, Kahului, HI 96732 |
| Boise | /city/auto-transport-boise-idaho/ | (208) 924-4078 | 999 W Main St #425A, Boise, ID 83702 |
| Meridian | /city/auto-transport-meridian-idaho/ | (208) 742-9621 | 1120 S Rackham Way Ste 429A, Meridian, ID 83642 |
| Nampa | /city/auto-transport-nampa-idaho/ | (208) 646-1142 | 5700 E Franklin Rd #499B, Nampa, ID 83687 |

Hawaii pages follow the Honolulu OCEAN structure, not the local template: h1 "Car Shipping TO …", stats row "Weekly
Sailings", sections The Process (three legs, barge in some weeks) / The Island / Lanes (Origin → port, land + ocean,
weeks, sedan rates = Honolulu figures + ~$300 and ~1 week; last row "Honolulu (inter-island barge), about 1 week,
$300–$450") / Terminal Rules (ULI) / Who Ships Here / Calendar & Weather / After Arrival / Why Ship Guy / office (HST).
The routing claim mirrors the Hawaii state page exactly: "some sailings call at Hilo/Kahului directly, others land in
Honolulu and transfer to the inter-island barge (three to seven days); we book whichever lands first". No Honolulu
builder exists (that page pre-dates the builder system), so build_hilo_local.py is the reference for any future
Kauai/Kona page. Hilo overlap started at 35% (terminal rules list and FAQs copied from Honolulu, process copied to
Kahului) and was rewritten to 11%; Kahului 14%.
Angles: Hilo = Hilo Harbor vs the barge, Puna lava-rock lanes (FAQ), the Kona side through Kawaihae (FAQ), the saddle,
UH Hilo, the observatories, the training area, rain, the 2018 eruption, Iselle/Lane, Merrie Monarch week, the
agricultural inspection both directions; Kahului = the only deep harbor, Wailuku/Kihei/Wailea gates, Upcountry and
Hana handoffs (FAQ), the west side rebuilding after the 2023 fire with Pali rockfall closures (FAQ), trade winds, Kona
storms, whale season, the resorts and the summit observatories; Boise = 84 and the Connector, closing-date deliveries
(FAQ), the chip maker's fab, North End/foothills vs the Bench, Mountain Home and Gowen Field (FAQ), the inversion, the
2017 snow, fire smoke (FAQ), runoff, Boise State Saturdays; Meridian = the Eagle Road exit, new-subdivision routing
(FAQ), Spurwing/Tuscany gates (FAQ), the insurer and the fragrance company, Dairy Days and the speedway, Old Town;
Nampa = the Karcher interchange as the first valley exit, downtown one-ways and the college blocks, farm-road pickups
(FAQ), the Stampede (FAQ), the sugar beet campaign and the beet trucks, the warehouse and the cheese plant, Caldwell and
Kuna price the same. Idaho overlap needed its own variant pass (Meridian had started at 35% against Boise/Nampa and the
Batch 31 alternates): final Boise 21.8%, Meridian 21.7%, Nampa 15.3%.
Integration: Hawaii City Pages block regenerated (3 cities) with links in The Islands section and the neighbor-island
FAQ (JSON-LD unchanged — links only). Idaho got its FIRST City Pages block (after the intro) with links in the quick
note, the Corridors, Newcomers and Who Ships Here sections, and two FAQs (new subdivisions → Meridian and Nampa; students
→ Boise); JSON-LD resynced. Hub: Hawaii block regenerated (anchored on Illinois, state-link kept) and an Idaho block
inserted after it; counts "One hundred twenty-eight" (×4) and the intro H2. Chips: Honolulu re-cut to Hilo, Kahului,
Long Beach, Los Angeles, Oakland, Anchorage; Salt Lake City re-cut to Provo, West Jordan, West Valley City, Boise,
Denver, Las Vegas, Phoenix, Portland (Henderson and Sacramento dropped, 8 chips); Portland gained Boise. "See all 128
cities" everywhere; sitemap 196 URLs (new entries lastmod 2026-10-17). Site audit clear (only the Gilbert note);
Playwright 0 failures on all five, both state pages, Honolulu, Salt Lake City, Portland and locations.html.

## Batch 33 — Indiana, Kauai & the Chicago collar (Oct 26, 2026)
| City | URL | Phone | Office |
|---|---|---|---|
| Fort Wayne | /city/auto-transport-fort-wayne-indiana/ | (260) 300-2248 | 1690 Broadway #1055A, Fort Wayne, IN 46802 (Electric Works) |
| Evansville | /city/auto-transport-evansville-indiana/ | (812) 954-6362 | 201 NW 4th St Suite 425B, Evansville, IN 47708 (Old Courthouse) |
| Kapaʻa (Kauai) | /city/auto-transport-kapaa-hawaii/ | (808) 435-7375 | 4-1624 Kuhio Hwy #145A, Kapaʻa, HI 96746 |
| Aurora, IL | /city/auto-transport-aurora-illinois/ | (331) 272-4208 | 160 S River St #473, Aurora, IL 60506 |
| Joliet | /city/auto-transport-joliet-illinois/ | (815) 853-1975 | 116 N Chicago St #788, Joliet, IL 60432 (beside the Rialto) |

MAPS: the five Google Business Profile embeds arrived in the same message as the rows but were lost to a context
compaction before they were written into the builders, so all five office cards currently use the address-based
`maps?q=` fallback (same as Kenosha). To swap in the real embeds: paste each iframe `src` into the builder's
`office(... map_src='...')` argument (currently `map_src=None`), rebuild the page, and push. Nothing else changes.

Second "Aurora" on the site (Aurora, CO is Batch 29): slug auto-transport-aurora-illinois, chips print "Aurora, IL" /
"Aurora, CO", `_s()` needs the full slug for either. Kapaʻa keeps the ʻokina in NAMES, the title, the h1 and the chips
(slug is plain `kapaa`); the office `map_q` uses "Kapaa". Hours: Fort Wayne and Evansville ET (both Eastern-zone
counties), Aurora and Joliet CT, Kapaʻa HST.
Kapaʻa follows the Hilo/Kahului OCEAN structure (build_hilo_local.py is the reference): port is Nawiliwili in Lihue
(ten miles down Kuhio Highway), "some sailings call at Nawiliwili directly, others land in Honolulu and ride the
inter-island barge (three to seven days)", same lane table as Hilo/Kahului, Port Allen named as the west-side option.
Angles: Fort Wayne = 69 and the 469 loop, Electric Works (the office), downtown one-ways and West Central brick streets,
the hospital systems and the pickup plant (FAQ), the campuses (FAQ), Three Rivers Festival (FAQ), the Auburn auctions
(FAQ), the 1982 flood and lake snow on 69 (FAQ), New Haven/Huntertown price the same (FAQ); Evansville = 64 to the north,
69 ending at the river until the new bridge (FAQ on the toll), the Lloyd, the Twin Bridges, the Old Courthouse (the
office), the West Side and Franklin Street, the Fall Festival (FAQ), the Toyota plant in Princeton (FAQ), the 1937 flood
and the 2005 tornado (FAQ), Newburgh/Henderson price the same (FAQ); Kapaʻa = the three legs, the Kapaʻa crawl and the
bypass, the Homesteads hill roads (FAQ), the one-lane Hanalei bridge with a hauler that stops at Princeville (FAQ),
Nawiliwili vs Honolulu + barge (FAQ), Iniki 1992 and the April 2018 north-shore flood (FAQ), the agricultural
inspection, the resorts, Wilcox, KCC and the missile range at Barking Sands; Aurora = the Reagan Tollway with the
tolls inside the quote (FAQ), Stolp Island one-ways and the Tanner district (FAQ), the far east side in DuPage, the
outlets and the casino by the tollway, the hospitals and the Eola warehouses (FAQ), closing-date deliveries (FAQ), the
Fourth of July, the Fox River floods of 2008/2013, the 2020 derecho; Joliet = 80 crossing 55, the intermodal (FAQ), the
80 rebuild (FAQ), the lift bridges (FAQ), the Cathedral Area, the refinery, JJC, the drag strip (race-car FAQ), the
1990 Plainfield tornado, the 2013 flood. All five CLEAR on the first audit pass after the usual long-sentence
splits; overlap after a wording pass: Fort Wayne 18.6%, Evansville 18.0%, Kapaʻa 15.5% (started 24.6% against Hilo),
Aurora 19.9%, Joliet 18.0%.
Integration: Indiana City Pages block regenerated (3 cities) and the intro, quick note, Regions paragraphs and the
"Do you serve Fort Wayne and Evansville?" FAQ rewritten (they said both were "covered from this page"); JSON-LD
resynced. Illinois block regenerated (3 cities) with links in the quick note, The Hub lead, Weather & Access and the
freight-hub FAQ (links only — JSON-LD unchanged). Hawaii block regenerated (4 cities) with a Kapaʻa sentence in The
Islands and a link in the neighbor-island FAQ; JSON-LD resynced. Hub: Hawaii, Illinois and Indiana chip rows
regenerated in place (chips div only, next-state anchor untouched); counts "One hundred thirty-three" (×4) and the intro
H2. Chips: Indianapolis re-cut to Fort Wayne, Evansville, Chicago, Louisville, Cincinnati, Dayton, Lexington, St. Louis
(Cleveland dropped); Chicago re-cut to Aurora, Joliet, Milwaukee, Kenosha, Indianapolis, Detroit, St. Louis, Cleveland
(Wichita and Louisville dropped); Louisville and St. Louis gained Evansville; Dayton and Detroit gained Fort Wayne;
Kenosha gained Aurora; Honolulu, Hilo and Kahului gained Kapaʻa. "See all 133 cities" everywhere; sitemap 201 URLs
(new entries lastmod 2026-10-26). Site audit clear (only the Gilbert note); Playwright 0 failures on all five, the
three state pages and locations.html. Pushed straight to main from the session (no zip).

## Batch 34 — Illinois round two (Oct 26, 2026)
| City | URL | Phone | Office |
|---|---|---|---|
| Rockford | /city/auto-transport-rockford-illinois/ | (815) 864-8085 | 303 N Main St #350A, Rockford, IL 61101 (across from the Coronado) |
| Springfield, IL | /city/auto-transport-springfield-illinois/ | (217) 395-6794 | 1 Horace Mann Plaza Suite 573, Springfield, IL 62715 |
| Champaign | /city/auto-transport-champaign-illinois/ | (217) 595-1736 | 1807 S Neil St #463, Champaign, IL 61820 |
| Waukegan | /city/auto-transport-waukegan-illinois/ | (224) 497-2802 | 13 N Genesee St #452, Waukegan, IL 60085 |

All four office cards carry the real Google Business Profile embeds (the rows and iframes are also saved in
`tools/rows/batch34_rows.txt`; save every future batch's rows there first, before anything else). Third "Springfield"
on the site (MA, MO, IL): slug auto-transport-springfield-illinois, chips print "Springfield, IL". Hours CT for all four.
Angles: Rockford = the 90/39 corner and the free US 20 bypass, downtown by the Coronado and the market, Signal Hill and
Churchill's Grove (FAQ), the cargo airport and the package hub (FAQ), the aerospace plants, the Belvidere plant idling
and restarting, Stroll on State (FAQ), the 2018 Rock River flood and Keith Creek, the 2015 Fairdale tornado, the
tollway and the transponder (FAQ), Loves Park/Belvidere/Rockton price the same (FAQ), DeKalb students (FAQ);
Springfield = 55 and 72, the parkways, Old Route 66 on 6th and 9th, the Capitol one-ways and the closed Lincoln Home
blocks (FAQ), Enos Park and Aristocracy Hill, the state agencies and the session (FAQ), the State Fair (FAQ), the
Route 66 Mother Road festival with enclosed show cars (FAQ), the 2006 ice storm and the March 2006 tornadoes (FAQ),
Lake Springfield drives, Chatham/Sherman price the same (FAQ), the Guard and the air wing; Champaign = the 57/74
interchange, Neil and Prospect, downtown one-ways and Campustown no-stopping zones (FAQ), move-in weekend with
deliveries the week before or after (FAQ), graduation shipping in May (FAQ), Carle and the research park (FAQ),
football Saturdays (FAQ), the prairie wind, the 2013 Gifford tornado, Urbana/Savoy/Mahomet price the same (FAQ);
Waukegan = the Tri-State vs free Route 41 (FAQ), Genesee Street and the bluff, the south side grid, Great Lakes with
recruits unable to keep a car and families on orders (FAQ), the pharmaceutical corridor to Deerfield (FAQ), Six Flags
traffic on Grand and Fright Fest (FAQ), graduation Fridays on Sheridan, lake snow, the Des Plaines closing Grand and
Belvidere in Gurnee (FAQ), Gurnee/Zion/North Chicago price the same (FAQ). All four CLEAR after the long-sentence
pass; overlap after a wording pass: Rockford 19.2% (started 24.6% against Aurora IL), Springfield 19.4%, Champaign
16.1%, Waukegan 17.4%.
Integration: Illinois City Pages block regenerated (7 cities); the intro and quick note now name every city page and
route Peoria and the Metro East to the state page; links added in the downstate paragraphs (Springfield, Rockford,
Champaign), Weather & Access (Waukegan) and the downstate FAQ (Springfield, Champaign); JSON-LD resynced. Hub:
Illinois chip row regenerated (7); counts "One hundred thirty-seven" (×4) and the intro H2. Chips: Chicago re-cut to
Aurora, Joliet, Waukegan, Rockford, Milwaukee, Kenosha, Indianapolis, St. Louis (Detroit and Cleveland dropped);
St. Louis re-cut with Springfield IL in place of Little Rock; Kenosha and Milwaukee gained Waukegan; Madison gained
Rockford; Aurora gained Rockford and Waukegan; Joliet gained Champaign. "See all 137 cities" everywhere; sitemap 205
URLs (lastmod 2026-10-26). Site audit clear (only the Gilbert note); Playwright 0 failures on all four, the Illinois
page, Chicago and locations.html. Pushed straight to main.

## Batch 35 — Johnson County, Topeka & Owensboro (Oct 26, 2026)
| City | URL | Phone | Office |
|---|---|---|---|
| Overland Park | /city/auto-transport-overland-park-kansas/ | (913) 565-7461 | 5440 W 110th St Ste 458A, Overland Park, KS 66211 (Corporate Woods) |
| Olathe | /city/auto-transport-olathe-kansas/ | (913) 298-6699 | 15571 S Mahaffie St #658A, Olathe, KS 66062 |
| Topeka | /city/auto-transport-topeka-kansas/ | (785) 503-3373 | 1035 SE Quincy St #775, Topeka, KS 66612 |
| Owensboro | /city/auto-transport-owensboro-kentucky/ | (270) 514-6233 | 1727 Sweeney St #355, Owensboro, KY 42303 |

GBP embeds on all four (rows saved in `tools/rows/batch35_rows.txt`). Hours CT for all four — Owensboro (Daviess
County) is in the Central zone, unlike Louisville and Lexington. Johnson County pages price with the Kansas City
pool and reuse the Kansas state page's Denver/Dallas figures ($450–$650 / $430–$620); the Topeka → Kansas City lane
($140–$230, ~65 mi) differs from Lee's Summit → Topeka (~85 mi) on purpose.
Angles: Overland Park = the 435/69 crossing, Corporate Woods (the office), downtown and the north grids, the Blue
Valley gates with the gate-code handoff (FAQ), the three hospitals and the engineering firm, the old wireless campus
at 119th and Nall, closing-date deliveries for the schools (FAQ), the soccer complex and Chiefs Sundays (FAQ), the
Fourth at Corporate Woods, the 2002 ice storm, the 2019 Linwood tornado, Fort Leavenworth staff-college families
(FAQ), Leawood/Lenexa/Prairie Village price the same (FAQ); Olathe = 35 straight through, K-10 and K-7, the square
and the courthouse, the GPS maker's campus on 151st (FAQ), the hospital, the intermodal at Gardner/Edgerton (FAQ),
the De Soto battery plant, Cedar Creek's gate, Old Settlers (FAQ), the county fair, the Gardner truck stops in ice,
Gardner/Spring Hill/Lenexa price the same (FAQ); Topeka = the Turnpike ending at the city with free 70 west (FAQ on
tolls), the 470 loop, the Capitol one-ways and the closed-off session days, Potwin's brick streets and traffic
circles (FAQ), NOTO, Oakland and Fiesta Mexicana (FAQ), the state agencies and the session (FAQ), the tire, snack
and candy plants, the rail shops, the refueling wing, the 1951 flood, the 1966 tornado, Washburn and Lawrence
students (FAQ), Lawrence/Silver Lake/Auburn price the same (FAQ); Owensboro = the US 60 bypass with no interstate
in town, I-165 south to Bowling Green, the Natcher Bridge vs the old blue bridge (FAQ), the Audubon Parkway,
Frederica, the regional hospital and the distilleries (FAQ), the mortgage office and the pipeline companies, the
barbecue festival (FAQ), ROMP, Friday After 5, the air show, the 1937/1997 floods, the January 2000 tornado, the
2009 ice storm, Rockport/Hawesville/Henderson price the same (FAQ). All four CLEAR after the long-sentence pass.
Overlap started at 26–28% (the Batch 34 alternates are now taken too) and needed a full fresh-wording pass on the
Basics paragraph, the checklist, the storm FAQ, the student FAQ, the military paragraph, Why Ship Guy, Your Options
and the "what do you need" FAQ: final Overland Park 20.7%, Olathe 22.0%, Topeka 21.9%, Owensboro 19.7%.
Integration: Kansas City Pages block regenerated (4 cities); the intro and quick note no longer say Johnson County
and Topeka are "covered from this page"; links in the Johnson County paragraph, the Interstate 70 paragraph, the
Johnson County FAQ and the Turnpike FAQ; JSON-LD resynced. Kentucky block regenerated (3 cities); intro, quick
note, The West & the Rivers paragraph and the western-Kentucky FAQ link Owensboro; JSON-LD resynced. Hub: Kansas
and Kentucky chip rows regenerated; counts "One hundred forty-one" (×4) and the intro H2. Chips: Kansas City re-cut
to Overland Park, Olathe, Independence, Lee's Summit, Topeka, Columbia, St. Louis, Wichita (Tulsa, Oklahoma City,
Denver dropped); Wichita re-cut to Oklahoma City, Kansas City, Overland Park, Topeka, Tulsa, Dallas, Denver,
Albuquerque (Indianapolis, Chicago, Independence dropped); Louisville re-cut to Lexington, Evansville, Owensboro,
Indianapolis, Cincinnati, St. Louis, Chicago, Atlanta (Cleveland dropped); Independence gained Overland Park;
Lee's Summit gained Olathe and Overland Park; Columbia gained Topeka; Evansville and Lexington gained Owensboro.
"See all 141 cities" everywhere; sitemap 209 URLs (lastmod 2026-10-26). Site audit clear (only the Gilbert note);
Playwright 0 failures on all four, both state pages, Kansas City and locations.html. Pushed straight to main.

## Batch 36 — Louisiana (Oct 26, 2026)
| City | URL | Phone | Office |
|---|---|---|---|
| Baton Rouge | /city/auto-transport-baton-rouge-louisiana/ | (225) 435-8297 | 440 N 3rd St #229B, Baton Rouge, LA 70802 |
| Shreveport | /city/auto-transport-shreveport-louisiana/ | (318) 583-6904 | 717 Crockett St #473A, Shreveport, LA 71101 |
| Metairie | /city/auto-transport-metairie-louisiana/ | (504) 514-1757 | 2121 N Causeway Blvd #554A, Metairie, LA 70001 |

GBP embeds on all three (rows in `tools/rows/batch36_rows.txt`). Hours CT. Baton Rouge and Metairie price on the
New Orleans pool and reuse the New Orleans lane figures (Baton Rouge → Houston $250–$380 matches the Louisiana state
page); Shreveport prices on the Dallas pool and says so. The Causeway claim mirrors the New Orleans page (carriers
cross it, northbound toll built in, wind/fog closures to high vehicles). The 2005 Metairie flooding is attributed to
the unmanned pumps, not the canal breach (that was the Orleans side).
Angles: Baton Rouge = the bridge and the 10/12 split (FAQ on the bridge and the basin), Spanish Town and the Garden
District oaks (FAQ), the LSU side with no campus handoff on a football Saturday (FAQ), the refinery and the river
plants (FAQ), the hospitals on Essen, the session, Gustav and Ida, the 2016 flood, Prairieville/Denham Springs/Zachary
price the same (FAQ), hurricane routine (FAQ); Shreveport = 20 and the 49 gap, the Dallas pool, Barksdale with the
gated housing (FAQ), the Highlands oaks (FAQ), the hospital system and the casinos (FAQ), the cyber campus, the State
Fair (FAQ), the parades on Clyde Fant, the 2021 freeze and the 2022 Keithville tornado (FAQ), Bossier/Haughton/Minden
price the same (FAQ); Metairie = the Causeway interchange and the toll (FAQ), Veterans and the parade route (FAQ), Old
Metairie oaks (FAQ), Ochsner and the airport (FAQ), the Saints facility, Elmwood, the pumps and the 2005 flooding, Zeta
and Ida, Belle Chasse sailors (FAQ), Kenner/Harahan/the Northshore price the same (FAQ). All three CLEAR after the
long-sentence pass; overlap needed a fresh-wording pass on the hurricane FAQ (Baton Rouge and Metairie had the same
one), the Basics paragraph, the military lines and the closers: final Baton Rouge 17.8%, Shreveport 20.0%, Metairie
15.9%.
Integration: Louisiana City Pages block regenerated (4 cities); the intro no longer says Baton Rouge and Shreveport
are covered from the state page; links in the plants paragraph, the Baton Rouge neighborhoods paragraph, the
Barksdale paragraph, The Bayou & the North, the LSU FAQ and the north FAQ; JSON-LD resynced. New Orleans page: the
Across the Lake sentence now links Metairie (links only). Hub: Louisiana chip row regenerated; counts "One hundred
forty-four" (×4) and the intro H2. Chips: New Orleans re-cut to Metairie, Baton Rouge, Mobile, Houston, Shreveport,
Atlanta, Tuscaloosa; Houston and Mobile gained Baton Rouge; Dallas, Fort Worth and Little Rock gained Shreveport.
"See all 144 cities" everywhere; sitemap 212 URLs (lastmod 2026-10-26). Site audit clear (only the Gilbert note);
Playwright 0 failures on all three, the Louisiana page, New Orleans and locations.html. Pushed straight to main.

## Batch 37 — Maine (Oct 26, 2026)
| City | URL | Phone | Office |
|---|---|---|---|
| Portland, ME | /city/auto-transport-portland-maine/ | (207) 360-4574 | 411 Congress St #355A, Portland, ME 04101 |
| Lewiston | /city/auto-transport-lewiston-maine/ | (207) 994-8972 | 75 Park St #452A, Lewiston, ME 04240 |
| Bangor | /city/auto-transport-bangor-maine/ | (207) 605-7681 | 28 Olive St #445A, Bangor, ME 04401 |

GBP embeds on all three (rows in `tools/rows/batch37_rows.txt`). Hours ET. Second "Portland" on the site (OR and ME):
slug auto-transport-portland-maine, chips print "Portland, ME" / "Portland, OR". Maine pages follow the Augusta
"honest timing" convention, not the 1–3 day default: stats row "2–4 Days / Honest Pickup", a "why does a pickup take
two to four days" FAQ on every page, date-range language in the CTA and the "what do you need" FAQ, and Bangor adds
the 3-to-6-day far-north FAQ. Portland reuses the Maine state page's lane table (priced from Portland); Lewiston adds
~35 miles and Bangor ~130 miles to every lane (the state page says so), with the prices stepped accordingly. Manchester
prices over Boston on fewer miles on all three (lighter lane), and each page says why.
Angles: Portland = the Turnpike/295 hub and the turnaround, the peninsula vs Marginal Way (FAQ), Deering and South
Portland curbs, the medical center and the insurers (FAQ), the shipyard in Bath, summer residents June/September (FAQ),
cruise season at the Ocean Gateway, the February 2013 blizzard, the January 2024 storm tides over Commercial Street,
mud season, South Portland/Falmouth/Freeport price the same (FAQ), USM/Bowdoin students (FAQ); Lewiston = the Auburn-side
Turnpike exits, the Kennedy Park three-decker grid and the mill lots (FAQ), Bates move-in (FAQ), the two hospitals and
the Auburn plants, the balloon festival (FAQ), the Dempsey weekend, the 1998 ice storm, the 1987 river flood, a mud
season FAQ, Auburn/Lisbon/Poland price the same (FAQ); Bangor = the top of the run with most carriers turning around
(FAQ), the 95 exits and the 395 spur, downtown brick and the Broadway oaks (FAQ), the mall side and the Hermon truck
stop, EMMC and the Bar Harbor lab (FAQ), UMaine Orono move-in (FAQ), the airport and the refueling wing, the waterfront
concerts, Acadia traffic, the 1976 Groundhog Day flood and the Kenduskeag ice jams, the far north with Houlton
meeting spots (FAQ). All three CLEAR after the long-sentence pass; overlap needed a wording pass (Your Options, Why
Ship Guy, the hospital paragraph, the checklist, the winter line): final Portland 21.9%, Lewiston 21.5%, Bangor 20.2%.
Integration: Maine City Pages block regenerated (4 cities); the intro no longer says Portland, Bangor and Lewiston are
covered from the state page; links in the corridor lead, the Portland lead and paragraph, the campuses paragraph and
two FAQs (links only — JSON-LD unchanged). Augusta page: Straight Talk and the colleges paragraph link Portland,
Bangor and Lewiston (links only). Hub: Maine chip row regenerated; counts "One hundred forty-seven" (×4) and the intro
H2. Chips: Augusta re-cut to Portland, Lewiston, Bangor, Boston, Manhattan, Philadelphia, Baltimore; Boston re-cut
with Portland ME in place of Rochester; Worcester gained Portland ME. "See all 147 cities" everywhere; sitemap 215
URLs (lastmod 2026-10-26). Site audit clear (only the Gilbert note); Playwright 0 failures on all three, the Maine
page, Augusta, Boston and locations.html. Pushed straight to main.

## Batch 38 — Tempe & Surprise (Oct 26, 2026)
| City | URL | Phone | Office |
|---|---|---|---|
| Tempe | /city/auto-transport-tempe-arizona/ | (928) 492-6068 | 4500 S Lakeshore Dr #458B, Tempe, AZ 85282 (the Lakes) |
| Surprise | /city/auto-transport-surprise-arizona/ | (928) 459-5190 | 15331 W Bell Rd #558, Surprise, AZ 85374 (by the stadium) |

GBP embeds on both (rows in `tools/rows/batch38_rows.txt`). Hours MST (Arizona keeps standard time year round, as on
the other Valley pages). Both numbers are 928 area codes inside the 480/602/623 Valley, like Glendale's — add them to the
"Arizona (928) area codes to confirm" owner item. Lane tables reuse the Mesa/Glendale Valley figures; Surprise prices
the Las Vegas lane under the rest of the Valley (the carriers pass on Grand) and Tempe adds a Chicago student lane.
Angles: Tempe = the four-freeway box and the rebuilt Broadway Curve, the campus and Mill Avenue with the streetcar and
the light rail streets a trailer cannot stop on (FAQ), Maple-Ash, the towers on the lake (FAQ), the research park, the
car retailer and the utility HQs, ASU move-in with deliveries the week before or after (FAQ), graduation (FAQ),
football Saturdays and the Ironman (FAQ), the Angels at Diablo, the 2014 Broadway Curve flood, the Lakes and
Guadalupe/Ahwatukee/Mesa price the same (FAQ); Surprise = Grand Avenue as the Las Vegas road and the 303, the railroad
crossings, the Bell Road bridge, the original townsite, Sun City Grand and Sun City West with the golf-cart lanes and
gated sections (FAQ), Marley Park and Prasada, the snowbird tide with two-to-three-week notice (FAQ), the Canadians
(FAQ — US addresses only, no border crossings), Luke families (FAQ), spring training on Bell (FAQ), the haboobs and the
Agua Fria crossings (FAQ), Sun City West/El Mirage/Wickenburg price the same (FAQ). Both CLEAR after the long-sentence
pass — note that splitting Tempe's first intro sentence pushed the broker disclosure to sentence three and the audit
caught it; the disclosure must stay inside the first two sentences of the first paragraph. Overlap: Tempe started
24.8% against Champaign (the student-town blocks) and finished 21.5%; Surprise 19.2%.
Integration: Arizona City Pages block regenerated (8 cities). The Valley chips block on the Arizona page used plain
<span> chips; the six that have pages (Tempe, Surprise, Mesa, Chandler, Gilbert, Glendale) are now links. Surprise
linked in the snowbird paragraph; Phoenix page links Tempe in the ASU sentence; Glendale page links Surprise in the
retirees paragraph and the Peoria/Surprise FAQ (JSON-LD resynced). Hub: Arizona chip row regenerated; counts "One
hundred forty-nine" (×4) and the intro H2. Chips: Phoenix re-cut to Tempe, Mesa, Chandler, Glendale, Gilbert, Surprise,
Tucson, Las Vegas (Albuquerque and San Diego dropped); Gilbert re-cut with Tempe in place of Albuquerque; Mesa,
Chandler and Tucson gained Tempe; Glendale gained Surprise. "See all 149 cities" everywhere; sitemap 217 URLs (lastmod
2026-10-26). Site audit clear (only the Gilbert note); Playwright 0 failures on both, the Arizona page, Phoenix,
Glendale and locations.html. Pushed straight to main.

## Batch 39 — Grand Rapids, Warren, Davenport, Sioux City, Ankeny, Columbia MD, Germantown (Oct 26, 2026)
| City | URL | Phone | Office |
|---|---|---|---|
| Grand Rapids, MI | /city/auto-transport-grand-rapids-michigan/ | (616) 883-2952 | 77 Monroe Center St NW #775A, Grand Rapids, MI 49503 (downtown, beside Rosa Parks Circle) |
| Warren, MI | /city/auto-transport-warren-michigan/ | (586) 551-7329 | 31850 Mound Rd #400A, Warren, MI 48092 (Mound at 13 Mile) |
| Davenport, IA | /city/auto-transport-davenport-iowa/ | (563) 921-0721 | 102 E 2nd St #473A, Davenport, IA 52801 (downtown by the riverfront) |
| Sioux City, IA | /city/auto-transport-sioux-city-iowa/ | (712) 412-4080 | 700 4th St STE 479, Sioux City, IA 51101 (downtown) |
| Ankeny, IA | /city/auto-transport-ankeny-iowa/ | (515) 373-2431 | 106 SW Linden St #199A, Ankeny, IA 50023 (Uptown) |
| Columbia, MD | /city/auto-transport-columbia-maryland/ | (410) 709-7449 | 9160 Guilford Rd #568, Columbia, MD 21046 (east side, by Route 32) |
| Germantown, MD | /city/auto-transport-germantown-maryland/ | (301) 321-7641 | 20900 N Frederick Rd #485A, Germantown, MD 20876 (Frederick Road at Milestone) |

GBP embeds on all seven (rows saved to `tools/rows/batch39_rows.txt` on arrival). Hours ET for Michigan and Maryland,
CT for Iowa. Stats rows: Warren uses the Detroit pool "1–2 Days", Sioux City "2–3 Days" (one interstate into the corner
of the state, with a "why does a pickup take two to three days" FAQ and date-range language), the rest "1–3 Days".
Pricing: Warren = the Detroit table; Grand Rapids a little under Detroit on the Chicago lane; Ankeny = the Iowa/Des
Moines table; Davenport under Des Moines on the Chicago lane; Sioux City a little over Omaha; Columbia and Germantown
track the Maryland/Baltimore tables (Germantown a little over Baltimore on the 95-north lanes, Pittsburgh cheaper).
Angles: Grand Rapids = 196/131/96 and the S-curve, Heritage Hill and the West Side grids, the Medical Mile and the
furniture makers, ArtPrize (FAQ), lake-effect bands and the 2013 flood, the snowbird lane (FAQ); Warren = 696 and the
mile roads, the plant carriers that take private cars on the return run, the Tech Center, the arsenal, the bungalow
grids (FAQ), the 696 rebuild, the 2014/2021 floods, the Dream Cruise; Davenport = 80 at the river, the Walcott truck
stop, the arsenal and the tractor plants, the Bix weekend (FAQ), the 2019 flood (no flood wall), Rock Island/Moline
across the bridges (FAQ); Sioux City = 29 as the only interstate, the packing plants, the refueling wing (FAQ), Saturday
in the Park, the 2019 flood that closed 29, ground blizzards; Ankeny = 35 with 80 five minutes south, the tractor
plant and the convenience-store chain, DMACC, the State Fair interchange backup (FAQ), the 2020 derecho and the
Saylorville spillway, cul-de-sacs (FAQ); Columbia = 95/29/32, the ten villages and the village-center handoff (FAQ),
Fort Meade and the cyber firms (FAQ), Merriweather nights (FAQ), the Ellicott City floods and the derecho, the tunnel/
bridge tolls (FAQ); Germantown = the 270 corridor and its rush hours (FAQ), MD 355, Town Center with MARC but no Metro
(FAQ), the energy campus, the satellite firm and the labs, Clarksburg/Gaithersburg/Damascus (FAQ), the ICC toll (FAQ),
the snow line above the Beltway. All seven CLEAR after one long-sentence pass (241 sentences). Overlap after a fresh-
wording pass on the Basics, checklist, storm, student, military, Why Ship Guy, Options, "what do you need", CTA and
hospital blocks: Germantown 15.7%, Davenport 17.9%, Warren 18.0%, Sioux City 18.4%, Grand Rapids 18.6%, Ankeny 18.8%,
Columbia 19.8%.
Integration: Michigan City Pages block regenerated (Detroit, Grand Rapids, Warren) with the intro and quick note
rewritten; Grand Rapids linked in the West & the Capital paragraph, the snowbird paragraph, the west-side chip and
the "Do you serve Grand Rapids" FAQ; Warren linked in the Plants sentence. Iowa got its FIRST City Pages block (after
The Corridors, before Des Moines) with Davenport, Sioux City, Ankeny; quick note rewritten ("Iowa has no city page
yet" retired); Davenport linked in the Quad Cities paragraph and FAQ, Sioux City in the I-29 sentence, Ankeny in the
subdivisions paragraph and the Des Moines FAQ; the three plain chips are now links. Maryland block regenerated
(Baltimore, Columbia, Germantown) with intro and quick note rewritten; Columbia linked in the Howard County sentence,
Germantown in the Clarksburg sentence and the Bethesda FAQ; both chips now links. Detroit page links Warren in the
plants sentence; Baltimore page links Columbia in the suburbs sentence and the Columbia/Towson FAQ. JSON-LD resynced
on Michigan, Iowa, Maryland and Baltimore. Chips regenerated on the seven new pages plus Detroit, Baltimore, Milwaukee,
Fort Wayne, Wilmington, Dover, Madison and Rockford. Hub: Michigan and Maryland rows regenerated, a new Iowa row
inserted between Indiana and Kansas; counts "One hundred fifty-six" (×4) and the intro H2. "See all 156 cities"
everywhere; sitemap 224 URLs (lastmod 2026-10-26). Site audit clear (only the Gilbert note); Playwright 0 failures on
all seven, the Michigan/Iowa/Maryland pages, Detroit, Baltimore and locations.html. Pushed straight to main.

## Batch 40 — South Bend, Lawrence, Lafayette, Ann Arbor, Seattle, Spokane (Oct 27, 2026)
| City | URL | Phone | Office |
|---|---|---|---|
| South Bend, IN | /city/auto-transport-south-bend-indiana/ | (574) 328-5795 | 511 E Colfax Ave #445, South Bend, IN 46617 (East Bank) |
| Lawrence, KS | /city/auto-transport-lawrence-kansas/ | (785) 384-4711 | 2029 Becker Dr #558, Lawrence, KS 66047 (west campus) |
| Lafayette, LA | /city/auto-transport-lafayette-louisiana/ | (337) 357-9845 | 116 E Congress St #359A, Lafayette, LA 70501 (downtown) |
| Ann Arbor, MI | /city/auto-transport-ann-arbor-michigan/ | (734) 212-1989 | 4750 Venture Dr #522, Ann Arbor, MI 48108 (south side, off State Street) |
| Seattle, WA | /city/auto-transport-seattle-washington/ | (206) 800-8980 | 1700 Westlake Ave N #563A, Seattle, WA 98109 (west shore of Lake Union) |
| Spokane, WA | /city/auto-transport-spokane-washington/ | (509) 369-5265 | 304 W Pacific Ave #477, Spokane, WA 99201 (downtown) |

GBP embeds on all six (rows saved to `tools/rows/batch40_rows.txt` on arrival). Hours ET for Indiana and Michigan, CT for
Kansas and Louisiana, PT for Washington. Stats rows: Ann Arbor uses the Detroit pool "1–2 Days", the rest "1–3 Days".
Seattle and Spokane are Washington's first city pages, so the Washington page got its FIRST City Pages block (after
The Corridor, before Seattle & the East Side) and the "Washington has no city page yet" note was retired. Pricing: South
Bend between Chicago and Fort Wayne (under Fort Wayne to Chicago, over it to Ohio); Lawrence = the Kansas City/Topeka
tables; Lafayette = the Baton Rouge table, a little under it to Houston and Dallas; Ann Arbor = the Detroit table, a
little under it to Chicago; Seattle = the Washington state table (priced from Seattle); Spokane = the Washington/Boise/
Portland cross-references, a little over Seattle south and east.
Angles: South Bend = the Toll Road with the tolls built in, the 31 bypass, the Near Northwest and Northeast grids, the
campus closed to a trailer, Granger/Mishawaka/Elkhart (FAQ), the Michigan towns across the line (FAQ), the RV plants
(FAQ), football Saturdays (FAQ), the Feb 2018 and Aug 2016 floods, the lake-effect bands (FAQ); Lawrence = the Turnpike
(toll FAQ) and K-10, Oread and the brick streets (FAQ), KU move-in (FAQ), Fort Leavenworth officers (FAQ), basketball
nights (FAQ), the 2019 Linwood tornado and the 2007 ice storm (FAQ), Eudora/Baldwin City/Topeka (FAQ); Lafayette =
10/49/the Thruway, the basin bridge in fog (FAQ), the Saint Streets and River Ranch (FAQ), the oilfield yards and the
two-week offshore rotations (FAQ), UL move-in (FAQ), Festival International and Mardi Gras (FAQ), hurricane season with
the rebook rule (FAQ), the Aug 2016 flood, the Feb 2021 ice, Youngsville/Broussard/New Iberia (FAQ); Ann Arbor = 94/23/
M-14, the campus one-way grid and the Old West Side (FAQ), the Big House Saturdays and the art fair (FAQ), Michigan
move-in and commencement (FAQ), Michigan Medicine and the automakers' research centers (FAQ), the Feb 2023 ice storm
(FAQ), the snowbird lane (FAQ), Ypsilanti/Saline/Dexter (FAQ); Seattle = 5 between the water and the hills, the two
floating bridges and the 520/99 tolls (FAQ), the ship canal drawbridges, Queen Anne's counterbalance (FAQ), the
stadium lots and park and rides as the handoffs, tech relocations in September (FAQ), the UW quarter calendar (FAQ),
the planemaker, the base/Whidbey/Everett, the port and the Alaska/Hawaii dock (FAQ), Seafair and game days (FAQ),
the Feb 2019 snow, the 2021 heat dome, the 2020 smoke, the Nov 2024 windstorm, Bellevue/Tacoma/Everett (FAQ);
Spokane = 90 and the north freeway, the South Hill and Browne's Addition (FAQ), Fairchild (FAQ), Gonzaga and EWU's
quarters (FAQ), Hoopfest and Bloomsday (FAQ), the Valley/Cheney/Coeur d'Alene across the line (FAQ), Snoqualmie
closures (FAQ), the Nov 2015 windstorm, the Dec 2008 snow, the 2021 heat, the Aug 2023 fires and smoke (FAQ).
All six CLEAR after one long-sentence pass (217 sentences) plus three trims. Overlap after a fresh-wording pass on the
Basics, checklist, student, military, Why Ship Guy, Options, cost-FAQ tail, "what do you need", CTA and non-running
blocks (the Batch 39 phrasings had already entered the corpus): Ann Arbor 17.2%, South Bend 17.3%, Lawrence 17.6%,
Spokane 17.7%, Lafayette 17.8%, Seattle 18.4%.
Integration: Indiana (4 cities), Kansas (5), Louisiana (5) and Michigan (4) City Pages blocks regenerated with intros
and quick notes rewritten; Washington block inserted (2). In-text links: Indiana Toll Road sentence and chip; Kansas
I-70 sentence, the KU/K-State sentence, the chip and the student FAQ; Louisiana I-10 sentence, the oil-patch
paragraph, the UL sentence, the chip, the basin FAQ and the LSU/UL FAQ; Michigan the Ann Arbor campus sentence, the
chip and the move-in FAQ; Washington the tech lead, the Spokane paragraph, both chips and three FAQs (Seattle house,
Spokane, tech relocations). City pages: Detroit (U-M sentence, note, chip, FAQ), Portland OR (I-5 sentence), Boise
(Spokane sentence + Seattle cost FAQ), Topeka (Turnpike sentence, chip, FAQ), Olathe (K-10 sentence), Kansas City MO
(KU sentence, chip, FAQ), Baton Rouge (basin sentence). JSON-LD resynced on Washington, Louisiana, Detroit and Topeka.
Chips regenerated on the six new pages plus Detroit, Indianapolis, Chicago, Kansas City, Portland, Boise, Warren,
Grand Rapids, Fort Wayne, Topeka, Overland Park, Olathe, Baton Rouge, New Orleans, Metairie, Shreveport, Meridian,
Nampa and Anchorage (Detroit, Indianapolis, Chicago, Kansas City, Portland and Boise re-cut to eight; the rest
appended). Hub: Indiana, Kansas, Louisiana and Michigan rows regenerated, a new Washington row inserted between Utah
and Wisconsin; counts "One hundred sixty-two" (×4) and the intro H2. "See all 162 cities" everywhere; sitemap 230
URLs (lastmod 2026-10-27). Site audit clear (only the Gilbert note); Playwright 0 failures on all six, the five state
pages, Detroit, Portland, Boise, Topeka, Kansas City, Baton Rouge, Olathe and locations.html. Pushed straight to main.

## Batch 41 — Virginia Beach, Pittsburgh, Allentown, Reading (Oct 27, 2026)
| City | URL | Phone | Office |
|---|---|---|---|
| Virginia Beach, VA | /city/auto-transport-virginia-beach-virginia/ | (757) 908-3865 | 4560 South Blvd #733, Virginia Beach, VA 23452 (by Lynnhaven) |
| Pittsburgh, PA | /city/auto-transport-pittsburgh-pennsylvania/ | (412) 314-2407 | 2681 Sidney St #399, Pittsburgh, PA 15203 (South Side Flats) |
| Allentown, PA | /city/auto-transport-allentown-pennsylvania/ | (610) 839-7989 | 1320 Hausman Rd #473, Allentown, PA 18104 (West End) |
| Reading, PA | /city/auto-transport-reading-pennsylvania/ | (610) 229-5982 | 2395 Lancaster Pike #599, Reading, PA 19607 (Shillington) |

GBP embeds on all four (rows saved to `tools/rows/batch41_rows.txt` on arrival). Hours ET; stats rows "1–3 Days" on all
four. Virginia Beach is Virginia's first city page, so the Virginia page got its FIRST City Pages block (after The
Corridors, before Northern Virginia) and the "Virginia has no city page yet" note was retired. Pricing: Virginia
Beach = the Virginia table's Norfolk figures, a little over Richmond on the lanes north (the carrier crosses the water
first); Pittsburgh = the Pennsylvania table's Pittsburgh rows plus the Philadelphia cross-reference; Allentown = the
Philadelphia table, a little under it to New York; Reading = Philadelphia on every lane, a little over Allentown to New
York and a little under it to Baltimore and Washington.
Angles: Virginia Beach = 264/64 and the tunnel schedule (FAQ), the tolled Downtown/Midtown tunnels built in, the
Oceanfront side streets closed to a trailer in summer (FAQ), the North End and Sandbridge, Oceana/Little Creek/Dam
Neck orders with the gate handoff (FAQ), the shipyards and the port with the customs release (FAQ), the Neptune
Festival (FAQ), Isabel/Matthew and the nor'easters (FAQ), Norfolk/Chesapeake/Newport News (FAQ); Pittsburgh = the
Turnpike tolls (FAQ), the Parkways and the two tunnels, the bridge weight limits and the 2022 Forbes Avenue
collapse, the hills with the handoff in the flats (FAQ), Oakland's residency changeover (FAQ), Pitt/CMU move-in (FAQ),
the robotics labs, the airlift wing, Steelers days and the marathon (FAQ), the landslides and the 2018 Route 30 slide
(FAQ), Cranberry/Monroeville/the Mon Valley (FAQ); Allentown = 78 and the state's storm closures to trucks (FAQ),
Route 22, the Northeast Extension toll (FAQ), the row-house blocks with the arena-garage handoff (FAQ), the health
network and the warehouses (FAQ), the college move-ins (FAQ), the fair at 17th and Chew and Musikfest (FAQ), the Jan
2016 and Nov 2018 storms, Ida and Diane, Bethlehem/Easton/Emmaus (FAQ); Reading = the 422 bypass and its rebuild
(FAQ), 222, the 176 Turnpike spur (FAQ), the row-house grid and Mount Penn (FAQ), the hospital and the plants (FAQ),
Albright/Alvernia/Kutztown move-in (FAQ), the Schuylkill floods with Agnes and Ida (FAQ), Boyertown's antique cars,
Wyomissing/Exeter/Kutztown (FAQ). All four CLEAR after one long-sentence pass (130 sentences) plus a few trims. The
standard blocks were written fresh for this batch (new Basics, checklist, student, military, Why Ship Guy, Options,
cost-FAQ tail, "what do you need", CTA and non-running wording), so no overlap pass was needed: Virginia Beach 16.0%,
Pittsburgh 17.2%, Allentown 17.9%, Reading 19.2%.
Integration: Virginia block inserted (1 city) with the intro and quick note rewritten; Virginia Beach linked in the
Hampton Roads suburbs sentence, the chip and the PCS FAQ (JSON-LD resynced). Pennsylvania block regenerated (4 cities)
with the intro and quick note rewritten; Pittsburgh linked in the Pittsburgh section lead and the house FAQ (resynced),
Allentown in the commuter sentence, Reading in the Lancaster/York sentence, and all three chips are now links. City
pages: Philadelphia (Turnpike sentence), Cleveland, Akron, Columbus and Buffalo (their Pittsburgh lane sentences).
Chips regenerated on the four new pages plus Philadelphia and Baltimore (re-cut to eight), Wilmington (re-cut to
eight), Cleveland, Akron, Columbus, Buffalo, Dover, Raleigh, Durham, Charlotte, Columbia MD and Bridgeport. Hub:
Pennsylvania row regenerated, a new Virginia row inserted between Utah and Washington; counts "One hundred sixty-six"
(×4) and the intro H2. "See all 166 cities" everywhere; sitemap 234 URLs (lastmod 2026-10-27). Site audit clear (only
the Gilbert note); Playwright 0 failures on all four, the Virginia and Pennsylvania pages, Philadelphia, Cleveland,
Akron, Columbus, Buffalo and locations.html. Pushed straight to main.

## SEO & best-practices pass (Oct 27, 2026)
No URL changed. What changed, site-wide:
- **Breadcrumbs.** Every city page now shows Home › Locations › State › City above the H1 (state pages: Home › Locations ›
  State), with a matching `BreadcrumbList` JSON-LD (`id="sg-breadcrumb"`). The legacy Corpus Christi page kept its own
  crumb style but gained the Locations and Texas links and the schema.
- **LocalBusiness schema** (`id="sg-localbusiness"`) on all 166 built city pages, generated from the office card: name
  "Ship Guy Auto Transports" (the GBP name), street/city/state/ZIP, the local phone, Mo–Su 06:00–23:00, `hasMap`, and
  `geo` coordinates parsed from the GBP embed URL (pages on the address-based map fallback have no `geo`).
- **Organization + WebSite schema** on the home page (`sg-organization`, `sg-website`): legal name Ship Guy Logistics LLC,
  logo `/assets/favicon-512.png`, telephone +1-866-499-2815 (the header/footer line), quotes@shipguy.com, Facebook and
  Instagram `sameAs`. The `BreadcrumbList` items on services.html and contact.html were relative (`index.html`) and are
  now absolute URLs.
- **Heads.** how-it-works.html had an empty meta/OG/Twitter description (" Free quote.") — fixed. locations.html's
  description was 169 characters and carried the city count — now 157 and count-free. Eight titles over 65 characters
  were trimmed (auction, cost, cross-country, military, open, services, state-to-state, Corpus Christi); title, og:title
  and twitter:title stay identical on each page.
- **Corpus Christi** was an orphan: not in NAMES, the hub, the Texas City Pages block or the sitemap, and its internal
  links still pointed at retired `.html` URLs (redirect hops) and a dead `#reviews` anchor. It is now registered
  (NAMES = 167), linked from the hub's Texas row, the Texas block/quick note/prose/chip, in the sitemap (235 URLs), its
  links are clean URLs, and its four "24/7" claims read "7 days" (house rule). It is still the old-generation page with
  the booking iframe (main-site key in the HTML) — the rebuild still waits on an address/phone row from the owner.
- **House style.** Fifteen legacy pages had semicolons in prose (rate-table footnotes, two core pages) — split.
- **Headers / robots / redirects.** `Strict-Transport-Security: max-age=31536000` added to `_headers`; `robots.txt`
  disallows `/tools/`; `_redirects` sends `/tools/*` to `/` so the versioned tooling is never served.
- **Tooling versioned.** `tools/` (localpage.py, builders, audits, overlap, Playwright test, patches, rows, this runbook)
  now lives in the repo. It is synced from `/home/claude/tools` at push time (see the recipe below); `__pycache__` is
  git-ignored. Nothing in it contains a key.
Plumbing changes that affect the next batch:
- `localpage.build()` now calls `seo_enrich.enrich_city()` after `clean_links()`, so every new page gets the breadcrumb,
  the BreadcrumbList and the LocalBusiness block automatically (a rebuild of an existing page is byte-identical to the
  enriched page). `_make_template()` strips those blocks from the Milwaukee source, so the cache stays clean.
- `locations.html`: the three meta descriptions no longer carry the count. The hub script's assertions are now
  `h.count('One hundred sixty-seven') == 1` (the body paragraph) and `h.count('one hundred sixty-seven local pages') == 1`
  (the intro H2) — update both strings to the new count each batch.
- `test_new_pages.cjs` counts Corpus Christi in EXPECT_COUNT; `audit_site.py` audits 239 pages (50 + 167 + 22).
- Push recipe: overlay the build tree, then re-copy the tooling (`rm -rf repo/tools && mkdir repo/tools && (cd /home/claude/tools &&
  tar --exclude=__pycache__ --exclude='*.pyc' -cf - .) | tar -xf - -C repo/tools`; rsync is not installed), then
  `diff -rq --exclude=.git --exclude=tools --exclude=.gitignore build repo`.
Verified: head scan clean (no title over 65, no meta outside 110–160, og:title == title everywhere, every JSON-LD block
parses: 217 FAQPage, 217 BreadcrumbList, 166 LocalBusiness, Organization, WebSite); `audit_site.py` clear (only the
Gilbert note); Playwright 0 failures on Reading, Detroit, the Michigan page and locations.html; breadcrumb screenshots
checked at 1366 and 390 px. Pushed straight to main.

## Florida Google Business Profile links (this delivery)
A fourth "Directions → Open in Google Maps" row was added to the office card on Gainesville, Jacksonville,
Tallahassee and Daytona Beach using the maps.app.goo.gl links you sent. The builders carry `map_link=` so rebuilds keep it.

## Site-wide fixes (this delivery)
1. **Duplicate canonical removed on 67 pages** (all 66 city pages + locations.html). Each of those pages carried a
   second `<link rel="canonical" href="https://shipguy.com/">` plus a homepage Open Graph block after its own tags —
   a latent template bug that told Google the city page's canonical might be the homepage. Every page now has exactly
   one canonical and one OG/Twitter block pointing at itself. (Phoenix had only the homepage block; it was rewritten to
   the page's own values.)
2. **ZIP lock re-applied** on 132 tool pages (`tools/patches/zip_lock.py`, idempotent). Verified in the browser:
   letters stripped, 4 digits blocked with the message, 5 digits pass, Places suggestions restricted to postal codes,
   payload sends `origin_postal_code` / `destination_postal_code`.

## Verification run (all green)
- `audit_content.py` on the 3 new pages: CLEAR.
- `audit_site.py` over 239 pages (50 state + 167 city + 22 core, latest run after the Oct 27 SEO pass): links/anchors resolve, tags balanced, JSON-LD valid, GTM ×2, one H1, one canonical,
  no orphans, hub/state/city interlinked, sitemap complete, ZIP lock + consent gate on every tool page.
  (One pre-existing note: Gilbert's "the number one thing that delays…" is not a superiority claim.)
- `test_new_pages.cjs` (Playwright) on Tulsa, Norman, Edmond, Gainesville + home, vehicle-quote, Texas: desktop & mobile
  layout, no JS errors, ZIP lock, consent gate, stubbed end-to-end quote → booking redirect, payload shape.
- Overlap (7-word shingles, prose only, vs every other city + state page): Tulsa 17.8%, Norman 19.3%, Edmond 21.0% —
  inside the range of the existing city pages (7–26%, median ≈ 19%). The shared part is the deliberately standard
  blocks (Basics, table footnote, Why Ship Guy, the two standard FAQs).

## Repo cleanup (Oct 19, 2026) — old-generation pages retired with 301s
Pushed directly to GitHub (`samson-ops/shipguy`, commit 9eabb3c) after the Batch 26–32 push (8049d1b). The GitHub
web uploader caps a drag at 100 files, so from now on batches are pushed from the session (the Claude GitHub App is
installed on the repo); the delta/bundle zips are a fallback only.
Removed 111 files the current site did not link to or list in the sitemap:
- the 49 old `car-shipping-<city>-<st>.html` root pages (first-generation city pages, each embedding the hosted
  BeRocker widget) — every one now 301s to its `/city/...` page, in both URL forms (`/car-shipping-miami-fl` and
  `/car-shipping-miami-fl.html`), taken from the old `redirect-map-301.txt`;
- `_preview-do-not-deploy/` (49 preview files);
- `about.html` → `/`, `privacy.html` → `/privacy-policy`, `car-shipping-insurance.html` → `/faq`,
  `car-shipping-texas.html` → `/texas-auto-transport`, `dealer-auto-transport.html` and `vehicle-shipping.html`
  (already redirected), `city/index.html` → `/locations`, `city/vehicle-quote/`, `vehicle-quote/vehicle-quote/` and
  `vehicle-quote-florida/` → `/vehicle-quote`, the stray flat `city/auto-transport-phoenix-arizona.html` → the real
  directory page, plus `README-CHANGES.md` and `redirect-map-301.txt`.
`_redirects` now carries 121 rules. Still in the repo on purpose: `city/auto-transport-corpus-christi-texas/` — an
older-style page with real content and no replacement yet (send a Corpus Christi phone/address/map row and it gets
rebuilt in the current format); and `vehicle-quote.html`, kept byte-identical to `vehicle-quote/index.html`.
The build tree (`/home/claude/build/shipguy`) mirrors the repo exactly (240 files); `audit_site.py` is clean.

## How to build the next city
```
cd /home/claude/tools            # (or wherever the tools zip is unpacked; set SG_SITE to the site root)
# 1) register the slug + neighbours in localpage.py (see the "Batch 17" block), 2) copy a builder, write the content,
python3 builders_city/build_<city>_local.py
python3 audit_content.py city/<slug>/index.html      # sentences, disclosure, tokens, schema
python3 overlap.py 1 --list                          # verbatim overlap vs every other page
# then: state page City Pages block, locations.html, "See all N cities" count, neighbours' chips, sitemap
python3 audit_site.py && node test_new_pages.cjs <slug>
```
The shell template is generated from `city/auto-transport-milwaukee-wisconsin/index.html` (cached as
`city_template.html`; delete the cache after any site-wide patch so new pages inherit it).

## Owner actions still open
- **The GitHub repo is public and the two BeRocker lead-source keys are in it** (`functions/api/quote/[[path]].js` and
  `functions/api/quote2/[[path]].js` carry them as `DEFAULT_KEY` fallbacks, and the legacy Corpus Christi page embeds the
  main-site key in its booking iframe). Either make the repo private (Settings → General → Danger Zone → Change
  visibility; the Cloudflare Pages GitHub app keeps working) or rotate the keys in BeRocker and set the new value only in
  the Pages `BEROCKER_LEAD_KEY` environment variable, after which the fallbacks can be removed. The keys are already in
  the git history, so rotation is the real fix.
- **Two main phone numbers are live.** The header, footer, contact page and every state page use (866) 499-2815; the
  home-page hero, the quote page and the SMS consent text use (866) 297-3244. Pick one — mixed NAP signals hurt local
  SEO — and say which; the Organization schema currently uses 499-2815.
- Add any new domains to the Google Maps key referrer restrictions.
- Submit the updated sitemap in Search Console after deploy; confirm `/vehicle-quote` and `/vehicle-quote/` don't redirect.
- Verify the "4.9/5 · 487+ Reviews" and the (866) 297-3244 line.
- Re-send the five Batch 33 Google Business Profile map embeds (Fort Wayne, Evansville, Kapaʻa, Aurora IL, Joliet) so the
  address-based maps can be swapped for the GBP embeds; Kenosha's embed is still outstanding too.
- Confirm the 928 area codes on the Valley pages (Mesa, Chandler, Glendale from Batch 31; Tempe and Surprise from Batch 38)
  and the Fremont (229) number; 928 is the northern/western Arizona code and 229 is southwest Georgia.
