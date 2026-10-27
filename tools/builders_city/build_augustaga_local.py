import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Augusta, Georgia','Car shipping on the Savannah River, where Interstate 20 crosses into South Carolina',
 ['Car shipping in Augusta starts on Interstate 20, halfway between Atlanta and Columbia. Ship Guy is a licensed auto transport broker with an office on Laney Walker Boulevard.',
  'We book vetted carriers across the river region, from Evans to Hephzibah and across into North Augusta. We do not own the trucks.',
  'Interstate 20 crosses the north side of the city and the river into South Carolina. Interstate 520 is the Bobby Jones Expressway, the loop around the south and west. Gordon Highway, Washington Road, and Wrightsboro Road carry the rest. Riverwatch Parkway runs downtown.',
  'This page covers the interstate, the loop, downtown, the Hill, the mill blocks, and the Carolina side. It also covers the fort, the medical district, the nuclear site, Masters week, and the lanes.'],
 'Augusta at a glance',
 ['Most pickups happen within 1 to 3 days. Interstate 20 brings the Atlanta-to-Columbia carriers past the city all day.',
  'Atlanta, Columbia, and Athens are same-day lanes. Charlotte and Savannah are the same day too. Charleston, Jacksonville, and Raleigh take a day. Washington and Dallas take two.'],
 'Tell us the neighborhood and the week. The Hill, Olde Town, and Harrisburg need a meeting spot. Evans, Martinez, and South Augusta usually allow the curb. Masters week moves everything.'))

