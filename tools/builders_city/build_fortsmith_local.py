import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Fort Smith, Arkansas','Car shipping on the Oklahoma line, where Interstate 40 meets Interstate 49 and the river turns west',
 ['Car shipping in Fort Smith starts at the Alma interchange, where the valley’s trucks stop for fuel. Ship Guy is a licensed auto transport broker with an office on South 6th Street downtown.',
  'We book vetted carriers across the river valley, from Van Buren to Greenwood and the Oklahoma side. We do not own the trucks.',
  'Interstate 40 runs along the north bank of the river through Van Buren and Alma. Interstate 49 leaves 40 at Alma and runs north to Fayetteville. Interstate 540 drops south from 40 into the city. Rogers Avenue carries it across town to Chaffee Crossing.',
  'This page covers the two interstates, the spur, downtown, the hills, and the new district on the post. It also covers the air base, the trucking headquarters, the plants, the colleges, the river, and the lanes.'],
 'Fort Smith at a glance',
 ['Most pickups happen within 1 to 3 days. Interstate 40 carries the Memphis-to-Oklahoma City carriers past the valley all day.',
  'Fayetteville, Tulsa, and Little Rock are same-day lanes. Oklahoma City is the same day too. Dallas, Memphis, Springfield, and Kansas City take a day. Houston and Denver take one to two.'],
 'Tell us the neighborhood. Downtown, Belle Grove, and Fianna Hills need a meeting spot. Chaffee Crossing, the north side, and Van Buren usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 40, 49, 540, Rogers Avenue, and the Alma Interchange',
 prose(
  L('Fort Smith sits a few miles south of the one interstate that crosses the state. The spur is the ramp down to it.'),
  P('Interstate 40 runs along the river through Van Buren and Alma. It connects Little Rock and Oklahoma City. Interstate 49 begins at Alma and climbs north through the Boston Mountains to Fayetteville. The Alma interchange and the truck stops around it are the meeting spot for the whole valley.'),
  P('Interstate 540 leaves 40 at Van Buren and crosses the river. It runs south through the city to Rogers Avenue and Zero Street. US 71 is Rogers Avenue and Towson Avenue, the long retail strips across town. US 64 is Garrison Avenue downtown, and it crosses the river into Oklahoma on the old bridge.'),
  P('Highway 22 runs east to Chaffee Crossing and Barling. US 71 runs south to Greenwood. The carriers come off 540 at Grand Avenue, Rogers Avenue, and Zero Street. The lots along Rogers Avenue and at the Alma truck stops are the usual meeting spots. No road in the valley charges a toll.'),
  P('Our office sits on South 6th Street downtown, a block off Garrison Avenue.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, Belle Grove, Fianna Hills, Chaffee Crossing, and Van Buren',
 prose(
  L('Fort Smith is an old river town, a line of hills, and a new district on the post. Each one parks differently.'),
  P('Garrison Avenue is one of the widest downtown streets in the country. A trailer can stop on it. The Belle Grove blocks behind it are narrow and historic. The driver meets you on Garrison or at a lot by the river. The old fort and the park sit at the end of the avenue.'),
  P('Fianna Hills and the south side climb on winding streets with low trees. The driver stays on Rogers Avenue or Highway 71. The north side along Grand Avenue and the blocks off Towson are flat grids. The truck often reaches the curb.'),
  P('Chaffee Crossing is the new district on the old post. It has wide streets, the medical college, and room everywhere. Barling and Greenwood are suburban grids where the curb usually works. Van Buren across the river has a historic Main Street and open grids beyond it.'),
  P('The Oklahoma side is ten minutes away. Pocola, Moffett, and Roland ride the same carriers, and the casino lot in Pocola works for a handoff. The plants along the river and the trucking terminals have truck entrances of their own.'),
 )))

ROUTES=[("Fayetteville, AR","I-49 · ~60 mi","Same day","$130–$220"),("Tulsa, OK","I-40/US-64 · ~115 mi","Same day","$160–$260"),
 ("Little Rock, AR","I-40 · ~160 mi","Same day","$190–$300"),("Oklahoma City, OK","I-40 · ~180 mi","Same day","$200–$320"),
 ("Springfield, MO","I-49/US-60 · ~170 mi","1 day","$200–$320"),("Dallas, TX","US-71/US-75 · ~290 mi","1 day","$280–$410"),
 ("Memphis, TN","I-40 · ~300 mi","1 day","$290–$420"),("Kansas City, MO","I-49 · ~280 mi","1 day","$280–$410"),
 ("Houston, TX","US-71/US-59 · ~460 mi","1–2 days","$390–$560"),("Denver, CO","I-40/I-70 · ~800 mi","2 days","$590–$840")]
