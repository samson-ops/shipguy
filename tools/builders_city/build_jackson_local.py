import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Jackson, Mississippi','Car shipping in the capital where 55 and 20 cross, from Fondren to the Reservoir and the plant up the road',
 ['Car shipping in Jackson works on the two interstates that cross south of downtown. Ship Guy is a licensed auto transport broker with an office on Bounds Street in Northeast Jackson.',
  'We book vetted carriers across the metro, from Belhaven and Fondren to Madison, Flowood, Brandon, and Clinton. The trucks belong to the carriers. Ship Guy holds the license and the bond.',
  'Interstate 55 carries the Memphis-to-New Orleans lane through the city and up to Ridgeland and Madison. Interstate 20 carries the Atlanta-to-Dallas lane across the south side. Interstate 220 loops the west side, and Lakeland Drive runs east to the Reservoir.',
  'This page covers 55, 20, 220, the Stack, Lakeland Drive, County Line Road, and Belhaven to Byram. It also covers the state workforce, the medical center, the plant, the campuses, the tornadoes, and the lanes.'],
 'Jackson at a glance',
 ['Most pickups happen within 1 to 3 days. The plant in Canton keeps car haulers based in the metro. The 55 and 20 traffic never stops.',
  'New Orleans, Memphis, Mobile, and Birmingham are same-day runs. Little Rock, Atlanta, Dallas, Nashville, and Houston need a day. Florida needs two.'],
 'Tell us the side of town and whether the street has oaks. Belhaven, Fondren, and the old grids meet the truck on a main road. Madison, Ridgeland, Flowood, Brandon, Clinton, and Byram usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 55, Interstate 20, Interstate 220, the Stack, US 49, Lakeland Drive, County Line Road, and the Trace',
 prose(
  L('Jackson is the crossroads of the state. A carrier reaches every suburb from the interstates without crossing a pothole downtown.'),
  P('Interstate 55 runs north and south through the city. It runs from Byram past downtown and the medical center to Ridgeland and Madison. Interstate 20 runs east and west along the south side, from Clinton to Pearl and Brandon. The two cross at the Stack south of downtown, and the Stack backs up both rush hours. Interstate 220 loops the west side from 20 to 55 at the north end.'),
  P('US 49 runs southeast to Hattiesburg and the coast and northwest to Yazoo City and the Delta. Lakeland Drive is Highway 25, from the medical center east through Flowood to the Reservoir. County Line Road is the retail line between Jackson and Ridgeland. The Natchez Trace runs along the west and north edges, and it bans commercial trucks. A carrier never uses it.'),
  P('The carriers come off 55 at County Line Road and off 20 at the outlet mall in Pearl. The mall lots on County Line Road are the usual meeting spot. The lifestyle center at Old Agency Road in Ridgeland and the outlet lots in Pearl work too. The fairgrounds lots on High Street work outside the fair and the rodeo.'),
  P('Our office is on Bounds Street in Northeast Jackson, off Northside Drive just east of 55.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, Belhaven, Fondren, Eastover, Northeast Jackson, West Jackson, South Jackson, Byram, Ridgeland, Madison, Flowood, Brandon, and Clinton',
 prose(
  L('Jackson is old neighborhoods under oaks and a ring of suburbs that grew faster than the city. The truck reaches the ring and meets the oaks on a main road.'),
  P('Downtown is the Capitol, the state office blocks, the museums, and the hospitals. The streets are wide, but the loading zones are not. The driver meets you at the fairgrounds lots or the convention center garages. Belhaven east of downtown is the historic district, narrow streets under low oaks around the college. The handoff moves to Fortification Street or Riverside Drive.'),
  P('Fondren is the restaurant strip on State Street and the bungalow blocks behind it. The driver meets you on State Street or at the lots by the medical center. Eastover and Woodland Hills are big houses on curving streets under the trees. A trailer stays off them. The handoff happens on Meadowbrook Road or at the Highland Village lots. Northeast Jackson from Meadowbrook to County Line Road is wider, and the curb often works.'),
  P('West Jackson around the university and the old grids west of downtown is narrow blocks and low branches. The handoff moves to the campus lots or Highway 80. South Jackson along Terry Road and McDowell Road is postwar grids. The curb works on most of them. Byram at the south end is new subdivisions, and the driver reaches the house.'),
  P('Ridgeland and Madison up 55 are the fastest-growing suburbs, with gated subdivisions and wide streets. Madison enforces its own rules for trucks, so give us the subdivision and the gate code. Flowood and Brandon east on Lakeland and 20 are the same, with the airport between them. Clinton west on 20 is the college town, and Pearl and Richland are flat and easy. All of them price the same as Jackson, and so does Canton.'),
 )))

