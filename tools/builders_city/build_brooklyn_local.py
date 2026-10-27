import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Brooklyn, New York','Car shipping for brownstone blocks, one-family streets, and a bridge that bans the truck',
 ['Car shipping in Brooklyn is a matter of picking the block where a trailer can stop. Ship Guy is a licensed auto transport broker with an office on Court Street in Downtown Brooklyn.',
  'We book vetted carriers for every neighborhood from Greenpoint to Coney Island. We do not own the trucks.',
  'The Brooklyn Bridge bans trucks, and the Belt, Ocean, and Eastern parkways do too. A seventy-five-foot carrier comes in over the Verrazzano or the Williamsburg Bridge. It works the BQE and the avenues. It meets you a few blocks from home.',
  'This page covers the bridges and the BQE, the meeting spots, and the brownstone-versus-driveway question. It also covers Fort Hamilton, the parades, the Florida lane, and the lanes down the corridor.'],
 'Brooklyn at a glance',
 ['Most pickups happen within 1 to 3 days. The meeting spot is an industrial block, a wide avenue, or a lot near the expressway.',
  'Philadelphia and Boston go the same day, and Washington the next. Florida takes three to four days, the West Coast seven to nine.'],
 'Tell us the neighborhood and whether you have a driveway. Park Slope and Williamsburg need a meeting spot. Marine Park, Mill Basin, and Dyker Heights often allow the curb.'))

BODY.append(sec('The Bridges &amp; the BQE','Which Crossings Carry a Trailer, and Which Roads Ban It',
 prose(
  L('Brooklyn has more bridges than any borough and fewer that a loaded carrier can use.'),
  P('The Brooklyn Bridge bans trucks outright. The Manhattan and Williamsburg bridges allow them with limits. The Verrazzano carries most of the carrier traffic in from Staten Island and New Jersey. It charges the biggest toll in the city.'),
  P('The Brooklyn-Queens Expressway is the only highway through the borough. The old cantilever under Brooklyn Heights runs two lanes each way. Carriers plan around it. The Gowanus Expressway connects the Verrazzano to downtown, and the Prospect Expressway reaches the middle of the borough.'),
  P('The Belt Parkway, Ocean Parkway, and Eastern Parkway all ban commercial vehicles. So does the Jackie Robinson. Atlantic Avenue, Flatbush Avenue, Fourth Avenue, and Linden Boulevard are the roads a trailer uses instead. So is Third Avenue under the Gowanus.'),
  P('Every crossing charges a toll, and any congestion fee in effect applies on the Manhattan side. The carrier pays all of it, and the quote you approve already has it inside.'),
 ), alt=True))

BODY.append(sec('The Meeting Spots','Sunset Park, Red Hook, Canarsie, and the Wide Avenues',
 prose(
  L('Brooklyn has a workable meeting spot within a ten-minute drive of every neighborhood. Most of them are industrial.'),
  P('For Park Slope, Carroll Gardens, Cobble Hill, and downtown, Sunset Park and Red Hook work best. The lots along Third Avenue under the Gowanus work the same way. Our office sits on Court Street near Borough Hall, in the middle of those neighborhoods.'),
  P('For Williamsburg, Greenpoint, and Bushwick, the warehouse blocks near the Navy Yard are the usual answer. For Bed-Stuy, Crown Heights, and Prospect Heights, Atlantic Avenue toward East New York works.'),
  P('For Flatbush, Midwood, and Borough Park, the handoff happens on Kings Highway or Linden Boulevard. Canarsie, Mill Basin, and Marine Park use the Flatbush Avenue lots toward the bay.'),
  P('Bay Ridge, Dyker Heights, and Bensonhurst meet the truck on Fourth Avenue or near the Verrazzano. Coney Island and Sheepshead Bay use the boardwalk-side lots in the off season.'),
 )))

