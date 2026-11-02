import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Newark, New Jersey','Car shipping in the port city, between the Turnpike, the airport, and one of the busiest car docks on the East Coast',
 ['Car shipping in Newark starts at one of the busiest interchanges in the country. Ship Guy is a licensed auto transport broker with an office on Broad Street downtown.',
  'We book vetted carriers across Essex County and the port towns, from the North Ward to the Oranges. The trucks belong to the carriers. Ship Guy holds the license and the bond.',
  'The Turnpike runs the east side past the airport and the port. Interstate 78 crosses it on the way to the Holland Tunnel. Interstate 280 runs through downtown to the Oranges, and the Parkway skirts the west. Route 21 runs the river, and Route 1 and 9 carry the airport.',
  'This page covers the Turnpike, 78, 280, Route 21, downtown, the Ironbound, the wards, and the suburbs. It also covers the port, the airport, the headquarters, the campuses, the blossoms, the storms, and the lanes.'],
 'Newark at a glance',
 ['Most pickups happen within 1 to 3 days. Every carrier on the 95 lane passes the city on the Turnpike. The port keeps haulers based next door.',
  'Manhattan, Allentown, Philadelphia, and Hartford are same-day runs. Baltimore and Washington are the same. Boston and Pittsburgh need a day. Chicago needs two, and Florida needs three.'],
 'Tell us the ward and whether the street is double-parked. The Ironbound, downtown, and the old grids meet the truck at a lot. Forest Hill, Vailsburg, the Oranges, Bloomfield, and Belleville sometimes allow the curb.'))

