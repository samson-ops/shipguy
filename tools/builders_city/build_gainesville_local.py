import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Gainesville, Florida','Car shipping for a city that runs on one campus and one interstate',
 ['Car shipping in Gainesville follows the University of Florida calendar more closely than any other lane we run in the state.',
  'Ship Guy is a licensed auto transport broker with an office on North Main Street downtown. We book vetted carriers across Alachua County, and we do not own the trucks.',
  'Interstate 75 runs down the west side of the city, and every carrier between Atlanta and Tampa passes the exits at Archer Road and Newberry Road. That keeps a college town supplied with trucks that a town its size would not otherwise see.',
  'This page covers the interstate and the fog that closes it, the campus calendar, the hospital, the neighborhoods, Ocala and the horse farms, and the lanes out of North Central Florida.'],
 'Gainesville at a glance',
 ['Most pickups happen within 1 to 3 days, with Interstate 75 bringing carriers past the city all day.',
  'Jacksonville, Orlando, Tampa, and Tallahassee are same-day lanes. Atlanta and Miami take a day. New York and Chicago run three days.'],
 'Send the apartment complex name with a student address. Archer Road and Southwest 34th Street hold dozens of complexes with similar names and tight lots.'))

BODY.append(sec('Interstate 75','The Exits, the Prairie, and the Fog',
 prose(
  L('Gainesville sits on the busiest freight road in the state, and one stretch of it closes in fog.'),
  P('Interstate 75 carries Atlanta-to-Tampa traffic past the city on the west side. Carriers exit at Archer Road, Newberry Road, or Northwest 39th Avenue and reach most of Gainesville in fifteen minutes.'),
  P('Paynes Prairie lies just south of town, and fog settles over the interstate there on winter mornings. The Highway Patrol closes the road when it does, and carriers wait at the truck stops in Micanopy or Alachua.'),
  P('US 441 runs through the middle of the city as Northwest 13th Street, straight past the campus. State Road 26 runs east and west as University Avenue and Newberry Road, and State Road 24 heads southwest to Archer.'),
  P('Everything in the city is within twenty minutes of the interstate, which keeps Gainesville pricing close to Orlando and Tampa despite its size.'),
 ), alt=True))

BODY.append(sec('The Campus','Move-In, Move-Out, and Football Saturdays',
 prose(
  L('The University of Florida brings more than fifty thousand students to a city of a hundred forty thousand, and they arrive at once.'),
  P('Move-in runs the second and third weeks of August, and move-out runs the first two weeks of May. Both windows fill weeks ahead, so a student car should be booked in July or April.'),
  P('The streets around campus and the apartment complexes along Archer Road and Southwest 34th Street are tight. A trailer cannot enter most complex lots, so the driver meets you at a shopping center lot nearby, most often in Butler Plaza or Celebration Pointe.'),
  P('Home football Saturdays fill the Swamp with ninety thousand people, and the roads around campus close from midmorning. We schedule the campus side for weekdays in the fall, and the west side runs on game days without trouble.'),
  P('An adult signs for a student car, and a parent can sign at the far end. Santa Fe College on the northwest side runs a smaller version of the same calendar.'),
 )))

ROUTES=[("Jacksonville, FL","SR-24/US-301/I-10 · ~75 mi","Same day","$150–$240"),("Orlando, FL","I-75/FL Tpke · ~115 mi","Same day","$170–$280"),
 ("Tampa, FL","I-75 · ~130 mi","Same day","$180–$290"),("Tallahassee, FL","I-75/I-10 · ~150 mi","Same day","$200–$320"),
 ("Daytona Beach, FL","US-441/SR-40 · ~100 mi","Same day","$170–$280"),("Miami, FL","FL Tpke · ~335 mi","1 day","$270–$400"),
 ("Atlanta, GA","I-75 · ~340 mi","1 day","$310–$450"),("Charlotte, NC","I-75/I-26/I-77 · ~470 mi","1–2 days","$400–$570"),
 ("Washington, DC","I-95 · ~760 mi","2 days","$560–$820"),("New York, NY","I-95 · ~990 mi","3 days","$700–$980")]
BODY.append(rate_table('Lanes &amp; Costs','Gainesville Car Shipping Lanes and Estimated Costs',
 'The lanes Gainesville households and students ask about most, with estimated open-transport ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates, running sedan, open trailer. SUVs and pickups run about 10 to 25 percent more, enclosed more still. The August and May student windows push short lanes up, and carrier availability on your dates sets the real quote.',
 prose(
  P('Every Florida lane from Gainesville is quick, because the interstate carries carriers between Atlanta and Tampa all day. Atlanta itself is the easiest out-of-state lane.'),
  P('The Northeast lanes fill with students each August and May. The <a href="car-shipping-cost.html">cost guide</a> explains the rest of the number.'),
 ), alt=True))

