import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Support")]))

BODY.append(intro_block('Texas','Texas auto transport across a state the size of a country, and the corners the city pages miss',
 ['Texas auto transport is the busiest state market in the country, and the four big metros are only part of it.',
  'Ship Guy is a licensed auto transport broker. We book vetted carriers across Texas, and we do not own the trucks.',
  'Interstate 35 runs from Laredo through San Antonio, Austin, and Dallas to Oklahoma. Interstate 10 crosses from El Paso through San Antonio to Houston and Louisiana, Interstate 20 crosses from the Permian Basin to Dallas, and Interstate 45 links Houston and Dallas.',
  'This page covers the corridors, the seven cities with their own pages, the Rio Grande Valley and the winter Texans, the border, the Permian Basin, the Panhandle, the posts, the Gulf, and the ice.'],
 'Texas at a glance',
 ['Most pickups happen within 1 to 3 days in the metros and along Interstate 35, 10, 20, and 45, and within 2 to 5 days in the Permian Basin, the Panhandle, Big Bend, and the Valley.',
  'Oklahoma City, Little Rock, Shreveport, and New Orleans are same-day lanes from one metro or another. Denver, Albuquerque, Memphis, and Atlanta take a day or two. The coasts run three.'],
 'Dallas, Fort Worth, Arlington, Houston, Austin, San Antonio, and El Paso have their own pages. This page carries the Valley, Corpus Christi, the Permian Basin, Lubbock, Amarillo, Waco, College Station, Killeen, and the rest.'))

BODY.append(sec('The Corridors','Interstate 35, 10, 20, 45, 30, 37, 27, and 69',
 prose(
  L('Texas has more interstate miles than any state, and the carriers use every one of them.'),
  P('Interstate 35 is the spine, from the Laredo border through San Antonio, Austin, Waco, and the Metroplex to Oklahoma. It carries more freight than any road in the state, and a car near it schedules in a day.'),
  P('Interstate 10 crosses the south from El Paso through the Hill Country, San Antonio, Houston, and Beaumont to Louisiana. Interstate 20 crosses the north from the Permian Basin through Abilene and the Metroplex to Shreveport.'),
  P('Interstate 45 links Houston to Dallas, Interstate 30 links Dallas to Texarkana, and Interstate 37 links San Antonio to Corpus Christi. Interstate 27 runs from Lubbock to Amarillo, Interstate 40 crosses the Panhandle, and Interstate 69 reaches the Valley.'),
  P('The toll roads around the metros are built into every quote. Big Bend, the Panhandle counties, and the ranch country take an extra day or two.'),
 ), alt=True))

BODY.append(state_cities_block('TX','Texas','Seven Texas cities have their own pages with local lanes, meeting spots, and phone lines. The Valley, Corpus Christi, the Permian Basin, Lubbock, Amarillo, Waco, College Station, Killeen, and the rest of Texas are covered from this page.'))

BODY.append(sec('The Valley &amp; the Border','Winter Texans, Laredo, and the Line We Do Not Cross',
 prose(
  L('The Rio Grande Valley fills with retirees every winter, and the border towns move more freight than any crossing in the country.'),
  P('McAllen, Harlingen, Brownsville, and the Valley draw winter Texans from the Midwest and Canada from October through March. They ship cars down in the fall and home in the spring, and Interstate 69 and US 281 carry the lane.'),
  P('Laredo is the largest inland port in the country, and thousands of trucks cross daily. A private pickup there slots into that flow, and Interstate 35 runs straight to San Antonio.'),
  P('A vehicle moving into Mexico is an international shipment with customs paperwork and a different carrier. We arrange domestic shipping only, and we deliver to the border towns on the Texas side.'),
  P('The Valley\u2019s colonias and farm roads sit on caliche and gravel, and the driver meets you on the US highway or in town. Our <a href="snowbird-car-shipping.html">snowbird</a> page covers the winter Texan lane.'),
 )))

