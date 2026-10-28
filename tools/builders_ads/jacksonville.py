#!/usr/bin/env python3
"""Google Ads landing page: Jacksonville, FL  ->  /vehicle-quote-jacksonville-florida  (phone line (904) 567-4124).
Built from the live /vehicle-quote page by adspage.build(); rerun after any quote-tool change."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import adspage

TEL = '+19045674124'
CFG = dict(
    slug='vehicle-quote-jacksonville-florida', city='Jacksonville', st='FL', lead_prefix='ADS-JAX',
    tel=TEL, disp='(904) 567-4124', disp_nbsp='(904)&nbsp;567-4124',
    tz='America/New_York', tz_label='ET', hours_open=6, hours_close=23, open_label='6 AM', close_label='11 PM',
    hours_static='Real people, seven days a week, 6 AM to 11 PM ET',

    title='Jacksonville Car Shipping Quote in 30 Seconds | Ship Guy',
    meta='Instant car shipping quote for Jacksonville, FL. Door-to-door auto transport from Riverside to the beaches, open or enclosed, to any state. Call (904) 567-4124.',

    eyebrow='Jacksonville Auto Transport &middot; The First Coast',
    variants={
        'default':  ['Jacksonville Car Shipping', 'Instant ', 'Quote'],
        'enclosed': ['Enclosed Car Shipping', 'Jacksonville · Instant ', 'Quote'],
        'exotic':   ['Exotic & Luxury Car Shipping', 'Jacksonville · Instant ', 'Quote'],
        'military': ['Military Car Shipping', 'Jacksonville · Instant ', 'Quote'],
        'port':     ['JAXPORT Pickup & Delivery', 'Instant ', 'Quote'],
        'snowbird': ['Snowbird Car Shipping', 'Jacksonville \u00b7 Instant ', 'Quote'],
        'newyork':  ['Jacksonville to New York', 'Car Shipping · Instant ', 'Quote'],
        'to':       ['Ship Your Car to Jacksonville', 'Instant ', 'Quote'],
        'from':     ['Ship Your Car from Jacksonville', 'Instant ', 'Quote'],
    },
    lede=('Ship Guy is a licensed auto transport broker with an office on Riverside Avenue. '
          'We price your route in seconds, then book a vetted, insured carrier to your door. '
          'Open or enclosed, to or from any state.'),
    badges=[
        ('bolt',  'Price on screen in 30 seconds', 'No account and no waiting on a callback'),
        ('truck', 'Pickup in 1&ndash;3 days', 'Three interstates bring carriers through the city'),
        ('pin',   'Door to door on the First Coast', 'Riverside to the beaches, Orange Park to Nocatee'),
    ],
    call_small='Jacksonville line &middot; Prefer to talk? Call now',
    pq_sub='Jacksonville pricing in 30 seconds. Free, no obligation.',

    reviews_sub='Trusted by vehicle owners nationwide.',

    lanes_eyebrow='Jacksonville Lanes &amp; Costs',
    lanes_h2='Jacksonville Car Shipping Lanes and Estimated Costs',
    lanes_sub='The lanes First Coast households ask about most, with estimated open-transport ranges. Price your exact route above.',
    lanes=[
        ('Daytona Beach, FL', 'I-95 &middot; ~90 mi', 'Same day', '$170&ndash;$280'),
        ('Orlando, FL', 'I-95/I-4 &middot; ~140 mi', 'Same day', '$180&ndash;$290'),
        ('Savannah, GA', 'I-95 &middot; ~140 mi', 'Same day', '$180&ndash;$290'),
        ('Tallahassee, FL', 'I-10 &middot; ~165 mi', 'Same day', '$220&ndash;$340'),
        ('Tampa, FL', 'I-75/I-10 &middot; ~200 mi', 'Same day', '$220&ndash;$340'),
        ('Charleston, SC', 'I-95/I-26 &middot; ~240 mi', '1 day', '$250&ndash;$380'),
        ('Atlanta, GA', 'I-10/I-75 &middot; ~345 mi', '1 day', '$320&ndash;$470'),
        ('Miami, FL', 'I-95 &middot; ~345 mi', '1 day', '$310&ndash;$450'),
        ('Washington, DC', 'I-95 &middot; ~700 mi', '2 days', '$520&ndash;$750'),
        ('New York, NY', 'I-95 &middot; ~930 mi', '3 days', '$650&ndash;$900'),
    ],
    lanes_foot=('*2026 estimates for a running sedan on an open trailer. SUVs and trucks run about 10 to 25 percent more, and enclosed more than that. '
                'Snowbird season swings the Interstate 95 lanes, and carrier availability on your dates sets the real quote.'),
    lanes_note=('Carriers headed anywhere on the East Coast pass through Jacksonville, which keeps pricing among the best in Florida. '
                'The Northeast lane fills southbound each fall and northbound each spring.'),

    access_eyebrow='Pickup in Jacksonville',
    access_h2='What Pickup Looks Like Across the First Coast',
    access_sub='Carriers run seventy-five-foot rigs. Here is how they reach you on each side of the river.',
    access_cards=[
        ('bridge', 'The Interstates and the Bridges', 'Interstate 95, 10, and 295 reach almost any address in the metro. Rush hour backs up the Fuller Warren and the Buckman, so carriers cross midmorning.'),
        ('tower',  'Riverside, Avondale, and San Marco', 'Brick streets and a low oak canopy keep a trailer out. The driver meets you on Riverside Avenue, San Marco Boulevard, or a main road nearby.'),
        ('gate',   'Mayport, NAS Jacksonville, and Gated Communities', 'Housing at each installation is gated, so the driver meets you outside it. Nocatee, Mandarin, and the Southside have gates too, so send the community name and code.'),
        ('home',   'The Beaches, Orange Park, and the Northside', 'Oceanfront condos run on garages, so the driver meets you on Third Street or by the Intracoastal bridges. Orange Park, Fleming Island, and the Northside are wide and easy.'),
    ],
    neighborhoods=['Downtown', 'Riverside', 'Avondale', 'Ortega', 'San Marco', 'Springfield', 'Mandarin', 'Southside', 'Baymeadows', 'Town Center', 'Arlington', 'Northside',
                   'Westside', 'Orange Park', 'Fleming Island', 'Jacksonville Beach', 'Atlantic Beach', 'Neptune Beach', 'Ponte Vedra', 'Nocatee', 'Fernandina', 'Yulee',
                   'Saint Augustine', 'Middleburg'],
    chips_cap='Serving Duval, Clay, Saint Johns, Nassau, and Baker Counties. Tell us the side of the river and the community name.',
    season=('<b>Timing tip.</b> Navy families move heaviest from May through August, and snowbird cars fill Interstate 95 each fall and spring. Book two to three weeks ahead in those windows. '
            'Hurricane season runs June through November, and no driver is dispatched into an evacuation zone.'),

    how_h2='Ship Your Car from Jacksonville in 3 Simple Steps',
    how_sub='From quote to delivery, Ship Guy keeps Jacksonville car shipping simple, transparent, and insured.',
    how_steps=[
        ('Get Your Instant Quote', 'Enter your ZIPs, vehicle, and timeframe. Your price appears on screen in about 30 seconds.'),
        ('Book and Schedule Pickup', 'We match you with a vetted, insured carrier and confirm a pickup window. Gate codes and the side of the river go straight to the driver.'),
        ('Inspect and Deliver', 'The driver inspects the car at pickup and again at delivery. You get updates on the way and sign off at your door.'),
    ],

    why_h2='Why Jacksonville Ships with Ship Guy',
    why_sub='A licensed, insured brokerage that treats your vehicle, and your time, like it matters.',
    why_support='Real representatives by phone to guide your Jacksonville shipment.',

    faq_h2='Jacksonville Car Shipping Questions',
    faq_sub='What First Coast shippers ask before they book.',
    faq=[
        ('How much does it cost to ship a car from Jacksonville?',
         'Orlando and Savannah run about $180 to $290 for a sedan on an open trailer. Atlanta runs $320 to $470, Miami $310 to $450, and New York $650 to $900. '
         'Season, vehicle size, and enclosed transport move the number. Your exact price shows in the quote tool above.'),
        ('How long does car shipping from Jacksonville take?',
         'Most pickups happen within 1 to 3 days, with three interstates bringing carriers through the city. Orlando, Savannah, Tallahassee, and Daytona Beach are same-day lanes. '
         'Atlanta, Charleston, and Miami take a day, and Washington and New York two to three.'),
        ('Do you handle Navy PCS moves at Mayport and NAS Jacksonville?',
         'Yes, and the heaviest moves land between May and August, so book two to three weeks ahead. Housing at each installation is gated, so the driver meets you outside it. '
         'Many families ship a second vehicle with us, since orders usually cover one car. Ship Guy is a private broker, unaffiliated with any installation.'),
        ('Can you pick up a car at JAXPORT or deliver one for the Puerto Rico sailing?',
         'Yes, once the car has been released. We ship imported cars domestically from the port once they clear customs. For the Puerto Rico sailing, we deliver to the terminal a day or two ahead. '
         'The ocean leg itself is booked separately with the line.'),
        ('Can the truck get into Riverside or the beaches?',
         'Usually not all the way. Riverside, Avondale, and San Marco have brick streets and a low oak canopy. The driver meets you on Riverside Avenue or another main road. '
         'At the beaches, the meeting spot is Third Street or a lot by the Intracoastal bridges.'),
        ('Should I choose open or enclosed transport in Jacksonville?',
         'Open transport is the everyday choice, and most Navy and seasonal cars ride it. Enclosed transport keeps a car covered against salt air, summer storms, and grit. '
         'It is the standard for exotics and anything a collector owns.'),
        ('Is Ship Guy a carrier or a broker?',
         'Ship Guy is a licensed auto transport broker, FMCSA MC #1457715, with an office on Riverside Avenue. We do not own trucks. '
         'We book vetted carriers with active insurance, and your car is covered while it is on the truck.'),
        ('What happens after I get my quote?',
         'Your price appears on screen. Book online right there or call <a data-track="call-faq" href="tel:%s">(904) 567-4124</a> to lock in a pickup window. '
         'The driver inspects the car at pickup, and you sign off at delivery.' % TEL),
    ],

    cta_h2='Ready to Ship Your Car to or from Jacksonville?',
    cta_sub='Get your free Jacksonville quote in about 30 seconds, or call and talk to a real specialist.',
    cta_btn='Get My Jacksonville Quote',
    cta_trust3='Jacksonville line, seven days a week',
    foot_tag='Licensed &amp; insured car shipping for the First Coast and all 50 states. Transparent pricing, vetted carriers, door to door.',
    foot_serving='Serving the First Coast and all 50 states',
)

if __name__ == '__main__':
    out, issues = adspage.build(CFG)
    print('built', out)
    for i in issues: print('  ISSUE', i)
    print('CLEAR' if not issues else '%d issue(s)' % len(issues))
