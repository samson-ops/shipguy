import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("3–6 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Fargo, North Dakota','Car shipping on the Red River, where 29 and 94 cross on the flattest ground in the country',
 ['Car shipping in Fargo rides Interstate 94 and Interstate 29, which cross at the west edge of town. Ship Guy is a licensed auto transport broker with an office on 1st Avenue North near downtown.',
  'We book vetted carriers across Fargo, West Fargo, and Moorhead, from Hawthorne to Osgood and Eagle Run. The carriers own the trucks. Ship Guy holds the license and the bond.',
  'Interstate 94 runs from Minneapolis through the south side of the city to Bismarck and Montana. Interstate 29 runs the Red River valley from Sioux Falls through the west side to Canada. US 10 is Main Avenue, and it crosses the river into Moorhead. US 81 is University Drive.',
  'This page covers 94, 29, the river, 13th Avenue, downtown, the old neighborhoods, and the new south side. It also covers the medical centers, the software campus, the plants, the campuses, the blizzards, and the floods.'],
 'Fargo at a glance',
 ['Most pickups happen within 3 to 6 days. North Dakota is a pass-through market, and a carrier adds a Fargo stop when the load lines up. A week of dates gets the next truck through.',
  'Bismarck, Minneapolis, and Sioux Falls are a day on the truck. Omaha takes one to two. Milwaukee, Kansas City, and Chicago take two. Denver takes two to three, and Dallas and Phoenix take four.'],
 'Tell us the neighborhood and whether the street is a snow route. Downtown, Roosevelt, Horace Mann, and Hawthorne meet the truck at a lot. Osgood, Brandt Crossing, West Fargo, Horace, and Moorhead usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 94, Interstate 29, Main Avenue, 13th Avenue, 32nd Avenue, 45th Street, University Drive, and the Bridges',
 prose(
  L('Fargo is a grid laid on a lake bed. A carrier sees the whole city from the 29 and 94 interchange.'),
  P('Interstate 94 is the Minneapolis-to-Montana road. It enters from Moorhead over the river and runs along the south side of the old city. It crosses 29 by the mall and leaves west past West Fargo for Bismarck. Interstate 29 is the Red River road. It comes up from Sioux Falls, crosses 94, and runs the west edge of town past the airport. It leaves north for Grand Forks and Winnipeg. The domestic leg of a Winnipeg move ends at the border.'),
  P('Main Avenue is US 10, the old road, and it carries the traffic over the river to Moorhead. 13th Avenue South is the commercial strip, from the mall at 29 east to the river. 32nd Avenue South carries the medical centers and the newer retail. 45th Street runs the west side from the airport to the south subdivisions. Veterans Boulevard does the same in West Fargo. University Drive is US 81, and it runs from the campus south through the old city.'),
  P('The carriers come off 94 at 45th Street or University Drive and off 29 at 13th Avenue. The mall lots at 13th and 29 are the usual meeting spot. The Fargodome lots work outside the football calendar. The big-box lots on 45th and 13th work every day. The airport lots work for a fly-and-ship.'),
  P('Our office is on 1st Avenue North, a mile west of Broadway and minutes from 29 and 94.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, Roosevelt, Horace Mann, Hawthorne, Island Park, the South Side, West Fargo, Horace, and Moorhead',
 prose(
  L('Fargo is an old railroad town on the river, with a new city growing south and west. The truck meets the old blocks at the edge.'),
  P('Downtown runs along Broadway north from Main Avenue, brick storefronts, the theater, and the lofts above them. The streets are one-way and the curb is metered. The driver meets you at the lots by the Civic Center or on Main Avenue. Roosevelt and Horace Mann north of downtown are the campus blocks. Old houses line narrow streets packed with student cars. The handoff moves to the Fargodome lots or University Drive.'),
  P('Hawthorne south of downtown is the old money, tree-lined streets along 8th down to Island Park. The elms meet over the road, and a trailer cannot clear them. The driver meets you on Main Avenue or at the park lots. Jefferson and Clara Barton south of there are the same bungalows on the same narrow streets. The handoff moves to 13th Avenue.'),
  P('The south side is where the city grew. Lewis and Clark, Southpointe, and the blocks along 32nd Avenue are wide postwar grids where the curb works. Osgood, Brandt Crossing, Urban Plains, Deer Creek, and Rose Creek south of 52nd Avenue are the newest. The streets outpace the carrier maps, so send the full address. The river blocks down there sit behind the levees and flood in a wet April.'),
  P('West Fargo past 45th Street is its own city with the same answer. Eagle Run, the Wilds, and the Shadow Wood cul-de-sacs all take the curb. Horace and Harwood ship with the same trucks, and so do Casselton and Mapleton out 94. Moorhead and Dilworth across the river in Minnesota ride the same carriers over the Main Avenue bridge. All of them price the same as Fargo.'),
 )))

ROUTES=[("Bismarck, ND","I-94 · ~195 mi","1 day","$220–$340"),("Minneapolis, MN","I-94 · ~240 mi","1 day","$250–$380"),
 ("Sioux Falls, SD","I-29 · ~245 mi","1 day","$250–$380"),("Omaha, NE","I-29 · ~420 mi","1–2 days","$400–$580"),
 ("Milwaukee, WI","I-94 · ~560 mi","2 days","$430–$620"),("Kansas City, MO","I-29 · ~600 mi","2 days","$450–$650"),
 ("Chicago, IL","I-94 · ~640 mi","2 days","$470–$680"),("Denver, CO","I-29/I-80 · ~880 mi","2–3 days","$600–$860"),
 ("Dallas, TX","I-29/I-35 · ~1,150 mi","3–4 days","$780–$1,100"),("Phoenix, AZ","I-29/I-80/I-25 · ~1,600 mi","4 days","$950–$1,350")]
BODY.append(rate_table('Lanes &amp; Costs','Fargo Car Shipping Lanes and Estimated Costs',
 'The lanes Red River valley cars run most, with estimated open-trailer ranges. Price your own route on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Fargo for a running sedan on an open trailer. An SUV or a pickup adds about 10 to 25 percent, and enclosed adds more. On a pass-through corridor the date range and the trucks crossing that week decide the real figure.',
 prose(
  P('Fargo prices like a stop on the Minneapolis-to-Montana road, because that is what it is. The Minneapolis lane rides 94 the whole way and fills every week. The Omaha and Kansas City lanes ride 29 straight south. The Chicago lane rides 94 through the Twin Cities and Madison. The Arizona lane fills each October with the valley’s snowbirds, and the price follows.'),
  P('A move-in week in August or a report date at the base lands in the busiest weeks. The <a href="car-shipping-cost.html">cost guide</a> walks through size, condition, and the date range.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Medical Centers, the Software Campus, the Equipment Plants, the Campuses, the Guard, and the Snowbirds',
 prose(
  L('Fargo relocates nurses, engineers, programmers, students, and airmen. The medical centers and the software campus move the most.'),
  P('The health system headquartered on Broadway runs the downtown hospital and the big campus on the south side. The second system on 32nd Avenue competes with it. Between them they hire traveling nurses year round and bring residents each June. Faculty for the nursing and pharmacy programs arrive on contract dates. Employer paying for the move? The receipts come from us.'),
  P('The software campus on the southwest side is one of the largest the company runs. It moves programmers in on start dates all year. The equipment maker in West Fargo and the tractor plant up north move engineers on project dates. The sporting goods retailer, the insurer, and the electrical distributor headquartered here do the same. The second car usually rides a trailer.'),
  P('The state university takes cars each August and sends them home in May. The two campuses across the river in Moorhead run the same calendar. The parent makes the booking, and an adult signs at the lot. Campus streets are full that week, and the truck meets you at the Fargodome lots.'),
  P('The Guard wing at the airport rotates airmen on orders. The Air Force base in Grand Forks sends families south the same way. Ship Guy is a private broker with no connection to either. The timing around orders is explained on the <a href="military-car-shipping.html">military</a> page. Retirees leave for Arizona each October and come back in April. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the paperwork.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Bison Saturdays, Move-In Week, the Street Fair, the Marathon, the Blizzards, the Gates, and the River',
 prose(
  L('Fargo runs on a football calendar and a river calendar. The blizzards decide when a truck can move at all.'),
  P('Bison home games fill the Fargodome on fall Saturdays. The playoff games fill it again in December and January. University Drive, 19th Avenue, and the campus blocks jam for hours. A handoff near the dome moves to a weekday. Move-in week in late August fills Roosevelt and Horace Mann. The street fair closes Broadway for three days in July. The valley fair fills West Fargo the same month. The marathon closes the Hawthorne and Island Park routes on a Saturday in May.'),
  P('Winter brings fifty inches of snow and wind chills of forty below. A blizzard on the open prairie closes 94 and 29 for a day at a time. The state drops the gates at the city limits. No carrier moves until the gates lift. A snow emergency puts the plows on the snow routes first. A car on the wrong side gets towed. We tell you which side to park on. A winter pickup can lose a day or two, and you hear it from us first.'),
  P('A car arriving from a warm state needs winter oil and a block heater before the first freeze. An electric car should arrive at half charge, because the cold takes the rest. The driver meets you in a plowed lot rather than a drifted street.'),
  P('The Red River floods in a wet April. In 2009 it crested at forty feet, the highest ever recorded. The city filled sandbags in the dome for a week. In 1997 and 2011 it came close. The diversion channel under construction west of the metro is built to end that. Until it opens, a pickup on the river blocks moves up to 13th Avenue until the water drops. Summer brings thunderstorms and the odd tornado warning, which shift the loading hour and nothing more.'),
 )+chips(["Downtown","Broadway","Civic Center","Roosevelt","Horace Mann","North Fargo","Hawthorne","Island Park","Jefferson","Clara Barton","Lewis and Clark","Southpointe","32nd Avenue","Osgood","Brandt Crossing","Urban Plains","Deer Creek","Rose Creek","West Acres","West Fargo","Eagle Run","The Wilds","Shadow Wood","Horace","Harwood","Casselton","Mapleton","Kindred","Moorhead","Dilworth"])
 +NOTE('Serving Fargo, West Fargo, and Moorhead, Hawthorne block or Osgood cul-de-sac. Tell us the neighborhood and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Fargo?',
 prose(
  L('Almost every car in the valley rides open, and the lane table above assumes it.'),
  P('An enclosed trailer keeps off six months of road salt, brine, and gravel. The collectors in Hawthorne and the executives relocating a new car to the software campus book one. A car leaving for Arizona ahead of the first blizzard often rides enclosed too.'),
  P('A commuter car or a student car rides open and arrives fine. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain the difference.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A number, a lot at the mall or the dome, and a signature at delivery. The date range decides which truck.'),
  P('Approve the price, and we watch for a carrier crossing on 94 or 29 that week. The lot and the window are confirmed the moment one commits. At pickup the driver walks the car with you and lists each mark on the Bill of Lading. You sign it, and the delivery inspection is held to it.'),
 )+ULI([
  "Belongings out of the cabin and the trunk",
  "Gas gauge at a quarter",
  "Photos of each side and the odometer, taken the morning of pickup",
  "A key that works, plus a word about anything that sticks",
  "Any add-on alarm switched off",
  "Downtown, in Roosevelt, or in Hawthorne, plan on a lot",
 ])+prose(P('The order of events is on the <a href="how-it-works.html">how it works</a> page. The checklist is on the <a href="car-shipping-preparation.html">preparation</a> page.'))))

BODY.append(sec('Why Ship Guy','Why Fargo Drivers Choose Ship Guy',
 prose(
  L('We know which carriers cross on 94 and 29 each week and when the gates will drop.'),
  P('Our FMCSA license and our $75,000 bond sit on the federal register for anyone to read. The office is on 1st Avenue North.'),
  P('The same coordinator answers from the first call until the delivery photo arrives. The <a href="services.html">services</a> page compares open, enclosed, and expedited.'),
 )))

BODY.append(office('Fargo','1630 1st Ave N #445','Fargo, ND 58102','+17013808189','(701) 380-8189','CT',
 '1630+1st+Ave+N+%23445,+Fargo,+ND+58102','Visit Us','Find Ship Guy in Fargo',
 'Our office is on 1st Avenue North, a mile west of Broadway and minutes from 29 and 94.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4165.538146031568!2d-96.8073766!3d46.876971999999995!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x52c8cbd8c6b17d1b%3A0x3b03106c42da2dc6!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793293368974!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Fargo to Minneapolis or Arizona?","Minneapolis runs two hundred fifty to three hundred eighty dollars for a sedan. That is about two hundred forty miles down 94. Phoenix runs nine hundred fifty to thirteen hundred fifty, about sixteen hundred miles. Bismarck is a short hop west and the lowest lane on the table. SUVs and pickups run 10 to 25 percent higher."),
 ("Why does a Fargo pickup take 3 to 6 days?","Because North Dakota is a pass-through market. The carriers cross on 94 between Minneapolis and Montana and on 29 between Winnipeg and Kansas City. One adds a Fargo stop when the load lines up. Give us a week of dates and we catch the next truck through. A single fixed date can mean waiting for one."),
 ("Can the carrier come to my street in Hawthorne or Roosevelt?","No. Hawthorne is elms over narrow streets, and Roosevelt is packed with student cars. The driver meets you on Main Avenue, at the park lots, or at the Fargodome. Osgood, Brandt Crossing, West Fargo, Horace, and Moorhead usually allow the curb."),
 ("Do you ship cars for the medical centers and the software campus?","Yes, every week. The two health systems bring residents each June and hire traveling nurses year round. The software campus moves programmers in on start dates, and the equipment plants move engineers on project dates. The second car usually rides a trailer. When an employer reimburses, we produce the receipts."),
 ("Can you deliver on the NDSU move-in date?","Yes. The campus takes cars in late August and sends them home in May. The Moorhead colleges run the same calendar. The parent makes the booking, and an adult signs at the lot. Campus streets are full that week, so the Fargodome lots are the meeting point. Give us a range around the date."),
 ("Can you ship a car to or from West Fargo, Moorhead, or Grand Forks?","Yes. West Fargo and Moorhead price the same as Fargo and ride the same trucks. Grand Forks is eighty miles up 29 and prices a shade higher. The handoff there is in town, and the base families meet the truck outside the gate. Send the full address for a new subdivision."),
 ("What happens if a blizzard closes 94 or 29 on my pickup day?","Nothing moves until the gates lift. The state closes the interstates at the city limits, and a carrier waits in Minneapolis or Bismarck. A closure usually lasts a day, and the truck arrives a day or two late. We tell you before the driver does. Park on the plowed side and leave the block heater plugged in."),
 ("Does Bison football affect my pickup?","Yes, near the dome. Home Saturdays and the playoff games in December and January jam University Drive and 19th Avenue for hours. A handoff in that corner of the city moves to a weekday. The rest of Fargo barely notices."),
 ("Can you ship a car that does not run from Fargo?","Yes. The carrier brings a winch, and the loading time is in the quote from day one. On a pass-through road that narrows which trucks can stop. The mall lots at 13th and 29 give the driver level ground. Let us know whether it rolls, steers, and brakes."),
 ("What do you need for a Fargo car shipping quote?","Pickup and delivery, with the neighborhood or the town. The year, make, and model. Whether it runs. Open or enclosed. The widest date range you can give. Five answers, and a Fargo number is back before the day ends."),
]
BODY.append(faq_section(FAQ,'Fargo FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Fargo?','Two minutes on the form above, and a Fargo number is on its way. Tell us the neighborhood and a date range, and we flag the next carrier on 94 or 29.','+17013808189','(701) 380-8189','Get your free Fargo quote'))

build({
 'slug':'auto-transport-fargo-north-dakota',
 'title':'Car Shipping in Fargo, ND — Auto Transport | Ship Guy',
 'meta':'Car shipping in Fargo, ND, where Interstate 94 and 29 cross on the Red River. Honest 3 to 6 day windows, NDSU move-in timing, medical center and software campus relocations, lot handoffs for Hawthorne and Roosevelt, curbside pickups in Osgood, Brandt Crossing, West Fargo, and Moorhead, the blizzards, the gates, and the river. Local office on 1st Avenue North. Free quote.',
 'h1':'Car Shipping in<br>Fargo, <span class="accent">North Dakota</span>',
 'lede':'Open, enclosed, and expedited auto transport across Fargo, West Fargo, and Moorhead, planned around 94, 29, the Bison calendar, the blizzards, and the honest windows of a pass-through market.',
 'tel':'+17013808189','disp':'(701) 380-8189','brand':'Fargo','keyword':'car shipping in fargo',
 'localterms':['fargo','red river','interstate 94','interstate 29','1st avenue north','broadway','west fargo','moorhead','hawthorne','osgood','eagle run','minneapolis','bismarck','montana','sioux falls','grand forks','canada','main avenue','university drive','13th avenue','downtown','medical centers','software campus','equipment','campuses','blizzards','floods','pass-through','omaha','milwaukee','kansas city','chicago','denver','dallas','phoenix','snow route','roosevelt','horace mann','brandt crossing','horace','lake bed','interchange','mall','winnipeg','border','32nd avenue','45th street','airport','veterans boulevard','fargodome','fly-and-ship','railroad','civic center','theater','lofts','student cars','island park','elms','jefferson','clara barton','lewis and clark','southpointe','urban plains','deer creek','rose creek','52nd avenue','levees','the wilds','shadow wood','harwood','casselton','mapleton','dilworth','madison','snowbirds','arizona','report date','traveling nurses','residents','nursing and pharmacy','programmers','tractor plant','sporting goods','insurer','electrical distributor','guard wing','air force base','bison','playoff','19th avenue','street fair','valley fair','marathon','fifty inches','forty below','gates','snow emergency','towed','block heater','electric car','2009','forty feet','sandbags','1997','2011','diversion channel','tornado','road salt','brine','gravel','bill of lading','fmcsa','winch','date range','north fargo','west acres','kindred'],
}, BODY, FAQ)
