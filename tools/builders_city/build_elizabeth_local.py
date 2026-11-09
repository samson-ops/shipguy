import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Elizabeth, New Jersey','Car shipping beside the biggest port on the East Coast, where the Turnpike drops two exits in town and the airport runways end at the city line',
 ['Car shipping in Elizabeth runs on the Turnpike, which drops two exits in the city at the port. Ship Guy is a licensed auto transport broker with an office on Union Street near the train station.',
  'We book vetted carriers across Elizabeth, from the Elizabethport grid to Elmora and the Westminster blocks. Union, Hillside, Linden, Roselle, and the Staten Island side of the Goethals ride the same trucks. The trucks are the carriers’ own. Ship Guy holds the license and the bond.',
  'The Turnpike runs the east side with exit 13 at the Goethals and exit 13A at the port. Routes 1 and 9 run beside it on the viaduct. Route 27 and Route 28 cross the west side, and Morris Avenue runs out to the university. Broad Street, Elizabeth Avenue, North Avenue, and Bayway Avenue carry the rest.',
  'This page covers the Turnpike, 1 and 9, the Goethals, the port roads, and the rowhouse wards. It also covers the port, the airport, the refinery, the warehouses, the university, and the hospital. The port’s peak season, the outlet-mall weekends, Sandy, and Ida are here too.'],
 'Elizabeth at a glance',
 ['Most Elizabeth pickups land within 1 to 3 days. The city sits at the Turnpike’s busiest exits beside the port and the airport. The carriers between New York, Philadelphia, and the South pass on the Turnpike every hour. The port keeps a deeper pool of trucks here than anywhere in the state.',
  'New York, Allentown, Philadelphia, Hartford, Baltimore, and Washington are a same-day haul. Boston and Pittsburgh take a day. Chicago takes two, and Florida takes three.'],
 'Tell us the ward. Midtown, Elmora, Peterstown, and North Elizabeth meet the truck on a main avenue or at the outlet-mall lots. Westminster, Elmora Hills, Union, Roselle, and Linden sometimes allow the curb.'))

