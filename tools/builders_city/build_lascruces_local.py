import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Las Cruces, New Mexico','Car shipping in the Mesilla Valley, where 10 meets 25 under the Organ Mountains, forty minutes from El Paso',
 ['Car shipping in Las Cruces runs on the two interstates that meet west of town. Ship Guy is a licensed auto transport broker with an office on Roadrunner Parkway on the East Mesa.',
  'We book vetted carriers across Doña Ana County, from Mesilla to the East Mesa and the border towns. The carriers own the trucks. Ship Guy holds the license and the bond.',
  'Interstate 10 runs from El Paso through the city west to Deming and Arizona. Interstate 25 starts here and runs north along the Rio Grande to Albuquerque. US 70 climbs over the pass to the missile range and Alamogordo. Lohman Avenue is the spine of the east side.',
  'This page covers 10, 25, the pass, the checkpoints, downtown, Mesilla, the East Mesa, and the border towns. It also covers the university, the missile range, the hospitals, the farms, the spring wind, and the lanes.'],
 'Las Cruces at a glance',
 ['Most pickups happen within 1 to 3 days. The El Paso carriers reach the city in forty minutes, and the Phoenix-to-Texas trucks run 10 all day.',
  'El Paso and Albuquerque are same-day runs. Tucson and Phoenix need a day. San Antonio, Dallas, Denver, Houston, and Los Angeles need two. Chicago and Florida need three to four.'],
 'Tell us the side of the river and whether the street is adobe-era. Mesilla, the Mesquite district, and the Alameda blocks meet the truck at a lot. The East Mesa, Sonoma Ranch, Picacho Hills, and the valley subdivisions usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 10, Interstate 25, US 70, the Pass, the Checkpoints, Lohman Avenue, and Valley Drive',
 prose(
  L('Las Cruces is the last big town before the desert in three directions. The carriers plan their fuel around it.'),
  P('Interstate 10 arrives from El Paso along the river and turns west at the interchange below Picacho Peak. It runs sixty miles to Deming and on to Tucson and Phoenix. Interstate 25 begins at that interchange and runs north up the valley to Truth or Consequences and Albuquerque. The two share the rebuilt interchange on the west side. The carriers come off it onto Avenida de Mesilla or Valley Drive.'),
  P('US 70 leaves the east side as Bataan Memorial Highway. It climbs San Augustin Pass through the Organ Mountains. The missile range gate sits at the top, and Alamogordo sits an hour beyond. The pass closes in a snow or ice storm a few mornings a winter. West of town US 70 is Picacho Avenue, the old road to Deming.'),
  P('Every road out of town has a Border Patrol checkpoint. The 10 checkpoint sits west of the city and the 25 checkpoint north of it. The 70 checkpoint sits on the pass. Every vehicle stops, trailers included, and a loaded carrier loses ten minutes at each. Lohman Avenue carries the east side from the river to the mesa, and Telshor Boulevard carries the mall.'),
  P('The carriers come off 25 at Lohman and off 10 at Avenida de Mesilla. The mall lots on Telshor are the usual meeting spot. The big-box lots at Lohman and Walton and the centers on the East Mesa work too. So do the arena lots on the campus. The Mesilla plaza does not, and the driver meets Mesilla cars on Avenida de Mesilla.'),
  P('Our office is on Roadrunner Parkway at Lohman Avenue on the East Mesa, minutes from 25.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the Mesquite District, Alameda-Depot, the University, Mesilla, the East Mesa, Sonoma Ranch, Picacho Hills, the Valley, and the Border Towns',
 prose(
  L('Las Cruces is an adobe core, a campus, and a mesa of new subdivisions climbing toward the mountains. The truck reaches the mesa and meets the core at the edge.'),
  P('Downtown along Main Street is the plaza, the Saturday market, and the county buildings. The streets close for the market, and the handoff moves to the lots off Water Street. The Mesquite district east of downtown is the original town, adobe houses on narrow streets. A seventy-five-foot trailer does not enter it. The driver meets you on Solano or at the Lohman lots. Alameda-Depot west of downtown is the same, with the handoff on Alameda Boulevard.'),
  P('Mesilla south of town is the old plaza, the basilica, and adobe blocks under the cottonwoods. The plaza and the lanes around it stay closed to a trailer. The driver meets you on Avenida de Mesilla or at the lots by the interchange. The university district along University Avenue is the campus, the stadium, and the apartment blocks. The handoff happens at a campus lot.'),
  P('The East Mesa from Lohman up to the mountains is the newest half of the city. It is subdivisions on wide streets. Sonoma Ranch, High Range, and the streets off Roadrunner allow the curb. Picacho Hills across the river sits on the golf course with big lots. The driver reaches the driveway. The valley south along Highway 28 is pecan orchards, chile fields, and dairies. The handoff happens on the highway.'),
  P('Doña Ana, Radium Springs, and Hatch sit up the valley on 25. The chile town prices the same as the city. Anthony, Vado, Sunland Park, and Santa Teresa sit down the valley at the state line and the border. The rail yard and the border crossing in Santa Teresa bring their own moves. Chaparral sits east of the mountains. All of them price the same as Las Cruces, and El Paso prices nearly the same.'),
 )))

