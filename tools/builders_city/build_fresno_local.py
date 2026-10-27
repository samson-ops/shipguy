import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Fresno, California','Car shipping in the middle of the San Joaquin Valley, on Highway 99 between Los Angeles and Sacramento',
 ['Car shipping in Fresno runs on Highway 99, the road every carrier crossing the valley uses. Ship Guy is a licensed auto transport broker with an office on North Howard Street in north Fresno.',
  'We book vetted carriers across Fresno County, from Clovis and Sanger to Reedley, Kerman, and Madera. We do not own the trucks.',
  'Highway 99 runs through the west side of the city between Bakersfield and Sacramento. Highway 41 crosses it on the way from the coast to Yosemite. Highway 180 runs east to the Sierra, and Highway 168 carries Clovis and the foothills.',
  'This page covers the highways, the older neighborhoods and the newer ones, and Clovis. It also covers the university, the hospitals, the farms, Lemoore, the fog, the heat, and the lanes.'],
 'Fresno at a glance',
 ['Most pickups happen within 1 to 3 days. Highway 99 brings carriers through the city from both directions all day.',
  'Bakersfield, Sacramento, San Jose, and Los Angeles are same-day lanes. Oakland and San Diego take a day. Las Vegas takes a day, and Phoenix takes one to two.'],
 'Tell us the neighborhood. The Tower District, Old Fig Garden, and the blocks near downtown need a meeting spot. Clovis and north Fresno usually allow the curb.'))

