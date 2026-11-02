import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('St. Paul, Minnesota','Car shipping in the capital on the bluffs, the quieter half of the Twin Cities on 94 and 35E',
 ['Car shipping in St. Paul runs on Interstate 94 and the ring around the Twin Cities. Ship Guy is a licensed auto transport broker with an office on Minnesota Street downtown.',
  'We book vetted carriers across Saint Paul and the east metro, from Highland Park to Roseville and Woodbury. The carriers own the trucks. Ship Guy holds the license and the bond.',
  'Interstate 94 crosses the city from Minneapolis through downtown to the Wisconsin line. Interstate 35E runs north and south through downtown. Its south half is a parkway that bans heavy trucks. Interstate 494 and 694 ring the metro, and US 52 runs south over the Lafayette Bridge to Rochester.',
  'This page covers 94, 35E, the ring, the truck ban, downtown, Summit Hill, the Midway, and the suburbs. It also covers the state workforce, the headquarters, the campuses, the fair, the snow emergencies, and the lanes.'],
 'St. Paul at a glance',
 ['Most pickups happen within 1 to 3 days. The Chicago and Fargo carriers run 94 through the city every day. The Iowa trucks come up 35.',
  'Rochester, Duluth, Fargo, and Des Moines are same-day runs. Milwaukee, Omaha, Chicago, and Kansas City need a day. Denver needs two, and Phoenix and Florida need three to four.'],
 'Tell us the neighborhood and whether the street is a snow route. Summit Hill, Cathedral Hill, the West Side, and downtown meet the truck at a lot. Highland Park, Como, Roseville, Maplewood, and Woodbury usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 94, Interstate 35E, the 494 and 694 Ring, US 52, Highway 36, Snelling, and University Avenue',
 prose(
  L('St. Paul sits on the east side of the metro. A carrier reaches every suburb from the ring without touching the hills.'),
  P('Interstate 94 is the Chicago-to-Fargo road. It runs from Minneapolis through the Midway and downtown to Hudson, Wisconsin. The downtown stretch backs up both rush hours. Interstate 35E comes down from the north suburbs through downtown and the West Seventh neighborhood. South of downtown it is a parkway with a 45 limit. Trucks over four and a half tons are banned. A loaded carrier cannot use it. The carriers come around on 494 or stay on 94.'),
  P('Interstate 494 and 694 form the ring, from the airport around the east metro to Maplewood and Roseville. US 52 leaves downtown over the Lafayette Bridge and runs south to Rochester. Highway 36 crosses the north suburbs from Roseville to Stillwater. Highway 5 is West Seventh, the road to the airport. Snelling Avenue runs north and south through the Midway, and University Avenue carries the light rail to Minneapolis.'),
  P('The carriers come off 94 at Snelling and off 694 at White Bear Avenue. The big-box lots in the Midway at Snelling and University are the usual meeting spot. The Rosedale lots in Roseville and the Maplewood Mall lots on 694 work too. So do the Woodbury centers on 94. The fairgrounds lots work outside the twelve days of the fair.'),
  P('Our office is on Minnesota Street downtown, between Rice Park and the Capitol.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, Lowertown, Summit Hill, Cathedral Hill, Mac-Groveland, Highland Park, the Midway, Como, the East Side, the West Side, and the East Metro',
 prose(
  L('St. Paul is a city of hills, brick, and narrow residential streets, with wide suburbs on every side. The truck meets the old city at the edge.'),
  P('Downtown sits on the bluff above the river, with the Capitol on the hill behind it. Lowertown is the old warehouse district turned lofts, with the ballpark and the farmers market. The streets are tight and the ramps are everywhere. The driver meets you at the lots on Kellogg Boulevard or by the ballpark. The West Side across the river is a flat grid of small houses. The handoff moves to Robert Street.'),
  P('Summit Hill and Cathedral Hill are the Victorian blocks along Summit Avenue, narrow streets parked on both sides. A seventy-five-foot trailer does not stop there. The driver meets you on Grand Avenue or at the lots by the cathedral. Mac-Groveland and Merriam Park are the college blocks west of there, with the same answer. Highland Park has wider streets and the new neighborhood on the old Ford plant. The curb usually works.'),
  P('The Midway along University Avenue is the soccer stadium, the rail line, old blocks, and big-box lots. The handoff happens at the lots. Hamline-Midway and Frogtown north of it are small houses on narrow streets. Como around the lake and the zoo is wider, and the curb works. The East Side, from Payne-Phalen to Dayton’s Bluff and Battle Creek, is a grid of older houses. The handoff moves to the shopping centers.'),
  P('The east metro is wide. Roseville, Maplewood, and Shoreview to the north are postwar grids and subdivisions, and the driver reaches the house. Woodbury, Oakdale, and Cottage Grove to the east are the newest and widest. Eagan, Mendota Heights, West St. Paul, and Inver Grove Heights to the south are the same. Stillwater sits on the river, and Hudson across the bridge in Wisconsin ships with the same trucks. All of them price the same as St. Paul, and so does Minneapolis.'),
 )))

ROUTES=[("Rochester, MN","US-52 · ~80 mi","Same day","$160–$260"),("Duluth, MN","I-35 · ~150 mi","Same day","$200–$310"),
 ("Fargo, ND","I-94 · ~240 mi","Same day","$250–$380"),("Des Moines, IA","I-35 · ~245 mi","Same day","$250–$380"),
 ("Milwaukee, WI","I-94 · ~330 mi","1 day","$320–$460"),("Omaha, NE","I-35/I-80 · ~380 mi","1 day","$340–$490"),
 ("Chicago, IL","I-94 · ~400 mi","1 day","$340–$490"),("Kansas City, MO","I-35 · ~440 mi","1 day","$380–$540"),
 ("Denver, CO","I-35/I-80 · ~915 mi","2 days","$650–$900"),("Phoenix, AZ","I-35/I-70/I-40 · ~1,650 mi","3–4 days","$950–$1,350")]
BODY.append(rate_table('Lanes &amp; Costs','St. Paul Car Shipping Lanes and Estimated Costs',
 'The lanes east-metro cars run most, with estimated open-trailer ranges. Your own route gets a number on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from St. Paul for a running sedan on an open trailer. SUVs and pickups cost about 10 to 25 percent more, and enclosed costs more still. The season and the carriers free on your dates set the real quote.',
 prose(
  P('St. Paul prices with Minneapolis on every lane, because the carriers are the same trucks ten miles west. The Chicago lane rides 94 the whole way and fills every day. The Iowa and Kansas City lanes ride 35 straight south. The Arizona and Florida lanes fill each fall with snowbirds. The price runs higher in October than in June.'),
  P('A September move-in or a January start date lands in the busiest weeks of the year. Vehicle size, condition, and the other factors are explained in the <a href="car-shipping-cost.html">cost guide</a>.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The State Workforce, the Headquarters, the Hospitals, the Colleges, and the Snowbirds',
 prose(
  L('St. Paul relocates state employees, chemists, insurance staff, nurses, and students. The state and the headquarters move the most.'),
  P('The state government fills the Capitol complex, and its agencies transfer staff on start dates all year. A new governor brings an appointee class to town every fourth January. The county and the city add their own transfers. Reimbursed by an employer? We supply the receipts the package needs.'),
  P('The headquarters move people every week. The water and hygiene company downtown and the insurer on Robert Street relocate staff on offer dates. The tape and adhesives company in Maplewood moves engineers the same way. The brewery and the food companies in the east metro do the same. The second car usually rides a trailer. The hospitals downtown and in Maplewood hire traveling nurses year round, and residents arrive each June.'),
  P('The campuses take cars each September and send them home each May. The university on Summit and the colleges along Snelling and Grand do it. So does the campus on Dayton’s Bluff. The parent handles the booking by phone, and any adult can sign at the lot. Campus streets are tight, so the meeting point is the Midway or Grand Avenue.'),
  P('Retirees leave for Arizona and Florida each fall and come back in May. Families moving between the two downtowns ship one car and drive the other. The Guard units at the airport and the Arden Hills post rotate staff on orders. Ship Guy is a private broker with no tie to them. Orders and their timing are covered on the <a href="military-car-shipping.html">military</a> page. Crossing state lines is covered on the <a href="state-to-state-car-shipping.html">state-to-state</a> page.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The State Fair, the Winter Carnival, Hockey Nights, the Marathon, the Snow Emergencies, and the River',
 prose(
  L('St. Paul runs on a fair calendar and a hockey calendar. The snow emergencies decide where a car can sit.'),
  P('The State Fair fills the fairgrounds for the twelve days ending on Labor Day. Two million people come. Snelling, Como, and Larpenteur jam from morning to midnight. A handoff anywhere near the fairgrounds moves to the week after. The Winter Carnival fills downtown and Rice Park for ten days in late January. The ice palace years close whole blocks.'),
  P('The arena downtown fills the ramps on hockey nights from October through April. The ballpark in Lowertown fills them on summer game nights. The soccer stadium in the Midway fills the Snelling lots on match days. The marathon closes Summit Avenue and the Capitol blocks on the first Sunday of October. Grand Old Day closes Grand Avenue for a Sunday in June. A handoff near any of them moves to the next morning.'),
  P('Winter brings fifty inches of snow and a month of nights below zero. A snow emergency puts the plows on the night routes first and the day routes next. A car on the wrong side gets towed. The driver knows the routes, and we tell you which side to park on. The April 2018 blizzard dropped fifteen inches and closed the airport. The carriers wait in Hudson or Rochester until the plows finish. A winter pickup can lose a day.'),
  P('The Mississippi rises with the spring melt. Shepard Road, Water Street, and Harriet Island closed for weeks in 2019 and again in 2023. A pickup on the river flats moves up the bluff until the water drops. Summer brings heat and the odd tornado warning. Neither shifts more than the loading hour.'),
 )+chips(["Downtown","Lowertown","Capitol","Rice Park","West Seventh","Summit Hill","Cathedral Hill","Summit Avenue","Grand Avenue","Mac-Groveland","Merriam Park","Highland Park","Highland Bridge","Midway","University Avenue","Snelling","Hamline-Midway","Frogtown","Como","Saint Anthony Park","North End","Payne-Phalen","Dayton's Bluff","Battle Creek","West Side","Roseville","Maplewood","Shoreview","White Bear Lake","Woodbury","Oakdale","Cottage Grove","Eagan","Mendota Heights","West St. Paul","Inver Grove Heights","Stillwater","Hudson"])
 +NOTE('Serving St. Paul and the whole east metro, Summit Avenue block or Woodbury cul-de-sac. Tell us the neighborhood and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in St. Paul?',
 prose(
  L('Nearly every east-metro car rides an open trailer, and the lane table above is priced that way.'),
  P('An enclosed trailer keeps off five months of road salt and brine. The collectors on Summit Avenue and the executives relocating a new car to the headquarters book one. A car leaving for Arizona ahead of the first snow emergency often rides enclosed too.'),
  P('A commuter sedan or a student car is a natural fit for the open trailer. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain the difference.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A number, a lot in the Midway or at Rosedale, and a signature at delivery. The start date or move-in day picks the week.'),
  P('Approve the price, and a carrier already running 94 through the city is booked. The meeting lot and the window are confirmed that day. The driver photographs the car and logs its condition on the Bill of Lading with you watching. That log is the reference at delivery.'),
 )+ULI([
  "Clear out the glovebox, the console, and the trunk",
  "A quarter tank is plenty",
  "Take your own photos of the car and the mileage that morning",
  "Hand over a working key and mention anything that sticks or leaks",
  "Disable any add-on alarm",
  "On Summit Hill, in Lowertown, or on the West Side, plan on a lot",
 ])+prose(P('The sequence is on the <a href="how-it-works.html">how it works</a> page, and the checklist is on the <a href="car-shipping-preparation.html">preparation</a> page.'))))

BODY.append(sec('Why Ship Guy','Why St. Paul Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already run 94 and the ring every day. We know which side of the street the plows want.'),
  P('Look us up on the federal register and you will find the FMCSA license and the $75,000 bond. The office is on Minnesota Street downtown.'),
  P('The coordinator who quotes the move answers the phone until the car is delivered. The <a href="services.html">services</a> page puts open, enclosed, and expedited next to each other.'),
 )))

BODY.append(office('St. Paul','428 Minnesota St Unit 369','St. Paul, MN 55101','+16515381308','(651) 538-1308','CT',
 '428+Minnesota+St+Unit+369,+St+Paul,+MN+55101','Visit Us','Find Ship Guy in St. Paul',
 'Our office is on Minnesota Street downtown, between Rice Park and the Capitol.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3485.569103873132!2d-93.0935269!3d44.948705499999996!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x87f7d5f59ecc58a9%3A0xbd43c1351a2421aa!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793288210686!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from St. Paul to Chicago or Arizona?","Chicago runs three hundred forty to four hundred ninety dollars for a sedan. That is about four hundred miles down 94. Phoenix runs nine hundred fifty to thirteen hundred fifty, about sixteen hundred fifty miles. Rochester and Duluth are a short hop and the cheapest lanes of all. Larger vehicles add 10 to 25 percent."),
 ("Can the carrier come to my street on Summit Hill or downtown?","No. Summit Hill and Cathedral Hill are narrow Victorian blocks parked on both sides. Downtown is ramps and one-way streets. The driver meets you on Grand Avenue, by the cathedral, or at the Kellogg Boulevard lots. Highland Park, Como, Roseville, Maplewood, and Woodbury usually allow the curb."),
 ("Why does the carrier avoid 35E through the city?","Because the south half of 35E is a parkway with a 45 limit. It bans trucks over four and a half tons. A loaded car carrier cannot legally use it. The driver comes around on 494 or stays on 94. That adds a few minutes and nothing to the price."),
 ("Do you ship cars for state employees and the headquarters?","Yes, every week. The agencies transfer staff on start dates all year. A new governor brings an appointee class every fourth January. The water and hygiene company, the insurer, and the tape company in Maplewood relocate staff on offer dates. The second car usually rides a trailer. If an employer is reimbursing you, we supply the receipts."),
 ("Can you deliver on a St. Thomas, Macalester, or Hamline move-in date?","Yes. Cars arrive on the campuses each September and leave each May. The parent handles the booking by phone, and any adult can sign at the lot. Campus streets are jammed that week, so the meeting point is the Midway or Grand Avenue. The window follows the date."),
 ("Can you ship a car to or from Woodbury, Roseville, or Minneapolis?","Yes, and all three price the same as St. Paul. Woodbury rides the same carriers off 94 at Radio Drive, and the curb works. Roseville rides them off 36 at Snelling. Minneapolis rides them ten miles west on 94, and its narrow blocks meet the truck at a lot. Send the full address for a suburb."),
 ("What happens if a snow emergency is declared on my pickup day?","The driver follows the plow routes. Night routes are plowed first and day routes next, and a car on the wrong side gets towed. We tell you which side to park on before the truck comes. A big storm keeps the carriers in Hudson or Rochester for a day. You hear it from us first."),
 ("Does the State Fair affect my pickup?","Yes, if the address is anywhere near the fairgrounds. Two million people come in twelve days, and Snelling, Como, and Larpenteur jam from morning to midnight. A handoff in that corner of the city moves to the week after Labor Day. The rest of the metro barely notices."),
 ("Can you ship a car that does not run from St. Paul?","Yes. The quote includes a winch truck and the extra loading time, so nothing is added later. The Midway lots or the Rosedale lots give the driver level ground. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a St. Paul car shipping quote?","Where it sits and where it goes, with the neighborhood or the suburb. The year, make, and model. Whether it drives. Open or enclosed. Your week. Those five, and the St. Paul price is in your inbox the same day."),
]
BODY.append(faq_section(FAQ,'St. Paul FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in St. Paul?','The form above takes two minutes and comes back with a price. Name the neighborhood and the week, and a carrier already on 94 does the rest.','+16515381308','(651) 538-1308','Get your free St. Paul quote'))

build({
 'slug':'auto-transport-st-paul-minnesota',
 'title':'Car Shipping in St. Paul, MN — Auto Transport | Ship Guy',
 'meta':'Car shipping in St. Paul, MN, the capital on the bluffs and the east half of the Twin Cities on 94 and the 494 ring. State and headquarters relocations, college move-in timing, the 35E truck ban, lot handoffs for Summit Hill and downtown, curbside pickups in Highland Park, Roseville, and Woodbury, the State Fair, the snow emergencies, and the river. Local office on Minnesota Street downtown. Free quote.',
 'h1':'Car Shipping in<br>St. Paul, <span class="accent">Minnesota</span>',
 'lede':'Open, enclosed, and expedited auto transport across the east metro, planned around 94, the ring, the truck ban on 35E, the campus calendar, and the snow emergencies.',
 'tel':'+16515381308','disp':'(651) 538-1308','brand':'St. Paul','keyword':'car shipping in st. paul',
 'localterms':['st. paul','capital','bluffs','twin cities','interstate 94','35e','494','694','minnesota street','downtown','saint paul','east metro','highland park','east side','roseville','woodbury','minneapolis','wisconsin line','parkway','heavy trucks','us 52','lafayette bridge','rochester','truck ban','summit hill','midway','highland','suburbs','state workforce','headquarters','campuses','state fair','snow emergencies','chicago','fargo','iowa','duluth','des moines','milwaukee','omaha','kansas city','denver','phoenix','florida','snow route','cathedral hill','west side','como','maplewood','hudson','rush hours','west seventh','45 limit','four and a half tons','airport','highway 36','stillwater','highway 5','snelling avenue','university avenue','light rail','white bear avenue','big-box','rosedale','maplewood mall','fairgrounds','rice park','lowertown','lofts','ballpark','farmers market','ramps','kellogg boulevard','robert street','victorian','summit avenue','grand avenue','cathedral','mac-groveland','merriam park','ford plant','soccer stadium','hamline-midway','frogtown','zoo','payne-phalen','dayton','battle creek','shoreview','oakdale','cottage grove','eagan','mendota heights','west st. paul','inver grove heights','snowbirds','move-in','january','appointee','chemists','water and hygiene','insurer','tape and adhesives','brewery','food companies','traveling nurses','residents','arden hills','guard','arizona','winter carnival','ice palace','hockey nights','game nights','match days','marathon','grand old day','fifty inches','below zero','night routes','day routes','towed','april 2018','fifteen inches','spring melt','shepard road','water street','harriet island','2019','2023','tornado','road salt','brine','bill of lading','fmcsa','saint anthony park','north end','white bear lake','radio drive','larpenteur','labor day'],
}, BODY, FAQ)
