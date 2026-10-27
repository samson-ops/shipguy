import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("2–5 Days","Honest Pickup"),("7 Days","Support")]))

BODY.append(intro_block('Vermont','Vermont auto transport on two interstates, and off the dirt roads that make up the rest',
 ['Vermont auto transport works on the two interstates that reach the state and stops at the dirt roads, covered bridges, and posted hills that make up most of it.',
  'Ship Guy is a licensed auto transport broker. We book vetted carriers across Vermont, and we do not own the trucks.',
  'Interstate 89 runs from New Hampshire through Montpelier to Burlington and the Canadian border. Interstate 91 runs the Connecticut River from Massachusetts through Brattleboro and White River Junction to the Northeast Kingdom, and US 7 carries the western side with no interstate at all.',
  'This page covers the two interstates and the honest windows, Burlington and the medical center, the ski towns and second homes, Rutland and the west, the Kingdom, mud season, and the roads a trailer cannot use.'],
 'Vermont at a glance',
 ['Most pickups happen within 2 to 5 days in Burlington, Montpelier, and the Interstate 89 and 91 towns, and within 3 to 6 days in the ski towns, Rutland, Bennington, and the Northeast Kingdom.',
  'Boston and Albany take one to two days. Hartford and New York take two. Philadelphia and Washington take two to three, and Florida runs four.'],
 'Vermont is a small market, and carriers come up from Boston, Albany, and New York. A flexible date range matters more here than almost anywhere in the Northeast.'))

BODY.append(sec('The Roads','Interstate 89, Interstate 91, and Everything a Trailer Cannot Use',
 prose(
  L('Vermont has more miles of dirt road than paved road, and a seventy-five-foot trailer stays off all of them.'),
  P('Interstate 89 carries Boston-to-Montreal traffic through White River Junction, Montpelier, and Burlington. Interstate 91 carries the Connecticut River valley from Brattleboro through St. Johnsbury to the border.'),
  P('US 7 runs the western side from Bennington through Rutland and Middlebury to Burlington on two lanes. US 4 reaches Killington and Rutland from the river, and US 2 crosses from Montpelier to the Kingdom.'),
  P('The town roads beyond those are gravel, and many cross covered bridges with weight and height limits no carrier can meet. The driver meets you on the state highway or in the village.'),
  P('Interstate towns schedule in 2 to 5 days. The ski towns, the west side, and the Kingdom take 3 to 6, and a wide date range keeps the price steady.'),
 ), alt=True))