BODY.append(sec('The Roads','Highway 99, 41, 180, 168, and the Grapevine',
 prose(
  L('Fresno is the biggest city in the country not on an interstate, and it does not matter.'),
  P('Highway 99 is the valley’s main street and the busiest truck road in it. It runs through the west side of Fresno between Bakersfield and Sacramento. Interstate 5 runs forty miles west across the empty side of the valley. Highway 180 and Highway 41 connect the two.'),
  P('Highway 41 runs north through the city to Madera and Yosemite and south to Lemoore and the coast. Highway 180 runs east to Kings Canyon and west to Mendota. Highway 168 runs northeast through Clovis to Shaver Lake.'),
  P('The Los Angeles lane crosses the Grapevine on Interstate 5 south of Bakersfield. The pass closes for snow a few times each winter, and the carriers wait at the bottom. The Bay Area lane runs Highway 152 over Pacheco Pass or Highway 99 to the Altamont.'),
  P('The carriers come off 99 at Herndon, Shaw, and Ventura. The lots along Blackstone and at the mall by Shaw are the usual meeting spots. No road in the valley charges a toll.'),
  P('Our office sits on North Howard Street in north Fresno by River Park, minutes from Highway 41.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','The Tower, Fig Garden, Woodward Park, Clovis, and the Grids',
 prose(
  L('Fresno grew north from the rail yard, and the streets get wider the farther north you go.'),
  P('Downtown and the Tower District are the oldest parts of the city, with narrow streets and alleys. Old Fig Garden has winding lanes under big trees and no sidewalks. The driver meets you on Blackstone, Palm, or Shaw rather than on those streets.'),
  P('North of Shaw, the city turns into wide grids. Woodward Park, Bullard, and the subdivisions along Herndon usually allow the truck at the curb. Clovis is a wide grid of its own, and Old Town Clovis is the exception.'),
  P('Sunnyside and the southeast side mix orchards and subdivisions. Some roads out there are not on a carrier’s map yet. Send the full address and the nearest cross street. Sanger, Reedley, Kerman, and the farm towns meet the truck on the state highway.'),
  P('Gated communities along Friant Road meet the driver at the gate or at the clubhouse lot. Tell us the gate arrangement when you book.'),
 )))

ROUTES=[("Bakersfield, CA","CA-99 · ~110 mi","Same day","$160–$260"),("Sacramento, CA","CA-99 · ~170 mi","Same day","$190–$300"),
 ("San Jose, CA","CA-152/US-101 · ~150 mi","Same day","$190–$300"),("Los Angeles, CA","CA-99/I-5 · ~220 mi","Same day","$230–$350"),
 ("Oakland, CA","CA-99/I-580 · ~190 mi","Same day","$210–$330"),("San Diego, CA","I-5 · ~340 mi","1 day","$310–$450"),
 ("Las Vegas, NV","CA-58/I-15 · ~400 mi","1 day","$360–$520"),("Phoenix, AZ","I-5/I-10 · ~590 mi","1–2 days","$470–$680"),
 ("Portland, OR","I-5 · ~650 mi","2 days","$520–$740"),("Dallas, TX","I-10/I-20 · ~1,500 mi","3–4 days","$980–$1,350")]
BODY.append(rate_table('Lanes &amp; Costs','Fresno Car Shipping Lanes and Estimated Costs',
 'The routes out of Fresno we price most often, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a sedan that runs, on an open trailer. An SUV or pickup adds about 10 to 25 percent, and enclosed adds more. Fog season, the Grapevine, and the carriers free on your dates fix the final figure.',
 prose(
  P('Fresno prices well for a city its size, because the valley lane runs full in both directions. Los Angeles and the Bay Area ride 99 and the passes, and Sacramento rides 99 north.'),
  P('The Arizona lane fills each fall when the retirees in the north side subdivisions head south. The <a href="car-shipping-cost.html">cost guide</a> explains how the number comes together.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The University, the Hospitals, the Farms, and Lemoore',
 prose(
  L('Fresno relocates people on the semester, the residency match, the harvest, and the Navy’s calendar.'),
  P('The state university on the north side brings cars in each August and sends them home each May. The campus blocks off Shaw and Cedar are tight on move-in weekend. The driver meets you at a lot on Shaw, and an adult signs for a student car.'),
  P('The regional medical center downtown and the two hospitals on the north side bring in residents every July. Most arrive from out of state with a car. The handoff happens on Fresno Street or Herndon Avenue rather than in a hospital garage.'),
  P('The farms and the packing houses run one of the richest farm counties in the country. They relocate managers and agronomists on the crop calendar. The distribution centers along 99 and the airport hire on start dates all year. If your employer reimburses the shipment, we send the documentation it asks for.'),
  P('The naval air station at Lemoore sits forty minutes southwest on Highway 41. Many of its families live in Fresno and Clovis. The orders pay for one car. The second one rides with us. The truck stops at the gate, and the handoff happens in Lemoore or Hanford. The <a href="military-car-shipping.html">military</a> page covers the planning.'),
  P('For the interstate side of a move, see the <a href="state-to-state-car-shipping.html">state-to-state</a> page.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Tule Fog, the Heat, the Smoke, and the Fair',
 prose(
  L('Fresno has no snow and no hurricanes. It has fog that stops traffic and heat that bakes a parked car.'),
  P('Tule fog settles on the valley from November into February. On the worst mornings it drops visibility on 99 to a few car lengths. The pileups close the highway. The carriers wait for it to lift, which usually means a late-morning handoff in winter.'),
  P('Summer runs past one hundred degrees for weeks at a time. The loading hour moves to early morning. A car waiting in a lot gets hot enough to matter. Wildfire smoke from the Sierra settles on the valley in late summer and slows everything.'),
  P('The Grapevine closes for snow a few times each winter. The Los Angeles lane waits a day when it does. The big fair fills the fairgrounds and Kings Canyon Road for two weeks each October. Winter rain is light, but an atmospheric river can flood the low roads for a day.'),
 )+chips(["Downtown","Tower District","Old Fig Garden","Fig Garden","Fresno High","Bullard","Woodward Park","Sunnyside","Hoover","Blackstone","Shaw Avenue","Herndon","Friant Road","River Park","Clovis","Old Town Clovis","Sanger","Reedley","Selma","Kerman","Fowler","Madera","Hanford","Lemoore","Visalia"])
 +NOTE('Serving Fresno, Clovis, and the whole county. Tell us the neighborhood, the month, and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Fresno?',
 prose(
  L('Open is how the valley ships, and the 99 lane is priced for it.'),
  P('An enclosed trailer keeps the dust, the sun, and the orchard spray off the car. The garages in Old Fig Garden and along Friant Road book enclosed trailers. So does a collector car headed to the auctions in Scottsdale each January.'),
  P('A daily driver rides open and arrives dusty but fine. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages lay out the difference.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a loading on Shaw or by 99, and a delivery. In winter the fog sets the hour.'),
  P('Accept the price and a carrier already running 99 takes the booking. We set the spot together. The driver and you inspect the car and note everything on a Bill of Lading. Both sign it, and delivery is measured against that sheet.'),
 )+ULI([
  "Remove anything personal from the car",
  "Leave a quarter tank of fuel or so",
  "Photograph the car before pickup, especially after a dust storm or the fog",
  "Give the driver a working key and note any mechanical issue",
  "Turn off any aftermarket alarm",
  "In summer, plan an early-morning handoff",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages cover each step.'))))

BODY.append(sec('Why Ship Guy','Why Fresno Drivers Choose Ship Guy',
 prose(
  L('We work 99 every day and plan around the fog, the heat, and the Grapevine.'),
  P('Ship Guy’s FMCSA brokerage authority is current, and a $75,000 surety bond is posted behind it. Both are a matter of public record. Our office is on North Howard Street in north Fresno.'),
  P('One coordinator owns the booking from the quote to the delivery signature. Open, enclosed, and expedited transport are all on offer. The <a href="services.html">services</a> page describes them.'),
 ), alt=True))

BODY.append(office('Fresno','7161 N Howard St Ste 731','Fresno, CA 93720','+15595534693','(559) 553-4693','PT',
 '7161+N+Howard+St+Ste+731,+Fresno,+CA+93720','Visit Us','Find Ship Guy in Fresno',
 'Our office is on North Howard Street in north Fresno by River Park, just off Highway 41.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3941.4284103675664!2d-119.78410590000001!3d36.8411366!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x809443693bc1b25d%3A0x18eadeaafefe53d7!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792077139794!5m2!1sen!2sus'))

FAQ=[
 ("Why is Fresno so easy to ship from without an interstate?","Because Highway 99 does the job an interstate does. It is the valley’s main truck road, and every carrier between Los Angeles and Sacramento runs it. A Fresno car rides a truck already making that trip."),
 ("How much does it cost to ship a car from Fresno to Los Angeles or the Bay Area?","Los Angeles runs two hundred thirty to three hundred fifty dollars for a sedan. That is about two hundred twenty miles down 99 and over the Grapevine. San Jose and Oakland run about the same over the passes. SUVs and pickups add 10 to 25 percent."),
 ("What happens when tule fog closes Highway 99?","The driver waits for it to lift. The worst fog comes in December and January, and the pileups close 99 for hours. A winter pickup usually happens late morning for that reason. We call the moment the plan changes."),
 ("Can you ship a car for a Fresno State student?","Yes. The cars come in each August and leave each May. The campus blocks are tight on move-in weekend, so the driver meets you at a lot on Shaw. An adult signs for the car at pickup. A parent can sign at the other end."),
 ("Do you handle a PCS move to NAS Lemoore from Fresno?","Yes. The air station is forty minutes southwest on Highway 41. Many of its families live in Fresno and Clovis. The orders pay for one car, and the second one rides with us. The truck stops at the gate, so the handoff happens in Lemoore or Hanford. Ship Guy is a private broker with no connection to the Navy."),
 ("Can the carrier come into the Tower District or Old Fig Garden?","Usually not. The Tower has narrow streets and alleys. Old Fig has winding lanes with no sidewalks and low trees. The driver meets you on Blackstone, Palm, or Shaw. North Fresno and Clovis usually allow the curb."),
 ("Do you ship cars for residents at the medical center?","Yes, every July. Residents arrive from every state, and most bring a car. The handoff happens on Fresno Street downtown or on Herndon Avenue, not in a hospital garage."),
 ("Does summer heat change how you ship from Fresno?","It changes the hour. The loading happens early in the morning when the valley is still cool. A car waiting in an open lot at noon gets hot enough to matter. We also check the tires and the battery before the truck arrives."),
 ("Can you ship a car that does not run from Fresno?","Yes. The carrier we send has a winch, and the slower loading is figured into the quote. The spot has to be flat, which usually means a lot by 99 or on Shaw. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Fresno car shipping quote?","Both addresses, with the neighborhood on the Fresno end. The year, make, and model. Whether it runs. Open or enclosed. Your dates, with the fog season in mind. That is a complete Fresno request."),
]
BODY.append(faq_section(FAQ,'Fresno FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Fresno?','A price takes about two minutes on the form above. Tell us the neighborhood and your dates, and a carrier already on 99 takes it from there.','+15595534693','(559) 553-4693','Get your free Fresno quote'))

build({
 'slug':'auto-transport-fresno-california',
 'title':'Car Shipping in Fresno, CA — Auto Transport | Ship Guy',
 'meta':'Car shipping in Fresno, CA on Highway 99 in the middle of the San Joaquin Valley. Tower District and Fig Garden handoffs, Clovis curbside, Fresno State move-in, hospital residents, NAS Lemoore second vehicles, tule fog and summer heat planning, the Grapevine. Local office on North Howard Street. Free quote.',
 'h1':'Car Shipping in<br>Fresno, <span class="accent">California</span>',
 'lede':'Open, enclosed, and expedited auto transport across Fresno County, planned around Highway 99, the fog, and the heat.',
 'tel':'+15595534693','disp':'(559) 553-4693','brand':'Fresno','keyword':'car shipping in fresno',
 'localterms':['fresno','highway 99','highway 41','highway 180','highway 168','highway 152','interstate 5','grapevine','pacheco pass','altamont','herndon','shaw','blackstone','ventura','friant road','river park','downtown','tower district','old fig garden','fig garden','fresno high','bullard','woodward park','sunnyside','hoover','clovis','old town clovis','sanger','reedley','selma','kerman','fowler','madera','hanford','lemoore','visalia','naval air station','navy','university','fresno state','medical center','hospitals','residents','farms','packing houses','harvest','distribution centers','airport','tule fog','fog','heat','smoke','fair','kings canyon','atmospheric river','bakersfield','sacramento','san jose','los angeles','oakland','san diego','las vegas','phoenix','portland','dallas','arizona','scottsdale'],
}, BODY, FAQ)
