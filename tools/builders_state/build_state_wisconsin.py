import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Support")]))

BODY.append(intro_block('Wisconsin','Wisconsin auto transport from the Chicago suburbs to the Northwoods cabins',
 ['Wisconsin auto transport is quick along the Chicago-to-Minneapolis lane and slows down the farther north the cabin sits.',
  'Ship Guy is a licensed auto transport broker. We book vetted carriers across Wisconsin, and we do not own the trucks.',
  'Interstate 94 runs from Kenosha through Milwaukee and Madison to Eau Claire and Minnesota. Interstate 90 joins it at Madison from Rockford and leaves it at Tomah for La Crosse, and Interstate 41 and 43 carry the Fox Valley and Green Bay.',
  'This page covers the corridor, Milwaukee, Madison and the university, Green Bay and the Fox Valley, the Northwoods and Door County, the snowbird lane, and the winter.'],
 'Wisconsin at a glance',
 ['Most pickups happen within 1 to 3 days in Milwaukee, Madison, Kenosha, and the Fox Valley, and within 2 to 5 days in the Northwoods, Door County, and the western farm counties.',
  'Chicago is a same-day lane from the southeast. Minneapolis, Des Moines, and Indianapolis take a day. Florida, Arizona, and the coasts run three to four.'],
 'Wisconsin has no city page yet, so this page carries the detail for Milwaukee, Madison, Green Bay, Appleton, Kenosha, Eau Claire, and the rest.'))

BODY.append(sec('The Corridor','Interstate 94, 90, 41, 43, and 39',
 prose(
  L('Wisconsin sits between two carrier hubs, and the road between them runs the length of the state.'),
  P('Interstate 94 carries the Chicago-to-Minneapolis lane through Kenosha, Racine, Milwaukee, Madison, and Eau Claire. A car anywhere along it rides a truck already making the trip.'),
  P('Interstate 90 comes in from Rockford, shares the road to Tomah, and leaves for La Crosse and Minnesota. Interstate 41 runs from Milwaukee through Fond du Lac, Oshkosh, and Appleton to Green Bay, and Interstate 43 follows the lake from Beloit through Milwaukee to Green Bay.'),
  P('Interstate 39 climbs from Madison through Stevens Point to Wausau. Everything north of Wausau is two-lane highway through forest and lakes.'),
  P('Towns on the interstates schedule fast. The Northwoods, Door County, and the western farm counties take an extra day or two.'),
 ), alt=True))

BODY.append(sec('Milwaukee','The Lake, the Brewers, and the Medical College',
 prose(
  L('Milwaukee is the largest city and the hub for the lakeshore, and it ships on the corporate and medical calendars.'),
  P('The manufacturers, the insurers, and the medical college relocate employees and residents on start dates each June and all year. The port receives cargo, and the motorcycle plant relocates engineers on program schedules.'),
  P('The older neighborhoods on the north and south sides have narrow streets and alleys, and the driver meets you on a main road or at a lot off Interstate 94. Brookfield, Waukesha, and the western suburbs are wide grids.'),
  P('Kenosha and Racine to the south fill with Chicago commuters and ship through the Chicago carrier pool. If your employer reimburses the shipment, we provide the documentation.'),
  P('The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side of a relocation.'),
 )))

ROUTES=[("Chicago, IL (from Milwaukee)","I-94 · ~90 mi","Same day","$170–$280"),("Minneapolis, MN (from Madison)","I-94 · ~270 mi","1 day","$260–$390"),
 ("Indianapolis, IN (from Milwaukee)","I-94/I-65 · ~280 mi","1 day","$260–$390"),("Des Moines, IA (from Madison)","I-90/I-80 · ~300 mi","1 day","$280–$420"),
 ("Detroit, MI (from Milwaukee)","I-94 · ~375 mi","1 day","$340–$490"),("St. Louis, MO (from Madison)","I-39/I-55 · ~375 mi","1 day","$340–$490"),
 ("Kansas City, MO (from Madison)","I-90/I-35 · ~560 mi","1–2 days","$450–$650"),("Nashville, TN (from Milwaukee)","I-65 · ~560 mi","1–2 days","$450–$650"),
 ("Denver, CO (from Madison)","I-90/I-80 · ~1,040 mi","3 days","$700–$1,000"),("Orlando, FL (from Milwaukee)","I-65/I-75 · ~1,300 mi","3–4 days","$850–$1,200")]
