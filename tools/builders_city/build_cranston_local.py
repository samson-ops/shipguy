import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Cranston, Rhode Island','Car shipping just south of Providence, between the bay and the reservoir on 95, Route 10, and Route 2',
 ['Car shipping in Cranston rides the Providence carrier pool, and the trucks reach the city on three highways. Ship Guy is a licensed auto transport broker with an office on Reservoir Avenue in Cranston.',
  'We book vetted carriers across the city and the state, from Edgewood to Garden City and Western Cranston. The carriers own the trucks. Ship Guy holds the license and the bond.',
  'Interstate 95 runs the east edge of the city between Providence and Warwick. Route 10 cuts through the middle to downtown Providence, and Route 37 crosses from 95 to Interstate 295. Reservoir Avenue is Route 2, the retail strip that carries Garden City. Interstate 295 runs the west side.',
  'This page covers 95, Route 10, Route 37, 295, Reservoir Avenue, the village grids, and Western Cranston. It also covers the state campus, the hospitals, the colleges, the airport, the storms, and the lanes.'],
 'Cranston at a glance',
 ['Most pickups happen within 1 to 3 days. The Providence carriers pass the city on 95 every hour. The Boston and New York trucks run it all day.',
  'Boston, Worcester, Hartford, New Haven, and Springfield are a same-day haul. New York and Albany are the same. Philadelphia and Washington take a day. Florida takes three.'],
 'Tell us the village and whether the street is a grid or a cul-de-sac. Edgewood, Pawtuxet, Arlington, and Knightsville meet the truck at a lot. Garden City, Oaklawn, Meshanticut, and Western Cranston usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 95, Route 10, Route 37, Interstate 295, Reservoir Avenue, Park Avenue, and Oaklawn Avenue',
 prose(
  L('Cranston sits between Providence and the airport. A carrier is never more than ten minutes from a highway.'),
  P('Interstate 95 runs the east edge from Providence past the Thurbers Avenue curve to Warwick and the airport. It is the New York-to-Boston lane, and it backs up both rush hours. Route 10 is the Huntington Expressway. It runs from Route 37 north through the middle of the city to Providence. Route 37 is the short crosstown freeway from 95 to Interstate 295, past the state campus. Interstate 295 runs the west side from Warwick to Johnston and the Massachusetts line.'),
  P('Reservoir Avenue is Route 2, the retail strip from Providence through Garden City to Warwick. Park Avenue is Route 12, the old east-west road from Edgewood through Auburn and Knightsville to the west. Oaklawn Avenue is Route 5, and Cranston Street carries the north side. Pontiac Avenue runs past the prison and the state campus, and Phenix Avenue carries the west.'),
  P('The carriers come off 95 at Route 37 and off Route 10 at Reservoir Avenue. The Garden City lots on Reservoir Avenue are the usual meeting spot. The Warwick Mall lots a few miles south and the centers on Oaklawn Avenue work too. The stadium lots on Park Avenue work outside game days.'),
  P('Our office is on Reservoir Avenue, minutes from Route 10 and 95.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Edgewood, Pawtuxet Village, Auburn, Arlington, Knightsville, Garden City, Oaklawn, Meshanticut, Dean Estates, Western Cranston, and Hope',
 prose(
  L('Cranston is a bay shore, a dozen village grids, and a wide-open west side. The truck reaches more of it every year.'),
  P('Edgewood on the bay is big old houses on narrow streets under the trees. The park and the zoo sit beside it. A seventy-five-foot trailer does not stop there. The driver meets you on Broad Street or at the lots by the boulevard. Pawtuxet Village south of it is colonial streets on the cove, shared with Warwick. The handoff moves to Narragansett Parkway.'),
  P('Auburn, Arlington, and Eden Park west of 95 are triple-decker grids on narrow streets. The handoff moves to Park Avenue or the Route 10 ramps. Knightsville along Cranston Street is the same grid around the church and the feast grounds. The driver meets you at the Garden City lots a few blocks south.'),
  P('Garden City around the shopping center is wide postwar streets, and the curb works. Oaklawn, Meshanticut, and Dean Estates along Oaklawn Avenue are the same. The lots get bigger as the road runs west. Stadium and Thornton along the Johnston line are tighter, and the handoff moves to Cranston Street.'),
  P('Western Cranston past 295 is acreage, horse farms, and new subdivisions on the reservoir side. The driver reaches the house or meets you on Phenix Avenue. Hope and Fiskeville at the far west sit on the river by Scituate. Providence, Warwick, Johnston, and West Warwick surround the city, and all four price the same as Cranston. So does the rest of the state.'),
 )))

