import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Omaha, Nebraska','Car shipping on the Missouri, where 80 meets 29 and the headquarters meet the base',
 ['Car shipping in Omaha runs on the busiest truck road in the Plains and the river crossing. Ship Guy is a licensed auto transport broker with an office on Howard Street downtown.',
  'We book vetted carriers across the metro, from the Old Market and Dundee to Millard, Elkhorn, and Bellevue. The carriers own the trucks. Ship Guy holds the license and the bond.',
  'Interstate 80 runs the south side of the city from the river to Gretna. It carries everything between Chicago and Denver. Interstate 29 runs the Iowa bank from Sioux City to Kansas City. Interstate 480 crosses the river downtown, and Interstate 680 loops the north and west. Dodge Street is the spine.',
  'This page covers 80, 29, 480, 680, Dodge, the Old Market, Midtown, the west side, and Sarpy County. It also covers the headquarters, the base, the medical center, the World Series, the floods, and the lanes.'],
 'Omaha at a glance',
 ['Most pickups happen within 1 to 3 days. Every carrier between Chicago and Denver passes the city on 80. The Kansas City trucks come up 29.',
  'Lincoln, Des Moines, Sioux Falls, and Kansas City are same-day runs. The Twin Cities, Saint Louis, and Chicago need a day. Denver needs one to two, Dallas needs two, and Phoenix needs three.'],
 'Tell us the side of 72nd Street and whether the street is brick. The Old Market, Dundee, Benson, and the older grids meet the truck at a lot. Millard, Elkhorn, Papillion, La Vista, and the west side usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 80, Interstate 29, Interstate 480, Interstate 680, the Kennedy Freeway, Dodge Street, and 72nd Street',
 prose(
  L('Omaha is where the Plains truck road meets the river road. A carrier reaches every suburb from one of them.'),
  P('Interstate 80 enters from Council Bluffs over the Missouri. It runs the south side of the city past the stockyards site, Millard, and Gretna. It is the busiest truck road between Chicago and Denver, and the carriers never stop coming. Interstate 29 runs the Iowa side of the river. The Kansas City and Sioux Falls trucks ride it to the 80 interchange at the bluffs.'),
  P('Interstate 480 is the downtown spur. It runs from 80 north past the Old Market and over the river to Council Bluffs. Interstate 680 loops from 80 in the west around the north side to the river. The Kennedy Freeway is US 75, from 480 south past the zoo to Bellevue and the base. The North Freeway carries it north to Florence. Dodge Street is US 6, the spine from downtown west to Elkhorn. Beyond 90th it is the elevated West Dodge expressway.'),
  P('The carriers come off 80 at 72nd Street and at Gretna. The outlet mall lots in Gretna at the 80 exit are the usual meeting spot. The mall lots at 144th and Center and the centers at 168th and Dodge work too. So do the big-box lots in Council Bluffs at the 29 interchange. The ballpark lots downtown work outside the two weeks of the series.'),
  P('Our office is on Howard Street downtown, a few blocks west of the Old Market.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the Old Market, Midtown, Dundee, Benson, Aksarben, South Omaha, North Omaha, Millard, Elkhorn, Papillion, Bellevue, and Council Bluffs',
 prose(
  L('Omaha is brick streets in the old core and wide subdivisions marching west. The truck reaches the west and meets the core at the edge.'),
  P('Downtown is the headquarters towers, the arena, and the ballpark along the river. The Old Market south of it is brick streets, horse carriages, and warehouses turned lofts. A seventy-five-foot trailer does not stop on those blocks. The driver meets you at the lots by the ballpark or along 10th Street. Little Italy and Little Bohemia south of there have the same narrow blocks.'),
  P('Midtown along Farnam and Dodge is the medical campus, Blackstone, and the apartment blocks. The handoff happens at the lots by the medical center. Dundee and Benson are streetcar neighborhoods of big houses on narrow streets under old trees. The driver meets you on Dodge or on Maple Street. Aksarben Village on the old racetrack is new and wide, and the curb works. Field Club and Hanscom Park are older and tighter.'),
  P('South Omaha around 24th Street is the old packinghouse neighborhood, now the Latino main street. The streets are tight, and the handoff moves to the zoo lots or Q Street. North Omaha from 24th Street up to Florence is a mix of old grids and wide streets. The handoff moves to the centers on Ames or the Florence riverfront.'),
  P('West of 72nd Street the city is subdivisions on wide streets, and the driver reaches the house. Millard, Elkhorn, and the streets off 168th are the same. Papillion, La Vista, Gretna, and Bellevue in Sarpy County are the fastest-growing part of the state. The curb works almost everywhere. Council Bluffs across the river ships with the same trucks. All of them price the same as Omaha.'),
 )))

