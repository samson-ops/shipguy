import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Aurora, Colorado','Car shipping along Interstate 225, between the medical campus and the airport',
 ['Car shipping in Aurora starts on Interstate 225, the spine that ties the city to 25 and 70. Ship Guy is a licensed auto transport broker with an office on South Abilene Street near the mall.',
  'We book vetted carriers across the east metro, from Colfax to Southlands and out to the airport. We do not own the trucks.',
  'Interstate 225 runs the length of the city from the Tech Center to Interstate 70. Interstate 70 crosses the north side on the way to the airport and Kansas. The E-470 toll road wraps the east side. Parker Road, Havana Street, and Colfax Avenue carry the rest.',
  'This page covers the three highways, the toll road, Colfax, the postwar grids, and the new southeast. It also covers the medical campus, the base, the aerospace plants, the airport, the hail, and the lanes.'],
 'Aurora at a glance',
 ['Most pickups happen within 1 to 3 days. Interstate 70 brings the Kansas City carriers past the north side all day.',
  'Denver and Colorado Springs are same-day lanes. Fort Collins is the same day too. Albuquerque, Kansas City, and Salt Lake City take a day. Dallas, Phoenix, and Las Vegas take two.'],
 'Tell us the neighborhood. Original Aurora, Heather Gardens, and the gated southeast need a meeting spot. Hoffman Heights, Aurora Hills, and most of the grids allow the curb.'))

