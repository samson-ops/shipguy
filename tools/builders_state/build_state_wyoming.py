import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("3–6 Days","Honest Pickup"),("7 Days","Support")]))

BODY.append(intro_block('Wyoming','Wyoming auto transport on the windiest interstate in the country',
 ['Wyoming auto transport runs on Interstate 80, and Interstate 80 runs on the weather.',
  'Ship Guy is a licensed auto transport broker. We book vetted carriers across Wyoming, and we do not own the trucks.',
  'Interstate 80 crosses the south from Cheyenne through Laramie, Rawlins, and Rock Springs to Evanston and Utah. Interstate 25 runs from Cheyenne through Casper to Buffalo, and Interstate 90 crosses the northeast through Gillette and Sheridan to Montana.',
  'This page covers the three interstates and the honest windows, Cheyenne and the base, Casper and the energy towns, Laramie, Jackson and the passes, the ranch roads, and the wind that closes the road.'],
 'Wyoming at a glance',
 ['Most pickups happen within 3 to 6 days in Cheyenne, Laramie, Casper, and the Interstate 80 towns, and within 5 to 10 days in Jackson, Cody, Sheridan, and the ranch country.',
  'Denver and Fort Collins take about a day from Cheyenne. Salt Lake City, Billings, and Rapid City take two. Omaha, Kansas City, and Boise take two to three, and the coasts run four to five.'],
 'Wyoming is the least populous state, and a pass-through market. Carriers cross on Interstate 80 between Salt Lake City and Nebraska and add a stop when the load justifies it. A wide date range is the biggest help you can give us.'))

BODY.append(sec('The Corridors','Interstate 80, 25, and 90, and the Road That Closes',
 prose(
  L('Three interstates cross Wyoming, and the one that matters most closes more than any road in the country.'),
  P('Interstate 80 carries Salt Lake City-to-Omaha freight across the high plains. Between Laramie and Rawlins it climbs above seven thousand feet, and the state closes it for wind, blowing snow, and crashes dozens of times each winter.'),
  P('Interstate 25 carries the Denver-to-Billings lane through Cheyenne, Wheatland, Douglas, and Casper. Interstate 90 carries Gillette and Sheridan on the Rapid City-to-Billings lane.'),
  P('US 287, 26, 20, and 191 reach everything else on two lanes, and the distances between towns run to a hundred miles. Cheyenne and the Interstate 80 towns schedule in 3 to 6 days, and the rest of the state takes 5 to 10.'),
 ), alt=True))

BODY.append(sec('Cheyenne','The Capital, the Base, and Frontier Days',
 prose(
  L('Cheyenne is the carrier hub of the state, an hour from Denver and sitting on two interstates.'),
  P('F.E. Warren Air Force Base runs a missile wing and rotates airmen and families year round, with a summer peak. Housing is gated, so the driver meets you outside it, and many families ship a second vehicle through us since orders may cover only one.'),
  P('State government relocates people on its own schedule, and the Denver lane keeps carriers coming through daily. Cheyenne\u2019s streets are a wide grid where the truck usually reaches the curb.'),
  P('Frontier Days fills the city for ten days each July, and the roads crawl. We schedule Cheyenne pickups before or after it.'),
  P('Ship Guy is a private broker with no military affiliation. Our <a href="military-car-shipping.html">military</a> page covers PCS timing.'),
 )))

ROUTES=[("Denver, CO (from Cheyenne)","I-25 · ~100 mi","1 day","$170–$280"),("Fort Collins, CO (from Cheyenne)","I-25 · ~45 mi","1 day","$150–$240"),
 ("Rapid City, SD (from Gillette)","I-90 · ~135 mi","1–2 days","$220–$340"),("Billings, MT (from Sheridan)","I-90 · ~130 mi","1–2 days","$220–$340"),
 ("Salt Lake City, UT (from Evanston)","I-80 · ~85 mi","1–2 days","$170–$280"),("Salt Lake City, UT (from Cheyenne)","I-80 · ~440 mi","2 days","$400–$570"),
 ("Omaha, NE (from Cheyenne)","I-80 · ~500 mi","2–3 days","$430–$620"),("Kansas City, MO (from Cheyenne)","I-80/I-29 · ~640 mi","3 days","$470–$680"),
 ("Dallas, TX (from Cheyenne)","I-25/US-287 · ~900 mi","3–4 days","$650–$900"),("Phoenix, AZ (from Cheyenne)","I-25/I-40 · ~1,000 mi","4 days","$700–$1,000")]
BODY.append(rate_table('Lanes &amp; Costs','Wyoming Car Shipping Lanes and Estimated Costs',
 'Common lanes out of Cheyenne and the corner towns, with estimated open-transport ranges. Casper adds about a hundred eighty miles to every Cheyenne lane, and Jackson adds a pass. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a running sedan on an open trailer, priced from the nearer town. SUVs and pickups add about 10 to 25 percent, enclosed more. In a pass-through market, your dates and carrier availability matter more than the miles.',
 prose(
  P('Denver from Cheyenne is the easiest lane in the state, because the two cities sit an hour apart on Interstate 25. Salt Lake City from Evanston works the same way at the other end.'),
  P('Jackson, Cody, and the ranch country cost more per mile because the carrier detours for hours. The <a href="car-shipping-cost.html">cost guide</a> explains the other variables.'),
 ), alt=True))

