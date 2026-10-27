import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Denver, Colorado','Car shipping a mile high, where Interstate 25 meets Interstate 70 and every lane west begins',
 ['Car shipping in Denver starts at the Mousetrap, where Interstate 25 crosses Interstate 70 north of downtown. Ship Guy is a licensed auto transport broker with an office on Lawrence Street in Lower Downtown.',
  'We book vetted carriers across the metro area, from Castle Rock to Broomfield and out to the airport. We do not own the trucks.',
  'Interstate 25 runs north and south through the city as the Valley Highway. Interstate 70 crosses it on the north side on the rebuilt stretch through Elyria. Interstate 76 leaves for Nebraska, and Interstate 225 loops through Aurora. The E-470 toll road circles the east side out to the airport.',
  'This page covers the interstates, the beltway, downtown, the bungalow blocks, and the suburbs. It also covers the stock show, the hail, the blizzards, the campuses, the hospitals, and the lanes.'],
 'Denver at a glance',
 ['Most pickups happen within 1 to 3 days. Interstate 70 and 25 bring the Kansas City and Albuquerque carriers through the Mousetrap all day.',
  'Colorado Springs and Fort Collins are same-day lanes. Cheyenne is the same day too. Albuquerque, Salt Lake City, and Kansas City take a day. Dallas, Phoenix, and Las Vegas take two.'],
 'Tell us the neighborhood. Capitol Hill, the Highlands, and Washington Park need a meeting spot. Central Park, Green Valley Ranch, and the suburbs usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 25, 70, 76, 225, and the E-470 Beltway',
 prose(
  L('Denver is where the plains carriers meet the mountain carriers, and the Mousetrap is the handoff.'),
  P('Interstate 25 runs the length of the metro area from Castle Rock to Thornton. The stretch through the city is the Valley Highway. It jams from Santa Fe to the Mousetrap twice a day. Interstate 70 crosses the north side on the lowered stretch through Elyria and Swansea, finished in 2023. West of the city, it climbs into the foothills toward the tunnel.'),
  P('Interstate 76 splits off 70 at Commerce City and runs northeast to Nebraska. Interstate 225 leaves 25 at the Tech Center and loops through Aurora back to 70. Interstate 270 is the short cut across the north side between the two.'),
  P('C-470 wraps the south and west sides for free. E-470 wraps the east side and runs out to the airport, and it charges a toll by plate. Peña Boulevard is the only road to the terminal. US 36 runs to Boulder and US 6 to Golden. Santa Fe Drive runs south to Littleton.'),
  P('The carriers come off 70 at Brighton Boulevard and Quebec Street. Off 25, they use Speer Boulevard and Hampden Avenue. The lots along Brighton Boulevard, at the stock show grounds, and off Quebec are the usual meeting spots. Colfax Avenue is the longest commercial street in the country, and it has a lot every few blocks.'),
  P('Our office sits on Lawrence Street in Lower Downtown, a few blocks from Union Station and the ballpark.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Lower Downtown, Capitol Hill, the Highlands, Washington Park, and the Suburbs',
 prose(
  L('Denver is a grid of brick bungalows around a downtown of towers. Both were laid out before the trailer.'),
  P('Lower Downtown and River North have lofts, breweries, and the ballpark on Blake Street. A trailer can stop on Brighton Boulevard or in a lot by the stadium. Capitol Hill, Uptown, and Cheesman Park are the densest blocks in the state. Apartments line both curbs, and the driver meets you on Colfax, on Broadway, or on Speer.'),
  P('The Highlands, Berkeley, and Sunnyside sit on the hill across the river. Their streets are narrow and lined with trees. The driver meets you on 38th Avenue or Federal Boulevard. Washington Park, Platt Park, and Congress Park are bungalow blocks where the handoff happens on a wide avenue. Cherry Creek has garages and a mall with room to load.'),
  P('Park Hill and Hilltop have wide streets and big trees, and the truck often reaches the curb. Central Park, the old airport site, is a new grid with wide streets and alleys. Green Valley Ranch and Montbello are open grids on the way to the airport. The trailer reaches the curb in all three.'),
  P('Highlands Ranch, Centennial, and Lone Tree are cul-de-sac suburbs where the driver meets you at the entrance. Lakewood, Arvada, Westminster, and Thornton are postwar grids that usually work curbside. Golden, Boulder, and Castle Rock are far enough out that we plan the stop in advance. Littleton and Englewood sit along Santa Fe with lots everywhere.'),
 )))

