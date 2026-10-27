import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("Weekly","Sailings"),("7 Days","Local Support")]))

BODY.append(intro_block('Hilo, Hawaii','Car shipping to the Big Island: a carrier to the coast, a sailing across the Pacific, and a harbor on the rainy side',
 ['Car shipping to Hilo is a three-leg trip, and the ocean sets the pace on two of them. Ship Guy is a licensed auto transport broker with an office on Kinoole Street downtown.',
  'We coordinate the mainland pickup, the sailing, and the island end, and we own neither trucks nor ships.',
  'Your car rides a carrier to a West Coast port, then sails to the islands. Some sailings call at Hilo Harbor directly. Others land in Honolulu and ride the inter-island barge across. We book whichever lands the car soonest.',
  'This page explains the three legs, the terminal rules, and the barge. It also covers both sides of the island, the Puna lava lanes, the rain, and the festival week.'],
 'Hilo at a glance',
 ['Count three to four weeks from a West Coast origin and four to five from the East. Add three to seven days for the barge in a week without a direct Hilo call.',
  'Southern California and the Bay Area are the shortest and least expensive origins. Seattle and Portland come next. Everything else adds a land leg first.'],
 'Tell us the district. Hilo town, Keaau, and Waimea are easy. Puna subdivisions, Kaumana, and the Ka’u coast need a meeting spot in town.'))

BODY.append(sec('The Process','The Three Legs of a Hilo Shipment',
 prose(
  L('A Hilo shipment has a highway leg, an ocean leg, and a short island leg. Sometimes a barge sits between.'),
  P('The first leg is ordinary. A carrier collects the car wherever it sits and hauls it to a West Coast port. Southern California and the Bay Area are a day or two away. Texas and the East Coast are five days or more. You sign a Bill of Lading at pickup like any domestic move.'),
  P('The car then boards a weekly sailing. Some sailings go direct to Hilo Harbor on the bay. Others arrive in Honolulu, clear that terminal, and transfer to the inter-island barge. The barge runs to Hilo on its own weekly schedule and adds three to seven days.'),
  P('The ship leaves on schedule whether the car is there or not. The highway leg aims at the cutoff with a day to spare. Miss it, and the car waits a week. We watch the sailing and the barge as one timeline, and nothing sits on a dock.'),
  P('When the car lands, the harbor clears and releases it. Pick it up at the terminal yourself, or let us set up the island delivery. Hilo town is minutes away. Kona is two hours over the saddle, and the Ka’u coast is farther still.'),
 ), alt=True))

BODY.append(sec('The Island','Hilo Town, Puna, the Hamakua Coast, Waimea, and the Kona Side',
 prose(
  L('The Big Island is bigger than the other islands combined. The last leg depends on which side you live on.'),
  P('Hilo town sits around the bay with a tight downtown grid along Kamehameha and Kinoole. The driver meets you on the bayfront or at the shopping center on Kanoelehua. Waiakea, Puainako, and the university blocks have wide enough streets for curbside. Kaumana and Waiakea Uka climb the mountain on narrow roads, and the handoff moves down the hill.'),
  P('Puna south of town is the fastest-growing district on the island, and its subdivisions sit on lava-rock lanes. Hawaiian Paradise Park, Orchidland, and Hawaiian Beaches have gravel roads a trailer cannot use. The driver meets you in Keaau or Pahoa. Keaukaha by the harbor and the airport has the shortest last leg of all.'),
  P('The Hamakua coast runs north through Honokaa to Waimea on a highway of gulches and one-lane bridges. The driver meets you on the highway in town. Waimea and the ranch country sit at the top with wide roads. The saddle road crosses to the Kona side at high elevation past the training area.'),
  P('Kailua-Kona, Waikoloa, and the resorts are two hours west. A car for the Kona side can also sail into Kawaihae Harbor on that coast. We route it that way when the schedule allows. Volcano and the Ka’u coast to the south sit at the end of long highways. The driver meets you in Volcano village or Naalehu.'),
 )))

