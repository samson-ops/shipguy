import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Minneapolis, Minnesota','Car shipping in the city of lakes, where the skyways keep winter out and the snow emergencies move every car on the street',
 ['Car shipping in Minneapolis runs on Interstate 94 and 35W, which cross downtown and leave in four directions. Ship Guy is a licensed auto transport broker with an office on 4th Street downtown.',
  'We book vetted carriers across Minneapolis, from Northeast to Linden Hills and out to Maple Grove. The trucks belong to the carriers, and the license and the bond belong to us.',
  'Interstate 94 crosses from St. Paul, passes under Lowry Hill, and runs north and west. Interstate 35W runs north and south through the city on the bridge rebuilt in 2008. Interstate 394 runs west to the lakes. Hiawatha, the Crosstown, and Highway 100 carry the rest.',
  'This page covers 94, 35W, 394, Hiawatha, downtown, Northeast, Uptown, the lakes, and the grids. It also covers the headquarters, the hospitals, the campus, the state fair, the snow emergencies, and the cold.'],
 'Minneapolis at a glance',
 ['A Minneapolis pickup usually lands within 1 to 3 days. The Twin Cities pool is the largest between Chicago and Seattle. The 94 carriers pass between Chicago and Fargo all day. The 35 trucks run Duluth to Kansas City.',
  'Rochester, Duluth, Fargo, and Des Moines ride a single day on the truck. Milwaukee, Omaha, and Chicago take a day. Kansas City takes one to two, and Denver takes two.'],
 'Tell us the neighborhood. Downtown, Uptown, the lake parkways, and the campus blocks meet the truck on a main road. The south grids, Northeast, the Southwest subdivisions, and the suburbs usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 94, Interstate 35W, Interstate 394, Highway 55, Highway 62, Highway 100, Hennepin Avenue, Lake Street, and the Skyways',
 prose(
  L('Minneapolis is a grid cut by a river, three freeways, and a chain of lakes. A carrier picks its exit and stays off the parkways.'),
  P('Interstate 94 comes across the river from St. Paul and passes under Lowry Hill in the tunnel. It runs north through the city to Brooklyn Center and Fargo. Interstate 35W runs north and south through the middle. It crosses the river on the bridge that fell in 2007 and was rebuilt in a year. It splits from 35E south of the cities and rejoins it north of them. Interstate 394 runs west from downtown to the lakes and Wayzata. The 494 and 694 loops ring the whole metro.'),
  P('Highway 55 is Hiawatha Avenue, south to the airport along the light rail. Highway 62 is the Crosstown across the south side. Highway 100 runs the west side, and 169 runs farther out. Hennepin Avenue runs from Northeast through downtown to Uptown and the lakes. Lake Street crosses the south side from the river to the lakes. Nicollet Mall is buses and bikes only, and the skyways carry downtown above the street for nine miles.'),
  P('The carriers come off 94 at Lyndale or Broadway and off 35W at Lake Street or Washington. The big-box lots on Lake Street are the usual meeting spot. The lots at the stadium work outside a game. So do the lots in the North Loop and the shopping center lots on Hiawatha. The airport cell lot is fifteen minutes south for a fly-and-ship.'),
  P('Our office is on 4th Street downtown in the Grain Exchange block, a block from the Government Center.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the North Loop, Northeast, North Minneapolis, Uptown, the Lakes, the South Grids, Southwest, Dinkytown, Cedar-Riverside, and the Suburbs',
 prose(
  L('Minneapolis is a dense core, a ring of old grids with alleys, and suburbs in every direction. The truck meets the core on a main road and the grids at the curb.'),
  P('Downtown runs from the river to Loring Park, towers and one-way streets and the skyways above them. The driver meets you at a garage entrance on Washington or at the stadium lots. The North Loop is old warehouses turned lofts on short blocks, and the handoff happens on Washington. Northeast across the river is the old immigrant grid with alleys and breweries. The curb works on most of it. North Minneapolis across 94 is the same grid, and the curb usually works.'),
  P('Uptown around Hennepin and Lake is dense apartments with cars on both curbs. The handoff moves to Lake Street. The streets around the lakes from Kenwood to Linden Hills are parkways and winding lanes. A trailer does not use them. The driver meets you on Hennepin or Lake. The south grids from Whittier and Phillips to Longfellow and Nokomis are the city’s bulk, bungalows with alleys. The curb works until a snow emergency.'),
  P('Southwest from Fulton to Tangletown is wider, and the truck reaches the curb. Dinkytown and the campus blocks are student cars on tight streets. The handoff moves to the lots on University Avenue. Cedar-Riverside is towers on one-way streets, and the handoff happens on Cedar. Edina, St. Louis Park, Richfield, and Golden Valley allow the curb nearly everywhere.'),
  P('St. Paul, Bloomington, and the first-ring suburbs ship with the same trucks and price the same as Minneapolis. So do Maple Grove, Plymouth, and Eden Prairie farther out. St. Cloud is an hour up 94 and adds a few hours.'),
 )))

