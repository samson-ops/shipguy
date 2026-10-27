import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("2–4 Days","Typical Pickup"),("7 Days","Support")]))

BODY.append(intro_block('West Virginia','West Virginia auto transport on the interstates, the Turnpike, and the roads that follow the creeks',
 ['West Virginia auto transport is easy where the interstates run and honest work everywhere the road turns into a hollow.',
  'Ship Guy is a licensed auto transport broker. We book vetted carriers across West Virginia, and we do not own the trucks.',
  'Interstate 64 crosses from Huntington through Charleston and Beckley to Virginia. Interstate 77 runs from Parkersburg through Charleston and the Turnpike to Princeton, Interstate 79 climbs from Charleston to Morgantown, and Interstate 81 clips the Eastern Panhandle.',
  'This page covers the corridors and the Turnpike, Charleston and Huntington, Morgantown and the university, the Eastern Panhandle and its commuters, the coalfields, the resorts, and the mountains in winter.'],
 'West Virginia at a glance',
 ['Most pickups happen within 2 to 4 days in Charleston, Huntington, Morgantown, and the Eastern Panhandle, and within 3 to 6 days in the coalfields, the Potomac Highlands, and the mountain resorts.',
  'Pittsburgh, Columbus, Cincinnati, and Washington take about a day from one end of the state or another. Charlotte, Richmond, and Cleveland take one to two. Florida and the Midwest run three.'],
 'West Virginia has no city page yet, so this page carries the detail for Charleston, Huntington, Morgantown, Martinsburg, Beckley, Wheeling, Parkersburg, and the rest.'))

BODY.append(sec('The Corridors','Interstate 64, 77, 79, 81, and the Turnpike',
 prose(
  L('West Virginia sits between Ohio and the Carolinas, and the carriers that cross it pay a toll to do it.'),
  P('Interstate 77 carries the Cleveland-to-Charlotte lane through Parkersburg, Charleston, and Beckley. The Turnpike from Charleston to Princeton charges by the axle, and the tolls are built into every quote.'),
  P('Interstate 64 carries the Kentucky-to-Virginia lane through Huntington, Charleston, Beckley, and Lewisburg. Interstate 79 links Charleston to Clarksburg, Morgantown, and Pittsburgh, and Interstate 70 crosses the Northern Panhandle at Wheeling.'),
  P('Interstate 81 crosses the Eastern Panhandle in twenty-six miles, carrying Martinsburg on the Washington lane. Interstate 68 reaches Morgantown from Maryland, and the new four-lane corridor across the mountains reaches the Potomac Highlands.'),
  P('Towns on those roads schedule in 2 to 4 days. The coalfields, the highlands, and the resorts take 3 to 6, because the roads follow the creeks and a trailer cannot.'),
 ), alt=True))

BODY.append(sec('Charleston &amp; Huntington','The Capital, the Chemical Valley, and the River',
 prose(
  L('The two largest cities sit on the rivers where the interstates meet, and carriers stage there.'),
  P('Charleston holds state government and the chemical plants along the Kanawha, and both relocate people on their own schedules. The older neighborhoods climb the hillsides on narrow streets, and the driver meets you on a main road or in the valley.'),
  P('Huntington sits on the Ohio River with the university and the hospitals, and residents arrive every June. Its streets are a grid where the truck usually reaches the curb.'),
  P('Parkersburg and Wheeling ship on the Ohio lane, with Interstate 77 and 70 to Columbus and Pittsburgh. If your employer reimburses the shipment, we provide the documentation.'),
  P('The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side of a relocation.'),
 )))

ROUTES=[("Pittsburgh, PA (from Morgantown)","I-79 · ~75 mi","Same day","$150–$240"),("Washington, DC (from Martinsburg)","I-81/I-66 · ~80 mi","Same day","$170–$280"),
 ("Columbus, OH (from Charleston)","US-35/I-70 · ~165 mi","1 day","$220–$340"),("Lexington, KY (from Huntington)","I-64 · ~120 mi","1 day","$200–$320"),
 ("Cincinnati, OH (from Huntington)","US-52/I-71 · ~150 mi","1 day","$220–$340"),("Cleveland, OH (from Wheeling)","I-70/I-77 · ~185 mi","1 day","$230–$350"),
 ("Charlotte, NC (from Beckley)","I-77 · ~230 mi","1 day","$260–$390"),("Richmond, VA (from Charleston)","I-64 · ~315 mi","1–2 days","$290–$420"),
 ("Nashville, TN (from Charleston)","I-64/I-75/I-40 · ~430 mi","2 days","$380–$540"),("Orlando, FL (from Beckley)","I-77/I-95 · ~840 mi","3 days","$620–$880")]
BODY.append(rate_table('Lanes &amp; Costs','West Virginia Car Shipping Lanes and Estimated Costs',
 'Common lanes out of Charleston, Huntington, Morgantown, Martinsburg, and Beckley, with estimated open-transport ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a running sedan on an open trailer, priced from the nearer city. SUVs and pickups add about 10 to 25 percent, enclosed more. Turnpike tolls are included, and mountain pickups plus carrier availability on your dates set the real quote.',
 prose(
  P('Pittsburgh from Morgantown and Washington from Martinsburg are among the cheapest lanes anywhere, because both cities sit an hour away on a busy interstate. Ohio and Kentucky follow.'),
  P('The coalfields and the highlands cost more per mile because the carrier detours. The <a href="car-shipping-cost.html">cost guide</a> explains the other variables.'),
 ), alt=True))

