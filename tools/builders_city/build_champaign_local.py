import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Champaign, Illinois','Car shipping in a university town, where Interstate 57 crosses Interstate 74 on the prairie',
 ['Car shipping in Champaign runs off the 57 and 74 interchange on the northwest corner of the city. Ship Guy is a licensed auto transport broker with an office on South Neil Street near campus.',
  'We arrange vetted carriers across Champaign County, from Urbana and Savoy to Mahomet and Rantoul. We own none of the trucks.',
  'Interstate 57 runs the west side on its way from Chicago to Memphis. Interstate 74 crosses the north side between Peoria and Indianapolis. Interstate 72 begins at 57 and runs west to Springfield. Neil Street, Prospect Avenue, Springfield Avenue, and University Avenue carry the two cities.',
  'This page covers the interstates, Neil and Prospect, downtown, Campustown, the west side, Urbana, and Savoy. It also covers move-in weekend, the hospital, the research park, football Saturdays, the wind, and the lanes.'],
 'Champaign at a glance',
 ['Most pickups happen within 1 to 3 days, and faster in August. Carriers running 57 between Chicago and Memphis and 74 between Indianapolis and Peoria pass the interchange.',
  'Indianapolis, Chicago, Springfield, and St. Louis are all a same-day haul. Louisville, Nashville, and Milwaukee take a day. Atlanta and the East Coast take two, and the West Coast takes four or five.'],
 'Tell us the side of Neil Street. Downtown and Campustown need a meeting spot. The west side, the southwest subdivisions, and Savoy usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 57, Interstate 74, Interstate 72, Neil Street, and Prospect Avenue',
 prose(
  L('Champaign is the one interchange on the prairie that every north-south and east-west carrier in central Illinois passes.'),
  P('Interstate 57 runs along the west side of the city from Chicago to Memphis. The exits at Curtis Road, Springfield Avenue, and University Avenue serve the city. The big interchange with 74 sits on the northwest corner. Interstate 74 crosses the north side with exits at Prospect, Neil, Lincoln, and Cunningham. Interstate 72 begins at 57 and runs west to Decatur and Springfield.'),
  P('Neil Street is the spine of Champaign. It runs from the mall at 74 through downtown to the campus and on to Savoy. Prospect Avenue runs parallel a mile west, past the retail strip and the hospital. Mattis Avenue and Duncan Road carry the west side. Lincoln Avenue and Cunningham Avenue are the Urbana side.'),
  P('Springfield Avenue, University Avenue, Green Street, and Kirby Avenue cross both cities east and west. Kirby becomes Florida Avenue in Urbana. Windsor Road and Curtis Road run the south side past the new subdivisions. Bradley Avenue and Olympian Drive cross the north. The airport sits south of Savoy off Route 45.'),
  P('The carriers come off 57 at Springfield Avenue and Curtis, and off 74 at Neil and Prospect. The mall, the arena on First Street, and the shopping centers on Prospect have the usual meeting lots. No road in Champaign County charges a toll.'),
  P('Our office is on South Neil Street, between downtown and the arena.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, Campustown, the West Side, the Southwest, Urbana, Savoy, and the Towns Around',
 prose(
  L('Champaign and Urbana are two cities around one campus. The campus sets the rules for the streets between them.'),
  P('Downtown Champaign is a grid of one-way streets around Neil and Main, full of restaurants and bars. A trailer cannot stop on Neil or Main. The driver meets you at the lots by the station or on the edge by Springfield Avenue. Campustown along Green Street is high-rises and no-stopping zones. The handoff moves to the arena lots on First Street or to a campus lot.'),
  P('The west side along Mattis, Springfield, and John Street is postwar grids with wide streets. The curb works on most blocks. The southwest off Curtis, Duncan, and Windsor is the newest growth, with subdivisions out to the interstate. The truck reaches the curb. Savoy south of the campus is its own village, with subdivisions and the airport. The curb works there too.'),
  P('Urbana east of the campus has its own downtown along Main and Race, the courthouse, and the hospital. The streets by the courthouse are narrow. The driver meets you at the hospital lots or on Cunningham. East Urbana and the Philo Road grids allow the curb. The north side of both cities along Bradley and Olympian is older grids and warehouses. A lot off 74 works.'),
  P('Mahomet west on 74 is the fastest-growing town in the county, with subdivisions around the lake. The driver meets you at a lot off the interstate or in town. Rantoul to the north is the old air base town, with wide streets and the old flight line. St. Joseph, Tolono, and Monticello are small towns with lots on every main road. All of them price the same as Champaign, and so does Urbana.'),
 )))

