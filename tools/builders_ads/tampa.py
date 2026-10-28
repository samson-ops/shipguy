#!/usr/bin/env python3
"""Google Ads landing page: Tampa, FL  ->  /vehicle-quote-tampa-florida  (phone line (813) 497-4151).
Built from the live /vehicle-quote page by adspage.build(); rerun after any quote-tool change."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import adspage

TEL = '+18134974151'
CFG = dict(
    slug='vehicle-quote-tampa-florida', city='Tampa', st='FL', lead_prefix='ADS-TPA',
    tel=TEL, disp='(813) 497-4151', disp_nbsp='(813)&nbsp;497-4151',
    tz='America/New_York', tz_label='ET', hours_open=6, hours_close=23, open_label='6 AM', close_label='11 PM',
    hours_static='Real people, seven days a week, 6 AM to 11 PM ET',

    title='Tampa Car Shipping Quote in 30 Seconds | Ship Guy',
    meta='Instant car shipping quote for Tampa, FL. Door-to-door auto transport from South Tampa to Wesley Chapel, open or enclosed, to any state. Call (813) 497-4151.',

    eyebrow='Tampa Auto Transport &middot; Hillsborough County',
    variants={
        'default':  ['Tampa Car Shipping', 'Instant ', 'Quote'],
        'enclosed': ['Enclosed Car Shipping', 'Tampa · Instant ', 'Quote'],
        'exotic':   ['Exotic & Luxury Car Shipping', 'Tampa · Instant ', 'Quote'],
        'military': ['Military Car Shipping', 'Tampa · Instant ', 'Quote'],
        'snowbird': ['Snowbird Car Shipping', 'Tampa to the Northeast · Instant ', 'Quote'],
        'newyork':  ['Tampa to New York', 'Car Shipping · Instant ', 'Quote'],
        'to':       ['Ship Your Car to Tampa', 'Instant ', 'Quote'],
        'from':     ['Ship Your Car from Tampa', 'Instant ', 'Quote'],
    },
    lede=('Ship Guy is a licensed auto transport broker serving Tampa and Hillsborough County. '
          'We price your route in seconds, then book a vetted, insured carrier to your door. '
          'Open or enclosed, to or from any state.'),
    badges=[
        ('bolt',  'Price on screen in 30 seconds', 'No account and no waiting on a callback'),
        ('truck', 'Pickup in 1&ndash;3 days', 'On most Tampa routes, longer in summer and storm season'),
        ('pin',   'Door to door across the bay', 'South Tampa to Wesley Chapel, Brandon to Clearwater'),
    ],
    call_small='Tampa line &middot; Prefer to talk? Call now',
    pq_sub='Tampa pricing in 30 seconds. Free, no obligation.',

    reviews_sub='Trusted by vehicle owners nationwide.',

    lanes_eyebrow='Tampa Lanes &amp; Costs',
    lanes_h2='Tampa Car Shipping Lanes and Estimated Costs',
    lanes_sub='Common lanes out of the bay area, with estimated open-transport ranges. Price your exact route above.',
    lanes=[
        ('Orlando, FL', 'I-4 &middot; ~85 mi', 'Same day', '$170&ndash;$280'),
        ('Jacksonville, FL', 'I-75/I-10 &middot; ~200 mi', 'Same day', '$220&ndash;$340'),
        ('Miami, FL', 'I-75 &middot; ~280 mi', '1 day', '$250&ndash;$380'),
        ('Atlanta, GA', 'I-75 &middot; ~460 mi', '1 day', '$400&ndash;$580'),
        ('Charlotte, NC', 'I-75/I-26 &middot; ~580 mi', '1&ndash;2 days', '$450&ndash;$650'),
        ('Nashville, TN', 'I-75/I-24 &middot; ~700 mi', '2 days', '$520&ndash;$750'),
        ('Dallas, TX', 'I-10/I-20 &middot; ~1,120 mi', '3 days', '$780&ndash;$1,100'),
        ('New York, NY', 'I-95 &middot; ~1,140 mi', '3&ndash;4 days', '$780&ndash;$1,100'),
        ('Chicago, IL', 'I-75/I-65 &middot; ~1,170 mi', '3 days', '$800&ndash;$1,150'),
        ('Boston, MA', 'I-95 &middot; ~1,350 mi', '4 days', '$880&ndash;$1,250'),
    ],
    lanes_foot=('*2026 estimates for a running sedan on an open trailer. SUVs and trucks run about 10 to 25 percent more, and enclosed more than that. '
                'Season and live carrier availability on your dates set the real quote.'),
    lanes_note=('Interstate 75 north is the workhorse lane, and Atlanta, Nashville, and Chicago all ride it. '
                'Northeast lanes swing with the season, costing more southbound in fall and northbound in spring.'),

    access_eyebrow='Pickup in Tampa',
    access_h2='What Pickup Looks Like Around Tampa Bay',
    access_sub='Carriers run seventy-five-foot rigs. Here is how they reach you in each part of the bay area.',
    access_cards=[
        ('bridge', 'The Bay Bridges and Pinellas', 'Carriers use the Howard Frankland, Gandy, and Courtney Campbell bridges without restriction. A pickup in Tampa and a delivery in Clearwater are the same trip.'),
        ('tower',  'South Tampa, Bayshore, and Davis Islands', 'Streets near Bayshore Boulevard are older and narrow. Davis Islands is reached by a short bridge, and the driver usually meets you near the entrance.'),
        ('gate',   'MacDill and Gated Communities', 'Base housing is gated, so the handoff happens just outside the gate. Westchase and Tampa Palms have gated sections, so share the community name and gate code.'),
        ('home',   'Brandon, Riverview, and the Suburbs', "Wide suburban streets mean the truck usually reaches the curb. Wesley Chapel, Land O' Lakes, and Apollo Beach load the same way."),
    ],
    neighborhoods=['South Tampa', 'Hyde Park', 'Davis Islands', 'Bayshore', 'Westshore', 'Carrollwood', "Town 'n' Country", 'Westchase', 'New Tampa', 'Tampa Palms', 'Temple Terrace',
                   'Seminole Heights', 'Ybor City', 'Brandon', 'Riverview', 'Apollo Beach', 'Sun City Center', 'Ruskin', 'Wesley Chapel', 'Lutz', "Land O' Lakes", 'Plant City'],
    chips_cap='Serving Hillsborough and Pasco Counties. Pinellas pickups in Saint Petersburg and Clearwater are the same trip.',
    season=('<b>Timing tip.</b> MacDill moves peak May through August, and snowbird cars arrive in fall and leave in spring. Book two to three weeks ahead in those windows. '
            'Know your evacuation zone, and call early if a storm is forecast for Zone A or B.'),

    how_h2='Ship Your Car from Tampa in 3 Simple Steps',
    how_sub='From quote to delivery, Ship Guy keeps Tampa car shipping simple, transparent, and insured.',
    how_steps=[
        ('Get Your Instant Quote', 'Enter your ZIPs, vehicle, and timeframe. Your price appears on screen in about 30 seconds.'),
        ('Book and Schedule Pickup', 'We match you with a vetted, insured carrier and confirm a pickup window. Gate codes and bridge details go straight to the driver.'),
        ('Inspect and Deliver', 'The driver inspects the car at pickup and again at delivery. You get updates on the way and sign off at your door.'),
    ],

    why_h2='Why Tampa Ships with Ship Guy',
    why_sub='A licensed, insured brokerage that treats your vehicle, and your time, like it matters.',
    why_support='Real representatives by phone to guide your Tampa shipment.',

    faq_h2='Tampa Car Shipping Questions',
    faq_sub='What Tampa shippers ask before they book.',
    faq=[
        ('How much does it cost to ship a car from Tampa?',
         'Orlando runs about $170 to $280 for a sedan on an open trailer, and Miami $250 to $380. Atlanta runs $400 to $580, New York $780 to $1,100, and Chicago $800 to $1,150. '
         'Season, vehicle size, and enclosed transport move the number. Your exact price shows in the quote tool above.'),
        ('How long does car shipping from Tampa take?',
         'Most pickups happen within 1 to 3 days, and carriers cross the bay bridges without trouble. Orlando is a same-day lane. '
         'Atlanta and Miami take about a day, New York three to four, and Chicago about three.'),
        ('Do you handle MacDill PCS moves?',
         'Yes, and summer is the peak, so book two to three weeks ahead from May through August. Base housing is gated, so the handoff happens just outside the gate. '
         'Ship Guy is a private broker with no connection to the military.'),
        ('What if a hurricane is forecast?',
         'Carriers leave the region days ahead of landfall, and pickups pause until the bridges reopen. If your car is in evacuation Zone A or B, call the moment a forecast firms up. '
         'Moving it early beats waiting on a crowded evacuation route.'),
        ('Should I choose open or enclosed transport in Tampa?',
         'Open transport is the everyday choice, and most seasonal and military cars ride it. Enclosed transport keeps a car covered against salt air, summer downpours, and grit. '
         'It is the standard for exotics and anything a collector owns.'),
        ('Can you pick up in Saint Petersburg or Clearwater?',
         'Yes. Carriers use the Howard Frankland, Gandy, and Courtney Campbell bridges without restriction. A pickup anywhere in Pinellas County prices like a Tampa pickup.'),
        ('Is Ship Guy a carrier or a broker?',
         'Ship Guy is a licensed auto transport broker, FMCSA MC #1457715. We do not own trucks. '
         'We book vetted carriers with active insurance, and your car is covered while it is on the truck.'),
        ('What happens after I get my quote?',
         'Your price appears on screen. Book online right there or call <a data-track="call-faq" href="tel:%s">(813) 497-4151</a> to lock in a pickup window. '
         'The driver inspects the car at pickup, and you sign off at delivery.' % TEL),
    ],

    cta_h2='Ready to Ship Your Car to or from Tampa?',
    cta_sub='Get your free Tampa quote in about 30 seconds, or call and talk to a real specialist.',
    cta_btn='Get My Tampa Quote',
    cta_trust3='Tampa line, seven days a week',
    foot_tag='Licensed &amp; insured car shipping for Tampa Bay and all 50 states. Transparent pricing, vetted carriers, door to door.',
    foot_serving='Serving Tampa Bay and all 50 states',
)

if __name__ == '__main__':
    out, issues = adspage.build(CFG)
    print('built', out)
    for i in issues: print('  ISSUE', i)
    print('CLEAR' if not issues else '%d issue(s)' % len(issues))
