import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("2–4 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Charleston, West Virginia','Car shipping in the capital on the Kanawha, where three interstates meet in a valley of hills',
 ['Car shipping in Charleston runs on Interstate 64, 77, and 79, which meet north of downtown. Ship Guy is a licensed auto transport broker with an office on Capitol Street downtown.',
  'We book vetted carriers across the Kanawha Valley, from the East End to Teays Valley and the hollows. The carriers own the trucks. Ship Guy holds the license and the bond.',
  'Interstate 64 runs from Huntington through the city and joins 77 on the Turnpike toward Beckley. Interstate 77 comes down from Parkersburg and Ohio. Interstate 79 climbs northeast to Clarksburg and Pittsburgh. Corridor G runs southwest past Southridge, and MacCorkle Avenue runs the south bank.',
  'This page covers 64, 77, 79, the Turnpike, Corridor G, downtown, the hills, and the valley towns. It also covers the Capitol, the hospitals, the chemical plants, the Guard wing, the floods, and the ice.'],
 'Charleston at a glance',
 ['Most pickups happen within 2 to 4 days. The Cleveland-to-Charlotte carriers ride 77 through the valley, and the Kentucky-to-Virginia carriers ride 64. One adds a Charleston stop when the load lines up.',
  'Columbus, Lexington, and Cincinnati are a day on the truck. So are Pittsburgh, Louisville, Cleveland, and Charlotte. Richmond and Washington take one to two, and Atlanta and Nashville take two.'],
 'Tell us the neighborhood and whether the street climbs. South Hills, the East End lanes, and the hollows meet the truck on a main road. Kanawha City, Teays Valley, Cross Lanes, and St. Albans usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 64, Interstate 77, Interstate 79, the Turnpike, Corridor G, MacCorkle, Kanawha Boulevard, and the Bridges',
 prose(
  L('Charleston is a river valley with three interstates braided through it. A carrier reaches the flats from an exit and the hills not at all.'),
  P('Interstate 64 is the Kentucky-to-Virginia road. It comes in from Huntington along the Kanawha and crosses the river on the Fort Hill Bridge. It joins 77 east of downtown. From there the two ride the Turnpike together to Beckley, where 64 leaves for Lewisburg and Virginia. Interstate 77 is the Cleveland-to-Charlotte road. It comes down from Parkersburg and meets 79 and 64 at the junction north of downtown. It leaves south on the Turnpike for Princeton and Bluefield.'),
  P('The Turnpike charges by the axle at three plazas between Charleston and Princeton. The tolls ride inside every quote. Its mountain section near Beckley closes in snow, and a carrier waits below it. Interstate 79 climbs out of the valley for Clarksburg, Morgantown, and Pittsburgh. Corridor G is US 119, four lanes southwest past the Southridge centers to Logan. US 35 leaves northwest for Point Pleasant and Ohio. MacCorkle Avenue runs the south bank, and Kanawha Boulevard runs the north bank through downtown.'),
  P('The carriers come off 64 at Montrose or 77 at Westmoreland, and the Turnpike at Kanawha City. The Southridge lots on Corridor G are the usual meeting spot. The big-box lots on MacCorkle in Kanawha City work too. So do the Coliseum lots outside event nights and the mall lots in Teays Valley. The airport lots on the mountaintop work for a fly-and-ship.'),
  P('Our office is on Capitol Street downtown, between the river and the Coliseum.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the East End, the West Side, South Hills, Kanawha City, the Hollows, South Charleston, St. Albans, Teays Valley, and the Elk Valley',
 prose(
  L('Charleston is a capital squeezed between a river and the hills. The flats take a truck, and the hills do not.'),
  P('Downtown runs along Capitol Street and Kanawha Boulevard, brick blocks with angled parking. The Coliseum sits at the west end. The driver meets you at the Coliseum lots or on the Boulevard. The East End climbs from the Capitol dome up narrow lanes of old houses. The handoff moves to Kanawha Boulevard East or the Capitol lots. The West Side across the Elk is older grids on narrow streets. The driver meets you on Patrick Street.'),
  P('South Hills above the river is winding lanes with switchbacks, from Loudon Heights to Bridge Road. A seventy-five-foot trailer cannot climb them, and ice closes them to everything. The driver meets you at the bottom on MacCorkle or at Southridge. Fort Hill and the hillside streets north of downtown are the same. Kanawha City across the river is the flat grid of the city. The curb works on nearly every block.'),
  P('The hollows run up every creek off the valley, one lane wide with no turnaround. Elk Two Mile, Davis Creek, and the rest meet the truck at the highway. South Charleston, Dunbar, Nitro, and St. Albans down the valley are old plant towns on flat grids. The curb usually works. Cross Lanes and Teays Valley are the newer subdivisions, and so is Hurricane beyond them. The driver reaches the house.'),
  P('Elkview and Clendenin up 79 ship with the same trucks and meet them in town. Belle, Marmet, and Montgomery up the river do the same. Sissonville up 77 is the same again. All of them price the same as Charleston. Huntington is an hour west and prices the same, and Beckley is an hour over the mountain.'),
 )))

ROUTES=[("Columbus, OH","US-35/I-70 · ~165 mi","1 day","$220–$340"),("Lexington, KY","I-64 · ~180 mi","1 day","$220–$340"),
 ("Cincinnati, OH","I-64/US-52 · ~200 mi","1 day","$230–$350"),("Pittsburgh, PA","I-79 · ~230 mi","1 day","$250–$380"),
 ("Louisville, KY","I-64 · ~250 mi","1 day","$250–$380"),("Cleveland, OH","I-77 · ~250 mi","1 day","$260–$390"),
 ("Charlotte, NC","I-77 · ~290 mi","1 day","$280–$410"),("Richmond, VA","I-64 · ~315 mi","1–2 days","$290–$420"),
 ("Washington, DC","I-79/I-68/I-70 · ~360 mi","1–2 days","$330–$470"),("Atlanta, GA","I-77/I-85 · ~530 mi","2 days","$430–$620")]
BODY.append(rate_table('Lanes &amp; Costs','Charleston Car Shipping Lanes and Estimated Costs',
 'The lanes Kanawha Valley cars run most, with estimated open-trailer ranges. Price your own route on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Charleston, running sedan, open trailer. An SUV or a pickup runs 10 to 25 percent higher, and enclosed higher still. Turnpike tolls are inside the number where the route uses it. The dates you give and the trucks through the valley that week set the real quote.',
 prose(
  P('Charleston prices like a valley on two cross-country roads, which is what it is. The Ohio lanes ride 77 north and 35 northwest and fill every week. The Carolina lanes ride 77 south over the Turnpike. The Kentucky lanes ride 64 west, and the Virginia lanes ride it east over the mountains. The Florida lane fills each October with the valley’s retirees.'),
  P('A session start in January or the June move-out means a busy week. How size, condition, and the dates shape the number is in the <a href="car-shipping-cost.html">cost guide</a>.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Capitol, the Hospitals, the Chemical Plants, the Guard Wing, the Engine Plant, the Colleges, and the Retirees',
 prose(
  L('Charleston relocates state employees, nurses, chemists, airmen, and students. The Capitol and the hospitals move the most.'),
  P('State government fills the Capitol complex on the East End and the office blocks downtown. The agencies move staff in on start dates all year. The legislature brings a crowd for sixty days from January. A new governor brings an appointee class every fourth January. When the state or an employer reimburses the move, we supply the receipts.'),
  P('The medical center runs three hospitals in the city and is the largest private employer in the state. It hires traveling nurses year round and brings residents each June. The other system across the river does the same. The chemical plants at Institute, South Charleston, and Belle move chemists and engineers on project dates. The coal and gas companies headquartered downtown move managers on contract dates. The engine plant in Putnam County moves them on production dates. The second car usually rides a trailer.'),
  P('The university on the river takes student cars in late August. The state university in Institute does the same. Both send them home in May. Mom or Dad books, and an adult signs at a lot. The Guard wing at the airport flies cargo planes and rotates crews on orders. Orders move one car, and the second one rides with us. Ship Guy is a private broker with no tie to the Guard. Our <a href="military-car-shipping.html">military</a> page covers the timing around orders.'),
  P('Retirees leave for Florida and the Carolinas each October and come back in April. Families moving out to Teays Valley and Hurricane ship one car and drive the other. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the paperwork for crossing a state line.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Session, FestivALL, the Regatta, the Distance Run, Bridge Day, Buck Season, the Floods, the Ice, and the Fog',
 prose(
  L('Charleston runs on a legislative calendar and a river calendar. The weather problem is water in the hollows and ice on the hills.'),
  P('The legislature meets for sixty days from January, and the East End fills with cars. FestivALL closes downtown streets for ten days in June. The regatta closes Kanawha Boulevard for the Fourth of July weekend. The distance run closes the Boulevard and South Hills on Labor Day morning. Bridge Day at the gorge fills every hotel in the valley for the third weekend of October. Buck season the week of Thanksgiving empties the offices and the roads.'),
  P('The floods come with a summer storm parked over the hills. In June 2016 the Elk and the creeks rose in an afternoon and took Clendenin with them. The floodwall keeps downtown dry, but a hollow can go under in an hour. A pickup up a creek waits for the water to drop, and the handoff moves to the highway. We tell you before the driver does.'),
  P('Winter brings thirty inches of snow and more ice than the hills can take. South Hills, the East End lanes, and the hollows close to a trailer until the ice melts. The Turnpike over the mountain closes for a day at a time. The carriers wait in Charleston or Beckley. The January 2016 storm shut the state for three days. A winter pickup can lose a day, and you hear it from us first.'),
  P('The fog sits in the valley on fall mornings and closes the airport on the mountaintop. The June 2012 derecho put the valley in the dark for a week. Trees came down on every hill road. The January 2014 chemical spill shut off the water for three hundred thousand people for a week. None of them stopped a carrier for more than a day.'),
 )+chips(["Downtown","Capitol Street","Kanawha Boulevard","East End","Capitol Complex","West Side","Patrick Street","South Hills","Loudon Heights","Bridge Road","Fort Hill","North Charleston","Kanawha City","MacCorkle Avenue","Southridge","Corridor G","South Charleston","Dunbar","Nitro","St. Albans","Cross Lanes","Teays Valley","Hurricane","Sissonville","Elkview","Clendenin","Belle","Marmet","Montgomery","Huntington","Beckley"])
 +NOTE('Serving Charleston and the whole Kanawha Valley, East End lane or Teays Valley cul-de-sac. Tell us the neighborhood and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Charleston?',
 prose(
  L('Most Kanawha Valley cars go out on an open trailer, and the table above assumes one.'),
  P('An enclosed trailer keeps off the salt and cinders of a mountain winter and the Turnpike grit. The collectors in South Hills book one. So do the executives bringing a new car to the headquarters downtown. A car crossing the mountains in January often goes enclosed as well.'),
  P('A commuter car or a student car is an open-trailer car. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages lay the two side by side.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a meeting spot at Southridge, and a signature at delivery. The session or the start date picks the week.'),
  P('Approve the price, and we match the car to a carrier coming through the valley that week. Lot and window are settled as soon as it commits. At pickup the driver circles the car with you and writes its condition on the Bill of Lading. You initial it, and delivery is judged against it.'),
 )+ULI([
  "Belongings out, trunk included",
  "About a quarter tank of gas",
  "Your own photos of the car and the mileage, taken the day of pickup",
  "A working key, and a word about anything that sticks or leaks",
  "Aftermarket alarm disabled",
  "In South Hills, on the East End lanes, or up a hollow, plan on the main road",
 ])+prose(P('Read the <a href="how-it-works.html">how it works</a> page for the sequence and the <a href="car-shipping-preparation.html">preparation</a> page for the checklist.'))))

BODY.append(sec('Why Ship Guy','Why Charleston Drivers Choose Ship Guy',
 prose(
  L('We know which carriers come through the valley on 77 and 64 each week. We know which hills a trailer cannot climb.'),
  P('The federal register carries our FMCSA license and our $75,000 bond for anyone to see. The office is on Capitol Street downtown.'),
  P('The coordinator who prices the move keeps it until the car is delivered. The <a href="services.html">services</a> page compares open, enclosed, and expedited.'),
 )))

BODY.append(office('Charleston','232 Capitol St #458','Charleston, WV 25301','+13046846422','(304) 684-6422','ET',
 '232+Capitol+St+%23458,+Charleston,+WV+25301','Visit Us','Find Ship Guy in Charleston',
 'Our office is on Capitol Street downtown, between the river and the Coliseum.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3862.28412543473!2d-81.6338055!3d38.350393!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x884f2d3d388346cd%3A0x42b2e73fc4657725!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793628944637!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Charleston to Columbus or Charlotte?","Columbus runs two hundred twenty to three hundred forty dollars for a sedan. That is about a hundred sixty-five miles out 35 and 70. Charlotte runs two hundred eighty to four hundred ten, about two hundred ninety miles down 77. Lexington and Columbus are the lowest lanes on the table. An SUV or a pickup runs 10 to 25 percent higher."),
 ("Is the Turnpike toll in my price?","Yes, when the route uses it. The carriers pay by the axle at the three plazas between Charleston and Princeton. The toll rides inside the quote. A car headed to Ohio, Kentucky, or Pittsburgh never touches it. There is no separate line, and nothing is added at delivery."),
 ("Why does a Charleston pickup take 2 to 4 days?","Because the valley sits on two pass-through roads. The Cleveland-to-Charlotte carriers ride 77, and the Kentucky-to-Virginia carriers ride 64. One adds a Charleston stop when the load lines up. A few days of flexibility gets the next truck through."),
 ("Can the carrier come to my street in South Hills or on the East End?","No. South Hills is switchbacks a trailer cannot climb. The East End lanes are too narrow to turn in. The driver meets you on MacCorkle, at Southridge, or on Kanawha Boulevard. Kanawha City, Cross Lanes, Teays Valley, and St. Albans usually allow the curb."),
 ("Do you ship cars for state employees and the hospitals?","Yes, every week. The agencies move staff on start dates all year, and the session brings a crowd each January. Residents reach the medical center each June, and traveling nurses arrive year round. When the state or an employer reimburses the move, we supply the receipts."),
 ("Can you deliver on a University of Charleston or WV State move-in date?","Yes. Student cars reach both campuses in late August and head home in May. A parent sets it up, and any adult can sign at the lot. The river campus is tight that week, so the truck meets you at the Capitol lots. Give us a range around the date."),
 ("Can you ship a car to or from Huntington, Teays Valley, or Beckley?","Yes. Huntington is an hour west on 64 and prices the same as Charleston. Teays Valley rides the same carriers off 64, and the curb works. Beckley is an hour over the mountain on the Turnpike, and the toll rides inside the quote. Send the full address for a hollow."),
 ("What happens if a flood or ice hits on my pickup day?","A flood moves the handoff to the highway until the water drops. Ice closes South Hills and the hollows to a trailer for a day or two. The carriers wait in Charleston or Beckley when the Turnpike closes over the mountain. You hear it from us before the driver does."),
 ("Can you ship a car that does not run from Charleston?","Yes. The carrier brings a winch, and the loading time is priced in from the start. The Southridge lots or the Kanawha City lots are level. Does it roll, steer, and brake? Tell us which."),
 ("What do you need for a Charleston car shipping quote?","Pickup and delivery, with the neighborhood or the valley town. Year, make, and model. Whether it starts. Open or enclosed. The week you have in mind. With those, a Charleston number comes back the same day."),
]
BODY.append(faq_section(FAQ,'Charleston FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Charleston?','The form above takes two minutes and comes back with a Charleston number. Name the neighborhood and the week, and a carrier coming through the valley takes it.','+13046846422','(304) 684-6422','Get your free Charleston quote'))

build({
 'slug':'auto-transport-charleston-west-virginia',
 'title':'Car Shipping in Charleston, WV — Auto Transport | Ship Guy',
 'meta':'Car shipping in Charleston, WV, the capital on the Kanawha where Interstate 64, 77, and 79 meet. Turnpike tolls inside the quote, Capitol and hospital relocations, main-road handoffs for South Hills, the East End, and the hollows, curbside pickups in Kanawha City, Teays Valley, Cross Lanes, and St. Albans, the floods, and the ice. Local office on Capitol Street downtown. Free quote.',
 'h1':'Car Shipping in<br>Charleston, <span class="accent">West Virginia</span>',
 'lede':'Open, enclosed, and expedited auto transport across the Kanawha Valley, planned around 64, 77, 79, the Turnpike, the session, the hills, and the hollows.',
 'tel':'+13046846422','disp':'(304) 684-6422','brand':'Charleston','keyword':'car shipping in charleston',
 'localterms':['charleston','capital','kanawha','interstate 64','77','79','capitol street','downtown','kanawha valley','east end','kanawha city','teays valley','hollows','huntington','turnpike','beckley','parkersburg','ohio','clarksburg','pittsburgh','corridor g','southridge','maccorkle avenue','bridges','hills','valley towns','capitol','hospitals','chemical plants','guard wing','floods','ice','cleveland','charlotte','kentucky','virginia','columbus','lexington','cincinnati','louisville','richmond','washington','atlanta','nashville','south hills','west side','cross lanes','st. albans','fort hill bridge','lewisburg','junction','princeton','bluefield','axle','plazas','morgantown','logan','us 35','point pleasant','kanawha boulevard','montrose','westmoreland','big-box','coliseum','mall','airport','mountaintop','fly-and-ship','angled parking','dome','elk','patrick street','switchbacks','loudon heights','bridge road','elk two mile','davis creek','south charleston','dunbar','nitro','hurricane','elkview','clendenin','belle','marmet','montgomery','sissonville','retirees','florida','carolinas','session','sixty days','appointee','medical center','traveling nurses','residents','institute','chemists','coal','gas','engine plant','putnam county','university','late august','cargo planes','orders','festivall','regatta','distance run','labor day','bridge day','gorge','buck season','thanksgiving','june 2016','floodwall','thirty inches','january 2016','fog','derecho','2012','chemical spill','2014','three hundred thousand','cinders','grit','bill of lading','fmcsa','north charleston','winch'],
}, BODY, FAQ)
