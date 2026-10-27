import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Little Rock, Arkansas','Car shipping at the crossroads of Interstate 40 and 30, in a state that runs on trucking',
 ['Car shipping in Little Rock is easy for one reason, which is that the trucks were already coming. Ship Guy is a licensed auto transport broker with an office on Rebsamen Park Road in Riverdale.',
  'We book vetted carriers across central Arkansas, from North Little Rock and Maumelle to Conway, Benton, and Jacksonville. We do not own the trucks.',
  'Interstate 40 runs along the north bank of the river between Memphis and Oklahoma City. Interstate 30 leaves downtown for Benton and Dallas. Interstate 430 and 440 loop the west and the south. Interstate 630 cuts through the middle of the city.',
  'This page covers the two interstates and the loops, the hills and the grids, and the suburbs. It also covers the air base, the medical school, the state offices, the ice, and the river.'],
 'Little Rock at a glance',
 ['Most pickups happen within 1 to 3 days. Two of the largest trucking companies in the country are based in the state. 40 and 30 cross here.',
  'Memphis, Fayetteville, and Fort Smith are same-day lanes. Dallas is the same day too. Tulsa, St. Louis, Nashville, and Houston take a day. Denver and Florida take two to three.'],
 'Tell us the neighborhood. Hillcrest, the Heights, and the River Market need a meeting spot. West Little Rock, Sherwood, and Maumelle usually allow the curb, gate permitting.'))