BODY.append(rate_table('Lanes &amp; Costs','Wisconsin Car Shipping Lanes and Estimated Costs',
 'Common lanes out of Milwaukee and Madison, with estimated open-transport ranges. Green Bay adds about a hundred miles to the north, and Eau Claire sits closer to Minneapolis. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a running sedan on an open trailer, priced from the nearer city. SUVs and pickups add about 10 to 25 percent, enclosed more. Winter and carrier availability on your dates set the real quote.',
 prose(
  P('Chicago and Minneapolis are the cheapest lanes, because Interstate 94 carries carriers between them all day. Indianapolis, Detroit, and St. Louis follow.'),
  P('The Northwoods and Door County cost more per mile because the carrier detours. The <a href="car-shipping-cost.html">cost guide</a> explains the other variables.'),
 ), alt=True))

BODY.append(sec('Madison','The Isthmus, the University, and the Software Campus',
 prose(
  L('Madison sits on an isthmus between two lakes, and its downtown was laid out before trucks.'),
  P('The state university brings tens of thousands of students to the isthmus each August and sends them home each May. The streets around campus are narrow, and the main street through downtown bans cars entirely, so the handoff happens at a lot off the Beltline or Interstate 90.'),
  P('Home football Saturdays close the streets around the stadium, and we schedule around the games. An adult signs for a student car, and both windows fill, so book two to three weeks ahead.'),
  P('State government and the software campus in Verona relocate employees from across the country on start dates. Middleton, Fitchburg, and the suburbs are wide grids where the truck reaches the curb.'),
 )))

BODY.append(sec('Green Bay &amp; the Fox Valley','Lambeau Sundays, the Paper Mills, and the Air Show',
 prose(
  L('The Fox Valley ships on paper, and Green Bay ships around eight Sundays a year.'),
  P('Home game Sundays fill every road around the stadium from Friday night through Sunday evening, and we schedule Green Bay pickups on other days. The port and the paper mills relocate managers on program schedules.'),
  P('Appleton, Oshkosh, Neenah, and Fond du Lac sit on Interstate 41 with the mills and the campuses. The air show in Oshkosh each July brings ten thousand aircraft and fills the highways for a week, and we schedule around it.'),
  P('Sheboygan and Manitowoc ship on Interstate 43 along the lake, and the Fox Valley pickups schedule in 1 to 3 days.'),
 ), alt=True))

BODY.append(sec('The Northwoods &amp; Door County','Cabins, Gravel, and One Road Up the Peninsula',
 prose(
  L('Half of Wisconsin goes up north on summer weekends, and some of it ships a car to stay.'),
  P('Minocqua, Eagle River, Hayward, and the Northwoods lake towns fill with cabin owners from May through October. Many keep a second car at the lake and ship it up in spring and back in fall.'),
  P('Cabin roads are gravel and narrow, and a seventy-five-foot trailer stays on the state highway. The driver meets you there or in town, and Northwoods pickups run 2 to 5 days.'),
  P('Door County is a peninsula with one main road and summer traffic from June through September. Sturgeon Bay, Fish Creek, and the peninsula towns run 2 to 4 days, and the driver meets you on Highway 42 or 57.'),
  P('Wausau, Stevens Point, and the Interstate 39 towns schedule faster. Fort McCoy near Sparta trains reserve units on drill schedules, and Ship Guy is a private broker with no military affiliation. Our <a href="military-car-shipping.html">military</a> page covers move planning.'),
 )))

