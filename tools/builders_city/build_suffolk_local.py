import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Suffolk, Virginia','Car shipping in the biggest city in the state by land, where Route 58 carries the region in and out, the peanut trucks roll each fall, and the swamp sets the fog',
 ['Car shipping in Suffolk runs on Route 58, Route 460, and the Monitor-Merrimac crossing on 664. Ship Guy is a licensed auto transport broker with an office on West Washington Street downtown.',
  'We book vetted carriers across Suffolk, from the brick blocks downtown to Harbour View and the villages. Chesapeake, Portsmouth, Smithfield, Franklin, and the Carolina line ride the same trucks. The trucks belong to the carriers. Ship Guy holds the license and the bond.',
  'Route 58 runs the bypass around downtown, east to Bowers Hill and west to Franklin and Interstate 95. Route 460 runs northwest to Petersburg and Interstate 85. Interstate 664 runs the north end through Harbour View to the bridge-tunnel. Route 10, Route 17, Route 13, Godwin Boulevard, and Main Street carry the rest.',
  'This page covers 58, 460, 664, 17, downtown, Harbour View, and the villages. It also covers the peanut plant, the warehouses, the defense complex, the hospital, and the sailors. The Peanut Fest, the harvest, the 2008 tornado, Isabel, and the swamp fires are here too.'],
 'Suffolk at a glance',
 ['Most Suffolk pickups land within 1 to 3 days. The city sits on the road every Hampton Roads truck takes to Carolina, Richmond, and the west. The 58 and 460 carriers pass all day, and the Peninsula trucks come over the bridge-tunnel. The warehouses keep trucks staged along 58.',
  'Richmond, Raleigh, Washington, and Baltimore are a same-day haul. Philadelphia, Charlotte, and New York take a day. Atlanta takes one to two, and Florida takes two.'],
 'Tell us the part of the city. Downtown and the old streets around it meet the truck on North Main Street. Harbour View, Bennett’s Creek, Kings Fork, and the subdivisions off Godwin Boulevard usually allow the curb. A village lane means the state road.'))

