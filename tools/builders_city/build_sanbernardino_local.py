import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('San Bernardino, California','Car shipping at the foot of the Cajon Pass, in the warehouse capital of the West',
 ['Car shipping in San Bernardino happens in one of the busiest freight counties in the country. Ship Guy is a licensed auto transport broker with an office on South Waterman Avenue.',
  'We book vetted carriers across the Inland Empire, from Highland and Redlands to Colton, Rialto, and Fontana. We do not own the trucks.',
  'Interstate 10 runs along the south edge of the city, and Interstate 215 runs through the middle. Interstate 15 climbs the Cajon Pass ten miles west, and the 210 runs along the foothills. Highway 18 climbs from Waterman Avenue to Lake Arrowhead and Big Bear.',
  'This page covers the freeways and the pass, the old city, the north end, and the mountain towns. It also covers the warehouses, the hospitals, the university, the wind, the fire, and the lanes.'],
 'San Bernardino at a glance',
 ['Most pickups happen within 1 to 3 days. The 10 and the 15 carry carriers past the city from every direction all day.',
  'Los Angeles, Orange County, and San Diego are same-day lanes. Las Vegas is the same day too. Phoenix and Bakersfield take a day. The Bay Area and Salt Lake City take one to two.'],
 'Tell us the neighborhood. The old city around downtown and the Westside needs a meeting spot. The north end, Highland, and Redlands usually allow the curb. The mountain towns ship from the bottom of the hill.'))

