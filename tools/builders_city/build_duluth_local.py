import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("2–4 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Duluth, Minnesota','Car shipping at the head of the lake, where the interstate ends and the hill begins',
 ['Car shipping in Duluth runs down Interstate 35 to the Twin Cities, a hundred fifty miles south. Ship Guy is a licensed auto transport broker with an office on West Superior Street downtown.',
  'We book vetted carriers across Duluth, from Park Point to Lakeside and up the hill to Hermantown. The carriers own the trucks. Ship Guy holds the license and the bond.',
  'Interstate 35 ends at the east end of downtown after running the waterfront through the tunnels. Highway 53 climbs the hill to the mall and runs north to the Iron Range. Highway 2 crosses the Bong Bridge to Superior and runs west. The Blatnik Bridge carries 535 across the bay, and London Road becomes 61 up the North Shore.',
  'This page covers 35, 53, 2, the two bridges, Superior Street, downtown, the hill, and the East End. It also covers the port, the hospitals, the campus, the marathon, the lake, and the winter.'],
 'Duluth at a glance',
 ['Most pickups happen within 2 to 4 days. The Twin Cities pool is two and a half hours south. The 35 carriers come up a few times a week. Summer weekends bring more of them.',
  'The Twin Cities ride a single day on the truck. Fargo and Madison take a day. Milwaukee, Des Moines, and Chicago take one to two. Omaha and Kansas City take two.'],
 'Tell us the neighborhood. The hillside streets, Park Point, and the East End mansions meet the truck on a main road. Lakeside, Duluth Heights, Piedmont, and the flats of West Duluth usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 35, Highway 53, Highway 2, Interstate 535, Superior Street, London Road, the Lift Bridge, and the Hill',
 prose(
  L('Duluth is a city on a hill above a lake, and the hill decides everything. A carrier stays on the flats along the water or on the plateau above.'),
  P('Interstate 35 comes up from the Twin Cities and drops down the hill at Spirit Mountain. It runs the waterfront through West Duluth and Lincoln Park. It passes under downtown in a series of tunnels and ends at 26th Avenue East. London Road takes over there. The 21st Avenue West interchange ties it to 53 and 535. The locals call that one the Can of Worms. Highway 53 climbs Piedmont Avenue to the mall and Hermantown and runs north to Virginia and the Range. Highway 2 crosses the bay on the Bong Bridge to Superior and runs west to Grand Rapids.'),
  P('Interstate 535 crosses the bay on the Blatnik Bridge, the high bridge to Superior. It is the one the trucks use. Superior Street is the downtown main street, one block up from the water. London Road runs east along the lake past the mansions and becomes Highway 61 at the city line. Lake Avenue runs down to Canal Park and over the lift bridge to Park Point. The bridge lifts for every ship, and the traffic waits. The avenues up the hill from 1st to 40th are among the steepest streets in the state. A trailer does not climb them.'),
  P('The carriers come off 35 at Lake Avenue, 21st Avenue West, or Mesaba Avenue. The mall lots at the top of 53 are the usual meeting spot. The big-box lots along Central Entrance work too. So do the Canal Park lots on a weekday and the lots at the West Duluth shopping centers. The airport cell lot up the hill works for a fly-and-ship.'),
  P('Our office is on West Superior Street downtown, a few blocks from the Depot and Canal Park.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, Canal Park, Park Point, Lincoln Park, West Duluth, the Hillside, Chester Park, the East End, Lakeside, Duluth Heights, Piedmont, and Hermantown',
 prose(
  L('Duluth is old brick on the waterfront, old houses on the hill, and a newer city above. The truck meets the hill on a flat road.'),
  P('Downtown runs along Superior Street and First Street, brick blocks and a skywalk system against the hill. The driver meets you at the lots on Michigan Street or at the Depot. Canal Park below it is hotels and the lakewalk on short crowded streets. The handoff moves to the Lake Avenue lots. Park Point across the lift bridge is a seven-mile sandbar with one road. A trailer does not cross the bridge, and the handoff happens in Canal Park.'),
  P('The Hillside between downtown and the Heights is the oldest neighborhood. Narrow streets of old houses climb the grade. The avenues ice first and close first. The driver meets you on Superior Street or at the hospitals. Chester Park and the campus blocks above it are the same. The lots at the university take the handoff. The East End along London Road is the mansions and the big lots. The curb works on London Road and the side streets near it.'),
  P('Lakeside and Lester Park out past 40th Avenue East are flat grids along the lake. The truck reaches the curb. Lincoln Park and West Duluth along the bay are plain grids on the flats below the hill. The curb usually works. Morgan Park and Gary at the far west end are the old company towns. Duluth Heights and Piedmont on the plateau are postwar subdivisions around the mall. The curb works nearly everywhere. Hermantown beyond them is the same with longer driveways.'),
  P('Superior across the bay ships with the same trucks and prices the same as Duluth. So do Hermantown, Proctor, and Cloquet. Two Harbors up the shore adds twenty-five miles. The Range towns ride the 53 carriers and add a day.'),
 )))

ROUTES=[("Minneapolis / St. Paul, MN","I-35 · ~150 mi","Same day","$200–$310"),("Fargo, ND","US-2/I-94 · ~250 mi","1 day","$250–$380"),
 ("Madison, WI","US-53/I-94 · ~330 mi","1 day","$300–$440"),("Milwaukee, WI","US-53/I-94 · ~390 mi","1–2 days","$330–$470"),
 ("Des Moines, IA","I-35 · ~400 mi","1–2 days","$330–$470"),("Chicago, IL","US-53/I-94 · ~465 mi","1–2 days","$380–$540"),
 ("Omaha, NE","I-35/I-80 · ~530 mi","2 days","$420–$600"),("Kansas City, MO","I-35 · ~590 mi","2 days","$450–$650"),
 ("Denver, CO","I-35/I-80 · ~1,060 mi","2–3 days","$700–$980"),("Phoenix, AZ","I-35/I-40 · ~1,800 mi","4 days","$1,000–$1,400")]
BODY.append(rate_table('Lanes &amp; Costs','Duluth Car Shipping Lanes and Estimated Costs',
 'The lanes Twin Ports cars run most, with estimated open-trailer ranges. Price your own route on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Duluth for a sedan that runs, open trailer. Figure 10 to 25 percent more for an SUV or a pickup, and more again for enclosed. Your date range and the trucks coming up 35 that week set the real figure.',
 prose(
  P('Duluth prices like the far end of the Twin Cities pool, a hundred fifty miles past it. The Twin Cities lane rides 35 and fills on the weekends. The Chicago lane rides 53 to 94 through Eau Claire. The Fargo lane rides 2 across the north. The Arizona lane fills each October with the snowbirds, and the price rises with the demand.'),
  P('A move-in date in late August or the marathon weekend means a busy week. How size, condition, and the date range shape the figure is in the <a href="car-shipping-cost.html">cost guide</a>.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Two Hospitals, the Port, the Campus, the Guard Wing, the Airplane Maker, the Railroad, and the Retirees',
 prose(
  L('Duluth relocates nurses, physicians, professors, students, airmen, and longshoremen. The two hospitals move the most.'),
  P('The two hospital systems downtown serve the whole north of the state. One of them opened a new tower downtown. Both bring residents each June and hire traveling nurses year round. Physicians arrive on contract dates from everywhere. The handoff for all of them happens on Superior Street or at the mall. If the hospital or an employer reimburses the shipment, the paperwork comes from us.'),
  P('The port on the bay moves ore, grain, and coal from March until the last ship in January. The ore docks and the elevators move managers on contract dates. The railroad’s yard in Proctor moves crews on bid cycles. The Guard’s fighter wing at the airport rotates airmen on orders. The airplane maker beside it brings engineers on project dates. Ship Guy is a private broker with no tie to the Guard.'),
  P('The university on the hill takes student cars in late August and sends them home in May. The college beside it does the same, and the community college up the hill follows. A parent sets it up, and an adult signs at the handoff. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the paperwork for crossing a state line.'),
  P('Retirees come for the lake and leave for Arizona each October. Half the Twin Cities keeps a cabin up the shore. Some of them ship a second car up for the summer.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Marathon, the Blues Festival, Move-In Week, the Lights, the Last Ship, the Gales, the Lake Effect, the Ice, and the Fog',
 prose(
  L('Duluth runs on a lake calendar, and the weather problem is a lake that makes its own.'),
  P('The marathon closes London Road, the shore highway, and Canal Park on a Saturday in June. Every hotel is full. The blues festival fills Bayfront Park in August. Move-in week in late August fills the campus blocks. The lights at Bayfront run from Thanksgiving through December and fill the waterfront every night. The last ship leaves in January, and the first one comes back in March. Book three weeks ahead for a June or an August date.'),
  P('Winter runs from November into April. The lake makes its own snow, and the hill holds it. The avenues ice first, and the city closes the steepest ones. The Halloween blizzard in 1991 dropped three feet, and nothing has matched it. A storm closes 35 at Hinckley and 53 on the Range a few times each winter. The carriers wait in the Twin Cities until the plows finish. A carrier does not load a car at thirty below.'),
  P('The gales of November push the lake over the lakewalk. The October 2019 storm tore the lakewalk apart and put the lake in Canal Park. The June 2012 flood dropped ten inches of rain in a night. The creeks ran through the streets. A handoff near the water moves up the hill for a day.'),
  P('Spring brings fog off the lake that shuts the airport and slows the bridges. Summer is cool by the water and hot on the plateau, and the lake keeps the storms short.'),
 )+chips(["Downtown","Superior Street","Canal Park","The Lakewalk","Park Point","The Hillside","Central Hillside","Chester Park","Kenwood","The East End","London Road","Congdon Park","Lakeside","Lester Park","Woodland","Lincoln Park","West Duluth","Denfeld","Spirit Mountain","Morgan Park","Gary","Duluth Heights","Piedmont","Miller Hill","The Airport","Hermantown","Proctor","Superior","Cloquet","Two Harbors"])
 +NOTE('Serving Duluth and the whole of the Twin Ports, Hillside avenue or Hermantown driveway. Tell us the neighborhood and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Duluth?',
 prose(
  L('Open trailers carry most of the Twin Ports, and the table above is priced for one.'),
  P('Enclosed keeps the salt, the hill sand, and the lake spray off the paint. East End collectors book it, and so do cabin owners with a car worth protecting. Ahead of a storm, the car takes the first truck with room. You hear that from us first.'),
  P('Open suits a commuter car or a student’s car. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages show the difference.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A figure, then a lot at the mall, then a signature at the other end. Your date range matters more than anything else here.'),
  P('When you approve the figure, the car goes to a carrier already planning a Duluth run that week. The lot and the window are agreed the same afternoon. At pickup the driver shoots photos and fills in the Bill of Lading. You initial it, and the delivery check works from it.'),
 )+ULI([
  "Everything personal out of the cabin and the trunk",
  "Fuel down to a quarter tank",
  "Photograph each side and the odometer before the truck comes",
  "One good key, and a note about any known faults",
  "Any add-on alarm turned off",
  "On the Hillside, in Canal Park, or on Park Point, expect a flat road or a lot",
 ])+prose(P('<a href="how-it-works.html">How it works</a> has the order of events, and <a href="car-shipping-preparation.html">preparation</a> has what to do before the truck comes.'))))

BODY.append(sec('Why Ship Guy','Why Duluth Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already come up 35 every week. We know which streets a trailer can climb and which ones it cannot.'),
  P('Our FMCSA license and our $75,000 bond are a public record on the federal register. The office is on West Superior Street downtown.'),
  P('One person at Ship Guy owns your move from the quote to the delivery call. The <a href="services.html">services</a> page explains open, enclosed, and expedited.'),
 )))

BODY.append(office('Duluth','317 W Superior St #456','Duluth, MN 55802','+12183924894','(218) 392-4894','CT',
 '317+W+Superior+St+%23456,+Duluth,+MN+55802','Visit Us','Find Ship Guy in Duluth',
 'Our office is on West Superior Street downtown, a few blocks from the Depot and Canal Park.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3372.355671628868!2d-92.1027702!3d46.783915199999996!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x52ae53dafbaab0e5%3A0xf7b8b01aeae60224!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793629280751!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Duluth to the Twin Cities or Chicago?","The Twin Cities run two hundred to three hundred ten dollars for a sedan. That is a hundred fifty miles down 35 and the lowest lane on the table. Chicago runs three hundred eighty to five hundred forty, about four hundred sixty-five miles on 53 and 94. An SUV or a pickup runs 10 to 25 percent higher."),
 ("Why does a Duluth pickup take 2 to 4 days?","Because the carriers are based in the Twin Cities, a hundred fifty miles south. They come up when a load justifies it. Summer weekends bring more of them. Give us a wide date range and the figure stays low. A tight one costs more."),
 ("Can the carrier come to my street on the Hillside or in the East End?","The East End, yes, on London Road and the flat side streets near it. The Hillside, no. The avenues are among the steepest streets in the state, and a loaded trailer does not climb them. The driver meets you on Superior Street or at the hospitals. Lakeside, Duluth Heights, Piedmont, and West Duluth usually allow the curb."),
 ("Can you deliver on a UMD move-in date?","Yes. Cars arrive in late August and leave in May. Mom or Dad books, and someone over eighteen signs at the lot. The campus blocks are jammed that week, so the meeting point is a campus lot or the mall. Your date fixes the window."),
 ("Do you ship cars for the hospitals and the port?","Yes, in every month. Both hospital systems take residents in June and traveling nurses all year. The handoff is on Superior Street. The port and the railroad move managers and crews on contract dates and bid cycles. If the employer pays you back, we write up what it needs."),
 ("Can you ship a car to or from Superior, Hermantown, or Two Harbors?","Yes. Superior across the bay rides the same carriers and prices the same as Duluth. Hermantown, Proctor, and Cloquet do too. Two Harbors adds twenty-five miles up the shore and a few hours on the day. The Range towns ride the 53 carriers and add a day."),
 ("What happens if a storm closes 35 on my pickup day?","The truck sits in the Twin Cities until the plows open 35, usually a day. We call when the closure posts. The pickup takes the next clear morning at the figure you were quoted. Give a January date some room."),
 ("Does the marathon affect my pickup?","Yes, for a weekend in June. The race closes London Road, the shore highway, and Canal Park on the Saturday. Every hotel in the city is full. We do not schedule a Duluth pickup on race day. The Friday and the Monday run normally."),
 ("Can you ship a car that does not run from Duluth?","Yes. A winch truck takes it, and the loading time is priced in from the start. The mall lots and the big-box lots on Central Entrance are flat. Say whether it rolls, steers, and brakes."),
 ("What do you need for a Duluth car shipping quote?","Where it starts and ends, with the neighborhood. What it is and whether it runs. Open or enclosed, and the widest date range you can live with. That is enough for a Duluth figure the same day."),
]
BODY.append(faq_section(FAQ,'Duluth FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Duluth?','Two minutes on the form above gets your lane a Duluth figure. Name the neighborhood and the date range, and a carrier already coming up 35 takes it.','+12183924894','(218) 392-4894','Get your free Duluth quote'))

build({
 'slug':'auto-transport-duluth-minnesota',
 'title':'Car Shipping in Duluth, MN — Auto Transport | Ship Guy',
 'meta':'Car shipping in Duluth, MN, at the head of Lake Superior where 35 ends. The honest 2 to 4 day window, hospital and port relocations, campus move-in, flat-road handoffs for the Hillside, Canal Park, and Park Point, curbside pickups in Lakeside and the Heights, the marathon, and the winter. Local office on Superior Street downtown. Free quote.',
 'h1':'Car Shipping in<br>Duluth, <span class="accent">Minnesota</span>',
 'lede':'Open, enclosed, and expedited auto transport across Duluth and the Twin Ports, planned around 35, the hill, the lake, the hospital calendar, the campus dates, and the winter.',
 'tel':'+12183924894','disp':'(218) 392-4894','brand':'Duluth','keyword':'car shipping in duluth',
 'localterms':['duluth','lake','interstate 35','twin cities','hill','superior street','highway 53','highway 2','bong bridge','blatnik bridge','535','london road','lift bridge','lake avenue','canal park','park point','downtown','hillside','chester park','east end','lakeside','lester park','lincoln park','west duluth','morgan park','gary','duluth heights','piedmont','hermantown','proctor','cloquet','superior','two harbors','iron range','range','virginia','grand rapids','fargo','madison','milwaukee','des moines','chicago','omaha','kansas city','denver','phoenix','arizona','snowbirds','can of worms','mesaba','central entrance','mall','depot','michigan street','skywalk','mansions','sandbar','spirit mountain','tunnels','airport','hospitals','residents','traveling nurses','physicians','new tower','port','ore','grain','coal','last ship','elevators','railroad','bid cycles','guard','fighter wing','airmen','airplane maker','engineers','university','college','community college','students','move-in','retirees','cabin','marathon','blues festival','bayfront','lights','gales','lake effect','halloween blizzard','1991','hinckley','october 2019','lakewalk','june 2012','flood','fog','salt','sand','spray','bill of lading','fmcsa','winch','eau claire','longshoremen','professors'],
}, BODY, FAQ)
