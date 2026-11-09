import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Lakewood, New Jersey','Car shipping in the fastest-growing town in the state, where Route 9 crawls, the yellow buses rule the morning, and the Florida lane runs all year',
 ['Car shipping in Lakewood runs on Route 9, Route 70, and the Parkway exits at 88 and 91. Ship Guy is a licensed auto transport broker with an office in the Lakewood industrial park.',
  'We book vetted carriers across Lakewood, from the yeshiva blocks to the new streets past Cross Street. Toms River, Jackson, Howell, Brick, and the Shore towns ride the same trucks. The trucks belong to the carriers. Ship Guy holds the license and the bond.',
  'Route 9 is the spine, four lanes that carry the whole town and stall twice a day. Route 70 runs east to the Parkway and the beaches and west into the pines. The Parkway allows trucks this far south, and the carriers use it. Cedar Bridge Avenue, New Hampshire Avenue, County Line Road, and Cross Street carry the rest.',
  'This page covers Route 9, Route 70, the Parkway, 195, the industrial park, and the old grid. It also covers the yeshiva, the schools, the hospital, the industrial park’s businesses, and the retirement villages. The Sabbath calendar, the Shore summer, the storms, and the Florida lane are here too.'],
 'Lakewood at a glance',
 ['Most Lakewood pickups land within 1 to 3 days. The town sits an hour from New York and Philadelphia on roads the carriers run daily. The Turnpike trucks come down 195, and the Shore trucks use the Parkway. The Florida lane runs both ways all year, not only in snowbird season.',
  'New York, Philadelphia, Hartford, Baltimore, and Washington are a same-day haul. Boston and Pittsburgh take a day. Charlotte takes two, and Florida takes three.'],
 'Tell us the block. The old grid between Route 9 and the lake meets the truck at the industrial park. The new developments past Cross Street, the villages, Jackson, and Howell usually allow the curb.'))

