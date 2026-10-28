#!/usr/bin/env python3
"""Google Ads landing page: Fort Lauderdale, FL  ->  /vehicle-quote-fort-lauderdale-florida  (phone line (954) 866-9281).
Built from the live /vehicle-quote page by adspage.build(); rerun after any quote-tool change.
No city page exists for Fort Lauderdale, so the lane figures interpolate the Miami, Boca Raton and Naples tables."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import adspage

TEL = '+19548669281'
CFG = dict(
    slug='vehicle-quote-fort-lauderdale-florida', city='Fort Lauderdale', st='FL', lead_prefix='ADS-FLL',
    tel=TEL, disp='(954) 866-9281', disp_nbsp='(954)&nbsp;866-9281',
    tz='America/New_York', tz_label='ET', hours_open=6, hours_close=23, open_label='6 AM', close_label='11 PM',
    hours_static='Real people, seven days a week, 6 AM to 11 PM ET',

    title='Fort Lauderdale Car Shipping Quote in 30 Seconds | Ship Guy',
    meta='Instant car shipping quote for Fort Lauderdale, FL. Door-to-door auto transport from Las Olas to Weston, open or enclosed, to any state. Call (954) 866-9281.',

    eyebrow='Fort Lauderdale Auto Transport &middot; Broward County',
    variants={
        'default':  ['Fort Lauderdale Car Shipping', 'Instant ', 'Quote'],
        'enclosed': ['Enclosed Car Shipping', 'Fort Lauderdale · Instant ', 'Quote'],
        'exotic':   ['Exotic & Luxury Car Shipping', 'Instant ', 'Quote'],
        'snowbird': ['Snowbird Car Shipping', 'Fort Lauderdale · Instant ', 'Quote'],
        'newyork':  ['Fort Lauderdale to New York', 'Car Shipping · Instant ', 'Quote'],
        'to':       ['Ship Your Car to Fort Lauderdale', 'Instant ', 'Quote'],
        'from':     ['Ship Your Car from Fort Lauderdale', 'Instant ', 'Quote'],
    },
    lede=('Ship Guy is a licensed auto transport broker serving Fort Lauderdale and all of Broward County. '
          'We price your route in seconds, then book a vetted, insured carrier to your door. '
          'Open or enclosed, to or from any state.'),
    badges=[
        ('bolt',  'Price on screen in 30 seconds', 'No account and no waiting on a callback'),
        ('truck', 'Pickup in 1&ndash;3 days', 'On most Broward routes, longer in peak season'),
        ('pin',   'Door to door across Broward', 'Las Olas to Weston, Pompano to Hollywood'),
    ],
    call_small='Fort Lauderdale line &middot; Prefer to talk? Call now',
    pq_sub='Fort Lauderdale pricing in 30 seconds. Free, no obligation.',

    reviews_sub='Trusted by vehicle owners nationwide.',

    lanes_eyebrow='Fort Lauderdale Lanes &amp; Costs',
    lanes_h2='Fort Lauderdale Car Shipping Lanes and Estimated Costs',
    lanes_sub='The lanes Broward households ask about most, with estimated open-transport ranges. Price your exact route above.',
    lanes=[
        ('Naples, FL', 'I-75 Alley &middot; ~110 mi', 'Same day', '$180&ndash;$290'),
        ('Orlando, FL', 'FL Tpke &middot; ~210 mi', 'Same day', '$220&ndash;$340'),
        ('Tampa, FL', 'I-75 &middot; ~260 mi', 'Same day', '$240&ndash;$360'),
        ('Jacksonville, FL', 'I-95 &middot; ~320 mi', '1 day', '$280&ndash;$410'),
        ('Atlanta, GA', 'I-75 &middot; ~650 mi', '1&ndash;2 days', '$450&ndash;$650'),
        ('Charlotte, NC', 'I-95/I-26 &middot; ~720 mi', '2 days', '$500&ndash;$720'),
        ('Washington, DC', 'I-95 &middot; ~1,030 mi', '2&ndash;3 days', '$700&ndash;$980'),
        ('New York, NY', 'I-95 &middot; ~1,260 mi', '3&ndash;4 days', '$800&ndash;$1,150'),
        ('Chicago, IL', 'I-75/I-65 &middot; ~1,360 mi', '3&ndash;4 days', '$850&ndash;$1,200'),
        ('Boston, MA', 'I-95 &middot; ~1,480 mi', '4 days', '$900&ndash;$1,250'),
    ],
    lanes_foot=('*2026 estimates for a running sedan on an open trailer. SUVs and trucks run about 10 to 25 percent more, and enclosed more than that. '
                'Season and live carrier availability on your dates set the real quote.'),
    lanes_note=('Interstate 95 to the New York area is the lane that fills Fort Lauderdale each fall. So many carriers work it that pricing stays competitive despite the distance. '
                'Across the Alley, Naples is a same-day run.'),

    access_eyebrow='Pickup in Fort Lauderdale',
    access_h2='What Pickup Looks Like Across Broward',
    access_sub='Carriers run seventy-five-foot rigs. Here is how they reach you in each part of the county.',
    access_cards=[
        ('bridge', 'The Barrier Island and the Drawbridges', 'Las Olas, the beach, and the Galt Ocean Mile sit across drawbridges on narrow streets. The driver meets you on the mainland side or at a lot by the causeway.'),
        ('tower',  'Downtown Towers and Condos', 'Valet decks and underground garages cannot take a carrier. Downtown, Victoria Park, and the beach condos meet at a nearby surface lot.'),
        ('gate',   'Weston, Parkland, and the Gated West', 'Weston, Parkland, and the communities along the Sawgrass set their own truck rules. Share the community name and gate code when you book.'),
        ('home',   'Plantation, Davie, and the Suburbs', 'Wide suburban streets mean the truck usually reaches the curb. Pembroke Pines, Coral Springs, and Pompano Beach load the same way.'),
    ],
    neighborhoods=['Downtown', 'Las Olas', 'Victoria Park', 'Rio Vista', 'Harbor Beach', 'Coral Ridge', 'Galt Ocean Mile', 'Wilton Manors', 'Oakland Park', 'Lauderdale-by-the-Sea',
                   'Pompano Beach', 'Deerfield Beach', 'Hollywood', 'Hallandale Beach', 'Dania Beach', 'Davie', 'Plantation', 'Sunrise', 'Weston', 'Pembroke Pines', 'Miramar',
                   'Coral Springs', 'Parkland', 'Cooper City'],
    chips_cap='Serving all of Broward County. Miami-Dade and Palm Beach pickups are the same trip.',
    season=('<b>Timing tip.</b> Snowbird season runs November through April, and the boat show fills the beach for a week each fall. Book two to three weeks ahead in those windows. '
            'Hurricane season runs June through November, and we never send a driver into a storm.'),

    how_h2='Ship Your Car from Fort Lauderdale in 3 Simple Steps',
    how_sub='From quote to delivery, Ship Guy keeps Fort Lauderdale car shipping simple, transparent, and insured.',
    how_steps=[
        ('Get Your Instant Quote', 'Enter your ZIPs, vehicle, and timeframe. Your price appears on screen in about 30 seconds.'),
        ('Book and Schedule Pickup', 'We match you with a vetted, insured carrier and confirm a pickup window. Gate codes and bridge details go straight to the driver.'),
        ('Inspect and Deliver', 'The driver inspects the car at pickup and again at delivery. You get updates on the way and sign off at your door.'),
    ],

    why_h2='Why Fort Lauderdale Ships with Ship Guy',
    why_sub='A licensed, insured brokerage that treats your vehicle, and your time, like it matters.',
    why_support='Real representatives by phone to guide your Fort Lauderdale shipment.',

    faq_h2='Fort Lauderdale Car Shipping Questions',
    faq_sub='What Broward shippers ask before they book.',
    faq=[
        ('How much does it cost to ship a car from Fort Lauderdale?',
         'Naples runs about $180 to $290 for a sedan on an open trailer, and Orlando $220 to $340. New York runs $800 to $1,150, Chicago $850 to $1,200, and Boston $900 to $1,250. '
         'Season, vehicle size, and enclosed transport move the number. Your exact price shows in the quote tool above.'),
        ('How long does car shipping from Fort Lauderdale take?',
         'Most pickups happen within 1 to 3 days, longer in peak season if your dates are rigid. Naples, Orlando, and Tampa are same-day lanes. '
         'Atlanta takes a day or two, and New York three to four.'),
        ('Can the truck reach my condo on the beach or Las Olas?',
         'Usually not. Valet decks and garages cannot take a carrier, and the barrier island streets are narrow. '
         'The driver meets you on the mainland side of the bridge or at a lot by the causeway.'),
        ('When should I book a snowbird car?',
         'Two to three weeks ahead. Southbound demand peaks October through December and northbound demand peaks April through June. '
         'Flexible dates get you a better price and a faster pickup.'),
        ('Should I choose open or enclosed transport in Fort Lauderdale?',
         'Open transport is the everyday choice, and most seasonal cars ride it up and down the coast. Enclosed transport keeps a car covered against salt air, downpours, and grit. '
         'It is the standard for exotics and anything a collector owns.'),
        ('Can you pick up a car at Port Everglades or the airport?',
         'Yes, once the car has been released to you. An imported car ships domestically once it clears customs, and we do not arrange the ocean leg. '
         'Fly in, and the car can arrive at your door a few days later.'),
        ('Is Ship Guy a carrier or a broker?',
         'Ship Guy is a licensed auto transport broker, FMCSA MC #1457715. We do not own trucks. '
         'We book vetted carriers with active insurance, and your car is covered while it is on the truck.'),
        ('What happens after I get my quote?',
         'Your price appears on screen. Book online right there or call <a data-track="call-faq" href="tel:%s">(954) 866-9281</a> to lock in a pickup window. '
         'The driver inspects the car at pickup, and you sign off at delivery.' % TEL),
    ],

    cta_h2='Ready to Ship Your Car to or from Fort Lauderdale?',
    cta_sub='Get your free Fort Lauderdale quote in about 30 seconds, or call and talk to a real specialist.',
    cta_btn='Get My Fort Lauderdale Quote',
    cta_trust3='Fort Lauderdale line, seven days a week',
    foot_tag='Licensed &amp; insured car shipping for Broward County and all 50 states. Transparent pricing, vetted carriers, door to door.',
    foot_serving='Serving Broward County and all 50 states',
)

if __name__ == '__main__':
    out, issues = adspage.build(CFG)
    print('built', out)
    for i in issues: print('  ISSUE', i)
    print('CLEAR' if not issues else '%d issue(s)' % len(issues))
