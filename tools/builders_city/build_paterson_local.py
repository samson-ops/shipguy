import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Paterson, New Jersey','Car shipping in the Silk City, twenty miles from the George Washington Bridge and a world away from it',
 ['Car shipping in Paterson runs on Interstate 80 along the south side and Route 20 along the river. Ship Guy is a licensed auto transport broker with an office on River Street downtown.',
  'We book vetted carriers across Paterson, from South Paterson to the Eastside and across the river to Hawthorne. The carriers own the trucks. Ship Guy holds the license and the bond.',
  'Interstate 80 runs along the south side with the Squirrelwood, Main Street, and Madison Avenue exits. Route 19 drops off it into downtown. Route 20 runs the river to Route 4 and the bridge. Route 46 runs the south edge to the Parkway and the mall. Route 21 follows the river to Newark.',
  'This page covers 80, 19, 20, 46, Main Street, the Falls district, the Eastside, South Paterson, and Riverside. It also covers the hospital, the warehouses, the Manhattan commute, the floods, and the snow.'],
 'Paterson at a glance',
 ['Most pickups happen within 1 to 3 days. The Newark and Meadowlands pool is fifteen miles south, and the 80 carriers pass the city all day. The Florida trucks load along 46 every week.',
  'Manhattan, Allentown, Philadelphia, and Hartford ride a single day on the truck. Baltimore, Boston, and Washington take a day. Pittsburgh takes one, Chicago takes two, and Florida takes three.'],
 'Tell us the neighborhood. Downtown, the Falls district, South Paterson, and the Riverside blocks meet the truck on a main road. The Eastside, Hillcrest, Lakeview, and the Totowa section usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 80, Route 19, Route 20, Route 46, Route 4, Route 21, Main Street, Market Street, and the Bridges',
 prose(
  L('Paterson is a mill city on a bend in the Passaic with an interstate along its back. A carrier picks its exit and stays off the one-way streets.'),
  P('Interstate 80 runs along the south side from the Willowbrook interchange to the Garden State Parkway. The Squirrelwood exit serves the west side, Main Street serves downtown, and Madison Avenue serves the Eastside. East of the Parkway it reaches the George Washington Bridge in fifteen minutes on a good day. Route 19 leaves 80 and drops into downtown at the Falls. Route 20 is McLean Boulevard, the river road along the east side to Route 4 and Fair Lawn.'),
  P('Route 46 runs the south edge through Clifton and Totowa to the mall at Willowbrook. It continues west to 23 and 287. Route 4 runs east from Route 20 to Paramus and the bridge. Route 21 follows the river south from Clifton to Newark. The Parkway runs north and south three miles east of the city, and a carrier stays off it. Main Street and Market Street cross downtown, both one way and both full. Broadway and Union Avenue carry the rest. Bridges cross the river to Hawthorne, Fair Lawn, and Elmwood Park. All of them back up at five.'),
  P('The carriers come off 80 at Main Street or Madison Avenue. The lots at the shopping center on Route 20 are the usual meeting spot. The big-box lots on Route 46 in Totowa and Clifton work too. So do the mall lots in Wayne and the stadium lot by the Falls outside a game. The airport in Newark is twenty-five minutes down 21 for a fly-and-ship.'),
  P('Our office is on River Street at the east edge of downtown, along the Passaic.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the Falls District, South Paterson, the Eastside, Hillcrest, Lakeview, the Totowa Section, Riverside, the Northside, Bunker Hill, and the Towns Around',
 prose(
  L('Paterson is one of the densest cities in the state, and the streets were laid out for mills. The truck meets most of the city on a main road.'),
  P('Downtown runs from the Falls east along Market and Main. It is the courthouse, the mall, and the bus terminal on Broadway. The driver meets you at the Route 20 lots or on Broadway. The Falls district is the old mills on the raceways, narrow one-way streets of brick on a hillside. A trailer does not enter. The handoff moves to McBride Avenue or the stadium lot. South Paterson along Main Street is the Turkish and Arab district, dense blocks of storefronts and apartments. The handoff happens on Route 46.'),
  P('The Eastside around the park is the old money, big houses on wide streets. The curb works on most of it, and the oaks are the only problem. Hillcrest and the Totowa section on the west side are suburban grids from the fifties. The truck reaches the curb. Lakeview at the south end by the Clifton line is the same. The Peoples Park and Wrigley Park blocks between them are tighter. The driver meets you on Union Avenue or 21st Avenue.'),
  P('Riverside and the Northside along the river are the blocks that flood, two-family houses on short streets. The handoff moves to River Street or Route 20. Bunker Hill at the northeast corner is the warehouse district along the river, and the lots there work. Sandy Hill and the blocks around the hospital are dense, and the driver meets you on Main Street.'),
  P('Clifton, Haledon, Hawthorne, and Prospect Park ship with the same trucks and price the same as Paterson. So do Totowa, Wayne, and Fair Lawn. Passaic and Garfield down the river do too. Newark is fifteen miles south and prices with the city.'),
 )))