BODY.append(sec('The Hospital &amp; the Employers','Shands, the Residents, and the Corporate Moves',
 prose(
  L('Outside the campus, Gainesville ships on medicine.'),
  P('The university hospital on Archer Road is one of the largest in the state, and it moves residents and fellows every June. The medical campus sits between Archer Road and the main campus, and its parking garages do not admit a trailer.'),
  P('Residents usually arrive from another program with a car and two weeks of notice. We plan the pickup around the start date, and if the hospital reimburses the shipment, we provide the documentation.'),
  P('The research park on the west side and the technology companies around it relocate engineers on hiring schedules. The interstate leg of any relocation is on the <a href="state-to-state-car-shipping.html">state-to-state</a> page.'),
 )))

BODY.append(sec('The Neighborhoods','Haile, Duckpond, and the Tree Canopy',
 prose(
  L('Gainesville is a city of old oaks, and a seventy-five-foot trailer has to respect them.'),
  P('The Duckpond and the historic districts near downtown have narrow streets under a canopy that hangs low. The driver meets you on Main Street or Northwest 13th Street instead.'),
  P('Haile Plantation and the west-side communities are wide but private, and many have gates. Send the community name and a gate code, and the driver meets you at the entrance if the truck cannot enter.'),
  P('Tioga, Jonesville, and Newberry to the west are new and open, and the truck usually reaches the curb. Alachua and High Springs to the north sit right off the interstate.'),
  P('Our office is on North Main Street downtown, a short drive from every neighborhood in the city.'),
 ), alt=True))

BODY.append(sec('Ocala &amp; the Horse Farms','Marion County, the Show Circuit, and Enclosed Carriers',
 prose(
  L('Forty minutes south, the interstate runs through the horse capital of the state.'),
  P('Ocala and Marion County hold hundreds of horse farms, and the equestrian center on the west side draws the show circuit each winter. Owners ship trucks, trailers, and collector cars in with the season and out in April.'),
  P('Farm roads are private and often unpaved, and the driver meets you at the gate or on the state road. Enclosed carriers stay busy in Marion County with show vehicles and collector cars.'),
  P('The Villages to the south is the largest retirement community in the country, and it ships cars on the snowbird calendar. Our <a href="snowbird-car-shipping.html">snowbird</a> page covers that lane.'),
 )+chips(["Downtown","Duckpond","University Park","Archer Road","Butler Plaza","Celebration Pointe","Haile Plantation","Tioga","Jonesville","Newberry","Alachua","High Springs","Micanopy","Archer","Waldo","Ocala","Belleview","The Villages"])
 +NOTE('Serving Alachua, Marion, and the surrounding counties. Include the complex or community name for a student or gated address.')))

BODY.append(sec('Your Options','Open or Enclosed in Gainesville?',
 prose(
  L('Open transport is the everyday choice, and the student lanes run on it.'),
  P('Enclosed transport keeps a car covered against summer storms, pollen, and the grit of a long lane. Ocala\u2019s show cars and the collector cars in Haile keep enclosed carriers busy.'),
  P('A commuter or student car rides open without any concern. Our <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages walk through the choice.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a pickup at a spot the truck can reach, and a delivery, with the calendar deciding the timing.'),
  P('When the price is approved, a carrier passing on Interstate 75 takes the booking. The driver lists the car\u2019s condition on a Bill of Lading, and you sign before it loads. That list is your comparison at delivery.'),
 )+ULI([
  "Remove personal belongings",
  "Keep about a quarter tank of fuel",
  "Photograph the vehicle before pickup",
  "Provide a working key and disclose mechanical issues",
  "Turn off aftermarket alarms",
  "Include the complex or community name and any gate code",
 ])+prose(P('Our <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> guides cover each step.'))))

BODY.append(sec('Why Ship Guy','Why Gainesville Drivers Choose Ship Guy',
 prose(
  L('We know the move-in weeks, the game days, and the mornings the prairie fog closes the interstate.'),
  P('Active FMCSA brokerage authority and a $75,000 surety bond back every Ship Guy booking, and our office sits on North Main Street.'),
  P('One coordinator handles the shipment from quote to delivery and books open, enclosed, or expedited transport. The <a href="services.html">services</a> page shows the full list.'),
 ), alt=True))

