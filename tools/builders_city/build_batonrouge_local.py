import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Baton Rouge, Louisiana','Car shipping in the state capital, where Interstate 10 crosses the Mississippi and Interstate 12 begins',
 ['Car shipping in Baton Rouge runs off the 10 and 12 split and the bridge over the river. Ship Guy is a licensed auto transport broker with an office on North 3rd Street downtown.',
  'We book vetted carriers across the capital region, from Zachary to Prairieville and over to Port Allen. The trucks belong to the carriers.',
  'Interstate 10 crosses the Mississippi on the bridge downtown and runs east to New Orleans. Interstate 12 splits off toward Hammond and the coast. Interstate 110 runs north to the Capitol, the refinery, and the airport. Airline Highway, Florida Boulevard, and Siegen Lane carry the rest.',
  'This page covers the bridge, the split, downtown, the old neighborhoods, the LSU side, and the southeast. It also covers the plants, the hospitals, the state, football Saturdays, the 2016 flood, and the lanes.'],
 'Baton Rouge at a glance',
 ['Most pickups happen within 1 to 3 days. Every carrier between Houston and Florida passes the city on 10 or 12. The Dallas trucks come down 49.',
  'New Orleans is ninety minutes. Houston, Jackson, Mobile, and Shreveport are a same-day haul. Dallas, Memphis, and Atlanta take a day. Florida takes two, and Chicago and the coasts take three to four.'],
 'Tell us the side of the split. Downtown, Spanish Town, and the Garden District need a meeting spot. The southeast subdivisions, Prairieville, and Zachary usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 10, Interstate 12, Interstate 110, the Bridge, Airline Highway, and Siegen Lane',
 prose(
  L('Baton Rouge is the one place a carrier crosses the Mississippi between Natchez and New Orleans. The bridge sets the schedule.'),
  P('Interstate 10 comes across the Atchafalaya Basin from Lafayette and crosses the river on the bridge downtown. The bridge backs up every weekday morning and afternoon, and the carriers plan around it. The exits at College, Essen, Bluebonnet, Siegen, and Highland cover the south side. Interstate 12 leaves 10 at the split and runs east past Denham Springs to Hammond.'),
  P('Interstate 110 runs north from the split past the Capitol, the refinery, and the airport to Scotlandville. Airline Highway is US 61, the old road south to Gonzales and north to the airport. The old bridge carries US 190 across the river to Port Allen. Florida Boulevard is US 190 across the city.'),
  P('Government Street, Perkins Road, and Highland Road run from downtown out to the southeast. Nicholson Drive runs along the river past the stadium. College Drive, Bluebonnet, and Siegen Lane cross the south side to the mall and the hospitals on Essen. Sherwood Forest, O’Neal Lane, and Coursey cover the east. Burbank Drive carries the student side.'),
  P('The carriers come off 10 at Siegen and Bluebonnet, and off 12 at Sherwood Forest and O’Neal. The mall on Bluebonnet, the hospital corridor on Essen, and the stadium have the usual meeting lots. No road in the parish charges a toll.'),
  P('Our office is on North 3rd Street downtown, between the riverfront and the Capitol.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, Spanish Town, the Garden District, Mid City, the LSU Side, the Southeast, and the Parishes Around',
 prose(
  L('Baton Rouge is an old river town with a capital in the middle. The subdivisions spread southeast toward Ascension Parish.'),
  P('Downtown is the Capitol, the state office buildings, and the Third Street blocks above the river. The one-way streets fill with state workers on weekdays. The driver meets you at the lots by the riverfront or at the casino lot. Spanish Town and Beauregard Town beside it are historic grids with narrow streets and low oaks. The handoff moves to North Boulevard or to the riverfront.'),
  P('The Garden District and Mid City along Government Street have old houses on narrow streets under live oaks. A trailer cannot get under the limbs. The driver meets you on Government or at the shopping center on Perkins. Old Goodwood, Bocage, and the streets off Jefferson Highway have wider lots. The curb works on most of them.'),
  P('The LSU side south of downtown is the campus, the stadium, and the student blocks off Burbank. The handoff happens at a campus lot or a lot on Burbank, never on a game day. Southdowns and College Town between the campus and Perkins are tight grids. The southeast off Highland, Bluebonnet, and Siegen is the growth side, and the truck reaches the curb. The University Club and the Highland Road estates sit behind gates, and the handoff waits at the gate.'),
  P('Prairieville and Gonzales down Airline are Ascension Parish, the fastest-growing part of the metro. The subdivisions are new, the streets are wide, and the maps lag. Denham Springs and Walker east on 12 are the same. Zachary, Baker, and Central to the north have wide streets and lots on the main roads. Port Allen and Brusly across the bridge price the same as Baton Rouge. So does the rest of the metro.'),
 )))

