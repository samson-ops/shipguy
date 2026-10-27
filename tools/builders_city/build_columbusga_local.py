import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Columbus, Georgia','Car shipping on the Chattahoochee, at the end of Interstate 185 and the gate of Fort Moore',
 ['Car shipping in Columbus starts where Interstate 185 ends, at the main gate of the post. Ship Guy is a licensed auto transport broker with an office on 9th Street in Uptown.',
  'We book vetted carriers across the river valley, from Harris County to Cusseta and across into Alabama. We do not own the trucks.',
  'Interstate 185 drops south from Interstate 85 at LaGrange and runs the length of the city. The J.R. Allen Parkway crosses the north side into Phenix City. Manchester Expressway, Macon Road, and Veterans Parkway carry the rest. Victory Drive runs to the post.',
  'This page covers the spur, the bypass, Uptown, the historic blocks, the hills, and the Alabama side. It also covers the post, the insurer, the payments campus, the hospitals, the river, and the lanes.'],
 'Columbus at a glance',
 ['Most pickups happen within 1 to 3 days. Interstate 185 brings the Atlanta carriers down to the post all week.',
  'Atlanta, Macon, and Montgomery are same-day lanes. Birmingham and Tallahassee are the same day too. Savannah, Jacksonville, and Charlotte take a day. Dallas and the Texas posts take two.'],
 'Tell us the neighborhood and the gate. Uptown, the Historic District, and Lakebottom need a meeting spot. North Columbus, Midland, and the Phenix City grids usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 185, the J.R. Allen Parkway, Manchester Expressway, and Victory Drive',
 prose(
  L('Columbus has one interstate, and it exists to reach the post. Everything else is a state highway.'),
  P('Interstate 185 leaves Interstate 85 at LaGrange and runs seventy miles south to the city. It passes the mall, crosses Macon Road, and ends at the post. The ramps at Manchester Expressway, Macon Road, and Buena Vista Road are the way into the neighborhoods. Carriers from Atlanta take it, and carriers from Alabama cross the river on US 80.'),
  P('The J.R. Allen Parkway is US 80, the north bypass. It carries the through trucks from Phenix City to the Macon side without touching the city. Manchester Expressway is the east-west strip past the mall. Veterans Parkway runs the length of the city along the river.'),
  P('Victory Drive is US 27 and US 280 south of downtown, and it runs to the main gate. Buena Vista Road and Macon Road reach the east side. The Fall Line Freeway leaves for Macon. The 13th Street and 14th Street bridges cross into Phenix City. The Alabama side rides the same carriers.'),
  P('The carriers come off 185 at Manchester, Macon Road, and Victory Drive. The lots at the mall, along Manchester Expressway, and at Columbus Park Crossing are the usual meeting spots. No road in the valley charges a toll.'),
  P('Our office sits on 9th Street in Uptown, a block from Broadway and the river.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Uptown, the Historic District, Lakebottom, North Columbus, and the Alabama Side',
 prose(
  L('Columbus is a mill town turned payments town, laid out along the river in long north-south blocks.'),
  P('Uptown has Broadway, a wide street with a median, and a trailer can stop on it. The Historic District behind it has narrow blocks and old trees. The driver meets you on Broadway, on Veterans Parkway, or at a lot by the river. The campus along the river has lots of its own.'),
  P('Lakebottom, Wynnton, Overlook, and Hilton Heights are the old neighborhoods on the hill. Their streets are narrow and shaded, and the driver meets you on Wynnton Road or 13th Street. Midtown along Macon Road is a postwar grid where the truck usually reaches the curb.'),
  P('North Columbus, Green Island Hills, and Midland are newer subdivisions with wide streets and some gates. The curb works on most of them, and the gated ones meet the driver at the entrance. Fortson and Harris County are farther out with long drives and open roads.'),
  P('South Columbus and the blocks around the post are flat grids with room to stop. Cusseta sits south of the post with the same answer. Phenix City and Smiths Station across the river are open grids. The casino lot by the bridge works for a handoff.'),
 )))

ROUTES=[("Atlanta, GA","I-185/I-85 · ~110 mi","Same day","$160–$260"),("Macon, GA","US-80/SR-540 · ~95 mi","Same day","$150–$240"),
 ("Montgomery, AL","US-80 · ~90 mi","Same day","$150–$240"),("Birmingham, AL","US-280 · ~170 mi","Same day","$190–$300"),
 ("Tallahassee, FL","US-27/I-10 · ~190 mi","Same day","$200–$320"),("Savannah, GA","SR-540/I-16 · ~260 mi","1 day","$250–$370"),
 ("Jacksonville, FL","I-75/I-10 · ~300 mi","1 day","$280–$410"),("Charlotte, NC","I-85 · ~350 mi","1 day","$320–$460"),
 ("Orlando, FL","I-75/Turnpike · ~430 mi","1 day","$380–$540"),("Dallas, TX","I-20 · ~800 mi","2 days","$560–$820")]
