import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Jacksonville, Florida','Car shipping across the biggest city in the country by land, and the port that moves the cars',
 ['Car shipping in Jacksonville covers eight hundred square miles, two naval installations, and a port that handles more vehicles than almost any in the country.',
  'Ship Guy is a licensed auto transport broker with an office on Riverside Avenue near downtown. We book vetted carriers across the First Coast, and we do not own the trucks.',
  'Interstate 95 runs north and south through the city, Interstate 10 ends downtown after crossing from Tallahassee, and Interstate 295 loops both sides of the river. A carrier can reach almost any address in the metro from one of the three.',
  'This page covers the interstates and the bridges, the Navy, the port and the Puerto Rico sailings, the neighborhoods, the beaches and Nocatee, and the lanes north and south.'],
 'Jacksonville at a glance',
 ['Most pickups happen within 1 to 3 days, with three interstates bringing carriers through the city.',
  'Orlando, Savannah, Tallahassee, and Daytona Beach are same-day lanes. Atlanta, Charlotte, and Miami take a day. Washington and New York run two to three.'],
 'Tell us which side of the river you are on. The beaches, the Westside, and the Northside are forty minutes apart, and the bridges decide the route.'))

BODY.append(sec('The Interstates','Interstate 95, 10, 295, and the Bridges',
 prose(
  L('Jacksonville is the largest city in the contiguous states by area, and the river splits it in half.'),
  P('Interstate 95 crosses the Saint Johns on the Fuller Warren Bridge downtown and carries the Northeast-to-Miami lane. Interstate 10 arrives from Tallahassee and ends at 95, and Interstate 295 loops the city with the Dames Point and Buckman bridges at either end.'),
  P('Butler Boulevard and State Road 9B carry the Southside and the beaches, and US 17 and 301 reach the outer counties. Rush hour backs up the Fuller Warren and the Buckman, so carriers cross midmorning.'),
  P('The Mathews and Hart bridges downtown have older ramps, and a loaded trailer stays on the interstates. The Intracoastal bridges to the beaches are wide and easy.'),
  P('Carriers headed anywhere on the East Coast pass through the city, which keeps Jacksonville pricing among the best in Florida.'),
 ), alt=True))

BODY.append(sec('The Navy','Mayport, NAS Jacksonville, Kings Bay, and Blount Island',
 prose(
  L('Jacksonville is one of the largest Navy towns in the country, and its families move on orders.'),
  P('Naval Station Mayport at the mouth of the river homeports destroyers and helicopter squadrons. Naval Air Station Jacksonville on the Westside flies patrol aircraft, and the submarine base at Kings Bay sits forty minutes north across the Georgia line.'),
  P('The Marine Corps depot on Blount Island and the Coast Guard station add rotations. Families rotate year round, with the heaviest moves from May through August, and many ship a second vehicle through us since orders may cover only one.'),
  P('Housing at each installation is gated, so the driver meets you outside it. Kings Bay families often live in Fernandina or Yulee, which ship through the Jacksonville carrier pool.'),
  P('Ship Guy is a private broker with no military affiliation. Our <a href="military-car-shipping.html">military</a> page covers PCS timing.'),
 )))

ROUTES=[("Orlando, FL","I-95/I-4 · ~140 mi","Same day","$180–$290"),("Savannah, GA","I-95 · ~140 mi","Same day","$180–$290"),
 ("Daytona Beach, FL","I-95 · ~90 mi","Same day","$170–$280"),("Tallahassee, FL","I-10 · ~165 mi","Same day","$220–$340"),
 ("Tampa, FL","I-75/I-10 · ~200 mi","Same day","$220–$340"),("Charleston, SC","I-95/I-26 · ~240 mi","1 day","$250–$380"),
 ("Atlanta, GA","I-10/I-75 · ~345 mi","1 day","$320–$470"),("Miami, FL","I-95 · ~345 mi","1 day","$310–$450"),
 ("Washington, DC","I-95 · ~700 mi","2 days","$520–$750"),("New York, NY","I-95 · ~930 mi","3 days","$650–$900")]
