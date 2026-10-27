import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Lawrence, Kansas','Car shipping on the Turnpike between Topeka and Kansas City, in a college town built on a hill',
 ['Car shipping in Lawrence runs off the Turnpike and the K-10 freeway east to Johnson County. Ship Guy is a licensed auto transport broker with an office on Becker Drive on the west campus.',
  'We book vetted carriers across Douglas County, from North Lawrence to Eudora, Baldwin City, and Lecompton. The trucks belong to the carriers, and we hold the authority and the bond.',
  'Interstate 70 is the Kansas Turnpike here, with exits at East Lawrence and West Lawrence. K-10 runs east to Overland Park and loops the south side as the Trafficway. US 59 is Iowa Street, south to Ottawa. US 40 is 6th Street, west toward Topeka.',
  'This page covers the Turnpike, K-10, downtown, Oread, Old West Lawrence, the west side, and North Lawrence. It also covers the university calendar, the fort, the hospital, basketball nights, the tornado sirens, and the lanes.'],
 'Lawrence at a glance',
 ['Most pickups happen within 1 to 3 days. The Kansas City carriers are forty minutes east on K-10. The Denver trucks pass the city on the Turnpike every day.',
  'Kansas City and Topeka are a same-day haul, and so are Wichita and Omaha. Tulsa, Oklahoma City, and St. Louis take a day. Dallas, Denver, and Chicago take one to two. The coasts take three.'],
 'Tell us the neighborhood. Oread, Old West Lawrence, and East Lawrence need a meeting spot. The streets are narrow, and the hill is steep. The west side off Wakarusa and the subdivisions south of Clinton Parkway usually allow the curb.'))

