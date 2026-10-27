import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Support")]))

BODY.append(intro_block('Utah','Utah auto transport along the Wasatch Front, and the long roads beyond it',
 ['Utah auto transport is easy along the hundred miles where nearly everyone lives, and honest work everywhere the state opens into desert and canyon.',
  'Ship Guy is a licensed auto transport broker. We book vetted carriers across Utah, and we do not own the trucks.',
  'Interstate 15 runs the Wasatch Front from Ogden through Salt Lake City and Provo to St. George and Nevada. Interstate 80 crosses from Wendover through the city and Parleys Canyon to Wyoming, and Interstate 70 cuts across the south with the longest stretch of nothing on the interstate system.',
  'This page covers the Front and its boom, Provo and the tech corridor, Ogden and the base, St. George and the retirees, Park City and the canyons, Logan and Moab, and the winter.'],
 'Utah at a glance',
 ['Most pickups happen within 1 to 3 days from Ogden to Provo, within 2 to 4 days in St. George, Logan, and Park City, and within 3 to 6 days in Moab, Vernal, and the desert counties.',
  'Las Vegas, Boise, Denver, and Reno take a day from the Front. Phoenix, Los Angeles, and Portland take two. Texas and the Midwest run three.'],
 'Salt Lake City has its own page covering the grid, the airport, and the Wasatch canyons. This page carries Provo, Ogden, St. George, Park City, Logan, Moab, and the rest of the state.'))