BODY.append(sec('The Roads','Interstate 20, the Bobby Jones Expressway, Gordon Highway, and Washington Road',
 prose(
  L('Augusta sits on the interstate between Atlanta and the Carolina coast, and the loop does the rest.'),
  P('Interstate 20 runs along the north side of the city from Grovetown to the river. The ramps at Washington Road, Riverwatch Parkway, and Wheeler Road are the way in. It crosses the Savannah River into North Augusta and runs on to Columbia. Carriers from Atlanta and the Carolinas pass on it all day.'),
  P('Interstate 520 is the Bobby Jones Expressway. It loops from 20 around the west and south sides and crosses the river as the Palmetto Parkway. Gordon Highway is US 78, the long strip to the fort gates and on to Thomson. Deans Bridge Road and Peach Orchard Road run south into the flat grids.'),
  P('Washington Road is the strip past the golf course to the interstate. Wrightsboro Road passes the mall. Riverwatch Parkway runs from 20 down to the river and downtown. Walton Way climbs the Hill. The 13th Street bridge crosses to North Augusta, and the Carolina side rides the same carriers.'),
  P('The carriers come off 20 at Washington Road and Wheeler Road. Off 520, they use Wrightsboro and Gordon Highway. The lots at the mall, along Washington Road, and on Gordon Highway are the usual meeting spots. No road in the region charges a toll.'),
  P('Our office sits on Laney Walker Boulevard in the medical district, a few blocks from downtown.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the Hill, Harrisburg, West Augusta, and the Carolina Side',
 prose(
  L('Augusta is a river town with a hill, a canal, and a ring of suburbs around the fort.'),
  P('Downtown has Broad Street, one of the widest main streets in the country. A trailer can stop on it. Olde Town and the blocks off Greene Street are narrow and historic. The driver meets you on Broad, on Reynolds Street by the river, or at the Common. The medical district along Laney Walker has garages and wide streets.'),
  P('Summerville, called the Hill, has old houses on narrow streets under big trees. The driver meets you on Walton Way or at a lot off Wrightsboro. Harrisburg and the mill blocks along the canal are tight. The handoff happens on Broad Street or at the canal lots. Forest Hills and National Hills have winding streets near the course.'),
  P('West Augusta along Washington Road is a postwar grid where the truck usually reaches the curb. Martinez and Evans in Columbia County are cul-de-sac subdivisions with gates on some entrances. The driver meets you at the entrance or on Washington Road. Grovetown sits by the fort gate with wide new streets.'),
  P('South Augusta along Peach Orchard and Deans Bridge is flat grids and apartment complexes with room to stop. Hephzibah and Blythe are farther out with long drives. North Augusta and Aiken across the river are open grids. The Carolina side prices the same as the Georgia side.'),
 )))

ROUTES=[("Atlanta, GA","I-20 · ~150 mi","Same day","$170–$280"),("Columbia, SC","I-20 · ~75 mi","Same day","$150–$240"),
 ("Athens, GA","US-78 · ~100 mi","Same day","$150–$240"),("Charlotte, NC","I-20/I-77 · ~170 mi","Same day","$190–$300"),
 ("Savannah, GA","US-25/SR-21 · ~130 mi","Same day","$170–$270"),("Charleston, SC","I-20/I-26 · ~160 mi","1 day","$190–$300"),
 ("Jacksonville, FL","US-25/I-95 · ~260 mi","1 day","$250–$370"),("Raleigh, NC","I-20/I-95 · ~310 mi","1 day","$290–$420"),
 ("Washington, DC","I-95 · ~540 mi","1–2 days","$430–$620"),("Dallas, TX","I-20 · ~870 mi","2 days","$600–$860")]
BODY.append(rate_table('Lanes &amp; Costs','Augusta Car Shipping Lanes and Estimated Costs',
 'The lanes that leave the river region most, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a sedan that runs, on an open trailer, priced from Augusta. Add about 10 to 25 percent for an SUV or pickup, and more for enclosed. Masters week, the storms, and the carriers free on your dates set the final price.',
 prose(
  P('Augusta prices like Columbia and a little above Atlanta, because the carrier leaves 20 to reach it. The fort keeps the Maryland, Texas, and Arizona lanes busy with signal and cyber moves. Interstate 20 runs west to Dallas without a turn.'),
  P('Carolina lanes ride 20 and 77 all year. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','Fort Eisenhower, the Cyber Command, the Medical District, and the Nuclear Site',
 prose(
  L('Augusta relocates soldiers, cyber specialists, residents, and engineers, and the fort calendar is the biggest one.'),
  P('Fort Eisenhower trains signal and cyber soldiers on class cycles and hosts the Army cyber command. Specialists and their families rotate in on orders all year. Orders cover one car, and the second one comes with us. The gates along Gordon Highway stop the truck. The handoff happens at a lot in Grovetown or on the highway.'),
  P('Ship Guy is a private broker with no connection to the fort. The <a href="military-car-shipping.html">military</a> page covers the timing around a report date.'),
  P('The cyber center downtown and the contractors around the fort hire engineers on contract cycles. The medical district brings in residents each June and nurses all year. The medical college brings students in each August. The campus garages and the lots along Laney Walker work for the handoff.'),
  P('The nuclear site across the river and the power plant in Burke County rotate engineers on outage schedules. The golf cart plants, the paper mill, and the tractor plant in Grovetown relocate staff on program schedules. We supply the paperwork a reimbursed move needs.'),
  P('Retirees and families arrive from the Northeast for Columbia County, and the second car usually rides a truck. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Masters Week, Helene, Ice, and the Heat',
 prose(
  L('One week in April changes everything in Augusta, and the weather supplies a few more.'),
  P('Masters week fills the city with visitors, and Washington Road crawls from Monday to Sunday. Rental houses turn over, and hotels fill for an hour in every direction. The roads near the course close. We schedule pickups near the course before or after the tournament. South Augusta runs normally.'),
  P('Helene in 2024 tore through the city with hurricane winds, and the trees came down on every street. Power was out for weeks. The carriers waited for the clearing crews, and pickups moved to the lots on Gordon Highway. A storm that strong is rare, but the remnants of a Gulf storm cross the region most years.'),
  P('Ice is the other big one. The 2014 storm coated the city for days, and nothing moved on the Hill. A glaze shuts the hills for a day or two, and the carriers hold on Interstate 20. Spring brings tornado warnings and hail, and a warning holds the driver until the all-clear.'),
  P('Summer runs hot and humid, and the loading hour moves to early morning in July and August. The pollen turns every car yellow for a few weeks in spring. Move-in at the medical college fills Laney Walker in August.'),
 )+chips(["Downtown","Broad Street","Olde Town","Riverwalk","Laney Walker","Bethlehem","Harrisburg","The Hill","Summerville","Forest Hills","National Hills","West Augusta","Montclair","Westside","South Augusta","Peach Orchard","Deans Bridge","Hephzibah","Blythe","Martinez","Evans","Grovetown","Harlem","Thomson","North Augusta","Aiken","Beech Island"])
 +NOTE('Serving Augusta and the whole river region, both sides of the line. Tell us the neighborhood, the gate, and the week.')))

BODY.append(sec('Your Options','Open or Enclosed in Augusta?',
 prose(
  L('Open is how the region ships, and the fort lanes are priced for it.'),
  P('An enclosed trailer keeps the pollen, the hail, and attention off a car. Soldiers with a restored car book enclosed for a long move. The garages on the Hill and in Evans book them for collector cars.'),
  P('A daily driver rides open without a problem. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain what the roof is for.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff on Washington Road or at the Gordon Highway lots, and a delivery. The calendar sets the week.'),
  P('Approve the price, and a carrier already on 20 is assigned. The spot and the window are confirmed that day. The driver circles the car with you and writes down its condition on a Bill of Lading. Both of you sign, and the sheet reappears at delivery.'),
 )+ULI([
  "Clear your belongings out of the car",
  "Run the tank down to about a quarter",
  "Photograph the car before the handoff, pollen and all",
  "Provide a working key and disclose any mechanical issue",
  "Turn off any aftermarket alarm",
  "Near the fort, plan to meet the truck outside the gate on Gordon Highway",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Augusta Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already run 20 between Atlanta and Columbia. We plan around the gates, the tournament, and the storms.'),
  P('Ship Guy’s FMCSA brokerage authority is active, and a $75,000 surety bond backs it. Both are on file in the federal register. Our office is on Laney Walker Boulevard in the medical district.'),
  P('Your coordinator is the same person from the first quote to the last signature. Open, enclosed, and expedited transport are all offered, and the <a href="services.html">services</a> page sets them out.'),
 ), alt=True))

BODY.append(office('Augusta','1143 Laney Walker Blvd #625','Augusta, GA 30901','+17067496343','(706) 749-6343','ET',
 '1143+Laney+Walker+Blvd+%23625,+Augusta,+GA+30901','Visit Us','Find Ship Guy in Augusta',
 'Our office is on Laney Walker Boulevard in the medical district, a few blocks from downtown.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5118.238330158953!2d-81.97860899999999!3d33.4656709!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x88f9cd5941c01a97%3A0x5dbd8769927b0da1!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792162180857!5m2!1sen!2sus'))

FAQ=[
 ("Will Masters week affect my Augusta pickup?","If you live near the course, yes. Washington Road and the surrounding streets crawl or close for the whole week in April. We schedule pickups near the course before or after the tournament. South Augusta, Grovetown, and the Carolina side run normally that week."),
 ("Do you handle a PCS move to Fort Eisenhower?","Yes, on every class cycle. Orders cover one car, and the second one comes with us. The gates along Gordon Highway stop the truck, so we meet you in Grovetown or on the highway. We schedule around your report date. Ship Guy is a private broker with no connection to the fort."),
 ("How much does it cost to ship a car from Augusta to Atlanta or Washington?","Atlanta runs one hundred seventy to two hundred eighty dollars for a sedan. That is about one hundred fifty miles out Interstate 20. Washington runs four hundred thirty to six hundred twenty, about five hundred forty miles up 95. The Fort Meade lane prices the same. SUVs and pickups add 10 to 25 percent."),
 ("Can you ship a car to or from North Augusta or Aiken?","Yes, and it prices the same. North Augusta, Aiken, and Beech Island ride the same carriers as Augusta. The lots along the Palmetto Parkway work for a handoff. The state line changes the paperwork, not the price."),
 ("Can the carrier come to my street on the Hill or in Olde Town?","Usually not. The Hill streets are narrow under big trees, and Olde Town blocks are tight and historic. The driver meets you on Walton Way, on Broad Street, or at a lot off Wrightsboro. West Augusta, Evans, and South Augusta usually allow the curb."),
 ("What happens if a storm like Helene hits before my pickup?","The carriers wait for the clearing crews. Helene in 2024 blocked every street with trees and cut power for weeks. Pickups moved to the Gordon Highway lots once the roads opened. An ice glaze or a tornado warning holds the driver for a day. We call before the window moves."),
 ("Do you ship cars for residents and students in the medical district?","Yes, every June and August. The hospitals bring in residents and nurses each summer, and the medical college brings students in each August. The campus garages and the lots along Laney Walker work for the handoff. An adult signs for a student car."),
 ("Do you ship cars for workers at the nuclear site or the power plant?","Yes, on the outage schedules. Engineers and contractors rotate in for months at a time and often ship a car behind the move. The handoff works at a lot on the Palmetto Parkway or in Waynesboro. We provide the paperwork a reimbursed move needs."),
 ("Can you ship a car that does not run from Augusta?","Yes. We send a carrier with a winch, and the extra loading time is priced in. Choose a flat, open spot, which usually means a lot on Washington Road or Gordon Highway. Tell us whether the car rolls, steers, and brakes."),
 ("What do you need for an Augusta car shipping quote?","Where the car is and where it goes, with the gate or the neighborhood here. Year, make, and model. Whether it runs and rolls. Open or enclosed, and dates that steer clear of Masters week. An Augusta quote needs nothing more."),
]
BODY.append(faq_section(FAQ,'Augusta FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Augusta?','Two minutes on the form above prices your lane. Send the neighborhood, the gate, and your dates, and a carrier already on 20 takes it.','+17067496343','(706) 749-6343','Get your free Augusta quote'))

build({
 'slug':'auto-transport-augusta-georgia',
 'title':'Car Shipping in Augusta, GA — Auto Transport | Ship Guy',
 'meta':'Car shipping in Augusta, GA on Interstate 20 between Atlanta and Columbia. Fort Eisenhower second cars and Gordon Highway gate handoffs, the Hill and Olde Town meeting spots, Evans and South Augusta curbside, the Carolina side, medical district residents, Masters week and storm planning. Local office on Laney Walker Boulevard. Free quote.',
 'h1':'Car Shipping in<br>Augusta, <span class="accent">Georgia</span>',
 'lede':'Open, enclosed, and expedited auto transport across the river region, both sides of the line, planned around 20, the gates, and Masters week.',
 'tel':'+17067496343','disp':'(706) 749-6343','brand':'Augusta','keyword':'car shipping in augusta',
 'localterms':['augusta','interstate 20','interstate 520','bobby jones expressway','palmetto parkway','gordon highway','us 78','washington road','wrightsboro road','riverwatch parkway','wheeler road','walton way','deans bridge road','peach orchard road','13th street bridge','savannah river','downtown','broad street','olde town','greene street','reynolds street','the common','laney walker','medical district','summerville','the hill','harrisburg','canal','forest hills','national hills','west augusta','martinez','evans','columbia county','grovetown','south augusta','hephzibah','blythe','north augusta','aiken','beech island','mall','fort eisenhower','cyber','signal','class cycles','orders','report date','contractors','residents','nurses','medical college','nuclear site','power plant','burke county','golf cart','paper mill','tractor plant','masters','tournament','golf course','helene','2024','ice','2014','tornado','hail','pollen','atlanta','columbia','athens','charlotte','savannah','charleston','jacksonville','raleigh','washington','dallas','fort meade','maryland','texas','arizona'],
}, BODY, FAQ)
