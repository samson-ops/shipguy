import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Tallahassee, Florida','Car shipping for the capital, two campuses, and the canopy roads a trailer cannot use',
 ['Car shipping in Tallahassee moves on the legislative calendar, the university calendar, and one interstate that runs along the top of the city.',
  'Ship Guy is a licensed auto transport broker with an office on East Tennessee Street between downtown and the campus. We book vetted carriers across the Big Bend, and we do not own the trucks.',
  'Interstate 10 crosses the north side of the city between Pensacola and Jacksonville, and Capital Circle loops everything else. No interstate reaches the city from the south, so the Gulf side of the region takes an extra day.',
  'This page covers the interstate and the loop, the Capitol and the session, the two universities, the canopy roads and the hills, the Big Bend after the storms, and the lanes in every direction.'],
 'Tallahassee at a glance',
 ['Most pickups happen within 1 to 3 days, with Interstate 10 bringing carriers past the city all day.',
  'Jacksonville, Gainesville, Panama City, and Thomasville are same-day lanes. Atlanta, Tampa, and Orlando take a day. New York and Chicago run three.'],
 'Tell us if your address sits on a canopy road. Live oaks over Miccosukee, Meridian, Old Bainbridge, and Centerville Roads hang too low for a trailer, and the driver meets you on Capital Circle instead.'))

BODY.append(sec('Interstate 10 &amp; Capital Circle','How Carriers Reach a City With One Interstate',
 prose(
  L('Every carrier between Jacksonville and the Gulf Coast passes the top of Tallahassee, and the loop road carries them the rest of the way.'),
  P('Interstate 10 runs along the north side with exits at Thomasville Road, Monroe Street, and Capital Circle. Capital Circle loops the city, and US 27, US 90, and US 319 run through it to the outer counties.'),
  P('Tennessee Street is US 90, and it carries the campus and downtown traffic east and west. Apalachee Parkway runs from the Capitol toward Monticello, and Thomasville Road runs north past Killearn to the Georgia line.'),
  P('Nothing reaches the city from the south but US 319 and 27 on two lanes. Crawfordville, Saint Marks, and the coast take an extra day, and the driver meets you on the US highway.'),
  P('Fog settles onto Interstate 10 on fall and winter mornings, and a smoke advisory from a controlled burn closes it a few times a year. Carriers wait it out at the truck stops in Midway or Monticello.'),
 ), alt=True))

BODY.append(sec('The Capitol','The Session, the Agencies, and the People Who Move on Them',
 prose(
  L('Tallahassee empties and fills twice a year on the state\u2019s schedule.'),
  P('The legislative session runs sixty days each spring, and staff, lobbyists, and press arrive in January and leave in March. Many bring a car for the session and ship it home after, and downtown parking runs on garages a trailer cannot enter.'),
  P('The state agencies along Capital Circle and in the Capitol complex relocate employees on start dates all year. The driver meets downtown addresses on Monroe Street or Tennessee Street.'),
  P('If your agency or employer reimburses the shipment, we provide the documentation. The interstate side of a relocation is on the <a href="state-to-state-car-shipping.html">state-to-state</a> page.'),
 )))

ROUTES=[("Jacksonville, FL","I-10 · ~165 mi","Same day","$220–$340"),("Gainesville, FL","I-10/I-75 · ~150 mi","Same day","$200–$320"),
 ("Panama City, FL","US-98/US-231 · ~100 mi","Same day","$180–$290"),("Pensacola, FL","I-10 · ~195 mi","Same day","$220–$340"),
 ("Tampa, FL","I-75 · ~240 mi","1 day","$260–$390"),("Orlando, FL","I-75/FL Tpke · ~255 mi","1 day","$260–$390"),
 ("Atlanta, GA","I-75 · ~270 mi","1 day","$270–$400"),("Mobile, AL","I-10 · ~250 mi","1 day","$260–$390"),
 ("New Orleans, LA","I-10 · ~390 mi","1–2 days","$350–$500"),("Miami, FL","I-75/FL Tpke · ~480 mi","2 days","$400–$570")]
BODY.append(rate_table('Lanes &amp; Costs','Tallahassee Car Shipping Lanes and Estimated Costs',
 'The lanes Big Bend households ask about most, with estimated open-transport ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates, running sedan, open trailer. SUVs and pickups run about 10 to 25 percent more, enclosed more still. The session and the campus windows push short lanes up, and carrier availability on your dates sets the real quote.',
 prose(
  P('Interstate 10 makes the Gulf Coast and Jacksonville easy in both directions, and Interstate 75 puts Atlanta a day away. Tallahassee sits closer to Georgia and Alabama than to South Florida.'),
  P('The South Florida lanes cost a little more per mile because they leave the interstate. The <a href="car-shipping-cost.html">cost guide</a> explains the rest of the number.'),
 ), alt=True))