BODY.append(sec('The Roads','Interstate 225, 70, E-470, Parker Road, and Colfax Avenue',
 prose(
  L('Aurora is the east side of the metro area. It has the only freeway that runs through the middle of a suburb.'),
  P('Interstate 225 leaves 25 at the Tech Center and runs north through Aurora to 70. The light rail runs beside it. The ramps at Parker Road, Iliff, Mississippi, and Colfax are the way into every neighborhood. Interstate 70 crosses the north end past the stadium district and on to the airport.'),
  P('E-470 is the toll road that wraps the east side from Parker to the airport. It charges by plate, and the carriers that use it build the toll into the price. Peña Boulevard leaves 70 for the terminal. Tower Road runs the airport’s west edge.'),
  P('Colfax Avenue is the old main street. It runs the whole north side from Denver to the plains. Havana Street, Peoria Street, and Chambers Road run north and south through the grids. Parker Road cuts southeast past the reservoir. Smoky Hill Road, Arapahoe Road, and Quincy Avenue reach the new southeast.'),
  P('The carriers come off 225 at Parker Road and Iliff, and off 70 at Chambers and Tower Road. The lots at the mall off Abilene, along Havana, and off Tower Road are the usual meeting spots. Our office sits on South Abilene Street, beside the mall and a block off 225.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Original Aurora, the Grids, the Medical Campus, and the Southeast',
 prose(
  L('Aurora is a century of subdivisions laid end to end, from the Colfax blocks to the new southeast.'),
  P('Original Aurora along Colfax has narrow blocks, apartments, and cars on both curbs. The driver meets you on Colfax or at a lot on Havana. The medical campus at Peoria and Colfax has garages and wide streets. A handoff works in the lots along Montview. Hoffman Heights and Del Mar are postwar grids where the truck usually reaches the curb.'),
  P('Aurora Hills, Expo Park, and Side Creek are grids and cul-de-sacs from the sixties and seventies. The curb works on most streets. Heather Gardens is a gated community by the mall. The driver meets you at the gate on Yale. The blocks around the Tech Center border have garages and wide streets.'),
  P('Mission Viejo, Seven Hills, and Meadow Hills are cul-de-sac subdivisions where the driver meets you at the entrance. Saddle Rock, Tallyn’s Reach, and Southlands are the new southeast, with wide streets and gates on many entrances. Send the gate code, and we confirm access before dispatch.'),
  P('The north end along 70 has the stadium, the warehouses, and Green Valley Ranch across the Denver line. The truck reaches the curb there. Buckley sits on the east side off Sixth Avenue, and the handoff happens outside its gate. Watkins and Bennett sit out on the plains with room everywhere.'),
 )))

ROUTES=[("Colorado Springs, CO","I-225/I-25 · ~65 mi","Same day","$150–$240"),("Albuquerque, NM","I-25 · ~450 mi","1 day","$400–$570"),
 ("Kansas City, MO","I-70 · ~590 mi","1–2 days","$450–$650"),("Wichita, KS","I-70/US-400 · ~510 mi","1 day","$420–$600"),
 ("Salt Lake City, UT","I-70/US-6 · ~530 mi","1–2 days","$430–$620"),("Omaha, NE","I-76/I-80 · ~530 mi","1–2 days","$430–$620"),
 ("Dallas, TX","I-25/US-287 · ~790 mi","2 days","$560–$820"),("Phoenix, AZ","I-25/I-40 · ~830 mi","2 days","$450–$650"),
 ("Las Vegas, NV","I-70/I-15 · ~760 mi","2 days","$540–$780"),("Chicago, IL","I-76/I-80 · ~990 mi","3 days","$700–$1,000")]
BODY.append(rate_table('Lanes &amp; Costs','Aurora Car Shipping Lanes and Estimated Costs',
 'Where east-metro cars go most, with estimated open-trailer ranges. Your exact route prices above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates, open trailer, running sedan, priced from Aurora. Figure 10 to 25 percent more for an SUV or pickup, and more again for enclosed. Any E-470 toll is in the number. Season and carrier availability on your dates set the final price.',
 prose(
  P('Aurora prices like Denver, because the same 70 and 25 carriers reach both. The Kansas City and Wichita lanes ride 70 east from the north end without touching the city. Texas and California send the most households, so those inbound lanes stay full.'),
  P('The base brings a new Texas or Florida lane with every rotation. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Medical Campus, the Base, the Aerospace Plants, and the Airport',
 prose(
  L('Aurora relocates residents, guardians, engineers, and airport crews, and the hospital calendar is the biggest one.'),
  P('The medical campus at Peoria and Colfax is the largest in the region. The university hospital, the children’s hospital, and the veterans hospital bring in residents each June. Nurses arrive all year. The medical school and the nursing school bring students in each August. The handoff happens in the lots along Montview.'),
  P('Buckley hosts Space Force units and the Guard fighter wing, and families rotate through on orders. One car moves on the orders, and the second comes with us. The gate stops the truck, so the handoff happens at a lot on Sixth Avenue or Mississippi. Ship Guy is a private broker with no connection to the base. The <a href="military-car-shipping.html">military</a> page covers the timing.'),
  P('The aerospace plants along the base and in the south hire engineers on program schedules. The airport brings in airline crews, mechanics, and warehouse managers all year. The hotels and the resort by the airport hire on their own calendar. We supply the paperwork a reimbursed move needs.'),
  P('Families arrive from Texas, California, and the Midwest for the schools in the southeast. Most ship one car and drive the other. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side of a move.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Hail, Blizzards, Airport Traffic, and the Reservoir',
 prose(
  L('Aurora sits on the plains edge of the metro area. The plains send the worst of the weather first.'),
  P('Hail is the costliest weather in the region, and Aurora takes it harder than Denver. The 2018 storm dented cars across the southeast in minutes. We shift the window when a storm is forecast. A collector car rides enclosed.'),
  P('Spring blizzards close Interstate 70 east of the airport and E-470 for a day. The March 2019 storm stranded cars on Peña Boulevard. The carriers wait at the truck stops off 70 in Aurora. A winter pickup can slide a day or two.'),
  P('Tornado warnings reach the east side a few times each spring. A warning holds the driver until the all-clear. Summer afternoons bring thunderstorms, and the loading hour moves to the morning in July. Wildfire smoke drifts in from the mountains in August and slows the roads.'),
  P('Airport traffic jams Peña Boulevard on holiday weekends, and a fly-and-ship handoff moves to Tower Road. The reservoir fills Parker Road on summer weekends. The stadium district fills the north end on match days. We move a pickup in those blocks to another day.'),
 )+chips(["Original Aurora","Colfax","Fitzsimons","Medical Campus","Hoffman Heights","Del Mar","Aurora Hills","Expo Park","Side Creek","Heather Gardens","Hampden Hills","Meadow Hills","Pheasant Run","Mission Viejo","Seven Hills","Saddle Rock","Tallyn’s Reach","Southlands","Murphy Creek","Blackstone","Tollgate","Buckley","Gateway","Green Valley Ranch","Watkins","Bennett","Centennial","Parker"])
 +NOTE('Serving Aurora and the whole east metro, from Colfax to Southlands and out to the airport. Tell us the neighborhood, the gate, and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Aurora?',
 prose(
  L('Open is how the east metro ships, and the 70 and 25 lanes are priced for it.'),
  P('An enclosed trailer keeps the hail, the road treatment, and attention off a car. The garages in the southeast book them for collector cars. So does a guardian with a restored car headed to a new post.'),
  P('A daily driver rides open without a problem. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain what the roof is for.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff at the mall lots or off Tower Road, and a delivery. The hail forecast sets the hour.'),
  P('Approve the price, and a carrier already on 70 or 225 takes the booking. We confirm the spot and the window the same day. The driver walks around the car with you and writes its condition on a Bill of Lading. Both of you sign, and the driver brings the same sheet back out at delivery.'),
 )+ULI([
  "Take everything personal out of the car",
  "Keep the tank near a quarter full",
  "Shoot photos of every panel before the handoff, especially after hail",
  "Give the driver a working key and name any mechanical issue",
  "Switch off any aftermarket alarm",
  "In a gated community, send the gate code or plan to meet at the entrance",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Aurora Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already run 70 and 225. We plan around the hail, the blizzards, and the gates.'),
  P('Ship Guy’s FMCSA brokerage authority is active, and a $75,000 surety bond backs it. Both are on file in the federal register. Our office is on South Abilene Street beside the mall.'),
  P('From the first quote to the last signature, one coordinator is your contact. Open, enclosed, and expedited transport are each explained on the <a href="services.html">services</a> page.'),
 ), alt=True))

BODY.append(office('Aurora','2675 S Abilene St Ste 598','Aurora, CO 80014','+17208939478','(720) 893-9478','MT',
 '2675+S+Abilene+St+Ste+598,+Aurora,+CO+80014','Visit Us','Find Ship Guy in Aurora',
 'Our office is on South Abilene Street beside the mall, a block off Interstate 225 at Iliff.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4722.697616680244!2d-104.82883149999999!3d39.668771299999996!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x876c89f42ed2799b%3A0xc4c09936f95f4ab2!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792161752176!5m2!1sen!2sus'))

FAQ=[
 ("Do you ship cars for residents and staff at the Anschutz medical campus?","Yes, every June and all year. The three hospitals on the campus bring in residents and nurses on the same calendar. Many ship a car from the coast behind the move. The handoff happens in the lots along Montview, and we provide the paperwork a reimbursed move needs."),
 ("How much does it cost to ship a car from Aurora to Kansas City or Dallas?","Kansas City runs four hundred fifty to six hundred fifty dollars for a sedan. That is about five hundred ninety miles straight out 70. Dallas runs five hundred sixty to eight hundred twenty. That is about seven hundred ninety miles down 25 and US 287. SUVs and pickups add 10 to 25 percent."),
 ("Do you handle a PCS move to Buckley?","Yes, on every rotation. One car moves on the orders, and the second comes with us. The gate stops the truck, so we meet you at a lot on Sixth Avenue or Mississippi. We schedule around your report date. Ship Guy is a private broker with no connection to the base."),
 ("What if hail is forecast for my Aurora pickup day?","We move it. Aurora takes hail harder than Denver, and the 2018 storm dented cars across the southeast in minutes. Pickups shift to the first clear morning after the storm passes. Anything collectible goes under a roof. You hear from us as soon as the forecast turns."),
 ("Can the carrier come into my gated community in the southeast?","Often, if the gate allows trucks. Saddle Rock, Tallyn’s Reach, and the Southlands subdivisions have gates on many entrances. Send the community name and the code, and we confirm access before dispatch. Where the truck cannot enter, the driver meets you at the entrance."),
 ("Can you meet me at the airport for a fly-and-ship?","Yes. The lots off Tower Road and along Peña Boulevard work for a handoff. Tell us your flight, and the driver meets you within a window around it. On a holiday weekend, Peña jams, and the handoff moves to Tower Road."),
 ("What happens if a blizzard hits on my pickup day?","The carriers sit at the truck stops off 70 in Aurora until the plows finish. Interstate 70 east of the airport and E-470 close for a day in a spring storm. No driver moves a loaded trailer on ice. Expect a winter pickup to shift a day or two, with a call from us first."),
 ("Can the carrier come to my street along Colfax or in Heather Gardens?","Usually not on Colfax, and never past the gate at Heather Gardens. The Colfax blocks are narrow with cars on both curbs. The driver meets you at a lot on Havana. Heather Gardens residents meet the driver at the gate on Yale. Hoffman Heights and Aurora Hills allow the curb."),
 ("Can you ship a car that does not run from Aurora?","Yes. A winch truck takes the job, and the longer loading is already in the price. The mall lots or a lot off Tower Road give the driver a flat, open spot. Say whether the car rolls, steers, and brakes when you book."),
 ("What do you need for an Aurora car shipping quote?","Pickup and delivery addresses, with the neighborhood or the gate code on this end. The car’s year, make, and model. Whether it starts and rolls. A choice of open or enclosed, and a date range. With those, an Aurora quote is exact."),
]
BODY.append(faq_section(FAQ,'Aurora FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Aurora?','Two minutes on the form above prices your lane. Send the neighborhood and your dates, and a carrier already rolling on 70 takes it.','+17208939478','(720) 893-9478','Get your free Aurora quote'))

build({
 'slug':'auto-transport-aurora-colorado',
 'title':'Car Shipping in Aurora, CO — Auto Transport | Ship Guy',
 'meta':'Car shipping in Aurora, CO along Interstate 225 between the medical campus and the airport. Anschutz residents, Buckley second cars and gate handoffs, Colfax and Heather Gardens meeting spots, gated southeast access, airport fly-and-ship, hail and blizzard planning. Local office on South Abilene Street by the mall. Free quote.',
 'h1':'Car Shipping in<br>Aurora, <span class="accent">Colorado</span>',
 'lede':'Open, enclosed, and expedited auto transport across the east metro, planned around 225, 70, the gates, and the hail.',
 'tel':'+17208939478','disp':'(720) 893-9478','brand':'Aurora','keyword':'car shipping in aurora',
 'localterms':['aurora','interstate 225','interstate 70','e-470','toll','parker road','havana street','peoria street','chambers road','colfax avenue','iliff','mississippi','tower road','peña boulevard','airport','smoky hill road','arapahoe road','quincy avenue','sixth avenue','abilene','mall','light rail','tech center','original aurora','medical campus','fitzsimons','montview','hoffman heights','del mar','aurora hills','expo park','side creek','heather gardens','yale','mission viejo','seven hills','meadow hills','saddle rock','tallyn’s reach','southlands','gate code','stadium','green valley ranch','buckley','watkins','bennett','university hospital','children’s hospital','veterans hospital','residents','nurses','medical school','space force','guard','fighter wing','orders','aerospace','airline crews','resort','hail','2018','blizzards','2019','tornado','thunderstorms','wildfire smoke','reservoir','match days','denver','colorado springs','fort collins','albuquerque','kansas city','wichita','salt lake city','omaha','dallas','phoenix','las vegas','chicago','texas','california','florida'],
}, BODY, FAQ)