ROUTES=[("Los Angeles / Long Beach","land + ocean","3–4 weeks","$1,750–$2,400"),("Bay Area / Oakland","land + ocean","3–4 weeks","$1,775–$2,450"),
 ("San Diego, CA","land + ocean","3–4 weeks","$1,800–$2,500"),("Seattle / Portland","land + ocean","3–4 weeks","$1,850–$2,550"),
 ("Phoenix, AZ","land + ocean","3.5–4.5 weeks","$2,050–$2,850"),("Denver, CO","land + ocean","4–4.5 weeks","$2,250–$3,100"),
 ("Dallas / Houston","land + ocean","4–4.5 weeks","$2,300–$3,150"),("Chicago, IL","land + ocean","4–5 weeks","$2,500–$3,400"),
 ("New York / New Jersey","land + ocean","4–5 weeks","$2,800–$3,900"),("Honolulu (inter-island barge)","barge only","about 1 week","$300–$450")]
BODY.append(rate_table('Lanes &amp; Costs','Car Shipping to Hilo: Estimated Times and Costs',
 'The usual mainland origins, with estimated door-to-door times and sedan rates. The form above prices your exact lane.',
 ['Origin → Hilo','Route type','Est. door to door','Est. rate*'],ROUTES,
 '*2026 estimates, running sedan, open trailer on the highway leg. The barge is included when there is no direct Hilo call. Trucks and SUVs run higher, and an oversized vehicle is priced by its dimensions on the ship. Carrier availability, the sailing calendar, and your dates set the firm number.',
 prose(
  P('The West Coast origins cluster tightly because the crossing costs what it costs. Only the highway miles and the barge move the total. A direct sailing into Hilo saves the barge fee, and we book it when the calendar lines up.'),
  P('An East Coast origin adds a long land leg and the days that come with it. The general factors are in the <a href="car-shipping-cost.html">cost guide</a>.'),
 ), alt=True))

BODY.append(sec('Terminal Rules','The Rules That Get Cars Turned Away at the Port',
 prose(
  L('Port rules are stricter than highway rules, and the gate checks every car on both ends.'),
 )+ULI([
  "Nothing of yours stays in the car, not a box, not a bag",
  "No more than a quarter tank of fuel at the terminal gate",
  "Washed and vacuumed, because the state inspects for soil, seeds, and plant matter",
  "Title or registration in hand, plus the lender’s authorization letter on a financed car",
  "The dock measures height and length, so a lift or a rack moves the price",
  "One working key rides with the car, and the aftermarket alarm is off",
 ])+prose(
  P('The cleanliness rule matters more for the Big Island than anywhere else. The island fights invasive species on every shipment, and a muddy wheel well gets a car refused. Wash the outside and vacuum the inside before pickup.'),
  P('Outbound cars get the same look on the way out. Volcanic grit and red dirt both count. We send a checklist before pickup, because a car that reaches the terminal ready never loses its sailing.'),
 )))

