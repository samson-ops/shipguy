import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Boise, Idaho','Car shipping in the Treasure Valley, where Interstate 84 meets the Connector and the foothills begin',
 ['Car shipping in Boise starts on the Connector, the spur that carries Interstate 84 into downtown. Ship Guy is a licensed auto transport broker with an office on West Main Street downtown.',
  'We book vetted carriers across the Treasure Valley, from Eagle to Kuna and out to Mountain Home. We do not own the trucks.',
  'Interstate 84 runs the south edge of the city on its way from Oregon to Utah. Interstate 184 is the Connector, and it leaves 84 for downtown. State Street runs west to Eagle, and Highway 21 climbs into the mountains. Federal Way and Broadway carry the southeast.',
  'This page covers the interstate, the Connector, downtown, the North End, the Bench, and the foothills. It also covers the chip maker, the hospitals, the bases, the inversion, the smoke, and the lanes.'],
 'Boise at a glance',
 ['Most pickups happen within 1 to 3 days. Interstate 84 carries the Portland-to-Salt-Lake carriers past the city all day.',
  'Salt Lake City and Portland are a day out, and so is Spokane. Seattle, Reno, and Sacramento run one to two. Las Vegas, Los Angeles, and Denver run two, and the East runs three to four.'],
 'Tell us the neighborhood. The North End, the East End, and the foothills need a meeting spot. The Bench, Southeast Boise, and most of the suburbs allow the curb.'))

