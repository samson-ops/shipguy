import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Rockford, Illinois','Car shipping on the Rock River, where Interstate 90 meets Interstate 39 an hour from Wisconsin',
 ['Car shipping in Rockford runs off the 90 and 39 interchange on the east side of the city. Ship Guy is a licensed auto transport broker with an office on North Main Street downtown.',
  'We book vetted carriers across Winnebago and Boone Counties, from Rockton to Belvidere and down to Cherry Valley. We do not own the trucks.',
  'Interstate 90 is the tollway along the east side, the road to Chicago and Madison. Interstate 39 leaves it at Cherry Valley and runs south to Bloomington. US 20 is the bypass around the south and west. State Street, Alpine, Perryville, and Riverside carry the city.',
  'This page covers the tollway, the bypass, downtown, the east side, the river towns, and Belvidere. It also covers the cargo airport, the aerospace plants, the hospitals, Stroll on State, and the lanes.'],
 'Rockford at a glance',
 ['Most pickups happen within 1 to 3 days. Carriers running 90 between Chicago and Minneapolis pass the city, and the 39 trucks come up from Bloomington.',
  'Chicago, Madison, and Milwaukee are all ninety minutes. Indianapolis, St. Louis, and Minneapolis are a same-day haul. Detroit and Nashville take a day. The coasts need three to five.'],
 'Tell us the side of the river. Downtown and the historic districts need a meeting spot. The east side, the northeast subdivisions, and Loves Park usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 90, Interstate 39, the US 20 Bypass, State Street, and Riverside Boulevard',
 prose(
  L('Rockford is the corner where the Chicago tollway turns toward Wisconsin, and the carriers pass on three sides.'),
  P('Interstate 90 runs along the east side of the city as the Jane Addams Tollway. The exits at State Street, Riverside, and Rockton Road serve the city, and the tolls are electronic. Every carrier between Chicago and Minneapolis passes them. Interstate 39 begins at the Cherry Valley interchange and runs south past the airport to Bloomington. The St. Louis and Memphis trucks use it.'),
  P('US 20 is the bypass, a free four-lane around the south and west sides of the city. Business 20 is State Street, the main road across the city from downtown to the mall. Route 2 is Main Street and the river road north to Beloit. US 251 runs through Loves Park and Machesney Park on the way to Wisconsin. Route 173 crosses the north end.'),
  P('Alpine Road, Mulford Road, and Perryville Road run north and south through the east side. Riverside Boulevard, Spring Creek Road, and Harrison Avenue cross it. Kishwaukee Street and 11th Street carry the southwest. Auburn Street and Rockton Avenue cover the northwest. Airport Drive reaches the cargo airport off Kishwaukee.'),
  P('The carriers come off 90 at State Street and Riverside, and off the bypass at Kishwaukee. The mall, the casino by the tollway, and the airport have the usual meeting lots. The tollway is the only toll in the county. The bypass and the river bridges are free.'),
  P('Our office is on North Main Street downtown, across from the Coronado and a block from the river.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the Historic Districts, the East Side, the Northeast, Loves Park, and Belvidere',
 prose(
  L('Rockford is a factory town on both banks of a river. The growth runs east toward the tollway.'),
  P('Downtown straddles the river between the Coronado and the arena. Main Street and State Street are busy, and the side streets by the market are narrow. The driver meets you at the arena lots, at Davis Park, or on the riverfront by the market. Signal Hill, Churchill’s Grove, and Haskell Park to the northwest are historic districts. Old houses sit on tight streets. The handoff moves to Auburn Street.'),
  P('Midtown along 7th Street is the old Swedish side, a dense grid with alleys. The driver meets you on 7th or at the shopping center on Harrison. The southwest along Kishwaukee is older grids and industrial blocks, and a lot off the bypass works. The southeast along Harrison and Alpine is postwar grids with wide streets. The curb works on most blocks.'),
  P('The east side along State, Alpine, and Perryville is the retail and hospital side. Edgebrook, Rolling Green, and the Spring Creek grids allow the curb. The northeast off Spring Creek and Mulford is the newest growth, and the streets are wide. Guilford and the subdivisions out to the tollway are the same. Cherry Valley by the interchange is a small town with lots on every road.'),
  P('Loves Park and Machesney Park north along the river are their own cities. They have wide streets and the aerospace plant. The driver meets you on Riverside or at a lot off 251. Rockton and Roscoe up the river are small towns with new subdivisions and lots on the main roads. Belvidere to the east is the Boone County seat, with the assembly plant and an old downtown. All of them price the same as Rockford.'),
 )))

