import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Irvine, California','Car shipping in the master-planned city, where every street has a village, a gate, or a toll road nearby',
 ['Car shipping in Irvine is a question of which village, which gate, and which lot. Ship Guy is a licensed auto transport broker with an office on MacArthur Boulevard by the airport.',
  'We book vetted carriers across Irvine, Tustin, Newport Beach, Lake Forest, and Laguna Hills. We do not own the trucks.',
  'Interstate 5 and the 405 run through the city and meet at the El Toro Y. The 55 runs from the airport to Riverside. The 73, 133, 241, and 261 are the toll roads. Jamboree, Culver, and Jeffrey are the arterials that cross the villages.',
  'This page covers the freeways and the toll roads, the villages and their gates, and the new construction. It also covers the university, the headquarters, the car companies, the Santa Ana winds, and the lanes.'],
 'Irvine at a glance',
 ['Most pickups happen within 1 to 3 days. The Southern California carrier pool is the largest in the West. The 5 and the 405 carry it past Irvine.',
  'Los Angeles, San Diego, and Riverside are same-day lanes. Las Vegas and Phoenix take a day. The Bay Area takes a day too. Texas runs three days, and Florida runs five to six.'],
 'Tell us the village. Woodbridge, Turtle Rock, and the gated villages meet the truck at the entrance or a center lot. Westpark, Northwood, and the Business Complex usually allow a curb or a lot.'))

BODY.append(sec('The Roads','The 5, the 405, the 55, the Toll Roads, and the El Toro Y',
 prose(
  L('Irvine sits on the two freeways every Southern California carrier runs. It also sits on four toll roads.'),
  P('Interstate 5 runs along the east side of the city past the Spectrum and the Great Park. The 405 runs along the west side past the airport and the university. They meet at the El Toro Y in the south, one of the busiest interchanges in the state. Rush hour on both runs from six to ten and from three to seven.'),
  P('The 55 runs north from the airport through Tustin to Riverside and the Inland Empire. The 73 is the toll road to the coast and San Diego County. The 133, 241, and 261 are the toll roads through the hills to the 91 and Riverside. The carriers pay them by transponder, and the toll is built into a quote that uses them.'),
  P('Jamboree Road, Culver Drive, Jeffrey Road, and Irvine Center Drive cross the villages between the freeways. The carriers leave the 5 at Jeffrey, Sand Canyon, and Alton. They leave the 405 at Culver, Jeffrey, and MacArthur. The lots at the Spectrum, the Market Place, and the village centers are the usual meeting spots.'),
  P('Our office sits on MacArthur Boulevard in the Business Complex, across from the airport.'),
 ), alt=True))

BODY.append(sec('The Villages','Woodbridge, Turtle Rock, the Gated Villages, the Great Park, and the Grids',
 prose(
  L('Irvine was planned one village at a time, and every village has its own rules about trucks.'),
  P('Every village in Irvine has an association, and most of them limit street parking and commercial trucks. A seventy-five-foot trailer cannot wait on a village street. The handoff happens at the village center, the park lot, or a shopping center on an arterial.'),
  P('Woodbridge has loops around two lakes and narrow spine streets. The driver meets you at the village center on Barranca. Turtle Rock, Turtle Ridge, Shady Canyon, and Orchard Hills are gated or hillside. The handoff happens at the gate or at the center below the hill.'),
  P('Northwood, Westpark, University Park, and Oak Creek have wider streets and more parking. A curb handoff works on many of them if the association allows it. The Business Complex around the airport has lots everywhere, and the apartment towers there have loading zones.'),
  P('The Great Park neighborhoods on the old air base are still being built. The newest streets are not on a carrier’s map yet. For Beacon Park, Cadence Park, and Solis Park, send the full address and the nearest arterial. Portola Springs and Eastwood are the same.'),
 )))

ROUTES=[("Los Angeles, CA","I-405/I-5 · ~40 mi","Same day","$110–$190"),("San Diego, CA","I-5 · ~85 mi","Same day","$140–$230"),
 ("Riverside, CA","CA-55/CA-91 · ~40 mi","Same day","$110–$190"),("Las Vegas, NV","I-15 · ~270 mi","1 day","$270–$400"),
 ("Phoenix, AZ","I-10 · ~370 mi","1 day","$330–$480"),("San Jose, CA","I-5/US-101 · ~400 mi","1 day","$350–$500"),
 ("Sacramento, CA","I-5 · ~420 mi","1 day","$360–$520"),("Denver, CO","I-15/I-70 · ~1,020 mi","2–3 days","$720–$1,000"),
 ("Dallas, TX","I-10/I-20 · ~1,400 mi","3 days","$920–$1,280"),("Orlando, FL","I-10/I-75 · ~2,500 mi","5–6 days","$1,350–$1,850")]
