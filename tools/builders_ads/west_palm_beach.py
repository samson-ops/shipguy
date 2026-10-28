#!/usr/bin/env python3
"""Google Ads landing page: West Palm Beach, FL  ->  /vehicle-quote-west-palm-beach-florida  (phone line (561) 960-3491).
Built from the live /vehicle-quote page by adspage.build(); rerun after any quote-tool change."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import adspage

TEL = '+15619603491'
CFG = dict(
    slug='vehicle-quote-west-palm-beach-florida', city='West Palm Beach', st='FL', lead_prefix='ADS-WPB',
    tel=TEL, disp='(561) 960-3491', disp_nbsp='(561)&nbsp;960-3491',
    tz='America/New_York', tz_label='ET', hours_open=6, hours_close=23, open_label='6 AM', close_label='11 PM',
    hours_static='Real people, seven days a week, 6 AM to 11 PM ET',

    title='West Palm Beach Car Shipping Quote in 30 Seconds | Ship Guy',
    meta='Instant car shipping quote for West Palm Beach, FL. Door-to-door auto transport from downtown to Wellington, open or enclosed, any state. Call (561) 960-3491.',

    eyebrow='West Palm Beach Auto Transport &middot; Palm Beach County',
    variants={
        'default':    ['West Palm Beach Car Shipping', 'Instant ', 'Quote'],
        'enclosed':   ['Enclosed Car Shipping', 'West Palm Beach · Instant ', 'Quote'],
        'exotic':     ['Exotic & Luxury Car Shipping', 'Instant ', 'Quote'],
        'snowbird':   ['Snowbird Car Shipping', 'West Palm Beach · Instant ', 'Quote'],
        'equestrian': ['Equestrian Season', 'Car Shipping \u00b7 Instant ', 'Quote'],
        'newyork':    ['West Palm Beach to New York', 'Car Shipping · Instant ', 'Quote'],
        'to':         ['Ship Your Car to West Palm Beach', 'Instant ', 'Quote'],
        'from':       ['Ship Your Car from West Palm Beach', 'Instant ', 'Quote'],
    },
    lede=('Ship Guy is a licensed auto transport broker based in Palm Beach County. '
          'We price your route in seconds, then book a vetted, insured carrier to your door. '
          'Open or enclosed, to or from any state.'),
    badges=[
        ('bolt',  'Price on screen in 30 seconds', 'No account and no waiting on a callback'),
        ('truck', 'Pickup in 1&ndash;3 days', 'Interstate 95 and the airport minutes from downtown'),
        ('pin',   'Door to door in Palm Beach County', 'Downtown to Wellington, Jupiter to Boynton Beach'),
    ],
    call_small='West Palm Beach line &middot; Prefer to talk? Call now',
    pq_sub='West Palm Beach pricing in 30 seconds. Free, no obligation.',

    reviews_sub='Trusted by vehicle owners nationwide.',

    lanes_eyebrow='West Palm Beach Lanes &amp; Costs',
    lanes_h2='West Palm Beach Car Shipping Lanes and Estimated Costs',
    lanes_sub='The lanes Palm Beach County households ask about most, with estimated open-transport ranges. Price your exact route above.',
    lanes=[
        ('Fort Myers, FL', 'US-27/I-75 &middot; ~130 mi', 'Same day', '$200&ndash;$310'),
        ('Orlando, FL', 'FL Tpke &middot; ~170 mi', 'Same day', '$210&ndash;$330'),
        ('Tampa, FL', 'I-4/I-75 &middot; ~210 mi', 'Same day', '$230&ndash;$350'),
        ('Jacksonville, FL', 'I-95 &middot; ~280 mi', '1 day', '$260&ndash;$390'),
        ('Atlanta, GA', 'I-95/I-75 &middot; ~600 mi', '2 days', '$450&ndash;$650'),
        ('Charlotte, NC', 'I-95/I-26 &middot; ~680 mi', '2 days', '$490&ndash;$710'),
        ('Washington, DC', 'I-95 &middot; ~980 mi', '3 days', '$700&ndash;$980'),
        ('Philadelphia, PA', 'I-95 &middot; ~1,120 mi', '3 days', '$770&ndash;$1,090'),
        ('New York, NY', 'I-95 &middot; ~1,210 mi', '3&ndash;4 days', '$790&ndash;$1,130'),
        ('Boston, MA', 'I-95 &middot; ~1,420 mi', '4 days', '$890&ndash;$1,240'),
    ],
    lanes_foot=('*2026 estimates for a running sedan on an open trailer. SUVs and trucks run about 10 to 25 percent more, and enclosed more than that. '
                'Season, the equestrian calendar, and carrier availability on your dates set the real quote.'),
    lanes_note=('Interstate 95 north is everything here, and New York, Boston, and Washington all ride it. The season sets the price more than the miles do. '
                'Lanes across the state to Fort Myers and Tampa are quick and inexpensive.'),

    access_eyebrow='Pickup in West Palm Beach',
    access_h2='What Pickup Looks Like Across Palm Beach County',
    access_sub='Carriers run seventy-five-foot rigs. Here is how they reach you in each part of the county.',
    access_cards=[
        ('bridge', 'Palm Beach and the Bridges', 'The Town of Palm Beach limits commercial trucks by size and hour. For an island address, the driver meets you on the mainland side near one of the bridges.'),
        ('tower',  'Downtown and Flagler Drive', 'Downtown towers run on valets and garages, so the handoff happens at a lot nearby. Flagler Drive and the lots by the bridge approaches work well.'),
        ('gate',   'Wellington and the Horse Country', 'Barn roads and show grounds are not built for a car carrier. The handoff happens on Forest Hill Boulevard or at the big centers along State Road 7.'),
        ('home',   'Palm Beach Gardens, Jupiter, and the Suburbs', 'Wide suburban streets mean the truck usually reaches the curb. Gated communities need the name and gate code, and the Acreage meets on a paved road.'),
    ],
    neighborhoods=['Downtown', 'Flagler Drive', 'Northwood', 'El Cid', 'Southend', 'Palm Beach', 'Palm Beach Gardens', 'Jupiter', 'Juno Beach', 'Tequesta', 'Lake Worth Beach',
                   'Lantana', 'Greenacres', 'Wellington', 'Royal Palm Beach', 'Loxahatchee', 'The Acreage', 'Riviera Beach', 'Singer Island', 'Boynton Beach'],
    chips_cap='Serving all of Palm Beach County. Boca Raton and Broward pickups are the same trip.',
    season=('<b>Timing tip.</b> Snowbird season runs November through April, and the equestrian season fills Wellington from January into April. Book two to three weeks ahead in those windows. '
            'Hurricane season runs June through November, and we never send a driver into a storm.'),

    how_h2='Ship Your Car from West Palm Beach in 3 Simple Steps',
    how_sub='From quote to delivery, Ship Guy keeps West Palm Beach car shipping simple, transparent, and insured.',
    how_steps=[
        ('Get Your Instant Quote', 'Enter your ZIPs, vehicle, and timeframe. Your price appears on screen in about 30 seconds.'),
        ('Book and Schedule Pickup', 'We match you with a vetted, insured carrier and confirm a pickup window. Gate codes and bridge details go straight to the driver.'),
        ('Inspect and Deliver', 'The driver inspects the car at pickup and again at delivery. You get updates on the way and sign off at your door.'),
    ],

    why_h2='Why West Palm Beach Ships with Ship Guy',
    why_sub='A licensed, insured brokerage that treats your vehicle, and your time, like it matters.',
    why_support='Real representatives by phone to guide your West Palm Beach shipment.',

    faq_h2='West Palm Beach Car Shipping Questions',
    faq_sub='What Palm Beach County shippers ask before they book.',
    faq=[
        ('How much does it cost to ship a car from West Palm Beach?',
         'Orlando runs about $210 to $330 for a sedan on an open trailer, Fort Myers $200 to $310. New York runs $790 to $1,130, Washington $700 to $980, and Boston $890 to $1,240. '
         'Season, vehicle size, and enclosed transport move the number. Your exact price shows in the quote tool above.'),
        ('How long does car shipping from West Palm Beach take?',
         'Most pickups happen within 1 to 3 days, with the airport and Interstate 95 minutes from downtown. Orlando and Tampa are same-day lanes. '
         'Atlanta takes about two days, and New York three to four.'),
        ('Can the truck deliver to an address on Palm Beach island?',
         'Rarely. The town limits commercial vehicles by size and by hour, and a seventy-five-foot carrier seldom qualifies. The driver meets you on the mainland side near one of the bridges. '
         'When a building has arranged access, we coordinate the hour with the town, so tell us early.'),
        ('Do you ship for the equestrian season in Wellington?',
         'Yes. Riders, trainers, and grooms ship trucks, SUVs, and everyday cars ahead of the season. Wellington carriers are busiest from December through April, so book two to three weeks ahead.'),
        ('When should I book a snowbird car?',
         'Two to three weeks ahead. Southbound demand peaks October through December and northbound demand peaks April through June. '
         'Flexible dates get you a better price and a faster pickup.'),
        ('Should I choose open or enclosed transport in West Palm Beach?',
         'Open transport is the everyday choice, and most seasonal cars ride it up and down the coast. Enclosed transport keeps a car covered against salt air, downpours, and grit. '
         'Many island cars are collector pieces, and enclosed is the norm for them.'),
        ('Is Ship Guy a carrier or a broker?',
         'Ship Guy is a licensed auto transport broker, FMCSA MC #1457715. We do not own trucks. '
         'We book vetted carriers with active insurance, and your car is covered while it is on the truck.'),
        ('What happens after I get my quote?',
         'Your price appears on screen. Book online right there or call <a data-track="call-faq" href="tel:%s">(561) 960-3491</a> to lock in a pickup window. '
         'The driver inspects the car at pickup, and you sign off at delivery.' % TEL),
    ],

    cta_h2='Ready to Ship Your Car to or from West Palm Beach?',
    cta_sub='Get your free West Palm Beach quote in about 30 seconds, or call a real specialist.',
    cta_btn='Get My West Palm Beach Quote',
    cta_trust3='West Palm Beach line, seven days a week',
    foot_tag='Licensed &amp; insured car shipping for Palm Beach County and all 50 states. Transparent pricing, vetted carriers, door to door.',
    foot_serving='Serving Palm Beach County and all 50 states',
)

if __name__ == '__main__':
    out, issues = adspage.build(CFG)
    print('built', out)
    for i in issues: print('  ISSUE', i)
    print('CLEAR' if not issues else '%d issue(s)' % len(issues))
