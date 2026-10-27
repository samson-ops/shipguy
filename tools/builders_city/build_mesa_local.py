import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Mesa, Arizona','Car shipping in the winter-visitor capital of the East Valley, along US 60 and the two loops',
 ['Car shipping in Mesa starts on the Superstition Freeway, the US 60 spine every East Valley truck uses. Ship Guy is a licensed auto transport broker with an office on Main Street downtown.',
  'We book vetted carriers across the East Valley, from the Tempe line to Apache Junction and Gateway. We do not own the trucks.',
  'US 60 runs east and west through the middle of the city. Loop 202 wraps the north side as the Red Mountain Freeway and the south as the Santan. Loop 101 runs the west edge, and State Route 24 reaches the Gateway airport. Main Street carries the light rail downtown.',
  'This page covers the freeway, the loops, downtown, the RV resorts, the age-restricted communities, and the new southeast. It also covers the helicopter plant, the data centers, the snowbird season, the monsoon, and the lanes.'],
 'Mesa at a glance',
 ['Most pickups happen within 1 to 3 days from October to April and faster in summer. The Interstate 10 carriers reach the East Valley on US 60 and the 202 all day.',
  'Phoenix and Tucson are same-day lanes. Flagstaff and Yuma take a day. Las Vegas, San Diego, and Los Angeles take one too. Salt Lake City, Denver, and the snowbird lanes north take two to four.'],
 'Tell us the community and the gate. The RV resorts, Las Sendas, and the age-restricted communities need a meeting spot. Dobson Ranch, the central grids, and Eastmark usually allow the curb.'))