BODY.append(rate_table('Lanes &amp; Costs','Jacksonville Car Shipping Lanes and Estimated Costs',
 'The lanes First Coast households ask about most, with estimated open-transport ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates, running sedan, open trailer. SUVs and pickups run about 10 to 25 percent more, enclosed more still. Snowbird season swings the Interstate 95 lanes, and carrier availability on your dates sets the real quote.',
 prose(
  P('Interstate 95 makes Jacksonville one of the easiest cities in the Southeast to ship from. Savannah, Orlando, and Charleston all sit a few hours away on roads carriers run daily.'),
  P('The Northeast lane fills southbound each fall and northbound each spring. The <a href="car-shipping-cost.html">cost guide</a> explains the rest of the number.'),
 ), alt=True))

BODY.append(sec('The Port','JAXPORT, the Imports, and the Puerto Rico Sailings',
 prose(
  L('More cars roll on and off ships in Jacksonville than in almost any port in the country.'),
  P('The terminals at Blount Island and Talleyrand handle hundreds of thousands of vehicles a year. Imported cars clear customs at the port, and we ship them domestically from there once they are released. The ocean leg is a separate process we do not arrange.'),
  P('Weekly sailings connect Jacksonville to San Juan, and a car headed to Puerto Rico boards here. We deliver it to the terminal, and the ocean crossing is booked separately with the line. Give us the sailing date, and we deliver a day or two ahead of it.'),
  P('The port keeps hundreds of car haulers based in the metro, which is why a private pickup in Jacksonville schedules so quickly.'),
 )))

BODY.append(sec('The Neighborhoods','Riverside, San Marco, Mandarin, and the Southside',
 prose(
  L('Old Jacksonville is oaks and narrow streets, and new Jacksonville is wide and gated.'),
  P('Riverside, Avondale, and Ortega have brick streets, low branches, and a canopy no trailer can pass under. San Marco and Springfield are the same. The driver meets you on Riverside Avenue, San Marco Boulevard, or a main road nearby.'),
  P('Mandarin, the Southside, and Baymeadows are wide, with apartment complexes and subdivisions that often allow curbside. Many have gates, so send the community name.'),
  P('Orange Park and Fleming Island in Clay County, and the Northside near the airport, are wide and easy. Our office is on Riverside Avenue in Brooklyn, beside the river and a mile from the interstates.'),
  P('If your employer reimburses the shipment, we provide the documentation. The financial and insurance headquarters downtown and the clinic on the Southside relocate people on start dates all year.'),
 ), alt=True))

BODY.append(sec('The Beaches &amp; the Growth','Jacksonville Beach, Ponte Vedra, Nocatee, and Saint Augustine',
 prose(
  L('The coast and the county line to the south are where the metro is growing.'),
  P('Jacksonville Beach, Atlantic Beach, and Neptune Beach have tight streets near the ocean, and oceanfront condos run on garages. The driver meets you on Third Street or at a lot near the Intracoastal bridges.'),
  P('Ponte Vedra Beach and Nocatee fill with newcomers from the Northeast and the Midwest on closing dates all year. Nocatee is one of the fastest-growing master-planned communities in the country, and its neighborhoods have gates. Send the neighborhood name.'),
  P('The golf tournament at Sawgrass in March fills Ponte Vedra for a week, and the Florida-Georgia game fills downtown for a weekend each fall. We schedule around both.'),
  P('Saint Augustine to the south has the oldest streets in the country, and no trailer enters the historic district. The driver meets you on US 1 or at a lot by the outlet mall.'),
 )+chips(["Downtown","Riverside","Avondale","Ortega","San Marco","Springfield","Mandarin","Southside","Baymeadows","Town Center","Arlington","Northside","Westside","Orange Park","Fleming Island","Jacksonville Beach","Atlantic Beach","Neptune Beach","Ponte Vedra","Nocatee","Fernandina","Yulee","Saint Augustine","Middleburg"])
 +NOTE('Serving Duval, Clay, Saint Johns, Nassau, and Baker Counties. Tell us the side of the river and the community name.')))

