import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Aurora, Illinois','Car shipping in the second-largest city in Illinois, on the Fox River forty miles west of the Loop',
 ['Car shipping in Aurora runs off the Reagan Tollway, which crosses the north side with four exits. Ship Guy is a licensed auto transport broker with an office on River Street downtown.',
  'We book vetted carriers across the Fox Valley, from Sugar Grove to Naperville and down to Oswego. The trucks are not ours.',
  'Interstate 88 is the tollway, with exits at Orchard Road, Route 31, Farnsworth Avenue, and Eola Road. Route 59 runs the far east side past the mall. Routes 25 and 31 follow the river. US 30 and US 34 reach the south and the east. Randall Road runs the west.',
  'This page covers the tollway, downtown, the West Side, the far east side, and the towns around. It also covers the hospitals, the outlets, the warehouses, the Fourth of July, the river, and the lanes.'],
 'Aurora at a glance',
 ['Most pickups happen within 1 to 3 days. Chicago carriers take the tollway out, and the cross-country trucks pass on 80 and 88.',
  'Chicago is an hour, and Milwaukee is two. Indianapolis, St. Louis, and Detroit are a same-day haul. Minneapolis and Nashville take a day. The coasts need three to five.'],
 'Tell us the side of the river. Downtown and the West Side historic blocks need a meeting spot. The far east side, Orchard Road, and the newer subdivisions usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 88, Route 59, Routes 25 and 31, Farnsworth Avenue, and Orchard Road',
 prose(
  L('Aurora is the western end of the Chicago tollway system. The carriers use it as the exit from the metro.'),
  P('Interstate 88 is the Reagan Tollway, and it crosses the north side of the city. The exits at Orchard Road, Route 31, Farnsworth, and Eola cover seven miles. A carrier leaving Chicago for Iowa or Denver takes it. The tolls are electronic, and the carriers pay them with a transponder. The cost rides inside the quote.'),
  P('Route 59 runs north and south on the far east side, past the mall and the Naperville line. Routes 25 and 31 run Broadway and Lake Street along the two banks of the river. US 30 crosses the south side toward Montgomery and Sugar Grove. US 34 is Ogden Avenue, the road east to Naperville and south to Oswego. Route 56 is Butterfield Road on the northeast side.'),
  P('Farnsworth Avenue runs from the tollway past the outlets to downtown. Orchard Road carries the west side from the tollway to US 30. Eola Road runs the warehouse corridor on the east. Galena Boulevard and New York Street cross downtown and the island. Indian Trail, Montgomery Road, and Randall Road fill in the rest.'),
  P('The carriers come off 88 at Farnsworth, Orchard, and Eola, and off 59 at the mall. The lots at the outlets, at the mall, and at the casino are the usual meeting spots. The tollway is the only toll in town. Everything else, river bridges included, is free.'),
  P('Our office is on River Street downtown, on the west bank across from the island.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown and the Island, the West Side, the Far East Side, Orchard Road, and the Towns Around',
 prose(
  L('Aurora is a river town that grew east to the county line and west into the farms. It is four cities in one.'),
  P('Downtown sits on both banks and on Stolp Island in the middle of the river. The island streets around the theater are narrow and one-way, and a trailer cannot stop on them. The driver meets you at the transportation center lots by the roundhouse or at the riverfront park. The near east side off Broadway is an older grid with alleys. The handoff moves to a lot on New York Street.'),
  P('The West Side is the old half of the city. The Tanner historic district above the river has Victorian houses on narrow streets under old trees. The driver meets you on Lake Street or at the hospital lot. Pigeon Hill and the grids off Galena allow the curb on most blocks. Aurora University and the Southlake blocks are the same.'),
  P('The far east side across Route 59 sits in DuPage County. It is subdivisions from the last forty years. Fox Valley, Eola, and the streets off Ogden have wide roads, and the truck reaches the curb. Stonebridge on the north side is a golf community with a gate. The handoff works at the clubhouse lot. The Orchard Road corridor on the west is the newest growth, and the curb works there too.'),
  P('North Aurora, Montgomery, and Oswego sit on the river to the north and south. They have wide streets and lots on the main roads. Sugar Grove is the college town to the west. Naperville is the big neighbor to the east, and Batavia is the lab town to the north. All of them price the same as Aurora, and so does Boulder Hill across the Kendall line.'),
 )))

