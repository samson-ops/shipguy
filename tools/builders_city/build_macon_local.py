import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Macon, Georgia','Car shipping where Interstate 75 meets Interstate 16, in the middle of the state',
 ['Car shipping in Macon starts at the interchange, where Interstate 16 leaves Interstate 75 for the coast. Ship Guy is a licensed auto transport broker with an office on Riverside Drive in north Macon.',
  'We book vetted carriers across middle Georgia, from Forsyth to Warner Robins and out to Milledgeville. We do not own the trucks.',
  'Interstate 75 runs north and south through the city on the way from Atlanta to Florida. Interstate 16 begins downtown and runs to Savannah. Interstate 475 bypasses the west side for the through trucks. Riverside Drive, Pio Nono Avenue, and Eisenhower Parkway carry the rest.',
  'This page covers the two interstates, the bypass, downtown, the historic hills, north Macon, and the air base. It also covers the insurer, the hospitals, the colleges, the cherry blossoms, the storms, and the lanes.'],
 'Macon at a glance',
 ['Most pickups happen within 1 to 3 days. Interstate 75 carries the Midwest-to-Florida carriers through the city all day.',
  'Atlanta, Columbus, and Savannah are same-day lanes. Augusta and Athens are the same day too. Jacksonville, Tallahassee, and Birmingham take a day. Orlando, Nashville, and Charlotte take one as well.'],
 'Tell us the neighborhood. Vineville, Ingleside, and the downtown blocks need a meeting spot. North Macon, Bloomfield, and Warner Robins usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 75, 16, 475, Riverside Drive, and the Interchange',
 prose(
  L('Macon is the fork where the Florida lane and the Savannah lane split. The carriers stage at the fork.'),
  P('Interstate 75 runs the length of the city from Bolingbroke to Byron. The interchange with Interstate 16 downtown has been under reconstruction for years. The lane shifts change by the month. The ramps at Riverside Drive, Pierce Avenue, and Hardeman Avenue are the way into the city.'),
  P('Interstate 16 begins at the interchange and runs east along the river to Savannah. Interstate 475 leaves 75 at Bolingbroke, swings around the west side, and rejoins at Byron. Most through trucks take it, so the city stretch stays lighter. The truck stops at the Bass Road and Byron exits are the staging spots.'),
  P('Riverside Drive is US 23, the strip from downtown up to the north Macon shopping. Pio Nono Avenue is US 41 through the south side. Eisenhower Parkway is US 80, the east-west strip past the old mall. Gray Highway runs northeast. The Fall Line Freeway leaves for Columbus and Augusta, and Houston Road runs to Warner Robins.'),
  P('The carriers come off 75 at Riverside Drive, Bass Road, and Eisenhower Parkway. The lots along Riverside, at Bass Road, and at the Byron truck stops are the meeting spots. No road in middle Georgia charges a toll.'),
  P('Our office sits on Riverside Drive in north Macon, a few blocks from the Pierce Avenue ramps.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, Vineville, Ingleside, North Macon, and Warner Robins',
 prose(
  L('Macon is a city of hills and wide avenues, laid out when the river ran the state.'),
  P('Downtown has Cherry Street and Poplar Street, wide enough that a trailer can stop on either. The college on the hill above downtown has narrow campus streets. The handoff happens at a campus lot. The historic blocks around Tattnall Square and College Hill are tight. The driver meets you on Poplar or at the lots by the river.'),
  P('Vineville, Ingleside, and Shirley Hills have old houses on winding streets under big trees. The driver meets you on Vineville Avenue, on Ingleside Avenue, or at a lot on Riverside. Pleasant Hill and the blocks off Forsyth Road are narrow grids with the same answer.'),
  P('North Macon along Bass Road, Zebulon Road, and Rivoli is newer subdivisions and shopping centers. The streets are wide, and the truck usually reaches the curb. Lake Tobesofkee and Lizella sit west of 475 with long drives and open roads. Gray and Bolingbroke are the same.'),
  P('South Macon and Bloomfield are flat postwar grids along Pio Nono where the curb works. East Macon across the river has open blocks and the mounds. Warner Robins, Centerville, and Perry are suburban grids built for the base. The curb works on most streets. Byron sits at the 75 exit with lots everywhere.'),
 )))

