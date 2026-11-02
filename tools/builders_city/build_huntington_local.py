import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("2–4 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Huntington, West Virginia','Car shipping on the Ohio River, where Interstate 64 carries the trucks, three bridges cross to Ohio, and the university sets the calendar',
 ['Car shipping in Huntington runs on Interstate 64, which passes south of the city between Charleston and Lexington. Ship Guy is a licensed auto transport broker with an office on 5th Avenue downtown.',
  'We book vetted carriers across Huntington, from the West End to Guyandotte and out to Barboursville and Kenova. The trucks belong to the carriers. The license and the bond are held by Ship Guy.',
  'Interstate 64 runs from Charleston through the hills south of town to Kentucky. Route 60 is the long east-west street through the city. Route 52 crosses the river west of town and runs south as the Tolsia Highway. Route 2 follows the river north. Route 10 climbs south from the campus to Logan.',
  'This page covers 64, Route 60, the bridges, the river, downtown, the campus, and the South Side. It covers the university, the hospitals, the port, the rail shops, the floodwall, the ice, and the fog.'],
 'Huntington at a glance',
 ['Count on 2 to 4 days for a pickup. Huntington sits on 64 between Charleston and Lexington. The carriers between the East Coast and the Ohio Valley pass through a few times a week. The pool is modest, and the window stretches when the ice closes the hills.',
  'Charleston, Lexington, Cincinnati, Columbus, and Louisville ride a single day on the truck. Dayton, Pittsburgh, and Cleveland take a day. Charlotte takes a day too, and Atlanta takes one to two.'],
 'Tell us the neighborhood. Downtown, the campus, the South Side hills, and the bridge approaches meet the truck on a main road. The grids east and west, Highlawn, Westmoreland, Barboursville, and the river towns usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 64, Route 60, Route 52, Route 2, Route 10, 3rd Avenue, 5th Avenue, Hal Greer Boulevard, and the Three Bridges',
 prose(
  L('Huntington is a long flat grid between the river and the hills. The interstate runs in the hills, and three bridges cross to Ohio. A carrier comes down off 64 and stays on the flat avenues.'),
  P('Interstate 64 comes from Charleston through the hills south of the city and leaves west into Kentucky. The exits drop into town on 5th Street Road, Hal Greer Boulevard, 29th Street, and Route 60. The mall exit in Barboursville and the Milton exit serve the east. Route 60 runs the length of the city on 3rd and 5th Avenues and on to Barboursville. Route 52 crosses the West End bridge to Chesapeake. It runs south as the Tolsia Highway to the airport and Kenova. Route 2 follows the river north toward Point Pleasant. Route 10 climbs from the campus south into the coalfields.'),
  P('The three bridges carry the city to Ohio. The West End bridge carries 52, and the downtown bridge carries the office traffic to Chesapeake. The East End bridge at 31st Street carries Proctorville. A trailer uses the West End bridge and avoids the downtown one. 3rd and 5th Avenues are the one-way pair through downtown and past the campus. Hal Greer runs from the campus south under 64. 8th Street climbs the South Side to Ritter Park.'),
  P('The carriers come off 64 at Hal Greer and 29th Street. They meet at the big-box lots on Route 60 and the mall lots in Barboursville. The lots at the stadium work outside a Saturday. So do the lots at the civic arena downtown and the lots on 5th Avenue past the campus. The airport is fifteen minutes west on 52 for a fly-and-ship.'),
  P('Our office is on 5th Avenue downtown, two blocks from Pullman Square and a short walk from Marshall.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the Campus, the South Side, Ritter Park, Highlawn, Guyandotte, the West End, Westmoreland, Barboursville, and the River Towns',
 prose(
  L('Huntington is a numbered grid along the river, with a university in the middle and hills behind. The truck meets the hills on a main road and the grid at the curb.'),
  P('Downtown runs from the river to 8th Avenue, brick blocks around Pullman Square and the civic arena. The driver meets you on 3rd Avenue or at the arena lots. The campus blocks from 16th to 20th Street are student rentals with cars on both curbs. The handoff happens at the lots on 5th Avenue or on Hal Greer. The South Side climbs from 8th Avenue to the park on steep streets. A trailer does not stop on the grade. The handoff moves to 8th Street or the park lots.'),
  P('Highlawn east of the campus is a grid of old houses around the hospital. The curb works where the hospital traffic allows. Guyandotte at the mouth of the river is the oldest part of town, small streets that flood. The handoff happens on Route 60. The West End around the alloy plant is a working grid, and the curb works. Westmoreland across the creek is the same.'),
  P('Barboursville along 60 is subdivisions and the mall. The truck comes to the house on most of it. Milton farther out is the same. Kenova and Ceredo at the Kentucky line are river grids, and the curb works. Across the bridges, Chesapeake and Proctorville are river towns on Ohio 7. The handoff happens on the highway.'),
  P('Barboursville, Kenova, Ceredo, and the Ohio river towns ship with the same trucks and price as Huntington. Ashland and Ironton do too. Charleston is an hour up 64 and shares the pool. Logan and the coalfield towns add an hour on the truck and a figure.'),
 )))

ROUTES=[("Charleston, WV","I-64 · ~50 mi","Same day","$120–$200"),("Lexington, KY","I-64 · ~125 mi","Same day","$200–$320"),
 ("Columbus, OH","US-52/US-23 · ~155 mi","Same day","$220–$340"),("Cincinnati, OH","US-52/OH-32 · ~160 mi","Same day","$220–$340"),
 ("Louisville, KY","I-64 · ~200 mi","Same day","$250–$380"),("Dayton, OH","US-23/I-71 · ~205 mi","1 day","$250–$380"),
 ("Pittsburgh, PA","I-64/I-79 · ~270 mi","1 day","$280–$410"),("Cleveland, OH","US-23/I-71 · ~290 mi","1 day","$280–$410"),
 ("Charlotte, NC","I-64/I-77 · ~300 mi","1 day","$300–$440"),("Atlanta, GA","I-64/I-75 · ~520 mi","1–2 days","$440–$630")]
BODY.append(rate_table('Lanes &amp; Costs','Huntington Car Shipping Lanes and Estimated Costs',
 'The lanes Cabell County cars run most, each with an open-trailer range. Your own lane gets a figure on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Huntington for a sedan that runs on an open trailer. SUVs and pickups come in 10 to 25 percent higher, and enclosed higher than that. The week and the carriers on 64 that week set the actual figure.',
 prose(
  P('Huntington prices with Charleston on most lanes, because the same 64 carriers serve both cities. The Lexington and Louisville lanes ride 64 west and fill every day. The Columbus and Cincinnati lanes ride 23 and 52 up the river. The Charlotte lane rides 64 to 77 through the mountains and thins in winter. The Florida lane fills each fall with the retirees and the students’ parents.'),
  P('A mid-August move-in at the university or a residency start in June means a busy week. The <a href="car-shipping-cost.html">cost guide</a> goes through size, condition, and timing one at a time.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The University, the Two Hospitals, the Medical School, the Port, the Rail Shops, the Alloy Plant, the Refinery, and the Steel Mill',
 prose(
  L('Huntington relocates students, residents, nurses, engineers, and railroaders. The university moves the most.'),
  P('Marshall University in the middle of the city takes thirteen thousand students, and the cars arrive in mid-August. A parent books, and an adult signs at the lots on 5th Avenue. The cars head home in May. The medical school across from the hospital brings residents each June. The two hospitals on Hal Greer and in Highlawn are the largest employers in the city. They hire traveling nurses from across the region year round.'),
  P('The port along the river moves more tonnage than almost any inland port in the country. The barge lines and the terminals relocate people from the Gulf. The rail shops east of town rebuild locomotives and bring railroaders from across the system. The alloy plant in the West End hires engineers from Pittsburgh and Ohio. The refinery across the river in Kentucky and the new steel mill upriver are hiring on start dates. The handoff happens in the lot closest to the job.'),
  P('The Guard units in the county rotate people on orders, and the handoff happens at the armory lots. Ship Guy is a private broker, unconnected to the Guard. How a set of orders shapes the dates is on the <a href="military-car-shipping.html">military</a> page.'),
  P('Retirees come back to the river from Ohio and go to Florida in the winter. Three states meet here, and the <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the paperwork for crossing a line.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Move-In Week, Football Saturdays, the November Memorial, the Hot Dog Festival, Chilifest, the Floods, the Ice, the Fog, and the Derecho',
 prose(
  L('Huntington runs on a university calendar and a river calendar. The weather problem is a river that floods, hills that ice, and a fog that closes the bridges.'),
  P('Move-in week in mid-August fills the campus blocks and 5th Avenue. Football Saturdays close the streets around the stadium from the morning on. The memorial on November 14 fills the campus for the plane crash of 1970. It closes the blocks around the fountain. The hot dog festival closes downtown for a Saturday in July, and Chilifest does the same in September. Three weeks of notice covers a mid-August date or a home Saturday.'),
  P('The 1937 flood put the whole city under water, and the floodwall built after it has held since. Guyandotte and the creek bottoms on the South Side still flood in a wet spring. A flood watch moves the handoff up to Route 60 or the mall. Ice closes 64 through the hills every winter for a day or two. The carriers wait in Charleston or Ashland until the salt trucks finish. River fog settles on the bridges and the interstate on fall mornings. A driver waits for it to lift.'),
  P('The June 2012 derecho crossed the city with hurricane winds and took the power for a week. A severe thunderstorm warning holds the truck at the lot until it passes. Summer brings heat and humidity in the river valley, and a driver loads in the morning.'),
  P('A snowstorm over the mountains closes the Charlotte lane for a few days. The car waits in Charleston or rides the Lexington lane instead. We call before the day moves.'),
 )+chips(["Downtown","Pullman Square","The Campus","The South Side","Ritter Park","Enslow Park","Highlawn","Guyandotte","Altizer","The West End","Westmoreland","Spring Valley","Barboursville","Milton","Pea Ridge","Ona","Lesage","Kenova","Ceredo","Chesapeake","Proctorville","Ashland","Ironton"])
 +NOTE('Serving Huntington, Cabell County, and the Tri-State, Highlawn curb or Barboursville cul-de-sac. Say which neighborhood and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Huntington?',
 prose(
  L('The Tri-State ships open nearly every time, and the table above is built on an open trailer.'),
  P('Enclosed keeps the road salt, the coal dust, and the river grit off the paint. The collectors on the South Side book it. So do the engineers moving a car they would not risk on the hills. When ice is coming and only an open truck runs 64 that week, we say so up front. The choice is yours.'),
  P('A commuter car or a student’s sedan is fine open. What separates the two is on the <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A figure, a lot on Route 60, and a signature at delivery, in that order. The move-in or the start date picks the week.'),
  P('Approve the figure, and a carrier already on 64 that week is assigned the car. The lot and the window are set that day. The driver photographs the car at pickup and lists its condition on the Bill of Lading. You initial it there, and the same sheet is the check at delivery.'),
 )+ULI([
  "Everything personal out of the cabin and the trunk",
  "A quarter tank of fuel or under",
  "Each side and the odometer in your own photos before pickup",
  "A good key and a word about anything that does not work",
  "Aftermarket alarms shut off",
  "On the campus blocks, the South Side hills, or a bridge approach, expect a lot on Route 60",
 ])+prose(P('Read <a href="how-it-works.html">how it works</a> for the order of things and <a href="car-shipping-preparation.html">preparation</a> for the morning the truck comes.'))))

BODY.append(sec('Why Ship Guy','Why Huntington Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already run 64 each week. We know which bridge a trailer uses and which mornings the fog holds it.'),
  P('Our FMCSA license and our $75,000 bond are on file in the federal register for anyone to see. The office is on 5th Avenue downtown.'),
  P('A single coordinator carries your move from the quote to the delivery call. The <a href="services.html">services</a> page sets out open, enclosed, and expedited.'),
 )))

BODY.append(office('Huntington','1000 5th Ave #438','Huntington, WV 25701','+13046895163','(304) 689-5163','ET',
 '1000+5th+Ave+%23438,+Huntington,+WV+25701','Visit Us','Find Ship Guy in Huntington',
 'Our office is on 5th Avenue downtown, two blocks from Pullman Square and a short walk from Marshall.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3858.5559903975054!2d-82.44091449999999!3d38.4202419!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x88460928ca491695%3A0x69c5291a520b659!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793628961277!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Huntington to Columbus or Charlotte?","Columbus runs two hundred twenty to three hundred forty dollars for a sedan. That is about one hundred fifty-five miles up 52 and 23. Charlotte runs three hundred to four hundred forty, about three hundred miles through the mountains. Charleston is the lowest lane on the table, fifty miles up 64. For an SUV or a pickup, add 10 to 25 percent."),
 ("Why does a Huntington pickup take 2 to 4 days instead of 1 to 3?","Because the pool is modest. The 64 carriers pass a few times a week. A car rides the next one with space. Lexington and Louisville trucks come most often. Ice over the hills or fog on the bridges stretches the window further. We tell you when it does."),
 ("Can you deliver on a Marshall University move-in date?","Yes. Cars arrive in mid-August and leave in May. A parent books, and anyone over eighteen signs at the lot. The campus blocks are full that week. The meeting point is the lots on 5th Avenue or Hal Greer. The date decides the window. Huntington allows curbside on most streets, but not those."),
 ("Can the carrier come to my street on the South Side or in Guyandotte?","The South Side, no. The streets climb to the park, and a loaded trailer does not stop on the grade. The driver meets you on 8th Street or at the park lots. Guyandotte floods and the streets are small, so the handoff happens on Route 60. Highlawn, the West End, Westmoreland, and Barboursville usually allow the curb."),
 ("What happens if ice closes 64 or fog closes the bridges on my pickup day?","The truck waits in Charleston or Ashland until the salt trucks finish, usually a day. Fog lifts by late morning, and the driver comes then. We phone the moment the forecast turns, and the pickup moves to the first clear morning. The figure stays put."),
 ("Do you ship cars for the hospitals, the port, or the rail shops?","Yes, in every season. The two hospitals bring residents each June and traveling nurses all year. The port, the rail shops, the alloy plant, and the refinery relocate people on start dates. The handoff happens at the lots nearest the site. If the employer covers the move, we write it up the way it wants."),
 ("Can you ship a car to or from Barboursville, Kenova, Ashland, or Charleston?","Yes. Barboursville, Milton, Kenova, Ceredo, and the Ohio river towns ride the same carriers and price as Huntington. Ashland and Ironton do too. Charleston is an hour up 64 and shares the pool. Logan and the coalfield towns add an hour on the truck and a figure."),
 ("What happens on a football Saturday or during the November memorial?","The campus closes. The streets around the stadium fill from the morning on a home Saturday. The memorial on November 14 closes the blocks around the fountain. The handoff moves to the Route 60 lots or the mall, and the figure does not change."),
 ("Can you ship a car that does not run from Huntington?","Yes. The carrier arrives with a winch, and the loading time is part of the figure. The big-box lots on Route 60 and the mall lots in Barboursville are flat. Tell us if it rolls, if it steers, and if it brakes."),
 ("What do you need for a Huntington car shipping quote?","The pickup and delivery addresses, with the neighborhood or the river town. The vehicle and whether it runs. Open or enclosed, and the week around the move-in or the start date. Give us those, and the Huntington figure comes back the same day."),
]
BODY.append(faq_section(FAQ,'Huntington FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Huntington?','Two minutes on the form above returns a Huntington figure for your lane. Name the neighborhood and the week, and the next carrier on 64 takes the car.','+13046895163','(304) 689-5163','Get your free Huntington quote'))

build({
 'slug':'auto-transport-huntington-west-virginia',
 'title':'Car Shipping in Huntington, WV — Auto Transport | Ship Guy',
 'meta':'Car shipping in Huntington, WV, on the Ohio River along Interstate 64. Marshall University move-in dates, hospital and medical-school hires, the port, the rail shops, and the plants, main-road handoffs for the campus blocks and the South Side hills, curbside pickups in Highlawn, the West End, and Barboursville, the ice, the fog, and the floods. Local office on 5th Avenue downtown. Free quote.',
 'h1':'Car Shipping in<br>Huntington, <span class="accent">West Virginia</span>',
 'lede':'Open, enclosed, and expedited auto transport across Huntington and the Tri-State, planned around Interstate 64, the campus dates, the start dates, the ice, the fog, and the river.',
 'tel':'+13046895163','disp':'(304) 689-5163','brand':'Huntington','keyword':'car shipping in huntington',
 'localterms':['huntington','ohio river','interstate 64','route 60','route 52','tolsia','route 2','route 10','3rd avenue','5th avenue','hal greer','29th street','5th street road','8th street','three bridges','west end bridge','downtown bridge','east end bridge','31st street','chesapeake','proctorville','point pleasant','coalfields','logan','mall','barboursville','milton','kenova','ceredo','ashland','ironton','charleston','pullman square','civic arena','stadium','downtown','campus','south side','ritter park','enslow park','highlawn','guyandotte','altizer','west end','westmoreland','spring valley','pea ridge','ona','lesage','tri-state','cabell county','marshall','university','thirteen thousand','students','medical school','residents','two hospitals','largest employers','traveling nurses','port','tonnage','barge','terminals','gulf','rail shops','locomotives','railroaders','alloy plant','engineers','pittsburgh','refinery','kentucky','steel mill','upriver','guard','armory','orders','retirees','florida','move-in','football saturdays','memorial','november 14','plane crash','1970','fountain','hot dog festival','chilifest','1937','flood','floodwall','creek bottoms','ice','salt trucks','fog','bridges','june 2012','derecho','hurricane winds','humidity','mountains','snowstorm','coal dust','grit','lexington','columbus','cincinnati','louisville','dayton','cleveland','charlotte','atlanta','airport','ohio 7','bill of lading','fmcsa','winch','fly-and-ship'],
}, BODY, FAQ)
