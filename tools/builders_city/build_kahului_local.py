import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("Weekly","Sailings"),("7 Days","Local Support")]))

BODY.append(intro_block('Kahului, Hawaii','Car shipping to Maui: a mainland carrier, a Pacific sailing, and the only deep harbor on the island',
 ['Car shipping to Kahului means getting a car to Maui, and every car reaches Maui by sea. Ship Guy is a licensed auto transport broker with an office on the Hana Highway near the harbor.',
  'We coordinate the mainland pickup, the sailing, and the island delivery, and we own neither trucks nor ships.',
  'A carrier takes your car to a West Coast port, and it sails from there. Some sailings call at Kahului Harbor directly. Others land in Honolulu and cross on the inter-island barge. We book the routing that lands the car first.',
  'This page covers the three legs, the terminal rules, and the barge. It also covers central Maui, the west side, Upcountry, Hana, the resorts, and the rebuilding in Lahaina.'],
 'Kahului at a glance',
 ['Plan on three to four weeks from the West Coast and four to five from the East. The barge from Honolulu adds three to seven days when the sailing does not call here.',
  'Southern California and the Bay Area are the shortest and least expensive origins. Seattle and Portland follow. Every other origin adds a land leg first.'],
 'Tell us the side of the island. Kahului, Wailuku, and Kihei are easy. Upcountry, the west side, and Hana need a meeting spot and an extra day.'))

BODY.append(sec('The Process','The Three Legs of a Maui Shipment',
 prose(
  L('A Maui shipment is a highway leg, an ocean leg, and a short island leg. Some weeks add a barge.'),
  P('A carrier picks up your car anywhere on the mainland and delivers it to a West Coast terminal. From Los Angeles or Oakland, that leg takes a day or two. From the Mountain West or the East Coast, count on several days. It is a normal domestic shipment with a Bill of Lading at pickup.'),
  P('The car then boards a weekly sailing. Some sailings call at Kahului Harbor on the north shore. Others arrive in Honolulu, clear that terminal, and transfer to the inter-island barge for Maui. The barge runs on its own weekly schedule and adds three to seven days.'),
  P('Departures are fixed, so the highway leg is timed to the port cutoff. A missed sailing waits a week for the next one. We track the sailing and the barge together, and nothing sits on a dock.'),
  P('After arrival, the car clears the harbor and is released. You can collect it at the terminal in Kahului, or we arrange delivery across the island. Wailuku and Kihei are twenty minutes away. The west side and Upcountry take an hour, and Hana takes a morning.'),
 ), alt=True))

BODY.append(sec('The Island','Kahului, Wailuku, Kihei, Upcountry, the West Side, and Hana',
 prose(
  L('Maui is one harbor and five very different last legs.'),
  P('Kahului is the commercial center, with the harbor, the airport, and the shopping centers on wide roads. The handoff happens at the harbor or at a lot on Dairy Road. Wailuku next door is the county seat, with an old downtown on narrow streets. Happy Valley climbs the hill behind it. The driver meets you on Kaahumanu Avenue or in Kahului.'),
  P('Kihei and Wailea run down the south shore on the Piilani Highway. The condos have garages and lots, and the resort communities in Wailea and Makena have gates. The driver meets you at the gate or at a lot on Piilani. Maalaea sits at the junction with room everywhere.'),
  P('Upcountry climbs the volcano through Pukalani, Makawao, Kula, and Haiku on winding two-lane roads with gulches. The driver meets you in Pukalani or Makawao town. The farms and the ranch roads above Kula are not trailer country. Paia on the north shore has a tight old main street. The handoff happens at the lot by the beach park.'),
  P('The west side across the Pali is Lahaina, Kaanapali, Napili, and Kapalua. Lahaina is rebuilding after the 2023 fire, and the construction changes the roads month to month. The resorts and the condo towers have lots, and the driver meets you at the resort entrance. Hana sits at the end of fifty miles of one-lane bridges. A car for Hana is handed off in Kahului.'),
 )))

