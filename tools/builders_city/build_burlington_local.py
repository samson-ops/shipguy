import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("2–5 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Burlington, Vermont','Car shipping on Lake Champlain, where Interstate 89 brings the trucks up from Boston and the lake, the campus, and the winter set the calendar',
 ['Car shipping in Burlington runs on Interstate 89, the one freeway into the north of Vermont. Ship Guy is a licensed auto transport broker with an Old North End office on North Street.',
  'We book vetted carriers across Burlington, from the waterfront to the Hill Section and out to Essex. The carriers drive their own trucks. The license and the bond are Ship Guy’s.',
  'Interstate 89 runs along the east side of the city between White River Junction and the Canadian border. The 189 spur drops to Shelburne Road. Route 7 runs north and south along the lake. Route 2 crosses east to Montpelier and west over the islands to New York. The Beltline carries the New North End.',
  'This page covers 89, the spur, Route 7, Main Street, the waterfront, the North Ends, and the hill. It covers the university, the medical center, the chip plant, the Guard wing, the mud, and the floods.'],
 'Burlington at a glance',
 ['A pickup here usually takes 2 to 5 days. Burlington is the end of the line for the 89 carriers out of Boston. The trucks come up two or three times a week. The pool is small, and the window stretches when the passes close.',
  'Albany, Manchester, Boston, and Hartford ride a single day on the truck. Portland and New York take a day. Philadelphia and Washington take one to two, and Florida takes three.'],
 'Tell us the neighborhood. Downtown, Church Street, the Hill Section, the campus, and the waterfront meet the truck on a main road. The New North End, South Burlington, Essex, Williston, and Shelburne usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 89, the 189 Spur, Route 7, Route 2, the Beltline, Main Street, Church Street, Pearl Street, and North Avenue',
 prose(
  L('Burlington is a small city on a hill above a lake, reached by one interstate and two routes. A carrier comes up 89 and stays on the flat roads below the hill.'),
  P('Interstate 89 comes up the Winooski valley from Montpelier. It runs along the east side of the city to Colchester and the border. Exit 13 is the 189 spur to Shelburne Road and the south side. Exit 14 is Williston Road and Main Street, the way into downtown and the campus. Exit 15 is Winooski. Exits 16 and 17 serve Colchester and the islands. Route 7 runs south through Shelburne and Middlebury to Rutland. Route 2 crosses east to Montpelier and west over the causeways and the islands to Plattsburgh. The Beltline runs from the Old North End up to the New North End along the river.'),
  P('Main Street climbs from the waterfront past City Hall to the university on the hill. A loaded trailer does not stop on the grade. Church Street is a pedestrian mall for four blocks, and no truck enters it. Pearl Street and College Street cross the hill. North Avenue runs the New North End. Shelburne Road and Williston Road carry the strip malls and the big-box lots in South Burlington. The ferry crossings up and down the lake carry cars to New York. A carrier does not use them.'),
  P('The carriers come off 89 at exit 14 and exit 13. They meet at the mall lots on Williston Road and the big-box lots on Shelburne Road. The lots at the fairgrounds in Essex Junction work outside the fair. So do the park-and-ride at exit 14 and the lots along the Beltline. The airport in South Burlington is five minutes from exit 14 for a fly-and-ship.'),
  P('Our office is on North Street in the Old North End, a few blocks up from the waterfront.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the Waterfront, the Hill Section, the Old North End, the New North End, the South End, Winooski, South Burlington, Colchester, Essex, Williston, and Shelburne',
 prose(
  L('Burlington is a dense core on a hill, two North Ends, and an arts district on the flats. The suburbs run across the river and down the lake. The truck meets the hill on a main road and the flats at the curb.'),
  P('Downtown runs from the waterfront up to the campus, brick blocks and one-way streets around the pedestrian mall. The driver meets you at a garage entrance on Cherry or at the waterfront lots. The Hill Section above the campus is big Victorian houses on steep streets. A trailer does not stop on the grade. The handoff moves to Main Street or the campus lots. The campus blocks and the student streets off Pearl are tight and full. The handoff happens at the lots on Colchester Avenue.'),
  P('The Old North End is the oldest grid, small houses on narrow streets with cars on both curbs. The handoff happens on North Street or North Avenue. The New North End is postwar ranches on wide streets out to the lake. The curb works nearly everywhere. The South End along Pine Street is warehouses turned studios and breweries. The handoff happens on Pine or at the big lots there.'),
  P('Winooski across the river is a mill town rebuilt around a roundabout. The handoff happens at the lots off Main Street. South Burlington is subdivisions and strip malls, and the curb works. Colchester, Essex, Williston, and Shelburne are cul-de-sacs and village centers. The truck comes to the house on most of them. Essex Junction around the chip plant is the same.'),
  P('Winooski, South Burlington, Colchester, Essex, Williston, and Shelburne ship with the same trucks and price as Burlington. Montpelier and Middlebury add an hour on the truck. Stowe and the ski towns add a figure in winter.'),
 )))

ROUTES=[("Albany, NY","I-89/I-87 · ~155 mi","Same day","$200–$320"),("Manchester, NH","I-89/I-93 · ~160 mi","Same day","$220–$340"),
 ("Boston, MA","I-89/I-93 · ~215 mi","Same day","$230–$350"),("Hartford, CT","I-89/I-91 · ~240 mi","Same day","$240–$360"),
 ("Portland, ME","US-2/I-93/I-95 · ~235 mi","1 day","$250–$380"),("New York, NY","I-89/I-87 · ~300 mi","1 day","$270–$400"),
 ("Philadelphia, PA","I-87/I-287/I-95 · ~390 mi","1–2 days","$340–$490"),("Washington, DC","I-87/I-95 · ~530 mi","1–2 days","$450–$650"),
 ("Chicago, IL","I-87/I-90 · ~900 mi","2–3 days","$650–$900"),("Orlando, FL","I-87/I-95 · ~1,450 mi","3 days","$900–$1,250")]
BODY.append(rate_table('Lanes &amp; Costs','Burlington Car Shipping Lanes and Estimated Costs',
 'The lanes Chittenden County cars travel most, with an open-trailer estimate for each. Use the form above for your own.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Burlington for a running sedan, open trailer. Add 10 to 25 percent for an SUV or a pickup, and more for an enclosed trailer. The week you choose and the carriers coming up 89 that week fix the real figure.',
 prose(
  P('Burlington prices above Boston on every lane. The trucks come up 89 to the end of the line and go back half empty. The Boston lane rides 89 and 93 and fills twice a week. The New York lane rides 87 down the other side of the lake. The Florida lane fills each October with the snowbirds, and the price rises with them. The Chicago lane rides 87 and 90 and fills once a week.'),
  P('A late August move-in at the university or a foliage week in October means a busy week. For what size, condition, and timing do to a figure, read the <a href="car-shipping-cost.html">cost guide</a>.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The University, the Medical Center, the Chip Plant, the Guard Wing, the Two Colleges, the Ski Towns, and the Snowbirds',
 prose(
  L('Burlington relocates students, residents, engineers, airmen, professors, and retirees. The university moves the most.'),
  P('The university on the hill takes thirteen thousand students, most of them from out of state. The cars arrive in late August. A parent books, and an adult signs at the lots on Colchester Avenue. The cars go home in May. The college downtown and the college in Colchester move their students the same weeks. The medical center on the hill is the largest employer in the state. It brings residents each June and traveling nurses all winter.'),
  P('The chip plant in Essex Junction employs thousands of engineers and technicians. It relocates them from Texas, New York, and overseas on start dates. The handoff happens at the fairgrounds lots or on Route 15. The Guard’s fighter wing at the airport rotates airmen on orders. The handoff happens at the airport lots. Ship Guy is a private broker and has nothing to do with the Guard. The <a href="military-car-shipping.html">military</a> page covers how orders set the dates.'),
  P('The ski towns east of the city hire seasonal workers each November. The cars come up 89 with them. The lake draws second-home owners from Boston and New York each May. The retirees go to Florida in October and come back in April. That lane is the busiest long one out of Vermont. The <a href="state-to-state-car-shipping.html">state-to-state</a> page has the paperwork a state line adds.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Move-In Week, the Jazz Festival, the Marathon, the Fair, the Foliage, Mud Season, the Snow, the Ice Storm, and the Floods',
 prose(
  L('Burlington runs on a campus calendar and a lake calendar. The weather problem is a six-month winter and a spring that turns the dirt roads to mud.'),
  P('Move-in week in late August fills the hill and the student streets. The city closes blocks for it. The jazz festival fills Church Street and the waterfront for ten days in June. The marathon closes the Beltline, North Avenue, and the waterfront on the Sunday of Memorial Day weekend. The fair fills Essex Junction for ten days around Labor Day. The foliage brings the buses in the first two weeks of October. The carriers run slow behind them. A late August date wants three weeks of notice.'),
  P('The snow comes in November and stays until April. The city plows the hill first and the North Ends last. A trailer waits a day after a big storm. The January 1998 ice storm coated the north of the state and took the power for a week. The cold snaps hold the city below zero for days. A carrier does not load at twenty below. Mud season in March and April closes the dirt roads in the hill towns to anything heavy. The handoff moves to the paved road.'),
  P('The July 2023 floods closed 89 in the valley and cut Montpelier off for days. The lake rose to a record in May 2011 and flooded the waterfront and the bike path. The Halloween windstorm in 2019 dropped trees across the county and took the power for two days. A flood watch on the Winooski moves the handoff off the river roads. We call before the day moves.'),
  P('Summer is short and mild, and the lake draws the whole city out. A thunderstorm holds the truck at the lot for an hour.'),
 )+chips(["Downtown","The Waterfront","Church Street","The Hill Section","The Old North End","The New North End","The South End","Pine Street","Lakeside","Winooski","South Burlington","Colchester","Essex","Essex Junction","Williston","Shelburne","Charlotte","Hinesburg","Jericho","Milton","Grand Isle","Montpelier","Stowe"])
 +NOTE('Serving Burlington, Chittenden County, and the Champlain Valley, New North End curb or Jericho dirt road. Tell us the street and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Burlington?',
 prose(
  L('Open trailers do most of the valley’s work, and the table above assumes one.'),
  P('Enclosed keeps the salt, the sand, and the mud off the paint. The collectors in the Hill Section book it. So do the second-home owners moving a car worth more than the rest of the trip. When an open truck is all that runs 89 ahead of a snowstorm, we say so. You choose.'),
  P('A commuter car or a student’s hatchback rides open and arrives fine. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain where the two part ways.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A figure, then a lot off exit 14, then a signature when the car lands. Move-in or the start date decides the week.'),
  P('Say yes, and the car is placed with a carrier already coming up 89 that week. The lot and the window follow the same day. The driver takes photos at pickup and fills in the condition on the Bill of Lading. You initial it, and that record settles delivery.'),
 )+ULI([
  "Nothing of yours left in the cabin or the hatch",
  "Fuel at a quarter tank, no more",
  "Photos of each side and the odometer, taken before the truck comes",
  "A key that works and a line about any known faults",
  "Add-on alarms disarmed",
  "On the hill, downtown, or on a dirt road in mud season, expect a lot off 89",
 ])+prose(P('The order of events is on <a href="how-it-works.html">how it works</a>, and the morning-of list is on <a href="car-shipping-preparation.html">preparation</a>.'))))

BODY.append(sec('Why Ship Guy','Why Burlington Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already come up 89 each week. We know which weeks the hill closes and when the dirt roads thaw.'),
  P('Our FMCSA license and our $75,000 bond are posted on the federal register for anyone to check. The office is on North Street in the Old North End.'),
  P('One coordinator takes your move from the quote all the way to the delivery call. Open, enclosed, and expedited are explained on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Burlington','12-22 North St #325','Burlington, VT 05401','+18023027127','(802) 302-7127','ET',
 '12-22+North+St+%23325,+Burlington,+VT+05401','Visit Us','Find Ship Guy in Burlington',
 'Our office is on North Street in the Old North End, a few blocks up from the waterfront.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3513.635530649302!2d-73.2217696!3d44.484635!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4cca7b1bba1d9467%3A0x586e2e22fab9b65b!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793631597118!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Burlington to Boston or Florida?","Boston runs two hundred thirty to three hundred fifty dollars for a sedan. That is about two hundred fifteen miles down 89 and 93. Orlando runs nine hundred to twelve hundred fifty, about fourteen hundred fifty miles. Albany is the lowest lane on the table, about one hundred fifty-five miles. An SUV or a pickup costs 10 to 25 percent more."),
 ("Why does a Burlington pickup take 2 to 5 days instead of 1 to 3?","Because the city is the end of the line. The 89 carriers come up from Boston two or three times a week and go back half empty. A car waits for the next one with room. A snowstorm, a foliage week, or mud season stretches the window further. We say so when it does."),
 ("Can you deliver on a University of Vermont move-in date?","Yes. Cars arrive in late August and leave in May. A parent books, and someone over eighteen signs at the lot. The hill and the student streets are closed that week. The meeting point is the lots on Colchester Avenue. The window is built around the date."),
 ("Can the carrier come to my street in the Hill Section or the Old North End?","No. The Hill Section is steep, and a loaded trailer does not stop on the grade. The Old North End is narrow streets with cars on both curbs. The driver meets you on Main Street, North Avenue, or at the lots off exit 14. The New North End, South Burlington, Essex, Williston, and Shelburne usually allow the curb."),
 ("What happens if a snowstorm or the cold hits on my pickup day?","The truck waits a day for the plows and the hill. A carrier does not load a car at twenty below, because the straps stiffen and the hydraulics slow. Our call goes out when the forecast turns, and the pickup moves to the first plowed morning. The figure stays."),
 ("Can you ship a car during mud season?","Yes, from the paved road. The dirt roads in the hill towns close to anything heavy in March and April. The handoff moves to the nearest paved road or the lots off 89. Burlington itself is paved, and the city streets work all spring."),
 ("Do you ship cars for the medical center, the chip plant, or the Guard?","Yes, in every season. The medical center brings residents each June and traveling nurses all winter. The chip plant in Essex Junction relocates engineers on start dates. The Guard’s fighter wing rotates airmen on orders. The handoff happens at the lots nearest the site. When the employer reimburses you, we supply the paperwork it wants."),
 ("Can you ship a car to or from Winooski, Essex, Montpelier, or Stowe?","Yes. Winooski, South Burlington, Colchester, Essex, Williston, and Shelburne ride the same carriers and price the same as Burlington. Montpelier and Middlebury add an hour on the truck. Stowe and the ski towns add a figure in winter, when the carriers stay on 89."),
 ("Can you ship a car that does not run from Burlington?","Yes. The truck brings a winch, and the figure includes the extra loading time. The mall lots on Williston Road and the big-box lots on Shelburne Road are flat. Let us know whether it rolls, steers, and brakes."),
 ("What do you need for a Burlington car shipping quote?","Where it starts and where it ends, with the neighborhood or the town. The car, and whether it runs. Open or enclosed, and the week around the move-in or the start date. From those, a Burlington figure comes back the same day."),
]
BODY.append(faq_section(FAQ,'Burlington FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Burlington?','Two minutes on the form above gets your lane priced for Burlington. Name the street and the week, and a carrier already coming up 89 takes the car.','+18023027127','(802) 302-7127','Get your free Burlington quote'))

build({
 'slug':'auto-transport-burlington-vermont',
 'title':'Car Shipping in Burlington, VT — Auto Transport | Ship Guy',
 'meta':'Car shipping in Burlington, VT, on Lake Champlain at the end of Interstate 89. University of Vermont move-in dates, medical center and chip-plant hires, the Guard wing at the airport, main-road handoffs for the hill and the Old North End, curbside pickups in the New North End, South Burlington, Essex, and Shelburne, the snow, mud season, and the floods. Local office on North Street. Free quote.',
 'h1':'Car Shipping in<br>Burlington, <span class="accent">Vermont</span>',
 'lede':'Open, enclosed, and expedited auto transport across Burlington and the Champlain Valley, planned around Interstate 89, the campus dates, the start dates, the foliage, the snow, and mud season.',
 'tel':'+18023027127','disp':'(802) 302-7127','brand':'Burlington','keyword':'car shipping in burlington',
 'localterms':['burlington','lake champlain','interstate 89','189','spur','route 7','route 2','beltline','main street','church street','pearl street','college street','north avenue','north street','cherry','colchester avenue','shelburne road','williston road','pine street','route 15','exit 13','exit 14','exit 15','exits 16','winooski valley','causeways','islands','plattsburgh','ferry','pedestrian mall','city hall','grade','hill','waterfront','bike path','downtown','hill section','old north end','new north end','south end','lakeside','winooski','roundabout','mill town','south burlington','colchester','essex','essex junction','williston','shelburne','charlotte','hinesburg','jericho','milton','grand isle','montpelier','middlebury','rutland','stowe','ski towns','border','canadian','university','thirteen thousand','students','out of state','colleges','medical center','largest employer','residents','traveling nurses','chip plant','engineers','technicians','guard','fighter wing','airmen','orders','airport','seasonal workers','second-home','retirees','snowbirds','florida','move-in','jazz festival','marathon','memorial day','fair','fairgrounds','labor day','foliage','buses','mud season','dirt roads','paved','snow','plows','january 1998','ice storm','cold snaps','twenty below','july 2023','floods','may 2011','record','halloween','2019','windstorm','winooski','salt','sand','mud','albany','manchester','boston','hartford','portland','new york','philadelphia','washington','chicago','orlando','park-and-ride','victorian','studios','breweries','bill of lading','fmcsa','winch','fly-and-ship'],
}, BODY, FAQ)
