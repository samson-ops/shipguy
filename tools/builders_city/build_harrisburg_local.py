import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Harrisburg, Pennsylvania','Car shipping where Interstates 81 and 83 meet the Turnpike, the warehouse belt stages trucks by the thousand, and the river decides the worst weeks',
 ['Car shipping in Harrisburg runs on Interstates 81 and 83, which meet the Turnpike south of the city. Ship Guy is a licensed auto transport broker with an office on North Third Street in Midtown.',
  'We book vetted carriers across Harrisburg, from the Capitol blocks to Hershey and the West Shore. Camp Hill, Mechanicsburg, Carlisle, Hummelstown, and Middletown ride the same trucks. The trucks belong to the carriers. Ship Guy holds the license and the bond.',
  'Interstate 81 crosses the Susquehanna north of the city and runs the Carlisle-to-Hershey axis. Interstate 83 comes over the South Bridge from the West Shore and ends at the Eisenhower Interchange. Interstate 283 drops to the Turnpike and the airport. Cameron Street, Front Street, Derry Street, and the Carlisle Pike carry the rest.',
  'This page covers 81, 83, 283, the Turnpike, 322, the river bridges, and the rowhouse wards. It also covers the state, the medical center in Hershey, the warehouse belt, the posts, and the colleges. The Farm Show, the car shows, the floods, and the snow are here too.'],
 'Harrisburg at a glance',
 ['Most Harrisburg pickups land within 1 to 3 days. The city sits where the Carlisle and Mechanicsburg warehouses stage trucks by the thousand. The carriers between New York, Baltimore, and the Midwest pass on 81 and 83 all day. Few cities this size have a deeper pool.',
  'Baltimore, Philadelphia, Washington, New York, and Pittsburgh are a same-day haul. Richmond, Cleveland, and Boston take a day. Charlotte takes one to two, and Florida takes three.'],
 'Tell us the ward. Downtown, Midtown, Allison Hill, and Shipoke meet the truck on Cameron Street or Forster Street. Colonial Park, Linglestown, Hershey, Camp Hill, and Mechanicsburg usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 81, Interstate 83, Interstate 283, the Turnpike, Route 322, Route 22, Route 15, Route 581, Front Street, Cameron Street, Derry Street, and the Carlisle Pike',
 prose(
  L('Harrisburg is a river capital with three interstates and the Turnpike within ten minutes of the Capitol dome. The carriers have more choices here than almost anywhere in the state.'),
  P('Interstate 81 comes up from Maryland through Carlisle and crosses the river north of the city. It runs east past Hershey to Scranton. The warehouses line it from Carlisle to Grantville. Interstate 83 comes up from York and Baltimore and crosses the South Bridge. It swings east along the south side to the Eisenhower Interchange with 283 and 322. Interstate 283 runs south to the Turnpike at Harrisburg East and on to the airport in Middletown. The Turnpike passes south of the city, with a second exit at Harrisburg West on the Carlisle Pike.'),
  P('Route 322 leaves the Eisenhower Interchange for Hershey, where it meets 39 and the park traffic. Route 22 and 322 run north along the river as Front Street and then out to State College. Route 15 and Route 581 carry the West Shore. The Carlisle Pike is the retail strip of Camp Hill and Mechanicsburg. Cameron Street is the industrial spine, with the Farm Show Complex at Maclay. Derry Street and Paxton Street climb Allison Hill to the east. The Harvey Taylor and Market Street bridges carry the cars over the river. The Walnut Street Bridge has carried only walkers since the 1996 ice.'),
  P('The carriers come off 81 at Progress Avenue or Paxtonia. On 83 they use Union Deposit Road or Paxton Street. They meet at the Farm Show lots on Cameron Street outside show weeks. The strip lots on Jonestown Road and the mall lots on the Carlisle Pike work too. So do the outlet lots in Hershey and the truck stops at Carlisle, where 81 meets the Turnpike. The airport in Middletown is fifteen minutes down 283 for a fly-and-ship. The train station on Market Street runs to Philadelphia and New York all day.'),
  P('Our office sits on North Third Street in Midtown, blocks from the Capitol and the Broad Street Market.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, Midtown, Uptown, Allison Hill, Shipoke, Bellevue Park, Colonial Park, Linglestown, Hershey, Hummelstown, Middletown, Steelton, Camp Hill, Mechanicsburg, and Carlisle',
 prose(
  L('Harrisburg is a rowhouse city on a riverbank and a suburban ring on both shores. A chocolate town sits twelve miles east. The truck meets the rowhouses on a main street and the ring at the curb.'),
  P('Downtown is the Capitol complex, the state office towers, and one-way streets full of garages. The driver meets you at a garage entrance or on Forster Street. Midtown is Third Street, the Broad Street Market, and rowhouses with permit parking. The handoff happens on Forster or at the market lot. Uptown runs north to Italian Lake with the same rowhouse blocks, and the handoff happens on Division Street. Allison Hill climbs steeply east of the tracks with narrow rowhouse streets. No trailer climbs it. The driver meets you on Cameron Street or Derry Street at the bottom. Shipoke is the little riverfront ward below the South Bridge. It floods, and the handoff happens on Front Street when the river is low.'),
  P('Bellevue Park is big houses on winding wooded streets with low limbs. The driver meets you on Market Street. Penbrook and Paxtang are older grids where the curb works. Colonial Park, Paxtonia, and Linglestown are postwar subdivisions on wide streets. The curb works nearly everywhere. Hershey is the park, the medical center, and streets named for chocolate. The curb works on most of them, and the handoff moves to the outlet lots in summer. Hummelstown is a tight old borough, and Middletown is the airport, the campus, and a grid. Steelton and Highspire are mill towns on a bluff, and the handoff happens on Front Street.'),
  P('The West Shore is Camp Hill, Lemoyne, Wormleysburg, and New Cumberland, older grids and wide postwar streets. The curb works in most of them. Mechanicsburg is the Navy base, the warehouses, and subdivisions off the Carlisle Pike. Enola is the railyard town. Carlisle is the college, the Army post, the fairgrounds, and a truck-stop cluster at the 81 interchange. The curb works in town, and the fairgrounds host the car shows. Dillsburg and Grantham sit south on Route 15.'),
  P('Camp Hill, Mechanicsburg, Hershey, Hummelstown, Middletown, and Linglestown ride the same trucks. They price the same as the city. Carlisle, Elizabethtown, and Lebanon do too. The northern tier up 322 adds a day.'),
 )))

