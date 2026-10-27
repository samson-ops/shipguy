import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Glendale, Arizona','Car shipping in the West Valley, between the stadium district and the fighter base',
 ['Car shipping in Glendale starts on Loop 101, the freeway that runs past the stadium and the arena. Ship Guy is a licensed auto transport broker with an office on Sunset Boulevard in the Westgate district.',
  'We book vetted carriers across the West Valley, from Arrowhead to Luke and out to Sun City. We do not own the trucks.',
  'Loop 101 runs north and south through the middle of the city. Grand Avenue is US 60, the diagonal from Phoenix through downtown Glendale to Sun City and Las Vegas. Interstate 17 runs the east edge, and Loop 303 runs the west. Glendale Avenue and Bell Road carry the rest.',
  'This page covers the loop, Grand Avenue, downtown, Arrowhead, the stadium district, and Sun City. It also covers the fighter base, spring training, the March auction, the game days, and the lanes.'],
 'Glendale at a glance',
 ['Most pickups happen within 1 to 3 days. Loop 101 and Interstate 10 bring the California carriers to the West Valley all day.',
  'Phoenix and Tucson are same-day lanes. Flagstaff takes a day. Las Vegas, San Diego, and Los Angeles take one too. Albuquerque, Salt Lake City, and Denver take one to two, and the Northwest takes three.'],
 'Tell us the neighborhood and the Sunday. Downtown, Westgate, and the base need a meeting spot. Arrowhead, the central grids, and Sun City usually allow the curb. Game days move everything near the stadium.'))