ROUTES=[("Philadelphia, PA","I-95 · ~95 mi","Same day","$180–$290"),("Boston, MA","I-95 · ~220 mi","Same day","$240–$360"),
 ("Washington, DC","I-95 · ~230 mi","1 day","$250–$370"),("Buffalo, NY","I-87/I-90 · ~410 mi","1 day","$390–$550"),
 ("Charlotte, NC","I-95/I-85 · ~640 mi","2 days","$480–$690"),("Chicago, IL","I-80 · ~800 mi","2 days","$570–$830"),
 ("Atlanta, GA","I-95/I-85 · ~870 mi","2–3 days","$620–$890"),("Orlando, FL","I-95 · ~1,080 mi","3 days","$770–$1,090"),
 ("Miami, FL","I-95 · ~1,280 mi","3–4 days","$810–$1,160"),("Los Angeles, CA","I-80/I-40 · ~2,790 mi","7–9 days","$1,350–$1,800")]
BODY.append(rate_table('Lanes &amp; Costs','Brooklyn Car Shipping Lanes and Estimated Costs',
 'The lanes that leave Brooklyn most often, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a running sedan, open trailer, bridge tolls included. Add roughly 10 to 25 percent for an SUV or pickup, and more for enclosed. Season and carrier availability on your dates set the final price.',
 prose(
  P('Interstate 95 south is the flagship lane out of Brooklyn. The Florida volume keeps it priced like a short trip. Philadelphia is under two hours away once the truck clears the Verrazzano.'),
  P('A handoff on the Staten Island side of the bridge saves the carrier an hour of borough traffic. The quote reflects it. The <a href="car-shipping-cost.html">cost guide</a> explains the rest of the number.'),
 ), alt=True))

BODY.append(sec('Brownstones &amp; Driveways','Park Slope, Ditmas Park, Marine Park, and the Garages',
 prose(
  L('Brooklyn splits into blocks with driveways and blocks without, and the handoff follows that line.'),
  P('Park Slope, Fort Greene, Clinton Hill, Bed-Stuy, and Crown Heights are brownstone and rowhouse blocks. Cars park on both curbs under the alternate-side rules, and a trailer cannot stop. The driver meets you at the industrial spot nearest you.'),
  P('Ditmas Park, Midwood, Marine Park, Mill Basin, Bergen Beach, and Dyker Heights have driveways and wider streets. On those blocks the truck often reaches the curb, and the handoff happens at home.'),
  P('Downtown, Williamsburg, and the waterfront towers run on garages. Someone brings the car out and drives it a few minutes to the spot. Warn the garage a day ahead so nothing is parked in front of it.'),
  P('Alternate-side parking decides which curb is free on which morning. A meeting spot on a wide avenue avoids the ticket. Snow suspends the rules for a day or two.'),
 )))

BODY.append(sec('Who Ships Here','Fort Hamilton, the Hospitals, the Colleges, and the Florida Lane',
 prose(
  L('Brooklyn moves on orders, residency match days, college calendars, and the oldest snowbird lane in the country.'),
  P('Fort Hamilton in Bay Ridge is the only active post in the city. Families rotate through on orders all year. The post is gated, so the handoff happens on Fourth Avenue or by the Verrazzano lots. Orders usually cover one vehicle, and the second rides with us. The <a href="military-car-shipping.html">military</a> page covers the planning.'),
  P('The hospitals in Borough Park, Sunset Park, and East Flatbush bring in residents every summer. The colleges in Midwood, Clinton Hill, and downtown add student cars in August and May. An adult signs for a student car.'),
  P('Bay Ridge, Bensonhurst, Mill Basin, and Sheepshead Bay empty toward Boca Raton, Delray Beach, and Hallandale every fall. The cars come north again from April through June. Our <a href="snowbird-car-shipping.html">snowbird</a> page has the planning tips.'),
  P('Households relocating to Florida, Texas, and the Carolinas for good are the other steady stream. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the longer move.'),
 ), alt=True))

