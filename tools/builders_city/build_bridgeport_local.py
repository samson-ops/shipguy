import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Bridgeport, Connecticut','Car shipping in the largest city in the state, where Interstate 95 meets Route 8 and the ferry to Long Island',
 ['Car shipping in Bridgeport is the easiest on the Gold Coast, because the city sits on a grid. Ship Guy is a licensed auto transport broker with an office on Golden Hill Street downtown.',
  'We book vetted carriers across the city and its suburbs, from Fairfield and Trumbull to Stratford and Shelton. We do not own the trucks.',
  'Interstate 95 runs through the city along the harbor, with exits 25 through 30. Route 8 and Route 25 leave the interstate downtown. They run north to the Merritt, Trumbull, and the Naugatuck Valley. The Post Road runs across the city as Boston Avenue and Fairfield Avenue.',
  'This page covers the interstate and the connector, the grid and the waterfront, and the suburbs. It also covers the helicopter plant, the hospitals, the universities, the ferry, the storms, and the lanes.'],
 'Bridgeport at a glance',
 ['Most pickups happen within 1 to 3 days. The New York and New England carriers pass the city on 95. Route 8 brings the valley trucks down to meet them.',
  'New Haven, Stamford, and Hartford are same-day lanes, and so are Manhattan and Boston. Philadelphia and Albany need a day, and Florida needs three.'],
 'Tell us the neighborhood. Black Rock, the East Side, and the blocks of three-family houses need a meeting spot. The North End, Trumbull, and Fairfield usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 95, Route 8 and 25, the Post Road, and the Ferry',
 prose(
  L('Bridgeport is where the shoreline interstate and the valley highway meet, and the carriers use both.'),
  P('Interstate 95 runs through the city between the harbor and downtown. Exits 25 through 30 carry Bridgeport, and the Route 8 and 25 connector leaves at exit 27A. The stretch west toward Fairfield backs up every weekday, and the stretch east toward New Haven moves better.'),
  P('Route 8 and Route 25 run together north from downtown to the Merritt Parkway, then split. Route 25 continues to Trumbull and Newtown. Route 8 runs up the Naugatuck Valley through Shelton to Waterbury. Both are built for trucks, which the Merritt is not.'),
  P('The ferry to Port Jefferson leaves from the harbor downtown. A car headed to Long Island can ride it with you. Or the carrier takes it through the city. We quote both ways. The carriers come off 95 at Lafayette, Main Street, and Seaview Avenue.'),
  P('The lots at Steelpointe by exit 29 and along Boston Avenue are the usual meeting spots. Our office sits on Golden Hill Street downtown, two blocks from the 95 and Route 8 interchange.'),
 ), alt=True))

BODY.append(sec('The Grid &amp; the Shore','Black Rock, the East Side, the North End, Stratford, and the Suburbs',
 prose(
  L('Bridgeport is a working grid with a waterfront on three sides, and the handoff depends on the block.'),
  P('Black Rock sits on the harbor with narrow streets, a seawall, and flooding in a storm. The East Side and the East End are tight grids of three-family houses with cars on both curbs. The driver meets you on Fairfield Avenue, on Boston Avenue, or at Steelpointe.'),
  P('Downtown has towers, garages, and one-way streets around the arena. The garage pulls the car out, and the driver meets you at a lot on Lafayette Boulevard. The Hollow and the West Side are the same tight grid as the East Side.'),
  P('The North End is wider. Brooklawn, Lake Forest, and the streets off Madison Avenue usually allow the truck at the curb. Trumbull and Fairfield are suburban grids with driveways. The mall lot in Trumbull is the backup for both.'),
  P('Stratford holds the helicopter plant and the airport along the river. Shelton holds the corporate parks up Route 8. A handoff at a plant gate or an office lot works when the employer allows it.'),
 )))

ROUTES=[("New Haven, CT","I-95 · ~20 mi","Same day","$100–$170"),("Stamford, CT","I-95 · ~25 mi","Same day","$110–$190"),
 ("Manhattan, NY","I-95 · ~60 mi","Same day","$150–$250"),("Hartford, CT","CT-8/I-84 · ~60 mi","Same day","$150–$250"),
 ("Boston, MA","I-95/I-90 · ~160 mi","Same day","$220–$340"),("Philadelphia, PA","I-95 · ~150 mi","1 day","$210–$330"),
 ("Washington, DC","I-95 · ~280 mi","1 day","$270–$400"),("Charlotte, NC","I-95/I-85 · ~680 mi","2 days","$500–$720"),
 ("Orlando, FL","I-95 · ~1,140 mi","3 days","$780–$1,100"),("Miami, FL","I-95 · ~1,330 mi","3–4 days","$820–$1,170")]
