import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Kansas City, Missouri','Car shipping from the middle of the map, on both sides of the state line',
 ['Car shipping in Kansas City starts at the center of the country, where four interstates cross and every long-haul carrier passes through.',
  'Ship Guy is a licensed auto transport broker with an office on Madison Avenue near the Plaza. We book vetted carriers on both sides of the state line, and we do not own the trucks.',
  'Interstate 70 crosses from Denver to Saint Louis, Interstate 35 runs from Oklahoma to Des Moines, Interstate 29 climbs to Omaha, and Interstate 49 drops toward Arkansas. Interstate 435 loops the whole metro across two states.',
  'This page covers the interstates and the loop, the two-state metro, the neighborhoods, the two assembly plants, the post and the base, the campuses, and the winter that decides the timing.'],
 'Kansas City at a glance',
 ['Most pickups happen within 1 to 3 days, with four interstates bringing carriers through the metro.',
  'Saint Louis, Wichita, Omaha, and Des Moines are same-day lanes. Chicago, Dallas, Denver, and Minneapolis take one to two days. The coasts run three to four.'],
 'Tell us which side of the state line you are on. Overland Park and Independence are the same metro and the same carrier pool, but the paperwork names a state.'))

BODY.append(sec('The Interstates','Interstate 70, 35, 29, 49, and the 435 Loop',
 prose(
  L('Kansas City is the most connected city between Chicago and Denver, and carriers treat it as a hub.'),
  P('Interstate 70 carries the Denver-to-Saint Louis lane through the middle of the city and past the stadium complex. Interstate 35 carries the Oklahoma-to-Minneapolis lane through downtown and the Kansas suburbs, and the two cross a mile from the river.'),
  P('Interstate 29 runs north past the airport to Omaha, and Interstate 49 runs south through Grandview toward Joplin and Arkansas. Interstate 435 loops the metro through both states, and Interstate 470 and 635 fill in the corners.'),
  P('The downtown loop is a tangle of ramps, and a loaded trailer stays on the outer loop. Carriers reach any suburb from Interstate 435 in twenty minutes outside rush hour.'),
  P('Because so many lanes cross here, Kansas City pricing runs close to the big Midwest hubs despite the smaller metro.'),
 ), alt=True))

BODY.append(sec('Two States, One Metro','The State Line, Johnson County, and the Northland',
 prose(
  L('Half the metro lives in Kansas, and the state line runs down the middle of a city street.'),
  P('Overland Park, Olathe, Leawood, Lenexa, and Shawnee in Johnson County are wide suburbs with subdivisions and homeowners associations, and many have gates. Kansas City, Kansas, and Wyandotte County sit north of them along the river.'),
  P('On the Missouri side, Lee\u2019s Summit, Blue Springs, Independence, and Raytown stretch east along Interstate 70. The Northland across the river holds Liberty, Parkville, and Platte City near the airport.'),
  P('The new airport terminal on the north side makes fly-and-ship routine. A carrier meets you at a lot near the terminal, and the car is on the truck the same day.'),
  P('If your employer reimburses the shipment, we provide the documentation. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side of a relocation.'),
 )))

ROUTES=[("Wichita, KS","I-35 · ~200 mi","Same day","$220–$340"),("Omaha, NE","I-29 · ~190 mi","Same day","$220–$340"),
 ("Des Moines, IA","I-35 · ~195 mi","Same day","$220–$340"),("St. Louis, MO","I-70 · ~250 mi","Same day","$250–$380"),
 ("Oklahoma City, OK","I-35 · ~350 mi","1 day","$320–$460"),("Minneapolis, MN","I-35 · ~440 mi","1 day","$380–$540"),
 ("Chicago, IL","I-35/I-80 · ~510 mi","1–2 days","$430–$620"),("Dallas, TX","I-35 · ~550 mi","1–2 days","$430–$620"),
 ("Denver, CO","I-70 · ~600 mi","2 days","$450–$650"),("Los Angeles, CA","I-70/I-15 · ~1,600 mi","4 days","$950–$1,350")]