ROUTES=[("Oklahoma City, OK (from Dallas)","I-35 · ~205 mi","Same day","$230–$350"),("New Orleans, LA (from Houston)","I-10 · ~350 mi","1 day","$320–$470"),
 ("Little Rock, AR (from Dallas)","I-30 · ~320 mi","1 day","$300–$440"),("Albuquerque, NM (from El Paso)","I-25 · ~265 mi","1 day","$250–$380"),
 ("Memphis, TN (from Dallas)","I-30/I-40 · ~450 mi","1–2 days","$400–$570"),("Denver, CO (from Dallas)","US-287/I-25 · ~800 mi","2 days","$560–$820"),
 ("Phoenix, AZ (from El Paso)","I-10 · ~430 mi","1 day","$380–$540"),("Atlanta, GA (from Houston)","I-10/I-65/I-85 · ~790 mi","2 days","$550–$800"),
 ("Chicago, IL (from Houston)","I-45/I-55 · ~1,080 mi","3 days","$780–$1,100"),("Los Angeles, CA (from Dallas)","I-20/I-10 · ~1,435 mi","3 days","$900–$1,250")]
BODY.append(rate_table('Lanes &amp; Costs','Texas Car Shipping Lanes and Estimated Costs',
 'The lanes Texas households ask about most, priced from the nearest big metro. The city pages carry the full tables for each metro. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a running sedan on an open trailer. SUVs and pickups add about 10 to 25 percent, enclosed more. Toll roads are included, and season plus carrier availability on your dates set the real quote.',
 prose(
  P('Texas-to-Texas moves between the metros are the cheapest lanes in the state, because carriers run Interstate 35, 10, and 45 all day. Oklahoma, Louisiana, and New Mexico follow.'),
  P('The Permian Basin, the Panhandle, and Big Bend cost more per mile because the carrier detours. The <a href="car-shipping-cost.html">cost guide</a> explains the other variables.'),
 ), alt=True))

BODY.append(sec('The Permian &amp; the Panhandle','Midland, Odessa, Lubbock, and Amarillo',
 prose(
  L('West Texas ships on the price of oil and the width of the plains.'),
  P('Midland and Odessa boom and bust with the Permian Basin, and workers ship pickups in and out on hiring cycles. The towns sit on Interstate 20 five hours from Dallas, and pickups run 2 to 5 days.'),
  P('Lubbock ships on the university, the cotton, and the hospitals, with Interstate 27 north to Amarillo. Amarillo sits on Interstate 40 and ships on the cattle, the Denver lane, and the cross-country carriers passing through.'),
  P('Ranch roads across the plains are caliche and gravel, and a seventy-five-foot trailer stays on the pavement. Dust storms and wind slow a high-profile trailer from March through May.'),
  P('Big Bend and the far west from Alpine to Presidio are the most remote places in the state, and pickups there run 4 to 7 days.'),
 )))

BODY.append(sec('The Posts &amp; the Bases','Fort Cavazos, Sheppard, Dyess, Goodfellow, and Corpus Christi',
 prose(
  L('Texas moves more military households than any state but California, and the ones outside the metros are covered here.'),
  P('Fort Cavazos at Killeen is the largest Army post in the country, and it deploys and returns whole divisions. Families rotate year round, with the heaviest moves from May through August, and Killeen sits on Interstate 14 an hour north of Austin.'),
  P('Sheppard in Wichita Falls trains pilots and maintainers on class cycles. Dyess in Abilene flies bombers and airlifters, and Goodfellow in San Angelo trains intelligence and fire specialists.'),
  P('The naval air station in Corpus Christi trains pilots and rotates squadrons, and the Coast Guard adds rotations along the Gulf. Fort Bliss, Lackland, Randolph, and Fort Sam Houston are covered on the El Paso and San Antonio pages.'),
  P('Many families ship a second vehicle through us, since orders may cover only one. Housing is gated at each, so the driver meets you outside it. Ship Guy is a private broker with no military affiliation, and our <a href="military-car-shipping.html">military</a> page covers PCS timing.'),
 ), alt=True))

