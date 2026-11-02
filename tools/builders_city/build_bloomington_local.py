import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Bloomington, Minnesota','Car shipping on the 494 strip, between the airport, the mall, and the river bluffs',
 ['Car shipping in Bloomington runs on Interstate 494, the strip the south metro drives to reach the airport. Ship Guy is a licensed auto transport broker with an office on American Boulevard West at France Avenue.',
  'We book vetted carriers across Bloomington and the south metro, from Normandale to the mall and the river. The carriers own the trucks. Ship Guy holds the license and the bond.',
  'Interstate 494 runs the north edge of the city from the airport west to Eden Prairie. Interstate 35W cuts through the middle on its way from Minneapolis to Iowa. Highway 77 is Cedar Avenue, past the mall and over the river. Highway 100 is Normandale Boulevard, and US 169 is the west edge.',
  'This page covers 494, 35W, Cedar, the mall, the airport, the old grids, the bluffs, and the river. It also covers the headquarters, the airline crews, the parking ban, the holiday crush, and the lanes.'],
 'Bloomington at a glance',
 ['Most pickups happen within 1 to 3 days. The Chicago and Fargo carriers ride 494 around the metro every day. The Iowa trucks come up 35W.',
  'Rochester, Duluth, Des Moines, and Fargo ride a single day on the truck. Milwaukee, Omaha, Chicago, and Kansas City take a day. Denver takes two, and Arizona and Florida take three to four.'],
 'Tell us the neighborhood and whether the street has been plowed. The bluffs, the Normandale cul-de-sacs, and the apartment towers on the strip meet the truck at a lot. East Bloomington, Oxboro, Richfield, Edina, and Burnsville usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 494, Interstate 35W, Cedar Avenue, Normandale Boulevard, US 169, Lyndale, France, Old Shakopee Road, and the Bridges',
 prose(
  L('Bloomington is a wide suburb with a freeway on three sides and a river on the fourth. A carrier reaches every block from an exit.'),
  P('Interstate 494 is the south half of the metro ring. It runs from the airport past the mall, the hotels, and the Normandale towers to Eden Prairie. Both rush hours jam the stretch between 35W and 169. Interstate 35W comes down from Minneapolis through the middle of the city and crosses the river to Burnsville. The Iowa and Kansas City carriers ride it. The Chicago and Fargo carriers ride 494 around.'),
  P('Highway 77 is Cedar Avenue. It runs past the mall and the airport, then over the river to Apple Valley and Eagan. Highway 100 is Normandale Boulevard, and it ends at 494 on the west side. US 169 runs the west edge and crosses the river to Shakopee on the Bloomington Ferry Bridge. Lyndale, Penn, and France run north and south through the grids. Old Shakopee Road runs the whole south side along the bluffs. American Boulevard parallels 494 the length of the strip.'),
  P('The carriers come off 494 at Lyndale, Penn, or France and off 35W at 98th. The mall’s surface lots on the east side are the usual meeting spot outside December. The Southtown lots at Penn and 494 and the Oxboro lots at Lyndale and 98th work every day. So do the big-box lots on American Boulevard. The airport cell lot works for a fly-and-ship.'),
  P('Our office is on American Boulevard West at France Avenue, right off 494.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','East Bloomington, Oxboro, the Strip, Normandale, Bush Lake, the Hyland Hills, the Bluffs, and the South Metro',
 prose(
  L('Bloomington is a postwar grid on the east side and lake lots and cul-de-sacs on the west. The truck reaches most of it.'),
  P('East Bloomington between 35W and Cedar is the original suburb, ramblers on wide streets with alleys behind. The curb works on almost every block. Oxboro around Lyndale and 98th is the same, with the old shopping center as a landmark. The blocks nearest the mall and the airport are apartments and hotels. The handoff there moves to the mall lots.'),
  P('The strip along 494 is hotels, office towers, and apartments from Cedar to Normandale. The towers run on garages and loading docks, and a trailer has nowhere to stop. The driver meets you at Southtown or on American Boulevard. The Penn-American district is rebuilding as apartments, and the answer is the same.'),
  P('West Bloomington is Normandale, Bush Lake, and the Hyland hills. The streets curve, the lots are bigger, and the cul-de-sacs dead-end at the lakes. A seventy-five-foot trailer cannot turn around in most of them. The driver meets you on Normandale Boulevard, at the Valley West lots on Old Shakopee, or on 98th. The park reserve and the ski hill close the south end to everything but the park roads.'),
  P('The bluffs from Bloomington Ferry to Old Cedar are steep streets and dead ends above the refuge. The handoff moves up to Old Shakopee Road. Richfield across 494, Edina to the northwest, and Eden Prairie to the west ship with the same trucks. Burnsville, Savage, Apple Valley, and Eagan across the river do too, and the curb usually works. All of them price the same as Bloomington, and so does Minneapolis.'),
 )))

