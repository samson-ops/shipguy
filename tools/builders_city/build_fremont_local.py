import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Fremont, California','Car shipping at the south end of the East Bay, between the car factory and the bridge to Silicon Valley',
 ['Car shipping in Fremont starts with a question no other city asks: was the car built here? Ship Guy is a licensed auto transport broker with an office on Research Avenue in Warm Springs.',
  'We book vetted carriers from Niles and Mission San Jose to Newark and Union City. We do not own the trucks.',
  'Interstate 880 runs along the bay side of the city and Interstate 680 runs along the hills. Highway 84 crosses the Dumbarton Bridge to the Peninsula and climbs Niles Canyon to the east. Mission Boulevard ties the old towns together between the two freeways.',
  'This page covers the two freeways and the bridge, the five old towns, the hills, and the flats. It also covers the factory, the tech campuses, the college, the hospitals, the Austin lane, and the winter.'],
 'Fremont at a glance',
 ['Most pickups happen within 1 to 3 days. The 880 carries the Bay Area carrier pool past the city all day.',
  'San Jose, Oakland, San Francisco, and Sacramento are same-day lanes. Stockton is the same day too. Los Angeles and Fresno take a day. Portland, Las Vegas, and Phoenix take one to two.'],
 'Tell us the district. Niles, Mission San Jose, and the hills need a meeting spot. Ardenwood, Warm Springs, and the flats usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 880, 680, Highway 84, the Dumbarton, and Mission Boulevard',
 prose(
  L('Fremont sits between the bay and the hills, with a freeway along each. A bridge crosses the water.'),
  P('Interstate 880 runs along the bay side from Oakland to San Jose. It is the truck road of the East Bay. Interstate 680 runs along the hills from Milpitas over the Sunol Grade to Pleasanton and Walnut Creek. The 680 leads to Sacramento and the Altamont. The 880 leads to everything else.'),
  P('Highway 84 crosses the Dumbarton Bridge to Menlo Park and the Peninsula. The toll is collected westbound, and a carrier builds it into a Peninsula quote. East of the city, 84 runs through Niles Canyon to Sunol. The canyon is too tight for a loaded trailer.'),
  P('Mission Boulevard runs the length of the city along the hills, and Fremont Boulevard runs the flats. The carriers come off 880 at Decoto, Mowry, Stevenson, Auto Mall Parkway, and Fremont Boulevard. The lots at the Hub, Pacific Commons, and the auto mall are the usual meeting spots. The bridge aside, no road in the city charges a toll.'),
  P('Our office sits on Research Avenue in Warm Springs, minutes from the factory and the 880.'),
 ), alt=True))

BODY.append(sec('The Five Towns','Niles, Centerville, Irvington, Mission San Jose, Warm Springs, and the Flats',
 prose(
  L('Fremont was five towns before it was a city, and each one parks the way it always did.'),
  P('Niles is the oldest, with a railroad, a narrow main street, and canyon roads behind it. The driver meets you on Niles Boulevard or at the lot by the depot. Centerville and Irvington have tight blocks around their old centers and open grids beyond them.'),
  P('Mission San Jose climbs into the hills. Mission Hills, Weibel, and the streets above Mission Boulevard wind, narrow, and drop off at the edges. A seventy-five-foot trailer stays on Mission Boulevard or at the lot by the old mission.'),
  P('Warm Springs holds the factory, the new transit village, and the tech campuses along the 880. The flats between the freeway and the bay are wide grids. Ardenwood, Northgate, Glenmoor, and Sundale usually allow the truck at the curb. The newest blocks around the station are still filling in, so send the full address.'),
  P('Newark and Union City sit on the same 880 lane and ship through the same carrier pool. The Peninsula sits across the bridge. A Palo Alto or Menlo Park delivery prices as a Fremont one plus the toll.'),
 )))

ROUTES=[("San Jose, CA","I-880 · ~20 mi","Same day","$100–$170"),("Oakland, CA","I-880 · ~30 mi","Same day","$110–$190"),
 ("San Francisco, CA","I-880/I-80 · ~40 mi","Same day","$120–$200"),("Sacramento, CA","I-680/I-80 · ~100 mi","Same day","$160–$260"),
 ("Stockton, CA","I-680/I-205 · ~65 mi","Same day","$140–$230"),("Fresno, CA","CA-152/CA-99 · ~150 mi","1 day","$190–$300"),
 ("Los Angeles, CA","I-5 · ~350 mi","1 day","$320–$460"),("Las Vegas, NV","I-5/CA-58/I-15 · ~540 mi","1–2 days","$440–$630"),
 ("Portland, OR","I-5 · ~630 mi","1–2 days","$510–$720"),("Austin, TX","I-10 · ~1,750 mi","3–4 days","$1,100–$1,500")]