BODY.append(sec('Burlington','The Lake, the Medical Center, the University, and the Chip Plant',
 prose(
  L('Burlington is the largest city in the state, and it ships on the medical and campus calendars.'),
  P('The medical center moves residents and physicians every June, and the university sends cars in each August and home each May. The hill streets near campus are steep and narrow, and the handoff happens at a lot near Interstate 89.'),
  P('The chip plant in Essex Junction relocates engineers on program schedules, and the airport in South Burlington makes fly-and-ship routine. Winooski and the older neighborhoods have tight streets, and Williston and the newer suburbs allow curbside.'),
  P('If your employer reimburses the shipment, we provide the documentation. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
 )))

ROUTES=[("Albany, NY","US-7/I-87 · ~155 mi","1 day","$200–$320"),("Manchester, NH","I-89 · ~160 mi","1 day","$220–$340"),
 ("Boston, MA","I-89/I-93 · ~215 mi","1–2 days","$230–$350"),("Hartford, CT","I-91 · ~230 mi","1–2 days","$240–$360"),
 ("Portland, ME","I-89/US-302 · ~230 mi","1–2 days","$250–$380"),("New York, NY","I-91/I-95 · ~300 mi","2 days","$270–$400"),
 ("Philadelphia, PA","I-91/I-95 · ~390 mi","2 days","$340–$490"),("Washington, DC","I-91/I-95 · ~530 mi","2–3 days","$450–$650"),
 ("Chicago, IL","I-90 · ~900 mi","3 days","$650–$900"),("Orlando, FL","I-95 · ~1,400 mi","4 days","$900–$1,250")]
BODY.append(rate_table('Lanes &amp; Costs','Vermont Car Shipping Lanes and Estimated Costs',
 'Common lanes out of Burlington, with estimated open-transport ranges. Brattleboro and Bennington sit closer to Hartford and Albany, and the Kingdom adds an hour to everything. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a running sedan on an open trailer, priced from Burlington. SUVs and pickups add about 10 to 25 percent, enclosed more. In a small market, your dates and carrier availability matter more than the miles.',
 prose(
  P('Albany, Boston, and Hartford are the easiest lanes, because that is where the carriers come from. The Florida lane runs full each fall and spring, which keeps it bookable despite the distance.'),
  P('The Kingdom and the west side cost more per mile because the carrier detours. The <a href="car-shipping-cost.html">cost guide</a> explains the other variables.'),
 ), alt=True))

BODY.append(sec('The Ski Towns','Stowe, Killington, Sugarbush, and Jay Peak',
 prose(
  L('Vermont\u2019s ski towns fill with second-home owners from New York and Boston, and every one sits at the end of a steep road.'),
  P('Stowe, Killington, Warren, and Jay draw families who ship a car up in November for the season and home in April. Summer adds a second wave in June and September.'),
  P('The access roads climb through gated drives and hairpins a trailer cannot take. The driver meets you in the village, at the resort base lot, or on the state route.'),
  P('Ski-town pickups run 3 to 6 days, and the holiday weeks fill the roads with visitors. A flexible date range in December and February keeps the price steady.'),
 )))

BODY.append(sec('The West, the Capital, and the Kingdom','Rutland, Bennington, Montpelier, and St. Johnsbury',
 prose(
  L('Away from the two interstates, Vermont ships on two-lane roads and small-town patience.'),
  P('Rutland and Bennington sit on US 7 with no interstate, and Middlebury and its college sit between them. Carriers reach the west side through Albany, and pickups run 3 to 6 days.'),
  P('Montpelier is the smallest state capital in the country, and state government relocates people on its own schedule. It sits on Interstate 89 and schedules in 2 to 5 days.'),
  P('St. Johnsbury and the Northeast Kingdom are the most remote corner of the state, hours from any carrier base. Pickups there run 4 to 7 days, and the handoff happens on US 2 or 5 or in town.'),
  P('Brattleboro and the southern river towns ship on Interstate 91 with the Hartford and New York lanes. Norwich and the Upper Valley share the lane with Hanover across the river.'),
 ), alt=True))

BODY.append(sec('Mud Season, Snow, and Foliage','The Vermont Calendar',
 prose(
  L('Vermont has a season named for what it does to the roads, and two more that fill them.'),
  P('Mud season runs from March into May. Towns post weight limits on their roads while the frost comes out, and the dirt roads turn to soup. A loaded carrier cannot use a posted road, so the driver meets you on the state highway.'),
  P('Snow closes the interstates a few times each winter, and the mountain roads more often. Carriers wait for the plows, and a car arriving from a warm state needs winter oil and a strong battery.'),
  P('Foliage brings tour buses and leaf-peepers to every road in the state for three weeks in October, and the ski holidays fill the mountain towns. A pickup in either can slide a day.'),
  P('The Canadian border sits at the top of both interstates. A move into Quebec is an international shipment with customs paperwork, and we arrange domestic shipping only.'),
 )+chips(["Burlington","South Burlington","Winooski","Essex Junction","Williston","Shelburne","Montpelier","Barre","Waterbury","Stowe","Warren","Waitsfield","Killington","Rutland","Middlebury","Bennington","Manchester VT","Brattleboro","Springfield VT","White River Junction","Norwich","St. Johnsbury","Newport VT","Jay"])
 +NOTE('Serving all fourteen Vermont counties. For a dirt-road, ski-town, or Kingdom address, tell us the town and the nearest state highway, and give us the widest date range you can.')))

BODY.append(sec('Your Options','Open or Enclosed in Vermont?',
 prose(
  L('Open transport is the everyday choice, and it is the easier one to match in a small market.'),
  P('Enclosed carriers reach Vermont less often, so an enclosed booking benefits even more from flexible dates. It keeps a car covered against road salt, mud-season grit, and slush.'),
  P('A commuter car rides open without a problem. Our <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages compare the two.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a pickup when the next carrier comes north, and a delivery, with the season deciding the timing.'),
  P('When the price is approved, we match the car with a carrier heading up Interstate 89 or 91. The driver records its condition on a Bill of Lading, and you sign at pickup. That record is your reference at delivery.'),
 )+ULI([
  "Remove personal belongings",
  "Keep about a quarter tank of fuel",
  "Photograph the vehicle before pickup, especially after a salty winter",
  "Provide a working key and disclose mechanical issues",
  "Turn off aftermarket alarms",
  "On a dirt road or in mud season, plan to meet the truck on the state highway",
 ])+prose(P('Our <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> guides cover each step.'))))

BODY.append(sec('Why Ship Guy','Why Vermont Drivers Choose Ship Guy',
 prose(
  L('We quote honest windows for a small state and know which roads, bridges, and hills a trailer cannot use.'),
  P('Ship Guy holds active FMCSA brokerage authority and a $75,000 surety bond, both listed with the federal register.'),
  P('One coordinator carries the shipment from quote to delivery and can arrange open, enclosed, or expedited transport. The <a href="services.html">services</a> page lists what we offer.'),
 ), alt=True))

FAQ=[
 ("Why does a Vermont pickup take two to five days?","Because Vermont is a small market, and carriers come up from Boston, Albany, and New York when a load justifies it. Interstate towns schedule in 2 to 5 days, and the ski towns, the west side, and the Kingdom take 3 to 6. A wide date range puts your car on the next truck north."),
 ("Can the carrier come down my dirt road?","No, a seventy-five-foot trailer stays on the pavement, and Vermont has more dirt road than paved. Many town roads also cross covered bridges with weight and height limits no carrier can meet. The driver meets you on the state highway or in the village, and the handoff is planned before dispatch."),
 ("Can you deliver to Stowe, Killington, or the ski towns?","Yes, with a meeting spot. The access roads climb through gated drives and hairpins, so the driver meets you in the village, at the resort base lot, or on the state route. Ski-town pickups run 3 to 6 days, and second-home owners ship up in November and home in April."),
 ("What is mud season, and does it affect car shipping in Vermont?","From March into May, towns post weight limits on their roads while the frost comes out, and the dirt roads turn to soup. A loaded carrier cannot use a posted road, so the driver meets you on the state highway. It adds a few minutes of driving on your end and nothing to the price."),
 ("How much does it cost to ship a car from Vermont to Florida?","Orlando from Burlington usually runs nine hundred to twelve hundred fifty dollars for a sedan, about fourteen hundred miles down Interstate 91 and 95. Miami runs a little more. Season matters more than distance, and a southbound car in November costs more than in July. Larger vehicles add 10 to 25 percent."),
 ("Do you serve Rutland, Bennington, and the west side?","Yes, but plan on 3 to 6 days. US 7 runs the west side with no interstate, and carriers reach it through Albany. The driver meets you on Route 7 or in town. A flexible date range keeps the price steady."),
 ("Do you serve the Northeast Kingdom?","Yes, with honest timing. St. Johnsbury, Newport, and the Kingdom sit hours from any carrier base, and pickups run 4 to 7 days. The handoff happens on US 2 or 5 or in town. A wide date range is the biggest help."),
 ("Can you ship a car to Canada from Vermont?","No, a move into Quebec is an international shipment with customs paperwork and a different carrier. We arrange domestic shipping only. We deliver to the border towns on the Vermont side."),
 ("Can you ship a car that does not run?","Yes, non-running cars ship from every part of Vermont. A winch-equipped carrier loads it, and the extra time carries a fee. In a small market, that also affects how soon the right truck arrives. Tell us whether it can roll, steer, and brake."),
 ("What do you need for a Vermont car shipping quote?","Both addresses, with the town and the nearest state highway for a dirt-road or ski-town pickup. The year, make, and model. Whether it runs and rolls. Open or enclosed, and the widest date range you can offer. That is a complete Vermont quote request."),
]
BODY.append(faq_section(FAQ,'Vermont FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book auto transport in Vermont?','A quote takes about two minutes. Then tell us your town and dates, and we will find the next carrier coming north and the spot where it can stop.','+18664992815','(866) 499-2815','Get your free Vermont quote'))

build_state({
 'slug':'vermont-auto-transport',
 'title':'Vermont Auto Transport &amp; Car Shipping | Ship Guy',
 'meta':'Vermont auto transport with honest windows for a small market. Interstate 89 and 91 lanes, Burlington and the medical center, ski-town meeting spots, Rutland and the Kingdom, dirt roads and covered bridges, mud season, the Florida lane. Free quote.',
 'h1':'Vermont<br>Auto <span class="accent">Transport</span>',
 'lede':'Open, enclosed, and expedited car shipping across Vermont, planned around the interstates, the seasons, and the roads a trailer cannot use.',
 'brand':'Vermont','keyword':'vermont auto transport','abbr':'VT',
 'localterms':['vermont','interstate 89','interstate 91','us 7','us 4','us 2','us 5','burlington','south burlington','winooski','essex junction','chip plant','williston','medical center','university of vermont','montpelier','barre','waterbury','stowe','warren','sugarbush','killington','jay peak','rutland','middlebury','bennington','brattleboro','white river junction','norwich','upper valley','st. johnsbury','northeast kingdom','newport','dirt road','covered bridge','posted','mud season','foliage','leaf','canada','quebec','border','boston','albany','florida'],
}, BODY, FAQ)