BODY.append(sec('Two Universities','Florida State, FAMU, and the August Crush',
 prose(
  L('Florida State and Florida A&amp;M sit a mile apart, and they fill the city in the same week.'),
  P('Move-in runs the third week of August for both, and move-out runs the first week of May. The student complexes along Tennessee Street, Ocala Road, and Pensacola Street have tight lots, so the driver meets you at a shopping center lot nearby.'),
  P('Home football Saturdays close the streets around the stadium from midmorning, and the FAMU homecoming weekend fills the south side each fall. We schedule the campus side for weekdays through the season.'),
  P('An adult signs for a student car, and a parent can sign at the far end. Tallahassee Community College on the west side adds a smaller wave on the same dates.'),
 )))

BODY.append(sec('The Canopy Roads &amp; the Hills','Where a Trailer Cannot Go, and Where It Can',
 prose(
  L('Tallahassee is the hilliest city in Florida, and it protects its oaks by law.'),
  P('The canopy roads are lined with live oaks that arch over the pavement, and the branches hang too low for a seventy-five-foot trailer. Miccosukee, Meridian, Old Bainbridge, Centerville, and Saint Augustine Roads all qualify, and so do the streets of Betton Hills and Midtown.'),
  P('For a canopy address, the driver meets you on Capital Circle, Thomasville Road, or a nearby shopping center. It is a few minutes from the house.'),
  P('Killearn, Golden Eagle, and the north side are wide and open, though the golf communities have gates. SouthWood on the southeast side is a master-planned community with wide streets and homeowners association rules for trucks.'),
  P('Our office is on East Tennessee Street between downtown and the campus, with Interstate 10 ten minutes north.'),
 ), alt=True))

BODY.append(sec('The Big Bend &amp; the Storms','The Coast, the Bases, and the Rebuilding',
 prose(
  L('The Big Bend has taken three hurricanes in a decade, and the region is still rebuilding from the last one.'),
  P('The 2024 storm crossed the coast at Perry and tore through Taylor and Madison Counties, and the 2018 storm flattened the Panhandle from Mexico Beach to Marianna. Contractors, adjusters, and families ship trucks and cars into the region on the rebuilding schedule.'),
  P('Hurricane season runs June through November, and Interstate 10 is the evacuation and supply route. Carriers clear the coast days before a landfall, and after a storm they return with the utility crews.'),
  P('Tyndall Air Force Base near Panama City is being rebuilt as a new fighter base and rotates airmen on that schedule. Moody Air Force Base sits an hour north at Valdosta. Ship Guy is a private broker with no military affiliation, and our <a href="military-car-shipping.html">military</a> page covers PCS timing.'),
  P('Thomasville, Bainbridge, and Cairo across the Georgia line ship through the Tallahassee carrier pool.'),
 )+chips(["Downtown","Midtown","Betton Hills","Killearn","Golden Eagle","SouthWood","Frenchtown","Southside","Lake Jackson","Bradfordville","Crawfordville","Saint Marks","Quincy","Havana","Monticello","Perry","Panama City","Thomasville","Bainbridge"])
 +NOTE('Serving Leon, Gadsden, Wakulla, Jefferson, and the Big Bend counties, plus the Georgia line. Tell us if your street is a canopy road.')))

BODY.append(sec('Your Options','Open or Enclosed in Tallahassee?',
 prose(
  L('Open transport is the everyday choice, and the campus and Capitol lanes run on it.'),
  P('Enclosed transport keeps a car covered against pollen, storm debris, and grit. Killearn and Golden Eagle keep enclosed carriers busy with collector cars.'),
  P('A student or commuter car rides open without concern. Our <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain both.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff where the oaks allow it, and a delivery, with the calendar setting the timing.'),
  P('When the price is approved, a carrier on Interstate 10 takes the booking. The driver marks the car\u2019s condition on a Bill of Lading, and you sign it before loading. That form is your reference at delivery.'),
 )+ULI([
  "Remove personal belongings",
  "Keep about a quarter tank of fuel",
  "Photograph the vehicle before pickup",
  "Provide a working key and disclose mechanical issues",
  "Turn off aftermarket alarms",
  "For a canopy road or a gated community, plan to meet the truck on the main road",
 ])+prose(P('Our <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> guides cover each step.'))))

BODY.append(sec('Why Ship Guy','Why Tallahassee Drivers Choose Ship Guy',
 prose(
  L('We know the session dates, the move-in weeks, and every road the oaks close to a truck.'),
  P('Active FMCSA brokerage authority and a $75,000 surety bond stand behind every Ship Guy booking, and our office is on East Tennessee Street.'),
  P('One coordinator carries the shipment from quote to delivery and sets up open, enclosed, or expedited transport. The <a href="services.html">services</a> page has the whole menu.'),
 ), alt=True))