BODY.append(rate_table('Lanes &amp; Costs','Kansas City Car Shipping Lanes and Estimated Costs',
 'The lanes Kansas City households ask about most, with estimated open-transport ranges from either side of the state line. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates, running sedan, open trailer. SUVs and pickups run about 10 to 25 percent more, enclosed more still. Winter and carrier availability on your dates set the real quote.',
 prose(
  P('Every neighboring hub is a same-day lane, because the interstates that reach them all leave from here. Chicago and Dallas are a day away on roads carriers run constantly.'),
  P('Denver on Interstate 70 crosses four hundred miles of open plains and swings with the weather. The <a href="car-shipping-cost.html">cost guide</a> explains the rest of the number.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','The Plaza, Brookside, Waldo, and the Old Streets',
 prose(
  L('Kansas City\u2019s oldest neighborhoods were built for streetcars, and its newest were built for trucks.'),
  P('The Plaza, Westport, Brookside, Waldo, and Hyde Park have narrow streets, alleys, and old trees. The driver meets you on Ward Parkway, Main Street, or a main road nearby, a few minutes from the house.'),
  P('Downtown, the Crossroads, and the River Market run on parking garages a trailer cannot enter. The handoff happens at a lot near the loop.'),
  P('The suburbs on both sides are wide, and the truck usually reaches the curb. Send the subdivision name and a gate code where there is one.'),
  P('Our office is on Madison Avenue near the Plaza, minutes from Interstate 35 and the state line.'),
 )))

BODY.append(sec('The Plants, the Post, and the Base','Claycomo, Fairfax, Fort Leavenworth, and Whiteman',
 prose(
  L('Kansas City builds vehicles on both sides of the river, and it trains officers and flies bombers within an hour.'),
  P('The assembly plant in Claycomo builds trucks and vans on the Missouri side, and the plant in the Fairfax district builds cars on the Kansas side. Both load car haulers every day, and those carriers take private cars on the return run.'),
  P('Fort Leavenworth sits thirty miles up the river and hosts the Army\u2019s staff college, which rotates a new class of officers each summer. Whiteman Air Force Base flies stealth bombers an hour east near Knob Noster and rotates airmen on the same calendar.'),
  P('The federal security campus on the south side relocates engineers on program schedules. Housing at the post and the base is gated, so the driver meets you outside it, and many families ship a second vehicle through us since orders may cover only one.'),
  P('Ship Guy is a private broker with no military affiliation. Our <a href="military-car-shipping.html">military</a> page covers PCS timing.'),
 ), alt=True))

BODY.append(sec('The Campuses &amp; the Employers','UMKC, Lawrence, and the Headquarters',
 prose(
  L('The metro sends students west and brings engineers in from everywhere.'),
  P('The University of Kansas in Lawrence sits forty minutes west on Interstate 70, and its August move-in and May move-out fill the town. The city university on the Missouri side, the Jesuit college nearby, and the medical center in Kansas run the same calendar.'),
  P('Campus streets are tight, so the driver meets you at a lot nearby, and an adult signs for a student car.'),
  P('The health-technology campus, the navigation-device maker in Olathe, the wireless headquarters in Overland Park, and the greeting-card company downtown relocate employees on start dates all year.'),
  P('Chiefs home Sundays fill the stadium complex on Interstate 70 from early morning, and we schedule the east side around them. The Royals draw smaller crowds on the same lots.'),
 )+chips(["Downtown","Crossroads","River Market","Westport","The Plaza","Brookside","Waldo","Hyde Park","Northland","Liberty","Parkville","Platte City","Independence","Raytown","Lee's Summit","Blue Springs","Grandview","Overland Park","Olathe","Leawood","Lenexa","Shawnee","Prairie Village","Kansas City KS","Lawrence","Leavenworth"])
 +NOTE('Serving the whole metro on both sides of the state line, plus Lawrence, Leavenworth, and Saint Joseph. Tell us the state and the subdivision name.')))

BODY.append(sec('Weather','Ice, Snow, Tornadoes, and the River',
 prose(
  L('Kansas City gets every season in full, and the ice is the one that stops a truck.'),
  P('Ice storms glaze the metro a few times each winter, and no one moves a loaded trailer on it. Snow closes Interstate 70 across the plains to the west for a day at a time from December through March, and carriers wait for the plows.'),
  P('Tornado season runs March through June, and when a warning is issued, the driver pulls off and waits. Hail in the same months can dent a car waiting outside.'),
  P('Summer heat passes a hundred degrees, and the rivers flood the bottoms in a wet spring. We tell you the moment the forecast changes the plan.'),
 ), alt=True))

BODY.append(sec('Your Options','Open or Enclosed in Kansas City?',
 prose(
  L('Open transport is the everyday choice, and the hub lanes run on it.'),
  P('Enclosed transport keeps a car covered against road salt, hail, and the grit of the plains. Mission Hills, Hallbrook, and the Ward Parkway estates keep enclosed carriers busy with collector cars.'),
  P('A commuter car rides open without trouble outside hail season. Our <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages describe both.'),
 )))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a loading on the loop, and a delivery, with the winter deciding the timing.'),
  P('When the price is approved, a carrier crossing on Interstate 70 or 35 takes the booking. The driver records the car\u2019s condition on a Bill of Lading, and you sign before it loads. That record is your reference at delivery.'),
 )+ULI([
  "Remove personal belongings",
  "Keep about a quarter tank of fuel",
  "Photograph the vehicle before pickup, especially after a salty winter",
  "Provide a working key and disclose mechanical issues",
  "Disable aftermarket alarms",
  "For an old-street address or a gated subdivision, plan to meet the truck on the main road",
 ])+prose(P('Our <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> guides cover each step.')), alt=True))

BODY.append(sec('Why Ship Guy','Why Kansas City Drivers Choose Ship Guy',
 prose(
  L('We use the traffic that already crosses at the center of the map and plan around the ice and the state line.'),
  P('Active FMCSA brokerage authority and a $75,000 surety bond back every Ship Guy booking, and our office is on Madison Avenue.'),
  P('One coordinator handles the shipment from quote to delivery and can set up open, enclosed, or expedited transport. The <a href="services.html">services</a> page shows the full range.'),
 )))

