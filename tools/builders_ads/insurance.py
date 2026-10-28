#!/usr/bin/env python3
"""Google Ads landing page: Car Shipping Insurance  ->  /vehicle-quote-car-shipping-insurance
(main line (866) 297-3244). Built from the live /vehicle-quote page by adspage.build().
Coverage statements follow the site's own wording (faq.html, services.html, terms.html, enclosed-auto-transport.html):
the carrier's cargo insurance covers the car on the truck, Ship Guy verifies it and helps with claims, the Bill of
Lading preserves a claim, personal items are not covered, enclosed carriers carry higher limits. No dollar limits."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import adspage

TEL = '+18662973244'
CALL = '<a data-track="call-tip" href="tel:%s">(866) 297-3244</a>' % TEL
CFG = dict(
    slug='vehicle-quote-car-shipping-insurance', city='Insurance', st='US', lead_prefix='ADS-INS',
    tel=TEL, disp='(866) 297-3244', disp_nbsp='(866)&nbsp;297-3244',

    title='Car Shipping Insurance, Explained | Instant Quote | Ship Guy',
    meta="How car shipping insurance works: the carrier's cargo coverage in your quote, the Bill of Lading, claims, and what is not covered. Call (866) 297-3244.",

    eyebrow='Car Shipping Insurance &middot; Included in Every Quote',
    variants={
        'default':  ['Car Shipping Insurance', 'Explained · Instant ', 'Quote'],
        'insured':  ['Fully Insured Car Shipping', 'Instant ', 'Quote'],
        'damage':   ['What If My Car Is Damaged?', 'Instant ', 'Quote'],
        'claims':   ['Car Shipping Claims, Explained', 'Instant ', 'Quote'],
        'enclosed': ['Enclosed, Insured Car Shipping', 'Instant ', 'Quote'],
        'luxury':   ['Insured Luxury Car Shipping', 'Instant ', 'Quote'],
    },
    lede=('Ship Guy is a licensed auto transport broker, and every carrier we book carries active cargo insurance. '
          'Your car is covered while it is on the truck, and the coverage is included in your quote. '
          'Here is how it works.'),
    badges=[
        ('shield', 'Covered while on the truck', 'Carrier cargo insurance, verified before pickup'),
        ('doc',    'Inspection report at both ends', 'The Bill of Lading protects your claim'),
        ('bolt',   'Price on screen in 30 seconds', 'Coverage included, no hidden fees'),
    ],
    pq_sub='Insured pricing in 30 seconds. Free, no obligation.',

    reviews_sub='Trusted by vehicle owners nationwide.',

    table_eyebrow='What Is Covered',
    table_h2='What Car Shipping Insurance Covers',
    table_sub="The carrier's cargo insurance in plain terms. Ask us for the coverage details before you book.",
    table_cols=['Situation', 'Covered?', 'What to know'],
    table_hide_m=None,
    table_rate_col=False,
    table_rows=[
        ('Damage caused in loading, transit, or unloading', "Yes, by the carrier's cargo insurance", 'Note it on the Bill of Lading at delivery and report it promptly'),
        ('Weather and road debris on an open trailer', 'Depends on the cause and the policy', 'Open cars arrive dusty by nature. Enclosed keeps a car sealed from the elements'),
        ('Personal items left in the car', 'No', 'Carriers move vehicles, not household goods. Keep the car empty'),
        ('Pre-existing scratches and dents', 'No', 'They are recorded on the Bill of Lading at pickup, with your photos'),
        ('Mechanical problems not caused by transport', 'No', 'A dead battery or a leak is noted at pickup and disclosed to the driver'),
        ('Enclosed and high-value vehicles', 'Yes, with higher limits', 'Enclosed carriers carry higher coverage limits for collector cars'),
    ],
    table_foot=("Ship Guy is a broker, so the carrier and its insurer handle claims for transport damage. "
                "We verify every carrier's coverage before pickup and help you communicate a claim."),
    table_note=('Your own auto policy may add coverage during shipping, so check with your insurer before pickup. '
                'For a collector or high-value car, enclosed transport is the standard.'),

    cards_eyebrow='How Claims Work',
    cards_h2='How to Protect Your Car and Your Claim',
    cards_sub='Four habits that make a claim simple if anything ever goes wrong.',
    cards=[
        ('doc',    'Photos before pickup', 'Wash the car and take date-stamped photos of every panel, the wheels, and the interior. Existing marks are then easy to tell apart from anything new.'),
        ('shield', 'The Bill of Lading at pickup', 'The driver inspects the car with you and records its condition on the Bill of Lading. Read it before you sign, and keep your copy.'),
        ('clock',  'Inspect at delivery, before you sign', 'Walk around the car in good light and compare it against the pickup report and your photos. Any new damage goes on the Bill of Lading before you sign.'),
        ('truck',  'Report it promptly', "Call us the same day with the signed report and photos. The carrier's insurer handles the claim, and we help you communicate it from start to finish."),
    ],
    chips=['Active cargo insurance', 'Verified before pickup', 'Included in your quote', 'Bill of Lading at both ends', 'Date-stamped photos', 'Licensed, bonded broker',
           'FMCSA MC #1457715', 'Enclosed for collector cars', 'Claims help from Ship Guy', 'Personal items not covered'],
    chips_cap='What every shipment includes, and the one thing it does not.',
    tip=('<b>Good to know.</b> Signing the Bill of Lading at delivery without noting damage can limit a claim. '
         'Take two minutes to inspect in good light, and call %s if anything looks off.' % CALL),

    how_h2='Insured Car Shipping in 3 Simple Steps',
    how_sub='From quote to delivery, Ship Guy keeps car shipping simple, transparent, and insured.',
    how_steps=[
        ('Get Your Instant Quote', "Enter your ZIPs, vehicle, and timeframe. Your price appears on screen in about 30 seconds, with the carrier's coverage included."),
        ('Book an Insured Carrier', 'We assign a vetted carrier with active cargo insurance and confirm a pickup window. Ask us for the coverage details any time before pickup.'),
        ('Inspect, Sign, Deliver', "The driver records the car's condition on the Bill of Lading at pickup and again at delivery. You compare, sign off, and drive away."),
    ],

    why_h2='Why Careful Owners Ship with Ship Guy',
    why_sub='A licensed, insured brokerage that treats your vehicle, and your time, like it matters.',
    why_support='Real representatives by phone to answer every coverage question.',

    faq_h2='Car Shipping Insurance Questions',
    faq_sub='What people ask about coverage before they book.',
    faq=[
        ('Is my car insured during shipping?',
         'Yes. Every carrier we book is verified for active cargo insurance before pickup. Your car is covered while it is on the truck. '
         'That coverage is included in your quote, and we share the details before you book.'),
        ('Who pays if my car is damaged in transit?',
         'The carrier and its insurer. Ship Guy is a broker and does not insure the car itself. We verify the coverage and help you communicate the claim. '
         'Damage noted on the Bill of Lading at delivery and reported promptly is what preserves it.'),
        ('What is the Bill of Lading and why does it matter?',
         'It is the inspection report the driver completes with you at pickup and again at delivery. It records the condition of the car at both ends, and a claim rests on it. '
         'Read it before you sign, note any new damage at delivery, and keep your copy.'),
        ('Are personal items in the car covered?',
         'No. Carriers are licensed to move vehicles, not household goods, so belongings left inside are not insured. Keep the car empty apart from the usual items in the trunk and glovebox.'),
        ('Does enclosed transport come with more coverage?',
         'Yes. Enclosed carriers carry higher coverage limits and load fewer cars per trip. It is the standard for classic, exotic, and high-value vehicles.'),
        ("Can I see the carrier's insurance before pickup?",
         'Yes. Ask us before you book or any time before pickup, and we share what the assigned carrier carries.'),
        ('Does my own auto insurance cover shipping?',
         "Sometimes. Some personal policies add coverage while the car is in transit, so check with your insurer before pickup. The carrier's cargo insurance is the primary coverage either way."),
        ('Is Ship Guy a carrier or a broker?',
         'Ship Guy is a licensed, bonded auto transport broker, FMCSA MC #1457715. We do not own trucks. '
         'We book vetted carriers with active insurance, and your car is covered while it is on the truck.'),
        ('What happens after I get my quote?',
         'Your price appears on screen. Book online right there or call <a data-track="call-faq" href="tel:%s">(866) 297-3244</a> to lock in a pickup window. '
         'The driver inspects the car at pickup, and you sign off at delivery.' % TEL),
    ],

    cta_h2='Ready to Ship, Fully Covered?',
    cta_sub='Get your free quote in about 30 seconds, or call and ask us anything about coverage.',
    cta_btn='Get My Free Quote',
    cta_trust3='Coverage included in every quote',
    foot_tag='Licensed, bonded &amp; insured car shipping to all 50 states. Transparent pricing, vetted carriers, door to door.',
    foot_serving='Serving all 50 states',
)

if __name__ == '__main__':
    out, issues = adspage.build(CFG)
    print('built', out)
    for i in issues: print('  ISSUE', i)
    print('CLEAR' if not issues else '%d issue(s)' % len(issues))