BODY.append(office('Tallahassee','541 E Tennessee St Ste 198','Tallahassee, FL 32308','+18508053761','(850) 805-3761','ET',
 '541+E+Tennessee+St+Ste+198,+Tallahassee,+FL+32308','Visit Us','Find Ship Guy in Tallahassee',
 'Our office is on East Tennessee Street between downtown and the campus, with Interstate 10 ten minutes north.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4245.887117010706!2d-84.2752008!3d30.444434700000006!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x88ecf5dd3cb5b5ef%3A0x293bd30e9c87741c!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1790274831399!5m2!1sen!2sus', map_link='https://maps.app.goo.gl/renq8nDrfCuiWcKv9'))

FAQ=[
 ("My street is a canopy road. Can the carrier reach my house?","No, the live oaks over Miccosukee, Meridian, Old Bainbridge, Centerville, and Saint Augustine Roads hang too low for a trailer. The same goes for Betton Hills and Midtown. The driver meets you on Capital Circle, Thomasville Road, or a nearby shopping center, a few minutes from the house."),
 ("Can you ship a car for the legislative session?","Yes, and many staff and lobbyists do. The session runs sixty days each spring, so cars arrive in January and leave in March. Downtown parking runs on garages a trailer cannot enter, so the driver meets you on Monroe or Tennessee Street. Book two to three weeks ahead of the session."),
 ("When should I book a car for an FSU or FAMU student?","In July for the August move-in and in April for the May move-out. Both schools fill the city in the same week, and the complexes along Tennessee Street and Ocala Road have tight lots. The driver meets you at a shopping center lot nearby, and an adult signs for the car."),
 ("How much does it cost to ship a car from Tallahassee to Atlanta?","Usually two hundred seventy to four hundred dollars for a sedan riding open. Interstate 75 carries most of the trip, about two hundred seventy miles, and Atlanta is a day away. Larger vehicles and enclosed add to it."),
 ("Do you serve the Big Bend coast and the areas hit by the hurricanes?","Yes, Perry, Taylor County, and the Panhandle towns are covered from this page. Contractors and families ship trucks and cars into the region on the rebuilding schedule. The coast sits on two-lane US highways, so plan on an extra day and a handoff in town."),
 ("Can you handle a PCS move to Tyndall or Moody?","Yes, Tyndall near Panama City is being rebuilt and rotates airmen on that schedule, and Moody sits an hour north at Valdosta. Housing is gated, so the driver meets you outside it. Many families ship a second vehicle through us, since orders may cover only one. Ship Guy has no military affiliation."),
 ("Why can Interstate 10 close near Tallahassee?","Fog settles onto the interstate on fall and winter mornings, and smoke from a controlled burn closes it a few times a year. Carriers wait it out at the truck stops in Midway or Monticello. A pickup can slide a few hours, and we tell you when it does."),
 ("Do you serve Thomasville and the Georgia side?","Yes, Thomasville, Bainbridge, and Cairo ship through the Tallahassee carrier pool. The Georgia line is thirty minutes north on Thomasville Road, and the plantation country between has private roads. The driver meets you at the gate or in town."),
 ("Can you ship a car that does not run from Tallahassee?","Yes, non-running cars ship out of Tallahassee regularly. A winch-equipped carrier loads it, and the added time carries a fee. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Tallahassee car shipping quote?","The pickup and delivery addresses, with a note if the street is a canopy road. The year, make, and model. Whether it runs and rolls. Open or enclosed, and your dates. That is everything an accurate Tallahassee quote needs."),
]
BODY.append(faq_section(FAQ,'Tallahassee FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Tallahassee?','A quote takes about two minutes on our form. Then tell us your street and your dates, and we will plan around the oaks, the session, and the semester.','+18508053761','(850) 805-3761','Get your free Tallahassee quote'))

build({
 'slug':'auto-transport-tallahassee-florida',
 'title':'Car Shipping in Tallahassee, FL — Auto Transport | Ship Guy',
 'meta':'Car shipping in Tallahassee, FL on Interstate 10 and Capital Circle. Legislative session timing, FSU and FAMU move-in, canopy-road handoffs, Big Bend rebuilding, Tyndall and Moody moves, Georgia-line pickups. Local office on East Tennessee Street. Free quote.',
 'h1':'Car Shipping in<br>Tallahassee, <span class="accent">Florida</span>',
 'lede':'Open, enclosed, and expedited auto transport across the Big Bend, planned around the Capitol, the campuses, and the canopy roads.',
 'tel':'+18508053761','disp':'(850) 805-3761','brand':'Tallahassee','keyword':'car shipping in tallahassee',
 'localterms':['tallahassee','big bend','leon','interstate 10','capital circle','tennessee street','monroe street','thomasville road','apalachee parkway','us 319','us 27','us 90','canopy','live oak','miccosukee','meridian','old bainbridge','centerville','capitol','session','legislature','agencies','lobbyists','florida state','fsu','famu','homecoming','move-in','killearn','golden eagle','southwood','betton hills','midtown','frenchtown','crawfordville','saint marks','perry','hurricane','panama city','tyndall','moody','valdosta','thomasville','bainbridge','fog','smoke','midway','monticello'],
}, BODY, FAQ)
