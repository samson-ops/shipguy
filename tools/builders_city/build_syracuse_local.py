import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Syracuse, New York','Car shipping in the snowiest big city in the country, at the crossroads of the state',
 ['Car shipping in Syracuse is booked around a snow total most cities never see. Ship Guy is a licensed auto transport broker with an office on South Clinton Street downtown.',
  'We book vetted carriers across Onondaga County, from Liverpool and Clay to DeWitt, Manlius, and Camillus. We do not own the trucks.',
  'Interstate 81 and the Thruway cross just north of the city. Interstate 690 runs east and west through downtown. The elevated stretch of 81 downtown is coming down, and through traffic is moving to the 481 loop.',
  'This page covers the interstates and the viaduct project, the hill and the hospitals, and the neighborhoods. It also covers the fair, the car show, the winter, and the lanes.'],
 'Syracuse at a glance',
 ['Most pickups happen within 1 to 3 days. A lake-effect band over the city can add a snow day in winter.',
  'Rochester, Albany, Buffalo, and Binghamton are same-day lanes. New York City, Boston, and Cleveland take a day. Florida runs three to four.'],
 'Tell us the neighborhood and the month. The university hill and Tipperary Hill need a meeting spot. Liverpool, Clay, and DeWitt usually meet the truck at the curb.'))

BODY.append(sec('The Roads','Interstate 81, the Thruway, 690, and the Viaduct Coming Down',
 prose(
  L('Syracuse sits where the north-south and east-west lanes of upstate cross, and both are being rebuilt at once.'),
  P('Interstate 81 runs south to Binghamton and Scranton and north to Watertown and Fort Drum. The Thruway crosses it north of the city with a toll by the mile. Interstate 690 carries the city traffic east to DeWitt and west past the fairgrounds.'),
  P('The viaduct that carried 81 over downtown is being replaced with a street-level grid. Through traffic uses the 481 loop around the east side while the work goes on. Carriers follow the detour signs, and the downtown handoff happens on a street off the loop.'),
  P('Route 481 continues north to Oswego. Route 5 is Erie Boulevard, the retail strip through DeWitt. Route 11 is Salina Street north to the airport and Cicero.'),
  P('The mall by the lake sits at the 81 and 690 interchange. It has the biggest lots in the city. Many Syracuse handoffs happen there. The Thruway toll is paid by the carrier and built into every quote.'),
 ), alt=True))

BODY.append(sec('The Hill &amp; the Hospitals','The University, the Medical School, and the Chip Plant in Clay',
 prose(
  L('Syracuse relocates people up the hill in August and down it in May. The hospitals hire in between.'),
  P('The university and the forestry college sit on the hill east of downtown. Tens of thousands of students arrive each August and leave each May. The streets around the campus are steep and parked solid. The driver meets you at a lot on Erie Boulevard or near the dome lots.'),
  P('The medical school and the three hospitals on the hill bring in residents every June and July. Most come from out of state with a car and two weeks of notice. The handoff happens on a wide street below the hill rather than in a hospital garage.'),
  P('The chip plant going up in Clay is hiring engineers from across the country. The defense contractors by the airport and the research companies in the tech district do the same. If your employer reimburses the shipment, we send the documentation.'),
  P('Fort Drum sits seventy miles north on Interstate 81. Many soldiers route a second vehicle through Syracuse, and the <a href="military-car-shipping.html">military</a> page covers the planning. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers a longer relocation.'),
 )))

ROUTES=[("Binghamton, NY","I-81 · ~75 mi","Same day","$160–$260"),("Rochester, NY","I-90 · ~90 mi","Same day","$170–$270"),
 ("Albany, NY","I-90 · ~145 mi","Same day","$190–$300"),("Buffalo, NY","I-90 · ~150 mi","Same day","$190–$300"),
 ("New York, NY","I-81/I-80 · ~250 mi","1 day","$280–$420"),("Boston, MA","I-90 · ~310 mi","1 day","$320–$460"),
 ("Cleveland, OH","I-90 · ~330 mi","1 day","$320–$460"),("Washington, DC","I-81 · ~350 mi","1 day","$340–$490"),
 ("Chicago, IL","I-90 · ~690 mi","2 days","$520–$740"),("Orlando, FL","I-81/I-77/I-95 · ~1,200 mi","3–4 days","$850–$1,200")]
BODY.append(rate_table('Lanes &amp; Costs','Syracuse Car Shipping Lanes and Estimated Costs',
 'Where Syracuse cars go most often, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a running sedan on an open trailer, Thruway toll included. Add roughly 10 to 25 percent for an SUV or pickup, more for enclosed. Snow weeks and carrier availability on your dates decide the final number.',
 prose(
  P('Binghamton and Rochester are the quick lanes, under two hours in either direction. Interstate 81 carries the Washington lane straight down the mountains without a toll.'),
  P('New York City is a day away on 81 and Interstate 80. Downstate, the truck meets you at a spot rather than a doorstep. The <a href="car-shipping-cost.html">cost guide</a> explains the rest of the number.'),
 ), alt=True))