ROUTES=[("Rochester, MN","US-52 · ~85 mi","Same day","$160–$260"),("Duluth, MN","I-35 · ~150 mi","Same day","$200–$310"),
 ("Fargo, ND","I-94 · ~240 mi","Same day","$250–$380"),("Des Moines, IA","I-35 · ~245 mi","Same day","$250–$380"),
 ("Milwaukee, WI","I-94 · ~340 mi","1 day","$320–$460"),("Omaha, NE","I-35/I-80 · ~380 mi","1 day","$340–$490"),
 ("Chicago, IL","I-94 · ~410 mi","1 day","$340–$490"),("Kansas City, MO","I-35 · ~440 mi","1–2 days","$380–$540"),
 ("Denver, CO","I-35/I-80 · ~915 mi","2 days","$650–$900"),("Phoenix, AZ","I-35/I-70/I-40 · ~1,650 mi","3–4 days","$950–$1,350")]
BODY.append(rate_table('Lanes &amp; Costs','Minneapolis Car Shipping Lanes and Estimated Costs',
 'The ten lanes Hennepin County cars ride most often, with open-trailer estimates. Your own lane prices on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Minneapolis, running sedan, open trailer. An SUV or a pickup adds 10 to 25 percent, and enclosed adds more. Your week and the carriers on 94 that week decide the final figure.',
 prose(
  P('Minneapolis prices with St. Paul on every lane, because the same pool serves both cities. The Chicago lane rides 94 and fills every day. The Fargo lane rides 94 the other way. The Kansas City and Texas lanes ride 35 south. The Arizona and Florida lanes fill each October with the snowbirds, and the price rises with them.'),
  P('A January start date at a headquarters or the late August move-in means a busy week. What size, condition, and timing each do to the figure is on the <a href="car-shipping-cost.html">cost guide</a>.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Headquarters, the Hospitals, the University, the Guard Wing, the Veterans Hospital, the Mills, and the Snowbirds',
 prose(
  L('Minneapolis relocates executives, engineers, nurses, professors, airmen, and students. The headquarters move the most.'),
  P('The city holds more large headquarters per capita than almost any in the country. The retailer on Nicollet, the bank towers, the medical device makers, and the food companies all relocate employees. The start dates bring them from across the country. The packages usually pay for a car, and the paperwork comes from us. The handoff happens at a garage entrance downtown or at the Lake Street lots.'),
  P('The county hospital downtown, the hospital in Phillips, and the university medical center bring residents each June. They hire traveling nurses year round. The veterans hospital by the airport does the same. The university on both banks of the river takes fifty thousand students. The cars arrive in late August. A parent books it, and an adult signs at the lots on University Avenue. The cars leave in May.'),
  P('The Guard’s airlift wing at the airport rotates airmen on orders. The handoff happens at the cell lot or outside the gate. Ship Guy is a private company and has no connection to the Guard. How orders drive the timing is on the <a href="military-car-shipping.html">military</a> page.'),
  P('Retirees leave for Arizona and Florida each October and come back in April. The lane is the busiest long lane out of the state. The paperwork for a state line is on the <a href="state-to-state-car-shipping.html">state-to-state</a> page.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The State Fair, Aquatennial, the Marathon, Move-In Week, Vikings Sundays, the Snow Emergencies, the Cold, the Blizzards, and the Tornadoes',
 prose(
  L('Minneapolis runs on a corporate calendar and a lake calendar. The weather problem is a winter the city has written parking rules for.'),
  P('The state fair fills Falcon Heights for twelve days through Labor Day. It takes Snelling and 94 with it. Aquatennial fills the riverfront in July. The marathon closes the parkways and the river road on the first Sunday in October. Move-in week in late August fills Dinkytown and the East Bank. Vikings Sundays close the blocks around the stadium. Book three weeks ahead for a date in the last week of August.'),
  P('A snow emergency bans parking on one side of every street for three days. The cars that stay get towed. A trailer that cannot stop on the block loses it, and the handoff moves to a lot. The Halloween blizzard in 1991 dropped twenty-eight inches, and the April 2018 storm dropped fifteen. The January 2019 cold held the city at twenty-eight below. A carrier does not load a car at that temperature, and the day moves. The carriers wait in the suburbs until the plows finish.'),
  P('The May 2011 tornado crossed North Minneapolis and took roofs for miles. A tornado watch holds the truck at the lot until it lifts, and we call before it does. The December 2010 storm dropped seventeen inches and collapsed the stadium roof of the time. The river crests in April some years and closes the low roads by the mills.'),
  P('Summer brings heat, humidity, and afternoon storms with hail. A carrier does not load under a hail warning. The storms clear by evening, and the lakes draw the whole city out.'),
 )+chips(["Downtown","The North Loop","The Mill District","Loring Park","Elliot Park","Northeast","St. Anthony","North Minneapolis","Camden","Bryn Mawr","Uptown","Lowry Hill","Kenwood","Linden Hills","Fulton","Tangletown","Whittier","Phillips","Powderhorn","Longfellow","Nokomis","Seward","Cedar-Riverside","Dinkytown","Marcy-Holmes","Prospect Park","Edina","St. Louis Park","Richfield","Golden Valley"])
 +NOTE('Serving Minneapolis and the whole west metro, Lowry Hill lane or Edina cul-de-sac. Give us the neighborhood and say whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Minneapolis?',
 prose(
  L('The metro ships open nine times in ten, and the table above is priced that way.'),
  P('Enclosed keeps the salt, the brine, and the sand the city spreads off the paint. Kenwood collectors book it. So do the executives moving a car worth more than the rest of the package. When a blizzard is coming, the car rides the first truck with room. We tell you that first.'),
  P('A commuter car or a student’s car does fine in the open. The differences are laid out on the <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('First a figure, then a lot on Lake Street, then a signature at the other end. Your start date or move-in picks the week.'),
  P('Approve the figure, and the car goes to a carrier already on 94 that week. The lot and the window get fixed before the day is out. At pickup the driver photographs the car and records its condition on the Bill of Lading. Your initials go on that sheet, and delivery is checked against it.'),
 )+ULI([
  "Nothing personal left in the cabin or the trunk",
  "No more than a quarter tank of fuel",
  "Photos of every side and the odometer the morning of pickup",
  "A working key plus a note on anything that acts up",
  "Aftermarket alarms disabled",
  "Downtown, in Uptown, or on a lake parkway, expect a main road or a garage entrance",
 ])+prose(P('The order of events is on the <a href="how-it-works.html">how it works</a> page. Pickup day is on the <a href="car-shipping-preparation.html">preparation</a> page.'))))

BODY.append(sec('Why Ship Guy','Why Minneapolis Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already run 94 every day. We know which side of the street a snow emergency clears and when.'),
  P('Our FMCSA license and our $75,000 bond sit on the federal register for anyone to check. The office is on 4th Street downtown.'),
  P('The same coordinator handles your move from the quote through the delivery call. Open, enclosed, and expedited are compared on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Minneapolis','400 S 4th St Ste 574','Minneapolis, MN 55415','+17633142219','(763) 314-2219','CT',
 '400+S+4th+St+Ste+574,+Minneapolis,+MN+55415','Visit Us','Find Ship Guy in Minneapolis',
 'Our office is on 4th Street downtown in the Grain Exchange block, a block from the Government Center.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3483.8128395711233!2d-93.2636967!3d44.977619399999995!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x52b333471d9a9841%3A0xe78a7d2c0043f2dc!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793629306288!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Minneapolis to Chicago or Arizona?","Chicago runs three hundred forty to four hundred ninety dollars for a sedan. That is about four hundred ten miles down 94. Phoenix runs nine hundred fifty to thirteen hundred fifty, about sixteen hundred fifty miles. Rochester is the lowest lane on the table, ninety minutes down 52. Add 10 to 25 percent for an SUV or a pickup."),
 ("Do you work with corporate relocation packages?","Yes, every week of the year. The headquarters downtown and in the western suburbs relocate employees on start dates. The packages usually pay for a car. We plan the pickup around the first day on the job and produce whatever paperwork the package wants. The handoff happens at a garage entrance downtown or at the Lake Street lots."),
 ("Can the carrier come to my street in Uptown or around the lakes?","No. Uptown is dense apartments with cars on both curbs, and the lake streets are parkways and winding lanes. The driver meets you on Hennepin or Lake Street. The south grids, Northeast, Southwest, and the suburbs usually allow the curb outside a snow emergency."),
 ("What does a snow emergency do to my pickup?","It moves it to a lot. The city bans parking on one side of every street for three days after a big snow. The cars that stay get towed. A trailer cannot stop on a block it cannot park on. We meet at the Lake Street lots or a garage entrance until the emergency ends. The figure does not change."),
 ("Can you deliver on a University of Minnesota move-in date?","Yes. Cars arrive in late August and leave in May. A parent books, and anyone over eighteen can sign at the lot. Dinkytown and the East Bank are full that week. The meeting point is the lots on University Avenue. The window follows the date."),
 ("Do you ship cars for the hospitals?","Yes, in every season. The county hospital, the one in Phillips, the university hospital, and the veterans hospital bring residents each June. Traveling nurses come all year. The handoff happens at a garage entrance or on Hiawatha. When the employer reimburses the move, we produce the paperwork it asks for."),
 ("Can you ship a car to or from St. Paul, Edina, or St. Cloud?","Yes. St. Paul, Edina, St. Louis Park, and Richfield ride the same carriers and price the same as Minneapolis. Maple Grove, Plymouth, and Eden Prairie do too. St. Cloud is an hour up 94 and adds a few hours on the day."),
 ("What happens if a blizzard or the cold hits on my pickup day?","The truck waits in the suburbs until the plows finish, usually a day. A carrier does not load a car at twenty below, because the straps stiffen and the hydraulics slow. You hear from us the moment the forecast turns. The pickup slides to the first workable morning at the same figure."),
 ("Can you ship a car that does not run from Minneapolis?","Yes. A winch truck comes, and the figure already includes the loading time. The big-box lots on Lake Street and the stadium lots are flat. We need to know whether it rolls, steers, and brakes."),
 ("What do you need for a Minneapolis car shipping quote?","Start and end, down to the neighborhood. Year, make, and model, and whether it runs. Open or enclosed, and the week around the start date or the move. With those four, the Minneapolis figure is back the same day."),
]
BODY.append(faq_section(FAQ,'Minneapolis FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Minneapolis?','Two minutes on the form above puts a Minneapolis figure on your lane. Give us the neighborhood and the week, and a carrier already on 94 takes the car.','+17633142219','(763) 314-2219','Get your free Minneapolis quote'))

build({
 'slug':'auto-transport-minneapolis-minnesota',
 'title':'Car Shipping in Minneapolis, MN — Auto Transport | Ship Guy',
 'meta':'Car shipping in Minneapolis, MN, the city of lakes on 94 and 35W. Corporate relocation packages, hospital and campus moves, the Guard wing at the airport, main-road handoffs for downtown, Uptown, and the lake parkways, curbside pickups in the grids and the suburbs, the snow emergencies, and the cold. Local office on 4th Street downtown. Free quote.',
 'h1':'Car Shipping in<br>Minneapolis, <span class="accent">Minnesota</span>',
 'lede':'Open, enclosed, and expedited auto transport across Minneapolis and the west metro, planned around 94, 35W, the corporate calendar, the campus dates, the snow emergencies, and the cold.',
 'tel':'+17633142219','disp':'(763) 314-2219','brand':'Minneapolis','keyword':'car shipping in minneapolis',
 'localterms':['minneapolis','lakes','skyways','snow emergencies','interstate 94','35w','394','hiawatha','crosstown','highway 100','169','494','694','hennepin','lake street','nicollet mall','lowry hill','tunnel','bridge','2007','rebuilt','4th street','grain exchange','government center','stadium','downtown','north loop','mill district','loring park','northeast','north minneapolis','uptown','kenwood','linden hills','fulton','tangletown','whittier','phillips','longfellow','nokomis','dinkytown','east bank','cedar-riverside','university avenue','washington','lyndale','broadway','edina','st. louis park','richfield','golden valley','maple grove','plymouth','eden prairie','st. paul','bloomington','st. cloud','rochester','duluth','fargo','des moines','milwaukee','omaha','chicago','kansas city','denver','phoenix','arizona','florida','snowbirds','headquarters','retailer','bank towers','medical device','food companies','executives','engineers','county hospital','medical center','residents','traveling nurses','veterans hospital','university','fifty thousand','students','guard','airlift wing','airmen','orders','retirees','state fair','falcon heights','snelling','aquatennial','marathon','parkways','move-in','vikings','halloween blizzard','1991','twenty-eight inches','april 2018','january 2019','twenty-eight below','may 2011','tornado','december 2010','seventeen inches','roof','hail','salt','brine','sand','bill of lading','fmcsa','winch','alleys','breweries','towed','cell lot','fly-and-ship'],
}, BODY, FAQ)