BODY.append(sec('The Roads','The Turnpike, Interstate 78, Interstate 280, the Parkway, Route 21, Routes 1 and 9, and Broad Street',
 prose(
  L('Newark is where the Turnpike, 78, and 280 meet. A carrier reaches every town in the county without a bridge.'),
  P('The Turnpike is Interstate 95. It runs the east edge of the city past the airport and the port. The exits for the airport, the port, and Route 78 all fall inside Newark. Interstate 78 crosses the Turnpike beside the airport. It runs east to the Holland Tunnel and west to Allentown. The Turnpike and 78 charge by the mile, and the toll rides inside the quote.'),
  P('Interstate 280 runs from the Turnpike at Kearny over the Passaic. It continues through downtown to the Oranges and 80. The Garden State Parkway skirts the west side through Irvington and East Orange. It bans trucks this far north. A carrier never uses it. Route 21 is McCarter Highway, along the river from the airport through downtown to Belleville. Routes 1 and 9 carry the airport and the port, and the Skyway above them bans trucks. A carrier stays on the Turnpike.'),
  P('The carriers come off the Turnpike at the airport exit and off 280 at First Street. The outlet mall lots in Elizabeth at the port exit are the usual meeting spot. The furniture store lot beside it and the big-box lots on Springfield Avenue work too. The Branch Brook Park lots in the North Ward work outside the blossom weeks.'),
  P('Our office is on Broad Street downtown, at Washington Park and a few blocks from the arts center.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the Ironbound, the North Ward, Forest Hill, University Heights, Vailsburg, Weequahic, Harrison, the Oranges, Bloomfield, and Belleville',
 prose(
  L('Newark is dense wards on a tight grid. The truck meets nearly all of them at a lot.'),
  P('Downtown is the headquarters towers, the arena, the arts center, and the station. The streets are one-way and double-parked, and a seventy-five-foot trailer does not stop on them. The driver meets you at the Raymond Boulevard lots by the river or at the Broad Street garages. University Heights west of downtown is the campuses and the hospital. The handoff happens at a campus lot.'),
  P('The Ironbound east of the station is the Portuguese and Brazilian neighborhood. Ferry Street and the row-house streets sit between the rail lines. The blocks are tight and the parking is full. The driver meets you at the riverfront park lots or on Raymond Boulevard. Harrison across the river is new apartment blocks around the soccer stadium. The handoff happens at the stadium lots.'),
  P('The North Ward climbs toward Branch Brook Park. Forest Hill above the park is big houses on wider streets. The curb sometimes works there. Roseville and Mount Pleasant below it are tighter. The handoff moves to the park lots or Bloomfield Avenue. Vailsburg in the West Ward and Weequahic in the South Ward are grids of two-family houses. The driver meets you on Springfield Avenue or at the park.'),
  P('The Oranges, Irvington, and Hillside are older grids with the same answer. Montclair and Bloomfield have wider streets where the curb sometimes works. Belleville and Nutley along the river are tight. Elizabeth and the port towns to the south ship with the same trucks. All of them price the same as Newark, and so do Jersey City and Hoboken.'),
 )))

ROUTES=[("Manhattan, NY","I-78 · ~10 mi","Same day","$100–$170"),("Allentown, PA","I-78 · ~80 mi","Same day","$160–$260"),
 ("Philadelphia, PA","NJ Tpke · ~85 mi","Same day","$160–$260"),("Hartford, CT","I-95/I-91 · ~115 mi","Same day","$190–$300"),
 ("Baltimore, MD","I-95 · ~180 mi","Same day","$220–$340"),("Washington, DC","I-95 · ~220 mi","Same day","$240–$360"),
 ("Boston, MA","I-95 · ~225 mi","1 day","$240–$360"),("Pittsburgh, PA","I-78/I-76 · ~360 mi","1 day","$330–$470"),
 ("Chicago, IL","I-80 · ~790 mi","2 days","$560–$820"),("Orlando, FL","I-95 · ~1,060 mi","3 days","$760–$1,080")]
BODY.append(rate_table('Lanes &amp; Costs','Newark Car Shipping Lanes and Estimated Costs',
 'The lanes Essex County cars run most, with estimated open-trailer ranges. Price your own route on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Newark for a sedan that runs, open trailer. Add 10 to 25 percent for an SUV or a pickup, and more for enclosed. The Turnpike, 78, and the Hudson crossings are inside the number. Season and the carriers free on your dates set the final figure.',
 prose(
  P('Newark prices among the best in the Northeast. Every carrier on the 95 lane passes the city, and the port keeps more based here. Manhattan is across the river, and the tunnel toll is the only difference. The Philadelphia and Washington lanes ride the Turnpike south. The Florida lane fills southbound each fall and northbound each spring, and the price follows.'),
  P('September move-ins and January start dates ship in the busiest weeks. How size, condition, and season move the number is in the <a href="car-shipping-cost.html">cost guide</a>.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Port, the Airport, the Headquarters, the Campuses, the Hospitals, and the Manhattan Commute',
 prose(
  L('Newark relocates longshoremen, airline crews, insurance staff, students, and residents. The port and the headquarters move the most.'),
  P('The auto terminals at the port land hundreds of thousands of imported cars a year. The dealers’ haulers carry them out. We do not move those. A private car that arrived by ship and has cleared customs is a domestic move like any other. Give us the release date and the terminal. The ocean leg is booked separately if you ever need one.'),
  P('The airport is a hub for one of the big airlines. Its crews and contractors relocate on bid dates all year. The headquarters downtown move people every week. The insurer on Broad Street and the utility beside it relocate staff on offer dates. So do the audiobook company at Washington Park and the electronics company by the station. The second car usually rides a trailer. A reimbursed move gets its receipts and its invoice from us.'),
  P('The campuses in University Heights take cars each September and send them home each May. The engineering school, the state university campus, the county college, and the medical school all do it. The booking comes from a parent, and an adult signs at the campus lot. The two hospitals hire traveling nurses year round, and residents arrive each June.'),
  P('Families priced out of the city across the river buy in Forest Hill, the Oranges, and Montclair. One car rides the trailer while the other is driven. Service members headed to the joint base in Burlington County ship through here too. Ship Guy has no tie to it. Moves on orders are explained on the <a href="military-car-shipping.html">military</a> page, and interstate moves on the <a href="state-to-state-car-shipping.html">state-to-state</a> page.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Cherry Blossoms, Portugal Day, Hockey Nights, the Nor’easters, Sandy, and Ida',
 prose(
  L('Newark runs on a port calendar and an arena calendar. The storms come up the river and down the Turnpike.'),
  P('The cherry blossoms fill Branch Brook Park for two weeks in April. The park roads close for the festival weekend. Portugal Day fills Ferry Street and the whole Ironbound for a June weekend. The arena downtown fills the garages on hockey nights from October through April. Concert nights do the same all year. The stadium in Harrison fills on soccer match days. A handoff near any of them moves to the next morning.'),
  P('The Thursday before Thanksgiving through New Year’s is the airport’s busiest stretch, and the Turnpike exit backs up. The port’s ship schedule sends a wave of haulers out the Doremus Avenue gates most mornings. Move-in week in late August clogs University Heights. The meeting spot moves to the river lots those weeks.'),
  P('Winter is nor’easters. The January 2016 blizzard dropped more than two feet and shut the Turnpike for a day. The plows reach the Turnpike and 280 first and the ward streets last. The carriers wait in Allentown or on the Turnpike service areas until the roads clear. A winter pickup can lose a day. You hear it from us first.'),
  P('Sandy in 2012 put the surge over the port and the Ironbound. Thousands of new cars on the docks were destroyed. The power stayed out for a week. Ida in 2021 flooded Route 21, 280, and the airport in a single night. Carriers leave the port district before a landfall. A pickup on the flats moves uphill until the water drops. The Passaic takes the river streets in a big rain.'),
 )+chips(["Downtown","Broad Street","Washington Park","Military Park","Penn Station","Ironbound","Ferry Street","Riverfront","University Heights","North Ward","Forest Hill","Branch Brook Park","Roseville","Mount Pleasant","Vailsburg","Weequahic","Clinton Hill","South Ward","Harrison","Kearny","East Orange","Orange","West Orange","South Orange","Montclair","Bloomfield","Belleville","Nutley","Irvington","Hillside","Elizabeth","Jersey City","Hoboken","Bayonne","Port Newark"])
 +NOTE('Serving Newark, all of Essex County, and the port towns, Ironbound row house or Montclair driveway. Tell us the ward and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Newark?',
 prose(
  L('Nearly every Essex County car rides an open trailer, and the lane table above is priced that way.'),
  P('An enclosed trailer keeps off the road salt, the port grit, and the Turnpike spray. The collectors in Forest Hill and Montclair book one. So do the executives relocating a new car to the towers. A car coming off a ship and headed far often rides enclosed too.'),
  P('A daily driver or a student car rides open without a second thought. Read the <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages to decide.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a lot at the outlets or on the river, and a signature at delivery. The closing or the move-in picks the week.'),
  P('Say yes to the number, and a carrier already running the Turnpike past the airport takes the job. Lot and window are locked in the same afternoon. The driver photographs the car and writes its condition on the Bill of Lading, and you initial it. The delivery inspection is held to that sheet.'),
 )+ULI([
  "Everything personal out of the car, trunk included",
  "Gas gauge near a quarter",
  "Photograph the car and the odometer yourself before the driver arrives",
  "One good key, and tell the driver about any known faults",
  "Turn off any alarm that was added after the factory",
  "In the Ironbound, downtown, or the wards, plan on a lot",
 ])+prose(P('Step by step detail is on the <a href="how-it-works.html">how it works</a> page. The pickup checklist is on the <a href="car-shipping-preparation.html">preparation</a> page.'))))

BODY.append(sec('Why Ship Guy','Why Newark Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already run the Turnpike past the port every hour. We know which ward streets a trailer cannot enter.'),
  P('Pull our FMCSA license and $75,000 bond on the federal register any time. The office is on Broad Street downtown.'),
  P('The same coordinator answers from the first call to the delivery call. Open, enclosed, and expedited options are side by side on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Newark','625 Broad St Ste 440','Newark, NJ 07102','+18624182888','(862) 418-2888','ET',
 '625+Broad+St+Ste+440,+Newark,+NJ+07102','Visit Us','Find Ship Guy in Newark',
 'Our office is on Broad Street downtown, at Washington Park and a few blocks from the arts center.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3731.4983312474346!2d-74.169975!3d40.740333799999995!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c253324bd9ddfd%3A0x4a231226155a2903!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793288409685!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Newark to Florida or Chicago?","Orlando runs seven hundred sixty to one thousand eighty dollars for a sedan. That is about one thousand sixty miles down 95. Chicago runs five hundred sixty to eight hundred twenty, about seven hundred ninety miles out 80. Philadelphia is ninety minutes down the Turnpike and costs far less than either. Larger vehicles add 10 to 25 percent."),
 ("Can the carrier come to my street in the Ironbound or downtown?","No. The Ironbound is tight row-house blocks with full parking, and downtown is one-way streets and garages. The driver meets you at the riverfront park lots, on Raymond Boulevard, or at the outlets in Elizabeth. Forest Hill, the Oranges, Montclair, and Bloomfield sometimes allow the curb."),
 ("Can you pick up a car that came through Port Newark?","Yes, once it has cleared customs and been released to you. The automaker shipments leave on the dealers’ haulers, and we do not move those. A private import ships domestically like any other car. Tell us the release date and the terminal. The ocean leg is booked separately if you need one."),
 ("Do you ship cars for the headquarters and the airport?","Yes, every week. The insurer, the utility, the audiobook company, and the electronics company relocate staff on offer dates. The airline hub moves crews on bid dates all year. The second car usually rides a trailer. A reimbursed move gets its receipts and its invoice from us."),
 ("Can you deliver on a Rutgers-Newark or NJIT move-in date?","Yes. University Heights fills with student cars each September and empties in May. The booking comes from a parent, and an adult signs at the campus lot. Move-in week clogs the Heights, so the truck meets you at the river lots. Give us the date and the window follows."),
 ("Are the Turnpike and tunnel tolls in my price?","Yes. A carrier that uses the Turnpike, 78, or a Hudson crossing pays by transponder. The toll rides inside the quote. There is no separate line. Route 21 and 280 carry no toll."),
 ("Can you ship a car to or from Montclair, Elizabeth, or Jersey City?","Yes, and all three price the same as Newark. Montclair rides the same carriers out Bloomfield Avenue, and the curb often works. Elizabeth rides them off the Turnpike at the port exit. Jersey City rides them across 78, and its blocks meet the truck at a lot. Send the full address for a hill street."),
 ("What happens if a nor’easter or a hurricane hits on my pickup day?","Carriers leave the port district before a landfall and wait on the Turnpike service areas after a snowstorm. Sandy flooded the port and the Ironbound, and Ida flooded Route 21 and the airport in a night. A pickup on the flats moves uphill until the water drops. You hear it from us before the driver does."),
 ("Can you ship a car that does not run from Newark?","Yes. A winch carrier is booked, with the loading time already in the price. The outlet lots in Elizabeth or the park lots in the North Ward give the driver level ground. We need to know whether it rolls, steers, and brakes."),
 ("What do you need for a Newark car shipping quote?","Start and finish addresses, with the ward or the town. The year, make, and model. Whether it drives. Open or enclosed. Your week. Give us those five and the Newark price is back before the day ends."),
]
BODY.append(faq_section(FAQ,'Newark FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Newark?','Your lane gets a price two minutes after you finish the form above. Name the ward and the week, and a Turnpike carrier does the rest.','+18624182888','(862) 418-2888','Get your free Newark quote'))

build({
 'slug':'auto-transport-newark-new-jersey',
 'title':'Car Shipping in Newark, NJ — Auto Transport | Ship Guy',
 'meta':'Car shipping in Newark, NJ, the port city on the Turnpike, 78, and 280. Port Newark releases, airport and headquarters relocations, Rutgers-Newark and NJIT move-in timing, lot handoffs for the Ironbound and downtown, curbside pickups in Forest Hill and Montclair, the tolls, the cherry blossoms, Sandy and Ida. Local office on Broad Street downtown. Free quote.',
 'h1':'Car Shipping in<br>Newark, <span class="accent">New Jersey</span>',
 'lede':'Open, enclosed, and expedited auto transport across Essex County and the port towns, planned around the Turnpike, the port, the ward streets, the campus calendar, and the storms.',
 'tel':'+18624182888','disp':'(862) 418-2888','brand':'Newark','keyword':'car shipping in newark',
 'localterms':['newark','port','turnpike','airport','car dock','east coast','interchange','ironbound','broad street','downtown','essex county','port towns','north ward','weequahic','oranges','harrison','78','holland tunnel','interstate 280','parkway','route 21','route 1 and 9','wards','suburbs','headquarters','campuses','cherry blossoms','sandy','ida','manhattan','allentown','philadelphia','hartford','baltimore','washington','boston','pittsburgh','chicago','florida','double-parked','forest hill','vailsburg','bloomfield','belleville','interstate 95','toll','kearny','passaic','irvington','east orange','mccarter highway','skyway','first street','outlet mall','elizabeth','furniture store','springfield avenue','branch brook park','washington park','penn station','arena','arts center','one-way','raymond boulevard','garages','university heights','hospital','portuguese','brazilian','ferry street','row-house','rail lines','riverfront park','soccer stadium','roseville','mount pleasant','bloomfield avenue','two-family','montclair','nutley','hillside','jersey city','hoboken','longshoremen','airline','crews','imported cars','customs','release date','terminal','ocean leg','hub','bid dates','insurer','utility','audiobook','electronics','engineering school','state university','county college','medical school','traveling nurses','residents','closing','joint base','portugal day','hockey nights','concert nights','match days','thanksgiving','doremus avenue','move-in','january 2016','two feet','service areas','2012','surge','docks','2021','landfall','road salt','spray','bill of lading','fmcsa','military park','clinton hill','south ward','orange','west orange','south orange','bayonne','port newark'],
}, BODY, FAQ)
