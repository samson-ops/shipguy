import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Stamford, Connecticut','Car shipping on the Gold Coast, thirty-five miles from Manhattan on the busiest stretch of Interstate 95',
 ['Car shipping in Stamford works around one road the trucks can use and one they cannot. Ship Guy is a licensed auto transport broker with an office on Summer Street at Bull’s Head.',
  'We book vetted carriers across lower Fairfield County, from Greenwich and Darien to New Canaan. We do not own the trucks.',
  'Interstate 95 runs along the shore through downtown. The Merritt Parkway runs across the north of the city. The Merritt bans commercial vehicles, so every carrier uses 95 or the Post Road. High Ridge and Long Ridge roads climb into North Stamford.',
  'This page covers the interstate and the parkway, downtown and the towers, and the estate roads. It also covers the headquarters, the hospital, the Florida lane, the storms, and the traffic.'],
 'Stamford at a glance',
 ['Most pickups happen within 1 to 3 days. The New England carriers pass the city on 95 all day, and so do the New York ones.',
  'Manhattan, Yonkers, Hartford, and New Haven are same-day lanes. Boston and Philadelphia are the same day too. Washington and Albany take a day. Florida runs three.'],
 'Tell us the neighborhood. Downtown towers, Shippan, and the North Stamford estate roads need a meeting spot. Springdale, Glenbrook, and the flatter grids often allow the curb.'))

BODY.append(sec('The Roads','Interstate 95, the Merritt Parkway, the Post Road, and the Ridges',
 prose(
  L('Stamford sits on the worst twenty miles of Interstate 95 in New England. The carriers plan around the clock.'),
  P('Interstate 95 runs through downtown between the harbor and the rail line. Exits 6 through 9 carry the city. The stretch from Greenwich to Bridgeport backs up from six in the morning until well into the evening. Carriers schedule Stamford stops early or after the rush.'),
  P('The Merritt Parkway crosses the north of the city under low stone bridges. Commercial vehicles are banned from it. A carrier never uses it. A North Stamford pickup happens on High Ridge or Long Ridge Road near the parkway. The estate road itself is out.'),
  P('The Post Road is US 1, and it runs through downtown as Main Street and Tresser Boulevard. Washington Boulevard and Summer Street run north from the harbor to Bull’s Head. The lots along Canal Street and by the 95 exits are the usual meeting spots.'),
  P('Our office sits on Summer Street at Bull’s Head, a mile north of downtown.'),
 ), alt=True))

BODY.append(sec('Downtown &amp; the Ridges','Harbor Point, Downtown, Shippan, Springdale, and North Stamford',
 prose(
  L('Stamford is towers by the harbor, grids in the middle, and estates in the hills. The handoff changes with each.'),
  P('Downtown and Harbor Point are apartment towers with garages, and a seventy-five-foot trailer cannot wait on Washington Boulevard. The garage pulls the car out, and the driver meets you at a lot nearby. Tell the garage a day ahead.'),
  P('Shippan Point and the Cove sit on the water with narrow streets and flooding in a storm. The driver meets you on Shippan Avenue or at the lot by the beach. Springdale, Glenbrook, and the Cove grids often allow the truck at the curb.'),
  P('North Stamford is estate country, with winding roads, stone walls, and gated drives under old trees. The truck stays on High Ridge or Long Ridge Road. Greenwich, Darien, and New Canaan are the same. The Post Road is the usual spot for all three.'),
  P('Enclosed transport is the norm for the collector cars and the exotics in the hills. The handoff happens in a lot off High Ridge Road or at the dealer. The car never sits on the street.'),
 )))

ROUTES=[("Manhattan, NY","I-95 · ~35 mi","Same day","$130–$220"),("Hartford, CT","I-95/I-91 · ~80 mi","Same day","$170–$280"),
 ("Philadelphia, PA","I-95 · ~130 mi","Same day","$200–$320"),("Boston, MA","I-95/I-90 · ~180 mi","Same day","$230–$350"),
 ("Albany, NY","I-684/I-87 · ~130 mi","1 day","$200–$320"),("Washington, DC","I-95 · ~260 mi","1 day","$260–$390"),
 ("Charlotte, NC","I-95/I-85 · ~660 mi","2 days","$490–$700"),("Chicago, IL","I-80 · ~820 mi","2 days","$580–$840"),
 ("Orlando, FL","I-95 · ~1,120 mi","3 days","$780–$1,100"),("Palm Beach, FL","I-95 · ~1,250 mi","3–4 days","$810–$1,160")]