ROUTES=[("El Paso, TX","I-10 · ~45 mi","Same day","$150–$240"),("Albuquerque, NM","I-25 · ~225 mi","Same day","$230–$350"),
 ("Tucson, AZ","I-10 · ~275 mi","1 day","$270–$400"),("Phoenix, AZ","I-10 · ~390 mi","1 day","$350–$510"),
 ("San Antonio, TX","I-10 · ~600 mi","1–2 days","$460–$670"),("Denver, CO","I-25 · ~650 mi","2 days","$480–$700"),
 ("Dallas, TX","I-10/I-20 · ~680 mi","2 days","$490–$710"),("Los Angeles, CA","I-10 · ~760 mi","2 days","$540–$790"),
 ("Houston, TX","I-10 · ~790 mi","2 days","$560–$820"),("Chicago, IL","I-25/I-70/I-55 · ~1,500 mi","3–4 days","$950–$1,300")]
BODY.append(rate_table('Lanes &amp; Costs','Las Cruces Car Shipping Lanes and Estimated Costs',
 'The lanes Mesilla Valley cars run most, with estimated open-trailer ranges. Your own route gets a number on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Las Cruces for a running sedan on an open trailer. SUVs and pickups run roughly 10 to 25 percent more, and enclosed runs more again. The season and carrier availability on your dates decide the actual quote.',
 prose(
  P('Las Cruces prices with El Paso on every lane. The carriers are the same trucks forty minutes south. The Phoenix and Tucson lanes ride 10 west and fill every day. The Albuquerque and Denver lanes ride 25 north. The Texas lanes ride 10 east through El Paso, and the long ones take two days.'),
  P('An August move-in or a start date at the range falls in the busiest weeks. The <a href="car-shipping-cost.html">cost guide</a> explains what size, condition, and timing do to the price.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The University, the Missile Range, the Hospitals, the Border Crossing, the Farms, and the Retirees',
 prose(
  L('Las Cruces relocates engineers, soldiers, faculty, nurses, and retirees. The university and the missile range move the most.'),
  P('The university is the state’s land-grant campus. It takes cars each August and sends them home each May. Faculty and researchers arrive on contract dates over the summer. A parent sets it up, and any adult can meet the truck and sign. The community college shares the calendar.'),
  P('The missile range over the pass is the largest employer in the county. It holds soldiers, civilians, and contractors by the thousand. Orders rotate soldiers in and out all year, with a summer peak. The handoff for the post happens at the gate or in town. Orders pay for one car, so families bring the second one to us. Fort Bliss in El Paso and the air base in Alamogordo send families here too. Ship Guy is a private broker with no connection to any of them. Timing around orders is explained on our <a href="military-car-shipping.html">military car shipping</a> page.'),
  P('The two hospitals on Lohman and Telshor hire traveling nurses year round, and residents arrive each June. The rail yard and the border crossing in Santa Teresa move managers on start dates. The pecan growers and the chile packers move a few each season. Employer reimbursement? We send the documents the HR package asks for.'),
  P('Retirees arrive from the Midwest and the coasts for the sun and the prices. They ship the car ahead of the moving truck. Winter visitors come in October and leave in April. The <a href="state-to-state-car-shipping.html">state-to-state</a> page explains the interstate side.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Spring Wind, the Monsoon, the Pass, Aggie Saturdays, the Chile Harvest, and the Market',
 prose(
  L('Las Cruces runs on a campus calendar and a harvest calendar. The wind decides the spring, and the monsoon decides the summer.'),
  P('Football Saturdays fill University Avenue and the stadium lots from September through November. The handoff moves away from the campus those days. Move-in week in late August clogs the blocks around the campus. The Saturday market closes Main Street every weekend, and the downtown handoff moves to the afternoon.'),
  P('The chile harvest fills Hatch for the festival on Labor Day weekend. The 25 exit backs up. The memorial march fills the missile range for a March weekend, and the pass crawls. The day of the dead fills the Mesilla plaza in early November. The arts fair fills the park the same week. A handoff near any of them moves to the next morning.'),
  P('Spring is wind. From March through May the afternoon wind blows forty and the dust closes 10 west of town. The pileups near Deming and Lordsburg have killed people. The state shuts the road when the visibility drops. The carriers wait in El Paso or Las Cruces until it lifts. A spring pickup can lose an afternoon.'),
  P('The monsoon runs from July through September. An afternoon storm floods the arroyos and the underpasses in an hour. The water drains by evening. Winter is dry and bright, and a rare storm ices the pass and closes 70 for a morning. The carriers wait at the bottom. Summer heat shifts the loading hour to the morning and nothing else.'),
 )+chips(["Downtown","Main Street","Mesquite District","Alameda-Depot","University","University Avenue","Mesilla","Mesilla Park","Avenida de Mesilla","Picacho Hills","Telshor","Lohman Avenue","East Mesa","Roadrunner Parkway","Sonoma Ranch","High Range","Las Alturas","Doña Ana","Radium Springs","Hatch","Highway 28","La Mesa","Vado","Anthony","Sunland Park","Santa Teresa","Chaparral","Organ","Deming","Alamogordo","El Paso"])
 +NOTE('Serving Las Cruces and all of Doña Ana County, adobe block or East Mesa cul-de-sac. Tell us the side of the river and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Las Cruces?',
 prose(
  L('Open trailers carry most Mesilla Valley cars, and the lane table above assumes one.'),
  P('An enclosed trailer keeps off the spring dust, the highway grit, and the sun. The collectors in Picacho Hills and the officers relocating a new car book one. A car making the long run to the coasts often rides enclosed too.'),
  P('A commuter car or a student car is an open-trailer car. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain where the line falls.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a lot on Telshor or Lohman, and a signature at delivery. The report date or move-in day picks the week.'),
  P('Approve the price, and the car goes on a carrier already running 10 through the valley. Lot and window are settled before the day ends. At pickup you go over the car with the driver. Every mark goes on the Bill of Lading. You countersign it, and delivery is judged against it.'),
 )+ULI([
  "Empty the car of anything that is yours",
  "Run the tank down to about a quarter",
  "Photos of the car and the odometer, taken the day of pickup",
  "A key the driver can use, and a note of anything that does not work",
  "Aftermarket alarm off",
  "In Mesilla, the Mesquite district, or downtown, plan on a lot",
 ])+prose(P('The full sequence is on the <a href="how-it-works.html">how it works</a> page. The pickup checklist is on the <a href="car-shipping-preparation.html">preparation</a> page.'))))

BODY.append(sec('Why Ship Guy','Why Las Cruces Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already run 10 through the valley every day. We know which adobe streets a trailer cannot enter.'),
  P('Check the federal register and you will see Ship Guy’s FMCSA license and $75,000 bond. The office is on Roadrunner Parkway on the East Mesa.'),
  P('The coordinator who prices the move is the one who tracks the truck. See open, enclosed, and expedited compared on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Las Cruces','141 Roadrunner Pkwy #447','Las Cruces, NM 88011','+15752105082','(575) 210-5082','MT',
 '141+Roadrunner+Pkwy+%23447,+Las+Cruces,+NM+88011','Visit Us','Find Ship Guy in Las Cruces',
 'Our office is on Roadrunner Parkway at Lohman Avenue on the East Mesa, minutes from 25.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4161.7723461040805!2d-106.7348909!3d32.3236081!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x86de3d867af7a42b%3A0x1335aa9e61e13c7f!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793288462164!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Las Cruces to Phoenix or Texas?","Phoenix runs three hundred fifty to five hundred ten dollars for a sedan. That is about three hundred ninety miles west on 10. Dallas runs four hundred ninety to seven hundred ten, about six hundred eighty miles east. El Paso is forty minutes away and costs the least. Larger vehicles add 10 to 25 percent."),
 ("Can the carrier come to my street in Mesilla or the Mesquite district?","No. Mesilla is adobe lanes around the plaza, and the Mesquite district is the original town on narrow streets. The driver meets you on Avenida de Mesilla, on Solano, or at the Lohman lots. The East Mesa, Sonoma Ranch, Picacho Hills, and the valley subdivisions usually allow the curb."),
 ("Do you handle PCS moves for White Sands and Fort Bliss?","Yes, and the summer is the peak. The range over the pass rotates soldiers on orders all year. Fort Bliss families live across the county. The handoff happens at the gate or in town. Orders pay for one car, and the second one comes to us. Ship Guy is a private broker and has no connection to the Army."),
 ("Can you deliver on the NMSU move-in date?","Yes. Student cars arrive each August and go home each May. A parent sets it up, and any adult can meet the truck and sign. Move-in week clogs University Avenue, so the truck meets you at the arena lots. The window is built around the date."),
 ("Do the Border Patrol checkpoints affect my shipment?","Only by a few minutes. Every vehicle stops at the checkpoints on 10, 25, and 70, trailers included. The driver carries the paperwork for the car, and a loaded carrier clears in about ten minutes. Nothing about the checkpoint changes the price."),
 ("Can you ship a car to or from Hatch, Anthony, or Santa Teresa?","Yes, and all three price the same as Las Cruces. Hatch rides the same carriers up 25, and the handoff happens on the highway. Anthony and Santa Teresa ride them down 10 and the valley, and the curb works in the subdivisions. Send the full address for a farm road."),
 ("What happens if a dust storm closes 10 on my pickup day?","The driver waits in El Paso or Las Cruces until the state reopens the road. The spring wind closes 10 west of town a few afternoons each year. The pileups near Deming are the reason. A spring pickup can lose an afternoon. You hear it from us before the driver does."),
 ("Can you pick up a car that came across the border at Santa Teresa?","Yes, once it has cleared customs and been released to you. The commercial shipments cross on their own carriers, and we do not move those. A private car that cleared at the crossing ships domestically like any other. Tell us the release date and where it sits."),
 ("Can you ship a car that does not run from Las Cruces?","Yes. A winch truck handles it, and the loading time is priced from the start. The mall lots on Telshor or the Lohman and Walton lots give the driver level ground. Rolls, steers, brakes: tell us which of those it does."),
 ("What do you need for a Las Cruces car shipping quote?","The two ends of the trip, with the side of the river. The year, make, and model. Whether it drives. Open or enclosed. The week that works. Five answers and the Las Cruces price lands in your inbox that day."),
]
BODY.append(faq_section(FAQ,'Las Cruces FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Las Cruces?','Fill in the form above and a price follows in about two minutes. Name the neighborhood and the week, and a truck already on 10 carries it.','+15752105082','(575) 210-5082','Get your free Las Cruces quote'))

build({
 'slug':'auto-transport-las-cruces-new-mexico',
 'title':'Car Shipping in Las Cruces, NM — Auto Transport | Ship Guy',
 'meta':'Car shipping in Las Cruces, NM, in the Mesilla Valley where 10 meets 25 under the Organ Mountains. NMSU move-in timing, White Sands and Fort Bliss PCS moves, the hospitals, the Border Patrol checkpoints, lot handoffs for Mesilla and the adobe blocks, curbside pickups on the East Mesa, the spring dust storms, and the monsoon. Local office on Roadrunner Parkway. Free quote.',
 'h1':'Car Shipping in<br>Las Cruces, <span class="accent">New Mexico</span>',
 'lede':'Open, enclosed, and expedited auto transport across the Mesilla Valley, planned around 10, 25, the pass, the checkpoints, the campus calendar, and the spring wind.',
 'tel':'+15752105082','disp':'(575) 210-5082','brand':'Las Cruces','keyword':'car shipping in las cruces',
 'localterms':['las cruces','mesilla valley','10','25','organ mountains','el paso','interstates','roadrunner parkway','east mesa','mesilla','valley','picacho hills','border towns','deming','arizona','rio grande','albuquerque','us 70','pass','missile range','alamogordo','lohman avenue','checkpoints','downtown','university','hospitals','pecan','chile','spring wind','tucson','phoenix','san antonio','dallas','denver','houston','los angeles','chicago','florida','adobe','mesquite','alameda','sonoma ranch','subdivisions','desert','fuel','picacho peak','truth or consequences','interchange','avenida de mesilla','valley drive','bataan memorial highway','san augustin pass','gate','picacho avenue','border patrol','telshor','mall','walton','arena','campus','plaza','saturday market','main street','county buildings','water street','solano','alameda boulevard','basilica','cottonwoods','stadium','high range','golf course','driveway','highway 28','orchards','dairies','doña ana','radium springs','hatch','anthony','vado','sunland park','santa teresa','rail yard','border crossing','chaparral','move-in','range start date','faculty','researchers','community college','soldiers','civilians','contractors','fort bliss','air base','pcs','traveling nurses','residents','packers','retirees','midwest','winter visitors','football saturdays','harvest','labor day','memorial march','day of the dead','arts fair','forty','dust','pileups','lordsburg','visibility','monsoon','arroyos','underpasses','ice','bill of lading','fmcsa','mesilla park','las alturas','la mesa','organ'],
}, BODY, FAQ)