BODY.append(sec('The Roads','Route 58, Route 460, Interstate 664, Route 17, Route 10, Route 13, Route 32, Route 125, Godwin Boulevard, Bridge Road, College Drive, Nansemond Parkway, Holland Road, and Washington Street',
 prose(
  L('Suffolk is four hundred square miles of city, most of it fields and swamp around one downtown. A carrier works the state roads and meets the villages where they meet the highway.'),
  P('Route 58 is the big road, four lanes from Bowers Hill in Chesapeake around the north of downtown. It runs west to Franklin, Emporia, and Interstate 95. Every Hampton Roads truck headed to Carolina or the west uses it. Route 460 leaves 58 at Elephant’s Fork and runs northwest through Windsor to Petersburg and Interstate 85. Interstate 664 runs the north end from Bowers Hill through Harbour View to the Monitor-Merrimac crossing. It carries no toll. Route 17 is Bridge Road, from the James River Bridge south through Harbour View to Portsmouth.'),
  P('Route 10 is Godwin Boulevard, north past the hospital to Chuckatuck and Smithfield. Route 13 is Carolina Road, south past the airport to the state line. Route 32 and Route 125 reach Whaleyville and Chuckatuck. Nansemond Parkway runs the east side from downtown to Bowers Hill. College Drive carries Harbour View, and Holland Road carries the west side. North Main Street is the strip of shopping centers, and Washington Street is downtown. The rail lines cross downtown at grade, and a train stops traffic several times a day.'),
  P('The carriers come off 58 at Godwin Boulevard or Holland Road and off 664 at College Drive. They meet at the North Main Street shopping centers or the Harbour View lots at the 664 exit. The lots at the 58 and 460 split work too. The airport grounds on Carolina Road work outside the festival. So do the truck stops at Bowers Hill. The Norfolk airport is forty minutes east for a fly-and-ship. The Newport News airport is thirty over the bridge-tunnel.'),
  P('Our office sits on West Washington Street downtown, across from City Hall and beside the library.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the Old Streets, Elephant’s Fork, Harbour View, Bennett’s Creek, Driver, Chuckatuck, Eclipse, Kings Fork, Whaleyville, Holland, Smithfield, Franklin, and the Carolina Line',
 prose(
  L('Suffolk is a small brick downtown, a fast-growing north end, and a dozen villages spread across the fields. The truck meets downtown on Main Street and the north end at the curb. The villages mean the state road.'),
  P('Downtown is Washington and Main, the old train station, the courthouse, and a few blocks of brick. The streets are narrow and one way in places, and the trains cut them off. The handoff happens on North Main Street at the shopping centers. The old streets around downtown, from Bank Street to Riverview, are big houses under oaks on narrow lanes. The driver meets you on Main or Washington. Elephant’s Fork is the 58 and 460 split, strip centers and subdivisions where the curb works.'),
  P('Harbour View is the north end along 664, the fastest-growing part of the city. It is subdivisions, apartment complexes, the contractors’ campus, and the shopping centers at College Drive. The curb works on most streets, and a covenant moves the handoff to the entrance. Bennett’s Creek and the Bridge Road corridor are the same story. Driver is the old village on Nansemond Parkway, rebuilt after the 2008 tornado. The handoff happens on the parkway. Kings Fork and the subdivisions off Godwin Boulevard allow the curb.'),
  P('Chuckatuck is a village on Route 10 among the fields. Eclipse and Crittenden are waterfront villages on narrow roads that flood on a tide. The driver meets you on Route 10 or Bridge Road. Whaleyville and Holland are farm villages on the south and west sides. The handoff happens on the state road. Smithfield to the north is the ham town, a tight main street with a lot on the edge. Franklin to the west is the mill town on the Blackwater. The Carolina line is twenty minutes south on 13, and Gates County rides the same trucks.'),
  P('Chesapeake, Portsmouth, Smithfield, Windsor, and Carrollton ship with the same trucks and price the same as Suffolk. Franklin and the Carolina line towns do too. Whaleyville and the far villages add a day.'),
 )))

ROUTES=[("Richmond, VA","US-460/I-295 · ~85 mi","Same day","$160–$260"),("Raleigh, NC","US-58/I-95 · ~165 mi","Same day","$220–$340"),
 ("Washington, DC","US-460/I-95 · ~195 mi","Same day","$230–$350"),("Baltimore, MD","I-64/I-95 · ~235 mi","Same day","$250–$380"),
 ("Philadelphia, PA","I-95 · ~275 mi","1 day","$270–$400"),("Charlotte, NC","US-58/I-85 · ~295 mi","1 day","$290–$420"),
 ("New York, NY","I-95 · ~365 mi","1 day","$350–$510"),("Atlanta, GA","US-58/I-85 · ~525 mi","1–2 days","$430–$620"),
 ("Jacksonville, FL","US-58/I-95 · ~565 mi","2 days","$440–$630"),("Orlando, FL","US-58/I-95 · ~715 mi","2 days","$510–$740")]
BODY.append(rate_table('Lanes &amp; Costs','Suffolk Car Shipping Lanes and Estimated Costs',
 'The lanes Suffolk cars travel most, with open-trailer estimates. Your exact lane prices on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Suffolk, running sedan, open trailer. SUVs and pickups add 10 to 25 percent, and enclosed adds more. The week and the carriers on 58 that week decide the figure.',
 prose(
  P('Suffolk prices a notch below Norfolk on the Carolina and western lanes, because the trucks pass here first. Raleigh and Charlotte ride 58 to 95 and 85 without touching the tunnels. Richmond rides 460 through Petersburg. Washington and Baltimore ride 95 north. The Florida lane fills in October with the retirees and all summer with the orders. The Peninsula sits across the bridge-tunnel and prices the same.'),
  P('The harvest in October and a rotation summer at the shipyard make for busy weeks. The <a href="car-shipping-cost.html">cost guide</a> explains size, condition, and timing one at a time.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Peanut Plant, the Warehouses on 58, the Defense Complex in Harbour View, the Hospital, the Sailors and Shipyard Workers, the Farmers, and the Retirees',
 prose(
  L('Suffolk relocates warehouse managers, defense analysts, nurses, sailors, shipbuilders, and retirees. The warehouses and the north end move the most.'),
  P('The peanut plant downtown has shelled and roasted since the mascot was born here. It hires on the harvest. The warehouses along 58 relocate managers in spring and fall. The online retailer, the big-box chain, and the hardware chain each run a distribution center here. The handoff happens at the lots on North Main Street. The defense complex in Harbour View trains the services on simulations. The contractors around it relocate analysts on clearance timelines. The hospital on Godwin Boulevard brings nurses all year. When the employer covers the shipment, we write it up however it needs.'),
  P('Sailors from the naval station and the Portsmouth shipyard buy in Harbour View for the schools. The shipbuilders in Newport News come over the bridge-tunnel for the same reasons. The orders peak each summer, and the families ship a second car. The farmers grow peanuts, cotton, and soybeans and stay put. Retirees come to Lake Prince Woods and the waterfront villages from the Northeast. The <a href="state-to-state-car-shipping.html">state-to-state</a> page explains the paperwork a state line adds.'),
  P('The Joint Staff’s training complex in Harbour View rotates officers on orders. The naval station is thirty minutes east. Ship Guy is a private broker and not part of the Navy or the Joint Staff. The <a href="military-car-shipping.html">military</a> page covers orders and the dates they set.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Peanut Fest, the Harvest, Driver Days, the Christmas Parade, the Evacuation Road, the 2008 Tornado, Isabel, Matthew, Floyd, the Swamp Fires, and the Fog',
 prose(
  L('Suffolk runs on a farm calendar and a Navy calendar. The weather problem is a hurricane every decade, a rare tornado, and a swamp that burns for months.'),
  P('The Peanut Fest fills the airport grounds on Carolina Road for four days each October. The harvest runs from September into November, and the peanut diggers and cotton pickers crawl along the two-lanes. Driver Days fills the village for a day each fall. The Christmas parade closes downtown in December. When the region evacuates for a hurricane, every car comes through Suffolk on 58 and 460. Give a festival week or a harvest weekend three weeks of notice.'),
  P('The April 2008 tornado was the strongest ever to hit the city. It ran from Suffolk to Norfolk with winds near one hundred sixty miles an hour. It flattened the village of Driver, tore through Burnetts Mill and Hillpoint Farms, and hurt two hundred people. The hospital lost its windows and kept working. A tornado watch holds the truck at the lot until it passes.'),
  P('Isabel in September 2003 put trees across every road in the city. The power stayed out for two weeks. Matthew in October 2016 dropped close to a foot of rain in a day. Floyd in 1999 put downtown Franklin under the Blackwater. The swamp fires of 2008 and 2011 smoldered for months and sat smoke on the city all summer. Fog rolls off the swamp onto 58 and 13 on fall mornings. A driver waits for it to lift. The January 2018 and 2022 snows closed the villages for days.'),
 )+chips(["Downtown","Riverview","Bank Street","Elephant’s Fork","Harbour View","Bennett’s Creek","Bridge Road","Driver","Burnetts Mill","Hillpoint Farms","Kings Fork","Lake Prince Woods","Chuckatuck","Eclipse","Crittenden","Whaleyville","Holland","Smithfield","Carrollton","Windsor","Franklin","Chesapeake","Portsmouth","Gates County"])
 +NOTE('Serving Suffolk, Isle of Wight, and the Carolina line, Harbour View cul-de-sac or Whaleyville farm road. Tell us the part of the city and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Suffolk?',
 prose(
  L('Open trailers carry most of Suffolk’s cars, and the table above assumes one.'),
  P('Enclosed keeps the field dust, the salt air, and the pollen off the paint. The officers moving a car worth more than the orders cover book it. So do the retirees arriving with a convertible. When a storm is coming and only an open truck has room, we tell you that first.'),
  P('A commuter car or a farm truck rides open and arrives fine. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages lay out the difference.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A figure, a lot on North Main Street, and a signature when the car rolls off the truck. The orders or the start date set the week.'),
  P('Approve the figure, and we place the car with a carrier already running 58 that week. The lot and the window come back the same day. At pickup the driver photographs the car and records its condition on the Bill of Lading. You initial it, and it governs the delivery check.'),
 )+ULI([
  "Your belongings out of the cabin and the trunk",
  "Fuel at a quarter tank or less",
  "Photos of every side and the odometer before the truck comes",
  "A working key and a note on anything that acts up",
  "Aftermarket alarms disabled",
  "Downtown, on a village lane, or in Eclipse, expect North Main Street or the state road",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> page walks the steps, and the <a href="car-shipping-preparation.html">preparation</a> page covers pickup morning.'))))

BODY.append(sec('Why Ship Guy','Why Suffolk Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already run 58 and 460 through the city every day. We know which villages flood on a tide and when the harvest slows the two-lanes.'),
  P('Our FMCSA license and our $75,000 bond are on the federal register for anyone to check. The office is on West Washington Street downtown.'),
  P('One person at Ship Guy handles the move from quote to delivery call. The <a href="services.html">services</a> page covers open, enclosed, and expedited in turn.'),
 )))

BODY.append(office('Suffolk','425 W Washington St #477','Suffolk, VA 23434','+17578297254','(757) 829-7254','ET',
 '425+W+Washington+St+%23477,+Suffolk,+VA+23434','Visit Us','Find Ship Guy in Suffolk',
 'Our office sits on West Washington Street downtown, across from City Hall and beside the library.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3947.1881104670915!2d-76.588212!3d36.729237!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89b00f759185d349%3A0xde1dc7b7600667d1!2sShip%20Guy%20Auto%20Transport!5e1!3m2!1sen!2sus!4v1794237459892!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Suffolk to Raleigh or Florida?","Raleigh runs two hundred twenty to three hundred forty dollars for a sedan. It is about one hundred sixty-five miles down 58 and 95. Orlando runs five hundred ten to seven hundred forty and takes two days. Richmond runs one hundred sixty to two hundred sixty. An SUV or a pickup adds 10 to 25 percent."),
 ("Why does Suffolk price a notch below Norfolk on the Carolina lanes?","Because every Hampton Roads truck headed to Carolina or the west passes through Suffolk on 58 first. A Suffolk pickup is the first stop out of the region, and the carrier skips the tunnels. The Peninsula and the Southside price the same as each other. Suffolk sits a few dollars under on the western lanes."),
 ("Can the carrier come to my street downtown or in a village?","Downtown, no. The streets are narrow, and the trains cut them off several times a day. The driver meets you on North Main Street at the shopping centers. Eclipse, Crittenden, Chuckatuck, and Whaleyville take a handoff on the state road. Harbour View, Bennett’s Creek, Kings Fork, and the Godwin Boulevard subdivisions usually allow the curb."),
 ("Do you ship cars for the Navy and shipyard families in Harbour View?","Yes, year round with a summer peak. Sailors from the naval station and the Portsmouth shipyard buy in Harbour View. So do the Newport News shipbuilders. The orders peak each summer, and the families ship a second car. The handoff happens at the house or the College Drive lots. Ship Guy is a private broker and not part of the Navy."),
 ("Do you ship cars for the warehouses or the defense complex?","Yes. The warehouses along 58 relocate managers in spring and fall. The defense complex and the contractors in Harbour View relocate analysts on clearance timelines. The hospital on Godwin Boulevard brings nurses all year. When the employer covers the shipment, we write it up however it needs."),
 ("What happens during the Peanut Fest or the harvest?","The airport grounds on Carolina Road fill for four days each October. The handoff moves to North Main Street that week. The harvest puts peanut diggers and cotton pickers on the two-lanes from September into November. A carrier plans the village pickups around them. The figure does not change."),
 ("What happens if a hurricane is coming?","The carriers move inland, and the city becomes the way out. Every car in Hampton Roads comes through Suffolk on 58 and 460 in an evacuation. Isabel in 2003 put trees across every road and took the power for two weeks. The pickup moves to the first clear day after the roads open. The figure stays where it was."),
 ("Can you ship a car to or from Smithfield, Franklin, or the Carolina line?","Yes. Chesapeake, Portsmouth, Smithfield, Windsor, and Carrollton ride the same carriers and price the same as Suffolk. Franklin and the towns across the Carolina line do too. Whaleyville and the far villages add a day."),
 ("Can you ship a car that does not run from Suffolk?","Yes. The carrier brings a winch, and the figure includes the loading time. The North Main Street lots and the Harbour View lots are flat. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Suffolk car shipping quote?","Both addresses, with the part of the city or the village. The year, make, and model, and whether it runs. Open or enclosed, and the week around the orders or the start date. With those, the Suffolk figure comes back the same day."),
]
BODY.append(faq_section(FAQ,'Suffolk FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Suffolk?','Two minutes on the form above puts a Suffolk figure on your lane. Tell us the part of the city and the week, and a carrier already on 58 takes it.','+17578297254','(757) 829-7254','Get your free Suffolk quote'))

build({
 'slug':'auto-transport-suffolk-virginia',
 'title':'Car Shipping in Suffolk, VA — Auto Transport | Ship Guy',
 'meta':'Car shipping in Suffolk, VA, on Route 58, Route 460, and the Monitor-Merrimac crossing. The warehouses on 58, the defense complex in Harbour View, the peanut plant, Navy and shipyard families, curbside pickups in Harbour View, Bennett’s Creek, and Kings Fork, state-road handoffs for the villages, the Peanut Fest, the harvest, the 2008 tornado, and the hurricanes. Local office on West Washington Street downtown. Free quote.',
 'h1':'Car Shipping in<br>Suffolk, <span class="accent">Virginia</span>',
 'lede':'Open, enclosed, and expedited auto transport across Suffolk, Isle of Wight, and the Carolina line, planned around 58 and 460, the orders, the harvest, the storms, and the fog off the swamp.',
 'tel':'+17578297254','disp':'(757) 829-7254','brand':'Suffolk','keyword':'car shipping in suffolk',
 'localterms':['suffolk','route 58','route 460','interstate 664','monitor-merrimac','bridge-tunnel','route 17','route 10','route 13','route 32','route 125','godwin boulevard','bridge road','college drive','nansemond parkway','holland road','washington street','north main street','bowers hill','elephant’s fork','franklin','emporia','interstate 95','interstate 85','petersburg','windsor','james river bridge','carolina road','state line','rail lines','trains','four hundred square miles','fields','swamp','downtown','train station','courthouse','brick','bank street','riverview','oaks','harbour view','apartment complexes','contractors’ campus','covenant','bennett’s creek','driver','2008 tornado','kings fork','chuckatuck','eclipse','crittenden','waterfront villages','tide','whaleyville','holland','smithfield','ham town','blackwater','gates county','portsmouth','chesapeake','carrollton','peanut plant','mascot','warehouses','online retailer','big-box chain','hardware chain','distribution center','defense complex','simulations','clearance','hospital','sailors','naval station','shipyard','shipbuilders','newport news','farmers','cotton','soybeans','retirees','lake prince woods','joint staff','peanut fest','airport grounds','four days','harvest','peanut diggers','cotton pickers','driver days','christmas parade','evacuates','april 2008','one hundred sixty','burnetts mill','hillpoint farms','two hundred people','windows','tornado watch','isabel','september 2003','two weeks','matthew','october 2016','foot of rain','floyd','1999','swamp fires','2011','smoldered','fog','january 2018','2022 snows','richmond','raleigh','washington','baltimore','philadelphia','charlotte','new york','atlanta','jacksonville','orlando','norfolk','fly-and-ship','truck stops','field dust','salt air','pollen','convertible','farm truck','bill of lading','fmcsa','winch'],
}, BODY, FAQ)
