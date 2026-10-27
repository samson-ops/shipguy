import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Savannah, Georgia','Car shipping where Interstate 16 meets Interstate 95, between the port and the squares',
 ['Car shipping in Savannah starts at the interchange west of the city, where Interstate 16 meets Interstate 95. Ship Guy is a licensed auto transport broker with an office off Chatham Parkway.',
  'We book vetted carriers across the coast, from Port Wentworth to Richmond Hill and out to Tybee. We do not own the trucks.',
  'Interstate 95 runs north and south west of the city, from the Carolina line to Richmond Hill. Interstate 16 comes in from Macon and ends downtown. Interstate 516 loops through the middle to the port. Abercorn Street and the Truman Parkway carry the south side.',
  'This page covers the interstates, the loop, the squares, the islands, the Southside, and the suburbs. It also covers the port, the airfield, the jet plant, the auto plant, the hurricanes, and the lanes.'],
 'Savannah at a glance',
 ['Most pickups happen within 1 to 3 days. Interstate 95 carries the Northeast-to-Florida carriers past the city all day.',
  'Jacksonville, Charleston, and Macon are same-day lanes. Augusta is the same day too. Atlanta, Charlotte, and Orlando take a day. Washington and New York take two.'],
 'Tell us the neighborhood. The Historic District, Ardsley Park, and the islands need a meeting spot. Pooler, Richmond Hill, and the Southside usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 95, 16, 516, Abercorn Street, and the Truman Parkway',
 prose(
  L('Savannah sits a few miles east of the coast’s main artery. One interstate carries the city to it.'),
  P('Interstate 95 passes west of the city through Pooler and Richmond Hill. Interstate 16 leaves it at the interchange and runs ten miles east into downtown. The ramps at Chatham Parkway, Lynes Parkway, and Montgomery Street are the way in. The interchange itself has been rebuilt with new flyovers.'),
  P('Interstate 516 is the Lynes Parkway, the loop from 16 north to the port terminals in Garden City. Dean Forest Road and the Jimmy DeLoach Parkway carry the port trucks to 95 without touching the city. US 17 crosses the river on the Talmadge Bridge into South Carolina. The bridge is being replaced, and the lanes shift.'),
  P('Abercorn Street is the long strip south through the Southside to the islands. The Truman Parkway runs beside it from downtown to Whitemarsh. US 80 is Victory Drive, and it is the only road to Tybee Island. The Islands Expressway and the Diamond Causeway reach Wilmington Island and Skidaway. DeRenne Avenue crosses the middle.'),
  P('The carriers come off 95 at Pooler Parkway and at Richmond Hill, and off 16 at Chatham Parkway. The lots along Chatham Parkway, at the outlets in Pooler, and on Abercorn are the usual meeting spots. No road on the coast charges a toll.'),
  P('Our office sits on Park of Commerce Way off Chatham Parkway, a minute from the Interstate 16 ramps.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','The Historic District, Ardsley Park, the Southside, the Islands, and Pooler',
 prose(
  L('Savannah is a grid of squares, a ring of oak-lined avenues, and a flat Southside. The marsh islands sit beyond.'),
  P('The Historic District is built around twenty-two squares and cobblestone lanes, and the city restricts trucks on them. A trailer cannot enter. The driver meets you on Martin Luther King Boulevard, on Liberty Street, or at a lot off 16. The Victorian District and Starland south of Forsyth Park have the same answer.'),
  P('Ardsley Park, Baldwin Park, and Parkside have wide medians and old oaks. The low branches stop a tall trailer. The driver meets you on Victory Drive or Habersham Street. Midtown along DeRenne has apartment complexes with room to stop. The hospital campuses along Waters and Reynolds have garages and wide lots.'),
  P('The Southside along Abercorn is flat grids, apartment complexes, and shopping centers. The truck usually reaches the curb. Windsor Forest and Georgetown are postwar grids with the same answer. Isle of Hope has oak-lined lanes, and the handoff happens on Skidaway Road. Skidaway Island is gated, and the driver meets you at the gate on the causeway.'),
  P('Wilmington Island and Whitemarsh have subdivisions with wide streets, and the curb works on most. Tybee Island has one road in, narrow streets, and summer traffic, so the handoff happens on Victory Drive. Pooler, Port Wentworth, and Richmond Hill are new subdivisions with gates on some entrances. Garden City and Thunderbolt are open grids.'),
 )))