BODY.append(sec('Campuses &amp; the Coast','College Station, Waco, Lubbock, Corpus Christi, and the Gulf',
 prose(
  L('Texas campuses ship on the same calendar, and the coast ships on the season.'),
  P('Texas A&M in College Station is one of the largest campuses in the country, and move-in week fills every road into town. Baylor in Waco, Texas Tech in Lubbock, and the state universities follow the same August and May dates.'),
  P('Home football Saturdays close the streets around each stadium, and we schedule around the games. Campus handoffs happen at a lot nearby, and an adult signs for a student car.'),
  P('Corpus Christi ships on the port, the refineries, and the naval air station, with Interstate 37 to San Antonio. Padre Island and the beach towns fill in summer and spring break, and the driver meets you on the mainland side of the causeway.'),
  P('Beaumont and Port Arthur ship on the refineries and Interstate 10, and Galveston is covered on the Houston page.'),
 )))

BODY.append(sec('Weather','Hurricanes, Ice, Tornadoes, Hail, Floods, and Heat',
 prose(
  L('Texas gets every kind of weather that stops a truck, and it gets each one somewhere every year.'),
  P('Hurricane season runs June through November along the Gulf, and carriers leave the coast days before landfall. Interstate 45 and 10 run contraflow for evacuation, and no truck moves against it.'),
  P('Ice is the quiet one. A winter storm can shut the whole state for days, as it did in 2021, and no one moves a loaded trailer on it. Tornadoes cross the north from March through May, and hail in the Metroplex dents a car waiting outside in minutes.'),
  P('Flash floods hit the Hill Country and the metros after heavy rain, and a low-water crossing waits for the water to drop. Summer passes 100 degrees from June through September, and drivers load early.'),
  P('We tell you the moment the forecast changes the plan, and we never send a driver into an evacuation zone.'),
 )+chips(["McAllen","Harlingen","Brownsville","Laredo","Corpus Christi","Victoria","Beaumont","Port Arthur","Tyler","Longview","Texarkana","Waco","Temple","Killeen","College Station","Bryan","Midland","Odessa","San Angelo","Abilene","Wichita Falls","Lubbock","Amarillo","Kerrville","Fredericksburg","New Braunfels"])
 +NOTE('Serving all two hundred fifty-four Texas counties. For a ranch, Valley, or Big Bend address, tell us the town and the nearest US highway.'), alt=True))

BODY.append(sec('Your Options','Open or Enclosed in Texas?',
 prose(
  L('Open transport is the everyday choice, and the metro lanes run on it by the thousand.'),
  P('Enclosed transport keeps a car covered against hail, sun, and Gulf salt air. Highland Park, River Oaks, and the Hill Country estates keep enclosed carriers busy with collector cars.'),
  P('A commuter car rides open without a problem outside hail season. Our <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages compare both.'),
 )))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a loading on the corridor, and a delivery, with the weather deciding the timing in season.'),
  P('When the price is approved, a carrier on Interstate 35, 10, 20, or 45 takes the booking. The driver writes the car\u2019s condition on a Bill of Lading, and you sign it before loading. That form is your checklist at delivery.'),
 )+ULI([
  "Remove personal belongings",
  "Keep about a quarter tank of fuel",
  "Photograph the vehicle before pickup, roof and hood included",
  "Provide a working key and disclose mechanical issues",
  "Turn off aftermarket alarms",
  "For a ranch or Valley address, plan to meet the truck on the US highway",
 ])+prose(P('Our <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> guides cover each step.')), alt=True))

BODY.append(sec('Why Ship Guy','Why Texas Drivers Choose Ship Guy',
 prose(
  L('We use the busiest carrier market in the country and quote honest windows for the corners of it.'),
  P('Ship Guy holds active FMCSA brokerage authority and a $75,000 surety bond, both verifiable in federal records.'),
  P('One coordinator carries the shipment from quote to delivery and can arrange open, enclosed, or expedited transport. The <a href="services.html">services</a> page lists everything we offer.'),
 )))

