import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Athens, Georgia','Car shipping in a college town with no interstate, where the Loop and Highway 316 do the work',
 ['Car shipping in Athens starts on the Loop, the perimeter highway every truck uses to reach the city. Ship Guy is a licensed auto transport broker with an office on Daniells Bridge Road.',
  'We book vetted carriers across the Classic City and the counties around it, from Commerce to Watkinsville. We do not own the trucks.',
  'Highway 316 is the four-lane to Interstate 85 and Atlanta, and the Loop circles the city. US 441 runs north to Interstate 85 at Commerce and south to Milledgeville. US 78 and US 29 run to Atlanta and Augusta. Atlanta Highway and Epps Bridge Parkway are the retail strips.',
  'This page covers the Loop, the four-lane, downtown, Five Points, Normaltown, and the Oconee suburbs. It also covers the university calendar, game days, the hospital, the plants, the storms, and the lanes.'],
 'Athens at a glance',
 ['Most pickups happen within 1 to 3 days. The carriers leave Interstate 85 at Commerce or Lawrenceville and reach the Loop in half an hour.',
  'Atlanta, Augusta, and Macon are same-day lanes. Greenville is the same day too. Charlotte, Savannah, and Nashville take a day. Washington and Chicago take two.'],
 'Tell us the neighborhood and the Saturday. Downtown, Five Points, and Boulevard need a meeting spot. The Westside, Cedar Creek, and the Oconee subdivisions usually allow the curb. Home game days move everything.'))