BODY.append(sec('Weather','Hurricanes, Nor\u2019easters, and the River',
 prose(
  L('Jacksonville sits far enough north to dodge many storms and close enough to the ocean to feel the rest.'),
  P('Hurricane season runs June through November, and the beaches and the riverfront evacuate first. Carriers clear the coast days before a landfall, and the river floods Riverside and San Marco in a strong storm.'),
  P('Nor\u2019easters push water over the beaches in fall and winter, and summer storms arrive most afternoons. Neither changes more than the loading hour.'),
  P('We tell you the moment the forecast changes the plan, and we never send a driver into an evacuation zone.'),
 ), alt=True))

BODY.append(sec('Your Options','Open or Enclosed in Jacksonville?',
 prose(
  L('Open transport is the everyday choice, and the port and the Navy lanes run on it.'),
  P('Enclosed transport keeps a car covered against salt air, storm debris, and a long lane\u2019s grit. Ponte Vedra and Ortega keep enclosed carriers busy with collector cars.'),
  P('A commuter car rides open without a second thought. Our <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages compare the two.'),
 )))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a loading on the corridor, and a delivery, with the bridge and the side of the river already planned.'),
  P('Once the price is approved, a carrier running Interstate 95 or 10 takes the booking. The driver notes the car\u2019s condition on a Bill of Lading, which you sign at loading. That note is your checklist at delivery.'),
 )+ULI([
  "Remove personal belongings",
  "Keep about a quarter tank of fuel",
  "Photograph the vehicle before pickup",
  "Provide a working key and disclose mechanical issues",
  "Disable aftermarket alarms",
  "For a base, a beach condo, or a gated community, plan to meet the truck outside it",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> guides go step by step.')), alt=True))

BODY.append(sec('Why Ship Guy','Why Jacksonville Drivers Choose Ship Guy',
 prose(
  L('We know the bridges, the base gates, the sailing schedule, and which streets the oaks close to a truck.'),
  P('Active FMCSA brokerage authority and a $75,000 surety bond stand behind every Ship Guy booking, and our office is on Riverside Avenue.'),
  P('One coordinator carries the shipment from quote to delivery and books open, enclosed, or expedited transport. The <a href="services.html">services</a> page lists the options.'),
 )))

BODY.append(office('Jacksonville','501 Riverside Ave #574','Jacksonville, FL 32202','+19043318141','(904) 331-8141','ET',
 '501+Riverside+Ave+%23574,+Jacksonville,+FL+32202','Visit Us','Find Ship Guy in Jacksonville',
 'Our office is on Riverside Avenue in Brooklyn, beside the river and a mile from Interstate 95 and 10.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4251.294995008879!2d-81.67431049999999!3d30.320040699999993!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x88e5b7c02a8c6f35%3A0x2eb8f1135e7fe157!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1790274768144!5m2!1sen!2sus', map_link='https://maps.app.goo.gl/qFJ6LbuCaUbd5EEe8'))

FAQ=[
 ("Can you handle a PCS move to Mayport, NAS Jacksonville, or Kings Bay?","Yes, all three are steady lanes for us, along with Blount Island and the Coast Guard station. Families rotate year round, with the heaviest moves from May through August, and many ship a second vehicle through us since orders may cover only one. Housing is gated, so the driver meets you outside it. Ship Guy has no military affiliation."),
 ("Can you ship a car from Jacksonville to Puerto Rico?","We handle the land side. Weekly sailings connect Jacksonville to San Juan, and we deliver the car to the terminal a day or two before the sailing you book with the line. The ocean crossing itself is a separate process we do not arrange. Give us the sailing date when you request the quote."),
 ("My car arrived at the port. Can you ship it from there?","Yes, once customs releases it. Imported cars clear at Blount Island or Talleyrand, and we ship them domestically like any other vehicle after release. Give us the release date and the terminal. Enclosed transport is available for a high-value import."),
 ("Can the carrier come to my house in Riverside or Avondale?","Not down the brick streets. The oaks in Riverside, Avondale, Ortega, and San Marco hang too low for a trailer. The driver meets you on Riverside Avenue, San Marco Boulevard, or another main road a few blocks away."),
 ("How much does it cost to ship a car from Jacksonville to New York?","Usually six hundred fifty to nine hundred dollars for a sedan riding open. Interstate 95 runs the whole way, about nine hundred thirty miles. Northbound demand rises each spring when seasonal residents head home, which lifts the price in April and May. Larger vehicles and enclosed add to it."),
 ("Do you serve Nocatee, Ponte Vedra, and Saint Augustine?","Yes, Saint Johns County is covered from this page. Nocatee and Ponte Vedra neighborhoods have gates, so send the neighborhood name. No trailer enters the Saint Augustine historic district, so the driver meets you on US 1 or at a lot by the outlet mall."),
 ("Does the Florida-Georgia game or the golf tournament affect pickups?","For a few days each. The game fills downtown and the stadium district for a weekend each fall, and the tournament at Sawgrass fills Ponte Vedra for a week in March. We schedule those areas around both, and the rest of the city runs normally."),
 ("Why is Jacksonville so quick to schedule?","Because three interstates and one of the busiest vehicle ports in the country keep hundreds of car haulers based in the metro. A private pickup slots into traffic that already exists. Most pickups happen within 1 to 3 days."),
 ("Can you ship a car that does not run from Jacksonville?","Yes, non-running cars ship out of Jacksonville every week. A winch-equipped carrier loads it, and the added time carries a fee. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Jacksonville car shipping quote?","The pickup and delivery addresses, with the side of the river and the community name. The year, make, and model. Whether it runs and rolls. Open or enclosed, and your dates, or the sailing date for Puerto Rico. That is everything an accurate Jacksonville quote needs."),
]
BODY.append(faq_section(FAQ,'Jacksonville FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Jacksonville?','A quote takes about two minutes on our form. Then tell us your side of the river and your dates, and we will plan the bridge, the gate, or the terminal.','+19043318141','(904) 331-8141','Get your free Jacksonville quote'))

build({
 'slug':'auto-transport-jacksonville-florida',
 'title':'Car Shipping in Jacksonville, FL — Auto Transport | Ship Guy',
 'meta':'Car shipping in Jacksonville, FL on Interstate 95, 10, and 295. Mayport, NAS Jacksonville, and Kings Bay moves, JAXPORT releases and Puerto Rico sailings, Riverside and San Marco handoffs, Nocatee and the beaches. Local office on Riverside Avenue. Free quote.',
 'h1':'Car Shipping in<br>Jacksonville, <span class="accent">Florida</span>',
 'lede':'Open, enclosed, and expedited auto transport across the First Coast, planned around the bridges, the bases, and the port.',
 'tel':'+19043318141','disp':'(904) 331-8141','brand':'Jacksonville','keyword':'car shipping in jacksonville',
 'localterms':['jacksonville','first coast','duval','interstate 95','interstate 10','interstate 295','fuller warren','dames point','buckman','butler boulevard','saint johns','river','mayport','nas jacksonville','kings bay','blount island','coast guard','jaxport','talleyrand','port','puerto rico','san juan','sailing','riverside','avondale','ortega','san marco','springfield','mandarin','southside','baymeadows','town center','orange park','fleming island','jacksonville beach','atlantic beach','neptune beach','ponte vedra','nocatee','sawgrass','florida-georgia','fernandina','yulee','saint augustine','hurricane','riverside avenue'],
}, BODY, FAQ)
