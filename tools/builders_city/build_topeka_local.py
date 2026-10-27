import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Topeka, Kansas','Car shipping in the state capital, where the Turnpike ends and Interstate 70 runs free to Colorado',
 ['Car shipping in Topeka runs off Interstate 70 and the 470 loop around the south and west sides. Ship Guy is a licensed auto transport broker with an office on Quincy Street downtown, near the Capitol.',
  'We book vetted carriers across Shawnee County, from North Topeka to Lake Shawnee and out to Auburn. We do not own the trucks.',
  'Interstate 70 arrives from Kansas City as the Turnpike and leaves west toll-free toward Salina. Interstate 470 loops the south and west sides. Interstate 335 is the Turnpike south to Emporia and Wichita. US 75 and Topeka Boulevard run north and south. Wanamaker Road is the west-side strip.',
  'This page covers 70, the loop, the Turnpike, downtown, North Topeka, the west side, and the lake. It also covers the state, the hospitals, the plants, the rail shops, the session, and the lanes.'],
 'Topeka at a glance',
 ['Most pickups happen within 1 to 3 days. Every carrier between Kansas City and Denver passes the city on 70. The Wichita trucks come up 335.',
  'Kansas City is an hour. Wichita, Omaha, Columbia, and Lincoln are a same-day haul. St. Louis, Tulsa, and Oklahoma City take a day. Denver, Dallas, and Chicago take one to two, and the coasts take three to five.'],
 'Tell us the side of the river. Downtown, Potwin, and the old west side need a meeting spot. The southwest subdivisions, the lake, and the suburbs usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 70, Interstate 470, the Turnpike, US 75, Topeka Boulevard, and Wanamaker Road',
 prose(
  L('Topeka is where the Turnpike ends and the free interstate begins. The carriers stop here to sort their loads.'),
  P('Interstate 70 crosses the city from the Turnpike gate in the east to the free road west. The exits downtown at 8th, 10th, and Topeka Boulevard sit beside the Capitol. Interstate 470 loops the south and west sides from the east gate to 70 at Wanamaker. Interstate 335 leaves the loop at the south end as the Turnpike to Emporia and Wichita.'),
  P('US 75 runs north and south through the city and the county. It reaches Holton to the north and the lake to the south. Topeka Boulevard is the main street through downtown and across the river. US 24 runs the north side toward Lawrence and Rossville. US 40 and K-4 reach the east and northwest. Kansas Avenue is downtown and the arts district across the river.'),
  P('Wanamaker Road is the west-side strip, with the mall, the hotels, and the big lots. Gage Boulevard runs past the zoo and the park. 21st, 29th, and 37th Streets cross the city east and west. Fairlawn, Burlingame, and Croix carry the southwest. California Avenue and Seward run the east side toward the airport.'),
  P('The carriers come off 70 at Topeka Boulevard and Wanamaker, and off the loop at Gage and Burlingame. The mall on Wanamaker, the expo center, and the lake have the usual meeting lots. The Turnpike is the only toll, and it ends at the city. Interstate 70 west of Topeka is free.'),
  P('Our office is on Quincy Street downtown, a few blocks east of the Capitol.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, Potwin, North Topeka, the West Side, the Southwest, the Lake, and the River Towns',
 prose(
  L('Topeka is a capital city of old brick neighborhoods and a west side that keeps growing toward Wanamaker.'),
  P('Downtown is the Capitol, the state office buildings, and the Kansas Avenue blocks. The streets fill with state workers on weekdays, and the one-way pairs around the Capitol are tight. The driver meets you at the lots on the east side of downtown or at the expo center. The historic district by the Brown v. Board site has narrow streets, and the handoff moves to a lot.'),
  P('Potwin west of downtown is a historic district of Victorian houses on brick streets. Traffic circles sit at every corner. A trailer cannot make the circles. The driver meets you on 6th Street or at the hospital lots. Holliday Park, Westboro, and College Hill by the university are old grids with mature trees. The curb works on some blocks, and a lot off Gage works for the rest.'),
  P('North Topeka across the river has the arts district, the tire plant, and older grids with wide streets. The curb works. Oakland on the east side is an old neighborhood with narrow streets, and the handoff moves to Seward. The west side along Wanamaker and the southwest off 29th are subdivisions from the last forty years. The truck reaches the curb.'),
  P('Lake Shawnee on the southeast is a ring of lake homes and parks. The driver meets you on the lake road. Highland Park and the southeast grids allow the curb. Silver Lake and Rossville to the northwest and Auburn to the south are small towns. Each has lots on its main road. Lawrence sits twenty-five minutes east on the Turnpike. All of them price the same as Topeka.'),
 )))

