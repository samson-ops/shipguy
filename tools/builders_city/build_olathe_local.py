import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Olathe, Kansas','Car shipping in the Johnson County seat, where Interstate 35 runs through the fastest-growing city in Kansas',
 ['Car shipping in Olathe runs off Interstate 35, which cuts through the city on the way to Wichita. Ship Guy is a licensed auto transport broker with an office on Mahaffie Street off 151st.',
  'We arrange vetted carriers across west Johnson County, from Lenexa to Gardner and down to Spring Hill. The trucks belong to the carriers.',
  'Interstate 35 runs diagonally through the city with exits at 119th, Santa Fe, and 151st. K-10 crosses the north edge toward Lawrence. K-7 runs the west side. US 169 is the east side, and Santa Fe Street is the old road through downtown.',
  'This page covers 35, the K-7 side, downtown and the square, the east side, the southwest, and Gardner. It also covers the GPS maker, the hospital, the courthouse, the intermodal, Old Settlers, and the lanes.'],
 'Olathe at a glance',
 ['Most pickups happen within 1 to 3 days. Every carrier between Kansas City and Wichita or Dallas passes the city on 35.',
  'Topeka is an hour, and Columbia is two. Wichita, Omaha, Tulsa, and St. Louis are a same-day haul. Oklahoma City and Chicago are a day. Dallas and Denver are one to two, and the coasts are three to five.'],
 'Tell us the side of 35. Downtown and the blocks around the square need a meeting spot. The subdivisions off 151st, Black Bob, and Ridgeview usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 35, K-10, K-7, US 169, Santa Fe Street, and 151st Street',
 prose(
  L('Olathe is the first city a southbound carrier reaches after the metro loop. Interstate 35 runs straight through it.'),
  P('Interstate 35 enters from Lenexa at 119th Street and leaves toward Gardner at 175th. The exits at 119th, Santa Fe, 151st, and 159th cover seven miles. Every carrier between Kansas City and Wichita, Oklahoma City, and Dallas passes all of them. Interstate 435 sits five minutes northeast at the Lenexa line.'),
  P('K-10 crosses the north edge of the city from 435 to Lawrence, and the Lawrence carriers use it. K-7 runs north and south along the west side from Shawnee to Spring Hill. US 169 runs the east side as Metcalf and continues south. US 56 is Old 56 Highway, the road west to Gardner and the intermodal.'),
  P('Santa Fe Street is the old main road through downtown and the square. 119th, 127th, 135th, 143rd, 151st, 159th, and 167th cross the city east and west. Ridgeview, Mur-Len, Black Bob, Pflumm, Woodland, and Lone Elm run north and south. College Boulevard runs the north side past the activity center.'),
  P('The carriers come off 35 at Santa Fe and 151st, and off K-10 at Ridgeview. The activity center, the shopping centers on 151st, and the Santa Fe exit have the usual meeting lots. No road in Olathe charges a toll. The Turnpike starts at Kansas City.'),
  P('Our office is on Mahaffie Street off 151st, a few minutes from the 151st Street exit on 35.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown and the Square, the East Side, the Southwest, Cedar Creek, Gardner, and Spring Hill',
 prose(
  L('Olathe is an old trail town that became a suburb, and the subdivisions now reach every county road.'),
  P('Downtown is the square around the courthouse. The old grid runs along Santa Fe, Kansas Avenue, and Park Street. The streets are narrow, and the courthouse fills them on weekdays. The driver meets you at the lots off Santa Fe or at the shopping center on the highway. The old grids between downtown and 119th have mature trees and alleys. The handoff moves to the main road.'),
  P('The east side between 35 and the Overland Park line is subdivisions from the last forty years. The streets off Black Bob, Mur-Len, and 151st are wide, and the truck reaches the curb. The stagecoach stop and the GPS campus sit on this side. The north side along College Boulevard and 119th is offices, the activity center, and apartments with big lots.'),
  P('The southwest off 151st, Lone Elm, and Woodland is the growth side, with subdivisions out to 175th. The curb works, and the streets are new enough that the maps lag. Send the full address. Cedar Creek on the far west side is a golf community with a gate. The handoff waits at the gate.'),
  P('Gardner to the southwest has the intermodal and the warehouses. Its roads are wide, with lots on every main street. Spring Hill to the south is a small town growing fast on 169. Lenexa to the north has the warehouses off 35. De Soto to the northwest is building the battery plant. All of them price the same as Olathe, and so does Overland Park next door.'),
 )))