BODY.append(sec('Morgantown','The University, the Hills, and the Pittsburgh Lane',
 prose(
  L('Morgantown is the fastest-growing city in the state, and one campus fills it every August.'),
  P('West Virginia University sends cars in each August and home each May, and home football Saturdays close the streets around the stadium. The campus and the older neighborhoods climb steep hills, and the driver meets you on a main road or at a lot off Interstate 79.'),
  P('An adult signs for a student car, and both windows fill, so book two to three weeks ahead. Pittsburgh is an hour north on Interstate 79, which keeps carriers coming.'),
  P('Clarksburg, an hour south, holds the FBI\u2019s identification center and relocates federal employees on program schedules. Fairmont and the Interstate 79 towns share the lane.'),
 )))

BODY.append(sec('The Eastern Panhandle','Martinsburg, the Washington Commute, and the Coast Guard',
 prose(
  L('The Eastern Panhandle is closer to Washington than to Charleston, and it moves on Washington\u2019s calendar.'),
  P('Martinsburg, Charles Town, and Berkeley County fill with commuters who moved west for the housing, and the county grows faster than any in the state. Most ship one car and drive the other.'),
  P('The Coast Guard operations center and the federal offices in Martinsburg relocate employees on start dates. Harpers Ferry and the river towns sit on narrow historic streets, and the driver meets you on the highway.'),
  P('Pickups in the panhandle schedule in 2 to 4 days through the Washington and Baltimore carrier pools. Ship Guy is a private broker with no military affiliation, and our <a href="military-car-shipping.html">military</a> page covers federal and PCS moves.'),
 ), alt=True))

BODY.append(sec('The Coalfields &amp; the Highlands','Beckley, Bluefield, Logan, Elkins, and the Hollows',
 prose(
  L('Southern and eastern West Virginia is where the roads follow the creeks, and a seventy-five-foot trailer cannot follow them.'),
  P('Beckley and Bluefield sit on Interstate 77 and 64 and schedule in 2 to 4 days. Logan, Williamson, Welch, and the coalfields sit on two-lane highways through the hollows, with switchbacks and no shoulders.'),
  P('For a hollow address, the driver meets you on the four-lane road or in the county seat. Coalfield pickups run 3 to 6 days, and a flexible date range keeps the price steady.'),
  P('Elkins and the Potomac Highlands sit on the new corridor and the old mountain roads, and the resorts at Snowshoe and the Greenbrier add seasonal waves. Resort roads are steep, and the driver meets you at the base or in town.'),
 )))

BODY.append(sec('Weather','Mountain Snow, Fog, Ice, and the Floods',
 prose(
  L('West Virginia weather works by elevation, and the interstates climb through all of it.'),
  P('Snow and ice close the Turnpike, Interstate 79, and the mountain stretches of Interstate 64 a few times each winter. Fog settles into the valleys on fall mornings and closes the mountain passes for hours.'),
  P('Carriers wait for the plows and the sun. A car arriving from a warm state needs winter oil in the highlands.'),
  P('Floods hit the state hard, from the creek valleys in the south to the river towns along the Ohio. A flooded hollow road can be out for weeks, and the handoff moves to the highway.'),
  P('Fall foliage brings traffic to the mountain roads for a few weeks in October. Summer is mild and busy.'),
 )+chips(["Charleston","South Charleston","Huntington","Barboursville","Morgantown","Fairmont","Clarksburg","Bridgeport","Martinsburg","Charles Town","Harpers Ferry","Wheeling","Weirton","Parkersburg","Vienna","Beckley","Bluefield","Princeton","Lewisburg","White Sulphur Springs","Elkins","Logan","Williamson","Summersville"])
 +NOTE('Serving all fifty-five West Virginia counties. For a hollow, highland, or resort address, tell us the county seat and the nearest four-lane road, and give us a wide date range.'), alt=True))