BODY.append(sec('The Roads','Interstate 10, 215, 15, the 210, Highway 18, and the Cajon Pass',
 prose(
  L('San Bernardino sits where the roads to Los Angeles, Phoenix, and Las Vegas all come together.'),
  P('Interstate 10 runs along the south edge of the city from Los Angeles to Palm Springs and Phoenix. Interstate 215 runs north and south through downtown between Riverside and the pass. The two cross by Hospitality Lane, and the warehouses line both.'),
  P('Interstate 15 climbs the Cajon Pass from Devore to Victorville and the high desert. It is the road to Las Vegas and Salt Lake City. The pass closes for snow, wind, and fire a few times each year. The 210 runs along the foothills from Pasadena through Highland to Redlands.'),
  P('Highway 18 leaves Waterman Avenue and climbs to Crestline, Lake Arrowhead, and Big Bear. Highway 330 climbs from Highland to Running Springs. Both carry chain controls from November into April. The carriers come off the 10 at Waterman and Tippecanoe. On the 215 they use Orange Show Road and University Parkway.'),
  P('The lots along Hospitality Lane and at the mall by the 10 are the usual meeting spots. No road in the county charges a toll. Our office sits on South Waterman Avenue, a block from Hospitality Lane and the 10.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the Westside, the North End, Highland, Redlands, and the Hill',
 prose(
  L('San Bernardino is an old railroad city, a ring of postwar grids, and a mountain range. Each one parks differently.'),
  P('Downtown and the blocks around the old depot have narrow streets, alleys, and one-way pairs. The Westside and Muscoy have unpaved shoulders and no curbs in places. The driver meets you on Mount Vernon, on Highland Avenue, or at a lot by the 215.'),
  P('The north end, Verdemont, and the streets around the university are newer grids. The truck usually reaches the curb there. Highland, Redlands, Loma Linda, and Grand Terrace are the same, with a few gated additions along the foothills. The handoff there happens at the gate.'),
  P('The mountain towns are a different trip. Lake Arrowhead, Crestline, Running Springs, and Big Bear sit above five thousand feet. The roads up have chain controls and no shoulders. A loaded trailer meets you at the bottom of the hill in Highland or on Waterman. On a clear day a lot in the village works too.'),
  P('Colton, Rialto, and Fontana sit on the 10 and the 210 with the warehouses. Many employers there let the truck load at the dock.'),
 )))

ROUTES=[("Los Angeles, CA","I-10 · ~60 mi","Same day","$120–$200"),("Irvine, CA","CA-91/CA-55 · ~60 mi","Same day","$120–$200"),
 ("San Diego, CA","I-215/I-15 · ~110 mi","Same day","$150–$250"),("Las Vegas, NV","I-15 · ~220 mi","Same day","$230–$350"),
 ("Phoenix, AZ","I-10 · ~310 mi","1 day","$300–$440"),("Bakersfield, CA","I-15/CA-58 · ~170 mi","1 day","$200–$310"),
 ("San Jose, CA","I-5/CA-152 · ~410 mi","1 day","$360–$520"),("Salt Lake City, UT","I-15 · ~640 mi","1–2 days","$510–$720"),
 ("Denver, CO","I-15/I-70 · ~960 mi","2–3 days","$690–$960"),("Dallas, TX","I-10/I-20 · ~1,340 mi","3 days","$890–$1,230")]
BODY.append(rate_table('Lanes &amp; Costs','San Bernardino Car Shipping Lanes and Estimated Costs',
 'San Bernardino’s most-booked lanes in every direction, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a sedan that runs, on an open trailer. Figure 10 to 25 percent more for an SUV or pickup, and more again for enclosed. The pass, the wind, and the carriers free on your dates set the final figure.',
 prose(
  P('San Bernardino prices like Los Angeles, because the warehouses keep trucks here by the thousand. Las Vegas and Salt Lake ride the 15 over the pass, and Phoenix rides the 10 east.'),
  P('The Texas and Arizona lanes run full with relocations. The high desert adds its own traffic to the 15. The <a href="car-shipping-cost.html">cost guide</a> lays out the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Warehouses, the Hospitals, the University, and the Base',
 prose(
  L('San Bernardino relocates people on the warehouse opening, the residency match, the semester, and the orders.'),
  P('The warehouses along the 10, the 215, and the 210 hire managers and drivers from every state. The air cargo hub at the airport and the rail yard run on their own schedules. Many employers allow a handoff at the dock. We supply the paperwork for a reimbursed move.'),
  P('The university medical center in Loma Linda is one of the largest in the region. It brings in residents every July. The county hospital in Colton and the two hospitals in the city hire nurses on start dates. The handoff happens on Barton Road or at a lot by the 10, not in a hospital garage.'),
  P('The state university on the north end fills each August and empties each May. The private university in Redlands does the same. The campus lots handle the handoff. An adult signs for a student car.'),
  P('The old air base is a cargo airport now. March Air Reserve Base sits twenty minutes south on the 215. Fort Irwin sits two hours up the 15. Families from both live in the city and the foothills. One car moves on the orders, and the other one rides with us. The <a href="military-car-shipping.html">military</a> page covers the planning, and the <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Cajon Pass, Santa Ana Winds, Fire Season, and the Heat',
 prose(
  L('San Bernardino’s weather comes through the pass, and so does everything else.'),
  P('The Santa Ana winds blow hardest through the Cajon Pass. They overturn high-profile trucks on the 15 every fall. The carriers hold at the bottom of the pass until the wind advisory lifts. A Las Vegas pickup can slide a day in that case, and we call ahead.'),
  P('Fire season runs from June into December. The foothills above the 210 have burned more than once in recent years. The pass closes for fire too, and smoke settles on the valley for days. An evacuation order moves the pickup down to the flats for a day. We call when it does.'),
  P('Summer runs past one hundred degrees from June into September, and the loading hour moves to dawn. Winter brings snow to the mountains from November into April. Chain controls go up on 18 and 330, and the pass closes now and then. A mountain pickup waits for the plows and the chain controls to lift.'),
  P('Flash floods come off the mountains after a summer storm or a winter atmospheric river. The washes across the foothills close for a day. Smog settles in the summer, and it changes nothing for a carrier.'),
 )+chips(["Downtown","Westside","Muscoy","North End","Verdemont","Arrowhead","Del Rosa","Highland","Redlands","Loma Linda","Colton","Rialto","Fontana","Grand Terrace","Yucaipa","Devore","Waterman Avenue","Hospitality Lane","Tippecanoe","University Parkway","Cajon Pass","Crestline","Lake Arrowhead","Running Springs","Big Bear","Victorville"])
 +NOTE('Serving San Bernardino and the whole east valley. Tell us the neighborhood, the month, and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in San Bernardino?',
 prose(
  L('Open is how the Inland Empire ships, and the 10 and the 15 are priced for it.'),
  P('An enclosed trailer keeps the dust, the wind, and the sun off the car. The garages in Redlands and along the foothills book enclosed trailers. So does a collector car that spends the summer in Big Bear.'),
  P('A commuter car rides open over the pass without trouble. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain what the roof is worth.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a loading by the 10 or at the bottom of the hill, and a delivery. The pass and the wind pick the day.'),
  P('Approve the price and a carrier already working the 10 or the 15 takes the job. We set the spot. The driver inspects the car with you there and records it on a Bill of Lading. Both sign, and the car is checked against that sheet at delivery.'),
 )+ULI([
  "Take anything personal out of the car",
  "Leave about a quarter tank of fuel in it",
  "Photograph the car before pickup, especially after a wind storm",
  "Leave a working key and point out anything mechanical",
  "Switch the aftermarket alarm off",
  "For a mountain address, plan to meet the truck at the bottom of the hill",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages have the rest.'))))

BODY.append(sec('Why Ship Guy','Why San Bernardino Drivers Choose Ship Guy',
 prose(
  L('We work the 10, the 215, and the pass every day. We plan around the wind, the fire, and the snow.'),
  P('Ship Guy carries active FMCSA brokerage authority, and a $75,000 surety bond is posted behind every booking. Both are searchable on the federal register. Our office is on South Waterman Avenue.'),
  P('The coordinator who quotes the move sees it through to delivery. Open, enclosed, and expedited transport are all bookable. The <a href="services.html">services</a> page explains each one.'),
 ), alt=True))

BODY.append(office('San Bernardino','1274 S Waterman Ave #425','San Bernardino, CA 92408','+19093163408','(909) 316-3408','PT',
 '1274+S+Waterman+Ave+%23425,+San+Bernardino,+CA+92408','Visit Us','Find Ship Guy in San Bernardino',
 'Our office is on South Waterman Avenue, a block from Hospitality Lane and the Interstate 10 exit.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4079.1789453399174!2d-117.27923229999999!3d34.0784521!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80dcadb6138a8c09%3A0xe25f78efda1bf396!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792077115093!5m2!1sen!2sus'))

FAQ=[
 ("What happens when the Cajon Pass closes?","The trucks wait at the bottom. The pass closes for snow, high wind, and fire a few times each year. Usually it is a few hours. The carriers hold in Devore or at the truck stops by the 15 until it reopens. A Las Vegas pickup can lose a day, and you hear from us first."),
 ("How much does it cost to ship a car from San Bernardino to Las Vegas or Phoenix?","Las Vegas runs two hundred thirty to three hundred fifty dollars for a sedan. That is about two hundred twenty miles over the pass. Phoenix runs three hundred to four hundred forty. That is about three hundred ten miles on Interstate 10. SUVs and pickups add 10 to 25 percent."),
 ("Can you deliver to Lake Arrowhead, Big Bear, or Crestline?","Yes, with a meeting spot. A loaded trailer meets you at the bottom of the hill in Highland or on Waterman. On a clear day a lot in the village works too. Chain controls from November into April add a day or two to a mountain pickup."),
 ("Do you ship cars for people hired at the warehouses or the cargo hub?","Yes, on start dates all year. The warehouses along the 10, the 215, and the 210 hire managers and drivers from every state. Many allow a handoff at the dock. We supply the paperwork for a reimbursed move."),
 ("What happens if the Santa Ana winds hit on my pickup day?","The carrier holds until the wind advisory lifts, especially for anything headed over the pass. A loaded trailer is a sail in a sixty-mile-an-hour crosswind. A pickup in the valley usually goes ahead. A Las Vegas run waits a few hours or a day."),
 ("Do you ship cars for residents at Loma Linda?","Yes, every July. Residents and fellows arrive from every state, and most bring a car. The handoff happens on Barton Road or at a lot by the 10, not in a hospital garage."),
 ("Can you ship a car for a Cal State San Bernardino or University of Redlands student?","Yes. The cars come in each August and leave each May. The campus lots on the north end and in Redlands handle the handoff. An adult signs for the car at pickup, and a parent can sign at delivery."),
 ("Do you handle a PCS move to March or Fort Irwin from San Bernardino?","Yes. March sits twenty minutes south on the 215. Fort Irwin sits two hours up the 15 past Barstow. One car moves on the orders, and the other one rides with us. Both gates stop the truck, so the handoff happens outside them. Ship Guy is a private broker with no connection to either base."),
 ("Can you ship a car that does not run from San Bernardino?","Yes. A carrier with a winch is booked, and the longer loading is priced in. The spot has to be flat and open, which usually means a lot by Hospitality Lane. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a San Bernardino car shipping quote?","Both addresses, with the neighborhood on this end and the elevation if it is a mountain address. The year, make, and model. Whether it runs. Open or enclosed. Your dates, with the pass in mind. That is a complete San Bernardino request."),
]
BODY.append(faq_section(FAQ,'San Bernardino FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in San Bernardino?','The form above returns a price in about two minutes. Tell us the neighborhood and your dates, and a carrier already working the 10 takes it from there.','+19093163408','(909) 316-3408','Get your free San Bernardino quote'))

build({
 'slug':'auto-transport-san-bernardino-california',
 'title':'Car Shipping in San Bernardino, CA — Auto Transport | Ship Guy',
 'meta':'Car shipping in San Bernardino, CA at the foot of the Cajon Pass on the 10, the 215, and the 15. Downtown and Westside meeting spots, north end and Redlands curbside, mountain-town handoffs for Big Bear and Lake Arrowhead, warehouse and Loma Linda relocations, Santa Ana wind and fire planning. Local office on South Waterman Avenue. Free quote.',
 'h1':'Car Shipping in<br>San Bernardino, <span class="accent">California</span>',
 'lede':'Open, enclosed, and expedited auto transport across the Inland Empire, planned around the pass, the wind, and the fire season.',
 'tel':'+19093163408','disp':'(909) 316-3408','brand':'San Bernardino','keyword':'car shipping in san bernardino',
 'localterms':['san bernardino','interstate 10','interstate 215','interstate 15','210','highway 18','highway 330','cajon pass','devore','victorville','waterman','tippecanoe','orange show road','university parkway','hospitality lane','mount vernon','highland avenue','barton road','downtown','westside','muscoy','north end','verdemont','highland','redlands','loma linda','colton','rialto','fontana','grand terrace','yucaipa','crestline','lake arrowhead','running springs','big bear','mountain','chain controls','warehouses','cargo hub','airport','rail yard','medical center','residents','county hospital','university','march','fort irwin','orders','santa ana winds','wind advisory','fire','smoke','evacuation','snow','plows','flash floods','smog','los angeles','irvine','orange county','san diego','las vegas','phoenix','bakersfield','san jose','salt lake','denver','dallas','texas','arizona'],
}, BODY, FAQ)