ROUTES=[("Chicago, IL","I-90 · ~90 mi","Same day","$150–$240"),("Madison, WI","I-90/I-39 · ~70 mi","Same day","$140–$230"),
 ("Milwaukee, WI","I-90/I-43 · ~90 mi","Same day","$150–$240"),("Indianapolis, IN","I-39/I-74 · ~260 mi","1 day","$260–$380"),
 ("St. Louis, MO","I-39/I-55 · ~300 mi","1 day","$290–$420"),("Minneapolis, MN","I-90/I-94 · ~330 mi","1 day","$310–$450"),
 ("Detroit, MI","I-90/I-94 · ~370 mi","1 day","$340–$490"),("Nashville, TN","I-39/I-57/I-24 · ~550 mi","1–2 days","$450–$640"),
 ("Dallas, TX","I-39/I-55/I-44 · ~950 mi","2–3 days","$650–$930"),("Orlando, FL","I-65/I-75 · ~1,260 mi","3 days","$830–$1,180")]
BODY.append(rate_table('Lanes &amp; Costs','Rockford Car Shipping Lanes and Estimated Costs',
 'The lanes Rock River cars take most, with estimated open-trailer ranges. Your exact route prices on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates priced out of Rockford for a sedan that runs, open trailer. An SUV or pickup adds 10 to 25 percent, and an enclosed trailer adds more. The tollway charge rides inside the number. Fuel, the week, and the carriers free on your dates settle the final figure.',
 prose(
  P('Rockford prices a few dollars over Chicago on most lanes, because the trailers fill in the city first. The Madison and Milwaukee lanes are the exception. Those carriers pass the door on 90 and 39 and pick up a car on the way. The Minneapolis lane runs the same way.'),
  P('The Florida lane climbs in October and falls in April with the snowbirds. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Cargo Airport, the Aerospace Plants, the Hospitals, the Assembly Plant, and the Campuses',
 prose(
  L('Rockford relocates pilots, aerospace engineers, nurses, and plant workers. The airport moves more people than it used to.'),
  P('The cargo airport on the south side is one of the busiest in the country. The package carriers have built a hub there. Pilots, mechanics, and sort managers arrive from every state on short notice. The aerospace plants in Loves Park and on the west side relocate engineers on program schedules. We supply the paperwork a reimbursed move needs.'),
  P('Three hospital systems run campuses on the east side, downtown, and in Loves Park. They bring in nurses on contracts all year and residents each June. The medical school downtown adds students and faculty each summer. Physicians arrive with a closing date and a second car.'),
  P('The assembly plant in Belvidere idles and restarts on the automaker’s calendar. When it restarts, it moves supervisors and skilled trades from Michigan and Ohio in a single season. The fastener shops and the machine shops that built the city still move operators between plants.'),
  P('Rockford University and the community college bring cars in each August. A parent ships the car, and an adult signs at a campus lot. The university in DeKalb sits forty minutes south on 39, and its students ship through Rockford too. Families priced out of the Chicago suburbs buy on the northeast side. Many ship a second car behind the move. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Stroll on State, the City Market, the Rock River, the Snow, and the 2015 Tornado',
 prose(
  L('Rockford runs on a holiday weekend downtown, a summer market on the river, and a northern Illinois winter.'),
  P('Stroll on State fills downtown on the Saturday after Thanksgiving. The streets around State and Main close, and the arena lots fill by noon. A downtown pickup that weekend moves to the east side. The City Market closes the riverfront blocks on Friday evenings from May through September. A handoff downtown on a market night moves to the morning.'),
  P('The hockey team fills the arena lots from October through April. The baseball team fills the Loves Park lots in summer. The county fair fills Pecatonica in August. The air show at the cargo airport fills Kishwaukee and the airport roads on its weekend. A handoff near any of them moves to the daytime.'),
  P('The Rock River floods. The 2018 flood put the river streets in Machesney Park under water for weeks. The river rises every spring. Keith Creek floods the near east side in a big storm, as it did in 2008. A pickup on those streets moves up the hill for a day.'),
  P('Winter brings three feet of snow, and the tollway closes a few times a season. The 2011 blizzard shut 90 for a day. The 2019 cold snap froze the trailers in place. The carriers park at the truck stops by the interchange until the plows finish. A winter pickup can lose a day. The 2015 Fairdale tornado crossed the county line south of the city. The sirens sound a few times each spring.'),
 )+chips(["Downtown","Main Street","State Street","Coronado","Davis Park","Riverfront","Signal Hill","Churchill’s Grove","Haskell Park","Midtown","7th Street","Southwest","Kishwaukee","Airport","Southeast","Harrison","Alpine","East Side","Edgebrook","Rolling Green","Spring Creek","Perryville","Mulford","Northeast","Guilford","Cherry Valley","Loves Park","Machesney Park","Rockton","Roscoe","Belvidere","Winnebago","Pecatonica"])
 +NOTE('Serving Rockford, Loves Park, Belvidere, and all of Winnebago and Boone Counties, river street or subdivision. Tell us the side of the river and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Rockford?',
 prose(
  L('Nine cars in ten leave the Rock River valley on an open trailer. The table above is priced that way.'),
  P('An enclosed trailer shuts out the road salt, the gravel, and the sky. The collectors who fill the summer cruise nights book one for the show cars. Families sending a car to a student book one too.'),
  P('A daily driver or a work truck rides open and comes off the trailer clean. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages compare the two.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a meeting spot at the mall or by the tollway, and a signature at delivery. Most moves take a week.'),
  P('Accept the price, and we match the car to a carrier already on 90 or 39. The lot and the pickup window come to you that day. The driver checks the car over with you and writes the condition on a Bill of Lading. You both sign, and the same sheet is used at delivery.'),
 )+ULI([
  "Take out everything personal, including the trunk and the glovebox",
  "Leave about a quarter tank of fuel",
  "Photograph every side of the car before the truck comes",
  "Give the driver one working key and name any fault",
  "Switch off any aftermarket alarm",
  "Downtown or in Signal Hill, meet the truck at the arena lots or on Auburn Street",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Rockford Drivers Choose Ship Guy',
 prose(
  L('We load the carriers passing on 90 and 39. We plan around Stroll on State, the river, and the winter.'),
  P('Ship Guy holds active FMCSA brokerage authority and a $75,000 surety bond, both on the federal register. Our office is on North Main Street downtown.'),
  P('One coordinator owns the move from the first number to the last signature. Open, enclosed, and expedited transport are on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Rockford','303 N Main St #350A','Rockford, IL 61101','+18158648085','(815) 864-8085','CT',
 '303+N+Main+St+%23350A,+Rockford,+IL+61101','Visit Us','Find Ship Guy in Rockford',
 'Our office is on North Main Street downtown, across from the Coronado and a block from the river.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4539.847123574552!2d-89.09272419999999!3d42.2732707!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8808bf2d07d0cc5b%3A0x2ccddc07c1dc11d7!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793024690027!5m2!1sen!2sus'))

FAQ=[
 ("How much does it cost to ship a car from Rockford to Chicago or Madison?","Chicago runs one hundred fifty to two hundred forty dollars for a sedan. That is about ninety miles down the tollway. Madison runs one hundred forty to two hundred thirty, about seventy miles up 90 and 39. Milwaukee prices the same as Chicago. Those numbers include the tolls. Add 10 to 25 percent for an SUV or a pickup."),
 ("Can the carrier come to my street downtown or in Signal Hill?","Usually not. The downtown side streets by the market are narrow. Signal Hill and Churchill’s Grove have old trees over tight streets. The driver meets you at the arena lots, at Davis Park, or on Auburn Street. The east side, the northeast subdivisions, and Loves Park usually allow the curb."),
 ("Do you ship cars for people relocating to the cargo airport or the aerospace plants?","Yes, all year. The package hub at the airport brings in pilots, mechanics, and managers from every state on short notice. The aerospace plants in Loves Park and on the west side move engineers on program schedules. Many ship a second car behind the move. The handoff works at the airport or a lot off the bypass. We provide the paperwork a reimbursed move needs."),
 ("Does Stroll on State affect my pickup?","Downtown, yes. The streets around State and Main close on the Saturday after Thanksgiving. The arena lots fill by noon. We move a downtown pickup that weekend to the east side. The rest of the county runs normally."),
 ("Can you ship a car to or from Loves Park, Belvidere, or Rockton?","Yes, and all three price the same as Rockford. Loves Park and Rockton ride the same carriers off 90 and 251. Belvidere rides them off 90 at Genoa Road. A lot off the interchange or on Riverside works for a handoff. Send the full address for a new subdivision."),
 ("Does the carrier pay the tollway, and is it in my price?","Yes on both. The carriers run 90 with a transponder, and the toll is inside the quote. There is no separate charge. A carrier that takes the free bypass or Route 2 prices the same."),
 ("What happens if a blizzard or the river hits on my pickup day?","A few times each winter the tollway shuts. The carriers sit at the Cherry Valley truck stops until it reopens. That can push a pickup back a day, and you hear from us first. After a big storm the river covers the streets in Machesney Park and the near east side. Those pickups move uphill until the water drops."),
 ("Can you ship a car that does not run from Rockford?","Yes. A carrier with a winch is sent, and the loading time is in the quote from the start. The mall lot or the airport lot gives the driver level ground. Tell us whether the car rolls, steers, and brakes."),
 ("Can you time delivery to a student move at Rockford University or in DeKalb?","Yes. Rockford University and the community college take cars in each August and send them home in May. The university in DeKalb sits forty minutes south on 39 and runs the same calendar. A parent books, and an adult signs at a campus lot. The delivery window follows the move-in date."),
 ("What do you need for a Rockford car shipping quote?","Where the car is and where it is going, with the side of the river or the suburb. The year, make, and model. Whether it starts. Open or enclosed. The week you have in mind. Five answers, and the Rockford quote is on its way the same day."),
]
BODY.append(faq_section(FAQ,'Rockford FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Rockford?','The form above takes two minutes and prices the lane. Add the side of the river and your dates, and the next carrier on 90 picks it up.','+18158648085','(815) 864-8085','Get your free Rockford quote'))

build({
 'slug':'auto-transport-rockford-illinois',
 'title':'Car Shipping in Rockford, IL — Auto Transport | Ship Guy',
 'meta':'Car shipping in Rockford, IL on the Rock River, where Interstate 90 meets Interstate 39. Cargo-airport and aerospace relocations, downtown and Signal Hill meeting spots, east side and Loves Park curbside pickups, Belvidere and Rockton, Stroll on State, the river, and the winter on the tollway. Local office on North Main Street. Free quote.',
 'h1':'Car Shipping in<br>Rockford, <span class="accent">Illinois</span>',
 'lede':'Open, enclosed, and expedited auto transport across Winnebago and Boone Counties, planned around 90, 39, the bypass, the river, and the winter.',
 'tel':'+18158648085','disp':'(815) 864-8085','brand':'Rockford','keyword':'car shipping in rockford',
 'localterms':['rockford','rock river','interstate 90','interstate 39','tollway','jane addams','cherry valley','us 20','bypass','business 20','state street','route 2','main street','us 251','route 173','alpine','mulford','perryville','riverside','spring creek','harrison','kishwaukee','11th street','auburn','rockton avenue','airport drive','downtown','coronado','arena','davis park','market','signal hill','churchill’s grove','haskell park','midtown','7th street','swedish','southwest','southeast','east side','edgebrook','rolling green','northeast','guilford','loves park','machesney park','rockton','roscoe','belvidere','boone','winnebago','cargo airport','package','pilots','aerospace','engineers','hospital','nurses','residents','medical school','assembly plant','automaker','fastener','university','community college','dekalb','stroll on state','city market','hockey','baseball','county fair','pecatonica','air show','2018 flood','keith creek','2008','snow','2011 blizzard','2019','truck stops','2015','fairdale','tornado','chicago','madison','milwaukee','indianapolis','st. louis','minneapolis','detroit','nashville','dallas','orlando','freeport','beloit','bloomington'],
}, BODY, FAQ)
