import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Cincinnati, Ohio','Car shipping on the river, where three states share one set of carriers',
 ['Car shipping in Cincinnati is a three-state booking with one bridge in the middle of it. Ship Guy is a licensed auto transport broker with an office on Vine Street downtown.',
  'We book vetted carriers across the metro, from West Chester and Mason to Northern Kentucky. We do not own the trucks.',
  'Interstate 75 and 71 share the Brent Spence Bridge over the Ohio River. Interstate 74 reaches Indiana, and Interstate 275 loops all three states. The hills on both sides of the river decide where the truck can stop.',
  'This page covers the interstates and the bridge, the hillside neighborhoods, and the headquarters and the hospitals. It also covers the Kentucky side, the river, game days, and the lanes in every direction.'],
 'Cincinnati at a glance',
 ['Most pickups happen within 1 to 3 days. Interstate 75 carries the Detroit-to-Florida traffic through the city every day.',
  'Columbus, Louisville, Lexington, and Indianapolis are same-day lanes. Cleveland, Detroit, Nashville, and Chicago take a day. Florida runs two to three.'],
 'Tell us the neighborhood. Mount Adams, Clifton, and Hyde Park need a meeting spot on the flat. Mason, West Chester, and Florence usually meet the truck at the curb.'))

BODY.append(sec('The Interstates','75, 71, 74, the Loop, and the Brent Spence Bridge',
 prose(
  L('Cincinnati is where the busiest truck bridge in the Midwest crosses a river between two states.'),
  P('Interstate 75 runs north to Dayton, Toledo, and Detroit, and south through Kentucky to Atlanta and Florida. Interstate 71 shares the downtown stretch, then splits northeast to Columbus and southwest to Louisville. Both cross the river on the Brent Spence Bridge.'),
  P('The bridge carries more trucks than it was built for. A companion span is going up beside it, and the work zone slows the crossing. Carriers time the bridge for off-peak hours. Some use the Interstate 275 crossings at either end of the metro instead.'),
  P('Interstate 74 runs northwest to Indianapolis. Interstate 275 loops through Ohio, Kentucky, and Indiana, and Interstate 471 reaches Newport. The Norwood Lateral and the Cross County Highway cross the north side of the city.'),
  P('The Roebling bridge downtown bans trucks. The Kentucky and Indiana suburbs share the Cincinnati carrier pool. No crossing in the metro charges a toll.'),
 ), alt=True))

BODY.append(sec('The Hills','Mount Adams, Clifton, Hyde Park, Indian Hill, and the Flat Suburbs',
 prose(
  L('Cincinnati was built on seven hills, and a seventy-five-foot trailer cannot climb most of them.'),
  P('Mount Adams, Mount Auburn, and Mount Lookout have steep, narrow streets with no room to stop a trailer. Over-the-Rhine and downtown run on garages and tight blocks. The driver meets you on the riverfront, on Central Parkway, or at a lot near Interstate 71. Our office sits on Vine Street a block from the square.'),
  P('Clifton, Corryville, and Northside near the university are dense student blocks. Hyde Park, Oakley, and East Walnut Hills are tree-lined with cars on both curbs. The handoff happens on Madison Road, Reading Road, or at a plaza in Oakley.'),
  P('Indian Hill, Mariemont, and the river villages sit on winding estate roads. The driver meets you on Wooster Pike or at the village edge. Mason, West Chester, Blue Ash, and Montgomery are wide grids where the truck usually reaches the curb.'),
  P('On the Kentucky side, Covington and Newport are tight near the river. They open up toward Fort Mitchell and Florence. Lawrenceburg and the Indiana towns schedule on Interstate 275.'),
 )))

ROUTES=[("Lexington, KY","I-75 · ~85 mi","Same day","$160–$260"),("Louisville, KY","I-71 · ~100 mi","Same day","$170–$280"),
 ("Columbus, OH","I-71 · ~110 mi","Same day","$170–$280"),("Indianapolis, IN","I-74 · ~110 mi","Same day","$170–$280"),
 ("Cleveland, OH","I-71 · ~250 mi","1 day","$250–$370"),("Detroit, MI","I-75 · ~260 mi","1 day","$250–$380"),
 ("Nashville, TN","I-71/I-65 · ~270 mi","1 day","$260–$390"),("Chicago, IL","I-74/I-65 · ~300 mi","1 day","$290–$420"),
 ("Atlanta, GA","I-75 · ~460 mi","1 day","$400–$570"),("Tampa, FL","I-75 · ~900 mi","2–3 days","$680–$970")]
