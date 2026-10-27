import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("Weekly","Sailings"),("7 Days","Local Support")]))

BODY.append(intro_block('Kapaʻa, Hawaii','Car shipping to Kauai: a carrier to the coast, a sailing to Nawiliwili, and one highway up the east side',
 ['Car shipping to Kapaʻa lands at Nawiliwili Harbor in Lihue, ten miles down Kuhio Highway. Ship Guy is a licensed auto transport broker with an office on Kuhio Highway in Kapaʻa town.',
  'We arrange the mainland pickup, the sailing, and the Kauai end. The trucks and the ships belong to carriers we vet, not to us.',
  'Your car rides a carrier to a West Coast port and boards a sailing for the islands. Some sailings put in at Nawiliwili. Others unload in Honolulu, and the car rides the inter-island barge across the channel. We book whichever lands it sooner.',
  'This page explains the legs, the terminal rules, and the barge. It also covers the Coconut Coast, the Homesteads, the north shore past the bridge, and the west side.'],
 'Kapaʻa at a glance',
 ['A West Coast origin lands on Kauai in three to four weeks. An East Coast origin takes four to five. A week without a direct Nawiliwili call adds the barge, three to seven days more.',
  'The cheapest origins are the ones closest to a port: Los Angeles, the Bay Area, Seattle, and Portland. An inland origin pays for the highway miles first and the crossing second.'],
 'Tell us the district. Kapaʻa town, Wailua, and Lihue are easy. The Homesteads, Anahola, and anything past the Hanalei bridge need a meeting spot on the highway.'))

BODY.append(sec('The Process','The Three Legs of a Kauai Shipment',
 prose(
  L('A Kapaʻa shipment has a highway leg, an ocean leg, and ten miles of Kuhio Highway. Some weeks a barge sits in the middle.'),
  P('The first leg is a plain highway haul. A carrier picks the car up at your door and drives it to the port. From Southern California or the Bay Area, that takes a day or two. From Texas or the East Coast, allow five days or more. The Bill of Lading you sign at pickup follows the car onto the ship.'),
  P('The car then boards a weekly sailing. Some sailings call at Nawiliwili Harbor on the Lihue side of the island. Others arrive in Honolulu, clear that terminal, and transfer to the inter-island barge for Kauai. The barge runs on its own weekly schedule and adds three to seven days.'),
  P('The ship sails on time whether the car has arrived or not. The highway leg aims at the cutoff with a day in hand. Miss it, and the car waits for the next sailing. We run the sailing and the barge as one timeline, and no car sits on a dock.'),
  P('When the car lands, the harbor clears it and releases it. Collect it at the terminal yourself, or let us set up the island delivery. Lihue is minutes away, Kapaʻa is fifteen, and Princeville is an hour up the coast. The west side past Waimea is an hour the other way.'),
 ), alt=True))

BODY.append(sec('The Island','Kapaʻa Town, Wailua, the Homesteads, Lihue, the North Shore, and the West Side',
 prose(
  L('Kauai has one highway that nearly circles the island and stops short at both ends. The last leg follows it.'),
  P('Kapaʻa town is a strip of old storefronts between Kuhio Highway and the beach park. The highway is the only through road, and the morning crawl toward Lihue fills it. The driver meets you at the beach park, the shopping center, or the bypass road behind town. Wailua and the Coconut Coast resorts south of town have the same highway and wider lots.'),
  P('The Kapaʻa Homesteads climb the hills above town on Olohena and Kawaihau Roads. Wailua Homesteads sit above the river on Kuamoʻo Road. Both are narrow, steep, and wet, and a trailer stays on the highway. The driver meets you at the bottom of the hill. Kealia and Anahola to the north are small beach communities with lots on the highway.'),
  P('Lihue is the county seat, with the airport, the harbor, and the mall at Kukui Grove. The streets are wide, and the harbor handoff is the shortest leg of all. Puhi and Hanamaulu next door are the same. Kilauea, Princeville, and Hanalei to the north are an hour up a two-lane highway. A car hauler stops at Princeville. Past the one-lane Hanalei bridge, the car goes on a local flatbed or you drive it in.'),
  P('Koloa and Poipu on the south shore sit at the end of the tree tunnel road. The resort lots work for a handoff. Kalaheo, Eleele, and Hanapepe run west along the highway. A car for the west side can also land at Port Allen when the barge schedule allows. Waimea and Kekaha are the end of the road, an hour from the harbor. The driver meets you on the highway in town.'),
 )))