BODY.append(sec('The Roads','Loop 101, Grand Avenue, Interstate 17, Loop 303, and Glendale Avenue',
 prose(
  L('Glendale is where the Las Vegas road leaves the valley, and the West Valley freeways meet around it.'),
  P('Loop 101 is the Agua Fria Freeway. It runs north and south through the city past the stadium district. The ramps at Glendale Avenue, Northern, Bell Road, and Union Hills reach every neighborhood. It carries the Interstate 10 carriers up from the south and the 17 carriers across from the north.'),
  P('Grand Avenue is US 60, the old diagonal with the railroad beside it. It runs from downtown Phoenix through downtown Glendale to Peoria, Sun City, and Wickenburg. Beyond Wickenburg it becomes US 93, the road to Las Vegas. The Las Vegas carriers leave the valley on it, and every intersection on it is a six-way.'),
  P('Interstate 17 runs the east edge of the city toward Flagstaff. Loop 303 runs the west edge past the base to the 10. Glendale Avenue is the main east-west street from downtown to Westgate and the base. Bell Road passes the Arrowhead mall. Camelback Road runs the south edge past the spring training camp.'),
  P('The carriers come off the 101 at Glendale Avenue and Bell Road. Off 17, they use Northern and Bell. The lots at Westgate, at the Arrowhead mall, and along Bell Road are the usual meeting spots. No road in the West Valley charges a toll.'),
  P('Our office sits on Sunset Boulevard in the Westgate district, beside the stadium and the 101.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, Catlin Court, Arrowhead, the Stadium District, Sun City, and the Base',
 prose(
  L('Glendale is a farm town, a stadium town, and the gateway to the retirement cities. Each one parks differently.'),
  P('Downtown and Catlin Court have bungalows and antique shops on a tight grid around Murphy Park. The driver meets you on Glendale Avenue or on Grand. The old grids along 59th and 67th Avenue south to Camelback are postwar blocks. The truck usually reaches the curb. Sahuaro Ranch and the college sit on Olive Avenue with lots of their own.'),
  P('Arrowhead Ranch, Arrowhead Lakes, and Sierra Verde in the north are lake and golf subdivisions with gates. The driver meets you at the gate or at the Arrowhead mall. The subdivisions along Union Hills and Deer Valley have wide streets, and the curb works on most.'),
  P('The stadium district along the 101 has the stadium, the arena, and the outlets. The lots there are the easiest handoff in the valley. On a game day or a concert night, they are the hardest. Westgate and Zanjero have apartment complexes with garages. The base sits west of the district behind gates on Litchfield Road.'),
  P('Sun City and Sun City West are age-restricted cities with wide streets and golf cart lanes. Most streets have no gates. The truck usually reaches the curb, and the driver watches for the carts. Peoria, Surprise, El Mirage, and Litchfield Park ride the same carriers. Surprise has gates on many subdivisions, and the driver meets you at the entrance.'),
 )))

ROUTES=[("Phoenix, AZ","I-17/Grand Ave · ~10 mi","Same day","$120–$200"),("Tucson, AZ","I-10 · ~125 mi","Same day","$160–$260"),
 ("Flagstaff, AZ","I-17 · ~140 mi","1 day","$170–$280"),("Las Vegas, NV","US-60/US-93 · ~280 mi","1 day","$260–$390"),
 ("San Diego, CA","I-10/I-8 · ~350 mi","1 day","$330–$470"),("Los Angeles, CA","I-10 · ~360 mi","1 day","$340–$490"),
 ("Albuquerque, NM","I-17/I-40 · ~470 mi","1 day","$400–$570"),("Salt Lake City, UT","US-93/I-15 · ~650 mi","2 days","$480–$690"),
 ("Denver, CO","I-17/I-40/I-25 · ~820 mi","2 days","$560–$800"),("Seattle, WA","I-10/I-5 · ~1,420 mi","3 days","$950–$1,350")]
BODY.append(rate_table('Lanes &amp; Costs','Glendale Car Shipping Lanes and Estimated Costs',
 'The lanes that leave the West Valley most, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a sedan that runs, on an open trailer, priced from Glendale. Add about 10 to 25 percent for an SUV or pickup, and more for enclosed. The season, the class cycles, and the carriers free on your dates set the final price.',
 prose(
  P('Glendale is the closest part of the valley to the Las Vegas road. That lane prices a little lower here than anywhere else in the metro area. California rides Interstate 10 from the south end of the 101. The Northwest lanes swing with the snowbird season.'),
  P('The base keeps the Florida, Texas, and Nevada lanes busy with every class. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Fighter Base, the Stadium District, the Hospitals, and the Retirement Cities',
 prose(
  L('Glendale relocates pilots, hotel staff, nurses, and retirees, and the base calendar is the one that never stops.'),
  P('Luke Air Force Base is the largest fighter pilot training base in the world. Pilots from the Air Force and a dozen allied countries rotate in on class cycles. Instructors and maintainers follow them. Orders cover one car, and the second one comes with us. The gates on Litchfield Road stop the truck, so the handoff happens on Glendale Avenue or at Westgate.'),
  P('Ship Guy is a private broker with no connection to the base. The <a href="military-car-shipping.html">military</a> page covers the timing around a report date.'),
  P('The stadium, the arena, the outlets, and the hotels around them hire on the event calendar. The spring training camp on Camelback brings staff in each February. The hospitals along Thunderbird and Union Hills bring in nurses all year and residents each June. We supply the paperwork a reimbursed move needs.'),
  P('Retirees fill Sun City, Sun City West, and Surprise from October through April. Many ship a second car down for the season. The <a href="snowbird-car-shipping.html">snowbird</a> page covers the seasonal lane. The community college on Olive brings cars in each August, and an adult signs for a student car.'),
  P('Families arrive from California for the prices, and the second car usually rides a truck. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Game Days, the March Auction, Spring Training, the Heat, and the Monsoon',
 prose(
  L('Glendale fills the stadium forty times a year, and every one of those days moves the meeting spot.'),
  P('Football Sundays from September through January gridlock the 101 and Glendale Avenue around Westgate for six hours. Concerts and the arena do the same on random nights. The bowl game fills the district around New Year’s. We never set a pickup at Westgate on an event day, and the Arrowhead mall takes over.'),
  P('The collector auction fills the stadium lots for a week in March. Buyers ship cars home from it. Enclosed carriers book out early that week. The spring training camp on Camelback fills the south side for six weeks in February and March. The holiday lights fill downtown from late November through January.'),
  P('Summer runs past 110 degrees from June into September, so loading happens at dawn. Tires and batteries get a look before a long haul. July and August bring the monsoon, dust walls from the southwest and flash floods behind them. A carrier waits out a dust wall on the shoulder. A pickup beside a wash moves uphill.'),
  P('From October through April, the snowbird season fills inbound carriers and tightens outbound space. Book two to three weeks ahead in those months. Spring wind on Grand Avenue slows a tall trailer in March and April.'),
 )+chips(["Downtown","Catlin Court","Murphy Park","Sahuaro Ranch","Thunderbird","Arrowhead Ranch","Arrowhead Lakes","Sierra Verde","Hillcrest Ranch","Union Hills","Deer Valley","Westgate","Stadium District","Zanjero","Camelback Ranch","Manistee Ranch","59th Avenue","67th Avenue","Luke","Litchfield Park","Peoria","Sun City","Sun City West","Surprise","El Mirage","Youngtown","Goodyear","Avondale"])
 +NOTE('Serving Glendale, Peoria, Sun City, and the whole West Valley. Tell us the neighborhood, the gate, and the Sunday to avoid.')))

BODY.append(sec('Your Options','Open or Enclosed in Glendale?',
 prose(
  L('Open is how the West Valley ships, and the Las Vegas and California lanes are priced for it.'),
  P('An enclosed trailer keeps the dust, the sun, and attention off a car. Buyers at the March auction book them by the dozen. Pilots with a restored car headed to a new post book them too.'),
  P('A commuter or a seasonal second car has no need for one. Compare the two on the <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff at Westgate or the Arrowhead mall, and a delivery. The event calendar picks the lot.'),
  P('After you approve the price, a carrier already working the 101 or 10 is booked. The same afternoon, you know the lot and the window. The driver and you walk the car together, and every mark goes on the Bill of Lading. It is signed twice and read again at delivery.'),
 )+ULI([
  "Clear out anything personal, including the glovebox",
  "Fuel to roughly a quarter tank, no more",
  "Take dated photos of each side before the handoff",
  "Bring a working key and point out anything mechanical",
  "Kill any aftermarket alarm",
  "From the base, meet the truck outside the gate on Glendale Avenue",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages walk through the rest.'))))

BODY.append(sec('Why Ship Guy','Why Glendale Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already run the 101 and Grand Avenue. We plan around the gates, the game days, and the heat.'),
  P('Ship Guy’s brokerage authority with the FMCSA is active, backed by a $75,000 surety bond. Both can be checked in the federal register. Our office is on Sunset Boulevard in the Westgate district.'),
  P('The person who prices your move is the person who answers the phone until it is delivered. Open, enclosed, and expedited are all explained on the <a href="services.html">services</a> page.'),
 ), alt=True))

BODY.append(office('Glendale','6751 N Sunset Blvd #225','Glendale, AZ 85305','+19285648665','(928) 564-8665','MST',
 '6751+N+Sunset+Blvd+%23225,+Glendale,+AZ+85305','Visit Us','Find Ship Guy in Glendale',
 'Our office is on Sunset Boulevard in the Westgate district, beside the stadium and Loop 101.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5114.071677163706!2d-112.2635739!3d33.5361675!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x872b416ce1768b19%3A0xcc616bd76eac2529!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792169796584!5m2!1sen!2sus'))

FAQ=[
 ("Do you handle a PCS move to Luke Air Force Base?","Yes, on every class cycle. Orders cover one car, and the second one comes with us. The gates on Litchfield Road stop the truck, so we meet you on Glendale Avenue or at Westgate. We schedule around your report date. Ship Guy is a private broker with no connection to the base."),
 ("Will a game day or a concert affect my pickup?","Near Westgate, yes. Football Sundays, the bowl game, and the big concerts gridlock the 101 and Glendale Avenue for hours. We never set a pickup at Westgate on an event day. The handoff moves to the Arrowhead mall or Bell Road. Arrowhead, Sun City, and the rest of the city run normally."),
 ("How much does it cost to ship a car from Glendale to Las Vegas or Los Angeles?","Las Vegas runs two hundred sixty to three hundred ninety dollars for a sedan. That is about two hundred eighty miles up Grand Avenue and US 93. Los Angeles runs three hundred forty to four hundred ninety, about three hundred sixty miles on Interstate 10. SUVs and pickups add 10 to 25 percent."),
 ("Do you ship cars bought at the March auction at the stadium?","Yes, and that week is one of our busiest. We work the pickup around the auction house’s release schedule. Collector cars almost always leave under a roof, and the enclosed carriers for that week fill weeks ahead. Book before the gavel if you can."),
 ("Can the carrier come into Sun City or Arrowhead Ranch?","Sun City, usually. The streets are wide and mostly ungated, and the driver watches for the golf carts. Arrowhead Ranch and the lake subdivisions have gates on many entrances. The driver meets you at the gate or at the Arrowhead mall. Send the gate code where there is one."),
 ("What happens if a dust storm hits on my pickup day?","Everybody parks. A dust wall rolls in from the southwest, swallows the 101 for an hour, and rolls out again. The car loads once it clears, that evening or early the next day. You get a call from us before anything shifts."),
 ("How far ahead should I book in the winter?","Give us two to three weeks between October and April. The winter crowd fills every inbound trailer, and outbound room is thin until spring. In summer, a few days is plenty. Flexibility on dates does more than anything else in the busy months."),
 ("Can you ship a car to or from Peoria, Surprise, or Sun City West?","Yes, and all three price the same as Glendale. They ride the same 101 and Grand Avenue carriers. Surprise has gates on many subdivisions, so the driver meets you at the entrance. The lots along Bell Road and Grand work for a handoff."),
 ("Can you ship a car that does not run from Glendale?","Yes. A winch truck takes the job, and the longer loading is already in the price. The Westgate lots or the Arrowhead mall give the driver a flat, open spot. Say whether the car rolls, steers, and brakes when you book."),
 ("What do you need for a Glendale car shipping quote?","Where it leaves and where it lands, with the gate or the neighborhood here. What the car is, year, make, and model. Whether it starts and rolls. Open or enclosed. Dates that dodge the event calendar. That is the whole Glendale request."),
]
BODY.append(faq_section(FAQ,'Glendale FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Glendale?','The form above prices your lane in about two minutes. Tell us the neighborhood, the gate, and your dates. A carrier already on the 101 handles the rest.','+19285648665','(928) 564-8665','Get your free Glendale quote'))

build({
 'slug':'auto-transport-glendale-arizona',
 'title':'Car Shipping in Glendale, AZ — Auto Transport | Ship Guy',
 'meta':'Car shipping in Glendale, AZ between the stadium district and Luke Air Force Base. PCS second cars and Litchfield Road gate handoffs, Westgate and Arrowhead meeting spots, Sun City curbside, game-day and March auction planning, the Las Vegas lane, heat and monsoon planning. Local office on Sunset Boulevard at Westgate. Free quote.',
 'h1':'Car Shipping in<br>Glendale, <span class="accent">Arizona</span>',
 'lede':'Open, enclosed, and expedited auto transport across the West Valley, planned around the 101, Grand Avenue, the gates, and the game days.',
 'tel':'+19285648665','disp':'(928) 564-8665','brand':'Glendale','keyword':'car shipping in glendale',
 'localterms':['glendale','loop 101','agua fria','grand avenue','us 60','us 93','wickenburg','interstate 17','loop 303','glendale avenue','bell road','northern','union hills','deer valley','camelback road','olive avenue','thunderbird','litchfield road','downtown','catlin court','murphy park','sahuaro ranch','college','59th','67th','arrowhead ranch','arrowhead lakes','sierra verde','arrowhead mall','westgate','stadium','arena','outlets','zanjero','sun city','sun city west','golf cart','peoria','surprise','el mirage','litchfield park','luke air force base','fighter pilot','allied','class cycles','orders','report date','hotels','spring training','hospitals','nurses','residents','retirees','snowbird','football sundays','concerts','bowl game','auction','march','holiday lights','110 degrees','monsoon','dust walls','flash floods','spring wind','phoenix','tucson','flagstaff','las vegas','san diego','los angeles','albuquerque','salt lake city','denver','seattle','california','florida','texas','nevada'],
}, BODY, FAQ)