FAQ=[
 ("Do you ship cars for winter Texans in the Rio Grande Valley?","Yes, the Valley is one of the busiest seasonal lanes in the state. Retirees from the Midwest and Canada ship cars down from October through December and home from March through May, on Interstate 69 and US 281. Two to three weeks of notice keeps the price steady, and the handoff happens on the US highway or in town."),
 ("Can you ship a car to Mexico from Texas?","No, a move across the border at Laredo, El Paso, or the Valley is an international shipment with customs paperwork and a different carrier. We arrange domestic shipping only. We deliver to the border towns on the Texas side."),
 ("Can you handle a PCS move to Fort Cavazos, Sheppard, or Dyess?","Yes, every Texas installation is a steady lane for us, and the metro bases are covered on the El Paso and San Antonio pages. Many families ship a second vehicle through us, since orders may cover only one. Housing is gated, so the driver meets you outside it. Ship Guy has no military affiliation."),
 ("Why does a pickup in Midland, Odessa, or Big Bend take longer?","Because the Permian Basin sits five hours from Dallas on Interstate 20, and Big Bend sits hours from any interstate at all. Carriers detour to reach them, and pickups run 2 to 5 days in the Basin and 4 to 7 in Big Bend. A flexible date range keeps the price steady."),
 ("How much does it cost to ship a car across Texas?","Dallas to Houston usually runs two hundred fifty to three hundred eighty dollars for a sedan, and Houston to San Antonio two hundred thirty to three hundred fifty. El Paso to Dallas runs four hundred seventy to six hundred eighty, because it is six hundred miles. The city pages carry the full tables for each metro."),
 ("Can you ship a car for a Texas A&M, Texas Tech, or Baylor student?","Yes, student cars move each August and again in May. Move-in week fills every road into College Station, and home football Saturdays close the streets around each stadium, so we schedule around both. The handoff happens at a lot near campus, and an adult signs for the car."),
 ("What happens if a hurricane threatens the Gulf Coast?","Carriers leave the coast days before landfall, and pickups pause. Interstate 45 and 10 run contraflow for evacuation, and no truck moves against it. If you want the car out beforehand, call the moment the track firms up. After a storm, demand rises as people replace flooded cars."),
 ("What happens if an ice storm shuts down Texas?","Carriers wait it out. A winter storm can shut the whole state for days, as it did in 2021, and no one moves a loaded trailer on it. We tell you the moment the forecast changes the plan and reschedule when the roads clear."),
 ("Can you ship a car that does not run?","Yes, non-running cars ship from every part of Texas. A winch-equipped carrier loads it, and the extra time carries a fee. Say whether it can roll, steer, and brake."),
 ("What do you need for a Texas car shipping quote?","Both addresses, with the town and the nearest highway for a ranch or Valley pickup. The year, make, and model. Whether it runs and rolls. Open or enclosed, and a date range. That is a complete Texas quote request."),
]
BODY.append(faq_section(FAQ,'Texas FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book auto transport in Texas?','A quote takes about two minutes. Then tell us your town and dates, and we will match you with a carrier in the busiest market in the country.','+18664992815','(866) 499-2815','Get your free Texas quote'))

build_state({
 'slug':'texas-auto-transport',
 'title':'Texas Auto Transport &amp; Car Shipping | Ship Guy',
 'meta':'Texas auto transport beyond the big four metros. Winter Texans in the Valley, Laredo and the border, the Permian Basin and the Panhandle, Fort Cavazos and the training bases, Texas A&amp;M move-in, Gulf hurricanes and ice, seven Texas city pages. Free quote.',
 'h1':'Texas<br>Auto <span class="accent">Transport</span>',
 'lede':'Open, enclosed, and expedited car shipping across Texas, from the busiest corridors in the country to the corners the maps forget.',
 'brand':'Texas','keyword':'texas auto transport','abbr':'TX',
 'localterms':['texas','interstate 35','interstate 10','interstate 20','interstate 45','interstate 30','interstate 37','interstate 27','interstate 40','interstate 69','interstate 14','us 281','dallas','houston','austin','san antonio','el paso','fort worth','arlington','rio grande valley','mcallen','harlingen','brownsville','winter texan','laredo','border','mexico','corpus christi','padre island','midland','odessa','permian','lubbock','amarillo','panhandle','big bend','waco','college station','texas a&m','killeen','fort cavazos','wichita falls','sheppard','abilene','dyess','san angelo','goodfellow','beaumont','port arthur','hill country','kerrville','hurricane','contraflow','ice','tornado','hail','flash flood','heat'],
}, BODY, FAQ)