ROUTES=[("New Orleans, LA","I-10 · ~80 mi","Same day","$160–$260"),("Jackson, MS","I-55 · ~170 mi","Same day","$210–$320"),
 ("Mobile, AL","I-12/I-10 · ~225 mi","Same day","$240–$360"),("Shreveport, LA","I-49 · ~250 mi","Same day","$250–$370"),
 ("Houston, TX","I-10 · ~270 mi","Same day","$250–$380"),("Memphis, TN","I-55 · ~375 mi","1 day","$340–$490"),
 ("Dallas, TX","I-49/I-20 · ~430 mi","1 day","$400–$570"),("Atlanta, GA","I-12/I-65/I-85 · ~535 mi","1–2 days","$440–$630"),
 ("Orlando, FL","I-10/I-75 · ~720 mi","2 days","$520–$750"),("Chicago, IL","I-55 · ~860 mi","2–3 days","$620–$870")]
BODY.append(rate_table('Lanes &amp; Costs','Baton Rouge Car Shipping Lanes and Estimated Costs',
 'The lanes capital-region cars take most, with estimated open-trailer ranges. Your exact route prices on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates priced from Baton Rouge, running sedan, open trailer. SUVs and pickups add 10 to 25 percent, and an enclosed trailer adds more. Storm season and the carriers free on your dates set the real number.',
 prose(
  P('Baton Rouge prices with New Orleans on every lane. The two cities share one carrier pool along 10. The Houston lane runs daily and prices the lowest per mile. The Dallas lane rides 49 and 20 through Shreveport. The Florida lanes run full in both directions on the snowbird calendar.'),
  P('A storm in the Gulf pulls the carriers off the coast for a week and moves every price. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Plants, the Hospitals, the State, the Campuses, and the Contractors',
 prose(
  L('Baton Rouge relocates plant engineers, nurses, state employees, and students. The petrochemical corridor moves more people than anyone.'),
  P('The refinery on the north side is one of the largest in the country. The chemical plants line the river from here to New Orleans. They move engineers, operators, and contractors in on turnaround and project schedules. The industrial contractors headquartered in town move crews the same way. We supply the paperwork a reimbursed move needs.'),
  P('The hospitals on Essen Lane and the women’s hospital bring in nurses all year and residents each June. Physicians arrive with a closing date and a second car. The state is the other big employer. The session fills downtown with staffers and lobbyists from spring into June.'),
  P('The university brings tens of thousands of students in each August and sends them home in May. Many ship a car from Texas, Florida, or the East Coast. A parent books, and an adult signs at a campus lot. The handoff never happens on a football Saturday. The university on the north side runs the same calendar. The home-office companies in town, from the billboard company to the chicken-finger chain, move managers in every month.'),
  P('Transplants arrive from Houston and New Orleans on closing dates in Prairieville and Zachary. One car ships while the other is driven. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Football Saturdays, Spanish Town Mardi Gras, the Session, the 2016 Flood, and the Hurricanes',
 prose(
  L('Baton Rouge runs on seven football Saturdays, a Mardi Gras parade, and a six-month storm season.'),
  P('Home football Saturdays bring a hundred thousand people to the stadium. The streets south of downtown close from the morning. Nicholson, Burbank, and Highland gridlock until midnight. A pickup anywhere near campus moves to a weekday. The Spanish Town parade on the Saturday before Mardi Gras fills downtown. The other parades close Government and Perkins on the weekends before it.'),
  P('The session fills the downtown garages from spring into June. The blues festival and the book festival close the downtown blocks for a weekend each. Graduation in May sends cars out in every direction. A handoff downtown on any of those days moves to the morning or to the riverfront lots.'),
  P('Hurricane season runs from June through November. Gustav crossed the city in 2008 and took the power out for weeks. Ida did the same in 2021. When a storm enters the Gulf, the carriers pull back from the coast days before landfall. Contraflow on 10 stops everything else. Sailings resume the week after, and so do we.'),
  P('The 2016 flood came from rain, not the Gulf. Two feet fell in three days. The Amite and Comite put Denham Springs, Central, and the east-side subdivisions under water. A carrier will not stage on a flooded street. The basin bridge west of town closes in fog, and the Mississippi runs high every spring. Summer heat and humidity move the loading hour to the morning. The 2021 freeze iced the bridge for two days.'),
 )+chips(["Downtown","Third Street","Capitol","Riverfront","Spanish Town","Beauregard Town","Garden District","Mid City","Government Street","Capital Heights","Old Goodwood","Bocage","Jefferson Highway","Broadmoor","Sherwood Forest","Shenandoah","LSU","Tiger Stadium","Nicholson","Burbank","Southdowns","College Town","Highland Road","Bluebonnet","Siegen","Essen","Scotlandville","Zachary","Baker","Central","Denham Springs","Walker","Prairieville","Gonzales","Port Allen","Brusly"])
 +NOTE('Serving Baton Rouge and the whole capital region, East Baton Rouge, Ascension, Livingston, and West Baton Rouge. Tell us the side of the split and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Baton Rouge?',
 prose(
  L('Most cars leave the capital region on an open trailer, and the lane prices are built around one.'),
  P('An enclosed trailer keeps a car out of the rain, the road grime, and the salt air. Collectors in Bocage and on Highland Road book one for the show cars. Parents shipping a new car to a student from Texas book one too.'),
  P('A commuter car or a plant truck rides open and arrives in the shape it left. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages weigh the two.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A number, a meeting spot at the mall or on Essen, and a signature at delivery. The turnaround or the move-in date sets the week.'),
  P('Once the number works for you, we put the car on a carrier already working 10. The lot and the pickup window follow the same day. At pickup the driver and you go over the car panel by panel. The Bill of Lading records what you find. Both signatures go on it, and the far end is checked against it.'),
 )+ULI([
  "Take everything personal out of the cabin and the trunk",
  "Keep the fuel around a quarter tank",
  "Photograph every side of the car before the truck arrives",
  "Give the driver one working key and say what the car does wrong",
  "Disarm any aftermarket alarm",
  "In the Garden District or Spanish Town, meet the truck on Government Street or at the riverfront",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Baton Rouge Drivers Choose Ship Guy',
 prose(
  L('We book the carriers already running 10 between Houston and New Orleans. We plan around the bridge, the football Saturdays, and the storms.'),
  P('Ship Guy holds active FMCSA brokerage authority and a $75,000 surety bond. Both are listed in the federal register. Our office is on North 3rd Street downtown.'),
  P('The coordinator who quotes the move is the one who closes it. Open, enclosed, and expedited transport are on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Baton Rouge','440 N 3rd St #229B','Baton Rouge, LA 70802','+12254358297','(225) 435-8297','CT',
 '440+N+3rd+St+%23229B,+Baton+Rouge,+LA+70802','Visit Us','Find Ship Guy in Baton Rouge',
 'Our office is on North 3rd Street downtown, between the riverfront and the Capitol.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5289.084807272352!2d-91.1878552!3d30.451049599999994!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8626a1ec3ff4e2e1%3A0xcdff351873abb3be!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793025006393!5m2!1sen!2sus'))

FAQ=[
 ("How much does it cost to ship a car from Baton Rouge to Houston or Dallas?","Houston runs two hundred fifty to three hundred eighty dollars for a sedan. That is about two hundred seventy miles down 10. Dallas runs four hundred to five hundred seventy, about four hundred thirty miles up 49 and 20. New Orleans is ninety minutes away and the least expensive lane of the three. Add 10 to 25 percent for an SUV or a pickup. All three run every day."),
 ("Can the carrier come to my street in the Garden District or Spanish Town?","Usually not. Both have narrow streets under live oaks, and a trailer cannot get under the limbs. The driver meets you on Government Street, on North Boulevard, or at the riverfront lots. The southeast subdivisions, Prairieville, and Zachary usually allow the curb."),
 ("Do you ship cars for people relocating to the plants or the hospitals?","Yes, all year. The refinery and the chemical plants along the river move engineers and contractors in on project schedules. The hospitals on Essen bring in nurses, residents, and physicians every month. Many ship a second car behind the move. The handoff works at the mall lot or on Essen. We provide the paperwork a reimbursed move needs."),
 ("Can you ship my student’s car to LSU?","Yes, and it is the move we make most each August. Cars come from Texas, Florida, and the East Coast. A parent books, and an adult signs at a campus lot or a lot on Burbank. We never schedule a campus handoff on a football Saturday. Graduation in May sends the cars home the same way."),
 ("Does a football Saturday affect my pickup?","South of downtown, yes. A hundred thousand people fill the stadium, and Nicholson, Burbank, and Highland close from the morning. We move any pickup near campus to a weekday. The rest of the parish runs normally, and the carriers stay on 10 and 12."),
 ("Can you ship a car to or from Prairieville, Denham Springs, or Zachary?","Yes, and all three price the same as Baton Rouge. Prairieville rides the same carriers off 10 and Airline. Denham Springs rides them off 12, and Zachary rides them off 110 and Highway 19. The subdivisions are new and the maps lag, so send the full address."),
 ("What happens if a hurricane is in the Gulf on my pickup day?","Nothing moves on the coast in the last three days before landfall. Contraflow on 10 shuts the rest. The pickup rebooks for the week after the storm clears. A car already on a trailer keeps heading inland. Rain is the other risk here, since a stalled storm floods the east-side subdivisions. No carrier stages on a flooded street. Every change reaches you by phone."),
 ("Can you ship a car that does not run from Baton Rouge?","Yes. We send a carrier with a winch, and the quote carries the loading time from the first number. The mall lot on Bluebonnet or a lot on Siegen gives the driver flat ground to work on. Tell us whether the car rolls, steers, and brakes."),
 ("Does the bridge or the basin add time?","Sometimes. The bridge downtown backs up every weekday morning and afternoon, and the carriers plan around it. The basin bridge west of town closes in fog and after accidents, with no quick detour. We build a cushion into windows that cross either one. A pickup on the east side of the split avoids both."),
 ("What do you need for a Baton Rouge car shipping quote?","Both addresses, with the side of the split or the parish here. Year, make, and model. Whether it runs. Open or enclosed. The week around the turnaround or the move-in date. Those five answers are the whole request, and the Baton Rouge number is back within the day."),
]
BODY.append(faq_section(FAQ,'Baton Rouge FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Baton Rouge?','The form above prices the lane in two minutes. Add the side of the split and the week, and the next carrier along 10 takes it.','+12254358297','(225) 435-8297','Get your free Baton Rouge quote'))

build({
 'slug':'auto-transport-baton-rouge-louisiana',
 'title':'Car Shipping in Baton Rouge, LA — Auto Transport | Ship Guy',
 'meta':'Car shipping in Baton Rouge, LA, the state capital where Interstate 10 crosses the Mississippi. Plant and hospital relocations, LSU student moves, downtown and Garden District meeting spots, southeast and Prairieville curbside pickups, football Saturdays, the session, the 2016 flood, and hurricane season. Local office on North 3rd Street downtown. Free quote.',
 'h1':'Car Shipping in<br>Baton Rouge, <span class="accent">Louisiana</span>',
 'lede':'Open, enclosed, and expedited auto transport across the capital region, planned around 10, 12, the bridge, football Saturdays, and the storms.',
 'tel':'+12254358297','disp':'(225) 435-8297','brand':'Baton Rouge','keyword':'car shipping in baton rouge',
 'localterms':['baton rouge','state capital','interstate 10','interstate 12','interstate 110','split','bridge','mississippi','atchafalaya','basin','airline highway','us 61','old bridge','us 190','florida boulevard','government street','perkins','highland road','nicholson','college drive','bluebonnet','siegen','essen','sherwood forest','o’neal','coursey','burbank','downtown','capitol','third street','riverfront','casino','spanish town','beauregard town','north boulevard','garden district','mid city','live oaks','old goodwood','bocage','jefferson highway','lsu','campus','stadium','student','southdowns','college town','southeast','university club','gate','prairieville','gonzales','ascension','denham springs','walker','zachary','baker','central','scotlandville','port allen','brusly','refinery','chemical plants','turnaround','contractors','hospitals','women’s hospital','nurses','residents','state','session','staffers','lobbyists','billboard','chicken-finger','transplants','closing date','football saturdays','mardi gras','parade','blues festival','book festival','graduation','hurricane','gustav','2008','ida','2021','contraflow','2016 flood','amite','comite','fog','2021 freeze','humidity','new orleans','jackson','mobile','shreveport','houston','memphis','dallas','atlanta','orlando','chicago','lafayette','hammond','natchez'],
}, BODY, FAQ)
