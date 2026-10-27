import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("2–4 Days","Honest Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Bangor, Maine','Car shipping at the top of the carrier run, where Interstate 95 crosses the Penobscot and most trucks turn around',
 ['Car shipping in Bangor runs off Interstate 95, which passes the west side of the city. Ship Guy is a licensed auto transport broker with an office on Olive Street near downtown.',
  'We book vetted carriers across Penobscot County, from Orono and Old Town to Hampden and Brewer. The trucks belong to the carriers we vet.',
  'Interstate 95 runs along the west side with exits at Hammond, Union, Broadway, and Stillwater. Interstate 395 crosses the river to Brewer. Route 1A runs to Ellsworth and Bar Harbor. Route 2 follows the river to Orono. Route 9 runs east to Canada, and Route 15 runs north to the lakes.',
  'This page covers 95, the spur, downtown, the Broadway side, the mall, Brewer, Orono, and the coast. It also covers the medical center, the university, the airport, the 1976 flood, and where the trucks stop.'],
 'Bangor at a glance',
 ['Most pickups happen within 2 to 4 days. Bangor is where the Maine run ends for most carriers. A pickup here goes on the truck that came this far.',
  'Portland is a same-day haul. Boston and Manchester take a day. Hartford, Albany, and New York take one to two. Philadelphia and Washington take two, and Florida takes four to five.'],
 'Tell us the side of 95. Downtown and the Broadway streets need a meeting spot. The mall side, Brewer, and Hampden usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 95, Interstate 395, Route 1A, Route 2, Stillwater Avenue, and the Bridges',
 prose(
  L('Bangor is the last city on the carrier run. The trucks that reach it have driven the whole length of Maine.'),
  P('Interstate 95 arrives free from Augusta and runs along the west side of the city. The exits at Hammond, Union, Broadway, Stillwater, and Hogan serve the city. The Orono exit sits eight miles north. Beyond Orono, 95 runs another hundred miles to Houlton with few towns beside it. Most carriers turn around here. The Turnpike tolls end at Augusta.'),
  P('Interstate 395 is the spur from 95 across the south side and over the river to Brewer. Route 1A continues from it to Ellsworth and the Bar Harbor road. Route 2 follows the river north through Veazie to Orono and Old Town. Route 9 is the Airline, the road east through Brewer to Calais and the border. Route 15 runs north from Broadway to Dover-Foxcroft and Moosehead.'),
  P('Stillwater Avenue and Hogan Road carry the mall and the big lots on the north side. Hammond Street and Union Street run from 95 into downtown. Broadway runs north from downtown past the old houses. State Street runs east to the medical center on the river. Main Street runs south toward Hampden and the waterfront. The two bridges cross to Brewer.'),
  P('The carriers come off 95 at Stillwater and Hammond, and off the spur at Main Street. The mall on Stillwater, the Bass Park arena, and the Hermon truck stop have the usual meeting lots. No road in the county charges a toll.'),
  P('Our office is on Olive Street, a few minutes from downtown and the Hammond Street exit.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, Broadway, the Tree Streets, the Mall Side, Brewer, Hampden, Orono, and the Coast',
 prose(
  L('Bangor is a river city with a downtown of old brick and a mall side built for trucks. The university town sits just upriver.'),
  P('Downtown sits where the Kenduskeag meets the Penobscot. It is a tight grid of brick blocks around Main, Central, and Harlow. The streets are narrow and the parking is angled. A trailer cannot work the downtown grid. The driver meets you at the waterfront lots, at the arena, or on lower Main Street. The Tree Streets above downtown are the same, and the handoff moves to the main road.'),
  P('The Broadway neighborhood north of downtown is the historic district. Big houses and old trees line narrow streets. The driver meets you on Broadway or at the hospital lots on State Street. Fairmount and Little City along Hammond and Ohio are older grids with wider streets. The curb works on most blocks.'),
  P('The mall side along Stillwater and Hogan Road is retail, hotels, and the lots the carriers prefer. The subdivisions off Essex, Kenduskeag, and Griffin Road have wide streets, and the truck reaches the curb. Capehart by the airport is the old base housing, and the streets are wide. Hermon by the truck stop is a town of wide roads and warehouses.'),
  P('Brewer across the river has the hospital offices, the Wilson Street strip, and grids with wide streets. The curb works. Hampden to the south is subdivisions and the academy. The driver meets you on Route 1A or at the curb. Orono and Old Town upriver are the university and the mill town. The village streets are narrow, and the campus lots are wide. Ellsworth, the coast, and the island sit an hour southeast. The summer roads there are too narrow for a trailer. All of them price the same as Bangor.'),
 )))

ROUTES=[("Portland, ME","I-95 · ~130 mi","Same day","$170–$270"),("Boston, MA","I-95 · ~240 mi","1 day","$250–$370"),
 ("Manchester, NH","I-95/I-93 · ~230 mi","1 day","$250–$370"),("Hartford, CT","I-95/I-84 · ~340 mi","1 day","$310–$450"),
 ("Albany, NY","I-95/I-90 · ~390 mi","1–2 days","$340–$490"),("New York, NY","I-95 · ~450 mi","1–2 days","$390–$560"),
 ("Philadelphia, PA","I-95 · ~540 mi","2 days","$440–$630"),("Washington, DC","I-95 · ~680 mi","2 days","$500–$720"),
 ("Charlotte, NC","I-95/I-85 · ~1,030 mi","3 days","$730–$1,020"),("Orlando, FL","I-95 · ~1,530 mi","4–5 days","$930–$1,300")]
BODY.append(rate_table('Lanes &amp; Costs','Bangor Car Shipping Lanes and Estimated Costs',
 'The lanes Penobscot County cars take most, with estimated open-trailer ranges. Your exact route prices on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates leaving Bangor, sedan in running order, open trailer. SUVs and pickups add 10 to 25 percent, and an enclosed trailer adds more. Bangor adds about a hundred thirty miles to every Portland lane, and the price follows. Season and the trucks that come this far north set the real figure.',
 prose(
  P('Bangor prices over Portland on every lane by the extra hundred thirty miles and the extra day. The carriers that come this far want a full trailer for the run south. That is why a flexible date matters more here than anywhere in the state. The Boston and New York lanes run most weeks. The Florida lane runs on the snowbird calendar.'),
  P('North of Bangor, the price climbs again and the window stretches to a week. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Medical Center, the University, the Airport, the Guard, the Lab, and the Woods',
 prose(
  L('Bangor relocates physicians, professors, pilots, and scientists bound for the coast. The medical center moves more people than anyone north of Portland.'),
  P('The medical center on State Street is the hospital for the whole northern half of the state. Nurses come on contracts all year and residents every June. Physicians arrive with a closing date and a second car. The second hospital on Broadway and the health centers in the small towns recruit the same way. We supply the paperwork a reimbursed move needs.'),
  P('The university in Orono brings cars in each late August and sends them home in May. A parent ships the car from Massachusetts, New York, or farther. An adult signs at a campus lot. The faculty arrive each summer. The university on the west side of Bangor and the community college run the same calendar.'),
  P('The airport is a diversion field for the Atlantic crossing. It is also home to the refueling wing of the Guard. The aviation shops at the airport relocate mechanics and engineers on contract. The wing rotates airmen on orders, and the orders pay for one car. We move the other. Ship Guy is a private broker with no military connection, and the timing is on the <a href="military-car-shipping.html">military</a> page.'),
  P('The genetics lab in Bar Harbor recruits scientists from every state. The car comes through Bangor on the way to the island. The bank headquartered downtown and the turbine plant relocate staff on their own calendars. Summer residents ship cars to the coast in June and home in September. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Waterfront Concerts, the State Fair, Acadia Traffic, the 1976 Flood, and the Snow',
 prose(
  L('Bangor runs on a waterfront concert season, a fair at Bass Park, and a five-month winter.'),
  P('The waterfront amphitheater fills Main Street and Railroad Street on concert nights from May through September. The lots by the river are gone by five on a show night. A downtown handoff that evening moves to the mall or to the morning. The state fair fills Bass Park and the arena lots for a week at the end of July.'),
  P('Acadia traffic fills Route 1A and the Bar Harbor road from late June through October. The cruise ships fill the island in the fall. A delivery to the coast in summer meets the truck in Ellsworth or on Route 1A. Move-in week at the university brings a few thousand cars to Orono in late August. The canoe race in April closes the roads along the Kenduskeag for a Saturday.'),
  P('The Kenduskeag floods downtown. The 1976 Groundhog Day gale pushed the river up twelve feet in minutes. The downtown blocks went under water. Ice jams on the stream flood the low streets in a thaw. A pickup downtown in a thaw moves up the hill for a day. The December 2023 storm flooded the river towns to the south the same way.'),
  P('Snow runs sixty-five inches a year, and the first storm comes in November. Nor’easters close 95 a few times a winter. The carriers park in Augusta or Portland until it reopens. A winter pickup can lose a day or two, and you hear before it does. The 1998 ice storm took the power out for a week. Mud season posts the back roads from March into May. Route 9 and Route 15 post with them.'),
 )+chips(["Downtown","Main Street","Central Street","Harlow Street","Waterfront","Kenduskeag","Tree Streets","Broadway","West Broadway","State Street","Fairmount","Hammond Street","Little City","Ohio Street","Union Street","Mall Side","Stillwater","Hogan Road","Essex Street","Griffin Road","Capehart","Airport","Bass Park","Hermon","Brewer","Wilson Street","Hampden","Veazie","Orono","Old Town","Holden","Eddington","Ellsworth","Bar Harbor"])
 +NOTE('Serving Bangor, Brewer, Orono, and all of Penobscot County, downtown block or mill town. Tell us the side of 95 and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Bangor?',
 prose(
  L('Open trailers carry most of the cars that leave Penobscot County. The lane table is priced for one.'),
  P('An enclosed trailer keeps a car out of the salt, the slush, and the plow sand. Summer residents shipping a collector car to the island book one. Snowbirds with a new car book one for the Florida run.'),
  P('A commuter car or a woods truck rides open and comes off the trailer unchanged. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages lay the two side by side.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A number, a handoff at the mall or the truck stop in Hermon, and a car at delivery. The truck that came this far north sets the week.'),
  P('Say yes to the number, and we book the car onto a carrier already making the run north. The lot and the window reach you once the truck is set. You and the driver go around the car together, and the Bill of Lading records its condition. Two signatures close it, and the same sheet comes out at delivery.'),
 )+ULI([
  "Empty the cabin and the trunk of anything personal",
  "Fuel down to a quarter tank",
  "Pictures of every side and the odometer before the truck comes",
  "One working key for the driver, and a word about any fault",
  "Turn off any aftermarket alarm",
  "Downtown or on Broadway, meet the truck at the waterfront lots or the arena",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Bangor Drivers Choose Ship Guy',
 prose(
  L('We catch the carriers that come all the way to the top of the run. We tell you the real window and plan around the snow and the mud.'),
  P('Ship Guy is an FMCSA-licensed broker backed by a $75,000 surety bond. Both appear in the federal register. Our office is on Olive Street in Bangor.'),
  P('The coordinator who prices the move stays with it until the car is signed for. Open, enclosed, and expedited transport are on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Bangor','28 Olive St #445A','Bangor, ME 04401','+12076057681','(207) 605-7681','ET',
 '28+Olive+St+%23445A,+Bangor,+ME+04401','Visit Us','Find Ship Guy in Bangor',
 'Our office is on Olive Street, a few minutes from downtown and the Hammond Street exit on 95.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4354.8436686236055!2d-68.7830268!3d44.7820493!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4cae4b80c62234f3%3A0x2cc2f51e5ce9f8d0!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793025078537!5m2!1sen!2sus'))

FAQ=[
 ("Why does a Bangor pickup take two to four days, and the far north longer?","Because Bangor is where the Maine run ends for most carriers. A truck comes up 95 from Boston, drops and loads along the way, and turns around here. A pickup in Bangor goes on that truck, which is two to four days in a normal week. North of Bangor, few carriers go at all. Plan on three to six days there and a meeting spot in Bangor or Houlton. A flexible date range is the biggest help."),
 ("How much does it cost to ship a car from Bangor to Boston or Florida?","Boston runs two hundred fifty to three hundred seventy dollars for a sedan. That is about two hundred forty miles down 95. Orlando runs nine hundred thirty to thirteen hundred, about fifteen hundred thirty miles the same way. Bangor adds about a hundred thirty miles to every Portland lane, and the price follows. An SUV or pickup adds 10 to 25 percent."),
 ("Can the carrier come to my street downtown or on Broadway?","Usually not. Downtown is a tight brick grid with angled parking, and the Broadway streets run under old trees. The driver meets you at the waterfront lots, at the arena, or at the hospital lots. The mall side, Brewer, and Hampden usually allow the curb."),
 ("Can you ship my student’s car to the university in Orono?","Yes, and it is the move we make most each August. Cars come from Massachusetts, New York, and farther. A parent books, and an adult signs at a campus lot. Move-in week fills the village streets, so the handoff never happens on them. The cars go home the same way in May. Book two or three weeks ahead, because the late-August trucks fill fast."),
 ("Do you ship cars for people relocating to the medical center or the lab in Bar Harbor?","Yes, all year. The medical center brings in nurses, residents, and physicians every month. The lab on the island recruits scientists from every state. Many ship a second car behind the move. The handoff works at the hospital lots or at the mall. A car for the island meets the truck in Ellsworth. We provide the paperwork a reimbursed move needs."),
 ("Can you ship a car to or from Brewer, Orono, or the coast?","Yes, and all of them price the same as Bangor. Brewer rides the same carriers off the spur, and Orono rides them off 95 to the north. The coast is different in summer. The roads onto the island and the peninsulas are too narrow for a trailer. The driver meets you in Ellsworth or on Route 1A. Send the full address, and we tell you which applies."),
 ("What happens if a nor’easter hits on my pickup day?","The carriers park in Augusta or Portland until 95 reopens. A winter pickup can slip a day or two. You hear from us before it does. In a thaw, ice jams on the Kenduskeag flood the low downtown streets. A pickup there moves up the hill. Mud season posts the back roads in spring, and the driver meets you on a paved state route."),
 ("Can you ship a car that does not run from Bangor?","Yes. The carrier comes with a winch, and the loading time is priced in from the first quote. The mall lot on Stillwater or the Hermon truck stop gives the driver room to work. Tell us whether the car rolls, steers, and brakes."),
 ("Do you ship cars north to Houlton and Aroostook County?","Yes, with honest timing. Few carriers go north of Bangor, and the ones that do want a full load. Plan on three to six days and a meeting spot in Bangor or Houlton. The potato harvest in September and the posted roads in spring stretch the window further. A wide date range is the biggest help."),
 ("What do you need for a Bangor car shipping quote?","Both addresses, with the side of 95 or the town here. Year, make, and model. Whether it runs. Open or enclosed. A date range rather than one day, which matters more at the top of the run than anywhere. Those five answers are the whole request, and the Bangor number is back within the day."),
]
BODY.append(faq_section(FAQ,'Bangor FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Bangor?','Two minutes on the form above prices your lane. Send the side of 95 and a date range. The next carrier making the run north takes it.','+12076057681','(207) 605-7681','Get your free Bangor quote'))

build({
 'slug':'auto-transport-bangor-maine',
 'title':'Car Shipping in Bangor, ME — Auto Transport | Ship Guy',
 'meta':'Car shipping in Bangor, ME at the top of the carrier run, where Interstate 95 crosses the Penobscot. Honest two-to-four-day pickups, medical-center and university moves, Orono move-in, downtown and Broadway meeting spots, mall-side and Brewer curbside pickups, Acadia traffic, the 1976 flood, the snow, and the far north. Local office on Olive Street. Free quote.',
 'h1':'Car Shipping in<br>Bangor, <span class="accent">Maine</span>',
 'lede':'Open, enclosed, and expedited auto transport across Penobscot County, planned around 95, the river, the university calendar, and the winter.',
 'tel':'+12076057681','disp':'(207) 605-7681','brand':'Bangor','keyword':'car shipping in bangor',
 'localterms':['bangor','penobscot','interstate 95','houlton','interstate 395','spur','route 1a','ellsworth','bar harbor','route 2','route 9','airline','calais','route 15','dover-foxcroft','moosehead','stillwater','hogan road','hammond street','union street','broadway','state street','main street','bridges','downtown','kenduskeag','central street','harlow','brick','waterfront','arena','bass park','tree streets','west broadway','historic district','fairmount','little city','ohio street','mall side','essex','griffin road','capehart','airport','hermon','truck stop','brewer','wilson street','hampden','academy','veazie','orono','old town','university','campus','island','coast','medical center','nurses','residents','second hospital','community college','diversion','refueling wing','guard','aviation shops','orders','genetics lab','bank','turbine plant','summer residents','concerts','amphitheater','railroad street','state fair','acadia','cruise ships','move-in week','canoe race','1976','groundhog day','ice jams','december 2023','snow','nor’easters','1998 ice storm','mud season','posted','potato harvest','aroostook','portland','boston','manchester','hartford','albany','new york','philadelphia','washington','charlotte','orlando','augusta'],
}, BODY, FAQ)