BODY.append(office('Gainesville','104 N Main St Ste 588','Gainesville, FL 32601','+13527583423','(352) 758-3423','ET',
 '104+N+Main+St+Ste+588,+Gainesville,+FL+32601','Visit Us','Find Ship Guy in Gainesville',
 'Our office is on North Main Street downtown, a short drive from Interstate 75 and the University of Florida.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4279.952028730886!2d-82.3261308!3d29.652983300000002!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x88e8a3086ccc7b91%3A0x98c3f735b18bb695!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1790274713454!5m2!1sen!2sus', map_link='https://maps.app.goo.gl/Sja56Uai5QEKFzwJ6'))

FAQ=[
 ("When should I book a car for a University of Florida student?","In July for the August move-in and in April for the May move-out. Both windows fill weeks ahead, because fifty thousand students arrive and leave at once. The driver meets you at a shopping center lot near the complex, since a trailer cannot enter most student lots. An adult signs for the car."),
 ("Can the carrier come to my apartment on Archer Road?","Usually not into the lot. The complexes along Archer Road and Southwest 34th Street have tight entrances and full lots, so the driver meets you at Butler Plaza, Celebration Pointe, or another lot nearby. Send the complex name, because several share similar names."),
 ("Does a Gators home game affect my pickup?","On the campus side, yes. Ninety thousand people fill the Swamp, and the roads around campus close from midmorning on a home Saturday. We schedule the campus side for weekdays in the fall. The west side and the interstate exits run on game days without trouble."),
 ("How much does it cost to ship a car from Gainesville to New York?","Usually seven hundred to nine hundred eighty dollars for a sedan riding open. Interstate 95 carries most of the trip, about a thousand miles. The lane fills with students each August and May, which lifts the price in those weeks. Larger vehicles and enclosed add to it."),
 ("Why would fog delay a pickup in Gainesville?","Because Paynes Prairie sits just south of the city, and fog settles over Interstate 75 there on winter mornings. The Highway Patrol closes the road when it does, and carriers wait at the truck stops in Micanopy or Alachua. A pickup can slide a few hours, and we tell you when it does."),
 ("Do you handle moves for residents at the university hospital?","Yes, the hospital on Archer Road moves residents and fellows every June, and most arrive with a car and two weeks of notice. We plan the pickup around the start date. The medical garages do not admit a trailer, so the handoff happens on Archer Road. If the hospital reimburses the shipment, we provide the documentation."),
 ("Do you serve Ocala and The Villages?","Yes, Marion County and The Villages are covered from this page. Horse farms hand off at the gate or on the state road, and enclosed carriers stay busy with show vehicles in winter. The Villages ships on the snowbird calendar, down in fall and home in spring."),
 ("Can the carrier reach a house in Haile Plantation?","Often to the entrance. Haile and the west-side communities are wide, but many have gates, and where the truck cannot enter, the driver meets you there. Send the community name and a gate code when you book."),
 ("Can you ship a car that does not run from Gainesville?","Yes, non-running cars ship out of Gainesville regularly. A winch-equipped carrier loads it, and the added time carries a fee. Tell us whether it rolls, steers, and brakes, because that decides which truck we send."),
 ("What do you need for a Gainesville car shipping quote?","The pickup and delivery addresses, with the complex or community name. The year, make, and model. Whether it runs and rolls. Open or enclosed, and your dates. That is everything an accurate Gainesville quote needs."),
]
BODY.append(faq_section(FAQ,'Gainesville FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Gainesville?','A quote takes about two minutes on our form. Then tell us your complex or neighborhood and your dates, and we will plan around the campus calendar.','+13527583423','(352) 758-3423','Get your free Gainesville quote'))

build({
 'slug':'auto-transport-gainesville-florida',
 'title':'Car Shipping in Gainesville, FL — Auto Transport | Ship Guy',
 'meta':'Car shipping in Gainesville, FL on Interstate 75. UF move-in and move-out timing, Archer Road handoffs, game-day planning, the university hospital, Ocala horse farms, prairie fog delays. Local office on North Main Street. Free quote.',
 'h1':'Car Shipping in<br>Gainesville, <span class="accent">Florida</span>',
 'lede':'Open, enclosed, and expedited auto transport across Alachua County, planned around the campus calendar and the interstate.',
 'tel':'+13527583423','disp':'(352) 758-3423','brand':'Gainesville','keyword':'car shipping in gainesville',
 'localterms':['gainesville','alachua','interstate 75','us 441','13th street','archer road','newberry road','university avenue','paynes prairie','fog','micanopy','university of florida','gators','swamp','move-in','move-out','butler plaza','celebration pointe','shands','hospital','residents','duckpond','haile','tioga','jonesville','newberry','high springs','ocala','marion county','horse','villages','santa fe college','main street'],
}, BODY, FAQ)
