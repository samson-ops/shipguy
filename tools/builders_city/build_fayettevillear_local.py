import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Fayetteville, Arkansas','Car shipping in Northwest Arkansas, on the Interstate 49 corridor between the campus and the headquarters',
 ['Car shipping in Fayetteville runs on two calendars, the university’s and the corporate relocation’s. Ship Guy is a licensed auto transport broker with an office on North Steele Boulevard by the mall.',
  'We book vetted carriers across Northwest Arkansas, from Springdale and Rogers to Bentonville, Bella Vista, and Siloam Springs. We do not own the trucks.',
  'Interstate 49 runs north and south through the whole corridor, from the Boston Mountains to the Missouri line. US 71B is College Avenue, the old road through town. US 412 crosses Springdale on the way to Tulsa. Highway 16 and 45 run east into the hills.',
  'This page covers the corridor and the mountains, the campus and the hills, and the new subdivisions. It also covers the headquarters, the hospitals, the game days, the ice, and the lanes.'],
 'Fayetteville at a glance',
 ['Most pickups happen within 1 to 3 days. The corridor is one of the fastest-growing in the country. The trucking company in Lowell keeps the carriers close.',
  'Tulsa, Springfield, Fort Smith, and Little Rock are same-day lanes. Kansas City is the same day too. Dallas, St. Louis, and Memphis take a day. Denver and Chicago take two.'],
 'Tell us the neighborhood. The campus hill, Dickson Street, and Mount Sequoyah need a meeting spot. The south side, Springdale, and Rogers usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 49, College Avenue, US 412, and the Boston Mountains',
 prose(
  L('Fayetteville sits on the one interstate in the corner of the state. Everything else is a two-lane road into the hills.'),
  P('Interstate 49 runs through the west side of the city. It continues north through Springdale, Rogers, and Bentonville to the Missouri line. South of town it climbs the Boston Mountains to Alma and Fort Smith. It passes through the only highway tunnel in the state. The grades and the ice on that stretch slow a loaded trailer.'),
  P('College Avenue is US 71B, the old highway through the middle of town. US 412 crosses Springdale east to west on the way to Tulsa and Siloam Springs. Highway 16 and Highway 45 run east into the Ozarks. The scenic highway south to the river is no road for a trailer.'),
  P('The carriers come off 49 at Joyce Boulevard, Wedington Drive, and Highway 112. The mall lot at Joyce Boulevard and the lots along College Avenue are the usual meeting spots. In Rogers and Bentonville, the retail centers along 49 do the same job. No road in the corridor charges a toll.'),
  P('Our office sits on North Steele Boulevard by the mall, at the Joyce Boulevard exit.'),
 ), alt=True))

BODY.append(sec('The Hills &amp; the Corridor','The Campus, Dickson Street, Mount Sequoyah, and the New Subdivisions',
 prose(
  L('Fayetteville is a campus on a hill with a boomtown growing up the corridor beside it. The two park differently.'),
  P('The campus sits on the hill above Dickson Street, with narrow streets and student parking. Game days close it. Dickson Street and the square are for walking. The driver meets you at the mall lot, on College Avenue, or at a lot off Wedington.'),
  P('Mount Sequoyah, Wilson Park, and the historic blocks around the square have narrow streets with low trees. The driver stays on College Avenue or Mission Boulevard. The south side along 71B and the subdivisions off Wedington are wide grids. The truck reaches the curb there.'),
  P('Springdale, Rogers, and Bentonville add new subdivisions faster than a carrier’s map updates. Send the full address and the nearest arterial. Bella Vista climbs through hills and around lakes on winding roads. The handoff there happens on US 71 or at the town center.'),
  P('The headquarters campuses in Bentonville, Springdale, and Lowell have lots. A handoff there works when the employer allows it. The supplier offices along 49 in Rogers and Bentonville do the same.'),
 )))

ROUTES=[("Tulsa, OK","US-412 · ~115 mi","Same day","$160–$260"),("Springfield, MO","I-49/US-60 · ~115 mi","Same day","$160–$260"),
 ("Fort Smith, AR","I-49 · ~60 mi","Same day","$130–$220"),("Little Rock, AR","I-49/I-40 · ~190 mi","Same day","$210–$330"),
 ("Kansas City, MO","I-49 · ~220 mi","Same day","$230–$350"),("Oklahoma City, OK","US-412/I-44 · ~215 mi","1 day","$230–$350"),
 ("Dallas, TX","I-49/US-69 · ~340 mi","1 day","$310–$450"),("St. Louis, MO","I-49/I-44 · ~330 mi","1 day","$300–$440"),
 ("Chicago, IL","I-49/I-55 · ~600 mi","1–2 days","$470–$680"),("Denver, CO","I-49/I-70 · ~850 mi","2 days","$620–$880")]