BODY.append(sec('The Calendar','The Parade, the Marathon, the Lights, and the Storms',
 prose(
  L('Brooklyn closes its widest avenues for its biggest days, and those are the avenues the truck needs.'),
  P('The West Indian Day Parade takes Eastern Parkway and the streets around it on Labor Day. The marathon closes Fourth Avenue, Lafayette, and Bedford on the first Sunday of November. The Dyker Heights lights jam the side streets every evening in December.'),
  P('We schedule around all three. Arena events downtown and Coney Island summer weekends add smaller closures.'),
  P('Nor’easters come through a few times each winter. The carriers hold on the BQE until the plows pass. The low ground in Red Hook, Coney Island, and Gerritsen Beach floods in a coastal storm. We move the handoff inland.'),
 )+chips(["Downtown Brooklyn","Brooklyn Heights","Dumbo","Fort Greene","Clinton Hill","Williamsburg","Greenpoint","Bushwick","Bed-Stuy","Crown Heights","Prospect Heights","Park Slope","Carroll Gardens","Cobble Hill","Red Hook","Sunset Park","Bay Ridge","Dyker Heights","Bensonhurst","Borough Park","Kensington","Windsor Terrace","Ditmas Park","Flatbush","Midwood","East Flatbush","Canarsie","Mill Basin","Marine Park","Bergen Beach","Sheepshead Bay","Brighton Beach","Coney Island","East New York"])
 +NOTE('Serving all of Brooklyn. Tell us the block, and whether the car sits in a garage, a driveway, or at the curb.')))

BODY.append(sec('Your Options','Open or Enclosed in Brooklyn?',
 prose(
  L('Most Brooklyn cars ride open, and the Florida lane is built around it.'),
  P('An enclosed trailer keeps salt, grit, and curious eyes off the car. The garages in Brooklyn Heights, Dyker Heights, and Mill Basin book enclosed trailers. Many Boca-bound cars do too.'),
  P('A daily driver travels open without a second thought. Our <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages set the two side by side.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a short drive to the meeting spot, and a delivery. The bridges and the parkways decide the spot.'),
  P('Approve the price and we assign a carrier already on Interstate 95, then tell you the spot. The driver writes up the car’s condition on a Bill of Lading when you meet. You both sign it, and delivery is checked against that record.'),
 )+ULI([
  "Remove personal belongings",
  "Keep about a quarter tank of fuel",
  "Take photos of the car before it leaves the garage or the block",
  "Provide a working key and disclose mechanical issues",
  "Disable aftermarket alarms",
  "Look up the alternate-side day for your block before you pick a pickup morning",
 ])+prose(P('Each step is laid out on the <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages.'))))

BODY.append(sec('Why Ship Guy','Why Brooklyn Drivers Choose Ship Guy',
 prose(
  L('We know which bridges carry the truck and which blocks can host it. The spot is settled before you leave the house.'),
  P('Our FMCSA brokerage authority is active and our $75,000 surety bond is on file, and both are public. Our office is on Court Street in Downtown Brooklyn.'),
  P('A single coordinator handles the booking from first quote to delivery. Open, enclosed, and expedited transport are all on offer, and the <a href="services.html">services</a> page lists them.'),
 ), alt=True))

BODY.append(office('Brooklyn','26 Court St #2216','Brooklyn, NY 11242','+19297061453','(929) 706-1453','ET',
 '26+Court+St+%232216,+Brooklyn,+NY+11242','Visit Us','Find Ship Guy in Brooklyn',
 'Our office is on Court Street near Borough Hall in Downtown Brooklyn, steps from the subway.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5116.70912694849!2d-73.9909517!3d40.6933254!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c25b72f0cbfb79%3A0xe9e2dcc33a0043fc!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792023064959!5m2!1sen!2sus'))