BODY.append(sec('Winter &amp; the Snowbird Lane','Blizzards, Lake Effect, and Florida in October',
 prose(
  L('Wisconsin winter closes the interstates a few times a year, and it sends cars south every fall.'),
  P('Blizzards and ice shut Interstate 94 and 90 for a day at a time from December through March, and Milwaukee adds lake-effect snow. Carriers wait for the plows.'),
  P('Temperatures reach twenty below in the north, and a car that arrives from a warm state needs winter oil and a strong battery. Road salt runs all winter, and some owners choose enclosed transport for a collector car.'),
  P('Retirees from Milwaukee, Madison, and the Fox Valley ship cars to Florida and Arizona from October through December and bring them home from March through May. Two to three weeks of notice keeps the price steady, and our <a href="snowbird-car-shipping.html">snowbird</a> page has planning tips.'),
  P('Summer brings construction closures on every interstate and tornadoes in the south. When a warning is issued, the driver pulls over until it passes.'),
 )+chips(["Milwaukee","Wauwatosa","Brookfield","Waukesha","Kenosha","Racine","Madison","Middleton","Fitchburg","Verona","Janesville","Beloit","Green Bay","De Pere","Appleton","Oshkosh","Neenah","Fond du Lac","Sheboygan","Manitowoc","Eau Claire","La Crosse","Wausau","Stevens Point","Minocqua","Eagle River","Hayward","Sturgeon Bay","Fish Creek"])
 +NOTE('Serving all seventy-two Wisconsin counties. For a cabin, peninsula, or farm address, tell us the town and the nearest state highway.'), alt=True))

BODY.append(sec('Your Options','Open or Enclosed in Wisconsin?',
 prose(
  L('Open transport is the everyday choice, and the Interstate 94 lanes run on it.'),
  P('Enclosed transport keeps a car covered against road salt, slush, and gravel dust. Whitefish Bay, Mequon, and the lake estates keep enclosed carriers busy with collector cars.'),
  P('A commuter car rides open without trouble. Our <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages compare the two.'),
 )))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a loading on the corridor, and a delivery, with winter deciding the timing.'),
  P('Once the price is approved, a carrier on Interstate 94 or 90 takes the booking. The driver notes the car\u2019s condition on a Bill of Lading, and you sign it before loading. That note is your checklist at delivery.'),
 )+ULI([
  "Remove personal belongings",
  "Keep about a quarter tank of fuel",
  "Photograph the vehicle before pickup, especially after a salty winter",
  "Provide a working key and disclose mechanical issues",
  "Disable aftermarket alarms",
  "For a cabin or peninsula address, plan to meet the truck on the state highway",
 ])+prose(P('Our <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> guides cover each step.')), alt=True))

BODY.append(sec('Why Ship Guy','Why Wisconsin Drivers Choose Ship Guy',
 prose(
  L('We use the lane between two hubs and plan around the games, the cabins, and the snow.'),
  P('Ship Guy holds active FMCSA brokerage authority and a $75,000 surety bond, both listed with the federal register.'),
  P('One coordinator handles the shipment from quote to delivery and can set up open, enclosed, or expedited transport. The <a href="services.html">services</a> page shows the full range.'),
 )))