BODY.append(sec('The Roads','Route 9, Route 70, Route 88, the Parkway, Interstate 195, Cedar Bridge Avenue, New Hampshire Avenue, County Line Road, Cross Street, Clifton Avenue, and Madison Avenue',
 prose(
  L('Lakewood is a township that grew into a city without the roads for one. A carrier learns which streets move and which never will.'),
  P('Route 9 runs north and south through the middle as Madison Avenue and River Avenue. It carries the town to Howell and Freehold one way and to Toms River the other. It stalls at the school hours and again at dusk. Route 70 crosses the south end from the Parkway at Brick west to Lakehurst and the pines. Route 88 runs east to Brick and Point Pleasant. The Garden State Parkway passes the east edge with exits at 88 and 91. Trucks are allowed on it this far south, so the carriers use it. Interstate 195 runs ten miles north to the Turnpike and Trenton.'),
  P('Cedar Bridge Avenue runs from Route 9 east through the industrial park to the Parkway. New Hampshire Avenue runs north and south through the park past the airport and the ballpark. County Line Road is the Monmouth County line and the newest townhouse corridor. Cross Street and Prospect Street carry the west side. Clifton Avenue is the old downtown, two lanes and tight. Oak Street and Pine Street cross the south end. Lake Carasaljo sits in the middle with the parks around it.'),
  P('The carriers come off the Parkway at 88 or 91. On Route 9 they turn at Cedar Bridge or Route 70. They meet at the industrial park, where the streets are wide and built for trucks. The ballpark lot off New Hampshire Avenue works outside game nights. So do the big-box lots on Route 70 at the Brick line. The Route 9 shopping centers in Howell work too. The airport in the park is small, and Newark is an hour up the Parkway for a fly-and-ship.'),
  P('Our office sits in Independence Plaza on Avenue of the States, in the industrial park off Cedar Bridge.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the Yeshiva Blocks, the West Side, County Line, the Industrial Park, Leisure Village, the Lake, Toms River, Brick, Jackson, Howell, Freehold, Lakehurst, and the Shore Towns',
 prose(
  L('Lakewood is an old resort-town grid now carrying a city of a hundred forty thousand people. The truck meets the grid on the edges and the new developments at the curb.'),
  P('Downtown is Clifton Avenue, two lanes of storefronts, and blocks of older houses toward the lake. The streets are narrow, the parking is full, and the yellow buses fill them twice a day. No trailer works there. The driver meets you at the industrial park or a Route 70 lot. The blocks around the yeshiva on Private Way and Forest Avenue are the densest in town. The handoff moves to the park there too. The streets off Route 9 south of the lake are the same story.'),
  P('The west side past Cross Street and Prospect Street is new developments, duplexes and townhouses on wide streets. The curb works on most of them, and a development entrance works where it does not. County Line Road and the north end are townhouse corridors still under construction. The driver meets you at the development entrance. The industrial park is wide streets and loading docks, and a trailer fits anywhere. Leisure Village, the retirement community on the south side, allows a trailer at the clubhouse lot.'),
  P('Toms River to the south is the county seat, grids and subdivisions where the curb works. Brick to the east is postwar grids, and the curb works there too. Jackson to the west is subdivisions, farms, and the amusement park off 195. The curb works in the subdivisions. Howell and Freehold to the north are the same. Lakehurst and Manchester to the west are pines and retirement villages, and the handoff happens on Route 70. Point Pleasant, Seaside, and Long Branch are the Shore. In summer the handoff happens on the mainland side of the bridges.'),
  P('Toms River, Brick, Jackson, Howell, and Manchester ship with the same trucks and price the same as Lakewood. Freehold and Point Pleasant do too. Long Beach Island and the barrier islands add a day in summer.'),
 )))

ROUTES=[("New York, NY","GSP/NJ Tpke · ~65 mi","Same day","$150–$240"),("Philadelphia, PA","I-195/NJ Tpke · ~65 mi","Same day","$150–$240"),
 ("Hartford, CT","GSP/I-95/I-91 · ~150 mi","Same day","$200–$320"),("Baltimore, MD","NJ Tpke/I-95 · ~165 mi","Same day","$210–$330"),
 ("Washington, DC","NJ Tpke/I-95 · ~210 mi","Same day","$230–$350"),("Boston, MA","I-95 · ~270 mi","1 day","$260–$390"),
 ("Pittsburgh, PA","I-195/I-76 · ~370 mi","1 day","$330–$470"),("Charlotte, NC","I-95/I-85 · ~600 mi","2 days","$470–$680"),
 ("Orlando, FL","I-95 · ~1,020 mi","3 days","$750–$1,070"),("Miami, FL","I-95 · ~1,240 mi","3 days","$820–$1,170")]
BODY.append(rate_table('Lanes &amp; Costs','Lakewood Car Shipping Lanes and Estimated Costs',
 'The lanes Ocean County cars travel most, with open-trailer estimates. Your exact lane prices on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Lakewood, running sedan, open trailer. An SUV or a pickup adds 10 to 25 percent, and enclosed costs more. The week and the carriers on the Parkway that week set the figure.',
 prose(
  P('Lakewood prices with central New Jersey on every lane, an hour from both big cities. New York rides the Parkway and the Turnpike north. Philadelphia rides 195 and the Turnpike south. Baltimore and Washington ride 95 and run daily. The Florida lane is the busiest lane in town, with families shipping to Miami and Boca all year. The Lakewood carriers know Miami better than Trenton.'),
  P('The weeks before the fall holidays and before Passover are busy ones. The <a href="car-shipping-cost.html">cost guide</a> covers size, condition, and timing in turn.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Yeshiva, the Schools, the Hospital, the Industrial Park, the Retirement Villages, the University, the Joint Base, and the Families Arriving Every Week',
 prose(
  L('Lakewood relocates students, young families, teachers, nurses, warehouse staff, and retirees. The yeshiva and the families that follow it move the most.'),
  P('The yeshiva is the largest outside Israel. Its students and young families arrive from Brooklyn, Monsey, Baltimore, Chicago, and overseas. The town adds thousands of residents a year, and most of them bring a car or buy one. The private schools hire teachers from across the region on the school calendar. A parent or an adult signs at the lot. The hospital on Route 9 brings nurses all year. When an employer covers the shipment, we write it up however it needs.'),
  P('The industrial park holds hundreds of businesses, from online retailers to staffing firms and real estate offices. They relocate managers on start dates, and the handoff happens at the park. Georgian Court University fills its lakeside campus each late August. The retirement villages on the south side and in Manchester bring retirees from the whole state. Many go to Florida each fall and come back in April, and they ship the car both ways. The <a href="state-to-state-car-shipping.html">state-to-state</a> page explains the paperwork a state line adds.'),
  P('The joint base at Lakehurst sits fifteen miles west on Route 70. Its families rotate year round with a summer peak. The Navy’s weapons station at Earle is twenty minutes north. Ship Guy is a private broker and not part of the base. The <a href="military-car-shipping.html">military</a> page covers orders and the dates they set.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Sabbath and the Holidays, the School Hours, the Shore Summer, the Ballpark Season, Sandy, the Blizzards, Ida, and the Pine Barrens Fires',
 prose(
  L('Lakewood runs on a religious calendar before anything else. The weather problem is a coastal storm every few years and a blizzard every few winters.'),
  P('Much of the town does not do business from Friday afternoon through Saturday night. The fall holidays in September and October and Passover in the spring follow the same rule. We never schedule a handoff in those hours, and the carriers who work Lakewood know the calendar. The weeks before the holidays are the busiest of the year. The week after each one is quiet. The yellow buses fill every street from seven to nine and again from three to five. A carrier plans a Lakewood pickup for mid-morning.'),
  P('The Shore traffic fills the Parkway and Route 70 every summer Friday and Sunday. The ballpark on New Hampshire Avenue fills its lot on game nights from April to September. The amusement park in Jackson fills 195 and Route 537 all summer. Give a holiday week or a summer weekend three weeks of notice.'),
  P('Sandy in October 2012 took the power for a week and the trees with it. The Shore towns east of here lost whole blocks. The January 2016 blizzard dropped close to two feet. Ida in September 2021 flooded the low roads for a day. The April 2025 wildfire in the pines closed the Parkway south of Toms River for a day. The smoke sat on the town. A nor’easter floods the Shore roads a few times each winter, and the Shore pickups wait.'),
 )+chips(["Downtown","Clifton Avenue","The Yeshiva Blocks","Forest Avenue","Lake Carasaljo","The West Side","Cross Street","Prospect Street","County Line","The Industrial Park","Cedar Bridge","Leisure Village","Route 9 South","Toms River","Brick","Point Pleasant","Jackson","Howell","Freehold","Lakehurst","Manchester","Whiting","Seaside Heights","Asbury Park","Long Branch"])
 +NOTE('Serving Lakewood, Ocean County, and the northern Shore, yeshiva block or Leisure Village cul-de-sac. Tell us the block and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Lakewood?',
 prose(
  L('Open trailers carry most of Ocean County’s cars, and the table above prices one.'),
  P('Enclosed keeps the road salt, the pine pollen, and the Shore sand off the paint. The families shipping a car worth more than the move book it. So do the retirees sending a convertible to Florida. When a storm is coming and only an open truck has room, you hear that first.'),
  P('A minivan or a commuter sedan rides open and arrives fine. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages set out the difference.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A figure, a lot in the industrial park, and a signature when the car comes off the truck. The calendar picks the day.'),
  P('Approve the figure, and we hand the car to a carrier already on the Parkway that week. The lot and the window are set the same day, around the Sabbath and the holidays. The driver photographs the car at pickup and records its condition on the Bill of Lading. You initial it, and it is the reference at delivery.'),
 )+ULI([
  "Your belongings out of the cabin and the trunk",
  "Fuel at a quarter tank or less",
  "Photos of every side and the odometer before the truck comes",
  "A working key, and a word if the car needs the winch",
  "Aftermarket alarms switched off",
  "In the old grid or near the yeshiva, expect the industrial park or a Route 70 lot",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> page walks the steps, and the <a href="car-shipping-preparation.html">preparation</a> page covers pickup morning.'))))

BODY.append(sec('Why Ship Guy','Why Lakewood Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already run the Parkway and the Florida lane every week. We know the calendar, the bus hours, and which blocks never take a trailer.'),
  P('Our FMCSA license and our $75,000 bond are public record on the federal register. The office is on Avenue of the States in the industrial park.'),
  P('One person at Ship Guy carries your move from the first figure to the delivery call. The <a href="services.html">services</a> page covers open, enclosed, and expedited one by one.'),
 )))

BODY.append(office('Lakewood','1776 Ave of the States #443','Lakewood, NJ 08701','+17324797353','(732) 479-7353','ET',
 '1776+Ave+of+the+States+%23443,+Lakewood,+NJ+08701','Visit Us','Find Ship Guy in Lakewood',
 'Our office sits in Independence Plaza on Avenue of the States, in the industrial park off Cedar Bridge.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3768.5139705673337!2d-74.191192!3d40.0760067!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c183756c886ea5%3A0x8035bd57a6a9007!2sShip%20Guy%20Auto%20Transport!5e1!3m2!1sen!2sus!4v1794237401799!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Lakewood to Florida?","Orlando runs seven hundred fifty to one thousand seventy dollars for a sedan and takes three days. Miami runs eight hundred twenty to one thousand one hundred seventy. The lane runs both ways all year, so the figure moves less than it does from most towns. New York and Philadelphia run one hundred fifty to two hundred forty. An SUV or a pickup adds 10 to 25 percent."),
 ("Do you schedule around the Sabbath and the holidays?","Yes, always. We never set a handoff from Friday afternoon through Saturday night or on the holidays. The weeks before the fall holidays and before Passover are the busiest of the year. Book those early. The carriers who work Lakewood know the calendar, and we confirm every date against it."),
 ("Can the carrier come to my street in the old grid or near the yeshiva?","No. The streets between Route 9 and the lake are narrow, and the parking is full. The buses fill them twice a day. The driver meets you at the industrial park or a Route 70 lot. The new developments past Cross Street, the villages, Jackson, and Howell usually allow the curb."),
 ("What time of day works for a Lakewood pickup?","Mid-morning or early afternoon. The yellow buses fill every street from seven to nine and again from three to five. Route 9 stalls with them. A carrier plans the Lakewood stop between the bus runs. The figure does not change with the hour."),
 ("Can you ship a car for a student at the yeshiva or Georgian Court?","Yes. The yeshiva’s students arrive from Brooklyn, Baltimore, Chicago, and overseas all year, and many bring a car. Georgian Court fills its lakeside campus in late August. A parent or an adult signs at the lot. The handoff happens at the industrial park or the campus lot."),
 ("Do you ship cars for the retirement villages?","Yes, both ways every year. Leisure Village and the Manchester villages send cars to Florida each fall and bring them back in April. The handoff happens at the clubhouse lot. Book the fall trip by September, because the whole Shore ships south in October."),
 ("Can the carrier use the Parkway to reach Lakewood?","Yes. The Parkway bans trucks only north of exit 105. Lakewood’s exits at 88 and 91 sit well south of it. The carriers come off there or down Route 9. The Turnpike trucks come across on 195."),
 ("What happens if a coastal storm hits on my pickup day?","The truck waits inland until the roads reopen, usually a day. Sandy in 2012 took the power for a week. A nor’easter floods the Shore roads a few times each winter. We call as soon as the forecast turns. The pickup moves to the first clear morning, and the figure stays where it was."),
 ("Can you ship a car to or from Toms River, Jackson, or the Shore?","Yes. Toms River, Brick, Jackson, Howell, and Manchester ride the same carriers and price the same as Lakewood. Freehold and Point Pleasant do too. Long Beach Island and the barrier islands add a day in summer. The handoff happens on the mainland side of the bridge."),
 ("What do you need for a Lakewood car shipping quote?","Both addresses, with the block or the development. The year, make, and model, and whether it runs. Open or enclosed, and the week you need, with the holidays in mind. With those, the Lakewood figure comes back the same day."),
]
BODY.append(faq_section(FAQ,'Lakewood FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Lakewood?','Two minutes on the form above puts a Lakewood figure on your lane. Tell us the block and the week, and a carrier already on the Parkway takes it.','+17324797353','(732) 479-7353','Get your free Lakewood quote'))

build({
 'slug':'auto-transport-lakewood-new-jersey',
 'title':'Car Shipping in Lakewood, NJ — Auto Transport | Ship Guy',
 'meta':'Car shipping in Lakewood, NJ, on Route 9, Route 70, and the Parkway. Pickups scheduled around the Sabbath, the holidays, and the school buses, industrial-park handoffs for the old grid and the yeshiva blocks, curbside pickups in the new developments, Toms River, Jackson, and Howell, the retirement villages, the year-round Florida lane, and the coastal storms. Local office on Avenue of the States. Free quote.',
 'h1':'Car Shipping in<br>Lakewood, <span class="accent">New Jersey</span>',
 'lede':'Open, enclosed, and expedited auto transport across Lakewood, Ocean County, and the northern Shore, planned around Route 9, the Parkway, the religious calendar, the school hours, and the storms.',
 'tel':'+17324797353','disp':'(732) 479-7353','brand':'Lakewood','keyword':'car shipping in lakewood',
 'localterms':['lakewood','route 9','route 70','route 88','parkway','exits at 88 and 91','195','turnpike','cedar bridge','new hampshire avenue','county line','cross street','prospect street','clifton avenue','madison avenue','river avenue','oak street','pine street','lake carasaljo','industrial park','independence plaza','avenue of the states','ballpark','airport','downtown','yeshiva','private way','forest avenue','yellow buses','west side','duplexes','townhouses','leisure village','clubhouse','toms river','brick','jackson','amusement park','howell','freehold','lakehurst','manchester','whiting','point pleasant','seaside','long branch','asbury park','long beach island','barrier islands','hundred forty thousand','largest outside israel','brooklyn','monsey','baltimore','chicago','private schools','hospital','online retailers','staffing','georgian court','retirement villages','florida','april','joint base','weapons station','earle','sabbath','friday afternoon','saturday night','fall holidays','passover','school hours','seven to nine','three to five','mid-morning','shore traffic','game nights','route 537','sandy','october 2012','january 2016','two feet','ida','september 2021','april 2025','wildfire','pines','nor’easter','new york','philadelphia','hartford','washington','boston','pittsburgh','charlotte','orlando','miami','boca','fly-and-ship','newark','salt','pollen','sand','convertible','minivan','bill of lading','fmcsa','winch'],
}, BODY, FAQ)
