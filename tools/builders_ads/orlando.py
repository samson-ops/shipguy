#!/usr/bin/env python3
"""Google Ads landing page: Orlando, FL  ->  /vehicle-quote-orlando-florida  (phone line (407) 604-7299).
Built from the live /vehicle-quote page by adspage.build(); rerun after any quote-tool change."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import adspage

TEL = '+14076047299'
CFG = dict(
    slug='vehicle-quote-orlando-florida', city='Orlando', st='FL', lead_prefix='ADS-ORL',
    tel=TEL, disp='(407) 604-7299', disp_nbsp='(407)&nbsp;604-7299',
    tz='America/New_York', tz_label='ET', hours_open=6, hours_close=23, open_label='6 AM', close_label='11 PM',
    hours_static='Real people, seven days a week, 6 AM to 11 PM ET',

    title='Orlando Car Shipping Quote in 30 Seconds | Ship Guy',
    meta='Instant car shipping quote for Orlando, FL. Door-to-door auto transport from Winter Park to Kissimmee, open or enclosed, to any state. Call (407) 604-7299.',

    eyebrow='Orlando Auto Transport &middot; Central Florida',
    variants={
        'default':  ['Orlando Car Shipping', 'Instant ', 'Quote'],
        'enclosed': ['Enclosed Car Shipping', 'Orlando · Instant ', 'Quote'],
        'exotic':   ['Exotic & Luxury Car Shipping', 'Orlando · Instant ', 'Quote'],
        'vacation': ['Vacation Home Car Shipping', 'Orlando · Instant ', 'Quote'],
        'snowbird': ['Snowbird Car Shipping', 'Orlando to the Northeast · Instant ', 'Quote'],
        'newyork':  ['Orlando to New York', 'Car Shipping · Instant ', 'Quote'],
        'to':       ['Ship Your Car to Orlando', 'Instant ', 'Quote'],
        'from':     ['Ship Your Car from Orlando', 'Instant ', 'Quote'],
    },
    lede=('Ship Guy is a licensed auto transport broker serving Orlando and all of Central Florida. '
          'We price your route in seconds, then book a vetted, insured carrier to your door. '
          'Open or enclosed, to or from any state.'),
    badges=[
        ('bolt',  'Price on screen in 30 seconds', 'No account and no waiting on a callback'),
        ('truck', 'Pickup in 1&ndash;3 days', 'Carriers pass through on Interstate 4 constantly'),
        ('pin',   'Door to door in Central Florida', 'Winter Park to Kissimmee, Lake Nona to Clermont'),
    ],
    call_small='Orlando line &middot; Prefer to talk? Call now',
    pq_sub='Orlando pricing in 30 seconds. Free, no obligation.',

    reviews_sub='Trusted by vehicle owners nationwide.',

    lanes_eyebrow='Orlando Lanes &amp; Costs',
    lanes_h2='Orlando Car Shipping Lanes and Estimated Costs',
    lanes_sub='The lanes Central Florida households ask about most, with estimated open-transport ranges. Price your exact route above.',
    lanes=[
        ('Tampa, FL', 'I-4 &middot; ~85 mi', 'Same day', '$170&ndash;$280'),
        ('Jacksonville, FL', 'I-95 &middot; ~140 mi', 'Same day', '$200&ndash;$310'),
        ('Miami, FL', 'FL Tpke &middot; ~235 mi', '1 day', '$220&ndash;$340'),
        ('Atlanta, GA', 'I-75 &middot; ~440 mi', '1 day', '$390&ndash;$570'),
        ('Charlotte, NC', 'I-95/I-26 &middot; ~525 mi', '1&ndash;2 days', '$430&ndash;$620'),
        ('Nashville, TN', 'I-75/I-24 &middot; ~690 mi', '2 days', '$510&ndash;$740'),
        ('New York, NY', 'I-95 &middot; ~1,080 mi', '3 days', '$760&ndash;$1,080'),
        ('Chicago, IL', 'I-75/I-65 &middot; ~1,160 mi', '3 days', '$800&ndash;$1,150'),
        ('Dallas, TX', 'I-10/I-20 &middot; ~1,090 mi', '3 days', '$770&ndash;$1,090'),
        ('Boston, MA', 'I-95 &middot; ~1,300 mi', '3&ndash;4 days', '$860&ndash;$1,220'),
    ],
    lanes_foot=('*2026 estimates for a running sedan on an open trailer. SUVs and trucks run about 10 to 25 percent more, and enclosed more than that. '
                'Season and live carrier availability on your dates set the real quote.'),
    lanes_note=('Orlando sits in the middle of the state, so both coasts are short lanes. '
                'Northeast routes swing with the season, costing more southbound in fall and northbound in spring.'),

    access_eyebrow='Pickup in Orlando',
    access_h2='What Pickup Looks Like Across Central Florida',
    access_sub='Carriers run seventy-five-foot rigs. Here is how they reach you in each part of the metro.',
    access_cards=[
        ('clock', 'Interstate 4 Timing', 'The corridor backs up from mid-morning until evening. Carriers plan Orlando stops for early mornings. A meeting spot near the 408, 417, or 528 beats a curbside pickup on the corridor.'),
        ('gate',  'Kissimmee, Davenport, and ChampionsGate', 'Vacation-home communities are gated, and truck rules vary. Give us the community name and gate code at booking, and the driver has it before dispatch.'),
        ('tower', 'International Drive and the Resorts', 'Resort driveways are not built for a seventy-five-foot truck. Along International Drive the driver meets you at a large lot rather than a hotel entrance.'),
        ('home',  'Lake Nona, Winter Park, and the Suburbs', 'Lake Nona sits beside the airport, and the truck never touches Interstate 4. Winter Park, Oviedo, Clermont, and Apopka usually load at the curb.'),
    ],
    neighborhoods=['Downtown', 'Thornton Park', 'College Park', 'Winter Park', 'Baldwin Park', 'Lake Nona', 'Dr. Phillips', 'MetroWest', 'Windermere', 'Kissimmee', 'Celebration',
                   'Davenport', 'ChampionsGate', 'Sanford', 'Lake Mary', 'Altamonte Springs', 'Oviedo', 'Clermont', 'Apopka', 'Winter Garden', 'Ocoee'],
    chips_cap='Serving Orange, Osceola, Seminole, and Lake Counties, with The Villages about an hour northwest.',
    season=('<b>Timing tip.</b> Seasonal owners and UCF students fill carriers each fall and spring. Book two to three weeks ahead in those windows. '
            'There is no storm surge inland, and shipping usually resumes within a day after a storm.'),

    how_h2='Ship Your Car from Orlando in 3 Simple Steps',
    how_sub='From quote to delivery, Ship Guy keeps Orlando car shipping simple, transparent, and insured.',
    how_steps=[
        ('Get Your Instant Quote', 'Enter your ZIPs, vehicle, and timeframe. Your price appears on screen in about 30 seconds.'),
        ('Book and Schedule Pickup', 'We match you with a vetted, insured carrier and confirm a pickup window. Gate codes and meeting spots go straight to the driver.'),
        ('Inspect and Deliver', 'The driver inspects the car at pickup and again at delivery. You get updates on the way and sign off at your door.'),
    ],

    why_h2='Why Orlando Ships with Ship Guy',
    why_sub='A licensed, insured brokerage that treats your vehicle, and your time, like it matters.',
    why_support='Real representatives by phone to guide your Orlando shipment.',

    faq_h2='Orlando Car Shipping Questions',
    faq_sub='What Orlando shippers ask before they book.',
    faq=[
        ('How much does it cost to ship a car from Orlando?',
         'Tampa runs about $170 to $280 for a sedan on an open trailer, and Miami $220 to $340. Atlanta runs $390 to $570, New York $760 to $1,080, and Chicago $800 to $1,150. '
         'Season, vehicle size, and enclosed transport move the number. Your exact price shows in the quote tool above.'),
        ('How long does car shipping from Orlando take?',
         'Most pickups happen within 1 to 3 days, with carriers passing through on Interstate 4 constantly. Tampa is a same-day lane. '
         'Miami, Jacksonville, and Atlanta take about a day, and New York three to four.'),
        ('Can you deliver to my vacation home in Kissimmee or Davenport?',
         'Yes, and Orlando ships more cars to vacation homes than almost any city in the country. Those communities are gated, so give us the community name and gate code at booking. '
         'The driver needs an adult there to sign, so tell us who will meet the truck.'),
        ('Can I fly in and have the car arrive later?',
         'Yes. New residents fly into Orlando International and have the car arrive a few days later. '
         'Give us the delivery address and the date you land, and we plan the pickup around it.'),
        ('When is the best time to meet the driver in Orlando?',
         'Early. Interstate 4 near the parks jams from mid-morning through the evening. A pickup you can meet at seven schedules faster than one at three. '
         'A spot off the corridor near the 408, 417, or 528 helps too.'),
        ('Should I choose open or enclosed transport in Orlando?',
         'Open transport is the everyday choice, and most seasonal and student cars ride it. Enclosed transport keeps a car covered against summer downpours, road grit, and attention. '
         'It is the standard for exotics and anything a collector owns.'),
        ('Is Ship Guy a carrier or a broker?',
         'Ship Guy is a licensed auto transport broker, FMCSA MC #1457715. We do not own trucks. '
         'We book vetted carriers with active insurance, and your car is covered while it is on the truck.'),
        ('What happens after I get my quote?',
         'Your price appears on screen. Book online right there or call <a data-track="call-faq" href="tel:%s">(407) 604-7299</a> to lock in a pickup window. '
         'The driver inspects the car at pickup, and you sign off at delivery.' % TEL),
    ],

    cta_h2='Ready to Ship Your Car to or from Orlando?',
    cta_sub='Get your free Orlando quote in about 30 seconds, or call and talk to a real specialist.',
    cta_btn='Get My Orlando Quote',
    cta_trust3='Orlando line, seven days a week',
    foot_tag='Licensed &amp; insured car shipping for Central Florida and all 50 states. Transparent pricing, vetted carriers, door to door.',
    foot_serving='Serving Central Florida and all 50 states',
)

if __name__ == '__main__':
    out, issues = adspage.build(CFG)
    print('built', out)
    for i in issues: print('  ISSUE', i)
    print('CLEAR' if not issues else '%d issue(s)' % len(issues))
