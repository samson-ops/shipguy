import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Springfield, Missouri','Car shipping at the gateway to the Ozarks, on the Interstate 44 trucking lane',
 ['Car shipping in Springfield is easier than its size suggests, because trucking is a major local industry. Ship Guy is a licensed auto transport broker with an office on South Avenue downtown.',
  'We book vetted carriers across the Ozarks, from Nixa and Ozark to Republic, Willard, and Branson. We do not own the trucks.',
  'Interstate 44 runs through the north side between St. Louis and Tulsa. US 65 runs south to Branson and north to the lake. Route 13 is the direct road to Kansas City, and US 60 loops the south side.',
  'This page covers the interstate and the highways, the trucking yards, and the university and the hospitals. It also covers Branson and the lakes, Fort Leonard Wood, the ice storms, and the lanes.'],
 'Springfield at a glance',
 ['Most pickups happen within 1 to 3 days. Carriers based here and carriers passing through on 44 give Springfield more trucks than most cities its size.',
  'Tulsa, Kansas City, Joplin, and Fayetteville are same-day lanes. St. Louis, Little Rock, and Oklahoma City take a day. Dallas and Chicago run one to two, and Florida runs three.'],
 'Tell us the neighborhood. Rountree, Phelps Grove, and the campus blocks need a meeting spot. Nixa, Ozark, and the south side usually meet the truck at the curb.'))

