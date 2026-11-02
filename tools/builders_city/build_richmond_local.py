import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Richmond, Virginia','Car shipping where 95 and 64 cross, in the capital on the fall line of the James',
 ['Car shipping in Richmond starts at the busiest interchange in the state, where Interstate 95 meets Interstate 64. Ship Guy is a licensed auto transport broker with an office on West Broad Street in Scott’s Addition.',
  'We book vetted carriers across the city and the counties, from the Fan to Short Pump and Mechanicsville. The trucks belong to the carriers. Ship Guy holds the license and the bond.',
  'Interstate 95 carries the Northeast-to-Florida lane straight through downtown. Interstate 64 runs from the mountains to Hampton Roads, and Interstate 295 loops the north and east. Route 288 loops the west and south, and the Downtown Expressway and the Powhite carry the toll crossings.',
  'This page covers 95, 64, 295, 288, the toll roads, the Fan, the West End, and the counties. It also covers the state workforce, the university, the headquarters, the Army post, the races, and the lanes.'],
 'Richmond at a glance',
 ['Most pickups happen within 1 to 3 days. Carriers stage in Richmond for the whole state, and the 95 lane passes every hour.',
  'Washington, Virginia Beach, Baltimore, and Raleigh are same-day runs. Philadelphia, Charlotte, and New York need a day. Atlanta needs one to two, and Florida needs two.'],
 'Tell us the neighborhood and whether the street has an alley. The Fan, Church Hill, Carytown, and Shockoe meet the truck at a lot. Short Pump, Glen Allen, Midlothian, Chester, and Mechanicsville usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 95, Interstate 64, Interstate 295, Route 288, the Downtown Expressway, the Powhite, and Broad Street',
 prose(
  L('Richmond is the crossroads of Virginia, and a carrier reaches every county without touching a city street.'),
  P('Interstate 95 runs north and south through downtown. It crosses the James on the bridge by the old train shed. It carries more car haulers than any other road in the state. Interstate 64 arrives from Charlottesville and shares the downtown miles with 95. It leaves east for Williamsburg and the coast. The two share four miles, and the shared stretch backs up both rush hours.'),
  P('Interstate 295 loops the north and east from Short Pump to Petersburg. Most carriers use it to skip downtown. Route 288 loops the west and south from Short Pump through Midlothian to Chester. Interstate 195 is the short spur from 64 to the Downtown Expressway. The Expressway and the Powhite Parkway are toll roads across the river. The toll rides inside the quote.'),
  P('Broad Street is the spine, from Church Hill through downtown and Scott’s Addition to Short Pump. Monument Avenue, Cary Street, and Main Street carry the Fan and the Near West End. Midlothian Turnpike and Hull Street carry the Southside, and Mechanicsville Turnpike carries Hanover. Arthur Ashe Boulevard crosses Broad by our office.'),
  P('The carriers come off 64 at Broad Street and off 295 at Nuckols Road. The mall lots at Short Pump are the usual meeting spot. The centers along Broad in the West End work too. The Southside centers on Midlothian Turnpike and the lots at Mechanicsville work too. The raceway lots on Laburnum Avenue work outside race weekends.'),
  P('Our office is on West Broad Street in Scott’s Addition, at Arthur Ashe Boulevard.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','The Fan, the Museum District, Scott’s Addition, Church Hill, Shockoe, Carytown, the West End, the Southside, Henrico, Chesterfield, and Hanover',
 prose(
  L('Richmond is a grid of alleys and row houses with wide counties on every side. The truck meets the city at the edges.'),
  P('The Fan is the city’s showpiece, blocks of row houses on narrow streets with alleys behind. Cars park on both sides, and a seventy-five-foot trailer does not fit. The driver meets you on Broad or on the Boulevard. The Museum District west of it is the same. Carytown on Cary Street is the same with shops. Scott’s Addition is old warehouses turned breweries and apartments, and the handoff happens on Broad.'),
  P('Church Hill climbs east of downtown on cobblestones and steep blocks. The driver meets you on Broad at the bottom of the hill. Shockoe Bottom and Shockoe Slip below it are cobblestones by the river. The handoff moves to the Main Street station lots. Jackson Ward and downtown meet the truck at the convention center garages.'),
  P('Manchester across the river is old industrial blocks turned apartments. The handoff happens on Hull Street. Westover Hills, Forest Hill, and Bon Air are hilly streets of older houses under big trees. The handoff moves to the Forest Hill Avenue centers. Midlothian and Chester in Chesterfield are wide subdivisions, and the curb works.'),
  P('The West End in Henrico is the big one. Short Pump, Glen Allen, Innsbrook, and Wyndham are subdivisions on wide streets, and the driver reaches the house. The Near West End along Grove and Patterson is older and tighter. The handoff moves to the centers on Patterson. Mechanicsville and Ashland in Hanover are wide, and the curb works. Petersburg, Hopewell, and Colonial Heights to the south price the same as Richmond.'),
 )))