ROUTES=[("Topeka, KS","K-10/I-70 · ~60 mi","Same day","$140–$230"),("Columbia, MO","I-70 · ~140 mi","Same day","$190–$300"),
 ("Wichita, KS","I-35 · ~175 mi","Same day","$210–$330"),("Omaha, NE","I-29 · ~200 mi","Same day","$230–$350"),
 ("Tulsa, OK","US-69/I-44 · ~240 mi","1 day","$250–$370"),("St. Louis, MO","I-70 · ~260 mi","1 day","$250–$380"),
 ("Oklahoma City, OK","I-35 · ~325 mi","1 day","$300–$440"),("Dallas, TX","I-35 · ~520 mi","1–2 days","$430–$620"),
 ("Denver, CO","I-70 · ~610 mi","1–2 days","$450–$650"),("Chicago, IL","I-35/I-80 · ~520 mi","1–2 days","$420–$600")]
BODY.append(rate_table('Lanes &amp; Costs','Olathe Car Shipping Lanes and Estimated Costs',
 'The lanes west Johnson County cars take most, with estimated open-trailer ranges. Your exact route prices on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates out of Olathe, sedan that starts and drives, open trailer. SUVs and pickups run 10 to 25 percent higher, and an enclosed trailer higher still. Turnpike tolls are inside the number when a carrier uses it. The season and the carriers free on your dates set the final figure.',
 prose(
  P('Olathe prices a few dollars under Kansas City on the Wichita and Dallas lanes. The southbound carriers reach it first and fill the last spot here. The Denver and Omaha lanes price with the metro. The Chicago lane rides 35 and 80 and runs lighter.'),
  P('The Sun Belt lanes rise in the fall with the snowbirds and ease in the spring. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The GPS Maker, the Hospital, the Courthouse, the Intermodal, and the Avionics Plant',
 prose(
  L('Olathe relocates engineers, nurses, county staff, and warehouse managers. The GPS campus moves more people than anyone.'),
  P('The GPS maker’s headquarters on 151st Street employs thousands and hires engineers from every state. They arrive on start dates all year, and many ship a car behind the move. The avionics plant on the north side and the insurance campus relocate staff on their own calendars. We supply the paperwork a reimbursed move needs.'),
  P('The hospital on 151st west of 35 brings in nurses all year and physicians with a closing date. The county government on the square moves attorneys, judges, and staff in every month. The trucking company headquartered in town moves its own people too.'),
  P('The intermodal and the warehouses in Gardner and Edgerton bring in managers and technicians from every state. The battery plant rising in De Soto is moving engineers in from Michigan and Japan on program schedules. The university on College Boulevard brings cars in each August. A parent ships the car, and an adult signs at a campus lot.'),
  P('Families priced out of Overland Park buy in the southwest subdivisions. Many ship a second car behind the move. Fort Leavenworth sits an hour north, and some staff-college families settle here each summer. The orders pay for one car, and the other rides with us. Ship Guy is a private broker and has nothing to do with the post. Timing around a report date is on the <a href="military-car-shipping.html">military</a> page. The interstate side is on the <a href="state-to-state-car-shipping.html">state-to-state</a> page.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Old Settlers, the County Fair, Friday Night Football, the Ice, and the Sirens',
 prose(
  L('Olathe runs on a September festival around the square, a county fair in Gardner, and an icy winter.'),
  P('Old Settlers fills downtown for a weekend in September. The carnival sits on the square, the parade closes Santa Fe, and the lots fill by noon. A downtown pickup that weekend moves to 151st or to the activity center. The county fair in Gardner does the same thing to Old 56 Highway at the end of July.'),
  P('Friday night football fills the activity center lots on College Boulevard from August through November. The Fourth of July fireworks fill the lake and the activity center lots. The soccer and baseball tournaments at the parks fill 151st on spring weekends. A handoff near any of them moves to the morning.'),
  P('Ice is the winter problem. The 2002 ice storm took the trees and the power down across the county for a week. The carriers parked on 35 for two days. Twenty inches of snow falls in a normal winter, and the 2011 blizzard closed 35 for a day. The carriers wait it out at the Gardner truck stops. A pickup that week can slip a day.'),
  P('The sirens sound a few times each spring. The 2019 tornado crossed the Kansas River at Linwood and Bonner Springs. The 2003 storms crossed the metro. A pickup waits for the warning to lift. Mill Creek and Cedar Creek flood the low roads in a big summer storm. Summer heat passes one hundred degrees in July, and the loading hour moves to the morning.'),
 )+chips(["Downtown","The Square","Courthouse","Santa Fe","Kansas Avenue","Park Street","Mahaffie","Old Grid","North Side","College Boulevard","Activity Center","119th","East Side","Black Bob","Mur-Len","Ridgeview","151st","Garmin Campus","Prairie Center","Southwest","Lone Elm","Woodland","159th","167th","175th","Cedar Creek","Lake Olathe","Gardner","Edgerton","Spring Hill","Lenexa","De Soto","Overland Park"])
 +NOTE('Serving Olathe, Gardner, Spring Hill, and the west side of Johnson County, courthouse block or new subdivision. Tell us the side of 35 and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Olathe?',
 prose(
  L('Nine cars in ten leave Olathe on an open trailer, and the table above is priced that way.'),
  P('An enclosed trailer shuts out the road salt, the gravel, and the hail. The garages in Cedar Creek book one for the show cars. Engineers relocating a new car to the GPS campus book one too.'),
  P('A daily driver or a work truck rides open and arrives fine. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain the trade-off.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A number, a meeting spot at the activity center or off 151st, and a car at delivery. The start date sets the week.'),
  P('Accept the number, and we hand the car to a carrier already running 35. The lot and the window reach you that day. The driver goes over the car with you and lists every mark on a Bill of Lading. You both sign, and the delivery is checked against the same sheet.'),
 )+ULI([
  "Empty the cabin, the trunk, and the console of anything personal",
  "Run the fuel down to about a quarter tank",
  "Photograph every panel and the mileage before the truck arrives",
  "Hand over one working key and describe any fault",
  "Switch off any aftermarket alarm",
  "Downtown or in Cedar Creek, meet the truck at a lot off Santa Fe or at the gate",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Olathe Drivers Choose Ship Guy',
 prose(
  L('We catch the southbound carriers at the first exits past the loop. We plan around the start date, Old Settlers, and the ice.'),
  P('Ship Guy holds FMCSA brokerage authority and a $75,000 surety bond, and the federal register shows both. Our office is on Mahaffie Street off 151st.'),
  P('The person who quotes the move is the person who sees it delivered. Open, enclosed, and expedited transport are on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Olathe','15571 S Mahaffie St #658A','Olathe, KS 66062','+19132986699','(913) 298-6699','CT',
 '15571+S+Mahaffie+St+%23658A,+Olathe,+KS+66062','Visit Us','Find Ship Guy in Olathe',
 'Our office is on Mahaffie Street off 151st, a few minutes from the 151st Street exit on 35.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4778.461375407146!2d-94.8031768!3d38.8458328!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x87c0bf0163082725%3A0x31dc156ea3f5a18a!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793024852111!5m2!1sen!2sus', alt=True))

FAQ=[
 ("Do you ship cars for engineers relocating to the GPS campus?","Yes, all year. The headquarters on 151st Street hires engineers from every state. They arrive on start dates in every month. Many ship a car behind the move. The handoff works at a lot on 151st or at the activity center. We provide the paperwork a reimbursed move needs."),
 ("How much does it cost to ship a car from Olathe to Wichita or Dallas?","Wichita runs two hundred ten to three hundred thirty dollars for a sedan. That is about one hundred seventy-five miles down 35. Dallas runs four hundred thirty to six hundred twenty, about five hundred twenty miles on the same road. Olathe prices a few dollars under Kansas City on both, because the southbound carriers reach it first. An SUV or pickup adds 10 to 25 percent."),
 ("Can the carrier come to my street downtown or in a new subdivision?","Downtown, usually not. The square and the old grid are narrow, and the courthouse fills them on weekdays. The driver meets you at a lot off Santa Fe or at the shopping center on the highway. The subdivisions off 151st, Black Bob, and Ridgeview allow the curb. The newest streets in the southwest are not on every map yet, so send the full address."),
 ("Does Old Settlers affect my pickup?","Downtown, yes. The carnival sits on the square for a weekend in September, and the parade closes Santa Fe. We move a downtown pickup that weekend to 151st or the activity center. The rest of the city runs normally."),
 ("Can you ship a car to or from Gardner, Spring Hill, or Lenexa?","Yes, and all three price the same as Olathe. Gardner rides the same carriers off 35 and Old 56 Highway. Spring Hill rides them off 169, and Lenexa rides them off 35 and 435. A lot on the main road works for a handoff. Send the full address for a new subdivision."),
 ("Do you ship cars for the warehouses at the intermodal?","Yes. The intermodal and the warehouses in Gardner and Edgerton bring in managers and technicians from every state. Many ship a second car behind the move. The handoff works at a lot off 35 in Gardner or on Old 56 Highway. We provide the paperwork a reimbursed move needs."),
 ("What happens if an ice storm or a tornado warning hits on my pickup day?","Ice is what stops the trucks here, long before the snow does. The carriers hold at the Gardner truck stops until the salt trucks have run 35. That can cost a day, and we tell you before it does. A tornado warning pauses the loading until it expires. Sirens come a few times every spring, and the driver generally finishes the same afternoon."),
 ("Can you ship a car that does not run from Olathe?","Yes. A winch-equipped carrier is sent, and the loading time is priced into the quote from the start. The activity center lots or a lot on 151st give the driver somewhere flat to winch from. Say whether the wheels turn, the steering works, and the brakes hold."),
 ("Can you time delivery to a student move at the university?","Yes. Cars arrive at the College Boulevard campus each August and leave each May. The community college in Overland Park keeps the same dates. The booking usually comes from a parent, and someone over eighteen signs at a campus lot. We pin the delivery to the move-in date and move it if the date moves."),
 ("What do you need for an Olathe car shipping quote?","The pickup and delivery addresses, with the side of 35 or the town here. Year, make, and model. Whether it runs. Open or enclosed. The week around the start date. Five answers, and the Olathe quote is on its way the same day."),
]
BODY.append(faq_section(FAQ,'Olathe FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Olathe?','The form above takes two minutes and prices the lane. Add the side of 35 and your dates, and the next carrier through takes it.','+19132986699','(913) 298-6699','Get your free Olathe quote'))

build({
 'slug':'auto-transport-olathe-kansas',
 'title':'Car Shipping in Olathe, KS — Auto Transport | Ship Guy',
 'meta':'Car shipping in Olathe, KS, the Johnson County seat on Interstate 35. GPS-campus and hospital relocations, intermodal and warehouse moves, downtown and square meeting spots, southwest-subdivision curbside pickups, Gardner and Spring Hill, Old Settlers weekend, and the ice storms. Local office on Mahaffie Street off 151st. Free quote.',
 'h1':'Car Shipping in<br>Olathe, <span class="accent">Kansas</span>',
 'lede':'Open, enclosed, and expedited auto transport across west Johnson County, planned around 35, K-10, the start date, Old Settlers, and the ice.',
 'tel':'+19132986699','disp':'(913) 298-6699','brand':'Olathe','keyword':'car shipping in olathe',
 'localterms':['olathe','johnson county','county seat','interstate 35','k-10','k-7','us 169','us 56','old 56','santa fe','119th','127th','135th','143rd','151st','159th','167th','175th','ridgeview','mur-len','black bob','pflumm','woodland','lone elm','college boulevard','activity center','interstate 435','downtown','square','courthouse','kansas avenue','park street','old grid','east side','stagecoach','gps campus','north side','southwest','cedar creek','gate','lake','gardner','intermodal','edgerton','spring hill','lenexa','de soto','battery plant','overland park','engineers','avionics','insurance campus','hospital','nurses','physicians','county government','trucking company','warehouses','university','fort leavenworth','orders','old settlers','carnival','parade','county fair','football','fourth of july','tournaments','ice storm','2002','snow','2011 blizzard','sirens','2019','linwood','2003','mill creek','heat','topeka','columbia','wichita','omaha','tulsa','st. louis','oklahoma city','dallas','denver','chicago','lawrence'],
}, BODY, FAQ)
