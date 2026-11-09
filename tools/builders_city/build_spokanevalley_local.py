import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Spokane Valley, Washington','Car shipping where Interstate 90 runs the length of town, the industrial park stages the trucks, and the Idaho line is ten minutes east',
 ['Car shipping in Spokane Valley runs on Interstate 90, which crosses the whole city in ten minutes. Ship Guy is a licensed auto transport broker with an office on North Sullivan Road.',
  'We book vetted carriers across Spokane Valley, from the Sprague grids to the Ponderosa pines and Greenacres. Millwood, Liberty Lake, Otis Orchards, and the east side of Spokane ride the same trucks. The trucks are the carriers’ own. Ship Guy holds the license and the bond.',
  'Interstate 90 runs the full width of the city between Spokane and the Idaho line. Trent Avenue runs beside it to the north through the industrial park and the rail yards. Sullivan, Pines, Argonne, and Barker run north and south across both. Sprague Avenue, Appleway, Mission, Broadway, and Dishman-Mica carry the rest.',
  'This page covers 90, Trent, Sullivan, Sprague, the grids, the south hills, and the river. It also covers the industrial park, the two mills, the dealers on Sprague, and the hospital. Valleyfest, the fair, the windstorms, the snow, and the smoke are here too.'],
 'Spokane Valley at a glance',
 ['Most Spokane Valley pickups land within 1 to 3 days. The carriers between Seattle, Montana, and the Idaho panhandle run 90 through town all day. The industrial park and the dealers on Sprague keep trucks around every week. A Valley pickup often beats a downtown Spokane one by a day.',
  'Missoula and Coeur d’Alene are a same-day haul. Seattle, Portland, and Boise take a day. Salt Lake City and Sacramento take two. Denver, Los Angeles, and Minneapolis take three, and Chicago takes three to four.'],
 'Tell us the cross street. Opportunity, Veradale, Greenacres, Dishman, and Trentwood usually allow the curb on the grids. Ponderosa, Painted Hills, the Saltese slopes, and Millwood meet the truck on a main road.'))

