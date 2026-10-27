import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Green Bay, Wisconsin','Car shipping at the head of the bay, in a city that runs on trucking, paper, and football Sundays',
 ['Car shipping in Green Bay is easier than the map suggests, because the city runs on trucking. Ship Guy is a licensed auto transport broker with an office on North Broadway downtown.',
  'We book vetted carriers across Brown County, from De Pere and Ashwaubenon to Howard, Suamico, and Bellevue. We do not own the trucks.',
  'Interstate 43 comes up the lakeshore from Milwaukee and crosses the bay on the tower bridge. Interstate 41 comes up the Fox Valley from Appleton and Oshkosh. Highway 29 runs west to Wausau, and Highway 172 ties the two interstates together on the south side.',
  'This page covers the interstates and the bridges, the two sides of the river, and the stadium district. It also covers the mills and the trucking yards, the hospitals, Door County, the winter, and the lanes.'],
 'Green Bay at a glance',
 ['Most pickups happen within 1 to 3 days. The trucking yards on the west side put more carriers here than the city’s size suggests.',
  'Milwaukee, Appleton, and Madison are same-day lanes. Chicago is the same day too. Minneapolis, Detroit, and Indianapolis take a day. Florida runs three to four.'],
 'Tell us which side of the river. The Astor and Broadway blocks need a meeting spot. Ashwaubenon, Howard, and the suburbs usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 43, 41, Highway 29, 172, and the Bridges',
 prose(
  L('Green Bay sits where the lakeshore interstate and the Fox Valley interstate meet at the bay.'),
  P('Interstate 43 runs up the lake from Milwaukee and Sheboygan. It crosses the Fox River on the tower bridge north of downtown. It ends at Interstate 41 in Howard on the northwest side. Interstate 41 runs south through Ashwaubenon and De Pere to Appleton, Oshkosh, and Milwaukee. Highway 172 is the south beltway, from 41 by the airport across the river to 43.'),
  P('Highway 29 runs west to Wausau and the Twin Cities. Highway 57 and 42 run up the peninsula into Door County. US 141 runs north to Marinette and the Upper Peninsula. Mason Street, Walnut Street, and Main Street carry the bridges across the river downtown.'),
  P('The carriers come off 41 at Lombardi Avenue, Oneida Street, and Highway 172. The stadium lots and the retail strip on Oneida Street are the usual meeting spots. No road in the metro charges a toll.'),
  P('Our office sits on North Broadway, in the Broadway District on the west bank of the river.'),
 ), alt=True))

BODY.append(sec('The Two Sides','Astor, Broadway, Ashwaubenon, De Pere, and the Grids',
 prose(
  L('The Fox River splits Green Bay into an east side and a west side. The meeting spot follows the side.'),
  P('The east side holds downtown, the Astor neighborhood, and the older blocks toward the bay. Astor’s streets are narrow, lined with mature trees, and parked on both sides. The driver meets you on Monroe Avenue or at a lot by the river.'),
  P('The west side holds the Broadway District, the rail yards, the mills, and the trucking terminals. The blocks behind Broadway are tight, and a main road is the usual spot. Howard and Suamico to the north are open grids where the truck reaches the curb.'),
  P('Ashwaubenon wraps the stadium with wide retail streets and the biggest lots in the county. De Pere sits upriver with a college on the west bank and old streets on both. Allouez and Bellevue are postwar grids where the curb works on most streets.'),
  P('The Oneida reservation runs west of the city past the casino and the airport. Send the full address, since many of the roads there are not on a carrier’s map.'),
 )))

ROUTES=[("Appleton, WI","I-41 · ~30 mi","Same day","$120–$200"),("Milwaukee, WI","I-43 · ~115 mi","Same day","$170–$270"),
 ("Madison, WI","I-41/US-151 · ~140 mi","Same day","$180–$290"),("Chicago, IL","I-43/I-94 · ~210 mi","Same day","$230–$350"),
 ("Minneapolis, MN","WIS-29/I-94 · ~280 mi","1 day","$270–$400"),("Indianapolis, IN","I-94/I-65 · ~390 mi","1 day","$340–$490"),
 ("Detroit, MI","I-94 · ~500 mi","1–2 days","$400–$570"),("St. Louis, MO","I-94/I-55 · ~490 mi","1–2 days","$400–$570"),
 ("Dallas, TX","I-39/I-44 · ~1,130 mi","3 days","$780–$1,080"),("Orlando, FL","I-65/I-75 · ~1,420 mi","3–4 days","$900–$1,260")]
