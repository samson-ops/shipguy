import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Chandler, Arizona','Car shipping in the Silicon Desert, between Interstate 10 and the Santan Freeway',
 ['Car shipping in Chandler starts on the Price Road corridor, where the chip plants line Loop 101. Ship Guy is a licensed auto transport broker with an office on West Ray Road near the 101.',
  'We book vetted carriers across the southeast valley, from Ahwatukee to Gilbert and down to Sun Lakes. We do not own the trucks.',
  'Interstate 10 runs along the west edge of the city on the way from Phoenix to Tucson. Loop 101 is the Price Freeway, the north-south spine on the west side. Loop 202 is the Santan Freeway, and it crosses the middle of the city. Arizona Avenue runs through downtown.',
  'This page covers the interstate, the two loops, downtown, the Price corridor, the gated south, and Sun Lakes. It also covers the chip plants, the Oregon transfers, the hospitals, the heat, the monsoon, and the lanes.'],
 'Chandler at a glance',
 ['Most pickups happen within 1 to 3 days. The Interstate 10 carriers between Phoenix and Tucson pass the west edge all day.',
  'Phoenix and Tucson are same-day lanes. Mesa and Gilbert are minutes away. San Diego, Los Angeles, and Las Vegas take a day. El Paso and Albuquerque take one too. Sacramento, Austin, and Portland take two to three.'],
 'Tell us the neighborhood and the gate. Downtown, Ocotillo, and Sun Lakes need a meeting spot. The central grids and most of the subdivisions allow the curb.'))