BODY.append(sec('The Roads','Interstate 90, Trent Avenue, Sullivan Road, Pines Road, Argonne Road, Barker Road, Sprague Avenue, Appleway Boulevard, Mission Avenue, Broadway Avenue, Dishman-Mica Road, and the River Bridges',
 prose(
  L('Spokane Valley is a flat grid on a river bench with a freeway laid straight across it. A carrier picks an exit and finds the lot within five minutes.'),
  P('Interstate 90 enters from Spokane at the Havana line and leaves at the state line ten minutes later. The exits are Sprague, Broadway, Argonne, Pines, Evergreen, Sullivan, Barker, Liberty Lake, and Otis Orchards. Coeur d’Alene is thirty minutes east, and Seattle is five hours west over the passes. Trent Avenue is Highway 290, running the north side from Spokane through Millwood and the industrial park. The rail crossings on Trent stop traffic for a passing train several times a day. Pines Road is Highway 27, south to the Palouse.'),
  P('Sullivan Road is the main north-south street. It runs from the industrial park over the river and the freeway to the south grids. The bridge over the river ices first. Argonne Road runs north through Millwood toward the ski hill and south to Dishman. Barker Road carries the east side and the new interchange. Sprague Avenue is the old highway, a dealer strip from Fancher to University and the grid’s spine beyond. Appleway runs one way beside it through the middle of town. Mission and Broadway cross the Valley north of Sprague, and Dishman-Mica runs south into the pines.'),
  P('The carriers come off 90 at Pines or Sullivan. They stage at the truck stops at the Broadway exit. They meet at the mall lots at Indiana and Sullivan or the big-box lots along Sprague. The fairgrounds at Broadway and Havana work outside the fair. The lots at Mirabeau Point work outside events. So do the dealer lots on Sprague when a dealer is shipping. The airport is twenty-five minutes west through Spokane for a fly-and-ship. The small field by Millwood takes private planes.'),
  P('Our office sits on North Sullivan Road north of the river, a mile up from the 90 exit.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Opportunity, Veradale, Greenacres, Dishman, Trentwood, Millwood, Ponderosa, Painted Hills, the Saltese Slopes, Otis Orchards, Liberty Lake, Newman Lake, and the East Side of Spokane',
 prose(
  L('Spokane Valley only became a city in 2003. It still reads as a string of older towns on one grid. The grid takes a trailer nearly everywhere, and the hills on the south edge do not.'),
  P('Opportunity is the middle of town around Sprague and Pines, mid-century houses on big lots and wide streets. The curb works. Veradale around Sullivan and Sprague is the same grid with the mall to the north. The curb works there too. Greenacres on the east side is new subdivisions among the old orchards off Barker. The streets are wide, and a covenant here and there moves the handoff to the entrance. Dishman on the west side is older streets around Appleway and the dealer strip. The curb works on most of them.'),
  P('Trentwood north of the river is the aluminum mill, rail sidings, and modest grids where the curb works. Millwood is its own small town around the paper mill and the Argonne crossing. The streets are tight, and the handoff happens at the edge. Ponderosa on the south edge is pines, winding streets, and the memory of the 1991 firestorm. The driver meets you on Dishman-Mica. Painted Hills and the Saltese slopes are new subdivisions climbing the south hills. The roads wind and ice. The handoff moves to the Sullivan lots in winter.'),
  P('Otis Orchards and Newman Lake east of Barker are country lots, lake houses, and gravel lanes. The handoff happens at the Harvard Road lots by the freeway. Liberty Lake is its own city of new streets, a lake, and the tech campus. The curb works. Spokane’s east side across Havana is older grids where the curb works. The fairgrounds sit right on the line.'),
  P('Millwood, Liberty Lake, Otis Orchards, Trentwood, and the east side of Spokane ride the same trucks. They price the same as Spokane Valley. Spokane itself does too. Post Falls and Coeur d’Alene add a figure for the state line, and Newman Lake adds a day.'),
 )))

ROUTES=[("Missoula, MT","I-90 · ~190 mi","Same day","$220–$340"),("Seattle, WA","I-90 · ~290 mi","1 day","$260–$390"),
 ("Portland, OR","US-395/I-84 · ~360 mi","1 day","$320–$460"),("Boise, ID","US-95 · ~430 mi","1 day","$370–$530"),
 ("Salt Lake City, UT","US-95/I-84 · ~700 mi","2 days","$500–$730"),("Sacramento, CA","US-97/I-5 · ~910 mi","2 days","$650–$920"),
 ("Denver, CO","I-90/I-25 · ~1,090 mi","3 days","$750–$1,050"),("Los Angeles, CA","US-95/I-15 · ~1,210 mi","3 days","$800–$1,150"),
 ("Minneapolis, MN","I-90/I-94 · ~1,390 mi","3 days","$900–$1,250"),("Chicago, IL","I-90 · ~1,790 mi","3–4 days","$1,050–$1,450")]
BODY.append(rate_table('Lanes &amp; Costs','Spokane Valley Car Shipping Lanes and Estimated Costs',
 'The lanes Valley cars ship most, with open-trailer estimates. The form above prices your exact lane.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Spokane Valley, running sedan, open trailer. An SUV or a pickup adds 10 to 25 percent, and enclosed adds more. The week and the carriers running 90 that week decide the figure.',
 prose(
  P('Spokane Valley prices with Spokane on every lane, and the Montana lane runs a little lower. Missoula is three hours east on 90, and the Seattle trucks run through to Montana daily. Seattle rides 90 over Snoqualmie Pass, and the pass closes a few days each winter. Portland rides 395 and 84 down the Columbia. Boise rides 95 through Lewiston. Salt Lake City and the Southwest ride 95 and 84. The Idaho panhandle ships on the same trucks for a few dollars more.'),
  P('A fair week in September or a smoke week in August makes for a crowded calendar. The <a href="car-shipping-cost.html">cost guide</a> explains size, condition, and timing in turn.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Industrial Park, the Aluminum Mill, the Paper Mill, the Dealers on Sprague, the Hospital, the Tech Campus in Liberty Lake, the Spokane Campuses, Fairchild, and the Retirees',
 prose(
  L('Spokane Valley relocates plant managers, mill crews, nurses, engineers, dealers’ cars, and retirees. The industrial park and the dealers move the most.'),
  P('The industrial park north of our office holds more than a hundred companies on six hundred acres. Its plants and warehouses relocate managers on start dates, and the handoff happens at the gate. The aluminum mill in Trentwood hires rolling crews from across the region. The paper mill in Millwood does the same on a smaller scale. The utility-meter maker whose old campus holds our office moved its headquarters to Liberty Lake. The tech campus there relocates engineers. When the employer pays for the shipment, we write it up however it needs.'),
  P('The dealers along Sprague ship trades and auction cars every week. A dealer’s car rides with the household moves. The hospital on Mission Avenue brings nurses all year. The Spokane campuses are twenty minutes west and send cars in each August and home each May. A parent books, and an adult signs at the lot. Retirees come to the Valley’s single-level houses from the coast and go south each winter. The <a href="state-to-state-car-shipping.html">state-to-state</a> page explains the paperwork a state line adds.'),
  P('Fairchild Air Force Base sits a half hour west on 90. Its airmen rotate on a summer calendar. Some live in the Valley, and the handoff happens at the Sullivan lots. Ship Guy is a private broker and not part of the Air Force. The <a href="military-car-shipping.html">military</a> page covers orders and the dates they set.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Valleyfest, the County Fair, the Ballclub, Hoopfest Weekend, the Lake Traffic, the Ski Traffic, the Windstorms, the Snow, the Cold, and the Smoke',
 prose(
  L('Spokane Valley runs on a fairgrounds calendar and a lake calendar. The weather problem is a windstorm every few years, a hard winter every winter, and smoke most Augusts.'),
  P('Valleyfest fills Mirabeau Point the fourth weekend of September and closes Sprague for the parade. The county fair fills the fairgrounds at Broadway and Havana for ten days in September. The minor-league ballclub plays there all summer. Hoopfest takes downtown Spokane the last weekend of June, and the Valley is the detour. The lake traffic fills 90 east every summer weekend. The Coeur d’Alene triathlon in late June fills it harder. The ski traffic runs up Argonne toward Mount Spokane on winter weekends. The mall traffic jams Sullivan and Indiana in December. Give a fair week three weeks of notice.'),
  P('The November 2015 windstorm gusted to seventy-one miles an hour and dropped the ponderosas across the lines. Close to two hundred thousand customers lost power, some for more than a week. The January 2021 windstorm hit the same speed. The November 1996 ice storm cut power to a hundred thousand. When the wind is up, the carriers wait in the lot until it drops.'),
  P('December 2008 buried the Valley under more than five feet of snow in one month. A foot shuts the south hills, and Sullivan ices on the bridge first. The January 2024 cold snap sat below zero for days. The drivers warmed the trucks for an hour. The August 2023 fires at Medical Lake and Elk burned hundreds of homes. The smoke sat on the Valley for a week. The October 1991 firestorm burned through Ponderosa. The June 2021 heat dome hit one hundred nine degrees, and the drivers loaded at dawn.'),
 )+chips(["Opportunity","Veradale","Greenacres","Dishman","Trentwood","Millwood","Ponderosa","Painted Hills","Saltese","Chester","Mica","Otis Orchards","Newman Lake","Liberty Lake","East Central","East Spokane","Spokane","Post Falls","Coeur d’Alene"])
 +NOTE('Serving Spokane Valley, Millwood, Liberty Lake, and the Idaho line, Sprague grid or Ponderosa pine. Tell us the cross street and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Spokane Valley?',
 prose(
  L('Open trailers carry most of the Inland Northwest’s cars, and the table above assumes one.'),
  P('Enclosed keeps the pass brine, the August smoke, and the hail off the paint. The dealers ship their nicest inventory enclosed. So do the retirees with a convertible and the engineers moving a car worth more than the move. When a storm is coming and only an open truck has room, we say so first.'),
  P('A commuter car or a student’s hatchback rides open and arrives fine. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages lay out the difference.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A figure, a lot off Sullivan, and a signature when the car rolls off the truck. The start date or the orders set the week.'),
  P('Approve the figure, and we hand the car to a carrier already running 90 that week. The lot and the window are set the same day. The driver photographs the car at pickup and records its condition on the Bill of Lading. You initial it, and it governs the delivery check.'),
 )+ULI([
  "Your belongings out of the cabin and the trunk",
  "Fuel at a quarter tank or less",
  "Photos of every side and the odometer before the truck arrives",
  "A working key and a note on anything that acts up",
  "Aftermarket alarms disabled",
  "In Ponderosa, on the Saltese slopes, or in Millwood, expect the Sullivan lots",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> page walks the steps, and the <a href="car-shipping-preparation.html">preparation</a> page covers pickup morning.'))))

BODY.append(sec('Why Ship Guy','Why Spokane Valley Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already run 90 between Seattle and Montana every day. We know which weeks the fair takes the fairgrounds and when the pass closes.'),
  P('Our FMCSA license and our $75,000 bond are on the federal register for anyone to check. The office is on North Sullivan Road.'),
  P('One person at Ship Guy handles the move from quote to delivery call. The <a href="services.html">services</a> page covers open, enclosed, and expedited one by one.'),
 )))

BODY.append(office('Spokane Valley','2818 N Sullivan Rd #535','Spokane Valley, WA 99216','+15092874409','(509) 287-4409','PT',
 '2818+N+Sullivan+Rd+%23535,+Spokane+Valley,+WA+99216','Visit Us','Find Ship Guy in Spokane Valley',
 'Our office sits on North Sullivan Road north of the river, a mile up from the 90 exit.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3315.611485031521!2d-117.19395730000001!3d47.68315760000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x5361df20fd1a746f%3A0x74fd787a0109839b!2sShip%20Guy%20Auto%20Transport!5e1!3m2!1sen!2sus!4v1794237296521!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Spokane Valley to Seattle or Boise?","Seattle runs two hundred sixty to three hundred ninety dollars for a sedan. It is about two hundred ninety miles over the pass. Boise runs three hundred seventy to five hundred thirty down 95. Missoula is the lowest lane on the table. Los Angeles runs eight hundred to one thousand one hundred fifty. An SUV or a pickup adds 10 to 25 percent."),
 ("Why does a Spokane Valley pickup sometimes beat a Spokane one?","Because the carriers stage at the Broadway exit and the industrial park. The grid takes a trailer nearly everywhere. A Valley pickup is the first stop of the morning before the truck fights downtown. The figure is the same as Spokane’s, and the window is often a day shorter."),
 ("Can the carrier come to my street in Ponderosa or on the Saltese slopes?","Not in winter, and often not in summer. Ponderosa is winding streets under the pines, and the Saltese and Painted Hills roads climb and ice. The driver meets you on Dishman-Mica or at the Sullivan lots. Opportunity, Veradale, Greenacres, Dishman, and Trentwood usually allow the curb."),
 ("Do you ship cars for the dealers on Sprague or the industrial park?","Yes, every week. The dealers ship trades and auction cars, and the industrial park relocates managers on start dates. The aluminum mill, the paper mill, and the tech campus in Liberty Lake do the same. The handoff happens at the dealer lot or the gate. When the employer pays, we write it up however it needs."),
 ("Can you ship a car to or from Coeur d’Alene or Post Falls?","Yes. The Idaho line is ten minutes east on 90, and Coeur d’Alene is thirty. Post Falls and Coeur d’Alene ride the same carriers and add a figure for the state line. Liberty Lake, Millwood, Otis Orchards, and Trentwood price the same as Spokane Valley."),
 ("What happens if a windstorm or a snowstorm hits on my pickup day?","The truck waits in the lot until the wind drops or the plows finish, usually a day. The November 2015 windstorm cut power to close to two hundred thousand customers. December 2008 dropped more than five feet of snow. We call as soon as the forecast turns. The pickup moves to the first clear morning, and the figure stays put."),
 ("Does the August smoke stop a shipment?","Rarely. The August 2023 fires sat smoke on the Valley for a week. The carriers kept running with the windows up. A driver may load earlier in the day. Enclosed keeps the ash off the paint, and some owners book it for August alone."),
 ("What happens during the county fair or Valleyfest?","The fairgrounds at Broadway and Havana fill for ten days in September. Valleyfest closes Sprague for the parade the fourth weekend. The handoff moves to the mall lots at Indiana and Sullivan, and the figure does not change. Give a fair week three weeks of notice."),
 ("Can you ship a car that does not run from Spokane Valley?","Yes. The carrier brings a winch, and the figure includes the loading time. The mall lots and the Sullivan big-box lots are flat. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Spokane Valley car shipping quote?","Both addresses, with the cross street. The year, make, and model, and whether it runs. Open or enclosed, and the week around the start date or the orders. With those, the Spokane Valley figure comes back the same day."),
]
BODY.append(faq_section(FAQ,'Spokane Valley FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Spokane Valley?','Two minutes on the form above puts a Spokane Valley figure on your lane. Tell us the cross street and the week, and a carrier already on 90 takes it.','+15092874409','(509) 287-4409','Get your free Spokane Valley quote'))

build({
 'slug':'auto-transport-spokane-valley-washington',
 'title':'Car Shipping in Spokane Valley, WA — Auto Transport | Ship Guy',
 'meta':'Car shipping in Spokane Valley, WA, on Interstate 90 between Spokane and the Idaho line. The industrial park, the aluminum mill, the paper mill, the dealers on Sprague, the hospital, and Fairchild, curbside pickups in Opportunity, Veradale, Greenacres, Dishman, and Trentwood, main-road handoffs for Ponderosa and the south hills, Valleyfest, the county fair, the windstorms, the snow, and the smoke. Local office on North Sullivan Road. Free quote.',
 'h1':'Car Shipping in<br>Spokane Valley, <span class="accent">Washington</span>',
 'lede':'Open, enclosed, and expedited auto transport across Spokane Valley, Millwood, Liberty Lake, and the Idaho line, planned around 90, Sullivan, the industrial park, the fair, the wind, the snow, and the smoke.',
 'tel':'+15092874409','disp':'(509) 287-4409','brand':'Spokane Valley','keyword':'car shipping in spokane valley',
 'localterms':['spokane valley','interstate 90','trent avenue','highway 290','sullivan road','pines road','highway 27','argonne road','barker road','sprague avenue','appleway','mission avenue','broadway avenue','dishman-mica','evergreen','liberty lake','otis orchards','havana','state line','idaho line','coeur d’alene','rail crossings','palouse','ski hill','mount spokane','dealer strip','fancher','university','indiana','mall','industrial park','six hundred acres','truck stops','fairgrounds','mirabeau point','airport','fly-and-ship','millwood','opportunity','veradale','greenacres','orchards','covenant','dishman','trentwood','aluminum mill','paper mill','ponderosa','1991 firestorm','painted hills','saltese','chester','mica','newman lake','harvard road','tech campus','east side','post falls','grids','single-level','utility-meter maker','hospital','spokane campuses','retirees','fairchild air force base','airmen','valleyfest','parade','county fair','ten days','ballclub','hoopfest','lake traffic','triathlon','ski traffic','november 2015','seventy-one','two hundred thousand','january 2021','november 1996','ice storm','december 2008','five feet','a foot','january 2024','below zero','august 2023','medical lake','elk','smoke','june 2021','one hundred nine','snoqualmie pass','lewiston','columbia','missoula','seattle','portland','boise','salt lake city','sacramento','denver','los angeles','minneapolis','chicago','montana','brine','hail','ash','convertible','bill of lading','fmcsa','winch'],
}, BODY, FAQ)