FAQ=[
 ("How much does it cost to ship a car from Wisconsin to Florida or Arizona?","Orlando from Milwaukee usually runs eight hundred fifty to twelve hundred dollars for a sedan, about thirteen hundred miles on Interstate 65 and 75. Phoenix runs nine hundred fifty to thirteen hundred fifty, about eighteen hundred miles. Season matters more than distance, and a southbound car in November costs more than in July. Larger vehicles add 10 to 25 percent."),
 ("Can you ship a car for a University of Wisconsin or Marquette student?","Yes, student cars move each August and again in May. Madison's isthmus streets are narrow, and the main street downtown bans cars, so the handoff happens at a lot off the Beltline or Interstate 90. Home football Saturdays close the streets around the stadium. An adult signs for the car."),
 ("Will a Packers home game affect my pickup in Green Bay?","Yes, home game Sundays fill every road around the stadium from Friday night through Sunday evening. We schedule Green Bay pickups on other days. The Fox Valley runs normally, except for the air show week in Oshkosh each July."),
 ("Can you deliver to a cabin up north?","To the state highway or the nearest town, yes. Cabin roads are gravel and narrow, and a seventy-five-foot trailer stays on pavement. Northwoods pickups run 2 to 5 days. Many owners ship a second car up in spring and back in fall."),
 ("Do you serve Door County?","Yes, with timing. The peninsula has one main road and summer traffic from June through September, so the driver meets you on Highway 42 or 57 or in town. Pickups run 2 to 4 days, and weekday mornings work best in summer."),
 ("Why are Chicago and Minneapolis so easy from Wisconsin?","Because Interstate 94 carries carriers between the two hubs all day, and the whole southern half of the state sits along it. Chicago is a same-day lane from Milwaukee at one hundred seventy to two hundred eighty dollars, and Minneapolis is a day from Madison."),
 ("Does winter close the interstates in Wisconsin?","A few times a season. Blizzards and ice shut Interstate 94 and 90 for a day at a time from December through March, and Milwaukee adds lake-effect snow. Carriers wait for the plows. A car arriving from a warm state needs winter oil and a strong battery."),
 ("Do you handle relocations to Madison and the software campus?","Yes, state government and the campus in Verona relocate employees from across the country on start dates. We plan the pickup around your first day. If your employer reimburses the shipment, we provide the documentation."),
 ("Can you ship a car that does not run?","Yes, non-running cars ship from every part of Wisconsin. A winch-equipped carrier loads it, and the extra time carries a fee. Tell us whether it can roll, steer, and brake."),
 ("What do you need for a Wisconsin car shipping quote?","Both addresses, with the town for a cabin, peninsula, or farm pickup. The year, make, and model. Whether it runs and rolls. Open or enclosed, and a date range. That is a complete Wisconsin quote request."),
]
BODY.append(faq_section(FAQ,'Wisconsin FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book auto transport in Wisconsin?','A quote takes about two minutes. Then tell us your town and dates, and we will match you with a carrier already on the corridor.','+18664992815','(866) 499-2815','Get your free Wisconsin quote'))

build_state({
 'slug':'wisconsin-auto-transport',
 'title':'Wisconsin Auto Transport &amp; Car Shipping | Ship Guy',
 'meta':'Wisconsin auto transport on the Chicago-to-Minneapolis lane and up to the Northwoods. Milwaukee and Madison, UW move-in and game days, Packers Sundays and the Oshkosh air show, cabin and Door County pickups, the snowbird lane, winter planning. Free quote.',
 'h1':'Wisconsin<br>Auto <span class="accent">Transport</span>',
 'lede':'Open, enclosed, and expedited car shipping across Wisconsin, planned around the corridor, the cabins, and the snow.',
 'brand':'Wisconsin','keyword':'wisconsin auto transport','abbr':'WI',
 'localterms':['wisconsin','interstate 94','interstate 90','interstate 41','interstate 43','interstate 39','beltline','milwaukee','wauwatosa','brookfield','waukesha','medical college','port','kenosha','racine','madison','isthmus','university of wisconsin','verona','software','middleton','janesville','green bay','lambeau','packers','appleton','oshkosh','air show','neenah','fond du lac','sheboygan','manitowoc','eau claire','la crosse','wausau','stevens point','northwoods','minocqua','eagle river','hayward','cabin','door county','sturgeon bay','fish creek','fort mccoy','blizzard','lake-effect','florida','arizona','snowbird'],
}, BODY, FAQ)
