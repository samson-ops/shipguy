import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Daytona Beach, Florida','Car shipping where two interstates meet and the whole year is an event',
 ['Car shipping in Daytona Beach starts where Interstate 4 ends at Interstate 95, five miles from the ocean and one mile from the speedway.',
  'Ship Guy is a licensed auto transport broker with an office on Seabreeze Boulevard on the beachside. We book vetted carriers across Volusia and Flagler Counties, and we do not own the trucks.',
  'Every carrier between Orlando and the coast, and every carrier running Interstate 95 between the Northeast and Miami, passes the Daytona interchange. Few Florida cities of this size see that much truck traffic.',
  'This page covers the interchange and the bridges, the event calendar that fills the city, the beachside and the mainland, the snowbirds from Ormond to Palm Coast, the aviation university, and the lanes north and south.'],
 'Daytona Beach at a glance',
 ['Most pickups happen within 1 to 3 days, with two interstates bringing carriers through the interchange.',
  'Orlando and Jacksonville are same-day lanes. Tampa and Miami take a day. Atlanta and Charlotte take one to two, and New York runs three.'],
 'Tell us the week you need. Speedweeks, Bike Week, Biketoberfest, and spring break close the beachside bridges to a trailer for days at a time.'))

BODY.append(sec('The Interchange &amp; the Bridges','Interstate 95, Interstate 4, and Crossing the River',
 prose(
  L('Daytona Beach is one of two places in Florida where two interstates meet, and the river decides the last mile.'),
  P('Interstate 4 arrives from Orlando and ends at Interstate 95 on the west side of the city. International Speedway Boulevard runs from the interchange past the speedway and the airport to the mainland downtown and over the river to the beach.'),
  P('The Halifax River separates the beachside from the mainland, and six bridges cross it from Ormond Beach to Port Orange. The Seabreeze and International Speedway bridges carry most of the traffic, and the Dunlawton bridge serves Port Orange.'),
  P('US 1 runs the mainland north and south, State Road A1A runs the beachside, and US 92 and State Road 44 reach DeLand and New Smyrna Beach. LPGA Boulevard reaches the newer communities on the west side.'),
  P('A carrier can reach the mainland from the interchange in ten minutes. The beachside adds a bridge, and on an event week it adds hours.'),
 ), alt=True))

BODY.append(sec('The Calendar','Speedweeks, Bike Week, Biketoberfest, and Spring Break',
 prose(
  L('Daytona Beach hosts a crowd bigger than the city several times a year, and each one fills the roads.'),
  P('Speedweeks build to the 500 in February, and the roads around the speedway and the interchange jam for ten days. Bike Week follows in early March with hundreds of thousands of riders, and Main Street on the beachside closes to everything else.'),
  P('Spring break fills the beachside in March, the summer race in August fills the speedway again, and Biketoberfest fills the city for a long weekend in October. Jeep Beach in April adds another.'),
  P('We schedule beachside pickups before or after each event, and the mainland runs normally during most of them. The interchange itself moves even on race day, just slowly.'),
  P('Some fans ship a car down for Speedweeks or Bike Week instead of renting. Book early, because February and March overlap with seasonal cars heading home.'),
 )))

ROUTES=[("Orlando, FL","I-4 · ~55 mi","Same day","$150–$240"),("Jacksonville, FL","I-95 · ~90 mi","Same day","$170–$280"),
 ("Gainesville, FL","SR-40/US-441 · ~100 mi","Same day","$170–$280"),("Tampa, FL","I-4 · ~140 mi","Same day","$180–$290"),
 ("West Palm Beach, FL","I-95 · ~200 mi","Same day","$220–$340"),("Miami, FL","I-95 · ~260 mi","1 day","$250–$380"),
 ("Atlanta, GA","I-95/I-75 · ~440 mi","1–2 days","$380–$540"),("Charlotte, NC","I-95/I-26/I-77 · ~500 mi","1–2 days","$420–$600"),
 ("Washington, DC","I-95 · ~800 mi","2–3 days","$580–$840"),("New York, NY","I-95 · ~1,030 mi","3 days","$720–$1,030")]
