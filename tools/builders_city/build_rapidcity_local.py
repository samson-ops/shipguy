import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("2–5 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Rapid City, South Dakota','Car shipping at the edge of the Black Hills, where Interstate 90 carries the trucks and the Air Force base and the rally set the calendar',
 ['Car shipping in Rapid City runs on Interstate 90, the one freeway across the top of the plains. Ship Guy is a licensed auto transport broker with an office on St. Joseph Street downtown.',
  'We book vetted carriers across Rapid City, from the Gap to Rapid Valley and out to Box Elder. The carriers run their own trucks. Ship Guy carries the license and the bond.',
  'Interstate 90 runs along the north edge of the city between Sioux Falls and Billings. The 190 spur drops into downtown. Highway 16 climbs south into the Hills toward Rushmore and Custer. Highway 44 heads east to the Badlands. Highway 79 runs the foot of the Hills north and south.',
  'This page covers 90, the spur, the Gap, downtown, the Hills roads, and the grids. It also covers the base, the school, the hospital, the rally, the blizzards, the wind, and the hail.'],
 'Rapid City at a glance',
 ['Plan on 2 to 5 days for a pickup. Rapid City sits on the 90 lane between Minneapolis and Billings. The 90 carriers pass through two or three times a week. The pool is small, and the window stretches when the Hills roads close.',
  'Cheyenne, Billings, Bismarck, and Sioux Falls take a day on the truck. Denver and Omaha take a day too. Minneapolis and Salt Lake take one to two, and Kansas City takes two.'],
 'Tell us the neighborhood. Downtown, the Gap, the canyon roads, and the school blocks meet the truck on a main road. The grids east and north, Rapid Valley, Box Elder, and the subdivisions off 44 usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 90, the 190 Spur, Highway 16, Highway 44, Highway 79, Omaha Street, Haines Avenue, Mount Rushmore Road, and the Gap',
 prose(
  L('Rapid City is one interstate, one spur, and a web of two-lane roads into the mountains. A carrier stays on 90 and the flat roads and does not take the canyons.'),
  P('Interstate 90 runs along the north side from Wall and Box Elder to Sturgis and Spearfish. It is the only road a carrier uses between Sioux Falls and Billings. The 190 spur leaves 90 at exit 57 and drops straight into downtown as West Boulevard. Exits 59 and 61 serve the north grids and the mall. Exit 67 is Box Elder and the base gate. Highway 16 leaves downtown as Mount Rushmore Road and climbs south through the Gap into the Hills. A trailer does not follow it past the first grade in winter. Highway 44 runs east along Rapid Creek to Rapid Valley and on to the Badlands. Highway 79 runs north and south along the foot of the Hills.'),
  P('Omaha Street follows the creek through the middle of town and takes the east-west load. Haines Avenue and LaCrosse Street run north to 90. Main and St. Joseph are the one-way pair downtown with the bronze presidents on the corners. The Gap is the cut in the ridge where Omaha, West Main, and Jackson Boulevard squeeze through.'),
  P('The carriers come off 90 at exits 59 and 61. They meet at the mall lots and the big-box lots on LaCrosse. The lots at the civic center work outside an event. So do the lots along Omaha Street and the truck stops at exit 61 and exit 55. The airport is ten miles east on 44 for a fly-and-ship.'),
  P('Our office sits downtown on St. Joseph, a block off Main Street and a mile from SD Mines.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, West Boulevard, the Gap, the Canyon Roads, North Rapid, the East Side, Rapid Valley, Robbinsdale, Box Elder, and the Hills Towns',
 prose(
  L('Rapid City is a small downtown, flat grids north and east, and canyon roads climbing into the Hills. The truck meets the canyons on a main road and the grids at the curb.'),
  P('Downtown is a few blocks of brick along Main and St. Joseph, one-way streets with angled parking. The handoff happens at the civic center lots or on Omaha. West Boulevard is the old money district of big houses on wide streets. A short trailer reaches the curb. Past the Gap, the west side climbs to Canyon Lake and Skyline Drive on roads with no shoulders. A trailer stops on West Main or at the Canyon Lake lots.'),
  P('North Rapid is grids and small ranches across the creek, and the curb works. The east side along East North Street and Cambell is the same. Robbinsdale and the south side along Fifth Street are postwar grids with wide lots. The curb works nearly everywhere. Rapid Valley along 44 is subdivisions on open ground, and the truck comes to the house.'),
  P('Box Elder outside the base gate is apartments and new subdivisions built for airmen. The curb works on most of it. The Hills towns ship from the flat roads. Hill City, Keystone, Custer, and Hot Springs meet the truck on 16 or 79. Sturgis, Spearfish, and Deadwood meet it off 90. Wall is an hour east on 90 and meets at the exit.'),
  P('Box Elder, Rapid Valley, and Black Hawk ship with the same trucks and price as Rapid City. Spearfish and Sturgis add an hour on the truck. Pierre and the reservation towns add a day and a figure.'),
 )))

ROUTES=[("Cheyenne, WY","US-85/I-25 · ~310 mi","Same day","$300–$440"),("Billings, MT","I-90 · ~360 mi","Same day","$310–$450"),
 ("Bismarck, ND","US-85/I-94 · ~320 mi","Same day","$320–$460"),("Sioux Falls, SD","I-90 · ~350 mi","Same day","$330–$480"),
 ("Denver, CO","US-85/I-25 · ~390 mi","1 day","$360–$520"),("Omaha, NE","I-90/US-281/I-80 · ~525 mi","1 day","$430–$620"),
 ("Minneapolis, MN","I-90/I-35 · ~590 mi","1–2 days","$450–$650"),("Salt Lake City, UT","I-90/I-25/I-80 · ~725 mi","1–2 days","$520–$750"),
 ("Kansas City, MO","I-90/US-81/I-29 · ~700 mi","2 days","$520–$750"),("Phoenix, AZ","I-25/I-40/I-17 · ~1,230 mi","2–3 days","$800–$1,150")]
BODY.append(rate_table('Lanes &amp; Costs','Rapid City Car Shipping Lanes and Estimated Costs',
 'The lanes Pennington County cars take most, each with an open-trailer estimate. The form above prices your own.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates out of Rapid City, sedan that runs, open trailer. Figure 10 to 25 percent more for an SUV or a pickup, and a step up for enclosed. The week and the carriers on 90 that week settle the real number.',
 prose(
  P('Rapid City prices above Sioux Falls on every lane. The pool is smaller, and the trucks pass less often. The Denver lane rides 85 and 25 and fills twice a week. The Minneapolis lane rides 90 east. The Billings lane rides 90 west and thins in winter. The Phoenix and Texas lanes fill with the base orders and the retirees each fall.'),
  P('A report date at the base or a rally week in August means a busy week. The <a href="car-shipping-cost.html">cost guide</a> walks through size, condition, and timing.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Air Force Base, the Engineering School, the Hospital, the Guard, the Tourism Season, the Ranches, and the Retirees',
 prose(
  L('Rapid City relocates airmen, engineers, nurses, students, and seasonal workers. The base moves the most.'),
  P('Ellsworth Air Force Base outside Box Elder flies the bombers. It takes a new wing of them in the next few years. Airmen and their families PCS in and out on orders in every month. The summer is the peak. Orders set the dates, and the handoff happens at the Box Elder lots or outside the gate. Ship Guy is a private broker, not part of the Air Force. The <a href="military-car-shipping.html">military</a> page shows how a report date shapes the window.'),
  P('The engineering school east of downtown brings students in late August and sends them home in May. A parent books, and anyone over eighteen signs at the lots on St. Joseph. The regional hospital on Fifth Street is the largest employer after the base. It hires nurses and specialists from across the country. The handoff happens on Fifth or at the lots across from it. The Guard units in the city rotate people on orders too.'),
  P('The tourism season brings workers to the Hills from May to October. The monuments, the lodges, and the parks hire them. The ranches and the mines bring the rest. The retirees come for the Hills and the tax rates and leave for Arizona in November. Crossing a state line adds paperwork, and the <a href="state-to-state-car-shipping.html">state-to-state</a> page lists it.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Rally, the Stock Show, the Central States Fair, Move-In Week, the Blizzards, the Wind, the Hail, and the 1972 Flood',
 prose(
  L('Rapid City runs on a base calendar and a tourist calendar. The weather problem is a plains winter and a Hills summer.'),
  P('The Sturgis rally fills the Hills for ten days in August. The carriers stay off every road but 90 for the week. The Black Hills Stock Show fills the civic center for ten days in late January. It parks trailers on every lot near it. The Central States Fair runs the last week of August and closes the lots at the fairgrounds. Move-in at the school is the same week. Give an August date three weeks of notice.'),
  P('The Atlas blizzard in October 2013 dropped four feet in the Hills and closed 90 for two days. A blizzard closes 90 from Wall to Sturgis, and the state drops the gates on the ramps. The truck waits at the exit until the gates lift. The wind on 90 across the plains tips high-profile trailers. The state posts advisories that stop the carriers for a day. We call before the day moves.'),
  P('Summer brings hail bigger than golf balls two or three afternoons a year. A carrier does not load under a hail warning and moves to a covered lot when it can. The June 1972 flood on Rapid Creek killed two hundred thirty-eight people. The city turned the creek banks into a greenway. A flood watch on the creek moves the handoff off Omaha Street.'),
  P('Ice on the canyon grades closes Highway 16 to trailers for weeks at a time. The handoff for the Hills towns moves to the flat roads until it clears.'),
 )+chips(["Downtown","West Boulevard","The Gap","Canyon Lake","Skyline Drive","North Rapid","East North Street","Cambell Street","Robbinsdale","Fifth Street","Rapid Valley","Box Elder","Black Hawk","Summerset","Piedmont","Sturgis","Spearfish","Deadwood","Hill City","Keystone","Custer","Hot Springs","Wall"])
 +NOTE('Serving Rapid City, Box Elder, and the Black Hills, West Boulevard curb or Hill City cabin road. Name the neighborhood and say whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Rapid City?',
 prose(
  L('Nearly everything out of the Hills rides open, and the table above assumes it does.'),
  P('Enclosed keeps the hail, the gravel, and the winter grit off the paint. The collectors in West Boulevard book it, and so do the retirees moving a car worth protecting. When an open truck is the only one on 90 that week, we tell you that first. You choose.'),
  P('A commuter car or an airman’s pickup rides open without trouble. Compare the two on the <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('You get a figure, a lot off 90, and a signature at delivery. Orders or the move-in decide the week.'),
  P('Once you accept the figure, a carrier already crossing 90 that week takes the car. The lot and the window are pinned down the same day. The driver walks the car with a camera at pickup and fills in the Bill of Lading. You initial it, and delivery is checked against that sheet.'),
 )+ULI([
  "Personal items cleared from the cabin and the bed",
  "A quarter tank of fuel at most",
  "Pictures of all four sides and the odometer before the truck comes",
  "One good key and a list of anything that does not work",
  "Any add-on alarm switched off",
  "Past the Gap, on a canyon road, or in a Hills town, expect a lot on 90",
 ])+prose(P('Read <a href="how-it-works.html">how it works</a> for the steps and <a href="car-shipping-preparation.html">preparation</a> for the morning of pickup.'))))

BODY.append(sec('Why Ship Guy','Why Rapid City Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already cross 90 each week. We know when the gates drop on the ramps and when the rally clears.'),
  P('Our FMCSA license and $75,000 bond are listed on the federal register, where anyone can look them up. The office is on St. Joseph Street downtown.'),
  P('One coordinator stays with your move from the first figure to the delivery call. The <a href="services.html">services</a> page lays out open, enclosed, and expedited.'),
 )))

BODY.append(office('Rapid City','402 St Joseph St #435','Rapid City, SD 57701','+16056335817','(605) 633-5817','MT',
 '402+St+Joseph+St+%23435,+Rapid+City,+SD+57701','Visit Us','Find Ship Guy in Rapid City',
 'Our office sits downtown on St. Joseph, a block off Main Street and a mile from SD Mines.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3537.933553654205!2d-103.22383389999999!3d44.079761999999995!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x877d4365cc56a0f5%3A0xcc336078421508c3!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793628664075!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Rapid City to Denver or Minneapolis?","Denver runs three hundred sixty to five hundred twenty dollars for a sedan. That is about three hundred ninety miles down 85 and 25. Minneapolis runs four hundred fifty to six hundred fifty, about five hundred ninety miles. Cheyenne is the lowest lane on the table, about three hundred ten miles. An SUV or a pickup runs 10 to 25 percent above those figures."),
 ("Do you ship cars for Ellsworth Air Force Base PCS moves?","Yes, in every month of the year. Orders set the dates, and we plan the pickup around the report date. The handoff happens at the Box Elder lots or outside the gate. The summer is the busy season. Ship Guy is a private broker and not part of the Air Force."),
 ("Why does a Rapid City pickup take 2 to 5 days instead of 1 to 3?","Because the pool is small. The 90 carriers pass through two or three times a week. A car rides the next truck with an open spot. Denver and Minneapolis trucks come most often. A blizzard that closes 90 or a rally week stretches the window further. We say so the day it does."),
 ("Can the carrier come to my street through the Gap or in the Hills?","Usually not. The west side past the Gap is canyon roads with no shoulders. The Hills towns are the same. The driver meets you on West Main, at the Canyon Lake lots, or on 16 and 79. West Boulevard, North Rapid, Robbinsdale, Rapid Valley, and Box Elder usually allow the curb."),
 ("What happens if a blizzard closes Interstate 90 on my pickup day?","The truck waits at the exit until the state lifts the gates, usually a day. The Atlas storm in 2013 closed it for two. We call the moment the forecast turns. The pickup moves to the first open morning at the same figure. The wind advisories work the same way."),
 ("Can you deliver on a School of Mines move-in date?","Yes. Students arrive in late August and leave in May. A parent sets it up, and an adult signs at the lot. The campus blocks are tight that week. The meeting point is the lots on St. Joseph or the civic center. The window comes from the date."),
 ("Can you ship a car to or from Spearfish, Sturgis, or Hot Springs?","Yes. Box Elder, Black Hawk, and Rapid Valley price the same as Rapid City. Spearfish and Sturgis add an hour on the truck and meet it off 90. Hill City, Keystone, Custer, and Hot Springs meet it on 16 or 79. Pierre and the reservation towns add a day."),
 ("Can you ship a car during the Sturgis rally?","Yes, from a lot on 90. The carriers stay off every other road in the Hills for the ten days in August. The handoff moves to the exits. Book three weeks ahead for that week, and expect the window at the long end."),
 ("Can you ship a car that does not run from Rapid City?","Yes. The carrier comes with a winch, and the figure covers the loading time. The mall lots and the big-box lots on LaCrosse are flat. Say whether it rolls, steers, and brakes."),
 ("What do you need for a Rapid City car shipping quote?","Pickup and delivery addresses, with the neighborhood or the Hills town. The vehicle, and whether it runs. Open or enclosed, and the week around the orders or the move. Those four lines get a Rapid City figure back the same day."),
]
BODY.append(faq_section(FAQ,'Rapid City FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Rapid City?','Two minutes on the form above and your lane has a Rapid City figure. Tell us the neighborhood and the week, and the next carrier across 90 takes the car.','+16056335817','(605) 633-5817','Get your free Rapid City quote'))

build({
 'slug':'auto-transport-rapid-city-south-dakota',
 'title':'Car Shipping in Rapid City, SD — Auto Transport | Ship Guy',
 'meta':'Car shipping in Rapid City, SD, at the edge of the Black Hills on Interstate 90. Ellsworth PCS moves, School of Mines dates, hospital hires, main-road handoffs for the Gap and the canyon roads, curbside pickups in the grids, Box Elder, and Rapid Valley, the rally, the blizzards, and the wind. Local office on St. Joseph Street downtown. Free quote.',
 'h1':'Car Shipping in<br>Rapid City, <span class="accent">South Dakota</span>',
 'lede':'Open, enclosed, and expedited auto transport across Rapid City and the Black Hills, planned around Interstate 90, the base orders, the school dates, the rally, the blizzards, and the wind.',
 'tel':'+16056335817','disp':'(605) 633-5817','brand':'Rapid City','keyword':'car shipping in rapid city',
 'localterms':['rapid city','black hills','interstate 90','190','spur','highway 16','mount rushmore road','highway 44','highway 79','omaha street','haines','lacrosse','main street','st. joseph','bronze presidents','the gap','west boulevard','canyon lake','skyline drive','north rapid','east north street','cambell','robbinsdale','fifth street','rapid valley','box elder','black hawk','summerset','piedmont','sturgis','spearfish','deadwood','hill city','keystone','custer','hot springs','wall','pierre','reservation','badlands','rushmore','civic center','mall','truck stops','exit 57','exits 59','exit 61','exit 67','exit 55','airport','ellsworth','air force','bombers','airmen','orders','pcs','engineering school','school of mines','students','regional hospital','largest employer','nurses','guard','tourism','monuments','lodges','ranches','mines','retirees','arizona','rally','stock show','central states fair','fairgrounds','move-in','atlas','october 2013','four feet','gates','ramps','wind','high-profile','advisories','hail','golf balls','june 1972','flood','rapid creek','two hundred thirty-eight','greenway','ice','grades','cheyenne','billings','bismarck','sioux falls','denver','omaha','minneapolis','salt lake','kansas city','phoenix','bill of lading','fmcsa','winch','fly-and-ship','gravel','grit'],
}, BODY, FAQ)