BODY.append(rate_table('Lanes &amp; Costs','Columbus Car Shipping Lanes and Estimated Costs',
 'Where valley cars go most often, with estimated open-trailer ranges. The form above prices your exact route.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates, priced from Columbus for a sedan that runs, open trailer. SUVs and pickups run roughly 10 to 25 percent higher, enclosed higher still. The class cycles, the storms, and the carriers free on your dates set the final figure.',
 prose(
  P('Columbus prices a little above Atlanta on most lanes. The carrier comes seventy miles down the spur to reach it. The post keeps the Texas, Carolina, and Kentucky lanes busy all year. Alabama lanes ride US 80 and US 280 straight west.'),
  P('Florida runs full in both snowbird seasons. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','Fort Moore, the Insurer, the Payments Campus, and the Hospitals',
 prose(
  L('Columbus relocates soldiers, families, underwriters, and programmers, and the post calendar runs the year.'),
  P('Fort Moore trains infantry and armor soldiers on class cycles that never stop. Drill sergeants, instructors, and their families rotate in on orders year round. Graduation weeks bring thousands of families to town. The orders move one car, and the family car comes with us.'),
  P('Because the gates stop the truck, the handoff happens on Victory Drive or at the mall. Ship Guy is a private broker and has no tie to the post. The <a href="military-car-shipping.html">military</a> page explains the report-date timing.'),
  P('The insurer headquartered on Wynnton Road and the payments company in Uptown bring in staff from every state. The bank headquartered in Uptown does the same. Start dates cluster in January and summer. We supply the paperwork a reimbursed move needs.'),
  P('The two hospital systems bring in nurses and residents every summer. The university brings cars in each August, and the campus lots along the river work for the handoff. An adult signs for a student car. The auto plant up Interstate 85 in West Point hires on program schedules.'),
  P('Families move in from Alabama and Florida for the jobs, and the second car usually rides a truck. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Graduation Weeks, Storms, the River, and the Heat',
 prose(
  L('Columbus runs on the post calendar and the Gulf weather, and both change where a truck can stop.'),
  P('Graduation weeks at the post fill every hotel from Columbus to Phenix City. Victory Drive and the gate roads crawl on those Thursdays and Fridays. A pickup near the post moves to another day or an early hour.'),
  P('Tornado warnings and hail arrive with the spring, March through May. The driver waits out a warning before loading. July and August thunderstorms push loading to the early hours. The humidity sits on the valley all summer.'),
  P('Hurricane remnants cross the valley a few times a decade. Michael in 2018 brought tropical winds and downed trees. The carriers hold until the roads are cleared. Ice reaches Columbus less often than Atlanta, but a glaze shuts the hills for a day.'),
  P('The river rises after a wet spring, and the lots by the whitewater course close. A riverside pickup moves up the hill to Uptown. The steeplechase fills Harris County on a Saturday in November. Market days close Broadway on Saturday mornings.'),
 )+chips(["Uptown","Broadway","Historic District","RiverWalk","Lakebottom","Wynnton","Overlook","Hilton Heights","Midtown","East Highland","Rose Hill","Bibb City","North Columbus","Green Island Hills","Bradley Park","Midland","Fortson","Cataula","Pine Mountain","South Columbus","Oakland Park","Benning Hills","Fort Moore","Cusseta","Columbus Park Crossing","Phenix City","Smiths Station","Ladonia"])
 +NOTE('Serving Columbus, Phenix City, and every town in the valley. Name the neighborhood and the gate, and say whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Columbus?',
 prose(
  L('Most cars leave the valley on an open trailer, and the PCS lanes are priced that way.'),
  P('A closed trailer shields a car from pollen, hail, and curious eyes. Soldiers moving a restored car across the country tend to book one. The garages in Green Island Hills book them for the shows.'),
  P('A daily driver or a work truck rides open without trouble. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain the difference.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff on Victory Drive or at the mall, and a delivery. The class cycle sets the week.'),
  P('Once you approve the price, a carrier already coming down 185 is assigned. The meeting spot and the window are set the same day. At the handoff, the driver notes the car’s condition on a Bill of Lading while you watch. Your signature and the driver’s go on it, and it reappears at delivery.'),
 )+ULI([
  "Empty the car of personal items",
  "Leave about a quarter tank of fuel",
  "Photograph the car before pickup",
  "Hand over a working key and mention any mechanical issue",
  "Disable any aftermarket alarm",
  "Near the post, plan to meet the truck outside the gate on Victory Drive",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages walk through the rest.'))))

BODY.append(sec('Why Ship Guy','Why Columbus Drivers Choose Ship Guy',
 prose(
  L('We bring the Atlanta carriers down the spur and plan around the gates, the graduations, and the storms.'),
  P('Our brokerage license with the FMCSA is current, and a $75,000 surety bond sits behind it. The federal register shows both. Our office is on 9th Street in Uptown.'),
  P('The coordinator who quotes your move is the one who sees it delivered. Open, enclosed, and expedited transport are all on the <a href="services.html">services</a> page.'),
 ), alt=True))

BODY.append(office('Columbus','18 9th St #574','Columbus, GA 31901','+17068138084','(706) 813-8084','ET',
 '18+9th+St+%23574,+Columbus,+GA+31901','Visit Us','Find Ship Guy in Columbus',
 'Our office is on 9th Street in Uptown, a block from Broadway and the RiverWalk.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5176.685947071903!2d-84.99226039999999!3d32.462525799999995!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x888ccdf03b72342f%3A0x3a366edba57aea16!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792162195238!5m2!1sen!2sus'))

FAQ=[
 ("Do you handle a PCS move to Fort Moore?","Yes, on every class cycle. Orders cover one car, and the second one comes with us. The gates stop the truck, so we meet you on Victory Drive or at the mall. The pickup is timed to your report date. Ship Guy is a private broker and is not affiliated with the post."),
 ("How much does it cost to ship a car from Columbus to Atlanta or Texas?","Atlanta runs one hundred sixty to two hundred sixty dollars for a sedan. That is about one hundred ten miles up 185 and 85. Dallas runs five hundred sixty to eight hundred twenty, about eight hundred miles out Interstate 20. The Texas posts price about the same. SUVs and pickups add 10 to 25 percent."),
 ("Can you ship a car to or from the Alabama side of the river?","Yes, and it prices the same. Phenix City, Smiths Station, and Ladonia ride the same carriers as Columbus. The casino lot by the bridge and the lots on US 280 work for a handoff. The state line changes the paperwork, not the price."),
 ("Can the carrier come into the Historic District or Lakebottom?","Usually not. The Historic District blocks are narrow, and Lakebottom streets are shaded and tight. The driver meets you on Broadway, on Wynnton Road, or at a lot by the river. North Columbus, Midland, and Midtown usually allow the curb."),
 ("Does graduation week at the post affect my pickup?","If you live near the post, yes. Thousands of families arrive on graduation Thursdays and Fridays, and Victory Drive crawls. We move a pickup near the gates to another day or an early hour. The north side of the city runs normally."),
 ("Do you ship cars for employees relocating to the insurer or the payments company?","Yes, all year, with peaks in January and summer. Both bring in staff from every state on start dates, and many ship a second car. We provide the paperwork for a reimbursed move. The handoff works in Uptown or at the mall."),
 ("What happens if a storm hits on my pickup day?","A tornado warning holds the driver until the all-clear. Hurricane remnants close roads with downed trees a few times a decade. The carriers wait for the clearing. An ice glaze shuts the hills for a day. We call before the window moves."),
 ("Can you ship a car for a Columbus State student?","Yes. Cars arrive each August and leave each May, and both windows book up early. The campus lots along the river and on the main campus work for the handoff. A parent or another adult signs at pickup."),
 ("Can you ship a car that does not run from Columbus?","Yes. The carrier arrives with a winch, and the quote already covers the slower loading. Pick a flat, open spot, which usually means a lot on Manchester Expressway or at the mall. Let us know if it rolls, steers, and brakes."),
 ("What do you need for a Columbus car shipping quote?","An origin and a destination, with the gate or the neighborhood on the Columbus end. The vehicle’s year, make, and model, and whether it runs. Open or enclosed. A date range that respects the report date or the class cycle. Nothing else is needed."),
]
BODY.append(faq_section(FAQ,'Columbus FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Columbus?','The form above prices your lane in about two minutes. Tell us the gate or the neighborhood and your dates. A carrier already on 185 handles the rest.','+17068138084','(706) 813-8084','Get your free Columbus quote'))

build({
 'slug':'auto-transport-columbus-georgia',
 'title':'Car Shipping in Columbus, GA — Auto Transport | Ship Guy',
 'meta':'Car shipping in Columbus, GA at the end of Interstate 185 and the gate of Fort Moore. PCS second cars and gate handoffs on Victory Drive, Uptown and Lakebottom meeting spots, North Columbus curbside, the Alabama side, insurer and payments relocations, graduation-week planning. Local office on 9th Street in Uptown. Free quote.',
 'h1':'Car Shipping in<br>Columbus, <span class="accent">Georgia</span>',
 'lede':'Open, enclosed, and expedited auto transport across the river valley, both sides of the line, planned around 185, the gates, and the storms.',
 'tel':'+17068138084','disp':'(706) 813-8084','brand':'Columbus','keyword':'car shipping in columbus',
 'localterms':['columbus','interstate 185','interstate 85','lagrange','j.r. allen parkway','us 80','manchester expressway','macon road','veterans parkway','victory drive','us 27','us 280','buena vista road','fall line freeway','13th street','14th street','uptown','broadway','historic district','river','lakebottom','wynnton','overlook','hilton heights','midtown','north columbus','green island hills','midland','fortson','harris county','south columbus','cusseta','phenix city','smiths station','ladonia','casino','mall','columbus park crossing','fort moore','class cycles','graduation','orders','report date','insurer','payments','bank','hospital','nurses','residents','university','west point','auto plant','tornado','hail','thunderstorms','humidity','michael','2018','ice','steeplechase','whitewater','market days','atlanta','macon','montgomery','birmingham','tallahassee','savannah','jacksonville','charlotte','orlando','dallas','texas','alabama','florida'],
}, BODY, FAQ)