BODY.append(sec('The Roads','Interstate 10, Loop 101, Loop 202, Arizona Avenue, and the Price Corridor',
 prose(
  L('Chandler sits in the corner where the interstate meets two loops. The carriers never have to leave a freeway.'),
  P('Interstate 10 runs down the west edge of the city between Ahwatukee and the chip plants. It carries the Phoenix-to-Tucson carriers and every California truck headed east. The ramps at Chandler Boulevard, Ray Road, and Queen Creek Road are the way in from the west. The dust storms on 10 south of the city are the one thing that stops it.'),
  P('Loop 101 is the Price Freeway. It runs north from the 202 past the chip plants to Tempe and Scottsdale. Loop 202 is the Santan Freeway. It crosses the city east to west from 10 to Gilbert and Mesa. The ramps at Arizona Avenue, McQueen, Cooper, and Gilbert Road reach the middle and the east side.'),
  P('Arizona Avenue is State Route 87, the north-south main street through downtown and on to Sun Lakes. Chandler Boulevard, Ray Road, Warner, Elliot, Germann, Queen Creek, and Ocotillo are the mile roads. Price Road is the corridor itself, from the chip campuses to the bank towers. Alma School and Dobson carry the west side.'),
  P('The carriers come off 10 at Ray Road and Chandler Boulevard. Off the 202, they use Arizona Avenue and Gilbert Road. The lots at the mall, along Arizona Avenue, and on Ray Road are the usual meeting spots. No road in the southeast valley charges a toll.'),
  P('Our office sits on West Ray Road, a minute from the Price Freeway ramps.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the Price Corridor, Ocotillo, Fulton Ranch, and Sun Lakes',
 prose(
  L('Chandler is a ranch town that turned into a chip town. Most of it was built with wide streets.'),
  P('Downtown has the square, the old hotel, and the arts center on a grid of narrow streets. A trailer meets you on Arizona Avenue or at a lot off Chandler Boulevard. The central grids between Alma School and McQueen are postwar and seventies blocks. The truck usually reaches the curb.'),
  P('The Price corridor is campuses, bank towers, and apartment complexes with garages and wide streets. A handoff works in any of the lots along Price. West Chandler along Ray and Warner is subdivisions with the same answer. The Ahwatukee side of the interstate rides the same carriers.'),
  P('Ocotillo, Fulton Ranch, and Clemente Ranch in the south are lake and golf communities with gates. The driver meets you at the gate or at a lot on Ocotillo Road. Cooper Commons and the subdivisions along Germann and Queen Creek have wide streets. The curb works on most. Send the gate code where there is one.'),
  P('Sun Lakes south of the city is an age-restricted community with gates and golf cart lanes. The driver meets you at the gate on Riggs Road or Alma School. The reservation land south of Sun Lakes and the casino lots off Interstate 10 ride the same carriers. Gilbert and Mesa are minutes east with pages of their own.'),
 )))

ROUTES=[("Phoenix, AZ","I-10 · ~25 mi","Same day","$120–$200"),("Tucson, AZ","I-10 · ~95 mi","Same day","$150–$240"),
 ("Las Vegas, NV","I-10/US-93 · ~310 mi","1 day","$280–$410"),("San Diego, CA","I-10/I-8 · ~350 mi","1 day","$330–$470"),
 ("Los Angeles, CA","I-10 · ~375 mi","1 day","$350–$500"),("El Paso, TX","I-10 · ~400 mi","1 day","$360–$520"),
 ("Albuquerque, NM","I-10/I-25 · ~460 mi","1 day","$400–$570"),("Sacramento, CA","I-10/I-5 · ~760 mi","2 days","$540–$770"),
 ("Austin, TX","I-10 · ~1,000 mi","2–3 days","$680–$960"),("Portland, OR","I-10/I-5 · ~1,330 mi","3 days","$880–$1,250")]
BODY.append(rate_table('Lanes &amp; Costs','Chandler Car Shipping Lanes and Estimated Costs',
 'Where southeast valley cars go most often, with estimated open-trailer ranges. The form above prices your exact route.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates, priced from Chandler for a sedan that runs, open trailer. SUVs and pickups run roughly 10 to 25 percent higher, enclosed higher still. The chip transfers, the season, and the carriers free on your dates set the final figure.',
 prose(
  P('Chandler prices like Phoenix on every lane, because the interstate runs along the city line. The Oregon, Northern California, and New Mexico lanes run full with chip plant transfers. Texas rides Interstate 10 straight east without a turn.'),
  P('The snowbird season lifts the northern lanes from October through April. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Chip Plants, the Banks, the Hospitals, and the Transfers From Oregon',
 prose(
  L('Chandler relocates engineers in both directions, and the chip company calendar runs the year.'),
  P('The chip maker’s campuses on Price and at Ocotillo are the biggest private employer in the city. The new fabs added thousands of jobs. Engineers transfer in from Oregon, Northern California, and New Mexico on program dates, and others transfer out. Most ship one car and drive the other.'),
  P('The other chip and electronics firms along Price and Chandler Boulevard hire on the same cycles. The launch vehicle plant and the bank campuses along Price relocate staff on start dates. We supply the paperwork a reimbursed move needs. The handoff works in any of the lots along Price.'),
  P('The two hospitals bring in nurses all year and residents each June. The community college on the east side brings cars in each August. An adult signs for a student car at a campus lot. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
  P('Retirees fill Sun Lakes from October through April, and many ship a second car down for the season. Families arrive from California for the schools and the prices. The <a href="snowbird-car-shipping.html">snowbird</a> page covers the seasonal lane, and the second car usually rides a truck.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Heat, the Dust on Interstate 10, the Ostrich Festival, and the Season',
 prose(
  L('Chandler weather is a summer problem and a dust problem, and the carriers plan around both.'),
  P('The heat passes 110 degrees from June through September. The driver loads early, and tires and batteries are checked before a long haul. Nothing else about the process changes. A car waiting outside gets a shade spot when there is one.'),
  P('The monsoon arrives in July and August with dust walls and flash floods. The dust comes up Interstate 10 from the farms around Casa Grande and Picacho. Visibility drops to nothing. The carriers pull off until it passes. The washes flood, and a pickup near one moves to higher ground.'),
  P('The ostrich festival fills Tumbleweed Park and the roads around Germann and McQueen for a weekend in March. The jazz festival fills downtown in April, and the tree lighting fills it in December. A pickup in those blocks moves to another day. Spring training traffic reaches the 101 in March.'),
  P('From October through April, the snowbird season fills inbound carriers and tightens outbound space. Book two to three weeks ahead in those months. Summer is the easy season. Spring wind slows a tall trailer on the open desert south of the city in March and April.'),
 )+chips(["Downtown","Arizona Avenue","Price Corridor","Ocotillo","Fulton Ranch","Clemente Ranch","Cooper Commons","Circle G","West Chandler","Ray Road","Warner Ranch","Pecos Ranch","Germann","Queen Creek Road","Sun Lakes","Riggs Road","Alma School","McQueen","Cooper","Gilbert Road","Ahwatukee","Gila River","Wild Horse Pass","Gilbert","Mesa","Tempe"])
 +NOTE('Serving Chandler, Sun Lakes, and the whole southeast valley. Name the neighborhood and the gate, and say whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Chandler?',
 prose(
  L('Most cars leave the southeast valley on an open trailer, and the California lanes are priced that way.'),
  P('A closed trailer shields a car from dust, sun, and curious eyes. Engineers moving a collector car from Oregon tend to book one. The garages in Ocotillo and Fulton Ranch book them for the shows.'),
  P('A commuter car goes open and arrives fine. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages lay out the trade.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff at a lot on Price or Ray Road, and a delivery. The heat sets the hour.'),
  P('Approve the number, and a carrier already running Interstate 10 is booked. You get the lot and the window that day. At pickup, the driver documents the car on a Bill of Lading as you watch. It is signed by both of you and compared at delivery.'),
 )+ULI([
  "Remove everything personal from the cabin and trunk",
  "Bring the fuel down to about a quarter tank",
  "Photograph all four sides before the handoff",
  "Leave a working key and flag any mechanical problem",
  "Deactivate any aftermarket alarm",
  "Behind a gate, send the code ahead or meet the truck at the entrance",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Chandler Drivers Choose Ship Guy',
 prose(
  L('We book the Interstate 10 carriers that already pass the city line. We plan around the transfers, the gates, and the heat.'),
  P('Ship Guy’s FMCSA broker license is active, and a $75,000 bond stands behind every booking. Both records are public in the federal register. Our office is on West Ray Road near the 101.'),
  P('One coordinator carries your move from the quote to the delivery call. Open, enclosed, and expedited transport are described on the <a href="services.html">services</a> page.'),
 ), alt=True))

BODY.append(office('Chandler','3075 W Ray Rd #525','Chandler, AZ 85226','+19286123715','(928) 612-3715','MST',
 '3075+W+Ray+Rd+%23525,+Chandler,+AZ+85226','Visit Us','Find Ship Guy in Chandler',
 'Our office is on West Ray Road, a minute from the Price Freeway ramps.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5126.861034835237!2d-111.89572190000001!3d33.3193628!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x872b07712357b18b%3A0x21e5aca06aef4233!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792169784291!5m2!1sen!2sus'))

FAQ=[
 ("Do you ship cars for engineers transferring to the chip plants?","Yes, in both directions and all year. Transfers arrive from Oregon, Northern California, and New Mexico on program dates. Most ship one car and drive the other. The handoff works in any of the lots along Price. We provide the paperwork a reimbursed move needs."),
 ("How much does it cost to ship a car from Chandler to Portland or Sacramento?","Portland runs eight hundred eighty to twelve hundred fifty dollars for a sedan. That is about thirteen hundred thirty miles on 10 and Interstate 5. Sacramento runs five hundred forty to seven hundred seventy, about seven hundred sixty miles. Both lanes move with the chip plant transfers. SUVs and pickups add 10 to 25 percent."),
 ("Can the carrier come into Ocotillo, Fulton Ranch, or Sun Lakes?","Often, if the gate allows trucks. Ocotillo and Fulton Ranch have gates on many entrances, and Sun Lakes has gates and golf cart lanes. Send the community name and the gate code, and we confirm access before dispatch. Where the truck cannot enter, the driver meets you at the gate."),
 ("What happens if a dust storm hits Interstate 10 on my pickup day?","The driver gets off the interstate and waits it out. In July and August, dust lifts off the farm fields south of the city and blanks out 10. The car loads that evening or at first light. We call before the window changes."),
 ("How far ahead should I book in the winter?","Two to three weeks from October to April. The winter visitors fill the inbound trailers, and outbound room runs short. Summer bookings take a few days. A loose date range is the best lever in the busy months."),
 ("Can the carrier come to my street downtown or in the central grids?","Downtown, no. The streets around the square are narrow. The driver meets you on Arizona Avenue or at a lot off Chandler Boulevard. The central grids between Alma School and McQueen usually allow the curb. So do the subdivisions along Germann and Queen Creek."),
 ("Can you ship a car to or from Ahwatukee or the reservation?","Yes, and both price the same as Chandler. Ahwatukee sits across the interstate and rides the same carriers. The casino lots off Interstate 10 work for a handoff on the reservation side. Send the community name for a gated Ahwatukee address."),
 ("Can you ship a car for a Chandler-Gilbert Community College student?","Yes. Cars arrive each August and leave each May, and both windows book up early. The campus lots on Pecos Road work for the handoff. A parent or another adult signs at pickup."),
 ("Can you ship a car that does not run from Chandler?","Yes. We send a truck with a winch, and the quote already includes the extra loading time. A lot on Price or at the mall gives the driver a flat place to work. Mention whether it rolls, steers, and brakes."),
 ("What do you need for a Chandler car shipping quote?","Origin and destination, plus the gate or the neighborhood on the Chandler end. The car’s year, make, and model, and whether it drives. Open or enclosed. A date window that fits the transfer or the season. That completes a Chandler request."),
]
BODY.append(faq_section(FAQ,'Chandler FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Chandler?','Two minutes on the form above prices your lane. Send the neighborhood, the gate, and your dates, and a carrier already on 10 takes it.','+19286123715','(928) 612-3715','Get your free Chandler quote'))

build({
 'slug':'auto-transport-chandler-arizona',
 'title':'Car Shipping in Chandler, AZ — Auto Transport | Ship Guy',
 'meta':'Car shipping in Chandler, AZ between Interstate 10 and the Santan Freeway. Chip plant transfers from Oregon and California, Price corridor handoffs, Ocotillo and Sun Lakes gates, downtown meeting spots, central-grid curbside, dust storm and heat planning, snowbird season lead times. Local office on West Ray Road near the 101. Free quote.',
 'h1':'Car Shipping in<br>Chandler, <span class="accent">Arizona</span>',
 'lede':'Open, enclosed, and expedited auto transport across the southeast valley, planned around 10, the loops, the gates, and the heat.',
 'tel':'+19286123715','disp':'(928) 612-3715','brand':'Chandler','keyword':'car shipping in chandler',
 'localterms':['chandler','interstate 10','loop 101','price freeway','loop 202','santan','arizona avenue','state route 87','chandler boulevard','ray road','warner','elliot','germann','queen creek','ocotillo','price road','alma school','dobson','mcqueen','cooper','gilbert road','mall','downtown','square','arts center','central grids','price corridor','west chandler','ahwatukee','fulton ranch','clemente ranch','cooper commons','sun lakes','riggs road','golf cart','reservation','casino','gilbert','mesa','chip','fabs','oregon','northern california','new mexico','engineers','program dates','launch vehicle','bank','hospitals','nurses','residents','community college','pecos road','retirees','snowbird','110 degrees','monsoon','dust','casa grande','picacho','flash floods','washes','ostrich festival','tumbleweed park','jazz festival','tree lighting','spring training','spring wind','phoenix','tucson','las vegas','san diego','los angeles','el paso','albuquerque','sacramento','austin','portland','texas','california'],
}, BODY, FAQ)