BODY.append(sec('The Roads','The Turnpike, Routes 1 and 9, Interstate 278, the Goethals Bridge, Route 27, Route 28, Route 439, Broad Street, Elizabeth Avenue, Morris Avenue, North Avenue, and Bayway Avenue',
 prose(
  L('Elizabeth is where the Turnpike, the port, and the airport meet, and the trucks never stop coming. A carrier here has more lots and more traffic than anywhere else in the state.'),
  P('The New Jersey Turnpike runs the east side of the city. Exit 13 feeds Interstate 278 over the Goethals Bridge to Staten Island and the Bayway side of town. Exit 13A feeds the port, the outlet mall, and the airport. Routes 1 and 9 run beside the Turnpike on a viaduct from Linden to the airport and Newark. The Goethals was rebuilt with twin spans in 2018, and it carries the Staten Island lane all day.'),
  P('Route 27 crosses the west side toward Rahway and Newark. Route 28 leaves North Broad Street for Roselle Park and Cranford. Route 439 is Bayway Avenue and the west side connector to Union. Morris Avenue runs from Midtown through Elmora to the university in Union. Broad Street is downtown, one way through Midtown with the bus lanes. Elizabeth Avenue runs from Broad Street east to the port. North Avenue and Dowd Avenue carry the container trucks. The Elizabeth River runs through the middle and floods in a big rain.'),
  P('The carriers come off the Turnpike at 13A and off 1 and 9 at North Avenue or Bayway. They meet at the outlet-mall lots at the port exit or the furniture store lot beside them. The big-box lots on 1 and 9 in Linden work too. The university lots on Morris Avenue work in summer. The county park lots in Roselle work year round. The airport is five minutes up 1 and 9 for a fly-and-ship. The train station reaches Penn Station in half an hour.'),
  P('Our office sits on Union Street at West Jersey Street, a few blocks from the train station.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Midtown, Elmora, Peterstown, Elizabethport, North Elizabeth, Westminster, Bayway, Keighry Head, Frog Hollow, Union, Hillside, Linden, Roselle, and Staten Island',
 prose(
  L('Elizabeth is two-family houses on narrow streets, a port on one side, a refinery on the other. The truck meets the wards on a main avenue and the suburbs at the curb.'),
  P('Midtown is Broad Street, the courthouse, the station, and the new apartment buildings around Union Square. The streets are one way with bus lanes. The handoff happens at a garage entrance or on West Jersey Street. Elmora is two-family houses on narrow streets with permit parking. The driver meets you on Morris Avenue or Elmora Avenue. Peterstown is the old Italian and Portuguese grid south of downtown, double-parked on both sides. The handoff happens on Elizabeth Avenue. North Elizabeth is the same story, and the handoff happens on North Broad Street.'),
  P('Elizabethport is the old port grid, with the waterfront park at the end of it. The streets are tight, and the driver meets you at the park lot or on First Street. Bayway is the refinery and the Goethals approach, and the handoff happens at the lots off Bayway Avenue. Westminster and Elmora Hills are bigger houses on wider streets with trees. The curb sometimes works, and a low limb moves the handoff to Westminster Avenue. Keighry Head and Frog Hollow are tight blocks near the port, and the handoff happens on Elizabeth Avenue.'),
  P('Union across the line is the university and postwar grids where the curb works. Hillside is the same. Linden is the old plant site, the strip on 1 and 9, and grids where the curb works. Roselle and Roselle Park are quiet grids, and the curb works. Staten Island sits across the Goethals, and the <a href="/city/auto-transport-staten-island-new-york/">Staten Island</a> page covers it. The outlet mall and the furniture store sit between the Turnpike and the port.'),
  P('Union, Hillside, Linden, Roselle, and Roselle Park ship with the same trucks and price the same as Elizabeth. Rahway and Cranford do too. Staten Island adds the bridge toll, which is built into the figure.'),
 )))

ROUTES=[("New York, NY","NJ Tpke/I-78 · ~15 mi","Same day","$100–$170"),("Allentown, PA","I-78 · ~75 mi","Same day","$160–$260"),
 ("Philadelphia, PA","NJ Tpke · ~80 mi","Same day","$160–$260"),("Hartford, CT","I-95/I-91 · ~120 mi","Same day","$190–$300"),
 ("Baltimore, MD","NJ Tpke/I-95 · ~175 mi","Same day","$220–$340"),("Washington, DC","NJ Tpke/I-95 · ~215 mi","Same day","$240–$360"),
 ("Boston, MA","I-95 · ~230 mi","1 day","$240–$360"),("Pittsburgh, PA","I-78/I-76 · ~355 mi","1 day","$330–$470"),
 ("Chicago, IL","I-80 · ~790 mi","2 days","$560–$820"),("Orlando, FL","I-95 · ~1,060 mi","3 days","$760–$1,080")]
BODY.append(rate_table('Lanes &amp; Costs','Elizabeth Car Shipping Lanes and Estimated Costs',
 'The lanes Union County cars run most, with open-trailer estimates. Price your exact lane on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Elizabeth, running sedan, open trailer. SUVs and pickups run 10 to 25 percent above, and enclosed sits higher still. The Turnpike tolls are inside the figure, and the week sets the rest.',
 prose(
  P('Elizabeth prices with Newark on every lane, because the same trucks serve both. New York is fifteen minutes up the Turnpike, one of the shortest lanes we run. Philadelphia, Baltimore, and Washington ride 95 south and run hourly. Allentown and Pittsburgh ride 78 west. Boston rides 95 north. The Florida lane fills in October with the snowbirds and in June with the families heading to Miami.'),
  P('The port’s peak season in the fall and the outlet-mall weekends in December make for a crowded calendar. The <a href="car-shipping-cost.html">cost guide</a> covers size, condition, and timing separately.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Port, the Airport, the Refinery, the Turnpike Warehouses, the University, the Hospital, the Families From Everywhere, and the Commuters',
 prose(
  L('Elizabeth relocates terminal managers, airport staff, refinery engineers, nurses, students, and families arriving from three continents. The port and the airport move the most.'),
  P('The port is the largest on the East Coast. Its terminals relocate managers and engineers from the other ports. The trucking companies around it hire drivers from across the region. The airport across the city line hires across Elizabeth, from the terminals to the hotels. The refinery at Bayway relocates engineers on turnaround schedules. The warehouses along the Turnpike from Elizabeth to Carteret relocate supervisors in spring and fall. The handoff happens at the lots nearest the gate. When the employer pays for the shipment, we write it up however it needs.'),
  P('Kean University in Union fills its campus each late August, and the county college’s Elizabeth campus follows. A parent books, and an adult signs at the lot. The hospital on Williamson Street brings nurses all year. Families arrive from Portugal, Brazil, Colombia, Peru, and the Dominican Republic. Many ship a car up from Miami. The commuters ride the train to Penn Station in half an hour and buy here for the price. The <a href="state-to-state-car-shipping.html">state-to-state</a> page explains the paperwork a state line adds.'),
  P('The joint base in Burlington County is an hour down the Turnpike. Its families pass through on the same calendar. The Coast Guard works the port from the Staten Island side. Ship Guy is a private broker and not part of the port or the base. The <a href="military-car-shipping.html">military</a> page covers orders and the dates they set.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Port’s Peak Season, the Outlet-Mall Weekends, the Fireworks, the Parades, Move-In Week, Sandy, Ida, the Blizzards, and the Wind on the Goethals',
 prose(
  L('Elizabeth runs on a port calendar and a shopping calendar. The weather problem is a surge up the Arthur Kill and a flash flood down the Elizabeth River.'),
  P('The port’s peak season runs from August through October. The container trucks fill North Avenue and Dowd Avenue. The outlet mall fills exit 13A every weekend from Thanksgiving to New Year’s. The Fourth of July fireworks fill the waterfront park in Elizabethport. The summer festivals close Elizabeth Avenue a few weekends each year. Move-in week fills the university in late August. Give a December weekend or a late-August date three weeks of notice.'),
  P('Sandy in October 2012 pushed the surge up the Arthur Kill into Elizabethport and the port. The terminals closed for a week, and the refinery shut down. Ida in September 2021 put the Elizabeth River through the low streets. It flooded hundreds of cars in a night. In a flood the carriers stay on the Turnpike, and the low pickups wait a day.'),
  P('The January 2016 blizzard dropped more than two feet. The twin storms of February 2010 did nearly as much. The Turnpike closes to trucks in a big storm, and the carriers wait in Linden or Newark. A winter pickup can slip two days. A strong wind closes the Goethals and the Turnpike bridges to high-profile vehicles. The Staten Island pickups wait for it to drop. Summer brings heat off the asphalt and a storm most afternoons that passes in an hour.'),
 )+chips(["Midtown","Union Square","Elmora","Elmora Hills","Peterstown","Elizabethport","North Elizabeth","Westminster","Bayway","Keighry Head","Frog Hollow","The Port","Union","Hillside","Linden","Roselle","Roselle Park","Kenilworth","Cranford","Rahway","Staten Island"])
 +NOTE('Serving Elizabeth, Union County, and the port towns, Elmora two-family or Westminster side street. Tell us the ward and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Elizabeth?',
 prose(
  L('Open trailers carry most of Union County’s cars, and the table above assumes one.'),
  P('Enclosed keeps the port dust, the road salt, and the brine off the paint. The engineers moving a car worth more than the relocation book it. So do the families shipping a car up from Miami that they want to arrive clean. When a storm is coming and only an open truck has room, we tell you that first.'),
  P('A commuter car or a student’s sedan rides open and arrives fine. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages lay out the difference.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A figure, a lot at the port exit, and a signature when the car comes down the ramp. The start date or the sailing date picks the week.'),
  P('Approve the figure, and we place the car with a carrier already on the Turnpike that week. The lot and the window come back the same day. The driver photographs the car at pickup and records its condition on the Bill of Lading. You initial it, and it governs the delivery check.'),
 )+ULI([
  "Your belongings out of the cabin and the trunk",
  "Fuel at a quarter tank or less",
  "Photos of every side and the odometer before the truck comes",
  "A working key and a note on known faults",
  "Aftermarket alarms disabled",
  "In Elmora, Peterstown, or Elizabethport, expect a lot at the port exit",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> page walks the steps, and the <a href="car-shipping-preparation.html">preparation</a> page covers pickup morning.'))))

BODY.append(sec('Why Ship Guy','Why Elizabeth Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already run the Turnpike past the port every hour. We know which wards never take a trailer and when the wind closes the Goethals.'),
  P('Our FMCSA license and our $75,000 bond are on the federal register for anyone to check. The office is on Union Street near the train station.'),
  P('One person at Ship Guy handles the move from quote to delivery call. The <a href="services.html">services</a> page covers open, enclosed, and expedited in turn.'),
 )))

BODY.append(office('Elizabeth','30 Union St #322','Elizabeth, NJ 07202','+19087749448','(908) 774-9448','ET',
 '30+Union+St+%23322,+Elizabeth,+NJ+07202','Visit Us','Find Ship Guy in Elizabeth',
 'Our office sits on Union Street at West Jersey Street, a few blocks from the train station.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3735.696005228985!2d-74.21731369999999!3d40.6654492!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c24d49791c2921%3A0xc2225306a82c27e7!2sShip%20Guy%20Auto%20Transport!5e1!3m2!1sen!2sus!4v1794237411721!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Elizabeth to New York or Florida?","New York runs one hundred to one hundred seventy dollars for a sedan, fifteen minutes up the Turnpike. It is one of the shortest lanes we run. Orlando runs seven hundred sixty to one thousand eighty and takes three days. Philadelphia runs one hundred sixty to two hundred sixty. An SUV or a pickup adds 10 to 25 percent."),
 ("Can the carrier come to my street in Elmora or Peterstown?","No. Elmora is two-family houses on narrow streets with permit parking, and Peterstown is double-parked on both sides. The driver meets you on Morris Avenue, on Elizabeth Avenue, or at the outlet-mall lots. Westminster, Union, Linden, and Roselle sometimes allow the curb."),
 ("Can you ship a car that arrived through the port?","Yes, once customs releases it. The ocean leg is an international process we do not arrange. Send us the release date and the terminal name, and we ship the car domestically like any other. A high-value import can ride enclosed from the terminal gate."),
 ("Do you ship cars for the port, the airport, or the refinery?","Yes, every week. The terminals relocate managers from the other ports, and the airport hires across the city. The refinery relocates engineers on turnaround schedules. The warehouses along the Turnpike move supervisors in spring and fall. When the employer pays, we write it up however it needs."),
 ("Can you ship a car for a Kean or county college student?","Yes. Kean fills its campus in Union in late August, and the cars leave in May. A parent books, and an adult signs at the campus lot on Morris Avenue. The county college’s Elizabeth campus works the same way."),
 ("What happens if a storm floods the low streets on my pickup day?","The carriers stay on the Turnpike, and the low pickups wait a day. Sandy in 2012 pushed the surge into Elizabethport and closed the terminals for a week. Ida in 2021 flooded hundreds of cars along the Elizabeth River in a night. We call when the forecast turns, and the figure stays where it was."),
 ("Does the wind on the Goethals affect a Staten Island shipment?","Sometimes. A strong wind closes the Goethals and the Turnpike bridges to high-profile vehicles. A loaded carrier is one. The Staten Island pickups wait a few hours for it to drop. The bridge toll is built into the figure."),
 ("Can you ship a car to or from Union, Linden, or Staten Island?","Yes. Union, Hillside, Linden, Roselle, and Roselle Park ride the same carriers and price the same as Elizabeth. Rahway and Cranford do too. Staten Island sits across the Goethals and adds the toll, which is inside the figure."),
 ("Can you ship a car that does not run from Elizabeth?","Yes. The carrier brings a winch, and the figure includes the loading time. The outlet-mall lots and the Linden big-box lots are flat. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for an Elizabeth car shipping quote?","Both addresses, with the ward or the building name. The year, make, and model, and whether it runs. Open or enclosed, and the week around the start date or the release date. With those, the Elizabeth figure comes back the same day."),
]
BODY.append(faq_section(FAQ,'Elizabeth FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Elizabeth?','Two minutes on the form above puts an Elizabeth figure on your lane. Tell us the ward and the week, and a carrier already on the Turnpike takes it.','+19087749448','(908) 774-9448','Get your free Elizabeth quote'))

build({
 'slug':'auto-transport-elizabeth-new-jersey',
 'title':'Car Shipping in Elizabeth, NJ — Auto Transport | Ship Guy',
 'meta':'Car shipping in Elizabeth, NJ, at the Turnpike exits for the port and the Goethals Bridge. The port, the airport, the refinery, and the Turnpike warehouses, main-avenue handoffs for Elmora, Peterstown, and Elizabethport, curbside pickups in Union, Linden, and Roselle, imports released from the terminals, the outlet-mall weekends, Sandy, and Ida. Local office on Union Street near the train station. Free quote.',
 'h1':'Car Shipping in<br>Elizabeth, <span class="accent">New Jersey</span>',
 'lede':'Open, enclosed, and expedited auto transport across Elizabeth, Union County, and the port towns, planned around the Turnpike, the port calendar, the start dates, the floods, and the wind on the Goethals.',
 'tel':'+19087749448','disp':'(908) 774-9448','brand':'Elizabeth','keyword':'car shipping in elizabeth',
 'localterms':['elizabeth','turnpike','exit 13','exit 13a','interstate 278','goethals','twin spans','routes 1 and 9','viaduct','route 27','route 28','route 439','broad street','bus lanes','elizabeth avenue','morris avenue','elmora avenue','north avenue','dowd avenue','bayway avenue','west jersey street','union street','first street','westminster avenue','elizabeth river','arthur kill','midtown','courthouse','station','union square','elmora','two-family','permit parking','peterstown','portuguese','double-parked','elizabethport','waterfront park','north elizabeth','westminster','elmora hills','bayway','refinery','keighry head','frog hollow','union','hillside','linden','old plant site','roselle','roselle park','kenilworth','cranford','rahway','staten island','the port','terminals','largest on the east coast','container trucks','trucking companies','airport','warehouses','carteret','kean university','county college','hospital','williamson street','portugal','brazil','colombia','peru','dominican republic','miami','commuters','penn station','joint base','burlington county','coast guard','peak season','august through october','outlet mall','furniture store','thanksgiving','fireworks','festivals','move-in','sandy','october 2012','ida','september 2021','hundreds of cars','january 2016','two feet','february 2010','high-profile','asphalt','new york','allentown','philadelphia','hartford','baltimore','washington','boston','pittsburgh','chicago','orlando','snowbirds','fly-and-ship','county park','port dust','salt','brine','bill of lading','fmcsa','winch','customs','release date'],
}, BODY, FAQ)