BODY.append(sec('The Winter','Lake Effect Off Ontario, the Tug Hill, and the Snow Days',
 prose(
  L('Syracuse wins the snowfall contest among big American cities most years, and the carriers know it.'),
  P('Lake-effect bands come off Lake Ontario from November into March. A band that sets up over the city can drop a foot overnight. The Tug Hill to the north takes far more. Interstate 81 toward Watertown closes to trucks a few times a winter.'),
  P('The plows keep 81, 690, and the Thruway open most days. A heavy week still slides a pickup by a day. We call the moment the forecast changes the plan.'),
  P('Road salt runs from November through April. Collector-car owners ride enclosed for that reason. A car arriving from a warm state needs a strong battery and winter oil.'),
  P('Spring and fall are the easy seasons. Summer brings the fair and the car show, and those close roads rather than weather.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Tipperary Hill, Eastwood, Westcott, the Northside, and the Suburbs',
 prose(
  L('Syracuse kept its streetcar-era streets. The hills around downtown were graded for a trolley rather than a trailer.'),
  P('Tipperary Hill, Strathmore, and the Westcott blocks near the university are steep and narrow. Cars line both curbs. The driver meets you on Genesee Street, Erie Boulevard, or a lot at the base of the hill.'),
  P('Eastwood, the Northside, and the Valley are flatter blocks of two-families with alley garages. The handoff happens on James Street, Salina Street, or a main road nearby. Downtown and Armory Square run on garages. Our office sits on South Clinton Street in the middle of it.'),
  P('Liverpool, Clay, Cicero, and North Syracuse are wide suburban grids where the truck reaches the curb. DeWitt, Fayetteville, and Manlius are the same on the east side, except in the older villages.'),
  P('Camillus, Solvay, and Baldwinsville sit west along 690. Skaneateles and the Finger Lakes villages are tight. The driver meets you on the state route at the village edge.'),
 )))

BODY.append(sec('The Calendar','The State Fair, the Car Show, and the Dome',
 prose(
  L('Syracuse closes the west side for the fair and fills the hill for basketball. The carriers plan around both.'),
  P('The state fair runs thirteen days through Labor Day at the fairgrounds west of the city. Interstate 690 and the roads around Geddes and Solvay crawl the whole time. We schedule west-side pickups before or after it.'),
  P('The car show in July brings thousands of classics and hot rods to the same fairgrounds. Collector cars ship into Syracuse that week on enclosed trailers, and the enclosed carriers book up early.'),
  P('Basketball and football at the dome fill the hill and the lots around it. Game days move a university-hill pickup to another day. The rest of the city runs normally.'),
 )+chips(["Downtown","Armory Square","University Hill","Westcott","Tipperary Hill","Strathmore","Sedgwick","Eastwood","Northside","Southside","The Valley","Inner Harbor","Liverpool","Clay","Cicero","North Syracuse","DeWitt","Fayetteville","Manlius","Jamesville","Camillus","Solvay","Baldwinsville","Skaneateles","Auburn","Oswego","Cortland"])
 +NOTE('Serving Onondaga County and the Finger Lakes villages. Tell us the neighborhood, the month, and whether the car runs.'), alt=True))

BODY.append(sec('Your Options','Open or Enclosed in Syracuse?',
 prose(
  L('Most Syracuse cars ride open, and the 81 and Thruway lanes are built around it.'),
  P('An enclosed trailer keeps salt, slush, and lake grit off the paint. The show cars headed to the fairgrounds in July ride enclosed. So do the collector garages in Fayetteville and Skaneateles.'),
  P('An everyday car travels open without a second thought. Our <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages set the two side by side.'),
 )))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a loading near the interchange, and a delivery. In winter, the lake has a say in the timing.'),
  P('Once you approve the price, a carrier already running Interstate 81 or the Thruway takes the booking. At the meeting spot, you and the driver note the car’s condition on a Bill of Lading. Both of you sign. That sheet is what the delivery inspection is measured against.'),
 )+ULI([
  "Remove personal belongings",
  "Keep about a quarter tank of fuel",
  "Photograph the vehicle before pickup, especially after a salty winter",
  "Provide a working key and disclose mechanical issues",
  "Disable aftermarket alarms",
  "On the university hill or Tipperary Hill, plan to meet the truck at a lot below the hill",
 ])+prose(P('Each step is laid out on the <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages.')), alt=True))

BODY.append(sec('Why Ship Guy','Why Syracuse Drivers Choose Ship Guy',
 prose(
  L('We work 81 and the Thruway every day and plan around the hill, the snow, and the fair.'),
  P('Our FMCSA brokerage authority is active and our $75,000 surety bond is on file, and both are public. Our office is on South Clinton Street downtown.'),
  P('A single coordinator handles the booking from first quote to delivery. Open, enclosed, and expedited transport are all on offer. See the <a href="services.html">services</a> page for the full list.'),
 )))

