import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Springfield, Illinois','Car shipping in the state capital, on Interstate 55 halfway between Chicago and St. Louis',
 ['Car shipping in Springfield runs off Interstate 55 on the east side and Interstate 72 across the north. Ship Guy is a licensed auto transport broker with an office in the Horace Mann tower downtown.',
  'We book vetted carriers across Sangamon County, from Chatham to Sherman and out to Lake Springfield. The trucks belong to the carriers we vet.',
  'Interstate 55 is the Chicago and St. Louis road, with exits at Clear Lake, Stevenson, and Toronto Road. Interstate 72 crosses to Champaign and Jacksonville. Veterans Parkway and Dirksen Parkway loop the west and east sides. Old Route 66 runs through on 6th and 9th Streets.',
  'This page covers the interstates, the parkways, downtown, the historic districts, the west side, and the lake. It also covers the state, the hospitals, the State Fair, the Route 66 car show, and the lanes.'],
 'Springfield at a glance',
 ['Most pickups happen within 1 to 3 days. Every carrier between Chicago and St. Louis passes the city on 55.',
  'St. Louis is ninety minutes, and Champaign is the same. Chicago and Indianapolis are a same-day haul. Kansas City, Memphis, and Nashville take a day. Dallas and Denver take two or three, and the coasts take three to five.'],
 'Tell us the side of the parkway. Downtown, the Lincoln blocks, and the historic districts need a meeting spot. The west side, the southeast, and Chatham usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 55, Interstate 72, Veterans Parkway, Dirksen Parkway, and Old Route 66',
 prose(
  L('Springfield sits on the busiest car-hauler lane in the state. The trucks pass the east side every hour.'),
  P('Interstate 55 runs north and south along the east side of the city. The exits at Sangamon Avenue, Clear Lake, Stevenson Drive, and Toronto Road cover eight miles. Every carrier between Chicago and St. Louis passes all four. Interstate 72 crosses the north side. It runs east to Decatur and Champaign and west to Jacksonville and Hannibal.'),
  P('Veterans Parkway is the loop on the west and south sides. It runs from 72 past the mall to 55 at Toronto Road. Dirksen Parkway is the east-side loop past the airport and the fairgrounds. Together they carry the trucks around downtown. Sangamon Avenue runs past the fairgrounds. Clear Lake Avenue and Stevenson Drive cross from 55 to the parkways.'),
  P('Old Route 66 is 6th Street southbound and 9th Street northbound through downtown. North of downtown it is Peoria Road. MacArthur Boulevard, Wabash Avenue, and Chatham Road carry the west side. Toronto Road and the lake roads reach the south. 2nd Street and Capitol Avenue cross the Capitol complex, and the Lincoln Home blocks are closed to cars.'),
  P('The carriers come off 55 at Clear Lake and Stevenson, and off 72 at Veterans. The mall lot on Wabash, the fairgrounds, and the lots by the 55 exits are the meeting spots. No road in Sangamon County charges a toll.'),
  P('Our office is in the Horace Mann tower downtown, a few blocks from the Capitol.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown and the Lincoln Blocks, the Historic Districts, the West Side, the Southeast, the Lake, and Chatham',
 prose(
  L('Springfield is a capital city of government blocks, old neighborhoods, and a west side that keeps growing.'),
  P('Downtown is the Capitol complex, the Old State Capitol square, and the office towers between them. The one-way streets fill with state workers on weekdays. A trailer cannot stop on 6th or Adams. The driver meets you at the lots by the presidential museum or by the arena. The Lincoln Home blocks are closed to traffic, and the handoff moves to 7th Street.'),
  P('Enos Park north of downtown and Aristocracy Hill to the south are historic districts. Big houses sit on narrow streets. The driver meets you on 5th Street or at the hospital lots. Vinegar Hill and the old grids off MacArthur are the same. The Washington Park blocks to the west have wide boulevards, and the curb works there.'),
  P('The west side along Wabash, Veterans, and Chatham Road is the retail and medical side. Its subdivisions date from the last fifty years. Panther Creek, Piper Glen, and the streets off Iles Avenue have wide roads. The truck reaches the curb. Leland Grove and Jerome are their own small cities inside the west side. They have big lots and old trees.'),
  P('The southeast along Toronto Road is the newest growth, around the university campus. The streets are wide. Lake Springfield to the south is a ring of lake homes on narrow drives. The driver meets you on the lake road. Chatham, Rochester, and Sherman are the suburbs, with lots on every main road. All of them price the same as Springfield, and so does the east side along Dirksen.'),
 )))

