import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("2–5 Days","Honest Pickup"),("7 Days","Support")]))

BODY.append(intro_block('South Dakota','South Dakota auto transport on Interstate 90, from the river to the Black Hills',
 ['South Dakota auto transport runs on one interstate across the state and one up its eastern edge, with the Missouri River splitting the two halves.',
  'Ship Guy is a licensed auto transport broker. We book vetted carriers across South Dakota, and we do not own the trucks.',
  'Interstate 90 crosses from Sioux Falls through Mitchell, Chamberlain, and Wall to Rapid City and Wyoming. Interstate 29 runs the eastern edge from Sioux City through Sioux Falls and Watertown to North Dakota.',
  'This page covers the two interstates and the honest windows, Sioux Falls, Rapid City and the Black Hills, the base and the rally, Pierre and the middle, the reservations, and the winter.'],
 'South Dakota at a glance',
 ['Most pickups happen within 2 to 5 days in Sioux Falls, Rapid City, and the Interstate 29 towns, and within 4 to 7 days in Pierre, the reservations, and the ranch country.',
  'Minneapolis, Omaha, and Fargo take one to two days from Sioux Falls. Denver and Billings take two from Rapid City. Chicago, Dallas, and the coasts run three to five.'],
 'South Dakota is a pass-through market. Carriers cross on Interstate 90 between Chicago and the Northwest and add a stop when the load justifies it. A wide date range is the biggest help you can give us.'))

BODY.append(sec('The Corridors','Interstate 90, Interstate 29, and the Two-Lane Middle',
 prose(
  L('Two roads carry the state, and the four hundred miles between the two cities on Interstate 90 is mostly empty.'),
  P('Interstate 90 carries Chicago-to-Seattle freight through Sioux Falls, Mitchell, and Rapid City. A carrier crossing the state picks up a South Dakota car when the timing and the load line up.'),
  P('Interstate 29 runs the Big Sioux valley through Sioux Falls, Brookings, and Watertown. It carries the Minneapolis and Omaha lanes, and the east side ships on it.'),
  P('Pierre, the capital, sits on US 14 and 83 with no interstate at all. US 18 crosses the reservations, and US 85 and 16 reach the Black Hills from Wyoming and Nebraska.'),
  P('Sioux Falls and Rapid City schedule in 2 to 5 days. Pierre, the reservations, and the ranch country take 4 to 7, and a flexible date range keeps the price steady.'),
 ), alt=True))

