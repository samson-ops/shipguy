#!/usr/bin/env python3
"""Google Ads landing page: Miami, FL  ->  /vehicle-quote-miami-florida  (phone line (305) 676-9433).
Built from the live /vehicle-quote page by adspage.build(); rerun after any quote-tool change."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import adspage

TEL = '+13056769433'
CFG = dict(
    slug='vehicle-quote-miami-florida', city='Miami', st='FL', lead_prefix='ADS-MIA',
    tel=TEL, disp='(305) 676-9433', disp_nbsp='(305)&nbsp;676-9433',
    tz='America/New_York', tz_label='ET', hours_open=6, hours_close=23, open_label='6 AM', close_label='11 PM',
    hours_static='Real people, seven days a week, 6 AM to 11 PM ET',

    title='Miami Car Shipping Quote in 30 Seconds | Ship Guy',
    meta='Instant car shipping quote for Miami, FL. Door-to-door auto transport from Brickell to Homestead, open or enclosed, to any state. Call (305) 676-9433.',

    eyebrow='Miami Auto Transport &middot; Miami-Dade County',
    variants={
        'default':  ['Miami Car Shipping', 'Instant ', 'Quote'],
        'enclosed': ['Enclosed Car Shipping', 'Miami · Instant ', 'Quote'],
        'exotic':   ['Exotic & Luxury Car Shipping', 'Miami · Instant ', 'Quote'],
        'snowbird': ['Snowbird Car Shipping', 'Miami \u00b7 Instant ', 'Quote'],
        'newyork':  ['Miami to New York', 'Car Shipping · Instant ', 'Quote'],
        'to':       ['Ship Your Car to Miami', 'Instant ', 'Quote'],
        'from':     ['Ship Your Car from Miami', 'Instant ', 'Quote'],
    },
    lede=('Ship Guy is a licensed auto transport broker serving all of Miami-Dade. '
          'We price your route in seconds, then book a vetted, insured carrier to your door. '
          'Open or enclosed, to or from any state.'),
    badges=[
        ('bolt',  'Price on screen in 30 seconds', 'No account and no waiting on a callback'),
        ('truck', 'Pickup in 1&ndash;3 days', 'On most Miami routes, longer in peak season'),
        ('pin',   'Door to door in Miami-Dade', 'Brickell to Homestead, the Beach to Doral'),
    ],
    call_small='Miami line &middot; Prefer to talk? Call now',
    pq_sub='Miami pricing in 30 seconds. Free, no obligation.',

    reviews_sub='Trusted by vehicle owners nationwide.',

    lanes_eyebrow='Miami Lanes &amp; Costs',
    lanes_h2='Miami Car Shipping Lanes and Estimated Costs',
    lanes_sub='The routes Miami shippers ask about most, with estimated open-transport ranges. Price your exact route above.',
    lanes=[
        ('Orlando, FL', 'FL Tpke &middot; ~235 mi', 'Same day', '$220&ndash;$340'),
        ('Tampa, FL', 'I-75 &middot; ~280 mi', 'Same day', '$250&ndash;$380'),
        ('Atlanta, GA', 'I-75 &middot; ~660 mi', '1&ndash;2 days', '$450&ndash;$650'),
        ('Charlotte, NC', 'I-95/I-26 &middot; ~735 mi', '2 days', '$500&ndash;$720'),
        ('Washington, DC', 'I-95 &middot; ~1,050 mi', '2&ndash;3 days', '$700&ndash;$980'),
        ('Houston, TX', 'I-10 &middot; ~1,190 mi', '3 days', '$800&ndash;$1,100'),
        ('New York, NY', 'I-95 &middot; ~1,280 mi', '3&ndash;4 days', '$800&ndash;$1,150'),
        ('Chicago, IL', 'I-75/I-65 &middot; ~1,380 mi', '3&ndash;4 days', '$850&ndash;$1,200'),
        ('Boston, MA', 'I-95 &middot; ~1,500 mi', '4 days', '$900&ndash;$1,250'),
        ('Los Angeles, CA', 'I-10 &middot; ~2,730 mi', '5&ndash;6 days', '$1,200&ndash;$1,700'),
    ],
    lanes_foot=('*2026 estimates for a running sedan on an open trailer. SUVs and trucks run about 10 to 25 percent more, and enclosed more than that. '
                'Season and live carrier availability on your dates set the real quote.'),
    lanes_note=('The New York lane is the busiest long-distance lane on the East Coast. Southbound demand peaks October through December, northbound April through June. '
                'Off season, Miami to New York can be one of the better values in the country.'),

    access_eyebrow='Pickup in Miami',
    access_h2='What Pickup Looks Like Across Miami-Dade',
    access_sub='Carriers run seventy-five-foot rigs. Here is how they reach you in each part of the county.',
    access_cards=[
        ('tower',  'Brickell, Downtown, and the Beach', 'Condo towers with valet and underground garages cannot take a carrier. The driver meets you at a nearby surface lot, usually within a few blocks.'),
        ('bridge', 'Causeways to Miami Beach', 'The Venetian Causeway has weight limits that keep a loaded carrier off. Drivers use the MacArthur or the Julia Tuttle instead, and Key Biscayne is reached over the Rickenbacker.'),
        ('gate',   'Coral Gables, Pinecrest, and Doral', 'Gated communities set their own truck rules. Share the community name and gate code when you book, and we pass it to the driver.'),
        ('home',   'Kendall, Hialeah, and the Suburbs', 'Flat, wide streets mean the truck usually reaches the curb. Homestead, Cutler Bay, and Miami Lakes load the same way.'),
    ],
    neighborhoods=['Brickell', 'Downtown', 'Wynwood', 'Little Havana', 'Coral Gables', 'Coconut Grove', 'Key Biscayne', 'Miami Beach', 'South Beach', 'North Beach',
                   'Sunny Isles', 'Bal Harbour', 'Aventura', 'North Miami', 'Miami Lakes', 'Hialeah', 'Doral', 'Kendall', 'Pinecrest', 'Cutler Bay', 'Homestead'],
    chips_cap='Serving all of Miami-Dade County. Broward and Palm Beach pickups are welcome too.',
    season=('<b>Timing tip.</b> Snowbird season runs November through April. Book two to three weeks ahead for a southbound car in fall or a northbound car in spring. '
            'Hurricane season runs June through November, and we never send a driver into a storm.'),

    how_h2='Ship Your Car from Miami in 3 Simple Steps',
    how_sub='From quote to delivery, Ship Guy keeps Miami car shipping simple, transparent, and insured.',
    how_steps=[
        ('Get Your Instant Quote', 'Enter your ZIPs, vehicle, and timeframe. Your price appears on screen in about 30 seconds.'),
        ('Book and Schedule Pickup', 'We match you with a vetted, insured carrier and confirm a pickup window. Condo and gate details go straight to the driver.'),
        ('Inspect and Deliver', 'The driver inspects the car at pickup and again at delivery. You get updates on the way and sign off at your door.'),
    ],

    why_h2='Why Miami Ships with Ship Guy',
    why_sub='A licensed, insured brokerage that treats your vehicle, and your time, like it matters.',
    why_support='Real representatives by phone to guide your Miami shipment.',

    faq_h2='Miami Car Shipping Questions',
    faq_sub='What Miami shippers ask before they book.',
    faq=[
        ('How much does it cost to ship a car from Miami?',
         'Orlando and Tampa run about $220 to $380 for a sedan on an open trailer. New York runs $800 to $1,150 and Los Angeles $1,200 to $1,700. '
         'Season, vehicle size, and enclosed transport move the number. Your exact price shows in the quote tool above.'),
        ('How long does car shipping from Miami take?',
         'Most pickups happen within 1 to 3 days, longer in peak season if your dates are rigid. Orlando and Tampa are same-day lanes. '
         'Atlanta takes a day or two, New York three to four, and Los Angeles five to six.'),
        ('Can the truck reach my condo in Brickell or Miami Beach?',
         'Usually not. Valet decks and garages cannot take a carrier, so the driver meets you at a surface lot nearby. '
         'Miami Beach pickups come over the MacArthur or Julia Tuttle, since the Venetian has weight limits.'),
        ('When should I book a snowbird car?',
         'Two to three weeks ahead. Southbound demand peaks October through December and northbound demand peaks April through June. '
         'Flexible dates get you a better price and a faster pickup.'),
        ('Should I choose open or enclosed transport in Miami?',
         'Open transport is the everyday choice, and most seasonal cars ride it up and down the coast. Enclosed transport keeps a car covered against salt air, downpours, and grit. '
         'It is the standard for exotics and anything a collector owns.'),
        ('Do you ship cars overseas from Port Miami?',
         'No. Overseas shipping is an international process with customs paperwork, and we do not arrange it. '
         'We move cars within the United States, including to and from Miami once a car has been released.'),
        ('Is Ship Guy a carrier or a broker?',
         'Ship Guy is a licensed auto transport broker, FMCSA MC #1457715. We do not own trucks. '
         'We book vetted carriers with active insurance, and your car is covered while it is on the truck.'),
        ('What happens after I get my quote?',
         'Your price appears on screen. Book online right there or call <a data-track="call-faq" href="tel:%s">(305) 676-9433</a> to lock in a pickup window. '
         'The driver inspects the car at pickup, and you sign off at delivery.' % TEL),
    ],

    cta_h2='Ready to Ship Your Car to or from Miami?',
    cta_sub='Get your free Miami quote in about 30 seconds, or call and talk to a real specialist.',
    cta_btn='Get My Miami Quote',
    cta_trust3='Miami line, seven days a week',
    foot_tag='Licensed &amp; insured car shipping for Miami and all 50 states. Transparent pricing, vetted carriers, door to door.',
    foot_serving='Serving Miami-Dade County and all 50 states',
)

if __name__ == '__main__':
    out, issues = adspage.build(CFG)
    print('built', out)
    for i in issues: print('  ISSUE', i)
    print('CLEAR' if not issues else '%d issue(s)' % len(issues))