BODY.append(rate_table('Lanes &amp; Costs','Bridgeport Car Shipping Lanes and Estimated Costs',
 'Where Bridgeport cars go, from the next exit to the bottom of Interstate 95, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a sedan that runs on an open trailer. An SUV or pickup costs 10 to 25 percent more, and enclosed costs more than that. The season, the 95 traffic, and the carriers free on your dates fix the final figure.',
 prose(
  P('Bridgeport prices like New Haven, because the two cities share twenty miles of 95 and the same trucks. Manhattan rides 95 south, Boston rides 95 north, and Hartford rides Route 8 and 84.'),
  P('The Florida lane runs full from October into December, and the Carolinas lane fills with relocations all year. The <a href="car-shipping-cost.html">cost guide</a> takes the number apart.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Helicopter Plant, the Hospitals, the Universities, and the Ferry',
 prose(
  L('Bridgeport relocates people on the program schedule, the residency match, the semester, and the Florida season.'),
  P('The helicopter plant in Stratford relocates engineers and technicians on program schedules, and they arrive from every state. The corporate parks in Shelton and the port hire on start dates. When an employer reimburses the move, we send the records it wants.'),
  P('Residents and nurses arrive at the two hospitals every June and July. Most come from out of state with a car. The handoff happens on Grant Street or Main Street rather than in a hospital garage.'),
  P('The two universities in Fairfield and the state university downtown fill with cars each August. They empty each May. The campus lots in Fairfield work for the handoff. An adult signs for a student car.'),
  P('Families move up from the city and down from the suburbs all year. Retirees leave for Florida and the Carolinas each fall. Our <a href="snowbird-car-shipping.html">snowbird</a> page covers the planning. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
  P('A car bound for Long Island can ride the ferry with you from the harbor. The carrier handles the rest of the trip on either end, and we quote it both ways.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Nor’easters, the Seawall, the Festivals, and the 95 Rush',
 prose(
  L('Bridgeport gets the Sound’s weather and the corridor’s traffic, and it plans for both.'),
  P('Nor’easters close 95 for a morning a few times each winter, and the carriers wait for the plows. Black Rock, the South End, and Seaside Park flood in a storm surge. A pickup there waits for the tide to fall and moves to Fairfield Avenue.'),
  P('The music festival fills Seaside Park for a weekend each September. The Barnum parade closes downtown in June. The arena brings game and concert traffic to downtown on weeknights. We move a pickup near any of them to another day.'),
  P('Interstate 95 backs up through both rushes, and the Fairfield stretch is the worst of it. A Bridgeport pickup happens between the rushes. The driver names the spot the day before.'),
  P('In summer the loading moves earlier in the day. Seaside Park traffic fills the South End on weekends. Wind off the Sound slows a trailer on the 95 bridges now and then.'),
 )+chips(["Downtown","Steelpointe","Black Rock","South End","West End","West Side","The Hollow","East Side","East End","Mill Hill","North End","Brooklawn","Lake Forest","Whiskey Hill","Seaside Park","Pleasure Beach","Boston Avenue","Fairfield Avenue","Madison Avenue","Fairfield","Trumbull","Stratford","Shelton","Monroe","Easton","Milford"])
 +NOTE('Serving Bridgeport, Fairfield, Trumbull, Stratford, and Shelton. Tell us the block, the garage, and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Bridgeport?',
 prose(
  L('Open is how Bridgeport ships, and the 95 lanes are priced for it.'),
  P('An enclosed trailer keeps salt and road grime off the car and keeps it out of sight. The garages in Brooklawn, Fairfield, and Easton book enclosed trailers. So does a car headed to Florida for the winter.'),
  P('A commuter car rides open and arrives the way it left. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages weigh the two choices.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff at Steelpointe or on a wide avenue, and a delivery. The rush decides the hour.'),
  P('Approve the price, and a carrier already on 95 or Route 8 takes the booking. We set the spot the same day. The driver and you go over the car and note it all on a Bill of Lading. Both sign, and that sheet governs the delivery check.'),
 )+ULI([
  "Pull anything personal out of the car",
  "Fuel at about a quarter tank",
  "Take photos of the car on pickup morning",
  "Leave a working key and describe any mechanical issue",
  "Kill the aftermarket alarm if it has one",
  "On a three-family block, plan to meet the truck on the avenue",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through the rest.'))))

BODY.append(sec('Why Ship Guy','Why Bridgeport Drivers Choose Ship Guy',
 prose(
  L('We work 95 and Route 8 every day. We plan around the rush, the tide, and the Florida season.'),
  P('Ship Guy is licensed as a broker by the FMCSA, with a $75,000 surety bond on file. Both are a matter of public record. Our office is on Golden Hill Street downtown.'),
  P('A single coordinator owns the booking from quote to delivery. Open, enclosed, and expedited transport are all bookable here, and the <a href="services.html">services</a> page describes each.'),
 ), alt=True))

BODY.append(office('Bridgeport','144 Golden Hill St Ste 731','Bridgeport, CT 06604','+14752605825','(475) 260-5825','ET',
 '144+Golden+Hill+St+Ste+731,+Bridgeport,+CT+06604','Visit Us','Find Ship Guy in Bridgeport',
 'Our office is on Golden Hill Street downtown, two blocks from the Interstate 95 and Route 8 interchange.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4617.727744403581!2d-73.1901589!3d41.180532799999995!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89e80f75725d2c05%3A0xfbd9003f09b11d04!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792153195319!5m2!1sen!2sus'))

FAQ=[
 ("Can the carrier come to my street in Bridgeport?","In the North End, Trumbull, and Fairfield, usually. On the East Side, in Black Rock, and on the three-family blocks, the streets are too tight. The driver meets you on Boston Avenue, Fairfield Avenue, or at the Steelpointe lots by exit 29. It is a few minutes from the house."),
 ("How much does it cost to ship a car from Bridgeport to Florida?","Orlando runs seven hundred eighty to eleven hundred dollars for a sedan. That is about eleven hundred forty miles down Interstate 95. Miami runs eight hundred twenty to eleven hundred seventy. The fall rush costs more than the spring return. Larger vehicles add 10 to 25 percent."),
 ("Can you ship a car to Long Island from Bridgeport?","Yes, two ways. The carrier can take it through the city and over the bridges, with the tolls built in. Or the car rides the Port Jefferson ferry with you. A carrier meets it on the other side. We quote both, and the ferry usually wins for the North Shore."),
 ("Do you ship cars for engineers hired at the helicopter plant?","Yes, on program schedules all year. New engineers and technicians arrive from every state, and most ship a car rather than drive it. The handoff happens at a lot by the plant on Main Street in Stratford or at Steelpointe. We provide the records a reimbursed move needs."),
 ("Can you ship a car for a Fairfield University or Sacred Heart student?","Yes. The cars come in each August and leave each May. The campus lots in Fairfield work for the handoff, and the Post Road is the backup. An adult signs for the car at pickup."),
 ("What happens if a nor’easter or a storm surge hits on my pickup day?","The carriers sit out the storm and run 95 once the plows are through. Black Rock, the South End, and Seaside Park wait for the tide to fall. A winter pickup can slide a day, and we call before it does."),
 ("Is Bridgeport priced like Stamford or like New Haven?","Like New Haven, and a little under Stamford. Bridgeport and New Haven share twenty miles of 95 and the same trucks. Route 8 adds the valley carriers. A truck headed either way can take the car."),
 ("Do you ship cars for residents at Bridgeport Hospital or St. Vincent’s?","Yes, every June and July. The two hospitals bring in residents and nurses from every state, and most of them bring a car. The handoff happens on Grant Street or Main Street, not in a hospital garage."),
 ("Can you ship a car that does not run from Bridgeport?","Yes. The truck we send carries a winch, and the slower loading is priced in. The spot has to be flat and open, which here means Steelpointe or a lot on Boston Avenue. Say whether it rolls, steers, and brakes."),
 ("What do you need for a Bridgeport car shipping quote?","Both addresses, with the block on the Bridgeport end. The year, make, and model. Does it run. Open or enclosed, and your dates. That is a complete Bridgeport request."),
]
BODY.append(faq_section(FAQ,'Bridgeport FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Bridgeport?','Run the form above for a price in about two minutes. Tell us the block and your dates. A carrier already on 95 or Route 8 takes it from there.','+14752605825','(475) 260-5825','Get your free Bridgeport quote'))

build({
 'slug':'auto-transport-bridgeport-connecticut',
 'title':'Car Shipping in Bridgeport, CT — Auto Transport | Ship Guy',
 'meta':'Car shipping in Bridgeport, CT where Interstate 95 meets Route 8. Steelpointe and Boston Avenue meeting spots, Black Rock and East Side blocks, North End and Trumbull curbside, Sikorsky-plant and hospital relocations, the Long Island ferry option, the Florida lane, nor’easter planning. Local office on Golden Hill Street. Free quote.',
 'h1':'Car Shipping in<br>Bridgeport, <span class="accent">Connecticut</span>',
 'lede':'Open, enclosed, and expedited auto transport across Bridgeport and its suburbs, planned around 95, Route 8, and the tide.',
 'tel':'+14752605825','disp':'(475) 260-5825','brand':'Bridgeport','keyword':'car shipping in bridgeport',
 'localterms':['bridgeport','interstate 95','route 8','route 25','connector','merritt parkway','post road','boston avenue','fairfield avenue','madison avenue','lafayette','main street','seaview avenue','grant street','golden hill','steelpointe','downtown','arena','black rock','south end','west end','west side','the hollow','east side','east end','mill hill','north end','brooklawn','lake forest','seaside park','pleasure beach','three-family','garage','fairfield','trumbull','stratford','shelton','monroe','easton','milford','helicopter plant','corporate parks','port','hospitals','residents','universities','state university','ferry','port jefferson','long island','snowbird','florida','carolinas','nor’easters','storm surge','seawall','music festival','barnum','rush','new haven','stamford','manhattan','hartford','boston','philadelphia','washington','charlotte','orlando','miami','albany'],
}, BODY, FAQ)
