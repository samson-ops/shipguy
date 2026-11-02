import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("2–5 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Sioux Falls, South Dakota','Car shipping where 29 meets 90, in the city that holds half the state',
 ['Car shipping in Sioux Falls rides Interstate 29 and Interstate 90, which cross at the edge of town. Ship Guy is a licensed auto transport broker with an office on South Reid Street downtown.',
  'We book vetted carriers across Sioux Falls and the Big Sioux valley, from the Cathedral district to Harrisburg. The carriers own the trucks. Ship Guy holds the license and the bond.',
  'Interstate 29 runs the west side of the city on its way from Sioux City to Fargo. Interstate 90 runs the north side between Minnesota and the Black Hills. Interstate 229 loops the south and east. Minnesota Avenue, Cliff Avenue, and 41st Street carry the rest.',
  'This page covers 29, 90, 229, 41st Street, downtown, the old districts, the south side, and the river. It also covers the health systems, the card centers, the Guard wing, the colleges, and the blizzards.'],
 'Sioux Falls at a glance',
 ['Most pickups happen within 2 to 5 days. The 29 carriers pass between Omaha and Fargo every day. The 90 carriers cross between Chicago and the Northwest. One adds a Sioux Falls stop when the load lines up.',
  'Sioux City is ninety minutes. Omaha, Minneapolis, Fargo, and Des Moines ride a day on the truck. Kansas City and Rapid City ride one to two, Chicago and Denver two, and Dallas three.'],
 'Tell us the neighborhood and whether the street is plowed. The Cathedral district, All Saints, and the East Bank blocks meet the truck at a lot. The south side, the west side, Harrisburg, Brandon, and Tea usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 29, Interstate 90, Interstate 229, Minnesota Avenue, Cliff Avenue, Louise, 41st Street, and the River Bridges',
 prose(
  L('Sioux Falls sits in the corner where two interstates cross. A carrier reaches every subdivision from the loop without seeing downtown.'),
  P('Interstate 29 is the Kansas City-to-Winnipeg road. It comes up from Sioux City along the west side of the city and crosses 90. It leaves north for Brookings, Watertown, and Fargo. Interstate 90 is the Chicago-to-Seattle road. It runs along the north side past the airport and leaves west for Mitchell and the Black Hills. Interstate 229 leaves 29 at the south end and loops east and north to 90. It has an exit for every part of the south and east sides.'),
  P('Minnesota Avenue and Cliff Avenue run north and south through the old city. Louise Avenue runs the west side past the mall. 41st Street is the commercial strip, from the mall at 29 east across the city. 12th Street runs west to the fairgrounds and Hartford. 57th and 85th Streets carry the new subdivisions on the south side. The bridges over the Big Sioux at 8th, 10th, and 26th tie the east side to downtown.'),
  P('The carriers come off 29 at 41st Street or 12th Street and off 229 at Cliff or Minnesota. The mall lots at 41st and Louise are the usual meeting spot. The big-box lots on 41st and Louise work too. So do the arena lots outside event nights and the fairgrounds lots outside fair week. The airport cell lot works for a fly-and-ship.'),
  P('Our office is on South Reid Street on the East Bank, across the river from downtown.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the East Bank, the Cathedral District, All Saints, McKennan Park, Whittier, the North End, the South Side, the West Side, and the Valley Towns',
 prose(
  L('Sioux Falls is an old quartzite downtown with new subdivisions spreading in every direction. The truck reaches most of it.'),
  P('Downtown runs along Phillips Avenue from the falls south to 14th Street, pink stone storefronts with angled parking. The driver meets you at the lots by the depot or on 10th Street. The East Bank across the river is lofts, old warehouses, and our office on short blocks. The handoff moves to the 8th Street lots. The Cathedral district on the hill west of downtown is the oldest neighborhood in the city. The streets are narrow and the trees are big. The handoff moves to Minnesota Avenue.'),
  P('All Saints south of downtown and McKennan Park beyond it are the same, old houses on tree-lined streets. The driver meets you on Minnesota or Cliff Avenue. Pettigrew Heights west of downtown is older and tighter still. Whittier east of the river is a plain grid where the curb usually works. The north end past the airport is the plant, the rail yards, and the newer blocks.'),
  P('The south side from 41st Street down to 85th is where the city grew. The subdivisions are wide. The streets outrun the carrier maps, so send the full address. The curb works on nearly every block. The west side along Louise and out toward Tea is the same. The mall and the big-box strip sit in the middle. The east side along Arrowhead Parkway toward Brandon is the same again.'),
  P('Harrisburg and Tea to the south and Brandon and Hartford on either side ship with the same trucks. All of them price the same as Sioux Falls. Dell Rapids and Canton add half an hour. Brookings and Watertown up 29 add an hour, and Vermillion and Yankton down the river add the same.'),
 )))

ROUTES=[("Sioux City, IA","I-29 · ~85 mi","Same day","$160–$260"),("Omaha, NE","I-29 · ~180 mi","1 day","$220–$340"),
 ("Minneapolis, MN","I-90/I-35 · ~240 mi","1 day","$250–$380"),("Fargo, ND","I-29 · ~245 mi","1–2 days","$250–$380"),
 ("Des Moines, IA","I-29/I-80 · ~280 mi","1–2 days","$260–$390"),("Rapid City, SD","I-90 · ~350 mi","1–2 days","$330–$480"),
 ("Kansas City, MO","I-29 · ~360 mi","2 days","$320–$460"),("Chicago, IL","I-90 · ~570 mi","2–3 days","$430–$620"),
 ("Denver, CO","I-29/I-80 · ~600 mi","2 days","$450–$650"),("Dallas, TX","I-29/I-35 · ~900 mi","3 days","$650–$900")]
BODY.append(rate_table('Lanes &amp; Costs','Sioux Falls Car Shipping Lanes and Estimated Costs',
 'The lanes eastern South Dakota cars run most, with estimated open-trailer ranges. Price your own route on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Sioux Falls for a sedan that runs, on an open trailer. An SUV or a pickup runs 10 to 25 percent higher, and enclosed higher again. The dates you offer and the trucks crossing on 29 and 90 that week set the real quote.',
 prose(
  P('Sioux Falls prices like the busiest corner of a pass-through state, which is what it is. The Omaha and Kansas City lanes ride 29 south and fill every week. The Minneapolis lane rides 90 east to 35. The Chicago lane rides 90 the whole way. The Arizona and Texas lanes fill each October with the valley’s snowbirds, and the price rises with them.'),
  P('A start date at the card centers or the late August move-in means a busy week. How size, condition, and the date range shape the number is in the <a href="car-shipping-cost.html">cost guide</a>.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Two Health Systems, the Card Centers, the Pork Plant, the Guard Wing, the Colleges, and the Snowbirds',
 prose(
  L('Sioux Falls relocates nurses, bankers, engineers, airmen, and students. The two health systems move the most.'),
  P('The two health systems headquartered in the city run the hospitals on 18th Street and Cliff Avenue. Between them they hire traveling nurses year round and bring residents each June. Physicians arrive on contract dates all year. The card centers on the north and west sides relocate managers on start dates. The banks downtown do the same. When an employer reimburses the move, we produce the receipts it needs.'),
  P('The pork plant on the north side moves managers on production dates. The ag technology company does the same on project dates. The fulfillment center by the airport moves them on opening schedules. The second car usually rides a trailer. The two universities on 33rd and 22nd Streets take student cars in late August. They send them home in May. Mom or Dad books, and an adult at the lot signs.'),
  P('The Guard wing at the airport flies fighters and rotates crews on orders. The base in Rapid City sends families east the same way. Orders pay for one car, so the second one comes to us. Ship Guy is a private broker with no tie to either base. Our <a href="military-car-shipping.html">military</a> page walks through the timing around orders.'),
  P('Retirees head for Arizona and Texas each October and come back in April. Families moving in from Minnesota and Iowa for the taxes ship one car and drive the other. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the paperwork for crossing a state line.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Fair, the Tournament, the Rally, Pheasant Opener, Move-In Week, the Blizzards, the Ice Storm, the Tornadoes, and the River',
 prose(
  L('Sioux Falls runs on a fair calendar and a hunting calendar. The blizzards decide whether a truck moves at all.'),
  P('The Empire Fair fills the fairgrounds on 12th Street for ten days in early August. The same week the rally in the Black Hills sends thousands of motorcycles west on 90. The truck stops fill up. The conference basketball tournament fills the arena and every hotel in the city for a week in March. The pheasant opener on the third Saturday of October fills the hotels again. The handoff moves to the morning. Move-in week in late August fills the blocks around the two campuses.'),
  P('Winter brings forty inches of snow and wind chills of forty below. A blizzard on the open prairie closes 29 and 90 for a day at a time. The state posts no travel until the plows catch up. No carrier moves until the roads reopen. A car on an unplowed street gets stuck or towed. We tell you to use the driveway or a lot before the truck comes. A winter pickup can lose a day or two, and you hear it from us first.'),
  P('The April 2013 ice storm put two inches of ice on every tree in the city. Half of it stayed dark for a week. The streets were a maze of broken branches for days. An ice warning moves the handoff to a cleared lot and the pickup to the day after. A car from the south needs winter oil and a block heater before the first cold snap. An electric car should arrive with half a charge.'),
  P('Three tornadoes crossed the city on a September night in 2019. They tore up 41st Street from the mall to the hospitals. A tornado warning holds the truck until the all-clear. The Big Sioux rises with the melt in March and again after a June storm. The diversion channel keeps downtown dry. The river parks and the low blocks on the east side flood. A pickup there moves up the hill until the water drops. Summer hail dents a car in minutes, and an enclosed trailer avoids it.'),
 )+chips(["Downtown","Phillips Avenue","Falls Park","East Bank","Cathedral District","All Saints","McKennan Park","Pettigrew Heights","Whittier","North End","Airport","41st Street","The Mall","Louise Avenue","South Side","57th Street","85th Street","West Side","Arrowhead Parkway","Harrisburg","Tea","Brandon","Hartford","Dell Rapids","Canton","Brookings","Watertown","Vermillion","Yankton"])
 +NOTE('Serving Sioux Falls and the whole Big Sioux valley, Cathedral district block or Harrisburg cul-de-sac. Tell us the neighborhood and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Sioux Falls?',
 prose(
  L('Open trailers carry nearly every car in the city, and the table above is priced for one.'),
  P('An enclosed trailer keeps off five months of salt and sand and the hail of a prairie summer. The collectors in the Cathedral district book one. So do the executives bringing a new car to the health systems. Snowbirds sending a car south before the first blizzard often choose enclosed as well.'),
  P('A commuter car or a student car travels open and arrives fine. Where enclosed earns its price is explained on the <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a meeting spot at the mall, and a signature at delivery. Your week of dates picks the truck.'),
  P('Say yes, and we line up a carrier crossing on 29 or 90 that week. Once one commits, the lot and the window are set. The driver photographs the car at pickup and lists every mark on the Bill of Lading. You sign the sheet. Delivery is measured against it.'),
 )+ULI([
  "Empty the car of anything that belongs to you, trunk and console included",
  "Run the gas down to a quarter tank",
  "Shoot each side and the mileage before the truck pulls up",
  "Hand over a working key and mention anything that sticks",
  "Aftermarket alarm off",
  "In the Cathedral district, in All Saints, or on the East Bank, plan on a lot",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> page lays out the steps. The <a href="car-shipping-preparation.html">preparation</a> page lists what to do before the truck comes.'))))

BODY.append(sec('Why Ship Guy','Why Sioux Falls Drivers Choose Ship Guy',
 prose(
  L('We know which carriers cross on 29 and 90 each week and when the state posts no travel.'),
  P('Look up our FMCSA license and our $75,000 bond on the federal register any time. The office is on South Reid Street.'),
  P('The coordinator who quotes the move keeps it until the delivery photo arrives. The <a href="services.html">services</a> page compares open, enclosed, and expedited.'),
 )))

BODY.append(office('Sioux Falls','101 S Reid St Suite 455','Sioux Falls, SD 57103','+16057022358','(605) 702-2358','CT',
 '101+S+Reid+St+Suite+455,+Sioux+Falls,+SD+57103','Visit Us','Find Ship Guy in Sioux Falls',
 'Our office is on South Reid Street on the East Bank, across the river from downtown.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3569.6373631357365!2d-96.7230185!3d43.546999400000004!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x878eb52abb982a5d%3A0x8c286e51ed0695a6!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793628650857!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Sioux Falls to Minneapolis or Denver?","Minneapolis runs two hundred fifty to three hundred eighty dollars for a sedan. That is about two hundred forty miles out 90 and up 35. Denver runs four hundred fifty to six hundred fifty, about six hundred miles down 29 and out 80. Sioux City is ninety minutes away and costs the least. Count on 10 to 25 percent more for an SUV or a pickup."),
 ("Why does a Sioux Falls pickup take 2 to 5 days?","Because South Dakota is a pass-through market, and Sioux Falls is its busiest corner. The 29 carriers run between Omaha and Fargo, and the 90 carriers cross between Chicago and the Northwest. One adds a stop when the load lines up. A week of dates puts the car on the next one through."),
 ("Can the carrier come to my street in the Cathedral district or on the south side?","The south side, yes. The subdivisions from 41st down to 85th are wide, and the curb works on nearly every block. The Cathedral district, usually not. The streets are narrow and the trees hang low. The driver meets you on Minnesota Avenue or at the mall lots."),
 ("Do you ship cars for the health systems and the card centers?","Yes, every week. The two health systems bring residents each June and hire traveling nurses year round. The card centers and the banks relocate managers on start dates. When an employer reimburses the move, we produce the receipts it needs."),
 ("Can you deliver on an Augustana or USF move-in date?","Yes. Student cars arrive at both campuses in late August and leave in May. Parents book, and whoever meets the truck signs, as long as they are an adult. The blocks around 33rd and 22nd Streets are full that week. The meeting point is the mall lots. Give us a range around the date."),
 ("Can you ship a car to or from Brandon, Harrisburg, or Brookings?","Yes. Brandon and Harrisburg price the same as Sioux Falls and ride the same trucks off 90 and 229. Brookings is an hour up 29 and prices a shade higher. The handoff is at a lot near campus. Send the full address for a new subdivision."),
 ("What happens if a blizzard closes 29 or 90 on my pickup day?","Nothing moves until the roads reopen. The state posts no travel on both interstates in a blizzard. A carrier waits in Omaha or Sioux City. A closure runs a day, and the truck shows up a day or two behind. You hear it from us first. Keep the car in the driveway with the block heater plugged in."),
 ("Does the fair or the rally affect my pickup?","Yes, for a week in early August. The fair jams 12th Street for ten days. The rally sends thousands of motorcycles west on 90 the same week. A handoff near the fairgrounds moves to the week after. The pheasant opener in October fills the hotels but not the roads."),
 ("Can you ship a car that does not run from Sioux Falls?","Yes. The quote includes a winch carrier and the loading time, so nothing is added later. A non-runner narrows the trucks that can stop, so leave room on the dates. The mall lots at 41st and Louise are level. Does it roll, steer, and brake? Say which."),
 ("What do you need for a Sioux Falls car shipping quote?","Pickup and delivery, with the neighborhood or the town. The year, make, and model. Does it start. Open or enclosed. The widest week of dates you can offer. Five answers, and the Sioux Falls number lands in your inbox the same day."),
]
BODY.append(faq_section(FAQ,'Sioux Falls FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Sioux Falls?','Two minutes on the form above, and a Sioux Falls number is on its way. Tell us the neighborhood and a week of dates, and we flag the next carrier through.','+16057022358','(605) 702-2358','Get your free Sioux Falls quote'))

build({
 'slug':'auto-transport-sioux-falls-south-dakota',
 'title':'Car Shipping in Sioux Falls, SD — Auto Transport | Ship Guy',
 'meta':'Car shipping in Sioux Falls, SD, where Interstate 29 meets Interstate 90. Honest 2 to 5 day windows, health system and card center relocations, lot handoffs for the Cathedral district and the East Bank, curbside pickups on the south side, the west side, Harrisburg, Brandon, and Tea, the blizzards, the ice, and the river. Local office on South Reid Street on the East Bank. Free quote.',
 'h1':'Car Shipping in<br>Sioux Falls, <span class="accent">South Dakota</span>',
 'lede':'Open, enclosed, and expedited auto transport across Sioux Falls and the Big Sioux valley, planned around 29, 90, the fair, the opener, the blizzards, and the honest windows of a pass-through state.',
 'tel':'+16057022358','disp':'(605) 702-2358','brand':'Sioux Falls','keyword':'car shipping in sioux falls',
 'localterms':['sioux falls','interstate 29','interstate 90','south reid street','east bank','big sioux','cathedral district','harrisburg','brandon','sioux city','fargo','minnesota','black hills','interstate 229','minnesota avenue','cliff avenue','41st street','downtown','south side','river','health systems','card centers','pork plant','guard wing','colleges','blizzards','omaha','minneapolis','des moines','kansas city','rapid city','chicago','denver','dallas','plowed','all saints','west side','tea','winnipeg','brookings','watertown','mitchell','louise avenue','mall','12th street','fairgrounds','hartford','57th','85th','bridges','8th','10th','26th','big-box','arena','cell lot','fly-and-ship','quartzite','phillips avenue','falls','14th street','angled parking','depot','lofts','warehouses','mckennan park','pettigrew heights','whittier','north end','airport','rail yards','arrowhead parkway','dell rapids','canton','vermillion','yankton','snowbirds','arizona','texas','18th street','traveling nurses','residents','physicians','contract dates','banks','production dates','ag technology','fulfillment center','universities','33rd','22nd','late august','fighters','orders','taxes','empire fair','rally','motorcycles','tournament','pheasant opener','forty inches','forty below','no travel','towed','april 2013','two inches of ice','block heater','electric car','tornadoes','2019','hospitals','diversion channel','river parks','hail','salt','sand','bill of lading','fmcsa','winch','console'],
}, BODY, FAQ)
