#!/usr/bin/env python3
"""Google Ads landing page: How Car Shipping Works  ->  /vehicle-quote-how-car-shipping-works
(main line (866) 297-3244). Built from the live /vehicle-quote page by adspage.build()."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import adspage

TEL = '+18662973244'
CFG = dict(
    slug='vehicle-quote-how-car-shipping-works', city='How It Works', st='US', lead_prefix='ADS-HOW',
    tel=TEL, disp='(866) 297-3244', disp_nbsp='(866)&nbsp;297-3244',

    title='How Car Shipping Works, Plus an Instant Quote | Ship Guy',
    meta='See exactly how car shipping works, from the instant quote to the inspection at delivery, then price your route in 30 seconds. Call (866) 297-3244.',

    eyebrow='How Car Shipping Works &middot; Quote to Delivery',
    variants={
        'default':    ['How Car Shipping Works', 'Instant ', 'Quote'],
        'cost':       ['What Car Shipping Costs', 'Instant ', 'Quote'],
        'first':      ['First Time Shipping a Car?', 'Instant ', 'Quote'],
        'process':    ['Car Shipping, Step by Step', 'Instant ', 'Quote'],
        'doortodoor': ['Door-to-Door Car Shipping', 'Instant ', 'Quote'],
    },
    lede=('Ship Guy is a licensed auto transport broker, and here is exactly how shipping works. '
          'We price your route in seconds, then book a vetted, insured carrier to your door. '
          'No guesswork and no surprises.'),
    badges=[
        ('bolt',   'Price on screen in 30 seconds', 'No account and no waiting on a callback'),
        ('doc',    'Inspection report at both ends', 'The Bill of Lading is your record'),
        ('shield', 'Insured on every carrier we book', 'Active cargo insurance, door to door'),
    ],
    pq_sub='See your price in 30 seconds. Free, no obligation.',

    reviews_sub='Trusted by vehicle owners nationwide.',

    table_eyebrow='Timing &amp; Cost',
    table_h2='How Long It Takes and What It Costs',
    table_sub='Transit time and open-transport ranges by distance band. Price your exact route above.',
    table_cols=['Distance', 'Example lane', 'Est. transit', 'Est. open rate*'],
    table_rows=[
        ('Under 500 miles', 'Orlando to Miami, Los Angeles to Phoenix', '1 day', '$170&ndash;$480'),
        ('500 to 1,000 miles', 'Dallas to Atlanta, Chicago to New York', '2 days', '$450&ndash;$820'),
        ('1,000 to 1,500 miles', 'New York to Florida, Seattle to Los Angeles', '3&ndash;4 days', '$700&ndash;$1,250'),
        ('1,500 to 2,500 miles', 'Chicago to Los Angeles', '4 days', '$1,050&ndash;$1,450'),
        ('Coast to coast, 2,500+ miles', 'New York to Los Angeles', '5&ndash;6 days', '$1,200&ndash;$1,700'),
    ],
    table_foot=('*2026 estimates for a running sedan on an open trailer, from our city lane tables. Add 1 to 3 days for pickup. '
                'SUVs and trucks run about 10 to 25 percent more, and enclosed more than that.'),
    table_note=('Distance is the biggest driver of cost, but longer moves cost less per mile. '
                'Season, vehicle size, open or enclosed, and how flexible your dates are set the rest.'),

    cards_eyebrow='Step by Step',
    cards_h2='What Happens at Each Stage',
    cards_sub='From the quote to the handshake at delivery, here is what to expect.',
    cards=[
        ('doc',    'The quote', "Enter your ZIPs, vehicle, and timeframe, and your all-in price appears on screen. It covers pickup, transport, delivery, and the carrier's insurance."),
        ('truck',  'Booking and dispatch', "Lock in the price and a pickup window online or by phone. We assign a licensed, insured carrier that fits the route and send you the driver's details."),
        ('shield', 'Pickup and the inspection report', 'The driver inspects the car with you and notes its condition on the Bill of Lading. That report is your record if anything changes in transit.'),
        ('home',   'Delivery', 'You get updates on the way and meet the truck at delivery. Inspect the car against the report, sign off, and drive away.'),
    ],
    chips=['Wash the car', 'Remove personal items', 'Toll tags out', 'Quarter tank of fuel', 'Date-stamped photos', 'Disable the alarm', 'Keys for the driver',
           'Note leaks or a dead battery', 'An adult to sign at both ends'],
    chips_cap='How to prepare your car before pickup.',
    tip=('<b>Good to know.</b> Open transport uses the same trailers that deliver new cars to dealerships. It is the best value on most routes. '
         'Enclosed adds full cover for classic, luxury, and high-value cars.'),

    how_h2='Ship Your Car in 3 Simple Steps',
    how_sub='From quote to delivery, Ship Guy keeps car shipping simple, transparent, and insured.',
    how_steps=[
        ('Get Your Instant Quote', 'Enter your ZIPs, vehicle, and timeframe. Your price appears on screen in about 30 seconds.'),
        ('Book and Schedule Pickup', 'We match you with a vetted, insured carrier and confirm a pickup window. Gate codes and meeting spots go straight to the driver.'),
        ('Inspect and Deliver', 'The driver inspects the car at pickup and again at delivery. You get updates on the way and sign off at your door.'),
    ],

    why_h2='Why First-Timers Ship with Ship Guy',
    why_sub='A licensed, insured brokerage that treats your vehicle, and your time, like it matters.',
    why_support='Real representatives by phone to walk you through every step.',

    faq_h2='Car Shipping Questions',
    faq_sub='What people ask the first time they ship a car.',
    faq=[
        ('How does car shipping work?',
         'You get a price, book a pickup window, and a vetted carrier collects the car at your address. The driver inspects it with you, hauls it, and delivers it to the destination address. '
         'You inspect it again, sign off, and drive away.'),
        ('How much does it cost to ship a car?',
         'Under 500 miles runs about $170 to $480 for a sedan on an open trailer. Florida to New York runs $780 to $1,150, and coast to coast $1,200 to $1,700. '
         'Vehicle size, season, and enclosed transport move the number. Your exact price shows in the quote tool above.'),
        ('How long does it take?',
         'Pickup usually happens within 1 to 3 days of booking. Under 500 miles takes about a day on the truck. '
         'A thousand to fifteen hundred miles takes 3 to 4 days, and coast to coast 5 to 7.'),
        ('What is the Bill of Lading?',
         'The inspection report the driver fills out with you at pickup and again at delivery. It records the condition of the car at both ends. '
         'That is your record if anything changes in transit. Keep your copy and take date-stamped photos as well.'),
        ('Is my car insured during transport?',
         'Yes. Every carrier we book carries active cargo insurance, so your car is covered on the truck. We share the coverage details before you book.'),
        ('Do I need to be there for pickup and delivery?',
         'An adult needs to be there to inspect the car and sign at both ends. It does not have to be you. Tell us who will meet the truck and we pass it to the driver.'),
        ('How do I prepare the car?',
         'Wash it so existing marks are easy to document. Remove personal items and toll tags, and leave about a quarter tank of fuel. '
         'Disable any alarm and take date-stamped photos. Tell the driver about leaks or a dead battery.'),
        ('Is Ship Guy a carrier or a broker?',
         'Ship Guy is a licensed auto transport broker, FMCSA MC #1457715. We do not own trucks. '
         'We book vetted carriers with active insurance, and your car is covered while it is on the truck.'),
        ('What happens after I get my quote?',
         'Your price appears on screen. Book online right there or call <a data-track="call-faq" href="tel:%s">(866) 297-3244</a> to lock in a pickup window. '
         'The driver inspects the car at pickup, and you sign off at delivery.' % TEL),
    ],

    cta_h2='Ready to See Your Price?',
    cta_sub='Get your free quote in about 30 seconds, or call and a real specialist walks you through it.',
    cta_btn='Get My Free Quote',
    cta_trust3='Real people, seven days a week',
    foot_tag='Licensed &amp; insured car shipping to all 50 states. Transparent pricing, vetted carriers, door to door.',
    foot_serving='Serving all 50 states',
)

if __name__ == '__main__':
    out, issues = adspage.build(CFG)
    print('built', out)
    for i in issues: print('  ISSUE', i)
    print('CLEAR' if not issues else '%d issue(s)' % len(issues))
