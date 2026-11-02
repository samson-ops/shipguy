import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Newport News, Virginia','Car shipping on the Peninsula, between the shipyard that builds the carriers and the Army post at the far end',
 ['Car shipping in Newport News runs the length of Interstate 64 down the Peninsula to 664. Ship Guy is a licensed auto transport broker with an office on Thimble Shoals Boulevard in Oyster Point.',
  'We book vetted carriers across Newport News, from the Southeast Community to Denbigh and out to Lee Hall. The carriers own the trucks. Ship Guy holds the license and the bond.',
  'Interstate 64 runs the length of the city from Lee Hall to the Hampton line. Interstate 664 leaves it in Hampton and crosses the harbor on the Monitor-Merrimac bridge-tunnel. Jefferson Avenue and Warwick Boulevard run parallel the whole way. J. Clyde Morris Boulevard is Route 17, and the James River Bridge carries 17 south.',
  'This page covers 64, 664, Jefferson, Warwick, the two bridges, downtown, Hilton Village, Oyster Point, and Denbigh. It also covers the shipyard, Fort Eustis, the hospital, the university, the tunnels, and the hurricanes.'],
 'Newport News at a glance',
 ['Most pickups happen within 1 to 3 days. The Richmond carriers come down 64 daily, and the Southside pool is across the harbor. The 95 trucks turn east at Petersburg.',
  'Richmond, Washington, Raleigh, and Baltimore ride a single day on the truck. Philadelphia and Charlotte take a day. New York takes one, Atlanta takes one to two, and Florida takes two.'],
 'Tell us the neighborhood and the post, if there is one. The Southeast Community, Hilton Village, and the old North End meet the truck on a main road. Denbigh, Kiln Creek, Oyster Point, and the subdivisions off Warwick usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 64, Interstate 664, Jefferson Avenue, Warwick Boulevard, Route 17, the James River Bridge, and the Tunnels',
 prose(
  L('Newport News is twenty-five miles long and three miles wide, and every road runs the long way. A carrier picks its exit by the mile marker.'),
  P('Interstate 64 is the spine. It comes down from Richmond and Williamsburg past Fort Eustis and runs the whole city to Hampton. The Fort Eustis, Jefferson Avenue, Victory Boulevard, and J. Clyde Morris exits serve the north and the middle. Beyond Hampton it dives under the harbor in the Hampton Roads bridge-tunnel, the busiest crossing in the state. A trailer that cannot clear it uses 664. Interstate 664 leaves 64 in Hampton and runs through the bottom of the city. It crosses on the Monitor-Merrimac bridge-tunnel to Suffolk. It carries no toll.'),
  P('Jefferson Avenue is the commercial strip from the shipyard to Fort Eustis, twenty miles of it. Warwick Boulevard is Route 60, a mile west, through Hilton Village and the old neighborhoods. J. Clyde Morris Boulevard is Route 17 across the middle. It runs from the James River Bridge to the Coleman Bridge and Gloucester. The James River Bridge carries 17 south to Smithfield. The state closes it to high trailers in a strong wind. Oyster Point Road and Denbigh Boulevard cross between the two long roads.'),
  P('The carriers come off 64 at J. Clyde Morris or Jefferson Avenue. The big-box lots on Jefferson at Oyster Point are the usual meeting spot. The mall lots farther up Jefferson work too. So do the shopping center lots in Denbigh and the lots on Warwick outside the villages. The airport cell lot off Jefferson works for a fly-and-ship.'),
  P('Our office is on Thimble Shoals Boulevard in Oyster Point, off J. Clyde Morris Boulevard and 64.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the Southeast Community, the East End, the North End, Hilton Village, Riverside, Hidenwood, Oyster Point, Port Warwick, Denbigh, Kiln Creek, and Lee Hall',
 prose(
  L('Newport News is a shipyard town at the bottom and a planned village in the middle. The subdivisions run all the way north. The truck meets the old blocks on a main road.'),
  P('Downtown and the Southeast Community sit at the bottom of the Peninsula beside the shipyard gates. The streets are a tight grid of row houses and the cranes above them. The driver meets you on Jefferson Avenue or at the lots on 35th Street. The East End between Jefferson and the shipyard is the same grid. The North End above it is old houses on short blocks, and some allow the curb.'),
  P('Hilton Village on Warwick is the planned village from the first war, brick cottages on narrow lanes. A trailer does not enter, and the handoff happens on Warwick. Riverside around the hospital and Hidenwood around the university are wooded streets from the fifties. The curb works where the trees allow it. Port Warwick is the new town center off Jefferson, apartments and townhouses on one-way streets. The handoff moves to Jefferson.'),
  P('Oyster Point is the office park and the city center in the middle of the Peninsula. Its lots are the meeting spot for half the city. Denbigh north of it is the largest neighborhood, wide postwar grids and subdivisions off Denbigh Boulevard and Warwick. The truck reaches the curb on most blocks. Kiln Creek at the York County line is a golf community of cul-de-sacs. The handoff happens at the entrance. Lee Hall at the top is the post’s town, and the gates are the handoff there too.'),
  P('Hampton next door ships with the same trucks and prices the same as Newport News. So do Yorktown, Poquoson, and Williamsburg up 64. Norfolk and Virginia Beach across the harbor add the tunnel and nothing else. Smithfield adds the James River Bridge.'),
 )))