BODY.append(rate_table('Lanes &amp; Costs','Irvine Car Shipping Lanes and Estimated Costs',
 'Where Irvine cars go most often, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a sedan that runs on an open trailer. An SUV or pickup adds roughly 10 to 25 percent, and enclosed adds more. The toll roads, the season, and the carriers free on your dates set the final price.',
 prose(
  P('Irvine prices like Los Angeles and San Diego, because the same carrier pool serves all three. Las Vegas and Phoenix ride the 91 or the 15 out of the basin. The Bay Area rides the 5 north.'),
  P('The Texas lane runs full every month with corporate relocations, and the East Coast lanes run all year. The <a href="car-shipping-cost.html">cost guide</a> explains the rest of the price.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The University, the Business Complex, the Car Companies, and the Hospitals',
 prose(
  L('Irvine relocates people on the quarter system, the fiscal year, the product launch, and the residency match.'),
  P('The university on the west side brings cars in each September and sends them home each June. The campus loops are tight. The driver meets you at a lot on Campus Drive or at the University Center. An adult signs for a student car.'),
  P('The Business Complex around the airport holds more headquarters than most cities. The game studio, the heart-valve company, the fast-food chains, and the biotech firms all relocate staff. They arrive from every state on start dates. Employers that reimburse the shipment get whatever paperwork they require from us.'),
  P('Three car companies keep their American headquarters in Irvine. An electric-truck maker is based here too. They relocate engineers and executives on program schedules and ship fleet and press cars in every direction. We move those on enclosed trailers more often than not.'),
  P('The new hospital on the campus and the two others bring in residents and nurses every summer. The handoff happens on a lot along Culver or Sand Canyon rather than in a hospital garage.'),
  P('The Marine air station here closed years ago. Camp Pendleton sits forty-five minutes south on the 5. Some of its families live in Irvine for the schools. A PCS move is covered on the <a href="military-car-shipping.html">military</a> page, and the interstate side on the <a href="state-to-state-car-shipping.html">state-to-state</a> page.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Santa Ana Winds, Fire Season, June Gloom, and the Y',
 prose(
  L('Irvine has no snow and no fog worth the name. It has wind, fire, and the El Toro Y.'),
  P('The Santa Ana winds blow from September into December, and fire season comes with them. The hills above Orchard Hills, Portola Springs, and Northwood have burned in recent years. The toll roads close when they do. Smoke and evacuation orders move a pickup to a lot on the flats. We call the moment that happens.'),
  P('June gloom keeps the mornings gray along the coast and burns off by noon, and it changes nothing. Winter rain is rare but heavy when it comes, and the canyon roads flood for a day. Summer heat is mild by the coast and real in the Great Park. The loading hour moves earlier inland.'),
  P('Traffic is the weather that never changes. The Y and the 405 jam every weekday from six to ten and from three to seven. A pickup near the freeways happens mid-morning or early afternoon for that reason. Game nights at the arena in Anaheim and the fair in Costa Mesa each July add to it.'),
 )+chips(["Woodbridge","Northwood","Turtle Rock","Turtle Ridge","Shady Canyon","University Park","University Town Center","Westpark","Oak Creek","Quail Hill","Stonegate","Cypress Village","Portola Springs","Orchard Hills","Eastwood","Great Park","Beacon Park","Cadence Park","Solis Park","Irvine Spectrum","Business Complex","Tustin","Newport Beach","Lake Forest","Laguna Hills","Costa Mesa"])
 +NOTE('Serving every village in Irvine and the cities around it. Tell us the village, the gate, and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Irvine?',
 prose(
  L('Irvine ships enclosed more often than most cities, and the villages explain why.'),
  P('An enclosed trailer keeps the sun, the road grit, and attention off the car. The garages in Shady Canyon, Turtle Ridge, and Orchard Hills book enclosed trailers. So do the fleet and press cars that leave the car companies.'),
  P('A commuter car still rides open to Los Angeles or San Diego without a second thought. Our <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages cover the trade-off in detail.'),
  P('Electric cars make up a big share of what leaves Irvine. Charge it to about half, switch off the cabin camera, and hand the driver a key card.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff at a village center or a lot by the freeway, and a delivery. The association decides where, and the Y decides when.'),
  P('Accept the price, and a carrier already working the 5 or the 405 takes the booking. We settle the lot with the village rules in mind. The driver goes over the car with you and writes it up on a Bill of Lading. Both sign, and delivery is checked against it.'),
 )+ULI([
  "Take personal items out of the car",
  "Leave the fuel at a quarter tank or so",
  "Photograph every panel before pickup, especially a dark car in the sun",
  "Hand the driver a working key or key card and mention any issue",
  "Switch off any aftermarket alarm",
  "Ask the association where a transport truck can stop, and tell us",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages carry the rest of the detail.'))))

BODY.append(sec('Why Ship Guy','Why Irvine Drivers Choose Ship Guy',
 prose(
  L('We work the 5 and the 405 every day. We plan around the gates, the Y, and the wind.'),
  P('Ship Guy is an FMCSA-licensed broker, and a $75,000 surety bond stands behind every booking. The record is public. Our office is on MacArthur Boulevard by the airport.'),
  P('One coordinator runs the booking from the quote to the delivery signature. Open, enclosed, and expedited transport are all on offer, and the <a href="services.html">services</a> page describes each.'),
 ), alt=True))

BODY.append(office('Irvine','18952 MacArthur Blvd #457a','Irvine, CA 92612','+19496385862','(949) 638-5862','PT',
 '18952+MacArthur+Blvd+%23457a,+Irvine,+CA+92612','Visit Us','Find Ship Guy in Irvine',
 'Our office is on MacArthur Boulevard in the Irvine Business Complex, across from John Wayne Airport.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4098.6012722071755!2d-117.86274159999998!3d33.6730721!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80dcdf2da250b6e5%3A0x30df7de80a63948d!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792077127993!5m2!1sen!2sus'))

FAQ=[
 ("Can the carrier come into my village in Irvine?","Usually not onto the street. Most village associations limit commercial trucks and street parking. A seventy-five-foot trailer cannot wait on a spine street. The driver meets you at the village center, the park lot, or a shopping center on an arterial. Gated villages meet at the gate."),
 ("How much does it cost to ship a car from Irvine to Texas or the Bay Area?","Dallas runs nine hundred twenty to twelve hundred eighty dollars for a sedan. That is about fourteen hundred miles on Interstate 10 and 20. San Jose runs three hundred fifty to five hundred, about four hundred miles up the 5. SUVs and pickups add 10 to 25 percent."),
 ("Do the toll roads change the price?","Only if the carrier uses one. The 73, 133, 241, and 261 are paid by transponder. The toll is built into the quote when a route needs one. Most Irvine pickups use the 5 and the 405 and pay no toll."),
 ("Can you ship a car for a UC Irvine student?","Yes. The cars come in each September and leave each June, on the quarter calendar. The campus loops are tight. The driver meets you at a lot on Campus Drive or at the University Center. An adult signs for the car at pickup."),
 ("Do you handle relocations to the Business Complex headquarters?","Yes, on start dates all year. The headquarters around the airport relocate staff from every state. Most ship a car rather than drive it across the country. The apartment towers in the Business Complex have loading zones that work for the handoff. The paperwork for a reimbursed move is ours to supply."),
 ("Do you ship cars for the car companies headquartered in Irvine?","Yes. Fleet cars, press cars, and show cars leave Irvine for every state, and most ride enclosed. We handle the engineers and executives those companies relocate on program schedules too. Tell us if a car is a pre-production model, because it changes the paperwork."),
 ("What happens if the Santa Ana winds bring a fire on my pickup day?","The pickup moves to a lot on the flats, away from the hills. Evacuation orders and smoke close the toll roads and the canyon villages for a day or two. We call the moment the plan changes, and a car already on the truck keeps moving."),
 ("Can you pick up in the Great Park neighborhoods?","Yes, with the full address. Beacon Park, Cadence Park, Solis Park, and the newest streets are not always on a carrier’s map yet. Send the address and the nearest arterial. The driver meets you there or at the community park lot."),
 ("Can you ship a car that does not run from Irvine?","Yes. A carrier with a winch takes it, and the longer loading is figured into the quote. The spot has to be flat, which usually means a shopping center lot rather than a village street. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for an Irvine car shipping quote?","Both addresses, with the village and the gate on this end. The year, make, and model, and whether it is electric. Whether it runs. Open or enclosed. Your dates. That is everything an Irvine quote needs."),
]
BODY.append(faq_section(FAQ,'Irvine FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Irvine?','Run the form above and you have a price in about two minutes. Tell us the village and your dates, and a carrier already working the 5 takes it from there.','+19496385862','(949) 638-5862','Get your free Irvine quote'))

build({
 'slug':'auto-transport-irvine-california',
 'title':'Car Shipping in Irvine, CA — Auto Transport | Ship Guy',
 'meta':'Car shipping in Irvine, CA on the 5 and the 405 at the El Toro Y. Village and gate handoffs from Woodbridge to Shady Canyon, Great Park addresses, UC Irvine quarters, Business Complex and car-company relocations, toll roads explained, Santa Ana wind and fire planning. Local office on MacArthur Boulevard. Free quote.',
 'h1':'Car Shipping in<br>Irvine, <span class="accent">California</span>',
 'lede':'Open, enclosed, and expedited auto transport across Irvine and Orange County, planned around the villages, the gates, and the Y.',
 'tel':'+19496385862','disp':'(949) 638-5862','brand':'Irvine','keyword':'car shipping in irvine',
 'localterms':['irvine','interstate 5','405','55','73','133','241','261','toll road','el toro y','jamboree','culver','jeffrey','sand canyon','alton','macarthur','irvine center drive','barranca','campus drive','spectrum','market place','business complex','airport','woodbridge','northwood','turtle rock','turtle ridge','shady canyon','orchard hills','university park','university center','westpark','oak creek','quail hill','stonegate','cypress village','portola springs','eastwood','great park','beacon park','cadence park','solis park','tustin','newport beach','lake forest','laguna hills','costa mesa','village','association','gate','university','headquarters','game studio','heart-valve','fast-food','biotech','car companies','electric','fleet','press cars','hospital','residents','pendleton','marine','santa ana winds','fire','smoke','evacuation','june gloom','traffic','los angeles','san diego','riverside','las vegas','phoenix','san jose','sacramento','denver','dallas','orlando','texas','florida'],
}, BODY, FAQ)
