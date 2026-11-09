import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Gresham, Oregon','Car shipping at the mouth of the Gorge, where the east wind brings the ice, the Mount Hood traffic crawls through town, and the Blue Line ends',
 ['Car shipping in Gresham runs on Interstate 84 and the Mount Hood Highway, with 205 ten minutes west. Ship Guy is a licensed auto transport broker with an office on Eastman Parkway by the light-rail station.',
  'We book vetted carriers across Gresham, from the Rockwood apartments to the Powell Valley farms. Troutdale, Wood Village, Fairview, Happy Valley, and Sandy ride the same trucks. The trucks are the carriers’ own. Ship Guy holds the license and the bond.',
  'Interstate 84 runs the north edge with exits at 181st, Fairview Parkway, Wood Village, and Troutdale. The Mount Hood Highway runs through town on Powell and Burnside to Sandy and the ski areas. Division, Stark, Glisan, and Sandy Boulevard run east and west. Eastman Parkway, Hogan Road, 181st, and Kane Drive run north and south.',
  'This page covers 84, 26, 205, the Gorge exit, the boulevards, and the hills. It also covers the chip fabs, the aerospace plant, the package hub, the hospital, and the college. The ski traffic, the ice storms, the Gorge fire, and the heat dome are here too.'],
 'Gresham at a glance',
 ['Most Gresham pickups land within 1 to 3 days. The city sits where the 84 trucks leave the Gorge and the 205 trucks reach the east side. The Seattle and California carriers run 5 and 205 past the city daily. The Boise and Spokane trucks come down 84. The Troutdale truck stops keep a pool staged a mile away.',
  'Eugene and Seattle are a same-day haul. Spokane and Boise take a day. Sacramento, San Francisco, and Salt Lake City take two. Los Angeles takes two to three, and Denver and Phoenix take three.'],
 'Tell us the part of town. Historic downtown, Gresham Butte, and the Persimmon hills meet the truck on a boulevard. Rockwood, Centennial, Powell Valley, Troutdale, and Fairview usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 84, US 26, Interstate 205, Powell Boulevard, Burnside Road, Division Street, Stark Street, Glisan Street, Sandy Boulevard, Eastman Parkway, Hogan Road, 181st Avenue, and Kane Drive',
 prose(
  L('Gresham is a grid at the foot of the Cascades. A freeway runs along the top, and the mountain highway runs through the middle. A carrier works the boulevards and leaves the hills alone.'),
  P('Interstate 84 runs along the north edge from Portland to the Gorge. The exits at 181st, Fairview Parkway, Wood Village, and Troutdale serve the city. Past Troutdale the freeway enters the Gorge. Wind, ice, and rockfall close it a few times each winter. Interstate 205 runs ten minutes west with exits at Division and Powell, carrying the Seattle and California lanes. US 26 is the Mount Hood Highway. It comes in on Powell Boulevard and turns up Burnside through downtown. Then it runs east to Sandy and the ski areas.'),
  P('Division Street carries the Town Fair shopping center and runs a block from the light rail. Stark Street runs the north side past the chip fab and the hospital to Troutdale. Glisan Street runs out to the second fab. Sandy Boulevard carries the aerospace plant and the Troutdale airport. Eastman Parkway runs from Division past City Hall to downtown and Powell. Hogan Road carries the east side north to south. 181st Avenue is the Rockwood spine from the freeway to Powell. Kane Drive runs southeast to the college and Orient Drive. Johnson Creek runs the south side and climbs its banks most winters.'),
  P('The carriers come off 84 at 181st or Wood Village and off 205 at Division. They meet at the Town Fair lots at Division and Eastman or the big-box lots at Gresham Station. The Troutdale truck stops at the Gorge exit work too. The college lots on Kane Drive work outside the term. The outlet lots in Troutdale and the park-and-ride at Cleveland Avenue work too. The Portland airport is fifteen minutes north across the slough for a fly-and-ship.'),
  P('Our office sits on Eastman Parkway beside the City Hall light-rail station, across from the Town Fair.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Historic Downtown, Rockwood, Centennial, Wilkes, Hollybrook, Gresham Butte, Persimmon, Powell Valley, Pleasant Valley, Kelly Creek, Troutdale, Wood Village, Fairview, Happy Valley, Sandy, and Corbett',
 prose(
  L('Gresham is an old farm town swallowed by Portland’s east side. A butte sits in the middle, and farms still ring the edge. The truck meets downtown and the hills on a boulevard and the grids at the curb.'),
  P('Historic downtown is Main Avenue, the arts plaza, and short blocks of storefronts. The streets are narrow, and the handoff happens at the Town Fair lots or on Eastman. Rockwood along 181st, Stark, and Burnside is the densest part of town. It is apartment complexes and small houses on a grid. The complexes allow a trailer at the entrance, and the grid allows the curb. Centennial and Wilkes on the west side are postwar grids where the curb works. Hollybrook and the blocks off Division are the same.'),
  P('Gresham Butte rises south of downtown with steep winding streets under firs. No trailer climbs it, and the driver meets you on Powell or Eastman. Persimmon is the golf course and the hills above Kane Drive, winding and steep. The handoff happens on Kane Drive. Powell Valley east of town is berry farms, nurseries, and houses on wide roads. The truck reaches the driveway. Pleasant Valley and Kelly Creek to the south are new subdivisions on the slopes. The curb works where the covenants allow it.'),
  P('Troutdale is the Gorge gateway, the outlets, the package hub, and old streets by the Sandy River. The curb works on the grid, and the hub takes a handoff at its gate. Wood Village and Fairview are small grids and apartments where the curb works. Happy Valley to the southwest is hills of new houses, and the handoff happens at the development entrance. Sandy is the mountain town fifteen miles east on 26. Corbett sits on the Gorge rim, where the east wind blows hardest and the ice comes first.'),
  P('Troutdale, Wood Village, Fairview, Happy Valley, and Damascus ride the same trucks. They price the same as Gresham. Sandy and Boring do too. Corbett and the Gorge towns add a day in winter.'),
 )))

