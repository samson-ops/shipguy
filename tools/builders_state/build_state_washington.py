import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Support")]))

BODY.append(intro_block('Washington','Washington auto transport from the Sound to Spokane, over one pass or another',
 ['Washington auto transport is easy along the Interstate 5 corridor and takes a mountain pass, a ferry, or a long dry drive to reach everywhere else.',
  'Ship Guy is a licensed auto transport broker. We book vetted carriers across Washington, and we do not own the trucks.',
  'Interstate 5 runs from Vancouver through Olympia, Tacoma, Seattle, and Everett to the Canadian border. Interstate 90 crosses Snoqualmie Pass to Ellensburg and Spokane, and Interstate 82 drops through Yakima to the Tri-Cities.',
  'This page covers the corridor, Seattle and the tech relocations, the bases on the Sound, the passes, Spokane and the east, the ferries and the peninsula, the ports, and the weather.'],
 'Washington at a glance',
 ['Most pickups happen within 1 to 3 days from Olympia to Everett and in Spokane, within 2 to 4 days in the Tri-Cities, Yakima, and Bellingham, and within 3 to 5 days on the peninsula and the islands.',
  'Portland is a same-day lane from the Sound. Spokane, Boise, and Sacramento take a day. California, the Mountain West, and the rest of the country run two to four.'],
 'Washington has no city page yet, so this page carries the detail for Seattle, Bellevue, Tacoma, Everett, Olympia, Spokane, the Tri-Cities, and the rest.'))

BODY.append(sec('The Corridor','Interstate 5 From Vancouver to the Border',
 prose(
  L('Most of Washington lives within thirty miles of Interstate 5, and the carriers run it all day.'),
  P('The corridor carries Portland-to-Canada traffic through Olympia, Tacoma, Seattle, Everett, and Bellingham, and it backs up from Tacoma to Everett every rush hour. Carriers plan Sound stops for mid-morning and early afternoon.'),
  P('Interstate 405 loops the east side through Bellevue and Redmond, and the floating bridges carry Seattle to the east side with a toll on one of them. Interstate 5 and 405 are the roads a trailer uses, and the bridge toll is built into every quote.'),
  P('Vancouver at the south end ships through the Portland carrier pool, and Bellingham at the north end ships on the Seattle lane.'),
 ), alt=True))

BODY.append(sec('Seattle &amp; the East Side','Tech Relocations, the Hills, and the Towers',
 prose(
  L('Seattle and Bellevue relocate more engineers than almost any metro in the country, and most of them ship a car.'),
  P('The software, retail, and aerospace employers in Seattle, Redmond, and Bellevue relocate households from across the country on start dates. Corporate packages usually cover a vehicle, and we provide the documentation.'),
  P('Seattle\u2019s hills are steep and its older neighborhoods narrow, and the towers downtown and in Bellevue run on garages. The driver meets you on a main road or at a lot near Interstate 5 or 405.'),
  P('Bothell, Issaquah, Sammamish, and the newer suburbs allow curbside on most streets, and many have gates, so send the community name. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side of a relocation.'),
 )))

ROUTES=[("Portland, OR","I-5 · ~175 mi","Same day","$220–$340"),("Spokane, WA","I-90 · ~280 mi","1 day","$260–$390"),
 ("Boise, ID","I-90/I-82/I-84 · ~500 mi","1 day","$430–$620"),("Sacramento, CA","I-5 · ~750 mi","2 days","$560–$820"),
 ("San Francisco, CA","I-5 · ~810 mi","2 days","$600–$880"),("Salt Lake City, UT","I-90/I-84 · ~840 mi","2 days","$600–$880"),
 ("Los Angeles, CA","I-5 · ~1,135 mi","3 days","$800–$1,150"),("Denver, CO","I-90/I-84/I-80 · ~1,320 mi","3 days","$850–$1,200"),
 ("Phoenix, AZ","I-5/US-93 · ~1,420 mi","3–4 days","$900–$1,300"),("Chicago, IL","I-90 · ~2,060 mi","4 days","$1,100–$1,550")]
BODY.append(rate_table('Lanes &amp; Costs','Washington Car Shipping Lanes and Estimated Costs',
 'Common lanes out of the Seattle area, with estimated open-transport ranges. Spokane sits closer to the Mountain West, and Vancouver follows Portland lanes. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a running sedan on an open trailer, priced from the Seattle area. SUVs and pickups add about 10 to 25 percent, enclosed more. Pass closures and carrier availability on your dates set the real quote.',
 prose(
  P('Portland and California are the cheapest lanes, because Interstate 5 carries carriers the length of the coast all day. Interstate 90 makes Spokane and the Mountain West steady.'),
  P('The peninsula, the islands, and the far east cost more per mile because the carrier detours. The <a href="car-shipping-cost.html">cost guide</a> explains the other variables.'),
 ), alt=True))

