import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Charleston, South Carolina','Car shipping in the Lowcountry, where 26 ends at a peninsula laid out before trucks and the port ships cars by the thousand',
 ['Car shipping in Charleston runs on Interstate 26, the Mark Clark loop, and the bridges off the peninsula. Ship Guy is a licensed auto transport broker with an office on Gardner Road in West Ashley.',
  'We book vetted carriers across the Charleston metro, from the peninsula to Mount Pleasant, Summerville, and the islands. The carriers own the trucks. Ship Guy holds the license and the bond.',
  'Interstate 26 arrives from Columbia through Summerville and North Charleston and ends on the peninsula at the Crosstown. Interstate 526 loops from West Ashley past the airport to Mount Pleasant. US 17 crosses the peninsula and rides the Ravenel Bridge over the Cooper. Savannah Highway, Rivers Avenue, and Folly Road carry the rest.',
  'This page covers 26, 526, the bridges, the peninsula, West Ashley, the islands, Mount Pleasant, and North Charleston. It also covers the joint base, the port, the plants, the colleges, the hurricanes, and the king tides.'],
 'Charleston at a glance',
 ['Most pickups happen within 1 to 3 days. The 95 carriers come over on 26 from Columbia and up 17 from Savannah every day. The port keeps more based in North Charleston.',
  'Savannah, Columbia, Augusta, and Charlotte are same-day runs. Jacksonville, Raleigh, Atlanta, and Orlando need a day. Washington needs one to two, and New York needs two.'],
 'Tell us the neighborhood and which side of the Crosstown it sits on. The lower peninsula, the Old Village, Sullivan’s Island, and the gated islands meet the truck at a lot. West Ashley, James Island, North Charleston, Summerville, and the Mount Pleasant subdivisions usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 26, Interstate 526, US 17, the Ravenel Bridge, the Crosstown, Savannah Highway, Rivers Avenue, Folly Road, and the Connector',
 prose(
  L('Charleston is water on three sides and a peninsula in the middle. Every carrier arrives on 26 and picks a bridge.'),
  P('Interstate 26 is the road in. It comes down from Columbia through Summerville, Ladson, and North Charleston. It ends at the Crosstown on the peninsula. The Columbia and Charlotte carriers ride it, and the state reverses it for a hurricane evacuation. Interstate 526 is the Mark Clark loop. It runs from Savannah Highway in West Ashley over the Ashley and past the airport. Then it crosses the Cooper on the Don Holt Bridge and Daniel Island to Mount Pleasant.'),
  P('US 17 is Savannah Highway in West Ashley, the Crosstown on the peninsula, and the Ravenel Bridge. The bridge closes in high wind and ice. Rivers Avenue is US 52 through North Charleston to Goose Creek and Moncks Corner. Folly Road crosses the Wappoo Cut to James Island and Folly Beach. The Connector ties the peninsula to James Island. Maybank Highway reaches Johns Island, and Bohicket Road runs to the gates of Kiawah and Seabrook.'),
  P('The carriers come off 26 at Montague or Ashley Phosphate and off 526 at Savannah Highway. The mall lots on Sam Rittenberg in West Ashley are the usual meeting spot. The outlet lots at 26 and Montague and the Towne Centre lots in Mount Pleasant work too. So do the big-box lots on Rivers Avenue. The lots at Meeting Street and the Crosstown work for the peninsula.'),
  P('Our office is on Gardner Road in West Ashley, by the mall on Sam Rittenberg Boulevard.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','The Peninsula, South of Broad, the Neck, West Ashley, James Island, Johns Island, Daniel Island, Mount Pleasant, the Beaches, North Charleston, and Summerville',
 prose(
  L('Charleston is single houses on lanes built for carriages, with wide suburbs across every bridge. The truck meets the old city at the Crosstown.'),
  P('The lower peninsula from South of Broad to Calhoun is narrow streets, low oaks, and truck restrictions. A trailer does not go below the Crosstown. The driver meets you at Meeting Street by the Crosstown or at a lot off 26. Harleston Village, Cannonborough, and Wagener Terrace above Calhoun are tight but reachable to the main roads. The Neck from the Crosstown to the old Navy base is wider, and the curb sometimes works.'),
  P('West Ashley across the river is the biggest suburb, from Avondale and Byrnes Downs out to Carolina Bay. The streets are wide and the driver reaches the house. James Island across the Wappoo is the same, from Riverland Terrace to Harbor View. Folly Beach at the end of the road is narrow and sandy. The handoff moves to the Folly Road lots. Johns Island is farm roads turning into subdivisions. Kiawah and Seabrook sit behind gates at the end of Bohicket. The handoff is at the gate or in town.'),
  P('Mount Pleasant across the Cooper is wide and new in Park West, Carolina Park, and Dunes West. The curb works. The Old Village and the new urbanist blocks of I’On are tight. The driver meets you on Coleman Boulevard. Sullivan’s Island and the Isle of Palms are beach lanes over the swing bridge and the connector. The handoff moves to the mainland lots. Daniel Island is a planned grid with its own rules, and the handoff happens at the park lots.'),
  P('North Charleston is Park Circle’s roundabouts, the airport, the plants, and the old Navy base. It is wide almost everywhere. Hanahan and Goose Creek around the weapons station are the same. Summerville up 26 is the fastest-growing town in the state, and its new subdivisions outrun the carrier maps. Send the full address. Ladson, Moncks Corner, and Ravenel ship with the same trucks. All of them price the same as Charleston.'),
 )))

