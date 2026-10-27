import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Independence, Missouri','Car shipping on the east side of the metro, where Interstate 70 leaves Kansas City',
 ['Car shipping in Independence starts on the interstate that runs through the middle of town. Ship Guy is a licensed auto transport broker with an office on North Forest Avenue near the Square.',
  'We book vetted carriers across eastern Jackson County, from Sugar Creek to Blue Springs and Raytown. We do not own the trucks.',
  'Interstate 70 crosses the city from the sports complex to Blue Springs. Interstate 435 forms the west edge, and Route 291 runs north and south through the east side. Every carrier between Kansas City and St. Louis passes the Noland Road exit.',
  'This page covers the 70 exits, the Square, the older blocks, the ammunition plant, and the hospital. It also covers the stadiums next door, the river bottoms, the storms, and the lanes.'],
 'Independence at a glance',
 ['Most pickups happen within 1 to 3 days. The 70 lane and the 435 loop bring carriers past the city all day.',
  'Columbia, Wichita, Omaha, Des Moines, and Topeka arrive the same day. Tulsa, St. Louis, and Oklahoma City arrive in a day. Denver, Dallas, and Chicago arrive in one to two.'],
 'Tell us the neighborhood. The Square, Englewood, and the river-bottom streets need a meeting spot. The subdivisions off 291 and 40 Highway usually meet the truck at the curb.'))

