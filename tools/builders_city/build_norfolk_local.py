import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Norfolk, Virginia','Car shipping in the city with the world’s biggest naval base, between the tunnels and the tide',
 ['Car shipping in Norfolk runs on Interstate 64 and 264 and through the tunnels between them. Ship Guy is a licensed auto transport broker with an office on Granby Street downtown.',
  'We book vetted carriers across Norfolk, from Ghent to Ocean View and out to the base gates. The carriers own the trucks. Ship Guy holds the license and the bond.',
  'Interstate 64 comes in from Richmond through the Hampton Roads tunnel and loops the east side. Interstate 264 runs from the Portsmouth tunnel through downtown to Virginia Beach. Interstate 564 reaches the naval station. Hampton Boulevard, Tidewater Drive, and Military Highway carry the rest.',
  'This page covers 64, 264, 564, the tunnels, the tolls, downtown, Ghent, Ocean View, and the base gates. It also covers the Navy, the port, the hospitals, the universities, the nor’easters, and the tides.'],
 'Norfolk at a glance',
 ['Most pickups happen within 1 to 3 days. The Richmond carriers come down 64 daily, and the 95 trucks turn east at Petersburg. The port keeps a pool based on the Southside.',
  'Richmond, Raleigh, Washington, and Baltimore ride a single day on the truck. Philadelphia, Charlotte, and New York take a day. Atlanta takes one to two, and Florida takes two.'],
 'Tell us the neighborhood and the base, if there is one. Ghent, Freemason, Colonial Place, and the Ocean View lanes meet the truck on a main road. Larchmont, Wards Corner, Norview, Ingleside, and Lake Taylor usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 64, Interstate 264, Interstate 564, the Tunnels, Hampton Boulevard, Tidewater Drive, Military Highway, and the Tolls',
 prose(
  L('Norfolk is a peninsula with water on three sides and tunnels on every exit. A carrier picks its crossing before it picks its lot.'),
  P('Interstate 64 is the Richmond road. It comes down the Peninsula and dives under the harbor in the Hampton Roads tunnel. Then it loops the east side past the airport to Chesapeake. The tunnel is the busiest crossing in the state, and it backs up every summer weekend. A trailer that cannot clear it uses the Monitor-Merrimac tunnel on 664. Interstate 264 runs from the Portsmouth tunnel through downtown to Virginia Beach. The Downtown and Midtown tunnels charge a toll in both directions, and the toll rides inside the quote.'),
  P('Interstate 564 leaves 64 at Wards Corner and runs to the gates of the naval station. Hampton Boulevard runs from downtown past the university and the port to the same gates. Tidewater Drive runs north and south through the middle of the city. Military Highway is US 13, the east side road to the bay bridge-tunnel and the Eastern Shore. Little Creek Road runs to the amphibious base, and Ocean View Avenue runs the bayfront.'),
  P('The carriers come off 64 at Northampton or Tidewater and off 264 at Brambleton. The shopping center lots at Wards Corner are the usual meeting spot. The big-box lots on Military Highway work too. So do the stadium lots outside game days and the Ocean View lots on a weekday. The airport cell lot works for a fly-and-ship.'),
  P('Our office is on Granby Street downtown, a few blocks from Waterside and the MacArthur Center.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, Freemason, Ghent, Larchmont, Colonial Place, Park Place, Wards Corner, Ocean View, Norview, Berkley, and the Base Gates',
 prose(
  L('Norfolk is old brick on narrow streets near the harbor and postwar grids out toward the bay. The truck meets the old city on a main road.'),
  P('Downtown runs along Granby Street from the harbor north to the arena, towers and garages on one-way streets. The driver meets you at the garage entrances on Brambleton or at the Waterside lots. Freemason beside it is cobblestones and townhouses, and a trailer does not enter. Ghent north of downtown is the city’s old neighborhood, narrow streets of brick houses around the Hague. The handoff moves to Colley Avenue or Hampton Boulevard.'),
  P('Larchmont and Edgewater by the university are wider, and the curb usually works. Colonial Place and Riverview along the river are narrow again, and the driver meets you on Tidewater Drive. Park Place and Lambert’s Point between the university and the port are tight blocks packed with student cars. The handoff moves to the stadium lots.'),
  P('Wards Corner is the crossroads of the north side. The grids around it from Titustown to Norview are wide enough for a trailer. Ocean View along the bay is beach lanes from Willoughby Spit to East Ocean View. The handoff moves to Ocean View Avenue. The base housing at the naval station and Little Creek is behind the gates. The handoff happens outside them.'),
  P('Berkley and Campostella across the river on the Southside are plain grids where the curb works. Ingleside, Lake Taylor, and the blocks along Military Highway are the same. Virginia Beach and Chesapeake ship with the same trucks and price the same as Norfolk. So does Portsmouth through the tunnel. Hampton and Newport News across the harbor add the tunnel and nothing else.'),
 )))

