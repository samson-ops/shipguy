import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Gulfport, Mississippi','Car shipping on the Mississippi coast, between the Seabee base, the port, and the beach',
 ['Car shipping in Gulfport runs along Interstate 10 and down Highway 49 to the harbor. Ship Guy is a licensed auto transport broker with an office on Seaway Road in north Gulfport.',
  'We book vetted carriers across Gulfport, from the beachfront to Orange Grove and out to Long Beach. The carriers own the trucks. Ship Guy holds the license and the bond.',
  'Interstate 10 runs along the north side of the city with the 49 and Lorraine Road exits. Highway 49 runs from the port past the airport to Hattiesburg and Jackson. Highway 90 is the beach road, rebuilt after Katrina. Pass Road and Cowan-Lorraine Road carry the rest.',
  'This page covers 10, 49, 90, Pass Road, downtown, Bayou View, Orange Grove, and the beachfront. It also covers the Seabees, the port, the casinos, the car week in October, and the hurricanes.'],
 'Gulfport at a glance',
 ['Most pickups happen within 1 to 3 days. The 10 carriers pass between Jacksonville and Houston every day. The 49 carriers link the coast to Jackson. New Orleans and Mobile are an hour each way.',
  'New Orleans, Mobile, Hattiesburg, and Pensacola ride a single day on the truck. Jackson and Baton Rouge take a day. Houston and Atlanta take one to two, and Tampa takes two.'],
 'Tell us the neighborhood and the base, if there is one. Bayou View, the beachfront, and downtown meet the truck on a main road. Orange Grove, the Lorraine Road subdivisions, and the grids off Pass Road usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 10, Highway 49, Highway 90, Pass Road, Cowan-Lorraine Road, Dedeaux Road, and the Bridges',
 prose(
  L('Gulfport is a grid between the interstate and the beach, five miles deep. A carrier picks its exit and comes straight down.'),
  P('Interstate 10 runs along the north edge of the city. The 49 exit is the main one, with the outlets and the truck stops beside it. Lorraine Road and Canal Road are the others. The interstate is the Florida-to-Texas road, and every carrier on the Gulf runs it. New Orleans is eighty miles west over the Pearl. Mobile is sixty-five miles east across the Pascagoula.'),
  P('Highway 49 runs north and south through the middle of the city. It starts at the port on the harbor and runs past the airport to the interstate. North of 10 it is the only road to Hattiesburg and Jackson. Highway 90 is the beach boulevard, four lanes along the sand from Bay St. Louis to Biloxi. Pass Road runs parallel a mile inland and carries the old commercial strip. Cowan-Lorraine Road and Dedeaux Road cross between them. The bridges at Bay St. Louis and Biloxi Bay carry 90 over the water.'),
  P('The carriers come off 10 at 49 or Lorraine Road. The outlet lots at the 49 exit are the usual meeting spot. The big-box lots on 49 north of the airport work too. So do the lots at the Pass Road shopping centers and the harbor lots downtown on a weekday. The airport cell lot works for a fly-and-ship.'),
  P('Our office is on Seaway Road in north Gulfport, between the airport and the outlets off 49.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the Beachfront, Mississippi City, Bayou View, Handsboro, Orange Grove, North Gulfport, Lyman, and Long Beach',
 prose(
  L('Gulfport is old streets near the water and new subdivisions north of the interstate. The truck meets the old streets on a main road.'),
  P('Downtown runs from the harbor north along 25th and 26th Avenues, old brick blocks around the courthouse. The driver meets you at the harbor lots or on 49. The beachfront along 90 is big lots, condo towers, and empty lots where the mansions stood before Katrina. The boulevard has no shoulder for a trailer. The handoff moves a block inland to a side street or to the Pass Road lots.'),
  P('Mississippi City and Handsboro on the east side are the oldest neighborhoods, narrow streets under live oaks. Bayou View around the bayou is winding streets of brick ranches, and the oaks come down low. The handoff moves to Pass Road or Courthouse Road. The grids between Pass Road and the tracks are plain blocks where the curb usually works.'),
  P('Orange Grove north of the interstate is the newest part of the city. The subdivisions off Dedeaux Road and Lorraine Road are wide, and the truck reaches the curb. North Gulfport along the tracks is an old community with narrow streets and low branches. The driver meets you on 49. Lyman and Saucier up 49 are rural lots and long driveways. The handoff happens at the gas station on the highway.'),
  P('Long Beach and Pass Christian ship with the same trucks and price the same as Gulfport. So do Biloxi, D’Iberville, and Ocean Springs to the east. Diamondhead and Bay St. Louis add the bridge and nothing else. Hattiesburg is seventy miles north on 49.'),
 )))

