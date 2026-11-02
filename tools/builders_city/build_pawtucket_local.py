import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Pawtucket, Rhode Island','Car shipping in the first mill town, where Interstate 95 runs through the S-curves and the Boston carriers reach the city in an hour',
 ['Car shipping in Pawtucket runs on Interstate 95, which crosses the city between Providence and Boston. Ship Guy is a licensed auto transport broker with an office in the business park off Newport Avenue.',
  'We book vetted carriers across Pawtucket, from downtown and the mill blocks to Darlington, Fairlawn, and Oak Hill. We cross the lines into Central Falls, Seekonk, and East Providence too. The trucks are the carriers’. The license, the bond, and the phone are ours.',
  'Interstate 95 runs through the middle of the city on the S-curves between Providence and the Massachusetts line. Interstate 295 loops the west side of the metro. Newport Avenue runs north and south through the east side. Main Street follows the Blackstone through downtown and north toward Cumberland.',
  'This page covers 95, the S-curves, Newport Avenue, Main Street, downtown, the mills, and the triple-deckers. It also covers the toy company, the stadium, the Providence colleges, the Florida lane, and the nor’easters.'],
 'Pawtucket at a glance',
 ['A pickup usually happens within 1 to 3 days. Pawtucket sits on the 95 lane between Boston and New York, and the carriers pass through all day. The Boston pool reaches the city in an hour and the Providence pool in fifteen minutes.',
  'Boston, Worcester, Hartford, Springfield, and New Haven are a same-day haul. Portland, Albany, and Manhattan take a day. Philadelphia and Washington take one to two, and Florida takes three.'],
 'Tell us the street. Downtown, the mill blocks, Woodlawn, and all of Central Falls meet the truck on a main road. Darlington, Fairlawn, Oak Hill, Seekonk, and Lincoln usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 95, the S-curves, Interstate 295, Newport Avenue, Main Street, Broadway, Armistice Boulevard, and the Blackstone Bridges',
 prose(
  L('Pawtucket is a tight mill-town grid on both banks of the Blackstone with an interstate through the middle. A carrier uses 95 and the avenues and stays off the side streets.'),
  P('Interstate 95 comes up from Providence and crosses the river. It bends through the S-curves past downtown to Attleboro and Boston. The exits at School Street, Broadway, and Cottage Street drop into the city. The Newport Avenue exit serves the east side. The S-curves slow every truck in the rain. Interstate 295 leaves 95 south of the city and loops west around Providence to Lincoln and Cumberland.'),
  P('Newport Avenue is Route 1A, the strip along the east side from East Providence to the Seekonk line. The business park and the toy headquarters sit on it. Main Street is Route 122, from the Slater Mill bridge through downtown and north to Woonsocket. Broadway and Pawtucket Avenue carry the south side to Providence. Armistice Boulevard and Mineral Spring Avenue cross the city east and west. The bridges over the Blackstone at Main, Exchange, and Division Streets are narrow. A trailer uses the Division Street bridge.'),
  P('The carriers come off 95 at Newport Avenue or Cottage Street. They meet at the big-box lots on Newport Avenue or the lots in the business park. The lots at the stadium on the Seekonk work outside a match day. So do the lots at the new train station and the shopping center lots on Mineral Spring Avenue. The Providence airport is twenty minutes south on 95 for a fly-and-ship.'),
  P('Our office is in the Narragansett Business Park off Newport Avenue, on the ground of the old racetrack.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the Mill Blocks, Woodlawn, Darlington, Fairlawn, Quality Hill, Oak Hill, Pleasant View, Central Falls, and the Line Towns',
 prose(
  L('Pawtucket is a brick downtown, mills along the river, and triple-decker streets in every direction. The truck meets the mills on a main road and the single-family streets at the curb.'),
  P('Downtown is Main Street and Broadway around the city hall, one-way streets and the mill at the falls. The American factory system started in that mill. The driver meets you on Main Street or at the train station lots. The mill blocks along the river and Mineral Spring Avenue are lofts and studios now. The handoff happens on the avenue. Woodlawn south of downtown is triple-deckers on narrow streets with cars on both curbs. The handoff moves to Broadway or Pawtucket Avenue.'),
  P('Darlington on the east side is single-family streets around the old racetrack ground. The curb works on most of it. Fairlawn and Quality Hill on the north side are the same. Oak Hill at the East Providence line is wider streets and bigger houses. The truck reaches the curb. Pleasant View in the northwest is tight, and the handoff happens on Smithfield Avenue.'),
  P('Central Falls, the separate city on Pawtucket’s north side, is the most crowded square mile in the state. No trailer enters its streets. The handoff happens on Broad Street or at the train station. Seekonk and Attleboro across the Massachusetts line are suburbs with driveways, and the truck comes to the house. Lincoln and Cumberland up the river are the same.'),
  P('Central Falls, East Providence, Seekonk, Lincoln, and Cumberland ship with the same trucks and price as Pawtucket. Providence and Cranston do too. Attleboro and Woonsocket add a few minutes on the day and nothing to the figure.'),
 )))