BODY.append(rate_table('Lanes &amp; Costs','Daytona Beach Car Shipping Lanes and Estimated Costs',
 'The lanes Volusia County households ask about most, with estimated open-transport ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates, running sedan, open trailer. SUVs and pickups run about 10 to 25 percent more, enclosed more still. Snowbird season and the event weeks swing the Interstate 95 lanes, and carrier availability on your dates sets the real quote.',
 prose(
  P('Orlando is the cheapest lane in the region, an hour down Interstate 4 on a road carriers run all day. Interstate 95 makes Jacksonville and Miami easy in either direction.'),
  P('The Northeast lane runs full southbound each fall and northbound each spring. The <a href="car-shipping-cost.html">cost guide</a> explains the rest of the number.'),
 ), alt=True))

BODY.append(sec('The Beachside &amp; the Mainland','Condos on A1A, Old Streets, and the Handoff',
 prose(
  L('The beachside is where the visitors stay, and the mainland is where the trucks fit.'),
  P('Oceanfront condos along State Road A1A run on garages and valets, and the old streets between Seabreeze Boulevard and Main Street are narrow. The driver meets you at a lot near the bridge or on the mainland side of it.'),
  P('Daytona Beach Shores and Ponce Inlet to the south are the same, with condo towers and one road in. Ormond Beach to the north has wide streets on the mainland and the famous canopy on the Loop, which no trailer enters.'),
  P('The mainland is easy. Port Orange, Holly Hill, and the LPGA and Latitude communities on the west side have wide streets, and the truck usually reaches the curb. Many have gates, so send the community name.'),
  P('Our office is on Seabreeze Boulevard on the beachside, a few blocks from the pier and the Seabreeze bridge.'),
 )))

BODY.append(sec('The Snowbirds','Ormond, Port Orange, New Smyrna, and Palm Coast',
 prose(
  L('The stretch of coast from Palm Coast to New Smyrna Beach fills every winter, and the cars arrive by trailer.'),
  P('Retirees from New York, New Jersey, Ohio, Michigan, and Canada fill Ormond Beach, Port Orange, and New Smyrna Beach from October through April. Many ship a car down in the fall and home in the spring rather than drive the corridor twice.'),
  P('Palm Coast to the north is one of the fastest-growing cities in the state, and its neighborhoods add streets faster than carrier maps update. Send the full address.'),
  P('Canadian snowbirds hand off on the Florida side, since we arrange domestic shipping only. Two to three weeks of notice in October and April keeps the price steady, and our <a href="snowbird-car-shipping.html">snowbird</a> page has the planning tips.'),
  P('The retirement communities off LPGA Boulevard ship on the same calendar, and their gates need a community name.'),
 ), alt=True))

BODY.append(sec('The University &amp; the Employers','Embry-Riddle, the Colleges, and the Headquarters',
 prose(
  L('Daytona Beach trains pilots, and the students arrive with cars.'),
  P('The aeronautical university beside the airport brings students from every state each August and sends them home each May, and many ship a car rather than fly one way. The campus lots are tight, so the driver meets you at a lot on International Speedway Boulevard.'),
  P('Bethune-Cookman on the mainland and the state college run the same calendar, and the homecoming weekend fills the mainland each fall. An adult signs for a student car.'),
  P('The racing sanctioning body, the insurance brokerage, and the hospital systems headquartered here relocate employees on start dates all year. If your employer reimburses the shipment, we provide the documentation.'),
  P('The interstate leg of a relocation is on the <a href="state-to-state-car-shipping.html">state-to-state</a> page.'),
 )+chips(["Beachside","Seabreeze","Main Street","Daytona Beach Shores","Ponce Inlet","Ormond Beach","Ormond-by-the-Sea","Holly Hill","Port Orange","South Daytona","LPGA","Latitude Margaritaville","New Smyrna Beach","Edgewater","DeLand","Deltona","Palm Coast","Flagler Beach","Bunnell"])
 +NOTE('Serving Volusia and Flagler Counties. Tell us the week, the side of the river, and the community name.')))

