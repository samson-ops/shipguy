import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Kent, Washington','Car shipping where the valley warehouses stage the carriers, Highway 167 floods and freezes, and two hills shut down on an inch of snow',
 ['Car shipping in Kent runs on Highway 167, the valley freeway, with Interstate 5 ten minutes west. Ship Guy is a licensed auto transport broker with an office among the north valley warehouses.',
  'We book vetted carriers across Kent, from the old grid downtown to Lake Meridian on the East Hill. Covington, Auburn, Renton, Tukwila, and Des Moines ride the same trucks. The trucks are the carriers’ own. Ship Guy carries the license and the bond.',
  'Highway 167 runs the floor of the valley with exits at 212th, 84th Avenue, Willis Street, and 277th. Highway 516 climbs the West Hill to Interstate 5 and the East Hill to Covington. The West Valley Highway and the East Valley Highway run beside the freeway. James Street, Central Avenue, the Benson Highway, and Kent-Kangley Road carry the rest.',
  'This page covers 167, 516, the valley highways, downtown, the two hills, and the warehouse district. It also covers the rocket company, the aerospace campus, the coffee roaster, the warehouses, and the colleges. The street fair, the hockey arena, the raceway, the floods, and the snow are here too.'],
 'Kent at a glance',
 ['Most Kent pickups land within 1 to 3 days. The carriers that serve Seattle stage in the Kent valley yards to begin with. The Portland and California trucks come up 5 and 167 every day. The Spokane trucks come down 405 to 90. The warehouse district keeps the pool as deep as anywhere in the state.',
  'Portland and the whole Sound are a same-day haul. Spokane and Boise take a day. Sacramento, San Francisco, and Salt Lake City take two. Los Angeles, Denver, and Phoenix take three, and Chicago takes four.'],
 'Tell us the hill or the valley. Downtown, Scenic Hill, and the steep streets off Military Road meet the truck in the valley. The East Hill subdivisions, Covington, Auburn, and the valley itself usually allow the curb.'))

