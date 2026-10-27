import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Owensboro, Kentucky','Car shipping on the Ohio River, where US 60 meets US 231 and the new interstate runs south to Bowling Green',
 ['Car shipping in Owensboro runs off the US 60 bypass and the two bridges across the Ohio. Ship Guy is a licensed auto transport broker with an office on Sweeney Street off Frederica.',
  'We arrange vetted carriers across Daviess County, from the riverfront to Whitesville and across the river to Rockport. The trucks belong to the carriers we vet.',
  'Interstate 165 begins at the bypass and runs south to Bowling Green and 65. US 60 runs east to Louisville and west to Henderson and 69. US 231 crosses the river on the Natcher Bridge and reaches 64 in Indiana. The Audubon Parkway runs west toward Henderson.',
  'This page covers the bypass, the bridges, downtown, the Frederica corridor, the east side, and the river towns. It also covers the hospital, the distilleries, the plants, the barbecue festival, the river, and the lanes.'],
 'Owensboro at a glance',
 ['Most pickups happen within 1 to 3 days. Carriers running 64 across Indiana drop down 231 for a load. The 65 trucks come up the new interstate.',
  'Evansville is forty minutes, and Louisville is two hours. Nashville, Indianapolis, Lexington, and St. Louis are a same-day haul. Cincinnati, Chicago, and Atlanta take a day. Dallas and Florida take two, and the coasts take three to five.'],
 'Tell us the side of the bypass. Downtown and the old streets off Frederica need a meeting spot. The east side, the southeast subdivisions, and Philpot usually allow the curb.'))