ROUTES=[("Los Angeles / Long Beach","land + ocean","3–4 weeks","$1,750–$2,400"),("Bay Area / Oakland","land + ocean","3–4 weeks","$1,775–$2,450"),
 ("San Diego, CA","land + ocean","3–4 weeks","$1,800–$2,500"),("Seattle / Portland","land + ocean","3–4 weeks","$1,850–$2,550"),
 ("Phoenix, AZ","land + ocean","3.5–4.5 weeks","$2,050–$2,850"),("Denver, CO","land + ocean","4–4.5 weeks","$2,250–$3,100"),
 ("Dallas / Houston","land + ocean","4–4.5 weeks","$2,300–$3,150"),("Chicago, IL","land + ocean","4–5 weeks","$2,500–$3,400"),
 ("New York / New Jersey","land + ocean","4–5 weeks","$2,800–$3,900"),("Honolulu (inter-island barge)","barge only","about 1 week","$300–$450")]
BODY.append(rate_table('Lanes &amp; Costs','Car Shipping to Kahului: Estimated Times and Costs',
 'Common origins with estimated door-to-door times and rates for a sedan. Price your exact route above.',
 ['Origin → Kahului','Route type','Est. door to door','Est. rate*'],ROUTES,
 '*2026 estimates for a running sedan with open transport on the highway leg. The barge is included when the sailing does not call at Kahului. SUVs and trucks cost more, and oversized vehicles price by dimensions on the ship. The real quote reflects carrier availability, the sailing schedule, and your dates.',
 prose(
  P('The West Coast origins sit within a hundred dollars of each other. The crossing is the same for all of them. The highway miles and the barge move the total. A direct call at Kahului saves the barge fee, and we book it when the calendar lines up.'),
  P('The East Coast adds a long land leg and the days that go with it. Our <a href="car-shipping-cost.html">cost guide</a> covers the general factors.'),
 ), alt=True))

BODY.append(sec('Terminal Rules','The Rules That Get Cars Turned Away at the Port',
 prose(
  L('The port has rules the highway does not, and the gate enforces them in both directions.'),
 )+ULI([
  "Nothing personal inside the vehicle, with no exceptions at the gate",
  "A quarter tank of fuel or less when the car reaches the terminal",
  "A car washed outside and vacuumed inside, because Hawaii inspects for soil, seeds, and plant matter",
  "The title or registration, and a lienholder authorization letter if the car is financed",
  "Height and length are measured on the dock, so lifts and racks change the price",
  "Keys stay with the car, and any aftermarket alarm is switched off",
 ])+prose(
  P('Maui enforces the agricultural rule hard. One invasive beetle or fire ant can cost the island its crops. A muddy tire or leaves under the seats gets a car refused. A car leaving Maui for the mainland is inspected the same way, and red dirt counts.'),
  P('The lienholder letter catches people out. Ask the lender the day you book, because some take two weeks. We tell you exactly what to request. A car that arrives at the terminal ready keeps its sailing.'),
 )))