ROUTES=[("Atlanta, GA","I-75 · ~85 mi","Same day","$150–$240"),("Columbus, GA","US-80/SR-540 · ~95 mi","Same day","$150–$240"),
 ("Savannah, GA","I-16 · ~165 mi","Same day","$190–$300"),("Augusta, GA","SR-540/US-1 · ~125 mi","Same day","$170–$270"),
 ("Birmingham, AL","US-80/US-280 · ~240 mi","1 day","$230–$350"),("Jacksonville, FL","I-75/I-10 · ~260 mi","1 day","$250–$370"),
 ("Nashville, TN","I-75/I-24 · ~330 mi","1 day","$300–$440"),("Charlotte, NC","I-75/I-85 · ~330 mi","1 day","$300–$440"),
 ("Orlando, FL","I-75/Turnpike · ~400 mi","1 day","$360–$520"),("Dallas, TX","I-20 · ~800 mi","2 days","$560–$820")]
BODY.append(rate_table('Lanes &amp; Costs','Macon Car Shipping Lanes and Estimated Costs',
 'The lanes that leave middle Georgia most, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a running sedan on an open trailer, priced from Macon. An SUV or pickup adds roughly 10 to 25 percent, and enclosed adds more. The snowbird seasons, the storms, and the carriers free on your dates set the final figure.',
 prose(
  P('Macon prices like Atlanta on the Florida lanes, because the same 75 carriers pass both. The snowbird trucks fill the road south every fall and north every spring. A Macon car on that lane rides a trailer that was already making the trip.'),
  P('The base keeps the Texas, Oklahoma, and Utah lanes busy with depot moves. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','Robins Air Force Base, the Insurer, the Hospitals, and the Colleges',
 prose(
  L('Macon relocates airmen, depot engineers, claims staff, and students, and the base is the biggest employer for miles.'),
  P('Robins Air Force Base in Warner Robins is one of the largest employers in the state. Airmen rotate in on orders, and the depot hires civilian engineers and mechanics all year. The orders pay for one car, and the family’s second car rides with us. The gates stop the truck, so the meeting spot is a lot on Watson Boulevard or Russell Parkway.'),
  P('Ship Guy is a private broker and is not part of the base. Report-date timing is covered on the <a href="military-car-shipping.html">military</a> page.'),
  P('The insurer with a regional office on Riverside Drive brings in claims and service staff from every state. The tire plant, the tissue mill, and the warehouses along 75 relocate engineers and managers on program schedules. We supply the paperwork a reimbursed move needs.'),
  P('The trauma center downtown and the hospital on the north side bring in residents each June. Nurses arrive all year. The university on the hill brings in students each August, including the medical and law schools. The women’s college in north Macon and the state college do the same. An adult signs for a student car at a campus lot.'),
  P('Families move down from Atlanta for the prices and up from Florida for the jobs. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side of a move.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Cherry Blossoms, the Fair, Storms, and the River',
 prose(
  L('Macon has a pink week in March and a storm season that runs from spring to fall. The carriers plan around both.'),
  P('The cherry blossom festival fills the city for ten days in late March. The parades close downtown and Third Street, and the historic neighborhoods crawl with visitors. A pickup in those blocks moves to another day or to Riverside Drive.'),
  P('March through May is tornado and hail season in middle Georgia. A warning keeps the driver parked until it lifts. Afternoon storms in July and August push loading to the early hours. The river keeps the air thick all summer.'),
  P('Hurricane remnants cross middle Georgia most years. Helene in 2024 knocked down trees across the city and cut power for days. The carriers waited for the clearing crews, and pickups moved to the lots on 75. Ice reaches Macon a few times a decade, and the 2014 storm shut the hills for days.'),
  P('The river rose over the levees in 1994 and 1998. A wet spring still closes the lots by the river. A riverside pickup moves up the hill to Riverside Drive. The state fair in Perry fills 75 south for eleven days in October. Game nights at the ballpark fill the lots by the interchange.'),
 )+chips(["Downtown","Cherry Street","College Hill","Tattnall Square","Beall’s Hill","Vineville","Ingleside","Shirley Hills","Pleasant Hill","Bellevue","North Macon","Riverside","Bass Road","Zebulon Road","Rivoli","Wesleyan Woods","Lake Tobesofkee","Lizella","Bolingbroke","Gray","South Macon","Bloomfield","East Macon","Byron","Warner Robins","Centerville","Perry","Fort Valley","Forsyth","Milledgeville"])
 +NOTE('Serving Macon and all of middle Georgia, from Forsyth to Perry. Tell us the neighborhood, the gate, and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Macon?',
 prose(
  L('Open is how middle Georgia ships, and the 75 lanes are priced for it.'),
  P('An enclosed trailer keeps the pollen, the hail, and attention off a car. The garages in Shirley Hills and north Macon book them for collector cars. So does an airman with a restored car headed to a new post.'),
  P('A commuter car or a work truck rides open without trouble. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages set the two side by side.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff on Riverside Drive or at the Byron truck stops, and a delivery. The 75 traffic sets the pace.'),
  P('Say yes to the price, and a carrier already rolling on 75 gets the booking. The same day, we set the meeting spot and the window. You and the driver go over the car together, and a Bill of Lading records its condition. Two signatures, and the sheet travels with the car to the delivery check.'),
 )+ULI([
  "Take your personal items out of the car",
  "Leave about a quarter tank of fuel",
  "Photograph the car before pickup, pollen and all",
  "Give the driver a working key and name any mechanical issue",
  "Switch off any aftermarket alarm",
  "Near the base, plan to meet the truck outside the gate on Watson Boulevard",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages take it from there.'))))

BODY.append(sec('Why Ship Guy','Why Macon Drivers Choose Ship Guy',
 prose(
  L('We use the 75 traffic that already passes the interchange. We plan around the gates, the blossoms, and the storms.'),
  P('Ship Guy is licensed as a broker by the FMCSA and bonded for $75,000. Look up either one in the federal register. Our office is on Riverside Drive in north Macon.'),
  P('You deal with one coordinator the whole way, quote to delivery. The <a href="services.html">services</a> page explains open, enclosed, and expedited transport.'),
 ), alt=True))

BODY.append(office('Macon','2960 Riverside Dr Ste 458','Macon, GA 31204','+14783313289','(478) 331-3289','ET',
 '2960+Riverside+Dr+Ste+458,+Macon,+GA+31204','Visit Us','Find Ship Guy in Macon',
 'Our office is on Riverside Drive in north Macon, a few blocks from the Pierce Avenue ramps.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5152.289985856693!2d-83.67285350000002!3d32.8845384!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x88f3ff4844a2fd25%3A0xa427319abcbeaa06!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792162230270!5m2!1sen!2sus'))

FAQ=[
 ("Why is car shipping from Macon so easy to book?","Because the Florida lane and the Savannah lane split here. Every carrier between the Midwest and Florida passes the interchange on 75. A Macon car fills a space on a trailer that was already making the trip. Atlanta and Columbus run one hundred fifty to two hundred forty dollars for a sedan."),
 ("Do you handle a PCS move to Robins Air Force Base?","Yes, on every rotation. Orders cover one car, and the second one comes with us. The gates stop the truck, so we meet you at a lot on Watson Boulevard or Russell Parkway. Your report date sets the pickup. Ship Guy is a private broker and is not part of the base."),
 ("How much does it cost to ship a car from Macon to Florida or Atlanta?","Orlando runs three hundred sixty to five hundred twenty dollars for a sedan. That is about four hundred miles down 75 and the Turnpike. Atlanta runs one hundred fifty to two hundred forty, about eighty-five miles up 75. Fall snowbird demand lifts the Florida price from October through December. SUVs and pickups add 10 to 25 percent."),
 ("Does the cherry blossom festival affect my pickup?","If you live downtown or in the historic neighborhoods, yes. The parades close downtown and Third Street for ten days in late March. The old streets crawl with visitors. We move a pickup in those blocks to another day or to Riverside Drive. North Macon runs normally."),
 ("Can the carrier come to my street in Vineville or Ingleside?","Usually not. Those streets wind under big trees, and a seventy-five-foot rig cannot turn there. The driver meets you on Vineville Avenue, on Ingleside Avenue, or at a lot on Riverside. North Macon, Bloomfield, and Warner Robins usually allow the curb."),
 ("Does the interchange construction affect my pickup?","Not much. The lane shifts at 75 and 16 slow the carriers for a few minutes. The driver knows the week’s pattern. We set the meeting spot away from the work zone, usually on Riverside Drive or at Bass Road. The through trucks take 475 around it."),
 ("Can you ship a car for a Mercer or Wesleyan student?","Yes. Cars arrive each August and leave each May, and both windows book up early. The campus lots on College Hill and off Forsyth Road work for the handoff. A parent or another adult signs at pickup."),
 ("What happens if a storm hits on my pickup day?","A tornado warning holds the driver until the all-clear. Hurricane remnants like Helene bring down trees and cut power, and the carriers wait for the clearing crews. An ice glaze shuts the hills for a day or two. We call before the window moves."),
 ("Can you ship a car that does not run from Macon?","Yes. A winch truck takes the job, and the longer loading is already in the price. The lots on Riverside Drive or at the Byron truck stops give the driver a flat, open spot. Say whether the car rolls, steers, and brakes when you book."),
 ("What do you need for a Macon car shipping quote?","The two addresses, with the neighborhood or the gate on the Macon end. Year, make, and model of the car. Whether it starts and rolls. Open or enclosed, plus a date range. That is enough for an exact Macon quote."),
]
BODY.append(faq_section(FAQ,'Macon FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Macon?','A price takes about two minutes on the form above. Tell us the neighborhood and your dates, and a carrier already on 75 takes it from there.','+14783313289','(478) 331-3289','Get your free Macon quote'))

build({
 'slug':'auto-transport-macon-georgia',
 'title':'Car Shipping in Macon, GA — Auto Transport | Ship Guy',
 'meta':'Car shipping in Macon, GA where Interstate 75 meets 16 in the middle of the state. Robins Air Force Base second cars and gate handoffs, Vineville and downtown meeting spots, north Macon curbside, insurer and hospital relocations, cherry blossom and storm planning, snowbird lanes. Local office on Riverside Drive. Free quote.',
 'h1':'Car Shipping in<br>Macon, <span class="accent">Georgia</span>',
 'lede':'Open, enclosed, and expedited auto transport across middle Georgia, planned around 75, 16, the base gates, and the storms.',
 'tel':'+14783313289','disp':'(478) 331-3289','brand':'Macon','keyword':'car shipping in macon',
 'localterms':['macon','interstate 75','interstate 16','interstate 475','interchange','riverside drive','us 23','pierce avenue','hardeman avenue','bass road','pio nono','us 41','eisenhower parkway','us 80','gray highway','fall line freeway','houston road','byron','bolingbroke','truck stops','downtown','cherry street','poplar street','third street','college hill','tattnall square','vineville','ingleside','shirley hills','pleasant hill','forsyth road','north macon','zebulon road','rivoli','lake tobesofkee','lizella','gray','south macon','bloomfield','east macon','mounds','warner robins','centerville','perry','watson boulevard','russell parkway','robins air force base','depot','orders','report date','insurer','tire plant','tissue mill','warehouses','trauma center','hospital','residents','nurses','university','medical','law','women’s college','state college','cherry blossom','festival','parades','tornado','hail','storms','helene','2024','ice','2014','river','levees','1994','state fair','ballpark','atlanta','columbus','savannah','augusta','athens','jacksonville','tallahassee','birmingham','orlando','nashville','charlotte','dallas','florida','texas','oklahoma','utah'],
}, BODY, FAQ)