BODY.append(sec('Sioux Falls','Banks, Hospitals, and the Fastest-Growing City on the Plains',
 prose(
  L('Sioux Falls holds half the state\u2019s growth, and it ships on the corporate and medical calendars.'),
  P('The credit-card operations and the trust companies headquartered here relocate employees from across the country on start dates. The two hospital systems move residents every June.'),
  P('The city is a wide grid where the truck usually reaches the curb. New subdivisions on the south and east sides outpace carrier maps, so send the full address.'),
  P('Brookings and the state university sit an hour north on Interstate 29, and Vermillion sits an hour south. Both send cars in each August and home each May.'),
  P('If your employer reimburses the shipment, we provide the documentation. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
 )))

ROUTES=[("Omaha, NE (from Sioux Falls)","I-29 · ~180 mi","1 day","$220–$340"),("Minneapolis, MN (from Sioux Falls)","I-90/I-35 · ~240 mi","1 day","$250–$380"),
 ("Fargo, ND (from Sioux Falls)","I-29 · ~245 mi","1–2 days","$250–$380"),("Des Moines, IA (from Sioux Falls)","I-29/I-80 · ~280 mi","1–2 days","$260–$390"),
 ("Kansas City, MO (from Sioux Falls)","I-29 · ~360 mi","2 days","$320–$460"),("Denver, CO (from Rapid City)","US-85/I-25 · ~390 mi","2 days","$360–$520"),
 ("Billings, MT (from Rapid City)","I-90 · ~320 mi","1–2 days","$310–$450"),("Chicago, IL (from Sioux Falls)","I-90 · ~570 mi","2–3 days","$430–$620"),
 ("Dallas, TX (from Sioux Falls)","I-29/I-35 · ~900 mi","3 days","$650–$900"),("Phoenix, AZ (from Rapid City)","I-25/I-40 · ~1,200 mi","4 days","$800–$1,150")]
BODY.append(rate_table('Lanes &amp; Costs','South Dakota Car Shipping Lanes and Estimated Costs',
 'Common lanes out of Sioux Falls and Rapid City, with estimated open-transport ranges. Pierre and the middle of the state add a day and a detour. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a running sedan on an open trailer, priced from the nearer city. SUVs and pickups add about 10 to 25 percent, enclosed more. In a pass-through market, your dates and carrier availability matter more than the miles.',
 prose(
  P('Omaha and Minneapolis are the easiest lanes from the east, because Interstate 29 carries carriers to both daily. Denver and Billings are the easiest from the west.'),
  P('The middle of the state costs more per mile because the carrier detours for hours. The <a href="car-shipping-cost.html">cost guide</a> explains the other variables.'),
 ), alt=True))

BODY.append(sec('Rapid City &amp; the Black Hills','Ellsworth, the Rally, and the Hills',
 prose(
  L('The west side of the state ships on a bomber base, a motorcycle rally, and the tourists who come for the mountain.'),
  P('Ellsworth Air Force Base outside Rapid City flies bombers and is gaining a new one, and it rotates airmen and families year round with a summer peak. Housing is gated, so the driver meets you outside it.'),
  P('Many families ship a second vehicle through us, since orders may cover only one. Ship Guy is a private broker with no military affiliation, and our <a href="military-car-shipping.html">military</a> page covers PCS timing.'),
  P('The Sturgis rally brings half a million riders to the Hills for ten days each August, and every road from Rapid City to Spearfish crawls. We schedule Black Hills pickups before or after it.'),
  P('Spearfish, Deadwood, Custer, and Hot Springs sit on winding hill roads, and the driver meets you on the highway or in town. Hills pickups run 3 to 6 days.'),
 )))

BODY.append(sec('The Middle &amp; the Reservations','Pierre, Chamberlain, Pine Ridge, and Honest Timing',
 prose(
  L('Between the two cities, South Dakota is ranch country, river bluffs, and some of the largest reservations in the country.'),
  P('Pierre has no interstate, and state government relocates people on its own schedule. The driver meets you on US 14 or 83, and pickups run 4 to 7 days.'),
  P('Pine Ridge, Rosebud, and Cheyenne River cover thousands of square miles of two-lane road and gravel. The tribal governments and the schools relocate staff, and the handoff happens in the nearest town on a US highway.'),
  P('Ranch roads are gravel with cattle guards, and a seventy-five-foot trailer stays on the pavement. The handoff is planned before dispatch.'),
 ), alt=True))

BODY.append(sec('Winter &amp; Weather','Blizzards, Wind, and the Interstate That Closes',
 prose(
  L('South Dakota winter closes Interstate 90 more often than any other state on the route.'),
  P('Ground blizzards shut the interstate for a day or more from November through April, and the state closes it with gates and no-travel advisories. Carriers wait in the towns until it reopens.'),
  P('Temperatures reach thirty below with the wind, and a car that arrives from a warm state needs winter-weight oil, a strong battery, and a block heater. An electric car should arrive at half charge and go straight to a charger.'),
  P('Wind blows across the plains most of the year and slows a high-profile trailer. Hail from May through August can dent a car waiting outside, and spring floods close the river-bottom roads.'),
  P('Road salt and sand run all winter, and some owners choose enclosed transport for a collector car.'),
 )+chips(["Sioux Falls","Brandon","Harrisburg","Brookings","Watertown","Aberdeen","Mitchell","Yankton","Vermillion","Huron","Pierre","Chamberlain","Wall","Rapid City","Box Elder","Spearfish","Sturgis","Deadwood","Custer","Hot Springs","Pine Ridge","Mission"])
 +NOTE('Serving all sixty-six South Dakota counties and the reservations. For a ranch, Hills, or reservation address, tell us the town and the nearest US highway, and give us the widest date range you can.')))

BODY.append(sec('Your Options','Open or Enclosed in South Dakota?',
 prose(
  L('Open transport is the everyday choice, and it is the easier one to match in a pass-through state.'),
  P('Enclosed carriers cross South Dakota less often, so an enclosed booking benefits even more from flexible dates. It keeps a car covered against hail, salt, and wind-blown grit.'),
  P('A daily driver rides open without concern outside hail season. Our <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages describe both.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a pickup when the next carrier crosses, and a delivery, with the winter deciding the timing.'),
  P('When the price is approved, we match the car with a carrier already crossing on Interstate 90 or 29. The driver records its condition on a Bill of Lading, and you sign at pickup. That record is your reference at delivery.'),
 )+ULI([
  "Remove personal belongings",
  "Keep about a quarter tank of fuel, or half a charge for an electric car",
  "Photograph the vehicle before pickup, roof and hood included",
  "Provide a working key and disclose mechanical issues",
  "Turn off aftermarket alarms",
  "For a ranch or reservation address, plan to meet the truck on the US highway",
 ])+prose(P('Our <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> guides cover each step.'))))

BODY.append(sec('Why Ship Guy','Why South Dakota Drivers Choose Ship Guy',
 prose(
  L('We quote the real window for a pass-through state and plan around the rally, the gates, and the wind.'),
  P('Ship Guy holds active FMCSA brokerage authority and a $75,000 surety bond, both listed with the federal register.'),
  P('One coordinator carries the shipment from quote to delivery and can arrange open, enclosed, or expedited transport. The <a href="services.html">services</a> page lists what we offer.'),
 ), alt=True))

FAQ=[
 ("Why does a South Dakota pickup take two to five days?","Because South Dakota is a pass-through market. Carriers cross on Interstate 90 between Chicago and the Northwest and add a stop when the timing and the load line up. Sioux Falls and Rapid City schedule in 2 to 5 days, and Pierre, the reservations, and the ranch country take 4 to 7. A wide date range puts your car on the next truck through."),
 ("How much does it cost to ship a car from South Dakota to Minneapolis or Denver?","Minneapolis from Sioux Falls usually runs two hundred fifty to three hundred eighty dollars for a sedan, about two hundred forty miles. Denver from Rapid City runs three hundred sixty to five hundred twenty, about three hundred ninety miles down US 85 and Interstate 25. Larger vehicles add 10 to 25 percent."),
 ("Can you handle a PCS move to Ellsworth?","Yes, the base outside Rapid City rotates airmen and families year round, with a summer peak. Many families ship a second vehicle through us, since orders may cover only one. Housing is gated, so the driver meets you outside it. Ship Guy has no military affiliation."),
 ("Does the Sturgis rally affect car shipping?","Yes, for ten days each August. Half a million riders fill every road from Rapid City to Spearfish, and carriers avoid the Hills entirely. We schedule Black Hills pickups before or after the rally. The east side of the state runs normally."),
 ("Do you serve Pierre and the middle of the state?","Yes, with honest timing. Pierre has no interstate, and the driver meets you on US 14 or 83. Pickups run 4 to 7 days, because the carrier detours off Interstate 90 for hours. A flexible date range is the biggest help."),
 ("Can you pick up on a ranch or a reservation?","Yes, on the US highway or in the nearest town. Ranch roads are gravel with cattle guards, and a seventy-five-foot trailer stays on the pavement. The reservations cover thousands of square miles of two-lane road, and the handoff is planned before dispatch."),
 ("Does winter stop car shipping in South Dakota?","It slows it. Ground blizzards shut Interstate 90 for a day or more from November through April, and the state closes it with gates. Carriers wait in the towns. A car arriving from a warm state needs winter oil, a strong battery, and a block heater."),
 ("Can you ship a car for an SDSU or USD student?","Yes, student cars move each August and again in May. Brookings and Vermillion both allow curbside on most streets, and the handoff happens at a lot near campus during move-in. An adult signs for the car. Winter arrivals need a block heater."),
 ("Can you ship a car that does not run?","Yes, non-running cars ship from every part of South Dakota. A winch-equipped carrier loads it, and the extra time carries a fee. On a pass-through corridor, that also affects how soon the right truck arrives. Tell us whether it can roll, steer, and brake."),
 ("What do you need for a South Dakota car shipping quote?","Both addresses, with the town and the nearest highway for a ranch or reservation pickup. The year, make, and model. Whether it runs and rolls. Open or enclosed, and the widest date range you can offer. That is a complete South Dakota quote request."),
]
BODY.append(faq_section(FAQ,'South Dakota FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book auto transport in South Dakota?','A quote takes about two minutes. Then give us the widest date range you can, and we will catch the next carrier crossing the state.','+18664992815','(866) 499-2815','Get your free South Dakota quote'))

build_state({
 'slug':'south-dakota-auto-transport',
 'title':'South Dakota Auto Transport &amp; Car Shipping | Ship Guy',
 'meta':'South Dakota auto transport with honest windows for a pass-through state. Interstate 90 and 29 lanes, Sioux Falls and Rapid City, Ellsworth moves, Sturgis rally timing, Pierre and the reservations, ranch-road pickups, blizzard gates. Free quote.',
 'h1':'South Dakota<br>Auto <span class="accent">Transport</span>',
 'lede':'Open, enclosed, and expedited car shipping across South Dakota, quoted the way the distances and the winter demand.',
 'brand':'South Dakota','keyword':'south dakota auto transport','abbr':'SD',
 'localterms':['south dakota','interstate 90','interstate 29','us 14','us 83','us 18','us 85','us 16','sioux falls','brookings','watertown','aberdeen','mitchell','yankton','vermillion','pierre','chamberlain','wall','rapid city','box elder','ellsworth','sturgis','rally','spearfish','deadwood','custer','black hills','pine ridge','rosebud','cheyenne river','reservation','ranch','gravel','cattle guard','blizzard','gates','no-travel','block heater','wind','hail','missouri river','sdsu','usd','pass-through'],
}, BODY, FAQ)
