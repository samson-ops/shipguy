import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Montgomery, Alabama','Car shipping in the capital, where Interstate 85 begins and Interstate 65 runs through',
 ['Car shipping in Montgomery starts at the interchange downtown, where Interstate 85 begins its run to Atlanta. Ship Guy is a licensed auto transport broker with an office off the Eastern Boulevard.',
  'We book vetted carriers across the River Region, from Prattville to Pike Road and down to the plant. We do not own the trucks.',
  'Interstate 65 runs north and south through the west side on the way from Birmingham to Mobile. Interstate 85 leaves it downtown and runs northeast past the east side. The Eastern Boulevard is the loop and the retail strip. US 231 runs south to the beaches, and US 80 runs west to Selma.',
  'This page covers the two interstates, the Boulevard, downtown, the Garden District, the east side, and Prattville. It also covers the base, the state, the Korean plant, the colleges, the storms, and the lanes.'],
 'Montgomery at a glance',
 ['Most pickups happen within 1 to 3 days. Interstate 65 carries the Birmingham-to-Mobile carriers through the city all day.',
  'Birmingham, Atlanta, and Columbus are same-day lanes. Mobile and Huntsville are the same day too. Nashville, New Orleans, and Jacksonville take a day. Houston and Washington take two.'],
 'Tell us the neighborhood and the gate. Old Cloverdale, the Garden District, and downtown need a meeting spot. Dalraida, the east side, and Prattville usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 65, 85, the Eastern Boulevard, US 231, and the Interchange',
 prose(
  L('Montgomery is where one interstate ends and another passes through, and the carriers stage at the join.'),
  P('Interstate 65 runs north and south along the west side, from Prattville to Hope Hull and the plant. Interstate 85 begins at the interchange downtown and runs northeast toward Auburn and Atlanta. The ramps at Eastern Boulevard, Taylor Road, and Chantilly Parkway serve the east side. The interchange itself is the busiest spot in the state outside Birmingham.'),
  P('The Eastern Boulevard is the loop around the east side. It is the retail strip from the Atlanta Highway to the Southern Boulevard. The outer loop beyond it is half built. Taylor Road and Vaughn Road carry the newer east side. Zelda Road and Carter Hill Road reach the middle of the city.'),
  P('US 231 is the Troy Highway, the road south to Dothan and the Gulf beaches. US 80 is the Atlanta Highway east and the Selma Highway west. US 82 crosses the river to Prattville and runs on to Tuscaloosa. US 31 is the Mobile Highway. Maxwell Boulevard and Day Street reach the base gates, and Coliseum Boulevard reaches the annex.'),
  P('The carriers come off 65 at Fairview and the Southern Boulevard. Off 85, they use Eastern Boulevard and Taylor Road. The lots along the Eastern Boulevard and at EastChase are the usual meeting spots. No road in the River Region charges a toll.'),
  P('Our office sits on Kershaw Industrial Boulevard off the Eastern Boulevard, a few minutes from the 85 ramps.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the Garden District, Dalraida, the East Side, and Prattville',
 prose(
  L('Montgomery is a capital on a bluff, a ring of streetcar neighborhoods, and a growing east side.'),
  P('Downtown has Dexter Avenue running up to the Capitol, and the streets around Court Square are wide. A trailer can stop on Commerce Street or at the riverfront lots. The state office blocks fill with cars from February to May during the session. The driver meets you on Commerce or at the riverfront.'),
  P('The Garden District, Old Cloverdale, and Capitol Heights have old houses on narrow, tree-lined streets. The driver meets you on Fairview Avenue, on Carter Hill, or at a lot on Zelda Road. The college in Cloverdale has lots of its own. Highland Gardens and Chisholm on the north side are grids with room to stop.'),
  P('Dalraida, Forest Hills, and Normandale are postwar grids where the truck usually reaches the curb. McGehee Estates and Perry Hill have winding streets under pines, and the driver stays on Perry Hill Road. The base housing sits behind the gates, and the handoff happens on Maxwell Boulevard or Day Street.'),
  P('The east side along Taylor Road and Vaughn Road is subdivisions and gated communities. Wynlakes, Deer Creek, and Sturbridge meet the driver at the gate. The open subdivisions allow the curb. Pike Road beyond them has new streets and horse farms. Prattville and Millbrook across the river are open grids, and Prattville prices the same as the city.'),
 )))

