#!/usr/bin/env python3
"""Google Ads landing page: Naples, FL  ->  /vehicle-quote-naples-florida  (phone line (239) 388-5753).
Built from the live /vehicle-quote page by adspage.build(); rerun after any quote-tool change."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import adspage

TEL = '+12393885753'
CFG = dict(
    slug='vehicle-quote-naples-florida', city='Naples', st='FL', lead_prefix='ADS-NAP',
    tel=TEL, disp='(239) 388-5753', disp_nbsp='(239)&nbsp;388-5753',
    tz='America/New_York', tz_label='ET', hours_open=6, hours_close=23, open_label='6 AM', close_label='11 PM',
    hours_static='Real people, seven days a week, 6 AM to 11 PM ET',

    title='Naples Car Shipping Quote in 30 Seconds | Ship Guy',
    meta='Instant car shipping quote for Naples, FL. Door-to-door auto transport from Old Naples to Golden Gate, open or enclosed, to any state. Call (239) 388-5753.',

    eyebrow='Naples Auto Transport &middot; Collier County',
    variants={
        'default':  ['Naples Car Shipping', 'Instant ', 'Quote'],
        'enclosed': ['Enclosed Car Shipping', 'Naples · Instant ', 'Quote'],
        'exotic':   ['Exotic & Luxury Car Shipping', 'Naples · Instant ', 'Quote'],
        'snowbird': ['Snowbird Car Shipping', 'Naples · Instant ', 'Quote'],
        'midwest':  ['Midwest to Naples', 'Car Shipping · Instant ', 'Quote'],
        'chicago':  ['Chicago to Naples', 'Car Shipping · Instant ', 'Quote'],
        'detroit':  ['Detroit to Naples', 'Car Shipping · Instant ', 'Quote'],
        'to':       ['Ship Your Car to Naples', 'Instant ', 'Quote'],
        'from':     ['Ship Your Car from Naples', 'Instant ', 'Quote'],
    },
    lede=('Ship Guy is a licensed auto transport broker with South Florida as home. '
          'We price your route in seconds, then book a vetted, insured carrier to your door or your gatehouse. '
          'Open or enclosed, to or from any state.'),
    badges=[
        ('bolt',  'Price on screen in 30 seconds', 'No account and no waiting on a callback'),
        ('truck', 'Pickup in 1&ndash;3 days', 'Interstate 75 and the Alley bring carriers through'),
        ('gate',  'Gates settled in advance', 'Give us the community name and gate code at booking'),
    ],
    call_small='Naples line &middot; Prefer to talk? Call now',
    pq_sub='Naples pricing in 30 seconds. Free, no obligation.',

    reviews_sub='Trusted by vehicle owners nationwide.',

    lanes_eyebrow='Naples Lanes &amp; Costs',
    lanes_h2='Naples Car Shipping Lanes and Estimated Costs',
    lanes_sub='The lanes Naples households ask about most, with estimated open-transport ranges. Price your exact route above.',
    lanes=[
        ('Fort Lauderdale, FL', 'I-75 Alley &middot; ~110 mi', 'Same day', '$180&ndash;$290'),
        ('Miami, FL', 'I-75 Alley &middot; ~125 mi', 'Same day', '$180&ndash;$290'),
        ('Tampa, FL', 'I-75 &middot; ~170 mi', 'Same day', '$220&ndash;$340'),
        ('Orlando, FL', 'I-75/FL Tpke &middot; ~230 mi', '1 day', '$230&ndash;$350'),
        ('Jacksonville, FL', 'I-75/I-10 &middot; ~340 mi', '1 day', '$310&ndash;$450'),
        ('Atlanta, GA', 'I-75 &middot; ~600 mi', '2 days', '$450&ndash;$650'),
        ('Nashville, TN', 'I-75/I-24 &middot; ~850 mi', '2&ndash;3 days', '$600&ndash;$880'),
        ('Columbus, OH', 'I-75/I-71 &middot; ~1,040 mi', '3 days', '$750&ndash;$1,050'),
        ('Chicago, IL', 'I-75/I-65 &middot; ~1,280 mi', '3&ndash;4 days', '$850&ndash;$1,200'),
        ('Detroit, MI', 'I-75 &middot; ~1,330 mi', '3&ndash;4 days', '$850&ndash;$1,200'),
    ],
    lanes_foot=('*2026 estimates for a running sedan on an open trailer, with the Alley toll included. SUVs and trucks run about 10 to 25 percent more, and enclosed more than that. '
                'The season swing and carrier availability on your dates set the real quote.'),
    lanes_note=('Interstate 75 north is the workhorse, carrying Atlanta, Ohio, Chicago, and Detroit. The season sets the price more than the miles. '
                'Because the Midwest volume is so large, those lanes are easy to book even in peak.'),

    access_eyebrow='Pickup in Naples',
    access_h2='What Pickup Looks Like Across Collier County',
    access_sub='Carriers run seventy-five-foot rigs. Here is what the gatehouse, the old streets, and the acreage each mean for pickup.',
    access_cards=[
        ('gate',  'Golf Communities and Country Clubs', 'Pelican Bay, Grey Oaks, Quail West, and Mediterra each set their own rules for commercial trucks. Some admit a carrier with a code and a time window, and others hold trucks at the gatehouse.'),
        ('pin',   'Meeting Spots That Work', 'Where the truck cannot enter, the handoff moves to just outside the gate or a lot nearby. Waterside, Mercato, and the plazas along Pine Ridge Road all work.'),
        ('tower', 'Old Naples, Port Royal, and the Beach', 'Port Royal, Aqualane Shores, and Old Naples are ungated but narrow, with low canopy and tight parking. The handoff there happens on Tamiami Trail or at a lot.'),
        ('home',  'Golden Gate Estates, Marco Island, and the Acreage', 'East of Collier Boulevard, long drives mean the driver meets you on a paved road. Marco Island condos meet near the bridge approach.'),
    ],
    neighborhoods=['Old Naples', 'Port Royal', 'Aqualane Shores', 'Park Shore', 'Pelican Bay', 'Grey Oaks', 'Tiburon', 'Mediterra', 'Quail West', 'Vineyards', 'Golden Gate',
                   'Golden Gate Estates', 'Lely', 'Marco Island', 'Isles of Capri', 'Ave Maria', 'Immokalee'],
    chips_cap='Serving Naples and all of Collier County. Bonita Springs and Estero are the same trip.',
    season=('<b>Timing tip.</b> Seasonal residents arrive from the upper Midwest starting in November and peak in January and February. They leave from April into May, so book two to three weeks ahead in those windows. '
            'Hurricane season runs June through November, and we never send a driver into a storm.'),

    how_h2='Ship Your Car from Naples in 3 Simple Steps',
    how_sub='From quote to delivery, Ship Guy keeps Naples car shipping simple, transparent, and insured.',
    how_steps=[
        ('Get Your Instant Quote', 'Enter your ZIPs, vehicle, and timeframe. Your price appears on screen in about 30 seconds.'),
        ('Book and Schedule Pickup', 'We match you with a vetted, insured carrier and confirm a pickup window. We confirm gate access with the community before the truck is dispatched.'),
        ('Inspect and Deliver', 'The driver inspects the car at pickup and again at delivery. You get updates on the way and sign off at your door.'),
    ],

    why_h2='Why Naples Ships with Ship Guy',
    why_sub='A licensed, insured brokerage that treats your vehicle, and your time, like it matters.',
    why_support='Real representatives by phone to guide your Naples shipment.',

    faq_h2='Naples Car Shipping Questions',
    faq_sub='What Naples shippers ask before they book.',
    faq=[
        ('How much does it cost to ship a car from Naples?',
         'Fort Lauderdale and Miami run about $180 to $290 for a sedan on an open trailer. Chicago and Detroit run $850 to $1,200, Atlanta $450 to $650, and Columbus $750 to $1,050. '
         'Season, vehicle size, and enclosed transport move the number. Your exact price shows in the quote tool above.'),
        ('How long does car shipping from Naples take?',
         'Most pickups happen within 1 to 3 days, with Interstate 75 and the Alley bringing carriers through. Fort Lauderdale, Miami, and Tampa are same-day lanes. '
         'Atlanta takes about two days, and Chicago and Detroit three to four.'),
        ('Will the truck get past my gatehouse?',
         'It depends on the community. Some admit a carrier with a code and a time window, and others hold trucks at the gatehouse. '
         'Give us the community name and gate code when you book, and we confirm access before dispatch.'),
        ('When should I book a seasonal car to Naples?',
         'Two to three weeks ahead in season. Arrivals from the upper Midwest start in November and peak in January and February. Departures run from April into May. '
         'Flexible dates get you a better price and a faster pickup.'),
        ('Should I choose open or enclosed transport in Naples?',
         'Open transport is the everyday choice, and most seasonal cars ride it down Interstate 75. Enclosed transport keeps a car covered against salt air, downpours, and grit. '
         'Many of the cars behind the gates are collector pieces, and enclosed is the norm for them.'),
        ('Is the Alligator Alley toll included?',
         'Yes. The toll is built into every quote. Carriers cross the Alley to Fort Lauderdale and Miami in under two hours.'),
        ('Is Ship Guy a carrier or a broker?',
         'Ship Guy is a licensed auto transport broker, FMCSA MC #1457715. We do not own trucks. '
         'We book vetted carriers with active insurance, and your car is covered while it is on the truck.'),
        ('What happens after I get my quote?',
         'Your price appears on screen. Book online right there or call <a data-track="call-faq" href="tel:%s">(239) 388-5753</a> to lock in a pickup window. '
         'The driver inspects the car at pickup, and you sign off at delivery.' % TEL),
    ],

    cta_h2='Ready to Ship Your Car to or from Naples?',
    cta_sub='Get your free Naples quote in about 30 seconds, or call and talk to a real specialist.',
    cta_btn='Get My Naples Quote',
    cta_trust3='Naples line, seven days a week',
    foot_tag='Licensed &amp; insured car shipping for Collier County and all 50 states. Transparent pricing, vetted carriers, door to door.',
    foot_serving='Serving Collier County and all 50 states',
)

if __name__ == '__main__':
    out, issues = adspage.build(CFG)
    print('built', out)
    for i in issues: print('  ISSUE', i)
    print('CLEAR' if not issues else '%d issue(s)' % len(issues))
