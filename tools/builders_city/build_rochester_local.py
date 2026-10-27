import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Rochester, New York','Car shipping between the lake and the Thruway, on the university calendar',
 ['Car shipping in Rochester runs on the Thruway and the hospital calendar. Ship Guy is a licensed auto transport broker with an office on Rutter Street on the west side.',
  'We book vetted carriers across Monroe County and the canal towns, from Greece to Victor. We do not own the trucks.',
  'Interstate 90 passes south of the city as the Thruway, and Interstate 490 brings the traffic through downtown. Route 390 runs north to the lake and south to the Thruway. Route 590 and Route 104 carry the east side.',
  'This page covers the expressways and the Thruway exits, the neighborhoods, the university, and the hospitals. It also covers the lake-effect winter, the festival calendar, the Florida lane, and the lanes.'],
 'Rochester at a glance',
 ['Most pickups happen within 1 to 3 days, with a lake-effect week adding one. The Thruway brings carriers past the city every day.',
  'Buffalo and Syracuse are same-day lanes. Cleveland, Albany, and New York City take a day. Chicago needs one to two, and Florida needs three to four.'],
 'Tell us the neighborhood. Park Avenue, the South Wedge, and the village of Pittsford need a meeting spot. Greece, Henrietta, and Webster usually allow the curb.'))