BODY.append(sec('The Roads','Highway 167, Highway 516, Highway 181, Highway 515, Highway 18, Interstate 5, the West Valley Highway, the East Valley Highway, James Street, Central Avenue, 212th Street, and Kent-Kangley Road',
 prose(
  L('Kent is a flat valley floor with a hill on each side. The freeway runs down the middle of the floor. A carrier works the valley and meets the hills at the bottom.'),
  P('Highway 167 runs the valley from Interstate 405 in Renton through Kent and Auburn to Puyallup. The Kent exits are 212th Street, 84th Avenue and Central, Willis Street, and 277th. The toll lanes run the middle, and the Green River runs beside it. Interstate 5 runs along the top of the West Hill. The Kent exits are Kent-Des Moines Road and Orillia Road. Highway 18 leaves 167 at Auburn for Covington, Maple Valley, and Interstate 90. Highway 516 is Kent-Des Moines Road up the West Hill and Kent-Kangley Road up the East Hill. It passes through downtown as Willis and Smith Streets.'),
  P('The West Valley Highway is Highway 181, and the East Valley Highway is 84th Avenue. Each runs the valley floor beside the freeway. 212th Street, 228th Street, and 196th cross the valley between them and carry the warehouse traffic. James Street climbs the East Hill from downtown. The Benson Highway is Highway 515, running the East Hill north to Renton. Central Avenue is the old highway through downtown. Meeker Street is downtown’s main street, and the Sounder trains stop at Kent Station. Military Road runs the West Hill. Reith Road and Kent-Des Moines Road drop steeply off it to the valley.'),
  P('The carriers come off 167 at 212th or 84th Avenue, because that is where they park anyway. They meet at the big-box lots on the West Valley Highway or the lots on Pacific Highway. The centers at 104th and 240th on the East Hill work too. The hockey arena lots on James Street work outside games. So do the outlet mall lots in Auburn at Highway 18 and the Southcenter mall lots in Tukwila. The airport is fifteen minutes west on 516 for a fly-and-ship, and its long-term lots take a handoff.'),
  P('Our office sits among the north valley warehouses on 85th Avenue South, a mile from the 212th ramps.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, Scenic Hill, the Valley, the East Hill, Panther Lake, Lake Meridian, the West Hill, Star Lake, Midway, Covington, Auburn, Renton, Tukwila, Des Moines, and SeaTac',
 prose(
  L('Kent is a railroad downtown, a warehouse valley, and two hills covered in subdivisions. The valley is the easiest place in the county to hand off a car. The hills are the hardest in snow.'),
  P('Downtown is Meeker Street, Railroad Avenue, the station, the arena, and an old grid of bungalows. The curb works on the grid away from the station. Otherwise the handoff happens at the arena lots. Scenic Hill rises just east of downtown with steep old streets. The driver meets you on Central Avenue or at the bottom. Mill Creek is the older grid east of the tracks, and the curb works. The Valley from 180th to 277th is warehouses, the aerospace campus, the rocket company, and the coffee roaster. The streets are wide and flat, and a trailer fits anywhere.'),
  P('The East Hill is the biggest part of town, from the Benson Highway out to 132nd and 148th. It is subdivisions from the seventies to the two-thousands, cul-de-sacs, and the strip centers at 104th and 240th. The curb works on most streets, and a covenant moves the handoff to the entrance. Panther Lake joined the city in 2010 and reads the same way. Lake Meridian is lake houses and newer streets on the far east side. Two inches of snow shuts the whole hill, and the handoff moves to the valley until it thaws.'),
  P('The West Hill is Military Road, Star Lake, Midway, and the streets above the airport. The roads down to the valley are steep, and the handoff moves to Pacific Highway in snow. Covington east on Kent-Kangley is newer subdivisions and strip centers, and the curb works. Auburn south is the outlet mall, the racetrack, the amphitheater, and grids where the curb works. Renton north is the jet plant, the hospital at the 180th exit, and hills of its own. Tukwila is the mall. Des Moines and SeaTac sit on the West Hill with the airport between them.'),
  P('Covington, Auburn, Renton, Tukwila, Des Moines, and SeaTac ride the same trucks. They price the same as Kent. Federal Way and Maple Valley do too. Enumclaw and the Plateau towns add a day.'),
 )))

ROUTES=[("Portland, OR","I-5 · ~160 mi","Same day","$210–$330"),("Spokane, WA","I-405/I-90 · ~290 mi","1 day","$260–$390"),
 ("Boise, ID","I-90/I-82/I-84 · ~490 mi","1 day","$430–$620"),("Sacramento, CA","I-5 · ~735 mi","2 days","$560–$820"),
 ("San Francisco, CA","I-5 · ~795 mi","2 days","$600–$880"),("Salt Lake City, UT","I-90/I-84 · ~830 mi","2 days","$600–$880"),
 ("Los Angeles, CA","I-5 · ~1,120 mi","3 days","$800–$1,150"),("Denver, CO","I-90/I-84/I-80 · ~1,310 mi","3 days","$850–$1,200"),
 ("Phoenix, AZ","I-5/US-93 · ~1,405 mi","3–4 days","$900–$1,300"),("Chicago, IL","I-90 · ~2,045 mi","4 days","$1,100–$1,550")]
BODY.append(rate_table('Lanes &amp; Costs','Kent Car Shipping Lanes and Estimated Costs',
 'The lanes south King County cars ship most, with open-trailer estimates. Price your exact lane on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Kent, running sedan, open trailer. An SUV or a pickup runs 10 to 25 percent above the sedan, and enclosed runs higher. The week you ship and the carriers staged in the valley that week set the figure.',
 prose(
  P('Kent prices a little below Seattle, because the carriers start the day here and skip the city traffic. Portland and California ride 5 the length of the coast, and the trucks run it daily. Spokane and the Mountain West ride 405 to 90 over Snoqualmie Pass. Boise rides 82 and 84 through the Tri-Cities. Arizona and Texas ride 5 and the desert highways and take most of a week. The Alaska cars go through the port on the water leg and ride the valley trucks from there.'),
  P('A rotation summer at the base or a start date at the rocket company means a busy week. The <a href="car-shipping-cost.html">cost guide</a> explains size, condition, and timing in turn.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Rocket Company, the Aerospace Campus, the Coffee Roaster, the Warehouse District, the Jet Plant in Renton, the Colleges, the Airport, the Base to the South, and Families From Everywhere',
 prose(
  L('Kent relocates engineers, warehouse managers, airport staff, soldiers, students, and families arriving from every continent. The valley employers move the most.'),
  P('The rocket company’s headquarters off 212th hires engineers from across the country on start dates. It builds hardware in the valley. The aerospace campus on the West Valley Highway and the Renton jet plant relocate engineers on program dates. The coffee roaster’s plant off 180th hires from across the region. The warehouse district from Tukwila to Sumner relocates supervisors in spring and fall. The handoff happens at the lots nearest the plant. When the employer pays for the shipment, we write it up however it needs.'),
  P('The airport hires across the valley, and the hospital at the 180th exit brings nurses all year. Green River College in Auburn and Highline College in Des Moines bring students each September. The schools teach children who speak more than a hundred languages, and the families arrive from everywhere. A parent or an adult signs at the lot. The Sounder carries the Seattle commuters who moved south for a yard.'),
  P('Joint Base Lewis-McChord sits forty minutes south on 167 and 512. Some of its families live on the East Hill and in Covington. The rotations peak each summer. Ship Guy is a private broker and not part of the base. The <a href="military-car-shipping.html">military</a> page covers orders and the dates they set.'),
  P('Retirees leave for Arizona and the desert each fall and ship the car ahead. The <a href="state-to-state-car-shipping.html">state-to-state</a> page explains the paperwork a state line adds.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Cornucopia Days, the Hockey Season, the Drag Races, the Fireworks at Lake Meridian, the Racetrack Season, the Floods, the Snow on the Hills, the Heat, and the Smoke',
 prose(
  L('Kent runs on a valley calendar and a river. The weather problem is a river flood every decade or so and the snow that shuts the hills.'),
  P('Cornucopia Days closes downtown for four days in the middle of July for the street fair. The hockey season fills the arena on James Street from September to March. The national drag races fill the roads around the raceway on 144th Avenue in late July. The track runs from April to October. The Fourth of July fireworks fill Kent-Kangley Road at Lake Meridian. The racetrack in Auburn runs horses from April to September. The amphitheater fills Highway 164 on concert nights. Seahawks Sundays jam 167 and 5 toward the stadium. Give a fair weekend or a concert night three weeks of notice.'),
  P('The Green River floods the valley floor. In December 2025 back-to-back atmospheric rivers pushed the river to levels not seen since the dam went in. Highway 167 closed from 212th to Auburn for most of a week. The West Valley Highway went under from Willis to 277th. A levee broke in Tukwila. After the dam was damaged in 2009, the valley stacked giant sandbags along the river for three winters. In a flood the carriers stay on 5 and the hills. The valley pickups wait a few days.'),
  P('Two inches of snow shuts the East Hill and the West Hill. The carriers wait in the valley until they thaw. The February 2019 snows closed the hills for two weeks. The December 2022 ice did it for three days. The June 2021 heat dome put the airport at one hundred eight degrees. The drivers loaded at dawn. The September 2020 smoke shut the valley down for a week. The November windstorms take the power on the hills.'),
 )+chips(["Downtown","Kent Station","Meeker Street","Scenic Hill","Mill Creek","The Valley","The East Hill","Benson","Panther Lake","Lake Meridian","Meridian Valley","The West Hill","Star Lake","Midway","Covington","Auburn","Renton","Tukwila","Des Moines","SeaTac","Federal Way","Maple Valley","Enumclaw"])
 +NOTE('Serving Kent, the Green River valley, and south King County, warehouse district or East Hill cul-de-sac. Tell us the hill or the valley and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Kent?',
 prose(
  L('Open trailers do most of the valley’s work, and the table above prices one.'),
  P('Enclosed keeps the grime of a wet winter, the pass brine, and the summer smoke off the paint. The race cars headed to the raceway ride enclosed. So do the engineers moving a car worth more than the relocation. When a storm is coming and only an open truck has room, we tell you that first.'),
  P('A commuter car or a student’s hatchback rides open and arrives fine. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages lay out the difference.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A figure, a lot in the valley, and a signature when the car rolls off the truck. The start date or the orders set the week.'),
  P('Approve the figure, and we hand the car to a carrier already staged in the valley that week. You get the lot and the window the same day. The driver photographs the car at pickup and records its condition on the Bill of Lading. You initial it, and it governs the delivery check.'),
 )+ULI([
  "Your belongings out of the cabin and the trunk",
  "Fuel at a quarter tank or less",
  "Photos of every side and the odometer before the truck comes",
  "A working key and a note on anything that acts up",
  "Aftermarket alarms disabled",
  "On Scenic Hill, off Military Road, or on a snow day, expect a lot in the valley",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> page walks the steps, and the <a href="car-shipping-preparation.html">preparation</a> page covers pickup morning.'))))

BODY.append(sec('Why Ship Guy','Why Kent Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already park in the Kent valley and run 5 and 167 every day. We know which streets ice first and when the river takes the freeway.'),
  P('Our FMCSA license and our $75,000 bond are a matter of public record on the federal register. The office is on 85th Avenue South in the valley.'),
  P('One person at Ship Guy handles your move from the quote to the delivery call. The <a href="services.html">services</a> page covers open, enclosed, and expedited one by one.'),
 )))

BODY.append(office('Kent','20024 85th Ave S #420A','Kent, WA 98031','+12535251531','(253) 525-1531','PT',
 '20024+85th+Ave+S+%23420A,+Kent,+WA+98031','Visit Us','Find Ship Guy in Kent',
 'Our office sits among the north valley warehouses on 85th Avenue South, a mile from the 212th ramps.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3332.2396321332953!2d-122.2261865!3d47.4209928!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x54905de53f823d15%3A0xf8771208d4beaf1b!2sShip%20Guy%20Auto%20Transport!5e1!3m2!1sen!2sus!4v1794237282028!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Kent to Portland or Los Angeles?","Portland runs two hundred ten to three hundred thirty dollars for a sedan. It is about one hundred sixty miles down 5. Los Angeles runs eight hundred to one thousand one hundred fifty and takes three days. Spokane runs two hundred sixty to three hundred ninety. An SUV or a pickup adds 10 to 25 percent."),
 ("Why does Kent price a little below Seattle?","Because the carriers that serve Seattle park in the Kent valley to begin with. They start the day here and skip the city traffic. A valley pickup is the first stop of the morning, and the figure reflects it."),
 ("Can the carrier come to my street on the East Hill or the West Hill?","Usually, in dry weather. The East Hill subdivisions and Covington allow the curb on most streets. A covenant moves the handoff to the entrance. Scenic Hill and the steep streets off Military Road take a main road. Two inches of snow shuts both hills, and the handoff moves to the valley until they thaw."),
 ("Do you ship cars for the rocket company or the aerospace campus?","Yes, on every start date. The rocket company off 212th and the aerospace campus on West Valley relocate engineers from across the country. The jet plant in Renton and the coffee roaster do the same. The handoff happens at the lots nearest the plant. When the employer pays, we write it up however it needs."),
 ("What happens when the Green River floods?","The valley pickups wait a few days, and the carriers stay on 5 and the hills. In December 2025 the river closed 167 from 212th to Auburn for most of a week. The West Valley Highway went under water. We call when the river rises. The pickup moves to the first dry day, and the figure stays where it was."),
 ("What happens if snow hits on my pickup day?","The hills shut on two inches. The truck waits in the valley until they thaw, usually a day. The February 2019 snows closed the hills for two weeks. The December 2022 ice did it for three days. We call as soon as the forecast turns. The pickup moves to the first clear morning, and the figure stays put."),
 ("Can you ship a race car to Pacific Raceways?","Yes. The race cars ride enclosed. The national drag races in late July book the enclosed trucks weeks out. The track runs from April to October. The handoff happens at the raceway lots on 144th Avenue or at your shop. Tell us whether it runs and whether it has ground clearance."),
 ("Do you ship cars for Joint Base Lewis-McChord families in Kent?","Yes, year round with a summer peak. The base sits forty minutes south on 167 and 512. Families live on the East Hill and in Covington. The handoff happens at a lot near the house or outside the gate. Ship Guy is a private broker and not part of the base."),
 ("Can you ship a car that does not run from Kent?","Yes. The carrier brings a winch, and the figure includes the loading time. The valley lots are flat, and so are the West Valley Highway big-box lots. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Kent car shipping quote?","Both addresses, with the hill or the valley. The year, make, and model, and whether it runs. Open or enclosed, and the week around the start date or the orders. With those, the Kent figure comes back the same day."),
]
BODY.append(faq_section(FAQ,'Kent FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Kent?','Two minutes on the form above puts a Kent figure on your lane. Tell us the hill or the valley and the week. A carrier already parked in Kent takes it.','+12535251531','(253) 525-1531','Get your free Kent quote'))

build({
 'slug':'auto-transport-kent-washington',
 'title':'Car Shipping in Kent, WA — Auto Transport | Ship Guy',
 'meta':'Car shipping in Kent, WA, on Highway 167 and the valley highways where the Seattle carriers stage. The rocket company, the aerospace campus, the coffee roaster, the warehouse district, the jet plant in Renton, and the base to the south, curbside pickups on the East Hill and in Covington and Auburn, valley handoffs in snow, the Green River floods, the street fair, and the raceway. Local office on 85th Avenue South. Free quote.',
 'h1':'Car Shipping in<br>Kent, <span class="accent">Washington</span>',
 'lede':'Open, enclosed, and expedited auto transport across Kent, the Green River valley, and south King County, planned around 167 and 5, the valley yards, the start dates, the floods, and the snow on the hills.',
 'tel':'+12535251531','disp':'(253) 525-1531','brand':'Kent','keyword':'car shipping in kent',
 'localterms':['kent','highway 167','highway 516','highway 181','highway 515','highway 18','interstate 5','interstate 405','west valley highway','east valley highway','james street','central avenue','212th','228th','196th','84th avenue','willis street','277th','kent-kangley','kent-des moines','orillia','benson highway','meeker street','kent station','sounder','military road','reith road','pacific highway','toll lanes','green river','downtown','railroad avenue','arena','bungalows','scenic hill','mill creek','the valley','warehouses','aerospace campus','rocket company','coffee roaster','the east hill','104th','240th','132nd','148th','cul-de-sacs','covenant','panther lake','2010','lake meridian','the west hill','star lake','midway','covington','auburn','outlet mall','racetrack','amphitheater','highway 164','renton','jet plant','hospital','180th','tukwila','southcenter','des moines','seatac','federal way','maple valley','enumclaw','plateau','airport','fly-and-ship','long-term lots','green river college','highline college','hundred languages','joint base lewis-mcchord','512','rotations','retirees','arizona','cornucopia days','street fair','hockey season','drag races','144th avenue','raceway','fireworks','seahawks','december 2025','atmospheric rivers','dam','levee','2009','sandbags','three winters','two inches','february 2019','two weeks','december 2022','ice','june 2021','heat dome','one hundred eight','september 2020','smoke','windstorms','portland','spokane','boise','sacramento','san francisco','salt lake city','los angeles','denver','phoenix','chicago','snoqualmie pass','tri-cities','alaska','port','race cars','brine','grime','bill of lading','fmcsa','winch'],
}, BODY, FAQ)
