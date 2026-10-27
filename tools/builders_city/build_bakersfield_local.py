import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Bakersfield, California','Car shipping at the foot of the Grapevine, where the valley meets Los Angeles and the desert',
 ['Car shipping in Bakersfield starts where the valley’s trucks line up for the Grapevine. Ship Guy is a licensed auto transport broker with an office on California Avenue near downtown.',
  'We book vetted carriers across Kern County, from Oildale and Rosedale to Tehachapi, Shafter, Delano, and Taft. We do not own the trucks.',
  'Highway 99 runs through the city and joins Interstate 5 at the base of the Grapevine. Highway 58 runs west to Interstate 5 and east over Tehachapi to Mojave and Barstow. Highway 178 runs east into the Kern River canyon, and Highway 65 runs north to Porterville.',
  'This page covers the highways and the pass, the older and newer neighborhoods, and the farm towns. It also covers the oil fields, the hospitals, Edwards, the fog, the heat, and the lanes.'],
 'Bakersfield at a glance',
 ['Most pickups happen within 1 to 3 days. Every carrier between Los Angeles and the valley passes the city on 99 or Interstate 5.',
  'Los Angeles, Fresno, and Santa Clarita are same-day lanes. Las Vegas and San Diego take a day. Sacramento, the Bay Area, and Phoenix take one to two.'],
 'Tell us the neighborhood. Oleander, Westchester, and the blocks near downtown need a meeting spot. The southwest, the northwest, and Rosedale usually allow the curb.'))