BODY.append(sec('Who Ships Here','The University, the Hospital, the Observatories, and the Training Area',
 prose(
  L('Hilo ships for a university, a hospital, and a mountain full of telescopes.'),
  P('The university above town brings students in each August. Many ship a car from the mainland for the year. The handoff happens at a campus lot, and an adult signs for a student car. The hospital brings in nurses and physicians on contracts all year. The observatories on the mountain relocate astronomers and engineers on program schedules.'),
  P('The Army training area on the saddle rotates units through on exercise cycles. Families stay in Hilo or Waimea. Orders cover one car, and the second one comes with us. Ship Guy is a private broker with no connection to the training area. The <a href="military-car-shipping.html">military</a> page covers the timing around a report date.'),
  P('Retirees and remote workers move to Puna and the Hamakua coast for the land prices. Most ship a car behind the move. The reverse trip is just as common. Families leaving for the mainland sail the car out of Hilo and finish on a carrier. We supply the paperwork a reimbursed move needs.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Rain, Lava, Hurricanes, and Merrie Monarch Week',
 prose(
  L('Hilo is the wettest city in the country, and the island adds volcanoes and hurricanes. The schedule bends around all three.'),
  P('Rain falls on Hilo most days of the year. A tropical downpour floods the bayfront and the river crossings for an hour. The handoff waits it out. Flash floods close the Hamakua bridges and the Puna roads a few times each winter. A pickup there moves to town.'),
  P('The volcano runs on its own schedule. The 2018 eruption buried roads and subdivisions in lower Puna, and lava closes highways without notice. Vog drifts to the Kona side and changes nothing about a shipment. A road closure reroutes the last leg, and we tell you when it does.'),
  P('Hurricane season is June through November. Iselle crossed Puna in 2014, and Lane dropped four feet of rain on Hilo in 2018. The port shuts before a storm arrives, and the ships hold offshore or in Honolulu. Sailings resume as soon as the harbor opens, and so do we.'),
  P('Merrie Monarch week fills every hotel on the island in the week after Easter. The parade closes downtown, and the stadium district fills every night. A pickup in town moves to another day. The Fourth of July and the county fair do the same on a smaller scale.'),
 )+chips(["Downtown Hilo","Bayfront","Kinoole","Waiakea","Waiakea Uka","Kaumana","Puainako","Keaukaha","Panaewa","Keaau","Pahoa","Hawaiian Paradise Park","Orchidland","Hawaiian Beaches","Volcano","Mountain View","Honokaa","Laupahoehoe","Waimea","Kawaihae","Waikoloa","Kailua-Kona","Captain Cook","Naalehu","Ocean View"])
 +NOTE('Serving Hilo and the whole Big Island, both sides of the saddle. Tell us the district, the road surface, and whether the car runs.')))

BODY.append(sec('After Arrival','Registering the Car in Hawaii',
 prose(
  L('The county has a short list for a car that just arrived.'),
  P('A mainland car needs a Hawaii safety inspection and a county registration inside a set window. The offices in Hilo and Kona handle both. Take the mainland title or registration and the shipping papers. Confirm the current rules with the county first.'),
  P('The shipment itself does not depend on any of it. Having the folder ready the day the harbor releases the car simply saves a trip.'),
 ), alt=True))

BODY.append(sec('Why Ship Guy','Why Big Island Shippers Choose Ship Guy',
 prose(
  L('We book the sailing and the barge together. We plan the last leg around the side of the island you live on.'),
  P('Ship Guy holds active FMCSA brokerage authority and a $75,000 surety bond for the highway legs. Both are in the federal register. The ocean legs ride licensed ocean carriers. Our office is on Kinoole Street downtown.'),
  P('The same coordinator follows the pickup, the cutoff, the sailing, and the barge. You hear from that person at each step. Open, enclosed, and expedited options for the highway legs are on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Hilo','688 Kinoole St #405','Hilo, HI 96720','+18088245278','(808) 824-5278','HST',
 '688+Kinoole+St+%23405,+Hilo,+HI+96720','Visit Us','Find Ship Guy in Hilo',
 'Our office is on Kinoole Street downtown, a few blocks from the bayfront and minutes from the harbor.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5775.643942598915!2d-155.08460399999998!3d19.717722799999997!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x79524b8d28969783%3A0xaca6e3e2113e9b12!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792169905493!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How long does car shipping to Hilo take?","Three to four weeks from the West Coast, four to five from the East. A day to five days on the highway, then one to two weeks on the water. Add three to seven more if the car rides the barge from Honolulu. A direct Hilo call skips the barge. The pickup is timed so the car makes the cutoff."),
 ("How much does it cost to ship a car from Los Angeles to Hilo?","Southern California is the least expensive origin, usually seventeen hundred fifty to twenty-four hundred dollars for a sedan. The crossing makes up most of that, and the barge adds a few hundred when it is needed. The ship prices by dimensions, so a lifted truck costs more. Ask for a quote for a firm number on your sailing."),
 ("Does my car sail direct to Hilo or through Honolulu?","Whichever is faster that week. Certain sailings put in at Hilo Harbor, while others unload in Honolulu for the barge across. We compare both calendars with your pickup date and choose the one that lands the car sooner. One quote and one coordinator cover it either way."),
 ("Can you deliver to the Kona side?","Yes. A car for Kailua-Kona or Waikoloa can sail into Kawaihae Harbor when the barge schedule allows. Otherwise it lands in Hilo and crosses the saddle on a local carrier, about two hours. Tell us the side of the island when you book, and we route it the shorter way."),
 ("Can the carrier come to my house in Puna?","Usually not. The Puna subdivisions sit on lava-rock and gravel lanes that a trailer cannot use. The driver meets you in Keaau or Pahoa, or at the harbor. Hilo town, Waimea, and the paved districts allow a closer handoff."),
 ("Why does the car have to be clean?","Because every car is an invasive-species risk to the island. Inspectors look for soil, seeds, and plant matter on the body, in the wheel wells, and inside. That goes for both directions. A dirty car is refused at the gate. Wash it and vacuum it before pickup, and expect a reminder from us the day before."),
 ("Can I ship a financed car to Hilo?","Yes, once the lender signs off. The shipping line will not load a financed car without a lienholder authorization letter. Request it from the lender the week you book, because some take ten days to produce it. Have the registration with you too. We spell out the wording the line wants."),
 ("Do you ship cars from Hilo back to the mainland?","Yes. Outbound, the car boards at Hilo Harbor and sails direct or through Honolulu to a West Coast gateway. A carrier takes it the rest of the way. The same rules apply: empty car, quarter tank, no red dirt, title in hand. One coordinator runs every leg."),
 ("What happens if a hurricane or an eruption is in the forecast?","Ahead of a storm, the harbor shuts and the ships wait offshore or in Honolulu. Once it reopens, we rebook the next available slot. Lava changes the island leg, not the sailing. You hear from us at every change, and a car already aboard stays aboard."),
 ("What do you need for a car shipping quote to Hilo?","The mainland pickup point and the island destination, district and road surface included. Year, make, and model. Whether it runs, whether a lender holds the title, and whether it carries a lift or a rack. We set those against the sailing and barge calendars, and the Hilo quote comes back firm."),
]
BODY.append(faq_section(FAQ,'Hilo FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping to Hilo?','A quote takes about two minutes on the form above. Tell us the origin, the district, and your dates. We line the pickup up with the next sailing.','+18088245278','(808) 824-5278','Get your free Hilo quote'))

build({
 'slug':'auto-transport-hilo-hawaii',
 'title':'Car Shipping to Hilo, HI — Auto Transport | Ship Guy',
 'meta':'Car shipping to Hilo, HI on the Big Island: a mainland carrier, a Pacific sailing direct or through Honolulu, and the inter-island barge. Terminal rules, the agricultural inspection, Puna lava-rock lanes, the Kona side through Kawaihae, hurricane and eruption planning, Merrie Monarch week. Local office on Kinoole Street downtown. Free quote.',
 'h1':'Car Shipping to<br>Hilo, <span class="accent">Hawaii</span>',
 'lede':'Door-to-door auto transport to the Big Island, with the highway leg, the sailing, the barge, and the island delivery under one coordinator.',
 'tel':'+18088245278','disp':'(808) 824-5278','brand':'Hilo','keyword':'car shipping to hilo',
 'localterms':['hilo','big island','harbor','sailing','barge','honolulu','west coast','port','cutoff','terminal','kinoole','kamehameha','bayfront','kanoelehua','waiakea','puainako','kaumana','keaukaha','airport','puna','hawaiian paradise park','orchidland','hawaiian beaches','lava-rock','gravel','keaau','pahoa','hamakua','honokaa','waimea','saddle','training area','kailua-kona','waikoloa','kawaihae','volcano','ka’u','naalehu','university','hospital','observatories','orders','retirees','rain','flash floods','2018','eruption','vog','hurricane','iselle','lane','merrie monarch','safety inspection','registration','lienholder','quarter tank','invasive','los angeles','long beach','oakland','san diego','seattle','portland','phoenix','denver','dallas','chicago','new york'],
}, BODY, FAQ)