BODY.append(rate_table('Lanes &amp; Costs','Cincinnati Car Shipping Lanes and Estimated Costs',
 'The lanes that leave Cincinnati most often, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a running sedan, open trailer. An SUV or pickup adds about 10 to 25 percent, and enclosed adds more again. Season and the carriers available on your dates set the final price.',
 prose(
  P('Four cities sit within two hours of the bridge. Those lanes price about as low as any in the country. Interstate 75 carries the Florida traffic straight south through Knoxville and Atlanta.'),
  P('The Florida lane swings with the fall migration more than with the mileage. The <a href="car-shipping-cost.html">cost guide</a> explains the rest of the number.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Headquarters, the University, the Hospitals, and the Airport Hubs',
 prose(
  L('Cincinnati relocates people on corporate start dates, the medical calendar, and the shifts at two air cargo hubs.'),
  P('The consumer-products and grocery headquarters downtown transfer staff in from every region on start dates. The jet-engine plant in Evendale and the uniform company in Mason do the same. If your employer reimburses the shipment, we send the documentation it asks for.'),
  P('The university in Clifton brings tens of thousands of students in each August. It sends them home each May. Its medical center and the children’s hospital next door bring in residents every June. The handoff happens on a wide road below the hill rather than in a hospital garage.'),
  P('The two cargo hubs at the airport in Northern Kentucky run overnight shifts. They transfer managers in on start dates. The pickup happens in Hebron or Florence, never on the airport roads.'),
  P('Households moving to Florida and Texas for good are the other steady stream. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the longer move.'),
 )))

BODY.append(sec('The River &amp; the Calendar','Flood Season, Game Days, Oktoberfest, and the Marathon',
 prose(
  L('The Ohio River sets Cincinnati’s weather calendar, and the riverfront sets its traffic calendar.'),
  P('The river rises in late winter and spring. The riverfront roads and the low ground in the East End flood a few times a decade. Carriers stay on the interstates, and we move the handoff uphill when the river is up.'),
  P('Baseball and football downtown fill Fort Washington Way and the bridge approaches for hours. We schedule downtown and Northern Kentucky pickups around game days. Oktoberfest closes the downtown streets for a weekend in September, and the marathon closes them again in May.'),
  P('Winter brings ice more than snow, and the hills close before the main roads do. Spring brings storms and the occasional tornado warning, and the driver pulls off until it passes. Summer humidity on the river is the easy season.'),
 )+chips(["Downtown","Over-the-Rhine","Mount Adams","Mount Auburn","Clifton","Corryville","Northside","Walnut Hills","Hyde Park","Oakley","Mount Lookout","Columbia-Tusculum","Pleasant Ridge","Westwood","Price Hill","Delhi","Indian Hill","Mariemont","Madeira","Montgomery","Blue Ash","Kenwood","Sharonville","Mason","West Chester","Loveland","Anderson","Fairfield","Hamilton","Covington","Newport","Fort Mitchell","Florence","Lawrenceburg"])
 +NOTE('Serving Hamilton, Butler, Warren, and Clermont Counties, plus Northern Kentucky and the Indiana line. Tell us the neighborhood and whether the street is on a hill.'), alt=True))

BODY.append(sec('Your Options','Open or Enclosed in Cincinnati?',
 prose(
  L('Open trailers carry nearly every car that leaves Cincinnati, and the 75 lanes are priced for them.'),
  P('An enclosed trailer keeps salt, grit, and attention off the car. The garages in Indian Hill and Hyde Park book enclosed trailers. Many of the cars headed to Naples for the winter do too.'),
  P('A car you drive every day is fine in the open. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages spell out the trade-off.'),
 )))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a loading on the flat, and a delivery. The hills and the river decide the spot.'),
  P('Approve the price and we assign a carrier already running Interstate 75 or 71. When you meet, the driver writes up the car’s condition on a Bill of Lading. You both sign it, and delivery is checked against it.'),
 )+ULI([
  "Remove personal belongings",
  "Keep about a quarter tank of fuel",
  "Take photos of the car before pickup, especially after a salty winter",
  "Leave a working key and tell us about any mechanical issues",
  "Switch off any aftermarket alarm",
  "On a hillside street, plan to meet the truck at a plaza on the flat",
 ])+prose(P('Read the <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages for the rest of the details.')), alt=True))

BODY.append(sec('Why Ship Guy','Why Cincinnati Drivers Choose Ship Guy',
 prose(
  L('We work the bridge every day and plan around the hills, the river, and the game schedule.'),
  P('Ship Guy carries active FMCSA brokerage authority and a $75,000 surety bond, both searchable on the federal register. Our office is on Vine Street downtown.'),
  P('One person at Ship Guy owns your booking from the first quote to the last signature. Open, enclosed, and expedited transport are all on the table, and the <a href="services.html">services</a> page describes each.'),
 )))

BODY.append(office('Cincinnati','600 Vine St #748','Cincinnati, OH 45202','+15135966763','(513) 596-6763','ET',
 '600+Vine+St+%23748,+Cincinnati,+OH+45202','Visit Us','Find Ship Guy in Cincinnati',
 'Our office is on Vine Street downtown, a block from Fountain Square and minutes from the interstate ramps.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3821.818402547532!2d-84.5130085!3d39.1029029!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8841b15448381109%3A0xf38d2e0db1277e2e!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792064691872!5m2!1sen!2sus'))

