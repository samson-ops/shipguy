import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Erie, Pennsylvania','Car shipping on the lake, halfway between Buffalo and Cleveland on 90 and at the top of 79',
 ['Car shipping in Erie runs on Interstate 90 along the south edge and Interstate 79 up from Pittsburgh. Ship Guy is a licensed auto transport broker with an office on State Street downtown.',
  'We book vetted carriers across Erie County, from the bayfront to Millcreek and Harborcreek to Edinboro. The carriers own the trucks. Ship Guy holds the license and the bond.',
  'Interstate 90 runs the Buffalo-to-Cleveland lane across the county without entering the city. Interstate 79 ends at 90 after climbing from Pittsburgh, and Interstate 86 starts at the New York line. Peach Street is Route 19, the retail strip from 90 to downtown. Route 5 runs along the lake.',
  'This page covers 90, 79, Peach Street, the bayfront, downtown, the old grids, Millcreek, and the lake towns. It also covers the insurer, the locomotive plant, the hospitals, the colleges, the lake-effect snow, and the lanes.'],
 'Erie at a glance',
 ['Most pickups happen within 1 to 3 days. Carriers running between Buffalo and Cleveland pass the city on 90 all day. The Pittsburgh trucks come up 79.',
  'Buffalo, Cleveland, Pittsburgh, and Rochester are a same-day haul. Columbus and Detroit take a day. Philadelphia, New York, and Chicago take one to two, and Florida takes three.'],
 'Tell us the township and the side of Peach Street. Downtown, the bayfront, and the old east and west side grids meet the truck at a lot. Millcreek, Harborcreek, Fairview, and the lake towns usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 90, Interstate 79, Interstate 86, Peach Street, 26th Street, Route 5, and the Bayfront Parkway',
 prose(
  L('Erie sits between two interstates and the lake. A carrier reaches every township from 90 without crossing downtown.'),
  P('Interstate 90 runs east and west across the county five miles south of the lake. The Buffalo and Cleveland carriers run it every hour. Interstate 79 comes up from Pittsburgh through Edinboro and ends at 90 on the south edge. The Bayfront Connector runs from 90 on the east side down to the bayfront. Interstate 86 begins at 90 by the New York line. It runs east through Jamestown to the Southern Tier.'),
  P('Peach Street is Route 19. It runs from the 90 interchange past the mall and the big-box strip to downtown. It is the busiest road in the county. 26th Street is Route 20, the old east-west road across the city. 12th Street and the lakefront road are Route 5. The Bayfront Parkway runs the shore from the west side to the port. State Street runs from Perry Square down to the water.'),
  P('The carriers come off 90 at Peach Street and at the Harborcreek exit. The mall lots on upper Peach are the usual meeting spot. The centers along 26th Street and the lots by the ballpark downtown work too. So do the Harborcreek centers on Buffalo Road. The lakefront lots at the park entrance work outside the summer weekends.'),
  P('Our office is on State Street downtown, a few blocks up from Perry Square and the bayfront.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the Bayfront, the West Side, the East Side, Glenwood, Millcreek, Harborcreek, Fairview, Lawrence Park, and the Lake Towns',
 prose(
  L('Erie is a lake city on a grid, with the townships spread along the shore. The truck meets the old grid at the edge.'),
  P('Downtown around Perry Square is the insurer’s campus, the arena, the ballpark, and the storefronts on State Street. The streets are a tight grid, and a seventy-five-foot trailer does not stop on them. The driver meets you at the ballpark lots or on the Bayfront Parkway. The bayfront below the bluff is the hospital, the hotels, and the marinas. The handoff happens at the Parkway lots.'),
  P('The west side along West 8th and West 26th is old neighborhoods of narrow blocks and double houses. Little Italy and Frontier are the same. The handoff moves to the centers on 26th Street. The east side along Parade and Buffalo Road is the same grid. The handoff moves to the Buffalo Road lots. Glenwood on the south side holds the university and the zoo on wider streets. The curb often works.'),
  P('Millcreek Township wraps the city on the south and west. It holds the mall, the airport, and the big subdivisions. Kearsarge, Belle Valley, and the streets off upper Peach are wide, and the driver reaches the house. Harborcreek and Wesleyville to the east are the same, with the locomotive plant in Lawrence Park between them. The subdivisions off Buffalo Road allow the curb.'),
  P('Fairview and Girard to the west sit on the lake plain with wide streets and the curb. North East to the east is the wine town among the vineyards. The handoff happens on Main Street. Edinboro south on 79 is the college town and the lake. Waterford, Union City, and Corry are the towns at the edges. All of them price the same as Erie.'),
 )))

