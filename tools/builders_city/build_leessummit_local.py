import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Lee’s Summit, Missouri','Car shipping for the lake communities and the southeast suburbs, on US 50 and the 470 loop',
 ['Car shipping in Lee’s Summit is a suburban booking with a gate code attached more often than not. Ship Guy is a licensed auto transport broker with an office on Southwest Main Street downtown.',
  'We book vetted carriers across the southeast metro, from Lakewood and Raintree to Greenwood and Lake Lotawana. We do not own the trucks.',
  'Interstate 470 crosses the north side of the city and ties into 70 and 435. US 50 runs through the middle of town toward Sedalia and Whiteman. Route 291 runs north to Independence, and Route 150 crosses the south side.',
  'This page covers the loop and US 50, the lake gates, the retirement village, and the hospitals. It also covers Whiteman, the federal campus, the downtown calendar, and the lanes.'],
 'Lee’s Summit at a glance',
 ['Most pickups happen within 1 to 3 days. The 470 loop puts every carrier passing Kansas City within ten minutes of the city.',
  'Topeka, Wichita, Omaha, Des Moines, and Columbia are all same-day deliveries. Tulsa, St. Louis, and Oklahoma City need a day. Chicago, Dallas, and Denver need one to two.'],
 'Tell us the addition and the gate. Lakewood, Raintree, and the lake roads meet the truck at the entrance. The newer additions off 291 and 150 usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 470, US 50, Route 291, 150, and the Loop',
 prose(
  L('Lee’s Summit sits on the southeast corner of the Kansas City loop. Every carrier that circles the metro passes it.'),
  P('Interstate 470 runs across the north side of the city between Interstate 70 and 435. The View High, Douglas, and 291 exits carry the city traffic. From the loop, 70 reaches St. Louis and 35 reaches Texas and Minnesota.'),
  P('US 50 runs through the middle of town. West it reaches the loop, and east it reaches Sedalia and the air base at Knob Noster. Route 291 runs north through the east side to Independence. Route 150 crosses the south side to Grandview and Interstate 49.'),
  P('Chipman Road, Ward Road, and Pryor Road are the section lines carriers use across the city. Blue Parkway is the old US 50 through the center. None of the roads charges a toll.'),
  P('Our office sits on Southwest Main Street in the historic downtown, by the rail line.'),
 ), alt=True))

BODY.append(sec('The Lake Communities','Lakewood, Raintree, Lotawana, Winnebago, and the Gates',
 prose(
  L('Lee’s Summit was built around lakes, and the lake roads were built for golf carts rather than trailers.'),
  P('Lakewood and Raintree are gated communities with winding lake roads a loaded trailer cannot turn on. The driver meets you at the gate or at the clubhouse lot. Tell us the gate arrangement when you book.'),
  P('Lake Lotawana and Lake Winnebago are private lake communities with narrow shoreline roads and low bridges. The handoff happens at the entrance or on the county road outside. Boats and jet skis ship separately, and we can arrange those too.'),
  P('New Longview and the additions along Chipman and Ward are open grids. The truck usually reaches the curb there. The subdivisions off 291 and 150 are the same. Some streets in the newest additions are not on a carrier’s map yet, so send the full address.'),
  P('Downtown runs on street parking and a festival calendar. The handoff happens on Douglas Street or at a lot by US 50.'),
 )))

ROUTES=[("Topeka, KS","I-470/I-70 · ~85 mi","Same day","$160–$260"),("Columbia, MO","I-70 · ~120 mi","Same day","$180–$290"),
 ("Omaha, NE","I-29 · ~205 mi","Same day","$230–$350"),("Wichita, KS","I-35 · ~200 mi","Same day","$230–$350"),
 ("Des Moines, IA","I-35 · ~210 mi","Same day","$230–$350"),("St. Louis, MO","I-70 · ~245 mi","1 day","$250–$370"),
 ("Tulsa, OK","US-71/I-49/I-44 · ~260 mi","1 day","$250–$380"),("Oklahoma City, OK","I-35 · ~360 mi","1 day","$320–$470"),
 ("Dallas, TX","I-35 · ~545 mi","1–2 days","$450–$640"),("Phoenix, AZ","I-35/I-40 · ~1,250 mi","3–4 days","$880–$1,200")]
