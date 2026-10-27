import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Davenport, Iowa','Car shipping in the Quad Cities, where Interstate 80 crosses the Mississippi and the Chicago carriers enter Iowa',
 ['Car shipping in Davenport runs off Interstate 80 on the north edge and the two river bridges. Ship Guy is a licensed auto transport broker with an office on 2nd Street downtown.',
  'We book vetted carriers across the Quad Cities, from Bettendorf and LeClaire to Rock Island and Moline. We do not own the trucks.',
  'Interstate 80 crosses the north side of the city and the river at LeClaire. Interstate 74 runs through Bettendorf and over the new bridge to Moline. Interstate 280 loops the west side and crosses to Rock Island. US 61 is Brady and Harrison, the one-way pair through the middle. Kimberly Road and 53rd Street carry the retail.',
  'This page covers 80, the bridges, downtown, the Brady corridor, the north side, Bettendorf, and the Illinois side. It also covers the arsenal, the tractor plants, the aluminum mill, the Bix weekend, and the lanes.'],
 'Davenport at a glance',
 ['Most pickups happen within 1 to 3 days. Every cross-country carrier on 80 crosses the river here, and the Chicago trucks are three hours away.',
  'Chicago, Des Moines, Madison, and Milwaukee are all a same-day haul. St. Louis, Omaha, Indianapolis, and Minneapolis take a day. Kansas City takes a day too. Dallas and Denver take two, and the coasts take three to five.'],
 'Tell us the side of the river. Downtown and the old grids off Brady need a meeting spot. The north side, Bettendorf, and the subdivisions off 53rd usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 80, Interstate 74, Interstate 280, the Bridges, Brady Street, and Kimberly Road',
 prose(
  L('Davenport is where the busiest truck road in the country crosses the biggest river. The carriers stop here on every run.'),
  P('Interstate 80 crosses the north side from the Walcott truck stop to the river bridge at LeClaire. The exits at Northwest Boulevard, Brady, and Middle Road serve the city. Every carrier between Chicago and Omaha passes all three. Interstate 74 leaves 80 at the north end and runs through Bettendorf to the new bridge and Moline. Interstate 280 loops the west and south sides from 80 to the Rock Island bridge.'),
  P('US 61 is Brady Street southbound and Harrison Street northbound, the one-way pair through the city. It runs north to Dubuque and south to Muscatine. US 67 follows the river road. Kimberly Road is the old retail strip across the city, and 53rd Street is the new one. Locust Street and Division Street cross the old grid. Elmore Avenue carries the east side past the casino.'),
  P('The Centennial Bridge carries US 67 downtown to Rock Island, and the Government Bridge crosses the arsenal island. Both are narrow and old. The carriers use the 74 and 280 bridges. River Drive runs the riverfront past the ballpark, and it closes when the river rises.'),
  P('The carriers come off 80 at Brady and Northwest Boulevard, and off 74 at Kimberly. The mall on Kimberly, the Walcott truck stop, and the casino on Elmore are the meeting spots. No road in the Quad Cities charges a toll.'),
  P('Our office is on 2nd Street downtown, a block from the riverfront and the ballpark.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the Hilltop Grids, the North Side, Bettendorf, and the Illinois Side',
 prose(
  L('Davenport climbs from the river in steps, and the streets get wider with each step up the hill.'),
  P('Downtown sits on the river flat around 2nd and 3rd Streets, the arena, and the Figge. The streets are narrow and one-way, and the river closes the lowest ones in a wet spring. The driver meets you at the riverfront lots, at the arena, or on River Drive. The old grids up the hill along Brady and Harrison are dense blocks with alleys. The handoff moves to the main road.'),
  P('The hilltop neighborhoods around the two colleges and Vander Veer Park are old houses on narrow streets. The driver meets you on Locust or at a campus lot. The grids between Locust and Kimberly are postwar blocks with wider streets. The curb works on most of them.'),
  P('The north side between Kimberly and 80 is the retail strip, the hospital campus, and newer subdivisions. The streets are wide, and the truck reaches the curb. The newest subdivisions off 53rd Street and Northwest Boulevard are not on every map yet. Send the full address.'),
  P('Bettendorf to the east is the quieter half of the Iowa side. It has the casino, the office parks, and subdivisions along Middle Road and 53rd. The curb works. LeClaire up the river is a small town with lots on the highway. Rock Island, Moline, and East Moline across the bridges are the Illinois half. They hold the tractor plants and the arsenal. All of them price the same as Davenport, and the Walcott truck stop serves them all.'),
 )))