FAQ=[
 ("Can the carrier come to my house in Hyde Park, Clifton, or Mount Adams?","Rarely. The streets are narrow, the hills are steep, and cars line both curbs. The driver meets you on Madison Road, Reading Road, or at a plaza on the flat. Mason, West Chester, Blue Ash, and Florence usually allow a curbside pickup."),
 ("Do you pick up on the Kentucky or Indiana side?","Yes. Covington, Newport, Florence, Fort Mitchell, and Lawrenceburg share the Cincinnati carrier pool and the same pricing. The handoff happens on the main roads near Interstate 75 or 275, away from the riverfront streets."),
 ("How much does it cost to ship a car from Cincinnati to Florida?","Figure six hundred eighty to nine hundred seventy dollars for a sedan to Tampa. Orlando and Naples add a little. The run is about nine hundred miles straight down Interstate 75. Fall southbound costs more than spring. SUVs and pickups add 10 to 25 percent."),
 ("Does the Brent Spence Bridge construction affect my pickup?","Only the timing. The companion bridge going up beside it slows the crossing. Carriers time the bridge for off-peak hours or use the Interstate 275 crossings. A downtown or Northern Kentucky handoff is planned around the work zone."),
 ("Do you ship cars for students at the University of Cincinnati or Xavier?","Yes. Student cars come in each August and go home each May. The streets in Clifton and Corryville are dense and parked solid. The driver meets you at a lot below the hill. An adult signs for the car at pickup."),
 ("Do you handle corporate relocations to the Cincinnati headquarters?","Yes, every week. The consumer-products, grocery, and uniform companies transfer staff in from every region on start dates. We plan the pickup around your first day. If your employer reimburses the shipment, we send the paperwork it asks for."),
 ("Does a Reds or Bengals game affect my pickup?","Downtown and on the Kentucky side, yes. Fort Washington Way and the bridge approaches fill for hours. We schedule those pickups around game days. The suburbs run normally."),
 ("What happens if the river floods on my pickup day?","We move the handoff uphill. The riverfront roads and the low ground in the East End go under a few times a decade. The interstates stay open, and the carriers keep rolling on them."),
 ("Can you ship a car that does not run from Cincinnati?","Yes. A winch truck takes it, and the longer loading shows up in the quote. The spot has to be flat, which matters on these hills. Tell us if it rolls, steers, and brakes."),
 ("What do you need for a Cincinnati car shipping quote?","The two addresses, with the Cincinnati neighborhood and whether it sits on a hill. The year, make, and model. Whether it runs. Open or enclosed, and your dates. A Cincinnati quote needs nothing else."),
]
BODY.append(faq_section(FAQ,'Cincinnati FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Cincinnati?','The form above gives you a price in about two minutes. Tell us the neighborhood and your dates. We will pair you with a carrier already crossing the bridge.','+15135966763','(513) 596-6763','Get your free Cincinnati quote'))

build({
 'slug':'auto-transport-cincinnati-ohio',
 'title':'Car Shipping in Cincinnati, OH — Auto Transport | Ship Guy',
 'meta':'Car shipping in Cincinnati, OH on Interstate 75 and 71. The Brent Spence Bridge work zone, hillside handoffs in Hyde Park and Clifton, Northern Kentucky pickups, headquarters relocations, UC and hospital timing, game days, the Florida lane. Local office on Vine Street. Free quote.',
 'h1':'Car Shipping in<br>Cincinnati, <span class="accent">Ohio</span>',
 'lede':'Open, enclosed, and expedited auto transport across three states, planned around the bridge, the hills, and the river.',
 'tel':'+15135966763','disp':'(513) 596-6763','brand':'Cincinnati','keyword':'car shipping in cincinnati',
 'localterms':['cincinnati','interstate 75','interstate 71','interstate 74','interstate 275','interstate 471','brent spence','roebling','norwood lateral','cross county','fort washington way','vine street','fountain square','downtown','over-the-rhine','mount adams','mount auburn','clifton','corryville','northside','hyde park','oakley','mount lookout','walnut hills','indian hill','mariemont','madison road','reading road','wooster pike','mason','west chester','blue ash','montgomery','covington','newport','fort mitchell','florence','hebron','lawrenceburg','headquarters','consumer-products','grocery','jet-engine','evendale','uniform','university','medical center','children','residents','cargo hubs','airport','river','flood','reds','bengals','oktoberfest','marathon','ice','tornado','florida','tampa','naples','columbus','louisville','lexington','indianapolis','cleveland','detroit','nashville','chicago','atlanta'],
}, BODY, FAQ)