BODY.append(sec('Who Ships Here','The Resorts, the Hospital, the College, and the Observatories',
 prose(
  L('Maui ships for the resorts, the hospital, the campus, and the summit.'),
  P('The resorts on the west and south shores hire managers, chefs, and seasonal staff from the mainland. Many ship a car for the season. The hospital in Wailuku brings in nurses and physicians on contracts. The college in Kahului brings students in each August. An adult signs for a student car at the campus lot.'),
  P('The observatories on the summit and the computing center in Kihei relocate scientists and engineers on program schedules. The farms in the central valley and Upcountry bring in managers on planting cycles. We supply the paperwork a reimbursed move needs.'),
  P('Families move to Maui for the life and leave it for the prices. Both directions ship with us. A car leaving the island sails from Kahului, direct or through Honolulu, and finishes on a mainland carrier. Ship Guy is a private broker, and the <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the mainland side.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Trade Winds, Kona Storms, the Fire, and Whale Season',
 prose(
  L('Maui weather is mild until it is not. The island calendar moves the last leg more than the sailing.'),
  P('Trade winds blow most days, and Kahului is one of the windiest spots in the state. A high-profile trailer on the Pali or the central valley slows down in a strong trade. Kona storms in winter bring rain from the south. The gulches on the Hana Highway and the Upcountry roads flood for a few hours. A pickup there moves to town.'),
  P('Hurricane season runs June through November. Lane in 2018 brushed the island. The winds from Dora in 2023 fed the fire that destroyed Lahaina town. The harbor closes ahead of a storm, and sailings hold at sea or in Honolulu. We reschedule the moment the port reopens.'),
  P('The west side is rebuilding. The Honoapiilani Highway carries construction traffic and periodic rockfall closures on the Pali. A west-side handoff is set at the resort entrance or in Maalaea when the road is slow. We check the road the morning of the delivery.'),
  P('Whale season fills the south shore from December through April, and the Maalaea and Kihei lots fill early. Spring break and the holidays fill every rental car and every resort lot. The handoff moves to the harbor side of Kahului in those weeks.'),
 )+chips(["Kahului","Harbor","Dairy Road","Airport","Wailuku","Happy Valley","Waikapu","Waihee","Kihei","Wailea","Makena","Maalaea","Pukalani","Makawao","Kula","Haiku","Paia","Spreckelsville","Lahaina","Kaanapali","Honokowai","Napili","Kapalua","Hana","Kaupo"])
 +NOTE('Serving Kahului and all of Maui, from the harbor to Hana. Tell us the side of the island, the gate, and whether the car runs.')))

BODY.append(sec('After Arrival','Registering the Car on Maui',
 prose(
  L('Once the car lands, the county asks a few things of its new owner.'),
  P('Out-of-state vehicles need a Hawaii safety inspection and county registration within a set window after arrival. The county office in Kahului handles both. Bring the mainland title or registration and the shipping paperwork. Check the current requirements with the county before you go.'),
  P('None of this touches the shipment itself. It helps to have the documents in one folder when the car is released at the harbor.'),
 ), alt=True))

BODY.append(sec('Why Ship Guy','Why Maui Shippers Choose Ship Guy',
 prose(
  L('We book the sailing and the barge as one move. We plan the last leg around the side of the island.'),
  P('Ship Guy carries active FMCSA brokerage authority and a $75,000 surety bond for the highway legs. The federal register lists both. The ocean legs ride licensed ocean carriers. Our office is on the Hana Highway in Kahului.'),
  P('One coordinator watches the pickup, the cutoff, the sailing, and the barge, and calls you at each step. The highway legs can be open, enclosed, or expedited, and the <a href="services.html">services</a> page describes each.'),
 )))

BODY.append(office('Kahului','400 Hana Hwy #225A','Kahului, HI 96732','+18084683952','(808) 468-3952','HST',
 '400+Hana+Hwy+%23225A,+Kahului,+HI+96732','Visit Us','Find Ship Guy in Kahului',
 'Our office is on the Hana Highway in Kahului, a few blocks from the harbor.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5732.255346430678!2d-156.4555656!3d20.885557599999995!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x7954d3b8050dee5b%3A0x56c1af49f6f449ff!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792169892664!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How long does car shipping to Maui take?","Three to four weeks from the West Coast and four to five from the East. The highway leg runs a day to five days by origin, and the crossing one to two weeks. The barge from Honolulu adds three to seven days when the sailing does not call at Kahului. A direct call saves that week. We time the pickup to the cutoff."),
 ("How much does it cost to ship a car from California to Kahului?","Los Angeles and Oakland run seventeen hundred fifty to twenty-four hundred fifty dollars for a sedan. The crossing is most of that, and the barge adds a few hundred when it is needed. The ship prices by dimensions, so a lifted truck or a roof rack costs more. Ask for a quote for a firm number on your sailing."),
 ("Does the car sail direct to Kahului or through Honolulu?","Both happen. Some weekly sailings call at Kahului Harbor directly. Others land in Honolulu and transfer to the inter-island barge. We check both schedules against your pickup date and book the routing that lands the car first. You get one quote and one coordinator either way."),
 ("Can you deliver to Lahaina or the west side?","Yes. The car lands in Kahului and crosses the Pali on a local carrier, about an hour. Lahaina is rebuilding, and the highway carries construction traffic and the occasional rockfall closure. We set the handoff at the resort entrance or in Maalaea when the road is slow. We check it the morning of delivery."),
 ("Can the carrier come to my house Upcountry or in Hana?","Not usually. Upcountry roads wind through gulches, and the Hana Highway is fifty miles of one-lane bridges. The driver meets you in Pukalani or Makawao town. A car for Hana is handed off in Kahului. Kihei, Wailuku, and central Maui allow a closer handoff."),
 ("Why does the car have to be clean?","Because Maui fights invasive species on every shipment. Inspectors check for soil, seeds, insects, and plant matter on and inside the vehicle, in both directions. A muddy tire or leaves under the seats gets a car refused. Wash the outside and vacuum the inside before pickup, and we remind you before the driver comes."),
 ("Can I ship a financed car to Maui?","Yes, with one extra document. If a lender holds the title, the shipping line needs a lienholder authorization letter before the car boards. Ask the lender the day you book, because some take two weeks. Bring the registration too. We tell you exactly what to request."),
 ("Do you ship cars from Maui back to the mainland?","Yes, the trip runs in reverse. The car sails from Kahului Harbor, direct or through Honolulu, to a West Coast gateway. A carrier finishes the trip. Empty the car, keep fuel at a quarter tank, wash off the red dirt, and bring the title. We coordinate every leg."),
 ("What happens if a hurricane or a Kona storm is in the forecast?","The harbor closes ahead of a hurricane, and sailings hold at sea or in Honolulu until it reopens. A Kona storm floods the gulch roads for a few hours and moves a last-leg handoff to town. We reschedule the moment the port and the roads clear. A car already on a ship keeps moving."),
 ("What do you need for a car shipping quote to Kahului?","The mainland pickup address and the Maui delivery address, with the side of the island. The year, make, and model. Whether it runs, whether it is financed, and any lift or rack. We line those details up against the sailing and barge schedules. That is what an accurate Maui quote requires."),
]
BODY.append(faq_section(FAQ,'Kahului FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping to Maui?','A quote takes about two minutes on the form above. Give us the origin, the side of the island, and your dates. We match the pickup to the next sailing.','+18084683952','(808) 468-3952','Get your free Kahului quote'))

build({
 'slug':'auto-transport-kahului-hawaii',
 'title':'Car Shipping to Kahului, HI — Maui Auto Transport | Ship Guy',
 'meta':'Car shipping to Kahului, HI and all of Maui: a mainland carrier, a Pacific sailing direct or through Honolulu, and the inter-island barge. Terminal rules, the agricultural inspection, Kihei and Wailea gates, Upcountry and Hana handoffs, the rebuilding west side, hurricane and Kona storm planning. Local office on the Hana Highway. Free quote.',
 'h1':'Car Shipping to<br>Kahului, <span class="accent">Hawaii</span>',
 'lede':'Door-to-door auto transport to Maui, with the highway leg, the sailing, the barge, and the island delivery under one coordinator.',
 'tel':'+18084683952','disp':'(808) 468-3952','brand':'Kahului','keyword':'car shipping to kahului',
 'localterms':['kahului','maui','harbor','sailing','barge','honolulu','west coast','port','cutoff','terminal','hana highway','dairy road','airport','wailuku','happy valley','kaahumanu','kihei','wailea','makena','piilani','maalaea','upcountry','pukalani','makawao','kula','haiku','gulches','paia','lahaina','kaanapali','napili','kapalua','pali','honoapiilani','hana','one-lane bridges','resorts','hospital','college','observatories','computing center','farms','trade winds','kona storms','hurricane','lane','2018','dora','2023','fire','rebuilding','rockfall','whale season','safety inspection','registration','lienholder','quarter tank','invasive','los angeles','long beach','oakland','san diego','seattle','portland','phoenix','denver','dallas','chicago','new york'],
}, BODY, FAQ)
