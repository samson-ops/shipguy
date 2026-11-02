import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Eugene, Oregon','Car shipping in Track Town, at the south end of the valley where 5 meets the McKenzie',
 ['Car shipping in Eugene rides Interstate 5, the Seattle-to-California road along the east edge of the city. Ship Guy is a licensed auto transport broker with an office on East 5th Avenue downtown.',
  'We book vetted carriers across Eugene and Springfield, from the Whiteaker to Thurston and the River Road farms. The carriers own the trucks. Ship Guy holds the license and the bond.',
  'Interstate 5 runs from Portland past the east side of the city to Medford and the Siskiyou. Interstate 105 spurs into downtown and Springfield. Highway 126 runs west to the coast and east up the McKenzie. Highway 58 climbs Willamette Pass, and the Beltline loops the north side.',
  'This page covers 5, 105, 126, the Beltline, downtown, the campus, the Whiteaker, the hills, and Springfield. It also covers the university, the hospital, the mills, the track meets, the ice storm, and the fires.'],
 'Eugene at a glance',
 ['Most pickups happen within 1 to 3 days. The Seattle-to-California carriers pass the city on 5 every day. A car near the interstate rides a truck already making the trip.',
  'Portland, Vancouver, and Medford are same-day runs. Seattle needs a day. Spokane, Sacramento, San Francisco, and Boise need one to two. Los Angeles needs two, and Phoenix needs three.'],
 'Tell us the neighborhood and whether the street climbs. The Whiteaker, College Hill, the campus blocks, and downtown meet the truck at a lot. River Road, Santa Clara, Bethel, Cal Young, Thurston, and Coburg usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 5, Interstate 105, Highway 126, Highway 99, Highway 58, the Beltline, Delta Highway, Franklin, and the Ferry Street Bridge',
 prose(
  L('Eugene sits where the Willamette and the McKenzie meet at the bottom of the valley. One interstate passes it, and every other road ends at a mountain or the sea.'),
  P('Interstate 5 is the Seattle-to-California road. It comes down from Portland and Salem past Coburg and passes the east side of Eugene. It leaves south for Cottage Grove and Roseburg. The Siskiyou Summit at the California line is two hundred miles down. It closes for snow and chains a few times a winter. A carrier waits in Medford until it opens. The exits that matter are Coburg Road, 105, Franklin Boulevard, and 30th Avenue.'),
  P('Interstate 105 leaves 5 at Springfield and runs into downtown Eugene over the Washington-Jefferson Bridge. Highway 126 runs west through Veneta to Florence and the coast. It runs east up the McKenzie to Blue River and the passes. Highway 99 is Franklin Boulevard past the campus and the old road north to Junction City. Highway 58 climbs Willamette Pass to Oakridge and the high desert. The Beltline loops the north side from 5 to West 11th. Delta Highway drops from the Beltline to the mall by the river. The Ferry Street Bridge ties downtown to the stadium and Coburg Road.'),
  P('The carriers come off 5 at Coburg Road or Franklin. The mall lots on Delta Highway are the usual meeting spot. The Gateway lots in Springfield and the big-box lots on West 11th work too. So do the stadium lots outside the football calendar. The community college lots on 30th work on a weekend.'),
  P('Our office is on East 5th Avenue downtown, across from the 5th Street Market.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the Whiteaker, the Campus, Fairmount, South Eugene, the Friendly Area, Cal Young, River Road, Bethel, Springfield, and the Valley Towns',
 prose(
  L('Eugene is bungalows on narrow streets near the river and hills with ivy and switchbacks to the south. The truck meets the old city at the edge.'),
  P('Downtown runs along the one-way couplets of 6th and 7th and 11th and 13th. The Park Blocks and the market sit at the center. The streets are short and the parking is angled. The driver meets you at the market garage entrance or on 7th. The Whiteaker west of downtown is bungalows, murals, and breweries on streets a trailer cannot turn in. The handoff moves to 7th or the big-box lots on West 11th.'),
  P('The campus and Fairmount east of downtown are tree-lined blocks packed with student cars most of the year. The driver meets you at the stadium lots or on Franklin. South Eugene and College Hill climb toward Spencer Butte on streets that narrow as they rise. The handoff moves to Willamette Street or Amazon Parkway. The Friendly Area and Jefferson Westside are flatter bungalows, and the curb sometimes works.'),
  P('Cal Young and Harlow north of the river are postwar grids and newer subdivisions. A trailer fits. River Road and Santa Clara to the northwest are old farm roads with wide lots. The driver reaches the house. Bethel and Danebo to the west are the same. West Eugene along West 11th is warehouses and big-box lots, the easiest handoff in the city.'),
  P('Springfield across the river is its own city with the same trucks. Gateway, Thurston, and Mohawk are wide and reachable, and Glenwood between the two downtowns is the same. Coburg, Junction City, and Creswell ship with the same carriers. So do Cottage Grove down 5 and Veneta out 126. All of them price the same as Eugene. Florence on the coast and Oakridge up the pass add an hour and a day.'),
 )))