ROUTES=[("Rochester, MN","US-52 · ~80 mi","Same day","$160–$260"),("Duluth, MN","I-35 · ~160 mi","Same day","$200–$310"),
 ("Des Moines, IA","I-35 · ~235 mi","Same day","$250–$380"),("Fargo, ND","I-94 · ~245 mi","Same day","$250–$380"),
 ("Milwaukee, WI","I-94 · ~335 mi","1 day","$320–$460"),("Omaha, NE","I-35/I-80 · ~375 mi","1 day","$340–$490"),
 ("Chicago, IL","I-94 · ~405 mi","1 day","$340–$490"),("Kansas City, MO","I-35 · ~435 mi","1 day","$380–$540"),
 ("Denver, CO","I-35/I-80 · ~910 mi","2 days","$650–$900"),("Phoenix, AZ","I-35/I-70/I-40 · ~1,640 mi","3–4 days","$950–$1,350")]
BODY.append(rate_table('Lanes &amp; Costs','Bloomington Car Shipping Lanes and Estimated Costs',
 'The lanes south-metro cars run most, with estimated open-trailer ranges. Your own route gets a number on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Bloomington for a sedan that runs, on an open trailer. SUVs and pickups run about 10 to 25 percent more, and enclosed runs more still. The week you choose and the trucks free that week settle the real number.',
 prose(
  P('Bloomington prices with Minneapolis and St. Paul on every lane, because the carriers ride 494 past all three. The Chicago lane rides 94 east and fills every day. The Iowa and Kansas City lanes ride 35W straight south from the city. The Arizona and Florida lanes fill each October with snowbirds, and the price rises with them.'),
  P('A move timed to the holiday rush or a January start date lands in a busy week. The <a href="car-shipping-cost.html">cost guide</a> covers what size, condition, and timing do to the price.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Health Plan, the Mower Maker, the Airline Crews, the Mall, the Fab, the Guard Wings, and the Snowbirds',
 prose(
  L('Bloomington relocates nurses, pilots, engineers, retail managers, and retirees. The headquarters on the strip move the most.'),
  P('The health plan headquartered off 494 relocates staff on start dates all year. The mower and irrigation company on Lyndale moves engineers the same way. So do the filter maker, the hair salon franchiser, and the semiconductor fab on Old Shakopee Road. The second car usually rides a trailer. If an employer picks up the cost, the paperwork for the package comes from us.'),
  P('The airport across 494 is a hub for one of the big airlines. Pilots, crews, and mechanics relocate on bid dates all year. The handoff happens in Bloomington rather than at the terminal. The mall employs thousands and moves store managers on opening dates. The community college on the west side takes student cars each August and sends them home in May. The university in Minneapolis does the same in September. A parent books it from home, and an adult meets the truck to sign.'),
  P('Two Guard wings fly out of the airport. The reserve units at Fort Snelling rotate staff on orders. Orders usually cover one vehicle, and the second one ships with us. Ship Guy is a private broker with no connection to any of them. The <a href="military-car-shipping.html">military</a> page explains the timing around orders.'),
  P('The snowbirds head for Arizona and Florida each October and return in April. Families moving across the river to Burnsville or Eagan ship one car and drive the other. Crossing a state line is covered on the <a href="state-to-state-car-shipping.html">state-to-state</a> page.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Holiday Crush, the Airport Weeks, the Summer Fete, the Parking Ban, the Blizzards, and the River',
 prose(
  L('Bloomington runs on a retail calendar and an airport calendar. The parking ban decides where a car can wait for the truck.'),
  P('The mall fills from Black Friday to New Year’s. Cedar, Killebrew, and the 494 ramps crawl every weekend of December. A handoff near the mall moves to a weekday morning or to Southtown. The airport weeks around Thanksgiving and Christmas jam the 494 and Cedar ramps the same way. The Summer Fete fills Normandale Lake Park on the third of July. The fireworks close Normandale Boulevard for the night.'),
  P('Winter brings fifty inches of snow and a month of nights below zero. The city bans street parking after a snowfall until the plow has been through. A car left on the street gets ticketed or towed. We tell you to use the driveway or a lot before the truck comes. The April 2018 blizzard dropped fifteen inches and closed the airport for a day. The carriers wait in Rochester or Hudson until 494 clears, and a winter pickup can lose a day.'),
  P('The Minnesota River rises with the snowmelt in April. The bottoms below the bluffs go under. The crossings to Shakopee and Savage on 101 close for weeks. The Cedar Avenue and 169 bridges stay open. A pickup on the bluffs moves up to Old Shakopee Road until the water drops. Summer brings heat and the occasional tornado warning, and neither moves more than the loading hour.'),
 )+chips(["East Bloomington","Oxboro","Southtown","Penn-American","The Strip","American Boulevard","Mall of America","Airport","Normandale","Normandale Lake","Bush Lake","Hyland Hills","Hyland Lake Park Reserve","Timberglade","Valley West","Bloomington Ferry","Nine Mile Creek","Old Cedar","The Bluffs","Richfield","Edina","Eden Prairie","Burnsville","Savage","Apple Valley","Eagan","Shakopee","Minneapolis"])
 +NOTE('Serving Bloomington and the whole south metro, East Bloomington rambler or Bush Lake cul-de-sac. Tell us the neighborhood and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Bloomington?',
 prose(
  L('Open trailers carry most of the south metro, and the table above is priced for one.'),
  P('An enclosed trailer keeps off five months of salt and brine. The collectors on Bush Lake and the executives relocating a new car to the headquarters book one. A car leaving for Arizona ahead of the first parking ban often rides enclosed too.'),
  P('A daily driver or a student car belongs on an open trailer. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain where enclosed earns its price.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A number, a lot at the mall or Southtown, and a signature at delivery. The start date or the snowbird flight picks the week.'),
  P('Approve the price, and we book a carrier already riding 494 that week. Lot and window are settled the same afternoon. At pickup the driver and you go over the car together. Every mark goes on the Bill of Lading. You countersign, and delivery is checked against it.'),
 )+ULI([
  "Belongings out of the car, including the trunk and the console",
  "Fuel at roughly a quarter tank",
  "Photos of every side and the odometer, taken that morning",
  "A key that works, and a word about anything that sticks",
  "Add-on alarm disabled",
  "On the bluffs, in the Normandale cul-de-sacs, or on the strip, plan on a lot",
 ])+prose(P('The sequence is on the <a href="how-it-works.html">how it works</a> page. The full checklist is on the <a href="car-shipping-preparation.html">preparation</a> page.'))))

BODY.append(sec('Why Ship Guy','Why Bloomington Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already ride 494 and 35W every day. We know when the parking ban is on.'),
  P('Our FMCSA license number and our $75,000 bond are listed on the federal register for anyone to check. The office is on American Boulevard West.'),
  P('One coordinator stays on the move from the quote to the delivery call. The <a href="services.html">services</a> page sets open, enclosed, and expedited side by side.'),
 )))

BODY.append(office('Bloomington','3800 American Blvd W #147','Bloomington, MN 55431','+19522488173','(952) 248-8173','CT',
 '3800+American+Blvd+W+%23147,+Bloomington,+MN+55431','Visit Us','Find Ship Guy in Bloomington',
 'Our office is on American Boulevard West at France Avenue, right off 494.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4319.74058416354!2d-93.32842649999999!3d44.85679689999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x87f625c3ac15c5ab%3A0x2ff001e9ae197c3e!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793300149821!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Bloomington to Chicago or Arizona?","Chicago runs three hundred forty to four hundred ninety dollars for a sedan. That is about four hundred five miles down 94. Phoenix runs nine hundred fifty to thirteen hundred fifty, about sixteen hundred forty miles. Rochester and Duluth are short hops and cost the least. An SUV or a pickup runs 10 to 25 percent higher."),
 ("Can the carrier come to my street in East Bloomington or on Bush Lake?","East Bloomington, yes. The grids between 35W and Cedar are wide, and the curb works on almost every block. Bush Lake and the Normandale cul-de-sacs, usually not. A trailer cannot turn around at the lake. The driver meets you on Normandale Boulevard, at Valley West, or on 98th."),
 ("Do you ship cars for the airline crews and the airport?","Yes, every week. Pilots, crews, and mechanics relocate on bid dates all year. The handoff happens at a lot in Bloomington rather than at the terminal. A fly-and-ship works the same way in reverse. Land, pick up the car at the cell lot, and drive home."),
 ("Do you ship cars for the headquarters on the strip?","Yes. The health plan, the mower maker, the filter maker, and the fab relocate staff all year. The second car usually rides a trailer. If an employer picks up the cost, the paperwork for the package comes from us."),
 ("Does the holiday crush at the mall affect my pickup?","Yes, near the mall. From Black Friday to New Year’s, Cedar, Killebrew, and the 494 ramps crawl every weekend. A handoff in that corner moves to a weekday morning or to Southtown. The rest of Bloomington runs normally."),
 ("Can you ship a car to or from Richfield, Edina, or Burnsville?","Yes, and all three price the same as Bloomington. Richfield rides the same carriers off 494 at Lyndale or Penn, and the curb works. Edina rides them off 100 or 169, and its older blocks meet the truck on a main road. Burnsville rides them over the 35W bridge. Send the full address for a cul-de-sac."),
 ("What happens if the parking ban is on when the truck comes?","The car waits in the driveway or at a lot instead of the street. The city bans street parking after a snowfall until the plow has been through. A car left out gets towed. We tell you before the truck comes. A big storm keeps the carriers in Rochester or Hudson for a day."),
 ("Can you deliver on a Normandale or University of Minnesota move-in date?","Yes. The college takes cars each August, and the university in Minneapolis takes them in September. Both send them home in May. A parent books it from home, and an adult meets the truck to sign. The handoff for the university happens in Bloomington and skips the campus streets."),
 ("Can you ship a car that does not run from Bloomington?","Yes. A carrier with a winch is booked, and the loading time is in the price from the start. The mall’s surface lots or the Southtown lots give the driver level ground. Say whether it rolls, steers, and brakes."),
 ("What do you need for a Bloomington car shipping quote?","Both ends of the move, with the neighborhood or the suburb. The year, make, and model. Whether it runs. Open or enclosed. The week around the start date or the flight. Five answers, and a Bloomington number is back the same day."),
]
BODY.append(faq_section(FAQ,'Bloomington FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Bloomington?','The form above takes two minutes and comes back with a Bloomington number. Tell us the neighborhood and the week, and a carrier already on 494 does the rest.','+19522488173','(952) 248-8173','Get your free Bloomington quote'))

build({
 'slug':'auto-transport-bloomington-minnesota',
 'title':'Car Shipping in Bloomington, MN — Auto Transport | Ship Guy',
 'meta':'Car shipping in Bloomington, MN, on the 494 strip between the airport, the mall, and the river bluffs. Headquarters and airline-crew relocations, the holiday crush at the mall, lot handoffs for the bluffs and the Normandale cul-de-sacs, curbside pickups in East Bloomington, Richfield, Edina, and Burnsville, the parking ban, and the river. Local office on American Boulevard West. Free quote.',
 'h1':'Car Shipping in<br>Bloomington, <span class="accent">Minnesota</span>',
 'lede':'Open, enclosed, and expedited auto transport across the south metro, planned around 494, 35W, the airport, the mall, the parking ban, and the river.',
 'tel':'+19522488173','disp':'(952) 248-8173','brand':'Bloomington','keyword':'car shipping in bloomington',
 'localterms':['bloomington','interstate 494','strip','airport','mall','river bluffs','american boulevard','france avenue','south metro','normandale','interstate 35w','minneapolis','iowa','highway 77','cedar avenue','highway 100','us 169','old grids','bluffs','river','health plan','mower','airline crews','parking ban','holiday crush','chicago','fargo','rochester','duluth','des moines','milwaukee','omaha','kansas city','denver','phoenix','florida','plowed','apartment towers','east bloomington','oxboro','richfield','edina','burnsville','eden prairie','penn','hotels','rush hours','apple valley','eagan','shakopee','bloomington ferry bridge','lyndale','old shakopee road','98th','surface lots','southtown','big-box','cell lot','fly-and-ship','ramblers','alleys','shopping center','garages','loading docks','penn-american','bush lake','hyland hills','cul-de-sacs','valley west','park reserve','ski hill','old cedar','refuge','savage','snowbirds','start dates','irrigation','filter','hair salon','semiconductor','fab','pilots','mechanics','bid dates','store managers','community college','university','guard wings','fort snelling','black friday','killebrew','thanksgiving','christmas','summer fete','normandale lake park','fireworks','fifty inches','below zero','ticketed','towed','april 2018','fifteen inches','hudson','snowmelt','bottoms','101','tornado','salt','brine','bill of lading','fmcsa','nine mile creek','timberglade','hyland lake park reserve','winch','console'],
}, BODY, FAQ)