ROUTES=[("Kansas City, MO","I-70 · ~65 mi","Same day","$140–$230"),("Wichita, KS","I-335/I-35 · ~140 mi","Same day","$190–$300"),
 ("Omaha, NE","US-75/I-29 · ~170 mi","Same day","$200–$310"),("Columbia, MO","I-70 · ~185 mi","Same day","$210–$320"),
 ("Tulsa, OK","US-75 · ~230 mi","1 day","$240–$360"),("Oklahoma City, OK","I-335/I-35 · ~300 mi","1 day","$290–$420"),
 ("St. Louis, MO","I-70 · ~310 mi","1 day","$290–$420"),("Dallas, TX","I-335/I-35 · ~500 mi","1–2 days","$420–$600"),
 ("Denver, CO","I-70 · ~540 mi","1–2 days","$430–$620"),("Chicago, IL","I-70/I-35/I-80 · ~570 mi","1–2 days","$450–$640")]
BODY.append(rate_table('Lanes &amp; Costs','Topeka Car Shipping Lanes and Estimated Costs',
 'The lanes Shawnee County cars take most, with estimated open-trailer ranges. Your exact route prices on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates priced from Topeka, open trailer, sedan that runs. SUVs and pickups land 10 to 25 percent higher, enclosed higher again. Turnpike tolls are built in. Fuel, the week, and the carriers free on your dates fix the final number.',
 prose(
  P('Topeka prices a few dollars under Kansas City on the Denver lane. The westbound carriers pass the door after the Turnpike. The Wichita and Dallas lanes ride 335 and 35 and price with the metro. The Omaha and Tulsa lanes ride US 75 and run lighter, which can add a day.'),
  P('The Sun Belt lanes climb in the fall with the snowbirds and ease in the spring. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The State, the Hospitals, the Tire Plant, the Snack Plants, the Rail Shops, and the Guard',
 prose(
  L('Topeka relocates state employees, nurses, plant managers, and railroaders. The session moves more people than any closing date.'),
  P('The state is the largest employer, and its agencies move staff in from across Kansas. The session runs from January into May, and staffers and lobbyists arrive in January with a car. The insurer downtown, the utility, and the pet-food company relocate staff on their own calendars. We supply the paperwork a reimbursed move needs.'),
  P('The two hospital systems west of downtown bring in nurses all year and residents each June. Physicians arrive with a closing date and a second car. The tire plant in North Topeka and the snack and candy plants move engineers on program schedules. The rail shops move railroaders between terminals.'),
  P('The university on 17th Street brings cars in each August, and a parent ships the car. An adult signs at a campus lot. The university in Lawrence sends overflow through Topeka on the same calendar. Retirees leave for Arizona and Texas each fall and ship the car ahead of them.'),
  P('The air refueling wing at the airport south of town rotates airmen on orders. Fort Riley sits an hour west, and some families settle in Topeka. Orders move one car, and we move the other. Ship Guy is a private broker with no tie to the wing or the post. The <a href="military-car-shipping.html">military</a> page covers the timing. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Session, Fiesta Mexicana, Tulip Time, the Balloon Rally, the River, and the 1966 Tornado',
 prose(
  L('Topeka runs on a legislative session, a July fiesta in Oakland, and a spring that brings the sirens.'),
  P('The session fills the downtown garages and the Capitol blocks from January into May. A downtown handoff on a session day moves to the morning or to the expo center. The expo center fills its lots for the farm show in January and the fairs through the summer. The university fills the lots on 17th on football Saturdays.'),
  P('Fiesta Mexicana fills the Oakland neighborhood for a week in July. The streets around the church close every evening. A pickup on the east side that week moves to Seward or to a lot off 70. Tulip Time fills the lake roads in April, and the balloon rally fills them on a September weekend. The Fourth of July does the same at the lake. Race weekends at the track on Topeka Boulevard back traffic up to the loop.'),
  P('The Kansas River floods. The 1951 flood put North Topeka under water, and the levees have held since. The river still closes the low roads by the arts district in a wet spring. A pickup there moves up the hill for a day. Shunganunga Creek floods the southeast in a big summer storm.'),
  P('The 1966 tornado crossed the city from the southwest through the university and downtown. Sirens go off a few times every spring, and a pickup waits until the warning expires. Ice is the winter problem, and the 2007 storm took the power out for days. Snow runs twenty inches a year. The carriers park at the truck stops by the Turnpike gate until the plows finish. A winter pickup can lose a day.'),
 )+chips(["Downtown","Capitol","Kansas Avenue","Quincy Street","Brown v. Board","Potwin","Holliday Park","Westboro","College Hill","Washburn","Gage Park","North Topeka","NOTO","Oakland","East Side","Seward","California Avenue","Airport","Forbes Field","West Side","Wanamaker","Sherwood","Southwest","29th Street","Burlingame","Fairlawn","Highland Park","Lake Shawnee","Tecumseh","Silver Lake","Rossville","Auburn","Wakarusa","Lawrence"])
 +NOTE('Serving Topeka and all of Shawnee County, brick street or new subdivision. Tell us the side of the river and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Topeka?',
 prose(
  L('Most cars leave Shawnee County on an open trailer, and the lane prices are built around one.'),
  P('An enclosed trailer keeps the salt, the gravel, and the hail off a car. The racers who run the track on Topeka Boulevard book one for the trip home. The collectors in Potwin and Westboro book one for the shows.'),
  P('A commuter car or a fleet sedan rides open and comes off the trailer unchanged. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages weigh the two.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff at the mall or the expo center, and a signature at the far end. The session or the start date sets the week.'),
  P('Say yes to the price, and we book a carrier already running 70 or the Turnpike. The lot and the window come back to you the same day. The driver walks the car with you at pickup and marks its condition on a Bill of Lading. Both signatures go on, and the sheet is compared at delivery.'),
 )+ULI([
  "Take everything personal out of the car, including the trunk",
  "Keep the fuel at about a quarter tank",
  "Photograph every side of the car and the odometer before the truck comes",
  "Give the driver one working key and mention any mechanical problem",
  "Turn off any aftermarket alarm",
  "In Potwin or downtown, meet the truck on 6th Street or at the expo center",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Topeka Drivers Choose Ship Guy',
 prose(
  L('We catch the carriers as they clear the Turnpike gate and sort their loads. We plan around the session, the fiesta, and the ice.'),
  P('Ship Guy holds FMCSA brokerage authority, backed by a $75,000 surety bond. Both are on the federal register. The office is on Quincy Street downtown.'),
  P('The coordinator who quotes the move stays on the phone until the car is signed for. Open, enclosed, and expedited transport are on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Topeka','1035 SE Quincy St #775','Topeka, KS 66612','+17855033373','(785) 503-3373','CT',
 '1035+SE+Quincy+St+%23775,+Topeka,+KS+66612','Visit Us','Find Ship Guy in Topeka',
 'Our office is on Quincy Street downtown, a few blocks east of the Capitol.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4765.084060076955!2d-95.6751063!3d39.044575699999996!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x87bf03c8d6aedb07%3A0x1cd3f770c8417e46!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793024884090!5m2!1sen!2sus'))

FAQ=[
 ("How much does it cost to ship a car from Topeka to Kansas City or Denver?","Kansas City runs one hundred forty to two hundred thirty dollars for a sedan. That is about sixty-five miles down the Turnpike. Denver runs four hundred thirty to six hundred twenty, about five hundred forty miles out 70. Topeka prices a few dollars under Kansas City on the Denver lane. The westbound carriers pass the door. An SUV or pickup adds 10 to 25 percent."),
 ("Can the carrier come to my street in Potwin or downtown?","Usually not. Potwin has brick streets with traffic circles at every corner, and a trailer cannot make them. Downtown is one-way pairs around the Capitol that fill with state workers. The driver meets you on 6th Street, at the hospital lots, or at the expo center. The west side, the southwest, and the lake usually allow the curb."),
 ("Do you ship cars for state employees moving to Topeka?","Yes, every month and especially in January. The agencies pull staff in from every corner of Kansas. The session adds staffers and lobbyists each January. A second car often follows the move. The expo center or a lot on Wanamaker works for the handoff. We provide the paperwork a reimbursed move needs."),
 ("Are the Turnpike tolls in my price?","Yes. A carrier coming from Kansas City or Wichita pays the Turnpike with a transponder. The toll rides inside the quote. There is no separate line. Interstate 70 west of Topeka is free, so the Denver lane carries no toll at all."),
 ("Does Fiesta Mexicana or the session affect my pickup?","In Oakland in July, yes. The streets around the church close every evening for a week. We move an east-side pickup that week to Seward or to a lot off 70. On a session day, a downtown handoff moves to the morning or to the expo center. The rest of the city runs normally."),
 ("Can you ship a car to or from Lawrence, Silver Lake, or Auburn?","Yes, and all three price the same as Topeka. Lawrence rides the same carriers off the Turnpike, and the handoff happens at a lot near campus. Silver Lake and Rossville ride them off US 24, and Auburn rides them off the loop. Send the full address for a new subdivision."),
 ("What happens if an ice storm or a tornado warning hits on my pickup day?","Ice parks the trucks before snow does. The carriers wait at the truck stops by the Turnpike gate until the salt trucks finish. A winter pickup can slip a day. You hear from us first. A tornado warning stops the loading until it lifts, and the sirens sound a few times each spring. The river closes the low roads by the arts district in a wet spring. A pickup there moves up the hill."),
 ("Can you ship a car that does not run from Topeka?","Yes. We dispatch a carrier with a winch. The extra loading time is inside the quote from the start. The mall lot on Wanamaker or the expo center lots give the driver level ground. Tell us whether the car rolls, steers, and brakes."),
 ("Can you time delivery to a student move at Washburn or in Lawrence?","Yes. Washburn takes cars in each August and sends them home in May. The university in Lawrence runs the same calendar. A parent books, and an adult signs at a campus lot. Lawrence has hilly streets near campus, so the handoff happens at a lot nearby. Both windows fill fast, so reserve early."),
 ("What do you need for a Topeka car shipping quote?","The two addresses, down to the side of the river. What the car is, year through model. Whether it starts. Open or enclosed. The week you are aiming for. That is everything, and the Topeka number is back the same day."),
]
BODY.append(faq_section(FAQ,'Topeka FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Topeka?','The form above prices the lane in two minutes. Tell us the side of the river and the week. The next carrier clearing the Turnpike gate takes it.','+17855033373','(785) 503-3373','Get your free Topeka quote'))

build({
 'slug':'auto-transport-topeka-kansas',
 'title':'Car Shipping in Topeka, KS — Auto Transport | Ship Guy',
 'meta':'Car shipping in Topeka, KS, the state capital where the Turnpike ends and Interstate 70 runs free to Denver. State-employee and hospital relocations, downtown and Potwin meeting spots, west side and Lake Shawnee curbside pickups, Lawrence, the session, Fiesta Mexicana, the river, and the ice. Local office on Quincy Street downtown. Free quote.',
 'h1':'Car Shipping in<br>Topeka, <span class="accent">Kansas</span>',
 'lede':'Open, enclosed, and expedited auto transport across Shawnee County, planned around 70, the loop, the Turnpike, the session, and the ice.',
 'tel':'+17855033373','disp':'(785) 503-3373','brand':'Topeka','keyword':'car shipping in topeka',
 'localterms':['topeka','state capital','shawnee county','interstate 70','interstate 470','loop','turnpike','interstate 335','emporia','us 75','topeka boulevard','us 24','us 40','k-4','kansas avenue','wanamaker','gage','21st','29th','37th','fairlawn','burlingame','croix','california avenue','seward','downtown','capitol','state office','one-way','expo center','brown v. board','potwin','brick streets','traffic circles','6th street','holliday park','westboro','college hill','university','north topeka','river','arts district','tire plant','oakland','west side','mall','southwest','lake shawnee','highland park','silver lake','rossville','auburn','wakarusa','lawrence','state','agencies','session','staffers','lobbyists','insurer','utility','pet-food','hospital','nurses','residents','snack plant','candy plant','rail shops','railroaders','retirees','air refueling wing','airport','fort riley','orders','farm show','football','fiesta mexicana','church','tulip time','balloon rally','fourth of july','track','race weekends','1951 flood','levees','shunganunga','1966 tornado','sirens','ice','2007','snow','truck stops','kansas city','wichita','omaha','columbia','tulsa','oklahoma city','st. louis','dallas','denver','chicago','lincoln','salina','holton'],
}, BODY, FAQ)
