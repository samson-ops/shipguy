import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Warwick, Rhode Island','Car shipping in the airport city, where 95, Route 2, and the bay meet',
 ['Car shipping in Warwick starts at the airport and ends at the bay. Ship Guy is a licensed auto transport broker with an office on Centerville Road in Apponaug.',
  'We book vetted carriers across the city, from Pawtuxet and Conimicut to Cowesett and Potowomut. The trucks belong to the carriers. Ship Guy holds the license and the bond.',
  'Interstate 95 runs through the middle of the city past the airport. Interstate 295 splits off it and runs north, and Route 37 crosses to Cranston. Route 2 is Bald Hill Road, the retail strip. Route 117 runs from the bay through Apponaug to the west.',
  'This page covers 95, 295, Route 2, Route 117, the airport, the bay villages, and the western hills. It also covers the hospital, the submarine yard, fly-and-ship, the Pawtuxet floods, and the lanes.'],
 'Warwick at a glance',
 ['Most pickups happen within 1 to 3 days. The Providence carriers pass the city on 95 every hour, and the airport sits beside the exit.',
  'Boston, Worcester, Hartford, and New Haven are same-day runs. Springfield, Albany, and New York are the same. Philadelphia and Washington need a day. Florida needs three.'],
 'Tell us the village and whether the street runs to the water. Pawtuxet, Conimicut, Oakland Beach, and Warwick Neck meet the truck at a lot. Greenwood, Cowesett, Hillsgrove, and the Route 2 side usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 95, Interstate 295, Route 2, Route 37, Route 117, Post Road, and the Airport Connector',
 prose(
  L('Warwick is the one Rhode Island city every carrier passes through. The airport, the mall, and the interchange all sit on 95.'),
  P('Interstate 95 runs the length of the city from the Cranston line to East Greenwich. It carries the New York-to-Boston lane. The exits for the airport, Route 37, Route 117, and Route 4 all fall inside Warwick. Interstate 295 leaves 95 south of the airport and runs north past Route 37 to Johnston. Route 4 leaves 95 two miles farther south and runs toward Quonset and South County.'),
  P('Route 2 is Bald Hill Road, the state’s busiest retail strip, from the mall north into Cranston. Route 37 is the short crosstown freeway from 295 to 95, along the Cranston line. Route 117 is Centerville Road and Warwick Avenue, from the bay through Apponaug to West Warwick. Post Road is Route 1, the old highway along the airport. The airport connector runs from 95 to the terminal.'),
  P('The carriers come off 95 at Route 37 and at the airport exit. The Warwick Mall lots on Route 2 are the usual meeting spot. The centers along Bald Hill Road and the station garage at the airport work too. The park lots at Rocky Point work outside summer weekends.'),
  P('Our office is on Centerville Road in Apponaug, minutes from 95 and the airport.'),
 ), alt=True))

BODY.append(sec('The Villages','Apponaug, Pawtuxet, Conimicut, Oakland Beach, Warwick Neck, Buttonwoods, Greenwood, Cowesett, Hillsgrove, and Potowomut',
 prose(
  L('Warwick is thirty villages on a bay. The ones on the water are the ones a trailer skips.'),
  P('Apponaug is the center, with City Hall, the roundabouts, and the old mill village along the cove. The streets are short and tight, and the driver meets you on Centerville Road. Pawtuxet at the north end is colonial houses on the cove, shared with Cranston. The handoff moves to Narragansett Parkway.'),
  P('Conimicut, Oakland Beach, and Buttonwoods sit on the bay down narrow beach lanes. A seventy-five-foot trailer stays on West Shore Road. The driver meets you there or at the beach lots. Warwick Neck is big houses on a point with one road in. The handoff happens at the Rocky Point lots. Gaspee Point and Governor Francis Farms are the same, with the handoff on Warwick Avenue.'),
  P('Greenwood, Hoxsie, and Norwood between Post Road and the bay are postwar grids on wide streets. The curb works on most of them. Hillsgrove around the airport is office parks and hotels, and the lots are everywhere. Lakewood and the streets off Route 2 are wide, and the driver reaches the house.'),
  P('Cowesett in the west is hills and big lots. The driver reaches the driveway or meets you on Cowesett Avenue. Potowomut across the river sits by the state park on the East Greenwich line. The handoff happens on Ives Road. Cranston, West Warwick, East Greenwich, and Coventry surround the city. All four price the same as Warwick, and so does the rest of the state.'),
 )))