BODY.append(sec('The Roads','Interstate 40, 30, 430, 440, 630, and the River Bridges',
 prose(
  L('Little Rock sits where the Memphis-to-Oklahoma lane crosses the Dallas lane. Every carrier in the mid-South passes it.'),
  P('Interstate 40 runs through North Little Rock on the far bank of the river. It carries Memphis and Nashville to the east and Fort Smith and Oklahoma City to the west. Interstate 30 crosses the river downtown on the new bridge and runs southwest to Benton, Texarkana, and Dallas.'),
  P('Interstate 630 runs through the middle of the city from downtown to the Big Rock interchange. Interstate 430 loops the west side from the river to 30. Interstate 440 loops the southeast past the airport. US 67 runs northeast to Jacksonville and the air base. Cantrell Road runs west to the Heights and Chenal.'),
  P('The carriers come off 630 at University Avenue and Fair Park, off 430 at Cantrell and Kanis. Off 30 at Geyer Springs. The lots along University Avenue, at the mall by 430. In the River Market garage district are the usual meeting spots. No road in the state charges a toll.'),
  P('Our office sits on Rebsamen Park Road in Riverdale, below Cantrell Hill and beside the river.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, Hillcrest, the Heights, West Little Rock, and the Suburbs',
 prose(
  L('Little Rock is a river town on a line of hills with wide grids beyond them. The handoff follows the ground.'),
  P('Downtown and the River Market run on one-way streets around the library and the convention center. The driver meets you on President Clinton Avenue or at a lot off 30. Argenta across the river has the same tight blocks and a ballpark.'),
  P('Hillcrest and the Heights climb Cantrell Hill on narrow, winding streets. Low trees and parked cars line both sides. The driver stays on Kavanaugh, Cantrell, or University Avenue. Riverdale below them is flat and open. Our own street works for a handoff when the river is down.'),
  P('West Little Rock is wide grids and gated subdivisions. Chenal, Pleasant Valley, and Maumelle meet the truck at the gate. The shopping center on Chenal Parkway is the backup. The newest streets out past 430 are not always on a carrier’s map yet. Send the full address.'),
  P('Sherwood, Jacksonville, Cabot, Benton, and Bryant are suburban grids where the truck usually reaches the curb. Conway sits thirty miles up 40 with two colleges and a technology company. The handoff there happens on Dave Ward Drive or at a lot off 40.'),
 )))

ROUTES=[("Memphis, TN","I-40 · ~140 mi","Same day","$180–$290"),("Fayetteville, AR","I-40/I-49 · ~190 mi","Same day","$210–$330"),
 ("Dallas, TX","I-30 · ~320 mi","Same day","$300–$440"),("Tulsa, OK","I-40/US-412 · ~280 mi","1 day","$280–$410"),
 ("St. Louis, MO","US-67/I-55 · ~350 mi","1 day","$320–$460"),("Nashville, TN","I-40 · ~350 mi","1 day","$320–$460"),
 ("Houston, TX","I-30/US-59 · ~430 mi","1 day","$370–$530"),("Atlanta, GA","I-40/I-22 · ~530 mi","1–2 days","$430–$620"),
 ("Denver, CO","I-40/I-70 · ~1,000 mi","2–3 days","$700–$980"),("Orlando, FL","I-40/I-75 · ~1,000 mi","2–3 days","$700–$980")]
BODY.append(rate_table('Lanes &amp; Costs','Little Rock Car Shipping Lanes and Estimated Costs',
 'Where Little Rock cars go, in every direction from the crossroads, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates, running sedan, open trailer. SUVs and pickups add roughly 10 to 25 percent, and enclosed adds more. Ice season, the river, and the carriers free on your dates settle the final figure.',
 prose(
  P('Little Rock prices among the best in the mid-South. The state’s trucking companies keep more carriers here than the city alone would. Memphis and Nashville ride 40 east, Dallas rides 30, and Fort Smith and Tulsa ride 40 west.'),
  P('The Texas lane runs full all year. The Air Force lanes to the big bases fill each summer. The <a href="car-shipping-cost.html">cost guide</a> has the rest of the arithmetic.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Air Base, the Medical School, the State, and the Headquarters',
 prose(
  L('Little Rock relocates airmen, residents, state employees, and corporate staff, and the base sets the summer pace.'),
  P('Little Rock Air Force Base in Jacksonville is the home of the airlifter fleet. Crews and families rotate through it all year, and summer is the peak. The orders pay to move one car, and the second one comes with us. The gate stops the truck. The handoff happens on John Harden Drive or at a lot off 67. The <a href="military-car-shipping.html">military</a> page covers the planning.'),
  P('The medical school and its hospital on Markham Street bring in residents every July. The children’s hospital and the two other systems hire nurses on start dates. Most arrive from out of state with a car. The handoff happens on Markham or at a lot off 630 rather than in a hospital garage.'),
  P('The state offices around the Capitol hire on the fiscal year and relocate staff on the session calendar. The department-store headquarters, the telecom headquarters, and the investment bank downtown relocate staff on start dates. The jet completion center at the airport moves technicians on program schedules. The records an employer needs for reimbursement come from us.'),
  P('The Guard post in North Little Rock runs training cycles all year. The veterans hospital on the hill above it hires on start dates. The technology company in Conway and the two colleges there add their own calendars.'),
  P('Retirees settle at Hot Springs Village and the lakes, and many ship a car in from the Midwest. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side of any relocation.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Ice Storms, Tornadoes, the River, and the Marathon',
 prose(
  L('Little Rock’s weather comes in three kinds, and the ice is the one the carriers respect most.'),
  P('Ice storms shut 40 and 30 for a day or two a few times a decade. Nothing moves a loaded trailer on glazed pavement. The carriers wait it out. A winter pickup can slide a day or two. We call the moment the forecast changes the plan.'),
  P('Tornado season runs March through May. The 2023 tornado cut across West Little Rock along Cantrell Road, and nobody here has forgotten it. A warning parks the driver until the all-clear. Hail in the forecast moves the window.'),
  P('The river rose to a record in 2019. Riverdale, the River Market lots, and the park roads went under water. Rebsamen Park Road itself closes in a flood. A pickup near the river moves to Cantrell Road or University Avenue until the water falls.'),
  P('Summer runs past ninety-five degrees from June into September, and the loading hour moves to early morning. The marathon closes downtown, Riverdale, and the Heights on a Sunday in March. The state fair fills Roosevelt Road for ten days in October.'),
 )+chips(["Downtown","River Market","Quapaw Quarter","MacArthur Park","Hillcrest","The Heights","Riverdale","Capitol View","Stifft Station","Midtown","West Little Rock","Chenal","Pleasant Valley","Otter Creek","Southwest Little Rock","North Little Rock","Argenta","Park Hill","Maumelle","Sherwood","Jacksonville","Cabot","Benton","Bryant","Conway","Pine Bluff"])
 +NOTE('Serving Little Rock and all of central Arkansas. Tell us the neighborhood, the gate, and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Little Rock?',
 prose(
  L('Open is how Arkansas ships, and the 40 and 30 lanes are priced for it.'),
  P('An enclosed trailer keeps the hail, the pollen, and attention off the car. The garages in the Heights and Chenal book enclosed trailers. So does a collector car headed to the shows in Texas.'),
  P('A daily driver rides open and arrives the way it left. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages set out what the roof is worth.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff on University Avenue or at a lot off the loop, and a delivery. The ice picks the day in winter.'),
  P('Accept the price, and a carrier already running 40 or 30 takes the booking. We set the spot the same day. The driver and you walk around the car and record its condition on a Bill of Lading. Both sign, and the delivery check runs against it.'),
 )+ULI([
  "Clear anything personal out of the car",
  "Leave about a quarter tank of gas",
  "Photograph the car before pickup, especially after a hail storm",
  "Give the driver a working key and note any mechanical issue",
  "Switch off any aftermarket alarm",
  "In a gated subdivision, plan to meet the truck at the entrance",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages fill in the rest.'))))

BODY.append(sec('Why Ship Guy','Why Little Rock Drivers Choose Ship Guy',
 prose(
  L('We work 40 and 30 every day and plan around the ice, the river, and the orders.'),
  P('The FMCSA carries Ship Guy as an active broker. The $75,000 surety bond behind the license is on file. Both are a matter of public record. Our office is on Rebsamen Park Road in Riverdale.'),
  P('The coordinator who prices your move is the one who sees it to the door. Open, enclosed, and expedited transport are all bookable, and the <a href="services.html">services</a> page lists them.'),
 ), alt=True))

BODY.append(office('Little Rock','1207 Rebsamen Park Rd #354','Little Rock, AR 72202','+15014322427','(501) 432-2427','CT',
 '1207+Rebsamen+Park+Rd+%23354,+Little+Rock,+AR+72202','Visit Us','Find Ship Guy in Little Rock',
 'Our office is on Rebsamen Park Road in Riverdale, below Cantrell Hill and beside the river.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5040.430651473453!2d-92.3096041!3d34.761292999999995!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x87d2a3cfcd480a0b%3A0xb9f191aaa1761409!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792153823441!5m2!1sen!2sus'))

FAQ=[
 ("Why is car shipping from Little Rock so easy to book?","Because the trucks are already here. Two of the largest trucking companies in the country are based in Arkansas. Interstate 40 and 30 cross in the city. A Little Rock car rides a carrier already making the trip, in almost any direction."),
 ("How much does it cost to ship a car from Little Rock to Dallas or Memphis?","Dallas runs three hundred to four hundred forty dollars for a sedan. That is about three hundred twenty miles down Interstate 30. Memphis runs one hundred eighty to two hundred ninety, about one hundred forty miles on 40. SUVs and pickups add 10 to 25 percent."),
 ("Do you handle a PCS move to Little Rock Air Force Base?","Yes, every week, with a summer peak. The base in Jacksonville rotates airlifter crews and families year round. The orders pay to move one car, and the second one comes with us. The gate stops the truck. The handoff happens on John Harden Drive or at a lot off 67. Ship Guy is a private broker with no connection to the base."),
 ("Can the carrier come into Hillcrest or the Heights?","Usually not. The streets wind up the hill under low trees with cars at both curbs. The driver meets you on Kavanaugh, on Cantrell, or on University Avenue. West Little Rock and the suburbs usually allow the curb, gate permitting."),
 ("What happens if an ice storm hits on my pickup day?","The carriers wait it out. Freezing rain shuts 40 and 30 for a day or two a few times a decade. No one moves a loaded trailer on glazed pavement. A winter pickup can slide a day or two. You hear from us as the forecast changes, and we reschedule as soon as the roads clear."),
 ("Do you ship cars for residents at UAMS?","Yes, every July. Residents arrive from every state, and most bring a car. The handoff happens on Markham Street or at a lot off 630, not in the hospital garage. We plan the pickup around the report date."),
 ("What happens if the river floods Riverdale on my pickup day?","It moves up the hill. The 2019 flood kept Riverdale, the River Market lots, and Rebsamen Park Road under water for weeks. The handoff shifts to Cantrell Road or University Avenue until the river drops."),
 ("Can you pick up in Chenal, Maumelle, or another gated subdivision?","Yes, at the gate or the shopping center. Give us the gate code or the guard arrangement when you book. The newest streets past 430 are not always on a carrier’s map. Send the full address and the nearest cross street."),
 ("Can you ship a car that does not run from Little Rock?","Yes. A winch-equipped carrier takes it, and the longer loading is part of the price. The spot has to be flat and open, which usually means a lot on University Avenue. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Little Rock car shipping quote?","Both addresses, with the neighborhood and the gate on this end. The year, make, and model. Whether it runs. Open or enclosed. Your dates, with the report date or the ice in mind. That is a complete Little Rock request."),
]
BODY.append(faq_section(FAQ,'Little Rock FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Little Rock?','Run the form above for a price in about two minutes. Tell us the neighborhood and your dates, and a carrier already crossing Arkansas takes it from there.','+15014322427','(501) 432-2427','Get your free Little Rock quote'))

build({
 'slug':'auto-transport-little-rock-arkansas',
 'title':'Car Shipping in Little Rock, AR — Auto Transport | Ship Guy',
 'meta':'Car shipping in Little Rock, AR where Interstate 40 meets 30. Air Force base second vehicles, UAMS residents, Hillcrest and Heights meeting spots, West Little Rock gates, state and headquarters relocations, ice storm, tornado, and river-flood planning. Local office on Rebsamen Park Road in Riverdale. Free quote.',
 'h1':'Car Shipping in<br>Little Rock, <span class="accent">Arkansas</span>',
 'lede':'Open, enclosed, and expedited auto transport across central Arkansas, planned around the crossroads, the ice, and the river.',
 'tel':'+15014322427','disp':'(501) 432-2427','brand':'Little Rock','keyword':'car shipping in little rock',
 'localterms':['little rock','interstate 40','interstate 30','interstate 430','interstate 440','interstate 630','us 67','cantrell','kavanaugh','university avenue','markham','rebsamen park road','chenal parkway','john harden drive','geyer springs','big rock','downtown','river market','quapaw quarter','hillcrest','the heights','riverdale','capitol view','west little rock','chenal','pleasant valley','north little rock','argenta','park hill','maumelle','sherwood','jacksonville','cabot','benton','bryant','conway','pine bluff','hot springs village','air force base','airlifter','orders','medical school','hospital','residents','children’s hospital','capitol','state offices','department-store','telecom','investment bank','jet completion','guard post','veterans hospital','technology company','trucking companies','ice storms','tornado','hail','river','flood','2019','marathon','state fair','memphis','fayetteville','fort smith','dallas','tulsa','st. louis','nashville','houston','atlanta','denver','orlando','texas'],
}, BODY, FAQ)