BODY.append(sec('Your Options','Open or Enclosed in West Virginia?',
 prose(
  L('Open transport is the everyday choice, and the Interstate 77 and 79 lanes run on it.'),
  P('Enclosed carriers cross the mountains less often, so an enclosed booking benefits from flexible dates. It keeps a car covered against road salt, mountain grit, and coal dust.'),
  P('A commuter car rides open without a problem. Our <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages compare both.'),
 )))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a loading on the interstate, and a delivery, with the mountains deciding the timing.'),
  P('Once the price is approved, a carrier on Interstate 77, 79, or 64 takes the booking. The driver records the car\u2019s condition on a Bill of Lading, and you sign it before loading. That record is your reference at delivery.'),
 )+ULI([
  "Remove personal belongings",
  "Keep about a quarter tank of fuel",
  "Photograph the vehicle before pickup",
  "Provide a working key and disclose mechanical issues",
  "Turn off aftermarket alarms",
  "For a hollow or hillside address, plan to meet the truck on the four-lane road",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> guides go step by step.')), alt=True))

BODY.append(sec('Why Ship Guy','Why West Virginia Drivers Choose Ship Guy',
 prose(
  L('We use the lanes that cross the state and quote honest windows for the hollows.'),
  P('Ship Guy holds active FMCSA brokerage authority and a $75,000 surety bond, both verifiable in federal records.'),
  P('One coordinator carries the shipment from quote to delivery and can arrange open, enclosed, or expedited transport. The <a href="services.html">services</a> page lists the options.'),
 )))

FAQ=[
 ("Is the West Virginia Turnpike toll added to my price?","It is built into the quote. Carriers pay the Turnpike between Charleston and Princeton by the axle and price accordingly. There is no separate line. Interstate 64, 79, and 81 carry no toll."),
 ("Can you pick up in the coalfields or a hollow?","Yes, on the four-lane road or in the county seat. Two-lane highways with switchbacks and no shoulders keep a seventy-five-foot trailer out of the hollows, and the driver meets you where it can stop. Coalfield pickups run 3 to 6 days, and a flexible date range keeps the price steady."),
 ("Why is Morgantown to Pittsburgh so cheap?","Because Pittsburgh sits an hour north on Interstate 79, and carriers run that lane daily. It usually costs one hundred fifty to two hundred forty dollars for a sedan. Martinsburg to Washington works the same way on Interstate 81 and 66."),
 ("Can you ship a car for a WVU or Marshall student?","Yes, student cars move each August and again in May. Morgantown's campus climbs steep hills, and home football Saturdays close the streets around the stadium, so the handoff happens at a lot off Interstate 79. Huntington allows curbside on most streets. An adult signs for the car."),
 ("Do you serve the Eastern Panhandle?","Yes, Martinsburg, Charles Town, and Berkeley County ship through the Washington and Baltimore carrier pools in 2 to 4 days. Commuters who moved west for the housing and the federal offices keep the lane steady. Harpers Ferry's historic streets mean a handoff on the highway."),
 ("Does winter close the interstates in West Virginia?","A few times each winter. Snow and ice close the Turnpike, Interstate 79, and the mountain stretches of Interstate 64 for a day, and fog closes the passes for hours on fall mornings. Carriers wait for the plows and the sun. We tell you when a road is in play."),
 ("Can you deliver to Snowshoe or the Greenbrier?","Yes, with a meeting spot. Resort roads are steep, so the driver meets you at the base or in town. Snowshoe sits hours from any interstate, and pickups run 3 to 6 days. Lewisburg and White Sulphur Springs sit on Interstate 64 and schedule faster."),
 ("Why does a West Virginia pickup take two to four days instead of one to three?","Because the state is a small market between bigger ones, and carriers come from Pittsburgh, Columbus, Charlotte, and Washington when a load justifies the stop. The interstate towns schedule in 2 to 4 days, and the mountains take longer. A wide date range puts your car on the next truck through."),
 ("Can you ship a car that does not run?","Yes, non-running cars ship from every part of West Virginia. A winch-equipped carrier loads it, and the extra time carries a fee. Tell us whether it can roll, steer, and brake."),
 ("What do you need for a West Virginia car shipping quote?","Both addresses, with the county seat and the nearest four-lane road for a hollow or mountain pickup. The year, make, and model. Whether it runs and rolls. Open or enclosed, and the widest date range you can offer. That is a complete West Virginia quote request."),
]
BODY.append(faq_section(FAQ,'West Virginia FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book auto transport in West Virginia?','A quote takes about two minutes. Then tell us your county and dates, and we will plan the interstate and the meeting spot.','+18664992815','(866) 499-2815','Get your free West Virginia quote'))

build_state({
 'slug':'west-virginia-auto-transport',
 'title':'West Virginia Auto Transport &amp; Car Shipping | Ship Guy',
 'meta':'West Virginia auto transport on Interstate 64, 77, and 79 and the Turnpike. Charleston and Huntington, WVU move-in and game days, the Eastern Panhandle commute, coalfield meeting spots, mountain snow and fog, honest windows. Free quote.',
 'h1':'West Virginia<br>Auto <span class="accent">Transport</span>',
 'lede':'Open, enclosed, and expedited car shipping across West Virginia, planned around the interstates, the Turnpike, and the hollows.',
 'brand':'West Virginia','keyword':'west virginia auto transport','abbr':'WV',
 'localterms':['west virginia','interstate 64','interstate 77','interstate 79','interstate 81','interstate 68','interstate 70','turnpike','corridor h','charleston','kanawha','chemical','huntington','marshall','morgantown','wvu','fairmont','clarksburg','fbi','martinsburg','charles town','berkeley county','harpers ferry','coast guard','eastern panhandle','wheeling','weirton','parkersburg','beckley','bluefield','princeton','lewisburg','greenbrier','white sulphur springs','snowshoe','elkins','potomac highlands','logan','williamson','welch','coalfields','hollow','fog','flood','foliage','pittsburgh'],
}, BODY, FAQ)
