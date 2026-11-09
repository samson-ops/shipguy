import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Chattanooga, Tennessee','Car shipping where Interstates 24 and 75 squeeze between the ridges, the German plant moves engineers, and the triathlon closes the riverfront',
 ['Car shipping in Chattanooga runs on Interstates 24 and 75, which meet east of downtown between the ridges. Ship Guy is a licensed auto transport broker with an office at Eleventh and Market downtown.',
  'We book vetted carriers across Chattanooga, from the Southside lofts to the mountain towns and the Georgia line. East Ridge, Hixson, Red Bank, Ooltewah, Collegedale, and Fort Oglethorpe ride the same trucks. The trucks are the carriers’ own. Ship Guy holds the license and the bond.',
  'Interstate 24 comes down Monteagle from Nashville, follows the river under Lookout Mountain, and cuts through Missionary Ridge. Interstate 75 climbs from Atlanta through East Ridge and leaves for Knoxville past the plant. Highway 27 runs north and south through downtown. Highway 153, Brainerd Road, Lee Highway, Shallowford Road, and Amnicola Highway carry the rest.',
  'This page covers 24, 75, 27, 153, the Ridge Cut, the bridges, downtown, and the mountains. It also covers the plant, the power authority, the insurers, the hospitals, and the university. The Ironman, the regatta, the tornadoes, and the fog on Monteagle are here too.'],
 'Chattanooga at a glance',
 ['Most Chattanooga pickups land within 1 to 3 days. The city sits where the Atlanta-to-Midwest trucks on 75 meet the Nashville trucks on 24. The carriers pass through the split all day. The plant and the warehouses keep the pool deep.',
  'Atlanta, Knoxville, Nashville, Huntsville, and Birmingham are a same-day haul. Asheville, Memphis, and Charlotte take a day. Jacksonville takes one to two, and Orlando takes two.'],
 'Tell us the neighborhood. Downtown, St. Elmo, Lookout Mountain, and Signal Mountain meet the truck on a main road below the grade. Brainerd, East Brainerd, Hixson, Red Bank, Ooltewah, and East Ridge usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 24, Interstate 75, Interstate 59, Highway 27, Highway 153, Highway 58, Brainerd Road, Lee Highway, Shallowford Road, Gunbarrel Road, Amnicola Highway, and the River Bridges',
 prose(
  L('Chattanooga is a river bend hemmed in by three ridges, and the interstates thread the gaps. A carrier learns the Ridge Cut and the split and stays off the mountains.'),
  P('Interstate 24 drops off Monteagle Mountain from Nashville. Fog and ice close the mountain a few times a winter. It runs along the river under Lookout Mountain, past downtown, and through the Ridge Cut in Missionary Ridge. It ends at the split with 75 on the east side. Interstate 75 comes up from Atlanta and Dalton through East Ridge and meets 24 at the split. It runs northeast past the mall and the plant to Knoxville. Interstate 59 joins 24 at Wildwood, just over the Georgia line, carrying Birmingham.'),
  P('Highway 27 runs north and south through downtown, rebuilt over the last decade. It crosses the Olgiati Bridge to Red Bank and Soddy-Daisy. Highway 153 leaves 75 for Hixson, the airport, and the Chickamauga Dam. Highway 58 runs out to Harrison and the lake. Brainerd Road, Lee Highway, and Shallowford Road fan east from the Ridge Cut. Gunbarrel Road carries the mall traffic. Amnicola Highway follows the river from downtown out to the dam, past the community college. Market Street, Broad Street, and Martin Luther King Boulevard carry downtown. The Market Street and Veterans bridges carry cars to the North Shore. The Walnut Street Bridge carries walkers.'),
  P('The carriers come off 75 at Shallowford Road or Hamilton Place Boulevard. On 24 they use Browns Ferry Road or the Market Street exit. They meet at the mall lots on Gunbarrel Road or the big-box lots on Lee Highway. The lots on 153 in Hixson work too. The stadium lots off Twentieth Street work outside game days. So do the truck stops at Tiftonia and the Georgia line. The airport is fifteen minutes east on Lee Highway for a fly-and-ship.'),
  P('Our office is in the eleven-story building at Eleventh and Market, beside Warehouse Row and near Miller Plaza.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the Southside, the North Shore, Riverview, Highland Park, St. Elmo, Lookout Mountain, Signal Mountain, Missionary Ridge, Brainerd, East Brainerd, East Ridge, Hixson, Red Bank, Ooltewah, Collegedale, and Fort Oglethorpe',
 prose(
  L('Chattanooga is a brick downtown on a river, three mountains with houses, and valleys of subdivisions between. The truck meets the mountains at the bottom and the valleys at the curb.'),
  P('Downtown is Market and Broad, the aquarium, the riverfront, and one-way streets full of garages. The driver meets you on Riverfront Parkway or at a garage entrance. The Southside is Main Street, brick warehouses turned lofts, and the new ballpark district on South Broad. The handoff happens on Main or at the stadium lots. The North Shore across the river is Frazier Avenue, Coolidge Park, and bungalows on short blocks. The handoff happens at the park lots. Riverview and Stuart Heights are winding streets under old trees, and the driver meets you on Hixson Pike.'),
  P('Highland Park and Ridgedale are bungalow grids where the curb works. St. Elmo sits under Lookout Mountain at the foot of the Incline, narrow and steep at the top. The handoff happens on Tennessee Avenue. Lookout Mountain and Signal Mountain are switchbacks, and no trailer climbs either one. The Lookout handoff happens in St. Elmo, and the Signal handoff happens in Red Bank. Missionary Ridge is one narrow road along the crest. The driver meets you on Brainerd Road below it.'),
  P('Brainerd and East Ridge are postwar grids, and East Brainerd is subdivisions on wide streets. The curb works in all three. Hixson and Red Bank north of the river are subdivisions and strip centers. The curb works there too. Ooltewah and Collegedale are new subdivisions around the college and the bakery, with covenants here and there. A covenant moves the handoff to the entrance. Soddy-Daisy, Harrison, and Apison are lake lots and country roads, and the handoff happens on 58 or 27. Fort Oglethorpe, Rossville, and Ringgold across the Georgia line are grids and subdivisions where the curb works.'),
  P('East Ridge, Hixson, Red Bank, Ooltewah, Collegedale, and Fort Oglethorpe ride the same trucks. They price the same as the city. Ringgold, Soddy-Daisy, and Cleveland do too. Dalton adds a figure, and the mountain towns add a day.'),
 )))

