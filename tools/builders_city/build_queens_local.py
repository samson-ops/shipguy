import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Queens, New York','Car shipping for the borough the carriers reach by expressway, not parkway',
 ['Car shipping in Queens is a question of which road the truck is allowed on. Ship Guy is a licensed auto transport broker with an office on Queens Boulevard in Forest Hills.',
  'We book vetted carriers for every neighborhood from Astoria to the Rockaways. We do not own the trucks.',
  'The Grand Central, the Belt, and the Cross Island are parkways, and trucks are banned from all three. A seventy-five-foot carrier comes in on the Long Island Expressway, the Van Wyck, or the BQE. It meets you a few blocks off the exit.',
  'This page covers the expressways and the parkways, the meeting spots by neighborhood, and the two airports. It also covers the Florida lane, the co-op and alternate-side rules, the US Open week, and the lanes.'],
 'Queens at a glance',
 ['Most pickups happen within 1 to 3 days. The meeting spot is a wide street or a lot near an expressway exit.',
  'Philadelphia and Boston are same-day lanes. Washington takes a day. Florida runs three to four, and Texas and California run five to seven.'],
 'Tell us the neighborhood. Forest Hills, Jackson Heights, and Astoria need a meeting spot. Bayside, Douglaston, and Howard Beach often allow the curb.'))

