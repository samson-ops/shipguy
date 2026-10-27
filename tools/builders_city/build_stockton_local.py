import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Stockton, California','Car shipping on the Delta, where Interstate 5 and Highway 99 both pass and the Bay Area commute begins',
 ['Car shipping in Stockton draws on two carrier lanes at once, Interstate 5 and Highway 99. Ship Guy is a licensed auto transport broker with an office on North San Joaquin Street downtown.',
  'We book vetted carriers across San Joaquin County, from Lodi and Manteca to Lathrop, Tracy, and Ripon. We do not own the trucks.',
  'Interstate 5 runs along the west side of the city by the Delta. Highway 99 runs along the east side. Highway 4 ties them together through downtown and runs west across the Delta. Interstate 205 leaves Tracy for the Altamont Pass and the Bay Area.',
  'This page covers the two highways and the pass, downtown and the Miracle Mile, and the gated subdivisions. It also covers the warehouses, the Bay Area commute, the university, the fog, the levees, and the lanes.'],
 'Stockton at a glance',
 ['Most pickups happen within 1 to 3 days. Carriers on Interstate 5 and Highway 99 pass the city from both directions all day.',
  'Sacramento, Oakland, San Jose, and Fresno are same-day lanes. San Francisco is the same day too. Los Angeles, Reno, and Bakersfield take a day. Portland and Las Vegas take one to two.'],
 'Tell us the neighborhood. Downtown, the Miracle Mile, and the blocks around the university need a meeting spot. Brookside and Spanos Park are gated, and Weston Ranch and Manteca usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 5, Highway 99, Highway 4, Interstate 205, and the Altamont',
 prose(
  L('Stockton is one of the few valley cities where both north-south lanes pass through town.'),
  P('Interstate 5 runs along the west side of the city past the port and the Delta. Highway 99 runs along the east side past the fairgrounds and the airport. Both carry carriers between Los Angeles and Sacramento every hour. A Stockton car can ride either one.'),
  P('Highway 4 is the Crosstown Freeway, and it ties 5 to 99 through downtown. West of the city it crosses the Delta on levee roads and bridges to Antioch. Interstate 205 leaves Tracy for the Altamont Pass, Interstate 580, and the Bay Area. Highway 12 crosses the Delta from Lodi to Fairfield and Napa.'),
  P('Highway 88 and Highway 26 run east into the Sierra foothills. The carriers come off 5 at March Lane and Eight Mile Road. On 99 they use Hammer Lane and Wilson Way. The lots along March Lane are the usual meeting spots. No road in the county charges a toll.'),
  P('Our office sits on North San Joaquin Street downtown, a block from the waterfront.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the Miracle Mile, Brookside, Weston Ranch, and the Grids',
 prose(
  L('Stockton is an old river port wrapped in forty years of subdivisions, and the two halves park differently.'),
  P('Downtown runs on one-way streets and the waterfront. The blocks around the Miracle Mile and the university are narrow. The driver meets you on Pacific Avenue, on March Lane, or at a lot by the ballpark. Magnolia and the older east side have alleys and tight parking.'),
  P('Brookside sits on the Delta behind gates, and Spanos Park and the north side additions are gated too. The handoff happens at the gate or at the shopping center across the road. Give us the gate code or the guard arrangement when you book.'),
  P('Weston Ranch, Lincoln Village, and the subdivisions along Eight Mile Road are wide grids. The truck usually reaches the curb there. Manteca, Lathrop, and Tracy are the same, and their newest streets are not always on a carrier’s map. Send the full address.'),
  P('Morada, Linden, and the farm roads east of the city have no curbs and narrow lanes. The driver meets you on the state highway.'),
 )))

ROUTES=[("Sacramento, CA","I-5/CA-99 · ~50 mi","Same day","$120–$200"),("Oakland, CA","I-205/I-580 · ~80 mi","Same day","$150–$240"),
 ("San Jose, CA","I-205/I-680 · ~80 mi","Same day","$150–$240"),("San Francisco, CA","I-580/I-80 · ~90 mi","Same day","$160–$250"),
 ("Fresno, CA","CA-99 · ~130 mi","Same day","$170–$270"),("Reno, NV","I-5/I-80 · ~180 mi","1 day","$210–$320"),
 ("Los Angeles, CA","I-5 · ~335 mi","1 day","$310–$450"),("Las Vegas, NV","CA-99/CA-58/I-15 · ~500 mi","1–2 days","$420–$600"),
 ("Portland, OR","I-5 · ~600 mi","1–2 days","$490–$700"),("Dallas, TX","I-10/I-20 · ~1,650 mi","3–4 days","$1,050–$1,450")]