ROUTES=[("Worcester, MA","MA-146 · ~45 mi","Same day","$120–$200"),("Boston, MA","I-95 · ~55 mi","Same day","$150–$240"),
 ("Hartford, CT","US-6/I-84 · ~75 mi","Same day","$160–$260"),("Springfield, MA","MA-146/I-90 · ~95 mi","Same day","$170–$280"),
 ("New Haven, CT","I-95 · ~100 mi","Same day","$180–$290"),("Albany, NY","MA-146/I-90 · ~170 mi","Same day","$220–$340"),
 ("Manhattan, NY","I-95 · ~175 mi","Same day","$220–$340"),("Philadelphia, PA","I-95 · ~265 mi","1 day","$260–$390"),
 ("Washington, DC","I-95 · ~405 mi","1 day","$340–$490"),("Orlando, FL","I-95 · ~1,245 mi","3 days","$820–$1,180")]
BODY.append(rate_table('Lanes &amp; Costs','Cranston Car Shipping Lanes and Estimated Costs',
 'The lanes Rhode Island cars run most, with estimated open-trailer ranges. Your own route gets a number on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Cranston for an operable sedan on an open trailer. SUVs and pickups run roughly 10 to 25 percent more, and enclosed runs more again. Tolls are inside the number when a carrier uses 90 or the Jersey Turnpike. The season and carrier availability on your dates decide the actual quote.',
 prose(
  P('Cranston prices with Providence on every lane, because the carriers are the same trucks five minutes north. Boston and Worcester are an hour away and the lowest lanes of all. The New York lane rides 95 the whole way and runs a same-day haul. The Florida lane fills with snowbirds each fall and runs higher southbound in October than in July.'),
  P('A move timed to the September move-in or a July closing ships with the busiest weeks. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The State Campus, the Prison, the Hospitals, the Colleges, the Airport, and the Snowbirds',
 prose(
  L('Cranston relocates state employees, corrections staff, nurses, students, and retirees. The state moves more people here than any company.'),
  P('The state campus on Pontiac Avenue holds a dozen agencies and the prison complex. The agencies transfer staff on start dates all year, and the corrections academy runs a class most years. The two Providence hospital systems, with campuses minutes up Route 10, hire traveling nurses year round. Residents arrive each June. Employer-reimbursed moves get their paperwork from us.'),
  P('The colleges in Providence take cars each September and send them home each May. The design school, the Ivy on the hill, and the Catholic college all do it. So does the state university’s downtown campus. The community college in Warwick does the same. A parent sets up the booking, and an adult over eighteen signs at a lot. Campus streets are tight, so the handoff happens at Garden City or the stadium lots.'),
  P('The airport in Warwick sits ten minutes south, and fly-and-ship is routine. New residents land and have the car arrive a few days later. The jewelry and textile shops that built the city have given way to medical offices and warehouses. The managers move in on start dates.'),
  P('Retirees leave Edgewood and Garden City for Florida each fall and come back in May. The Guard units at the state armory rotate staff on orders. The Navy base in Newport moves officers through the city. Ship Guy is a private broker with no tie to either. Timing for orders is on the <a href="military-car-shipping.html">military</a> page, and the interstate side is on the <a href="state-to-state-car-shipping.html">state-to-state</a> page.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Feast, Gaspee Days, the Pumpkins, the Nor’easters, the Blizzard, and the Pawtuxet Floods',
 prose(
  L('Cranston runs on a feast calendar and a bay forecast. The nor’easters decide the winter, and the river decides the spring.'),
  P('The feast in Knightsville fills Cranston Street for a weekend in July. The streets around the church close. Gaspee Days fills Pawtuxet Village for the parade on the second Saturday of June. The pumpkin show at the zoo fills Edgewood every October night, and the park lots overflow. A handoff near any of them moves to the next morning.'),
  P('The stadium on Park Avenue fills on high school football Fridays and track weekends. The Warwick Mall and Garden City fill every December weekend. A handoff at either moves to a weekday morning that month. Move-in week in late August clogs the Providence campuses, and the carriers skip downtown.'),
  P('Winter is nor’easters. A storm drops a foot overnight, and the plows get the highways before the village grids. The blizzard of 1978 trapped cars on 95 for days. Every big storm since has closed the state for a day. The February 2013 blizzard dropped two feet. The carriers wait in Connecticut or Worcester until the roads clear. A winter pickup can lose a day. We tell you first.'),
  P('The Pawtuxet River runs the south edge of the city, and it floods in a wet spring. The March 2010 flood put the river over the mall in Warwick. It closed 95 at the river for days. The low streets in Pawtuxet and along the river closed with it. A pickup on the flat moves up the hill until the water drops. The bay takes Edgewood in a hurricane, and the carriers leave before a landfall.'),
 )+chips(["Edgewood","Broad Street","Pawtuxet Village","Narragansett Parkway","Auburn","Arlington","Eden Park","Knightsville","Cranston Street","Garden City","Reservoir Avenue","Chapel View","Oaklawn","Meshanticut","Dean Estates","Stadium","Park Avenue","Thornton","Pontiac Avenue","Howard","Western Cranston","Phenix Avenue","Hope","Fiskeville","Natick","Providence","Warwick","Johnston","West Warwick","Scituate","Coventry","East Greenwich"])
 +NOTE('Serving Cranston and all of Rhode Island, Edgewood street or Western Cranston acreage. Tell us the village and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Cranston?',
 prose(
  L('Nearly every Rhode Island car rides an open trailer, and the lane table above is priced that way.'),
  P('An enclosed trailer keeps off the road salt, the brine, and the salt air off the bay. The collectors in Edgewood and the executives relocating a new car book one. A car leaving for Florida before the first nor’easter often rides enclosed too.'),
  P('A commuter car or a student car rides open without a second thought. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages walk through the choice.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A number, a lot at Garden City or the stadium, and a signature at delivery. The closing or the move-in picks the week.'),
  P('Approve the price, and the car is booked with a carrier already running 95 through Providence. The spot and the window are settled the same day. You and the driver inspect the car at pickup, and the Bill of Lading records every existing mark. Both of you sign it. Delivery is compared to that record.'),
 )+ULI([
  "Personal items out of the cabin and the trunk",
  "Fuel at about a quarter tank",
  "Every side and the odometer photographed before the handoff",
  "One working key handed to the driver, with any fault named",
  "Aftermarket alarm shut off",
  "In Edgewood, Pawtuxet, or a village grid, meet the truck at a lot",
 ])+prose(P('Each step is covered on the <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages.'))))

BODY.append(sec('Why Ship Guy','Why Cranston Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already run 95 through Providence every day. We know which village grids a trailer cannot enter.'),
  P('Ship Guy’s FMCSA license and $75,000 bond are a public record on the federal register. Our office is on Reservoir Avenue in Cranston.'),
  P('A single coordinator stays with you from the first call to the last signature. The <a href="services.html">services</a> page explains open, enclosed, and expedited transport.'),
 )))

BODY.append(office('Cranston','869 Reservoir Ave #42a','Cranston, RI 02910','+14015841240','(401) 584-1240','ET',
 '869+Reservoir+Ave+%2342a,+Cranston,+RI+02910','Visit Us','Find Ship Guy in Cranston',
 'Our office is on Reservoir Avenue, minutes from Route 10 and 95.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3672.714598032118!2d-71.4469254!3d41.7773743!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89e44ffafdfc3bc1%3A0x64eea3539f781aa7!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793288005485!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Cranston to New York or Florida?","New York runs two hundred twenty to three hundred forty dollars for a sedan. That is about one hundred seventy-five miles down 95. Orlando runs eight hundred twenty to eleven hundred eighty, about twelve hundred fifty miles down 95. Boston is an hour away and the lowest of the three. An SUV or a pickup adds 10 to 25 percent."),
 ("Can the carrier come to my street in Edgewood or Knightsville?","Usually not. Edgewood is big houses on narrow streets under the trees, and Knightsville is a triple-decker grid. The driver meets you on Broad Street, on Park Avenue, or at the Garden City lots. Garden City, Oaklawn, Meshanticut, and Western Cranston usually allow the curb."),
 ("Do you ship cars for state employees and the hospitals?","Yes, every week. The agencies on the state campus transfer staff on start dates all year. The corrections academy runs a class most years. The Providence hospitals hire traveling nurses year round. A second car usually comes along on a trailer. Employer-reimbursed moves get their paperwork from us."),
 ("Can you deliver on a Providence college move-in date?","Yes. The campuses take cars in each September and send them home in May. A parent sets it up, and an adult over eighteen signs at a lot. Campus streets are tight and move-in week clogs them. The handoff happens at Garden City or the stadium lots. The window moves with the date."),
 ("Can you ship a car to or from Warwick, Providence, or Johnston?","Yes, and all three price the same as Cranston. Warwick rides the same carriers off 95 at Route 37, and the curb works in most of it. Providence rides them up Route 10, and the hill streets meet the truck at a lot. Johnston rides them out Route 295. Send the full address for a lane in Western Cranston."),
 ("What happens if a nor’easter hits on my pickup day?","The driver waits in Connecticut or Worcester until 95 clears. A storm drops a foot overnight, and the plows reach the highways before the village grids. The February 2013 blizzard dropped two feet and closed the state for a day. A winter pickup can lose a day. You hear it from us before the driver does."),
 ("What happens if the Pawtuxet floods?","A pickup on the flat moves up the hill until the water drops. The March 2010 flood closed 95 at the river for days. The water went over the mall in Warwick. The low streets in Pawtuxet closed with it. Garden City, Oaklawn, and the west side never notice."),
 ("Can I fly into Warwick and have the car arrive later?","Yes, and new residents do it every week. The airport sits ten minutes south of the city. Give us the delivery address and the date you land, and the pickup is planned around it. An adult over eighteen signs at delivery, so tell us who will be there."),
 ("Can you ship a car that does not run from Cranston?","Yes. We assign a winch truck, and the loading time is in the quote from the start. The Garden City lots or the stadium lots give the driver level ground. Say whether the car rolls, steers, and brakes."),
 ("What do you need for a Cranston car shipping quote?","Pickup and delivery addresses, with the village. Year, make, and model. Does it run. Open or enclosed. The week around the closing or the move-in. Five answers, and the Cranston number is back within the day."),
]
BODY.append(faq_section(FAQ,'Cranston FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Cranston?','The form above gives your lane a number in two minutes. Name the village and the week, and a carrier already on 95 takes it.','+14015841240','(401) 584-1240','Get your free Cranston quote'))

build({
 'slug':'auto-transport-cranston-rhode-island',
 'title':'Car Shipping in Cranston, RI — Auto Transport | Ship Guy',
 'meta':'Car shipping in Cranston, RI, just south of Providence on 95, Route 10, and Route 2. State and hospital relocations, Providence college move-in timing, Garden City handoffs for Edgewood and the village grids, curbside pickups in Oaklawn and Western Cranston, the airport in Warwick, the nor’easters, and the Pawtuxet floods. Local office on Reservoir Avenue. Free quote.',
 'h1':'Car Shipping in<br>Cranston, <span class="accent">Rhode Island</span>',
 'lede':'Open, enclosed, and expedited auto transport across Cranston and all of Rhode Island, planned around 95, Route 10, the village grids, the campus calendar, and the nor’easters.',
 'tel':'+14015841240','disp':'(401) 584-1240','brand':'Cranston','keyword':'car shipping in cranston',
 'localterms':['cranston','providence','bay','reservoir','interstate 95','route 10','route 2','reservoir avenue','edgewood','pawtuxet','garden city','knightsville','western cranston','warwick','route 37','interstate 295','retail strip','village grids','state campus','prison','hospitals','colleges','airport','storms','boston','worcester','hartford','new haven','springfield','new york','albany','philadelphia','washington','florida','thurbers avenue','huntington expressway','johnston','massachusetts line','park avenue','route 12','auburn','oaklawn avenue','route 5','cranston street','pontiac avenue','phenix avenue','warwick mall','stadium','game days','zoo','broad street','boulevard','colonial','cove','narragansett parkway','arlington','eden park','triple-decker','church','feast grounds','shopping center','postwar','meshanticut','dean estates','thornton','acreage','horse farms','subdivisions','hope','fiskeville','scituate','west warwick','snowbirds','move-in','closing','corrections','academy','traveling nurses','residents','design school','ivy','catholic college','state university','community college','fly-and-ship','jewelry','textile','warehouses','retirees','guard','armory','navy base','newport','gaspee days','parade','pumpkin','october','high school football','december','blizzard','1978','february 2013','two feet','connecticut','pawtuxet river','march 2010','hurricane','landfall','salt air','brine','bill of lading','fmcsa','chapel view','howard','natick','coventry','east greenwich'],
}, BODY, FAQ)