ROUTES=[("Buffalo, NY","I-90 · ~95 mi","Same day","$160–$260"),("Cleveland, OH","I-90 · ~100 mi","Same day","$170–$280"),
 ("Pittsburgh, PA","I-79 · ~130 mi","Same day","$200–$320"),("Rochester, NY","I-90 · ~165 mi","Same day","$210–$330"),
 ("Columbus, OH","I-90/I-71 · ~250 mi","1 day","$250–$380"),("Detroit, MI","I-90/I-75 · ~275 mi","1 day","$270–$400"),
 ("Philadelphia, PA","I-79/I-80/I-476 · ~420 mi","1 day","$370–$540"),("New York, NY","I-90/I-81/I-80 · ~450 mi","1–2 days","$400–$580"),
 ("Chicago, IL","I-90 · ~450 mi","1–2 days","$400–$580"),("Orlando, FL","I-79/I-77/I-95 · ~1,130 mi","3 days","$780–$1,100")]
BODY.append(rate_table('Lanes &amp; Costs','Erie Car Shipping Lanes and Estimated Costs',
 'The lanes Erie County cars run most, with estimated open-trailer ranges. Price your own route on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*Estimated 2026 ranges from Erie for a sedan that runs, open trailer. An SUV or a pickup runs 10 to 25 percent more, and enclosed runs more than that. Tolls are inside the number when a carrier uses the Thruway or the Turnpike. Winter and the trucks free on your dates set the real quote.',
 prose(
  P('Erie prices with Buffalo and Cleveland on every lane, because it sits on the road between them. The Pittsburgh lane rides 79 straight down. The Chicago lane rides 90 the whole way, and the New York lane rides 90 and 81. The Florida lane fills with snowbirds each fall, and the Erie price follows Cleveland’s.'),
  P('A move timed to the August move-in or a plant start date ships with the busiest weeks. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Insurer, the Locomotive Plant, the Hospitals, the Colleges, the Plastics Shops, and the Snowbirds',
 prose(
  L('Erie relocates claims staff, plant engineers, nurses, and students. The insurer downtown moves more people than anyone in the county.'),
  P('The insurance company headquartered on the square is the largest employer in the city. It hires claims and software staff on start dates all year and relocates managers from its branch states. A second car usually comes along on a trailer. The documentation for a reimbursed move comes from us.'),
  P('The locomotive plant in Lawrence Park has built engines on the lake for a century. Its engineers and the suppliers in Harborcreek move in on production schedules. The plastics and tooling shops across Millcreek and the east side do the same. The two hospital systems, one on the bayfront and one on West 25th, hire traveling nurses year round. Residents arrive each June.'),
  P('The four campuses take cars each August and send them home each May. The Catholic university downtown and the college on the south side do it. So do the state campus in Harborcreek and the university in Edinboro. A parent sets up the booking. An adult over eighteen signs at a campus lot or the mall.'),
  P('Retirees leave for Florida and the Carolinas each fall and come back in May. Families moving back from Pittsburgh and Cleveland buy in Millcreek and Fairview on closing dates. The Guard units at the armory rotate staff on orders. Ship Guy is a private broker with no tie to them. PCS timing is on the <a href="military-car-shipping.html">military</a> page, and interstate detail is on the <a href="state-to-state-car-shipping.html">state-to-state</a> page.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Lake-Effect Snow, the Christmas Storm, the Park Summers, Celebrate Erie, the Tall Ships, and the Hockey Nights',
 prose(
  L('Erie runs on a lake that buries the city each winter and fills it each summer. The snow decides the schedule.'),
  P('Erie averages a hundred inches of snow, the most of any big city in the state. The lake-effect bands set up from November through March and drop a foot in an afternoon. The Christmas storm of 2017 dropped more than five feet in two days. The city stayed buried for a week. The 90 corridor closes in a squall, and the state bans trucks until it lifts. The carriers wait in Cleveland or Buffalo. A winter pickup can lose a day or two, and we tell you first.'),
  P('Summer is the opposite. The peninsula park on the lake draws millions, and the lakefront road jams every warm weekend. The handoff moves away from the park entrance. Celebrate Erie fills State Street downtown for an August weekend. The tall ships fill the bayfront every third August, and the next festival is already on the calendar. The county fair fills Wattsburg for a week in late August.'),
  P('The arena downtown fills the lots on hockey nights from September through March. The ballpark beside it fills them on game nights from April through September. A handoff near Perry Square moves to the daytime. Move-in week in late August clogs the blocks around the downtown campus and the Harborcreek campus.'),
  P('The lake takes the shore in a fall gale. The bayfront floods when the wind sets up from the west. The spring melt swells the creeks through the west side. Neither shifts more than the loading hour. The snow does the rest.'),
 )+chips(["Downtown","Perry Square","State Street","Bayfront","Bayfront Parkway","West Side","West 8th","Little Italy","Frontier","East Side","Parade Street","Buffalo Road","Glenwood","Millcreek","Peach Street","Upper Peach","Millcreek Mall","Kearsarge","Belle Valley","Harborcreek","Wesleyville","Lawrence Park","Fairview","Girard","Lake City","North East","Edinboro","Waterford","Union City","Corry","Wattsburg","Jamestown"])
 +NOTE('Serving Erie and all of Erie County, downtown block or Millcreek subdivision. Tell us the township and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Erie?',
 prose(
  L('Most Erie County cars ride an open trailer, and that is what the lane table prices.'),
  P('An enclosed trailer keeps off five months of road salt, brine, and cinders. The collectors who fill the summer cruise nights on upper Peach book one. A car leaving for Florida before the first squall often rides enclosed too.'),
  P('A commuter car or a student car rides open without a worry. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages lay out the difference.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A number, a lot on upper Peach or at the ballpark, and a signature at delivery. The start date or the first snow picks the week.'),
  P('Approve the price, and we book a carrier already running 90 or 79. The spot and the window are set the same day. The driver and you check the car together at pickup. Every existing mark is noted on the Bill of Lading. You both sign it. At delivery the car is checked against that same sheet.'),
 )+ULI([
  "Clear personal items from the cabin and the trunk",
  "About a quarter tank of fuel",
  "Each side and the odometer photographed before the truck arrives",
  "One working key for the driver, with any fault named",
  "Aftermarket alarm switched off",
  "Downtown or on the old grids, meet the truck at the ballpark or on 26th Street",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Erie Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already run the lake road between Buffalo and Cleveland. We know when a squall closes 90.'),
  P('Anyone can look up our FMCSA license and $75,000 bond on the federal register. Our office is on State Street downtown.'),
  P('One coordinator sees the move through from the first call to the last signature. The <a href="services.html">services</a> page lays out open, enclosed, and expedited transport.'),
 )))

BODY.append(office('Erie','900 State St #473','Erie, PA 16501','+18142929839','(814) 292-9839','ET',
 '900+State+St+%23473,+Erie,+PA+16501','Visit Us','Find Ship Guy in Erie',
 'Our office is on State Street downtown, a few blocks up from Perry Square and the bayfront.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3652.667313931434!2d-80.0834368!3d42.1262524!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x882d7f4767564099%3A0xf8a94036fa828fed!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793287839615!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Erie to Pittsburgh or Florida?","Pittsburgh runs two hundred to three hundred twenty dollars for a sedan. That is about one hundred thirty miles down 79. Orlando runs seven hundred eighty to eleven hundred, about eleven hundred miles down 79, 77, and 95. Buffalo and Cleveland are ninety minutes away and the lowest lanes of all. An SUV or a pickup adds 10 to 25 percent."),
 ("Can the carrier come to my street downtown or on the west side?","Usually not. Downtown is a tight grid around Perry Square. The old east and west sides are narrow blocks of double houses. The driver meets you at the ballpark lots, on the Bayfront Parkway, or on 26th Street. Millcreek, Harborcreek, Fairview, and the lake towns usually allow the curb."),
 ("What happens if a lake-effect squall hits on my pickup day?","The driver waits in Cleveland or Buffalo until 90 reopens. A band can drop a foot in an afternoon. The state bans trucks from the interstate until it lifts. The Christmas storm of 2017 buried the city for a week. A winter pickup can lose a day or two. You hear it from us before the driver does."),
 ("Do you ship cars for the insurer and the locomotive plant?","Yes, every month. The insurance company on the square hires claims and software staff on start dates all year. The locomotive plant in Lawrence Park moves engineers in on production schedules. A second car usually comes along on a trailer. The documentation for a reimbursed move comes from us."),
 ("Can you deliver on the Gannon, Mercyhurst, Behrend, or Edinboro move-in date?","Yes. The four campuses take cars in each August and send them home in May. A parent handles the booking, and someone over eighteen signs at a campus lot. The downtown campus sits inside the grid, so the handoff happens at the ballpark lots. The window moves with the date."),
 ("Can you ship a car to or from Millcreek, Harborcreek, or North East?","Yes, and all three price the same as Erie. Millcreek rides the same carriers off 90 at Peach Street, and the curb works. Harborcreek rides them off 90 at the Harborcreek exit. North East rides them along 90 to the state line, and the handoff happens on Main Street. Send the full address for a township road."),
 ("Does the summer traffic at Presque Isle affect my pickup?","Only on the lakefront. The park draws millions, and the lakefront road jams every warm weekend from Memorial Day to Labor Day. A handoff near the park entrance moves inland to upper Peach. The rest of the county never notices."),
 ("Are the tolls in my price?","Yes, where a carrier pays one. The Thruway east of the state line and the Turnpike south of Pittsburgh charge by the mile. The toll rides inside the quote. There is no separate line. Interstate 90 in Pennsylvania and 79 carry no toll."),
 ("Can you ship a car that does not run from Erie?","Yes. A carrier with a winch is booked, and the loading time is priced from the start. The mall lots on upper Peach or the Harborcreek centers give the driver level ground. Tell us whether the car rolls, steers, and brakes."),
 ("What do you need for an Erie car shipping quote?","The pickup and delivery addresses, with the township. Year, make, model. Running or not. Open or enclosed. The week around the start date or the first snow. Five answers, and the Erie number comes back the same day."),
]
BODY.append(faq_section(FAQ,'Erie FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Erie?','The form above puts a number on your lane in about two minutes. Give us the township and the week, and a carrier already on 90 takes it.','+18142929839','(814) 292-9839','Get your free Erie quote'))

build({
 'slug':'auto-transport-erie-pennsylvania',
 'title':'Car Shipping in Erie, PA — Auto Transport | Ship Guy',
 'meta':'Car shipping in Erie, PA, on the lake between Buffalo and Cleveland on 90 and at the top of 79. Insurer and locomotive plant relocations, college move-in timing for Gannon, Mercyhurst, Behrend, and Edinboro, ballpark-lot handoffs downtown, curbside pickups in Millcreek, Harborcreek, and Fairview, the lake-effect snow, the Presque Isle summers, and the tolls. Local office on State Street downtown. Free quote.',
 'h1':'Car Shipping in<br>Erie, <span class="accent">Pennsylvania</span>',
 'lede':'Open, enclosed, and expedited auto transport across Erie County, planned around 90, 79, Peach Street, the campus calendar, and a hundred inches of snow.',
 'tel':'+18142929839','disp':'(814) 292-9839','brand':'Erie','keyword':'car shipping in erie',
 'localterms':['erie','lake','buffalo','cleveland','interstate 90','interstate 79','pittsburgh','state street','downtown','erie county','bayfront','millcreek','harborcreek','edinboro','interstate 86','new york line','peach street','route 19','retail strip','12th street','route 5','bayfront parkway','east side','west side','lake towns','insurer','locomotive plant','hospitals','colleges','lake-effect snow','rochester','columbus','detroit','philadelphia','new york','chicago','florida','fairview','bayfront connector','jamestown','southern tier','mall','big-box','26th street','route 20','perry square','ballpark','buffalo road','park entrance','arena','bluff','hotels','marinas','west 8th','double houses','little italy','frontier','parade','glenwood','university','zoo','airport','kearsarge','belle valley','wesleyville','lawrence park','girard','north east','wine','vineyards','main street','waterford','union city','corry','thruway','turnpike','snowbirds','move-in','claims','software','branch states','suppliers','plastics','tooling','west 25th','traveling nurses','residents','catholic university','state campus','carolinas','guard','armory','hundred inches','squall','christmas storm','2017','five feet','bans trucks','peninsula park','millions','celebrate erie','tall ships','third august','county fair','wattsburg','hockey nights','game nights','gale','spring melt','creeks','brine','cinders','cruise nights','bill of lading','fmcsa','presque isle','memorial day','labor day','gannon','mercyhurst','behrend','lake city'],
}, BODY, FAQ)