ROUTES=[("Mobile, AL","I-10 · ~65 mi","Same day","$140–$230"),("Hattiesburg, MS","US-49 · ~70 mi","Same day","$140–$230"),
 ("New Orleans, LA","I-10 · ~80 mi","Same day","$150–$240"),("Pensacola, FL","I-10 · ~110 mi","Same day","$190–$300"),
 ("Baton Rouge, LA","I-10/I-12 · ~160 mi","Same day","$200–$310"),("Jackson, MS","US-49 · ~160 mi","Same day","$220–$340"),
 ("Houston, TX","I-10 · ~400 mi","1 day","$380–$540"),("Atlanta, GA","I-59/I-20 · ~400 mi","1 day","$380–$540"),
 ("Tampa, FL","I-10/I-75 · ~560 mi","1–2 days","$480–$690"),("Dallas, TX","I-10/I-49/I-20 · ~560 mi","1–2 days","$480–$690")]
BODY.append(rate_table('Lanes &amp; Costs','Gulfport Car Shipping Lanes and Estimated Costs',
 'The lanes coast cars run most, with estimated open-trailer ranges. Price your own route on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Gulfport, sedan that runs, open trailer. An SUV or a pickup costs 10 to 25 percent more, and enclosed more again. The week you offer and the carriers free on 10 that week set the final figure.',
 prose(
  P('Gulfport prices with Biloxi on every lane, because the same trucks serve the whole coast. The Texas and Florida lanes ride 10 and fill every day. The Jackson lane rides 49 and fills on the weekends. The Atlanta lane rides 59 and 20 through Birmingham. The October car week fills every enclosed trailer on the Gulf, and the price rises with it.'),
  P('A June report date at the base or the October car week lands in the busiest weeks. The <a href="car-shipping-cost.html">cost guide</a> explains what size, condition, and timing do to the figure.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Seabees, the Airmen, the Port, the Casinos, the Hospital, the Shipyard, the Colleges, and the Winter Residents',
 prose(
  L('Gulfport relocates sailors, airmen, longshoremen, dealers, nurses, and students. The two bases move more households than everyone else combined.'),
  P('The Seabee base on Pass Road deploys and returns battalions all year. Sailors and families rotate on orders, with the summer peak. Housing sits behind the gate, so the truck meets you outside it or at the Pass Road lots. Orders pay for one car, and the family ships the second one with us. The Air Force base in Biloxi trains airmen on class cycles, and the instructors rotate every few years. Ship Guy is a private broker with no tie to either base. The <a href="military-car-shipping.html">military</a> page explains how orders set the timing.'),
  P('The port at the foot of 49 unloads fruit ships and moves managers on contract dates. A car that arrived by ship moves like any other once customs releases it. The casino on the beach and the dozen in Biloxi move dealers and managers between properties. The hospital near downtown brings nurses and residents each summer. The shipyard in Pascagoula relocates engineers on program schedules, and many of them live in Gulfport. The rocket test center across the Pearl does the same.'),
  P('The community college on Switzer Road takes student cars in late August. The university campus on the beach in Long Beach does the same. A parent sets it up, and an adult signs at the lot. The cars head home in May. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers what crossing a state line involves.'),
  P('Winter residents arrive in January from Canada and the Midwest. They fill the parks and the condos until March. Many ship a second car down and back. Retirees from the bases stay for the water.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Mardi Gras, the Fishing Rodeo, the Car Week, the Deployments, Move-In Week, the Winter Residents, the Hurricanes, and the Heat',
 prose(
  L('Gulfport runs on a Navy calendar and a hurricane calendar. The weather problem is the Gulf, five miles from every address.'),
  P('Mardi Gras closes downtown on Fat Tuesday afternoon for the parade. The fishing rodeo fills the harbor and Jones Park over the Fourth of July. The car week in early October brings thousands of classic cars to 90 along the whole coast. The beach road crawls for a week, and every enclosed trailer on the Gulf is booked. Move-in week in late August fills the blocks around the colleges. The deployments and the homecomings at the base set their own weeks. Book three weeks ahead for a June or an October date.'),
  P('The storms run June through November. Katrina in 2005 is still the benchmark. The surge took the beachfront, the port, and everything south of the tracks. Camille in 1969 did it before. Nate in 2017 and Zeta in 2020 came ashore within a few miles of the city. An evacuation order closes the bridges, and the carriers stage in Hattiesburg. A pickup in an evacuation waits for the all-clear, and we call the moment a watch goes up.'),
  P('Heavy rain floods the bayou and the low streets in North Gulfport a few times a year. A handoff in those blocks moves to the afternoon or to 49. Ice comes once a decade. The January 2014 ice closed the bridges on 90 and 10 for a day.'),
  P('Summer brings heat and an afternoon storm most days from June through September. The storm shifts the loading hour, and the heat shifts it earlier. The humidity does the rest.'),
 )+chips(["Downtown","The Harbor","Jones Park","The Beachfront","East Beach","Mississippi City","Hardy Court","Handsboro","Bayou View","Bel-Aire","Pass Road","Courthouse Road","Orange Grove","Dedeaux Road","Lorraine Road","North Gulfport","Turkey Creek","The Airport","Seaway Road","Lyman","Saucier","Long Beach","Pass Christian","Bay St. Louis","Diamondhead","Biloxi","D'Iberville","Ocean Springs","Hattiesburg"])
 +NOTE('Serving Gulfport and the whole Mississippi coast, Bayou View street or Orange Grove cul-de-sac. Tell us the neighborhood and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Gulfport?',
 prose(
  L('Open trailers carry most of the coast, and the table above is priced for one.'),
  P('An enclosed trailer keeps off the salt air, the sand, and the sap from the live oaks. The car week crowd books one, and so do the collectors in Bayou View. Ahead of a hurricane, the car goes on whatever truck has room, and we say that plainly.'),
  P('An everyday car or a student’s car is fine in the open. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages compare them line by line.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A figure, a lot at the outlets, and your signature at delivery. The orders or the move-in date set the week.'),
  P('Approve the figure, and we book a carrier already running 10 that week. The lot and the window are fixed the same afternoon. At pickup the driver photographs every panel and records the condition on the Bill of Lading. You sign that sheet, and it is what delivery is checked against.'),
 )+ULI([
  "Everything personal out of the cabin and the trunk",
  "Fuel down to a quarter tank",
  "Photograph each side and the odometer before the truck comes",
  "One good key, and a note about any known faults",
  "Any add-on alarm turned off",
  "On the beachfront, in Bayou View, or behind a gate, expect a lot or a side street",
 ])+prose(P('The sequence is on the <a href="how-it-works.html">how it works</a> page, and the pickup checklist is on the <a href="car-shipping-preparation.html">preparation</a> page.'))))

BODY.append(sec('Why Ship Guy','Why Gulfport Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already run 10 every day. We know which week the car crowd takes every enclosed trailer.'),
  P('Our FMCSA license and our $75,000 bond are a public record on the federal register. The office is on Seaway Road in north Gulfport.'),
  P('The coordinator who quotes the move stays with it until the car is signed for. See the <a href="services.html">services</a> page for open, enclosed, and expedited.'),
 )))

BODY.append(office('Gulfport','14231 Seaway Rd #789','Gulfport, MS 39503','+12283958234','(228) 395-8234','CT',
 '14231+Seaway+Rd+%23789,+Gulfport,+MS+39503','Visit Us','Find Ship Guy in Gulfport',
 'Our office is on Seaway Road in north Gulfport, between the airport and the outlets off 49.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4246.377921890638!2d-89.0760772!3d30.433164!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x889c1579f6c53e81%3A0xba209768d38e4457!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793629570072!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Gulfport to Houston or Atlanta?","Houston runs three hundred eighty to five hundred forty dollars for a sedan. That is about four hundred miles west on 10. Atlanta runs the same, about four hundred miles up 59 and 20. New Orleans and Mobile are an hour away and the lowest lanes on the table. An SUV or a pickup runs 10 to 25 percent higher."),
 ("Do you ship cars for Seabees on orders to the Gulfport base?","Yes, in every month of the year. Orders cover one car, and the second one comes to us. Base housing is behind the gate, so the driver meets you outside it or on Pass Road. The deployments and the homecomings set the busy weeks. Ship Guy is a private broker with no connection to the base."),
 ("Do you handle PCS moves for Keesler?","Yes. The base in Biloxi is twelve miles east, and the same carriers serve it. Instructors and permanent party rotate on orders. Students on class cycles ship a car for a long course. The handoff happens outside the gate or at the Pass Road lots. Keesler prices the same as Gulfport."),
 ("Can the carrier come to my street in Bayou View or on the beachfront?","No. Bayou View is winding streets under low oaks, and the beach boulevard has no shoulder for a trailer. The driver meets you on Pass Road, Courthouse Road, or a side street a block inland. Orange Grove, the Lorraine Road subdivisions, and the grids off Pass Road usually allow the curb."),
 ("Does the car week in October affect my pickup?","Yes. Thousands of classic cars fill 90 for a week in early October. Every enclosed trailer on the Gulf is booked for the event. A commuter car ships the same week on an open trailer with a day or two of slack. A classic car for the week wants a booking in August."),
 ("Can you deliver on an MGCCC or Southern Miss Gulf Park move-in date?","Yes. The community college on Switzer Road takes cars in late August. The campus on the beach in Long Beach follows the same week. Mom or Dad books, and an adult signs at a lot. The date sets the window."),
 ("Can you ship a car to or from Biloxi, Long Beach, or Hattiesburg?","Yes. Biloxi and Long Beach ride the same carriers and price the same as Gulfport. So do Pass Christian, D’Iberville, and Ocean Springs. Hattiesburg is seventy miles north on 49 and rides the carriers running to Jackson."),
 ("What happens if a hurricane hits on my pickup day?","A watch holds the truck in Hattiesburg until the all-clear, and an evacuation closes the bridges. We call the moment a watch goes up. The pickup lands on the first clear day after the roads reopen, at the same price. A car leaving ahead of the storm rides whatever truck has room."),
 ("Can you ship a car that does not run from Gulfport?","Yes. We send a winch-equipped carrier and build the loading time into the quote. The outlet lots and the big-box lots on 49 are flat. Let us know whether it rolls, steers, and brakes."),
 ("What do you need for a Gulfport car shipping quote?","The two addresses, with the neighborhood and the base if one is involved. The year, make, and model, and whether it runs. Open or enclosed, and the week around the report date. Send those, and the Gulfport figure comes back the same day."),
]
BODY.append(faq_section(FAQ,'Gulfport FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Gulfport?','Two minutes on the form above gets your lane a Gulfport figure. Name the neighborhood and the week, and a carrier already running 10 takes it.','+12283958234','(228) 395-8234','Get your free Gulfport quote'))

build({
 'slug':'auto-transport-gulfport-mississippi',
 'title':'Car Shipping in Gulfport, MS — Auto Transport | Ship Guy',
 'meta':'Car shipping in Gulfport, MS, on the Mississippi coast between the Seabee base, the port, and the beach. Navy and Keesler PCS moves outside the gates, the October car week, casino and hospital relocations, main-road handoffs for Bayou View and the beachfront, curbside pickups in Orange Grove, and the hurricanes. Local office on Seaway Road. Free quote.',
 'h1':'Car Shipping in<br>Gulfport, <span class="accent">Mississippi</span>',
 'lede':'Open, enclosed, and expedited auto transport across Gulfport and the Mississippi coast, planned around 10, 49, the Navy’s orders, the October car week, and hurricane season.',
 'tel':'+12283958234','disp':'(228) 395-8234','brand':'Gulfport','keyword':'car shipping in gulfport',
 'localterms':['gulfport','seabee','port','beach','interstate 10','highway 49','highway 90','pass road','seaway road','airport','outlets','lorraine road','canal road','dedeaux road','courthouse road','harbor','downtown','bayou view','orange grove','north gulfport','beachfront','mississippi city','handsboro','lyman','saucier','long beach','pass christian','bay st. louis','diamondhead','biloxi','ocean springs','hattiesburg','jackson','new orleans','mobile','pensacola','baton rouge','houston','atlanta','tampa','dallas','keesler','airmen','sailors','longshoremen','dealers','nurses','students','casino','hospital','shipyard','pascagoula','rocket test center','pearl','fruit ships','customs','community college','switzer road','university campus','winter residents','canada','midwest','mardi gras','fat tuesday','fishing rodeo','jones park','car week','classic cars','move-in','deployments','homecomings','katrina','2005','camille','1969','nate','2017','zeta','2020','evacuation','bridges','january 2014','ice','live oaks','salt air','sand','sap','bill of lading','fmcsa','winch','gate','orders','truck stops','25th','26th'],
}, BODY, FAQ)