ROUTES=[("New Orleans, LA","I-55/I-10 · ~185 mi","Same day","$220–$340"),("Memphis, TN","I-55 · ~210 mi","Same day","$230–$350"),
 ("Mobile, AL","US-49/I-10 · ~200 mi","Same day","$230–$350"),("Birmingham, AL","I-20 · ~240 mi","Same day","$250–$380"),
 ("Little Rock, AR","US-65/I-530 · ~270 mi","1 day","$260–$390"),("Atlanta, GA","I-20 · ~380 mi","1 day","$340–$490"),
 ("Dallas, TX","I-20 · ~400 mi","1 day","$360–$520"),("Nashville, TN","I-55/I-40 · ~420 mi","1 day","$370–$540"),
 ("Houston, TX","I-20/I-49/I-10 · ~440 mi","1 day","$400–$570"),("Orlando, FL","I-10/I-75 · ~700 mi","2 days","$500–$730")]
BODY.append(rate_table('Lanes &amp; Costs','Jackson Car Shipping Lanes and Estimated Costs',
 'The lanes metro Jackson cars run most, with estimated open-trailer ranges. Price your own route on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Jackson for an operable sedan on an open trailer. Figure 10 to 25 percent more for an SUV or a pickup, and more again for enclosed. The season and the trucks free on your dates decide the real number.',
 prose(
  P('Jackson prices among the best in the Deep South. Four interstates cross here, and the plant keeps haulers based nearby. New Orleans and Memphis are three hours away on 55 and cost the least. The Dallas and Atlanta lanes ride 20 in opposite directions. The Florida lane fills with retirees each fall and with students each August.'),
  P('An August move-in or a plant hiring wave falls in the busiest weeks. What size, condition, and season do to the price is in the <a href="car-shipping-cost.html">cost guide</a>.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The State Workforce, the Medical Center, the Assembly Plant, the Campuses, and the Airlift Wing',
 prose(
  L('Jackson relocates state employees, physicians, plant engineers, and students. The state and the medical center move the most.'),
  P('The state government is the largest employer in the city. Its agencies transfer staff on start dates all year. Each new governor brings a class of appointees in with the January inauguration. The medical center on the north side is one of the largest employers in the state. It brings residents each June and faculty on contract dates, and it hires traveling nurses year round. If your employer reimburses moves, the receipts come from us.'),
  P('The assembly plant in Canton twenty miles north moves engineers in on launch schedules. Its suppliers along 55 do the same. The tire plant in Clinton does it on production dates. The banks and the utility headquartered downtown relocate managers on offer dates. The second car usually rides a trailer.'),
  P('The campuses take cars each August and send them home each May. The state university in West Jackson and the college in Belhaven do it. So do the college on North State Street and the one in Clinton. Parents book it, and whoever meets the truck signs, as long as they are an adult. Campus streets are tight, so the meeting point is a lot on Highway 80 or State Street.'),
  P('The airlift wing at the airport flies cargo jets and rotates crews on orders. The handoff for the base happens outside the gate. Ship Guy is a private broker with no connection to the wing. The <a href="military-car-shipping.html">military</a> page covers moves on orders. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate rules.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The State Fair, the Rodeo, the Parade, the Classic, the Tornadoes, the Ice, and the Pearl',
 prose(
  L('Jackson runs on a fairgrounds calendar and a football calendar. The weather comes in sideways in the spring.'),
  P('The State Fair fills the fairgrounds on High Street for twelve days in October. The downtown streets around it close. The rodeo and the livestock show fill the same grounds for three weeks in February. The parade in March fills State Street downtown, and the street closes for the day. A handoff near any of them moves to the next morning.'),
  P('The classic in the fall and the homecoming games fill the stadium on North State Street. The streets around it fill too. The ballpark in Pearl fills its lots on summer game nights. Move-in week in late August clogs the blocks around every campus. The flea market in Canton fills the square twice a year, in May and October.'),
  P('Spring brings tornadoes. Warnings close the roads for an hour at a time from March through May. A carrier parks until the cell passes. Winter brings an ice storm every few years. The February 2021 storm iced the city for a week and shut the interstates. Trucks sat stranded on 55. The carriers wait in Memphis or New Orleans until the roads thaw. A winter pickup can lose a day or two.'),
  P('The Pearl River runs along the east side, and it floods the low neighborhoods in a wet year. The Easter flood of 1979 put thousands of homes under water. The August 2022 flood reached the same streets in Northeast Jackson. A pickup on the flat moves to higher ground until the water drops. Summer heat and afternoon storms shift the loading hour and nothing else.'),
 )+chips(["Downtown","Capitol","Belhaven","Fondren","State Street","Eastover","Woodland Hills","Meadowbrook","Highland Village","Northeast Jackson","Northside Drive","LeFleur's Bluff","Lakeland Drive","Midtown","Farish Street","West Jackson","South Jackson","Terry Road","Byram","Ridgeland","County Line Road","Old Agency","Madison","Gluckstadt","Flowood","Pearl","Brandon","Reservoir","Clinton","Richland","Canton","Yazoo City","Vicksburg","Hattiesburg"])
 +NOTE('Serving Jackson and all of Hinds, Rankin, and Madison Counties, Belhaven oak street or Madison gate. Tell us the side of town and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Jackson?',
 prose(
  L('Open trailers carry most Jackson cars, and the lane table above assumes one.'),
  P('An enclosed trailer keeps off the pollen, the spring hail, and the grit of 20. The collectors in Eastover and Madison book one. So do executives relocating a new car to the plant. A car bound for a long storage often rides enclosed too.'),
  P('A commuter car or a student car needs no roof. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages compare the two.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a lot on County Line Road or in Pearl, and a signature at delivery. The start date or move-in day picks the week.'),
  P('Say yes to the number, and a carrier already crossing at the Stack is booked. The lot and the window are nailed down before the day is out. At pickup the driver logs the car’s condition on the Bill of Lading, and you initial it. At delivery the car is checked against the same log.'),
 )+ULI([
  "Take everything out of the cabin and the trunk",
  "Fuel around a quarter full",
  "Your own photos of the car and the mileage that morning",
  "A key that works, and a word about anything that leaks or sticks",
  "Add-on alarm shut off",
  "In Belhaven, Fondren, or West Jackson, plan on a main road, not the curb",
 ])+prose(P('Every step is on the <a href="how-it-works.html">how it works</a> page. The <a href="car-shipping-preparation.html">preparation</a> page lists what to do before pickup.'))))

BODY.append(sec('Why Ship Guy','Why Jackson Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already cross at the Stack every day. We know which oak streets a trailer cannot enter.'),
  P('The federal register lists our FMCSA license and our $75,000 bond for anyone to check. The office is on Bounds Street in Northeast Jackson.'),
  P('Whoever quotes your move stays on it until the car is delivered. The <a href="services.html">services</a> page compares open, enclosed, and expedited service.'),
 )))

BODY.append(office('Jackson','135 Bounds St #132','Jackson, MS 39206','+16016888963','(601) 688-8963','CT',
 '135+Bounds+St+%23132,+Jackson,+MS+39206','Visit Us','Find Ship Guy in Jackson',
 'Our office is on Bounds Street in Northeast Jackson, off Northside Drive just east of 55.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4159.640780966632!2d-90.1513901!3d32.3699563!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8629cd1b1985db3f%3A0x83b5b3ea344577eb!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793288271515!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Jackson to Dallas or Atlanta?","Dallas runs three hundred sixty to five hundred twenty dollars for a sedan. That is about four hundred miles west on 20. Atlanta runs three hundred forty to four hundred ninety, about three hundred eighty miles east. New Orleans and Memphis are three hours away and cost the least. Larger vehicles add 10 to 25 percent."),
 ("Can the carrier come to my street in Belhaven or Fondren?","Usually not. Belhaven and the Fondren blocks are narrow streets under low oaks. A seventy-five-foot trailer stays on the main roads. The driver meets you on State Street, Fortification Street, or at the lots by the medical center. Madison, Ridgeland, Flowood, Brandon, Clinton, and Byram usually allow the curb."),
 ("Why are Jackson pickups quick to schedule?","Because four interstates cross here and the plant in Canton keeps car haulers based in the metro. The Memphis-to-New Orleans and Atlanta-to-Dallas lanes both pass through. A carrier with space is rarely more than a day away."),
 ("Do you ship cars for state employees and the medical center?","Yes, every week. The agencies transfer staff on start dates all year. Each new governor brings a class of appointees in January. The medical center brings residents each June and faculty on contract dates. The second car usually rides a trailer. If your employer reimburses moves, the receipts come from us."),
 ("Can you deliver on a Jackson State, Millsaps, or Belhaven move-in date?","Yes. Cars reach the campuses each August and leave again in May. Parents book it, and whoever meets the truck signs, as long as they are an adult. Campus streets are jammed that week. The truck meets you at a lot on Highway 80 or State Street. The date sets the window."),
 ("Can you ship a car to or from Madison, Flowood, or Clinton?","Yes, and all three price the same as Jackson. Madison rides the same carriers up 55, and its gated subdivisions need the name and the code. Flowood rides them out Lakeland Drive, and Clinton rides them west on 20. Send the full address for a county road."),
 ("What happens if a tornado warning hits on my pickup day?","The driver parks until the cell passes, usually an hour. Warnings close the roads from March through May. The window moves to later the same day or the next morning. You hear it from us before the driver does."),
 ("Does the State Fair affect my pickup?","Yes, if the address is downtown or near the fairgrounds. The fair fills High Street for twelve days in October. The rodeo fills it for three weeks in February. A handoff near the grounds moves to the morning or to the suburbs. The rest of the metro barely notices."),
 ("Can you ship a car that does not run from Jackson?","Yes. We book a truck with a winch and price the loading time up front. The mall lots on County Line Road or the outlet lots in Pearl give the driver level ground. Does it roll, steer, and brake? Tell us which."),
 ("What do you need for a Jackson car shipping quote?","Pickup and delivery addresses, with the side of town. The year, make, and model. Whether it drives. Open or enclosed. The week you want. With those five we price the Jackson lane the same day."),
]
BODY.append(faq_section(FAQ,'Jackson FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Jackson?','Price the lane on the form above in two minutes. Tell us the side of town and the week, and a carrier crossing at the Stack handles it.','+16016888963','(601) 688-8963','Get your free Jackson quote'))

build({
 'slug':'auto-transport-jackson-mississippi',
 'title':'Car Shipping in Jackson, MS — Auto Transport | Ship Guy',
 'meta':'Car shipping in Jackson, MS, the capital where 55 and 20 cross, from Belhaven and Fondren to Madison, Flowood, and Clinton. State and medical center relocations, the Canton plant, college move-in timing, main-road handoffs for the oak streets, curbside pickups in the suburbs, the State Fair, the tornadoes, and the Pearl. Local office on Bounds Street in Northeast Jackson. Free quote.',
 'h1':'Car Shipping in<br>Jackson, <span class="accent">Mississippi</span>',
 'lede':'Open, enclosed, and expedited auto transport across metro Jackson, planned around the Stack, the oak streets, the suburbs up 55, the campus calendar, and the spring storms.',
 'tel':'+16016888963','disp':'(601) 688-8963','brand':'Jackson','keyword':'car shipping in jackson',
 'localterms':['jackson','capital','55','20','fondren','reservoir','plant','bounds street','northeast jackson','belhaven','madison','flowood','brandon','clinton','memphis','new orleans','ridgeland','atlanta','dallas','interstate 220','lakeland drive','the stack','county line road','byram','state workforce','medical center','assembly plant','campuses','fair','tornadoes','canton','mobile','birmingham','little rock','nashville','houston','florida','oaks','pothole','pearl','us 49','hattiesburg','coast','yazoo city','delta','highway 25','natchez trace','commercial trucks','outlet mall','old agency road','fairgrounds','high street','rodeo','northside drive','museums','hospitals','convention center','fortification street','riverside drive','state street','bungalow','eastover','woodland hills','meadowbrook road','highland village','university','highway 80','terry road','mcdowell road','subdivisions','gate code','airport','richland','residents','faculty','traveling nurses','suppliers','tire plant','banks','utility','state university','north state street','airlift wing','cargo jets','move-in','appointee','classic','homecoming','stadium','ballpark','flea market','square','warnings','ice storm','february 2021','stranded','pearl river','easter flood','1979','august 2022','pollen','hail','storage','bill of lading','fmcsa','lefleur','midtown','farish street','gluckstadt','vicksburg','deep south'],
}, BODY, FAQ)