BODY.append(sec('Military','Lewis-McChord, Kitsap, Whidbey, Everett, and Fairchild',
 prose(
  L('Washington has more military households on the move than any state in the Northwest.'),
  P('Joint Base Lewis-McChord south of Tacoma deploys and returns whole brigades and airlift wings, and families rotate year round with a summer peak. Naval Base Kitsap in Bremerton and Bangor rotates submarine crews across the Sound.'),
  P('The naval air station on Whidbey Island and the naval station in Everett rotate squadrons and ship crews. Fairchild Air Force Base in Spokane flies tankers and rotates airmen on the same summer calendar.'),
  P('Many families ship a second vehicle through us, since orders may cover only one. Housing is gated at each, so the driver meets you outside it. Kitsap and Whidbey sit across the water, and the handoff happens on the base side of the ferry.'),
  P('Ship Guy is a private broker with no military affiliation. Our <a href="military-car-shipping.html">military</a> page covers PCS timing.'),
 )))

BODY.append(sec('The Passes &amp; the East','Snoqualmie, Stevens, Spokane, and the Tri-Cities',
 prose(
  L('Everything east of the Cascades is a different state in climate, and one pass decides when it is reachable.'),
  P('Snoqualmie Pass on Interstate 90 carries chain controls from November through April and closes for avalanche control and crashes. Stevens Pass on US 2 and White Pass on US 12 close more often. A loaded carrier waits below a closure.'),
  P('Spokane is the second-largest city in the state and the hub for eastern Washington and the Idaho panhandle. The hospitals, the universities, and Fairchild relocate people year round, and pickups schedule in 1 to 3 days.'),
  P('The Tri-Cities ship on the national laboratory and the Hanford cleanup, with engineers relocating on program schedules. Yakima and Wenatchee ship on agriculture, and Pullman sends university cars in each August and home each May.'),
  P('Walla Walla, the Palouse, and the far east run 2 to 4 days, and wind on the Columbia slows a high-profile trailer.'),
 ), alt=True))

BODY.append(sec('Ferries, the Peninsula, and the Ports','Where the Truck Stops and the Boat Takes Over',
 prose(
  L('A lot of Washington is reached by ferry, and a car carrier does not board one.'),
  P('Bainbridge, Vashon, Whidbey, and the San Juan Islands take a ferry from the mainland terminals. Carriers deliver to the terminal, and you or a local driver take the car across. Ferry reservations fill weeks ahead in summer.'),
  P('The Olympic Peninsula sits at the end of US 101, a winding two-lane loop around the mountains. Port Angeles, Sequim, and the peninsula towns run 3 to 5 days, and the driver meets you on 101 or in town.'),
  P('The ports of Seattle and Tacoma receive imported cars, and we ship them domestically once customs releases them. The ocean leg is separate.'),
  P('Retirees in Sequim and the islands, and second-home owners on the Sound, ship on their own seasonal calendar.'),
 )))

BODY.append(sec('Weather','Rain, Snow on the Passes, and Smoke in the East',
 prose(
  L('Washington weather is rain on the Sound, snow on the passes, and dry heat and smoke in the east.'),
  P('The Sound gets rain from October through May, and it changes only the loading hour. A rare lowland snow shuts Seattle\u2019s hills for a day or two, and carriers wait for the melt.'),
  P('The passes get real snow, and the east gets subzero nights from December through February. A car arriving from a warm state needs winter oil and a strong battery east of the mountains.'),
  P('Fire season from July through October fills the east with smoke and closes highways a few times a summer. Carriers reroute around a closure, and we tell you the moment the forecast changes the plan.'),
 )+chips(["Seattle","Bellevue","Redmond","Kirkland","Bothell","Issaquah","Renton","Kent","Federal Way","Tacoma","Lakewood","Puyallup","Olympia","Everett","Marysville","Bellingham","Bremerton","Silverdale","Oak Harbor","Port Angeles","Sequim","Vancouver","Spokane","Spokane Valley","Richland","Kennewick","Pasco","Yakima","Wenatchee","Walla Walla","Pullman"])
 +NOTE('Serving all thirty-nine Washington counties, with the islands by ferry. For a hillside, island, peninsula, or eastern address, tell us the town and we will name the meeting spot.'), alt=True))

BODY.append(sec('Your Options','Open or Enclosed in Washington?',
 prose(
  L('Open transport is the everyday choice, and the Interstate 5 lanes run on it.'),
  P('Enclosed transport keeps a car covered against rain, road grit, and pass salt. Medina, Mercer Island, and the Sound estates keep enclosed carriers busy with collector cars.'),
  P('A commuter car rides open without a problem. Our <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages describe both.'),
 )))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a loading on the corridor, and a delivery, with the pass or the ferry deciding the last leg.'),
  P('Once the price is approved, a carrier on Interstate 5 or 90 takes the booking. The driver records the car\u2019s condition on a Bill of Lading, and you sign it before loading. That record is your reference at delivery.'),
 )+ULI([
  "Remove personal belongings",
  "Keep about a quarter tank of fuel",
  "Photograph the vehicle before pickup",
  "Provide a working key and disclose mechanical issues",
  "Disable aftermarket alarms",
  "For an island or a hillside address, plan to meet the truck at the terminal or on the main road",
 ])+prose(P('Our <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> guides cover each step.')), alt=True))

