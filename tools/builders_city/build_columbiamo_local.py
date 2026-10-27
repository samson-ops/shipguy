import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Columbia, Missouri','Car shipping halfway between the metros, on the Mizzou calendar',
 ['Car shipping in Columbia runs on one interstate and one university calendar. Ship Guy is a licensed auto transport broker with an office on Green Meadows Road.',
  'We book vetted carriers across mid-Missouri, from Columbia and Jefferson City to Fulton, Boonville, and Ashland. We do not own the trucks.',
  'Interstate 70 crosses the north side of the city two hours from each metro. US 63 runs south to the capital and north to Kirksville. Providence Road and Stadium Boulevard carry the campus traffic between them.',
  'This page covers the interstate exits, move-in weeks, fall Saturdays, the hospitals, and the headquarters. It also covers the capital, the neighborhoods, the weather, and the lanes.'],
 'Columbia at a glance',
 ['Most pickups happen within 1 to 3 days. Every carrier running between Kansas City and St. Louis passes the city on 70.',
  'St. Louis and Kansas City are same-day lanes. Springfield, Indianapolis, and Chicago take a day. Dallas and Denver run one to two, and Florida runs three.'],
 'Tell us the week. Move-in in August, move-out in May, and seven home Saturdays decide where the truck can meet you.'))

BODY.append(sec('The Interstate','Interstate 70, US 63, Providence, and Stadium',
 prose(
  L('Columbia is the only city between Kansas City and St. Louis. Every carrier on 70 passes its exits.'),
  P('Interstate 70 runs along the north side with exits at Stadium Boulevard, Providence Road, and US 63. West it reaches Kansas City in two hours. East it reaches St. Louis in the same time, and both metros are carrier hubs.'),
  P('US 63 runs south thirty minutes to Jefferson City and the Capitol, and north to Kirksville. Providence Road and Stadium Boulevard cross the city from the interstate past the campus. Broadway is the main street through downtown.'),
  P('Route 740 connects Stadium to the east side, and Rangeline is the old highway through the north. None of the Columbia roads charges a toll.'),
  P('Our office sits on Green Meadows Road on the south side, off Providence and minutes from the stadium.'),
 ), alt=True))

BODY.append(sec('The University Weeks','Move-In, Move-Out, Seven Saturdays, and the Hospitals',
 prose(
  L('The university sets the calendar in Columbia, and the carriers read it before they quote.'),
  P('Move-in fills Providence, Stadium, and the streets around the campus for a week in mid-August. The driver meets you at a lot on Stadium or near the interstate rather than at the dorms. The same thing happens in reverse in early May, and graduation weekend fills every hotel in town.'),
  P('Seven home football Saturdays each fall close the streets around the stadium and fill 70 from both metros. We schedule Columbia pickups on another day of that week. An adult signs for a student car.'),
  P('The university hospital and the other hospital across town bring in residents every June and July. Most arrive from out of state with a car. The handoff happens on Stadium or Providence rather than in a hospital garage.'),
  P('The colleges downtown add smaller waves on the same dates. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the longer move.'),
 )))

ROUTES=[("St. Louis, MO","I-70 · ~125 mi","Same day","$180–$290"),("Kansas City, MO","I-70 · ~125 mi","Same day","$180–$290"),
 ("Springfield, MO","US-63/I-44 · ~170 mi","Same day","$200–$320"),("Indianapolis, IN","I-70 · ~370 mi","1 day","$340–$490"),
 ("Tulsa, OK","US-63/I-44 · ~400 mi","1 day","$360–$520"),("Chicago, IL","I-70/I-55 · ~410 mi","1 day","$370–$530"),
 ("Dallas, TX","I-70/I-49/US-75 · ~620 mi","1–2 days","$480–$690"),("Denver, CO","I-70 · ~730 mi","2 days","$540–$770"),
 ("Phoenix, AZ","I-70/I-40 · ~1,370 mi","3–4 days","$930–$1,280"),("Orlando, FL","I-70/I-24/I-75 · ~1,100 mi","3 days","$780–$1,100")]
BODY.append(rate_table('Lanes &amp; Costs','Columbia Car Shipping Lanes and Estimated Costs',
 'The lanes Columbia students, families, and faculty book most, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a sedan that runs, open trailer. An SUV or pickup costs about 10 to 25 percent more, enclosed more than that. Move-in week, game weekends, and the carriers free on your dates set the final figure.',
 prose(
  P('Both metros sit two hours away on 70. A Columbia car usually rides a truck that was already going to one of them. That keeps the price close to a metro price.'),
  P('Denver rides 70 straight west, and Chicago rides 70 and 55. The <a href="car-shipping-cost.html">cost guide</a> explains the rest of the number.'),
 ), alt=True))