ROUTES=[("Los Angeles / Long Beach","land + ocean","3–4 weeks","$1,750–$2,400"),("Bay Area / Oakland","land + ocean","3–4 weeks","$1,775–$2,450"),
 ("San Diego, CA","land + ocean","3–4 weeks","$1,800–$2,500"),("Seattle / Portland","land + ocean","3–4 weeks","$1,850–$2,550"),
 ("Phoenix, AZ","land + ocean","3.5–4.5 weeks","$2,050–$2,850"),("Denver, CO","land + ocean","4–4.5 weeks","$2,250–$3,100"),
 ("Dallas / Houston","land + ocean","4–4.5 weeks","$2,300–$3,150"),("Chicago, IL","land + ocean","4–5 weeks","$2,500–$3,400"),
 ("New York / New Jersey","land + ocean","4–5 weeks","$2,800–$3,900"),("Honolulu (inter-island barge)","barge only","about 1 week","$300–$450")]
BODY.append(rate_table('Lanes &amp; Costs','Car Shipping to Kapaʻa: Estimated Times and Costs',
 'The usual mainland origins, with estimated door-to-door times and sedan rates. The form above prices your exact lane.',
 ['Origin → Kapaʻa','Route type','Est. door to door','Est. rate*'],ROUTES,
 '*2026 estimates for a running sedan on an open highway leg, landed at Nawiliwili and delivered to Kapaʻa. The barge is included in a week without a direct call. The ship prices by dimensions, so a lifted truck or a roof rack moves the number. The sailing calendar and your dates set the firm figure.',
 prose(
  P('The West Coast origins price within a hundred dollars of each other because the crossing is the same. The highway miles and the barge are the only variables. A direct call at Nawiliwili saves the barge fee, and we book it whenever the calendar allows.'),
  P('An East Coast origin adds a long land leg and the days that go with it. The general factors are in the <a href="car-shipping-cost.html">cost guide</a>.'),
 ), alt=True))

BODY.append(sec('Terminal Rules','The Rules That Get Cars Turned Away at the Port',
 prose(
  L('The terminal gate is stricter than any highway pickup, and it checks every car on both ends.'),
 )+ULI([
  "The car ships empty, with nothing of yours inside, not even in the trunk",
  "A quarter tank of fuel or less at the gate",
  "Washed outside and vacuumed inside, because the inspectors look for soil, seeds, and plant matter",
  "Title or registration in hand, and the lender’s letter on a financed car",
  "The dock measures every car, so a lift, a rack, or a camper shell changes the price",
  "One working key goes with the car, and any aftermarket alarm is switched off",
 ])+prose(
  P('The cleanliness rule is the one that catches people. Kauai fights invasive species on every sailing. A muddy wheel well gets a car refused at the gate. Wash the outside and vacuum the inside the day before pickup.'),
  P('Outbound cars get the same inspection in Nawiliwili. Red dirt from the Homesteads counts. We send a checklist before pickup, because a car that reaches the terminal ready never loses its sailing.'),
 )))