BODY.append(sec('The Roads','The US 60 Bypass, Interstate 165, the Two Bridges, the Audubon Parkway, and Frederica Street',
 prose(
  L('Owensboro sits between two interstates without touching either, and the bypass is how the carriers reach it.'),
  P('The US 60 bypass is the Wendell Ford Expressway, a four-lane loop around the south and east sides. Every carrier coming into Owensboro uses it. Interstate 165 begins at the bypass on the south side. It runs seventy miles to Bowling Green and 65. Nashville and Atlanta carriers come up that road.'),
  P('US 231 crosses the Ohio on the Natcher Bridge east of town. It reaches Interstate 64 in Indiana in twenty minutes. The old blue bridge downtown carries local traffic to Rockport. US 60 runs west to Henderson and Interstate 69, and east to Hardinsburg and Louisville. The Audubon Parkway is the free four-lane west to Henderson.'),
  P('Frederica Street is the main strip, from the riverfront south through the retail corridor to the bypass. Parrish Avenue crosses the city east and west. Carter Road and Scherm Road carry the west side. Highway 54 runs east to Whitesville and the subdivisions. Highway 81 and 56 reach the farm towns to the southwest. Veterans Boulevard runs the riverfront.'),
  P('The carriers come off the bypass at Frederica, at Highway 54, and at Carter Road. The mall on Frederica, the sportscenter, and the convention center on the riverfront have the usual meeting lots. No road in Daviess County charges a toll. The bridges and the parkway are free.'),
  P('Our office is on Sweeney Street off Frederica, a mile south of the riverfront.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown and the Riverfront, the Frederica Corridor, the Old West Side, the East Side, the Southeast, and the River Towns',
 prose(
  L('Owensboro is a river town with a rebuilt downtown and subdivisions running east along Highway 54.'),
  P('Downtown sits on the river around the convention center, the bluegrass museum, and the park. The riverfront streets fill on festival weekends and summer Fridays. The driver meets you at the convention center lots or on Veterans Boulevard. The old grids between downtown and Parrish Avenue have narrow streets with alleys. The handoff moves to Frederica.'),
  P('The Frederica corridor from Parrish to the bypass is the retail strip. It has the mall, the shopping centers, and the college. There is room everywhere. The old west side along Carter Road and the streets off Parrish are postwar grids. The curb works on most blocks, and a lot on Carter works for the rest.'),
  P('The east side along Highway 54 and the southeast off Pleasant Valley are the growth side. The new hospital and the subdivisions run out past the bypass. The streets are wide, and the truck reaches the curb. Philpot and Whitesville beyond them are farm towns with lots on the highway.'),
  P('Rockport across the river in Indiana is a small town on the bluff. The driver meets you at the bridge. Hawesville and Lewisport downriver have the aluminum plants and lots on US 60. Calhoun and Livermore to the southwest sit on the Green River. Henderson sits thirty minutes west on the parkway. All of them price the same as Owensboro.'),
 )))

ROUTES=[("Evansville, IN","US-231/I-64 · ~40 mi","Same day","$120–$200"),("Louisville, KY","US-60/I-64 · ~110 mi","Same day","$160–$260"),
 ("Nashville, TN","I-165/I-65 · ~150 mi","Same day","$190–$300"),("Lexington, KY","I-64 · ~175 mi","Same day","$210–$320"),
 ("Indianapolis, IN","I-64/I-69 · ~180 mi","Same day","$210–$320"),("St. Louis, MO","I-64 · ~200 mi","Same day","$220–$330"),
 ("Cincinnati, OH","I-64/I-71 · ~230 mi","1 day","$240–$360"),("Chicago, IL","I-64/I-65 · ~320 mi","1 day","$300–$440"),
 ("Atlanta, GA","I-65/I-24/I-75 · ~380 mi","1 day","$350–$500"),("Dallas, TX","I-64/I-44 · ~690 mi","2 days","$520–$750")]
BODY.append(rate_table('Lanes &amp; Costs','Owensboro Car Shipping Lanes and Estimated Costs',
 'The lanes Daviess County cars take most, with estimated open-trailer ranges. Your exact route prices on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates leaving Owensboro, sedan in running order, open trailer. SUVs and pickups add 10 to 25 percent, and an enclosed trailer adds more. Fuel, the season, and the carriers free on your dates decide the final figure.',
 prose(
  P('Owensboro prices a few dollars over Evansville on most lanes. The carriers leave the interstate to reach it. The Louisville and Nashville lanes run daily and price the closest to the interstate towns. The Chicago lane rides 64 and 65 and runs lighter.'),
  P('Florida and Texas climb in October and fall in April with the snowbirds. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Hospital, the Distilleries, the Plants, the Mortgage Office, the Campuses, and the Pipeline Companies',
 prose(
  L('Owensboro relocates nurses, distillers, plant engineers, and loan processors. The hospital moves more people than anyone.'),
  P('The regional hospital on the east side is the largest employer in the county. It brings in nurses on contracts all year and physicians with a closing date and a second car. The clinics across the city do the same. We supply the paperwork a reimbursed move needs.'),
  P('The distilleries downtown and on the west side bring in distillers and managers from Louisville and Scotland. The bottling plant moves staff the same way. The sauce plant, the frame plant, and the auto-parts plant relocate engineers on program schedules. The aluminum mills in Lewisport and Hawesville move operators between plants.'),
  P('The mortgage office on the east side hires loan processors by the hundred. It moves managers in from every state. The two pipeline companies headquartered in town relocate engineers on their own calendars. The two colleges on Frederica and the community college bring cars in each August. A parent ships the car, and an adult signs at a campus lot.'),
  P('Fort Campbell sits two hours southwest, and some families on orders settle in Owensboro. The orders pay for one car, and the family’s other car rides with us. Ship Guy is a private broker with no link to the post. The <a href="military-car-shipping.html">military</a> page walks through the timing. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Barbecue Festival, ROMP, Friday After 5, the Air Show, the River, and the 2000 Tornado',
 prose(
  L('Owensboro runs on a May barbecue weekend, a June bluegrass festival, and a river that rises every spring.'),
  P('The barbecue festival fills downtown on the second weekend of May. The cooking teams set up on the riverfront streets on Friday. The streets stay closed through Saturday night. A downtown pickup that weekend moves to the mall or to Carter Road. The bluegrass festival fills the park on the south side for four days in June. Highway 56 backs up each evening.'),
  P('Friday After 5 fills the riverfront every Friday evening from May through August. The air show fills the riverfront and the bridges for a September weekend. The Fourth of July does the same. The Christmas parade closes Frederica on a Saturday in November. A handoff near any of them moves to the daytime or to another day.'),
  P('The Ohio River rises every spring. The 1937 flood covered most of the city, and the 1997 flood closed the riverfront again. The levee holds. The river still closes Veterans Boulevard and the low roads toward Rockport in a wet March. A pickup there moves up Frederica for a day.'),
  P('The January 2000 tornado crossed the city from the west side through the hospital district. The sirens sound a few times each spring. A pickup waits for the warning to lift. Ice is the winter problem. The 2009 storm took the power out across western Kentucky for a week. Snow is light, and the carriers rarely park. Summer heat and humidity move the loading hour to the morning.'),
 )+chips(["Downtown","Riverfront","Convention Center","Smothers Park","Bluegrass Museum","Veterans Boulevard","Old Grid","Frederica","Parrish Avenue","Mall","Sportscenter","West Side","Carter Road","Scherm Road","Wesleyan Park","Southtown","East Side","Highway 54","Fairview","Pleasant Valley","Hospital District","Southeast","Thruston","Philpot","Whitesville","Masonville","Sorgho","Maceo","Rockport","Hawesville","Lewisport","Calhoun","Livermore","Henderson"])
 +NOTE('Serving Owensboro and all of Daviess County, riverfront block or new subdivision. Tell us the side of the bypass and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Owensboro?',
 prose(
  L('Open trailers move most Daviess County cars, and the lane table is priced for one.'),
  P('An enclosed trailer keeps a car out of the salt, the gravel, and the rain. The collectors who fill the riverfront on cruise nights book one for the show cars. Parents sending a new car to a student book one too.'),
  P('A daily driver or a farm truck goes open and arrives none the worse. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages set out the difference.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A number, a handoff at the mall or the convention center lots, and a signature at delivery. Most moves fit inside a week.'),
  P('Give the number a yes, and we pair the car with a carrier already working 64 or 65. The meeting lot and the window come back within hours. The driver walks the car at the handoff and notes every existing mark on the Bill of Lading. Both of you sign, and the sheet settles the delivery.'),
 )+ULI([
  "Remove everything personal from the cabin and the trunk",
  "Leave the fuel at about a quarter tank",
  "Take dated photos of every panel and the mileage",
  "One working key goes to the driver, with a word about any fault",
  "Kill any aftermarket alarm before the handoff",
  "Downtown or in the old grid, meet the truck at the convention center lots or on Frederica",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Owensboro Drivers Choose Ship Guy',
 prose(
  L('We pull the carriers off 64 and 65 and onto the bypass. We plan around the barbecue weekend, the river, and the tornado season.'),
  P('Ship Guy holds active FMCSA brokerage authority and a $75,000 surety bond, both on the federal register. Our office is on Sweeney Street off Frederica.'),
  P('Whoever prices the move is whoever you call until the car is signed for. Open, enclosed, and expedited transport are on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Owensboro','1727 Sweeney St #355','Owensboro, KY 42303','+12705146233','(270) 514-6233','CT',
 '1727+Sweeney+St+%23355,+Owensboro,+KY+42303','Visit Us','Find Ship Guy in Owensboro',
 'Our office is on Sweeney Street off Frederica, a mile south of the riverfront.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4850.566128163759!2d-87.1041036!3d37.7594345!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x886fbba292080149%3A0x8dc45a77124bdad2!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793024933533!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Owensboro to Louisville or Nashville?","Louisville runs one hundred sixty to two hundred sixty dollars for a sedan. That is about one hundred ten miles east on 60 and 64. Nashville runs one hundred ninety to three hundred, about one hundred fifty miles down 165 and 65. Evansville is forty minutes and prices the lowest of all. An SUV or pickup adds 10 to 25 percent. All three lanes run daily."),
 ("Can the carrier come to my street downtown or in the old grid?","Usually not. The riverfront streets close for the festivals. The old grid between downtown and Parrish has narrow streets with alleys. The driver meets you at the convention center lots, on Veterans Boulevard, or on Frederica. The east side, the southeast subdivisions, and Philpot usually allow the curb."),
 ("Do you ship cars for people relocating to the hospital or the distilleries?","Yes, all year. The regional hospital brings in nurses, residents, and physicians every month. The distilleries and the bottling plant move distillers and managers from Louisville and overseas. Many ship a second car behind the move. The handoff works at the hospital lots or the mall. We provide the paperwork a reimbursed move needs."),
 ("Does the barbecue festival affect my pickup?","Downtown, yes. The cooking teams take over the riverfront streets on the second weekend of May. They stay closed until Saturday night. We move a downtown pickup that weekend to the mall or to Carter Road. The rest of the county runs normally. The bluegrass festival in June does the same thing to Highway 56."),
 ("Can you ship a car to or from Rockport, Hawesville, or Henderson?","Yes, and all three price the same as Owensboro. Rockport rides the same carriers across the bridge, and the handoff happens at the bridge or in town. Hawesville and Lewisport ride them off US 60 to the east. Henderson rides them off the parkway and 69. Send the full address for a new subdivision."),
 ("Which bridge does the carrier use?","The Natcher Bridge on the bypass. It is a four-lane bridge built for trucks, and it puts the carrier on 64 in twenty minutes. The old blue bridge downtown is narrow and carries local traffic. A carrier coming from Louisville or Nashville never crosses the river at all."),
 ("What happens if the river or a tornado warning hits on my pickup day?","In a wet March the river closes Veterans Boulevard and the low roads toward Rockport. A pickup there moves up Frederica for a day. A tornado warning pauses the loading until it expires, and the sirens are a spring fixture here. The driver waits it out and nearly always finishes the same day. An ice storm costs a day, and you hear from us before it does."),
 ("Can you ship a car that does not run from Owensboro?","Yes. A carrier with a winch is sent, and the loading time is in the quote from the start. The mall lot on Frederica or the sportscenter lot gives the driver level ground to work from. Let us know whether it rolls, steers, and stops."),
 ("Can you time delivery to a student move at the colleges?","Yes. The two colleges on Frederica and the community college take cars in each August. They send them home in May. Parents do most of the booking, and someone over eighteen signs at a campus lot. The delivery window tracks the move-in date."),
 ("What do you need for an Owensboro car shipping quote?","Pickup and delivery addresses, with the side of the bypass or the river town. Year, make, model. Whether it drives. Open or enclosed. The week you want it gone. With those five, the Owensboro quote comes back within the day."),
]
BODY.append(faq_section(FAQ,'Owensboro FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Owensboro?','Two minutes on the form above prices your lane. Send the side of the bypass and your dates, and a carrier already on 64 takes it.','+12705146233','(270) 514-6233','Get your free Owensboro quote'))

build({
 'slug':'auto-transport-owensboro-kentucky',
 'title':'Car Shipping in Owensboro, KY — Auto Transport | Ship Guy',
 'meta':'Car shipping in Owensboro, KY on the Ohio River, between Interstate 64 and the new Interstate 165. Hospital and distillery relocations, downtown and old-grid meeting spots, east side and Highway 54 curbside pickups, Rockport and Henderson, the barbecue festival, the river, and the tornado season. Local office on Sweeney Street off Frederica. Free quote.',
 'h1':'Car Shipping in<br>Owensboro, <span class="accent">Kentucky</span>',
 'lede':'Open, enclosed, and expedited auto transport across Daviess County, planned around the bypass, the bridges, the barbecue weekend, and the river.',
 'tel':'+12705146233','disp':'(270) 514-6233','brand':'Owensboro','keyword':'car shipping in owensboro',
 'localterms':['owensboro','ohio river','daviess county','us 60','bypass','wendell ford','interstate 165','bowling green','us 231','natcher bridge','blue bridge','rockport','interstate 64','audubon parkway','henderson','interstate 69','frederica','parrish avenue','carter road','scherm road','highway 54','highway 81','highway 56','veterans boulevard','downtown','riverfront','convention center','bluegrass museum','park','old grid','mall','sportscenter','college','west side','east side','fairview','pleasant valley','hospital','southeast','philpot','whitesville','hawesville','lewisport','aluminum','calhoun','livermore','green river','nurses','physicians','distilleries','distillers','bottling plant','sauce plant','frame plant','auto-parts','mortgage office','loan processors','pipeline companies','colleges','community college','fort campbell','orders','barbecue festival','cooking teams','bluegrass festival','friday after 5','air show','fourth of july','christmas parade','1937 flood','1997 flood','levee','2000 tornado','sirens','ice','2009','humidity','evansville','louisville','nashville','lexington','indianapolis','st. louis','cincinnati','chicago','atlanta','dallas','florida','hardinsburg'],
}, BODY, FAQ)
