import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("3–6 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Bozeman, Montana','Car shipping in the Gallatin Valley, where Interstate 90 crosses the pass, the university fills the town each August, and the transplants keep coming',
 ['Car shipping in Bozeman runs on Interstate 90, which crosses the north edge of town. Ship Guy is a licensed auto transport broker with an office on North 19th Avenue.',
  'We book vetted carriers across Bozeman, from downtown and the Northeast to the subdivisions off Baxter and Cottonwood. Belgrade and Four Corners ride the same trucks. Carriers own the trucks. The license and the bond sit with Ship Guy.',
  'Interstate 90 runs along the north edge of the city and climbs Bozeman Pass to Livingston. Highway 191 runs west as Huffine Lane to Four Corners and south through the canyon to Big Sky. Highway 86 climbs Bridger Canyon to the ski hill. 19th Avenue and 7th Avenue run from the interstate to the campus.',
  'This page covers 90, the pass, 191, 19th Avenue, Main Street, the campus blocks, and the new subdivisions. It also covers the university, the hospital, the software and laser firms, the ski towns, and the snow.'],
 'Bozeman at a glance',
 ['Figure 3 to 6 days for a pickup. Bozeman sits on the 90 lane between Seattle and Chicago. The carriers crossing Montana stop when a load justifies it. The Billings pool is two hours east. The Salt Lake trucks come up 15 and over Monida Pass.',
  'Billings is a same-day haul. Great Falls, Missoula, Spokane, and Salt Lake City take one to two days. Boise, Denver, and Seattle take two, and Las Vegas and Minneapolis take three.'],
 'Tell us the neighborhood. Downtown, the campus blocks, the canyons, and the gated ranch communities meet the truck on a main road. The subdivisions on the west side, the Northeast grids, Belgrade, and Four Corners usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 90, Bozeman Pass, Highway 191, Huffine Lane, Bridger Canyon, 19th Avenue, 7th Avenue, Main Street, and Kagy Boulevard',
 prose(
  L('Bozeman is a grid at the foot of the Bridgers with the interstate along the top. A carrier stays on 90 and the avenues and keeps out of the canyons.'),
  P('Interstate 90 comes from Billings over Bozeman Pass and drops along the north side of the city. It runs west past Belgrade to Butte and Missoula. The 19th Avenue exit serves the west side and the strip. The 7th Avenue exit serves the north side. The East Main exit serves downtown. The Belgrade exit serves the airport. The pass between Bozeman and Livingston climbs to fifty-seven hundred feet. The state requires chains or closes it a few times each winter.'),
  P('Highway 191 runs west from Main Street as Huffine Lane to Four Corners. From there it runs south through the Gallatin Canyon to Big Sky and West Yellowstone. The canyon is two lanes along the river with no shoulders. A trailer takes it slowly in daylight. Highway 86 climbs Bridger Canyon to the ski hill and the ranches. 19th Avenue is the commercial strip from the interstate south to Kagy. 7th Avenue is the older strip. Main Street runs through downtown on brick blocks with the Mendenhall and Babcock one-way pair on either side. Kagy Boulevard runs along the south edge of the campus. Oak Street and Baxter Lane cross the west side.'),
  P('The carriers come off 90 at 19th Avenue. They meet at the big-box lots on 19th or the shopping center lots at 19th and Oak. The lots at the fieldhouse and the stadium work outside a game. So do the lots along Huffine at Four Corners and the truck stops at the Belgrade exit. The airport is ten minutes west for a fly-and-ship.'),
  P('Our office is on North 19th Avenue, two blocks north of Main Street on the west side.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the Northeast, the Campus Blocks, the South Side, the West Side Subdivisions, Baxter Meadows, Story Mill, Bridger Canyon, Sourdough, Belgrade, and Four Corners',
 prose(
  L('Bozeman is a brick downtown, an old grid, and new subdivisions spreading west faster than the maps. The truck meets the old grid on a main road and the new streets at the curb.'),
  P('Downtown is eight blocks of Main Street with angled parking and the one-way pair behind it. The driver meets you on Mendenhall or at the lots by the library. The Northeast between Main and the tracks is the old railroad grid, with the cannery district and breweries. The curb works where the streets allow. The campus blocks between Main and Kagy are student rentals with cars on both curbs. The handoff happens at the stadium lots or on College Street.'),
  P('The south side from Kagy to Sourdough is bigger houses on wider streets. The truck reaches the curb until the streets turn to gravel in the foothills. The west side from 19th Avenue to Cottonwood is the new town. The subdivisions sit on open ground with wide streets and no trees yet. The curb works nearly everywhere. Baxter Meadows and Story Mill on the north side are the same.'),
  P('Bridger Canyon is ranches and cabins on a paved road with gravel driveways. The handoff happens at the fish hatchery lot or on the highway. Sourdough and Hyalite south of town are canyon roads, and the handoff moves to the paved road. Belgrade is a working town around the airport with wide streets, and the truck comes to the house. Four Corners is subdivisions along Huffine.'),
  P('Belgrade, Four Corners, and Gallatin Gateway ship with the same trucks and price the same as Bozeman. Manhattan and Three Forks do too. Livingston is over the pass and adds the pass. Big Sky adds the canyon and a figure. The gated ranch communities meet the truck at the gate.'),
 )))

ROUTES=[("Billings, MT","I-90 · ~140 mi","Same day","$150–$240"),("Great Falls, MT","US-287/I-15 · ~185 mi","1 day","$220–$340"),
 ("Missoula, MT","I-90 · ~200 mi","1 day","$230–$350"),("Spokane, WA","I-90 · ~400 mi","1–2 days","$380–$540"),
 ("Salt Lake City, UT","I-90/I-15 · ~440 mi","1–2 days","$400–$570"),("Boise, ID","I-15/I-84 · ~500 mi","2 days","$430–$620"),
 ("Denver, CO","I-90/I-25 · ~700 mi","2 days","$500–$720"),("Seattle, WA","I-90 · ~680 mi","2 days","$560–$800"),
 ("Las Vegas, NV","I-15 · ~850 mi","3 days","$650–$920"),("Minneapolis, MN","I-90/I-94 · ~980 mi","3 days","$650–$920")]
BODY.append(rate_table('Lanes &amp; Costs','Bozeman Car Shipping Lanes and Estimated Costs',
 'The lanes Gallatin County cars ride most, each with an open-trailer estimate. Price your own above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates out of Bozeman for a running sedan, open trailer. An SUV or a pickup costs 10 to 25 percent more, and enclosed costs more than that. The week and the carriers crossing 90 that week set the real figure.',
 prose(
  P('Bozeman prices with Billings on the long lanes and a little above it on the short ones. The Billings pool is two hours away. The Seattle lane rides 90 west and fills twice a week. The Salt Lake lane rides 15 over Monida Pass. The Denver lane rides 90 and 25 through Wyoming. The California and Colorado lanes fill each summer with the transplants, and the price rises with them.'),
  P('A late August move-in at the university or a ski-season start in November means a busy week. The <a href="car-shipping-cost.html">cost guide</a> covers size, condition, and timing one by one.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The University, the Transplants, the Hospital, the Software and Laser Firms, the Airport, the Ski Towns, the Guard, and the Ranches',
 prose(
  L('Bozeman relocates students, professors, engineers, nurses, remote workers, and ski bums. The transplants move the most.'),
  P('The city is the fastest-growing in the state. The newcomers come from California, Colorado, Washington, and Texas with a car or two each. The Seattle and Denver lanes bring them. The handoff happens at the 19th Avenue lots or the house. The university on the south side takes seventeen thousand students, and the cars arrive in late August. A parent sets it up, and an adult signs at the stadium lots. The cars leave in May.'),
  P('The hospital on the east side brings residents each June and traveling nurses all winter. The software campus on the north side and the laser and optics firms relocate engineers on start dates. So do the wader and backpack makers. The handoff happens at the lots nearest the office. Employers that reimburse the move get the paperwork in whatever form they want.'),
  P('The ski towns hire each November. The cars come up 191 to Big Sky and over the hill to Bridger Bowl. The ranches ship pickups and horse trailers on their own calendar. The Guard units in the valley rotate people on orders, and the handoff happens at the armory lots. Ship Guy is a private broker and not part of the Guard. The <a href="military-car-shipping.html">military</a> page covers orders and timing.'),
  P('Second-home owners come in June and December and send a car ahead. What a state line changes is on the <a href="state-to-state-car-shipping.html">state-to-state</a> page.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Move-In Week, Bobcat Saturdays, Sweet Pea, the Summer Traffic, the Pass, the Cold, the Smoke, and the 2022 Flood',
 prose(
  L('Bozeman runs on a campus calendar and a tourist calendar. The weather problem is a pass that closes, a cold that stops the trucks, and a smoky August.'),
  P('Move-in week in late August fills the campus blocks and 19th Avenue. Bobcat Saturdays close the streets around the stadium. The November game against Missoula fills every motel in the years it comes to town. Sweet Pea takes Lindley Park and the east side for the first weekend in August. Music on Main closes downtown on summer Thursday evenings. The summer traffic to the park runs 191 at a crawl from June to September. A late August date wants three weeks of notice.'),
  P('Bozeman Pass closes for ice and crashes a few times each winter. The state requires chains on the grade. The carriers wait in Livingston or Bozeman until it reopens, usually a few hours. The wind at Livingston tips trailers on 90, and the state posts advisories that hold the trucks. The January 2024 cold held the valley near thirty below. A carrier does not load a car at that temperature. The snow comes in October and stays until April, and a spring blizzard can land in May.'),
  P('The September 2020 fire in the Bridger foothills took more than two dozen homes northeast of town. Smoke settles in the valley in August most years, and the carriers keep moving through it. The June 2022 flood took out the roads into the park and closed 89 at Gardiner. The Livingston side of the pass flooded. We call before the day moves.'),
  P('Summer is short, dry, and mild. A thunderstorm holds the truck at the lot for an hour.'),
 )+chips(["Downtown","The Northeast","The Cannery District","The Campus Blocks","The South Side","Sourdough","Hyalite","Bridger Canyon","Story Mill","Baxter Meadows","Flanders Mill","Valley West","Cottonwood","Belgrade","Four Corners","Gallatin Gateway","Manhattan","Three Forks","Livingston","Big Sky"])
 +NOTE('Serving Bozeman, Belgrade, and the Gallatin Valley, west-side curb or canyon road. Tell us the part of town and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Bozeman?',
 prose(
  L('Open trailers handle most of the valley, and the figures above assume one.'),
  P('Enclosed keeps the gravel, the magnesium chloride, and the road grit off the paint. The collectors on the south side book it. So do the transplants moving a car worth more than the moving van. When the only truck crossing 90 that week is open, we tell you first and let you decide.'),
  P('A commuter car or a student’s wagon is fine in the open. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages lay the two side by side.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A figure, a lot on 19th Avenue, and a signature at delivery. Move-in or the start date sets the week.'),
  P('Accept the figure, and the car is placed with a carrier already crossing 90 that week. The lot and the window follow the same day. The driver walks the car with a camera at pickup and completes the Bill of Lading. You initial it, and the same sheet settles delivery.'),
 )+ULI([
  "Cabin and cargo area emptied of personal items",
  "No more than a quarter tank",
  "Each side and the odometer photographed before the truck arrives",
  "One good key plus a note about any faults",
  "Add-on alarms switched off",
  "On a canyon road, in the student blocks, or at a gated ranch, expect a lot off 90",
 ])+prose(P('The sequence lives on the <a href="how-it-works.html">how it works</a> page, and the day-of list lives on the <a href="car-shipping-preparation.html">preparation</a> page.'))))

BODY.append(sec('Why Ship Guy','Why Bozeman Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already cross 90 each week. We know when the pass closes and which subdivisions the carrier maps have not caught up with.'),
  P('Anyone can check our FMCSA license and our $75,000 bond on the federal register. The office is on North 19th Avenue.'),
  P('A single coordinator follows your move from quote to delivery. The <a href="services.html">services</a> page describes open, enclosed, and expedited.'),
 )))

BODY.append(office('Bozeman','219 N 19th Ave #477','Bozeman, MT 59718','+14064139740','(406) 413-9740','MT',
 '219+N+19th+Ave+%23477,+Bozeman,+MT+59718','Visit Us','Find Ship Guy in Bozeman',
 'Our office is on North 19th Avenue, two blocks north of Main Street on the west side.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3440.7641406033845!2d-111.06271149999999!3d45.681850399999995!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x53454584e4946d89%3A0x8b1fd4e5dcdb1fa6!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793629882174!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Bozeman to Seattle or Denver?","Seattle runs five hundred sixty to eight hundred dollars for a sedan. That is about six hundred eighty miles west on 90. Denver runs five hundred to seven hundred twenty, about seven hundred miles down 90 and 25. Billings is the lowest lane on the table, two hours east on 90. An SUV or a pickup adds 10 to 25 percent."),
 ("Why does a Bozeman pickup take 3 to 6 days?","Because Montana is a pass-through market. The carriers crossing 90 between Seattle and Chicago stop when a load justifies it. The Billings pool is two hours away. A car waits for the next truck with room. A pass closure or a cold snap stretches the window further. We say so the day it does."),
 ("Can you deliver on a Montana State move-in date?","Yes. Cars arrive in late August and go home in May. A parent sets it up, and someone over eighteen signs at the lot. The blocks between Main and Kagy are full that week. The meeting point is the stadium lots or College Street. Your date sets the window."),
 ("Can the carrier come to my street in Bozeman?","On the west side, Baxter Meadows, Belgrade, and Four Corners, yes. The subdivisions have wide streets, and the truck reaches the curb. Send the full address, because the new streets outpace the carrier maps. Downtown and the campus blocks meet the truck on Mendenhall or at the stadium lots. Bridger Canyon, Sourdough, and the gated ranch communities meet it on the paved road or at the gate."),
 ("What happens if Bozeman Pass closes or the cold hits on my pickup day?","The truck waits in Livingston or Bozeman until the pass reopens, usually a few hours. A carrier does not load a car at thirty below, because the straps stiffen and the hydraulics slow. We call the moment the forecast turns. The pickup moves to the first workable day, and the figure holds."),
 ("Do you work with relocation packages at the software and laser firms?","Yes, every month. The software campus, the optics firms, and the gear makers relocate engineers on start dates. The packages usually pay for a car. We plan the pickup around the first day. The handoff happens at the lots nearest the office. Employers that reimburse the move get the paperwork in whatever form they want."),
 ("Can you ship a car to or from Big Sky, Livingston, or Belgrade?","Yes. Belgrade, Four Corners, and Gallatin Gateway ride the same carriers and price the same as Bozeman. Livingston is over the pass and adds the pass. Big Sky is an hour down the canyon and adds a figure. The gated communities meet the truck at the gate or in the village."),
 ("Can you ship a car during the summer park traffic or a Bobcat Saturday?","Yes, from a lot. The traffic to the park runs 191 at a crawl from June to September. The carriers stay on 90 and Huffine. A Bobcat Saturday closes the streets around the stadium, and the handoff moves to the 19th Avenue lots. The figure does not change."),
 ("Can you ship a car that does not run from Bozeman?","Yes. A winch truck comes, and the loading time is built into the figure. The big-box lots on 19th Avenue are flat. Tell us whether it rolls, whether it steers, and whether it brakes."),
 ("What do you need for a Bozeman car shipping quote?","Pickup and delivery addresses, with the subdivision or the canyon. The vehicle, and whether it runs. Open or enclosed, and the week around the move-in or the start date. Those get the Bozeman figure back before the day ends."),
]
BODY.append(faq_section(FAQ,'Bozeman FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Bozeman?','Two minutes on the form above and your lane has a Bozeman figure. Tell us the neighborhood and the week, and a carrier already crossing 90 takes the car.','+14064139740','(406) 413-9740','Get your free Bozeman quote'))

build({
 'slug':'auto-transport-bozeman-montana',
 'title':'Car Shipping in Bozeman, MT — Auto Transport | Ship Guy',
 'meta':'Car shipping in Bozeman, MT, in the Gallatin Valley on Interstate 90. Montana State move-in dates, the transplants from California and Colorado, hospital and software hires, curbside pickups in the west-side subdivisions, Belgrade, and Four Corners, main-road handoffs downtown, in the campus blocks, and on the canyon roads, Bozeman Pass, the cold, and the honest 3 to 6 day window. Local office on North 19th Avenue. Free quote.',
 'h1':'Car Shipping in<br>Bozeman, <span class="accent">Montana</span>',
 'lede':'Open, enclosed, and expedited auto transport across Bozeman, Belgrade, and the Gallatin Valley, planned around Interstate 90, the pass, the campus dates, the transplants, the snow, and the smoke.',
 'tel':'+14064139740','disp':'(406) 413-9740','brand':'Bozeman','keyword':'car shipping in bozeman',
 'localterms':['bozeman','gallatin valley','interstate 90','bozeman pass','fifty-seven hundred feet','chains','highway 191','huffine','gallatin canyon','big sky','west yellowstone','highway 86','bridger canyon','ski hill','bridger bowl','19th avenue','7th avenue','main street','mendenhall','babcock','east main','kagy','college street','oak street','baxter','cottonwood','belgrade','four corners','gallatin gateway','manhattan','three forks','livingston','monida pass','butte','missoula','downtown','library','northeast','cannery district','breweries','campus blocks','student rentals','south side','sourdough','hyalite','west side','subdivisions','baxter meadows','story mill','flanders mill','valley west','fish hatchery','gated ranch','gate','university','seventeen thousand','students','stadium','fieldhouse','transplants','california','colorado','washington','texas','fastest-growing','hospital','residents','traveling nurses','software campus','laser','optics','engineers','wader','backpack','ski towns','ranches','horse trailers','guard','armory','orders','second-home','move-in','bobcat saturdays','november game','sweet pea','lindley park','music on main','park traffic','ice','crashes','wind','advisories','january 2024','thirty below','snow','october','spring blizzard','september 2020','fire','foothills','smoke','june 2022','flood','gardiner','89','airport','truck stops','shopping center','fly-and-ship','billings','great falls','spokane','salt lake','boise','denver','seattle','las vegas','minneapolis','gravel','magnesium chloride','grit','bill of lading','fmcsa','winch'],
}, BODY, FAQ)
