#!/usr/bin/env python3
"""Google Ads landing page: Florida (state)  ->  /vehicle-quote-florida  (main line (866) 297-3244).
Built from the live /vehicle-quote page by adspage.build(); content follows florida-auto-transport.html.
The old `/vehicle-quote-florida -> /vehicle-quote` redirect was removed from _redirects so this page is served."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import adspage

TEL = '+18662973244'
CFG = dict(
    slug='vehicle-quote-florida', city='Florida', st='FL', lead_prefix='ADS-FL',
    tel=TEL, disp='(866) 297-3244', disp_nbsp='(866)&nbsp;297-3244',

    title='Florida Car Shipping Quote in 30 Seconds | Ship Guy',
    meta='Instant car shipping quote for Florida. Door-to-door auto transport to or from any Florida address, open or enclosed, snowbird both ways. Call (866) 297-3244.',

    eyebrow='Florida Auto Transport &middot; All 67 Counties',
    variants={
        'default':  ['Florida Car Shipping', 'Instant ', 'Quote'],
        'to':       ['Ship Your Car to Florida', 'Instant ', 'Quote'],
        'from':     ['Ship Your Car from Florida', 'Instant ', 'Quote'],
        'snowbird': ['Snowbird Car Shipping', 'Florida · Instant ', 'Quote'],
        'newyork':  ['New York to Florida', 'Car Shipping · Instant ', 'Quote'],
        'midwest':  ['Midwest to Florida', 'Car Shipping · Instant ', 'Quote'],
        'enclosed': ['Enclosed Car Shipping', 'Florida · Instant ', 'Quote'],
        'military': ['Military Car Shipping', 'Florida · Instant ', 'Quote'],
    },
    lede=('Ship Guy is a licensed auto transport broker headquartered in Palm Beach County. '
          'We price your route in seconds, then book a vetted, insured carrier to any Florida door. '
          'Open or enclosed, to or from any state.'),
    badges=[
        ('bolt',  'Price on screen in 30 seconds', 'No account and no waiting on a callback'),
        ('truck', 'Pickup in 1&ndash;3 days in the metros', 'Panhandle interior, Big Bend, and the Keys run 2&ndash;5'),
        ('pin',   'Every Florida region, door to door', 'Pensacola to Key West, Jacksonville to Naples'),
    ],
    pq_sub='Florida pricing in 30 seconds. Free, no obligation.',

    reviews_sub='Trusted by vehicle owners nationwide.',

    lanes_eyebrow='Florida Lanes &amp; Costs',
    lanes_h2='Florida Car Shipping Lanes and Estimated Costs',
    lanes_sub='The lanes Florida households ask about most, shown as ranges from Orlando to Miami. Price your exact route above.',
    lanes=[
        ('Atlanta, GA', 'I-75 &middot; ~440&ndash;660 mi', '1&ndash;2 days', '$400&ndash;$650'),
        ('Charlotte, NC', 'I-95/I-26 &middot; ~520&ndash;730 mi', '2 days', '$430&ndash;$720'),
        ('Nashville, TN', 'I-75/I-24 &middot; ~700&ndash;850 mi', '2 days', '$520&ndash;$880'),
        ('Washington, DC', 'I-95 &middot; ~850&ndash;1,000 mi', '3 days', '$650&ndash;$1,000'),
        ('Houston, TX', 'I-10 &middot; ~970&ndash;1,190 mi', '3 days', '$700&ndash;$1,100'),
        ('Dallas, TX', 'I-10/I-20 &middot; ~1,100&ndash;1,300 mi', '3 days', '$800&ndash;$1,200'),
        ('New York, NY', 'I-95 &middot; ~1,080&ndash;1,280 mi', '3&ndash;4 days', '$760&ndash;$1,150'),
        ('Chicago, IL', 'I-75/I-65 &middot; ~1,150&ndash;1,350 mi', '3&ndash;4 days', '$800&ndash;$1,200'),
        ('Detroit, MI', 'I-75 &middot; ~1,150&ndash;1,330 mi', '3&ndash;4 days', '$800&ndash;$1,200'),
        ('Boston, MA', 'I-95 &middot; ~1,300&ndash;1,500 mi', '4 days', '$850&ndash;$1,250'),
    ],
    lanes_foot=('*2026 estimates for a running sedan on an open trailer, toll roads included. SUVs and trucks run about 10 to 25 percent more, and enclosed more than that. '
                'Season, storm season, and carrier availability on your dates set the real quote.'),
    lanes_note=('The Northeast and Midwest lanes swing with the season, and the Texas lanes hold steady. '
                'Florida-to-Florida moves across the state are quick and inexpensive year round.'),

    access_eyebrow='Pickup Across Florida',
    access_h2='What Pickup Looks Like in Each Region',
    access_sub='Where the car sits in Florida decides the corridor and the carrier pool. Here is how each region loads.',
    access_cards=[
        ('pin',    'South Florida', 'Miami, Fort Lauderdale, Boca Raton, and West Palm Beach run on Interstate 95 and the Turnpike. Condo towers meet at a lot nearby, and gated communities need the name and gate code.'),
        ('truck',  'The Gulf Coast and Central Florida', 'Tampa, Saint Petersburg, Fort Myers, and Naples run on Interstate 75, with the bay bridges open to carriers. Orlando and The Villages sit on the Interstate 4 corridor, where early pickups beat the traffic.'),
        ('bridge', 'The Northeast and the Panhandle', 'Jacksonville is the Interstate 95 gateway, with its port and its bases. The Panhandle runs on Interstate 10 from Pensacola through Tallahassee, and the interior takes a few extra days.'),
        ('home',   'The Keys and the Islands', 'The Keys are one road from Florida City to Key West, and pickups run 2 to 5 days. Barrier islands and beach condos meet on the mainland side or at a lot by the bridge.'),
    ],
    neighborhoods=['Miami', 'Fort Lauderdale', 'Boca Raton', 'West Palm Beach', 'Port Saint Lucie', 'Vero Beach', 'Melbourne', 'Daytona Beach', 'Jacksonville', 'Saint Augustine',
                   'Gainesville', 'Ocala', 'The Villages', 'Orlando', 'Lakeland', 'Tampa', 'Saint Petersburg', 'Sarasota', 'Bradenton', 'Fort Myers', 'Naples', 'Tallahassee',
                   'Pensacola', 'Destin', 'Panama City', 'Key West'],
    chips_cap='Serving all sixty-seven Florida counties. Give us the community name for any gated address, and the building for a beachfront condo.',
    season=('<b>Timing tip.</b> Southbound demand builds from October through December and northbound from April through June. Book two to three weeks ahead in both windows. '
            'Hurricane season runs June through November, and no driver is dispatched into an evacuation zone.'),

    how_h2='Ship Your Car to or from Florida in 3 Simple Steps',
    how_sub='From quote to delivery, Ship Guy keeps Florida car shipping simple, transparent, and insured.',
    how_steps=[
        ('Get Your Instant Quote', 'Enter your ZIPs, vehicle, and timeframe. Your price appears on screen in about 30 seconds.'),
        ('Book and Schedule Pickup', 'We match you with a vetted, insured carrier and confirm a pickup window. Gate codes, condo meeting spots, and base gates go straight to the driver.'),
        ('Inspect and Deliver', 'The driver inspects the car at pickup and again at delivery. You get updates on the way and sign off at your door.'),
    ],

    why_h2='Why Florida Ships with Ship Guy',
    why_sub='A licensed, insured brokerage that treats your vehicle, and your time, like it matters.',
    why_support='Real representatives by phone, from our Palm Beach County home.',

    faq_h2='Florida Car Shipping Questions',
    faq_sub='What Florida shippers ask before they book.',
    faq=[
        ('How much does it cost to ship a car to or from Florida?',
         'Atlanta runs about $400 to $650 for a sedan on an open trailer, and Charlotte $430 to $720. New York runs $760 to $1,150, Chicago and Detroit $800 to $1,200, and Boston $850 to $1,250. '
         'Season, vehicle size, and enclosed transport move the number. Your exact price shows in the quote tool above.'),
        ('How long does car shipping to Florida take?',
         'Most pickups happen within 1 to 3 days in the metros. The Panhandle interior, the Big Bend, and the Keys run 2 to 5 days. '
         'Atlanta is a one-day lane from most of the state. New York and the Midwest run three to four days.'),
        ('When should I book a snowbird car?',
         'Two to three weeks ahead. Southbound cars arrive from October through December and go home from April through June. '
         'The lanes are easy to book even in the peak, because the volume is so large. Flexible dates still get a better price and a faster pickup.'),
        ('What happens if a hurricane is forecast?',
         'Carriers leave the coast days before landfall, and pickups pause until roads reopen. To get a car out ahead of a storm, call as soon as the track firms up. '
         'After a storm, demand jumps as residents replace flooded cars, and a little patience saves money.'),
        ('Do you handle military moves at Florida bases?',
         'Yes. Pensacola, Eglin, Hurlburt, Tyndall, Jacksonville, Mayport, MacDill, Patrick, and Key West all move families on orders. Each has a gate, and the handoff is outside it. '
         'Ship Guy is a private broker with no military affiliation.'),
        ('Are the tolls included?',
         'Yes. The Turnpike, the Orlando toll roads, Alligator Alley, and the bay bridges are built into every quote.'),
        ('Should I choose open or enclosed transport in Florida?',
         'Open transport is the everyday choice, and most seasonal cars ride it up and down the coast. Enclosed transport keeps a car covered against salt air, downpours, and grit. '
         'It is the standard for exotics and anything a collector owns.'),
        ('Is Ship Guy a carrier or a broker?',
         'Ship Guy is a licensed auto transport broker, FMCSA MC #1457715. We do not own trucks. '
         'We book vetted carriers with active insurance, and your car is covered while it is on the truck.'),
        ('What happens after I get my quote?',
         'Your price appears on screen. Book online right there or call <a data-track="call-faq" href="tel:%s">(866) 297-3244</a> to lock in a pickup window. '
         'The driver inspects the car at pickup, and you sign off at delivery.' % TEL),
    ],

    cta_h2='Ready to Ship Your Car to or from Florida?',
    cta_sub='Get your free Florida quote in about 30 seconds, or call and talk to a real specialist.',
    cta_btn='Get My Florida Quote',
    cta_trust3='Real people, seven days a week',
    foot_tag='Licensed &amp; insured car shipping for Florida and all 50 states. Transparent pricing, vetted carriers, door to door.',
    foot_serving='Serving all 67 Florida counties and all 50 states',
)

if __name__ == '__main__':
    out, issues = adspage.build(CFG)
    print('built', out)
    for i in issues: print('  ISSUE', i)
    print('CLEAR' if not issues else '%d issue(s)' % len(issues))