ROUTES=[("Eugene, OR","I-205/I-5 · ~120 mi","Same day","$180–$290"),("Seattle, WA","I-205/I-5 · ~180 mi","Same day","$220–$340"),
 ("Spokane, WA","I-84/US-395 · ~335 mi","1 day","$320–$460"),("Boise, ID","I-84 · ~415 mi","1 day","$370–$530"),
 ("Sacramento, CA","I-5 · ~590 mi","1–2 days","$480–$700"),("San Francisco, CA","I-5 · ~645 mi","2 days","$520–$750"),
 ("Salt Lake City, UT","I-84 · ~755 mi","2 days","$560–$820"),("Los Angeles, CA","I-5 · ~975 mi","2–3 days","$700–$980"),
 ("Denver, CO","I-84/I-80 · ~1,225 mi","3 days","$850–$1,200"),("Phoenix, AZ","I-5/US-93 · ~1,340 mi","3–4 days","$900–$1,250")]
BODY.append(rate_table('Lanes &amp; Costs','Gresham Car Shipping Lanes and Estimated Costs',
 'The lanes east Multnomah County cars ship most, with open-trailer estimates. Price your exact lane on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Gresham, running sedan, open trailer. An SUV or a pickup runs 10 to 25 percent higher, and enclosed sits above that. The week and the carriers on 84 and 205 that week set the figure.',
 prose(
  P('Gresham prices with Portland on the valley lanes and a little under on the eastern ones. Seattle and California ride 205 to 5 and run daily. Boise and Salt Lake City ride 84 up the Gorge. The Gresham pickup is the last stop before the trucks climb. Spokane rides 84 and 395 through the Tri-Cities. The California lane fills with the households leaving the Bay Area for the east side. The Gorge closures in winter can hold the eastern lanes a day.'),
  P('A September move-in at the college or a fab hiring wave makes for a busy week. The <a href="car-shipping-cost.html">cost guide</a> covers size, condition, and timing in turn.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Chip Fabs, the Aerospace Plant, the Package Hub, the Hospital, the College, the Nurseries, the Portland Households Moving East, and the Families From Everywhere',
 prose(
  L('Gresham relocates fab engineers, machinists, warehouse staff, nurses, students, and families priced out of Portland. The fabs and the plant move the most.'),
  P('The two chip fabs on Stark and Glisan relocate engineers and technicians on program dates. They come from Arizona, Texas, and overseas. The aerospace plant on Sandy Boulevard machines landing gear and relocates machinists from the other plants. The package hub in Troutdale and the warehouses around the airport relocate supervisors in spring and fall. The handoff happens at the lots nearest the gate. When the employer pays for the shipment, we write it up however it needs.'),
  P('The hospital on Stark Street brings nurses all year. Mount Hood Community College fills its campus on Kane Drive each September, and the cars leave in June. A parent books, and an adult signs at the campus lot. The nurseries and berry farms of Powell Valley hire on the season. Households priced out of Portland buy in Gresham and Troutdale and ride the Blue Line in. Families arrive in Rockwood from Latin America, Ukraine, and the Pacific islands. Many bring a car from a relative in California. The <a href="state-to-state-car-shipping.html">state-to-state</a> page explains the paperwork a state line adds.'),
  P('The Air Guard wing at the Portland airport rotates airmen on orders. The Guard’s post in Clackamas does the same. Ship Guy is a private broker and not part of the Guard. The <a href="military-car-shipping.html">military</a> page covers orders and the dates they set.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Ski Traffic, the Gorge Weekends, the Arts Festival, the Saturday Market, the College Term, the East Wind, the Ice Storms, the Gorge Fire, the Heat Dome, and Johnson Creek',
 prose(
  L('Gresham runs on a mountain calendar and a Gorge calendar. The weather problem is the east wind, which ices Gresham before the rest of the metro.'),
  P('The ski traffic crawls through town on Burnside and Powell every winter Friday evening and Sunday afternoon. The Gorge traffic fills 84 past Troutdale every summer weekend, and the falls run on timed permits. The arts festival closes Main Avenue for a weekend each July. The Saturday market fills downtown from May to October. The college term fills Kane Drive each September. Give a winter weekend or a September date three weeks of notice.'),
  P('The east wind pours out of the Gorge in winter and freezes the rain as it falls. The January 2024 ice storm shut Gresham and Troutdale for a week and closed 84 at Troutdale. Tens of thousands lost power for days. The February 2021 ice storm did the same for most of a week. The January 2017 snow sat for ten days. Two inches of ice stops every truck, and the carriers wait in Portland until the wind drops. A winter pickup can slip two days.'),
  P('The Gorge fire in September 2017 closed 84 east of Troutdale for two weeks. Ash fell on the city. The September 2020 fires put the south side on evacuation notice. The smoke sat on the metro for ten days. The June 2021 heat dome hit one hundred sixteen degrees, and the drivers loaded at dawn. Johnson Creek climbs its banks most winters and floods the low streets along the trail. The Sandy River runs high every winter, and Troutdale watches it.'),
 )+chips(["Historic Downtown","Main Avenue","Rockwood","Centennial","Wilkes","Hollybrook","Gresham Butte","Persimmon","Powell Valley","Pleasant Valley","Kelly Creek","Hogan Cedars","Gresham Vista","Troutdale","Wood Village","Fairview","Happy Valley","Damascus","Boring","Sandy","Corbett","Portland"])
 +NOTE('Serving Gresham, east Multnomah County, and the Gorge gateway, Rockwood complex or Persimmon hillside. Tell us the part of town and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Gresham?',
 prose(
  L('Open trailers carry most of east county’s cars, and the table above assumes one.'),
  P('Enclosed keeps the Gorge grit, the winter brine, and the summer smoke off the paint. The engineers moving a car worth more than the relocation book it. So do the collectors in Powell Valley with a restored truck. When an ice storm is coming and only an open truck has room, we tell you that first.'),
  P('A commuter car or a student’s hatchback rides open and arrives fine. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages lay out the difference.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A figure, a lot off Division, and a signature when the car comes off the truck. The program date or the term picks the week.'),
  P('Approve the figure, and we hand the car to a carrier already running 84 or 205 that week. The lot and the window are set the same day. The driver photographs the car at pickup and records its condition on the Bill of Lading. You initial it, and it is the reference at delivery.'),
 )+ULI([
  "Your belongings out of the cabin and the trunk",
  "Fuel at a quarter tank or less",
  "Photos of every side and the odometer before the truck arrives",
  "A working key and a note on known faults",
  "Aftermarket alarms turned off",
  "On the Butte, in Persimmon, or in an ice storm, expect the Town Fair lots",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> page walks the steps, and the <a href="car-shipping-preparation.html">preparation</a> page covers the morning of pickup.'))))

BODY.append(sec('Why Ship Guy','Why Gresham Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already stage in Troutdale and run 84 and 205 every day. We know when the east wind is coming and which hills never take a trailer.'),
  P('Our FMCSA license and our $75,000 bond are public record on the federal register. The office is on Eastman Parkway by the light-rail station.'),
  P('One person at Ship Guy carries your move from the quote to the delivery call. The <a href="services.html">services</a> page covers open, enclosed, and expedited one by one.'),
 )))

BODY.append(office('Gresham','1333 NW Eastman Pkwy #478','Gresham, OR 97030','+15037838394','(503) 783-8394','PT',
 '1333+NW+Eastman+Pkwy+%23478,+Gresham,+OR+97030','Visit Us','Find Ship Guy in Gresham',
 'Our office sits on Eastman Parkway beside the City Hall light-rail station, across from the Town Fair.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3451.0660091940376!2d-122.4228701!3d45.5140983!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x5495997b524923cd%3A0xc8fa52bb6fd7c9a0!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1794237493403!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Gresham to Seattle or Boise?","Seattle runs two hundred twenty to three hundred forty dollars for a sedan. It is about one hundred eighty miles up 205 and 5. Boise runs three hundred seventy to five hundred thirty up the Gorge. Eugene is the lowest lane on the table. Los Angeles runs seven hundred to nine hundred eighty. An SUV or a pickup adds 10 to 25 percent."),
 ("Why does the ice hit Gresham before the rest of Portland?","Because the east wind pours out of the Gorge and freezes the rain as it falls. Gresham, Troutdale, and Corbett ice up while the west side stays wet. The January 2024 and February 2021 storms each shut the east side for most of a week. The carriers wait in Portland until the wind drops."),
 ("Can the carrier come to my street on Gresham Butte or in Persimmon?","No. The Butte is steep winding streets under firs, and Persimmon climbs the same way above Kane Drive. The driver meets you on Powell, Eastman, or Kane Drive. Rockwood, Centennial, Powell Valley, Troutdale, and Fairview usually allow the curb."),
 ("Do you ship cars for the chip fabs or the aerospace plant?","Yes, on every program date. The two fabs on Stark and Glisan relocate engineers from Arizona, Texas, and overseas. The aerospace plant on Sandy Boulevard relocates machinists. The package hub in Troutdale moves supervisors in spring and fall. When the employer pays, we write it up however it needs."),
 ("Does the Gorge closing affect my shipment?","The eastern lanes, a few times each winter. Wind, ice, and rockfall close 84 past Troutdale, and the Boise and Salt Lake trucks wait below it. The 2017 fire closed it for two weeks. The valley lanes on 205 and 5 run normally. We tell you when the Gorge is in play."),
 ("What happens during the ski traffic?","Burnside and Powell crawl every winter Friday evening and Sunday afternoon with the mountain traffic. A carrier plans the Gresham stop for a weekday or a Saturday morning. The handoff moves to the Town Fair lots when the highway is jammed. The figure does not change."),
 ("Can you deliver a car for a Mount Hood Community College student?","Yes. The term fills the campus on Kane Drive each September, and the cars leave in June. A parent books, and an adult signs at the campus lot. The handoff happens at the lot off Kane Drive or at the Town Fair."),
 ("Can you ship a car to or from Troutdale, Sandy, or Happy Valley?","Yes. Troutdale, Wood Village, Fairview, Happy Valley, and Damascus ride the same carriers and price the same as Gresham. Sandy and Boring do too. Corbett and the Gorge towns add a day in winter."),
 ("Can you ship a car that does not run from Gresham?","Yes. The carrier brings a winch, and the figure includes the loading time. The Town Fair lots and the Gresham Station lots are flat. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Gresham car shipping quote?","Both addresses, with the part of town. The year, make, and model, and whether it runs. Open or enclosed, and the week around the program date or the term. With those, the Gresham figure comes back the same day."),
]
BODY.append(faq_section(FAQ,'Gresham FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Gresham?','Two minutes on the form above puts a Gresham figure on your lane. Tell us the part of town and the week, and a carrier already staged in Troutdale takes it.','+15037838394','(503) 783-8394','Get your free Gresham quote'))

build({
 'slug':'auto-transport-gresham-oregon',
 'title':'Car Shipping in Gresham, OR — Auto Transport | Ship Guy',
 'meta':'Car shipping in Gresham, OR, on Interstate 84, the Mount Hood Highway, and 205. The chip fabs, the aerospace plant, the package hub in Troutdale, the hospital, and the college, boulevard handoffs for Gresham Butte and Persimmon, curbside pickups in Rockwood, Centennial, Powell Valley, and Troutdale, the ski traffic, the Gorge closures, and the east-wind ice storms. Local office on Eastman Parkway. Free quote.',
 'h1':'Car Shipping in<br>Gresham, <span class="accent">Oregon</span>',
 'lede':'Open, enclosed, and expedited auto transport across Gresham, east Multnomah County, and the Gorge gateway, planned around 84 and 205, the program dates, the ski traffic, the east wind, and the fires.',
 'tel':'+15037838394','disp':'(503) 783-8394','brand':'Gresham','keyword':'car shipping in gresham',
 'localterms':['gresham','interstate 84','us 26','mount hood highway','interstate 205','powell boulevard','burnside','division street','stark street','glisan street','sandy boulevard','eastman parkway','hogan road','181st','kane drive','orient drive','fairview parkway','wood village','troutdale','gorge','rockfall','light rail','blue line','city hall','town fair','gresham station','park-and-ride','cleveland avenue','johnson creek','sandy river','historic downtown','main avenue','arts plaza','rockwood','apartment complexes','centennial','wilkes','hollybrook','gresham butte','firs','persimmon','golf course','powell valley','berry farms','nurseries','pleasant valley','kelly creek','covenants','hogan cedars','gresham vista','outlets','airport','package hub','fairview','happy valley','damascus','boring','sandy','corbett','east wind','portland','chip fabs','arizona','texas','aerospace plant','landing gear','machinists','warehouses','hospital','mount hood community college','term','latin america','ukraine','pacific islands','priced out','air guard','clackamas','ski traffic','friday evening','sunday afternoon','timed permits','arts festival','saturday market','january 2024','ice storm','february 2021','january 2017','ten days','two inches of ice','gorge fire','september 2017','two weeks','ash','september 2020','evacuation notice','smoke','june 2021','heat dome','one hundred sixteen','eugene','seattle','spokane','boise','sacramento','san francisco','salt lake city','los angeles','denver','phoenix','tri-cities','bay area','fly-and-ship','slough','truck stops','grit','brine','restored truck','bill of lading','fmcsa','winch'],
}, BODY, FAQ)
