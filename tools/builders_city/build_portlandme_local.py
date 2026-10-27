import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("2–4 Days","Honest Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Portland, Maine','Car shipping in the carrier hub of Maine, where the Turnpike meets 295 and the coast begins',
 ['Car shipping in Portland runs off the Turnpike and Interstate 295, the two roads every Maine carrier uses. Ship Guy is a licensed auto transport broker with an office on Congress Street downtown.',
  'We book vetted carriers across Cumberland County, from Scarborough to Freeport and inland to Gorham and Windham. The trucks belong to the carriers.',
  'Interstate 295 runs through the city along the peninsula and Back Cove. The Turnpike carries Interstate 95 past the west side and the mall. Route 1 follows the coast through South Portland and Falmouth. Forest Avenue, Brighton Avenue, and Washington Avenue carry the rest.',
  'This page covers 295, the Turnpike, the peninsula, the neighborhoods beyond it, South Portland, and the coast. It also covers the medical center, the insurers, the shipyard, cruise season, the January tides, and the lanes.'],
 'Portland at a glance',
 ['Most pickups happen within 2 to 4 days. Portland is where the carriers coming up from Boston turn around. A pickup here joins a truck already making the run.',
  'Boston and Manchester are a same-day haul. Hartford, Albany, and New York take a day. Philadelphia and Washington take two. Florida takes four, and the West Coast takes six to eight.'],
 'Tell us the side of 295. The peninsula needs a meeting spot. Deering, South Portland, and the suburbs usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 295, the Turnpike, Route 1, Forest Avenue, and the Bridges',
 prose(
  L('Portland is where the Maine carrier run begins and ends. The trucks know the city better than any other in the state.'),
  P('Interstate 295 runs from the Turnpike at Scarborough through the city to Falmouth and on to Brunswick. The exits at Congress, Forest, Franklin, and Washington serve the peninsula. The carriers come off at Franklin for the Old Port and at Forest for Deering. Tukey’s Bridge carries 295 over Back Cove to Falmouth.'),
  P('The Turnpike carries Interstate 95 past the west side of the city. Its exits serve the mall, Westbrook, and Falmouth. Its tolls are built into every quote. Route 1 is the coast road, from Kittery through South Portland and Falmouth to Freeport and Brunswick. In summer it crawls from Kennebunk north.'),
  P('Forest Avenue is Route 302, the road inland to Sebago and the mountains. Brighton Avenue and Congress Street run west to the Jetport. Washington Avenue runs the east side. Marginal Way is the flat road along Bayside where the carriers meet the peninsula. Commercial Street runs the waterfront. The Casco Bay Bridge crosses to South Portland and opens for ships.'),
  P('The carriers come off 295 at Franklin and Forest, and off the Turnpike at the mall. Marginal Way, the mall in South Portland, and the Jetport have the usual meeting lots. The Turnpike is the only toll. The bridges and 295 are free.'),
  P('Our office is on Congress Street downtown, a block from Monument Square and City Hall.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','The Peninsula, Deering, Stroudwater, South Portland, Westbrook, Falmouth, and the Coast',
 prose(
  L('Portland is a peninsula of narrow brick streets with a ring of wider neighborhoods around it. The truck stops at the edge.'),
  P('The peninsula is the Old Port, the Arts District, the West End, and Munjoy Hill. The streets are narrow, cobbled in places, and full. A trailer cannot enter the Old Port or climb the hill. The driver meets you on Marginal Way, at the Franklin Street lots, or on the Eastern Promenade. Bayside along Marginal Way is flat and open, and the handoff works there any day.'),
  P('Deering, Woodfords Corner, and Rosemont off Forest Avenue are the streetcar neighborhoods, with wider streets and old trees. The curb works on most blocks. North Deering, Riverton, and Stroudwater by the Jetport are postwar grids with wide streets. The truck reaches the curb.'),
  P('South Portland across the harbor has the mall, the oil terminals, and grids from Knightville to Willard Beach. The curb works, and the mall lot works for the rest. Westbrook along the river has the mill and the animal-health campus. Scarborough, Gorham, and Windham are the growth suburbs, and the subdivisions allow the curb.'),
  P('Falmouth, Cumberland, and Yarmouth up the coast are old towns. The village streets are narrow and the roads between them wide. The driver meets you on Route 1 or at a lot in the village. Cape Elizabeth has the lighthouses and narrow shore roads. Freeport has the outlets and the outfitter. Brunswick has the college and the old air station. All of them price the same as Portland.'),
 )))

ROUTES=[("Boston, MA","I-95 · ~110 mi","Same day","$170–$280"),("Manchester, NH","I-95/US-4 · ~95 mi","Same day","$220–$340"),
 ("Hartford, CT","I-95/I-84 · ~200 mi","1 day","$260–$390"),("Albany, NY","I-95/I-90 · ~260 mi","1 day","$270–$400"),
 ("New York, NY","I-95 · ~320 mi","1 day","$340–$490"),("Philadelphia, PA","I-95 · ~410 mi","1–2 days","$400–$570"),
 ("Washington, DC","I-95 · ~550 mi","2 days","$460–$660"),("Charlotte, NC","I-95/I-85 · ~900 mi","3 days","$700–$980"),
 ("Chicago, IL","I-90 · ~1,050 mi","3 days","$750–$1,050"),("Orlando, FL","I-95 · ~1,400 mi","4 days","$900–$1,250")]
BODY.append(rate_table('Lanes &amp; Costs','Portland Car Shipping Lanes and Estimated Costs',
 'The lanes southern Maine cars take most, with estimated open-trailer ranges. Your exact route prices on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates priced from Portland, Maine, open trailer, sedan that runs. SUVs and pickups land 10 to 25 percent higher, enclosed higher again. Turnpike tolls are inside the number. Season and carrier availability on your dates set the real quote.',
 prose(
  P('Portland prices under the rest of Maine. The carriers come this far on every run and no farther on most. The Boston lane runs daily. The New York and Philadelphia lanes run most days. The Florida lane follows the snowbird calendar, higher in October and lower in April.'),
  P('Manchester prices over Boston despite the shorter miles, because fewer trucks make that run. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Medical Center, the Insurers, the Shipyard, the Campuses, and the Summer People',
 prose(
  L('Portland relocates physicians, insurance staff, shipbuilders, and students. The medical center moves more people than anyone in the state.'),
  P('The medical center on the west side of the peninsula is the largest employer in Maine. Nurses arrive on contracts all year and residents every June. Physicians come with a closing date and a second car. The second hospital on the west side hires the same way. We supply the paperwork a reimbursed move needs.'),
  P('The insurer on Bayside and the payments company on the waterfront move analysts and managers in every month. The animal-health company in Westbrook and the outfitter in Freeport relocate staff on their own calendars. The shipyard in Bath moves welders and engineers in on contract cycles, and the car follows the job.'),
  P('The university on Forest Avenue and in Gorham brings cars in each September. The art college downtown does the same. The college in Brunswick runs the same calendar. A parent ships the car, and an adult signs at a campus lot. The tech institute on the waterfront adds graduate students each fall.'),
  P('Summer residents ship cars up in June and home in September, and the coast runs on that clock. Retirees leave for Florida each October and come back in April. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side. Ship Guy is a private broker with no military connection. The <a href="military-car-shipping.html">military</a> page covers the shipyard and the Guard.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Cruise Season, Summer on Route 1, the Nor’easters, Mud Season, and the January Tides',
 prose(
  L('Portland runs on a ten-week summer, a fall of cruise ships, and a winter off the water.'),
  P('Cruise ships tie up at the Ocean Gateway from May through October. The big weeks are September and October. On a ship day, the Old Port fills with passengers by nine. A handoff on the peninsula moves to Marginal Way or to the morning. Leaf season fills Route 1 the same weeks.'),
  P('Summer fills the coast from late June through Labor Day. Route 1 crawls from Kennebunk to Freeport, and the ferry terminal on Commercial Street backs up every weekend. The ballpark on Park Avenue fills its lots on game nights. The road race in Cape Elizabeth closes Route 77 on a Saturday in August. The marathon closes Back Cove on an October Sunday.'),
  P('Nor’easters are the winter problem. The February 2013 storm dropped more than thirty inches on the city. The carriers parked in Kittery for two days. Sixty inches of snow falls in a normal winter, and the Turnpike shuts a few times a season. A pickup in a storm week can lose a day or two, and we call before it does. Mud season posts the inland back roads from March into May. The driver meets you on a paved state route.'),
  P('The January 2024 storms sent the tide over Commercial Street and the working waterfront. It was the highest water the city had seen. The low streets by the harbor flood on a storm tide now. A pickup there moves up the hill for a day. Fog sits on the harbor in summer, and the bridge opens for ships. Neither changes a schedule.'),
 )+chips(["Old Port","Arts District","Congress Street","Monument Square","West End","Munjoy Hill","Eastern Promenade","Bayside","Marginal Way","Parkside","Deering","Woodfords Corner","Rosemont","North Deering","Riverton","Stroudwater","Jetport","Libbytown","South Portland","Knightville","Willard Beach","Maine Mall","Cape Elizabeth","Westbrook","Scarborough","Gorham","Windham","Falmouth","Cumberland","Yarmouth","Freeport","Brunswick"])
 +NOTE('Serving Portland, South Portland, and all of Cumberland County, peninsula block or suburb. Tell us the side of 295 and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Portland?',
 prose(
  L('Open trailers carry most of the cars that leave Cumberland County, and the table above assumes one.'),
  P('An enclosed trailer keeps a car out of the salt, the slush, and the sea air. Summer residents shipping a collector car to the coast book one. Snowbirds with a new car book one for the Florida run.'),
  P('The commuter car and the lobster truck go open and come off the trailer as they went on. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages weigh the two.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A number, a meeting spot on Marginal Way or at the mall, and a car at delivery. The next truck making the Maine run sets the week.'),
  P('Approve the number, and we match the car to a carrier already headed up 95 from Boston. The lot and the window reach you as soon as the truck is set. The driver walks the car with you at pickup and writes its condition on a Bill of Lading. Both of you sign, and the sheet is compared at delivery.'),
 )+ULI([
  "Take everything personal out of the cabin and the trunk",
  "Keep the fuel near a quarter tank",
  "Photograph every side of the car and the mileage before the handoff",
  "Give the driver one working key and mention any mechanical problem",
  "Disarm any aftermarket alarm",
  "On the peninsula, meet the truck on Marginal Way or at the Franklin Street lots",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Portland Drivers Choose Ship Guy',
 prose(
  L('We put your car on the carriers already making the Maine run. We tell you the real window, not a hopeful one.'),
  P('Ship Guy holds active FMCSA brokerage authority and a $75,000 surety bond. Both are in the federal register. Our office is on Congress Street downtown.'),
  P('The coordinator who quotes the move is the one who closes it. Open, enclosed, and expedited transport are on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Portland','411 Congress St #355A','Portland, ME 04101','+12073604574','(207) 360-4574','ET',
 '411+Congress+St+%23355A,+Portland,+ME+04101','Visit Us','Find Ship Guy in Portland',
 'Our office is on Congress Street downtown, a block from Monument Square and City Hall.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4438.730004900504!2d-70.2576303!3d43.658778899999994!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4cb29d3297a58f15%3A0xa028f097ca7346cc!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793025068059!5m2!1sen!2sus'))

FAQ=[
 ("Why does a Portland pickup take two to four days?","Because Maine is a small market, and the carriers come up 95 from Boston and beyond. Portland is where most of them turn around. A pickup here joins a truck already making the run. That is two to four days in a normal week. A flexible date range puts you on the next truck. Rigid dates work on the Boston lane but narrow the pool."),
 ("How much does it cost to ship a car from Portland to Boston or Florida?","A sedan to Boston runs one hundred seventy to two hundred eighty dollars. That covers about one hundred ten miles down 95. Orlando runs nine hundred to twelve hundred fifty, about fourteen hundred miles the same way. Season counts more than distance on the Florida lane. A southbound car in November costs more than in July. An SUV or pickup adds 10 to 25 percent."),
 ("Can the carrier come to my street on the peninsula?","No. The Old Port, the West End, and Munjoy Hill are narrow streets, cobbled in places. A trailer cannot enter them. The driver meets you on Marginal Way, at the Franklin Street lots, or on the Eastern Promenade. Deering, South Portland, and the suburbs usually allow the curb."),
 ("Do you ship cars for people relocating to the medical center or the insurers?","Yes, all year. The medical center brings in nurses, residents, and physicians every month. The insurer on Bayside and the payments company on the waterfront move staff from every state. Many ship a second car behind the move. The handoff works on Marginal Way or at the mall. We provide the paperwork a reimbursed move needs."),
 ("Can you ship a summer resident’s car up in June and home in September?","Yes, and the coast runs on that clock. Cars come up from New York, Connecticut, and Florida in June and go home after Labor Day. The driver meets you on Route 1 or in the nearest town. The shore roads are too narrow for a trailer. Book a few weeks ahead, because the June and September trucks fill early."),
 ("Can you ship a car to or from South Portland, Falmouth, or Freeport?","Yes, and all three price the same as Portland. South Portland rides the same carriers off the Turnpike at the mall. Falmouth and Freeport ride them off 295 to the north. A lot on Route 1 or at the outlets works for a handoff. Send the full address for a new subdivision in Scarborough or Gorham."),
 ("What happens if a nor’easter hits on my pickup day?","The carriers park in Kittery or Portsmouth until the Turnpike reopens. A winter pickup can slip a day or two. You hear from us before it does. A storm tide floods the low streets by the harbor now. A pickup there moves up the hill. Mud season posts the inland back roads in spring. The driver then meets you on a paved state route."),
 ("Can you ship a car that does not run from Portland?","Yes. A carrier with a winch is sent, and the loading time is in the quote from the start. The lots on Marginal Way or the mall lot in South Portland give the driver room to winch. Say whether it rolls, whether it steers, and whether the brakes hold."),
 ("Can you time delivery to a student move at the university or Bowdoin?","Yes. The campuses in Portland and Gorham take cars in each September and send them home in May. The college in Brunswick runs the same calendar. A parent books, and an adult signs at a campus lot. Book a couple of weeks ahead, because the September trucks fill fast."),
 ("What do you need for a Portland car shipping quote?","Both addresses, with the side of 295 or the town here. Year, make, and model. Whether it runs. Open or enclosed. A date range rather than a single day, which matters more in Maine than anywhere. That is a complete Portland request, and the number comes back the same day."),
]
BODY.append(faq_section(FAQ,'Portland FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Portland?','Two minutes on the form above prices your lane. Send the side of 295 and a date range. The next carrier making the Maine run takes it.','+12073604574','(207) 360-4574','Get your free Portland quote'))

build({
 'slug':'auto-transport-portland-maine',
 'title':'Car Shipping in Portland, ME — Auto Transport | Ship Guy',
 'meta':'Car shipping in Portland, ME, the carrier hub of Maine where the Turnpike meets 295. Honest two-to-four-day pickups, medical-center and insurer relocations, peninsula meeting spots on Marginal Way, Deering and South Portland curbside pickups, summer residents and snowbirds, cruise season, the nor’easters, and the January tides. Local office on Congress Street. Free quote.',
 'h1':'Car Shipping in<br>Portland, <span class="accent">Maine</span>',
 'lede':'Open, enclosed, and expedited auto transport across Cumberland County, planned around 295, the Turnpike, the summer clock, and the winter.',
 'tel':'+12073604574','disp':'(207) 360-4574','brand':'Portland','keyword':'car shipping in portland',
 'localterms':['portland','maine','carrier hub','interstate 295','turnpike','interstate 95','route 1','forest avenue','route 302','brighton','congress street','washington avenue','marginal way','commercial street','franklin street','tukey’s bridge','back cove','casco bay bridge','jetport','peninsula','old port','arts district','west end','munjoy hill','eastern promenade','bayside','monument square','city hall','deering','woodfords corner','rosemont','north deering','riverton','stroudwater','south portland','knightville','willard beach','mall','oil terminals','westbrook','mill','scarborough','gorham','windham','falmouth','cumberland','yarmouth','cape elizabeth','lighthouses','freeport','outfitter','brunswick','college','air station','medical center','nurses','residents','insurer','payments company','animal-health','shipyard','bath','university','art college','tech institute','summer residents','retirees','snowbirds','cruise ships','ocean gateway','leaf season','ferry','ballpark','road race','marathon','nor’easters','february 2013','kittery','snow','mud season','posted','january 2024','tide','fog','boston','manchester','hartford','albany','new york','philadelphia','washington','charlotte','chicago','orlando','kennebunk'],
}, BODY, FAQ)
