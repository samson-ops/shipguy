#!/usr/bin/env python3
"""Google Ads landing page: Snowbird Car Shipping  ->  /vehicle-quote-snowbird-car-shipping
(main line (866) 297-3244). Built from the live /vehicle-quote page by adspage.build()."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import adspage

TEL = '+18662973244'
CFG = dict(
    slug='vehicle-quote-snowbird-car-shipping', city='Snowbird', st='US', lead_prefix='ADS-SNOW',
    tel=TEL, disp='(866) 297-3244', disp_nbsp='(866)&nbsp;297-3244',

    title='Snowbird Car Shipping Quote in 30 Seconds | Ship Guy',
    meta='Instant snowbird car shipping quote. Door-to-door seasonal auto transport between the North and Florida, Arizona, and the Sun Belt. Call (866) 297-3244.',

    eyebrow='Snowbird Auto Transport &middot; South in Fall, North in Spring',
    variants={
        'default':  ['Snowbird Car Shipping', 'Instant ', 'Quote'],
        'florida':  ['Snowbird Car Shipping', 'to Florida · Instant ', 'Quote'],
        'arizona':  ['Snowbird Car Shipping', 'to Arizona · Instant ', 'Quote'],
        'north':    ['Heading Home North?', 'Ship Your Car · Instant ', 'Quote'],
        'enclosed': ['Enclosed Snowbird Shipping', 'Instant ', 'Quote'],
        'newyork':  ['New York to Florida', 'Car Shipping · Instant ', 'Quote'],
        'chicago':  ['Chicago to Florida', 'Car Shipping · Instant ', 'Quote'],
    },
    lede=('Ship Guy is a licensed auto transport broker that moves seasonal cars both ways. '
          'We price your route in seconds, then book a vetted, insured carrier to your winter or summer door. '
          'Fly down, and the car follows.'),
    badges=[
        ('bolt',  'Price on screen in 30 seconds', 'No account and no waiting on a callback'),
        ('truck', 'Both directions, every season', 'Florida, Arizona, and the Sun Belt, door to door'),
        ('clock', 'Book 2&ndash;3 weeks ahead in peak', 'October to December south, April to June north'),
    ],
    pq_sub='Snowbird pricing in 30 seconds. Free, no obligation.',

    reviews_sub='Trusted by vehicle owners nationwide.',

    table_eyebrow='Snowbird Lanes &amp; Costs',
    table_h2='Snowbird Lanes and Estimated Costs',
    table_sub='The seasonal lanes we run most, with estimated open-transport ranges outside the peak weeks. Price your exact route above.',
    table_cols=['Lane', 'Corridor &middot; distance', 'Est. transit', 'Est. open rate*'],
    table_rows=[
        ('New York &rarr; South Florida', 'I-95 &middot; ~1,280 mi', '3&ndash;4 days', '$800&ndash;$1,150'),
        ('Boston &rarr; Orlando', 'I-95 &middot; ~1,300 mi', '3&ndash;4 days', '$860&ndash;$1,220'),
        ('Philadelphia &rarr; Orlando', 'I-95 &middot; ~1,000 mi', '3 days', '$700&ndash;$1,000'),
        ('Chicago &rarr; Tampa', 'I-65/I-75 &middot; ~1,170 mi', '3 days', '$800&ndash;$1,150'),
        ('Chicago &rarr; Naples', 'I-65/I-75 &middot; ~1,280 mi', '3&ndash;4 days', '$850&ndash;$1,200'),
        ('Detroit &rarr; Fort Myers', 'I-75 &middot; ~1,290 mi', '3&ndash;4 days', '$850&ndash;$1,200'),
        ('Denver &rarr; Phoenix', 'I-25/I-40 &middot; ~820 mi', '2 days', '$450&ndash;$650'),
        ('Seattle &rarr; Phoenix', 'I-5/US-93 &middot; ~1,420 mi', '3&ndash;4 days', '$900&ndash;$1,300'),
    ],
    table_foot=('*2026 estimates for a running sedan on an open trailer, from our city lane tables. Southbound in October and November and northbound in April and May run higher. '
                'SUVs and trucks add about 10 to 25 percent, and enclosed more.'),
    table_note=('Interstate 95 and Interstate 75 are the busiest snowbird corridors in the country. So many carriers work them that pricing stays competitive despite the distance. '
                'Off-peak weeks can be a real value.'),

    cards_eyebrow='Seasonal Know-How',
    cards_h2='What Snowbirds Should Know Before Booking',
    cards_sub='Four things that make the seasonal move smooth in both directions.',
    cards=[
        ('clock',  'When to book', 'Southbound demand peaks October through December, northbound April through June. Book two to three weeks ahead in those windows, and earlier for a fixed date.'),
        ('truck',  'Fly down, the car follows', 'Fly to your winter home and have the car arrive a few days later. The driver needs an adult there to sign, so tell us who will meet the truck.'),
        ('tower',  'Condo towers and gated communities', 'Valet decks and garages cannot take a carrier, so the driver meets you at a nearby lot. Gated communities need the community name and gate code at booking.'),
        ('shield', 'Open or enclosed', 'Most seasonal cars ride open trailers up and down the coast. Enclosed keeps a collector car covered against salt air, grit, and attention.'),
    ],
    chips=['Miami', 'Fort Lauderdale', 'Boca Raton', 'West Palm Beach', 'Naples', 'Fort Myers', 'Sarasota', 'Tampa', 'Saint Petersburg', 'Orlando', 'The Villages',
           'Jacksonville', 'Phoenix', 'Scottsdale', 'Tucson', 'Palm Springs', 'Las Vegas', 'San Diego', 'Myrtle Beach', 'Hilton Head'],
    chips_cap='Both directions, every season. Northern pickups from New York, New Jersey, New England, Pennsylvania, Ohio, Michigan, Illinois, Minnesota, and the Pacific Northwest.',
    tip=('<b>Timing tip.</b> The same car costs more southbound in November than in July. Flexible dates get you a better price and a faster pickup. '
         'Book the return trip with us too, and the paperwork stays in one place.'),

    how_h2='Ship Your Car South or North in 3 Simple Steps',
    how_sub='From quote to delivery, Ship Guy keeps snowbird car shipping simple, transparent, and insured.',
    how_steps=[
        ('Get Your Instant Quote', 'Enter your ZIPs, vehicle, and timeframe. Your price appears on screen in about 30 seconds.'),
        ('Book and Schedule Pickup', 'We match you with a vetted, insured carrier and confirm a pickup window. Gate codes and condo meeting spots go straight to the driver.'),
        ('Inspect and Deliver', 'The driver inspects the car at pickup and again at delivery. You get updates on the way and sign off at your door.'),
    ],

    why_h2='Why Snowbirds Ship with Ship Guy',
    why_sub='A licensed, insured brokerage that treats your vehicle, and your time, like it matters.',
    why_support='Real representatives by phone to guide your seasonal shipment.',

    faq_h2='Snowbird Car Shipping Questions',
    faq_sub='What seasonal shippers ask before they book.',
    faq=[
        ('How much does snowbird car shipping cost?',
         'New York to South Florida runs about $800 to $1,150 for a sedan, open trailer, off peak. Chicago to Naples runs $850 to $1,200, and Denver to Phoenix $450 to $650. '
         'Peak weeks, vehicle size, and enclosed transport move the number. Your exact price shows in the quote tool above.'),
        ('When should I book my snowbird car?',
         'Two to three weeks ahead, and earlier if your date is fixed. Southbound demand peaks October through December and northbound demand peaks April through June. '
         'Flexible dates get you a better price and a faster pickup.'),
        ('How long does the trip take?',
         'Pickup usually happens within 1 to 3 days, longer in peak weeks with rigid dates. New York to Florida takes 3 to 4 days on the truck, and so does Chicago. '
         'Denver to Phoenix takes about 2.'),
        ('Can I fly down and have the car delivered later?',
         'Yes, and most snowbirds do. Give us the delivery address and the date you land, and we plan the pickup around it. '
         'The driver needs an adult there to sign, so tell us who will meet the truck.'),
        ('Can the truck reach my condo or gated community?',
         'Usually not all the way. Valet decks and garages cannot take a carrier, so the driver meets you at a nearby lot. '
         'Gated communities need the community name and gate code at booking.'),
        ('Open or enclosed for a seasonal car?',
         'Open transport is the everyday choice, and most seasonal cars ride it up and down the coast. Enclosed transport keeps a car covered against salt air, grit, and attention. '
         'It is the standard for exotics and anything a collector owns.'),
        ('Is Ship Guy a carrier or a broker?',
         'Ship Guy is a licensed auto transport broker, FMCSA MC #1457715. We do not own trucks. '
         'We book vetted carriers with active insurance, and your car is covered while it is on the truck.'),
        ('What happens after I get my quote?',
         'Your price appears on screen. Book online right there or call <a data-track="call-faq" href="tel:%s">(866) 297-3244</a> to lock in a pickup window. '
         'The driver inspects the car at pickup, and you sign off at delivery.' % TEL),
    ],

    cta_h2='Ready for the Seasonal Move?',
    cta_sub='Get your free snowbird quote in about 30 seconds, or call and talk to a real specialist.',
    cta_btn='Get My Snowbird Quote',
    cta_trust3='Real people, seven days a week',
    foot_tag='Licensed &amp; insured snowbird car shipping, both directions, all 50 states. Transparent pricing, vetted carriers, door to door.',
    foot_serving='Serving all 50 states',
)

if __name__ == '__main__':
    out, issues = adspage.build(CFG)
    print('built', out)
    for i in issues: print('  ISSUE', i)
    print('CLEAR' if not issues else '%d issue(s)' % len(issues))