BODY.append(rate_table('Lanes &amp; Costs','Fort Smith Car Shipping Lanes and Estimated Costs',
 'The lanes that leave the river valley most, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a sedan that runs on an open trailer. Add roughly 10 to 25 percent for an SUV or pickup, and more for enclosed. The ice, the river, and the carriers free on your dates fix the final figure.',
 prose(
  P('Fort Smith prices like Fayetteville and Little Rock, because the same 40 and 49 carriers reach all three. Tulsa and Oklahoma City ride 40 west, and Dallas rides US 71 south through the Ouachitas.'),
  P('The Texas and Oklahoma lanes run full all year. The base brings in a new lane every time a training class rotates. The <a href="car-shipping-cost.html">cost guide</a> covers the rest of the math.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Air Base, the Trucking Headquarters, the Plants, and the Medical College',
 prose(
  L('Fort Smith relocates airmen, drivers, plant engineers, and medical students, and the base calendar is the newest one.'),
  P('The Air National Guard base at the airport became the training center for foreign fighter pilots. The first classes have arrived. Pilots and families from allied countries rotate in on class cycles. Fort Chaffee trains Guard units on cycles of its own. One car moves on the orders, and the family car comes with us.'),
  P('The gates stop the truck, so the handoff happens on Rogers Avenue or at Chaffee Crossing. The <a href="military-car-shipping.html">military</a> page covers the planning. Ship Guy is a private broker with no connection to either base.'),
  P('The trucking company headquartered in the city moves drivers, dispatchers, and office staff in from every state. The poultry plant, the baby-food plant, the pet-food plant, and the motor plant relocate engineers on program schedules. The records an employer needs for reimbursement come from us.'),
  P('The medical college at Chaffee Crossing brings students in each July and sends them out on rotations. The two hospitals bring in residents and nurses every summer. The university brings cars in each August. The campus lots work for the handoff, and an adult signs for a student car.'),
  P('Families move in from Oklahoma and Texas for the jobs, and the second car usually rides a truck. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side of a move.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Ice, Tornadoes, the River, and the Rally',
 prose(
  L('Fort Smith gets the ice from the north and the floods from the river. The carriers plan around both.'),
  P('Ice storms glaze 40 and the Boston Mountain grades a few times a decade. Nothing moves a loaded trailer on them. The carriers hold at the Alma truck stops until the sand trucks finish. A winter pickup can slide a day or two.'),
  P('Tornado season runs March through May. The 1996 tornado tore through downtown and Van Buren, and the valley remembers. A warning holds the driver until the all-clear. Forecast hail moves the window.'),
  P('The river rose to a record in 2019. The riverfront, the port, and the Oklahoma bottoms went under water. A pickup near the river moves up to Rogers Avenue until the river drops. Summer runs past one hundred degrees, and the loading hour moves to early morning.'),
  P('The motorcycle rally closes Garrison Avenue for a weekend in May. The rodeo fills the fairgrounds a few weeks later. The riverfront festival does the same in summer. We move a downtown pickup to another day for each.'),
 )+chips(["Downtown","Garrison Avenue","Belle Grove","Riverfront","North Side","Grand Avenue","Towson Avenue","Rogers Avenue","Fianna Hills","Rye Hill","Chaffee Crossing","Zero Street","Barling","Greenwood","Van Buren","Alma","Lavaca","Charleston","Pocola","Moffett","Roland","Sallisaw","Poteau","Ozark","Booneville","Paris"])
 +NOTE('Serving Fort Smith and the whole river valley, both sides of the line. Tell us the neighborhood, the gate, and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Fort Smith?',
 prose(
  L('Open is how the valley ships, and the 40 and 49 lanes are priced for it.'),
  P('An enclosed trailer keeps the hail, the dust, and attention off the car. The garages in Fianna Hills and Chaffee Crossing book enclosed trailers. So does a car headed to Texas for a new post.'),
  P('A work truck or a daily driver rides open without trouble. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain what the roof is for.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff on Rogers Avenue or at the Alma truck stops, and a delivery. The ice picks the day in winter.'),
  P('Approve the price, and a carrier already on 40 or 49 takes the booking. We name the spot the same day. The driver looks the car over with you and writes its condition on a Bill of Lading. Both sign, and that sheet rides along to the delivery check.'),
 )+ULI([
  "Take everything personal out of the car",
  "Leave the gas at about a quarter tank",
  "Photograph the car before pickup, especially after hail",
  "Leave a working key and tell us about any mechanical issue",
  "Shut off any aftermarket alarm",
  "Near either base, plan to meet the truck outside the gate on Rogers Avenue",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages take it from there.'))))

BODY.append(sec('Why Ship Guy','Why Fort Smith Drivers Choose Ship Guy',
 prose(
  L('We work 40 and 49 every day and plan around the ice, the river, and the class cycles.'),
  P('Ship Guy’s FMCSA brokerage authority is active. The $75,000 surety bond behind it is on file. Both are searchable on the federal register. Our office is on South 6th Street downtown.'),
  P('One coordinator handles your move from the first call to the delivery signature. Open, enclosed, and expedited transport are all on offer, and the <a href="services.html">services</a> page lists each one.'),
 ), alt=True))

BODY.append(office('Fort Smith','51 S 6th St #321','Fort Smith, AR 72901','+14795529711','(479) 552-9711','CT',
 '51+S+6th+St+%23321,+Fort+Smith,+AR+72901','Visit Us','Find Ship Guy in Fort Smith',
 'Our office is on South 6th Street downtown, a block off Garrison Avenue and minutes from Interstate 540.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5002.032794825495!2d-94.4268449!3d35.385324000000004!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x87ca4d359bb299bf%3A0x97a377cef148159d!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792153813407!5m2!1sen!2sus'))

FAQ=[
 ("Do you handle a PCS move to the air base or Fort Chaffee?","Yes, on every class cycle. The Guard base at the airport trains fighter pilots from allied countries, and Fort Chaffee trains Guard units. One car moves on the orders, and the family car comes with us. The gates stop the truck, so the handoff happens on Rogers Avenue or at Chaffee Crossing. Ship Guy is a private broker with no connection to either base."),
 ("How much does it cost to ship a car from Fort Smith to Dallas or Tulsa?","Dallas runs two hundred eighty to four hundred ten dollars for a sedan. That is about two hundred ninety miles down US 71 and 75. Tulsa runs one hundred sixty to two hundred sixty. That is about one hundred fifteen miles on 40 and US 64. SUVs and pickups add 10 to 25 percent."),
 ("Can you ship a car to or from the Oklahoma side of the line?","Yes, and it prices the same. Pocola, Moffett, Roland, and Sallisaw ride the same carriers as Fort Smith. The casino lot in Pocola and the Alma truck stops work for a handoff. The state line changes the paperwork, not the price."),
 ("Do you ship cars for drivers hired at the trucking headquarters?","Yes, all year. New drivers and office staff arrive from every state, and many ship a personal car behind the move. The terminals have truck entrances, and a handoff in the yard works when the company allows it. We provide the records a reimbursed move needs."),
 ("What happens if an ice storm hits on my pickup day?","The carriers hold at the Alma truck stops until the sand trucks finish. Glazed pavement shuts 40 and the Boston Mountain grades for a day or two. A winter pickup can lose a day or two, and we call before it does."),
 ("Can the carrier come into Belle Grove or Fianna Hills?","Usually not. Belle Grove is narrow and historic, and Fianna Hills winds up the hill under low trees. The driver meets you on Garrison Avenue, on Rogers Avenue, or at a lot by the river. Chaffee Crossing, the north side, and Van Buren usually allow the curb."),
 ("Do you ship cars for students at the medical college or the university?","Yes. The medical college brings students in each July, and the university brings cars in each August. The campus lots at Chaffee Crossing and on Grand Avenue work for the handoff. An adult signs for a student car at pickup."),
 ("What happens if the river floods on my pickup day?","Up the hill. The 2019 flood left the riverfront, the port, and the Oklahoma bottoms under water for weeks. The handoff moves to Rogers Avenue or Chaffee Crossing until the river drops."),
 ("Can you ship a car that does not run from Fort Smith?","Yes. The carrier we send brings a winch, and the slower loading is in the quote. Pick a flat, open spot, which usually means a lot on Rogers Avenue or at Alma. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Fort Smith car shipping quote?","Both addresses, with the neighborhood and the gate on this end. The year, make, and model. Whether it runs. Open or enclosed. Your dates, with the class cycle or the ice in mind. That is a complete Fort Smith request."),
]
BODY.append(faq_section(FAQ,'Fort Smith FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Fort Smith?','A price takes about two minutes on the form above. Tell us the neighborhood and your dates, and a carrier already on 40 takes it from there.','+14795529711','(479) 552-9711','Get your free Fort Smith quote'))

build({
 'slug':'auto-transport-fort-smith-arkansas',
 'title':'Car Shipping in Fort Smith, AR — Auto Transport | Ship Guy',
 'meta':'Car shipping in Fort Smith, AR where Interstate 40 meets 49 on the Oklahoma line. Air base and Fort Chaffee second vehicles, Garrison Avenue and Rogers Avenue meeting spots, Chaffee Crossing curbside, trucking and plant relocations, the Oklahoma side, ice storm and river-flood planning. Local office on South 6th Street downtown. Free quote.',
 'h1':'Car Shipping in<br>Fort Smith, <span class="accent">Arkansas</span>',
 'lede':'Open, enclosed, and expedited auto transport across the river valley, both sides of the line, planned around 40, 49, the ice, and the river.',
 'tel':'+14795529711','disp':'(479) 552-9711','brand':'Fort Smith','keyword':'car shipping in fort smith',
 'localterms':['fort smith','interstate 40','interstate 49','interstate 540','us 71','us 64','highway 22','rogers avenue','towson avenue','garrison avenue','grand avenue','zero street','alma','interchange','truck stops','boston mountains','downtown','belle grove','riverfront','old fort','north side','fianna hills','rye hill','chaffee crossing','barling','greenwood','van buren','pocola','moffett','roland','sallisaw','poteau','oklahoma','casino','air base','guard','fighter pilots','fort chaffee','class cycles','orders','trucking company','terminals','poultry plant','baby-food','pet-food','motor plant','medical college','hospitals','residents','university','port','ice storms','tornado','1996','hail','river','flood','2019','rally','rodeo','festival','fayetteville','tulsa','little rock','oklahoma city','springfield','dallas','memphis','kansas city','houston','denver','texas'],
}, BODY, FAQ)