ROUTES=[("Birmingham, AL","I-65 · ~90 mi","Same day","$150–$240"),("Atlanta, GA","I-85 · ~160 mi","Same day","$170–$280"),
 ("Columbus, GA","US-80 · ~90 mi","Same day","$150–$240"),("Mobile, AL","I-65 · ~170 mi","Same day","$190–$300"),
 ("Huntsville, AL","I-65 · ~190 mi","Same day","$200–$320"),("Nashville, TN","I-65 · ~290 mi","1 day","$280–$400"),
 ("New Orleans, LA","I-65/I-10 · ~300 mi","1 day","$280–$410"),("Jacksonville, FL","I-10 · ~370 mi","1 day","$340–$490"),
 ("Houston, TX","I-10 · ~600 mi","2 days","$460–$660"),("Washington, DC","I-85/I-95 · ~760 mi","2 days","$560–$800")]
BODY.append(rate_table('Lanes &amp; Costs','Montgomery Car Shipping Lanes and Estimated Costs',
 'Where River Region cars go most often, with estimated open-trailer ranges. The form above prices your exact route.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates out of Montgomery for a running sedan on an open trailer. Figure 10 to 25 percent more for an SUV or pickup, and more for enclosed. The class dates, the storms, and the carriers free on your dates set the final figure.',
 prose(
  P('Montgomery schedules faster than a city its size should, because the Korean plant keeps car carriers based here. Trucks that haul new cars out take private cars on the return run. The base keeps the Texas, Ohio, and Virginia lanes busy on the school calendar.'),
  P('Florida rides 65 and 10 all year. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','Maxwell, the Annex, the State, the Korean Plant, and the Colleges',
 prose(
  L('Montgomery relocates officers, state employees, plant engineers, and students, and the base runs on a school year.'),
  P('Maxwell Air Force Base hosts the officer schools. The classes start each summer and turn over through the year. Students, instructors, and their families arrive on class dates rather than random orders. The annex on the north side adds cyber and systems staff. The orders pay for one car, and the household’s other car rides with us.'),
  P('Since the gates stop the truck, the handoff happens on Maxwell Boulevard, Day Street, or the Boulevard. Ship Guy is a private broker and is not part of the base. Report-date timing is covered on the <a href="military-car-shipping.html">military</a> page.'),
  P('The state is the biggest employer in town, and the agencies hire on their own calendar. The session runs February through May, and the staff arrive before it. The insurer headquartered on the east side and the water heater plant relocate staff on start dates. We supply the paperwork a reimbursed move needs.'),
  P('The Korean plant south of the city and its suppliers relocate engineers on program schedules. The three hospitals bring in nurses and residents every summer. The university on the east side and the colleges downtown and in Cloverdale bring cars in each August. Auburn, an hour up 85, sends student cars in and out on the same calendar.'),
  P('Families arrive from Georgia and Florida for the plant jobs, and the second car usually rides a truck. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side of a move.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Session, Hurricane Remnants, Tornadoes, and the Heat',
 prose(
  L('Montgomery has a legislative calendar and a Gulf weather calendar, and both change where a truck can stop.'),
  P('The session runs from February into May, and downtown parking disappears on session days. A downtown pickup moves to the riverfront lots or the Boulevard. The fair fills the coliseum grounds for ten days in October. Game nights at the ballpark fill the riverfront on summer evenings.'),
  P('Hurricane remnants cross the River Region most years. Zeta in 2020 cut power across the city and brought down trees on every street. Opal in 1995 did the same. The carriers wait for the clearing crews. Pickups move to the lots on the Boulevard once the roads open.'),
  P('Tornado warnings and hail arrive with the spring, March through May. The driver waits out a warning before loading. Summer runs hot and humid from June through September, and the loading hour moves to early morning. Ice reaches the city a few times a decade and shuts the overpasses for a day.'),
  P('Game weekends at Auburn and in Tuscaloosa fill 85 and 65 on fall Saturdays. A carrier loses hours. We set fall pickups for weekdays when we can. The civil rights anniversaries in March close Dexter Avenue for the marches. A downtown handoff moves to the riverfront.'),
 )+chips(["Downtown","Dexter Avenue","Court Square","Riverfront","Cottage Hill","Garden District","Old Cloverdale","Capitol Heights","Highland Gardens","Chisholm","Dalraida","Forest Hills","Normandale","McGehee Estates","Perry Hill","Wynlakes","Deer Creek","Sturbridge","Halcyon","EastChase","Taylor Road","Vaughn Road","Pike Road","Maxwell","Gunter Annex","Hope Hull","Prattville","Millbrook","Wetumpka"])
 +NOTE('Serving Montgomery, Prattville, and the whole River Region. Name the neighborhood and the gate, and say whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Montgomery?',
 prose(
  L('Most cars leave the River Region on an open trailer, and the 65 lanes are priced that way.'),
  P('A closed trailer shields a car from pollen, hail, and curious eyes. Officers moving a restored car between schools tend to book one. The garages in Wynlakes and Old Cloverdale book them for the shows.'),
  P('A commuter car or a work truck travels open without an issue. See the <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages for the difference.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff on the Boulevard or outside the gate, and a delivery. The class date sets the week.'),
  P('When you approve the price, a carrier already on 65 or 85 is booked. The meeting spot and the window follow the same day. The driver walks the car with you and lists its condition on a Bill of Lading. You sign, the driver signs, and the sheet is checked again at delivery.'),
 )+ULI([
  "Empty the car of personal items",
  "Leave about a quarter tank of fuel",
  "Photograph the car before pickup, pollen and all",
  "Hand over a working key and mention any mechanical issue",
  "Disable any aftermarket alarm",
  "On base, plan to meet the truck outside the gate on Maxwell Boulevard",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages walk through the rest.'))))

BODY.append(sec('Why Ship Guy','Why Montgomery Drivers Choose Ship Guy',
 prose(
  L('We use the plant carriers that already work the River Region. We plan around the gates, the session, and the storms.'),
  P('Ship Guy is licensed by the FMCSA as a broker and bonded for $75,000. Both are a matter of federal record. Our office is on Kershaw Industrial Boulevard off the Eastern Boulevard.'),
  P('One coordinator follows your move from the quote to the delivery call. The <a href="services.html">services</a> page describes open, enclosed, and expedited transport.'),
 ), alt=True))

BODY.append(office('Montgomery','335 Kershaw Industrial Blvd #522','Montgomery, AL 36117','+13345424055','(334) 542-4055','CT',
 '335+Kershaw+Industrial+Blvd+%23522,+Montgomery,+AL+36117','Visit Us','Find Ship Guy in Montgomery',
 'Our office is on Kershaw Industrial Boulevard off the Eastern Boulevard, minutes from Interstate 85.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5182.304237136761!2d-86.1179902!3d32.3646448!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x888c2d50a98c10db%3A0x810f13a1a0fcb336!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792162612834!5m2!1sen!2sus'))

FAQ=[
 ("Do you handle a PCS move to Maxwell or the Gunter Annex?","Yes, on every class date. The orders cover one car, and the second one rides with us. Because the gates stop the truck, we meet you on Maxwell Boulevard, Day Street, or the Boulevard. The pickup is timed to your report date. Ship Guy is a private broker and is not affiliated with the base."),
 ("Why do Montgomery pickups schedule so fast?","Because the Korean plant keeps car carriers based in the city. The trucks that haul new cars out take private cars on the return run. Dealer transfers add to the flow. Interstate 65 brings the Birmingham and Mobile carriers through all day. A private pickup slots in easily."),
 ("How much does it cost to ship a car from Montgomery to Atlanta or Texas?","Atlanta runs one hundred seventy to two hundred eighty dollars for a sedan. That is about one hundred sixty miles up 85. Houston runs four hundred sixty to six hundred sixty, about six hundred miles out Interstate 10. The San Antonio training lane prices a little more. SUVs and pickups add 10 to 25 percent."),
 ("Can the carrier come to my street in Old Cloverdale or the Garden District?","Usually not. Those streets are narrow and lined with old trees, and a seventy-five-foot rig cannot turn there. The driver meets you on Fairview Avenue, on Carter Hill, or at a lot on Zelda Road. Dalraida, the east side, and Prattville usually allow the curb."),
 ("Can you ship a car to or from Prattville or Pike Road?","Yes, and both price the same as the city. Prattville and Millbrook ride the same 65 carriers, and Pike Road rides the 85 carriers. The lots along Cobbs Ford Road and at EastChase work for a handoff. Send the gate code for a gated community in Pike Road."),
 ("Does the legislative session affect my pickup?","Only downtown. Parking around the Capitol and the state offices disappears on session days from February into May. We move a downtown handoff to the riverfront lots or the Boulevard. The rest of the city runs normally."),
 ("Can you ship a car for an ASU, AUM, or Auburn student?","Yes. Cars arrive each August and leave each May, and both windows book up early. The campus lots downtown, on Taylor Road, and in Cloverdale work for the handoff. Auburn students meet the driver at a lot off Interstate 85. A parent or another adult has to sign at pickup."),
 ("What happens if a storm hits on my pickup day?","A tornado warning parks the driver until it lifts. When remnants like Zeta drop trees and cut power, the carriers wait for the clearing crews. An ice glaze closes the overpasses for a day. You hear from us before the window changes."),
 ("Can you ship a car that does not run from Montgomery?","Yes. A winch truck handles it, and the quote already includes the slower loading. A lot on the Eastern Boulevard or at EastChase gives the driver a flat spot. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Montgomery car shipping quote?","Both ends of the trip, with the gate or the neighborhood on the Montgomery side. The car’s year, make, and model, and whether it runs. Open or enclosed. A date range that works around the class date or the session. That is the whole request."),
]
BODY.append(faq_section(FAQ,'Montgomery FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Montgomery?','A price takes about two minutes on the form above. Tell us the gate or the neighborhood and your dates. A carrier already on 65 takes it from there.','+13345424055','(334) 542-4055','Get your free Montgomery quote'))

build({
 'slug':'auto-transport-montgomery-alabama',
 'title':'Car Shipping in Montgomery, AL — Auto Transport | Ship Guy',
 'meta':'Car shipping in Montgomery, AL where Interstate 85 begins and 65 runs through. Maxwell and Gunter second cars and gate handoffs, Garden District and downtown meeting spots, east side and Prattville curbside, Korean plant carriers, state and college relocations, session and storm planning. Local office off the Eastern Boulevard. Free quote.',
 'h1':'Car Shipping in<br>Montgomery, <span class="accent">Alabama</span>',
 'lede':'Open, enclosed, and expedited auto transport across the River Region, planned around 65, 85, the gates, and the storms.',
 'tel':'+13345424055','disp':'(334) 542-4055','brand':'Montgomery','keyword':'car shipping in montgomery',
 'localterms':['montgomery','interstate 65','interstate 85','interchange','eastern boulevard','outer loop','taylor road','vaughn road','zelda road','carter hill','us 231','troy highway','us 80','atlanta highway','selma','us 82','us 31','maxwell boulevard','day street','coliseum boulevard','fairview','southern boulevard','eastchase','downtown','dexter avenue','capitol','court square','commerce street','riverfront','garden district','old cloverdale','capitol heights','highland gardens','chisholm','dalraida','forest hills','normandale','mcgehee estates','perry hill','wynlakes','deer creek','sturbridge','pike road','prattville','millbrook','hope hull','maxwell','officer schools','annex','class dates','orders','report date','state','session','insurer','water heater','korean plant','suppliers','hospitals','nurses','residents','university','colleges','auburn','fair','ballpark','hurricane remnants','zeta','2020','opal','tornado','hail','humid','ice','game weekends','civil rights','birmingham','atlanta','columbus','mobile','huntsville','nashville','new orleans','jacksonville','houston','washington','texas','ohio','virginia','florida','georgia'],
}, BODY, FAQ)
