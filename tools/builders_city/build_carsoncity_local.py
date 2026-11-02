import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Carson City, Nevada','Car shipping in the capital, where the Reno carriers reach the city in half an hour and the passes to Tahoe and California set the winter days',
 ['Car shipping in Carson City runs on the 580 freeway and Highway 50, which cross east of downtown. Ship Guy is a licensed auto transport broker with an office on West Proctor Street downtown.',
  'We book vetted carriers across Carson City, from the west side and downtown to Lakeview and south Carson. Dayton, Minden, and the lake ride the same trucks. The trucks belong to the carriers we vet. The license and the bond belong to Ship Guy.',
  'The 580 freeway runs along the east side of the city from Reno to the south end. Highway 395 continues south to Minden, Gardnerville, and California. Highway 50 climbs west over Spooner Summit to Lake Tahoe and runs east to Dayton and Fallon. Carson Street is the old highway through downtown past the Capitol.',
  'This page covers the freeway, 395, 50, Spooner, Carson Street, the west side, and the valley towns. It also covers the state offices, the legislature, the hospital, the lake, the passes, and the wind.'],
 'Carson City at a glance',
 ['Pickups in Carson City run 1 to 3 days. The city sits half an hour south of Reno. The Reno pool covers it on the same day. The 80 carriers come through Reno all day. The 395 trucks run the east side of the Sierra between Southern California and Oregon.',
  'Reno, Sacramento, and San Francisco are a same-day haul. Boise, Salt Lake City, Las Vegas, and Los Angeles take a day. Portland takes one to two, and Phoenix and Denver take two.'],
 'Tell us the neighborhood. The west side, the Capitol blocks, Kings Canyon, and the lake meet the truck on a main road. The east side, Lakeview, south Carson, Dayton, and the Carson Valley usually allow the curb.'))

