#!/usr/bin/env python3
"""Google Ads landing page: Boca Raton, FL  ->  /vehicle-quote-boca-raton-florida  (phone line (561) 960-3491, shared with
West Palm Beach). Built from the live /vehicle-quote page by adspage.build(); rerun after any quote-tool change."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import adspage

TEL = '+15619603491'
CFG = dict(
    slug='vehicle-quote-boca-raton-florida', city='Boca Raton', st='FL', lead_prefix='ADS-BOCA',
    tel=TEL, disp='(561) 960-3491', disp_nbsp='(561)&nbsp;960-3491',
    tz='America/New_York', tz_label='ET', hours_open=6, hours_close=23, open_label='6 AM', close_label='11 PM',
    hours_static='Real people, seven days a week, 6 AM to 11 PM ET',

    title='Boca Raton Car Shipping Quote in 30 Seconds | Ship Guy',
    meta='Instant car shipping quote for Boca Raton, FL. Door-to-door auto transport from Mizner Park to West Boca, open or enclosed, to any state. Call (561) 960-3491.',

    eyebrow='Boca Raton Auto Transport &middot; South Palm Beach County',
    variants={
        'default':  ['Boca Raton Car Shipping', 'Instant ', 'Quote'],
        'enclosed': ['Enclosed Car Shipping', 'Boca Raton · Instant ', 'Quote'],
        'exotic':   ['Exotic & Luxury Car Shipping', 'Boca Raton · Instant ', 'Quote'],
        'snowbird': ['Snowbird Car Shipping', 'Boca Raton · Instant ', 'Quote'],
        'newyork':  ['Boca Raton to New York', 'Car Shipping · Instant ', 'Quote'],
        'to':       ['Ship Your Car to Boca Raton', 'Instant ', 'Quote'],
        'from':     ['Ship Your Car from Boca Raton', 'Instant ', 'Quote'],
    },
    lede=('Ship Guy is a licensed auto transport broker headquartered in Palm Beach County. '
          'We price your route in seconds, then book a vetted, insured carrier to your door or your gatehouse. '
          'Open or enclosed, to or from any state.'),
    badges=[
        ('bolt',  'Price on screen in 30 seconds', 'No account and no waiting on a callback'),
        ('truck', 'Pickup in 1&ndash;3 days', 'Interstate 95 and the Turnpike both run through town'),
        ('gate',  'Gates settled in advance', 'Give us the community name and gate code at booking'),
    ],
    call_small='Boca Raton line &middot; Prefer to talk? Call now',
    pq_sub='Boca Raton pricing in 30 seconds. Free, no obligation.',

    reviews_sub='Trusted by vehicle owners nationwide.',

    lanes_eyebrow='Boca Raton Lanes &amp; Costs',
    lanes_h2='Boca Raton Car Shipping Lanes and Estimated Costs',
    lanes_sub='The lanes Boca households ask about most, with estimated open-transport ranges. Price your exact route above.',
    lanes=[
        ('Naples, FL', 'I-75 &middot; ~130 mi', 'Same day', '$200&ndash;$310'),
        ('Orlando, FL', 'FL Tpke &middot; ~200 mi', 'Same day', '$220&ndash;$340'),
        ('Tampa, FL', 'I-75 &middot; ~230 mi', 'Same day', '$230&ndash;$350'),
        ('Jacksonville, FL', 'I-95 &middot; ~300 mi', '1 day', '$270&ndash;$400'),
        ('Atlanta, GA', 'I-75 &middot; ~630 mi', '2 days', '$450&ndash;$650'),
        ('Charlotte, NC', 'I-95/I-26 &middot; ~700 mi', '2 days', '$500&ndash;$720'),
        ('Washington, DC', 'I-95 &middot; ~1,000 mi', '3 days', '$700&ndash;$1,000'),
        ('Philadelphia, PA', 'I-95 &middot; ~1,150 mi', '3 days', '$780&ndash;$1,100'),
        ('New York, NY', 'I-95 &middot; ~1,240 mi', '3&ndash;4 days', '$800&ndash;$1,150'),
        ('Boston, MA', 'I-95 &middot; ~1,450 mi', '4 days', '$900&ndash;$1,250'),
    ],
    lanes_foot=('*2026 estimates for a running sedan on an open trailer. SUVs and trucks run about 10 to 25 percent more, and enclosed more than that. '
                'Season and live carrier availability on your dates set the real quote.'),
    lanes_note=('The Northeast lanes swing with the season more than with distance. A car coming south in November costs more than the same car in July. '
                'Florida lanes across the state are quick and inexpensive.'),

    access_eyebrow='Pickup in Boca Raton',
    access_h2='What Pickup Looks Like Across Boca',
    access_sub='Carriers run seventy-five-foot rigs. Here is what the gatehouse, the condo, and the curb each mean for pickup.',
    access_cards=[
        ('gate',  'Country Clubs and Gated Communities', 'Boca West, Broken Sound, and the Polo Club each publish rules for trucks on interior streets. Some admit a carrier with a code and an hour window, and others keep it at the gatehouse.'),
        ('pin',   'Meeting Spots That Work', 'Where the truck cannot enter, you meet the driver outside the gate or at a lot nearby. Town Center, the plazas along Glades Road, and the centers on State Road 7 all work.'),
        ('tower', 'Condos, Valets, and the Intracoastal', 'Valet decks and garages cannot take a carrier, and the older streets east of Federal Highway are tight. Mizner Park and downtown meet at a lot as well.'),
        ('home',  'West Boca, Delray, and Deerfield', 'Wide streets mean the truck usually reaches the curb or the community entrance. Delray Beach, Deerfield Beach, and Parkland load the same way.'),
    ],
    neighborhoods=['Downtown Boca', 'Mizner Park', 'Royal Palm', 'Boca West', 'Broken Sound', 'St. Andrews', 'The Polo Club', 'Woodfield', 'Boca Grove', 'Boca Pointe', 'Boca Isles',
                   'West Boca', 'Boca Del Mar', 'Highland Beach', 'Deerfield Beach', 'Delray Beach', 'Coconut Creek', 'Parkland'],
    chips_cap='Serving Boca Raton and south Palm Beach County. Broward addresses are the same trip.',
    season=('<b>Timing tip.</b> Seasonal residents arrive October through December and head north April through June. Book two to three weeks ahead in those windows, and give us the gate code at booking. '
            'Hurricane season runs June through November, and we never send a driver into a storm.'),

    how_h2='Ship Your Car from Boca Raton in 3 Simple Steps',
    how_sub='From quote to delivery, Ship Guy keeps Boca Raton car shipping simple, transparent, and insured.',
    how_steps=[
        ('Get Your Instant Quote', 'Enter your ZIPs, vehicle, and timeframe. Your price appears on screen in about 30 seconds.'),
        ('Book and Schedule Pickup', 'We match you with a vetted, insured carrier and confirm a pickup window. We confirm gate access with the community before the truck is dispatched.'),
        ('Inspect and Deliver', 'The driver inspects the car at pickup and again at delivery. You get updates on the way and sign off at your door.'),
    ],

    why_h2='Why Boca Raton Ships with Ship Guy',
    why_sub='A licensed, insured brokerage that treats your vehicle, and your time, like it matters.',
    why_support='Real representatives by phone to guide your Boca Raton shipment.',

    faq_h2='Boca Raton Car Shipping Questions',
    faq_sub='What Boca shippers ask before they book.',
    faq=[
        ('How much does it cost to ship a car from Boca Raton?',
         'Orlando runs about $220 to $340 for a sedan on an open trailer, and Naples $200 to $310. New York runs $800 to $1,150, Philadelphia $780 to $1,100, and Boston $900 to $1,250. '
         'Season, vehicle size, and enclosed transport move the number. Your exact price shows in the quote tool above.'),
        ('How long does car shipping from Boca Raton take?',
         'Most pickups happen within 1 to 3 days, with Interstate 95 and the Turnpike close by. Orlando and Tampa are same-day trips. '
         'Atlanta and Charlotte take about two days, and New York three to four.'),
        ('Will the truck get past my gatehouse?',
         'It depends on the community. Some admit a carrier with a code and an hour window, and others keep trucks at the gate. '
         'Give us the community name and gate code when you book, and we confirm access before dispatch.'),
        ('When should I book a snowbird car?',
         'Two to three weeks ahead. Seasonal residents from the Northeast arrive October through December and leave April through June. '
         'Flexible dates get you a better price and a faster pickup.'),
        ('Should I choose open or enclosed transport in Boca Raton?',
         'Open transport is the everyday choice, and most seasonal cars ride it up and down the coast. Enclosed transport keeps a car covered against salt air, downpours, and grit. '
         'It is the standard for exotics and anything a collector owns.'),
        ('Can you deliver to my condo on the Intracoastal?',
         'The driver meets you at a lot nearby, since valet decks and garages cannot take a carrier. Tell us the building and we suggest the spot before dispatch.'),
        ('Is Ship Guy a carrier or a broker?',
         'Ship Guy is a licensed auto transport broker, FMCSA MC #1457715. We do not own trucks. '
         'We book vetted carriers with active insurance, and your car is covered while it is on the truck.'),
        ('What happens after I get my quote?',
         'Your price appears on screen. Book online right there or call <a data-track="call-faq" href="tel:%s">(561) 960-3491</a> to lock in a pickup window. '
         'The driver inspects the car at pickup, and you sign off at delivery.' % TEL),
    ],

    cta_h2='Ready to Ship Your Car to or from Boca Raton?',
    cta_sub='Get your free Boca Raton quote in about 30 seconds, or call and talk to a real specialist.',
    cta_btn='Get My Boca Raton Quote',
    cta_trust3='Boca Raton line, seven days a week',
    foot_tag='Licensed &amp; insured car shipping for Boca Raton and all 50 states. Transparent pricing, vetted carriers, door to door.',
    foot_serving='Serving Boca Raton and all 50 states',
)

if __name__ == '__main__':
    out, issues = adspage.build(CFG)
    print('built', out)
    for i in issues: print('  ISSUE', i)
    print('CLEAR' if not issues else '%d issue(s)' % len(issues))