BODY.append(sec('The Roads','Interstate 84, the Connector, State Street, Federal Way, and Highway 21',
 prose(
  L('Boise sits on the one interstate that crosses the south of the state. The Connector is the ramp into town.'),
  P('Interstate 84 enters from Oregon and crosses Nampa and Meridian. It runs the south edge of Boise past the airport to Mountain Home. The ramps at Cole Road, Vista Avenue, Broadway, and Gowen Road reach the Bench and the southeast. It carries nearly every carrier that touches the valley.'),
  P('Interstate 184 is the Connector, the short freeway from 84 into downtown. It ends at Myrtle and Front, the one-way couplet through the core. State Street is Highway 44, the road west through the North End to Eagle. Chinden Boulevard runs parallel through Garden City. Highway 55 leaves for McCall, and Highway 21 climbs to Idaho City and the lake.'),
  P('Federal Way runs southeast past the chip maker to the desert. Broadway and ParkCenter reach the university and the river. Vista Avenue runs from the Connector to the airport. Fairview, Franklin, and Overland are the mile roads across the Bench. Hill Road and Bogus Basin Road climb into the foothills.'),
  P('The carriers come off 84 at Cole, Vista, and Broadway, and off the Connector at Fairview. The lots along Fairview, at the mall on Milwaukee, and off Federal Way are the usual meeting spots. No road in the valley charges a toll.'),
  P('Our office sits on West Main Street downtown, a block from the Basque Block.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the North End, the Bench, the Foothills, Southeast Boise, and Eagle',
 prose(
  L('Boise is a streetcar city with a desert bench and a mountain behind it. Each piece parks differently.'),
  P('Downtown is a grid of one-ways between the Connector and the foothills. The lots on the couplet work for a handoff. The North End has bungalows on narrow streets under old maples. The driver meets you on State Street or Harrison Boulevard. The East End along Warm Springs has big houses and tight streets. The handoff happens on Warm Springs or at the river.'),
  P('The Bench is the postwar grid above the river, from Vista to Cole. The truck usually reaches the curb. The Depot Bench and the Central Bench are the same. The foothills neighborhoods climb above Hill Road on steep, winding streets. The driver stays on Hill Road or Bogus Basin Road.'),
  P('Southeast Boise along Federal Way and ParkCenter is newer subdivisions, the university blocks, and Harris Ranch. The curb works on most of it. Garden City is light industry and new apartments along Chinden with room everywhere. Northwest Boise and the Collister area are wide grids off State Street.'),
  P('Eagle sits along the river and the foothills with gated communities and estate lots. The driver meets you at the gate or on State Street. Kuna, Star, and the subdivisions off Lake Hazel are growing faster than the carrier maps. Send the full address and the nearest main road. Meridian and Nampa next door have pages of their own.'),
 )))

ROUTES=[("Salt Lake City, UT","I-84 · ~340 mi","1 day","$320–$460"),("Portland, OR","I-84 · ~430 mi","1 day","$370–$530"),
 ("Spokane, WA","US-95 · ~420 mi","1 day","$370–$530"),("Seattle, WA","I-84/I-90 · ~500 mi","1 day","$400–$570"),
 ("Reno, NV","I-84/US-95 · ~420 mi","1 day","$370–$530"),("Sacramento, CA","I-84/I-80 · ~560 mi","1–2 days","$450–$650"),
 ("Las Vegas, NV","I-84/US-93 · ~630 mi","2 days","$470–$680"),("Los Angeles, CA","I-84/I-15 · ~850 mi","2 days","$580–$830"),
 ("Denver, CO","I-84/I-80 · ~820 mi","2 days","$560–$800"),("Chicago, IL","I-84/I-80 · ~1,700 mi","3–4 days","$1,000–$1,400")]
BODY.append(rate_table('Lanes &amp; Costs','Boise Car Shipping Lanes and Estimated Costs',
 'The lanes that leave the Treasure Valley most, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a running sedan on an open trailer, priced from Boise. An SUV or pickup adds roughly 10 to 25 percent, and enclosed adds more. The rush from the coast, the winter, and the carriers free on your dates set the final figure.',
 prose(
  P('The inbound lanes from California, Washington, and Oregon run full all year, and that keeps them competitive. The return legs to the coast run lighter, so an outbound quote can sit a little higher. Salt Lake City rides 84 straight down without a turn.'),
  P('Denver and the Midwest ride 84 and 80 through Wyoming. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Chip Maker, the Hospitals, the University, the Guard Base, and the Transplants',
 prose(
  L('Boise relocates engineers, nurses, students, and families from the coast. Most arrive on a closing date.'),
  P('The chip maker on Federal Way is the biggest private employer in the state. Its new fab is adding thousands of jobs. Engineers transfer in from every state on program dates, and most ship one car and drive the other. The two hospital systems bring in residents each June and nurses all year. The handoff works at a lot on Federal Way or at the hospital garages.'),
  P('The university on Broadway brings cars in each August. Move-in fills the blocks along University Drive for a weekend. An adult signs for a student car at a campus lot. The state offices around the Capitol hire on their own calendar. The grocery chain and the food company headquartered downtown relocate staff on start dates.'),
  P('The Guard base at the airport rotates airmen and soldiers on drill and deployment cycles. The Air Force base an hour southeast rotates families year round, with a summer peak. One car moves on the orders, and the family’s second car moves with us. Ship Guy is a private broker, unaffiliated with either base, and the <a href="military-car-shipping.html">military</a> page explains the timing.'),
  P('The households keep coming from California, Washington, and Oregon, each with a closing date. Most Boise bookings are timed to one, and when the closing moves, so does the delivery. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Inversion, Snow, Fire Smoke, Runoff, and Game Days',
 prose(
  L('Boise has four seasons and a fifth one made of smoke, and each touches a different road.'),
  P('Winter brings the inversion, when cold fog sits in the valley for weeks in December and January. The roads stay open, but the Bench hills ice over. The foothills streets close to a loaded trailer. The 2017 winter dropped two feet on the city and shut it down for days. A winter pickup can slide a day, and the carriers hold on 84.'),
  P('Fire season runs July through September. Smoke settles into the valley. A highway closure in the mountains reroutes a carrier by a hundred miles. Highway 55 and Highway 21 close for fire and rockfall. Summer heat passes one hundred degrees in July, and the loading hour moves to the morning.'),
  P('Spring runoff fills the river in May and June. The Greenbelt and the low roads along it flood. A pickup near the river moves up to the Bench. Wind on 84 across the desert slows a tall trailer in spring.'),
  P('Home football Saturdays fill Broadway and the university blocks from September through November. The music festival fills downtown for a week in March, and the fair fills Garden City in August. A pickup in those blocks moves to another day.'),
 )+chips(["Downtown","Basque Block","North End","Hyde Park","East End","Warm Springs","The Bench","Depot Bench","Central Bench","Vista","Cole","West Bench","Foothills","Highlands","Southeast Boise","ParkCenter","Harris Ranch","Barber Valley","Federal Way","Lake Hazel","Garden City","Northwest Boise","Collister","Eagle","Star","Kuna","Hidden Springs","Mountain Home"])
 +NOTE('Serving Boise and the whole Treasure Valley, from Eagle to Mountain Home. Tell us the neighborhood, the gate, and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Boise?',
 prose(
  L('Open is how the valley ships, and the coast lanes are priced for it.'),
  P('An enclosed trailer keeps the road salt, the smoke, and attention off a car. The garages in Eagle and the East End book them for collector cars. So does an engineer moving a restored car from California.'),
  P('A daily driver goes open and arrives fine. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages compare the two.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff on Fairview or at a lot off Federal Way, and a delivery. The pass forecast sets the day.'),
  P('Approve the price, and a carrier already crossing the valley on 84 is booked. The lot and the window are set that day. The driver inspects the car with you and notes its condition on a Bill of Lading. Both of you sign, and the same sheet is read again at delivery.'),
 )+ULI([
  "Clear everything personal out of the car",
  "Leave roughly a quarter tank of fuel",
  "Photograph each side before the handoff, smoke film and all",
  "Give the driver a working key and name any mechanical issue",
  "Switch off any aftermarket alarm",
  "In the North End or the foothills, pick a wide street or a lot for the truck",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Boise Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already run 84 between the coast and Utah. We plan around the inversion, the smoke, and the closing date.'),
  P('Ship Guy’s broker authority with the FMCSA is current, and a $75,000 surety bond backs it. The federal register shows both. Our office is on West Main Street downtown.'),
  P('From the first quote to the delivery signature, you have one coordinator. The <a href="services.html">services</a> page sets out open, enclosed, and expedited transport.'),
 ), alt=True))

BODY.append(office('Boise','999 W Main St #425A','Boise, ID 83702','+12089244078','(208) 924-4078','MT',
 '999+W+Main+St+%23425A,+Boise,+ID+83702','Visit Us','Find Ship Guy in Boise',
 'Our office is on West Main Street downtown, a block from the Basque Block.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4441.864551138731!2d-116.20563620000001!3d43.6163612!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x54aef96026a1edf5%3A0x9c252150a5901cd9!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792170048465!5m2!1sen!2sus'))

FAQ=[
 ("Can you time delivery to my closing date in Boise?","Yes. Boise closings drive more of our bookings than anything else. The delivery window is built around the closing date. If the closing slides, the window slides with it. Say so as soon as you know, and the carrier adjusts."),
 ("How much does it cost to ship a car from California or Washington to Boise?","Sacramento runs four hundred fifty to six hundred fifty dollars for a sedan. That is about five hundred sixty miles on 80 and 84. Seattle runs four hundred to five hundred seventy, about five hundred miles on 90 and 84. Los Angeles lands between five hundred eighty and eight hundred thirty. Full inbound trailers keep those numbers down. Add 10 to 25 percent for an SUV or pickup."),
 ("Can the carrier come to my street in the North End or the foothills?","Usually not. The North End streets are narrow under old maples, and the foothills streets are steep and winding. The driver meets you on State Street, on Harrison Boulevard, or on Hill Road. The Bench, Southeast Boise, and most of the suburbs allow the curb."),
 ("Do you ship cars for engineers transferring to the chip maker?","Yes, all year, on program dates. Engineers arrive from every state, and most ship one car and drive the other. The handoff works at a lot on Federal Way. We provide the paperwork a reimbursed move needs."),
 ("What happens if the inversion or a snowstorm hits on my pickup day?","Fog from the inversion slows traffic without closing anything, and the trucks keep running. A real snowstorm glazes the Bench hills and shuts the foothills streets to a loaded trailer. The carriers wait on 84 for the plows, and a winter pickup may lose a day. You hear from us before it does."),
 ("Does fire season affect car shipping in Boise?","Sometimes. Smoke settles into the valley from July through September. A fire closure on Highway 55 or 21 reroutes a carrier by a hundred miles. Interstate 84 almost never closes for fire. A pickup in the valley runs normally, and a mountain pickup waits for the road to reopen."),
 ("Can you handle a PCS move to Mountain Home or Gowen Field?","Yes, on every rotation. The Air Force base rotates families year round with a summer peak. The Guard base at the airport rotates on drill and deployment cycles. The orders move one car, and the second rides with us. Housing is gated, so the driver waits outside it. Ship Guy is a private broker and is not connected to either base."),
 ("Can you ship a car for a Boise State student?","Yes. Cars arrive each August and leave each May, and both windows book up early. Move-in fills the blocks along University Drive for a weekend. The handoff happens at a campus lot off Broadway. A parent or another adult signs at pickup."),
 ("Can you ship a car that does not run from Boise?","Yes. A winch truck takes the job, and the longer loading is already in the price. A lot on Fairview or off Federal Way gives the driver a flat, open spot. Say whether the car rolls, steers, and brakes when you book."),
 ("What do you need for a Boise car shipping quote?","Both addresses, with the neighborhood or the gate on the Boise end. The year, make, and model. Whether it runs and rolls. Open or enclosed, and a date range that fits the closing. That is a complete Boise request."),
]
BODY.append(faq_section(FAQ,'Boise FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Boise?','The form above returns a price in about two minutes. Name the neighborhood and the dates, and a carrier already on 84 picks it up from there.','+12089244078','(208) 924-4078','Get your free Boise quote'))

build({
 'slug':'auto-transport-boise-idaho',
 'title':'Car Shipping in Boise, ID — Auto Transport | Ship Guy',
 'meta':'Car shipping in Boise, ID on Interstate 84 and the Connector. Closing-date deliveries for transplants from California and Washington, chip maker transfers, North End and foothills meeting spots, Bench curbside, Mountain Home and Gowen Field second cars, inversion and fire-smoke planning. Local office on West Main Street downtown. Free quote.',
 'h1':'Car Shipping in<br>Boise, <span class="accent">Idaho</span>',
 'lede':'Open, enclosed, and expedited auto transport across the Treasure Valley, planned around 84, the Connector, the closing date, and the winter.',
 'tel':'+12089244078','disp':'(208) 924-4078','brand':'Boise','keyword':'car shipping in boise',
 'localterms':['boise','interstate 84','interstate 184','connector','myrtle','front','state street','highway 44','chinden','highway 55','mccall','highway 21','federal way','broadway','parkcenter','vista','fairview','franklin','overland','cole','hill road','bogus basin','mall','milwaukee','airport','downtown','main street','basque block','couplet','north end','harrison','hyde park','east end','warm springs','the bench','depot bench','foothills','southeast boise','harris ranch','university','garden city','northwest boise','collister','eagle','star','kuna','lake hazel','mountain home','chip maker','fab','engineers','hospital','residents','nurses','capitol','grocery','food company','guard base','air force base','orders','closing date','transplants','california','washington','oregon','inversion','snow','2017','fire season','smoke','runoff','greenbelt','football','music festival','fair','salt lake city','portland','spokane','seattle','reno','sacramento','las vegas','los angeles','denver','chicago'],
}, BODY, FAQ)