BODY.append(sec('Casper, Laramie, and the Energy Towns','The Middle, the University, and the Boom Cycle',
 prose(
  L('Away from Cheyenne, Wyoming ships on oil, gas, coal, and one university.'),
  P('Casper sits in the middle of the state on Interstate 25 and ships on the oil fields and the hospitals. Gillette, Rock Springs, and Evanston boom and bust with coal, gas, and trona, and workers ship pickups in and out on hiring cycles.'),
  P('Laramie holds the state university, an hour west of Cheyenne on Interstate 80 at seven thousand feet. Student cars move each August and May, and the handoff happens at a lot near campus.'),
  P('Sheridan and Buffalo ship on Interstate 90 toward Billings. Riverton, Lander, and the Wind River country sit on two-lane highways and run 5 to 10 days.'),
  P('If your employer reimburses the shipment, we provide the documentation. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
 )))

BODY.append(sec('Jackson &amp; the Passes','Teton Pass, the Park, and the Resort Season',
 prose(
  L('Jackson is the hardest place in the state to reach with a car carrier, and the wealthiest.'),
  P('The town sits at the end of US 191 and 26, hours from any interstate, with Teton Pass to the west closing to trucks in winter and Togwotee Pass to the east closing in a storm. Carriers reach it through Idaho Falls or up from Rock Springs.'),
  P('Second-home owners ship cars in for ski season in November and for summer in June, and the resort roads have gates and steep drives. The driver meets you at a lot in Jackson or on the highway.'),
  P('Jackson pickups run 5 to 10 days, and the airport makes fly-and-ship routine. Cody at the east gate of the park runs the same window, and both fill with tourists from June through September.'),
 ), alt=True))

BODY.append(sec('Ranch Country','Gravel, Cattle Guards, and Antelope',
 prose(
  L('Most of Wyoming is ranchland, and a seventy-five-foot trailer stays on the pavement.'),
  P('Ranch roads are gravel, cross cattle guards, and run for miles from the nearest highway. The driver meets you on the paved road or in the nearest town, and the handoff is planned before dispatch.'),
  P('Antelope and deer cross the highways at dawn and dusk year round, and drivers slow down for them. It never stops a shipment, but it shapes the schedule.'),
  P('Spring turns the gravel to mud, and fall brings hunters and stock trucks to every county road.'),
 )))

BODY.append(sec('The Wind &amp; the Winter','Why Interstate 80 Closes, and What the Cold Does to a Car',
 prose(
  L('Wyoming wind is a fact of shipping, not a forecast.'),
  P('Gusts on Interstate 80 between Laramie and Rawlins reach sixty and seventy miles an hour, and the state closes the road to high-profile vehicles when they do. A loaded car carrier is exactly the vehicle the closure is for, and it waits in Laramie or Rawlins until the road reopens.'),
  P('Ground blizzards close all three interstates for a day or more from October through April. Temperatures reach thirty below, and a car arriving from a warm state needs winter-weight oil, a strong battery, and a block heater.'),
  P('An electric car loses real range in that cold and should arrive at half charge and go straight to a charger. Summer brings hail on the plains and fire smoke in the mountains.'),
  P('We build the wind into every Interstate 80 window and tell you the moment the road closes.'),
 )+chips(["Cheyenne","Laramie","Rawlins","Rock Springs","Green River","Evanston","Casper","Douglas","Wheatland","Torrington","Gillette","Sheridan","Buffalo","Riverton","Lander","Jackson","Cody","Powell","Worland","Thermopolis","Pinedale","Afton"])
 +NOTE('Serving all twenty-three Wyoming counties. For a ranch, Jackson, or park-gateway address, tell us the town and the nearest paved highway, and give us the widest date range you can.'), alt=True))

BODY.append(sec('Your Options','Open or Enclosed in Wyoming?',
 prose(
  L('Open transport is the everyday choice, and it is the easier one to match on a pass-through interstate.'),
  P('Enclosed carriers cross Wyoming less often, so an enclosed booking benefits even more from flexible dates. It keeps a car covered against gravel, salt, and wind-driven grit, and Jackson keeps them busy with collector cars.'),
  P('A daily driver rides open without concern. Our <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages describe both.'),
 )))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a pickup when the next carrier crosses, and a delivery, with the wind deciding the timing.'),
  P('When the price is approved, we match the car with a carrier already crossing on Interstate 80, 25, or 90. The driver records its condition on a Bill of Lading, and you sign at pickup. That record is your reference at delivery.'),
 )+ULI([
  "Remove personal belongings",
  "Keep about a quarter tank of fuel, or half a charge for an electric car",
  "Photograph the vehicle before pickup, roof and hood included",
  "Provide a working key and disclose mechanical issues",
  "Turn off aftermarket alarms",
  "For a ranch or resort address, plan to meet the truck on the paved highway",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> guides go step by step.')), alt=True))

BODY.append(sec('Why Ship Guy','Why Wyoming Drivers Choose Ship Guy',
 prose(
  L('We quote the real window for the emptiest state on the map and plan around the road that closes.'),
  P('Ship Guy holds active FMCSA brokerage authority and a $75,000 surety bond, both verifiable in federal records.'),
  P('One coordinator carries the shipment from quote to delivery and can arrange open, enclosed, or expedited transport. The <a href="services.html">services</a> page lists what we offer.'),
 )))

FAQ=[
 ("Why does a Wyoming pickup take three to six days?","Because Wyoming is the least populous state and a pass-through market. Carriers cross on Interstate 80 between Salt Lake City and Nebraska and add a stop when the timing and the load line up. Cheyenne and the corridor towns schedule in 3 to 6 days, and Jackson, Cody, and the ranch country take 5 to 10. A wide date range puts your car on the next truck through."),
 ("Does the wind really close Interstate 80?","Yes, dozens of times each winter. Gusts between Laramie and Rawlins reach sixty and seventy miles an hour, and the state closes the road to high-profile vehicles when they do. A loaded car carrier is exactly what the closure is for, and it waits in Laramie or Rawlins until the road reopens. We build the wind into every Interstate 80 window."),
 ("How much does it cost to ship a car from Wyoming to Denver or Salt Lake City?","Denver from Cheyenne usually runs one hundred seventy to two hundred eighty dollars for a sedan, about a hundred miles down Interstate 25. Salt Lake City from Cheyenne runs four hundred to five hundred seventy across the whole state, and from Evanston it is a hundred seventy to two hundred eighty. Larger vehicles add 10 to 25 percent."),
 ("Can you handle a PCS move to F.E. Warren?","Yes, the base in Cheyenne rotates airmen and families year round, with a summer peak. Many families ship a second vehicle through us, since orders may cover only one. Housing is gated, so the driver meets you outside it. Ship Guy has no military affiliation."),
 ("Can you deliver to Jackson?","Yes, with honest timing. Jackson sits hours from any interstate, with Teton Pass closed to trucks in winter, and carriers reach it through Idaho Falls or up from Rock Springs. Pickups run 5 to 10 days, and the driver meets you at a lot in town or on the highway. Second-home owners ship in for November and June."),
 ("Can you pick up on a ranch?","Yes, on the paved highway or in the nearest town. Ranch roads are gravel with cattle guards, and a seventy-five-foot trailer stays off them. The handoff is planned before dispatch, and spring mud and fall hunting traffic each add a day."),
 ("Does Frontier Days affect car shipping in Cheyenne?","Yes, for ten days each July. The city fills and the roads crawl, so we schedule Cheyenne pickups before or after it. The rest of the state runs normally."),
 ("Can you ship a car for a University of Wyoming student?","Yes, student cars move each August and again in May. Laramie sits an hour west of Cheyenne on Interstate 80 at seven thousand feet, and the handoff happens at a lot near campus. An adult signs for the car. Winter arrivals need a block heater and a strong battery."),
 ("Can you ship a car that does not run?","Yes, non-running cars ship from every part of Wyoming. A winch-equipped carrier loads it, and the extra time carries a fee. On a pass-through corridor, that also affects how soon the right truck arrives. Tell us whether it can roll, steer, and brake."),
 ("What do you need for a Wyoming car shipping quote?","Both addresses, with the town and the nearest paved highway for a ranch or resort pickup. The year, make, and model. Whether it runs and rolls. Open or enclosed, and the widest date range you can offer. That is a complete Wyoming quote request."),
]
BODY.append(faq_section(FAQ,'Wyoming FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book auto transport in Wyoming?','A quote takes about two minutes. Then give us the widest date range you can, and we will catch the next carrier crossing the state when the road is open.','+18664992815','(866) 499-2815','Get your free Wyoming quote'))

build_state({
 'slug':'wyoming-auto-transport',
 'title':'Wyoming Auto Transport &amp; Car Shipping | Ship Guy',
 'meta':'Wyoming auto transport with honest windows for the emptiest state on the map. Interstate 80 wind closures, Cheyenne and F.E. Warren, Casper and the energy towns, Laramie, Jackson through the passes, ranch-road pickups, thirty-below winters. Free quote.',
 'h1':'Wyoming<br>Auto <span class="accent">Transport</span>',
 'lede':'Open, enclosed, and expedited car shipping across Wyoming, quoted the way the wind and the distances demand.',
 'brand':'Wyoming','keyword':'wyoming auto transport','abbr':'WY',
 'localterms':['wyoming','interstate 80','interstate 25','interstate 90','us 287','us 26','us 20','us 191','cheyenne','warren','frontier days','laramie','university of wyoming','rawlins','rock springs','green river','evanston','casper','douglas','gillette','sheridan','buffalo','riverton','lander','wind river','jackson','teton pass','togwotee','cody','yellowstone','park','ranch','gravel','cattle guard','antelope','wind','high-profile','ground blizzard','thirty below','block heater','pass-through','denver','salt lake'],
}, BODY, FAQ)