ROUTES=[("Springfield, IL","I-72 · ~90 mi","Same day","$150–$240"),("Indianapolis, IN","I-74 · ~120 mi","Same day","$170–$270"),
 ("Chicago, IL","I-57 · ~135 mi","Same day","$180–$290"),("St. Louis, MO","I-72/I-55 · ~180 mi","Same day","$210–$320"),
 ("Louisville, KY","I-74/I-65 · ~235 mi","1 day","$240–$360"),("Nashville, TN","I-57/I-24 · ~360 mi","1 day","$330–$480"),
 ("Atlanta, GA","I-57/I-24/I-75 · ~560 mi","1–2 days","$460–$650"),("New York, NY","I-74/I-70/I-76 · ~830 mi","2–3 days","$600–$850"),
 ("Dallas, TX","I-57/I-44 · ~800 mi","2 days","$580–$830"),("Los Angeles, CA","I-57/I-44/I-40 · ~1,950 mi","4–5 days","$1,150–$1,600")]
BODY.append(rate_table('Lanes &amp; Costs','Champaign Car Shipping Lanes and Estimated Costs',
 'The lanes Champaign County cars take most, with estimated open-trailer ranges. Your exact route prices on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates out of Champaign for a sedan that starts, open trailer. SUVs and pickups run 10 to 25 percent higher, and an enclosed trailer higher still. August prices sit above the rest of the year. Fuel and the carriers free on your dates set the final number.',
 prose(
  P('Champaign prices like a town on a main line, because it is one. The Chicago, St. Louis, and Indianapolis lanes all pass the interchange. A carrier picks up a car here without leaving its route. The student lanes to the Chicago suburbs run full in August and May.'),
  P('The East Coast and California lanes carry students in both directions. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The University, the Hospital, the Research Park, the Food Plant, and the Transplants',
 prose(
  L('Champaign moves on the academic calendar. Students, faculty, and the hospital account for most of the cars we ship.'),
  P('The university brings tens of thousands of students in each August and sends them home each May. Many ship a car from the Chicago suburbs, the East Coast, Texas, or California. A parent books, and an adult signs for the car at a campus lot or at the arena. The handoff never happens on Green Street. The faculty arrive each summer with a closing date and a second car.'),
  P('The hospital in Urbana is the largest in central Illinois and brings in nurses and physicians all year. Residents arrive each June, and the new medical school adds a class each summer. The clinics across both cities relocate staff the same way. We supply the paperwork a reimbursed move needs.'),
  P('The research park south of campus holds the offices of a dozen national companies. They move engineers and data scientists in every month. The food plant on the north side moves plant managers on program schedules. The packaging plant and the warehouses along 74 do the same.'),
  P('Graduates leave for Chicago, the coasts, and Texas each May, and the car goes ahead of them. Retirees from the faculty leave for the Sun Belt each fall. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Move-In Weekend, Football Saturdays, the Marathon, the Wind, and the 2013 Tornado',
 prose(
  L('Champaign runs on an August move-in, a fall of football Saturdays, and a windy prairie winter.'),
  P('Move-in weekend in August brings ten thousand cars into Campustown in two days. The streets around the quad close to trucks, and the police run one-way loops. A carrier delivering that weekend meets you at the arena lots or a lot off 57. We book move-in deliveries for the week before or the week after when the dates allow.'),
  P('Football Saturdays fill the stadium lots and every street south of Kirby from September through November. Basketball fills the arena lots through March. The marathon closes the streets around campus on a Saturday in April. Graduation in May fills the hotels and sends cars out in every direction. A handoff near any of them moves to the morning or to another day.'),
  P('The wind runs across the prairie in every season. A tall trailer slows on 57 and 74 in a crosswind. Winter brings two feet of snow, and the 2011 blizzard closed 57 for a day. Ice is the bigger problem on the overpasses. The carriers park at the truck stops by the interchange until the plows finish. A winter pickup can lose a day.'),
  P('Tornadoes cross the county. The 2013 storm destroyed much of Gifford to the north. The sirens sound a few times each spring. A pickup waits for the warning to lift. The creek through Campustown floods in a big summer storm. A handoff there moves to the arena lots.'),
 )+chips(["Downtown","Neil Street","Main Street","Station","Campustown","Green Street","Quad","Arena","Stadium","First Street","West Side","Mattis","Springfield Avenue","John Street","Prospect","Southwest","Curtis","Duncan","Windsor","Cherry Hills","Savoy","Airport","Urbana","Race Street","Courthouse","Hospital","Lincoln Avenue","Cunningham","Philo Road","North Side","Bradley","Olympian","Mahomet","Rantoul","St. Joseph","Tolono","Monticello"])
 +NOTE('Serving Champaign, Urbana, Savoy, and all of Champaign County, campus block or subdivision. Tell us the side of Neil Street and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Champaign?',
 prose(
  L('Open trailers carry most of the cars that leave Champaign County. The lane table is priced for one.'),
  P('An enclosed trailer keeps a car out of the salt, the gravel, and the rain. Parents sending a new car to a student from the coast often book one. Faculty bringing a collector car to the subdivisions off Curtis book one too.'),
  P('A student commuter or a work truck goes open and arrives in good shape. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages weigh the two.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff at the arena lots or the mall, and a signed sheet at delivery. The move-in date sets the week.'),
  P('Say yes to the price, and we assign a carrier already running 57 or 74. The lot and the pickup window come back the same day. The driver inspects the car with you and records every mark on a Bill of Lading. You both sign it, and the delivery is compared against it.'),
 )+ULI([
  "Clear the cabin and the trunk of everything personal, including the dorm boxes",
  "Bring the fuel down to a quarter tank",
  "Photograph every panel and the odometer before the truck arrives",
  "Hand over one working key and describe any fault",
  "Switch off any aftermarket alarm",
  "In Campustown or downtown, meet the truck at the arena lots or a campus lot",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Champaign Drivers Choose Ship Guy',
 prose(
  L('We load the carriers passing the interchange on 57 and 74. We plan around move-in weekend, football Saturdays, and the winter.'),
  P('Ship Guy is an FMCSA-licensed broker with a $75,000 surety bond behind it. The federal register carries both. Our office is on South Neil Street.'),
  P('One coordinator answers for the move from the first quote to the signed delivery. Open, enclosed, and expedited transport are on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Champaign','1807 S Neil St #463','Champaign, IL 61820','+12175951736','(217) 595-1736','CT',
 '1807+S+Neil+St+%23463,+Champaign,+IL+61820','Visit Us','Find Ship Guy in Champaign',
 'Our office is on South Neil Street, between downtown and the arena.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4693.509067821164!2d-88.2473067!3d40.0938811!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x880cd151a0c18473%3A0xdc2caf8ef9bb1a5f!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793024749135!5m2!1sen!2sus'))

FAQ=[
 ("Can you ship my student’s car to Champaign for move-in?","Yes, and it is the move we make most. Cars come from the Chicago suburbs, the East Coast, Texas, and California each August. A parent books, and an adult signs for the car at the arena lots or a campus lot. We deliver the week before or after move-in weekend when the dates allow. Campustown closes to trucks that weekend."),
 ("How much does it cost to ship a car from Chicago or Indianapolis to Champaign?","Chicago runs one hundred eighty to two hundred ninety dollars for a sedan. That is about one hundred thirty-five miles down 57. Indianapolis runs one hundred seventy to two hundred seventy, about one hundred twenty miles on 74. Springfield and St. Louis price in the same range. August prices run higher than the rest of the year. An SUV or pickup adds 10 to 25 percent."),
 ("Can the carrier come to my street downtown or in Campustown?","Usually not. Downtown is one-way streets around Neil and Main, and Campustown is high-rises and no-stopping zones. The driver meets you at the arena lots on First Street, a campus lot, or the station. The west side, the southwest subdivisions, and Savoy usually allow the curb."),
 ("Do you ship cars for people relocating to the hospital or the research park?","Yes, all year. The hospital in Urbana brings in nurses, residents, and physicians every month. The research park moves engineers and data scientists from the coasts. Many ship a second car behind the move. The handoff works at the hospital lots or a lot off 57. We provide the paperwork a reimbursed move needs."),
 ("Do football Saturdays affect my pickup?","South of Kirby, yes. The stadium lots and the streets around them fill from the morning tailgates to the evening. We move a pickup near the stadium to the morning or to Sunday. The rest of the county runs normally. Basketball nights do the same thing to the arena lots on a smaller scale."),
 ("Can you ship a car to or from Urbana, Savoy, or Mahomet?","Yes, and all three price the same as Champaign. Urbana rides the same carriers off 74 at Lincoln and Cunningham. Savoy rides them off 57 at Curtis, and Mahomet rides them off 74 to the west. Any lot off the interstate works for the handoff. New subdivisions need the full address, since the maps lag."),
 ("What happens if a blizzard or a tornado warning hits on my pickup day?","Ice shuts 57 and 74 a few times each winter. The carriers hold at the interchange truck stops until the salt trucks pass. That can cost a pickup a day, and you hear about it before it happens. Under a tornado warning the driver stops loading until it expires. Sirens sound a few times every spring. Wind by itself never cancels a pickup."),
 ("Can you ship a car that does not run from Champaign?","Yes. We send a carrier with a winch, and the loading time is in the quote from the start. The arena lots or the mall lot give the driver flat pavement to winch on. Say whether it rolls, whether it steers, and whether the brakes hold."),
 ("Can you ship a graduate’s car out of Champaign in May?","Yes. Graduates leave for Chicago, the coasts, and Texas each May. We ship the car the week after finals. The handoff works at the arena lots or a campus lot. Book in April, because the May carriers fill early. An adult signs at pickup if the graduate has already left."),
 ("What do you need for a Champaign car shipping quote?","The pickup and delivery addresses, with the side of Neil Street or the campus lot here. Year, make, and model. Whether it runs. Open or enclosed. The week around move-in or the start date. That is a full Champaign request, and the number comes back the same day."),
]
BODY.append(faq_section(FAQ,'Champaign FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Champaign?','Two minutes on the form above prices your lane. Send the side of Neil Street and your dates, and a carrier already on 57 takes it.','+12175951736','(217) 595-1736','Get your free Champaign quote'))

build({
 'slug':'auto-transport-champaign-illinois',
 'title':'Car Shipping in Champaign, IL — Auto Transport | Ship Guy',
 'meta':'Car shipping in Champaign, IL, the university town where Interstate 57 crosses Interstate 74. Student move-in and graduation moves, hospital and research-park relocations, downtown and Campustown meeting spots, west side and Savoy curbside pickups, Urbana and Mahomet, football Saturdays, and the prairie winter. Local office on South Neil Street. Free quote.',
 'h1':'Car Shipping in<br>Champaign, <span class="accent">Illinois</span>',
 'lede':'Open, enclosed, and expedited auto transport across Champaign County, planned around 57, 74, move-in weekend, football Saturdays, and the winter.',
 'tel':'+12175951736','disp':'(217) 595-1736','brand':'Champaign','keyword':'car shipping in champaign',
 'localterms':['champaign','urbana','university','interstate 57','interstate 74','interstate 72','interchange','neil street','prospect','mattis','duncan','lincoln avenue','cunningham','springfield avenue','university avenue','green street','kirby','florida avenue','windsor','curtis','bradley','olympian','route 45','downtown','main street','station','campustown','high-rises','arena','first street','stadium','quad','west side','john street','southwest','subdivisions','savoy','airport','race street','courthouse','hospital','east urbana','philo road','north side','warehouses','mahomet','lake','rantoul','air base','st. joseph','tolono','monticello','students','faculty','parent','campus lot','nurses','physicians','residents','medical school','research park','engineers','data scientists','food plant','packaging plant','graduates','retirees','move-in weekend','football saturdays','basketball','marathon','graduation','wind','crosswind','snow','2011 blizzard','ice','truck stops','tornadoes','2013','gifford','sirens','creek','springfield','indianapolis','chicago','st. louis','louisville','nashville','atlanta','new york','dallas','los angeles','memphis','peoria','decatur'],
}, BODY, FAQ)