BODY.append(sec('The Roads','US 60, Loop 202, Loop 101, State Route 24, and Main Street',
 prose(
  L('Mesa has no interstate of its own, and three freeways make sure it never needs one.'),
  P('US 60 is the Superstition Freeway. It runs the length of the city from the Tempe line to Apache Junction. It carries the Interstate 10 carriers in from the west and the Globe traffic from the east. The ramps at Dobson, Country Club, Gilbert Road, Val Vista, Power Road, and Signal Butte reach every neighborhood.'),
  P('Loop 202 wraps the north side along the Salt River as the Red Mountain Freeway. The south side is the Santan. Loop 101 is the Price Freeway on the west edge. State Route 24 leaves the 202 for the Gateway airport and Eastmark. State Route 87 is Country Club Drive, and it climbs north to Payson.'),
  P('Main Street is the old US 60 with the light rail down the middle. A trailer cannot stop on it. Broadway, Southern, Baseline, University, and McKellips are the mile roads that cross the city. Falcon Field sits off McKellips on the north side. The Apache Trail leaves east for the lake country.'),
  P('The carriers come off 60 at Dobson, Stapley, and Power Road. Off the 202, they use Higley and Ellsworth. The lots at Riverview, along Power Road, and at the Superstition Springs center are the usual meeting spots. No road in the East Valley charges a toll.'),
  P('Our office sits on Main Street downtown, a block from the arts center and the light rail.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, Dobson Ranch, Lehi, Las Sendas, the RV Resorts, and Eastmark',
 prose(
  L('Mesa is a farm town that became the third-largest city in the state. It parks in a dozen different ways.'),
  P('Downtown has Main Street and the temple district on a grid of wide streets. The light rail runs through it. A trailer meets you on a side street or at a lot off Country Club. West Mesa and the Fiesta District are older grids where the truck reaches the curb. Dobson Ranch is a lake community with wide streets and some gates.'),
  P('Lehi on the north side is horse property with irrigation ditches, dirt roads, and no curbs. The driver meets you on McKellips. Las Sendas, Red Mountain Ranch, and Mountain Bridge climb the hills behind gates. The driver meets you at the gate or at a lot on Power Road. Alta Mesa and the central grids usually allow the curb.'),
  P('East Mesa holds dozens of RV resorts and age-restricted communities. Leisure World, Sunland Village, Fountain of the Sun, and the resorts along Main Street all have gates. Tell us the resort and the gate code, and we clear access ahead of time. Most meet the driver at the gate or at a lot on Main.'),
  P('Eastmark and Cadence in the southeast are new master-planned communities with wide streets and alleys. The truck reaches the curb. Apache Junction and Gold Canyon beyond the city line ride the same carriers. Gold Canyon is gated, and Apache Junction is RV parks and open lots. The Gateway airport sits between them with room everywhere.'),
 )))

ROUTES=[("Phoenix, AZ","US-60/I-10 · ~20 mi","Same day","$120–$200"),("Tucson, AZ","US-60/I-10 · ~110 mi","Same day","$150–$240"),
 ("Las Vegas, NV","US-60/US-93 · ~300 mi","1 day","$280–$410"),("San Diego, CA","I-10/I-8 · ~370 mi","1 day","$340–$490"),
 ("Los Angeles, CA","I-10 · ~390 mi","1 day","$350–$500"),("Albuquerque, NM","SR-87/I-40 · ~460 mi","1 day","$400–$570"),
 ("Salt Lake City, UT","I-17/I-15 · ~660 mi","2 days","$490–$700"),("Denver, CO","I-17/I-40/I-25 · ~830 mi","2 days","$560–$800"),
 ("Seattle, WA","I-10/I-5 · ~1,450 mi","3 days","$950–$1,350"),("Minneapolis, MN","I-40/I-35 · ~1,700 mi","3–4 days","$1,000–$1,450")]
BODY.append(rate_table('Lanes &amp; Costs','Mesa Car Shipping Lanes and Estimated Costs',
 'Where East Valley cars most often go, with estimated open-trailer ranges. Your exact lane prices above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Mesa, open trailer, running sedan. Expect roughly 10 to 25 percent more for an SUV or pickup, and more again for enclosed. The snowbird season outweighs distance, and the carriers free on your dates set the final figure.',
 prose(
  P('Mesa prices like Phoenix on every lane, because the same Interstate 10 carriers reach both. The northern lanes swing with the season. A car headed to Minneapolis or Seattle in April rides a trailer that came down full in November. The price follows the direction of the crowd.'),
  P('California lanes ride Interstate 10 all year. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Winter Visitors, the Helicopter Plant, the Hospitals, and the Data Centers',
 prose(
  L('Mesa fills up every October and empties every April, and the carriers run on that tide.'),
  P('Winter visitors from Minnesota, Iowa, Washington, and the Canadian prairies arrive from October through December. They fill the RV resorts and the age-restricted communities until April. Many ship a second car down for the season and ship it home in spring. We handle the domestic leg, and a car crossing from Canada clears customs before we touch it.'),
  P('The helicopter plant at Falcon Field is the largest private employer in the city. It hires engineers on program schedules. The data centers along Elliot Road and the chip and medical device firms around them do the same. The <a href="snowbird-car-shipping.html">snowbird</a> page covers the seasonal lane.'),
  P('The hospitals along Dobson, Baywood, and Gateway bring in nurses all year and residents each June. The community college and the polytechnic campus at Gateway bring cars in each August. An adult signs for a student car at a campus lot. We supply the paperwork a reimbursed move needs.'),
  P('Families arrive from California for the prices and the schools, and the second car usually rides a truck. Retirees who stop going home sell the northern house and ship the last car down. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Snowbird Season, Spring Training, the Heat, and the Monsoon',
 prose(
  L('Mesa has two seasons for shipping cars, and the weather decides the loading hour in both.'),
  P('From October through April, inbound carriers arrive full and outbound space is scarce until the visitors head home. Book two to three weeks ahead in both windows. From March through May the direction reverses, and the northbound trailers fill. Summer is the easy season, with open space in every direction.'),
  P('Spring training fills Riverview and the lots along Dobson for six weeks in February and March. The Renaissance festival fills US 60 east on weekends in those months. The Easter pageant fills downtown for a week in spring. A pickup in those blocks moves to another day.'),
  P('From June through September the thermometer passes 110, and the carriers load at first light. Tires and batteries are checked before a long haul. The monsoon follows in July and August. A dust wall on US 60 or Interstate 10 blanks the road for an hour. The carriers wait on the shoulder. The washes run, and a pickup beside one moves to higher ground.'),
  P('Spring wind slows a tall trailer on the open desert east of the city in March and April. The rest of the year, the weather is the reason people come. Nothing about loading or transport changes on a clear day.'),
 )+chips(["Downtown","Main Street","Temple District","West Mesa","Fiesta District","Riverview","Dobson Ranch","Lehi","Alta Mesa","Northeast Mesa","Las Sendas","Red Mountain Ranch","Mountain Bridge","Falcon Field","East Mesa","Superstition Springs","Leisure World","Sunland Village","Fountain of the Sun","Dreamland Villa","Eastmark","Cadence","Gateway","Apache Junction","Gold Canyon","Queen Creek"])
 +NOTE('Serving Mesa, Apache Junction, and the whole East Valley. Tell us the community, the gate code, and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Mesa?',
 prose(
  L('Open is how the East Valley ships, and the snowbird lanes are priced for it.'),
  P('An enclosed trailer keeps the dust, the sun, and attention off a car. The garages in Las Sendas and Gold Canyon book them for collector cars. So does a car bought at the January auctions up the road.'),
  P('A seasonal second car or a daily driver goes open and arrives fine. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages compare the two.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff at the gate or a lot on Power Road, and a delivery. The season sets the lead time.'),
  P('Approve the price, and we book a carrier already working the East Valley. The spot and the window are confirmed that day. The driver and you check the car over, and the Bill of Lading records what you both see. Two signatures, and the same sheet is checked at delivery.'),
 )+ULI([
  "Clear personal items out of the car",
  "Keep roughly a quarter tank of fuel in it",
  "Shoot photos of the car before pickup, dust included",
  "Supply a working key and name any mechanical issue",
  "Shut down any aftermarket alarm",
  "In a resort or gated community, send the gate code or meet at the gate",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Mesa Drivers Choose Ship Guy',
 prose(
  L('We ride the snowbird tide in both directions. We plan around the gates, the heat, and the monsoon.'),
  P('Ship Guy carries active FMCSA brokerage authority and a $75,000 surety bond, and the federal register lists both. Our office is on Main Street downtown.'),
  P('Your coordinator does not change between the quote and the delivery. The <a href="services.html">services</a> page covers open, enclosed, and expedited transport.'),
 ), alt=True))

BODY.append(office('Mesa','225 E Main St #144B','Mesa, AZ 85201','+19284476589','(928) 447-6589','MST',
 '225+E+Main+St+%23144B,+Mesa,+AZ+85201','Visit Us','Find Ship Guy in Mesa',
 'Our office is on Main Street downtown, a block from the arts center and the light rail.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5121.249258903212!2d-111.8258077!3d33.414646499999996!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x872ba76911e1ba05%3A0xf9d21165103b4d4a!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792169773192!5m2!1sen!2sus'))

FAQ=[
 ("How far ahead should I book a Mesa pickup in winter?","Two to three weeks from October through April. Inbound carriers arrive full of seasonal cars. Outbound space is scarce until the visitors head home in spring. A summer pickup books in a few days. In the busy months, a loose date range is worth more than anything else."),
 ("Can the carrier come into my RV resort or age-restricted community?","Sometimes. Leisure World, Sunland Village, and most of the resorts along Main Street have gates and truck rules. Give us the resort name and the gate code, and we check access before the truck is dispatched. If the truck cannot enter, the handoff happens at the gate or a lot on Main."),
 ("How much does it cost to ship a car from Mesa to Minneapolis or Seattle?","Minneapolis runs one thousand to fourteen hundred fifty dollars for a sedan, about seventeen hundred miles. Seattle runs nine hundred fifty to thirteen hundred fifty, about fourteen hundred fifty miles. Season outweighs distance, and a northbound car in April costs more than one in July. SUVs and pickups add 10 to 25 percent."),
 ("Do you ship cars for Canadian winter visitors?","We handle the domestic leg. A car coming down from Alberta or Saskatchewan clears customs at the border first. We ship it from the first stop inside the country. Many visitors drive down and ship home, or the reverse. Give us the dates on each end of the season."),
 ("What happens if a dust storm or the monsoon hits on my pickup day?","The carriers pull off and wait. A wall of dust on US 60 or Interstate 10 drops visibility to nothing for an hour. Flash floods close the washes, and a pickup near one moves to higher ground. The storm passes, the loading happens that evening or the next morning, and we call before it moves."),
 ("Can the carrier come to my street in Lehi or Las Sendas?","Not usually. Lehi has dirt roads, ditches, and no curbs, and Las Sendas sits on the hills behind a gate. The driver meets you on McKellips, at the gate, or at a lot on Power Road. Dobson Ranch, the central grids, and Eastmark allow the curb."),
 ("Does spring training affect my pickup?","Near Riverview, yes. The ballpark fills the lots along Dobson and the 202 for six weeks in February and March. We move a pickup in those blocks to another day or an early hour. The rest of the city runs normally."),
 ("Can you ship a car for an ASU Polytechnic or Mesa Community College student?","Yes. Cars arrive each August and leave each May, and both windows book up early. The campus lots at Gateway and off Dobson work for the handoff. A parent or another adult signs at pickup."),
 ("Can you ship a car that does not run from Mesa?","Yes. A winch-equipped truck takes it, and the slower loading is already in the quote. A lot on Power Road or at Riverview gives the driver a flat, open place. Say whether it rolls, steers, and brakes."),
 ("What do you need for a Mesa car shipping quote?","Both addresses, with the community and the gate code on this end. The year, make, and model. Whether it runs and rolls. Open or enclosed, and the dates you can work with, the season in mind. That is everything a Mesa quote needs."),
]
BODY.append(faq_section(FAQ,'Mesa FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Mesa?','The form above prices your lane in about two minutes. Tell us the community and your dates. A carrier already working the East Valley takes it from there.','+19284476589','(928) 447-6589','Get your free Mesa quote'))

build({
 'slug':'auto-transport-mesa-arizona',
 'title':'Car Shipping in Mesa, AZ — Auto Transport | Ship Guy',
 'meta':'Car shipping in Mesa, AZ, the winter-visitor capital of the East Valley, along US 60 and the 202. RV resort and age-restricted community gates, Las Sendas and Lehi meeting spots, Eastmark curbside, snowbird lanes north, Canadian visitors, spring training, heat and monsoon planning. Local office on Main Street downtown. Free quote.',
 'h1':'Car Shipping in<br>Mesa, <span class="accent">Arizona</span>',
 'lede':'Open, enclosed, and expedited auto transport across the East Valley, planned around US 60, the loops, the gates, and the season.',
 'tel':'+19284476589','disp':'(928) 447-6589','brand':'Mesa','keyword':'car shipping in mesa',
 'localterms':['mesa','us 60','superstition freeway','loop 202','red mountain','santan','loop 101','price freeway','state route 24','gateway','state route 87','country club','payson','main street','light rail','broadway','southern','baseline','university','mckellips','dobson','stapley','gilbert road','val vista','power road','higley','ellsworth','signal butte','falcon field','apache trail','riverview','superstition springs','downtown','temple','arts center','west mesa','fiesta district','dobson ranch','lehi','las sendas','red mountain ranch','mountain bridge','alta mesa','east mesa','leisure world','sunland village','fountain of the sun','rv resorts','age-restricted','gate code','eastmark','cadence','apache junction','gold canyon','winter visitors','minnesota','canadian','customs','helicopter plant','data centers','elliot road','hospitals','nurses','residents','community college','polytechnic','snowbird','spring training','renaissance','easter pageant','monsoon','dust','flash floods','washes','spring wind','phoenix','tucson','flagstaff','yuma','las vegas','san diego','los angeles','albuquerque','salt lake city','denver','seattle','minneapolis','california'],
}, BODY, FAQ)