ROUTES=[("Knoxville, TN","I-75 · ~110 mi","Same day","$150–$240"),("Huntsville, AL","US-72 · ~100 mi","Same day","$160–$260"),
 ("Atlanta, GA","I-75 · ~120 mi","Same day","$170–$280"),("Nashville, TN","I-24 · ~135 mi","Same day","$190–$300"),
 ("Birmingham, AL","I-59 · ~150 mi","Same day","$200–$310"),("Asheville, NC","I-75/I-40 · ~225 mi","1 day","$260–$390"),
 ("Memphis, TN","I-24/I-40 · ~340 mi","1 day","$330–$480"),("Charlotte, NC","I-75/I-85 · ~360 mi","1 day","$340–$490"),
 ("Jacksonville, FL","I-75/I-10 · ~430 mi","1–2 days","$390–$560"),("Orlando, FL","I-75 · ~580 mi","2 days","$470–$690")]
BODY.append(rate_table('Lanes &amp; Costs','Chattanooga Car Shipping Lanes and Estimated Costs',
 'The lanes Hamilton County cars run most, with open-trailer estimates. Your exact lane prices on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Chattanooga, running sedan, open trailer. An SUV or a pickup runs 10 to 25 percent above, and enclosed runs higher still. The week and the carriers on 75 that week set the number.',
 prose(
  P('Chattanooga prices below Nashville and Knoxville on the Georgia and Alabama lanes. Atlanta is two hours down 75, and the trucks run it hourly. Huntsville rides 72 along the river, and Birmingham rides 59. The Knoxville and Ohio Valley lanes ride 75 north. Nashville and the Midwest ride 24 over Monteagle. The Florida lane fills each fall when the retirees go south and each spring when they return.'),
  P('A plant hiring wave or the Ironman weekend means a busy week. The <a href="car-shipping-cost.html">cost guide</a> explains size, condition, and timing one at a time.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The German Plant, the Warehouses at Enterprise South, the Power Authority, the Two Insurers, the Hospitals, the University, the College in Collegedale, the Bakery, and the Remote Workers',
 prose(
  L('Chattanooga relocates engineers, warehouse managers, nurses, students, and people who came for the river and the fiber. The plant moves the most.'),
  P('The German plant at Enterprise South builds cars and electric vehicles. It relocates engineers from Germany and across the country on program dates. The handoff happens at the lots off Volkswagen Drive. The online retailer’s warehouses next door relocate managers in spring and fall. The power authority’s office complex downtown moves engineers on start dates. The two insurers with headquarters downtown and on Cameron Hill move analysts and managers. When the employer pays for the shipment, we write it up however it needs.'),
  P('The three hospital systems bring residents each July and traveling nurses all year. The university downtown sends cars in each August and home each May. The college in Collegedale does the same on its own calendar. A parent books, and an adult signs at the lot. The bakery in Collegedale and the plants in the industrial parks hire from across the South. The city’s fiber network drew remote workers from both coasts. The climbers and paddlers followed the rock and the river.'),
  P('The Guard’s armory and the reserve center rotate people on orders. The posts in Georgia and Alabama send families through on the same calendar. Ship Guy is a private broker and not part of the services. The <a href="military-car-shipping.html">military</a> page covers orders and the dates they set.'),
  P('Retirees come to the lake and the mountains from Florida and the Midwest. Some go back south each winter. The <a href="state-to-state-car-shipping.html">state-to-state</a> page sets out the paperwork a state line adds.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Riverbend, the Ironman, the Regatta, Nightfall, the Sunday Market, Football Saturdays, the Leaf Traffic, the Tornadoes, the Ice, and the Fog on Monteagle',
 prose(
  L('Chattanooga runs on a riverfront calendar and a university calendar. The weather problem is a tornado season and a mountain pass that closes in fog and ice.'),
  P('Riverbend fills the riverfront for a weekend each June. The Ironman closes Riverfront Parkway, the bridges, and Amnicola each September. The half-distance race does it again in May. The world championship for the half comes to the city at the end of August 2027. The regatta brings thousands of rowers to the river the first weekend of November. Nightfall closes a block of Market Street at Miller Plaza on summer Fridays. The Sunday market fills the pavilion on the Southside from spring to fall. Football Saturdays fill the stadium lots off Twentieth Street. The leaf traffic crawls up Lookout Mountain every October weekend. Give a race weekend three weeks of notice.'),
  P('The April 2011 outbreak put EF4 tornadoes through Apison and Ringgold. The Easter 2020 tornado ran through East Brainerd and Ooltewah at one hundred forty-five miles an hour. It killed three people in the county and damaged hundreds of homes. A tornado watch holds the truck at the lot until it passes.'),
  P('Monteagle closes 24 in fog or ice a few times a winter. The Nashville trucks wait in Manchester. The March 1993 blizzard dropped close to twenty inches on the city. The February 2015 ice shut the ridges for a day or two. February 2019 was the wettest February on record, and the low roads went under water. Fog settles on the river on fall mornings. Summer brings heat and an afternoon storm that passes in an hour.'),
 )+chips(["Downtown","The Southside","Main Street","South Broad","The North Shore","Frazier Avenue","Riverview","Stuart Heights","Hill City","Highland Park","Ridgedale","St. Elmo","Lookout Mountain","Signal Mountain","Missionary Ridge","Brainerd","East Brainerd","East Ridge","Hixson","Red Bank","Ooltewah","Collegedale","Soddy-Daisy","Harrison","Apison","Enterprise South","Fort Oglethorpe","Rossville","Ringgold","Cleveland","Dalton"])
 +NOTE('Serving Chattanooga, Hamilton County, and the north Georgia towns, Southside loft or Signal Mountain switchback. Name the neighborhood and tell us whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Chattanooga?',
 prose(
  L('Open trailers do most of the Tennessee Valley’s work, and the table above prices one.'),
  P('Enclosed keeps the pollen, the brine before an ice storm, and the spring hail off the paint. The engineers moving a car worth more than the relocation book it. So do the collectors on Lookout Mountain and the retirees arriving with a convertible. When a storm is in the forecast and only an open truck has room, we say that first.'),
  P('A commuter car or a student’s hatchback rides open and arrives fine. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain the difference.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A figure, a lot off 75, and a signature when the car comes down the ramp. The program date or the start date picks the week.'),
  P('Approve the figure, and we place the car with a carrier already on 24 or 75 that week. The lot and the window come the same day. At pickup the driver photographs the car and records its condition on the Bill of Lading. You initial it, and it is the reference when the car arrives.'),
 )+ULI([
  "Your belongings out of the cabin and the trunk",
  "Fuel at a quarter tank or less",
  "Photos of every side and the odometer before the truck comes",
  "A working key and a note on anything that acts up",
  "Aftermarket alarms switched off",
  "On Lookout, on Signal, or on the Ridge, expect a lot at the bottom of the grade",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> page walks the steps, and the <a href="car-shipping-preparation.html">preparation</a> page covers pickup morning.'))))

BODY.append(sec('Why Ship Guy','Why Chattanooga Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already run 24 and 75 through the split every day. We know when Monteagle closes and which weekends the river takes the parkway.'),
  P('Our FMCSA license and our $75,000 bond are a matter of public record on the federal register. The office is at Eleventh and Market downtown.'),
  P('One person at Ship Guy carries your move from the quote to the delivery call. The <a href="services.html">services</a> page covers open, enclosed, and expedited in turn.'),
 )))

BODY.append(office('Chattanooga','1100 Market St Ste 770','Chattanooga, TN 37402','+14232053243','(423) 205-3243','ET',
 '1100+Market+St+Ste+770,+Chattanooga,+TN+37402','Visit Us','Find Ship Guy in Chattanooga',
 'Our office is in the eleven-story building at Eleventh and Market, beside Warehouse Row and near Miller Plaza.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4032.11763157492!2d-85.3089386!3d35.043594299999995!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x88605fe1a7c1d035%3A0x952e2dabb6a7935!2sShip%20Guy%20Auto%20Transport!5e1!3m2!1sen!2sus!4v1794237179114!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Chattanooga to Atlanta or Nashville?","Atlanta runs one hundred seventy to two hundred eighty dollars for a sedan. It is about one hundred twenty miles down 75. Nashville runs one hundred ninety to three hundred over Monteagle. Knoxville is the lowest lane on the table. Orlando runs four hundred seventy to six hundred ninety. An SUV or a pickup adds 10 to 25 percent."),
 ("Can the carrier come up Lookout Mountain or Signal Mountain?","No. Both are switchbacks, and no trailer climbs them. The Lookout handoff happens in St. Elmo at the foot of the Incline. The Signal handoff happens in Red Bank. Missionary Ridge works the same way from Brainerd Road. Brainerd, East Brainerd, Hixson, Red Bank, Ooltewah, and East Ridge usually allow the curb."),
 ("Do you ship cars for the plant at Enterprise South?","Yes, on every program date. The German plant relocates engineers from Germany and across the country. The warehouses next door move managers in spring and fall. The handoff happens at the lots off Volkswagen Drive. When the employer pays for the shipment, we write it up however it needs."),
 ("What happens on an Ironman weekend?","The riverfront closes. Riverfront Parkway, the bridges, and Amnicola shut down for the race each September. They close again for the half in May. The handoff moves to the Gunbarrel Road lots or the Lee Highway lots. The figure does not change. The world championship for the half comes at the end of August 2027. Give a race weekend three weeks of notice."),
 ("Is Monteagle a problem for a Nashville shipment?","A few times each winter. Fog or ice closes 24 on the mountain. The Nashville trucks wait in Manchester until it reopens, usually a day. The rest of the year the grade only slows the truck. We tell you when the mountain is closed."),
 ("What happens if a tornado watch is posted on my pickup day?","The truck stays at the lot until the watch passes. The April 2011 outbreak hit Apison and Ringgold. The Easter 2020 tornado ran through East Brainerd and Ooltewah. A watch moves the pickup by a few hours or to the next morning. The figure stays where it was."),
 ("Can you deliver a car for a student at the university or the college in Collegedale?","Yes. Cars arrive in August and leave in May on both calendars. A parent books, and an adult signs at the lot. The downtown campus streets are closed to a trailer in move-in week. The handoff moves to the stadium lots. The window follows your date."),
 ("Can you ship a car to or from Fort Oglethorpe, Ringgold, or Cleveland?","Yes. East Ridge, Hixson, Red Bank, Ooltewah, Collegedale, and Fort Oglethorpe ride the same carriers. They price the same as the city. Ringgold, Soddy-Daisy, and Cleveland do too. Dalton adds a figure, and the mountain towns add a day."),
 ("Can you ship a car that does not run from Chattanooga?","Yes. The carrier brings a winch, and the figure includes the loading time. The mall lots on Gunbarrel Road and the Lee Highway lots are flat. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Chattanooga car shipping quote?","Both addresses, with the neighborhood. The year, make, and model, and whether it runs. Open or enclosed, and the week around the program date or the start date. With those, the Chattanooga figure comes back the same day."),
]
BODY.append(faq_section(FAQ,'Chattanooga FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Chattanooga?','Two minutes on the form above puts a Chattanooga figure on your lane. Name the neighborhood and the week, and a carrier already on 75 takes it.','+14232053243','(423) 205-3243','Get your free Chattanooga quote'))

build({
 'slug':'auto-transport-chattanooga-tennessee',
 'title':'Car Shipping in Chattanooga, TN — Auto Transport | Ship Guy',
 'meta':'Car shipping in Chattanooga, TN, where Interstates 24 and 75 meet between the ridges. The German plant at Enterprise South, the power authority, the insurers, the hospitals, and the university, main-road handoffs for Lookout Mountain, Signal Mountain, and the Southside, curbside pickups in Brainerd, East Brainerd, Hixson, Red Bank, and Ooltewah, the Ironman, the tornadoes, and the fog on Monteagle. Local office at Eleventh and Market downtown. Free quote.',
 'h1':'Car Shipping in<br>Chattanooga, <span class="accent">Tennessee</span>',
 'lede':'Open, enclosed, and expedited auto transport across Chattanooga, Hamilton County, and the north Georgia towns, planned around 24 and 75, the plant dates, the river weekends, the tornado season, and the mountain pass.',
 'tel':'+14232053243','disp':'(423) 205-3243','brand':'Chattanooga','keyword':'car shipping in chattanooga',
 'localterms':['chattanooga','interstate 24','interstate 75','interstate 59','highway 27','highway 153','highway 58','brainerd road','lee highway','shallowford road','gunbarrel road','amnicola','market street','broad street','martin luther king','riverfront parkway','olgiati bridge','market street and veterans','walnut street bridge','monteagle','ridge cut','missionary ridge','the split','wildwood','georgia line','hamilton place','browns ferry','tiftonia','twentieth street','stadium lots','eleventh and market','warehouse row','miller plaza','eleven-story','downtown','aquarium','garages','the southside','main street','lofts','ballpark','south broad','the north shore','frazier avenue','coolidge park','riverview','stuart heights','hixson pike','highland park','ridgedale','st. elmo','incline','tennessee avenue','lookout mountain','signal mountain','switchbacks','brainerd','east brainerd','east ridge','hixson','red bank','ooltewah','collegedale','covenant','soddy-daisy','harrison','apison','fort oglethorpe','rossville','ringgold','cleveland','dalton','enterprise south','german plant','electric vehicles','volkswagen drive','online retailer','warehouses','power authority','insurers','cameron hill','hospital systems','residents','traveling nurses','university','college','bakery','industrial parks','fiber','remote workers','climbers','paddlers','armory','reserve center','retirees','lake','riverbend','ironman','half-distance','world championship','august 2027','regatta','rowers','nightfall','sunday market','pavilion','football saturdays','leaf traffic','april 2011','ef4','easter 2020','one hundred forty-five','three people','hundreds of homes','tornado watch','manchester','march 1993','twenty inches','february 2015','february 2019','wettest february','fog','fly-and-ship','airport','mall lots','big-box lots','truck stops','knoxville','huntsville','atlanta','nashville','birmingham','asheville','memphis','charlotte','jacksonville','orlando','pollen','brine','hail','convertible','bill of lading','fmcsa','winch'],
}, BODY, FAQ)