ROUTES=[("Chicago, IL","I-88 · ~40 mi","Same day","$120–$200"),("Milwaukee, WI","I-88/I-94 · ~120 mi","Same day","$170–$270"),
 ("Indianapolis, IN","I-80/I-65 · ~205 mi","Same day","$220–$330"),("St. Louis, MO","I-55 · ~280 mi","1 day","$270–$400"),
 ("Detroit, MI","I-94 · ~300 mi","1 day","$290–$420"),("Minneapolis, MN","I-39/I-90 · ~385 mi","1 day","$340–$490"),
 ("Nashville, TN","I-57/I-24 · ~490 mi","1 day","$410–$590"),("Dallas, TX","I-55/I-44 · ~940 mi","2–3 days","$650–$920"),
 ("Denver, CO","I-88/I-80/I-76 · ~960 mi","2–3 days","$660–$940"),("Orlando, FL","I-65/I-75 · ~1,210 mi","3 days","$800–$1,130")]
BODY.append(rate_table('Lanes &amp; Costs','Aurora Car Shipping Lanes and Estimated Costs',
 'The lanes Fox Valley cars take most, with estimated open-trailer ranges. Your exact route prices on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates priced from Aurora for a sedan that runs, on an open trailer. SUVs and pickups add 10 to 25 percent, and enclosed adds more. Tollway charges are included. Fuel, the week, and the carriers free on your dates decide the final number.',
 prose(
  P('Aurora prices within a few dollars of Chicago on every lane. The carriers load in the city and finish the trailer out here on the way west. The Denver and Iowa lanes price a little under the city. The trucks pass the door on 88.'),
  P('Florida and Texas follow the snowbird calendar, higher in the fall and lower in the spring. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Hospitals, the Outlets, the Warehouses, the Lab, and the Tech Corridor',
 prose(
  L('Aurora relocates nurses, warehouse managers, physicists, and engineers from the corridor. Most arrive on a closing date.'),
  P('The hospital on Ogden Avenue and the hospital on Lake Street bring in nurses on contracts all year. Residents arrive each June. The clinics across the Fox Valley move physicians with a closing date and a second car. We supply the paperwork a reimbursed move needs.'),
  P('The warehouses along Eola Road and the tollway move managers and technicians from every state. The outlets at Farnsworth and the casino by the tollway hire managers on short notice. The lab in Batavia relocates physicists and engineers on program schedules. The tech corridor on 88 toward Naperville moves engineers in every month.'),
  P('Aurora University brings cars in each August, and the community college in Sugar Grove does the same. A parent ships the car, and an adult signs at a campus lot. Families priced out of Naperville buy on the far east side. Many ship a second car behind the move.'),
  P('Great Lakes sits an hour and a half north, and families on orders settle across the Fox Valley. The orders cover one car, and the second one comes with us. Ship Guy is a private broker with no connection to the base. The <a href="military-car-shipping.html">military</a> page covers the timing. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Fourth of July, the Riverfront, the Fox, the Snow, and the Wind',
 prose(
  L('Aurora runs on a parade in July, a riverfront summer, and a Chicago winter with more wind.'),
  P('The Fourth of July parade and fireworks fill downtown and both banks of the river. The island closes, and the lots by the roundhouse fill by noon. A downtown pickup that day moves to the outlets or to a lot on Farnsworth. The heritage festival and the pride parade do the same thing on a smaller scale in summer.'),
  P('The riverfront park fills its lots for the blues festival in June and the concerts through September. The theater on the island fills the island lots on show nights. The outlets gridlock Farnsworth on Black Friday and the weekends before Christmas. A handoff near any of them moves to the morning.'),
  P('The Fox River floods. The 2013 storm put the island and the riverfront under water, and the 2008 flood did the same. A pickup on the island or the low streets along Broadway moves up the hill for a day. The subdivisions on the ridges never notice.'),
  P('Winter brings three feet of snow, and the tollway closes a few times a season. The 2011 blizzard shut 88 for a day. The 2019 cold snap froze the trailers to the pavement. The carriers park at the outlets until the plows finish, and a winter pickup can lose a day. Summer brings the derechos. The 2020 storm took the trees down across the Fox Valley. The sirens sound a few times each spring.'),
 )+chips(["Downtown","Stolp Island","River Street","Roundhouse","RiverEdge Park","Near East Side","Broadway","West Side","Tanner District","Lake Street","Pigeon Hill","Galena","Southlake","Aurora Hills","Indian Trail","Stonebridge","North Side","Farnsworth","Outlets","Eola","Far East Side","Fox Valley","Route 59","Ogden","Orchard Road","Randall Road","Montgomery","North Aurora","Oswego","Boulder Hill","Sugar Grove","Naperville","Batavia"])
 +NOTE('Serving Aurora and the whole Fox Valley across Kane, DuPage, Kendall, and Will Counties. Tell us the side of the river and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Aurora?',
 prose(
  L('Most cars leave the Fox Valley on an open trailer, and the lane prices assume one.'),
  P('A closed trailer keeps a car away from the salt, the gravel, and the weather. The garages in Stonebridge and on the far east side book one for the shows. Families shipping a new car to a student book one too.'),
  P('An everyday car or a work truck goes open and comes off the trailer clean. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain the trade-off.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a meeting spot at the outlets or the mall, and a signed sheet at delivery. The closing date sets the week.'),
  P('Agree to the price, and we assign the car to a carrier already headed out 88. The lot and the window come back to you that day. The driver goes over the car with you and marks every scratch on a Bill of Lading. Both of you sign, and the sheet is checked again at delivery.'),
 )+ULI([
  "Clear out the cabin, the trunk, and the glovebox",
  "Bring the fuel down to a quarter tank",
  "Photograph every panel and the mileage before the handoff",
  "Give the driver one working key and name any mechanical fault",
  "Disable any aftermarket alarm",
  "Downtown or in the Tanner district, meet the truck at the roundhouse lots or on Lake Street",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Aurora Drivers Choose Ship Guy',
 prose(
  L('We load the carriers as they leave the metro on 88. We plan around the closing date, the river, and the winter.'),
  P('Ship Guy is an active FMCSA broker with a $75,000 surety bond on file. The federal register shows both. Our office is on River Street downtown.'),
  P('The coordinator who prices your move stays on it until the car is signed for. Open, enclosed, and expedited transport are on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Aurora','160 S River St #473','Aurora, IL 60506','+13312724208','(331) 272-4208','CT',
 '160+S+River+St+%23473,+Aurora,+IL+60506','Visit Us','Find Ship Guy in Aurora',
 'Our office is on River Street downtown, on the west bank of the Fox across from Stolp Island.',
 map_src=None))

FAQ=[
 ("Can you time delivery to my closing date in Aurora?","Yes. Closings drive most Aurora bookings. Families come from Chicago and from out of state. They buy on the far east side or along Orchard Road. We build the delivery window around the closing, and it moves when the closing does. Tell us as soon as the date changes."),
 ("How much does it cost to ship a car from Aurora to Chicago or Milwaukee?","Chicago runs one hundred twenty to two hundred dollars for a sedan, about forty miles down the tollway. Milwaukee runs one hundred seventy to two hundred seventy, about one hundred twenty miles on 88 and 94. Indianapolis comes in between two hundred twenty and three hundred thirty. The tolls are already inside those numbers. An SUV or pickup adds 10 to 25 percent."),
 ("Can the carrier come to my street downtown or in the Tanner district?","Usually not. The island streets are narrow and one-way, and the Tanner district has old trees over narrow streets. The driver meets you at the roundhouse lots, on Lake Street, or at the park by the river. The far east side, Orchard Road, and the newer subdivisions usually allow the curb."),
 ("Does the carrier pay the tollway, and is it in my price?","Yes on both. The carriers run 88 with a transponder, and the tolls ride inside the quote. You never see a separate charge. A carrier that avoids the tollway takes US 30 or Route 59. The price does not change either way."),
 ("Do you ship cars for people relocating to the hospitals or the warehouses?","Yes, all year. The hospitals on Ogden and Lake Street bring in nurses, residents, and physicians every month. The warehouses on Eola and the tollway move managers from every state. Many ship a second car behind the move. The handoff works at the outlets or a lot on Farnsworth. We provide the paperwork a reimbursed move needs."),
 ("Can you ship a car to or from Naperville, Oswego, or Sugar Grove?","Yes, and all three price the same as Aurora. Naperville rides the same carriers off 88 and Route 59. Oswego rides them off US 34, and Sugar Grove rides them off Orchard Road and US 30. A lot off the main road works for a handoff. Send the full address for a new subdivision."),
 ("What happens if a blizzard or the river hits on my pickup day?","Snow closes the tollway a few times a winter. The carriers park at the outlets until the plows finish. A winter pickup can slip a day, and you hear before it does. The river floods the island and the low streets along Broadway after a big storm. A pickup there moves up the hill for a day. A derecho or a tornado warning stops the loading until the warning lifts."),
 ("Can you ship a car that does not run from Aurora?","Yes. We dispatch a carrier with a winch. The extra loading time is inside the quote from the first number. The outlet lots or the mall lot give the driver level pavement. Tell us whether the car rolls, steers, and brakes."),
 ("Can you time delivery to a student move at Aurora University?","Yes. The Southlake campus and the community college in Sugar Grove take cars in every August. They send them out every May. A parent books, and an adult signs at a campus lot. We tie the delivery window to the move-in date and slide it when the date slides."),
 ("What do you need for an Aurora car shipping quote?","The two addresses, with the side of the river or the town here. Year, make, and model. Whether it moves under its own power. Open or enclosed. The week around the closing. That is a complete Aurora request, and the number comes back the same day."),
]
BODY.append(faq_section(FAQ,'Aurora FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Aurora?','Two minutes on the form above prices your lane. Send the side of the river and your dates, and a carrier already on 88 takes it.','+13312724208','(331) 272-4208','Get your free Aurora quote'))

build({
 'slug':'auto-transport-aurora-illinois',
 'title':'Car Shipping in Aurora, IL — Auto Transport | Ship Guy',
 'meta':'Car shipping in Aurora, IL on the Fox River, where the Reagan Tollway leaves the Chicago metro. Closing-date deliveries across the Fox Valley, hospital and warehouse relocations, downtown and Tanner district meeting spots, far east side and Orchard Road curbside pickups, the Fourth of July, the river, and the winter. Local office on River Street. Free quote.',
 'h1':'Car Shipping in<br>Aurora, <span class="accent">Illinois</span>',
 'lede':'Open, enclosed, and expedited auto transport across the Fox Valley, planned around 88, Route 59, the closing date, the river, and the winter.',
 'tel':'+13312724208','disp':'(331) 272-4208','brand':'Aurora','keyword':'car shipping in aurora',
 'localterms':['aurora','fox river','fox valley','interstate 88','reagan tollway','tollway','transponder','orchard road','route 31','farnsworth','eola','route 59','route 25','broadway','lake street','us 30','us 34','ogden','route 56','butterfield','galena','new york street','indian trail','montgomery road','randall road','downtown','stolp island','island','theater','transportation center','roundhouse','park','near east side','west side','tanner','victorian','pigeon hill','southlake','aurora university','far east side','dupage','fox valley mall','mall','stonebridge','gate','clubhouse','north aurora','montgomery','oswego','sugar grove','naperville','batavia','boulder hill','kendall','kane','will','hospital','nurses','residents','clinics','warehouses','outlets','casino','lab','physicists','tech corridor','community college','great lakes','orders','closing date','fourth of july','parade','fireworks','heritage festival','pride','blues','concerts','black friday','2013','2008','flood','snow','2011 blizzard','2019','derecho','2020','sirens','chicago','milwaukee','indianapolis','st. louis','detroit','minneapolis','nashville','dallas','denver','orlando','iowa'],
}, BODY, FAQ)