ROUTES=[("Jacksonville, FL","I-95 · ~140 mi","Same day","$170–$270"),("Charleston, SC","US-17/I-95 · ~110 mi","Same day","$160–$260"),
 ("Macon, GA","I-16 · ~165 mi","Same day","$190–$300"),("Augusta, GA","SR-21/US-25 · ~130 mi","Same day","$170–$270"),
 ("Atlanta, GA","I-16/I-75 · ~250 mi","1 day","$240–$360"),("Charlotte, NC","I-95/I-26/I-77 · ~250 mi","1 day","$240–$360"),
 ("Orlando, FL","I-95/I-4 · ~280 mi","1 day","$260–$390"),("Raleigh, NC","I-95 · ~350 mi","1 day","$320–$460"),
 ("Washington, DC","I-95 · ~570 mi","1–2 days","$450–$650"),("New York, NY","I-95 · ~800 mi","2 days","$600–$860")]
BODY.append(rate_table('Lanes &amp; Costs','Savannah Car Shipping Lanes and Estimated Costs',
 'The lanes that leave the coast most, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a running sedan on an open trailer, priced from Savannah. SUVs and pickups add about 10 to 25 percent, and enclosed adds more. Hurricane season, the snowbird months, and the carriers free on your dates set the final price.',
 prose(
  P('Savannah prices like Jacksonville, because the same 95 carriers pass both an hour apart. The Northeast lanes run full in both snowbird seasons. Atlanta rides 16 and 75, and the inland lanes price a little higher than the coast.'),
  P('The airfield and the fort keep the Texas, Kentucky, and Washington State lanes busy with every rotation. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Port, the Airfield, the Jet Plant, the Auto Plant, and the Art School',
 prose(
  L('Savannah relocates longshoremen, soldiers, engineers, and art students, and the new plant added a fifth calendar.'),
  P('The port in Garden City is one of the largest container ports in the country. The terminal by the bridge handles imported cars. We ship a car domestically once customs releases it, and the ocean leg is separate. The port and the logistics companies around it relocate managers all year.'),
  P('The Army airfield inside the city and the fort in Hinesville deploy and return whole brigades. Families rotate in on orders, with a summer peak. Orders cover one car, and the second one comes with us. The gates stop the truck, so the handoff happens on Montgomery Street or in Hinesville. Ship Guy is a private broker with no connection to either post. The <a href="military-car-shipping.html">military</a> page covers the timing.'),
  P('The jet plant at the airport is the largest private employer on the coast. It hires engineers on program schedules. The new electric-vehicle plant west of the city and its suppliers are hiring by the thousand. Those workers relocate on hiring schedules from across the country, and the handoff works at the Pooler outlets.'),
  P('The art school downtown brings students in each September and sends them out each spring. The university campus on Abercorn and the state university in Thunderbolt bring cars in each August. The hospitals bring in residents each June. An adult signs for a student car, and the handoff happens at a lot near campus.'),
  P('Retirees arrive from the Northeast for the islands and Richmond Hill. The second car usually rides a truck. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Hurricanes, King Tides, St. Patrick’s Day, and the Heat',
 prose(
  L('Savannah plans its year around the storm season and one green weekend in March.'),
  P('Hurricane season runs June through November. Matthew in 2016 and Irma in 2017 flooded the islands and downed trees across the city. Debby in 2024 dropped a foot of rain and flooded the Southside. When an evacuation is ordered, the carriers leave up 16 before the lanes reverse. We reschedule once the roads reopen.'),
  P('King tides flood Victory Drive to Tybee and the island causeways a few times each fall. A pickup on the islands moves to the mainland until the tide drops. Summer afternoons bring thunderstorms, and the loading hour moves to the morning in July and August. The humidity sits on the coast all summer.'),
  P('St. Patrick’s Day brings one of the biggest parades in the country, and downtown closes for days. The music festival in spring and the film festival in fall fill the squares. A pickup downtown in those weeks moves to the Chatham Parkway lots. Beach traffic jams Victory Drive every summer weekend.'),
  P('Snow is rare, but the 2018 and 2025 storms each shut the coast for a day. Ice on the Talmadge Bridge closes it. The pollen turns every car yellow in March. Move-in at the art school fills downtown in September.'),
 )+chips(["Historic District","River Street","Victorian District","Starland","Thomas Square","Forsyth Park","Ardsley Park","Baldwin Park","Parkside","Midtown","Southside","Windsor Forest","Georgetown","Isle of Hope","Skidaway Island","The Landings","Wilmington Island","Whitemarsh Island","Tybee Island","Thunderbolt","Garden City","Port Wentworth","Pooler","Bloomingdale","Richmond Hill","Rincon","Hinesville","Bluffton"])
 +NOTE('Serving Savannah and the whole coast, from the Carolina line to Richmond Hill. Tell us the neighborhood, the gate, and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Savannah?',
 prose(
  L('Open is how the coast ships, and the 95 lanes are priced for it.'),
  P('An enclosed trailer keeps the salt air, the pollen, and attention off a car. The garages on Skidaway and in Ardsley Park book them for collector cars. So does a high-value import released from the port.'),
  P('A daily driver rides open without a problem. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain what the roof buys you.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff on Chatham Parkway or at the Pooler outlets, and a delivery. The tide and the season set the day.'),
  P('Approve the price, and a carrier already on 95 takes the booking. We confirm the spot and the window the same day. The driver walks around the car with you and records its condition on a Bill of Lading. You both sign it, and the same sheet comes out at delivery.'),
 )+ULI([
  "Empty the car of personal items",
  "Leave about a quarter tank of fuel",
  "Photograph the car before the handoff, salt and pollen included",
  "Hand over a working key and mention any mechanical issue",
  "Disable any aftermarket alarm",
  "Downtown or on a gated island, pick a lot or the gate where the truck can stop",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Savannah Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already run 95 past the city. We plan around the squares, the gates, the tides, and the storms.'),
  P('Ship Guy holds active brokerage authority with the FMCSA, backed by a $75,000 surety bond. Both are on file in the federal register. Our office is on Park of Commerce Way off Chatham Parkway.'),
  P('One coordinator handles your shipment from the first quote to the delivery signature. Open, enclosed, and expedited transport are all on offer, and the <a href="services.html">services</a> page lists each one.'),
 ), alt=True))

BODY.append(office('Savannah','49 Park of Commerce Way #445','Savannah, GA 31405','+19124552132','(912) 455-2132','ET',
 '49+Park+of+Commerce+Way+%23445,+Savannah,+GA+31405','Visit Us','Find Ship Guy in Savannah',
 'Our office is on Park of Commerce Way off Chatham Parkway, a minute from the Interstate 16 ramps.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5199.421391672142!2d-81.1649305!3d32.06479110000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x88fba1a037e915cf%3A0x7f3b3f53d3dc17a1!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792162218014!5m2!1sen!2sus'))

FAQ=[
 ("Can the carrier come to my house in the Historic District?","No. The city restricts trucks around the squares, and a seventy-five-foot trailer could not turn on the lanes anyway. The driver meets you on Martin Luther King Boulevard, on Liberty Street, or at a lot off 16. It is minutes from any square. Pooler and the Southside allow the curb."),
 ("Can you ship a car that arrived at the Port of Savannah?","Once customs releases it, yes. The ocean leg and the customs process are separate, and we do not handle them. Give us the release date and the terminal, and a carrier picks the car up at the gate. Enclosed transport suits a high-value import."),
 ("How much does it cost to ship a car from Savannah to New York or Atlanta?","New York runs six hundred to eight hundred sixty dollars for a sedan. That is about eight hundred miles up 95. Atlanta runs two hundred forty to three hundred sixty, about two hundred fifty miles on 16 and 75. Snowbird season lifts the Northeast price in spring and fall. SUVs and pickups add 10 to 25 percent."),
 ("Do you handle a PCS move to Hunter Army Airfield or Fort Stewart?","Yes, on every rotation, with the peak in summer. Orders cover one car, and the second one comes with us. The gates stop the truck, so we meet you on Montgomery Street or at a lot in Hinesville. We schedule around your report date. Ship Guy is a private broker with no connection to either post."),
 ("What happens if a hurricane is forecast during my shipment?","The carriers leave the coast before the evacuation lanes reverse on Interstate 16. Nothing moves on the coast until the order lifts and the roads are cleared. We reschedule the moment they reopen, and we call you at every step. A car already on a trailer keeps moving inland."),
 ("Can you pick up on Tybee Island or Skidaway Island?","Yes, with a meeting spot. Tybee has one road in and narrow streets, so the driver meets you on Victory Drive. Skidaway is gated, and the handoff happens at the gate on the Diamond Causeway. A king tide can move either pickup to the mainland for a day."),
 ("Do you ship cars for SCAD students?","Yes. Students arrive each September and leave each spring, and both windows book up early. Downtown is closed to trucks. The handoff happens at a lot off Interstate 16 or on Martin Luther King Boulevard. A parent or another adult signs at pickup."),
 ("Do you ship cars for workers hired at the new electric-vehicle plant?","Yes, every week. Workers and engineers arrive from across the country on hiring schedules. Many ship a car behind the move. The handoff works at the Pooler outlets or along Interstate 16 near the plant. We provide the paperwork a reimbursed move needs."),
 ("Can you ship a car that does not run from Savannah?","Yes. The carrier arrives with a winch, and the quote already covers the slower loading. Pick a flat, open spot, which usually means a lot on Chatham Parkway or Abercorn. Let us know if it rolls, steers, and brakes."),
 ("What do you need for a Savannah car shipping quote?","Both addresses, with the gate or the square on this end. The year, make, and model. Whether it runs and rolls. Open or enclosed, and the dates you can work with, hurricane season in mind. That is everything a Savannah quote needs."),
]
BODY.append(faq_section(FAQ,'Savannah FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Savannah?','The form above prices your lane in about two minutes. Tell us the neighborhood and your dates, and a carrier already on 95 takes it from there.','+19124552132','(912) 455-2132','Get your free Savannah quote'))

build({
 'slug':'auto-transport-savannah-georgia',
 'title':'Car Shipping in Savannah, GA — Auto Transport | Ship Guy',
 'meta':'Car shipping in Savannah, GA where Interstate 16 meets 95, between the port and the squares. Historic District meeting spots, island and gate handoffs, Hunter and Fort Stewart second cars, port releases, SCAD move-in, the new auto plant, hurricane and king-tide planning. Local office off Chatham Parkway. Free quote.',
 'h1':'Car Shipping in<br>Savannah, <span class="accent">Georgia</span>',
 'lede':'Open, enclosed, and expedited auto transport across the coast, planned around 95, 16, the squares, the gates, and the storms.',
 'tel':'+19124552132','disp':'(912) 455-2132','brand':'Savannah','keyword':'car shipping in savannah',
 'localterms':['savannah','interstate 95','interstate 16','interstate 516','lynes parkway','interchange','chatham parkway','montgomery street','martin luther king','dean forest road','jimmy deloach','us 17','talmadge bridge','abercorn','truman parkway','us 80','victory drive','islands expressway','diamond causeway','derenne','pooler parkway','historic district','squares','cobblestone','liberty street','victorian district','starland','forsyth park','ardsley park','baldwin park','parkside','habersham','midtown','waters','southside','windsor forest','georgetown','isle of hope','skidaway','the landings','wilmington island','whitemarsh','tybee','thunderbolt','garden city','port wentworth','pooler','outlets','richmond hill','hinesville','port','customs','container','imported','airfield','fort','brigades','orders','report date','jet plant','airport','electric-vehicle plant','suppliers','art school','september','university','hospitals','residents','hurricane','matthew','2016','irma','2017','debby','2024','evacuation','king tides','st. patrick','parade','music festival','film festival','snow','2018','2025','pollen','jacksonville','charleston','macon','augusta','atlanta','charlotte','orlando','raleigh','washington','new york','texas','kentucky'],
}, BODY, FAQ)