BODY.append(rate_table('Lanes &amp; Costs','Fayetteville Car Shipping Lanes and Estimated Costs',
 'The lanes Northwest Arkansas books most, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a sedan that runs, open trailer. An SUV or pickup runs 10 to 25 percent higher, and enclosed higher again. Game weekends, the ice, and the carriers free on your dates set the final price.',
 prose(
  P('Fayetteville prices well for a city in a corner. The corridor keeps a trucking company and a retailer’s supply chain on the road. Tulsa rides 412, Kansas City rides 49 north, and Little Rock rides 49 and 40.'),
  P('The corporate lanes to Dallas, Chicago, and the coasts run full all year. The <a href="car-shipping-cost.html">cost guide</a> explains how the number is built.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Headquarters, the University, the Hospitals, and the Suppliers',
 prose(
  L('Fayetteville relocates people on the start date, the semester, the residency match, and the supplier’s contract.'),
  P('The retailer in Bentonville, the poultry company in Springdale. The trucking company in Lowell relocate staff from every state. The new headquarters campus in Bentonville brought thousands more. Hundreds of supplier offices along the corridor move teams in and out on contract cycles. The records an employer needs for reimbursement come from us.'),
  P('The university brings cars in each mid-August and sends them home each May. The campus hill is tight on move-in day. The driver meets you at the mall lot or on College Avenue. An adult signs for a student car.'),
  P('The regional hospital and the medical school’s northwest campus bring in residents every July. The veterans hospital hires on start dates. Most arrive from out of state with a car. The handoff happens on North Hills Boulevard or at the mall lot rather than in a hospital garage.'),
  P('Families arrive from every state for the jobs and the schools. The second car usually rides a truck. Bella Vista and the lakes draw retirees who ship a car in from the Midwest. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
  P('Fort Chaffee sits an hour south in Fort Smith, and the Guard trains there on cycles. The <a href="military-car-shipping.html">military</a> page covers a PCS move.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Game Days, Shareholders Week, Ice, and the Spring Storms',
 prose(
  L('Fayetteville closes for football, fills for a shareholders meeting, and ices over every few winters.'),
  P('Home football Saturdays fill the campus hill, Dickson Street, and the corridor from Friday afternoon through Saturday night. We schedule a campus-area pickup on another day, and the mall lot works the rest of the week. Basketball nights do the same on a smaller scale.'),
  P('The retailer’s shareholders week in June fills every hotel from Fayetteville to Bentonville and jams 49. The concerts at the amphitheater in Rogers and the motorcycle rally there do the same on their weekends. We move a corridor pickup around all three.'),
  P('Ice is the winter risk. The 2009 ice storm took the corner of the state down for a week. Glazed pavement shuts 49 and the mountain grades for a day or two. The carriers wait for the sand. A winter pickup can slide a day or two.'),
  P('Tornado season runs March through May, and the 2024 Memorial Day storm cut across Rogers and Bentonville. A warning parks the driver until the all-clear. Spring rains flood the low crossings, and summer heat moves the loading hour earlier.'),
 )+chips(["Downtown","The Square","Dickson Street","Campus","Mount Sequoyah","Wilson Park","College Avenue","Mission Boulevard","Wedington","Joyce Boulevard","Steele Crossing","South Fayetteville","Farmington","Elkins","Springdale","Johnson","Lowell","Rogers","Pinnacle Hills","Bentonville","Bella Vista","Siloam Springs","Prairie Grove","West Fork","Highfill","Centerton"])
 +NOTE('Serving Fayetteville and the whole Northwest Arkansas corridor. Tell us the neighborhood, the week, and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Fayetteville?',
 prose(
  L('Open trailers carry most of what leaves the corridor, and the corporate lanes are priced for them.'),
  P('An enclosed trailer keeps the hail, the dust, and attention off the car. The garages in Pinnacle Hills and the hills above Fayetteville book enclosed trailers. So does an executive’s car moving in on a corporate relocation.'),
  P('A student car or a daily driver rides open and arrives the way it left. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages lay out the choice.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff at the mall lot or on College Avenue, and a delivery. The game schedule picks the day in fall.'),
  P('Say yes to the price, and a carrier already running 49 takes the booking. We set the spot the same day. You and the driver inspect the car and note it on a Bill of Lading. Both sign, and delivery is inspected against that sheet.'),
 )+ULI([
  "Remove your belongings from the car",
  "Keep the gas around a quarter tank",
  "Photograph the car before pickup, especially after a hail storm",
  "Hand the driver a working key and describe any mechanical issue",
  "Turn off any aftermarket alarm",
  "On a game Saturday, plan to meet the truck away from the campus hill",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages spell out the rest.'))))

BODY.append(sec('Why Ship Guy','Why Fayetteville Drivers Choose Ship Guy',
 prose(
  L('We work 49 every day and plan around the games, the ice, and the start dates.'),
  P('Ship Guy is registered with the FMCSA as a broker, and a $75,000 surety bond backs the registration. Both are on the federal register. Our office is on North Steele Boulevard by the mall.'),
  P('The same coordinator quotes the move, books it, and sees it delivered. Open, enclosed, and expedited transport are all available here, and the <a href="services.html">services</a> page describes each.'),
 ), alt=True))

BODY.append(office('Fayetteville','3537 N Steele Blvd #558','Fayetteville, AR 72703','+14794322108','(479) 432-2108','CT',
 '3537+N+Steele+Blvd+%23558,+Fayetteville,+AR+72703','Visit Us','Find Ship Guy in Fayetteville',
 'Our office is on North Steele Boulevard by the mall, at the Joyce Boulevard exit on Interstate 49.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4956.319105980147!2d-94.15773100000001!3d36.1159996!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x87c96dc1a2b2687f%3A0xa6e21c6d6448fa2e!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792153801233!5m2!1sen!2sus'))

FAQ=[
 ("Do you handle relocations to the headquarters in Bentonville, Springdale, or Lowell?","Yes, on start dates all year. The retailer, the poultry company, and the trucking company relocate staff from every state. The supplier offices along 49 do the same on contract cycles. Most ship a car rather than drive it. We provide the records a reimbursed move needs."),
 ("How much does it cost to ship a car from Fayetteville to Dallas or Kansas City?","Dallas runs three hundred ten to four hundred fifty dollars for a sedan. That is about three hundred forty miles down 49 and US 69. Kansas City runs two hundred thirty to three hundred fifty, about two hundred twenty miles up 49. SUVs and pickups add 10 to 25 percent."),
 ("Can you ship a car for a University of Arkansas student?","Yes, every August and May. The campus hill is tight on move-in day. The driver meets you at the mall lot or on College Avenue. An adult signs at pickup, and a parent can sign when it arrives. Two to three weeks of notice keeps the August price steady."),
 ("Does a Razorback home game affect my pickup?","On the hill and along Dickson Street, yes. Game Saturdays fill the campus and the corridor from Friday afternoon through Saturday night. We schedule a campus-area pickup on another day. Springdale, Rogers, and the south side run normally."),
 ("What happens if an ice storm hits on my pickup day?","The carriers wait for the sand trucks. Glazed pavement shuts 49 and the Boston Mountain grades for a day or two. The 2009 storm shut the corner of the state for a week. A winter pickup can lose a day or two. We call as the forecast changes."),
 ("Can you pick up in a new subdivision in Rogers or Bentonville?","Yes, with the full address. The corridor adds streets faster than a carrier’s map updates. Send the address and the nearest arterial. The driver meets you there or at the retail center by 49. Most of those streets are wide enough for the curb."),
 ("Can you deliver to Bella Vista or the Ozark hill towns?","Yes, with a meeting spot. Bella Vista winds through hills and around lakes, and the hollow roads east of town have no shoulders. The driver meets you on US 71, at the town center, or at the nearest highway. Those pickups run 2 to 4 days."),
 ("Do you ship cars for residents at Washington Regional or the UAMS campus?","Yes, every July. Residents arrive from every state, and most bring a car. The handoff happens on North Hills Boulevard or at the mall lot, not in a hospital garage. We plan the pickup around the report date."),
 ("Can you ship a car that does not run from Fayetteville?","Yes. A winch-equipped carrier is lined up, and the slower loading is in the quote. The spot has to be flat and open, which here means the mall lot. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Fayetteville car shipping quote?","Both addresses, with the neighborhood on this end. The year, make, and model. Whether it runs. Open or enclosed. Your dates, with the game schedule or the start date in mind. That is everything a Fayetteville quote needs."),
]
BODY.append(faq_section(FAQ,'Fayetteville FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Fayetteville?','The form above prices it in about two minutes. Tell us the neighborhood and your dates, and a carrier already running 49 takes it from there.','+14794322108','(479) 432-2108','Get your free Fayetteville quote'))

build({
 'slug':'auto-transport-fayetteville-arkansas',
 'title':'Car Shipping in Fayetteville, AR — Auto Transport | Ship Guy',
 'meta':'Car shipping in Fayetteville, AR on the Interstate 49 corridor. Razorback move-in and game-day timing, Bentonville, Springdale, and Lowell headquarters relocations, new-subdivision addresses in Rogers and Bentonville, hospital residents, Bella Vista hills, ice storm and tornado planning. Local office on North Steele Boulevard. Free quote.',
 'h1':'Car Shipping in<br>Fayetteville, <span class="accent">Arkansas</span>',
 'lede':'Open, enclosed, and expedited auto transport across Northwest Arkansas, planned around the corridor, the campus, and the ice.',
 'tel':'+14794322108','disp':'(479) 432-2108','brand':'Fayetteville','keyword':'car shipping in fayetteville',
 'localterms':['fayetteville','interstate 49','college avenue','us 71b','us 412','highway 16','highway 45','highway 112','boston mountains','tunnel','joyce boulevard','wedington','mission boulevard','north hills boulevard','steele boulevard','mall','downtown','the square','dickson street','campus','mount sequoyah','wilson park','south side','springdale','johnson','lowell','rogers','pinnacle hills','bentonville','bella vista','siloam springs','farmington','elkins','prairie grove','retailer','poultry company','trucking company','headquarters','suppliers','university','razorback','move-in','regional hospital','medical school','veterans hospital','residents','shareholders','amphitheater','motorcycle rally','ice storm','2009','tornado','2024','hail','fort chaffee','guard','tulsa','springfield','fort smith','little rock','kansas city','oklahoma city','dallas','st. louis','memphis','chicago','denver'],
}, BODY, FAQ)