ROUTES=[("Virginia Beach, VA","I-64 · ~105 mi","Same day","$170–$280"),("Washington, DC","I-95 · ~110 mi","Same day","$170–$280"),
 ("Baltimore, MD","I-95 · ~155 mi","Same day","$210–$330"),("Raleigh, NC","I-85/I-95 · ~170 mi","Same day","$220–$340"),
 ("Philadelphia, PA","I-95 · ~250 mi","1 day","$250–$380"),("Charlotte, NC","I-85 · ~290 mi","1 day","$270–$400"),
 ("New York, NY","I-95 · ~340 mi","1 day","$320–$460"),("Atlanta, GA","I-85 · ~530 mi","1–2 days","$440–$630"),
 ("Jacksonville, FL","I-95 · ~560 mi","2 days","$450–$650"),("Orlando, FL","I-95 · ~700 mi","2 days","$500–$730")]
BODY.append(rate_table('Lanes &amp; Costs','Richmond Car Shipping Lanes and Estimated Costs',
 'The lanes Richmond cars run most, with estimated open-trailer ranges. Your own route gets a number on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Richmond, running sedan, open trailer. Add 10 to 25 percent for an SUV or a pickup, and more for enclosed. The Expressway and Powhite tolls are inside the number when a carrier uses them. Season and the carriers free on your dates set the final figure.',
 prose(
  P('Richmond prices among the best in the Mid-Atlantic, because every carrier on the 95 lane passes through. Washington is two hours north, and the Northeast lanes start there. The Raleigh and Charlotte lanes ride 85 southwest. The Florida lane fills southbound each fall and northbound each spring, and the price swings with it.'),
  P('A move timed to a July closing or the August move-in ships with the busiest weeks. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The State Workforce, the University, the Headquarters, the Army Post, the Hospitals, and the Port',
 prose(
  L('Richmond relocates state employees, bankers, medical residents, soldiers, and students. The state and the university move the most.'),
  P('The state government fills downtown, and its agencies transfer staff on start dates all year. Every four years a new administration moves an appointee class in January. The university downtown and its medical campus bring faculty, residents, and students in on their own calendars. Residents arrive each June, and students arrive each August. A parent sets up a student booking, and an adult over eighteen signs at a lot.'),
  P('The headquarters along the West End corridor move people every week. The credit card bank in Goochland and the used-car chain beside it relocate staff on offer dates. The tobacco company, the power utility, and the insurers do the same. The used-car chain ships its own inventory on its own trucks, and we do not move those. We produce the paperwork a reimbursed move needs.'),
  P('The Army logistics post beside Petersburg trains and rotates soldiers on orders all year, with a summer peak. The supply depot in Chesterfield does the same with civilians. Housing at both is gated, and the handoff happens outside the gate. Orders usually cover one vehicle, so the second one ships privately. Ship Guy is a private broker with no tie to either. Our <a href="military-car-shipping.html">military car shipping</a> page has the PCS timing.'),
  P('The port on the James south of downtown lands containers by barge from Norfolk. Imported cars clear at the Norfolk piers instead, and a released car is a domestic move from there. The hospital systems hire traveling nurses year round. The <a href="state-to-state-car-shipping.html">state-to-state</a> page has the interstate side.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Race Weekends, the Folk Festival, Move-In, the Ice Storms, the Hurricanes, and the River',
 prose(
  L('Richmond runs on a race schedule and a campus calendar. The river climbs the Bottom in a hurricane.'),
  P('The raceway on Laburnum Avenue runs its big race weekend in late summer. Smaller events fill the year. The lots fill, Laburnum closes, and 295 backs up at the exits. A handoff in Henrico moves to the weekday. The folk festival fills the riverfront downtown for a weekend in October. The Monument Avenue 10K fills the Fan on a Saturday in April.'),
  P('Move-in week in late August clogs the blocks around the university from Broad to the river. The handoff moves to the Boulevard that week. Graduation in May fills the downtown garages. The state fair fills the Meadow Event Park in Doswell for ten days in late September. The 95 exit backs up.'),
  P('Winter is ice more than snow. A January ice storm takes the power out in the West End for days. The hills in Church Hill and Forest Hill glaze first. The January 2022 storm shut 95 north of the city for a full day with drivers trapped overnight. The carriers wait in Petersburg or Fredericksburg until the roads clear. A winter pickup can lose a day. We tell you first.'),
  P('Hurricane remnants bring the floods. Gaston in 2004 put Shockoe Bottom under feet of water and pulled cars down the streets. Camille and Agnes flooded the same blocks before the floodwall went up. The floodwall holds the river off downtown, and the Bottom drains in a day. A pickup on the flat moves up the hill until the water drops.'),
 )+chips(["The Fan","Museum District","Scott's Addition","Carytown","Church Hill","Shockoe Bottom","Shockoe Slip","Jackson Ward","Downtown","Manchester","Westover Hills","Forest Hill","Bon Air","Near West End","Grove Avenue","Patterson Avenue","Short Pump","Glen Allen","Innsbrook","Wyndham","Tuckahoe","Lakeside","Northside","Bellevue","Ginter Park","Highland Springs","Sandston","Midlothian","Brandermill","Chester","Mechanicsville","Ashland","Petersburg","Colonial Heights","Hopewell","Goochland"])
 +NOTE('Serving Richmond and all of Henrico, Chesterfield, and Hanover Counties, Fan alley or Short Pump cul-de-sac. Tell us the neighborhood and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Richmond?',
 prose(
  L('Open trailers carry most Richmond cars, and the lane table above assumes one.'),
  P('An enclosed trailer keeps off the road salt, the pollen, and the grit of the 95 lane. The collectors in the West End and the executives relocating a new car book one. The race-weekend crowd ships a few show cars enclosed too.'),
  P('A commuter sedan or a student car is fine on an open trailer. The difference is spelled out on the <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A number, a lot on Broad or at Short Pump, and a signature at delivery. The closing or the start date picks the week.'),
  P('Approve the price, and the car is booked with a carrier already on the 95 lane. The spot and the window are settled the same day. The pickup inspection puts every existing mark on the Bill of Lading, and both of you sign it. Delivery is compared to that record.'),
 )+ULI([
  "Nothing personal left in the cabin or the trunk",
  "Roughly a quarter tank of fuel",
  "Photos of each side and the odometer before the truck comes",
  "A working key for the driver, and a note of any fault",
  "Any aftermarket alarm disabled",
  "In the Fan, Church Hill, or the Bottom, meet the truck on Broad",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages cover each step.'))))

BODY.append(sec('Why Ship Guy','Why Richmond Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already stage at the 95 and 64 interchange. We know which blocks of the Fan a trailer cannot enter.'),
  P('Ship Guy’s FMCSA license and $75,000 bond can be checked on the federal register by anyone. Our office is on West Broad Street in Scott’s Addition.'),
  P('You get one coordinator from the first call to the last signature. The <a href="services.html">services</a> page explains open, enclosed, and expedited transport.'),
 )))

BODY.append(office('Richmond','2920 W Broad St #420a','Richmond, VA 23230','+18045811574','(804) 581-1574','ET',
 '2920+W+Broad+St+%23420a,+Richmond,+VA+23230','Visit Us','Find Ship Guy in Richmond',
 'Our office is on West Broad Street in Scott’s Addition, at Arthur Ashe Boulevard.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3903.848322613531!2d-77.47205989999999!3d37.56422070000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89b115cc463594e5%3A0x68162b377e1dd52d!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793287623957!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Richmond to New York or Florida?","New York runs three hundred twenty to four hundred sixty dollars for a sedan. That is about three hundred forty miles up 95. Orlando runs five hundred to seven hundred thirty, about seven hundred miles down 95. Washington is two hours north and the lowest of the three. An SUV or a pickup adds 10 to 25 percent."),
 ("Can the carrier come to my street in the Fan or Church Hill?","No. The Fan is row houses on narrow streets with cars on both sides. Church Hill is cobblestones on a slope. The driver meets you on Broad Street or on the Boulevard. Short Pump, Glen Allen, Midlothian, Chester, and Mechanicsville usually allow the curb."),
 ("Do you ship cars for state employees and the headquarters?","Yes, every week. The state transfers staff on start dates all year and moves an appointee class every fourth January. The bank, the utility, the tobacco company, and the insurers relocate staff on offer dates. A second car usually comes along on a trailer. We produce the paperwork a reimbursed move needs."),
 ("Can you deliver on the VCU move-in date?","Yes. The campus takes cars in each August and sends them home in May. A parent books it, and an adult over eighteen signs at a lot. Move-in week clogs the blocks from Broad to the river, so the handoff happens on the Boulevard. The window moves with the date."),
 ("Do you handle PCS moves for Fort Gregg-Adams?","Yes, and the summer is the peak. The post beside Petersburg rotates soldiers on orders all year. Housing is gated, and the handoff happens outside the gate. Orders usually cover one vehicle, so the second one ships privately. Ship Guy is a private broker with no connection to the Army."),
 ("Can you ship a car to or from Short Pump, Midlothian, or Mechanicsville?","Yes, and all three price the same as Richmond. Short Pump rides the same carriers off 64 and 295, and the curb works. Midlothian rides them off 288, and Mechanicsville rides them off 295. Send the full address for a county road."),
 ("Does a race weekend affect my pickup?","Yes, if the address is in eastern Henrico. The raceway lots fill, Laburnum Avenue closes, and 295 backs up at the exits. A handoff near the track moves to the weekday. The rest of the region barely notices."),
 ("Are the Expressway and Powhite tolls in my price?","Yes. A carrier that crosses the river on either one pays the toll with a transponder. It rides inside the quote. There is no separate line. Interstate 95, 64, 295, and Route 288 carry no toll."),
 ("Can you ship a car that does not run from Richmond?","Yes. The quote includes a winch and the loading time from the start. The mall lots at Short Pump or the raceway lots give the driver level ground. Say whether the car rolls, steers, and brakes."),
 ("What do you need for a Richmond car shipping quote?","Where it is and where it goes, with the neighborhood or the county. Year, make, and model. Whether it runs. Open or enclosed. The week around the closing or the start date. Five answers, and the Richmond number is back the same day."),
]
BODY.append(faq_section(FAQ,'Richmond FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Richmond?','Two minutes on the form above gets your lane a number. Tell us the neighborhood and the week, and a carrier already on 95 takes it.','+18045811574','(804) 581-1574','Get your free Richmond quote'))

build({
 'slug':'auto-transport-richmond-virginia',
 'title':'Car Shipping in Richmond, VA — Auto Transport | Ship Guy',
 'meta':'Car shipping in Richmond, VA, the capital where 95 and 64 cross on the James. State and headquarters relocations, VCU move-in timing, Fort Gregg-Adams PCS moves, Broad Street handoffs for the Fan and Church Hill, curbside pickups in Short Pump, Midlothian, and Mechanicsville, the race weekends, the ice storms, and the river. Local office on West Broad Street in Scott’s Addition. Free quote.',
 'h1':'Car Shipping in<br>Richmond, <span class="accent">Virginia</span>',
 'lede':'Open, enclosed, and expedited auto transport across the capital region, planned around the 95 lane, the alleys of the Fan, the county subdivisions, the Army post, and the river.',
 'tel':'+18045811574','disp':'(804) 581-1574','brand':'Richmond','keyword':'car shipping in richmond',
 'localterms':['richmond','interstate 95','interstate 64','capital','fall line','james','interchange','west broad street','scott','the fan','church hill','short pump','midlothian','mechanicsville','northeast','florida','hampton roads','interstate 295','route 288','downtown expressway','powhite','toll','west end','counties','state workforce','university','headquarters','army post','port','race weekends','washington','virginia beach','baltimore','raleigh','philadelphia','charlotte','new york','atlanta','alley','carytown','shockoe','glen allen','chester','train shed','charlottesville','williamsburg','petersburg','interstate 195','broad street','monument avenue','cary street','main street','midlothian turnpike','hull street','hanover','arthur ashe boulevard','nuckols road','mall','laburnum avenue','raceway','row houses','museum district','breweries','cobblestones','jackson ward','convention center','manchester','southside','westover hills','forest hill','bon air','henrico','chesterfield','innsbrook','wyndham','grove','patterson','ashland','hopewell','colonial heights','closing','move-in','residents','students','appointee','credit card bank','goochland','used-car chain','tobacco','utility','insurers','inventory','logistics post','supply depot','gated','pcs','barge','norfolk','traveling nurses','folk festival','10k','graduation','state fair','doswell','ice storm','january 2022','fredericksburg','gaston','2004','camille','agnes','floodwall','pollen','show cars','bill of lading','fmcsa','tuckahoe','lakeside','northside','bellevue','ginter park','highland springs','sandston','brandermill'],
}, BODY, FAQ)