BODY.append(rate_table('Lanes &amp; Costs','Lee’s Summit Car Shipping Lanes and Estimated Costs',
 'The lanes Lee’s Summit books most, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a sedan that runs, open trailer. Expect about 10 to 25 percent more for an SUV or pickup, and more again for enclosed. Hail season, ice, and the carriers free on your dates fix the final figure.',
 prose(
  P('Lee’s Summit prices like Kansas City, because the 470 loop puts it ten minutes from the same carriers. Columbia and St. Louis ride 70 east from the loop, and Wichita and Dallas ride 35 south.'),
  P('The Arizona lane runs every fall when the retirement village and the lake communities send their cars south. The <a href="car-shipping-cost.html">cost guide</a> explains the rest of the number.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Retirement Village, the Hospitals, the Federal Campus, and Whiteman',
 prose(
  L('Lee’s Summit relocates retirees, nurses, federal engineers, and Air Force families, each on a calendar of their own.'),
  P('The retirement village on the east side is one of the largest in the country. Residents arrive from across the Midwest with a car. Many ship it rather than drive it in, and many ship it to Arizona or Florida each fall. Our <a href="snowbird-car-shipping.html">snowbird</a> page has the planning tips.'),
  P('The two hospitals on the north side bring in nurses and physicians on start dates. The health-plan headquarters by the loop transfers staff in on start dates. The federal security campus across the line in south Kansas City brings engineers in from every state. If your employer reimburses the shipment, we send the documentation.'),
  P('Whiteman Air Force Base sits forty-five minutes east on US 50. Many of its families live in Lee’s Summit for the schools. The government moves one car under most orders, and we move the second. Because the base is gated, the handoff happens in Warrensburg or Knob Noster. The <a href="military-car-shipping.html">military</a> page covers the planning.'),
  P('The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side of a relocation.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Downtown Days, the Festivals, Hail, and Ice',
 prose(
  L('Lee’s Summit closes its downtown for festivals and loses its driveways to hail. The carriers plan for both.'),
  P('Downtown Days fills the historic district for a weekend in June. The fall festival does the same in October. The driver meets you on Douglas Street or by US 50 on those weekends rather than downtown.'),
  P('Hail is the bigger risk to a car waiting outside. The southeast metro has taken baseball hail more than once. We shift the window when it is forecast. A tornado warning parks the driver until the all-clear.'),
  P('Ice closes 470 and 50 for a day a few times each winter. The lake roads stay slick longer than the main roads. A winter pickup can slide a day. Summer heat moves the loading hour earlier.'),
 )+chips(["Downtown","Lakewood","Raintree","New Longview","Longview","Lake Lotawana","Lake Winnebago","Summit Woods","Chipman Road","Ward Road","Pryor Road","View High","Unity Village","Greenwood","Pleasant Hill","Raymore","Belton","Grandview","Blue Springs","Independence","Raytown","Kansas City"])
 +NOTE('Serving the southeast metro and the lake communities. Tell us the addition, the gate, and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Lee’s Summit?',
 prose(
  L('Most Lee’s Summit cars go open, and the loop lanes are priced accordingly.'),
  P('An enclosed trailer keeps hail, salt, and attention off the car. The garages in Lakewood and Raintree book enclosed trailers. So does a car headed to Scottsdale for the winter.'),
  P('A commuter car needs no roof for the trip. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages set out the difference.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a loading at the gate or near the loop, and a delivery. The hail forecast has a say in the timing.'),
  P('Accept the price and a carrier already circling the loop is assigned, with the spot named up front. At the gate, you and the driver complete a Bill of Lading and both sign. Delivery is inspected against it.'),
 )+ULI([
  "Take your belongings out of the car",
  "Run the tank down to about a quarter",
  "Photograph the car the morning of pickup, especially after hail",
  "Hand the driver a working key and mention any mechanical issue",
  "Shut off any aftermarket alarm",
  "In a gated community or on a lake road, plan to meet the truck at the entrance",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages walk you through the rest.'))))

BODY.append(sec('Why Ship Guy','Why Lee’s Summit Drivers Choose Ship Guy',
 prose(
  L('We work the loop every day and plan around the gates, the hail, and the base calendar.'),
  P('Ship Guy’s FMCSA brokerage authority is active and backed by a $75,000 surety bond. Both are on the public record. Our office is on Southwest Main Street downtown.'),
  P('A single coordinator runs your booking from quote to delivery, with open, enclosed, and expedited transport all available. The <a href="services.html">services</a> page describes them.'),
 ), alt=True))

BODY.append(office('Lee’s Summit','310 SW Main St #560','Lee’s Summit, MO 64063','+18162030327','(816) 203-0327','CT',
 '310+SW+Main+St+%23560,+Lee%27s+Summit,+MO+64063','Visit Us','Find Ship Guy in Lee’s Summit',
 'Our office is on Southwest Main Street in the historic downtown, by the rail line.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3832.1810979428355!2d-94.3777509!3d38.9113641!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x87c11f2f589633c5%3A0xe4df27c5a1b0c58f!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792076120878!5m2!1sen!2sus'))

FAQ=[
 ("Can the carrier come inside Lakewood, Raintree, or a lake community?","Usually not. The lake roads wind and the bridges are low, and a loaded trailer cannot turn on them. The driver meets you at the gate or at the clubhouse lot. Tell us the gate code or the guard arrangement when you book."),
 ("Is Lee’s Summit priced the same as Kansas City?","Yes. The 470 loop puts the city ten minutes from the same carriers. A Lee’s Summit pickup prices like a Kansas City one. Greenwood, Pleasant Hill, and the lake communities add a few dollars for the extra miles."),
 ("How much does it cost to ship a car from Lee’s Summit to Arizona or Florida?","Phoenix runs eight hundred eighty to twelve hundred dollars for a sedan. That is about twelve hundred fifty miles on 35 and 40. Orlando runs about the same on 70 and 75. Fall southbound costs more than spring. SUVs and pickups add 10 to 25 percent."),
 ("Do you handle a PCS move to Whiteman from Lee’s Summit?","Yes. The base is forty-five minutes east on US 50. Many of its families live here for the schools. Most orders cover one car, and the second one travels with us. The gate stops the truck, so the handoff happens in Warrensburg or Knob Noster. Ship Guy is a private broker with no connection to the base."),
 ("Do you ship cars for residents moving into the retirement village?","Yes, every week. Residents arrive from across the Midwest, and many ship the car rather than drive it in. The handoff happens at the village entrance or on Route 291. We also ship those cars to Arizona and Florida each fall and home each spring."),
 ("What happens if hail is forecast on my pickup day?","We shift the window. A car waiting outside on a hail day is the real risk in the southeast metro. If a storm is already overhead, the driver pulls off and waits."),
 ("Does Downtown Days or the fall festival affect pickups?","Downtown, yes. The historic district closes for a weekend in June and again in October. The driver meets you on Douglas Street or by US 50 on those weekends. The rest of the city runs normally."),
 ("Can you pick up in a brand-new addition off 291 or 150?","Yes. Some streets in the newest additions are not on a carrier’s map yet. Send the full address and the nearest section line, and the driver meets you on the paved road. Most of those streets are wide enough for the curb."),
 ("Can you ship a car that does not run from Lee’s Summit?","Yes. A winch carrier is booked and the longer loading is priced in. The spot has to be flat, which usually means the clubhouse lot rather than a lake road. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Lee’s Summit car shipping quote?","The addresses at both ends, with the addition and the gate here. Year, make, model. Does it run. Open or enclosed. Your dates. That completes a Lee’s Summit request."),
]
BODY.append(faq_section(FAQ,'Lee’s Summit FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Lee’s Summit?','The form above takes two minutes. Send the addition and your dates, and a carrier already circling the loop takes the job.','+18162030327','(816) 203-0327','Get your free Lee’s Summit quote'))

build({
 'slug':'auto-transport-lees-summit-missouri',
 'title':'Car Shipping in Lee’s Summit, MO — Auto Transport | Ship Guy',
 'meta':'Car shipping in Lee’s Summit, MO on the 470 loop and US 50. Gated lake-community handoffs at Lakewood, Raintree, and Lotawana, retirement village moves, hospital and federal campus relocations, Whiteman second vehicles, hail and ice planning. Local office on Southwest Main Street. Free quote.',
 'h1':'Car Shipping in<br>Lee’s Summit, <span class="accent">Missouri</span>',
 'lede':'Open, enclosed, and expedited auto transport across the southeast metro, planned around the gates, the loop, and the hail.',
 'tel':'+18162030327','disp':'(816) 203-0327','brand':'Lee’s Summit','keyword':'car shipping in lee’s summit',
 'localterms':['summit','interstate 470','us 50','route 291','route 150','interstate 49','chipman','ward road','pryor','blue parkway','view high','douglas street','downtown','lakewood','raintree','lake lotawana','lake winnebago','new longview','longview','summit woods','unity village','greenwood','pleasant hill','raymore','belton','grandview','blue springs','independence','gated','gate','clubhouse','boats','retirement village','hospitals','health-plan','federal security campus','whiteman','knob noster','warrensburg','downtown days','festival','hail','ice','tornado','arizona','scottsdale','florida','topeka','columbia','omaha','wichita','des moines','st. louis','tulsa','oklahoma city','dallas','phoenix','kansas city'],
}, BODY, FAQ)