BODY.append(sec('The Roads','Interstate 70, 435, 470, Route 291, and the Stadiums',
 prose(
  L('Independence sits where the busiest interstate in the state leaves the metro. The carriers are already on it.'),
  P('Interstate 70 runs east from the sports complex through the city to Blue Springs. It continues to Columbia and St. Louis. The Noland Road, Lee’s Summit Road, and Little Blue Parkway exits carry the city traffic. Interstate 435 loops the metro along the west edge of the city.'),
  P('Interstate 470 runs south from 70 toward Lee’s Summit. Route 291 runs north and south through the east side to Liberty and Lee’s Summit. US 24 and 40 Highway are the old roads across the city. Noland Road is the retail strip between them.'),
  P('The stadiums sit at the 70 and 435 interchange on the city line. On game days, the interchange and the frontage roads fill for hours. We schedule west-side pickups around the schedule.'),
  P('None of the roads through Independence charges a toll. Our office sits on North Forest Avenue near the Square, minutes from the Noland Road exit.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','The Square, Englewood, Sugar Creek, and the Subdivisions Off 291',
 prose(
  L('Independence is a historic core wrapped in postwar subdivisions. The meeting spot follows the age of the street.'),
  P('The Square, the blocks around the Truman home, and the historic district have narrow streets with street parking. Englewood, Fairmount, and Maywood are older grids with alley garages. The driver meets you on Truman Road, on Noland Road, or at a lot off 70.'),
  P('Sugar Creek and the river bottoms along the Missouri sit on low roads that flood. The handoff happens on US 24 or at a lot near the interstate.'),
  P('The subdivisions off Route 291, 40 Highway, and Little Blue Parkway are wide grids. The truck usually reaches the curb. Blue Springs, Grain Valley, and Oak Grove are the same farther east on 70. Raytown is open along 350 Highway.'),
  P('The mall lots at 70 and 291 are the usual meeting spot for the whole east side. So is the sporting-goods lot at Little Blue Parkway.'),
 )))

ROUTES=[("Columbia, MO","I-70 · ~120 mi","Same day","$180–$290"),("Topeka, KS","I-70 · ~75 mi","Same day","$150–$250"),
 ("Omaha, NE","I-29 · ~195 mi","Same day","$220–$340"),("Des Moines, IA","I-35 · ~200 mi","Same day","$230–$350"),
 ("Wichita, KS","I-35 · ~210 mi","Same day","$230–$350"),("St. Louis, MO","I-70 · ~240 mi","1 day","$250–$370"),
 ("Oklahoma City, OK","I-35 · ~350 mi","1 day","$320–$460"),("Minneapolis, MN","I-35 · ~440 mi","1 day","$390–$550"),
 ("Denver, CO","I-70 · ~600 mi","1–2 days","$470–$680"),("Dallas, TX","I-35 · ~540 mi","1–2 days","$450–$640")]
BODY.append(rate_table('Lanes &amp; Costs','Independence Car Shipping Lanes and Estimated Costs',
 'The lanes Independence households book most, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a sedan that runs, open trailer. SUVs and pickups come in about 10 to 25 percent higher, and enclosed higher still. Ice season and the carriers free on your dates fix the final figure.',
 prose(
  P('Independence prices like Kansas City, because it sits on the same loop and shares the same carrier pool. Columbia and St. Louis ride 70 east, and Topeka and Denver ride it west.'),
  P('Interstate 35 carries the Texas and Minnesota lanes from the loop in opposite directions. The <a href="car-shipping-cost.html">cost guide</a> explains the rest of the number.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Ammunition Plant, the Hospital, the Stadium Employers, and Whiteman',
 prose(
  L('Independence relocates people on a federal plant’s hiring, a hospital’s calendar, and the orders that come through Whiteman.'),
  P('The ammunition plant on the east side is one of the largest employers in the county. Its expansion brings in engineers and technicians on start dates. The hospital on 39th Street brings in nurses and residents every summer. The handoff happens on 39th or Noland rather than in a hospital garage.'),
  P('The stadium employers, the arena, and the distribution centers along 70 transfer staff in on their own schedules. When an employer reimburses the shipment, we supply the documentation it needs.'),
  P('Whiteman Air Force Base sits an hour east on US 50. Many of its families live in eastern Jackson County. Orders pay for one vehicle, and the family car comes with us. The driver cannot pass the gate, so the meeting point is Knob Noster or Warrensburg. The <a href="military-car-shipping.html">military</a> page covers the planning.'),
  P('The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side of a relocation.'),
 ), alt=True))

BODY.append(sec('The Weather','Ice, Tornadoes, Hail, and the River',
 prose(
  L('Eastern Jackson County gets every kind of weather the Plains can produce, and the river adds one more.'),
  P('Ice is the one that stops a truck. An ice storm closes 70 and 435 for a day, and the carriers wait for the sand trucks. A winter pickup can slide a day.'),
  P('Tornado watches run from March into June, and the metro has taken direct hits on the east side. When a warning is issued, the driver pulls off and waits. Hail is worse for a parked car than wind, and we push the window when it is forecast.'),
  P('The Missouri River rises in wet springs, and Sugar Creek and the bottoms go under. We move the handoff uphill when the river is up. Summer heat moves the loading hour earlier.'),
 )+chips(["The Square","Truman District","Englewood","Fairmount","Maywood","Sugar Creek","Courtney","Noland Road","40 Highway","Little Blue Valley","Bundschu","Crysler","Glendale","Blue Springs","Grain Valley","Oak Grove","Lake Tapawingo","Raytown","Buckner","Liberty","Kansas City"])
 +NOTE('Serving eastern Jackson County. Tell us the neighborhood and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Independence?',
 prose(
  L('Open trailers do most of the work out of Independence, and the 70 lane is priced for them.'),
  P('An enclosed trailer keeps hail, salt, and attention off the car. The collector garages around Lake Tapawingo and the Square book enclosed trailers. So does a car headed to Arizona for the winter.'),
  P('A commuter car arrives fine on an open trailer. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain when a roof is worth the extra.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a loading near the interstate, and a delivery. Ice decides the timing in winter.'),
  P('Accept the price and a carrier already running 70 or the loop takes the booking. We name the spot up front. There, you and the driver record the car’s condition on a Bill of Lading and both sign. The delivery check runs against that sheet.'),
 )+ULI([
  "Clear your belongings out",
  "Leave roughly a quarter tank",
  "Photograph the car before the truck arrives, especially after hail",
  "Give the driver a working key and note any mechanical issue",
  "Turn off the aftermarket alarm if there is one",
  "Near the Square or in the river bottoms, plan to meet the truck on Truman Road or Noland",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages have the rest.'))))

BODY.append(sec('Why Ship Guy','Why Independence Drivers Choose Ship Guy',
 prose(
  L('We work 70 and the loop every day. We plan around the ice, the river, and the game schedule.'),
  P('Our brokerage authority with the FMCSA is active and a $75,000 surety bond is posted. Both are searchable on the federal register. Our office is on North Forest Avenue near the Square.'),
  P('One coordinator stays on your shipment from quote to delivery. Open, enclosed, and expedited transport are all bookable, and the <a href="services.html">services</a> page lists them.'),
 ), alt=True))

BODY.append(office('Independence','201 N Forest Ave #336','Independence, MO 64050','+18167102639','(816) 710-2639','CT',
 '201+N+Forest+Ave+%23336,+Independence,+MO+64050','Visit Us','Find Ship Guy in Independence',
 'Our office is on North Forest Avenue near the Square, minutes from the Noland Road exit.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3822.342835260761!2d-94.4358178!3d39.093228499999995!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x87c0fdf405d87cdf%3A0x14f42ad989641c3c!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792076188479!5m2!1sen!2sus'))

FAQ=[
 ("Is Independence priced the same as Kansas City?","Yes. The city sits on the same 435 loop and shares the same carrier pool. A pickup off Noland Road prices like one in Kansas City. Blue Springs and Grain Valley add a few dollars for the extra miles on 70."),
 ("Can the carrier come to my house near the Square or in Englewood?","Rarely. The streets are narrow and the parking is on the street. The driver meets you on Truman Road, on Noland Road, or at the mall lots by 70. The subdivisions off 291 and 40 Highway usually allow a curbside pickup."),
 ("Does a game at the sports complex affect my pickup?","On the west side, yes. The 70 and 435 interchange and the frontage roads fill for hours on game days. We schedule west-side pickups around the schedule. The rest of the city runs normally."),
 ("How much does it cost to ship a car from Independence to Texas?","Count on four hundred fifty to six hundred forty dollars for a sedan to Dallas. The route runs about five hundred forty miles down 435 and Interstate 35. Houston runs a hundred to a hundred fifty more. An SUV or pickup adds 10 to 25 percent."),
 ("Do you handle a PCS move to Whiteman from Independence?","Yes. Many Whiteman families live in eastern Jackson County. Orders pay for one vehicle, and the family car comes with us. The driver cannot pass the gate, so you meet in Knob Noster or Warrensburg. Ship Guy is a private broker with no connection to the base."),
 ("Do you ship cars for people hired at the ammunition plant?","Yes. The plant on the east side brings in engineers and technicians on start dates. Many ship a car from out of state. The pickup is planned around the start date. When the plant reimburses the move, we provide the paperwork it wants."),
 ("What happens if an ice storm hits on my pickup day?","The driver holds until 70 and the loop reopen behind the sand trucks. A winter pickup can lose a day. You hear from us the moment the forecast changes the plan."),
 ("Can you pick up in Sugar Creek or the river bottoms?","Yes, when the river is down. The low roads flood in a wet spring. The handoff moves to US 24 or a lot by the interstate until the water falls."),
 ("Can you ship a car that does not run from Independence?","Yes. We send a winch-equipped carrier and the extra loading time is in the quote. Choose a flat spot. Let us know if it rolls, steers, and brakes."),
 ("What do you need for an Independence car shipping quote?","Both addresses, with the Independence neighborhood. The year, make, and model. Does it run and roll. Open or enclosed, and the dates. Nothing more is needed."),
]
BODY.append(faq_section(FAQ,'Independence FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Independence?','Price the trip on the form above. Then send the neighborhood and your dates, and a carrier already on 70 takes the job.','+18167102639','(816) 710-2639','Get your free Independence quote'))

build({
 'slug':'auto-transport-independence-missouri',
 'title':'Car Shipping in Independence, MO — Auto Transport | Ship Guy',
 'meta':'Car shipping in Independence, MO on Interstate 70 and the 435 loop. Square and Englewood meeting spots, the mall lots at 70 and 291, game-day planning at the sports complex, the ammunition plant and hospital hiring, Whiteman second vehicles, ice and storm season. Local office near the Square. Free quote.',
 'h1':'Car Shipping in<br>Independence, <span class="accent">Missouri</span>',
 'lede':'Open, enclosed, and expedited auto transport across eastern Jackson County, planned around the interstate, the stadiums, and the ice.',
 'tel':'+18167102639','disp':'(816) 710-2639','brand':'Independence','keyword':'car shipping in independence',
 'localterms':['independence','interstate 70','interstate 435','interstate 470','route 291','us 24','40 highway','noland road','truman road','little blue parkway','lee','sports complex','stadiums','square','truman','englewood','fairmount','maywood','sugar creek','river bottoms','mall','sporting-goods','blue springs','grain valley','oak grove','raytown','lake tapawingo','ammunition plant','hospital','39th','distribution','whiteman','knob noster','warrensburg','ice','tornado','hail','missouri river','columbia','topeka','omaha','des moines','wichita','st. louis','oklahoma city','minneapolis','denver','dallas','kansas city'],
}, BODY, FAQ)