BODY.append(rate_table('Lanes &amp; Costs','Stockton Car Shipping Lanes and Estimated Costs',
 'Stockton’s busiest lanes, from the Bay Area commute to the long hauls, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a sedan that runs, open trailer. Plan on 10 to 25 percent more for an SUV or pickup, and more for enclosed. Fog season, the Altamont, and the carriers free on your dates settle the final figure.',
 prose(
  P('Stockton prices like Sacramento and a little under the Bay Area, because both north-south lanes pass it. Oakland and San Jose ride 205 over the Altamont, and Los Angeles rides Interstate 5 south.'),
  P('The Reno lane crosses Donner Pass, and chain controls add a day to it from November through April. The <a href="car-shipping-cost.html">cost guide</a> covers the rest of the number.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Warehouses, the Bay Area Commute, the University, and the Hospitals',
 prose(
  L('Stockton relocates people on the lease, the warehouse opening, the semester, and the residency match.'),
  P('Families move over the Altamont from the Bay Area for the housing every month of the year. A second car often ships rather than making the drive over the pass on moving day. The commuter train and the 205 carry them back to work each morning.'),
  P('The warehouses and fulfillment centers along 5, 99, and 205 hire managers from every state. The battery factory in Lathrop relocates engineers on start dates. Many of them allow a handoff at the loading dock. The paperwork for a reimbursed move comes from us.'),
  P('The private university on the Miracle Mile fills with student cars each August and empties each May. The campus streets are narrow, so the driver meets you on Pacific Avenue. The community college on the north side does the same on a smaller scale. An adult signs for a student car.'),
  P('The county hospital in French Camp brings in residents every July. The two hospitals in town hire nurses on start dates. Most arrive from out of state with a car. The handoff happens on California Street or at a lot off 5.'),
  P('Travis Air Force Base sits an hour west on Highway 12. Some of its families live in Lodi for the schools. For a PCS move, see the <a href="military-car-shipping.html">military</a> page. For the interstate side of any relocation, see the <a href="state-to-state-car-shipping.html">state-to-state</a> page.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Tule Fog, the Levees, the Altamont Wind, and the Fair',
 prose(
  L('Stockton gets the valley’s fog and the Delta’s water, and the carriers plan for both.'),
  P('Tule fog settles on the Delta from November into February, and Stockton sits in the thick of it. Pileups close 5 and 99 for a morning at a time. Winter pickups happen late in the morning once it lifts, and we call if the plan changes.'),
  P('Winter rain fills the rivers, and the levees along the San Joaquin hold the low neighborhoods dry. Weston Ranch and French Camp have evacuated in a wet year. A pickup there waits for the water to fall and moves to a lot off 5.'),
  P('Summer runs near one hundred degrees, and the Delta breeze cools the evenings. The loading hour moves to early morning in July and August. Wildfire smoke drifts in from the Sierra and the coast range in late summer.'),
  P('The wind through the Altamont Pass pushes a loaded trailer around on 580. The carriers slow down for it. The county fair fills the fairgrounds on Airport Way for a week each June. The grape festival fills Lodi each September.'),
 )+chips(["Downtown","Waterfront","Miracle Mile","Magnolia","Pacific Avenue","Lincoln Village","Brookside","Spanos Park","Weston Ranch","Morada","March Lane","Hammer Lane","Eight Mile Road","Wilson Way","French Camp","Lathrop","Manteca","Tracy","Lodi","Ripon","Escalon","Linden","Mountain House","Galt"])
 +NOTE('Serving Stockton and all of San Joaquin County. Tell us the neighborhood, the gate, and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Stockton?',
 prose(
  L('Open carriers haul most of what leaves Stockton, and both lanes are priced for them.'),
  P('An enclosed trailer keeps the fog grime, the dust, and the sun off the car. The garages in Brookside and Lincoln Village book enclosed trailers. So does a collector car headed to the January auctions in Arizona.'),
  P('A commuter car rides open over the Altamont without a problem. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain what the roof buys.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a loading at the gate or by the highway, and a delivery. The fog decides the hour from November on.'),
  P('Accept the price, and a carrier already on 5 or 99 takes the booking. We settle the spot the same day. You and the driver look the car over and record it on a Bill of Lading. Both sign. Delivery is checked against that record.'),
 )+ULI([
  "Remove your belongings from the car",
  "Leave about a quarter tank of fuel",
  "Photograph the car before pickup, especially during fog season",
  "Hand the driver a working key and note any mechanical issue",
  "Disable the aftermarket alarm if it has one",
  "In a gated community, plan to meet the truck at the entrance",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages spell out the rest.'))))

BODY.append(sec('Why Ship Guy','Why Stockton Drivers Choose Ship Guy',
 prose(
  L('We work 5, 99, and the Altamont every day. We plan around the fog, the levees, and the gates.'),
  P('Our FMCSA brokerage authority is active, with a $75,000 surety bond behind it. Both are on file with the federal register. Our office is on North San Joaquin Street downtown.'),
  P('One coordinator sees the booking through from the quote to the signature at delivery. Open, enclosed, and expedited transport are all on the table, and the <a href="services.html">services</a> page covers each.'),
 ), alt=True))

BODY.append(office('Stockton','110 N San Joaquin St #455','Stockton, CA 95202','+12097218115','(209) 721-8115','PT',
 '110+N+San+Joaquin+St+%23455,+Stockton,+CA+95202','Visit Us','Find Ship Guy in Stockton',
 'Our office is on North San Joaquin Street downtown, a block from the waterfront and the Crosstown Freeway.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3883.306896325857!2d-121.28737939999999!3d37.954483100000004!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x809013c661ebbf0d%3A0xd87582be73042f56!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792077100041!5m2!1sen!2sus'))

FAQ=[
 ("Is Stockton priced like Sacramento or like the Bay Area?","Like Sacramento, and a little under the Bay Area. Both north-south lanes pass the city, so a carrier headed either way can take the car. Oakland and San Jose run one hundred fifty to two hundred forty dollars for a sedan."),
 ("Can you ship a car for a family moving from the Bay Area to Stockton or Manteca?","Yes, every week. Families cross the Altamont for the housing all year. The second car often ships rather than making the drive on moving day. The carrier picks it up in the Bay Area and delivers to the curb or the gate here."),
 ("What happens when tule fog closes Interstate 5 or Highway 99?","The driver waits for it to lift. Stockton sits in some of the thickest fog in the valley from November into February. Pileups close both highways for a morning. Winter pickups run late in the morning for that reason. We call the moment the plan changes."),
 ("Can the carrier come into Brookside, Spanos Park, or another gated community?","Not past the gate. The driver meets you at the entrance or at the shopping center across the road. Give us the gate code or the guard arrangement when you book. The handoff takes a few minutes."),
 ("Do you ship cars for people hired at the warehouses or the battery factory?","Yes, on start dates all year. The warehouses along 5, 99, and 205 and the factory in Lathrop hire from every state. Many employers allow a handoff at the dock. The paperwork for a reimbursed move comes from us."),
 ("Can you ship a car for a University of the Pacific student?","Yes. The cars come in each August and leave each May. The campus streets off the Miracle Mile are narrow. The driver meets you on Pacific Avenue or at a lot nearby. An adult signs for the car at pickup."),
 ("What happens if the river floods on my pickup day?","The pickup waits for the water to fall. A wet winter puts Weston Ranch, French Camp, and the Delta islands under evacuation orders now and then. The handoff moves to a lot off Interstate 5 or March Lane until the roads reopen."),
 ("Do you handle a PCS move to Travis from Stockton or Lodi?","Yes. The base sits an hour west on Highway 12. Some of its families live in Lodi and the north side. One vehicle moves on the orders, and the other ships with us. The handoff happens in Fairfield or Vacaville outside the gate. Ship Guy is a private broker with no connection to the Air Force."),
 ("Can you ship a car that does not run from Stockton?","Yes. We send a carrier with a winch, and the slower loading is part of the price. The spot has to be flat and open, which usually means a lot by March Lane. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Stockton car shipping quote?","Both addresses, with the neighborhood and the gate on this end. The year, make, and model, and whether it runs. Open or enclosed. Your dates, with fog season in mind. That is a complete Stockton request."),
]
BODY.append(faq_section(FAQ,'Stockton FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Stockton?','Get a price from the form above in about two minutes. Send the neighborhood and your dates, and a carrier already on 5 or 99 takes it from there.','+12097218115','(209) 721-8115','Get your free Stockton quote'))

build({
 'slug':'auto-transport-stockton-california',
 'title':'Car Shipping in Stockton, CA — Auto Transport | Ship Guy',
 'meta':'Car shipping in Stockton, CA on Interstate 5 and Highway 99 at the edge of the Delta. Miracle Mile and downtown handoffs, gated Brookside and Spanos Park, Bay Area families crossing the Altamont, warehouse and Lathrop relocations, Pacific students, tule fog and levee planning. Local office on North San Joaquin Street. Free quote.',
 'h1':'Car Shipping in<br>Stockton, <span class="accent">California</span>',
 'lede':'Open, enclosed, and expedited auto transport across San Joaquin County, planned around both highways, the fog, and the Delta.',
 'tel':'+12097218115','disp':'(209) 721-8115','brand':'Stockton','keyword':'car shipping in stockton',
 'localterms':['stockton','interstate 5','highway 99','highway 4','interstate 205','interstate 580','highway 12','highway 88','highway 26','crosstown freeway','altamont','delta','port','march lane','hammer lane','eight mile road','wilson way','pacific avenue','california street','downtown','waterfront','miracle mile','magnolia','lincoln village','brookside','spanos park','weston ranch','morada','linden','french camp','lathrop','manteca','tracy','lodi','ripon','gated','gate','warehouses','fulfillment','battery factory','commuter train','university','pacific','community college','county hospital','residents','travis','air force','tule fog','fog','levees','flood','smoke','wind','fair','grape festival','sacramento','oakland','san jose','san francisco','fresno','reno','donner','los angeles','las vegas','portland','dallas','arizona','bakersfield'],
}, BODY, FAQ)