BODY.append(sec('The Roads','The Loop, Highway 316, US 441, US 78, and the Way to Interstate 85',
 prose(
  L('Athens is the biggest city in Georgia without an interstate, and two roads make up for it.'),
  P('Highway 316 is the University Parkway, the four-lane from the Loop to Interstate 85 at Lawrenceville. It is the Atlanta road, and most carriers arrive on it. US 441 runs north from the Loop to Interstate 85 at Commerce, where the truck stops are. Carriers coming from the Carolinas leave 85 there.'),
  P('The Loop is Highway 10, the perimeter around the city. Every exit on it is a meeting spot, and the carriers rarely leave it. Atlanta Highway is US 78 west of the Loop, the strip past the old mall. Epps Bridge Parkway in Oconee County has the newest shopping centers and the widest lots.'),
  P('US 78 runs east to Washington and Augusta. US 29 runs northeast to Danielsville. Lexington Road runs southeast, and Highway 15 runs south to Watkinsville and Greensboro. Prince Avenue, Milledge Avenue, Lumpkin Street, and Broad Street carry the city inside the Loop.'),
  P('The carriers come off the Loop at Atlanta Highway, Prince Avenue, College Station Road, and Lexington Road. The lots along Atlanta Highway, on Epps Bridge, and at the Commerce truck stops are the meeting spots. No road in the region charges a toll.'),
  P('Our office sits on Daniells Bridge Road on the west side, between Atlanta Highway and Epps Bridge Parkway.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, Five Points, Normaltown, Boulevard, the Westside, and Oconee',
 prose(
  L('Athens is a campus, a downtown grid built against it, and a ring of neighborhoods. All of it fills and empties with the semester.'),
  P('Downtown is a tight grid of one-way streets between Broad Street and the railroad. Parking is scarce on a normal day and gone on a game day. A trailer cannot stop there. The driver meets you at a lot off Broad Street, by the convention center, or on the Loop.'),
  P('Five Points has bungalows and student rentals on narrow streets under old trees. The driver meets you on Milledge Avenue or Lumpkin Street. Boulevard, Cobbham, and Pulaski Heights are historic blocks with the same answer. Prince Avenue is the meeting spot. Normaltown has the health sciences campus and a little more room.'),
  P('The Westside along Atlanta Highway and Timothy Road is postwar grids and subdivisions. The truck usually reaches the curb. Homewood Hills, Beechwood, and Forest Heights are the same. The student complexes off Baxter Street and along the Loop have garages and gates. The handoff happens at the leasing office.'),
  P('East Athens and Cedar Creek are subdivisions with wide streets, and Winterville sits beyond with open roads. Watkinsville, Bogart, and the Oconee County subdivisions have wide streets and some gates. The driver meets you at the entrance or on Epps Bridge. Commerce, Jefferson, and Monroe are county seats with lots on every strip.'),
 )))

ROUTES=[("Atlanta, GA","SR-316/I-85 · ~70 mi","Same day","$150–$240"),("Augusta, GA","US-78 · ~100 mi","Same day","$150–$240"),
 ("Macon, GA","US-129/US-441 · ~100 mi","Same day","$150–$240"),("Greenville, SC","I-85 · ~100 mi","Same day","$150–$240"),
 ("Charlotte, NC","I-85 · ~200 mi","1 day","$210–$320"),("Savannah, GA","US-441/I-16 · ~230 mi","1 day","$230–$350"),
 ("Nashville, TN","I-85/I-24 · ~320 mi","1 day","$300–$440"),("Raleigh, NC","I-85 · ~350 mi","1 day","$320–$460"),
 ("Orlando, FL","I-75/Turnpike · ~470 mi","1 day","$400–$570"),("Washington, DC","I-85/I-95 · ~600 mi","2 days","$470–$680")]
BODY.append(rate_table('Lanes &amp; Costs','Athens Car Shipping Lanes and Estimated Costs',
 'The lanes that leave the Classic City most, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a sedan that runs, on an open trailer, priced from Athens. Add about 10 to 25 percent for an SUV or pickup, and more for enclosed. The semester, the Saturdays, and the carriers free on your dates set the final price.',
 prose(
  P('Athens prices a little above Atlanta on every lane, because the carrier leaves Interstate 85 to reach it. The half hour on 316 or 441 adds a few dollars and sometimes a day. The student lanes to the Northeast and Florida run full every August and May.'),
  P('Carolina lanes ride 85 all year. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The University, the Hospital, the Plants, and the Transplants',
 prose(
  L('Athens relocates students, professors, residents, and plant engineers, and the semester runs the calendar.'),
  P('The university brings in forty thousand students, and the cars arrive in the second week of August. Move-in fills every street inside the Loop for three days. Cars leave the first week of May after finals. Both windows book up a month ahead, and an adult signs for a student car.'),
  P('Campus streets are closed to trucks during move-in. The handoff happens at a lot on the Loop, on Atlanta Highway, or at the leasing office. The Greek houses on Milledge Avenue meet the driver on Milledge. The veterinary school and the research campus on College Station Road have lots of their own.'),
  P('The faculty and staff arrive on academic start dates in August and January. The hospital on Prince Avenue brings in residents each June and nurses all year. The health sciences campus in Normaltown brings students in each August. We supply the paperwork a reimbursed move needs.'),
  P('The equipment plant in Bogart, the refrigeration plant, and the animal health plant hire engineers on program schedules. Retirees and families move out from Atlanta for Oconee County, and the second car usually rides a truck. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Game Days, Move-In, Ice, and the Pollen',
 prose(
  L('Seven Saturdays a year, Athens doubles in size. The carriers plan around all seven.'),
  P('Home football Saturdays close the campus streets and fill every road inside the Loop from Friday night. Hotels book a year out, and the lots we use become tailgates. We never schedule a pickup inside the Loop on a home game day. The Westside and Oconee run normally, and the Friday before is tight too.'),
  P('Move-in in August and move-out in May fill the student blocks for three days each. The handoff moves to the Loop or Atlanta Highway. Graduation in early May fills the stadium and downtown. The bike race in April closes downtown for a day. The music festival in June does the same.'),
  P('Ice reaches Athens a few times a decade, and the 2014 storm shut the city for days. The 2017 snow dropped half a foot on the hills. Nothing moves a loaded trailer on either, and the carriers hold at the Commerce truck stops. Helene in 2024 downed trees across the county and cut power for days.'),
  P('Tornado warnings and hail come with spring, and the driver waits one out before loading. The pollen coats every car yellow for three weeks in March and April. Summer afternoons bring thunderstorms, and the loading hour moves to the morning in July.'),
 )+chips(["Downtown","Five Points","Normaltown","Boulevard","Cobbham","Pulaski Heights","Chicopee-Dudley","East Athens","Cedar Creek","Green Acres","Westside","Homewood Hills","Beechwood","Forest Heights","Timothy Road","Atlanta Highway","Epps Bridge","Baxter Street","College Station","Winterville","Bogart","Watkinsville","Bishop","Hull","Jefferson","Commerce","Monroe","Madison"])
 +NOTE('Serving Athens and the counties around it, from Commerce to Watkinsville. Tell us the neighborhood, the Saturday, and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Athens?',
 prose(
  L('Open is how the Classic City ships, and the student lanes are priced for it.'),
  P('An enclosed trailer keeps the pollen, the hail, and attention off a car. The garages in Five Points and Oconee book them for collector cars. So does a graduate shipping a first new car to a first job.'),
  P('A student car rides open without a problem. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain what the roof is for.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff on the Loop or at an Atlanta Highway lot, and a delivery. The Saturday sets the day.'),
  P('Approve the price, and a carrier already on 85 takes the booking and turns onto 316. We confirm the spot and the window the same day. The driver inspects the car with you and writes its condition on a Bill of Lading. Both of you sign, and the same form comes out when the car arrives.'),
 )+ULI([
  "Take everything personal out of the car, including the dorm boxes",
  "Keep the tank near a quarter full",
  "Shoot photos of every panel before the handoff, pollen and all",
  "Give the driver a working key and name any mechanical issue",
  "Switch off any aftermarket alarm",
  "For a student car, have the adult who will sign at the meeting spot",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages walk through the rest.'))))

BODY.append(sec('Why Ship Guy','Why Athens Drivers Choose Ship Guy',
 prose(
  L('We bring the 85 carriers in on 316 and 441. We plan around the semester, the Saturdays, and the ice.'),
  P('Ship Guy’s FMCSA brokerage authority is active, and a $75,000 surety bond stands behind it. Both can be checked in the federal register. Our office is on Daniells Bridge Road on the west side.'),
  P('One coordinator stays with your move from the first call to the last signature. You can book open, enclosed, or expedited transport, and the <a href="services.html">services</a> page describes each.'),
 ), alt=True))

BODY.append(office('Athens','2500 Daniells Bridge Rd #578','Athens, GA 30606','+17068906131','(706) 890-6131','ET',
 '2500+Daniells+Bridge+Rd+%23578,+Athens,+GA+30606','Visit Us','Find Ship Guy in Athens',
 'Our office is on Daniells Bridge Road on the west side, between Atlanta Highway and Epps Bridge Parkway.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5091.846534040728!2d-83.458777!3d33.910013400000004!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x88f673b438fc6e37%3A0x31d18623e5080b34!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792162207172!5m2!1sen!2sus'))

FAQ=[
 ("Can you ship a car for a University of Georgia student?","Yes, and it is most of what we do in Athens. Cars arrive the second week of August and leave the first week of May. Both windows book up a month ahead. Campus streets are closed to trucks. The handoff happens at a lot on the Loop or on Atlanta Highway. An adult signs for the car at pickup."),
 ("Will a home football Saturday affect my pickup?","Yes, if you live inside the Loop. The campus streets close, the roads fill from Friday night, and the lots become tailgates. We never schedule a pickup inside the Loop on a home game day. The Westside and Oconee County run normally."),
 ("How much does it cost to ship a car from Athens to Atlanta or the Northeast?","Atlanta runs one hundred fifty to two hundred forty dollars for a sedan. That is about seventy miles down 316 and 85. Washington runs four hundred seventy to six hundred eighty, about six hundred miles up 85 and 95. New York adds about two hundred more. SUVs and pickups add 10 to 25 percent."),
 ("Can the carrier come to my street in Five Points or downtown?","Usually not. Five Points streets are narrow under old trees. Downtown is a one-way grid with no room to stop. The driver meets you on Milledge Avenue, on Prince Avenue, or at a lot off Broad Street. The Westside, Cedar Creek, and Oconee usually allow the curb."),
 ("Why does Athens cost a little more than Atlanta?","Because no interstate reaches it. The carrier leaves Interstate 85 at Lawrenceville or Commerce and drives half an hour on 316 or 441. That adds a few dollars and sometimes a day. The student lanes keep enough trucks coming that the difference stays small."),
 ("Can you pick up at a student apartment complex?","Yes. The complexes off Baxter Street and along the Loop have gates and garages. The handoff happens at the leasing office or the entrance. Send the complex name and the gate code. During move-in, we set the handoff on the Loop instead."),
 ("Do you ship cars for residents at the hospital or the health sciences campus?","Yes, every June and August. The hospital on Prince Avenue brings in residents and nurses each summer. The health sciences campus brings students in each August. The hospital garages and the lots on Prince Avenue work for the handoff. We provide the paperwork a reimbursed move needs."),
 ("What happens if ice or a storm hits on my pickup day?","The carriers hold at the Commerce truck stops until the roads clear. An ice glaze shuts the hills for a day or two. A tornado warning holds the driver until the all-clear. Helene in 2024 blocked roads with trees for days. We call before the window moves."),
 ("Can you ship a car that does not run from Athens?","Yes. A winch truck takes the job, and the longer loading is already in the price. The lots on Atlanta Highway or Epps Bridge give the driver a flat, open spot. Say whether the car rolls, steers, and brakes when you book."),
 ("What do you need for an Athens car shipping quote?","Pickup and delivery addresses, with the neighborhood or the complex on this end. The car’s year, make, and model. Whether it starts and rolls. A choice of open or enclosed, and a date range with the Saturdays in mind. With those, an Athens quote is exact."),
]
BODY.append(faq_section(FAQ,'Athens FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Athens?','Two minutes on the form above prices your lane. Send the neighborhood, the Saturday to avoid, and your dates, and a carrier already on 85 takes it.','+17068906131','(706) 890-6131','Get your free Athens quote'))

build({
 'slug':'auto-transport-athens-georgia',
 'title':'Car Shipping in Athens, GA — Auto Transport | Ship Guy',
 'meta':'Car shipping in Athens, GA, the college town with no interstate, served off Interstate 85 by Highway 316 and the Loop. UGA move-in and move-out, home game Saturday planning, Five Points and downtown meeting spots, Westside and Oconee curbside, student complex gates, hospital residents. Local office on Daniells Bridge Road. Free quote.',
 'h1':'Car Shipping in<br>Athens, <span class="accent">Georgia</span>',
 'lede':'Open, enclosed, and expedited auto transport across the Classic City, planned around 316, the Loop, the semester, and the Saturdays.',
 'tel':'+17068906131','disp':'(706) 890-6131','brand':'Athens','keyword':'car shipping in athens',
 'localterms':['athens','the loop','highway 316','university parkway','interstate 85','lawrenceville','commerce','us 441','us 78','us 29','highway 15','atlanta highway','epps bridge','lexington road','prince avenue','milledge avenue','lumpkin street','broad street','baxter street','college station road','timothy road','daniells bridge','downtown','one-way','convention center','five points','normaltown','health sciences','boulevard','cobbham','pulaski heights','westside','homewood hills','beechwood','forest heights','student complexes','leasing office','east athens','cedar creek','winterville','watkinsville','bogart','oconee county','jefferson','monroe','university','forty thousand','move-in','finals','greek houses','veterinary','research campus','faculty','hospital','residents','nurses','equipment plant','refrigeration','animal health','football','saturdays','tailgates','graduation','bike race','music festival','ice','2014','snow','2017','helene','2024','tornado','hail','pollen','atlanta','augusta','macon','greenville','charlotte','savannah','nashville','raleigh','orlando','washington','chicago','new york','florida'],
}, BODY, FAQ)
