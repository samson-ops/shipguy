import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Tulsa, Oklahoma','Car shipping on the turnpike between the Plains and the Ozarks',
 ['Car shipping in Tulsa starts with a toll road. Ship Guy is a licensed auto transport broker with an office on South Baltimore Avenue near downtown.',
  'We book vetted carriers across Green Country, from Sand Springs to Broken Arrow and from Owasso to Bixby. We do not own the trucks, and we say so up front.',
  'Interstate 44 reaches the city as the Turner Turnpike from Oklahoma City. It leaves as the Will Rogers Turnpike toward Joplin. US 75 carries the north-south traffic, and the Creek Turnpike wraps the south side.',
  'This page covers the turnpikes and the loops, the airport and the aerospace base, and the older neighborhoods. It also covers the remote-worker arrivals, the fair, the Chili Bowl, the river, and the lanes.'],
 'Tulsa at a glance',
 ['Most pickups happen within 1 to 3 days. Carriers crossing between Missouri and Texas pass the city every day.',
  'Oklahoma City, Joplin, and Wichita are same-day lanes. Dallas and Kansas City take a day. Denver runs two, and Phoenix and the coasts run three to four.'],
 'Tell us the part of town. Maple Ridge, Brookside, and Cherry Street need a meeting spot on a main road. Broken Arrow and Owasso usually do not.'))