BODY.append(sec('The Roads','The Thruway, Interstate 490, and the 390 and 590 Loops',
 prose(
  L('Rochester is an easy city for a carrier once it leaves the Thruway. The expressways reach every suburb.'),
  P('Interstate 90 runs along the south edge of the county, with exits at Le Roy, Rochester, and Victor. Interstate 490 leaves the Thruway at both ends and carries the traffic through downtown. The Thruway toll is paid by the mile.'),
  P('Route 390 runs from the Thruway north through Henrietta, Gates, and Greece to the lake at Charlotte. Route 590 does the same on the east side through Brighton and Irondequoit. Route 104 crosses the north side to Webster, and Route 531 reaches Spencerport.'),
  P('The Lake Ontario State Parkway bans trucks. A carrier reaches the lakeshore on Lake Avenue or Route 390. Everything else is open to a seventy-five-foot rig.'),
  P('Our office is on Rutter Street off Lyell Avenue, minutes from Route 390 and the Interstate 490 interchange. The Thruway toll is built into every quote.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Park Avenue, the South Wedge, the East Side, and the Canal Towns',
 prose(
  L('Rochester kept its nineteenth-century streets, and the prettiest ones are the hardest for a trailer.'),
  P('Park Avenue, the East End, and the Neighborhood of the Arts have narrow streets. Cars line both curbs. The driver meets you on East Avenue, Monroe Avenue, or a lot near Interstate 490. The South Wedge, Swillburg, and Corn Hill are the same.'),
  P('The Nineteenth Ward, Maplewood, and the Lyell-Otis blocks on the west side are tighter near the river. They open up toward the suburbs. The handoff happens on Lyell Avenue, Lake Avenue, or Mount Read Boulevard.'),
  P('Brighton, Pittsford, and Penfield are wide outside the villages. The village of Pittsford on the canal is tight. The driver meets you on Monroe Avenue or at the plaza. Greece, Gates, Chili, and Henrietta are open grids where the truck reaches the curb.'),
  P('Webster, Irondequoit, Fairport, and Perinton sit on the east side off Route 104 and Route 590. Victor, Spencerport, and Brockport are canal and Thruway towns that schedule easily.'),
 )))

ROUTES=[("Buffalo, NY","I-90 · ~75 mi","Same day","$160–$260"),("Syracuse, NY","I-90 · ~90 mi","Same day","$170–$270"),
 ("Albany, NY","I-90 · ~225 mi","1 day","$240–$360"),("Cleveland, OH","I-90 · ~260 mi","1 day","$250–$380"),
 ("Pittsburgh, PA","I-90/I-79 · ~290 mi","1 day","$270–$400"),("Philadelphia, PA","I-390/I-81/I-476 · ~330 mi","1 day","$350–$500"),
 ("New York, NY","I-90/I-87 · ~335 mi","1 day","$360–$520"),("Boston, MA","I-90 · ~390 mi","1 day","$380–$540"),
 ("Chicago, IL","I-90 · ~600 mi","1–2 days","$480–$680"),("Fort Myers, FL","I-390/I-79/I-95 · ~1,350 mi","3–4 days","$900–$1,300")]
BODY.append(rate_table('Lanes &amp; Costs','Rochester Car Shipping Lanes and Estimated Costs',
 'The routes Rochester families and employers price most often, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates, running sedan, open trailer. SUVs and pickups add roughly 10 to 25 percent, and enclosed adds more. The Thruway toll is included. A snowy week and carrier availability on your dates set the real quote.',
 prose(
  P('Buffalo and Syracuse are the quick lanes, an hour and a half in either direction on the Thruway. Cleveland and Chicago ride Interstate 90 west, and Boston rides it east.'),
  P('New York City is a day down the Thruway and Interstate 87. The downstate handoff happens at a meeting spot rather than a doorstep. The <a href="car-shipping-cost.html">cost guide</a> explains the rest of the number.'),
 ), alt=True))

BODY.append(sec('The University &amp; the Hospitals','Match Day, Move-In, and the Employers',
 prose(
  L('Rochester relocates people on the hospital calendar first and the corporate calendar second.'),
  P('The university and its medical center are the largest employer in the region. Residents and fellows arrive every June and July, and the undergraduates arrive each August. The handoff happens on Elmwood Avenue or Mount Hope rather than in a hospital garage.'),
  P('The institute in Henrietta moves engineering students in on its own calendar. Co-op students ship cars to and from their placements. An adult signs for a student car, and the driver meets you at a lot on Jefferson Road.'),
  P('The grocery headquarters in Gates and the payroll company in Penfield transfer staff on start dates. The optics and imaging companies do the same. The defense electronics plants bring engineers in from across the country. If your employer reimburses the shipment, we send the documentation.'),
  P('The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side of a relocation.'),
 ), alt=True))

BODY.append(sec('The Lake-Effect Winter','Snow Off Lake Ontario, Salt, and the Spring Thaw',
 prose(
  L('Rochester is one of the snowiest big cities in the country. The lake delivers the snow a few inches at a time.'),
  P('Lake-effect season runs from November into March. Rochester gets its snow in steady accumulation more than in single bands. The plows keep the expressways open most days. A heavy week can still slide a pickup by a day.'),
  P('The Thruway closes to trucks a few times a winter, usually west of the city toward Buffalo. Carriers wait at the service areas and roll when it reopens. Road salt runs from November through April.'),
  P('Spring brings high water on the lake and the canal. The lakeshore roads in Charlotte and Greece can flood. Summer is the easy season, and the festival calendar is the only thing that closes a street.'),
  P('A car arriving from a warm state needs a strong battery, winter oil, and tires rated for snow.'),
 )))

BODY.append(sec('The Calendar','The Lilac Festival, the Jazz Festival, and the Park Avenue Weekend',
 prose(
  L('Rochester closes its best streets for its best weekends, and the carriers plan around them.'),
  P('The lilac festival fills Highland Park and the surrounding streets for ten days in May. The jazz festival closes the East End for nine nights in June. The Park Avenue festival takes the whole avenue for a weekend in August. Corn Hill does the same in July.'),
  P('We schedule those neighborhoods around the dates. The suburbs run normally through all of it.'),
  P('Pittsford, Brighton, and Greece send their cars to Fort Myers, Naples, and The Villages each fall. The cars come north again each spring. Our <a href="snowbird-car-shipping.html">snowbird</a> page has the planning tips.'),
 )+chips(["Downtown","East End","Park Avenue","Neighborhood of the Arts","South Wedge","Swillburg","Highland Park","Corn Hill","Nineteenth Ward","Maplewood","Lyell-Otis","Charlotte","North Winton Village","Browncroft","Cobbs Hill","Brighton","Pittsford","Penfield","Webster","Irondequoit","Fairport","Perinton","Henrietta","Greece","Gates","Chili","Spencerport","Brockport","Victor","Canandaigua"])
 +NOTE('Serving Monroe County and the canal towns. Tell us the neighborhood, the month, and whether the car runs.'), alt=True))

BODY.append(sec('Your Options','Open or Enclosed in Rochester?',
 prose(
  L('Open transport carries most of Rochester, and the Thruway lanes run on it.'),
  P('Enclosed transport keeps a car covered against road salt, slush, and lake grit. The collector garages on East Avenue and in Pittsford book enclosed trailers. A car wintering in Naples often does the same.'),
  P('A daily driver is fine on an open trailer. Our <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages compare the two.'),
 )))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a loading near the expressway, and a delivery. The lake decides the timing in winter.'),
  P('Once you approve the price, a carrier already running the Thruway takes the booking. The driver writes up the car’s condition on a Bill of Lading at the meeting spot. You sign it there, and you check the car against it at delivery.'),
 )+ULI([
  "Remove personal belongings",
  "Keep about a quarter tank of fuel",
  "Photograph the vehicle before pickup, especially after a salty winter",
  "Provide a working key and disclose mechanical issues",
  "Disable aftermarket alarms",
  "On Park Avenue or in a canal village, plan to meet the truck at a plaza",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> guides walk through each step.')), alt=True))

BODY.append(sec('Why Ship Guy','Why Rochester Drivers Choose Ship Guy',
 prose(
  L('We work the Thruway every day and plan around the lake, the hospital calendar, and the festival weekends.'),
  P('Ship Guy holds active FMCSA brokerage authority and a $75,000 surety bond, both on the public register. Our office is on Rutter Street on the west side.'),
  P('You get one coordinator from quote to delivery, with open, enclosed, and expedited transport on the menu. The <a href="services.html">services</a> page lists everything we book.'),
 )))

BODY.append(office('Rochester','46 Rutter St #857','Rochester, NY 14606','+15856321459','(585) 632-1459','ET',
 '46+Rutter+St+%23857,+Rochester,+NY+14606','Visit Us','Find Ship Guy in Rochester',
 'Our office is on Rutter Street on the west side, off Lyell Avenue and minutes from Route 390.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4922.143573084283!2d-77.6467103!3d43.16564539999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89d6b5a30ecf8e21%3A0x5827015150d0843b!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792023033567!5m2!1sen!2sus'))

FAQ=[
 ("Does lake-effect snow delay a Rochester pickup?","Sometimes by a day. Rochester gets steady snow more than single bands. The plows keep Interstate 490 and Route 390 open most days. The Thruway closes to trucks a few times a winter toward Buffalo. We tell you the moment the forecast shifts the plan."),
 ("How much does it cost to ship a car from Rochester to Florida?","Expect nine hundred to thirteen hundred dollars for a sedan to Fort Myers. Orlando comes in a little under that. The run is about thirteen hundred miles on Interstate 390, 79, 77, and 95. Fall southbound costs more than spring. SUVs and pickups add 10 to 25 percent."),
 ("Is the Thruway toll added to my price?","No. The carrier pays the Thruway by the mile and prices the trip with it. The toll sits inside the number you approve. Interstate 490, Route 390, and Route 590 are free."),
 ("Can the carrier come to my house on Park Avenue or in the South Wedge?","Rarely. The streets are narrow and cars park on both curbs. The driver meets you on East Avenue, Monroe Avenue, or at a lot near Interstate 490. Greece, Henrietta, Webster, and the open parts of Brighton usually allow curbside."),
 ("Do you ship cars for residents at the medical center?","Yes, every June and July. The university hospital brings in residents and fellows from every state. Most arrive with about two weeks of notice. The handoff happens on Elmwood Avenue or Mount Hope rather than in a hospital garage."),
 ("Can you ship a car for a University of Rochester or RIT student?","Yes. Student cars arrive each August and leave each May, and co-op students ship to their placements in between. The driver meets you at a lot on Jefferson Road or near Interstate 490. An adult signs for the car at pickup."),
 ("Does the lilac festival or the jazz festival affect pickups?","In those neighborhoods, yes. Highland Park fills for ten days in May, and the East End closes for nine nights in June. We schedule Park Avenue, Highland, and East End pickups around the dates. The suburbs run normally."),
 ("Can you pick up in Pittsford, Fairport, or another canal village?","Yes. The village streets are tight. The driver meets you on Monroe Avenue, at the plaza, or at the village edge. The newer streets in Perinton, Penfield, and Victor usually allow curbside."),
 ("Can you ship a car that does not run from Rochester?","Yes. A carrier with a winch loads a car that will not start. The loading time is priced in. In winter, clear the snow around it before the truck arrives. Let us know whether it rolls, steers, and brakes."),
 ("What do you need for a Rochester car shipping quote?","Both addresses, with the neighborhood or the village. The year, make, and model. Whether it runs and rolls. Open or enclosed, and the dates you can give us. That is a complete Rochester quote request."),
]
BODY.append(faq_section(FAQ,'Rochester FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Rochester?','The form above takes about two minutes. Tell us the neighborhood and your dates. We will match you with a carrier already running the Thruway.','+15856321459','(585) 632-1459','Get your free Rochester quote'))

build({
 'slug':'auto-transport-rochester-new-york',
 'title':'Car Shipping in Rochester, NY — Auto Transport | Ship Guy',
 'meta':'Car shipping in Rochester, NY on the Thruway and Interstate 490. Lake-effect planning, Park Avenue and Pittsford handoffs, the medical center and RIT calendar, festival timing, the Fort Myers snowbird lane, tolls built in. Local office on Rutter Street. Free quote.',
 'h1':'Car Shipping in<br>Rochester, <span class="accent">New York</span>',
 'lede':'Open, enclosed, and expedited auto transport across Monroe County, planned around the Thruway, the lake, and the hospital calendar.',
 'tel':'+15856321459','disp':'(585) 632-1459','brand':'Rochester','keyword':'car shipping in rochester',
 'localterms':['rochester','interstate 90','thruway','interstate 490','route 390','route 590','route 104','route 531','lake ontario','lyell avenue','lake avenue','mount read','east avenue','monroe avenue','park avenue','east end','south wedge','swillburg','corn hill','nineteenth ward','maplewood','lyell-otis','charlotte','highland park','brighton','pittsford','penfield','webster','irondequoit','fairport','perinton','henrietta','greece','gates','chili','spencerport','brockport','victor','canal','university','medical center','residents','institute','jefferson road','grocery','payroll','optics','imaging','defense','lake-effect','salt','lilac','jazz','festival','snowbird','fort myers','naples','buffalo','syracuse','cleveland','albany','boston','chicago'],
}, BODY, FAQ)