ROUTES=[("Lincoln, NE","I-80 · ~55 mi","Same day","$140–$230"),("Des Moines, IA","I-80 · ~135 mi","Same day","$190–$300"),
 ("Sioux Falls, SD","I-29 · ~180 mi","Same day","$220–$340"),("Kansas City, MO","I-29 · ~190 mi","Same day","$220–$340"),
 ("Minneapolis, MN","I-29/I-90 · ~380 mi","1 day","$340–$490"),("St. Louis, MO","I-29/I-70 · ~430 mi","1 day","$380–$540"),
 ("Chicago, IL","I-80 · ~470 mi","1 day","$400–$580"),("Denver, CO","I-80/I-76 · ~540 mi","1–2 days","$430–$620"),
 ("Dallas, TX","I-29/I-35 · ~660 mi","2 days","$480–$700"),("Phoenix, AZ","I-80/I-25/I-40 · ~1,300 mi","3 days","$850–$1,200")]
BODY.append(rate_table('Lanes &amp; Costs','Omaha Car Shipping Lanes and Estimated Costs',
 'The lanes metro Omaha cars run most, with estimated open-trailer ranges. Your own route gets a number on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*Estimated 2026 ranges from Omaha, operable sedan, open trailer. Larger vehicles run 10 to 25 percent higher, and enclosed runs higher still. Carrier availability on your dates and the season set the actual quote.',
 prose(
  P('Omaha prices among the best in the Plains. The 80 traffic never stops, and the 29 trucks turn here. Lincoln is an hour west and costs the least. The Chicago and Denver lanes ride 80 in opposite directions. The Dallas lane rides 29 to Kansas City and 35 south. The Arizona lane fills each fall with snowbirds.'),
  P('A report date at the base or an August move-in means the busiest weeks of the year. The <a href="car-shipping-cost.html">cost guide</a> walks through size, condition, and the other factors.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Headquarters, the Base, the Medical Center, the Railroad, the Trucking Firms, and the Campuses',
 prose(
  L('Omaha relocates insurance staff, railroaders, airmen, physicians, and students. The headquarters and the base move the most.'),
  P('Several Fortune 500 companies are headquartered in the city, and they move people every week. The insurer on Dodge, the railroad downtown, and the builder relocate staff on offer dates. So does the holding company run by the city’s most famous investor. The bank with the tallest tower and the agricultural companies do the same. The second car usually rides a trailer. The documentation for an employer-paid move is ours to provide.'),
  P('The base in Bellevue is the headquarters of the strategic command. It moves thousands of airmen and officers on orders every year. Summer is the peak. Housing is gated, and the handoff happens outside the gate or at the Bellevue centers. The government pays to move one car, and the family ships the second one with us. Ship Guy is a private broker with no connection to the Air Force. How orders change the timing is on our <a href="military-car-shipping.html">military car shipping</a> page.'),
  P('The medical center in Midtown brings residents each June and hires traveling nurses year round. The trucking companies headquartered along 80 move dispatchers and managers on start dates. Those companies haul freight, not cars, and we do not use their trucks. The campuses downtown and on Dodge take cars each August and send them home each May. Mom or Dad books, and an adult at the lot signs the paperwork.'),
  P('Retirees leave for Arizona each fall and come back in May. Families moving between Omaha and Lincoln ship one car and drive the other. Crossing a state line is covered on the <a href="state-to-state-car-shipping.html">state-to-state</a> page.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The College World Series, the Shareholder Weekend, Husker Saturdays, the Blizzards, the Tornadoes, and the River',
 prose(
  L('Omaha runs on a baseball calendar and a shareholder calendar. The weather does everything the Plains can do.'),
  P('The College World Series fills the ballpark downtown for two weeks in June. Every hotel in the metro fills with it. The streets around the ballpark close, and the downtown ramps fill. A handoff downtown moves to the suburbs those weeks. The shareholder weekend fills the arena on the first Saturday of May, and forty thousand people come. Downtown moves the same way for that weekend.'),
  P('Husker Saturdays fill 80 from Omaha to Lincoln from September through November. A carrier headed west crosses Friday or Sunday. The zoo draws two million a year, and the lots on 10th Street fill on summer weekends. The summer concert at Memorial Park closes the Dodge Street blocks for a night in late June. Move-in week in late August clogs the campus streets downtown and on Dodge.'),
  P('Winter brings thirty inches of snow in blizzards and ice. The plows reach 80 and Dodge first and the brick streets last. A storm closes 80 west of Lincoln for a day. The carriers wait in Des Moines or Council Bluffs. Spring brings tornadoes. The April 2024 storm tore through Elkhorn and Bennington. Warnings park the carriers for an hour at a time. A winter or spring pickup can lose a day.'),
  P('The Missouri rises with the Plains snowmelt. The March 2019 flood closed 29 for months and put the base under water. The river crossings shut for days. The 2011 flood did the same for a summer. The carriers came around on 80 both times. A pickup on the river flats moves up the bluff until the water drops. Summer heat shifts the loading hour and nothing else.'),
 )+chips(["Downtown","Old Market","Little Italy","Little Bohemia","Midtown","Blackstone","Dundee","Benson","Aksarben Village","Field Club","Hanscom Park","Gifford Park","South Omaha","24th Street","North Omaha","Florence","Millard","Elkhorn","West Omaha","168th and Dodge","Regency","Ralston","La Vista","Papillion","Gretna","Bellevue","Offutt","Bennington","Council Bluffs","Carter Lake","Fremont","Lincoln"])
 +NOTE('Serving Omaha and all of Douglas and Sarpy Counties, Old Market loft or Elkhorn cul-de-sac. Tell us the side of 72nd and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Omaha?',
 prose(
  L('Most Omaha cars ride an open trailer, and that is what the lane table prices.'),
  P('An enclosed trailer keeps off the road salt, the Plains grit, and the spring hail. The collectors in Dundee and the west side book one. So do the executives relocating a new car to the towers. A car headed for a long storage during a deployment often rides enclosed too.'),
  P('A commuter car or a student car belongs on the open trailer. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages lay out the difference.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A number, a lot in Gretna or at 144th and Center, and a signature at delivery. The report date or the start date picks the week.'),
  P('Approve the price, and we put the car on a carrier already running 80 through the city. The lot and the window are set before you hang up. The driver walks the car with you and marks every blemish on the Bill of Lading. The delivery inspection is checked against those marks.'),
 )+ULI([
  "Belongings out of the car, including the trunk",
  "Fuel down to a quarter tank or so",
  "Snap each side and the mileage before the driver comes",
  "A key the driver can use, plus a heads-up on any quirks",
  "Any add-on alarm switched off",
  "In the Old Market, Dundee, or South Omaha, plan on a lot",
 ])+prose(P('Read the <a href="how-it-works.html">how it works</a> page for the sequence and the <a href="car-shipping-preparation.html">preparation</a> page for the checklist.'))))

BODY.append(sec('Why Ship Guy','Why Omaha Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already run 80 through the city every hour. We know which brick streets a trailer cannot turn on.'),
  P('The federal register shows our FMCSA license and our $75,000 bond to anyone who looks. The office is on Howard Street downtown.'),
  P('One person at Ship Guy owns your move from quote to delivery. The <a href="services.html">services</a> page sets open, enclosed, and expedited side by side.'),
 )))

BODY.append(office('Omaha','1901 Howard St Suite 256','Omaha, NE 68102','+14022794512','(402) 279-4512','CT',
 '1901+Howard+St+Suite+256,+Omaha,+NE+68102','Visit Us','Find Ship Guy in Omaha',
 'Our office is on Howard Street downtown, a few blocks west of the Old Market.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3702.4611807907318!2d-95.94149039999999!3d41.2552708!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x87938ff8538ab767%3A0xe1f69a3e8644654f!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793288330268!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Omaha to Chicago or Arizona?","Chicago runs four hundred to five hundred eighty dollars for a sedan. That is about four hundred seventy miles east on 80. Phoenix runs eight hundred fifty to twelve hundred, about thirteen hundred miles. Lincoln is an hour west and costs the least. Larger vehicles add 10 to 25 percent."),
 ("Can the carrier come to my street in the Old Market or Dundee?","No. The Old Market is brick streets and carriages. Dundee is big houses on narrow streets under old trees. The driver meets you at the ballpark lots, on 10th Street, or on Dodge. Millard, Elkhorn, Papillion, La Vista, and the west side usually allow the curb."),
 ("Do you handle PCS moves for Offutt?","Yes, and the summer is the peak. The base moves thousands of airmen and officers on orders every year. Housing is gated, so the handoff happens outside the gate or at the Bellevue centers. The government pays to move one car, and the family ships the second one with us. Ship Guy is a private broker and has no connection to the Air Force."),
 ("Do you ship cars for the headquarters downtown?","Yes, every week. The insurer, the railroad, the builder, and the holding company relocate staff from across the country. The bank and the agricultural companies do the same. The second car usually rides a trailer. The documentation for an employer-paid move is ours to provide."),
 ("Can you deliver on a Creighton or UNO move-in date?","Yes. The campuses fill with cars each August and empty each May. Mom or Dad books, and an adult at the lot signs the paperwork. Campus streets are packed that week. The truck meets you at a lot on Dodge or by the ballpark. The window tracks the date."),
 ("Can you ship a car to or from Papillion, Elkhorn, or Council Bluffs?","Yes, and all three price the same as Omaha. Papillion rides the same carriers off 80 at Highway 50, and the curb works. Elkhorn rides them off West Dodge, and Council Bluffs rides them off 29 at the bluffs. Send the full address for a county road."),
 ("Does the College World Series affect my pickup?","Yes, if the address is downtown. The ballpark fills for two weeks in June, and the streets around it close. Every hotel in the metro fills. A handoff downtown moves to the suburbs those weeks. Midtown and the west side barely notice."),
 ("What happens if a blizzard or a tornado warning hits on my pickup day?","The driver waits in Des Moines or Council Bluffs until 80 reopens, or parks until the cell passes. A blizzard closes 80 west of Lincoln for a day. A warning closes the roads for an hour. The April 2024 tornado tore through Elkhorn. You hear it from us before the driver does."),
 ("Can you ship a car that does not run from Omaha?","Yes. A carrier with a winch takes it, and the loading time is part of the quote. The outlet lots in Gretna or the mall lots at 144th and Center give the driver level ground. Let us know if it rolls, steers, and brakes."),
 ("What do you need for an Omaha car shipping quote?","Both ends of the trip, with the side of 72nd Street. The year, make, and model. Whether it drives. Open or enclosed. Your week. Five answers put an Omaha price in front of you the same day."),
]
BODY.append(faq_section(FAQ,'Omaha FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Omaha?','Two minutes on the form above and we price your lane. Give us the neighborhood and the week, and a truck already on 80 takes the car.','+14022794512','(402) 279-4512','Get your free Omaha quote'))

build({
 'slug':'auto-transport-omaha-nebraska',
 'title':'Car Shipping in Omaha, NE — Auto Transport | Ship Guy',
 'meta':'Car shipping in Omaha, NE, on the Missouri where 80 meets 29. Headquarters relocations, Offutt PCS timing, the medical center, Creighton and UNO move-in, lot handoffs for the Old Market and Dundee, curbside pickups in Millard, Elkhorn, and Papillion, the College World Series, the blizzards, and the river floods. Local office on Howard Street downtown. Free quote.',
 'h1':'Car Shipping in<br>Omaha, <span class="accent">Nebraska</span>',
 'lede':'Open, enclosed, and expedited auto transport across metro Omaha, planned around 80, the river crossings, the brick streets, the base calendar, and the Plains weather.',
 'tel':'+14022794512','disp':'(402) 279-4512','brand':'Omaha','keyword':'car shipping in omaha',
 'localterms':['omaha','missouri','80','29','headquarters','base','plains','river crossing','howard street','downtown','old market','dundee','millard','elkhorn','papillion','bellevue','interstate 80','gretna','chicago','denver','interstate 29','sioux city','kansas city','interstate 480','interstate 680','dodge street','midtown','west side','sarpy county','medical center','railroad','college world series','floods','lincoln','des moines','sioux falls','twin cities','saint louis','dallas','phoenix','72nd street','brick','benson','la vista','council bluffs','stockyards','bluffs','kennedy freeway','us 75','zoo','north freeway','florence','us 6','west dodge','outlet mall','144th and center','168th and dodge','big-box','ballpark','arena','horse carriages','lofts','10th street','little italy','little bohemia','farnam','blackstone','maple street','aksarben','racetrack','field club','hanscom park','24th street','packinghouse','latino','q street','ames','subdivisions','fortune 500','builder','holding company','investor','tallest tower','agricultural companies','strategic command','airmen','gated','pcs','residents','traveling nurses','trucking companies','dispatchers','campuses','retirees','arizona','shareholder weekend','forty thousand','husker saturdays','two million','summer concert','memorial park','move-in','thirty inches','blizzards','tornadoes','april 2024','bennington','warnings','march 2019','2011','snowmelt','hail','deployment','bill of lading','fmcsa','gifford park','regency','ralston','offutt','carter lake','fremont','highway 50','creighton','uno'],
}, BODY, FAQ)