ROUTES=[("Worcester, MA","MA-146 · ~50 mi","Same day","$120–$200"),("Boston, MA","I-95 · ~60 mi","Same day","$150–$240"),
 ("Hartford, CT","US-6/I-84 · ~75 mi","Same day","$160–$260"),("New Haven, CT","I-95 · ~95 mi","Same day","$170–$280"),
 ("Springfield, MA","MA-146/I-90 · ~100 mi","Same day","$180–$290"),("Albany, NY","MA-146/I-90 · ~175 mi","Same day","$220–$340"),
 ("Manhattan, NY","I-95 · ~170 mi","Same day","$220–$340"),("Philadelphia, PA","I-95 · ~260 mi","1 day","$260–$390"),
 ("Washington, DC","I-95 · ~400 mi","1 day","$340–$490"),("Orlando, FL","I-95 · ~1,240 mi","3 days","$820–$1,180")]
BODY.append(rate_table('Lanes &amp; Costs','Warwick Car Shipping Lanes and Estimated Costs',
 'The lanes Warwick cars run most, with estimated open-trailer ranges. Price your own route on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*Estimated 2026 ranges from Warwick for a sedan that runs, open trailer. Count on 10 to 25 percent more for an SUV or a pickup, and more for enclosed. Tolls are inside the number where a carrier pays one. The calendar and the trucks free on your dates decide the final quote.',
 prose(
  P('Warwick prices with Providence on every lane, because the carriers are the same trucks ten minutes north. The New York lane rides 95 the whole way and runs a same-day haul. Boston and Worcester are an hour away and cost the least. The Florida lane fills with snowbirds each fall and costs more southbound in October than in June.'),
  P('A July closing or a September move-in lands in the busiest weeks of the year. Size, condition, and the season are explained in the <a href="car-shipping-cost.html">cost guide</a>.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Airport, the Hospital, the Submarine Yard, the Community College, and the Snowbirds',
 prose(
  L('Warwick relocates airline staff, nurses, submarine engineers, and retirees. The airport and the hospital move the most.'),
  P('The airport is the state’s front door. Its airlines, its contractors, and the car-rental lots hire year round. New residents land and have the car arrive a few days later. The hospital on Toll Gate Road is the largest employer in the city. It hires traveling nurses year round, and residents arrive each June. When an employer reimburses the move, the paperwork comes from us.'),
  P('The submarine yard at Quonset sits fifteen minutes south, and it hires engineers and welders by the thousand. Many of them buy in Warwick for the commute. The start dates land all year, and the second car usually rides a trailer. The pharmaceutical plant in West Greenwich and the plastics plant at Quonset move managers the same way.'),
  P('The community college campus by the airport takes cars each September and sends them home each May. The Providence colleges do the same, and their students fly in through Warwick. A parent books it from home, and an adult meets the truck at a lot to sign. The Navy base in Newport moves officers through the city on orders. Ship Guy is a private broker with no tie to it.'),
  P('Retirees leave the bay villages for Florida each fall and come back in May. The Guard headquarters next door in Cranston rotates staff on orders too. Our <a href="military-car-shipping.html">military</a> page explains how orders change the timing, and our <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate paperwork.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Gaspee Days, the Summer Beaches, the Holiday Mall, the Nor’easters, the Hurricanes, and the Pawtuxet',
 prose(
  L('Warwick runs on a beach calendar and a mall calendar. The bay brings the storms, and the river brings the floods.'),
  P('Gaspee Days fills Pawtuxet for the parade on the second Saturday of June, and the village closes. The summer concerts and the beaches fill Oakland Beach and Rocky Point every warm weekend. A handoff near the water moves to a weekday morning. The mall on Route 2 fills every weekend from Thanksgiving to Christmas, and so does Bald Hill Road. The meeting spot moves to the train station lots that month.'),
  P('The airport runs its busiest weeks around the holidays and the school breaks. The connector and Post Road back up on those mornings. A pickup in Hillsgrove moves to midday. The Providence college move-in in late August fills 95 from the airport north.'),
  P('Winter is nor’easters. A storm drops a foot overnight, and the plows reach 95 before the village lanes. The blizzard of 1978 trapped cars on 95 in Warwick for days. The February 2013 storm dropped two feet and closed the state for a day. The carriers wait in Connecticut or Worcester until the roads clear. A winter pickup can lose a day. You hear it from us first.'),
  P('The Pawtuxet runs along the north edge of the city. The March 2010 flood put it over the mall. Route 2 and 95 closed at the river for days. The bay takes Oakland Beach and Conimicut in a hurricane. The 1938 storm and Carol in 1954 wiped the beach villages out. Carriers leave before a landfall, and a pickup on the water moves inland until the surge drops.'),
 )+chips(["Apponaug","Centerville Road","Pawtuxet","Gaspee Point","Governor Francis","Conimicut","Oakland Beach","Buttonwoods","Warwick Neck","Rocky Point","Greenwood","Hoxsie","Norwood","Lakewood","Hillsgrove","Post Road","Jefferson Boulevard","Bald Hill Road","Warwick Mall","Cowesett","Natick","Potowomut","Goddard Park","Cranston","West Warwick","East Greenwich","Coventry","Quonset","Providence"])
 +NOTE('Serving Warwick and all of Rhode Island, bay cottage or Cowesett hill. Tell us the village and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Warwick?',
 prose(
  L('Open trailers carry nearly every Warwick car, and the lane table above assumes one.'),
  P('An enclosed trailer keeps off the salt air, the road brine, and the winter grit. The collectors on Warwick Neck and the officers headed to Newport book one. A car going to Florida ahead of the first nor’easter often rides enclosed too.'),
  P('A daily driver or a student car has no need of a roof. Compare the two on the <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a lot at the mall or the train station, and a signature at the far end. The closing or the flight picks the week.'),
  P('Say yes to the number, and a carrier already running 95 past the airport gets the job. We confirm the lot and the window that afternoon. The driver notes every scratch and ding on the Bill of Lading while you watch, and you countersign. The same sheet is checked at the other end.'),
 )+ULI([
  "Take your belongings out of the car before the driver arrives",
  "Leave the tank around a quarter full",
  "Snap each side, the roof, and the odometer that morning",
  "Give the driver a key that works and mention any quirks",
  "Shut off any add-on alarm",
  "On the bay or in Apponaug, plan on a lot instead of the curb",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> page walks the whole sequence, and the <a href="car-shipping-preparation.html">preparation</a> page has the checklist.'))))

BODY.append(sec('Why Ship Guy','Why Warwick Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already run 95 past the airport every day. We know which beach lanes a trailer cannot turn in.'),
  P('Our FMCSA license number and our $75,000 bond can be checked on the federal register in a minute. The office is on Centerville Road in Apponaug.'),
  P('The person who quotes the move is the person who sees it delivered. Open, enclosed, and expedited service are compared on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Warwick','200 Centerville Rd #404','Warwick, RI 02886','+14019925420','(401) 992-5420','ET',
 '200+Centerville+Rd+%23404,+Warwick,+RI+02886','Visit Us','Find Ship Guy in Warwick',
 'Our office is on Centerville Road in Apponaug, minutes from 95 and the airport.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3677.2883442204748!2d-71.46746089999999!3d41.6974453!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89e44db9070c979f%3A0x208803bddd450dcb!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793288018292!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Warwick to New York or Florida?","New York runs two hundred twenty to three hundred forty dollars for a sedan. That is about one hundred seventy miles down 95. Orlando runs eight hundred twenty to eleven hundred eighty, about twelve hundred forty miles down 95. Boston is an hour away and costs the least of the three. An SUV or a truck runs 10 to 25 percent higher."),
 ("Can the carrier come to my street in Conimicut or Oakland Beach?","Usually not. The bay villages are narrow beach lanes, and a seventy-five-foot trailer stays on West Shore Road. The driver meets you there or at the beach lots. Greenwood, Hillsgrove, Cowesett, and the streets off Route 2 usually allow the curb."),
 ("Can I fly into Warwick and have the car arrive later?","Yes, and new residents do it every week. The airport sits beside the 95 exit. Give us the delivery address and the date you land, and we plan the pickup around it. Someone over eighteen signs at delivery, so tell us who will meet the truck."),
 ("Do you ship cars for the hospital and the submarine yard?","Yes, every week. The hospital on Toll Gate Road hires traveling nurses year round and takes residents each June. The submarine yard at Quonset hires engineers on start dates all year, and many buy in Warwick. The second car usually rides a trailer. When an employer reimburses the move, the paperwork comes from us."),
 ("Can you ship a car to or from Cranston, East Greenwich, or Coventry?","Yes, and all three price the same as Warwick. Cranston rides the same carriers up Route 2 or 95. East Greenwich rides them down Route 4, and the hill streets meet the truck on Main Street. Coventry rides them out Route 117. Send the full address for a lane in the west."),
 ("What happens if a nor’easter hits on my pickup day?","The driver holds in Connecticut or Worcester until 95 is plowed. A foot can fall overnight, and the village lanes are cleared last. The February 2013 storm dropped two feet and shut the state for a day. Expect a winter pickup to slip a day, and expect to hear it from us first."),
 ("What happens if the Pawtuxet floods?","A pickup near the river moves up the hill until the water drops. The March 2010 flood put the river over the mall and closed 95 and Route 2 for days. The bay villages and the hills to the west never notice. We tell you the moment the forecast changes the plan."),
 ("Can you deliver on a college move-in date?","Yes. The community college by the airport and the Providence campuses take cars each September. They send them home in May. A parent books it from home, and an adult meets the truck to sign. Campus streets are jammed that week, so the handoff happens at the mall or the station."),
 ("Can you ship a car that does not run from Warwick?","Yes. A truck with a winch is assigned, and the loading time is quoted up front. The mall lots on Route 2 or the station lots at the airport give the driver level ground. Tell the coordinator whether it rolls, steers, and brakes."),
 ("What do you need for a Warwick car shipping quote?","Where the car is and where it goes, with the village. The year, make, and model. Whether it drives. Open or enclosed. The week you have in mind. Answer those five and the Warwick price comes back the same day."),
]
BODY.append(faq_section(FAQ,'Warwick FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Warwick?','Two minutes on the form above and your lane has a price. Add the village and the week, and a carrier already passing the airport picks it up.','+14019925420','(401) 992-5420','Get your free Warwick quote'))

build({
 'slug':'auto-transport-warwick-rhode-island',
 'title':'Car Shipping in Warwick, RI — Auto Transport | Ship Guy',
 'meta':'Car shipping in Warwick, RI, the airport city on 95, Route 2, and the bay. Fly-and-ship through the airport, hospital and submarine yard relocations, lot handoffs for Pawtuxet, Conimicut, and Oakland Beach, curbside pickups in Greenwood, Cowesett, and Hillsgrove, the nor’easters, and the Pawtuxet floods. Local office on Centerville Road in Apponaug. Free quote.',
 'h1':'Car Shipping in<br>Warwick, <span class="accent">Rhode Island</span>',
 'lede':'Open, enclosed, and expedited auto transport across Warwick and all of Rhode Island, planned around 95, the airport, the bay villages, and the nor’easters.',
 'tel':'+14019925420','disp':'(401) 992-5420','brand':'Warwick','keyword':'car shipping in warwick',
 'localterms':['warwick','airport','interstate 95','route 2','bay','centerville road','apponaug','pawtuxet','conimicut','cowesett','potowomut','interstate 295','route 37','cranston','bald hill road','retail strip','route 117','villages','hills','hospital','submarine yard','fly-and-ship','pawtuxet floods','boston','worcester','hartford','new haven','springfield','albany','new york','philadelphia','washington','florida','oakland beach','warwick neck','greenwood','hillsgrove','east greenwich','route 4','cowesett avenue','navy base','south county','johnston','mall','west warwick','post road','route 1','connector','terminal','warwick mall','train station','rocky point','city hall','roundabouts','mill village','cove','narragansett parkway','west shore road','beach lots','gaspee point','governor francis farms','warwick avenue','hoxsie','norwood','office parks','hotels','lakewood','driveway','state park','ives road','coventry','snowbirds','closing','move-in','airline','car-rental','toll gate road','traveling nurses','residents','quonset','welders','pharmaceutical','west greenwich','plastics','community college','newport','retirees','guard','gaspee days','parade','second saturday','concerts','thanksgiving','christmas','school breaks','blizzard','1978','february 2013','two feet','connecticut','march 2010','hurricane','1938','carol','1954','surge','salt air','brine','bill of lading','fmcsa','buttonwoods','jefferson boulevard','natick','goddard park','providence'],
}, BODY, FAQ)
