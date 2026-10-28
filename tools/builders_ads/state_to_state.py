#!/usr/bin/env python3
"""Google Ads landing page: State-to-State Auto Transport  ->  /vehicle-quote-state-to-state-car-shipping
(main line (866) 297-3244). Built from the live /vehicle-quote page by adspage.build()."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import adspage

TEL = '+18662973244'
CFG = dict(
    slug='vehicle-quote-state-to-state-car-shipping', city='State to State', st='US', lead_prefix='ADS-S2S',
    tel=TEL, disp='(866) 297-3244', disp_nbsp='(866)&nbsp;297-3244',

    title='State-to-State Car Shipping Quote in 30 Seconds | Ship Guy',
    meta='Instant state-to-state car shipping quote. Door-to-door auto transport between any two states, open or enclosed, insured carriers. Call (866) 297-3244.',

    eyebrow='State-to-State Auto Transport &middot; All 50 States',
    variants={
        'default':    ['State-to-State Car Shipping', 'Instant ', 'Quote'],
        'interstate': ['Interstate Auto Transport', 'Instant ', 'Quote'],
        'crosscountry': ['Cross-Country Car Shipping', 'Instant ', 'Quote'],
        'relocation': ['Moving Out of State?', 'Ship Your Car · Instant ', 'Quote'],
        'dealer':     ['Bought a Car Out of State?', 'Ship It Home · Instant ', 'Quote'],
        'enclosed':   ['Enclosed State-to-State Shipping', 'Instant ', 'Quote'],
    },
    lede=('Ship Guy is a licensed auto transport broker covering all 50 states. '
          'We price your route in seconds, then book a vetted, insured carrier door to door. '
          'Open or enclosed, any distance.'),
    badges=[
        ('bolt',   'Price on screen in 30 seconds', 'No account and no waiting on a callback'),
        ('truck',  'Any two states, door to door', 'Neighboring states in 1&ndash;3 days, coast to coast in 5&ndash;7'),
        ('shield', 'Insured on every mile', 'Active cargo insurance on every carrier we book'),
    ],
    pq_sub='State-to-state pricing in 30 seconds. Free, no obligation.',

    reviews_sub='Trusted by vehicle owners nationwide.',

    table_eyebrow='Popular Lanes &amp; Costs',
    table_h2='State-to-State Lanes and Estimated Costs',
    table_sub='The interstate lanes people ask about most, with estimated open-transport ranges. Price your exact route above.',
    table_cols=['Lane', 'Corridor &middot; distance', 'Est. transit', 'Est. open rate*'],
    table_rows=[
        ('Georgia &harr; Florida', 'I-75 &middot; ~350&ndash;660 mi', '1&ndash;2 days', '$320&ndash;$650'),
        ('Texas &harr; Georgia', 'I-20 &middot; ~780 mi', '2 days', '$550&ndash;$800'),
        ('Illinois &harr; New York', 'I-80 &middot; ~790 mi', '2 days', '$560&ndash;$820'),
        ('Colorado &harr; Arizona', 'I-25/I-40 &middot; ~820 mi', '2 days', '$450&ndash;$650'),
        ('Washington &harr; California', 'I-5 &middot; ~1,135 mi', '3 days', '$800&ndash;$1,150'),
        ('New York &harr; Florida', 'I-95 &middot; ~1,100&ndash;1,300 mi', '3&ndash;4 days', '$780&ndash;$1,150'),
        ('Illinois &harr; Florida', 'I-65/I-75 &middot; ~1,170&ndash;1,380 mi', '3&ndash;4 days', '$800&ndash;$1,200'),
        ('Texas &harr; California', 'I-20/I-10 &middot; ~1,435 mi', '3 days', '$900&ndash;$1,250'),
        ('Illinois &harr; California', 'I-40/I-55 &middot; ~2,015 mi', '4 days', '$1,050&ndash;$1,450'),
        ('New York &harr; California', 'I-40/I-70 &middot; ~2,790 mi', '5&ndash;6 days', '$1,200&ndash;$1,700'),
    ],
    table_foot=('*2026 estimates for a running sedan on an open trailer, from our city lane tables. SUVs and trucks run about 10 to 25 percent more, and enclosed more than that. '
                'Season and live carrier availability on your dates set the real quote.'),
    table_note=('Longer moves cost more in total but less per mile. A cross-country shipment can work out to well under a dollar a mile. '
                'A short hop costs more per mile, since the carrier still has fixed costs.'),

    cards_eyebrow='What You Get',
    cards_h2='What State-to-State Shipping Includes',
    cards_sub='Every interstate move with Ship Guy comes with the same four things.',
    cards=[
        ('truck',  'Door to door between any two states', 'The carrier picks up at your address and delivers to the new one. Where a seventy-five-foot rig cannot turn, the driver meets you at a lot nearby.'),
        ('clock',  'Timing by distance', 'A neighboring state takes 1 to 3 days on the truck. Coast to coast usually runs 5 to 7 days, plus 1 to 3 days for pickup.'),
        ('shield', 'Insured on every mile', 'Every carrier we book carries active cargo insurance, so your car is covered on the truck. The inspection report at pickup and delivery is your record.'),
        ('doc',    'One all-in price', "Your quote covers pickup, transport, delivery, and the carrier's insurance. There are no hidden fees or surprise charges at delivery."),
    ],
    chips=['Florida', 'Texas', 'California', 'New York', 'Georgia', 'Arizona', 'Illinois', 'North Carolina', 'Colorado', 'Washington', 'Pennsylvania', 'Ohio',
           'Michigan', 'Massachusetts', 'New Jersey', 'Virginia', 'Tennessee', 'Nevada', 'South Carolina', 'Minnesota'],
    chips_cap='All 50 states, with local pages for 167 metros.',
    tip=('<b>Timing tip.</b> Summer and the snowbird peaks are the busiest and priciest windows. A flexible pickup window of a few days lets carriers slot your car into a full load. '
         'That lowers the price.'),

    how_h2='Ship Your Car State to State in 3 Simple Steps',
    how_sub='From quote to delivery, Ship Guy keeps interstate car shipping simple, transparent, and insured.',
    how_steps=[
        ('Get Your Instant Quote', 'Enter your ZIPs, vehicle, and timeframe. Your price appears on screen in about 30 seconds.'),
        ('Book and Schedule Pickup', 'We match you with a vetted, insured carrier and confirm a pickup window. Gate codes and meeting spots go straight to the driver.'),
        ('Inspect and Deliver', 'The driver inspects the car at pickup and again at delivery. You get updates on the way and sign off at your door.'),
    ],

    why_h2='Why Ship State to State with Ship Guy',
    why_sub='A licensed, insured brokerage that treats your vehicle, and your time, like it matters.',
    why_support='Real representatives by phone to guide your interstate shipment.',

    faq_h2='State-to-State Car Shipping Questions',
    faq_sub='What people ask before they ship a car to another state.',
    faq=[
        ('How much does state-to-state car shipping cost?',
         'A neighboring-state move runs about $320 to $650 for a sedan on an open trailer. Florida to New York runs $780 to $1,150, and coast to coast $1,200 to $1,700. '
         'Vehicle size, season, and enclosed transport move the number. Your exact price shows in the quote tool above.'),
        ('How long does it take?',
         'Pickup usually happens within 1 to 3 days of booking. A neighboring state takes 1 to 3 days on the truck. '
         'Florida to New York runs 3 to 4 days, and coast to coast 5 to 7.'),
        ('I bought a car in another state. Can you bring it home?',
         "Yes. We pick up from dealers, auctions, and private sellers. Give us the seller's contact and the release details, and we coordinate the handoff."),
        ('Is my car insured across state lines?',
         'Yes. Every carrier we book carries active cargo insurance, so your car is covered on the truck. The inspection report at pickup and delivery documents its condition.'),
        ('Open or enclosed for a long interstate move?',
         'Open transport is the everyday choice and the best value on any distance. Enclosed transport keeps a car covered against weather, road grit, and attention. '
         'It is the standard for exotics and anything a collector owns.'),
        ('Can I pack things in the car?',
         'Carriers are licensed to move vehicles, not household goods, so belongings are not covered in transit. Keep the car empty apart from the usual items in the trunk and glovebox.'),
        ('Is Ship Guy a carrier or a broker?',
         'Ship Guy is a licensed auto transport broker, FMCSA MC #1457715. We do not own trucks. '
         'We book vetted carriers with active insurance, and your car is covered while it is on the truck.'),
        ('What happens after I get my quote?',
         'Your price appears on screen. Book online right there or call <a data-track="call-faq" href="tel:%s">(866) 297-3244</a> to lock in a pickup window. '
         'The driver inspects the car at pickup, and you sign off at delivery.' % TEL),
    ],

    cta_h2='Ready to Ship Your Car to Another State?',
    cta_sub='Get your free state-to-state quote in about 30 seconds, or call and talk to a real specialist.',
    cta_btn='Get My Free Quote',
    cta_trust3='Real people, seven days a week',
    foot_tag='Licensed &amp; insured car shipping between all 50 states. Transparent pricing, vetted carriers, door to door.',
    foot_serving='Serving all 50 states',
)

if __name__ == '__main__':
    out, issues = adspage.build(CFG)
    print('built', out)
    for i in issues: print('  ISSUE', i)
    print('CLEAR' if not issues else '%d issue(s)' % len(issues))
