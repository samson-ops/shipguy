#!/usr/bin/env python3
"""Google Ads landing page: Instant Car Shipping Quote  ->  /vehicle-quote-instant-car-shipping-quote
(main line (866) 297-3244). Built from the live /vehicle-quote page by adspage.build()."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import adspage

TEL = '+18662973244'
CFG = dict(
    slug='vehicle-quote-instant-car-shipping-quote', city='Instant Quote', st='US', lead_prefix='ADS-IQ',
    tel=TEL, disp='(866) 297-3244', disp_nbsp='(866)&nbsp;297-3244',

    title='Instant Car Shipping Quote in 30 Seconds | Ship Guy',
    meta='Get an instant car shipping quote in 30 seconds. Door-to-door auto transport to any state, open or enclosed, all-in pricing. Call (866) 297-3244.',

    eyebrow='Instant Car Shipping Quote &middot; All 50 States',
    variants={
        'default':    ['Get an Instant', 'Car Shipping ', 'Quote'],
        'cost':       ['How Much to Ship a Car?', 'Instant ', 'Quote'],
        'affordable': ['Affordable Car Shipping', 'Instant ', 'Quote'],
        'online':     ['Car Shipping Quote Online', 'Instant ', 'Quote'],
        'calculator': ['Car Shipping Cost Calculator', 'Instant ', 'Quote'],
        'enclosed':   ['Enclosed Car Shipping', 'Instant ', 'Quote'],
        'door':       ['Door-to-Door Car Shipping', 'Instant ', 'Quote'],
        'nationwide': ['Nationwide Auto Transport', 'Instant ', 'Quote'],
    },
    lede=('Ship Guy is a licensed auto transport broker, and your price appears on screen in about 30 seconds. '
          'No account, no callback, and no obligation. '
          'Then book online or call, and a vetted, insured carrier comes to your door.'),
    badges=[
        ('bolt',  'Price on screen in 30 seconds', 'No account and no waiting on a callback'),
        ('doc',   'All-in pricing', 'Pickup, transport, delivery, and insurance in one number'),
        ('truck', 'Any two addresses, door to door', 'All 50 states, open or enclosed'),
    ],
    pq_sub='Fast, secure pricing in 30 seconds. Free, no obligation.',

    reviews_sub='Trusted by vehicle owners nationwide.',

    table_eyebrow='What You Pay For',
    table_h2='What Sets Your Car Shipping Price',
    table_sub='Seven things the quote tool weighs. Enter your route above to see the exact number.',
    table_cols=['What moves the price', 'Effect', 'Example'],
    table_hide_m=None,
    table_rate_col=False,
    table_rows=[
        ('Distance', 'The biggest factor, but longer moves cost less per mile', 'Orlando to Miami $220 to $340, New York to Los Angeles $1,200 to $1,700'),
        ('Route popularity', 'Busy lanes have more trucks and lower prices', 'Florida to New York runs $780 to $1,150 despite 1,300 miles'),
        ('Vehicle size', 'SUVs and trucks take more deck space', 'About 10 to 25 percent more than a sedan'),
        ('Open or enclosed', 'Enclosed carriers are fewer and carry higher limits', 'Enclosed runs more than open, typically 30 to 40 percent'),
        ('Season', 'Summer and snowbird peaks raise demand', 'The same car costs more southbound in November than in July'),
        ('Flexibility', 'A multi-day pickup window lets carriers fill a load', 'Flexible dates get a better price and a faster pickup'),
        ('Running or not', 'An inoperable car needs a winch and extra time', 'Tell us at booking so the right truck is sent'),
    ],
    table_foot=('Example figures are 2026 estimates for a running sedan on an open trailer, from our city lane tables. '
                'Your quote reflects live carrier availability on your dates.'),
    table_note=("The number you see is the number you pay. "
                "It covers pickup, transport, delivery, and the carrier's insurance, with no hidden fees or surprise charges at delivery."),

    cards_eyebrow='Why Instant',
    cards_h2='What Makes the Quote Instant and Accurate',
    cards_sub='How the tool prices your route in seconds, and what happens next.',
    cards=[
        ('bolt',   'Live pricing, not a form', 'The tool prices your exact route and vehicle against live carrier availability. The number appears on screen, not in an email two days later.'),
        ('doc',    'Three short steps', 'Route, vehicle, then your contact details. Most people finish in about 30 seconds, and nothing is charged for a quote.'),
        ('truck',  'Book online or by phone', 'Happy with the price? Continue to booking right there, or call <a data-track="call-card" href="tel:%s">(866) 297-3244</a> and a specialist locks in your pickup window.' % TEL),
        ('shield', 'Vetted, insured carriers', 'Every carrier we book is screened for licensing, safety record, and active cargo insurance. Your car is covered while it is on the truck.'),
    ],
    chips=['Open transport', 'Enclosed transport', 'Door to door', 'State to state', 'Cross country', 'Snowbird', 'Expedited', 'Military PCS', 'Auction and dealer',
           'Inoperable vehicles', 'Classic and exotic'],
    chips_cap='Every service is priced by the same tool above.',
    tip=('<b>Tip.</b> Have your ZIP codes and the year, make, and model ready, and the quote takes about 30 seconds. '
         'If the car does not run, choose that option so the right truck is sent.'),

    how_h2='Ship Your Car in 3 Simple Steps',
    how_sub='From quote to delivery, Ship Guy keeps car shipping simple, transparent, and insured.',
    how_steps=[
        ('Get Your Instant Quote', 'Enter your ZIPs, vehicle, and timeframe. Your price appears on screen in about 30 seconds.'),
        ('Book and Schedule Pickup', 'We match you with a vetted, insured carrier and confirm a pickup window. Gate codes and meeting spots go straight to the driver.'),
        ('Inspect and Deliver', 'The driver inspects the car at pickup and again at delivery. You get updates on the way and sign off at your door.'),
    ],

    why_h2='Why Shippers Choose Ship Guy',
    why_sub='A licensed, insured brokerage that treats your vehicle, and your time, like it matters.',
    why_support='Real representatives by phone to guide your shipment.',

    faq_h2='Instant Quote Questions',
    faq_sub='What people ask before they price a shipment.',
    faq=[
        ('How does the instant quote work?',
         'Enter your pickup and delivery ZIPs, the vehicle, and a timeframe. The tool prices the route against live carrier availability and shows the number on screen. '
         'Nothing is charged, and there is no obligation.'),
        ('How much does it cost to ship a car?',
         'Under 500 miles runs about $170 to $480 for a sedan on an open trailer. Florida to New York runs $780 to $1,150, and coast to coast $1,200 to $1,700. '
         'Vehicle size, season, and enclosed transport move the number. Your exact price shows in the quote tool above.'),
        ('Is the quote the final price?',
         "The quote is an all-in price for the route, vehicle, and dates you enter. It covers pickup, transport, delivery, and the carrier's insurance, with no hidden fees at delivery. "
         'Changing the vehicle, the dates, or an inoperable condition changes the price.'),
        ('How long does it take?',
         'Pickup usually happens within 1 to 3 days of booking. Under 500 miles takes about a day on the truck. '
         'A thousand to fifteen hundred miles takes 3 to 4 days, and coast to coast 5 to 7.'),
        ('Do I have to pay to get a quote?',
         'No. The quote is free and there is no obligation. You pay only when you book, and the payment terms are explained clearly at that point.'),
        ('Open or enclosed?',
         'Open transport is the everyday choice and the best value on any distance. Enclosed transport keeps a car covered against weather, road grit, and attention. '
         'It is the standard for exotics and anything a collector owns.'),
        ('Can you ship a car that does not run?',
         'Yes. Choose the inoperable option in the quote tool so the right carrier, with a winch, is assigned. The car needs to roll, steer, and brake for loading.'),
        ('Is Ship Guy a carrier or a broker?',
         'Ship Guy is a licensed auto transport broker, FMCSA MC #1457715. We do not own trucks. '
         'We book vetted carriers with active insurance, and your car is covered while it is on the truck.'),
        ('What happens after I get my quote?',
         'Your price appears on screen. Book online right there or call <a data-track="call-faq" href="tel:%s">(866) 297-3244</a> to lock in a pickup window. '
         'The driver inspects the car at pickup, and you sign off at delivery.' % TEL),
    ],

    cta_h2='Ready to See Your Price?',
    cta_sub='Get your free quote in about 30 seconds, or call and talk to a real specialist.',
    cta_btn='Get My Instant Quote',
    cta_trust3='Real people, seven days a week',
    foot_tag='Licensed &amp; insured car shipping to all 50 states. Transparent pricing, vetted carriers, door to door.',
    foot_serving='Serving all 50 states',
)

if __name__ == '__main__':
    out, issues = adspage.build(CFG)
    print('built', out)
    for i in issues: print('  ISSUE', i)
    print('CLEAR' if not issues else '%d issue(s)' % len(issues))