BODY.append(sec('Why Ship Guy','Why Washington Drivers Choose Ship Guy',
 prose(
  L('We know which pass is closed, which ferry the truck cannot board, and which hour the corridor moves.'),
  P('Ship Guy holds active FMCSA brokerage authority and a $75,000 surety bond, both listed with the federal register.'),
  P('One coordinator handles the shipment from quote to delivery and can set up open, enclosed, or expedited transport. The <a href="services.html">services</a> page shows what we arrange.'),
 )))

FAQ=[
 ("How much does it cost to ship a car from California to Seattle?","Sacramento to Seattle usually runs five hundred sixty to eight hundred twenty dollars for a sedan, about seven hundred fifty miles up Interstate 5. Los Angeles runs eight hundred to eleven hundred fifty. The lane runs full with tech relocations, which keeps it competitive. Larger vehicles add 10 to 25 percent."),
 ("Can you handle a PCS move to Lewis-McChord, Kitsap, Whidbey, or Fairchild?","Yes, Washington moves more military households than any state in the Northwest, and every installation is a steady lane for us. Many families ship a second vehicle through us, since orders may cover only one. Housing is gated, so the driver meets you outside it. Kitsap and Whidbey handoffs happen on the base side of the ferry. Ship Guy has no military affiliation."),
 ("Can the carrier come to my house in Seattle?","Rarely on the hills or downtown. Seattle's streets are steep and narrow, and the towers run on garages, so the driver meets you on a main road or at a lot near Interstate 5 or 405. Bothell, Issaquah, and the newer suburbs often allow curbside."),
 ("Do you ship cars to Bainbridge, Whidbey, or the San Juans?","We deliver to the ferry terminal on the mainland, and the island leg goes by ferry. Ferry reservations for a car fill weeks ahead in summer, so book that first. Once the car is on the island, you or a local driver take it from the dock."),
 ("Does Snoqualmie Pass close for car shipping?","Chain controls apply on Interstate 90 from November through April, and the pass closes for avalanche control and crashes a few times each winter. A loaded carrier waits below a closure rather than chain up. Stevens and White passes close more often. We tell you when a pass is in play."),
 ("Do you serve Spokane and eastern Washington?","Yes, Spokane is the second-largest market in the state for us, with the hospitals, the universities, and Fairchild relocating people year round. Pickups schedule in 1 to 3 days, and Boise and the Mountain West are the natural lanes. The Tri-Cities, Yakima, and Walla Walla run 2 to 4 days."),
 ("Do you handle tech relocations to Seattle and Bellevue?","Yes, the software, retail, and aerospace employers relocate households from across the country on start dates, and most ship a car. We plan the pickup around your first day. If your employer reimburses the shipment, we provide the documentation. Many east-side subdivisions have gates, so send the community name."),
 ("Can you ship a car that arrived at the port of Seattle or Tacoma?","The ocean leg is an international process we do not arrange. Once customs releases the car, we ship it domestically like any other. Give us the release date and the terminal. Enclosed transport is available for a high-value import."),
 ("Can you ship a car that does not run?","Yes, non-running cars ship from every part of Washington. A winch-equipped carrier loads it, and the extra time carries a fee. Say whether it can roll, steer, and brake."),
 ("What do you need for a Washington car shipping quote?","Both addresses, with the town for an island, peninsula, or eastern pickup. The year, make, and model. Whether it runs and rolls. Open or enclosed, and a date range. That is a complete Washington quote request."),
]
BODY.append(faq_section(FAQ,'Washington FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book auto transport in Washington?','A quote takes about two minutes. Then tell us your town and dates, and we will plan around the corridor, the pass, or the ferry.','+18664992815','(866) 499-2815','Get your free Washington quote'))

build_state({
 'slug':'washington-auto-transport',
 'title':'Washington Auto Transport &amp; Car Shipping | Ship Guy',
 'meta':'Washington auto transport from the Sound to Spokane. Seattle and Bellevue tech relocations, Lewis-McChord, Kitsap, and Whidbey moves, Snoqualmie Pass timing, ferry-terminal delivery for the islands, the Tri-Cities and the east, port releases. Free quote.',
 'h1':'Washington<br>Auto <span class="accent">Transport</span>',
 'lede':'Open, enclosed, and expedited car shipping across Washington, planned around the corridor, the passes, and the water.',
 'brand':'Washington','keyword':'washington auto transport','abbr':'WA',
 'localterms':['washington','interstate 5','interstate 90','interstate 82','interstate 405','us 2','us 12','us 101','snoqualmie','stevens pass','white pass','floating bridge','seattle','bellevue','redmond','kirkland','bothell','issaquah','tacoma','lakewood','olympia','everett','bellingham','vancouver','lewis-mcchord','kitsap','bremerton','bangor','whidbey','oak harbor','naval station everett','fairchild','spokane','tri-cities','richland','kennewick','pasco','hanford','yakima','wenatchee','walla walla','pullman','ferry','bainbridge','vashon','san juan','olympic peninsula','port angeles','sequim','port','customs','smoke','fire season'],
}, BODY, FAQ)