BODY.append(office('Kansas City','4600 Madison Ave Ste 497','Kansas City, MO 64112','+18166563244','(816) 656-3244','CT',
 '4600+Madison+Ave+Ste+497,+Kansas+City,+MO+64112','Visit Us','Find Ship Guy in Kansas City',
 'Our office is on Madison Avenue near the Country Club Plaza, minutes from Interstate 35 and the state line.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3824.9883252117365!2d-94.5977995!3d39.0443955!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x87c0ef5297488391%3A0x5519e3b823ed1880!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1790274910315!5m2!1sen!2sus'))

FAQ=[
 ("Do you serve the Kansas side of the metro?","Yes, Overland Park, Olathe, Leawood, Lenexa, Shawnee, and Kansas City, Kansas, are the same carrier pool as the Missouri side. The price does not change across the state line. The paperwork names a state, so tell us which one when you book."),
 ("How much does it cost to ship a car from Kansas City to Denver or Chicago?","Denver usually runs four hundred fifty to six hundred fifty dollars for a sedan, about six hundred miles on Interstate 70. Chicago runs four hundred thirty to six hundred twenty, about five hundred ten miles. The Denver lane swings with the weather on the plains. Larger vehicles add 10 to 25 percent."),
 ("Can you handle a PCS move to Fort Leavenworth or Whiteman?","Yes, the staff college at Leavenworth rotates a new class of officers each summer, and Whiteman rotates airmen on the same calendar. Housing is gated, so the driver meets you outside it. Many families ship a second vehicle through us, since orders may cover only one. Ship Guy has no military affiliation."),
 ("Can the carrier come to my house in Brookside or Waldo?","Not down the old streets. Brookside, Waldo, Westport, and Hyde Park have narrow streets, alleys, and old trees, so the driver meets you on Ward Parkway, Main Street, or a main road nearby. The suburbs on both sides usually allow curbside."),
 ("Does a Chiefs home game affect my pickup?","On the east side, yes. The stadium complex on Interstate 70 fills from early morning on a home Sunday, and the roads around it crawl. We schedule Independence, Raytown, and the east side around the games. The rest of the metro runs normally."),
 ("Can you ship a car for a KU or UMKC student?","Yes, student cars move each August and again in May. Lawrence fills on move-in weekend, and campus streets on both sides of the line are tight, so the driver meets you at a lot nearby. An adult signs for the car. Winter arrivals need a strong battery."),
 ("What happens if an ice storm hits during my shipment?","Carriers wait it out. Ice glazes the metro a few times each winter, and no one moves a loaded trailer on it. Snow can also close Interstate 70 across the plains for a day. We tell you the moment the forecast changes the plan and reschedule when the roads clear."),
 ("Can you meet me at the airport?","Yes, the new terminal on the north side makes fly-and-ship routine. The driver meets you at a lot near the terminal off Interstate 29, and the car is on the truck the same day. Tell us the flight time when you book."),
 ("Can you ship a car that does not run from Kansas City?","Yes, non-running cars ship out of Kansas City every week. A winch-equipped carrier loads it, and the added time carries a fee. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Kansas City car shipping quote?","The pickup and delivery addresses, with the state and the subdivision name. The year, make, and model. Whether it runs and rolls. Open or enclosed, and your dates. That is everything an accurate Kansas City quote needs."),
]
BODY.append(faq_section(FAQ,'Kansas City FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Kansas City?','A quote takes about two minutes on our form. Then tell us your side of the line and your dates, and we will match you with a carrier already crossing the metro.','+18166563244','(816) 656-3244','Get your free Kansas City quote'))

build({
 'slug':'auto-transport-kansas-city-missouri',
 'title':'Car Shipping in Kansas City, MO — Auto Transport | Ship Guy',
 'meta':'Car shipping in Kansas City, MO where Interstate 70, 35, 29, and 49 cross. Both sides of the state line, Plaza and Brookside handoffs, the Claycomo and Fairfax plants, Fort Leavenworth and Whiteman moves, KU and UMKC timing, ice-storm planning. Local office on Madison Avenue. Free quote.',
 'h1':'Car Shipping in<br>Kansas City, <span class="accent">Missouri</span>',
 'lede':'Open, enclosed, and expedited auto transport across the two-state metro, planned around the loop, the line, and the winter.',
 'tel':'+18166563244','disp':'(816) 656-3244','brand':'Kansas City','keyword':'car shipping in kansas city',
 'localterms':['kansas city','metro','state line','interstate 70','interstate 35','interstate 29','interstate 49','interstate 435','interstate 470','loop','johnson county','overland park','olathe','leawood','lenexa','shawnee','wyandotte','lee\u2019s summit','blue springs','independence','raytown','northland','liberty','parkville','platte city','airport','terminal','plaza','westport','brookside','waldo','hyde park','ward parkway','crossroads','river market','claycomo','fairfax','plant','fort leavenworth','staff college','whiteman','bomber','security campus','lawrence','ku','umkc','chiefs','stadium','royals','ice','tornado','hail','madison avenue'],
}, BODY, FAQ)