BODY.append(sec('The Roads','The Turnpike, K-10, the Trafficway, Iowa Street, and 23rd Street',
 prose(
  L('Lawrence sits between the two biggest carrier pools in Kansas, and the Turnpike brings both to its door.'),
  P('Interstate 70 runs the north edge as the Kansas Turnpike. The East Lawrence exit sits by the river, and the West Lawrence exit sits at the Trafficway. It is a toll road with a transponder lane, and the toll rides inside every quote. Topeka is twenty-five minutes west and Kansas City forty minutes east on it. Every carrier between Denver and St. Louis passes the city on it.'),
  P('K-10 is the freeway east to Overland Park and Olathe. The Johnson County carriers use it every day. The South Lawrence Trafficway carries K-10 around the south side from the Turnpike to the east edge. US 59 is Iowa Street, the main commercial strip through the west side and south to Ottawa. US 40 is 6th Street, west to Lecompton and Topeka. US 24 crosses North Lawrence.'),
  P('23rd Street and Clinton Parkway cross the city east and west. Wakarusa Drive runs the west side, and Massachusetts Street is downtown. Kasold, Louisiana, and Haskell run north and south. The river splits North Lawrence from the rest, and one bridge connects them. Campus streets run over the hill, and Jayhawk Boulevard closes to traffic on weekdays.'),
  P('The carriers come off the Turnpike at West Lawrence and off K-10 at Iowa Street. The big-box lots at 31st and Iowa and the west campus park and ride are the meeting spots. The lots at the East Lawrence exit work too. The stadium lots work outside game days.'),
  P('Our office is on Becker Drive on the west campus, off Iowa Street.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, Oread and the Hill, Old West Lawrence, East Lawrence, the West Side, North Lawrence, Eudora, and Baldwin City',
 prose(
  L('Lawrence is a hill with a campus on top and a river at the bottom. The handoff depends on where you sit between them.'),
  P('Downtown is Massachusetts Street, a dozen blocks of storefronts and angled parking too tight for a trailer. The driver meets you at the lots on New Hampshire and Vermont or at the East Lawrence exit. Oread is the student neighborhood on the hill between downtown and the campus. Its streets are steep and narrow, and the cars park on both sides. The handoff moves to a campus lot or to Iowa Street.'),
  P('Old West Lawrence and East Lawrence flank downtown with brick streets, big trees, and houses from the 1870s. A trailer cannot work either one, and the driver meets you on 6th Street or at the lots. The Pinckney and Barker neighborhoods are the same. North Lawrence across the river is older grids on the flood plain by the Turnpike. A lot by the exit works.'),
  P('West Lawrence off Wakarusa and Bob Billings is the newest part of the city. It has wide loops and open curbs. The driver reaches the house on most streets. The subdivisions south of Clinton Parkway and along Iowa Street are the same. Prairie Park and the east side off Harper Street are postwar grids with wider streets. The curb works on most of them.'),
  P('Eudora sits ten minutes east on K-10 with new subdivisions and lots at the exit. Baldwin City sits twenty minutes south with the small college and a Main Street a trailer avoids. Lecompton and Tonganoxie are small towns on the river roads. All of them price the same as Lawrence. So do Topeka and Johnson County at the two ends of the Turnpike.'),
 )))

ROUTES=[("Topeka, KS","I-70 · ~25 mi","Same day","$120–$200"),("Kansas City, MO","K-10/I-70 · ~40 mi","Same day","$130–$210"),
 ("Wichita, KS","I-70/I-335 · ~165 mi","Same day","$200–$310"),("Omaha, NE","K-10/I-29 · ~190 mi","Same day","$220–$340"),
 ("Tulsa, OK","US-59/US-75 · ~250 mi","1 day","$250–$370"),("St. Louis, MO","I-70 · ~285 mi","1 day","$270–$400"),
 ("Oklahoma City, OK","I-335/I-35 · ~310 mi","1 day","$290–$420"),("Dallas, TX","I-335/I-35 · ~520 mi","1–2 days","$420–$600"),
 ("Chicago, IL","I-70/I-35/I-80 · ~530 mi","1–2 days","$430–$620"),("Denver, CO","I-70 · ~560 mi","1–2 days","$440–$630")]
BODY.append(rate_table('Lanes &amp; Costs','Lawrence Car Shipping Lanes and Estimated Costs',
 'The lanes Douglas County cars use most, with estimated open-trailer ranges. Your exact route gets its number on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates priced from Lawrence, open trailer, sedan that runs. SUVs and pickups land 10 to 25 percent higher, enclosed higher again. Turnpike tolls are built in. The carriers free on your dates settle the final figure.',
 prose(
  P('Lawrence prices with Kansas City on every lane. The Johnson County carriers reach it on K-10 in forty minutes. It prices a little under Topeka to the east and about the same to the west. The Denver lane rides the Turnpike and runs daily. The Dallas and Oklahoma lanes ride 35 from Emporia.'),
  P('A move timed to the August move-in or the May commencement costs more. The student cars fill the trucks. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The University, the Fort, the Hospital, the Card Plant, and the Bioscience Firms',
 prose(
  L('Lawrence relocates professors, officers, nurses, and twenty-eight thousand students. The university on the hill moves more people than anyone in the county.'),
  P('The university brings its students in each August and sends them home each May. The parent arranges the car, and an adult meets the truck at a campus lot. Faculty hires land each summer with a closing date and a second car to ship. The tribal university on the south side runs the same calendar. The medical school in Kansas City rotates residents through the hospital on Maine Street.'),
  P('The Army post at Leavenworth sits thirty minutes north on K-10 and US 24. Its staff college rotates a class of officers every summer. Many of them rent in West Lawrence for the year. The government moves one car, and the other one ships with us. Ship Guy is a private broker and not part of the post. See the timing on the <a href="military-car-shipping.html">military</a> page.'),
  P('The card maker’s plant and the packaging plant beside it move supervisors on production schedules. The bioscience firms on the west campus hire scientists from every state. The pharmaceutical research buildings on the west campus and the chemical firm do the same. We supply the paperwork a reimbursed move needs.'),
  P('Commuters to Topeka and Johnson County buy in West Lawrence on closing dates. One car rides the trailer while the other is driven. Retirees who stay for the campus ship a second car in from the coasts. The interstate side is on the <a href="state-to-state-car-shipping.html">state-to-state</a> page.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Basketball Nights, Move-In, the Walk Down the Hill, the Sirens, and the Ice',
 prose(
  L('Lawrence runs on the basketball schedule from November through March. The student calendar runs the rest of the year.'),
  P('The fieldhouse holds sixteen thousand. A game night fills every lot and street on the hill from four o’clock. A handoff near the campus on a game night moves to the morning or to Iowa Street. Football Saturdays do the same thing on a smaller scale. Move-in week in August fills Oread. The walk down the hill at commencement closes the campus roads for a May Sunday.'),
  P('The farmers’ market fills the lots on New Hampshire on Saturday mornings. The downtown art walks close Massachusetts Street for a Friday evening each month. The county fair fills the fairgrounds on 23rd Street for a week in August. The sidewalk sale closes downtown for a July Thursday. A handoff near any of them moves to the daytime.'),
  P('The sirens sound a few times each spring. The 2019 tornado crossed Douglas County south of the city on a May evening. It leveled homes in Linwood. A warning pauses the loading until it clears, and the driver nearly always finishes that day. Summer brings a hundred degrees and a wind that never stops.'),
  P('Winter brings twenty inches of snow and an ice storm every few years. The 2007 ice storm took the power out for a week and closed the Turnpike for days. The Kaw floods North Lawrence in a wet spring, as it did in 1993. A pickup there moves up the hill. The carriers wait in Topeka or Kansas City until the Turnpike reopens.'),
 )+chips(["Downtown","Massachusetts Street","Oread","The Hill","Campus","Jayhawk Boulevard","Old West Lawrence","East Lawrence","Pinckney","Barker","North Lawrence","The Kaw","West Lawrence","Wakarusa","Bob Billings","Clinton Parkway","Iowa Street","23rd Street","Prairie Park","Harper Street","Haskell","Becker Drive","West Campus","Eudora","Baldwin City","Lecompton","Tonganoxie","De Soto","Ottawa","Clinton Lake"])
 +NOTE('Serving Lawrence and all of Douglas County, brick street on the hill or new loop out west. Tell us the neighborhood and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Lawrence?',
 prose(
  L('Open trailers carry nearly every car that leaves Douglas County, and the table above assumes one.'),
  P('An enclosed trailer keeps off the gravel, the ice, and the hail. The collectors who fill the downtown car show book one. Parents shipping a new car to a student book one too.'),
  P('A commuter car or a student’s sedan rides open and arrives as it left. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages go into the difference.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a lot on Iowa Street or at the campus, and a signature at the far end. The move-in date or the closing picks the week.'),
  P('Accept the price, and the car joins a carrier already running the Turnpike or K-10. Within hours you have the lot and the window. Before loading, the driver walks the car with you. Every existing mark goes on the Bill of Lading. You both sign, and that list settles any question at the other end.'),
 )+ULI([
  "Cabin and trunk cleared of anything personal",
  "Fuel gauge near a quarter",
  "All four sides and the mileage photographed first",
  "A working key for the driver, and a word on any fault",
  "Aftermarket alarm turned off",
  "On the hill or downtown, meet the truck at a campus lot or on Iowa Street",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Lawrence Drivers Choose Ship Guy',
 prose(
  L('We book the carriers already running the Turnpike between Topeka and Kansas City. We know which streets on the hill take a trailer and which do not.'),
  P('Ship Guy’s FMCSA brokerage authority and $75,000 surety bond can both be looked up on the federal register. Our office is on Becker Drive on the west campus.'),
  P('You get one coordinator from the first call to the final signature. Open, enclosed, and expedited transport are set out on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Lawrence','2029 Becker Dr #558','Lawrence, KS 66047','+17853844711','(785) 384-4711','CT',
 '2029+Becker+Dr+%23558,+Lawrence,+KS+66047','Visit Us','Find Ship Guy in Lawrence',
 'Our office is on Becker Drive on the west campus, off Iowa Street.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4771.556266876486!2d-95.2667948!3d38.9485265!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x87bf697eedf1ac47%3A0x3d386dee2def5f0e!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793102876595!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Lawrence to Kansas City or Denver?","Kansas City runs one hundred thirty to two hundred ten dollars for a sedan. That is about forty miles east on K-10. Denver runs four hundred forty to six hundred thirty, about five hundred sixty miles west on 70. Topeka is twenty-five minutes away and the lowest of the three. An SUV or a pickup adds 10 to 25 percent."),
 ("Can the carrier come to my street in Oread or Old West Lawrence?","Usually not. Oread is steep and narrow with cars on both sides. Old West Lawrence and East Lawrence are brick streets under old trees. The driver meets you at a campus lot, on 6th Street, or at the lots on New Hampshire. West Lawrence, Prairie Park, and the subdivisions south of Clinton Parkway usually allow the curb."),
 ("Can you deliver on the KU move-in date?","Yes. The university takes cars in each August and sends them home in May. A parent books, and an adult over eighteen signs at a campus lot. The window is built around move-in day and shifts if the date does. Oread fills that week, so the handoff happens at the lots off Iowa Street. Both windows fill early, so book ahead."),
 ("Does a basketball game affect my pickup?","On the hill, yes. The fieldhouse fills every lot and street near the campus from four o’clock on a game night. We move a handoff near the campus to the morning or to Iowa Street. The west side and the subdivisions run normally. Football Saturdays work the same way."),
 ("Can you ship a car to or from Eudora, Baldwin City, or Topeka?","Yes, and all three price the same as Lawrence. Eudora rides the same carriers off K-10, and the handoff works at the exit. Baldwin City rides them down US 59. The driver meets you on the highway rather than on Main Street. Topeka rides them twenty-five minutes west on the Turnpike. Send the full address for a new subdivision."),
 ("Do you ship cars for officers at Fort Leavenworth?","Yes, every summer. The staff college rotates a class each year, and many officers rent in West Lawrence. The orders cover a single car, and the second one rides with us. Ship Guy is a private broker and not part of the post. Send the report date, and the window is built to it."),
 ("What happens if a tornado warning or an ice storm hits on my pickup day?","A warning pauses the loading until it clears, and the driver waits it out in the cab. The sirens sound a few times each spring, and the loading nearly always finishes that day. An ice storm closes the Turnpike for a day or two. The carriers wait in Topeka or Kansas City. A winter pickup can slip a day, and you hear it from us first."),
 ("Can you ship a car that does not run from Lawrence?","Yes. A winch truck is dispatched, and the slower loading is already priced in. The big-box lots at 31st and Iowa or the park and ride give the driver level ground. Let us know whether it rolls, steers, and brakes."),
 ("Are the Turnpike tolls in my price?","Yes. The carrier pays the Turnpike with a transponder, and the toll rides inside the quote. There is no separate line for it. K-10, Iowa Street, and the county roads carry no toll."),
 ("What do you need for a Lawrence car shipping quote?","Both addresses, with the Lawrence neighborhood named. The year, make, and model. Whether it runs. Open or enclosed. The week around the move-in date or the closing. That is everything, and the Lawrence number comes back the same day."),
]
BODY.append(faq_section(FAQ,'Lawrence FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Lawrence?','The form above prices the lane in the time it takes to read this. Name the neighborhood and the week, and a Turnpike carrier takes it.','+17853844711','(785) 384-4711','Get your free Lawrence quote'))

build({
 'slug':'auto-transport-lawrence-kansas',
 'title':'Car Shipping in Lawrence, KS — Auto Transport | Ship Guy',
 'meta':'Car shipping in Lawrence, KS, on the Turnpike between Topeka and Kansas City. KU move-in and commencement timing, campus-lot handoffs for Oread and the brick streets, curbside pickups in West Lawrence, Fort Leavenworth officers, basketball nights, the sirens, and the ice. Local office on Becker Drive on the west campus. Free quote.',
 'h1':'Car Shipping in<br>Lawrence, <span class="accent">Kansas</span>',
 'lede':'Open, enclosed, and expedited auto transport across Douglas County, planned around the Turnpike, K-10, the hill, the student calendar, and the storms.',
 'tel':'+17853844711','disp':'(785) 384-4711','brand':'Lawrence','keyword':'car shipping in lawrence',
 'localterms':['lawrence','douglas county','turnpike','interstate 70','east lawrence','west lawrence','transponder','topeka','kansas city','denver','st. louis','k-10','overland park','olathe','johnson county','trafficway','us 59','iowa street','ottawa','us 40','6th street','lecompton','us 24','north lawrence','23rd street','clinton parkway','wakarusa','massachusetts street','kasold','louisiana','haskell','river','bridge','jayhawk boulevard','31st','park and ride','west campus','stadium','becker drive','downtown','angled parking','new hampshire','vermont','oread','student','steep','old west lawrence','brick streets','1870s','pinckney','barker','flood plain','bob billings','prairie park','harper street','eudora','baldwin city','college','main street','tonganoxie','wichita','omaha','tulsa','oklahoma city','dallas','chicago','emporia','move-in','commencement','professors','officers','nurses','twenty-eight thousand','tribal university','medical school','residents','maine street','army post','leavenworth','staff college','card maker','packaging plant','bioscience','scientists','pharmaceutical','chemical firm','commuters','retirees','basketball','fieldhouse','sixteen thousand','game night','football saturdays','walk down the hill','farmers’ market','art walks','county fair','fairgrounds','sidewalk sale','sirens','2019 tornado','linwood','hundred degrees','wind','twenty inches','ice storm','2007','the kaw','1993','car show','bill of lading','fmcsa','surety bond','de soto','clinton lake'],
}, BODY, FAQ)