ROUTES=[("Colorado Springs, CO","I-25 · ~70 mi","Same day","$150–$240"),("Albuquerque, NM","I-25 · ~450 mi","1 day","$400–$570"),
 ("Salt Lake City, UT","I-70/US-6 · ~520 mi","1–2 days","$430–$620"),("Kansas City, MO","I-70 · ~600 mi","1–2 days","$450–$650"),
 ("Omaha, NE","I-76/I-80 · ~540 mi","1–2 days","$430–$620"),("Dallas, TX","I-25/US-287 · ~800 mi","2 days","$560–$820"),
 ("Phoenix, AZ","I-25/I-40 · ~820 mi","2 days","$450–$650"),("Las Vegas, NV","I-70/I-15 · ~750 mi","2 days","$540–$780"),
 ("Chicago, IL","I-76/I-80 · ~1,000 mi","3 days","$700–$1,000"),("Los Angeles, CA","I-70/I-15 · ~1,015 mi","3 days","$750–$1,050")]
BODY.append(rate_table('Lanes &amp; Costs','Denver Car Shipping Lanes and Estimated Costs',
 'The lanes that leave the metro area most, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a running sedan on an open trailer, priced from the Denver metro area. Add about 10 to 25 percent for an SUV or pickup, and more for enclosed. Mountain pickups carry a surcharge. The season and the carriers free on your dates set the final price.',
 prose(
  P('Texas and California send more households to Denver than anywhere else, so those inbound lanes stay full. The return legs to Dallas and Los Angeles price a little lower. Phoenix runs cheap because the snowbird trucks come back empty.'),
  P('Kansas City and Chicago ride 70 and 76 east all year. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Headquarters, the Aerospace Plants, the Hospitals, and the Campuses',
 prose(
  L('Denver relocates engineers, nurses, students, and transplants from Texas, and most arrive on a start date.'),
  P('The headquarters downtown and in the Tech Center bring in staff from every state. The aerospace plants in Littleton, Boulder, and Aurora hire engineers on program schedules. The federal center in Lakewood rotates people on its own calendar. Most newcomers ship one car and drive the other.'),
  P('The hospitals bring in residents each June and nurses all year. The medical campus in Aurora, the downtown hospital, and the hospitals on Colorado Boulevard hire every summer. We supply the paperwork a reimbursed move needs.'),
  P('The campus downtown on the Auraria site brings cars in each August. So do the university in University Park and the campuses in Boulder and Golden. The handoff for a student car happens at a lot near campus, and an adult signs for it.'),
  P('Transplants from Texas, California, and the Midwest arrive all year, and the corporate packages often cover the car. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side of a move.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Hail, Blizzards, the Stock Show, and a Mile of Altitude',
 prose(
  L('Denver weather turns in an hour. The carriers plan around the hail and the spring blizzards.'),
  P('Hail is the most expensive weather in the state, and it falls from May through August. A car waiting outside for pickup can be dented in minutes. We shift the window when a storm is forecast, and a collector car rides enclosed.'),
  P('Spring blizzards close Interstate 70 east of the airport and Interstate 25 toward Wyoming for a day. The March storms of 2019 and 2021 shut the city down for two. The carriers wait at the truck stops in Aurora or Commerce City. A winter pickup can slide a day or two.'),
  P('The stock show fills the grounds along Brighton Boulevard for sixteen days each January. The ballpark fills Lower Downtown on summer game nights. The stadium does the same on football Sundays. Move-in at the campuses fills late August. We move a pickup in those blocks to another day.'),
  P('Altitude changes the car, not the shipment. A car from sea level runs rough for a few days, and the tires read low. An electric car loses some range in the thin, cold air. Wildfire smoke in late summer slows the roads but rarely closes them.'),
 )+chips(["Lower Downtown","River North","Five Points","Capitol Hill","Uptown","Cheesman Park","Congress Park","City Park","Park Hill","Hilltop","Cherry Creek","Washington Park","Platt Park","Baker","University Park","The Highlands","Berkeley","Sunnyside","Sloan’s Lake","Central Park","Lowry","Montbello","Green Valley Ranch","Globeville","Elyria","Lakewood","Arvada","Westminster","Thornton","Northglenn","Broomfield","Golden","Littleton","Englewood","Centennial","Highlands Ranch","Lone Tree","Parker","Castle Rock","Boulder"])
 +NOTE('Serving Denver and the whole metro area, from Castle Rock to Broomfield and out to the airport. Tell us the neighborhood and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Denver?',
 prose(
  L('Open is how the Front Range ships, and the Texas and California lanes are priced for it.'),
  P('An enclosed trailer keeps the hail, the magnesium chloride, and the eyes off a car. The garages in Cherry Creek and Hilltop book them for collector cars. So does a car headed over the mountains in winter, since the road spray is corrosive.'),
  P('A daily driver rides open without a problem. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain what the roof buys you.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff on Brighton Boulevard or at a lot off Quebec, and a delivery. The forecast sets the hour.'),
  P('Approve the price, and a carrier already headed through the Mousetrap takes the booking. We confirm the spot and the window the same day. The driver inspects the car with you and marks its condition on a Bill of Lading. Both sign, and that sheet rides along to the delivery check.'),
 )+ULI([
  "Take your personal items out of the car",
  "Leave about a quarter tank of fuel",
  "Photograph the car before pickup, especially after a hailstorm",
  "Provide a working key and disclose any mechanical issue",
  "Turn off any aftermarket alarm",
  "On a bungalow block, pick a wide avenue or a lot where the truck can stop",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages take it from there.'))))

BODY.append(sec('Why Ship Guy','Why Denver Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already cross the Mousetrap. We plan around the hail, the blizzards, and the tunnel.'),
  P('Ship Guy’s brokerage authority with the FMCSA is active, and a $75,000 surety bond backs it. Both are searchable in the federal register. Our office is on Lawrence Street in Lower Downtown.'),
  P('One coordinator handles your shipment from the first quote to the delivery signature. Open, enclosed, and expedited transport are all available, and the <a href="services.html">services</a> page lists each one.'),
 ), alt=True))

BODY.append(office('Denver','1401 Lawrence St #1688','Denver, CO 80202','+19832122105','(983) 212-2105','MT',
 '1401+Lawrence+St+%231688,+Denver,+CO+80202','Visit Us','Find Ship Guy in Denver',
 'Our office is on Lawrence Street in Lower Downtown, a few blocks from Union Station and Speer.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4717.3373766298855!2d-104.9986103!3d39.7471232!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x876c790e32d31abd%3A0xed83356cfd8d0179!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792161728584!5m2!1sen!2sus'))

FAQ=[
 ("What if hail is forecast for my Denver pickup day?","We move the window. Front Range hail falls from May through August, and a car waiting outside can be dented in minutes. The carrier loads early in the morning or on the next clear day. A collector car rides on an enclosed trailer. We call the moment the forecast changes the plan."),
 ("How much does it cost to ship a car from Denver to Dallas or Los Angeles?","Dallas runs five hundred sixty to eight hundred twenty dollars for a sedan. That is about eight hundred miles down 25 and US 287. Los Angeles runs seven hundred fifty to ten hundred fifty. That is about a thousand miles on 70 and Interstate 15. SUVs and pickups add 10 to 25 percent."),
 ("Can the carrier come to my street in Capitol Hill or the Highlands?","Usually not. Capitol Hill has apartments parked on both curbs, and the Highlands streets are narrow under old trees. A seventy-five-foot rig cannot turn there. The driver meets you on Colfax, on Speer, on 38th Avenue, or at a lot nearby. Central Park, Park Hill, and most suburbs allow the curb."),
 ("Can you ship my car to or from the airport?","Yes. The lots off Peña Boulevard and along Tower Road work for a fly-and-ship handoff. E-470 charges a toll by plate on the way out, and it is in the quote. Tell us your flight, and the driver meets you within a window around it."),
 ("What happens if a blizzard hits on my pickup day?","The carriers wait at the truck stops in Aurora and Commerce City. Interstate 70 east of the airport and Interstate 25 toward Wyoming close for a day. A loaded trailer does not move on ice. A winter pickup can slide a day or two, and we call before it does."),
 ("Can you ship a car for a student at Auraria, DU, or CU Boulder?","Yes. Cars arrive each August and leave each May, and both windows fill early. The Auraria campus has lots along Speer, and University Park has lots off Evans Avenue. Boulder is tight, so the handoff happens at a lot off US 36. An adult signs for the car."),
 ("Do you handle relocations to the Tech Center or the aerospace plants?","Yes, all year. The Tech Center headquarters and the plants in Littleton and Boulder bring in staff on start dates. Most ship one car and drive the other. We provide the paperwork a reimbursed move needs, and the handoff works at a lot off Interstate 25."),
 ("Does the mountain traction law affect a Denver pickup?","Not in the city. The traction law covers Interstate 70 in the mountains from September through May. A Denver pickup headed east, north, or south never touches it. A car headed to Vail or Aspen meets the driver at a lot in Silverthorne or Frisco. That lane carries a mountain surcharge."),
 ("Can you ship a car that does not run from Denver?","Yes. The carrier arrives with a winch, and the quote already covers the slower loading. Choose a flat, open spot, which usually means a lot off Brighton Boulevard or Quebec Street. Let us know if it rolls, steers, and brakes."),
 ("What do you need for a Denver car shipping quote?","Both addresses, with the neighborhood on this end. The year, make, and model. Whether it runs and rolls. Open or enclosed, and the dates you can work with. That is everything an accurate Denver quote needs."),
]
BODY.append(faq_section(FAQ,'Denver FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Denver?','The form above prices your lane in about two minutes. Tell us the neighborhood and your dates. A carrier already headed through the Mousetrap takes it from there.','+19832122105','(983) 212-2105','Get your free Denver quote'))

build({
 'slug':'auto-transport-denver-colorado',
 'title':'Car Shipping in Denver, CO — Auto Transport | Ship Guy',
 'meta':'Car shipping in Denver, CO at the Mousetrap, where Interstate 25 meets 70. Capitol Hill and Highlands meeting spots, suburban curbside, airport fly-and-ship, hail and blizzard planning, Tech Center and aerospace relocations, hospital residents, campus move-in. Local office on Lawrence Street in Lower Downtown. Free quote.',
 'h1':'Car Shipping in<br>Denver, <span class="accent">Colorado</span>',
 'lede':'Open, enclosed, and expedited auto transport across the metro area, planned around 25, 70, the hail, and the blizzards.',
 'tel':'+19832122105','disp':'(983) 212-2105','brand':'Denver','keyword':'car shipping in denver',
 'localterms':['denver','mousetrap','interstate 25','interstate 70','interstate 76','interstate 225','interstate 270','valley highway','elyria','swansea','c-470','e-470','toll','peña boulevard','airport','us 36','us 6','santa fe drive','brighton boulevard','quebec street','speer boulevard','hampden avenue','colfax avenue','lower downtown','river north','union station','ballpark','blake street','capitol hill','uptown','cheesman park','the highlands','berkeley','sunnyside','38th avenue','federal boulevard','washington park','platt park','congress park','cherry creek','park hill','hilltop','central park','green valley ranch','montbello','highlands ranch','centennial','lone tree','lakewood','arvada','westminster','thornton','golden','boulder','castle rock','littleton','englewood','tech center','aerospace','federal center','hospitals','residents','medical campus','auraria','university park','hail','blizzards','2019','2021','stock show','stadium','altitude','electric car','wildfire smoke','magnesium chloride','traction law','silverthorne','colorado springs','fort collins','cheyenne','albuquerque','salt lake city','kansas city','omaha','dallas','phoenix','las vegas','chicago','los angeles','texas','california'],
}, BODY, FAQ)