ROUTES=[("Richmond, VA","I-64 · ~70 mi","Same day","$150–$240"),("Washington, DC","I-64/I-95 · ~175 mi","Same day","$220–$340"),
 ("Raleigh, NC","US-58/I-95 · ~190 mi","Same day","$230–$350"),("Baltimore, MD","I-64/I-95 · ~215 mi","Same day","$240–$360"),
 ("Philadelphia, PA","I-64/I-95 · ~260 mi","1 day","$260–$390"),("Charlotte, NC","US-58/I-85 · ~310 mi","1 day","$300–$440"),
 ("New York, NY","I-95 · ~350 mi","1 day","$340–$490"),("Atlanta, GA","I-85 · ~560 mi","1–2 days","$440–$630"),
 ("Jacksonville, FL","I-95 · ~600 mi","2 days","$450–$650"),("Orlando, FL","I-95 · ~750 mi","2 days","$520–$750")]
BODY.append(rate_table('Lanes &amp; Costs','Newport News Car Shipping Lanes and Estimated Costs',
 'The lanes Peninsula cars run most, with estimated open-trailer ranges. Price your own route on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Newport News for a running sedan on an open trailer. SUVs and pickups run 10 to 25 percent more, and enclosed runs more again. The week and the carriers free on 64 that week decide the final figure.',
 prose(
  P('Newport News prices a shade under Norfolk on the northern lanes, because the truck skips the tunnel. The Richmond lane rides 64 and fills every day. The Carolina lanes ride 664 and 58 to 95 and 85. The Florida lane rides 95 and fills each fall with the retirees and the soldiers on orders. The New York lane rides 95 north through Washington.'),
  P('A report date at the post in July or the August move-in lands in the busiest weeks. The <a href="car-shipping-cost.html">cost guide</a> explains what size, condition, and timing do to the figure.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Shipyard, the Army Post, the Air Base, the Accelerator Lab, the Hospital, the University, the Terminal, and the Retirees',
 prose(
  L('Newport News relocates shipbuilders, soldiers, airmen, physicists, nurses, and students. The shipyard and the post move more households than everyone else combined.'),
  P('The shipyard at the bottom of the Peninsula builds the Navy’s carriers and submarines. It is the largest industrial employer in the state. It brings engineers on program schedules and apprentices every fall. The handoff for all of them happens on Jefferson Avenue. The gates and the grid leave no room. If the yard or an employer reimburses the shipment, the paperwork comes from us.'),
  P('Fort Eustis at the north end is the Army’s transportation school and an aviation post. Soldiers and families rotate on orders all year, with the summer peak. Langley across the Hampton line rotates airmen the same way. Housing is gated, so the handoff happens outside the gate or in Denbigh. Orders pay for one car, and families ship the second one with us. Ship Guy is a private broker with no tie to either post. The <a href="military-car-shipping.html">military</a> page explains how orders set the timing.'),
  P('The accelerator lab in Oyster Point brings physicists on grant cycles. The hospital on J. Clyde Morris brings residents each June and hires traveling nurses year round. The university on Warwick takes student cars in late August and sends them home in May. A parent sets it up, and someone over eighteen signs at the lot. The marine terminal on the river receives imported cars that clear customs before they move. Send the release date and the terminal.'),
  P('Retirees from the yard and the post stay for the water, and many leave for Florida each October. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the paperwork for crossing a state line.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Christenings, the PCS Season, Move-In Week, the Williamsburg Traffic, the Nor’easters, the Hurricanes, the Snow, and the Wind',
 prose(
  L('Newport News runs on a Navy calendar and an Army calendar. The weather problem is water on two sides and a harbor between the city and everywhere else.'),
  P('A christening at the shipyard closes Washington Avenue and fills the bottom of the city for a day. The PCS season at the post runs June through August and fills the carriers with second cars. Move-in week in late August fills Hidenwood. The Williamsburg traffic fills 64 every summer Friday, and the tunnel backs up behind it. The Fourth fills the waterfront at Victory Landing. Book three weeks ahead for a July date.'),
  P('The storms run June through November. Isabel in 2003 is still the benchmark. It put the river into the low streets at the bottom of the city and closed the bridges. Matthew in 2016 dropped a foot of rain in a night. An evacuation order shuts the tunnels, and the carriers sit in Richmond until it lifts. We call you when the watch posts, and the pickup waits for the all-clear.'),
  P('A nor’easter in the fall pushes the river into the low streets at the bottom of the city. Snow comes once every few years and shuts everything. The January 2018 storm dropped a foot and slowed the tunnels for two days. The carriers waited in Richmond until the Peninsula thawed. A strong wind closes the James River Bridge to high trailers. A Smithfield handoff moves to the next day.'),
  P('Summer brings heat and afternoon storms that shift the loading hour. The tunnel backups on a July weekend shift the whole day, and a Peninsula handoff avoids them.'),
 )+chips(["Downtown","Washington Avenue","The Southeast Community","The East End","The North End","Huntington Heights","Hilton Village","Riverside","Hidenwood","Oyster Point","City Center","Port Warwick","Jefferson Avenue","Warwick Boulevard","Denbigh","Kiln Creek","Menchville","Lucas Creek","Lee Hall","Fort Eustis","Hampton","Langley","Yorktown","Tabb","Poquoson","Williamsburg","Smithfield","Gloucester","Norfolk"])
 +NOTE('Serving Newport News and the whole Peninsula, Hilton Village lane or Denbigh cul-de-sac. Tell us the neighborhood and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Newport News?',
 prose(
  L('Open trailers carry most of the Peninsula, and the table above is priced for one.'),
  P('Enclosed keeps the salt air, the pollen, and the pre-snow brine off the paint. Hilton Village collectors book it, and so do officers bringing a car home from a tour. If a hurricane is coming, the car takes the first truck with a slot. We say that up front.'),
  P('Open is right for a commuter car or a student’s car. See how the two stack up on the <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('You get a figure first, then a lot in Oyster Point, then a signature when the car lands. Orders or the program start pick the week.'),
  P('Say yes to the figure, and the car goes to a carrier already headed down 64 that week. The lot and the two-hour window get settled that same afternoon. The driver photographs each panel at pickup and marks the Bill of Lading. Your initials on it make it the record both ends work from.'),
 )+ULI([
  "Cabin and trunk emptied of personal items",
  "Fuel at a quarter tank or less",
  "Each side and the odometer photographed before pickup",
  "A good key and a list of known faults",
  "Add-on alarms switched off",
  "In the Southeast Community, Hilton Village, or behind a gate, we meet on a main road",
 ])+prose(P('For the step-by-step, read <a href="how-it-works.html">how it works</a>, and for the day-of list, read <a href="car-shipping-preparation.html">preparation</a>.'))))

BODY.append(sec('Why Ship Guy','Why Newport News Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already come down 64 every day. We know which crossing a loaded trailer can take and which one it cannot.'),
  P('Our FMCSA license and our $75,000 bond are a public record on the federal register. The office is on Thimble Shoals Boulevard in Oyster Point.'),
  P('You deal with one coordinator from the quote to the delivery call. Open, enclosed, and expedited are laid out on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Newport News','733 Thimble Shoals Blvd #425a','Newport News, VA 23606','+17577979348','(757) 797-9348','ET',
 '733+Thimble+Shoals+Blvd+%23425a,+Newport+News,+VA+23606','Visit Us','Find Ship Guy in Newport News',
 'Our office is on Thimble Shoals Boulevard in Oyster Point, off J. Clyde Morris Boulevard and 64.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3928.861526442025!2d-76.46706379999999!3d37.08428010000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89b0792f6808f259%3A0x24b10f7aeaf662b7!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793629109589!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Newport News to Florida or New York?","Orlando runs five hundred twenty to seven hundred fifty dollars for a sedan. That is about seven hundred fifty miles down 95. New York runs three hundred forty to four hundred ninety, about three hundred fifty miles north. Richmond, an hour up 64, is the lowest lane on the table. Add 10 to 25 percent for an SUV or a pickup."),
 ("Do you ship cars for soldiers on orders to Fort Eustis or airmen at Langley?","Yes, in every season. Orders cover one car, and the second one usually comes to us. On-post housing is gated, so the driver meets you outside the gate or at the Denbigh lots. July is the peak, so give a July date three weeks. Ship Guy is a private broker with no connection to either post."),
 ("Do you ship cars for shipyard employees?","Yes. The yard brings engineers on program schedules and apprentices every fall. The handoff happens on Jefferson Avenue outside the gates. If the yard reimburses the shipment, we produce the paperwork it wants. A christening day moves the handoff up the Peninsula to Oyster Point."),
 ("Can the carrier come to my street in Hilton Village or the Southeast Community?","No. Hilton Village is brick cottages on narrow lanes. The Southeast Community is a tight grid beside the shipyard. The driver meets you on Warwick or Jefferson. Denbigh, Oyster Point, Riverside, and the subdivisions off Warwick usually allow the curb."),
 ("Which crossing does the carrier use to reach the Southside?","Whichever one the trailer clears. The Hampton Roads bridge-tunnel on 64 is the busiest crossing in the state. A tall trailer takes the Monitor-Merrimac on 664 instead. Neither carries a toll. The James River Bridge carries 17 to Smithfield and closes to high trailers in a strong wind."),
 ("Can you deliver on a Christopher Newport move-in date?","Yes. Cars reach the campus on Warwick in late August and leave in May. Mom or Dad books, and an adult signs at the lot. Hidenwood is full that week, so the lots on Warwick take the handoff. The date sets the window."),
 ("Can you ship a car to or from Hampton, Williamsburg, or Smithfield?","Yes. Hampton, Yorktown, and Poquoson ride the same carriers and price the same as Newport News. Williamsburg is twenty-five miles up 64 and prices with the city. Smithfield adds the James River Bridge, and a windy day moves it to the next morning."),
 ("What happens if a hurricane or a nor’easter hits on my pickup day?","Under a hurricane watch the truck stays in Richmond, and an evacuation order shuts the tunnels. A nor’easter floods the low streets at the bottom of the city for a day. We call when the watch posts. Once the roads reopen, the pickup takes the first clear day, and the figure holds."),
 ("Can you ship a car that does not run from Newport News?","Yes. A winch truck handles it, and the loading time is in the figure from the start. The big-box lots on Jefferson at Oyster Point are flat. We need to know if it rolls, steers, and brakes."),
 ("What do you need for a Newport News car shipping quote?","Where it starts and where it ends, down to the neighborhood and the post. What it is and whether it runs. Open or enclosed, and the week you have in mind. Those five lines get you a Newport News figure the same day."),
]
BODY.append(faq_section(FAQ,'Newport News FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Newport News?','Two minutes on the form above gets your lane a Newport News figure. Name the neighborhood and the week, and a carrier already coming down 64 takes it.','+17577979348','(757) 797-9348','Get your free Newport News quote'))

build({
 'slug':'auto-transport-newport-news-virginia',
 'title':'Car Shipping in Newport News, VA — Auto Transport | Ship Guy',
 'meta':'Car shipping in Newport News, VA, on the Peninsula between the shipyard and Fort Eustis. Army and Air Force PCS moves outside the gates, shipyard relocations on Jefferson Avenue, the two bridge-tunnels, main-road handoffs for Hilton Village and the Southeast Community, curbside pickups in Denbigh and Oyster Point, and the hurricanes. Local office in Oyster Point. Free quote.',
 'h1':'Car Shipping in<br>Newport News, <span class="accent">Virginia</span>',
 'lede':'Open, enclosed, and expedited auto transport across Newport News and the Peninsula, planned around 64, 664, the shipyard, the post, the tunnels, and hurricane season.',
 'tel':'+17577979348','disp':'(757) 797-9348','brand':'Newport News','keyword':'car shipping in newport news',
 'localterms':['newport news','peninsula','shipyard','carriers','army post','interstate 64','664','jefferson avenue','warwick boulevard','route 17','james river bridge','tunnels','thimble shoals','oyster point','downtown','southeast community','east end','north end','hilton village','riverside','hidenwood','port warwick','denbigh','kiln creek','lee hall','fort eustis','langley','hampton','yorktown','poquoson','williamsburg','smithfield','gloucester','norfolk','virginia beach','richmond','petersburg','washington','raleigh','baltimore','philadelphia','charlotte','new york','atlanta','jacksonville','orlando','florida','monitor-merrimac','hampton roads','coleman bridge','j. clyde morris','victory boulevard','denbigh boulevard','35th street','mall','airport','cell lot','fly-and-ship','row houses','cranes','planned village','first war','brick cottages','office park','city center','golf community','gates','shipbuilders','soldiers','airmen','physicists','nurses','students','submarines','largest industrial employer','program schedules','apprentices','transportation school','aviation','orders','accelerator lab','grant cycles','hospital','residents','traveling nurses','university','marine terminal','customs','release date','retirees','christening','washington avenue','pcs season','move-in','victory landing','isabel','2003','matthew','2016','evacuation','january 2018','wind','salt air','pollen','brine','bill of lading','fmcsa','winch','mile marker','huntington heights','menchville','lucas creek','tabb'],
}, BODY, FAQ)