ROUTES=[("St. Louis, MO","I-55 · ~100 mi","Same day","$150–$250"),("Champaign, IL","I-72 · ~90 mi","Same day","$150–$240"),
 ("Chicago, IL","I-55 · ~200 mi","Same day","$220–$330"),("Indianapolis, IN","I-72/I-74 · ~210 mi","Same day","$220–$330"),
 ("Kansas City, MO","I-72/US-36 · ~300 mi","1 day","$290–$420"),("Memphis, TN","I-55 · ~390 mi","1 day","$350–$500"),
 ("Nashville, TN","I-64/I-24 · ~430 mi","1 day","$380–$550"),("Dallas, TX","I-55/I-44 · ~730 mi","2 days","$540–$770"),
 ("Denver, CO","I-72/I-70 · ~900 mi","2–3 days","$630–$900"),("Orlando, FL","I-57/I-75 · ~1,050 mi","3 days","$720–$1,020")]
BODY.append(rate_table('Lanes &amp; Costs','Springfield Car Shipping Lanes and Estimated Costs',
 'The lanes Sangamon County cars take most, with estimated open-trailer ranges. Your exact route prices on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Springfield, Illinois, running sedan, open trailer. Count on 10 to 25 percent more for an SUV or a pickup and more again for enclosed. Fuel, the season, and the carriers free on your dates fix the final price.',
 prose(
  P('Springfield prices under Chicago on the St. Louis and southern lanes. The carriers are already on 55 and pick up a car in passing. The Chicago lane runs daily and prices the same as the suburbs. The Kansas City lane rides 72 and 36 and runs lighter, which can add a day.'),
  P('Florida and Texas follow the snowbird calendar, higher in the fall and lower in the spring. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The State, the Hospitals, the Insurer, the Campuses, and the Session',
 prose(
  L('Springfield relocates state employees, nurses, insurance staff, and students. The legislative calendar moves more people than any closing date.'),
  P('The state is the largest employer, and its agencies move staff in from every corner of Illinois. The session runs from January into May, and staffers, lobbyists, and press arrive in January with a car. The veto session brings a smaller wave in the fall. We supply the paperwork a reimbursed move needs.'),
  P('The two hospital systems run the campuses north of downtown and bring in nurses on contracts all year. The medical school adds residents each June and faculty each summer. The insurer downtown and the coffee-machine maker on the north side relocate staff on their own calendars.'),
  P('The university on the southeast side brings cars in each August, and the community college does the same. A parent ships the car, and an adult signs at a campus lot. Retirees and state pensioners leave for Florida and Arizona each fall and ship the car ahead of them.'),
  P('The National Guard headquarters and the air wing at the airport move soldiers and airmen on orders. The orders cover one car, and the second one comes with us. Ship Guy is a private broker with no connection to the Guard. The <a href="military-car-shipping.html">military</a> page covers the timing. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The State Fair, the Route 66 Car Show, the Session, the Ice, and the 2006 Tornadoes',
 prose(
  L('Springfield runs on an eleven-day fair in August, a car show in September, and a winter session downtown.'),
  P('The State Fair fills the fairgrounds on the north side for eleven days in August. Sangamon Avenue and Peoria Road gridlock from the morning gates to the evening concerts. A pickup on the north side that week moves to the west side or to 55. The county fair in New Berlin does the same thing on a smaller scale.'),
  P('The Route 66 festival fills downtown with thousands of classic cars on a weekend in September. The streets around the square close, and the cruise runs up and down 6th and 9th. A downtown pickup that weekend moves to the parkways. Many of the cars arrive on enclosed trailers, and we book them months ahead.'),
  P('The session fills the downtown garages and the hotel lots from January into May. The Capitol blocks run slow on session days, and a downtown handoff moves to the morning. The presidential museum and the Lincoln sites draw tour buses all summer. The lots by the museum fill by midday.'),
  P('Ice is the winter problem. The 2006 ice storm took the power out across the city for a week. The carriers parked on 55 for two days. Snow runs twenty inches a year, and the 2011 blizzard closed 55 for a day. Tornadoes crossed the west side in March 2006 and tore up the parkway. The 2009 derecho did the same in May. The sirens sound a few times each spring, and a pickup waits for the warning to lift.'),
 )+chips(["Downtown","Capitol Complex","Old State Capitol","Lincoln Home","Presidential Museum","Enos Park","Aristocracy Hill","Vinegar Hill","Washington Park","MacArthur","West Side","Wabash","Veterans Parkway","White Oaks","Panther Creek","Piper Glen","Iles Avenue","Leland Grove","Jerome","Southeast","Toronto Road","University","Lake Springfield","East Side","Dirksen","Clear Lake","North End","Fairgrounds","Peoria Road","Chatham","Rochester","Sherman","Riverton"])
 +NOTE('Serving Springfield, Chatham, and all of Sangamon County, historic district or new subdivision. Tell us the side of the parkway and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Springfield?',
 prose(
  L('Most cars leave Sangamon County on an open trailer, and the lane prices assume one.'),
  P('A closed trailer keeps a car away from the salt, the gravel, and the weather. The Route 66 crowd books enclosed for the show cars every September. Collectors on the lake and in Leland Grove book one for the rest of the year.'),
  P('A commuter car or a state fleet sedan goes open and arrives fine. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages set out the trade-off.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A number, a handoff at the mall or by a 55 exit, and a car at delivery. The session or the start date sets the week.'),
  P('Approve the number, and we book a carrier already running 55. The lot and the window reach you the same day. At pickup, the driver walks the car with you and marks its condition on a Bill of Lading. Both of you sign, and the delivery is checked against that sheet.'),
 )+ULI([
  "Empty the cabin and the trunk of anything personal",
  "Keep the fuel near a quarter tank",
  "Photograph each panel and the mileage before the handoff",
  "Give the driver one working key and mention any fault",
  "Disarm any aftermarket alarm",
  "Downtown or in Enos Park, meet the truck at the museum lots or on 5th Street",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Springfield Drivers Choose Ship Guy',
 prose(
  L('We catch the carriers already on 55 between Chicago and St. Louis. We plan around the fair, the car show, and the session.'),
  P('Ship Guy is an active FMCSA broker backed by a $75,000 surety bond. The federal register lists both. Our office is in the Horace Mann tower downtown.'),
  P('The coordinator who quotes the move stays with it until the delivery sheet is signed. Open, enclosed, and expedited transport are on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Springfield','1 Horace Mann Plaza Suite 573','Springfield, IL 62715','+12173956794','(217) 395-6794','CT',
 '1+Horace+Mann+Plaza+Suite+573,+Springfield,+IL+62715','Visit Us','Find Ship Guy in Springfield',
 'Our office is in the Horace Mann tower downtown, a few blocks from the Capitol.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4713.557648881339!2d-89.6449305!3d39.802295!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x887539937857987f%3A0x7f539d1efefe54e1!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793024762223!5m2!1sen!2sus'))

FAQ=[
 ("How much does it cost to ship a car from Springfield to St. Louis or Chicago?","St. Louis runs one hundred fifty to two hundred fifty dollars for a sedan. That is about one hundred miles down 55. Chicago runs two hundred twenty to three hundred thirty, about two hundred miles the other way. Champaign prices the same as St. Louis, and Indianapolis the same as Chicago. An SUV or pickup adds 10 to 25 percent. All four lanes run daily."),
 ("Can the carrier come to my street downtown or in Enos Park?","Usually not. Downtown is one-way streets around the Capitol, and the Lincoln Home blocks are closed to cars. Enos Park and Aristocracy Hill have narrow streets under old trees. The driver meets you at the museum lots, on 5th Street, or at the hospital lots. The west side, the southeast, and Chatham usually allow the curb."),
 ("Do you ship cars for state employees moving to Springfield?","Yes, every month and especially in January. The agencies move staff in from across Illinois. The session brings staffers and lobbyists with a car each winter. Many ship a second car behind the move. The handoff works at the museum lots or a lot off 55. We provide the paperwork a reimbursed move needs."),
 ("Does the State Fair affect my pickup?","On the north side, yes. The fairgrounds fill for eleven days in August. Sangamon Avenue and Peoria Road gridlock from morning to night. We move a north-side pickup that week to the west side or to a lot off 55. The rest of the county runs normally."),
 ("Can you ship a classic car to the Route 66 festival?","Yes, and we book those months ahead. The festival fills downtown with thousands of classic cars on a weekend in September. Most owners book an enclosed trailer, and we deliver to the shop or the hotel the week before. A car that does not drive on the street goes on a winch carrier. The cruise closes 6th and 9th, so the handoff sits outside downtown."),
 ("Can you ship a car to or from Chatham, Sherman, or the lake?","Yes, and all three price the same as Springfield. Chatham rides the same carriers off 55 at Toronto Road. Sherman rides them off 55 to the north. The lake homes sit on narrow drives, and the driver meets you on the lake road. Send the full address for a new subdivision in Chatham."),
 ("What happens if an ice storm or a tornado warning hits on my pickup day?","Ice stops the trucks before snow does. The carriers park on 55 until the salt trucks finish, and a winter pickup can slip a day. We call before it does. A tornado warning stops the loading until it lifts, and the sirens sound a few times each spring. The driver waits it out and finishes the same day in most cases."),
 ("Can you ship a car that does not run from Springfield?","Yes. The carrier comes with a winch, and the loading time is priced in from the first quote. The mall lot on Wabash or the fairgrounds lot gives the driver level pavement. Tell us whether the car rolls, steers, and brakes."),
 ("Can you time delivery to a student move at the university?","Yes. The campus on the southeast side takes cars in each August and sends them home in May. The community college runs the same calendar. A parent books, and an adult signs at a campus lot. The delivery window follows the move-in date and shifts with it."),
 ("What do you need for a Springfield car shipping quote?","The pickup and delivery addresses, with the side of the parkway or the suburb here. Year, make, and model. Whether it drives. Open or enclosed. The week you want it gone. With those, the Springfield number comes back the same day."),
]
BODY.append(faq_section(FAQ,'Springfield FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Springfield?','Two minutes on the form above prices your lane. Send the side of the parkway and your dates, and a carrier already on 55 takes it.','+12173956794','(217) 395-6794','Get your free Springfield quote'))

build({
 'slug':'auto-transport-springfield-illinois',
 'title':'Car Shipping in Springfield, IL — Auto Transport | Ship Guy',
 'meta':'Car shipping in Springfield, IL, the state capital on Interstate 55 between Chicago and St. Louis. State-employee and hospital relocations, downtown and Lincoln-block meeting spots, west side and Chatham curbside pickups, the State Fair, the Route 66 car show, the session, and the ice. Local office in the Horace Mann tower. Free quote.',
 'h1':'Car Shipping in<br>Springfield, <span class="accent">Illinois</span>',
 'lede':'Open, enclosed, and expedited auto transport across Sangamon County, planned around 55, 72, the parkways, the fair, and the session.',
 'tel':'+12173956794','disp':'(217) 395-6794','brand':'Springfield','keyword':'car shipping in springfield',
 'localterms':['springfield','state capital','interstate 55','interstate 72','veterans parkway','dirksen parkway','route 66','6th street','9th street','peoria road','sangamon avenue','clear lake','stevenson','toronto road','macarthur','wabash','chatham road','2nd street','capitol avenue','downtown','capitol','old state capitol','lincoln home','presidential museum','arena','7th street','enos park','aristocracy hill','vinegar hill','washington park','5th street','west side','mall','panther creek','piper glen','iles avenue','leland grove','jerome','southeast','university','lake springfield','lake road','chatham','rochester','sherman','east side','airport','fairgrounds','new berlin','state','agencies','session','staffers','lobbyists','veto session','hospital','nurses','medical school','residents','insurer','coffee-machine','community college','retirees','national guard','air wing','orders','state fair','route 66 festival','classic cars','cruise','tour buses','ice storm','2006','snow','2011 blizzard','tornadoes','march 2006','2009 derecho','sirens','st. louis','champaign','chicago','indianapolis','kansas city','memphis','nashville','dallas','denver','orlando','decatur','jacksonville','hannibal'],
}, BODY, FAQ)