BODY.append(rate_table('Lanes &amp; Costs','Stamford Car Shipping Lanes and Estimated Costs',
 'The lanes Stamford households and headquarters price most, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a running sedan on an open trailer. SUVs and pickups run roughly 10 to 25 percent higher, and enclosed higher still. The season, the 95 traffic, and the carriers free on your dates set the final figure.',
 prose(
  P('Stamford prices like the city and the suburbs at once. Every carrier between New York and New England passes it. Manhattan and Philadelphia ride 95 south, and Boston and Hartford ride 95 and 91 north.'),
  P('The Palm Beach lane fills with finance households from October into December. It prices well because of it. The <a href="car-shipping-cost.html">cost guide</a> explains how the number is built.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Headquarters, the Hospital, the Commuters, and the Florida Lane',
 prose(
  L('Stamford relocates people on the bonus cycle, the start date, the residency match, and the Florida season.'),
  P('The cable company, the consumer-finance company, and the Harbor Point funds relocate staff from every state and abroad. Most arrive on start dates and ship a car rather than drive it. The towers have loading zones that work for a handoff when the garage allows it.'),
  P('Finance households move between Fairfield County, Manhattan, Palm Beach, and Texas on a schedule of their own. Many keep a car in two places and ship it between them twice a year. Our <a href="snowbird-car-shipping.html">snowbird</a> page covers the planning.'),
  P('The hospital on the west side brings in residents every June and July. Most arrive from out of state with a car. The handoff happens on Washington Boulevard or at a lot off 95 rather than in the hospital garage.'),
  P('Thousands of residents ride the express train to Grand Central every morning. Families move up from the city for the schools all year. The second car often ships instead of fighting 95 on moving day.'),
  P('Employers that reimburse the shipment get the records they ask for from us. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side of a move.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Nor’easters, Shippan Floods, the Parade, and the 95 Rush',
 prose(
  L('Stamford gets the coast’s weather and the corridor’s traffic, and the second one matters more.'),
  P('Interstate 95 backs up from six to ten and again from three to seven. A Stamford pickup happens between the two rushes. The driver names the spot the day before, usually near an exit. A pickup downtown on a weekday afternoon is the one thing we avoid.'),
  P('Nor’easters close 95 for a morning a few times each winter, and the carriers wait for the plows. Shippan Point and the Cove flood in a storm surge. A pickup there waits for the tide to fall. A winter pickup can slide a day.'),
  P('The balloon parade fills downtown on the Sunday before Thanksgiving. The summer concerts close Bedford Street on Thursday evenings. We move a downtown pickup to another day for both.'),
  P('Summer heat moves the loading hour earlier, and the beach traffic fills Shippan Avenue on weekends. Wind off the Sound slows a trailer on the 95 bridges now and then.'),
 )+chips(["Downtown","Harbor Point","South End","Shippan","The Cove","East Side","Glenbrook","Springdale","Belltown","Newfield","Turn of River","North Stamford","Westover","Waterside","High Ridge","Long Ridge","Bull’s Head","Ridgeway","Greenwich","Riverside","Old Greenwich","Darien","New Canaan","Norwalk"])
 +NOTE('Serving Stamford, Greenwich, Darien, and New Canaan. Tell us the neighborhood, the garage, and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Stamford?',
 prose(
  L('Stamford books enclosed trailers more often than almost any city we serve, and the hills explain why.'),
  P('An enclosed trailer keeps the salt, the road grime, and attention off the car. The garages in North Stamford, Greenwich, and Darien book enclosed trailers as a matter of course. So do the cars headed to Palm Beach for the winter.'),
  P('A commuter car still rides open to Florida or Boston without a second thought. Our <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain what the roof buys and what it costs.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff at a lot between the rushes, and a delivery. The garage and the traffic decide the hour.'),
  P('Accept the price, and a carrier already running 95 takes the booking. We set the spot and the hour around the rush. The driver and you circle the car and record its condition on a Bill of Lading. Both sign, and the delivery check runs against it.'),
 )+ULI([
  "Pack your belongings out of the car",
  "Leave the tank at about a quarter",
  "Photograph the car before pickup, especially a dark car in salt season",
  "Pass the driver a working key and mention any mechanical issue",
  "Aftermarket alarm off before the truck arrives",
  "In a tower, have the garage bring the car out an hour before the window",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages carry the rest.'))))

BODY.append(sec('Why Ship Guy','Why Stamford Drivers Choose Ship Guy',
 prose(
  L('We work 95 every day and plan around the rush, the parkway, and the Florida season.'),
  P('Ship Guy’s FMCSA brokerage authority is active, and the $75,000 surety bond behind it is public record. Our office is on Summer Street at Bull’s Head.'),
  P('One coordinator carries your booking from the quote to the signature at delivery. You can book open, enclosed, or expedited, and the <a href="services.html">services</a> page describes the three.'),
 ), alt=True))

BODY.append(office('Stamford','1100 Summer St #488','Stamford, CT 06905','+14754453917','(475) 445-3917','ET',
 '1100+Summer+St+%23488,+Stamford,+CT+06905','Visit Us','Find Ship Guy in Stamford',
 'Our office is on Summer Street at Bull’s Head, a mile north of downtown.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4626.195003090361!2d-73.5411298!3d41.0602972!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c2a1d6a23b2ef7%3A0x1c300040808100b2!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792153169612!5m2!1sen!2sus'))

FAQ=[
 ("Can the carrier come to my house in North Stamford or Greenwich?","Usually not. The roads wind, the stone walls sit at the edge, and the drives are gated. The Merritt Parkway bans trucks entirely. The driver meets you on High Ridge Road, on Long Ridge Road, or near a 95 exit. It is a short drive from the front door."),
 ("How much does it cost to ship a car from Stamford to Palm Beach or Manhattan?","Palm Beach runs eight hundred ten to eleven hundred sixty dollars for a sedan. That is about twelve hundred fifty miles down Interstate 95. Manhattan runs one hundred thirty to two hundred twenty, about thirty-five miles. Fall southbound costs more than spring. SUVs and pickups add 10 to 25 percent."),
 ("My car is in a garage in Harbor Point. How does the handoff work?","Have the garage bring the car up an hour before the window. Drive it a few minutes to the lot the driver names, usually off Canal Street. Tell the garage a day ahead. At delivery, the same thing happens in reverse."),
 ("What time will the driver come in Stamford?","Between the rushes. The highway backs up from six to ten and again from three to seven. A Stamford pickup happens mid-morning or early afternoon. The driver names the spot the day before. A weekend pickup is easier still."),
 ("Do you handle relocations to the headquarters in Stamford?","Yes, on start dates all year. The cable company, the finance company, and the funds relocate staff from every state and abroad. Most ship a car rather than drive it. We provide the records a reimbursed move needs."),
 ("Can you ship a collector car or an exotic from Stamford?","Yes, and most of them ride enclosed. The handoff happens at a lot off High Ridge Road or at the dealer, never on the street. Tell us the make, the ground clearance, and whether it runs. A liftgate trailer is booked when the clearance calls for it."),
 ("What happens if a nor’easter hits on my pickup day?","The truck holds until 95 is plowed. A winter pickup can slide a day. Shippan and the Cove wait for the tide to fall after a storm surge. You hear from us the moment the forecast changes the plan."),
 ("Do you ship cars for residents at Stamford Hospital?","Yes, every June and July. Residents arrive from every state, and most bring a car. The handoff happens on Washington Boulevard or at a lot off 95, not in the hospital garage."),
 ("Can you ship a car that does not run from Stamford?","Yes. A winch-equipped truck is assigned, and the slower loading shows up in the quote. The spot has to be flat and open, so a lot by 95 rather than a tower garage. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Stamford car shipping quote?","Both addresses, with the neighborhood and the garage on this end. Year, make, and model, and whether it runs. Open or enclosed. Your dates, with the Florida season in mind. That is a complete Stamford request."),
]
BODY.append(faq_section(FAQ,'Stamford FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Stamford?','Get a price from the form above in about two minutes. Tell us the neighborhood and your dates, and a carrier already running 95 takes it from there.','+14754453917','(475) 445-3917','Get your free Stamford quote'))

build({
 'slug':'auto-transport-stamford-connecticut',
 'title':'Car Shipping in Stamford, CT — Auto Transport | Ship Guy',
 'meta':'Car shipping in Stamford, CT on Interstate 95 and off the Merritt Parkway. Harbor Point garage handoffs, North Stamford estate roads, headquarters and hospital moves, the Palm Beach lane, enclosed collector cars, nor’easter planning. Local office on Summer Street. Free quote.',
 'h1':'Car Shipping in<br>Stamford, <span class="accent">Connecticut</span>',
 'lede':'Open, enclosed, and expedited auto transport across lower Fairfield County, planned around 95, the parkway, and the garages.',
 'tel':'+14754453917','disp':'(475) 445-3917','brand':'Stamford','keyword':'car shipping in stamford',
 'localterms':['stamford','interstate 95','merritt parkway','post road','high ridge','long ridge','washington boulevard','summer street','canal street','tresser','bull’s head','downtown','harbor point','south end','shippan','the cove','glenbrook','springdale','belltown','newfield','turn of river','north stamford','westover','waterside','greenwich','darien','new canaan','norwalk','towers','garage','estate','stone walls','gated','headquarters','cable company','consumer-finance','hedge funds','hospital','residents','express train','grand central','commuters','finance households','palm beach','florida','texas','collector','exotic','enclosed','nor’easters','storm surge','balloon parade','concerts','rush','manhattan','yonkers','hartford','new haven','boston','philadelphia','washington','albany','charlotte','chicago','orlando'],
}, BODY, FAQ)