BODY.append(sec('The Roads','Highway 99, 58, 178, Interstate 5, and the Grapevine',
 prose(
  L('Bakersfield is where the valley trucks wait when the Grapevine closes. The rest of the year they refuel here.'),
  P('Highway 99 runs north and south through the city, a few blocks west of downtown. Twenty miles south it joins Interstate 5 at Wheeler Ridge. The Grapevine climbs from there to four thousand feet. Interstate 5 itself runs twenty miles west of town along the empty side of the valley.'),
  P('Highway 58 is the road around Los Angeles. It runs east over the Tehachapi summit to Mojave and Barstow. At Barstow it meets Interstate 15 for Las Vegas and Interstate 40 for Arizona. West of town it reaches Interstate 5 at Buttonwillow. The Westside Parkway carries the southwest side into downtown.'),
  P('The carriers come off 99 at Rosedale, California Avenue, Ming, and White Lane. The truck stops at the base of the Grapevine are one meeting spot. The lots along Rosedale Highway are the other. No road in the county charges a toll.'),
  P('Our office sits on California Avenue, between downtown and Highway 99.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Oleander, Westchester, Seven Oaks, Oildale, and the Grids',
 prose(
  L('Bakersfield grew out from the rail yard in rings, and each ring parks differently.'),
  P('Downtown, Oleander, Sunset, and Westchester are the oldest rings, with narrow streets, alleys, and big trees. The driver meets you on Chester Avenue, Oak Street, or California Avenue. Oildale across the river has the same tight blocks.'),
  P('The southwest and the northwest are the newest rings. Seven Oaks, the Stockdale additions, and Riverlakes are wide grids where the truck usually reaches the curb. Some of the newer additions are gated. The handoff happens at the gate or the clubhouse.'),
  P('The northeast climbs into the bluffs above the river, and the streets wind. The driver stays on Panorama Drive or Highway 178. The farm towns ship on the state highway, and Tehachapi ships on 58 when the summit is clear.'),
  P('The warehouses at the base of the Grapevine have truck entrances of their own. Employers there often allow a handoff at the dock.'),
 )))

ROUTES=[("Los Angeles, CA","CA-99/I-5 · ~115 mi","Same day","$160–$260"),("Fresno, CA","CA-99 · ~110 mi","Same day","$160–$260"),
 ("San Diego, CA","I-5 · ~240 mi","1 day","$240–$360"),("Las Vegas, NV","CA-58/I-15 · ~290 mi","1 day","$280–$410"),
 ("Sacramento, CA","CA-99 · ~280 mi","1 day","$270–$400"),("San Jose, CA","I-5/CA-152 · ~240 mi","1 day","$250–$370"),
 ("Phoenix, AZ","I-5/I-10 · ~480 mi","1–2 days","$410–$590"),("Portland, OR","I-5 · ~760 mi","2 days","$580–$820"),
 ("Denver, CO","I-15/I-70 · ~1,100 mi","3 days","$760–$1,060"),("Dallas, TX","I-10/I-20 · ~1,390 mi","3–4 days","$920–$1,280")]
BODY.append(rate_table('Lanes &amp; Costs','Bakersfield Car Shipping Lanes and Estimated Costs',
 'Bakersfield’s busiest lanes over the pass and across the valley, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a running sedan, open trailer. Expect about 10 to 25 percent more for an SUV or pickup, and more for enclosed. The pass, the fog, and the carriers free on your dates decide the final number.',
 prose(
  P('Bakersfield prices close to Los Angeles, because every carrier leaving Southern California for the north passes it. Las Vegas and Arizona ride 58 around the city instead of through it.'),
  P('The Texas lane fills with oil-field crews following the work, and it prices well because of it. The <a href="car-shipping-cost.html">cost guide</a> has the rest of the math.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Oil Fields, the Farms, the Hospitals, and Edwards',
 prose(
  L('Bakersfield relocates people on the drilling schedule, the harvest, the residency match, and the Air Force calendar.'),
  P('The oil companies in the Kern River and Elk Hills fields transfer engineers and crews in from Texas. They send them back out again when the work moves. The carrot and grape growers on the west side relocate managers on the crop calendar. The warehouses at the base of the Grapevine hire on start dates all year.'),
  P('The county hospital brings in residents every July, and the two other systems hire nurses on start dates. The state university on the southwest side brings cars in each August and sends them home each May. The handoff happens on Stockdale Highway or at a lot by the campus.'),
  P('Edwards Air Force Base sits a little over an hour east on Highway 58 past Mojave. Many of its engineers and families live in Bakersfield and Tehachapi. Orders usually move one vehicle. The second one comes with us, and the handoff happens in Rosamond or Mojave outside the gate. The <a href="military-car-shipping.html">military</a> page covers the planning.'),
  P('Employers that reimburse the move get the paperwork they ask for from us. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side of a move, Texas included.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Grapevine, Tule Fog, the Heat, and the Wind',
 prose(
  L('Bakersfield’s weather lives on the pass above it and the fog below it.'),
  P('The Grapevine closes for snow a few times each winter, sometimes for a day. The trucks wait at the base of the pass or in town until it reopens. A Los Angeles pickup slides a day when that happens, and we call before it does.'),
  P('Tule fog is thickest at the south end of the valley from November into February. It closes 99 and Interstate 5 for a morning after a pileup. Winter pickups happen late in the morning for that reason.'),
  P('Summer runs past one hundred degrees from June into September. The loading hour moves to dawn, and a car left in an open lot bakes. Spring brings wind and blowing dust on Interstate 5 and on 58 toward Mojave. A loaded trailer slows down in it.'),
  P('Tehachapi gets real snow, and 58 over the summit closes to trucks until the plows finish. The county fair fills the fairgrounds and South P Street for two weeks each September.'),
 )+chips(["Downtown","Oleander","Sunset","Westchester","Oildale","Kern City","Stockdale","Seven Oaks","Riverlakes","Rosedale","Northeast","Panorama","Southwest","Ming Avenue","White Lane","California Avenue","Rosedale Highway","Wheeler Ridge","Tehachapi","Shafter","Wasco","Delano","Taft","Arvin","Lamont","Frazier Park"])
 +NOTE('Serving Bakersfield and all of Kern County. Tell us the neighborhood, the month, and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Bakersfield?',
 prose(
  L('Most Bakersfield cars ride open, and the 99 and Interstate 5 lanes are priced for it.'),
  P('An enclosed trailer keeps the dust, the sun, and the road grit from the pass off the car. The garages in Seven Oaks and the northeast book enclosed trailers. So do the cars that head to the Arizona auctions each January.'),
  P('A work truck or a commuter car rides open without trouble. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages compare the cost and the cover.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a loading by 99 or at the base of the pass, and a delivery. The pass picks the day in winter.'),
  P('Approve the price and a carrier already running 99 or Interstate 5 takes the job. We name the spot. You and the driver walk around the car and write it up on a Bill of Lading. You both sign, and delivery is checked against it.'),
 )+ULI([
  "Pull your belongings out of the car",
  "Keep the fuel around a quarter tank",
  "Photograph the car before pickup, especially after a dust storm",
  "Leave a working key and tell us about any mechanical issue",
  "Switch off any aftermarket alarm",
  "In summer, plan a dawn handoff",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages take it from there.'))))

BODY.append(sec('Why Ship Guy','Why Bakersfield Drivers Choose Ship Guy',
 prose(
  L('We work 99, 58, and the pass every day. We plan around the fog, the heat, and the snow.'),
  P('Ship Guy holds FMCSA brokerage authority, and a $75,000 surety bond stands behind every booking. Both are searchable on the federal register. Our office is on California Avenue near downtown.'),
  P('The coordinator who quotes your move stays with it to delivery. Open, enclosed, and expedited transport are all available, and the <a href="services.html">services</a> page explains each.'),
 ), alt=True))

BODY.append(office('Bakersfield','1603 California Ave #425B','Bakersfield, CA 93304','+16617623480','(661) 762-3480','PT',
 '1603+California+Ave+%23425B,+Bakersfield,+CA+93304','Visit Us','Find Ship Guy in Bakersfield',
 'Our office is on California Avenue, between downtown and the Highway 99 exit.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4016.0333429377224!2d-119.02036509999999!3d35.368168!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80ea6b99cd9945a9%3A0x9c6c0a34970b426f!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792077075055!5m2!1sen!2sus'))

FAQ=[
 ("What happens when the Grapevine closes?","The trucks wait. The pass closes for snow a few times each winter. Usually it is a few hours, sometimes a day. The carriers hold at the base of the pass or in town until it reopens. A Los Angeles pickup slides a day, and we call before it does."),
 ("How much does it cost to ship a car from Bakersfield to Los Angeles or Las Vegas?","Los Angeles runs one hundred sixty to two hundred sixty dollars for a sedan. That is about one hundred fifteen miles over the pass. Las Vegas runs two hundred eighty to four hundred ten. That is about two hundred ninety miles on 58 and Interstate 15. SUVs and pickups add 10 to 25 percent."),
 ("Do you ship cars for oil-field crews moving between Bakersfield and Texas?","Yes, in both directions. Engineers and crews follow the work between Kern County and the Permian. Many ship a truck rather than drive it. Midland and Odessa price like Dallas. We plan the pickup around the start date, and the paperwork for a reimbursed move comes from us."),
 ("What happens if tule fog closes 99 on my pickup day?","The driver waits for it to lift, which usually means a late-morning handoff. The south end of the valley gets the thickest fog from November into February. Pileups close 99 and Interstate 5 for a morning at a time. We call the moment the plan changes."),
 ("Do you handle a PCS move to Edwards from Bakersfield?","Yes. The base is a little over an hour east on 58 past Mojave. Many of its engineers and families live here. Orders usually move one vehicle, and the second one comes with us. The handoff happens outside the gate in Rosamond or Mojave. Ship Guy is a private broker with no connection to the Air Force."),
 ("Can you ship a car for a CSU Bakersfield student?","Yes. The cars come in each August and leave each May. The campus lots on the southwest side work for the handoff, and Stockdale Highway is the backup. An adult signs for the car at pickup."),
 ("Can the carrier come into Oleander, Westchester, or Oildale?","Usually not. The streets are narrow, the trees are big, and the alleys are tight. The driver meets you on Chester Avenue, Oak Street, or California Avenue. The southwest, the northwest, and Rosedale usually allow the curb."),
 ("Can you deliver to Tehachapi, Taft, or the farm towns?","Yes. Tehachapi ships on 58 when the summit is clear. The handoff happens in town or at the truck stop. Taft, Shafter, Wasco, Delano, and Arvin meet the truck on the state highway. Those pickups run 2 to 4 days."),
 ("Can you ship a car that does not run from Bakersfield?","Yes. We book a carrier with a winch, and the extra loading time goes into the price. The spot has to be flat, which usually means a lot off 99 or Rosedale Highway. Say whether it rolls, steers, and brakes."),
 ("What do you need for a Bakersfield car shipping quote?","Both addresses, with the neighborhood on this end. The year, make, and model. Whether it runs. Open or enclosed. The dates you have in mind, with the pass and the fog in mind too. That is all a Bakersfield quote needs."),
]
BODY.append(faq_section(FAQ,'Bakersfield FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Bakersfield?','Fill in the form above and the price comes back in about two minutes. Tell us the neighborhood and your dates. A carrier already headed for the pass takes it from there.','+16617623480','(661) 762-3480','Get your free Bakersfield quote'))

build({
 'slug':'auto-transport-bakersfield-california',
 'title':'Car Shipping in Bakersfield, CA — Auto Transport | Ship Guy',
 'meta':'Car shipping in Bakersfield, CA at the foot of the Grapevine on Highway 99 and 58. Oleander and Westchester handoffs, Seven Oaks and Rosedale curbside, oil-field crews to Texas, CSUB and hospital moves, Edwards second vehicles, Grapevine closures, tule fog and summer heat. Local office on California Avenue. Free quote.',
 'h1':'Car Shipping in<br>Bakersfield, <span class="accent">California</span>',
 'lede':'Open, enclosed, and expedited auto transport across Kern County, planned around the pass, the fog, and the heat.',
 'tel':'+16617623480','disp':'(661) 762-3480','brand':'Bakersfield','keyword':'car shipping in bakersfield',
 'localterms':['bakersfield','highway 99','highway 58','highway 178','highway 65','interstate 5','grapevine','wheeler ridge','tehachapi','mojave','barstow','buttonwillow','westside parkway','rosedale','california avenue','ming','white lane','chester avenue','oak street','stockdale','panorama','downtown','oleander','sunset','westchester','oildale','kern city','seven oaks','riverlakes','northeast','southwest','northwest','shafter','wasco','delano','taft','arvin','lamont','frazier park','oil','kern river','elk hills','permian','carrot','grape','warehouses','county hospital','residents','university','edwards','air force','rosamond','tule fog','fog','heat','dust','wind','snow','fair','los angeles','fresno','santa clarita','san diego','las vegas','sacramento','san jose','phoenix','portland','denver','dallas','midland','odessa','arizona'],
}, BODY, FAQ)