BODY.append(sec('The Roads','The 580 Freeway, Highway 395, Highway 50, Spooner Summit, Carson Street, William Street, Fairview Drive, and College Parkway',
 prose(
  L('Carson City is a small grid between the Sierra and the desert with a freeway along one side. A carrier stays on the freeway and the wide streets and leaves the passes to the day.'),
  P('The 580 freeway comes down from Reno through Washoe Valley along the east side of the city. It ends at the south end of town. It opened in stages and was finished in 2017, and it took the trucks off Carson Street. The College Parkway exit serves the north side, and the Highway 50 exits serve the middle. The Fairview exit serves the south. Highway 395 continues south from the freeway through Indian Hills to Minden, Gardnerville, and the California line.'),
  P('Highway 50 comes in from the east as William Street and meets Carson Street downtown. From the south end of town it climbs Spooner Summit to the lake at seventy-one hundred feet. The state puts chain controls on it from November to April. A loaded trailer waits below a closure. Highway 50 east runs through Mound House to Dayton, Silver Springs, and Fallon. Carson Street is the old 395 through downtown past the Capitol. It has been two lanes and angled parking since the freeway opened. Fairview Drive and College Parkway cross the city east and west.'),
  P('The carriers come off the freeway at Highway 50 or Fairview. They meet at the big-box lots on Highway 50 east or the lots along south Carson Street. The lots at the mall on south Carson work outside the Nevada Day weekend. So do the lots at the fairgrounds off Clear Creek and the truck stops at Mound House. The Reno airport is forty minutes north for a fly-and-ship.'),
  P('Our office is on West Proctor Street downtown, a block off Carson Street near the Capitol.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the West Side, Kings Canyon, the North Side, Lakeview, the East Side, South Carson, Indian Hills, Mound House, Dayton, and the Carson Valley',
 prose(
  L('Carson City is a historic west side, a working east side, and new subdivisions at both ends. The truck meets the old streets on a main road and the new ones at the curb.'),
  P('Downtown is the Capitol, the legislature, and the state offices along Carson Street. The old hotels and the museum in the mint sit among them. The driver meets you on Carson Street outside the session or at the lots by the museum. The west side from Carson Street to the foothills is the historic district. The big houses from the Comstock years sit under cottonwoods on narrow streets. The handoff happens on Carson Street or at the lots on Division. Kings Canyon above it is winding roads into the foothills. The handoff moves to the bottom of the hill.'),
  P('The north side from College Parkway to Lakeview is subdivisions and the hospital on wide streets. The truck reaches the curb. Lakeview above Washoe Valley is bigger lots on paved roads, and the curb works. The east side along Highway 50 and Fairview is the industrial parks, the airport, and working grids. The curb works on most of it. South Carson from the mall to the prison is older ranch houses on wide streets. The truck comes to the house.'),
  P('Indian Hills and Johnson Lane south of the city are subdivisions on open ground, and the curb works. Mound House is industrial lots along Highway 50, and the handoff happens on the highway. Dayton is subdivisions along the river with wide streets. Minden and Gardnerville in the Carson Valley are small grids and ranches. The truck reaches the curb on most streets. The lake communities from Glenbrook to Stateline are gated drives on steep roads. The handoff happens on 50 or at a lot in Stateline.'),
  P('Dayton, Indian Hills, Mound House, and the Carson Valley ship with the same trucks and prices. Reno and Sparks do too. The lake adds the summit and a day in winter, and Fallon adds an hour on the day.'),
 )))

ROUTES=[("Reno, NV","I-580 · ~30 mi","Same day","$110–$190"),("Sacramento, CA","US-50/I-80 · ~140 mi","Same day","$180–$290"),
 ("San Francisco, CA","I-80 · ~250 mi","Same day","$230–$350"),("Boise, ID","US-95/I-84 · ~450 mi","1 day","$380–$540"),
 ("Salt Lake City, UT","I-80 · ~550 mi","1 day","$390–$550"),("Las Vegas, NV","US-95 · ~430 mi","1 day","$400–$560"),
 ("Los Angeles, CA","US-395/I-15 · ~440 mi","1 day","$400–$570"),("Portland, OR","US-395/I-5 · ~540 mi","1–2 days","$460–$670"),
 ("Phoenix, AZ","US-95/I-10 · ~720 mi","2 days","$600–$850"),("Denver, CO","I-80/I-25 · ~930 mi","2 days","$650–$920")]
BODY.append(rate_table('Lanes &amp; Costs','Carson City Car Shipping Lanes and Estimated Costs',
 'The lanes out of the capital, with open-trailer estimates for each. The form above prices your own.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Carson City, sedan that runs, open trailer. Add 10 to 25 percent for an SUV or a pickup, and more for enclosed. The week you pick and the Reno carriers free that week set the final number.',
 prose(
  P('Carson City prices with Reno on every lane. The Reno pool covers the capital on the same day. The Sacramento and Bay Area lanes ride 80 over Donner and fill every day with the California transplants. The Los Angeles lane rides 395 down the east side of the Sierra. The Las Vegas lane rides 95 across the desert and fills twice a week. The Boise and Portland lanes thin in winter.'),
  P('A session start in February or a Nevada Day weekend means a busy week. Size, condition, and timing are explained on the <a href="car-shipping-cost.html">cost guide</a>.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The State, the Legislature, the Hospital, the Industrial Parks, the Guard, the Naval Air Station, the College, the California Transplants, and the Lake',
 prose(
  L('Carson City relocates state workers, lawmakers, nurses, machinists, airmen, and retirees. The state moves the most.'),
  P('State government is the largest employer in the city. The agencies relocate staff on start dates with every administration. The legislature meets for a hundred twenty days in odd years from February into June. The members and the staff bring cars for the session. The handoff happens on Carson Street or at the museum lots. The courts and the state offices on the east side hire from across the state.'),
  P('The regional hospital on the north side brings residents each June and traveling nurses all winter. The handoff happens at the lots by the hospital. The industrial parks by the airport make fasteners, aircraft parts, and electronics. They relocate machinists and engineers on start dates. The college on the west side takes students in late August, and most of them commute. If the state or the hospital reimburses you, we produce the paperwork.'),
  P('The Guard’s state headquarters on Fairview Drive and the naval air station in Fallon rotate people on orders. The handoff happens at the headquarters lots or outside the Fallon gate. Ship Guy is a private broker, with no tie to the Navy or the Guard. See the <a href="military-car-shipping.html">military</a> page for how orders fix the timing.'),
  P('Households leaving California for the tax rates fill the Sacramento and Bay Area lanes year round. Most ship one car over the pass and drive the other. The lake communities send a car up in November and June. The paperwork for a state line is covered on the <a href="state-to-state-car-shipping.html">state-to-state</a> page.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Nevada Day, the Session, the Rendezvous, the Lake Summers, Spooner and Donner, the Washoe Zephyr, the Floods, the Fires, and the Smoke',
 prose(
  L('Carson City runs on a state calendar and a lake calendar. The weather problem is a pass that closes, a wind that stops high trailers, and the smoke.'),
  P('Nevada Day closes Carson Street for the biggest parade in the state on the last Saturday of October. The lots downtown fill the whole weekend. The session fills the capital from February into June in odd years. The Rendezvous takes Mills Park for a June weekend. The lake fills from Memorial Day to Labor Day, and 50 over Spooner crawls on summer weekends. Give a Nevada Day or a session-start date three weeks of notice.'),
  P('Spooner Summit and Donner Pass carry chain controls from November to April. The state closes them for a storm a few times each winter. A loaded trailer waits below a closure, and the Sacramento lane moves a day. The Washoe Zephyr blows every afternoon in spring. The state closes 395 through Washoe Valley to high-profile vehicles when it gusts past sixty. The carriers wait in Reno or Carson until it drops.'),
  P('The Carson River flooded the east side and Dayton in January 1997 and again in January 2017. The low roads along it closed for days. The Waterfall fire in 2004 burned down the west side foothills to the edge of the historic district. The Caldor fire in 2021 sent the south shore down the hill to Carson City for a week. The Tamarack fire the same summer closed 395 south of Minden. Smoke settles in the valley in August and September most years, and the carriers keep moving through it.'),
  P('Summer brings dry heat in the nineties and afternoon wind. A driver loads in the morning, and the figure holds.'),
 )+chips(["Downtown","The Capitol","The West Side","Kings Canyon","The North Side","Lakeview","Northridge","The East Side","Empire","South Carson","Stewart","Indian Hills","Johnson Lane","Mound House","Dayton","Minden","Gardnerville","Genoa","Washoe Valley","Glenbrook","Stateline"])
 +NOTE('Serving Carson City, the Carson Valley, and the Nevada shore of Tahoe, east-side curb or Glenbrook gate. Let us know the neighborhood and whether it runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Carson City?',
 prose(
  L('Open is the default in Carson City, and the table above is built on it.'),
  P('Enclosed keeps the cinders, the brine, and the desert grit off the paint. The collectors on the west side book it. So do the lake households moving a car worth more than the rest of the move. When a storm is coming over the pass and only an open truck has room, we say so.'),
  P('A commuter car or a state worker’s sedan does fine open. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain the trade.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('You get a figure, a lot off the freeway, and a signature when the car arrives. The session or the start date picks the week.'),
  P('Once you say yes, a carrier already working the Reno pool that week gets the car. The lot and the window are agreed the same day. The driver photographs the car at pickup and notes its condition on the Bill of Lading. Your initials go on it, and it is the check at delivery.'),
 )+ULI([
  "Everything personal out of the car",
  "A quarter tank of fuel, give or take",
  "Photos of each side and the odometer, taken before pickup",
  "A working key and a line on any known faults",
  "Any aftermarket alarm turned off",
  "On the west side, at the lake, or in a gated Tahoe drive, expect a freeway lot",
 ])+prose(P('Every step is on <a href="how-it-works.html">how it works</a>, and pickup morning is on <a href="car-shipping-preparation.html">preparation</a>.'))))

BODY.append(sec('Why Ship Guy','Why Carson City Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already work the Reno pool every day. We know when Spooner closes and when the Zephyr shuts 395 to high trailers.'),
  P('Our FMCSA license and our $75,000 bond are on the federal register, open to the public. The office is on West Proctor Street downtown.'),
  P('The same person answers from the quote until the car is delivered. The <a href="services.html">services</a> page has open, enclosed, and expedited side by side.'),
 )))

BODY.append(office('Carson City','111 W Proctor St #225','Carson City, NV 89701','+17753698161','(775) 369-8161','PT',
 '111+W+Proctor+St+%23225,+Carson+City,+NV+89701','Visit Us','Find Ship Guy in Carson City',
 'Our office is on West Proctor Street downtown, a block off Carson Street near the Capitol.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3818.4460807708406!2d-119.76723650000001!3d39.165065399999996!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80990b55613d5a53%3A0xfaea79c6f38e2362!2sShip%20Guy%20Auto%20Transport!5e1!3m2!1sen!2sus!4v1793631072573!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Carson City to Sacramento or Los Angeles?","Sacramento runs one hundred eighty to two hundred ninety dollars for a sedan. That is about one hundred forty miles over the Sierra. Los Angeles runs four hundred to five hundred seventy, about four hundred forty miles down 395. Reno is the lowest lane on the table, thirty miles up the freeway. SUVs and pickups cost 10 to 25 percent more."),
 ("Do you ship cars for state employees and the legislature?","Yes, in every season. The agencies relocate staff on start dates. The session brings members and staff to the capital from February into June in odd years. The handoff happens on Carson Street outside the session or at the museum lots. If the state reimburses the move, we produce the paperwork it asks for."),
 ("Can the carrier come to my street on the west side or at the lake?","The west side, no. The historic district is narrow streets under big cottonwoods. The driver meets you on Carson Street or at the lots on Division. The lake communities are gated drives on steep roads. The handoff happens on 50 or at a lot in Stateline. The north side, the east side, Lakeview, south Carson, Dayton, and the Carson Valley usually allow the curb."),
 ("What happens if Spooner or Donner closes on my pickup day?","The Sacramento lane moves a day. A loaded trailer waits below a closure until the state lifts the chain control. The carriers stage in Reno or Carson. The Las Vegas and Los Angeles lanes down 395 and 95 cross no pass and keep moving. We call the moment the forecast turns, and the figure holds."),
 ("Does the Washoe Zephyr stop car shipping?","For an afternoon. When the wind gusts past sixty, the state closes 395 through Washoe Valley to high-profile vehicles. A loaded trailer is one. The carriers wait in Reno or Carson until it drops, usually by evening. A spring pickup wants a morning window."),
 ("Do you ship cars for the Guard, the naval air station, or the hospital?","Yes. The Guard’s state headquarters on Fairview Drive and the naval air station in Fallon rotate people on orders. The handoff happens at the headquarters lots or outside the Fallon gate. The regional hospital brings residents each June and traveling nurses all winter. Ship Guy is a private broker with no tie to the Navy, the Guard, or the hospital."),
 ("Can you ship a car to or from Dayton, Minden, or Lake Tahoe?","Yes. Dayton, Indian Hills, Mound House, and the Carson Valley ride the same carriers and price as Carson City. Reno and Sparks do too. The lake adds Spooner Summit and a day in winter. The handoff happens on 50 or in Stateline. Fallon adds an hour on the day."),
 ("Does Nevada Day affect my pickup?","For a weekend. The parade closes Carson Street on the last Saturday of October, and the lots downtown fill from Friday. The handoff moves to the Highway 50 lots or the fairgrounds that weekend. The figure does not change. Give a Nevada Day date three weeks of notice."),
 ("Can you ship a car that does not run from Carson City?","Yes. The carrier brings a winch, and the figure covers the extra loading time. The lots off the freeway at Fairview and the big-box lots on Highway 50 are flat. Say whether it rolls, steers, and brakes."),
 ("What do you need for a Carson City car shipping quote?","The two addresses, with the neighborhood or the lake community. What it is and whether it runs. Open or enclosed, and the week around the session or the start date. With those, the Carson City figure comes back the same day."),
]
BODY.append(faq_section(FAQ,'Carson City FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Carson City?','Two minutes on the form above gets a Carson City figure on your lane. Name the neighborhood and the week, and a Reno carrier takes it.','+17753698161','(775) 369-8161','Get your free Carson City quote'))

build({
 'slug':'auto-transport-carson-city-nevada',
 'title':'Car Shipping in Carson City, NV — Auto Transport | Ship Guy',
 'meta':'Car shipping in Carson City, NV, the capital, half an hour south of Reno on the 580 freeway. State and legislature moves, hospital and industrial-park hires, the Guard and the Fallon air station, curbside pickups on the east side, in Lakeview, Dayton, and the Carson Valley, main-road handoffs on the west side and at the lake, Spooner and Donner, the Zephyr, and the fires. Local office on West Proctor Street. Free quote.',
 'h1':'Car Shipping in<br>Carson City, <span class="accent">Nevada</span>',
 'lede':'Open, enclosed, and expedited auto transport across Carson City, the Carson Valley, and the Nevada shore of Tahoe, planned around the freeway, 395, Highway 50, the session, the passes, and the wind.',
 'tel':'+17753698161','disp':'(775) 369-8161','brand':'Carson City','keyword':'car shipping in carson city',
 'localterms':['carson city','capital','580','freeway','highway 395','highway 50','spooner summit','seventy-one hundred feet','chain controls','donner','carson street','william street','fairview','college parkway','division','capitol','legislature','session','hundred twenty days','odd years','state offices','agencies','administration','courts','museum','mint','old hotels','comstock','cottonwoods','west side','historic district','kings canyon','north side','lakeview','northridge','east side','empire','industrial parks','airport','fasteners','aircraft parts','electronics','machinists','south carson','mall','prison','stewart','indian hills','johnson lane','mound house','dayton','silver springs','fallon','naval air station','minden','gardnerville','carson valley','genoa','washoe valley','reno','sparks','glenbrook','stateline','lake','tahoe','gated','regional hospital','residents','traveling nurses','college','students','guard','state headquarters','orders','california','transplants','tax rates','nevada day','parade','last saturday of october','rendezvous','mills park','memorial day','labor day','washoe zephyr','sixty','high-profile','carson river','january 1997','january 2017','waterfall fire','2004','caldor','2021','south shore','tamarack','smoke','nineties','fairgrounds','truck stops','fly-and-ship','sacramento','san francisco','bay area','boise','salt lake','las vegas','los angeles','portland','phoenix','denver','cinders','brine','grit','bill of lading','fmcsa','winch','2017','stages','clear creek'],
}, BODY, FAQ)