ROUTES=[("Baltimore, MD","I-83 · ~80 mi","Same day","$150–$240"),("Philadelphia, PA","Turnpike · ~105 mi","Same day","$170–$280"),
 ("Washington, DC","I-83/I-95 · ~120 mi","Same day","$170–$280"),("New York, NY","I-78 · ~170 mi","Same day","$220–$340"),
 ("Pittsburgh, PA","Turnpike · ~200 mi","Same day","$230–$350"),("Richmond, VA","I-83/I-95 · ~230 mi","1 day","$240–$360"),
 ("Cleveland, OH","Turnpike/I-80 · ~330 mi","1 day","$290–$420"),("Boston, MA","I-78/I-84/I-90 · ~380 mi","1 day","$320–$470"),
 ("Charlotte, NC","I-81/I-77 · ~490 mi","1–2 days","$400–$580"),("Orlando, FL","I-95 · ~990 mi","3 days","$700–$1,000")]
BODY.append(rate_table('Lanes &amp; Costs','Harrisburg Car Shipping Lanes and Estimated Costs',
 'The lanes Dauphin and Cumberland County cars take most, with open-trailer estimates. Use the form above for your exact lane.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Harrisburg, running sedan, open trailer. SUVs and pickups run 10 to 25 percent higher, with enclosed above that. The figure follows the week and the carriers on 81 and 83 that week.',
 prose(
  P('Harrisburg prices among the lowest cities in the Northeast on nearly every lane. Baltimore and Washington ride 83 and 95, and the trucks run them hourly. Philadelphia and Pittsburgh ride the Turnpike in both directions. New York rides 78 through Allentown. Cleveland and Chicago ride 80 across the north. The Florida lane fills in October when the snowbirds leave.'),
  P('Farm Show week in January and the Hershey meet in October are busy weeks. The <a href="car-shipping-cost.html">cost guide</a> covers size, condition, and timing separately.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The State, the Medical Center in Hershey, the Chocolate Company, the Warehouse Belt, the Navy Base, the War College, the Depot, the Guard, and the Campuses',
 prose(
  L('Harrisburg relocates agency staff, residents, warehouse managers, sailors, officers, and students. The state and the warehouses move the most.'),
  P('The state is the biggest employer, and the agencies relocate staff on session calendars and fiscal years. The handoff happens at a garage entrance downtown. The medical center and the medical school in Hershey bring residents each June and faculty all year. The chocolate company relocates managers on product launches. The insurers and the bank back offices on both shores move analysts on start dates. When the employer covers the shipment, we write it up their way.'),
  P('The warehouse belt from Carlisle to Grantville holds one of the largest distribution clusters in the country. The supervisors move in spring and fall, and the handoff happens at the lots nearest the warehouse. The railroad relocates crews to the yards at Enola and Rutherford. The airport in Middletown and the state university campus there bring staff and students. Penn State Harrisburg fills Middletown each late August. Harrisburg University, Messiah University in Grantham, and Dickinson College in Carlisle follow. A parent books, and an adult signs at the campus lot.'),
  P('The Navy’s supply command in Mechanicsburg rotates sailors and civilians on orders. The Army War College at Carlisle Barracks brings a class of officers each summer and sends one home. The depot at New Cumberland and Fort Indiantown Gap rotate on the same calendar. The Guard’s wing at the airport flies on orders too. Ship Guy is a private broker and not part of the services. The <a href="military-car-shipping.html">military</a> page sets out orders and the dates they fix.'),
  P('Retirees come to the Hershey area and the West Shore from New Jersey and Philadelphia. Some winter in Florida and ship both ways. The <a href="state-to-state-car-shipping.html">state-to-state</a> page explains the paperwork a state line adds.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Farm Show, the Outdoor Show, Kipona, Artsfest, the Hershey Meet, the Carlisle Shows, the Park Traffic, the Floods, and the Blizzards',
 prose(
  L('Harrisburg runs on a show calendar and a state calendar. The weather problem is a river that climbs its banks and a blizzard every few winters.'),
  P('The Farm Show fills the complex on Cameron Street for a week in January. The parking fills for a mile around. The Outdoor Show takes it for nine days in February. Kipona closes Front Street and City Island over Labor Day weekend. Artsfest does the same on Memorial Day weekend. The antique car meet in Hershey each October books every enclosed trailer within two hundred miles. The Carlisle shows from April to October move thousands of collector cars through the fairgrounds. The park traffic fills 39 and 322 in Hershey every summer weekend. Give a show week three weeks of notice.'),
  P('The Susquehanna is the story. Agnes in June 1972 set the record at nearly thirty-three feet. Lee in September 2011 crested above twenty-five feet and submerged Shipoke. City Island sat under seven feet of water. The city evacuated thousands along Front Street. The January 1996 ice flood took spans off the Walnut Street Bridge. In a flood the carriers wait in Carlisle or Hershey and the Shipoke pickups move inland.'),
  P('The January 2016 blizzard dropped close to thirty inches. The state closes 81, 83, and the Turnpike to trucks in a big storm. The carriers wait it out. A winter pickup can slip two days. The 81 corridor piles up in a snow squall, and we hold a truck until the squall passes. Summer brings heat and an afternoon storm that is gone in an hour.'),
 )+chips(["Downtown","The Capitol","Midtown","Broad Street Market","Uptown","Italian Lake","Allison Hill","Shipoke","Bellevue Park","Penbrook","Paxtang","Colonial Park","Paxtonia","Linglestown","Hershey","Hummelstown","Middletown","Steelton","Highspire","Camp Hill","Lemoyne","Wormleysburg","New Cumberland","Mechanicsburg","Enola","Carlisle","Dillsburg","Grantham","Elizabethtown","Lebanon"])
 +NOTE('Serving Harrisburg, Dauphin County, Cumberland County, and Hershey, rowhouse ward or West Shore cul-de-sac. Give us the ward and tell us whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Harrisburg?',
 prose(
  L('Open trailers move most of the capital region’s cars, and the table above prices one.'),
  P('Enclosed keeps the brine, the river mud, and the hail off the paint. The collectors headed to Hershey or Carlisle book it months out. So do the officers moving a car worth more than the orders cover. When a storm is coming and only an open truck has room, we tell you that first.'),
  P('A commuter car or a student’s sedan rides open and arrives fine. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages set out the difference.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A figure, a lot off 81 or 83, and a signature when the car rolls off the truck. The session date or the orders set the week.'),
  P('Approve the figure, and we place the car with a carrier already on 81 or 83 that week. The lot and the window come back the same day. The driver photographs the car at pickup and records its condition on the Bill of Lading. You initial it, and it governs the delivery check.'),
 )+ULI([
  "Your belongings out of the cabin and the trunk",
  "Fuel at a quarter tank or less",
  "Photos of every side and the odometer before the truck arrives",
  "A working key and a note on anything that acts up",
  "Aftermarket alarms disabled",
  "On Allison Hill, in Midtown, or in Shipoke, expect a lot on Cameron Street",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> page walks the steps, and the <a href="car-shipping-preparation.html">preparation</a> page covers pickup morning.'))))

BODY.append(sec('Why Ship Guy','Why Harrisburg Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already stage in the warehouse belt and run 81 and 83 every day. We know which weeks the Farm Show takes the lots and when the river closes Front Street.'),
  P('Our FMCSA license and our $75,000 bond are on the federal register for anyone to check. The office is on North Third Street in Midtown.'),
  P('One person at Ship Guy carries your move from the quote to the delivery call. The <a href="services.html">services</a> page covers open, enclosed, and expedited one by one.'),
 )))

BODY.append(office('Harrisburg','922 N 3rd St #477','Harrisburg, PA 17102','+17174201853','(717) 420-1853','ET',
 '922+N+3rd+St+%23477,+Harrisburg,+PA+17102','Visit Us','Find Ship Guy in Harrisburg',
 'Our office sits on North Third Street in Midtown, blocks from the Capitol and the Broad Street Market.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3757.911325493002!2d-76.88730699999999!3d40.267222499999995!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c8c1ea75396e17%3A0xcf46b1220ccfc0a7!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1794237071911!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Harrisburg to Baltimore or Philadelphia?","Baltimore runs one hundred fifty to two hundred forty dollars for a sedan, about eighty miles down 83. Philadelphia runs one hundred seventy to two hundred eighty on the Turnpike. Washington is the same. Pittsburgh runs two hundred thirty to three hundred fifty. An SUV or a pickup adds 10 to 25 percent."),
 ("Why is Harrisburg such an easy place to ship a car from?","Because the warehouse belt from Carlisle to Grantville stages trucks by the thousand. The carriers between New York, Baltimore, and the Midwest pass on 81 and 83 all day. A private pickup slots into that flow, and the figures come in among the lowest in the Northeast."),
 ("Can the carrier come to my rowhouse in Midtown or on Allison Hill?","No. Midtown is permit parking on narrow streets, and Allison Hill is too steep and tight for a trailer. The driver meets you on Forster Street, Cameron Street, or Derry Street. Colonial Park, Linglestown, Hershey, Camp Hill, and Mechanicsburg usually allow the curb."),
 ("Do you ship cars for the Navy base, the War College, or the depot?","Yes, in every season. The supply command in Mechanicsburg and the War College at Carlisle Barracks rotate on orders. So do the depot at New Cumberland and the Gap. The handoff happens at a lot outside the gate. Ship Guy is a private broker and not part of the services."),
 ("Can you ship a collector car to the Hershey meet or the Carlisle shows?","Yes, and book early. The Hershey meet in October books every enclosed trailer within two hundred miles. The Carlisle shows run from April to October and move thousands of cars through the fairgrounds. An enclosed truck keeps the brine and the hail off the paint. We tell you when a week is already full."),
 ("What happens when the Susquehanna floods?","The Shipoke and Front Street pickups move inland, and the carriers wait in Carlisle or Hershey. Lee in September 2011 crested above twenty-five feet and submerged Shipoke. Agnes in 1972 set the record near thirty-three feet. The pickup moves to the first dry day, and the figure stays where it was."),
 ("Can you deliver during Farm Show week?","Yes. The complex on Cameron Street and the parking for a mile around fill for a week each January. The handoff moves to the Jonestown Road lots or the Carlisle Pike mall lots that week. The figure does not change. Give a Farm Show date three weeks of notice."),
 ("Can you ship a car to or from Hershey, Carlisle, or Mechanicsburg?","Yes. Camp Hill, Mechanicsburg, Hershey, Hummelstown, Middletown, and Linglestown ride the same carriers. They price the same as the city. Carlisle, Elizabethtown, and Lebanon do too. The northern tier up 322 adds a day."),
 ("Can you ship a car that does not run from Harrisburg?","Yes. The carrier brings a winch, and the figure includes the loading time. The Farm Show lots and the Carlisle Pike mall lots are flat. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Harrisburg car shipping quote?","Both addresses, with the ward or the borough. The year, make, and model, and whether it runs. Open or enclosed, and the week around the orders or the start date. With those, the Harrisburg figure comes back the same day."),
]
BODY.append(faq_section(FAQ,'Harrisburg FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Harrisburg?','Two minutes on the form above puts a Harrisburg figure on your lane. Give us the ward and the week, and a carrier already on 81 picks it up.','+17174201853','(717) 420-1853','Get your free Harrisburg quote'))

build({
 'slug':'auto-transport-harrisburg-pennsylvania',
 'title':'Car Shipping in Harrisburg, PA — Auto Transport | Ship Guy',
 'meta':'Car shipping in Harrisburg, PA, where Interstates 81 and 83 meet the Turnpike. The warehouse belt from Carlisle to Grantville, the state, the medical center in Hershey, the Navy base and the War College, main-street handoffs for Midtown, Allison Hill, and Shipoke, curbside pickups in Colonial Park, Hershey, Camp Hill, and Mechanicsburg, the Farm Show, the Hershey car meet, the floods, and the snow. Local office on North Third Street. Free quote.',
 'h1':'Car Shipping in<br>Harrisburg, <span class="accent">Pennsylvania</span>',
 'lede':'Open, enclosed, and expedited auto transport across Harrisburg, Dauphin and Cumberland Counties, and Hershey, planned around 81 and 83, the show weeks, the orders, the river, and the snow.',
 'tel':'+17174201853','disp':'(717) 420-1853','brand':'Harrisburg','keyword':'car shipping in harrisburg',
 'localterms':['harrisburg','interstate 81','interstate 83','interstate 283','turnpike','route 322','route 22','route 15','route 581','front street','cameron street','derry street','paxton street','carlisle pike','south bridge','eisenhower interchange','harrisburg east','harrisburg west','susquehanna','harvey taylor','market street','walnut street bridge','1996 ice','progress avenue','paxtonia','union deposit','jonestown road','farm show','maclay','downtown','capitol','state office towers','garages','forster street','midtown','third street','broad street market','permit parking','uptown','italian lake','division street','allison hill','tracks','shipoke','bellevue park','penbrook','paxtang','colonial park','linglestown','hershey','medical center','chocolate','hummelstown','middletown','airport','steelton','highspire','camp hill','lemoyne','wormleysburg','new cumberland','mechanicsburg','navy','enola','railyard','carlisle','war college','carlisle barracks','fairgrounds','truck-stop','dillsburg','grantham','elizabethtown','lebanon','grantville','warehouse belt','distribution','supervisors','railroad','rutherford','penn state harrisburg','harrisburg university','messiah university','dickinson college','supply command','depot','fort indiantown gap','guard','wing','retirees','outdoor show','kipona','city island','artsfest','car meet','antique car meet','enclosed trailer','carlisle shows','collector cars','park traffic','agnes','1972','thirty-three feet','lee','september 2011','twenty-five feet','seven feet','evacuated','january 2016','thirty inches','squall','fly-and-ship','train station','baltimore','philadelphia','washington','new york','pittsburgh','richmond','cleveland','boston','charlotte','orlando','chicago','snowbirds','brine','river mud','hail','bill of lading','fmcsa','winch'],
}, BODY, FAQ)