BODY.append(sec('Who Ships Here','The Resorts, the Hospital, the College, the Missile Range, and the Transplants',
 prose(
  L('Kapaʻa ships for the resorts, a hospital, a college, and a Navy range across the island.'),
  P('The resorts on the Coconut Coast, in Poipu, and in Princeville hire managers and chefs on mainland contracts. Most ship a car behind the move. The hospital in Lihue brings in nurses and physicians all year. The county and the utility co-op relocate engineers on their own schedules. We supply the paperwork a reimbursed move needs.'),
  P('The missile range at Barking Sands on the west side rotates sailors and contractors on orders. Families live from Kekaha to Kapaʻa, and the orders cover one car. The second one comes with us. Ship Guy is a private broker with no connection to the range. The <a href="military-car-shipping.html">military</a> page covers the timing around a report date.'),
  P('The community college in Puhi brings students in each August, and some ship a car for the year. An adult signs at a campus lot. Remote workers and retirees move to Kapaʻa and the north shore every month. The reverse trip is just as common. Families leaving for the mainland sail the car out of Nawiliwili and finish on a carrier.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Rain, Hurricanes, the Hanalei Bridge, and the Coconut Festival',
 prose(
  L('Kauai is the oldest and wettest of the islands, and the schedule bends around the water.'),
  P('The mountain in the middle of the island is one of the wettest places on earth. The east side gets the showers. A downpour floods Kuhio Highway at the Wailua River and the bypass for an hour. The handoff waits it out. The winter rains from December to March close the Homestead roads a few times a season.'),
  P('The north shore floods hardest. The April 2018 storm dropped four feet of rain on Hanalei in a day. The highway beyond it stayed closed for a year. Landslides still close the road at Hanalei after a wet week. A delivery past Princeville waits for the road, and we tell you when it does.'),
  P('Hurricane season runs June through November. Iniki crossed the island in September 1992 and took the roofs off Kapaʻa. The harbor shuts before a storm arrives, and the ships hold offshore or in Honolulu. Sailings resume as soon as Nawiliwili opens, and so do we.'),
  P('The Coconut Festival fills the beach park in Kapaʻa on a weekend in October. The county fair fills the stadium in Lihue in August. The marathon closes the Poipu roads on a Sunday in September. A handoff near any of them moves to the morning or to another lot.'),
 )+chips(["Kapaʻa Town","Beach Park","Kuhio Highway","Bypass Road","Coconut Coast","Wailua","Lydgate","Kapaʻa Homesteads","Wailua Homesteads","Olohena","Kawaihau","Kealia","Anahola","Moloaʻa","Kilauea","Princeville","Hanalei","Lihue","Nawiliwili","Kalapaki","Hanamaulu","Puhi","Kukui Grove","Koloa","Poipu","Kalaheo","Eleele","Port Allen","Hanapepe","Waimea","Kekaha"])
 +NOTE('Serving Kapaʻa and all of Kauai, from the Homesteads to the end of the road. Tell us the district, the road, and whether the car runs.')))

BODY.append(sec('After Arrival','Registering the Car on Kauai',
 prose(
  L('The county keeps a short list for a car that has just landed.'),
  P('A mainland car needs a Hawaii safety inspection and a county registration within a set window. The county office in Lihue handles both. Bring the mainland title or registration and the shipping papers. Confirm the current rules with the county before you go.'),
  P('None of it holds up the shipment. Having the folder ready the day the harbor releases the car saves a second trip to Lihue.'),
 ), alt=True))

BODY.append(sec('Why Ship Guy','Why Kauai Shippers Choose Ship Guy',
 prose(
  L('We book the sailing and the barge as one trip. We plan the last leg around the highway, the hill roads, and the bridge.'),
  P('Ship Guy holds active FMCSA brokerage authority with a $75,000 surety bond behind the highway legs. Both appear in the federal register. The ocean legs ride licensed ocean carriers. Our office is on Kuhio Highway in Kapaʻa town.'),
  P('One coordinator follows the pickup, the cutoff, the sailing, and the harbor release. You hear from that person at every step. Open, enclosed, and expedited options for the highway legs are on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Kapaʻa','4-1624 Kuhio Hwy #145A','Kapaʻa, HI 96746','+18084357375','(808) 435-7375','HST',
 '4-1624+Kuhio+Hwy+%23145A,+Kapaa,+HI+96746','Visit Us','Find Ship Guy in Kapaʻa',
 'Our office is on Kuhio Highway in Kapaʻa town, a short walk from the beach park.',
 map_src=None, alt=True))

FAQ=[
 ("How long does car shipping to Kapaʻa take?","Three to four weeks from the West Coast and four to five from the East. The highway leg takes a day to five days, and the crossing takes one to two weeks. Add three to seven more when the car rides the barge from Honolulu. A direct Nawiliwili call skips the barge. We time the pickup so the car makes the cutoff."),
 ("How much does it cost to ship a car from California to Kapaʻa?","Southern California and the Bay Area are the least expensive origins. Count on seventeen hundred fifty to twenty-four hundred fifty dollars for a sedan. The crossing is most of that. The barge adds a few hundred in a week without a direct call. Height and length set the ocean fare, so a lifted truck pays more than a sedan. The form above returns a firm number for your sailing."),
 ("Does my car sail direct to Kauai or through Honolulu?","Whichever lands it sooner that week. Some sailings put in at Nawiliwili, and others unload in Honolulu for the barge across the channel. We lay both calendars against your pickup date and choose the faster one. One quote and one coordinator cover it either way."),
 ("Can you deliver past the Hanalei bridge?","Not on a car hauler. The one-lane bridge at Hanalei carries a weight limit a loaded trailer exceeds. The road beyond it closes after heavy rain. The hauler stops at Princeville. From there a local flatbed finishes the trip, or you drive the car in yourself. Tell us the address, and we price the option that fits."),
 ("Can the carrier come to my house in the Homesteads?","Usually not. Olohena, Kawaihau, and Kuamoʻo Roads are steep, narrow, and wet, and a trailer stays on the highway. The driver meets you at the bottom of the hill or at the beach park in town. Kapaʻa town, Wailua, and Lihue allow a closer handoff."),
 ("Why does the car have to be clean?","Kauai treats every arriving car as a possible carrier of seeds, soil, and insects. The inspectors go over the body, the wheel wells, and the cabin. A dirty car is turned away at the gate, inbound or outbound. Wash it and vacuum it the day before pickup. We send a reminder so it is not forgotten."),
 ("Can I ship a financed car to Kauai?","Yes, with the lender’s letter. The shipping line will not load a financed car without a lienholder authorization. Ask the lender for it the week you book, since some take ten days. Bring the registration as well. We send you the wording the line wants."),
 ("Do you ship cars from Kapaʻa back to the mainland?","Yes. Outbound, the car boards at Nawiliwili and sails direct or by way of Honolulu. It lands at a West Coast port. A carrier finishes the trip to your new address. The gate rules run in reverse: nothing inside, a quarter tank, no red dirt, title in hand. One coordinator holds every leg."),
 ("What happens if a hurricane is in the forecast?","The harbor closes ahead of the storm, and the ships wait offshore or in Honolulu. Once Nawiliwili reopens, we rebook the next available slot. A car already aboard stays aboard. The north shore road is the other variable, and a delivery past Princeville waits for it to reopen. You hear from us at every change."),
 ("What do you need for a car shipping quote to Kapaʻa?","Where the car is on the mainland and where it is going on Kauai, down to the road. The year, make, and model. Whether it drives, whether it is financed, and whether anything raises its height. We match those to the next sailing and the barge. The Kapaʻa number is firm when it arrives."),
]
BODY.append(faq_section(FAQ,'Kapaʻa FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping to Kapaʻa?','The form above takes two minutes. Give us the mainland origin, the Kauai district, and your dates. We aim the pickup at the next sailing.','+18084357375','(808) 435-7375','Get your free Kapaʻa quote'))

build({
 'slug':'auto-transport-kapaa-hawaii',
 'title':'Car Shipping to Kapaʻa, HI — Auto Transport | Ship Guy',
 'meta':'Car shipping to Kapaʻa, HI on Kauai: a mainland carrier, a Pacific sailing direct to Nawiliwili or through Honolulu, and the inter-island barge. Terminal rules, the agricultural inspection, the Homesteads, the Hanalei bridge, the west side, hurricane planning, and the Coconut Festival. Local office on Kuhio Highway. Free quote.',
 'h1':'Car Shipping to<br>Kapaʻa, <span class="accent">Hawaii</span>',
 'lede':'Door-to-door auto transport to Kauai, with the highway leg, the sailing, the barge, and the island delivery under one coordinator.',
 'tel':'+18084357375','disp':'(808) 435-7375','brand':'Kapaʻa','keyword':'car shipping to kapaʻa',
 'localterms':['kapaʻa','kapaa','kauai','nawiliwili','lihue','kuhio highway','sailing','barge','honolulu','west coast','port','cutoff','terminal','beach park','shopping center','bypass','coconut coast','wailua','resorts','homesteads','olohena','kawaihau','kuamoʻo','kealia','anahola','airport','harbor','kukui grove','puhi','hanamaulu','kilauea','princeville','hanalei','one-lane','bridge','flatbed','koloa','poipu','tree tunnel','kalaheo','eleele','hanapepe','port allen','waimea','kekaha','hospital','college','county','utility','missile range','barking sands','orders','retirees','remote workers','rain','wettest','2018','landslides','hurricane','iniki','1992','coconut festival','county fair','marathon','safety inspection','registration','lienholder','quarter tank','invasive','red dirt','los angeles','long beach','oakland','san diego','seattle','portland','phoenix','denver','dallas','chicago','new york'],
}, BODY, FAQ)