ROUTES=[("Richmond, VA","I-64 · ~95 mi","Same day","$170–$280"),("Raleigh, NC","US-58/I-95 · ~190 mi","Same day","$230–$350"),
 ("Washington, DC","I-64/I-95 · ~200 mi","Same day","$230–$350"),("Baltimore, MD","I-64/I-95 · ~240 mi","Same day","$250–$380"),
 ("Philadelphia, PA","I-64/I-95 · ~280 mi","1 day","$270–$400"),("Charlotte, NC","US-58/I-85 · ~320 mi","1 day","$300–$440"),
 ("New York, NY","I-95 · ~370 mi","1 day","$350–$510"),("Atlanta, GA","I-85 · ~550 mi","1–2 days","$440–$630"),
 ("Jacksonville, FL","I-95 · ~590 mi","2 days","$450–$650"),("Orlando, FL","I-95 · ~740 mi","2 days","$520–$750")]
BODY.append(rate_table('Lanes &amp; Costs','Norfolk Car Shipping Lanes and Estimated Costs',
 'The lanes Norfolk cars run most, with estimated open-trailer ranges. Price your own route on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Norfolk, running sedan, open trailer. An SUV or a pickup runs 10 to 25 percent higher, and enclosed higher still. Tunnel tolls are inside the number where the route uses them. The week and the carriers free that week set the final figure.',
 prose(
  P('Norfolk prices with Virginia Beach on every lane, because the same trucks serve the whole Southside. The Richmond lane rides 64 and fills every day. The Carolina lanes ride 58 west to 95 and 85. The Florida lane rides 95 and fills each fall with the retirees and the sailors on orders. The New York lane rides 95 north through Washington.'),
  P('A report date in July or the August move-in lands in the busiest weeks of the year. The <a href="car-shipping-cost.html">cost guide</a> explains how size, condition, and timing move the number.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Navy, the Port, the Hospitals, the Two Universities, the Allied Command, and the Retirees',
 prose(
  L('Norfolk relocates sailors, longshoremen, nurses, professors, and foreign officers. The Navy moves more households than everyone else combined.'),
  P('The naval station at the end of Hampton Boulevard is the largest in the world. The amphibious base at Little Creek sits beside it. Sailors and families rotate on orders all year, with the summer peak the Navy calls the moving season. Housing sits behind the gates, so the truck meets you outside them or at Wards Corner. The Navy moves one car on orders. The family sends the second one with us. Ship Guy is a private broker with no tie to the Navy. The <a href="military-car-shipping.html">military</a> page explains how orders set the timing.'),
  P('The allied command on the base brings officers from thirty countries on tours that start all year. Their cars arrive by ship and leave by trailer. The port terminals on the river move managers on contract dates. The ships’ cars clear customs at the terminal. A private car that arrived by ship and cleared customs moves like any other car from that point. Send the release date and the terminal.'),
  P('The hospital system headquartered here runs the trauma center in Ghent and the children’s hospital beside it. Both bring residents each June and hire traveling nurses year round. The medical school across the street brings faculty on contract dates. The university on Hampton Boulevard takes student cars in late August. The university on Brambleton does the same. Both send them home in May. Mom or Dad books, and an adult signs at a lot.'),
  P('Retirees from the Navy stay for the water and leave for Florida each October. Families priced out of the beach buy in Norfolk and ship one car across. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the paperwork for crossing a state line.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Harborfest, the Tattoo, the Illumination, Move-In Week, the Moving Season, the Nor’easters, the Hurricanes, and the Tides',
 prose(
  L('Norfolk runs on a Navy calendar and a tide table. The weather problem is water in the streets a dozen times a year.'),
  P('Harborfest fills the downtown waterfront for a weekend in June and closes Waterside Drive. The tattoo fills the arena for a week in April, and the parade of nations closes Granby Street. The illumination parade closes downtown on a Saturday night in November. Move-in week in late August fills Lambert’s Point and the blocks around both campuses. The moving season at the base runs June through August and fills the carriers with second cars. Book three weeks ahead for a July date.'),
  P('The tide floods the Hague in Ghent and the Ocean View lanes a dozen times a year. A handoff in those blocks checks the tide table and moves to the afternoon. A nor’easter in the fall pushes the bay into Ocean View for a day. The November 2009 storm put Ocean View Avenue under for two days.'),
  P('The storms run June through November. Isabel in 2003 is still the benchmark. Matthew in 2016 dropped fourteen inches of rain on the city in a night. An evacuation order closes the tunnels, and the carriers stage in Richmond. A pickup in an evacuation waits for the all-clear, and we call the moment a watch goes up.'),
  P('Snow comes once every few years and shuts everything. The January 2018 storm dropped a foot and closed the tunnels and the bridges for two days. The carriers waited in Richmond until the Southside thawed. Summer brings heat and afternoon storms that shift the loading hour. The tunnel backups on a July weekend shift the whole day.'),
 )+chips(["Downtown","Granby Street","Waterside","Freemason","Ghent","The Hague","West Ghent","Larchmont","Edgewater","Colonial Place","Riverview","Park Place","Lambert's Point","Wards Corner","Titustown","Norview","Ocean View","Willoughby Spit","East Ocean View","Naval Station","Little Creek","Berkley","Campostella","Ingleside","Lake Taylor","Military Highway","Portsmouth","Hampton","Newport News"])
 +NOTE('Serving Norfolk and the whole Southside, Ghent block or Lake Taylor cul-de-sac. Tell us the neighborhood and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Norfolk?',
 prose(
  L('Open trailers carry most of the Southside, and the table above is priced for one.'),
  P('An enclosed trailer keeps off the salt air, the pollen, and the brine sprayed before a snow. The collectors in Ghent book one. So do the officers bringing a car back from a tour overseas. A car leaving ahead of a hurricane takes whatever truck is available, and we say so.'),
  P('A commuter car or a student car is fine on an open trailer. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages set the two side by side.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a meeting spot at Wards Corner, and a signature at delivery. The report date or the move-in picks the week.'),
  P('Approve the price, and a carrier already coming down 64 that week takes the car. Lot and window are settled the same afternoon. At pickup the driver photographs the car and writes its condition on the Bill of Lading. You initial the sheet, and it is the reference at delivery.'),
 )+ULI([
  "Everything personal out of the cabin and the trunk",
  "Fuel down to a quarter tank",
  "Photograph each side and the odometer before the truck comes",
  "One good key, and a note about any known faults",
  "Any add-on alarm turned off",
  "In Ghent, Freemason, Ocean View, or behind a gate, plan on a main road or a lot",
 ])+prose(P('Read the <a href="how-it-works.html">how it works</a> page for the sequence and the <a href="car-shipping-preparation.html">preparation</a> page for the pickup checklist.'))))

BODY.append(sec('Why Ship Guy','Why Norfolk Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already come down 64 every day. We know which tunnel a loaded trailer can take.'),
  P('Our FMCSA license and our $75,000 bond are a public record on the federal register. The office is on Granby Street downtown.'),
  P('The same coordinator answers from the quote until the car is delivered. The <a href="services.html">services</a> page compares open, enclosed, and expedited.'),
 )))

BODY.append(office('Norfolk','259 Granby St Ste 556','Norfolk, VA 23510','+17577863123','(757) 786-3123','ET',
 '259+Granby+St+Ste+556,+Norfolk,+VA+23510','Visit Us','Find Ship Guy in Norfolk',
 'Our office is on Granby Street downtown, a few blocks from Waterside and the MacArthur Center.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3940.9910309031766!2d-76.2907793!3d36.8496221!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89ba99f59d086cb1%3A0x9e844d7ceee18f33!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793629099305!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Norfolk to Florida or New York?","Orlando runs five hundred twenty to seven hundred fifty dollars for a sedan. That is about seven hundred forty miles down 95. New York runs three hundred fifty to five hundred ten, about three hundred seventy miles north. Richmond is ninety minutes away and the lowest lane on the table. An SUV or a pickup runs 10 to 25 percent higher."),
 ("Do you ship cars for sailors on orders to the naval station or Little Creek?","Yes, every week of the year. The Navy moves one car on orders, and the family sends the second one with us. Housing sits behind the gates, so the truck meets you outside them or at Wards Corner. Summer is the Navy’s moving season, so a July date wants three weeks of notice. Ship Guy is a private broker and has no tie to the Navy."),
 ("Are the tunnel tolls in my price?","Yes, when the route uses a tolled tunnel. The Downtown and Midtown tunnels charge both directions, and the bay bridge-tunnel charges too. The Hampton Roads and Monitor-Merrimac tunnels are free. Whichever crossing the carrier takes, the toll rides inside the quote and nothing is added at delivery."),
 ("Can the carrier come to my street in Ghent or Ocean View?","No. Ghent is narrow brick streets around the Hague, and Ocean View is beach lanes. The driver meets you on Colley Avenue, Hampton Boulevard, or Ocean View Avenue. Larchmont, Wards Corner, Norview, Ingleside, and Lake Taylor usually allow the curb."),
 ("Can you pick up a car that came through the port?","Yes. Once customs releases it and the terminal signs it out, it moves like any other car. We need the release date and the terminal name. The officers at the allied command ship cars in this way every month."),
 ("Can you deliver on an ODU or Norfolk State move-in date?","Yes. Both campuses take cars in late August and send them home in May. Mom or Dad books, and an adult signs at a lot. Lambert’s Point and the Brambleton blocks are full that week, so the meeting point is the stadium lots. The date sets the window."),
 ("Can you ship a car to or from Virginia Beach, Portsmouth, or Hampton?","Yes, and all three price the same as Norfolk. Virginia Beach rides the same carriers out 264, and the subdivisions allow the curb. Portsmouth rides them through the Downtown tunnel with the toll inside the quote. Hampton rides them through the Hampton Roads tunnel, and a tall trailer takes 664 instead."),
 ("What happens if a hurricane or a nor’easter hits on my pickup day?","A hurricane watch holds the truck in Richmond until the all-clear, and an evacuation closes the tunnels. A nor’easter puts the bay in the Ocean View lanes for a day, and the handoff moves inland. You hear from us the moment a watch goes up. A car leaving ahead of the storm takes whatever truck is available."),
 ("Can you ship a car that does not run from Norfolk?","Yes. We send a carrier with a winch and quote the loading time up front. The Wards Corner lots or the big-box lots on Military Highway are level. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Norfolk car shipping quote?","Start and finish, with the neighborhood and the base if there is one. Year, make, and model. Running or not. Open or enclosed. The week around the report date or the move. Give us those five, and the Norfolk number is back before the day ends."),
]
BODY.append(faq_section(FAQ,'Norfolk FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Norfolk?','Two minutes on the form above gets your lane a Norfolk number. Name the neighborhood and the week, and a carrier already coming down 64 takes it.','+17577863123','(757) 786-3123','Get your free Norfolk quote'))

build({
 'slug':'auto-transport-norfolk-virginia',
 'title':'Car Shipping in Norfolk, VA — Auto Transport | Ship Guy',
 'meta':'Car shipping in Norfolk, VA, home of the world’s largest naval base, between the tunnels and the tide. Navy PCS moves outside the gates, tunnel tolls inside the quote, port releases, hospital and university relocations, main-road handoffs for Ghent, Freemason, and Ocean View, curbside pickups in Larchmont, Wards Corner, Norview, and Lake Taylor, the nor’easters, and the hurricanes. Local office on Granby Street downtown. Free quote.',
 'h1':'Car Shipping in<br>Norfolk, <span class="accent">Virginia</span>',
 'lede':'Open, enclosed, and expedited auto transport across Norfolk and the Southside, planned around 64, 264, the tunnels, the Navy’s moving season, the campus calendar, and the tide.',
 'tel':'+17577863123','disp':'(757) 786-3123','brand':'Norfolk','keyword':'car shipping in norfolk',
 'localterms':['norfolk','naval base','tunnels','tide','interstate 64','264','granby street','downtown','ghent','ocean view','little creek','richmond','hampton roads','portsmouth','virginia beach','564','naval station','hampton boulevard','tidewater drive','military highway','tolls','base gates','navy','port','hospitals','universities','nor’easters','petersburg','southside','raleigh','washington','baltimore','philadelphia','charlotte','new york','atlanta','florida','freemason','colonial place','larchmont','wards corner','norview','ingleside','lake taylor','peninsula','harbor','chesapeake','airport','monitor-merrimac','664','midtown','eastern shore','bay bridge-tunnel','amphibious base','ocean view avenue','northampton','brambleton','shopping center','big-box','stadium','cell lot','fly-and-ship','waterside','macarthur center','arena','garages','cobblestones','townhouses','hague','colley avenue','edgewater','riverview','park place','lambert','titustown','willoughby spit','east ocean view','berkley','campostella','hampton','newport news','retirees','sailors','longshoremen','moving season','allied command','thirty countries','customs','release date','terminal','trauma center','children','medical school','late august','harborfest','tattoo','parade of nations','illumination','november 2009','isabel','2003','matthew','2016','fourteen inches','evacuation','january 2018','salt air','pollen','brine','bill of lading','fmcsa','west ghent','winch'],
}, BODY, FAQ)