BODY.append(sec('The Front','Interstate 15 From Ogden to Provo, and the Boom Along It',
 prose(
  L('Utah grew faster than any state this decade, and nearly all of it happened along one road.'),
  P('Interstate 15 carries the Wasatch Front from Ogden through Salt Lake City, Lehi, and Provo, with Interstate 215 looping the capital. A car anywhere along it schedules in a day or two.'),
  P('Households from California, Washington, and Colorado fill Lehi, Saratoga Springs, Eagle Mountain, and Herriman on closing dates all year. Most ship one car and drive the other, and the subdivisions outpace carrier maps, so send the full address.'),
  P('Utah families are large, and the cars are big. An SUV or a minivan costs 10 to 25 percent more than a sedan on every lane, and we quote the real size.'),
  P('If your employer reimburses the shipment, we provide the documentation. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
 ), alt=True))

BODY.append(state_cities_block('UT','Utah','Salt Lake City has its own page with the grid, the airport, and the canyon meeting spots. Provo, Ogden, St. George, Park City, Logan, Moab, and the rest of Utah are covered from this page.'))

BODY.append(sec('Provo &amp; the Tech Corridor','The University, Lehi, and Silicon Slopes',
 prose(
  L('Utah County ships on the largest private university in the West and the tech companies that grew up around it.'),
  P('Brigham Young University in Provo sends cars in each August and home each April, on a calendar that also sends thousands of students abroad and back. Move-in week clogs the campus streets, and the handoff happens at a lot nearby.'),
  P('The software and hardware companies in Lehi, Draper, and the Point of the Mountain relocate engineers from across the country on start dates. Corporate packages usually cover a vehicle.'),
  P('Provo and Orem are wide grids where the truck usually reaches the curb. An adult signs for a student car.'),
 )))

ROUTES=[("Provo, UT","I-15 · ~45 mi","Same day","$150–$240"),("Ogden, UT","I-15 · ~40 mi","Same day","$150–$240"),
 ("Boise, ID","I-84 · ~340 mi","1 day","$320–$460"),("Las Vegas, NV","I-15 · ~420 mi","1 day","$380–$540"),
 ("Denver, CO","I-80/I-70 · ~520 mi","1–2 days","$430–$620"),("Reno, NV","I-80 · ~520 mi","1–2 days","$430–$620"),
 ("Sacramento, CA","I-80 · ~650 mi","2 days","$480–$700"),("Los Angeles, CA","I-15 · ~690 mi","2 days","$500–$730"),
 ("Portland, OR","I-84 · ~770 mi","2 days","$560–$820"),("Seattle, WA","I-84/I-82 · ~840 mi","2–3 days","$600–$880")]
BODY.append(rate_table('Lanes &amp; Costs','Utah Car Shipping Lanes and Estimated Costs',
 'Common lanes out of the Wasatch Front, with estimated open-transport ranges. St. George sits three hundred miles closer to Las Vegas and Los Angeles. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a running sedan on an open trailer, priced from the Salt Lake area. SUVs and pickups add about 10 to 25 percent, enclosed more. Canyon closures and carrier availability on your dates set the real quote.',
 prose(
  P('Las Vegas, Denver, and Boise are the cheapest long lanes, because Interstate 15, 80, and 84 carry carriers between them all day. California runs full inbound.'),
  P('Moab, Vernal, and the desert counties cost more per mile because the carrier detours. The <a href="car-shipping-cost.html">cost guide</a> explains the other variables.'),
 ), alt=True))

BODY.append(sec('Ogden &amp; the Base','Hill Air Force Base and the North End',
 prose(
  L('The north end of the Front ships on one of the largest Air Force bases in the country.'),
  P('Hill Air Force Base between Ogden and Layton maintains fighters and rotates airmen, civilians, and contractors year round with a summer peak. Its civilian workforce is one of the largest employers in the state.'),
  P('Housing is gated, so the driver meets you outside it. Many families ship a second vehicle through us, since orders may cover only one.'),
  P('Ogden\u2019s older neighborhoods have narrow streets, and the driver meets you on a main road. Layton, Syracuse, and the Davis County suburbs are wide grids.'),
  P('Ship Guy is a private broker with no military affiliation. Our <a href="military-car-shipping.html">military</a> page covers PCS timing.'),
 )))

BODY.append(sec('St. George &amp; the South','Retirees, Snowbirds Within the State, and the Vegas Lane',
 prose(
  L('St. George is the fastest-growing corner of a fast-growing state, and it ships through Las Vegas.'),
  P('Retirees from the Front, California, and the Northwest fill St. George, Washington, and Hurricane on closing dates all year. Many Front families keep a second car in the south and ship it down each winter and back each spring.'),
  P('The city sits on Interstate 15 two hours from Las Vegas and four from Salt Lake City, and it shares the Las Vegas carrier pool. Pickups run 2 to 4 days, and the golf communities have gates, so send the community name.'),
  P('Cedar City and the state university ship on the same lane. Summer heat in the south passes 105 degrees, and drivers load early.'),
 ), alt=True))

BODY.append(sec('Park City, Logan, and Moab','The Resorts, the Cache Valley, and the Desert',
 prose(
  L('The rest of Utah ships on ski towns, a college valley, and canyon country.'),
  P('Park City sits up Parleys Canyon on Interstate 80, and its resort neighborhoods are steep and gated. The driver meets you at a lot in Kimball Junction or on Park Avenue, and the film festival each January fills the town for ten days.'),
  P('Second-home owners ship cars up in November and out in April. Heber, Midway, and the Wasatch Back share the lane.'),
  P('Logan and the state university sit in the Cache Valley an hour north of the Front on US 89 and 91, with a winter inversion that traps the cold. Student cars move each August and May.'),
  P('Moab sits on US 191 four hours from the Front, and Vernal on US 40 three hours east. Both run 3 to 6 days, and the driver meets you on the highway or in town.'),
 )))

BODY.append(sec('Winter &amp; the Canyons','Parleys, the Inversion, and the Passes',
 prose(
  L('Utah winter is snow in the canyons and cold trapped in the valleys.'),
  P('Parleys Canyon on Interstate 80 carries chain controls from November through April, and a loaded carrier waits below a closure. Spanish Fork Canyon on US 6 and the Wasatch Back passes close more often.'),
  P('The inversion settles over the Front and the Cache Valley for weeks each winter, and it changes nothing for a carrier. Interstate 15 south of the Front closes in a blizzard a few times a season.'),
  P('Interstate 70 across the south runs more than a hundred miles with no services, and wind slows a high-profile trailer there. Spring runoff floods the canyon roads in May.'),
  P('Summer brings fire season and smoke to the mountains from July through September. A car that arrives from sea level runs a little rough at altitude at first.'),
 )+chips(["Salt Lake City","Sandy","Draper","Herriman","Lehi","Saratoga Springs","Eagle Mountain","Provo","Orem","Ogden","Layton","Syracuse","Bountiful","Park City","Heber","Midway","Logan","Tooele","St. George","Washington","Hurricane","Cedar City","Moab","Vernal","Richfield"])
 +NOTE('Serving all twenty-nine Utah counties. For a resort, canyon, or desert address, tell us the town and the nearest highway.'), alt=True))

BODY.append(sec('Your Options','Open or Enclosed in Utah?',
 prose(
  L('Open transport is the everyday choice, and the Interstate 15 lanes run on it.'),
  P('Enclosed transport keeps a car covered against road salt, canyon grit, and desert sun. Park City, Holladay, and the Alpine estates keep enclosed carriers busy with collector cars.'),
  P('A commuter car rides open without trouble. Our <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages describe both.'),
 )))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a loading on the Front or the highway, and a delivery, with the canyon deciding the timing in winter.'),
  P('Once the price is approved, a carrier on Interstate 15 or 80 takes the booking. The driver records the car\u2019s condition on a Bill of Lading, and you sign it before loading. That record is your reference at delivery.'),
 )+ULI([
  "Remove personal belongings",
  "Keep about a quarter tank of fuel",
  "Photograph the vehicle before pickup",
  "Provide a working key and disclose mechanical issues",
  "Disable aftermarket alarms",
  "For a resort or desert address, plan to meet the truck on the highway",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> guides go step by step.')), alt=True))

BODY.append(sec('Why Ship Guy','Why Utah Drivers Choose Ship Guy',
 prose(
  L('We know which canyon is closed, which lane St. George belongs to, and how much a minivan really costs to ship.'),
  P('Ship Guy holds active FMCSA brokerage authority and a $75,000 surety bond, both listed with the federal register.'),
  P('One coordinator handles the shipment from quote to delivery and can set up open, enclosed, or expedited transport. The <a href="services.html">services</a> page shows what we arrange.'),
 )))

FAQ=[
 ("How much does it cost to ship a car from California to Utah?","Los Angeles to the Wasatch Front usually runs five hundred to seven hundred thirty dollars for a sedan, about six hundred ninety miles up Interstate 15. Sacramento runs four hundred eighty to seven hundred on Interstate 80. St. George is three hundred miles closer to Los Angeles. The lane runs full with California transplants, and larger vehicles add 10 to 25 percent."),
 ("Why does an SUV or a minivan cost more to ship in Utah?","Because a carrier is priced by the space and weight a vehicle takes, and Utah ships more large family vehicles than almost any state. An SUV or minivan costs 10 to 25 percent more than a sedan on every lane, and a full-size truck can cost more. We quote the real size up front."),
 ("Can you handle a PCS move to Hill Air Force Base?","Yes, the base between Ogden and Layton rotates airmen, civilians, and contractors year round, with a summer peak. Many families ship a second vehicle through us, since orders may cover only one. Housing is gated, so the driver meets you outside it. Ship Guy has no military affiliation."),
 ("Do you serve St. George?","Yes, St. George is one of our busiest lanes in the state. It sits two hours from Las Vegas and shares that city's carrier pool, so pickups run 2 to 4 days. Many Front families ship a second car down each winter and back each spring. The golf communities have gates, so send the community name."),
 ("Can you deliver to Park City in winter?","Yes, with a canyon in the way. Parleys Canyon carries chain controls from November through April, and a loaded carrier waits below a closure. The resort neighborhoods are steep and gated, so the driver meets you at a lot in Kimball Junction or on Park Avenue. We schedule around the film festival in January."),
 ("Can you ship a car for a BYU, Utah, or Utah State student?","Yes, student cars move each August and again in April or May. Move-in week clogs the campus streets in Provo, so the handoff happens at a lot nearby. Logan allows curbside on most streets. An adult signs for the car, and the Salt Lake campus is covered on the city page."),
 ("Do you serve Moab, Vernal, and rural Utah?","Yes, with honest timing. Moab sits four hours from the Front on US 191, and Vernal three hours east on US 40, so pickups run 3 to 6 days. Interstate 70 across the south runs more than a hundred miles with no services. A flexible date range keeps the price steady."),
 ("Do you handle relocations to the tech corridor in Lehi?","Yes, the software and hardware companies at the Point of the Mountain relocate engineers from across the country on start dates. We plan the pickup around your first day. If your employer reimburses the shipment, we provide the documentation. New subdivisions outpace carrier maps, so send the full address."),
 ("Can you ship a car that does not run?","Yes, non-running cars ship from every part of Utah. A winch-equipped carrier loads it, and the extra time carries a fee. Tell us whether it can roll, steer, and brake."),
 ("What do you need for a Utah car shipping quote?","Both addresses, with the community name for a gated address. The year, make, and model, and the real size if it is an SUV or a minivan. Whether it runs and rolls. Open or enclosed, and a date range. That is a complete Utah quote request."),
]
BODY.append(faq_section(FAQ,'Utah FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book auto transport in Utah?','A quote takes about two minutes. Then tell us your town and dates, and we will plan around the canyon and the lane.','+18664992815','(866) 499-2815','Get your free Utah quote'))

build_state({
 'slug':'utah-auto-transport',
 'title':'Utah Auto Transport &amp; Car Shipping | Ship Guy',
 'meta':'Utah auto transport along the Wasatch Front and beyond. Provo and the tech corridor, Hill Air Force Base moves, St. George through the Las Vegas lane, Park City and Parleys Canyon, Logan and Moab windows, real pricing for family SUVs, city page for Salt Lake City. Free quote.',
 'h1':'Utah<br>Auto <span class="accent">Transport</span>',
 'lede':'Open, enclosed, and expedited car shipping across Utah, planned around the Front, the canyons, and the desert.',
 'brand':'Utah','keyword':'utah auto transport','abbr':'UT',
 'localterms':['utah','interstate 15','interstate 80','interstate 70','interstate 84','interstate 215','us 6','us 89','us 191','us 40','wasatch','salt lake city','provo','orem','byu','lehi','draper','point of the mountain','silicon slopes','saratoga springs','eagle mountain','herriman','ogden','layton','hill air force base','davis county','st. george','washington','hurricane','cedar city','park city','kimball junction','parleys','film festival','heber','midway','logan','cache valley','inversion','moab','vernal','tooele','minivan','suv','california','chain','fire season','altitude'],
}, BODY, FAQ)