BODY.append(sec('Who Else Moves Here','The Capital, the Insurer, the Lender, and the Plants',
 prose(
  L('Outside the campus, Columbia ships on state government and a set of headquarters that grew up here.'),
  P('The Capitol in Jefferson City sits thirty minutes south, and state workers relocate on the legislative calendar. The session runs January through May. The handoff in the capital happens on Missouri Boulevard or by the river.'),
  P('The home-loan company and the insurance headquarters in Columbia transfer staff in on start dates. The construction-equipment company and the food plants on the north side do the same. If your employer reimburses the shipment, we send the documentation it asks for.'),
  P('The nuclear plant near Fulton and the college there add smaller moves on their own schedules.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, East Campus, the Old Southwest, and the New South Side',
 prose(
  L('Columbia is tight near the campus and wide everywhere else, and the meeting spot follows that line.'),
  P('Downtown, East Campus, and Benton-Stephens have narrow streets with student parking on both curbs. The Old Southwest and the Grasslands wind under old trees. The driver meets you on Broadway, on Providence, or at a lot on Stadium.'),
  P('The south side along Nifong and Green Meadows is wide subdivisions where the truck usually reaches the curb. Thornbrook, Rock Bridge, and the additions toward the airport are the same.'),
  P('The north side along Rangeline and Vanderveen is open. The new construction past Scott Boulevard is not always on a carrier’s map yet. Send the full address.'),
  P('Jefferson City is tight on the hills by the Capitol and open in the suburbs. Fulton, Boonville, Ashland, and Hallsville schedule in a day or two on the highways.'),
 )))

BODY.append(sec('The Calendar &amp; the Weather','Homecoming, the Film Festival, the Ice, and the Storms',
 prose(
  L('Columbia fills for a film festival in winter and a homecoming in fall. The ice comes in between.'),
  P('The film festival fills downtown for a weekend in late winter. Homecoming fills the campus and the stadium for a weekend in October. The music festival fills the park on the east side in September. We schedule the affected neighborhoods around those dates.'),
  P('Ice closes 70 for a day a few times each winter. The carriers wait for the sand trucks. Tornado watches run from March into June, and the driver pulls off when a warning is issued. Hail hurts a parked car more than wind does, and we move the window when it is forecast.'),
  P('Summer heat moves the loading hour earlier. The Missouri River floods the bottoms below the bluffs in a wet spring. A river-town pickup waits for the water to fall.'),
 )+chips(["Downtown","The District","East Campus","Benton-Stephens","Old Southwest","Grasslands","West Boulevard","Thornbrook","Rock Bridge","Green Meadows","Nifong","Vanderveen","Rangeline","Smithton","Parkade","Cherry Hill","Jefferson City","Fulton","Boonville","Ashland","Hallsville","Centralia","Moberly"])
 +NOTE('Serving Boone and Cole Counties and the towns around them. Tell us the week, the neighborhood, and whether the car runs.'), alt=True))

BODY.append(sec('Your Options','Open or Enclosed in Columbia?',
 prose(
  L('Nearly every Columbia car rides open, and the 70 lane is quoted on it.'),
  P('An enclosed trailer keeps hail, salt, and attention off the car. A collector car or a graduation gift usually rides enclosed through the storm months.'),
  P('A student car does fine in the open. See the <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages for when a roof makes sense.'),
 )))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a loading near the interstate, and a delivery. The calendar decides the week.'),
  P('When you approve the price, a carrier already on 70 takes the booking and we set the spot. You and the driver inspect the car together and write it up on a Bill of Lading. Both sign, and the delivery check runs against it.'),
 )+ULI([
  "Remove personal belongings",
  "Keep about a quarter tank of fuel",
  "Photograph the vehicle before pickup, especially after a hail storm",
  "Provide a working key and disclose mechanical issues",
  "Disable aftermarket alarms",
  "On a move-in day or a game Saturday, plan to meet the truck by the interstate",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages hold the step-by-step.')), alt=True))

BODY.append(sec('Why Ship Guy','Why Columbia Drivers Choose Ship Guy',
 prose(
  L('We work the 70 lane every day and plan around move-in, the games, and the ice.'),
  P('Ship Guy’s FMCSA brokerage authority is current, with a $75,000 surety bond behind it. Both are public record. Our office is on Green Meadows Road.'),
  P('You get one coordinator for the whole move, and open, enclosed, and expedited transport are all on offer. The <a href="services.html">services</a> page explains each.'),
 )))

BODY.append(office('Columbia','108 Green Meadows Rd #542','Columbia, MO 65203','+15734982555','(573) 498-2555','CT',
 '108+Green+Meadows+Rd+%23542,+Columbia,+MO+65203','Visit Us','Find Ship Guy in Columbia',
 'Our office is on Green Meadows Road on the south side, off Providence Road.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3831.933187639851!2d-92.33737769999999!3d38.915955600000004!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x87dcb75d678412d7%3A0xf50e98c30e0b3fdf!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792076177352!5m2!1sen!2sus'))

FAQ=[
 ("Can you ship a car for a Mizzou student?","Yes. Student cars arrive in mid-August and leave in early May. Move-in week fills Providence and Stadium. The driver meets you at a lot on Stadium or near the interstate. An adult signs for the car at pickup, and a parent can sign at the far end."),
 ("Does a home football Saturday affect my pickup?","Yes, if it falls on one. The streets around the stadium close, and 70 fills from both metros. We schedule Columbia pickups on another day of that week."),
 ("How much does it cost to ship a car from Columbia to St. Louis or Kansas City?","A sedan usually runs one hundred eighty to two hundred ninety dollars to either one. Both sit about one hundred twenty-five miles away on 70. A Columbia car usually rides a truck already headed there. SUVs and pickups add 10 to 25 percent."),
 ("How much does it cost to ship a car from Columbia to Texas or Florida?","Dallas runs four hundred eighty to six hundred ninety dollars for a sedan, about six hundred twenty miles. Orlando runs seven hundred eighty to eleven hundred, about eleven hundred miles. Fall southbound costs more than spring."),
 ("Can the carrier come to my house near the campus or downtown?","Rarely. The streets are narrow and student parking fills both curbs. The driver meets you on Broadway, on Providence, or at a lot on Stadium. The south side, Thornbrook, and the north side usually allow curbside."),
 ("Do you pick up in Jefferson City?","Yes. The capital is thirty minutes south on US 63 and shares the Columbia carrier pool. The hills by the Capitol are tight. The driver meets you on Missouri Boulevard or by the river. The suburbs allow curbside."),
 ("Do you ship cars for residents at the university hospital?","Yes, every June and July. Both hospitals bring in residents from every state, most with a car. The handoff happens on Stadium or Providence rather than in a hospital garage."),
 ("What happens if ice or a tornado warning hits on my pickup day?","Ice closes 70 until the sand trucks finish, and the pickup slides a day. A tornado warning parks the driver until the all-clear. Spring and winter bookings both carry a cushion for it."),
 ("Can you ship a car that does not run from Columbia?","Yes. A winch carrier is assigned and the slower loading is built into the quote. Say whether it rolls, steers, and brakes, because the equipment depends on it."),
 ("What do you need for a Columbia car shipping quote?","The addresses at both ends, with the Columbia neighborhood. Year, make, model. Does it run and roll. Open or enclosed. Your dates, with the game schedule in mind. Nothing else is needed."),
]
BODY.append(faq_section(FAQ,'Columbia FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Columbia?','The form above prices it in about two minutes. Send the week and the neighborhood, and a carrier already on 70 handles the rest.','+15734982555','(573) 498-2555','Get your free Columbia quote'))

build({
 'slug':'auto-transport-columbia-missouri',
 'title':'Car Shipping in Columbia, MO — Auto Transport | Ship Guy',
 'meta':'Car shipping in Columbia, MO on the Interstate 70 lane between Kansas City and St. Louis. Mizzou move-in and game-day planning, hospital timing, Jefferson City pickups, campus and downtown meeting spots, ice and storm season. Local office on Green Meadows Road. Free quote.',
 'h1':'Car Shipping in<br>Columbia, <span class="accent">Missouri</span>',
 'lede':'Open, enclosed, and expedited auto transport across mid-Missouri, planned around the interstate, the campus, and the weather.',
 'tel':'+15734982555','disp':'(573) 498-2555','brand':'Columbia','keyword':'car shipping in columbia',
 'localterms':['columbia','interstate 70','us 63','providence','stadium','broadway','route 740','rangeline','green meadows','nifong','downtown','east campus','benton-stephens','old southwest','grasslands','thornbrook','rock bridge','vanderveen','scott boulevard','jefferson city','capitol','fulton','boonville','ashland','university','move-in','football','saturdays','hospital','residents','home-loan','insurance','construction-equipment','food plants','nuclear plant','film festival','homecoming','music festival','ice','tornado','hail','missouri river','st. louis','kansas city','springfield','indianapolis','tulsa','chicago','dallas','denver','phoenix','orlando'],
}, BODY, FAQ)
