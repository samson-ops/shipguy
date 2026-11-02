import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("3–6 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Casper, Wyoming','Car shipping in the middle of Wyoming, where Interstate 25 brings the trucks up from Denver and the oil field and the wind set the calendar',
 ['Car shipping in Casper runs on Interstate 25, the one freeway through the middle of the state. Ship Guy is a licensed auto transport broker with an office on South Center Street downtown.',
  'We book vetted carriers across Casper, from the Old Yellowstone District to Paradise Valley and Bar Nunn. The carriers own and run the trucks. Ship Guy holds the license and the bond and does the booking.',
  'Interstate 25 runs along the east and north edges of the city between Cheyenne and Buffalo. Highway 20 and 26 run west past the airport to Shoshoni and Riverton. Highway 220 runs southwest to Alcova and Rawlins. Wyoming Boulevard loops the city, and the mountain road climbs south to the ski hill.',
  'This page covers 25, the Yellowstone Highway, 220, Wyoming Boulevard, downtown, the east side, and the river. It also covers the oil field, the hospital, the college, the rodeos, the wind, and the window.'],
 'Casper at a glance',
 ['Plan on 3 to 6 days for a pickup. Casper sits a hundred eighty miles north of the Interstate 80 lane. The carriers come up 25 from Denver and Cheyenne when a load justifies the stop. The Billings trucks come down the same road.',
  'Cheyenne, Fort Collins, and Denver are a day on the truck. Billings, Rapid City, and Salt Lake City take one to two. Omaha and Kansas City take two to three, and Dallas and Phoenix take three to four.'],
 'Tell us the part of town. Downtown, the mountain road, the river bottoms, and the county subdivisions meet the truck on a main road. The east side grids, Paradise Valley, Mills, Evansville, and Bar Nunn usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 25, the Yellowstone Highway, Highway 220, Wyoming Boulevard, Center Street, CY Avenue, 2nd Street, and the Mountain Road',
 prose(
  L('Casper is a grid on the North Platte with the interstate wrapped around two sides of it. A carrier comes off 25 and stays on the wide streets.'),
  P('Interstate 25 comes up from Cheyenne and Douglas along the east side of the city. It bends west along the river and leaves north for Buffalo and Billings. The Center Street exit drops into downtown, and the Poplar exit serves the west side. The Wyoming Boulevard and Hat Six exits serve the east. Highway 20 and 26 leave west as the Yellowstone Highway past Mills and the airport to Shoshoni. Highway 220 leaves southwest as CY Avenue to Alcova, Independence Rock, and Rawlins. Highway 259 runs north to Midwest and the Salt Creek field.'),
  P('Wyoming Boulevard is the loop around the south and east sides. It carries the trucks around the grid. Center Street is the downtown spine from the river south to the base of the mountain. 2nd Street is the long east-west strip with the mall, the big-box lots, and the car dealers. 12th Street and 13th Street cross the south side. Casper Mountain Road climbs from the end of Wolcott Street to the top in eight miles. A trailer does not use it.'),
  P('The carriers come off 25 at Center Street or Wyoming Boulevard. They meet at the mall lots on 2nd Street or the big-box lots on Wyoming Boulevard. The lots at the events center work outside a rodeo or a concert. So do the lots on the Yellowstone Highway in Mills and the truck stops at Hat Six. The airport is ten miles west on 20 and 26 for a fly-and-ship.'),
  P('Our office is on South Center Street downtown, a few blocks south of 2nd Street.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the Old Yellowstone District, North Casper, the East Side, Paradise Valley, the South Side, the Mountain, Mills, Evansville, and Bar Nunn',
 prose(
  L('Casper is an old downtown, wide grids on both banks, and subdivisions climbing toward the mountain. The truck reaches the curb on most of it.'),
  P('Downtown is a dozen blocks of brick between the river and the tracks, angled parking and one-way pairs. The driver meets you on Center Street or at the events center lots. The Old Yellowstone District west of downtown is warehouses turned shops and apartments. The handoff happens on Yellowstone Highway. North Casper across the river is a working grid of small houses. The curb works on most of it.'),
  P('The east side from Wyoming Boulevard to the mall is postwar grids and newer subdivisions with wide streets. The truck reaches the curb. Paradise Valley on the west side is the same. The south side climbs toward the mountain on wider lots. The curb works until the streets turn to gravel. The Mountain itself is cabins on dirt roads with no turnaround. The handoff happens at the base lots.'),
  P('Mills and Evansville are separate towns at the two ends of the city. Both allow the curb on most streets. Bar Nunn north of the airport is a subdivision laid out on an old airfield. The truck comes to the house. The county subdivisions off the paved roads meet the truck on the highway.'),
  P('Mills, Evansville, and Bar Nunn ship with the same trucks and price the same as Casper. Glenrock and Douglas down 25 do too. Riverton and Lander add a figure and a day, because the truck leaves the interstate for them.'),
 )))

ROUTES=[("Cheyenne, WY","I-25 · ~180 mi","1 day","$230–$350"),("Fort Collins, CO","I-25 · ~225 mi","1 day","$250–$380"),
 ("Denver, CO","I-25 · ~280 mi","1 day","$300–$440"),("Billings, MT","I-25/I-90 · ~300 mi","1–2 days","$300–$440"),
 ("Rapid City, SD","I-25/I-90 · ~360 mi","1–2 days","$340–$490"),("Salt Lake City, UT","WY-220/I-80 · ~390 mi","1–2 days","$450–$650"),
 ("Omaha, NE","I-25/I-80 · ~680 mi","2–3 days","$520–$750"),("Kansas City, MO","I-25/I-80/I-29 · ~820 mi","3 days","$560–$800"),
 ("Dallas, TX","I-25/US-287 · ~1,000 mi","3–4 days","$720–$1,000"),("Phoenix, AZ","I-25/I-40/I-17 · ~1,150 mi","4 days","$800–$1,150")]
BODY.append(rate_table('Lanes &amp; Costs','Casper Car Shipping Lanes and Estimated Costs',
 'The lanes Natrona County cars travel most, with open-trailer estimates. Your own route prices on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Casper for a sedan that runs, open trailer. SUVs and pickups add 10 to 25 percent, and enclosed adds more on top. The week and the carriers on 25 that week decide the real figure.',
 prose(
  P('Casper prices above Cheyenne on every lane. Every truck comes a hundred eighty miles off the 80 lane to reach it. The Denver lane rides 25 and fills twice a week. The Billings lane rides 25 north and thins in winter. The Salt Lake lane rides 220 to Rawlins and then 80. The Texas lanes fill with the oil-field hiring, and the Arizona lane fills with the retirees each November.'),
  P('A spring start in the oil field or a rodeo week in July means a busy week. How size, condition, and timing push the figure up or down is on the <a href="car-shipping-cost.html">cost guide</a>.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Oil Field, the Hospital, the College, the Guard, the Retirees, and the Ranches',
 prose(
  L('Casper relocates roughnecks, engineers, nurses, students, and retirees. The oil field moves the most, and it moves in cycles.'),
  P('Salt Creek and the Powder River Basin north of the city have boomed and busted for a century. The service companies and the drilling contractors hire in the spring and lay off in a bust. The pickups move with them. The handoff happens at the Yellowstone Highway lots or the truck stops on 25. The refinery that stood on the river is gone. The golf course and the river walk sit on its ground.'),
  P('The hospital on the east side is the largest in the state. It brings residents each June and traveling nurses all year. The handoff happens on 2nd Street or at the mall lots. The college on the south side takes students from across the state in late August. A parent sets it up, and an adult signs at the lots on Wolcott. The Guard units in the city rotate people on orders, and the handoff happens at the armory lots. Ship Guy is a private company with no connection to the Guard. The <a href="military-car-shipping.html">military</a> page explains how a report date sets the window.'),
  P('The ranches ship pickups and stock trailers on their own calendar, and the handoff happens on the highway. Retirees leave for Arizona in November and come back in May. A state line adds paperwork, and the <a href="state-to-state-car-shipping.html">state-to-state</a> page lists it.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The College Rodeo, the Fair, the Beartrap Festival, the Wind, the Blizzards, the 25 Closures, and the Eclipse That Filled the Town',
 prose(
  L('Casper runs on an oil calendar and a rodeo calendar. The weather problem is a wind that never quits and a blizzard that can close 25 in May.'),
  P('The college rodeo finals fill the events center and every motel for a week in June. The county fair and rodeo take the fairgrounds on CY Avenue for a week in July. The Beartrap festival fills the mountain road for a weekend in August. The total eclipse in August 2017 brought a crowd the size of the city, and the roads stopped. Give a June or July date three weeks of notice.'),
  P('The wind blows sixty miles an hour on the 25 grade south of town. It tips trailers on the Bordeaux stretch near Chugwater. The state closes 25 to light and high-profile vehicles when it does. The carriers wait in Douglas or Cheyenne. A blizzard closes 25 between Casper and Cheyenne with gates. The trucks wait a day or two for the plows. The April 2016 blizzard shut the city for two days. The October storms come before the leaves are down.'),
  P('Cold snaps hold the city at twenty below for days. A carrier does not load a car at that temperature, because the straps stiffen and the hydraulics slow. Summer brings hail on the east side a few afternoons a year. A carrier waits out a warning under cover.'),
  P('The river runs high in June when the mountain melts. The low roads along it close some years. The handoff moves to the highway until it drops.'),
 )+chips(["Downtown","The Old Yellowstone District","North Casper","East Casper","Eastridge","Paradise Valley","The South Side","Wolf Creek","The Bench","Casper Mountain","Mills","Evansville","Bar Nunn","Glenrock","Douglas","Midwest","Alcova"])
 +NOTE('Serving Casper, Natrona County, and the middle of Wyoming, Paradise Valley curb or mountain cabin road. Give us the neighborhood and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Casper?',
 prose(
  L('Open trailers carry nearly everything out of Casper, and the table above assumes one.'),
  P('Enclosed keeps the gravel, the hail, and the winter salt off the paint. The collectors on the south side book it. So do the retirees moving a car worth more than the rest of the household. When the only truck coming up 25 that week is open, we say so first. You decide.'),
  P('A commuter car or an oil-field pickup rides open and arrives fine. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages compare the two.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A figure, a lot off 25, and a signature when the car lands. The hiring date or the move picks the week.'),
  P('Say yes, and the car goes to a carrier already headed up 25 that week. The lot and the window are settled that day. The driver photographs the car at pickup and writes its condition on the Bill of Lading. You initial that sheet, and it is the record at delivery.'),
 )+ULI([
  "Personal items out of the cabin and the bed",
  "Fuel at a quarter tank or below",
  "Each side and the odometer photographed the day before",
  "A working key and a note on any known faults",
  "Add-on alarms off",
  "On the mountain, in a county subdivision, or on a ranch road, expect a lot off 25",
 ])+prose(P('The order of events is on the <a href="how-it-works.html">how it works</a> page. The pickup-day list is on the <a href="car-shipping-preparation.html">preparation</a> page.'))))

BODY.append(sec('Why Ship Guy','Why Casper Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already come up 25 each week. We know when the state closes the road to high-profile trailers and when the rodeo takes the motels.'),
  P('Our FMCSA license and our $75,000 bond are on the federal register for anyone to read. The office is on South Center Street downtown.'),
  P('One coordinator handles the move from the first call to the last. Open, enclosed, and expedited are set out on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Casper','444 S Center St #33','Casper, WY 82601','+13046355787','(304) 635-5787','MT',
 '444+S+Center+St+%2333,+Casper,+WY+82601','Visit Us','Find Ship Guy in Casper',
 'Our office is on South Center Street downtown, a few blocks south of 2nd Street.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3610.8880516461177!2d-106.3253922!3d42.8458967!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8760bde60906bb19%3A0xabdc65d467fd60df!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793629022920!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Casper to Denver or Salt Lake City?","Denver runs three hundred to four hundred forty dollars for a sedan. That is about two hundred eighty miles down 25. Salt Lake City runs four hundred fifty to six hundred fifty, about three hundred ninety miles through Rawlins. Cheyenne is the lowest lane on the table, three hours down 25. Figure 10 to 25 percent more for an SUV or a pickup."),
 ("Why does a Casper pickup take 3 to 6 days?","Because the city sits a hundred eighty miles off the 80 lane. The carriers come up 25 from Denver and Cheyenne when a load justifies the stop. The Billings trucks come down the same road. A car waits for the next one with room. A wind closure or a blizzard on 25 stretches the window further. We say so when it does."),
 ("Can the carrier come to my street in Casper?","On most of them, yes. The east side grids, Paradise Valley, North Casper, Mills, Evansville, and Bar Nunn have wide streets. The truck reaches the curb. Downtown and the Old Yellowstone District meet the truck on Center Street or Yellowstone Highway. The mountain and the county subdivisions off the paved road meet it on the highway."),
 ("What happens if the wind or a blizzard closes Interstate 25 on my pickup day?","The truck waits in Douglas or Cheyenne until the state lifts the closure, usually a day. The wind closes 25 to high-profile trailers south of town a few times each winter month. A blizzard closes it with gates. We call the moment the forecast turns. The pickup moves to the first open day at the same figure."),
 ("Do you ship cars for oil-field workers?","Yes, and the lane runs in cycles. The service companies hire in the spring and lay off in a bust. The pickups move with them from Texas, Oklahoma, and North Dakota. The handoff happens at the Yellowstone Highway lots or the truck stops on 25. If the company reimburses the move, we produce whatever paperwork it wants."),
 ("Can you ship a car for a Casper College student?","Yes. Students arrive in late August and leave in May. A parent sets it up, and someone over eighteen signs at the lot. The college sits on the south side with wide streets. The meeting point is the lots on Wolcott or the campus lots. Your date sets the window."),
 ("Can you ship a car to or from Mills, Glenrock, or Riverton?","Yes. Mills, Evansville, and Bar Nunn ride the same carriers and price the same as Casper. Glenrock and Douglas down 25 do too. Riverton and Lander are two hours west on 20 and 26 and add a figure and a day. The truck leaves the interstate for them."),
 ("Can you ship a car during the college rodeo or the fair?","Yes, from a lot. The college rodeo finals fill the events center in June. The fair takes the fairgrounds on CY Avenue in July. The handoff moves to the mall lots on 2nd Street or the truck stops on 25 those weeks. Give a June or July date three weeks of notice."),
 ("Can you ship a car that does not run from Casper?","Yes. A winch truck takes it, and the loading time is in the figure from the start. The mall lots on 2nd Street and the big-box lots on Wyoming Boulevard are flat. Say whether it rolls, steers, and brakes, and we send the right truck."),
 ("What do you need for a Casper car shipping quote?","Both addresses, with the neighborhood or the county road. What it is and whether it runs. Open or enclosed, and the widest week you can give. With those, a Casper figure comes back the same day."),
]
BODY.append(faq_section(FAQ,'Casper FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Casper?','Two minutes on the form above gets your lane a Casper figure. Name the neighborhood and the week, and the next carrier up 25 takes the car.','+13046355787','(304) 635-5787','Get your free Casper quote'))

build({
 'slug':'auto-transport-casper-wyoming',
 'title':'Car Shipping in Casper, WY — Auto Transport | Ship Guy',
 'meta':'Car shipping in Casper, WY, in the middle of the state on Interstate 25. Oil-field hiring cycles, hospital and college dates, curbside pickups on the east side, in Paradise Valley, Mills, Evansville, and Bar Nunn, main-road handoffs downtown and on the mountain, the wind and blizzard closures on 25, and the honest 3 to 6 day window. Local office on South Center Street downtown. Free quote.',
 'h1':'Car Shipping in<br>Casper, <span class="accent">Wyoming</span>',
 'lede':'Open, enclosed, and expedited auto transport across Casper and Natrona County, planned around Interstate 25, the oil-field cycle, the rodeo weeks, the wind, and the blizzards.',
 'tel':'+13046355787','disp':'(304) 635-5787','brand':'Casper','keyword':'car shipping in casper',
 'localterms':['casper','wyoming','interstate 25','yellowstone highway','highway 20','and 26','highway 220','highway 259','wyoming boulevard','center street','cy avenue','2nd street','12th street','wolcott','poplar','hat six','mountain road','casper mountain','ski hill','north platte','river','downtown','old yellowstone district','north casper','east side','eastridge','paradise valley','south side','wolf creek','the bench','mills','evansville','bar nunn','glenrock','douglas','midwest','alcova','riverton','lander','shoshoni','rawlins','independence rock','buffalo','salt creek','powder river basin','oil field','century','service companies','drilling','roughnecks','refinery','golf course','river walk','hospital','largest in the state','residents','traveling nurses','college','students','guard','armory','orders','ranches','stock trailers','retirees','arizona','college rodeo','events center','county fair','fairgrounds','beartrap','eclipse','august 2017','wind','sixty miles an hour','bordeaux','chugwater','high-profile','gates','blizzard','april 2016','two days','twenty below','hail','mall','big-box','truck stops','airport','fly-and-ship','cheyenne','fort collins','denver','billings','rapid city','salt lake','omaha','kansas city','dallas','phoenix','texas','oklahoma','north dakota','gravel','salt','bill of lading','fmcsa','winch'],
}, BODY, FAQ)