ROUTES=[("Worcester, MA","I-295/MA-146 · ~45 mi","Same day","$130–$210"),("Boston, MA","I-95 · ~45 mi","Same day","$150–$240"),
 ("Hartford, CT","US-6/I-84 · ~80 mi","Same day","$160–$260"),("Springfield, MA","MA-146/I-90 · ~95 mi","Same day","$170–$280"),
 ("New Haven, CT","I-95 · ~105 mi","Same day","$180–$290"),("Portland, ME","I-95 · ~150 mi","1 day","$220–$340"),
 ("Manhattan, NY","I-95 · ~175 mi","1 day","$220–$340"),("Philadelphia, PA","I-95 · ~270 mi","1 day","$260–$390"),
 ("Washington, DC","I-95 · ~405 mi","1–2 days","$340–$490"),("Orlando, FL","I-95 · ~1,250 mi","3 days","$820–$1,180")]
BODY.append(rate_table('Lanes &amp; Costs','Pawtucket Car Shipping Lanes and Estimated Costs',
 'Where Blackstone Valley cars go most, with open-trailer ranges. Price your own lane above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Pawtucket, sedan that runs, open trailer. Count on 10 to 25 percent more for an SUV or a pickup and a premium for enclosed. The week you choose and the carriers on 95 that week set what you pay.',
 prose(
  P('Pawtucket prices with Providence on every lane, because the same carriers cover both in the same hour. The Boston lane rides 95 and fills every day in both directions. The New York lane rides 95 the other way. The Florida lane fills each fall with the snowbirds from the East Bay and the Blackstone Valley. The price rises with them. Worcester rides 146 and is the lowest lane on the table.'),
  P('A September start at the mills’ new tenants or a Boston relocation means a busy week. The <a href="car-shipping-cost.html">cost guide</a> breaks the figure down by size, condition, and timing.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Toy Company, the Mills’ New Tenants, the Providence Hospitals, the Colleges, the Soccer Club, the Navy and the Guard, and the Snowbirds',
 prose(
  L('Pawtucket relocates designers, nurses, students, engineers, and retirees. The toy company has moved the most for decades, and now it is moving itself.'),
  P('The toy company’s headquarters on Newport Avenue is leaving for Boston. The families are moving with it or staying and commuting. Both directions ship with us, and the handoff happens at the business park lots. The mills along the river hold design studios, breweries, and small manufacturers that relocate staff on start dates. The public television station sits in the business park beside us. The plastics compounder and the tour company keep their headquarters here and hire from across the country.'),
  P('The city’s own hospital closed in 2018. The nurses commute to the Providence hospitals a few miles south. Residents arrive each June and traveling nurses all winter. The handoff happens on Broadway or at the business park. The Providence colleges take student cars in late August. A Pawtucket family with a student in Boston ships the car up 95. A parent books, and an adult signs at the lot.'),
  P('The soccer club at the new stadium on the Seekonk brings players and staff each winter. The Navy in Newport and the Guard’s airlift wing at Quonset rotate people on orders. The handoff happens outside the gates. Ship Guy is a private broker and has nothing to do with the Navy. How orders set the dates is on the <a href="military-car-shipping.html">military</a> page.'),
  P('Retirees leave for Florida in October and come back in April. The <a href="state-to-state-car-shipping.html">state-to-state</a> page has what crossing a state line adds.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Match Days, the Arts Festival, the Dragon Boats, College Move-In, the Nor’easters, the Blizzards, the River, and the Heat',
 prose(
  L('Pawtucket runs on a Providence calendar and a Boston calendar. The weather problem is a nor’easter that closes 95 and a river that climbs its banks some springs.'),
  P('Match days at the stadium fill Taft Street and the Division Street bridge for an afternoon. The arts festival takes downtown for a September weekend. The dragon boat races fill the river by the stadium the same month. College move-in in late August fills 95 south to Providence. The Fourth closes the East Bay towns. A late August or early September date wants three weeks of notice.'),
  P('The February 2013 blizzard dropped two feet and brought a statewide travel ban. The January 2022 blizzard did it again. A nor’easter closes 95 for a day. The carriers wait in Attleboro or Warwick until the plows finish. Ice on the S-curves closes the interstate for hours a few times a winter. The March 2010 floods put the Blackstone and the Pawtuxet over their banks for a week. The low streets along the river closed.'),
  P('Sandy in 2012 pushed the bay into the shore towns. Bob in 1991 took the power for days. A hurricane watch holds the truck in Hartford until the all-clear, and we call before the day moves.'),
  P('Summer brings humid heat and afternoon storms. A driver loads in the morning, and a thunderstorm holds the truck for an hour.'),
 )+chips(["Downtown","Slater Mill","The Mill Blocks","Woodlawn","Darlington","Fairlawn","Quality Hill","Oak Hill","Pleasant View","Countryside","Central Falls","East Providence","Seekonk","Attleboro","Lincoln","Cumberland","Providence","North Providence"])
 +NOTE('Serving Pawtucket, Central Falls, and the Blackstone Valley, Darlington curb or Woodlawn triple-decker. Name the street and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Pawtucket?',
 prose(
  L('Most Blackstone Valley cars ride open, and the table above is priced for an open trailer.'),
  P('Enclosed keeps the road salt, the brine, and the sand off the paint. The collectors on Oak Hill book it. So do the retirees sending a car to Florida they would rather not wash on arrival. Ahead of a nor’easter, the car rides the first truck with room, and we say so up front.'),
  P('A commuter car or a student’s hatchback is fine open. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages show where they differ.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('First the figure, then a lot off 95, then a signature at the other end. The move or the start date decides the week.'),
  P('Approve the figure, and a carrier already running 95 that week takes the car. We fix the lot and the window the same afternoon. At pickup the driver photographs the car and fills in its condition on the Bill of Lading. You initial it, and delivery is checked against it.'),
 )+ULI([
  "Nothing personal left in the car",
  "A quarter tank of fuel or less",
  "Four sides and the odometer in your own photos",
  "A key that works and a note on known problems",
  "Aftermarket alarms disarmed",
  "Downtown, in the mill blocks, or on a Darlington side street, expect a main road",
 ])+prose(P('Read <a href="how-it-works.html">how it works</a> for the sequence and <a href="car-shipping-preparation.html">preparation</a> for the morning of pickup.'))))

BODY.append(sec('Why Ship Guy','Why Pawtucket Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already run 95 between Boston and New York every day. We know which bridge a trailer uses and when the stadium closes Taft Street.'),
  P('Our FMCSA license and our $75,000 bond are public on the federal register. The office is in the Narragansett Business Park.'),
  P('You get one coordinator from the quote to the delivery call. The <a href="services.html">services</a> page explains the open, enclosed, and expedited options.'),
 )))

BODY.append(office('Pawtucket','716 Narragansett Park Dr #225','Pawtucket, RI 02861','+14012989783','(401) 298-9783','ET',
 '716+Narragansett+Park+Dr+%23225,+Pawtucket,+RI+02861','Visit Us','Find Ship Guy in Pawtucket',
 'Our office is in the Narragansett Business Park off Newport Avenue, at the East Providence line.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3667.9480234098514!2d-71.34883239999999!3d41.8605405!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89e45b08d58e537b%3A0xf4b0421110e97f73!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793629189809!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Pawtucket to Boston or Florida?","Boston runs one hundred fifty to two hundred forty dollars for a sedan. That is about forty-five miles up 95. Orlando runs eight hundred twenty to eleven hundred eighty, about twelve hundred fifty miles down 95. Worcester is the lowest lane on the table, forty-five minutes up 146. SUVs and pickups run 10 to 25 percent above that."),
 ("Can the carrier come to my street in Woodlawn or Central Falls?","No. Woodlawn is triple-deckers on narrow streets with cars on both curbs. Central Falls is the most crowded square mile in the state. The driver meets you on Broadway, Pawtucket Avenue, or Broad Street, or at the train station lots. Darlington, Fairlawn, Oak Hill, Seekonk, and Lincoln usually allow the curb."),
 ("Do you ship cars for the toy company’s move to Boston?","Yes, in both directions. The headquarters on Newport Avenue is leaving for Boston. The families are moving with it or staying and commuting. We plan the pickup around the start date in the new office. The handoff happens at the business park lots. When an employer pays you back, the paperwork comes from us in the form it asks for."),
 ("Can you ship a car for a student at the Providence colleges?","Yes. The colleges take cars in late August and send them home in May. A parent books, and someone over eighteen signs at the lot. The campus streets on the East Side of Providence are tight. The handoff happens at a lot on the Providence side. A Pawtucket family with a student in Boston ships the car up 95 the same way."),
 ("What happens if a nor’easter or a blizzard hits on my pickup day?","The truck waits in Attleboro or Warwick until the plows finish, usually a day. The February 2013 and January 2022 blizzards each dropped two feet and closed 95. We call the moment the forecast turns. The pickup moves to the first clear morning, and the figure does not move. A hurricane watch holds the truck in Hartford until the all-clear."),
 ("Do you ship cars for nurses at the Providence hospitals?","Yes, all year. The city’s hospital closed in 2018, and the nurses commute to the Providence hospitals a few miles south. Residents arrive each June and traveling nurses all winter. The handoff happens on Broadway or at the business park lots. The figure is the same as Providence."),
 ("Can you ship a car to or from Seekonk, East Providence, or Woonsocket?","Yes. Central Falls, East Providence, Seekonk, Lincoln, and Cumberland ride the same carriers and price the same as Pawtucket. Providence and Cranston do too. Attleboro and Woonsocket add a few minutes on the day and nothing to the figure."),
 ("Does a match at the stadium affect my pickup?","For an afternoon. The stadium on the Seekonk fills Taft Street and the Division Street bridge on a match day. The handoff moves to the Newport Avenue lots. The arts festival and the dragon boat races do the same for a September weekend. The figure does not change."),
 ("Can you ship a car that does not run from Pawtucket?","Yes. The carrier arrives with a winch, and the figure already includes the loading time. The big-box lots on Newport Avenue and the lots in the business park are flat. Let us know if it rolls, steers, and brakes."),
 ("What do you need for a Pawtucket car shipping quote?","Where the car starts and ends, with the neighborhood. Year, make, and model, and whether it runs. Open or enclosed, and the week around the move. That is a complete Pawtucket quote request, and the figure comes back the same day."),
]
BODY.append(faq_section(FAQ,'Pawtucket FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Pawtucket?','Two minutes on the form above prices your lane out of Pawtucket. Name the street and the week, and a carrier already on 95 takes it.','+14012989783','(401) 298-9783','Get your free Pawtucket quote'))

build({
 'slug':'auto-transport-pawtucket-rhode-island',
 'title':'Car Shipping in Pawtucket, RI — Auto Transport | Ship Guy',
 'meta':'Car shipping in Pawtucket, RI, the first mill town, on Interstate 95 between Providence and Boston. The toy company’s move, the Providence hospitals and colleges, the stadium on the Seekonk, main-road handoffs downtown, in Woodlawn, and in Central Falls, curbside pickups in Darlington, Fairlawn, Oak Hill, and Seekonk, the nor’easters, and the Florida lane. Local office in the Narragansett Business Park. Free quote.',
 'h1':'Car Shipping in<br>Pawtucket, <span class="accent">Rhode Island</span>',
 'lede':'Open, enclosed, and expedited auto transport across Pawtucket, Central Falls, and the Blackstone Valley, planned around 95, the S-curves, the Boston and Providence calendars, the match days, and the nor’easters.',
 'tel':'+14012989783','disp':'(401) 298-9783','brand':'Pawtucket','keyword':'car shipping in pawtucket',
 'localterms':['pawtucket','mill town','interstate 95','s-curves','interstate 295','newport avenue','route 1a','main street','route 122','broadway','pawtucket avenue','armistice boulevard','mineral spring avenue','smithfield avenue','broad street','school street','cottage street','division street','exchange','blackstone','slater mill','falls','factory system','the seekonk','downtown','city hall','mill blocks','lofts','woodlawn','triple-deckers','darlington','racetrack','fairlawn','quality hill','oak hill','pleasant view','countryside','central falls','crowded square mile','east providence','seekonk','attleboro','lincoln','cumberland','woonsocket','providence','cranston','north providence','business park','narragansett','toy company','headquarters','boston','design studios','breweries','public television','plastics compounder','tour company','hospital','closed in 2018','nurses','residents','colleges','east side','student','soccer club','stadium','taft street','match days','navy','newport','guard','airlift wing','quonset','orders','retirees','florida','snowbirds','arts festival','dragon boat','move-in','the fourth','east bay','nor’easter','february 2013','january 2022','two feet','travel ban','plows','ice','march 2010','floods','pawtuxet','sandy','2012','bob','1991','hurricane','hartford','humid','train station','airport','fly-and-ship','worcester','146','springfield','new haven','portland','albany','manhattan','philadelphia','washington','orlando','road salt','brine','sand','bill of lading','fmcsa','winch'],
}, BODY, FAQ)
