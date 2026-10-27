import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('West Jordan, Utah','Car shipping for the fastest-growing corner of Salt Lake County',
 ['Car shipping in West Jordan serves the southwest valley, where new subdivisions open faster than the maps that carriers use.',
  'Ship Guy is a licensed auto transport broker with an office on Redwood Road at 8800 South. We book vetted carriers across the southwest valley, and we do not own the trucks.',
  'Bangerter Highway and the Mountain View Corridor carry the city north and south, and 9000 South and 7800 South carry it east to Interstate 15. A carrier reaches West Jordan from the interstate in fifteen minutes and from the Mountain View Corridor in five.',
  'This page covers the two highways, the new construction from Daybreak to Herriman, the Jordan Landing handoff, the Guard base and the data center, the tech commute, and the lanes out of the valley.'],
 'West Jordan at a glance',
 ['Most pickups happen within 1 to 3 days, with two highways bringing carriers into the southwest valley.',
  'Provo and Ogden are same-day lanes. Las Vegas, Boise, and Denver take a day. Los Angeles, Phoenix, and Seattle take two, and Texas and the Midwest run three.'],
 'Send the subdivision name with the address. Daybreak, Copper Hills, and the streets west of the Mountain View Corridor add blocks every month, and a new one may not be on a carrier\u2019s map yet.'))

BODY.append(sec('Two Highways','Bangerter, the Mountain View Corridor, and the Way In',
 prose(
  L('West Jordan has two north-south highways now, and the newer one changed how carriers reach the west side.'),
  P('Bangerter Highway runs through the middle of the city and carries most of the traffic, with its intersections being converted to freeway-style interchanges one at a time. The Mountain View Corridor runs along the west edge at the foot of the Oquirrhs and connects to the 201 and the airport.'),
  P('9000 South, 7800 South, and 10400 South carry the city east to Interstate 15 at Sandy and Midvale. Redwood Road runs the east side north to Salt Lake City.'),
  P('The numbered grid tells the driver exactly where an address sits, and the streets are wide enough for a trailer. Salt Lake City and West Valley City have their own pages for the north end of the valley.'),
 ), alt=True))