ROUTES=[("Chicago, IL","I-80/I-88 · ~175 mi","Same day","$210–$330"),("Des Moines, IA","I-80 · ~170 mi","Same day","$210–$320"),
 ("Madison, WI","US-61/US-151 · ~170 mi","Same day","$210–$330"),("Milwaukee, WI","I-88/I-39/I-90 · ~200 mi","Same day","$230–$350"),
 ("St. Louis, MO","US-61/I-55 · ~270 mi","1 day","$260–$380"),("Omaha, NE","I-80 · ~300 mi","1 day","$290–$420"),
 ("Indianapolis, IN","I-74 · ~310 mi","1 day","$300–$440"),("Minneapolis, MN","US-61/I-90/I-35 · ~330 mi","1 day","$310–$450"),
 ("Kansas City, MO","I-80/I-35 · ~370 mi","1 day","$340–$490"),("Dallas, TX","I-35 · ~850 mi","2 days","$600–$850")]
BODY.append(rate_table('Lanes &amp; Costs','Davenport Car Shipping Lanes and Estimated Costs',
 'The lanes Quad Cities cars travel most, with estimated open-trailer ranges. Your exact route gets a number on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates leaving Davenport, sedan in running order, open trailer. SUVs and pickups add 10 to 25 percent, and an enclosed trailer adds more. Harvest season and the winter move the number. The carriers free on your dates settle the final price.',
 prose(
  P('Davenport prices under Des Moines on the Chicago lane, because the Quad Cities sit three hours closer. The 80 carriers cross the river here on every run and take a car without a detour. The Omaha and Denver lanes ride the same road west. The Madison and Milwaukee lanes ride 61 and 151 and run lighter.'),
  P('The Walcott truck stop west of the city is the biggest in the world. The carriers stage there between loads. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Arsenal, the Tractor Plants, the Aluminum Mill, the Hospitals, and the Colleges',
 prose(
  L('Davenport relocates Army civilians, plant engineers, nurses, and chiropractic students. The arsenal and the tractor maker move more people than anyone.'),
  P('The arsenal on the island between the cities is the largest government-owned manufacturing site in the Army. It moves civilians, officers, and the staff of two commands in on assignment cycles. The orders pay for one car, and the second one rides with us. Ship Guy is a private broker and has no tie to the arsenal. Timing is on the <a href="military-car-shipping.html">military</a> page.'),
  P('The tractor maker headquartered in Moline runs plants on both sides of the river. The Davenport works builds the big construction machines. It moves engineers and supervisors between plants on program schedules. The aluminum mill in Riverdale and the meat plant on the west side relocate engineers the same way. We supply the paperwork a reimbursed move needs.'),
  P('Both hospital systems hire traveling nurses all year and take new residents each June. The physicians come with a closing date and a second car to ship. The chiropractic college draws students from every state and every continent each fall. The parent arranges the car. The two colleges on the hilltop and the one in Rock Island run the same calendar.'),
  P('Families from Chicago buy in Bettendorf and the north side on closing dates in every month. One car rides the trailer while the other is driven. The interstate side is on the <a href="state-to-state-car-shipping.html">state-to-state</a> page.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Bix Weekend, the Fair, the Air Show, the River, the Derecho, and the Snow',
 prose(
  L('Davenport runs on a road race in July and a county fair in August. The river comes into downtown every few springs.'),
  P('The Bix weekend fills downtown and the hilltop on the last weekend of July. The race closes Brady Street and the hill on Saturday morning. The jazz festival fills the riverfront that night. A pickup on the route that weekend moves to the north side. The fair fills the fairgrounds on Locust for a week in August. The air show fills the airport roads for a June weekend.'),
  P('The ballpark on the riverfront fills its lots on game nights from April through September. The arena fills them on hockey nights all winter. The golf tournament in Silvis fills the Illinois side for a week in July. A handoff downtown on any of those days moves to the daytime or to Kimberly.'),
  P('The river is the weather here. Davenport never built a flood wall, and the Mississippi comes into downtown when it rises. The 2019 flood broke through the temporary barrier. River Drive and the downtown blocks sat under water for weeks. The 1993 and 2008 floods did the same. A pickup downtown in a wet spring moves up the hill, and we tell you when it does.'),
  P('The 2020 derecho crossed the Quad Cities on its way to Cedar Rapids. It took the trees down across the north side. The sirens sound a few times each spring. Winter brings thirty inches of snow, and 80 closes a few times a season. The carriers park at Walcott until the plows finish, and a winter pickup can lose a day. Ice is the bigger problem on the bridges.'),
 )+chips(["Downtown","2nd Street","Riverfront","River Drive","Ballpark","Arena","Brady Street","Harrison","Hilltop","Vander Veer","St. Ambrose","Palmer","Locust Street","Division","Kimberly Road","North Side","53rd Street","Northwest Boulevard","Elmore","Casino","Hospital Campus","Bettendorf","Middle Road","LeClaire","Walcott","Riverdale","Blue Grass","Eldridge","Rock Island","Moline","East Moline","Arsenal Island","Silvis","Muscatine"])
 +NOTE('Serving Davenport, Bettendorf, and all of the Quad Cities on both sides of the river. Tell us the side of the river and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Davenport?',
 prose(
  L('Open trailers move most Quad Cities cars, and the lane table is priced for one.'),
  P('An enclosed trailer keeps a car out of the salt, the gravel, and the harvest dust. The collectors who fill the riverfront cruise nights book one for the show cars. Families sending a car to a student from overseas book one too.'),
  P('A commuter car or a farm truck is fine on an open trailer. The difference is spelled out on the <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A quote, a lot at the mall or Walcott, and the car waiting at the far end. Most moves wrap up inside a week.'),
  P('Say yes to the number, and the car is booked onto a carrier already crossing on 80. The lot and the window come back that day. The driver and you inspect the car together before it loads. Every mark is written on the Bill of Lading. Two signatures, and the same sheet is read again at delivery.'),
 )+ULI([
  "Nothing personal left in the cabin or the trunk",
  "Fuel at roughly a quarter tank",
  "Dated photos of each panel and the mileage",
  "One working key handed over, with any fault described",
  "Aftermarket alarm disabled",
  "Downtown or on the hilltop, meet the truck at the riverfront lots or on Locust",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Davenport Drivers Choose Ship Guy',
 prose(
  L('We catch the 80 carriers as they cross the river. We plan around the Bix weekend, the flood stage, and the winter.'),
  P('Ship Guy’s brokerage authority and $75,000 surety bond are both on the FMCSA register. Our office is on 2nd Street downtown.',),
  P('Whoever prices your move is the person who sees it signed for at the far end. The <a href="services.html">services</a> page describes open, enclosed, and expedited transport.'),
 )))

BODY.append(office('Davenport','102 E 2nd St #473A','Davenport, IA 52801','+15639210721','(563) 921-0721','CT',
 '102+E+2nd+St+%23473A,+Davenport,+IA+52801','Visit Us','Find Ship Guy in Davenport',
 'Our office is on 2nd Street downtown, a block from the riverfront and the ballpark.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4593.595185258625!2d-90.5732931!3d41.521646700000005!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x87e235b9f2c63759%3A0xc7e386f160b72662!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793025214142!5m2!1sen!2sus'))

FAQ=[
 ("How much does it cost to ship a car from Davenport to Chicago or Des Moines?","Chicago runs two hundred ten to three hundred thirty dollars for a sedan. That is about one hundred seventy-five miles on 80 and 88. Des Moines runs two hundred ten to three hundred twenty, about one hundred seventy miles west on 80. Madison and Milwaukee cost about the same. Figure 10 to 25 percent more for an SUV or a pickup. Trucks run all of them daily."),
 ("Can the carrier come to my street downtown or on the hilltop?","Usually not. Downtown is narrow one-way streets on the river flat. The hilltop around the colleges is old houses on narrow streets under big trees. The driver meets you at the riverfront lots, at the arena, or on Locust. The north side, Bettendorf, and the subdivisions off 53rd usually allow the curb."),
 ("Do you ship cars for people relocating to the arsenal or the tractor plants?","Yes, all year. The arsenal moves civilians and officers in on assignment cycles, and the orders cover one car. The tractor maker moves engineers and supervisors between its plants on both sides of the river. Many ship a second car behind the move. The handoff works at the mall lot on Kimberly or a lot off 80. We provide the paperwork a reimbursed move needs."),
 ("Does the river affect my pickup?","Some springs, yes. Davenport has no flood wall, and the Mississippi comes into downtown when it rises. The 2019 flood put River Drive and the downtown blocks under water for weeks. A pickup downtown in a wet spring moves up the hill to Locust or Kimberly. The hilltop and the north side never notice."),
 ("Can you ship a car to or from Bettendorf, Rock Island, or Moline?","Yes, and all of them price the same as Davenport. Bettendorf rides the same carriers off 74 and Middle Road. Rock Island and Moline ride them across the 74 and 280 bridges. The handoff works at a lot off the interstate. Send the full address, and we tell you which bridge the carrier uses."),
 ("Does the Bix weekend affect my pickup?","Downtown and on the hill, yes. The race closes Brady Street and the hilltop on the last Saturday of July. The jazz festival fills the riverfront that night. We move a pickup on the route to the north side or to Sunday. The rest of the Quad Cities runs normally."),
 ("What happens if a blizzard or a tornado warning hits on my pickup day?","Snow and ice close 80 and the bridges a few times a winter. The carriers park at Walcott until the plows finish. When a winter pickup slides a day, you know before it happens. Spring brings a few siren days, and a tornado warning pauses the loading until it clears. The driver sits it out and nearly always finishes that day."),
 ("Can you ship a car that does not run from Davenport?","Yes. A winch truck comes, and the quote includes the loading time from the first number. The mall lot on Kimberly or the Walcott truck stop gives the driver room to work. Let us know whether it rolls, steers, and brakes."),
 ("Can you deliver on the Palmer or St. Ambrose move-in date?","Yes. The three colleges take cars in each August and send them home in May. Students come from every state and from overseas. A parent arranges it, and an adult meets the truck at a campus lot. The window is tied to move-in day and moves if it moves."),
 ("What do you need for a Davenport car shipping quote?","The pickup and delivery addresses, with the side of the river or the town. The year, make, and model. Whether it runs. Open or enclosed. The week it should go. Five answers make a full Davenport request, and the number follows the same day."),
]
BODY.append(faq_section(FAQ,'Davenport FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Davenport?','The form above turns your lane into a number in two minutes. Name the side of the river and the week, and a carrier already crossing on 80 takes it.','+15639210721','(563) 921-0721','Get your free Davenport quote'))

build({
 'slug':'auto-transport-davenport-iowa',
 'title':'Car Shipping in Davenport, IA — Auto Transport | Ship Guy',
 'meta':'Car shipping in Davenport, IA and the Quad Cities, where Interstate 80 crosses the Mississippi. Arsenal and tractor-plant relocations, downtown and hilltop meeting spots, north side and Bettendorf curbside pickups, the Illinois side, the Bix weekend, the 2019 flood, the derecho, and the Walcott truck stop. Local office on 2nd Street downtown. Free quote.',
 'h1':'Car Shipping in<br>Davenport, <span class="accent">Iowa</span>',
 'lede':'Open, enclosed, and expedited auto transport across the Quad Cities, planned around 80, the bridges, the river stage, and the winter.',
 'tel':'+15639210721','disp':'(563) 921-0721','brand':'Davenport','keyword':'car shipping in davenport',
 'localterms':['davenport','quad cities','mississippi','interstate 80','interstate 74','interstate 280','bridges','leclaire','walcott','truck stop','us 61','brady','harrison','one-way','us 67','kimberly','53rd street','locust','division','elmore','casino','centennial bridge','government bridge','river drive','northwest boulevard','middle road','downtown','2nd street','arena','figge','riverfront','ballpark','hilltop','colleges','vander veer','north side','hospital campus','subdivisions','bettendorf','office parks','rock island','moline','east moline','arsenal','island','tractor','plants','aluminum mill','riverdale','meat plant','hospital systems','nurses','residents','chiropractic','overseas','civilians','officers','orders','bix','race','jazz festival','fair','fairgrounds','air show','hockey','golf tournament','silvis','flood wall','2019 flood','1993','2008','2020 derecho','cedar rapids','sirens','snow','ice','chicago','des moines','madison','milwaukee','st. louis','omaha','indianapolis','minneapolis','kansas city','dallas','denver','dubuque','muscatine'],
}, BODY, FAQ)
