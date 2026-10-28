#!/usr/bin/env python3
"""Google Ads landing page: Expedited Car Shipping  ->  /vehicle-quote-expedited-car-shipping
(main line (866) 297-3244). Built from the live /vehicle-quote page by adspage.build()."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import adspage

TEL = '+18662973244'
CFG = dict(
    slug='vehicle-quote-expedited-car-shipping', city='Expedited', st='US', lead_prefix='ADS-EXP',
    tel=TEL, disp='(866) 297-3244', disp_nbsp='(866)&nbsp;297-3244',

    title='Expedited Car Shipping Quote in 30 Seconds | Ship Guy',
    meta='Instant expedited car shipping quote. Priority dispatch for the quickest available pickup, door to door, open or enclosed, to any state. Call (866) 297-3244.',

    eyebrow='Expedited Auto Transport &middot; Priority Dispatch',
    variants={
        'default':    ['Expedited Car Shipping', 'Instant ', 'Quote'],
        'fast':       ['Need Your Car Moved Fast?', 'Instant ', 'Quote'],
        'rush':       ['Rush Car Shipping', 'Priority Pickup · Instant ', 'Quote'],
        'sameweek':   ['Same-Week Car Shipping', 'Instant ', 'Quote'],
        'enclosed':   ['Expedited Enclosed Shipping', 'Instant ', 'Quote'],
        'relocation': ['Last-Minute Relocation?', 'Ship Your Car · Instant ', 'Quote'],
    },
    lede=('Ship Guy is a licensed auto transport broker, and expedited service puts your car first in line. '
          'We price your route in seconds, then dispatch a vetted, insured carrier for the quickest available pickup. '
          'Open or enclosed, to any state.'),
    badges=[
        ('bolt',  'Priority dispatch', 'Posted at a rate carriers act on first'),
        ('clock', 'Pickup often within 1&ndash;3 days', 'The quickest available truck on your lane'),
        ('truck', 'Faster, tighter delivery window', 'Fewer stops between pickup and delivery'),
    ],
    call_small='Need it moved now? Call',
    pq_sub='Expedited pricing in 30 seconds. Free, no obligation.',

    reviews_sub='Trusted by vehicle owners nationwide.',

    table_eyebrow='Standard vs Expedited',
    table_h2='What Expedited Car Shipping Changes',
    table_sub='Same vetted carriers and the same insurance. Expedited changes how fast your car gets on a truck.',
    table_cols=['What you get', 'Standard service', 'Expedited service'],
    table_hide_m=None,
    table_rate_col=False,
    table_rows=[
        ('Carrier match', 'The next carrier with space on your lane', 'Priority posting that carriers act on first'),
        ('Pickup window', 'Usually 1 to 3 days, longer in peak season', 'The quickest available pickup, often within 1 to 3 days'),
        ('Routing', 'Shared load with other stops along the way', 'Time-sensitive routing with fewer stops'),
        ('Delivery window', 'Estimated at dispatch, updated in transit', 'Tighter window, updated in transit'),
        ('Price', 'Your all-in quote', 'Your quote plus a priority premium, shown before you book'),
        ('Insurance', 'Active cargo insurance on every carrier', 'The same. Speed never cuts coverage'),
    ],
    table_foot='Pickup timing depends on the lane. Busy corridors with many trucks move fastest, and rural pickups take longer even when expedited.',
    table_note='Expedited is worth it for a job start, a closing, or a storm in the forecast. When a few days do not matter, standard service is the better value.',

    cards_eyebrow='How Expedited Works',
    cards_h2='What Happens When You Choose Expedited',
    cards_sub='Four things that get your car moving faster.',
    cards=[
        ('bolt',  'Priority dispatch', 'Your car is posted at a rate carriers act on first, instead of waiting for a standard match. That gets it on a truck as quickly as the lane allows.'),
        ('clock', 'Pickup, often within 1 to 3 days', 'The quickest available pickup on your lane, often within 1 to 3 days. Busy corridors with many trucks move fastest.'),
        ('truck', 'Faster, more predictable transit', 'Time-sensitive routing means fewer stops between pickup and delivery. You get a tighter delivery window and updates along the way.'),
        ('doc',   'When it is worth it', 'Job start dates, home closings, a lease ending, or a storm in the forecast. Standard service is the better value when a few days do not matter.'),
    ],
    chips=['Florida &harr; Northeast', 'Texas &harr; California', 'Chicago &harr; Florida', 'Atlanta &harr; Florida', 'Los Angeles &harr; Phoenix', 'Dallas &harr; Atlanta',
           'New York &harr; Chicago', 'Seattle &harr; Los Angeles', 'Denver &harr; Phoenix', 'Charlotte &harr; Florida'],
    chips_cap='The busiest corridors have the most trucks, so expedited pickups there are the fastest.',
    tip=('<b>Need it moved now?</b> Choose As soon as possible for the pickup timeframe. '
         'Then call <a data-track="call-tip" href="tel:%s">(866) 297-3244</a> and we flag the order as expedited and price the priority dispatch.' % TEL),

    how_h2='Expedited Car Shipping in 3 Simple Steps',
    how_sub='From quote to delivery, Ship Guy keeps expedited car shipping simple, transparent, and insured.',
    how_steps=[
        ('Get Your Instant Quote', 'Enter your ZIPs, vehicle, and timeframe, and choose As soon as possible. Your price appears on screen in about 30 seconds.'),
        ('Book and Flag It Expedited', 'Call us or book online and tell us the deadline. We price the priority dispatch and post your car at the front of the line.'),
        ('Pickup and Delivery', 'The first available carrier loads your car, inspects it with you, and heads out. You get updates on the way and sign off at delivery.'),
    ],

    why_h2='Why Rush Moves Ship with Ship Guy',
    why_sub='A licensed, insured brokerage that treats your vehicle, and your time, like it matters.',
    why_support='Real representatives by phone to keep your expedited shipment moving.',

    faq_h2='Expedited Car Shipping Questions',
    faq_sub='What people on a deadline ask before they book.',
    faq=[
        ('How fast can you pick up my car?',
         'Expedited dispatch targets the quickest available pickup on your lane, often within 1 to 3 days. Busy corridors with many trucks move fastest. '
         'Rural pickups take longer even when expedited, and we tell you the realistic window before you book.'),
        ('How much more does expedited cost?',
         'Expedited adds a priority premium, because the carrier is paid to move your car first. The exact figure depends on the lane and the date, and we show it before you book. '
         'Standard service is the better value when a few days do not matter.'),
        ('Does expedited make the drive itself faster?',
         'Partly. Time-sensitive routing means fewer stops between pickup and delivery, so the window is tighter. '
         'Drivers still follow federal hours-of-service limits, so a coast-to-coast run takes several days.'),
        ('Can I get same-day pickup?',
         'Sometimes, when a truck with space is already near you on a busy lane. Call <a data-track="call-faq" href="tel:%s">(866) 297-3244</a> with the pickup address and we check live availability. '
         'We do not promise a same-day pickup before we see the lane.' % TEL),
        ('Is expedited available on enclosed transport?',
         'Yes. Enclosed carriers are fewer, so the window runs a little longer, but the same priority applies. Tell us the vehicle and we quote both.'),
        ('Does faster mean less careful?',
         'No. Expedited uses the same vetted carriers with active cargo insurance and the same inspection report. Speed changes the schedule, not the handling.'),
        ('Is Ship Guy a carrier or a broker?',
         'Ship Guy is a licensed auto transport broker, FMCSA MC #1457715. We do not own trucks. '
         'We book vetted carriers with active insurance, and your car is covered while it is on the truck.'),
        ('What happens after I get my quote?',
         'Your price appears on screen. Book online right there or call <a data-track="call-faq" href="tel:%s">(866) 297-3244</a> to flag the order as expedited. '
         'The driver inspects the car at pickup, and you sign off at delivery.' % TEL),
    ],

    cta_h2='Need Your Car Moved Fast?',
    cta_sub='Get your free expedited quote in about 30 seconds, or call and we check your lane live.',
    cta_btn='Get My Expedited Quote',
    cta_trust3='Priority dispatch, same insurance',
    foot_tag='Licensed &amp; insured expedited car shipping to all 50 states. Transparent pricing, vetted carriers, door to door.',
    foot_serving='Serving all 50 states',
)

if __name__ == '__main__':
    out, issues = adspage.build(CFG)
    print('built', out)
    for i in issues: print('  ISSUE', i)
    print('CLEAR' if not issues else '%d issue(s)' % len(issues))