BODY.append(sec('The Roads','The Expressways the Truck Can Use, and the Parkways It Cannot',
 prose(
  L('Half the fast roads in Queens were built with low stone bridges on purpose. A car carrier cannot fit under them.'),
  P('The Grand Central Parkway, the Belt Parkway, the Cross Island, and the Jackie Robinson all ban commercial vehicles. That rules out the roads along both airports and the whole south shore.'),
  P('Carriers use the Long Island Expressway across the middle of the borough. The Van Wyck carries them south toward Kennedy Airport, and the Brooklyn-Queens Expressway carries them west. The Clearview and the Whitestone Expressway reach the north shore.'),
  P('The Throgs Neck and the Whitestone bridges connect to the Bronx and New England. The Queens-Midtown Tunnel and the Queensboro Bridge connect to Manhattan. The Verrazzano connects through Brooklyn to New Jersey.'),
  P('Every crossing charges a toll, and the carrier pays it. Tolls and any congestion fee in effect are built into the quote. There is no separate line.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Where the Handoff Happens, Neighborhood by Neighborhood',
 prose(
  L('Queens has one-family blocks in Bayside and apartment towers in Long Island City. The handoff works differently in each.'),
  P('Forest Hills, Rego Park, and Kew Gardens are co-op and garden-apartment neighborhoods with alternate-side parking on every block. The driver meets you on Queens Boulevard, Yellowstone, or a lot near the Expressway. Our office sits on Queens Boulevard in the middle of it.'),
  P('Jackson Heights, Elmhurst, Corona, and Woodside are dense, and a trailer cannot stop on the side streets. The handoff happens on Northern Boulevard, Roosevelt Avenue, or near the Expressway exits.'),
  P('Astoria and Long Island City run on towers and garages. The industrial blocks near the Queensboro Bridge have room for a trailer. Most of those pickups happen there.'),
  P('Bayside, Douglaston, Little Neck, Whitestone, and Fresh Meadows are one-family streets with driveways. The truck often reaches the curb on the wider blocks. Howard Beach, Ozone Park, and Richmond Hill are the same on the south side.'),
  P('The Rockaways sit across the Cross Bay Bridge. The carrier meets you in Howard Beach or on Beach Channel Drive, not on the peninsula.'),
 )))

ROUTES=[("Philadelphia, PA","I-95 · ~100 mi","Same day","$190–$300"),("Boston, MA","I-95 · ~215 mi","Same day","$240–$360"),
 ("Washington, DC","I-95 · ~235 mi","1 day","$250–$370"),("Buffalo, NY","I-87/I-90 · ~400 mi","1 day","$380–$540"),
 ("Charlotte, NC","I-95/I-85 · ~640 mi","2 days","$480–$690"),("Chicago, IL","I-80 · ~800 mi","2 days","$570–$830"),
 ("Atlanta, GA","I-95/I-85 · ~880 mi","2–3 days","$620–$890"),("Orlando, FL","I-95 · ~1,090 mi","3 days","$770–$1,090"),
 ("Miami, FL","I-95 · ~1,290 mi","3–4 days","$810–$1,160"),("Los Angeles, CA","I-80/I-40 · ~2,800 mi","7–9 days","$1,350–$1,800")]
BODY.append(rate_table('Lanes &amp; Costs','Queens Car Shipping Lanes and Estimated Costs',
 'The lanes Queens households ask about most, with estimated open-transport ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates, running sedan, open trailer. SUVs and pickups add roughly 10 to 25 percent, and enclosed adds more. Bridge and tunnel tolls are included. Season and carrier availability on your dates set the real quote.',
 prose(
  P('Interstate 95 south is the busiest lane out of Queens. Florida moves so many borough cars that the price holds even in season. Boston and Philadelphia run the same day in the other directions.'),
  P('A pickup inside the borough is priced a little above one at the city line. The truck loses an hour in Queens traffic, and the quote reflects it. The <a href="car-shipping-cost.html">cost guide</a> explains the rest of the number.'),
 ), alt=True))

BODY.append(sec('The Florida Lane','October Out, April Back, and the Auto Train Question',
 prose(
  L('Queens sends more cars to Florida each fall than most whole states. Nearly all of them ride a trailer.'),
  P('From October through December, Forest Hills and Bayside send their cars to Boca Raton and West Palm. The cars come back between April and June, all of it on Interstate 95.'),
  P('Some owners drive to Virginia and put the car on the train. Most find that a trailer from the borough costs about the same and skips the drive. Two to three weeks of notice keeps the price steady in season. Our <a href="snowbird-car-shipping.html">snowbird</a> page has the planning tips.'),
  P('Spring is the easier direction, because carriers come north empty and want the load.'),
 )))

BODY.append(sec('The Airports &amp; Who Ships Here','Kennedy, LaGuardia, the Hospitals, and the Universities',
 prose(
  L('Queens relocates people through two airports, three hospital systems, and a university on each side of the borough.'),
  P('Households flying in through Kennedy from overseas often ship a car up from Florida. Others bring one in from family in another state. The pickup near the airport happens in Jamaica or on Rockaway Boulevard, never on the airport roads.'),
  P('The hospitals in Flushing, Jamaica, and New Hyde Park bring in residents every summer. The handoff happens on a main road near the hospital rather than in its garage.'),
  P('The university in Jamaica and Queens College in Flushing bring cars in each August. They send them home each May. An adult signs for a student car, and the driver meets you at a lot near the Expressway.'),
  P('Fort Totten in Bayside and Fort Hamilton across the Verrazzano rotate families on orders. The second vehicle usually rides with us, and the <a href="military-car-shipping.html">military</a> page covers the planning. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers a longer move.'),
 ), alt=True))

BODY.append(sec('The Calendar','The US Open, Citi Field, and Alternate-Side Parking',
 prose(
  L('Queens runs on a calendar of events and parking rules, and the carrier works around both.'),
  P('The US Open fills Flushing Meadows for two weeks around Labor Day. The Van Wyck and the Grand Central crawl the whole time. Mets home games add the same traffic on summer nights. We schedule Flushing and Corona pickups around both.'),
  P('Alternate-side parking rules decide which side of the street is free on which morning. A meeting spot on a wide road avoids the ticket. Snow suspends the rules and closes the side streets for a day or two.'),
  P('Nor’easters hit a few times each winter, and the carriers wait on the Expressway until the plows pass. Summer brings heat on the bridges and the occasional tropical storm. The low ground in Howard Beach and the Rockaways floods.'),
 )+chips(["Astoria","Long Island City","Sunnyside","Woodside","Jackson Heights","Elmhurst","Corona","Flushing","Whitestone","College Point","Bayside","Douglaston","Little Neck","Fresh Meadows","Forest Hills","Rego Park","Kew Gardens","Richmond Hill","Jamaica","Hollis","Queens Village","Ozone Park","Howard Beach","Ridgewood","Glendale","Middle Village","Maspeth","Far Rockaway","Rockaway Beach","Great Neck"])
 +NOTE('Serving all of Queens plus the Nassau County line. Tell us the neighborhood and whether the car lives in a garage.')))

BODY.append(sec('Your Options','Open or Enclosed in Queens?',
 prose(
  L('Open transport carries most of Queens, and the Florida lane runs on it.'),
  P('Enclosed transport keeps a car covered against road salt, grit, and attention. The collector garages in Douglaston and Jamaica Estates book enclosed trailers. So do many of the cars headed to Palm Beach.'),
  P('A commuter car rides open without trouble. Our <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages lay out each option.'),
 )))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a short drive to the meeting spot, and a delivery. The parkways decide the spot.'),
  P('Once you approve the price, a carrier already running Interstate 95 takes the booking. We name the meeting spot before the driver is dispatched. At the spot, the driver records the car’s condition on a Bill of Lading. You both sign it.'),
 )+ULI([
  "Remove personal belongings",
  "Keep about a quarter tank of fuel",
  "Photograph the car before you leave the garage or the block",
  "Provide a working key and disclose mechanical issues",
  "Disable aftermarket alarms",
  "Check the alternate-side schedule so the car is not ticketed on pickup morning",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> guides take it step by step.')), alt=True))

BODY.append(sec('Why Ship Guy','Why Queens Drivers Choose Ship Guy',
 prose(
  L('We know which roads ban the truck. We name the meeting spot before you ever wait on a corner.'),
  P('Active FMCSA brokerage authority and a $75,000 surety bond stand behind every booking we make. Our office is on Queens Boulevard in Forest Hills.'),
  P('One coordinator carries your shipment from quote to delivery and can book open, enclosed, or expedited transport. The <a href="services.html">services</a> page shows the full lineup.'),
 )))

BODY.append(office('Queens','118-35 Queens Blvd #488','Forest Hills, NY 11375','+19295604543','(929) 560-4543','ET',
 '118-35+Queens+Blvd+%23488,+Forest+Hills,+NY+11375','Visit Us','Find Ship Guy in Queens',
 'Our office is on Queens Boulevard in Forest Hills, a block from the Seventy-First Avenue station.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5115.058942733726!2d-73.8311739!3d40.7148089!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c261b7c2dad0e5%3A0xdf86446d15cb83cb!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792023125428!5m2!1sen!2sus'))

FAQ=[
 ("Can the carrier come to my block in Queens?","On a wide one-family street in Bayside, Douglaston, or Howard Beach, often yes. In Forest Hills, Jackson Heights, Astoria, or Flushing, no. The side streets are too narrow to stop a trailer, and the parkways ban it. The driver meets you on a main road or at a lot near an expressway exit."),
 ("How much does it cost to ship a car from Queens to Florida?","Figure seven hundred seventy to one thousand ninety dollars for a sedan to Orlando. Miami adds a little. The trip is about eleven hundred miles down Interstate 95. November southbound costs more than July. SUVs and pickups add 10 to 25 percent."),
 ("Are the bridge and tunnel tolls added to my price?","No. The carrier pays the Throgs Neck, the Whitestone, the Verrazzano, and any congestion fee in effect. The quote you approve already has all of it inside."),
 ("Is it cheaper to meet the truck in New Jersey or on Long Island?","Usually a little. A pickup inside the borough costs the carrier an hour of traffic, and the quote reflects it. A handoff near the Nassau line or across the Verrazzano trims that. We will quote both if you want to compare."),
 ("Does the US Open or a Mets game affect my pickup?","Around Flushing Meadows, yes. The Van Wyck and the Grand Central crawl for the two weeks of the tournament. Game nights do the same. We schedule Flushing, Corona, and Willets Point pickups on other days. The rest of the borough runs normally."),
 ("Can you pick up near Kennedy or LaGuardia?","Yes, but not on the airport roads. For Kennedy, the handoff happens in Jamaica or on Rockaway Boulevard. For LaGuardia, it happens in East Elmhurst or on Astoria Boulevard. Tell us your flight time and we will plan around it."),
 ("My car is in a garage in Forest Hills. How does the handoff work?","You or the garage staff bring the car out on pickup day. You drive it a few minutes to the meeting spot. Give the garage notice so the car is not blocked in. At delivery, the reverse happens. An adult signs the Bill of Lading at the spot."),
 ("Can you ship a car for a college student in Queens?","Yes. Student cars arrive each August and leave each May. Campus streets are tight, so the driver meets you at a lot near the Expressway. An adult signs for the car at pickup, and a parent can sign at the far end."),
 ("Can you ship a car that does not run from Queens?","Yes. A carrier with a winch handles a car that will not start. The extra loading time is part of the price. The meeting spot has to be flat and wide. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Queens car shipping quote?","The pickup and delivery addresses, with the neighborhood. Whether the car lives in a garage or on the street. The year, make, and model. Whether it runs. Open or enclosed, and your dates. That is everything an accurate Queens quote needs."),
]
BODY.append(faq_section(FAQ,'Queens FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Queens?','Two minutes on the form above gets you a price. Tell us the neighborhood and your dates. We name the meeting spot before the truck is dispatched.','+19295604543','(929) 560-4543','Get your free Queens quote'))

build({
 'slug':'auto-transport-queens-new-york',
 'title':'Car Shipping in Queens, NY — Auto Transport | Ship Guy',
 'meta':'Car shipping in Queens, NY by expressway, not parkway. Meeting spots by neighborhood, Forest Hills and Jackson Heights handoffs, Kennedy and LaGuardia pickups, the Florida snowbird lane, US Open timing, tolls built in. Local office on Queens Boulevard. Free quote.',
 'h1':'Car Shipping in<br>Queens, <span class="accent">New York</span>',
 'lede':'Open, enclosed, and expedited auto transport across the borough, planned around the parkways, the airports, and the Florida season.',
 'tel':'+19295604543','disp':'(929) 560-4543','brand':'Queens','keyword':'car shipping in queens',
 'localterms':['queens','long island expressway','van wyck','brooklyn-queens expressway','clearview','whitestone','grand central parkway','belt parkway','cross island','jackie robinson','throgs neck','queensboro','queens-midtown tunnel','verrazzano','forest hills','rego park','kew gardens','queens boulevard','jackson heights','elmhurst','corona','woodside','astoria','long island city','bayside','douglaston','little neck','whitestone','fresh meadows','howard beach','ozone park','richmond hill','rockaway','flushing','jamaica','kennedy','laguardia','hospitals','college','queens college','fort totten','fort hamilton','florida','boca raton','snowbird','us open','citi field','mets','alternate-side','nor','philadelphia','boston','washington','buffalo'],
}, BODY, FAQ)