ROUTES=[("Manhattan, NY","I-80/I-95 · ~20 mi","Same day","$110–$190"),("Allentown, PA","I-80/I-287/I-78 · ~80 mi","Same day","$160–$260"),
 ("Philadelphia, PA","NJ Tpke · ~110 mi","Same day","$170–$280"),("Hartford, CT","I-287/I-84 · ~120 mi","Same day","$180–$290"),
 ("Baltimore, MD","I-95 · ~175 mi","Same day","$230–$350"),("Boston, MA","I-287/I-84/I-90 · ~220 mi","1 day","$240–$360"),
 ("Washington, DC","I-95 · ~240 mi","1 day","$250–$380"),("Pittsburgh, PA","I-80/I-76 · ~370 mi","1 day","$330–$470"),
 ("Chicago, IL","I-80 · ~780 mi","2 days","$560–$820"),("Orlando, FL","I-95 · ~1,080 mi","3 days","$760–$1,080")]
BODY.append(rate_table('Lanes &amp; Costs','Paterson Car Shipping Lanes and Estimated Costs',
 'The lanes Passaic County cars run most, with estimated open-trailer ranges. Price your own route on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Paterson for a running sedan on an open trailer. SUVs and pickups cost 10 to 25 percent more, and enclosed costs more still. The Turnpike, Parkway, and bridge tolls ride inside the figure where the route uses them. The week and the carriers free on 80 that week set the final figure.',
 prose(
  P('Paterson prices with Newark on every lane, plus a few dollars for the fifteen miles north. The Manhattan lane rides 80 to the bridge and fills every day. The Philadelphia and Washington lanes ride the Turnpike and 95. The Chicago lane rides 80 the whole way, because the interstate starts at the bridge. The Florida lane rides 95 and fills each fall with the retirees and the families going home.'),
  P('A move-in date in late August or the week before Christmas lands in the busiest days. What size, condition, and timing do to the figure is in the <a href="car-shipping-cost.html">cost guide</a>.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Hospital, the Warehouses, the Manhattan Commute, the Immigrant Blocks, the County, the Universities, and the Families Going South',
 prose(
  L('Paterson relocates nurses, warehouse managers, commuters, and families with relatives in three countries. The hospital and the warehouses move the most.'),
  P('The hospital downtown on Main Street is the largest private employer in the county. It brings residents each June and hires traveling nurses year round. The handoff for all of them happens on Route 20. The blocks around the hospital leave no room. The county runs the courthouse and the offices downtown and moves staff on start dates. If the hospital or an employer reimburses the shipment, the paperwork comes from us.'),
  P('The warehouses along 46 and in the Meadowlands move managers on opening dates. Thousands ride the bus from the Broadway terminal to Manhattan every morning. The commuters ship a car when a job moves across the river or down to the Shore. The stadium in the Meadowlands that hosted the World Cup final this summer is ten miles away. The event crews moved in and out through the city.'),
  P('The Dominican and Peruvian blocks downtown ship cars to and from Florida every month. The Turkish and Arab blocks on Main Street do the same. Families send a car to a relative in Orlando or Miami and bring one back. A car that landed at the port in Newark ships like any other once customs clears it. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the paperwork for crossing a state line.'),
  P('The state university in Wayne takes student cars in late August, and the community college downtown follows. The university in Montclair does the same. A parent sets it up, and an adult signs when the truck comes. Retirees leave for Florida each October and come back in April.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Parades, the Falls Festival, Move-In Week, the Holiday Rush, the Floods, the Nor’easters, the Snowbanks, and the Bridge',
 prose(
  L('Paterson runs on a Manhattan calendar and a river calendar. The weather problem is a river that comes up the streets twice a decade.'),
  P('The Peruvian parade closes downtown on a Sunday in July, and the Dominican parade does it in August. The festival at the Falls fills the district over Labor Day weekend. Move-in week in late August fills Wayne and Montclair. The holiday rush fills 80 and the bridge from Thanksgiving to New Year. The carriers move at dawn. Book three weeks ahead for a date in the last week of August.'),
  P('The Passaic floods the Northside and Riverside in a big storm. Floyd in 1999 put the river up to the second floors. Irene in 2011 set the record, and Ida in 2021 flooded the streets in an hour. The April 2007 storm did the same in spring. A handoff near the river moves up the hill for a day. We call the moment the river forecast turns.'),
  P('The nor’easters run from December into March. The January 2016 blizzard dropped two feet and closed 80 for a day. The snowbanks take a lane off every street in the city for a week after. A trailer needs the full width. The carriers wait in the Meadowlands until the plows finish. A storm shifts a pickup to the next clear morning at the same figure.'),
  P('Summer brings humidity and an afternoon storm a few times a week. The storm shifts the loading hour and nothing else. The bridge backs up every Friday afternoon, and a Manhattan handoff moves to the morning.'),
 )+chips(["Downtown","Market Street","Main Street","Broadway","The Falls District","McBride Avenue","South Paterson","The Eastside","Eastside Park","Hillcrest","Lakeview","The Totowa Section","Peoples Park","Wrigley Park","Sandy Hill","Riverside","River Street","The Northside","Bunker Hill","Route 20","Clifton","Haledon","Hawthorne","Prospect Park","Totowa","Wayne","Fair Lawn","Passaic","Garfield","Little Falls"])
 +NOTE('Serving Paterson and the whole of Passaic County, Falls district block or Hillcrest driveway. Tell us the neighborhood and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Paterson?',
 prose(
  L('Open trailers carry most of north Jersey, and the table above is priced for one.'),
  P('Enclosed keeps the salt, the brine, and the plow grit off the paint. Eastside collectors book it, and so do families sending a car they care about. When a nor’easter is coming, the car rides the first truck with a slot. We tell you so.'),
  P('An everyday car rides open without a second thought. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages set the two beside each other.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A figure, then a lot on Route 20, then a signature in Florida or wherever it lands. The closing or the move-in picks the week.'),
  P('Once you approve the figure, a carrier already rolling on 80 that week takes the car. The lot and the window get agreed that afternoon. The driver shoots photos at pickup and fills in the Bill of Lading. You initial it, and that sheet decides any question at the other end.'),
 )+ULI([
  "Everything personal out of the cabin and the trunk",
  "Fuel down to a quarter tank",
  "Photograph each side and the odometer before the truck comes",
  "One good key, and a note about any known faults",
  "Any add-on alarm turned off",
  "Downtown, in the Falls district, or in South Paterson, the meeting point is a main road",
 ])+prose(P('Read <a href="how-it-works.html">how it works</a> for the steps and <a href="car-shipping-preparation.html">preparation</a> for pickup day.'))))

BODY.append(sec('Why Ship Guy','Why Paterson Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already pass on 80 every day. We know which streets a trailer fits on and which ones it never will.'),
  P('Our FMCSA license and our $75,000 bond are a public record on the federal register. The office is on River Street at the east edge of downtown.'),
  P('You get one coordinator from the quote to the delivery call, and no handoffs in between. The <a href="services.html">services</a> page explains open, enclosed, and expedited.'),
 )))

BODY.append(office('Paterson','237 River St #449','Paterson, NJ 07501','+18622929533','(862) 292-9533','ET',
 '237+River+St+%23449,+Paterson,+NJ+07501','Visit Us','Find Ship Guy in Paterson',
 'Our office is on River Street at the east edge of downtown, along the Passaic.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3721.129406758841!2d-74.1670723!3d40.9248258!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c2fd9946eddee7%3A0x1dd709ce954a7613!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793631137351!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Paterson to Florida or Chicago?","A sedan to Orlando runs seven hundred sixty to one thousand eighty dollars. The trip is about one thousand eighty miles down 95. Chicago runs five hundred sixty to eight hundred twenty, about seven hundred eighty miles on 80. Manhattan is twenty miles away and the lowest lane on the table. An SUV or a pickup runs 10 to 25 percent higher."),
 ("Are the tolls in my price?","Yes, when the route uses them. Carriers pay the Turnpike, the Parkway, and the bridge and tunnel tolls into New York and price accordingly. There is no separate line at delivery. Interstate 80 west to the Delaware carries no toll."),
 ("Can the carrier come to my street downtown or in the Falls district?","No. Downtown is one-way streets full of buses, and the Falls district is narrow brick streets on a hillside. The driver meets you at the Route 20 lots, on Broadway, or on McBride Avenue. The Eastside, Hillcrest, Lakeview, and the Totowa section usually allow the curb."),
 ("Do you ship cars to Florida for families?","Yes, every month of the year. Families send a car to a relative in Orlando or Miami and bring another one back. The lane runs full both ways. The Route 20 lots are the usual meeting spot. A car going to a gated community in Florida meets the truck outside the gate there."),
 ("Can you pick up a car that came through the port in Newark?","Yes. After customs clears it and the terminal releases it, it is an ordinary car to us. Send the release date and the terminal. Cars come in that way from Lima, Santo Domingo, and Istanbul every month."),
 ("Can you deliver on a William Paterson or Montclair State move-in date?","Yes. The university in Wayne takes cars in late August, and the university in Montclair follows the same week. Mom or Dad books, and someone over eighteen signs at the lot. The campus blocks are full that week, so we use the lots on 46. The date sets the window."),
 ("Can you ship a car to or from Clifton, Wayne, or Newark?","Yes. Clifton, Haledon, Hawthorne, and Totowa ride the same carriers and price the same as Paterson. Wayne and Fair Lawn do too. Newark is fifteen miles south and prices with the city on every lane."),
 ("What happens if the river floods or a nor’easter hits on my pickup day?","A flood closes the Northside and Riverside streets. The handoff moves up the hill or to Route 46. A nor’easter keeps the truck in the Meadowlands until the plows are done, usually a day. You get a call as the forecast turns. The pickup takes the next clear morning, and the figure does not change."),
 ("Can you ship a car that does not run from Paterson?","Yes. We send a winch truck and price the loading time in. The Route 20 lots and the big-box lots on 46 are flat. Let us know if it rolls, steers, and brakes."),
 ("What do you need for a Paterson car shipping quote?","Where it starts and where it ends, with the neighborhood. What it is and whether it runs. Open or enclosed, and the week around the move-in or the closing. Send those, and the Paterson figure lands the same day."),
]
BODY.append(faq_section(FAQ,'Paterson FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Paterson?','Two minutes on the form above gets your lane a Paterson figure. Name the neighborhood and the week, and a carrier already passing on 80 takes it.','+18622929533','(862) 292-9533','Get your free Paterson quote'))

build({
 'slug':'auto-transport-paterson-new-jersey',
 'title':'Car Shipping in Paterson, NJ — Auto Transport | Ship Guy',
 'meta':'Car shipping in Paterson, NJ, the Silk City twenty miles from the George Washington Bridge. Hospital and warehouse relocations, the Florida family lane, port cars from Newark, tolls inside the figure, main-road handoffs for downtown, the Falls district, and South Paterson, curbside pickups on the Eastside and in Hillcrest, the floods, and the snow. Local office on River Street. Free quote.',
 'h1':'Car Shipping in<br>Paterson, <span class="accent">New Jersey</span>',
 'lede':'Open, enclosed, and expedited auto transport across Paterson and Passaic County, planned around 80, Route 20, the bridge, the Florida lane, the river, and the winter.',
 'tel':'+18622929533','disp':'(862) 292-9533','brand':'Paterson','keyword':'car shipping in paterson',
 'localterms':['paterson','silk city','george washington bridge','interstate 80','route 19','route 20','route 46','route 4','route 21','main street','market street','broadway','union avenue','river street','passaic','downtown','falls district','falls','raceways','mcbride avenue','south paterson','eastside','hillcrest','lakeview','totowa section','peoples park','wrigley park','sandy hill','riverside','northside','bunker hill','clifton','haledon','hawthorne','prospect park','totowa','wayne','fair lawn','garfield','paramus','newark','manhattan','meadowlands','allentown','philadelphia','hartford','baltimore','boston','washington','pittsburgh','chicago','orlando','miami','florida','parkway','turnpike','willowbrook','mall','squirrelwood','madison avenue','stadium','airport','hospital','residents','traveling nurses','county','courthouse','warehouses','commuters','bus terminal','world cup','dominican','peruvian','turkish','arab','port','customs','state university','community college','montclair','student','retirees','parades','festival','move-in','holiday rush','floyd','1999','irene','2011','ida','2021','april 2007','january 2016','blizzard','snowbanks','salt','brine','grit','bill of lading','fmcsa','winch','one-way','two-family','mills','densest','lima','santo domingo','istanbul'],
}, BODY, FAQ)