BODY.append(rate_table('Lanes &amp; Costs','Fremont Car Shipping Lanes and Estimated Costs',
 'Fremont’s busiest lanes, across the bay and across the country, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a running sedan on an open trailer. An SUV or pickup runs about 10 to 25 percent more, and enclosed more again. The bridge toll, the season, and the carriers free on your dates settle the final number.',
 prose(
  P('Fremont prices like San Jose and Oakland, because it sits on the 880 between them. Sacramento rides the 680 and the 80, and Los Angeles rides the 5.'),
  P('The Austin lane runs full every month with tech relocations in both directions. Seattle and Denver are close behind. The <a href="car-shipping-cost.html">cost guide</a> shows where the number comes from.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Factory, the Tech Campuses, the College, and the Hospitals',
 prose(
  L('Fremont relocates people on the hiring class, the product launch, the visa, the semester, and the residency match.'),
  P('The car factory on Fremont Boulevard is the largest employer in the city. It relocates engineers and technicians on program schedules. Cars built there leave on carriers every day. An owner from out of state can ship a new one home the same way. We move a lot of them.'),
  P('The chip-equipment maker in Warm Springs and the campuses along the 880 hire from every state and abroad. New arrivals on a visa often buy a car in the first month. They ship it later when the job moves. When an employer picks up the cost, we provide the paperwork it wants.'),
  P('The community college in Mission San Jose fills with cars each August and empties each May. The campus sits on a hill. The driver meets you at the lot below it on Mission Boulevard. An adult signs for a student car.'),
  P('The hospital on Mowry and the one on Paseo Padre bring in nurses and residents every summer. Most arrive from out of state with a car. The handoff happens on Mowry Avenue or at the Hub rather than in a hospital garage.'),
  P('Travis Air Force Base sits an hour north, and the Coast Guard station sits in Alameda. See the <a href="military-car-shipping.html">military</a> page for a PCS move. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side of any relocation.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Hiring Season, the Bridge, the Wind, and the Rain',
 prose(
  L('Fremont has mild weather and a hard commute, and the commute decides more than the sky does.'),
  P('The 880 jams from six to ten and from three to seven. The Dumbarton backs up westbound every morning. A pickup near the freeway happens mid-morning or early afternoon for that reason. The Sunol Grade on the 680 adds time to anything headed over the hill.'),
  P('Winter rain comes in atmospheric rivers from December into March. The creeks off the hills flood the low streets for a day. Alameda Creek in Niles Canyon closes 84 now and then. The carriers wait for a washed-out road to reopen instead of cutting through the hills.'),
  P('Summer stays cool by the bay and runs hot in the hills. The afternoon wind off the bay pushes a trailer around on the bridge. Wildfire smoke settles on the East Bay in late summer and slows everything. Fog is rare this far south.'),
  P('Hiring season at the factory and the campuses runs all year. It bumps each summer when the new graduates arrive. The Austin lane fills in both directions when a company opens or closes an office.'),
 )+chips(["Niles","Centerville","Irvington","Mission San Jose","Warm Springs","Ardenwood","Northgate","Glenmoor","Sundale","Cherry-Guardino","Kimber-Gomes","Weibel","Mission Hills","Brookvale","Cabrillo","Parkmont","Fremont Boulevard","Mission Boulevard","Mowry Avenue","Auto Mall Parkway","Pacific Commons","The Hub","Newark","Union City","Milpitas","Sunol"])
 +NOTE('Serving Fremont, Newark, and Union City. Tell us the district, the week, and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Fremont?',
 prose(
  L('Open trailers carry most of what leaves Fremont, including most of the new cars from the factory.'),
  P('An enclosed trailer keeps the salt air, the road grit, and attention off the car. The garages in Mission San Jose and the hills book enclosed trailers. So does a car with a paint-protection film headed across the country.'),
  P('A commuter car rides open over the bridge or down the 880 without trouble. Our <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages weigh the roof against the price.'),
  P('Electric cars are a large share of what leaves Fremont, and many of them were built here. Charge to about half and use transport mode if the car has one. Leave a key card with the driver.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff at a lot by the 880 or on Mission Boulevard, and a delivery. The commute decides the hour.'),
  P('Accept the price, and a carrier already running the 880 takes the booking. We set the spot the same day. You and the driver check the car together and record it on a Bill of Lading. You both sign, and the delivery inspection runs against it.'),
 )+ULI([
  "Clear your personal things out of the car",
  "Keep about a quarter tank in it",
  "Photograph the car before pickup, including the film and the wheels",
  "Leave a working key or key card with the driver and mention any issue",
  "Turn off any aftermarket alarm and sentry recording",
  "In the hills, plan to meet the truck on Mission Boulevard",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages cover the rest in order.'))))

BODY.append(sec('Why Ship Guy','Why Fremont Drivers Choose Ship Guy',
 prose(
  L('We work the 880 and the bridge every day. We plan around the commute, the rain, and the hiring calendar.'),
  P('The FMCSA shows Ship Guy as an active broker with a $75,000 surety bond on file. The record is public. Our office is on Research Avenue in Warm Springs.'),
  P('One coordinator carries the booking from the first quote to the last signature. Open, enclosed, and expedited transport are all available. The <a href="services.html">services</a> page explains each.'),
 ), alt=True))

BODY.append(office('Fremont','45401 Research Ave #425A','Fremont, CA 94539','+12294902759','(229) 490-2759','PT',
 '45401+Research+Ave+%23425A,+Fremont,+CA+94539','Visit Us','Find Ship Guy in Fremont',
 'Our office is on Research Avenue in Warm Springs, minutes from the factory, the station, and the 880.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3907.142993372974!2d-121.93184559999997!3d37.5013043!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x808fc774b57b85b9%3A0x41a21a79bb21658e!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792077062449!5m2!1sen!2sus'))

FAQ=[
 ("Can you ship a new car from the Fremont factory to another state?","Yes, every week. An owner from out of state can take delivery here and ship the car home. Driving it is optional. Charge it to about half and set transport mode before the truck arrives. Tell us the exact model, because the weight changes how the carrier builds the load."),
 ("How much does it cost to ship a car from Fremont to Austin or Los Angeles?","Austin runs eleven hundred to fifteen hundred dollars for a sedan. That is about seventeen hundred fifty miles on Interstate 10. Los Angeles runs three hundred twenty to four hundred sixty, about three hundred fifty miles down the 5. SUVs and pickups add 10 to 25 percent."),
 ("Can the carrier come up into Mission San Jose or the hills?","Usually not. The streets above Mission Boulevard wind, narrow, and drop off at the edges. The driver meets you on Mission Boulevard or at the lot by the old mission. Ardenwood, Warm Springs, and the flats usually allow the curb."),
 ("Does the Dumbarton toll change the price of a Peninsula delivery?","A little. The toll is collected westbound only, and the carrier pays it by transponder. It goes into the quote for a Palo Alto or Menlo Park delivery. A pickup on the Fremont side pays no toll at all."),
 ("Do you ship cars for people hired at the factory or the tech campuses?","Yes, on start dates all year. New hires arrive from every state and every continent, and most ship a car rather than drive it. Many buy a car in the first month and ship it later when the job moves. We provide the paperwork for a reimbursed move."),
 ("Can you ship a car for an Ohlone College student?","Yes. The cars come in each August and leave each May. The campus sits on a hill in Mission San Jose. The driver meets you at the lot below it. An adult signs for the car at pickup."),
 ("What happens if an atmospheric river floods the roads on my pickup day?","The pickup waits for the water to drain. The creeks off the hills flood the low streets for a day. Niles Canyon closes now and then. The handoff moves to a lot by the 880 until the roads reopen. We call the moment the plan changes."),
 ("Is Fremont priced like San Jose or like Oakland?","Both, because it sits on the 880 between them and shares the two carrier pools. San Jose runs one hundred to one hundred seventy dollars for a sedan. Oakland runs one hundred ten to one hundred ninety. A carrier headed either way can take the car."),
 ("Can you ship a car that does not run from Fremont?","Yes. We assign a carrier with a winch, and the slower loading is priced in. The spot has to be flat and open, which usually means a lot by the 880. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Fremont car shipping quote?","Pickup and delivery addresses, with the district on this end. Year, make, model, and whether it is electric. Does it run. Open or enclosed. The dates you have in mind. That is all a Fremont quote takes."),
]
BODY.append(faq_section(FAQ,'Fremont FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Fremont?','Price the lane on the form above in about two minutes. Tell us the district and your dates, and a carrier already on the 880 takes it from there.','+12294902759','(229) 490-2759','Get your free Fremont quote'))

build({
 'slug':'auto-transport-fremont-california',
 'title':'Car Shipping in Fremont, CA — Auto Transport | Ship Guy',
 'meta':'Car shipping in Fremont, CA on the 880 and the 680 at the south end of the East Bay. Factory-new cars shipped home, Niles and Mission San Jose meeting spots, Warm Springs and the flats curbside, tech and visa relocations, the Dumbarton toll explained, the Austin lane, atmospheric-river planning. Local office on Research Avenue. Free quote.',
 'h1':'Car Shipping in<br>Fremont, <span class="accent">California</span>',
 'lede':'Open, enclosed, and expedited auto transport across the south East Bay, planned around the 880, the bridge, and the commute.',
 'tel':'+12294902759','disp':'(229) 490-2759','brand':'Fremont','keyword':'car shipping in fremont',
 'localterms':['fremont','interstate 880','interstate 680','highway 84','dumbarton','niles canyon','sunol','mission boulevard','fremont boulevard','mowry','decoto','stevenson','auto mall parkway','paseo padre','research avenue','niles','centerville','irvington','mission san jose','warm springs','ardenwood','northgate','glenmoor','sundale','weibel','mission hills','the hub','pacific commons','newark','union city','milpitas','peninsula','palo alto','menlo park','factory','electric','transport mode','key card','chip-equipment','campuses','visa','college','ohlone','hospital','residents','travis','coast guard','commute','atmospheric river','creeks','wind','smoke','hiring','san jose','oakland','san francisco','sacramento','stockton','fresno','los angeles','las vegas','portland','austin','seattle','denver'],
}, BODY, FAQ)