BODY.append(sec('New Construction','Daybreak, Copper Hills, Herriman, and the Streets the Map Missed',
 prose(
  L('The southwest valley is the fastest-growing part of Salt Lake County, and it shows on the west side of the corridor.'),
  P('Daybreak in South Jordan, Copper Hills on the west edge of the city, and the subdivisions in Herriman and Riverton add streets every month. Most have homeowners associations, and many have rules about where a truck can stop.'),
  P('A brand-new street can take months to reach a carrier\u2019s map. Send the subdivision name, and we route the driver ourselves rather than trust the map.'),
  P('Timing delivery to a closing date is the most common request here. Households arriving from California, Washington, and Colorado buy on the west side, and most ship one car and drive the other.'),
  P('If your employer reimburses the shipment, we provide the documentation. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
 )))

ROUTES=[("Provo, UT","I-15 · ~35 mi","Same day","$150–$240"),("Ogden, UT","I-15 · ~50 mi","Same day","$150–$240"),
 ("Boise, ID","I-15/I-84 · ~350 mi","1 day","$320–$460"),("Las Vegas, NV","I-15 · ~405 mi","1 day","$380–$540"),
 ("Denver, CO","I-15/I-80/I-70 · ~530 mi","1–2 days","$430–$620"),("Reno, NV","I-80 · ~530 mi","1–2 days","$430–$620"),
 ("Phoenix, AZ","I-15/US-93 · ~650 mi","2 days","$480–$700"),("Los Angeles, CA","I-15 · ~675 mi","2 days","$500–$730"),
 ("Seattle, WA","I-84/I-82 · ~845 mi","2–3 days","$600–$880"),("Dallas, TX","I-15/I-40 · ~1,230 mi","3 days","$850–$1,200")]
BODY.append(rate_table('Lanes &amp; Costs','West Jordan Car Shipping Lanes and Estimated Costs',
 'The lanes southwest-valley households ask about most, with estimated open-transport ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates, running sedan, open trailer. SUVs, pickups, and minivans run about 10 to 25 percent more, enclosed more still. Season and carrier availability on your dates set the real quote.',
 prose(
  P('Interstate 15 makes Las Vegas and Los Angeles the easiest long lanes from the southwest valley. Boise and Denver follow on Interstate 84 and 80.'),
  P('The California lane runs full with newcomers, which keeps it competitive. The <a href="car-shipping-cost.html">cost guide</a> explains the rest of the number.'),
 ), alt=True))

BODY.append(sec('Jordan Landing &amp; the Handoff','Where the Truck Meets You When the Street Cannot',
 prose(
  L('When a subdivision rule or a tight cul-de-sac keeps the truck out, West Jordan has an easy answer.'),
  P('The shopping district at Jordan Landing sits beside Bangerter Highway at 7800 South, with wide lots a carrier can enter. Most west-side handoffs that cannot happen at the curb happen there.'),
  P('The medical center at 3500 West and the district park along the Jordan River add two more easy spots. The driver names the lot before dispatch, and it is a few minutes from the house.'),
  P('Our office is on Redwood Road at 8800 South, minutes from Bangerter Highway and Jordan Landing.'),
 )))

BODY.append(sec('The Guard Base &amp; the Data Center','Camp Williams, Bluffdale, and the Federal Moves',
 prose(
  L('The south end of the valley holds a National Guard base and one of the largest federal data centers in the country.'),
  P('Camp Williams at Bluffdale trains Guard units on drill and mobilization schedules, and the data center beside it relocates engineers and contractors on program dates. Both sit fifteen minutes south on the Mountain View Corridor or Redwood Road.'),
  P('Housing at the base is gated, so the driver meets you outside it. Ship Guy is a private broker with no military affiliation, and our <a href="military-car-shipping.html">military</a> page covers Guard and PCS moves.'),
  P('Hill Air Force Base rotates families through the whole valley, and its airmen who live in the southwest valley ship through this office. Our Salt Lake City page covers the base itself.'),
 ), alt=True))

BODY.append(sec('The Tech Commute &amp; the Big Vehicles','Point of the Mountain, Family Cars, and the Canyons',
 prose(
  L('Half the southwest valley drives to the tech corridor, and most of it drives something large.'),
  P('The software and hardware companies at the Point of the Mountain in Lehi and Draper sit fifteen minutes south, and they relocate engineers from across the country on start dates. Many of them buy in Herriman, Riverton, and Daybreak, and we plan the pickup around the first day.'),
  P('Families here are large, and a minivan or full-size SUV costs 10 to 25 percent more to ship than a sedan. A carrier is priced by the space and weight it carries, and we quote the real size.'),
  P('The ski canyons sit forty minutes east across the valley, and no trailer climbs them. Ski-season cars for Alta, Snowbird, or Brighton hand off in Sandy or at the mouth of the canyon.'),
 )+chips(["Jordan Landing","Copper Hills","Oquirrh Shadows","Jordan Hills","West Jordan Center","South Jordan","Daybreak","Riverton","Herriman","Bluffdale","Camp Williams","Taylorsville","Midvale","Sandy","Draper","Lehi"])
 +NOTE('Serving the southwest valley from Taylorsville to Bluffdale. Send the subdivision name, the vehicle size, and any gate code.')))

BODY.append(sec('Weather','Snow, the Inversion, and the Oquirrh Wind',
 prose(
  L('The southwest valley gets the same winter as the rest of the Front, with one difference on the west edge.'),
  P('Snow closes Interstate 80 and 15 outside the valley a few times a season, and a lane that crosses Parleys Canyon waits out the chain law. Inside the valley, the plows keep the highways open.'),
  P('Wind comes off the Oquirrhs onto the west side and slows a high-profile trailer on the Mountain View Corridor. The inversion settles over everything for weeks each winter and changes nothing for a carrier.'),
  P('Summer heat passes a hundred degrees in July, and drivers load early. We tell you the moment the forecast changes the plan.'),
 ), alt=True))

BODY.append(sec('Your Options','Open or Enclosed in West Jordan?',
 prose(
  L('Open transport is the everyday choice, and the Interstate 15 lanes run on it.'),
  P('Enclosed transport keeps a car covered against road salt, canyon grit, and the sun. Daybreak and the east-bench estates keep enclosed carriers busy with collector cars.'),
  P('A family vehicle rides open without a second thought. Our <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain the choice.'),
 )))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff at the curb or at Jordan Landing, and a delivery, with the closing date setting the window.'),
  P('When the price is approved, a carrier on Interstate 15 takes the booking. The driver notes the car\u2019s condition on a Bill of Lading, and you sign it as the car loads. That note is your comparison at delivery.'),
 )+ULI([
  "Remove personal belongings",
  "Keep about a quarter tank of fuel",
  "Photograph the vehicle before pickup",
  "Provide a working key and disclose mechanical issues",
  "Disable aftermarket alarms",
  "Include the subdivision name, the vehicle size, and any gate code",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> guides go step by step.')), alt=True))

BODY.append(sec('Why Ship Guy','Why West Jordan Drivers Choose Ship Guy',
 prose(
  L('We route the driver to streets the map has not caught up with and time the delivery to your closing.'),
  P('Active FMCSA brokerage authority and a $75,000 surety bond stand behind every booking we make, and our office is on Redwood Road.'),
  P('One coordinator carries the shipment from quote to delivery and can line up open, enclosed, or expedited transport. The <a href="services.html">services</a> page has the whole menu.'),
 )))

BODY.append(office('West Jordan','8833 S Redwood Rd #366','West Jordan, UT 84088','+13854942325','(385) 494-2325','MT',
 '8833+S+Redwood+Rd+%23366,+West+Jordan,+UT+84088','Visit Us','Find Ship Guy in West Jordan',
 'Our office is on Redwood Road at 8800 South, minutes from Bangerter Highway and Jordan Landing.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3739.876464724971!2d-111.9365074!3d40.59075829999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x875289504ef7379b%3A0x25d32dd032d9b284!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1790275068336!5m2!1sen!2sus'))

FAQ=[
 ("My house is in a brand-new subdivision in Herriman or Daybreak. Can the carrier find it?","Yes, as long as you send the subdivision name with the address. The streets west of the Mountain View Corridor add blocks every month, and a new one can take months to reach a carrier\\u2019s map. We route the driver ourselves. If the association keeps trucks off the street, the handoff moves to the entrance or to Jordan Landing."),
 ("Can delivery be timed to my closing?","Yes, that is the most common request in the southwest valley. We set the window so the car lands a day or two after you get keys. If the closing moves, tell us early and we adjust. A flexible range on your side helps."),
 ("Where does the handoff happen if the truck cannot reach my street?","Usually at Jordan Landing, beside Bangerter Highway at 7800 South, where the lots are wide enough for a carrier. The medical center at 3500 West and the district park are the other easy spots. The driver names the place before dispatch, a few minutes from the house."),
 ("How much does it cost to ship a car from West Jordan to Los Angeles or Las Vegas?","Los Angeles usually runs five hundred to seven hundred thirty dollars for a sedan, about six hundred seventy-five miles down Interstate 15. Las Vegas runs three hundred eighty to five hundred forty. A minivan or full-size SUV adds 10 to 25 percent, so tell us the model."),
 ("Do you handle relocations to the tech companies at the Point of the Mountain?","Yes, the companies in Lehi and Draper relocate engineers from across the country on start dates, and many of them buy in Herriman, Riverton, and Daybreak. We plan the pickup around the first day. If your employer reimburses the shipment, we provide the documentation."),
 ("Can you handle a move to Camp Williams or the data center in Bluffdale?","Yes, both sit fifteen minutes south, and the base rotates Guard units while the data center relocates engineers on program dates. Housing at the base is gated, so the driver meets you outside it. Ship Guy is a private broker with no military affiliation."),
 ("Can you deliver a car for ski season at Alta, Snowbird, or Brighton?","To Sandy or the mouth of the canyon, yes. No trailer climbs the ski canyons, and the resorts sit forty minutes east across the valley. The driver meets you at a lot in Sandy, and the last leg is a short drive up."),
 ("Is Bangerter Highway construction a problem?","Only for timing. The intersections are being converted to freeway-style interchanges one at a time, and a carrier plans around the closures. The Mountain View Corridor and Redwood Road carry the city while a stretch of Bangerter is closed."),
 ("Can you ship a car that does not run from West Jordan?","Yes, non-running cars ship out of the southwest valley regularly. A winch-equipped carrier loads it, and the extra loading time goes on the quote. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a West Jordan car shipping quote?","The pickup and delivery addresses, with the subdivision name. The year, make, and model, and whether it is a minivan or a full-size SUV. Whether it runs and rolls. Open or enclosed, and your dates. That is everything an accurate West Jordan quote needs."),
]
BODY.append(faq_section(FAQ,'West Jordan FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in West Jordan?','A quote takes about two minutes on the form above. Then tell us your subdivision and your closing date, and we will route the driver and set the window.','+13854942325','(385) 494-2325','Get your free West Jordan quote'))

build({
 'slug':'auto-transport-west-jordan-utah',
 'title':'Car Shipping in West Jordan, UT — Auto Transport | Ship Guy',
 'meta':'Car shipping in West Jordan, UT for the fastest-growing corner of the valley. Bangerter and Mountain View Corridor routing, new-subdivision delivery in Daybreak and Herriman, Jordan Landing handoffs, Camp Williams moves, the tech commute, real pricing for family SUVs. Local office on Redwood Road. Free quote.',
 'h1':'Car Shipping in<br>West Jordan, <span class="accent">Utah</span>',
 'lede':'Open, enclosed, and expedited auto transport across the southwest valley, routed to the newest streets and timed to your closing.',
 'tel':'+13854942325','disp':'(385) 494-2325','brand':'West Jordan','keyword':'car shipping in west jordan',
 'localterms':['west jordan','southwest valley','salt lake county','bangerter','mountain view corridor','9000 south','7800 south','redwood road','interstate 15','grid','subdivision','new construction','daybreak','copper hills','herriman','riverton','south jordan','bluffdale','camp williams','data center','guard','jordan landing','medical center','jordan river','point of the mountain','lehi','draper','tech','engineers','closing','minivan','suv','family','alta','snowbird','brighton','canyon','sandy','oquirrh','wind','inversion','parleys','chain law'],
}, BODY, FAQ)