FAQ=[
 ("Can the carrier come to my block in Brooklyn?","If you have a driveway in Marine Park, Mill Basin, Ditmas Park, or Dyker Heights, often yes. On a brownstone block in Park Slope, Bed-Stuy, or Williamsburg, no. Cars line both curbs and a trailer cannot stop there. The driver waits at an industrial spot or a wide avenue a few minutes away."),
 ("Where are the usual meeting spots in Brooklyn?","Sunset Park and Red Hook for the brownstone neighborhoods and downtown. The Navy Yard blocks for Williamsburg and Greenpoint. Atlantic Avenue toward East New York for central Brooklyn. Flatbush Avenue toward the bay for Canarsie and Marine Park. Fourth Avenue or the Verrazzano lots for Bay Ridge."),
 ("How much does it cost to ship a car from Brooklyn to Florida?","Seven hundred seventy to one thousand ninety dollars for a sedan to Orlando is typical. Miami adds a little. The route runs about eleven hundred miles down Interstate 95. Fall southbound costs more than spring. SUVs and pickups add 10 to 25 percent."),
 ("Are the bridge tolls and the congestion fee added to my price?","No. The carrier pays the Verrazzano, the Hudson crossings, and any congestion fee in effect on the Manhattan side. It prices the trip with all of that inside. The number you approve is the number you pay."),
 ("Is it cheaper to meet the truck on Staten Island?","A little. Inside the borough, the carrier loses an hour to traffic and pays the Verrazzano toll. The quote shows it. Meeting on the Staten Island side of the bridge trims both. Ask and we will quote it both ways."),
 ("Do you handle a PCS move to Fort Hamilton?","Yes. The post in Bay Ridge rotates families on orders all year. Orders usually pay to move one vehicle, and the second one rides with us. The post is gated, so the handoff happens on Fourth Avenue or by the Verrazzano lots. Ship Guy is a private broker with no connection to the post."),
 ("Does the West Indian Day Parade or the marathon affect my pickup?","On those days, yes. Eastern Parkway closes on Labor Day. Fourth Avenue, Lafayette, and Bedford close on the first Sunday of November. The Dyker Heights lights jam the side streets every December evening. We schedule around all three."),
 ("My car is in a garage in Williamsburg. How does the handoff work?","Have the garage pull the car out on pickup morning. Drive it a few minutes to the spot by the Navy Yard. Tell the garage a day ahead so nothing is parked in front of it. At delivery, the same thing happens in reverse. An adult signs the Bill of Lading at the spot."),
 ("Can you ship a car that does not run from Brooklyn?","Yes. The carrier brings a winch, and the extra time to load goes into the quote. The spot has to be flat and wide, which usually means Sunset Park or Red Hook. Let us know if it rolls, steers, and brakes."),
 ("What do you need for a Brooklyn car shipping quote?","Pickup and delivery addresses, with the block on the Brooklyn end. Garage, driveway, or street. Year, make, and model. Whether it runs. Open or enclosed. The dates you can work with. That is all a Brooklyn quote takes."),
]
BODY.append(faq_section(FAQ,'Brooklyn FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Brooklyn?','Price the lane on the form above in about two minutes. Tell us the block and your dates, and the meeting spot is settled before the truck rolls.','+19297061453','(929) 706-1453','Get your free Brooklyn quote'))

build({
 'slug':'auto-transport-brooklyn-new-york',
 'title':'Car Shipping in Brooklyn, NY — Auto Transport | Ship Guy',
 'meta':'Car shipping in Brooklyn, NY over the bridges that allow a trailer. Meeting spots in Sunset Park, Red Hook, and Canarsie, brownstone and driveway blocks, Fort Hamilton moves, parade and marathon timing, the Florida lane, tolls built in. Local office on Court Street. Free quote.',
 'h1':'Car Shipping in<br>Brooklyn, <span class="accent">New York</span>',
 'lede':'Open, enclosed, and expedited auto transport across the borough, planned around the bridges, the parkways, and the alternate-side rules.',
 'tel':'+19297061453','disp':'(929) 706-1453','brand':'Brooklyn','keyword':'car shipping in brooklyn',
 'localterms':['brooklyn','brooklyn bridge','manhattan','williamsburg bridge','verrazzano','brooklyn-queens expressway','gowanus','prospect expressway','belt parkway','ocean parkway','eastern parkway','jackie robinson','atlantic avenue','flatbush avenue','fourth avenue','linden boulevard','third avenue','court street','borough hall','downtown','brooklyn heights','park slope','carroll gardens','cobble hill','williamsburg','greenpoint','bushwick','navy yard','bed-stuy','crown heights','prospect heights','flatbush','midwood','borough park','ditmas park','canarsie','mill basin','marine park','bergen beach','bay ridge','dyker heights','bensonhurst','coney island','sheepshead bay','red hook','sunset park','east new york','fort hamilton','hospitals','colleges','alternate-side','garage','west indian','marathon','lights','nor','florida','boca raton','philadelphia','boston','washington','staten island'],
}, BODY, FAQ)