BODY.append(sec('The Turnpikes','Interstate 44, the Loops, and the Toll Roads',
 prose(
  L('Tulsa is ringed by toll roads. The carrier pays every one of them before you ever see a price.'),
  P('Interstate 44 arrives from Oklahoma City on the Turner Turnpike. It continues northeast toward Joplin on the Will Rogers Turnpike. Interstate 244 cuts through downtown and across the Arkansas River as the inner crosstown.'),
  P('US 75 runs north to Bartlesville and south to Okmulgee. It carries the Dallas lane without a toll. US 169 is the Mingo Valley Expressway up to Owasso. The Broken Arrow Expressway runs southeast, and the Creek Turnpike loops the south and east sides.'),
  P('The Cimarron Turnpike heads west to Stillwater and Interstate 35. The Muskogee Turnpike heads southeast toward Interstate 40, and the Cherokee Turnpike carries US 412 into Arkansas.'),
  P('Every toll is paid by the carrier and folded into the quote. There is no toll line on a Ship Guy price, in Tulsa or anywhere else in Oklahoma.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, Midtown, the River, and the Suburbs',
 prose(
  L('Tulsa was laid out in the oil boom. The older streets were never meant for a seventy-five-foot trailer.'),
  P('Downtown sits inside the Inner Dispersal Loop. The Arts District, the Blue Dome, and Greenwood run on garages and one-way streets. The driver meets you on a wide block near the loop or in a surface lot.'),
  P('Maple Ridge, Swan Lake, Cherry Street, and Brookside have narrow streets and low oaks. Cars park on both sides. The handoff happens on Peoria Avenue, Utica, or Fifteenth Street. Kendall-Whittier near the university is the same.'),
  P('Riverside Drive carries the park traffic along the Arkansas River, and it fills on warm weekends. South Tulsa around Seventy-First and Memorial is wide and easy, and the truck usually reaches the curb.'),
  P('Broken Arrow, Owasso, Jenks, Bixby, Sand Springs, and Glenpool are open grids with room to load. Send the subdivision name where there is one.'),
  P('Our office is on South Baltimore Avenue just south of downtown. It is a short drive from the loop and Riverside Drive.'),
 )))

ROUTES=[("Oklahoma City, OK","Turner Tpk · ~105 mi","Same day","$170–$280"),("Joplin, MO","Will Rogers Tpk · ~115 mi","Same day","$180–$290"),
 ("Wichita, KS","Cimarron Tpk/I-35 · ~180 mi","Same day","$210–$320"),("Dallas, TX","US-75 · ~260 mi","1 day","$250–$370"),
 ("Kansas City, MO","US-169/I-49 · ~250 mi","1 day","$250–$370"),("Little Rock, AR","Muskogee Tpk/I-40 · ~275 mi","1 day","$260–$390"),
 ("St. Louis, MO","I-44 · ~395 mi","1 day","$350–$500"),("Houston, TX","US-75/I-45 · ~480 mi","1–2 days","$400–$570"),
 ("Denver, CO","I-35/I-70 · ~700 mi","2 days","$520–$740"),("Phoenix, AZ","I-40/I-17 · ~1,000 mi","3 days","$720–$1,000")]
BODY.append(rate_table('Lanes &amp; Costs','Tulsa Car Shipping Lanes and Estimated Costs',
 'The lanes Tulsa households and employers ask about most, with estimated open-transport ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates, running sedan, open trailer. SUVs and pickups add roughly 10 to 25 percent, and enclosed adds more. Turnpike tolls are included. Spring storms and carrier availability on your dates set the real quote.',
 prose(
  P('Oklahoma City and Joplin are the quick lanes. Each sits an hour and a half away on Interstate 44. Dallas rides US 75 through Okmulgee and McAlester without a toll.'),
  P('Northwest Arkansas is two hours east on the Cherokee Turnpike, and the corporate moves there run all year. The <a href="car-shipping-cost.html">cost guide</a> explains the rest of the number.'),
 ), alt=True))

BODY.append(sec('The Airport &amp; the Employers','The Maintenance Base, the Energy Towers, and the Remote-Worker Lane',
 prose(
  L('Tulsa relocates people on airplane schedules, drilling budgets, and a city program that pays them to move here.'),
  P('The airline maintenance base at Tulsa International is one of the largest of its kind. The aerospace plants around the airport hire on program cycles. Mechanics and engineers arrive from Texas, Kansas, and the coasts with a start date and a car.'),
  P('The pipeline and energy companies downtown transfer engineers in and out on project calendars. If your employer reimburses the shipment, we send the paperwork it asks for.'),
  P('The remote-worker incentive brings a steady stream of households from both coasts. Many of them ship a car rather than drive it across. We quote those lanes every week, and California to Tulsa runs four to five days.'),
  P('The hospitals in Midtown and South Tulsa bring in residents each summer. The handoff happens on Yale Avenue or Utica rather than in a hospital garage. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the longer relocation.'),
 )))

BODY.append(sec('The Campuses &amp; the Season','TU, ORU, the State Fair, and the Chili Bowl',
 prose(
  L('Tulsa fills Expo Square twice a year, and the carriers plan around both weeks.'),
  P('The University of Tulsa in Midtown and Oral Roberts in South Tulsa bring cars in each August. They send them home each May. Campus streets are tight, so the driver meets you at a lot nearby. An adult signs for a student car.'),
  P('The Tulsa State Fair runs eleven days from late September into early October at Expo Square. Twenty-First Street and Yale Avenue clog for the whole run, and we schedule Midtown pickups around it.'),
  P('The Chili Bowl brings race teams and their haulers to Expo Square every January. Race cars and show cars ship into Tulsa that week on enclosed trailers, and the lots fill early.'),
  P('Tulsa Tough closes streets in the Arts District, Cherry Street, and Riverside in June. Oktoberfest fills the west bank in October. The downtown arena and the ballpark add event nights all year.'),
 ), alt=True))

BODY.append(sec('The Weather','Tornadoes, Ice, Hail, and the River',
 prose(
  L('Green Country gets every kind of weather the Plains can produce, and the river adds one more.'),
  P('Tornado watches run from April into June. A warning sends the driver to the shoulder until it passes. A pickup can slide a few hours. We tell you the moment the window moves.'),
  P('Hail does more damage to a parked car than any tornado. An enclosed trailer keeps a collector car under a roof on a stormy week. Ice storms shut the turnpikes a few times a decade and bring down the old oaks in Midtown.'),
  P('The Arkansas River can rise fast when the dam upstream releases water. The low ground in Sand Springs, West Tulsa, and Bixby floods. Carriers stay on the high roads, and we reroute the handoff when the river is up.'),
  P('July and August run past a hundred degrees for weeks at a stretch. A car arriving from a cooler climate should have its cooling system checked before the trip.'),
 )+chips(["Downtown","Arts District","Blue Dome","Greenwood","Pearl District","Kendall-Whittier","Cherry Street","Maple Ridge","Swan Lake","Brookside","Riverview","Midtown","Utica Square","Florence Park","Riverside","South Tulsa","Woodland Hills","Jenks","Bixby","Broken Arrow","Owasso","Sand Springs","Sapulpa","Glenpool","Catoosa","Claremore"])
 +NOTE('Serving Tulsa, Rogers, Wagoner, Creek, and Osage Counties. Tell us the neighborhood and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Tulsa?',
 prose(
  L('Open transport carries most of Tulsa, and the turnpike lanes run on it every day.'),
  P('Enclosed transport keeps a car covered against hail, road grit, and the spring storms. The collector garages in Maple Ridge and South Tulsa keep enclosed carriers busy. The race teams at the Chili Bowl do the same.'),
  P('A daily driver rides open without trouble. Our <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages lay out each option.'),
 )))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a loading near the turnpike, and a delivery. The storms and the fair decide the timing.'),
  P('Once you approve the price, a carrier already running Interstate 44 or US 75 takes the booking. Before the car goes up the ramp, the driver notes its condition on a Bill of Lading. You sign it. Keep that form, because it is your checklist when the car comes off in Dallas or Denver.'),
 )+ULI([
  "Remove personal belongings",
  "Keep about a quarter tank of fuel",
  "Photograph the vehicle before pickup, especially after a hail storm",
  "Provide a working key and disclose mechanical issues",
  "Disable aftermarket alarms",
  "For Midtown or downtown, plan to meet the truck on a main road or in a lot",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> guides take it step by step.')), alt=True))

BODY.append(sec('Why Ship Guy','Why Tulsa Drivers Choose Ship Guy',
 prose(
  L('We work the turnpike lanes every day and plan around the fair, the storms, and the river.'),
  P('Active FMCSA brokerage authority and a $75,000 surety bond stand behind every booking we make. Our office is on South Baltimore Avenue.'),
  P('One coordinator carries your shipment from quote to delivery and can book open, enclosed, or expedited transport. The <a href="services.html">services</a> page shows the full lineup.'),
 )))

BODY.append(office('Tulsa','1800 S Baltimore Ave Ste 578','Tulsa, OK 74119','+19188973349','(918) 897-3349','CT',
 '1800+S+Baltimore+Ave+Ste+578,+Tulsa,+OK+74119','Visit Us','Find Ship Guy in Tulsa',
 'Our office is on South Baltimore Avenue just south of downtown. It is a short drive from the Inner Dispersal Loop and Riverside Drive.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5450.1629202552485!2d-95.98668239999999!3d36.135706299999995!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x87b6eb675c3234f5%3A0xcea3c3c15f0c56d2!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792022864324!5m2!1sen!2sus'))

FAQ=[
 ("Are the Tulsa turnpike tolls added to my quote?","No. The carrier pays the Turner, Will Rogers, Creek, and Cimarron turnpikes and prices the trip accordingly. The toll is folded into the number you approve. US 75 to Dallas carries no toll at all."),
 ("How much does it cost to ship a car from Tulsa to Dallas?","A sedan usually runs two hundred fifty to three hundred seventy dollars on US 75. That is about two hundred sixty miles through Okmulgee and McAlester. Houston runs four hundred to five hundred seventy on the same road. Larger vehicles add 10 to 25 percent."),
 ("Can the carrier come to my house in Maple Ridge or Brookside?","Rarely. The streets are narrow, the oaks hang low, and cars park on both sides. The driver meets you on Peoria Avenue, Utica, or Fifteenth Street instead. Broken Arrow, Owasso, Jenks, and Bixby usually allow a curbside pickup."),
 ("Do you ship cars for people moving to Tulsa through the remote-worker program?","Yes, every week. Most of those households come from California, New York, and the Northeast. Many ship a car rather than drive it. The West Coast lane runs four to five days, and the Northeast runs three to four."),
 ("Does the Tulsa State Fair affect pickups?","Around Expo Square, yes. Twenty-First Street and Yale Avenue clog for the eleven-day run from late September into early October. We schedule Midtown pickups before or after the fair, and the rest of the city runs normally."),
 ("Can you ship a race car or a show car into Tulsa for the Chili Bowl?","Yes. Race teams ship cars into Expo Square every January on enclosed trailers. Book early, because the enclosed carriers fill fast that week. Tell us the length of the car and whether it rolls."),
 ("What happens if a tornado warning is issued during my pickup?","The driver pulls off the road and waits it out. The pickup can slide a few hours or a day. Tornado watches run April into June, and we leave room in every spring window for that."),
 ("Can you ship a car from Tulsa to northwest Arkansas or Joplin?","Yes. Joplin is about one hundred fifteen miles up the Will Rogers Turnpike and runs same day. Northwest Arkansas is about two hours east on the Cherokee Turnpike. Both lanes run one hundred eighty to two hundred ninety dollars for a sedan."),
 ("Can you ship a car that does not run from Tulsa?","Yes, non-running cars leave Tulsa every week. A winch-equipped carrier loads it, and the extra loading time goes on the quote. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Tulsa car shipping quote?","The pickup and delivery addresses, with the neighborhood. The year, make, and model. Whether it runs and rolls. Open or enclosed, and your dates. That is everything an accurate Tulsa quote needs."),
]
BODY.append(faq_section(FAQ,'Tulsa FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Tulsa?','Two minutes on the form above gets you a price. Tell us the neighborhood and your dates. We will match you with a carrier already on the turnpike.','+19188973349','(918) 897-3349','Get your free Tulsa quote'))

build({
 'slug':'auto-transport-tulsa-oklahoma',
 'title':'Car Shipping in Tulsa, OK — Auto Transport | Ship Guy',
 'meta':'Car shipping in Tulsa, OK on the Turner and Will Rogers turnpikes. Tolls built in, Maple Ridge and Brookside handoffs, the airport maintenance base, remote-worker arrivals, State Fair and Chili Bowl timing, spring storms and the river. Local office on South Baltimore Avenue. Free quote.',
 'h1':'Car Shipping in<br>Tulsa, <span class="accent">Oklahoma</span>',
 'lede':'Open, enclosed, and expedited auto transport across Green Country, planned around the turnpikes, the storms, and the fair.',
 'tel':'+19188973349','disp':'(918) 897-3349','brand':'Tulsa','keyword':'car shipping in tulsa',
 'localterms':['tulsa','interstate 44','interstate 244','turner turnpike','will rogers','creek turnpike','cimarron','muskogee turnpike','cherokee turnpike','us 75','us 169','mingo valley','broken arrow expressway','inner dispersal loop','arkansas river','riverside','downtown','arts district','blue dome','greenwood','maple ridge','swan lake','cherry street','brookside','kendall-whittier','utica','peoria','south tulsa','seventy-first','memorial','broken arrow','owasso','jenks','bixby','sand springs','glenpool','sapulpa','catoosa','claremore','airport','maintenance base','aerospace','pipeline','energy','remote-worker','hospitals','residents','university of tulsa','oral roberts','state fair','expo square','chili bowl','tulsa tough','oktoberfest','tornado','hail','ice','flood','dallas','joplin','oklahoma city','wichita','kansas city'],
}, BODY, FAQ)