BODY.append(office('Syracuse','250 S Clinton St #473','Syracuse, NY 13202','+13158094321','(315) 809-4321','ET',
 '250+S+Clinton+St+%23473,+Syracuse,+NY+13202','Visit Us','Find Ship Guy in Syracuse',
 'Our office is on South Clinton Street downtown at the edge of Armory Square.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4931.525924343336!2d-76.1539416!3d43.049077499999996!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89d9f3224a60ac55%3A0x38dc398021d4c6fa!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792023078515!5m2!1sen!2sus'))

FAQ=[
 ("Does the snow delay a Syracuse pickup?","Sometimes by a day. A lake-effect band over the city can drop a foot overnight. Interstate 81 toward Watertown closes to trucks a few times a winter. The plows keep 81, 690, and the Thruway open most days. We call the moment the forecast changes the plan."),
 ("How does the Interstate 81 construction affect my pickup?","Mostly timing. The viaduct over downtown is being replaced. Through traffic runs on the 481 loop while the work goes on. Carriers follow the detour, and a downtown handoff happens on a street off the loop. The suburbs are not affected."),
 ("How much does it cost to ship a car from Syracuse to Florida?","Count on eight hundred fifty to twelve hundred dollars for a sedan to Orlando. Fort Myers and Naples add a little. The route runs about twelve hundred miles down Interstate 81, 77, and 95. November southbound costs more than spring. SUVs and pickups add 10 to 25 percent."),
 ("Is the Thruway toll added to my price?","No. Carriers pay the Thruway by the mile and quote with it included. The price you approve is the whole price. Interstate 81 and 690 charge nothing."),
 ("Can you ship a car for a Syracuse University or ESF student?","Yes. Student cars arrive each August and leave each May. The streets on the hill are steep and parked solid. The driver meets you at a lot on Erie Boulevard or near the dome. An adult signs for the car at pickup, and a parent can sign at the far end."),
 ("Do you ship cars for residents at the hospitals on the hill?","Yes, every June and July. The medical school and the three hospitals bring in residents from every state. Most arrive with a car and two weeks of notice. The handoff happens on a wide street below the hill rather than in a hospital garage."),
 ("Does the state fair affect pickups?","On the west side, yes. The fairgrounds in Geddes fill for thirteen days through Labor Day. Route 690 and the roads around Solvay crawl. We schedule west-side pickups before or after the fair. The rest of the county runs normally."),
 ("Can you ship a show car in for the July car show?","Yes. Classics and hot rods ship into the fairgrounds that week on enclosed trailers. The enclosed carriers book up early. Tell us the length of the car and whether it rolls. Three weeks of notice helps."),
 ("Can you ship a car that does not run from Syracuse?","Yes. We send a carrier with a winch, and the extra time to load goes into the quote. In winter the car has to be shoveled out and reachable. Say whether it rolls, steers, and brakes, because that sets the equipment."),
 ("What do you need for a Syracuse car shipping quote?","Pickup and delivery addresses, with the neighborhood or village on the Syracuse end. Year, make, and model. Whether it runs and rolls. Open or enclosed. The dates you can work with, and the month matters here. That is all a Syracuse quote takes."),
]
BODY.append(faq_section(FAQ,'Syracuse FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Syracuse?','Give the form above two minutes. Add the neighborhood and your dates. We will pair you with a carrier already running 81 or the Thruway.','+13158094321','(315) 809-4321','Get your free Syracuse quote'))

build({
 'slug':'auto-transport-syracuse-new-york',
 'title':'Car Shipping in Syracuse, NY — Auto Transport | Ship Guy',
 'meta':'Car shipping in Syracuse, NY where Interstate 81 meets the Thruway. Lake-effect planning, the 81 viaduct detour, university-hill and hospital handoffs, Fort Drum second vehicles, state fair and car show timing, tolls built in. Local office on South Clinton Street. Free quote.',
 'h1':'Car Shipping in<br>Syracuse, <span class="accent">New York</span>',
 'lede':'Open, enclosed, and expedited auto transport across Onondaga County, planned around the interchange, the hill, and the snow.',
 'tel':'+13158094321','disp':'(315) 809-4321','brand':'Syracuse','keyword':'car shipping in syracuse',
 'localterms':['syracuse','interstate 81','thruway','interstate 690','481','viaduct','erie boulevard','salina street','genesee street','james street','mall','downtown','armory square','south clinton','university hill','westcott','tipperary hill','strathmore','eastwood','northside','the valley','liverpool','clay','cicero','north syracuse','dewitt','fayetteville','manlius','camillus','solvay','baldwinsville','skaneateles','finger lakes','university','forestry','medical school','hospitals','residents','chip plant','defense','fort drum','watertown','lake-effect','lake ontario','tug hill','salt','state fair','fairgrounds','geddes','car show','dome','basketball','rochester','albany','buffalo','binghamton','boston','cleveland','washington','chicago','orlando'],
}, BODY, FAQ)