BODY.append(sec('The Roads','Interstate 44, US 65, Route 13, and the James River Freeway',
 prose(
  L('Springfield sits on the lane that carries the Southwest to the Midwest. The trucks that run it are parked here.'),
  P('Interstate 44 runs along the north side of the city. It reaches Rolla and St. Louis to the east and Joplin and Tulsa to the west. One of the largest trucking companies in the country is based beside it. The carriers that haul cars share the same yards and fuel stops.'),
  P('US 65 runs south to Branson and Table Rock Lake and north to the Lake of the Ozarks. Route 13 heads northwest to Clinton and Kansas City, the fastest road between the two. US 60 is the James River Freeway across the south side.'),
  P('Glenstone Avenue, Kansas Expressway, Chestnut Expressway, and Battlefield Road are the surface roads carriers use across the city. None of the Springfield roads charges a toll.'),
  P('Our office sits on South Avenue downtown, a block from the square.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The University, the Hospitals, the Retailer, and the Trucking Yards',
 prose(
  L('Springfield relocates people on the university calendar, two hospital systems, and the headquarters that grew up here.'),
  P('The state university on National Avenue brings cars in each August and sends them home each May. The private universities nearby do the same. Campus streets are tight, so the driver meets you at a lot on Glenstone or near the campus. An adult signs for a student car.'),
  P('The two hospital systems are the referral centers for the whole Ozarks. They bring in residents and nurses every summer. The handoff happens on National Avenue or Sunshine Street rather than in a hospital garage.'),
  P('The outdoor-retailer headquarters, the auto-parts headquarters, and the trucking companies transfer staff in on start dates. If the employer reimburses the move, the documentation it needs comes from us.'),
  P('The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side of a relocation.'),
 )))

ROUTES=[("Joplin, MO","I-44 · ~70 mi","Same day","$150–$250"),("Fayetteville, AR","US-60/I-49 · ~120 mi","Same day","$180–$290"),
 ("Kansas City, MO","Route 13/I-49 · ~165 mi","Same day","$200–$320"),("Tulsa, OK","I-44 · ~180 mi","Same day","$210–$320"),
 ("St. Louis, MO","I-44 · ~215 mi","Same day","$230–$350"),("Little Rock, AR","US-65 · ~250 mi","1 day","$250–$370"),
 ("Oklahoma City, OK","I-44 · ~280 mi","1 day","$260–$390"),("Dallas, TX","I-44/US-75 · ~440 mi","1 day","$390–$550"),
 ("Chicago, IL","I-44/I-55 · ~500 mi","1–2 days","$420–$600"),("Orlando, FL","US-60/I-24/I-75 · ~1,150 mi","3 days","$820–$1,150")]
BODY.append(rate_table('Lanes &amp; Costs','Springfield Car Shipping Lanes and Estimated Costs',
 'The lanes Springfield books most, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a sedan that runs, on an open trailer. SUVs and pickups run about 10 to 25 percent higher, enclosed higher still. Ice season and the carriers free on your dates set the final figure.',
 prose(
  P('Joplin and Tulsa ride 44 west and St. Louis rides it east. All three price like local trips. Route 13 puts Kansas City under three hours.'),
  P('Dallas rides 44 to Oklahoma and US 75 south, and the Texas lane runs every week. The <a href="car-shipping-cost.html">cost guide</a> explains the rest of the number.'),
 ), alt=True))

BODY.append(sec('Branson &amp; the Lakes','Table Rock, the Strip, the Lake of the Ozarks, and the Second Homes',
 prose(
  L('Springfield is the carrier hub for a lake country that fills with second-home owners every spring.'),
  P('Branson sits forty miles south on US 65, and its strip crawls from spring through the holiday shows. The driver meets you in Hollister or at a highway lot rather than on the strip. Table Rock Lake and the lake roads around it are narrow and steep.'),
  P('The Lake of the Ozarks sits ninety minutes north, and its shoreline roads are the same. The handoff happens in Osage Beach or Camdenton. Lake pickups run 2 to 4 days because the carrier detours off the interstate.'),
  P('Retirees in Branson and the lake towns ship cars to Florida and Arizona each fall. The cars come home each spring. Our <a href="snowbird-car-shipping.html">snowbird</a> page has the planning tips.'),
 ), alt=True))

BODY.append(sec('The Post &amp; the Neighborhoods','Fort Leonard Wood, the Campus Blocks, and the South Side',
 prose(
  L('An Army post sits ninety miles up the interstate, and its families route through Springfield all year.'),
  P('The post near Rolla trains soldiers on class cycles, and families arrive and leave constantly. Orders typically cover one vehicle, and the other one ships with us. The gate is controlled, so the meeting point is St. Robert or Waynesville. Ship Guy is a private broker with no connection to the post. The <a href="military-car-shipping.html">military</a> page covers the planning.'),
  P('Inside the city, Rountree, Phelps Grove, and the campus blocks have narrow streets with cars on both curbs. Downtown and the historic district on Commercial Street run on street parking. The driver meets you on National, Glenstone, or at a lot by Chestnut Expressway.'),
  P('The south side, Nixa, Ozark, Republic, and Battlefield are wide grids where the truck reaches the curb. The gated golf additions on the east side meet the truck at the gate. Willard and Strafford schedule on 44.'),
 )))

BODY.append(sec('The Weather','Ice Storms, Tornadoes, and the Flash Floods',
 prose(
  L('The Ozarks get ice the way the lake cities get snow. Ice is the one that stops a truck.'),
  P('Ice storms have shut the city for a week at a time. Interstate 44 closes to trucks until the sand trucks finish. A winter pickup can lose a day or two. Expect a call from us as soon as the forecast changes the plan.'),
  P('Tornado watches run from March into June, and the region remembers Joplin. When a warning is issued, the driver pulls off and waits. Hail hurts a parked car more than wind does. When it is in the forecast, we shift the window.'),
  P('Flash floods close the low crossings after a heavy rain. The James River runs over its banks a few times a year. Summer heat moves the loading hour earlier.'),
 )+chips(["Downtown","Commercial Street","Rountree","Phelps Grove","University Heights","Midtown","Delaware","Doling","Southern Hills","Galloway","Brentwood","Millwood","Highland Springs","Nixa","Ozark","Republic","Battlefield","Willard","Strafford","Rogersville","Branson","Hollister","Joplin","Lebanon","Osage Beach","Camdenton"])
 +NOTE('Serving Greene, Christian, Taney, and Webster Counties and the lake towns. Tell us the neighborhood and whether the car runs.'), alt=True))

BODY.append(sec('Your Options','Open or Enclosed in Springfield?',
 prose(
  L('Open is how most Springfield cars travel, and the 44 lane is quoted on that basis.'),
  P('An enclosed trailer keeps ice, hail, and attention off the car. The garages in Millwood and Highland Springs book enclosed trailers. So do the collector cars headed to the lake.'),
  P('A daily driver has no need of a roof for the trip. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain the difference in cost and cover.'),
 )))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a loading near 44 or Glenstone, and a delivery. Ice has a say in the timing.'),
  P('Once you accept the price, a carrier already on 44 is assigned and the spot is set. You and the driver go over the car at the spot. Its condition goes on a Bill of Lading. Both sign it. At delivery the car is checked against that sheet.'),
 )+ULI([
  "Clear out anything personal",
  "A quarter tank of fuel is plenty",
  "Photograph every panel before pickup, especially after hail",
  "Leave a key that works and tell us about mechanical issues",
  "Switch off the aftermarket alarm if it has one",
  "On a campus block or in Rountree, plan to meet the truck on National or Glenstone",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages cover each step in order.')), alt=True))

BODY.append(sec('Why Ship Guy','Why Springfield Drivers Choose Ship Guy',
 prose(
  L('We work the 44 lane every day and plan around the ice, the lake roads, and the post.'),
  P('Ship Guy’s FMCSA brokerage authority is active, and a $75,000 surety bond backs it. Both are on the public record. Our office is on South Avenue downtown.'),
  P('One coordinator handles your move from start to finish and can book open, enclosed, or expedited transport. See the <a href="services.html">services</a> page for the full list.'),
 )))

BODY.append(office('Springfield','313 South Ave Suite 300','Springfield, MO 65806','+14177543371','(417) 754-3371','CT',
 '313+South+Ave+Suite+300,+Springfield,+MO+65806','Visit Us','Find Ship Guy in Springfield',
 'Our office is on South Avenue downtown, a block from the square and minutes from Chestnut Expressway.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3922.4532983031477!2d-93.2926675!3d37.20774189999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x87cf63d54485098b%3A0x323cb22f11183b96!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792076148507!5m2!1sen!2sus'))

FAQ=[
 ("Why is Springfield easier to book than other cities its size?","Because trucking is one of its biggest industries. Carriers are based beside Interstate 44, and the cross-country trucks between St. Louis and Tulsa pass every day. A pickup in the city usually schedules in 1 to 3 days."),
 ("How much does it cost to ship a car from Springfield to Texas?","Count on three hundred ninety to five hundred fifty dollars for a sedan to Dallas. The route runs about four hundred forty miles on 44 and US 75. Houston is a hundred to a hundred fifty more. Figure 10 to 25 percent extra for an SUV or pickup."),
 ("Can you deliver to Branson or the lakes?","Yes, with a meeting spot. The Branson strip crawls in season, so the driver meets you in Hollister or at a highway lot. Table Rock and the Lake of the Ozarks have narrow shoreline roads, and the handoff happens in town. Lake pickups run 2 to 4 days."),
 ("Do you handle a PCS move to Fort Leonard Wood from Springfield?","Yes. The post trains on class cycles, so families move all year. Orders typically cover one vehicle, and the other one ships with us. The driver stops short of the gate and meets you in St. Robert or Waynesville. Ship Guy is a private broker with no connection to the post."),
 ("Can the carrier come to my house in Rountree or near the campus?","Rarely. The streets are narrow and cars line both curbs. The driver meets you on National Avenue, on Glenstone, or at a lot by Chestnut Expressway. Nixa, Ozark, Republic, and the south side usually allow a curbside pickup."),
 ("Can you ship a car for a Missouri State, Drury, or Evangel student?","Yes. The cars arrive each August and leave each May. The streets around campus are tight. The driver meets you at a lot on Glenstone or near the campus. An adult has to sign at pickup."),
 ("What happens if an ice storm hits on my pickup day?","The driver waits for 44 to reopen to trucks. An Ozarks ice storm can shut the city for days. A winter pickup can lose a day or two, and we call when the plan changes."),
 ("Do you ship cars for residents at the Springfield hospitals?","Yes, every summer. The two hospital systems are the referral centers for the whole region. They bring in residents and nurses from every state. The handoff happens on National Avenue or Sunshine Street rather than in a hospital garage."),
 ("Can you ship a car that does not run from Springfield?","Yes. The carrier brings a winch and the longer loading is figured into the quote. Pick a flat spot. Tell us if it rolls, steers, and brakes."),
 ("What do you need for a Springfield car shipping quote?","Pickup and delivery addresses, with the neighborhood or lake town. The year, make, and model. Does it run. Open or enclosed. The dates you have in mind. Nothing else is needed for a Springfield quote."),
]
BODY.append(faq_section(FAQ,'Springfield FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Springfield?','Get a price from the form above, then send the neighborhood and your dates. A carrier already running 44 takes it from there.','+14177543371','(417) 754-3371','Get your free Springfield quote'))

build({
 'slug':'auto-transport-springfield-missouri',
 'title':'Car Shipping in Springfield, MO — Auto Transport | Ship Guy',
 'meta':'Car shipping in Springfield, MO on the Interstate 44 trucking lane. Missouri State and hospital timing, Branson and lake handoffs, Fort Leonard Wood second vehicles, Rountree and campus meeting spots, ice-storm planning, the Dallas and St. Louis lanes. Local office on South Avenue. Free quote.',
 'h1':'Car Shipping in<br>Springfield, <span class="accent">Missouri</span>',
 'lede':'Open, enclosed, and expedited auto transport across the Ozarks, planned around the interstate, the lakes, and the ice.',
 'tel':'+14177543371','disp':'(417) 754-3371','brand':'Springfield','keyword':'car shipping in springfield',
 'localterms':['springfield','interstate 44','us 65','route 13','us 60','james river','glenstone','kansas expressway','chestnut expressway','battlefield road','national avenue','sunshine','south avenue','square','downtown','commercial street','rountree','phelps grove','campus','south side','millwood','highland springs','nixa','ozark','republic','battlefield','willard','strafford','branson','hollister','table rock','lake of the ozarks','osage beach','camdenton','trucking','state university','hospital','residents','outdoor-retailer','auto-parts','fort leonard wood','st. robert','waynesville','ice','tornado','joplin','hail','flash flood','tulsa','kansas city','st. louis','fayetteville','little rock','oklahoma city','dallas','chicago','orlando'],
}, BODY, FAQ)