BODY.append(rate_table('Lanes &amp; Costs','Green Bay Car Shipping Lanes and Estimated Costs',
 'Green Bay’s most-booked lanes, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a running sedan on an open trailer. Figure 10 to 25 percent more for an SUV or pickup, and more for enclosed. The snow, the game schedule, and the carriers free on your dates settle the final price.',
 prose(
  P('Green Bay prices a little above Milwaukee on most lanes. The carriers come up 43 or 41 to reach it, and the trucking yards fill the gap. Appleton and Milwaukee ride 41 and 43, and Minneapolis rides 29 and 94.'),
  P('The Florida and Arizona lanes fill each October when the peninsula and the lake towns empty out. The <a href="car-shipping-cost.html">cost guide</a> walks through the rest of the number.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Mills, the Trucking Yards, the Hospitals, and the Packers',
 prose(
  L('Green Bay relocates people on the paper calendar, the trucking calendar, the hospital calendar, and the football calendar.'),
  P('The paper mills along the river and the tissue plants relocate engineers and managers on program schedules. The trucking company headquartered on the southwest side moves drivers, dispatchers, and office staff in from every state. The bank headquartered downtown relocates staff on start dates. The insurer’s campus in De Pere does the same.'),
  P('The hospitals bring in nurses and residents every summer, and most arrive with a car. The handoff happens on Webster Avenue or at a lot off 43 rather than in a hospital ramp.'),
  P('The football club relocates players, coaches, and staff on the league calendar. Cars come in for training camp in July and leave after the season. The stadium district employers hire on the same schedule.'),
  P('The university on the bay and the college in De Pere fill each August and empty each May. The campus lots work for the handoff, and an adult signs for a student car.'),
  P('Fort McCoy sits about three hours west, and the Guard units here rotate on a smaller scale. The <a href="military-car-shipping.html">military</a> page covers a PCS move. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side of any relocation. If your employer reimburses the shipment, the paperwork comes from us.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Game Days, Training Camp, the Snow, and the Bay',
 prose(
  L('Green Bay closes around the stadium on game days and digs out the rest of the winter.'),
  P('Home games fill Lombardi Avenue, Oneida Street, and Ridge Road from Saturday afternoon through Sunday night. Training camp in late July and the preseason scrimmage fill them on weekdays too. We schedule stadium-area pickups on other days, and the rest of the city runs normally.'),
  P('Winter is long and the bay freezes. Green Bay gets about fifty inches of snow a year. Squalls off the bay add to it on a north wind. Blizzards shut 41 and 43 for a day a few times each winter. The carriers wait for the plows, and a winter pickup can slide a day or two.'),
  P('Spring floods the East River and the low streets along the Fox a few times a decade. Summer brings thunderstorms and a short, loud festival season on the Broadway District. The driver meets you off Broadway on festival nights.'),
  P('Door County fills from June through October, and the one road up the peninsula crawls on summer weekends. A peninsula pickup happens on Highway 42 or 57 or in Sturgeon Bay. It takes 2 to 4 days.'),
 )+chips(["Downtown","Astor","Broadway District","Olde Main Street","Navarino","Preble","Allouez","Ashwaubenon","De Pere","Howard","Suamico","Bellevue","Hobart","Oneida","Lombardi Avenue","Oneida Street","Webster Avenue","Titletown","Sturgeon Bay","Door County","Appleton","Manitowoc"])
 +NOTE('Serving both sides of the Fox and the whole bay. Tell us the side, the week, and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Green Bay?',
 prose(
  L('Open is the default out of Green Bay, and the 41 and 43 lanes are quoted that way.'),
  P('An enclosed trailer keeps the salt, the slush, and the eyes off the car. The garages in Allouez and De Pere book enclosed trailers. The cars headed to Arizona for the winter often do too.'),
  P('A daily driver rides open and arrives the way it left. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain the cost and the cover.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff by the stadium or the interstate, and a delivery. The game schedule picks the day.'),
  P('Approve the price, and a carrier already on 41 or 43 gets the job. The spot is set the same day. The driver inspects the car with you and records it on a Bill of Lading. You both sign. Delivery is checked against that record.'),
 )+ULI([
  "Take everything personal out of the car",
  "Leave about a quarter tank in it",
  "Photograph the car before pickup, especially in salt season",
  "Give the driver a working key and flag any mechanical issue",
  "Disable any aftermarket alarm",
  "On a game weekend, plan to meet the truck away from the stadium district",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages fill in the rest, step by step.'))))

BODY.append(sec('Why Ship Guy','Why Green Bay Drivers Choose Ship Guy',
 prose(
  L('We work 41 and 43 every week and plan around the games, the bay, and the snow.'),
  P('Ship Guy holds active FMCSA brokerage authority, and a $75,000 surety bond stands behind it. Both are on the federal register. Our office is on North Broadway downtown.'),
  P('One coordinator carries the booking from the quote to the signature at delivery. Open, enclosed, and expedited transport are all available, and the <a href="services.html">services</a> page lists each one.'),
 ), alt=True))

BODY.append(office('Green Bay','340 N Broadway #522','Green Bay, WI 54303','+19209812245','(920) 981-2245','CT',
 '340+N+Broadway+%23522,+Green+Bay,+WI+54303','Visit Us','Find Ship Guy in Green Bay',
 'Our office is on North Broadway in the Broadway District, on the west bank of the Fox River.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3511.477781685769!2d-88.01879629999999!3d44.520448099999996!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8802fb6cf18ae77b%3A0xfbba999a6a547ce3!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792076659605!5m2!1sen!2sus'))

FAQ=[
 ("Will a Packers home game affect my pickup?","Near the stadium, yes. Lombardi Avenue, Oneida Street, and Ridge Road fill from Saturday afternoon through Sunday night. We schedule a stadium-area pickup on another day. The east side, De Pere, and Howard run normally on game days."),
 ("How much does it cost to ship a car from Green Bay to Milwaukee or Chicago?","Milwaukee runs one hundred seventy to two hundred seventy dollars for a sedan. That is about one hundred fifteen miles down 43. Chicago runs two hundred thirty to three hundred fifty, about two hundred ten miles. Both lanes leave daily. SUVs and pickups add 10 to 25 percent."),
 ("Can you ship a car for a UW–Green Bay or St. Norbert student?","Yes. The cars arrive each August and leave each May. The campus lots on the bay and in De Pere work for the handoff. An adult signs here, and a parent can sign at delivery."),
 ("Do you ship cars for drivers hired at the trucking company?","Yes, all year. New drivers and office staff arrive from every state, and many ship a personal car behind the move. The yards on the southwest side allow a handoff in the lot. We plan the pickup around orientation."),
 ("What happens if a blizzard or a squall off the bay hits on my pickup day?","The driver waits for 41 and 43 to reopen behind the plows. A winter pickup can slide a day or two. We call the moment the forecast changes the plan, and the handoff moves to a cleared lot."),
 ("Can you deliver to Door County or Sturgeon Bay?","Yes, with a meeting spot and some patience in summer. One main road serves the peninsula, and it crawls from June through October. The handoff happens on Highway 42 or 57 or in Sturgeon Bay, and a weekday morning is best."),
 ("Can the carrier come into Astor or the blocks behind Broadway?","Usually not. The streets are narrow, the trees are low, and the cars are parked on both sides. The driver meets you on Monroe Avenue, on Broadway itself, or at a lot by the river. Ashwaubenon, Howard, and Bellevue usually allow the curb."),
 ("Do you handle relocations to the mills or the hospitals?","Yes. The mills relocate engineers on program schedules, and the hospitals bring in nurses and residents every summer. We plan the pickup around the report date. When an employer reimburses the shipment, we send the paperwork it wants."),
 ("Can you ship a car that does not run from Green Bay?","Yes. A winch truck is assigned, and the slower loading is figured into the quote. Choose a flat, open spot, which usually means a lot off 41. Let us know whether it rolls, steers, and brakes."),
 ("What do you need for a Green Bay car shipping quote?","The pickup and delivery addresses, with the side of the river on this end. The year, make, and model. Whether it runs. Open or enclosed. Your dates, with the game schedule in mind. That is a complete Green Bay request."),
]
BODY.append(faq_section(FAQ,'Green Bay FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Green Bay?','Two minutes on the form above gets you a price. Tell us the side of the river and your dates. A carrier already coming up 41 takes it from there.','+19209812245','(920) 981-2245','Get your free Green Bay quote'))

build({
 'slug':'auto-transport-green-bay-wisconsin',
 'title':'Car Shipping in Green Bay, WI — Auto Transport | Ship Guy',
 'meta':'Car shipping in Green Bay, WI at the top of Interstate 43 and 41. Packers game-day timing, east side and west side handoffs, trucking and paper mill relocations, hospital moves, Door County deliveries, blizzard and bay-squall planning. Local office on North Broadway. Free quote.',
 'h1':'Car Shipping in<br>Green Bay, <span class="accent">Wisconsin</span>',
 'lede':'Open, enclosed, and expedited auto transport across Brown County and the bay, planned around the river, the games, and the snow.',
 'tel':'+19209812245','disp':'(920) 981-2245','brand':'Green Bay','keyword':'car shipping in green bay',
 'localterms':['green bay','interstate 43','interstate 41','highway 29','highway 172','highway 57','highway 42','us 141','tower bridge','fox river','mason street','walnut street','main street','lombardi avenue','oneida street','ridge road','webster avenue','monroe avenue','broadway','astor','downtown','ashwaubenon','de pere','allouez','howard','suamico','bellevue','hobart','oneida','stadium','packers','training camp','titletown','paper mills','tissue','trucking','bank','insurer','hospitals','residents','university','college','fort mccoy','guard','door county','sturgeon bay','peninsula','bay','squalls','blizzards','plows','east river','festival','appleton','oshkosh','sheboygan','manitowoc','milwaukee','madison','chicago','minneapolis','indianapolis','detroit','st. louis','dallas','orlando','florida','arizona'],
}, BODY, FAQ)