ROUTES=[("Portland, OR","I-5 · ~110 mi","Same day","$180–$290"),("Vancouver, WA","I-5 · ~120 mi","Same day","$180–$290"),
 ("Medford, OR","I-5 · ~170 mi","Same day","$210–$320"),("Seattle, WA","I-5 · ~280 mi","1 day","$280–$410"),
 ("Spokane, WA","I-5/I-84/US-395 · ~460 mi","1–2 days","$400–$570"),("Sacramento, CA","I-5 · ~470 mi","1–2 days","$400–$570"),
 ("San Francisco, CA","I-5 · ~530 mi","1–2 days","$440–$630"),("Boise, ID","I-5/I-84 · ~540 mi","1–2 days","$420–$600"),
 ("Los Angeles, CA","I-5 · ~860 mi","2 days","$600–$860"),("Phoenix, AZ","I-5/I-10 · ~1,240 mi","3 days","$900–$1,250")]
BODY.append(rate_table('Lanes &amp; Costs','Eugene Car Shipping Lanes and Estimated Costs',
 'The lanes southern Willamette Valley cars run most, with estimated open-trailer ranges. Price your own route on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Eugene for a sedan that runs, on an open trailer. An SUV or a pickup adds about 10 to 25 percent, and enclosed adds more. The season, the Siskiyou, and the trucks free on your dates set the real quote.',
 prose(
  P('Eugene prices like Portland with a hundred miles moved from the California side to the Seattle side. The California lanes ride 5 over the Siskiyou and fill every day with students and transplants. The Seattle lane rides 5 north through Portland. The Boise and Spokane lanes ride 84 up the gorge. The Arizona lane fills each October with the valley’s retirees.'),
  P('The late September move-in and the June move-out are the busiest weeks of the year. The <a href="car-shipping-cost.html">cost guide</a> explains how size, condition, and timing shape the number.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The University, the Hospital, the Timber Companies, the Shoe and Track Business, the Community College, and the Transplants',
 prose(
  L('Eugene relocates professors, nurses, runners, mill managers, and students. The university moves the most.'),
  P('The university on Franklin is the largest employer in the city. Faculty arrive on contract dates over the summer, and the campus takes student cars in late September. It sends them home in June. A parent books it from home, and an adult meets the truck at the stadium lots to sign. The community college on 30th runs the same calendar and takes cars the same week.'),
  P('The hospital system runs the big campus in Springfield and the older one by the university. It hires traveling nurses year round and brings residents each June. The timber companies with mills in Springfield and along Highway 99 move managers on contract dates. The running shoe company born here moves designers and coaches in and out on the track calendar. The health plan in Springfield and the retailer headquartered on the west side relocate staff on offer dates. If an employer is reimbursing the move, the paperwork comes from us.'),
  P('Transplants arrive from California every month for the rain and the trails. They ship the car behind the moving truck. Retirees go south to Arizona in October and return in April. Crossing state lines is covered on the <a href="state-to-state-car-shipping.html">state-to-state</a> page. The Guard armory and the joint base in Portland send a few families down 5 on orders. Ship Guy is a private broker with no connection to either, and the <a href="military-car-shipping.html">military</a> page explains the timing.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Ducks Saturdays, the Track Meets, Move-In Week, the Country Fair, the Marathon, the Rain, the Ice Storm, the Fires, and the Siskiyou',
 prose(
  L('Eugene runs on a football calendar and a track calendar. The weather problem is ice one week a year and smoke one month a year.'),
  P('Ducks home games fill the stadium across the river on fall Saturdays. The Ferry Street Bridge, Coburg Road, and Martin Luther King Boulevard jam for hours before and after. A handoff near the stadium moves to a weekday. The track meets at Hayward Field fill the campus blocks in late May and June. The national championships and the trials fill every hotel in the valley. Move-in week in late September fills Fairmount and the campus blocks.'),
  P('The Country Fair fills Veneta for the second weekend of July, and Highway 126 west crawls both directions. The marathon closes downtown and the river paths on a Sunday in late April. The county fair fills the fairgrounds on West 13th for a week in July. The Saturday Market closes the Park Blocks every Saturday from April to November. A handoff near any of them moves to the next morning.'),
  P('Rain falls from October to May and changes nothing. The January 2024 ice storm changed everything for a week. Half an inch of ice brought down firs and oaks across the city. The power stayed off for days. The carriers waited in Salem until the roads were clear. The February 2019 storm dropped a foot of snow and did the same for three days. A winter pickup can lose a day, and you hear it from us before the driver does.'),
  P('The fires come in September. In 2020 the Holiday Farm fire burned down the McKenzie and closed Highway 126 east for weeks. The smoke over the city was the worst measured anywhere in the world for two days. A pickup in the smoke still happens, and a pickup in an evacuation zone waits. The June 2021 heat reached one hundred eleven degrees, and the carriers loaded at dawn. The Siskiyou closes for chains a few times a winter. The California car waits a day in Medford.'),
 )+chips(["Downtown","5th Street Market","Park Blocks","Whiteaker","Jefferson Westside","Campus","Fairmount","Hendricks Park","South Eugene","College Hill","Amazon","Friendly Area","Churchill","Cal Young","Harlow","Ferry Street Bridge","River Road","Santa Clara","Bethel","Danebo","West Eugene","West 11th","Springfield","Gateway","Thurston","Mohawk","Glenwood","Coburg","Junction City","Creswell","Cottage Grove","Veneta","Oakridge","Florence"])
 +NOTE('Serving Eugene, Springfield, and the whole south valley, Whiteaker bungalow or Thurston cul-de-sac. Tell us the neighborhood and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Eugene?',
 prose(
  L('Open trailers carry most of the valley, and the table above is priced for one.'),
  P('An enclosed trailer keeps off the grime of seven wet months and the cinders on the Siskiyou. The collectors in the south hills book one. So do the coaches bringing a new car in on the track calendar. A car headed over the pass in January often rides enclosed too.'),
  P('A commuter car or a student car has no need of a roof. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages put the two side by side.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A number, a lot at the mall or the stadium, and a signature at delivery. The term date or the meet picks the week.'),
  P('Approve the price, and a carrier already running 5 past the city takes the job. The lot and the window are confirmed the same afternoon. At pickup the driver walks the car with you and marks every blemish on the Bill of Lading. You sign it, and the delivery inspection is checked against those marks.'),
 )+ULI([
  "Personal items out of the car, including the trunk",
  "Fuel at about a quarter tank",
  "Photos of each side and the odometer before the driver arrives",
  "One working key, plus a note about anything that sticks or leaks",
  "Aftermarket alarm switched off",
  "In the Whiteaker, on College Hill, or near the campus, plan on a lot",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> page has the order of events, and the <a href="car-shipping-preparation.html">preparation</a> page has the checklist.'))))

BODY.append(sec('Why Ship Guy','Why Eugene Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already run 5 past the city every day. We know when the Siskiyou is chained up.'),
  P('Our FMCSA license and our $75,000 bond are on the federal register, open to anyone. The office is on East 5th Avenue downtown.'),
  P('One coordinator owns the move from the quote to the delivery photo. The <a href="services.html">services</a> page sets open, enclosed, and expedited side by side.'),
 )))

BODY.append(office('Eugene','207 E 5th Ave #922','Eugene, OR 97401','+15412369511','(541) 236-9511','PT',
 '207+E+5th+Ave+%23922,+Eugene,+OR+97401','Visit Us','Find Ship Guy in Eugene',
 'Our office is on East 5th Avenue downtown, across from the 5th Street Market.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4379.507559292856!2d-123.08926269999999!3d44.05441999999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x54c11f5199dac26d%3A0xbe084d720a847bfa!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793300465622!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Eugene to California or Seattle?","Los Angeles runs six hundred to eight hundred sixty dollars for a sedan. That is about eight hundred sixty miles down 5. San Francisco runs four hundred forty to six hundred thirty, about five hundred thirty miles. Seattle runs two hundred eighty to four hundred ten. Portland is two hours away and costs the least. Add about 10 to 25 percent for an SUV or a pickup."),
 ("Can the carrier come to my street in the Whiteaker or on College Hill?","No. The Whiteaker is bungalows on streets a trailer cannot turn in, and College Hill narrows as it climbs. The driver meets you on 7th, on Willamette Street, or at the big-box lots on West 11th. River Road, Santa Clara, Bethel, Cal Young, and Thurston usually allow the curb."),
 ("Can you deliver on the University of Oregon move-in date?","Yes. The campus takes cars in late September and sends them home in June. The community college runs the same calendar. The parent books from home, and an adult signs at the stadium lots. Fairmount and the campus blocks are closed to a trailer that week. The date sets the window."),
 ("Do you ship cars for the hospital and the timber companies?","Yes, every month. The hospital system brings residents each June and hires traveling nurses year round. The mills move managers on contract dates, and the shoe company moves designers on the track calendar. If an employer is reimbursing the move, the paperwork comes from us."),
 ("Does Ducks football or a track meet affect my pickup?","Yes, near the stadium and the campus. Home Saturdays jam the Ferry Street Bridge and Coburg Road for hours. The meets at Hayward Field fill the campus blocks in late May and June. A handoff in that corner of the city moves to a weekday. The rest of Eugene barely notices."),
 ("Can you ship a car to or from Springfield, Corvallis, or Florence?","Yes. Springfield prices the same as Eugene and rides the same trucks off 5 and 105. Corvallis is forty minutes up 99 and prices the same. Florence on the coast adds an hour over the Coast Range and a day of waiting. The handoff there is in town."),
 ("What happens if the Siskiyou closes on my pickup day?","A California car waits a day in Medford. The summit closes for chains and snow a few times a winter, usually for hours. The carrier crosses when the state lifts the restriction. A car headed north or east is not affected. You hear it from us before the driver does."),
 ("What happens if an ice storm or the smoke hits on my pickup day?","Ice stops everything for a day or two. The January 2024 storm brought down firs across the city. The carriers waited in Salem until the streets were clear. Smoke stops nothing but the loading hour, unless the address is in an evacuation zone. Then the pickup waits for the all-clear."),
 ("Can you ship a car that does not run from Eugene?","Yes. A winch truck is booked, and the loading time is in the price from the start. The mall lots on Delta Highway or the West 11th lots give the driver level ground. Say whether it rolls, steers, and brakes."),
 ("What do you need for an Eugene car shipping quote?","Pickup and delivery, with the neighborhood or the valley town. The year, make, and model. Whether it runs. Open or enclosed. The week around the term date or the move. Five answers, and an Eugene number is back the same day."),
]
BODY.append(faq_section(FAQ,'Eugene FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Eugene?','The form above takes two minutes and comes back with an Eugene number. Name the neighborhood and the week, and a carrier already on 5 takes it.','+15412369511','(541) 236-9511','Get your free Eugene quote'))

build({
 'slug':'auto-transport-eugene-oregon',
 'title':'Car Shipping in Eugene, OR — Auto Transport | Ship Guy',
 'meta':'Car shipping in Eugene, OR, at the south end of the valley on Interstate 5. University move-in and the track calendar, hospital and timber relocations, lot handoffs for the Whiteaker, College Hill, and the campus, curbside pickups in River Road, Santa Clara, Bethel, Cal Young, and Thurston, the ice storm, the fires, and the Siskiyou. Local office on East 5th Avenue downtown. Free quote.',
 'h1':'Car Shipping in<br>Eugene, <span class="accent">Oregon</span>',
 'lede':'Open, enclosed, and expedited auto transport across Eugene and Springfield, planned around 5, the campus calendar, the track meets, the rain, and the one week a year the ice shuts the valley.',
 'tel':'+15412369511','disp':'(541) 236-9511','brand':'Eugene','keyword':'car shipping in eugene',
 'localterms':['eugene','track town','valley','interstate 5','mckenzie','seattle','california','east 5th avenue','downtown','springfield','whiteaker','thurston','river road','portland','salem','roseburg','medford','siskiyou','interstate 105','highway 126','coast','highway 58','willamette pass','beltline','campus','hills','university','hospital','timber','track meets','ice storm','fires','vancouver','spokane','sacramento','san francisco','boise','los angeles','phoenix','college hill','santa clara','bethel','cal young','coburg','willamette','cottage grove','chains','coburg road','franklin','30th avenue','washington-jefferson bridge','veneta','florence','blue river','highway 99','junction city','oakridge','high desert','west 11th','delta highway','mall','ferry street bridge','stadium','gateway','big-box','community college','5th street market','bungalows','ivy','switchbacks','couplets','park blocks','angled','garage','murals','breweries','fairmount','student cars','spencer butte','willamette street','amazon parkway','friendly area','jefferson westside','harlow','danebo','warehouses','mohawk','glenwood','creswell','transplants','retirees','arizona','contract dates','late september','traveling nurses','residents','mills','running shoe','designers','coaches','health plan','armory','joint base','ducks','martin luther king boulevard','hayward field','championships','trials','country fair','marathon','county fair','fairgrounds','saturday market','january 2024','half an inch','firs','oaks','february 2019','holiday farm','2020','smoke','evacuation','june 2021','one hundred eleven','grime','cinders','bill of lading','fmcsa','hendricks park','churchill','corvallis','coast range','winch'],
}, BODY, FAQ)