BODY.append(sec('Weather','Hurricanes, Erosion, and the Afternoon Storm',
 prose(
  L('The coast here has taken direct and glancing hits in the last decade, and the beach itself moves.'),
  P('Hurricane season runs June through November, and the beachside evacuates first. Carriers clear the coast days before a landfall, and the recent storms washed out the seawalls in the Shores and Wilbur-by-the-Sea.'),
  P('Nor\u2019easters erode the beach in fall and winter, and summer storms roll in most afternoons. Neither changes more than the loading hour.'),
  P('We tell you the moment the forecast changes the plan, and we never send a driver into an evacuation zone.'),
 ), alt=True))

BODY.append(sec('Your Options','Open or Enclosed in Daytona Beach?',
 prose(
  L('Open transport is the everyday choice, and the seasonal lane runs on it.'),
  P('Enclosed transport keeps a car covered against salt air, sand, and storm debris. Race weeks and the collector cars in Ormond keep enclosed carriers busy here.'),
  P('A commuter car rides open without a problem. Our <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages compare the two.'),
 )))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff on the right side of the river, and a delivery, with the event calendar deciding the week.'),
  P('Once the price is approved, a carrier on Interstate 95 or 4 takes the booking. The driver notes the car\u2019s condition on a Bill of Lading, and you sign it at loading. That note is your checklist at delivery.'),
 )+ULI([
  "Remove personal belongings",
  "Keep about a quarter tank of fuel",
  "Photograph the vehicle before pickup",
  "Provide a working key and disclose mechanical issues",
  "Turn off aftermarket alarms",
  "For a beachside condo or a gated community, plan to meet the truck at the bridge or the entrance",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> guides go step by step.')), alt=True))

BODY.append(sec('Why Ship Guy','Why Daytona Beach Drivers Choose Ship Guy',
 prose(
  L('We know the event calendar, the bridges, and which week the beachside closes to a truck.'),
  P('Active FMCSA brokerage authority and a $75,000 surety bond stand behind every Ship Guy booking, and our office is on Seabreeze Boulevard.'),
  P('One coordinator carries the shipment from quote to delivery and books open, enclosed, or expedited transport. The <a href="services.html">services</a> page lists everything we arrange.'),
 )))

BODY.append(office('Daytona Beach','444 Seabreeze Blvd Suite 482','Daytona Beach, FL 32118','+13867667915','(386) 766-7915','ET',
 '444+Seabreeze+Blvd+Suite+482,+Daytona+Beach,+FL+32118','Visit Us','Find Ship Guy in Daytona Beach',
 'Our office is on Seabreeze Boulevard on the beachside, a few blocks from the pier and the Seabreeze bridge.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4297.637479484155!2d-81.014698!3d29.2344252!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x88e6db6a73bbdbe9%3A0xdc65c1b19a7dcda6!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1790274878513!5m2!1sen!2sus', map_link='https://maps.app.goo.gl/DWfaoKHT4h5gHV9cA'))

FAQ=[
 ("Can you pick up on the beachside during Bike Week or Speedweeks?","Before or after, yes. Main Street closes to everything but motorcycles during Bike Week, and the roads around the speedway jam for ten days in February. We schedule beachside pickups around each event, and the mainland runs normally during most of them. Tell us the week when you request the quote."),
 ("Can the carrier come to my condo on A1A?","To a lot near the bridge or the mainland side of it. Oceanfront condos run on garages and valets, and the old streets between Seabreeze and Main Street are narrow. The driver names the spot before dispatch, and it is a few minutes from the building."),
 ("How much does it cost to ship a car from Daytona Beach to New York?","Usually seven hundred twenty to a thousand thirty dollars for a sedan riding open. Interstate 95 runs the whole way, about a thousand miles. Northbound cars in April and May cost more than in summer, because the seasonal residents head home then. Larger vehicles and enclosed add to it."),
 ("When should snowbirds in Ormond or Port Orange book?","Two to three weeks ahead in the busy windows. Southbound demand builds from October through December, and the return runs from April through June. Booking early keeps carrier options open. Canadian residents hand off on the Florida side, since we arrange domestic shipping only."),
 ("Do you ship cars for Embry-Riddle students?","Yes, students arrive from every state each August and leave each May, and many ship a car rather than fly one way. The campus lots are tight, so the driver meets you at a lot on International Speedway Boulevard. An adult signs for the car, and a parent can sign at the far end."),
 ("Do you serve Palm Coast, New Smyrna Beach, and DeLand?","Yes, Volusia and Flagler Counties are covered from this page. Palm Coast adds streets faster than carrier maps update, so send the full address. New Smyrna Beach has the same beachside handoff as Daytona, and DeLand ships on the Interstate 4 lane."),
 ("Why is Orlando so cheap from Daytona Beach?","Because Interstate 4 runs straight there in an hour, and carriers work that road all day. It usually costs one hundred fifty to two hundred forty dollars for a sedan. Jacksonville on Interstate 95 is nearly as easy."),
 ("Can you ship a race car or a collector car for a race week?","Yes, enclosed carriers stay busy here around the February and August races. An enclosed booking benefits from flexible dates, and the speedway infield and the garages have their own access rules. Tell us the event and the days you need the car there."),
 ("Can you ship a car that does not run from Daytona Beach?","Yes, non-running cars ship out of Daytona Beach regularly. A winch-equipped carrier loads it, and the added time carries a fee. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Daytona Beach car shipping quote?","The pickup and delivery addresses, with the side of the river and the community name. The year, make, and model. Whether it runs and rolls. Open or enclosed, the week you need, and your dates. That is everything an accurate Daytona Beach quote needs."),
]
BODY.append(faq_section(FAQ,'Daytona Beach FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Daytona Beach?','A quote takes about two minutes on our form. Then tell us your week and your side of the river, and we will plan around the calendar.','+13867667915','(386) 766-7915','Get your free Daytona Beach quote'))

build({
 'slug':'auto-transport-daytona-beach-florida',
 'title':'Car Shipping in Daytona Beach, FL — Auto Transport | Ship Guy',
 'meta':'Car shipping in Daytona Beach, FL where Interstate 4 meets 95. Speedweeks, Bike Week, and Biketoberfest timing, beachside condo handoffs, the Ormond-to-Palm Coast snowbird lane, Embry-Riddle students, race-week enclosed transport. Local office on Seabreeze Boulevard. Free quote.',
 'h1':'Car Shipping in<br>Daytona Beach, <span class="accent">Florida</span>',
 'lede':'Open, enclosed, and expedited auto transport across Volusia and Flagler Counties, planned around the bridges and the calendar.',
 'tel':'+13867667915','disp':'(386) 766-7915','brand':'Daytona Beach','keyword':'car shipping in daytona beach',
 'localterms':['daytona beach','volusia','flagler','interstate 95','interstate 4','interchange','international speedway','speedway','halifax','bridge','seabreeze','main street','a1a','us 1','lpga','speedweeks','500','bike week','biketoberfest','spring break','jeep beach','beachside','mainland','shores','ponce inlet','ormond','loop','holly hill','port orange','latitude','snowbird','palm coast','new smyrna','edgewater','deland','deltona','embry-riddle','aeronautical','bethune-cookman','headquarters','hurricane','erosion','canada'],
}, BODY, FAQ)