ROUTES=[("Savannah, GA","US-17/I-95 · ~110 mi","Same day","$170–$280"),("Columbia, SC","I-26 · ~115 mi","Same day","$170–$280"),
 ("Augusta, GA","I-26/I-20 · ~150 mi","Same day","$200–$310"),("Charlotte, NC","I-26/I-77 · ~210 mi","Same day","$230–$350"),
 ("Jacksonville, FL","I-95 · ~240 mi","1 day","$250–$380"),("Raleigh, NC","I-95/I-40 · ~280 mi","1 day","$270–$400"),
 ("Atlanta, GA","I-26/I-20 · ~300 mi","1 day","$280–$410"),("Orlando, FL","I-95 · ~380 mi","1 day","$340–$490"),
 ("Washington, DC","I-95 · ~540 mi","1–2 days","$440–$630"),("New York, NY","I-95 · ~760 mi","2 days","$560–$800")]
BODY.append(rate_table('Lanes &amp; Costs','Charleston Car Shipping Lanes and Estimated Costs',
 'The lanes Lowcountry cars run most, with estimated open-trailer ranges. Price your own route on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Charleston for a sedan that runs, on an open trailer. An SUV or a pickup adds about 10 to 25 percent, and enclosed adds more. Storm season and the carriers free on your dates decide the real quote.',
 prose(
  P('Charleston prices among the best on the Southeast coast. The 95 carriers come over on 26 and 17 every day. The port keeps a pool of them based in North Charleston. Savannah and Columbia are short hops and cost the least. The Florida lane rides 95 south and fills each fall with retirees. The New York lane rides 95 north and fills each spring with the families heading home.'),
  P('A report date in July, the August move-in, or a hurricane week lands in the busiest days. The <a href="car-shipping-cost.html">cost guide</a> covers what size, condition, and timing do to the number.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Joint Base, the Port, the Aircraft Plant, the Van Plant, the Medical University, the Colleges, and the Retirees',
 prose(
  L('Charleston relocates airmen, sailors, engineers, residents, cadets, and retirees. The joint base moves more households than anyone.'),
  P('The joint base combines the airlift wing at the airport and the weapons station in Goose Creek. The nuclear school sits on the station. Airmen and sailors rotate on orders all year, with a summer peak. Housing is gated, so the handoff happens outside the gate or at a lot in North Charleston. The orders pay for one car, and the family ships the second one with us. Ship Guy is a private broker and has no tie to the base. The <a href="military-car-shipping.html">military</a> page explains how orders set the timing.'),
  P('The port lands imported cars by the thousand and ships the state’s own cars out the same way. The dealers’ haulers carry those. We do not. A private car that arrived by ship and cleared customs is a domestic move like any other. Give us the release date and the terminal. The aircraft plant by the airport and the van plant up Palmetto Commerce move engineers on program dates. The car plant up 26 in Ridgeville and the parts maker on Dorchester Road do the same. The second car usually rides a trailer.'),
  P('The medical university on the peninsula brings residents each June and hires traveling nurses year round. The college downtown takes student cars in mid-August and sends them home in May. The military college takes its cadets in August, and the campus is closed to a trailer that week. The parent handles the booking, and any adult can sign at the lot. The software companies on Daniel Island relocate staff on offer dates. When an employer reimburses the move, we supply the paperwork it asks for.'),
  P('Retirees arrive from the Northeast and the Midwest every month for Mount Pleasant, Daniel Island, and Summerville. They ship the car ahead of the moving truck. Families priced off the peninsula buy in West Ashley and James Island and ship one car across. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate paperwork.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Bridge Run, Spoleto, Move-In Week, the PCS Season, the Hurricanes, the Evacuations, the King Tides, and the Ice',
 prose(
  L('Charleston runs on a festival calendar and a storm calendar. The weather problem is water from above and water from below.'),
  P('The Bridge Run closes the Ravenel Bridge and the downtown finish for a Saturday morning in early April. Forty thousand runners come, and Mount Pleasant and the peninsula are shut until noon. Spoleto fills downtown from late May into June. The wildlife expo fills it in February and the wine festival in March. Move-in at the college comes in mid-August, and the cadets report the same month. A handoff near any of them moves to the next morning.'),
  P('The base turns over from June through August, and second cars fill the carriers. A July pickup wants three weeks of notice. The Second Sunday closes King Street once a month. The lights at the county park on James Island jam Riverland Drive every evening through December.'),
  P('Hurricane season runs June through November, and the city watches every storm. Hugo in 1989 is still the benchmark. Matthew in 2016, Irma in 2017, and Idalia in 2023 flooded the peninsula and low West Ashley. When the governor orders an evacuation, the state reverses 26 toward Columbia and nothing comes in. A pickup in an evacuation waits for the all-clear, and the carriers stage in Columbia. We tell you the moment a watch is posted.'),
  P('The king tides flood the Crosstown, Lockwood, and the Market on sunny days a dozen times a year. A peninsula handoff checks the tide table. The October 2015 rain put the whole Lowcountry under for a week. Ice comes once every few years. The January 2018 storm dropped five inches and closed the Ravenel and the Don Holt for three days. A winter car waited in Columbia. Summer brings heat and afternoon storms that shift the loading hour.'),
 )+chips(["South of Broad","French Quarter","Harleston Village","Ansonborough","Cannonborough","Radcliffeborough","Wagener Terrace","Hampton Park","The Neck","West Ashley","Avondale","Byrnes Downs","Shadowmoss","Carolina Bay","James Island","Riverland Terrace","Folly Beach","Johns Island","Kiawah","Seabrook","Daniel Island","Mount Pleasant","Old Village","I'On","Park West","Carolina Park","Sullivan's Island","Isle of Palms","North Charleston","Park Circle","Hanahan","Goose Creek","Summerville","Nexton","Ladson","Moncks Corner","Ravenel"])
 +NOTE('Serving Charleston and the whole Lowcountry, South of Broad lane or Summerville cul-de-sac. Tell us the neighborhood and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Charleston?',
 prose(
  L('Open trailers carry most of the cars in the Lowcountry, and the table above is priced for one.'),
  P('An enclosed trailer keeps off the salt air, the pollen, and the debris on 26 after a blow. The collectors South of Broad and on Kiawah book one. So do the retirees bringing a new car down from the Northeast. A car leaving ahead of a hurricane rides whatever is available, and we say so.'),
  P('A daily driver or a student car is fine on an open trailer. Compare the two on the <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A number, a lot in West Ashley or North Charleston, and a signature at delivery. The report date or the move-in picks the week.'),
  P('Approve the price, and a carrier already coming over on 26 that week gets the job. Lot and window are settled by the end of the day. The driver photographs the car at pickup and writes up its condition on the Bill of Lading. You countersign, and the delivery inspection is held to that sheet.'),
 )+ULI([
  "Personal items out of the car, trunk included",
  "Fuel at roughly a quarter tank",
  "Your own photos of each side and the odometer that morning",
  "A working key, plus a word about anything that sticks or leaks",
  "Any add-on alarm turned off",
  "Below the Crosstown, on the beaches, or behind a gate, plan on a lot",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> page walks through the sequence. The <a href="car-shipping-preparation.html">preparation</a> page has the checklist.'))))

BODY.append(sec('Why Ship Guy','Why Charleston Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already come over on 26 and 17 every day. We know which streets end at the Crosstown.'),
  P('Our FMCSA license and our $75,000 bond can be checked on the federal register in a minute. The office is on Gardner Road in West Ashley.'),
  P('The coordinator who quotes the move stays on it until the car is delivered. The <a href="services.html">services</a> page compares open, enclosed, and expedited.'),
 )))

BODY.append(office('Charleston','1064 Gardner Rd Suite 257','Charleston, SC 29407','+18437031419','(843) 703-1419','ET',
 '1064+Gardner+Rd+Suite+257,+Charleston,+SC+29407','Visit Us','Find Ship Guy in Charleston',
 'Our office is on Gardner Road in West Ashley, by the mall on Sam Rittenberg Boulevard.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5122.28956040995!2d-80.0182092!3d32.7995738!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x88fe7d0f5c69d745%3A0xa7ba7edde730c05b!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793300545764!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Charleston to Florida or New York?","Orlando runs three hundred forty to four hundred ninety dollars for a sedan. That is about three hundred eighty miles down 95. New York runs five hundred sixty to eight hundred, about seven hundred sixty miles up the same road. Savannah and Columbia are two hours away and cost the least. Add about 10 to 25 percent for an SUV or a pickup."),
 ("Can the carrier come to my house on the peninsula?","Not below the Crosstown. The streets are narrow, the oaks are low, and the city restricts trucks. The driver meets you at Meeting Street by the Crosstown or at a lot off 26. West Ashley, James Island, North Charleston, Summerville, and the Mount Pleasant subdivisions usually allow the curb."),
 ("Do you handle PCS moves for Joint Base Charleston?","Yes, and summer is the peak. The airlift wing and the weapons station rotate airmen and sailors on orders all year. Housing is gated, so the handoff happens outside the gate or at a lot in North Charleston. The orders pay for one car, and the family ships the second one with us. Ship Guy is a private broker and has no tie to the base."),
 ("Can you pick up a car that came through the port?","Yes, once it has cleared customs and the terminal has released it. From that point it is a domestic move like any other. Give us the release date and the terminal name. The ocean leg is booked separately if you ever need one. The dealers’ haulers carry the new imports, and we do not."),
 ("Do you ship cars for the medical university and the aircraft plant?","Yes, every week. The medical university brings residents each June and hires traveling nurses year round. The aircraft plant, the van plant, and the car plant up 26 move engineers on program dates. The second car usually rides a trailer. Reimbursed by an employer? The paperwork comes from us."),
 ("Can you deliver on a College of Charleston or Citadel move-in date?","Yes. The college takes cars in mid-August and sends them home in May. The cadets report the same month, and the military college is closed to a trailer that week. The parent handles the booking, and any adult can sign at the lot. The date sets the window."),
 ("Can you ship a car to or from Mount Pleasant, Summerville, or Kiawah?","Yes, and all three price the same as Charleston. Mount Pleasant rides the same carriers off 526 at Long Point, and the subdivisions allow the curb. Summerville rides them off 26, and its new streets need the full address. Kiawah sits behind a gate at the end of Bohicket. The handoff is at the gate or in town."),
 ("What happens if a hurricane is coming on my pickup day?","The pickup waits for the all-clear. When the governor orders an evacuation, the state reverses 26 toward Columbia and no carrier comes in. The trucks stage in Columbia and return when the roads reopen. We tell you the moment a watch is posted. A car leaving ahead of the storm rides whatever is available."),
 ("Can you ship a car that does not run from Charleston?","Yes. A carrier with a winch is booked, and the loading time is priced from the start. The mall lots on Sam Rittenberg or the outlet lots at Montague give the driver level ground. Say whether it rolls, steers, and brakes."),
 ("What do you need for a Charleston car shipping quote?","Both addresses, with the neighborhood and which side of the Crosstown or the bridge. The year, make, and model. Whether it runs. Open or enclosed. The week around the report date or the move. Five answers, and a Charleston number is back the same day."),
]
BODY.append(faq_section(FAQ,'Charleston FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Charleston?','Two minutes on the form above gets your lane a Charleston number. Name the neighborhood and the week, and a carrier already coming over on 26 takes it.','+18437031419','(843) 703-1419','Get your free Charleston quote'))

build({
 'slug':'auto-transport-charleston-south-carolina',
 'title':'Car Shipping in Charleston, SC — Auto Transport | Ship Guy',
 'meta':'Car shipping in Charleston, SC, where Interstate 26 ends at the peninsula and the Mark Clark loop ties the Lowcountry together. Joint Base Charleston PCS moves outside the gate, port releases, aircraft plant and medical university relocations, lot handoffs below the Crosstown and behind the gates, curbside pickups in West Ashley, James Island, North Charleston, Summerville, and Mount Pleasant, the hurricanes, and the king tides. Local office on Gardner Road in West Ashley. Free quote.',
 'h1':'Car Shipping in<br>Charleston, <span class="accent">South Carolina</span>',
 'lede':'Open, enclosed, and expedited auto transport across the Lowcountry, planned around 26, the bridges, the Crosstown, the base calendar, the festivals, and hurricane season.',
 'tel':'+18437031419','disp':'(843) 703-1419','brand':'Charleston','keyword':'car shipping in charleston',
 'localterms':['charleston','lowcountry','interstate 26','peninsula','port','mark clark','bridges','gardner road','west ashley','mount pleasant','summerville','islands','columbia','north charleston','crosstown','interstate 526','airport','us 17','ravenel bridge','cooper','savannah highway','rivers avenue','folly road','joint base','aircraft plant','medical university','colleges','hurricanes','king tides','savannah','augusta','charlotte','jacksonville','raleigh','atlanta','orlando','washington','new york','old village','sullivan','gated','james island','ladson','evacuation','ashley','don holt bridge','daniel island','wind','ice','us 52','goose creek','moncks corner','wappoo cut','folly beach','connector','maybank highway','johns island','bohicket','kiawah','seabrook','montague','ashley phosphate','long point','mall','sam rittenberg','outlet','towne centre','big-box','meeting street','single houses','carriages','south of broad','calhoun','oaks','truck restrictions','harleston village','cannonborough','wagener terrace','neck','navy base','avondale','byrnes downs','shadowmoss','carolina bay','riverland terrace','harbor view','sandy','farm roads','park west','carolina park','dunes west','coleman boulevard','isle of palms','swing bridge','park circle','roundabouts','hanahan','weapons station','ravenel','retirees','storm season','airlift wing','nuclear school','airmen','sailors','orders','summer peak','imported cars','customs','release date','terminal','van plant','palmetto commerce','ridgeville','dorchester road','residents','traveling nurses','mid-august','cadets','software','northeast','midwest','bridge run','forty thousand','spoleto','wildlife expo','wine festival','pcs season','second sunday','king street','county park','hugo','1989','matthew','irma','idalia','governor','reverses','lockwood','market','tide table','october 2015','january 2018','five inches','salt air','pollen','bill of lading','fmcsa','french quarter','ansonborough','radcliffeborough','hampton park','nexton','winch'],
}, BODY, FAQ)
