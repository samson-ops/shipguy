import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Yonkers, New York','Car shipping for the city of seven hills, where only one highway lets a truck in',
 ['Car shipping in Yonkers comes down to one road, because the parkways and the hills exclude the others. Ship Guy is a licensed auto transport broker with an office on South Broadway downtown.',
  'We book vetted carriers across southern Westchester, from the Bronx line to Hastings and east to Eastchester. We do not own the trucks.',
  'Interstate 87 is the Thruway here. It is the only highway through the city a carrier can use. The Saw Mill, the Sprain, the Cross County, and the Bronx River are parkways with low stone bridges. The handoff happens near a Thruway exit or on Central Park Avenue.',
  'This page covers the Thruway and the parkways, the hills, and the meeting spots by neighborhood. It also covers the commuters, the hospitals, the Florida lane, and the lanes down the corridor.'],
 'Yonkers at a glance',
 ['Most pickups happen within 1 to 3 days. The Thruway and Interstate 95 bring carriers past the city all day.',
  'Philadelphia, Hartford, and Boston are same-day lanes. Washington and Albany take a day. Florida runs three, and the West Coast runs seven to nine.'],
 'Tell us the neighborhood. The hills downtown and in Nodine Hill need a flat meeting spot. Crestwood, Colonial Heights, and the east side usually meet the truck on a main road.'))

BODY.append(sec('The Roads','The Thruway, the Parkways, and the Hills',
 prose(
  L('Westchester built its parkways with stone arches too low for a truck. Yonkers sits in the middle of them.'),
  P('Interstate 87 runs up the east side of the city, from the Major Deegan toward the Tappan Zee. The Yonkers Avenue, Tuckahoe Road, and Cross County exits are where carriers come off. The toll barrier sits just north of the city.'),
  P('The Saw Mill River Parkway, the Sprain Brook, the Bronx River, and the Cross County prohibit commercial vehicles. So does the Hutchinson. A loaded carrier that tries one meets a bridge it cannot fit under.'),
  P('Central Park Avenue, Yonkers Avenue, Tuckahoe Road, and Route 9 are the surface roads a trailer can use. Interstate 95 and Interstate 287 sit a few miles east. They connect to New England and the Tappan Zee.'),
  P('The hills are the other problem. Getty Square, Nodine Hill, and Park Hill climb grades a loaded trailer cannot stop on. The driver meets you on the flat.'),
  P('The Thruway toll and the bridge tolls are paid by the carrier and built into every quote.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the Hills, Crestwood, and the Bronxville Line',
 prose(
  L('Yonkers has riverfront towers, hillside two-families, and Tudor streets on the east side. The meeting spot depends on which one you live in.'),
  P('Downtown and the riverfront run on garages and steep one-way streets. The driver meets you on South Broadway near the station, on Nepperhan Avenue, or by the Thruway. Our office sits on South Broadway a few blocks from Getty Square.'),
  P('Nodine Hill, Park Hill, and Ludlow are hillside blocks of two-families with cars on both curbs. The handoff happens on Yonkers Avenue, McLean Avenue, or Riverdale Avenue on the flat.'),
  P('Crestwood, Colonial Heights, Lincoln Park, and Cedar Knolls are the east side, with winding streets and low trees. The truck meets you on Central Park Avenue, Tuckahoe Road, or at the Cross County Center lot.'),
  P('Bronxville, Tuckahoe, and Eastchester sit next door with village streets that ban trucks. Hastings and Dobbs Ferry on the river meet the truck on Route 9. Mount Vernon and the Riverdale side of the Bronx use the Deegan exits.'),
 )))

ROUTES=[("Hartford, CT","I-95/I-91 · ~100 mi","Same day","$190–$300"),("Philadelphia, PA","I-95 · ~115 mi","Same day","$200–$320"),
 ("Albany, NY","I-87 · ~140 mi","Same day","$210–$330"),("Boston, MA","I-95/I-90 · ~195 mi","Same day","$240–$360"),
 ("Washington, DC","I-95 · ~245 mi","1 day","$260–$380"),("Buffalo, NY","I-87/I-90 · ~390 mi","1 day","$380–$540"),
 ("Charlotte, NC","I-95/I-85 · ~650 mi","2 days","$480–$690"),("Chicago, IL","I-80 · ~800 mi","2 days","$570–$830"),
 ("Orlando, FL","I-95 · ~1,110 mi","3 days","$770–$1,090"),("Miami, FL","I-95 · ~1,300 mi","3–4 days","$810–$1,160")]
BODY.append(rate_table('Lanes &amp; Costs','Yonkers Car Shipping Lanes and Estimated Costs',
 'The lanes Yonkers and southern Westchester households ask about most, with estimated open-transport ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates, running sedan, open trailer. SUVs and pickups add roughly 10 to 25 percent, and enclosed adds more. Thruway and bridge tolls are included. Season and carrier availability on your dates set the real quote.',
 prose(
  P('The Interstate 95 corridor is the busiest freight lane in the country, and Yonkers sits on it. Philadelphia, Hartford, and Boston price like local trips because the trucks never stop coming.'),
  P('Florida prices by the calendar more than the mileage. The <a href="car-shipping-cost.html">cost guide</a> explains the rest of the number.'),
 ), alt=True))

BODY.append(sec('The Florida Lane','Westchester to Boca, Palm Beach, and Naples',
 prose(
  L('Southern Westchester sends a wave of cars down Interstate 95 every October. The hills empty out for the winter.'),
  P('Crestwood, Colonial Heights, and Bronxville ship their cars to Boca Raton, Palm Beach, and Naples each fall. The cars come back home in the spring.'),
  P('The lane is so busy that it stays easy to book even at the peak. Two to three weeks of notice holds the price, and the spring return is the cheaper direction. Our <a href="snowbird-car-shipping.html">snowbird</a> page has the planning tips.'),
 )))

BODY.append(sec('Who Moves Here','Commuters, the Hospitals, the Colleges, and the Corporate Campuses',
 prose(
  L('Yonkers relocates on Metro-North schedules, hospital start dates, and the corporate campuses up the county.'),
  P('Households moving in for a Manhattan job land in Yonkers for the train. The Hudson Line and the Harlem Line both run through the city. Many of those households ship a car from Florida, Texas, or California rather than drive it.'),
  P('The two hospitals in the city and the medical center in Valhalla hire clinicians on start dates. The handoff happens on Broadway or Yonkers Avenue rather than in a hospital garage.'),
  P('The biotech campus in Tarrytown and the corporate campuses in Purchase and Armonk transfer staff year round. If your employer reimburses the shipment, we send the documentation it asks for.'),
  P('The college on the Bronxville line and the campuses in Riverdale and New Rochelle add student cars. An adult signs for a student car. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the longer move.'),
 ), alt=True))

BODY.append(sec('The Weather','Ice on the Hills, Nor’easters, and the Saw Mill Floods',
 prose(
  L('Yonkers weather is ordinary until it lands on a hill.'),
  P('Nor’easters hit a few times each winter and close the corridor for a day. Ice is the bigger problem, because the hillside streets become impassable long before the main roads do. The driver waits on the flat, and a pickup can slide a day.'),
  P('Heavy summer rain floods the Saw Mill River Parkway and the low blocks along Nepperhan Avenue. The surface roads a trailer uses stay open, and we reroute the handoff when the river is up.'),
  P('Road salt runs all winter, and collector-car owners ride enclosed for that reason. Summer heat on the Thruway is the easy season.'),
 )+chips(["Downtown","Getty Square","Riverfront","Nodine Hill","Park Hill","Ludlow","Lincoln Park","Bryn Mawr","Homefield","Crestwood","Colonial Heights","Cedar Knolls","Dunwoodie","Lawrence Park West","Northeast Yonkers","Ridge Hill","Cross County","McLean Avenue","Bronxville","Tuckahoe","Eastchester","Scarsdale","Hastings-on-Hudson","Dobbs Ferry","Mount Vernon","New Rochelle","Riverdale"])
 +NOTE('Serving Yonkers and southern Westchester. Tell us the neighborhood and whether the street is on a hill.')))

BODY.append(sec('Your Options','Open or Enclosed in Yonkers?',
 prose(
  L('Open transport carries most of Yonkers, and the Interstate 95 corridor runs on it every day.'),
  P('Enclosed transport keeps a car covered against road salt, grit, and attention. The garages in Lawrence Park West and Bronxville book enclosed trailers. Many Palm Beach-bound cars do too.'),
  P('A commuter car rides open without trouble. Our <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages lay out each option.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a short drive to a flat meeting spot, and a delivery. The parkways and the hills decide the spot.'),
  P('Once you approve the price, a carrier already running the corridor takes the booking. We name the meeting spot before the driver is dispatched. There, the driver records the car’s condition on a Bill of Lading and you both sign.'),
 )+ULI([
  "Remove personal belongings",
  "Keep about a quarter tank of fuel",
  "Photograph the vehicle before pickup, especially after a salty winter",
  "Provide a working key and disclose mechanical issues",
  "Disable aftermarket alarms",
  "On a hillside street, plan to meet the truck on Yonkers Avenue, Central Park Avenue, or Route 9",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> guides take it step by step.'))))

BODY.append(sec('Why Ship Guy','Why Yonkers Drivers Choose Ship Guy',
 prose(
  L('We know which Westchester roads ban the truck and which hills stop it. The spot is named before you wait on a corner.'),
  P('Active FMCSA brokerage authority and a $75,000 surety bond stand behind every booking we make. Our office is on South Broadway downtown.'),
  P('One coordinator carries your shipment from quote to delivery and can book open, enclosed, or expedited transport. The <a href="services.html">services</a> page shows the full lineup.'),
 ), alt=True))

BODY.append(office('Yonkers','30 S Broadway #1210','Yonkers, NY 10701','+19147433643','(914) 743-3643','ET',
 '30+S+Broadway+%231210,+Yonkers,+NY+10701','Visit Us','Find Ship Guy in Yonkers',
 'Our office is on South Broadway downtown, a few blocks from Getty Square and the Yonkers train station.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5098.265116987244!2d-73.8986429!3d40.932915699999995!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c2f32ed325a485%3A0x4dcc02cd68ae3997!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792023099681!5m2!1sen!2sus'))

FAQ=[
 ("Can the carrier come to my house in Yonkers?","On a flat, wide street on the east side, sometimes. Downtown, in Nodine Hill, or in Park Hill, no. The grades are too steep to stop a loaded trailer. The parkways keep it off the fast roads. The driver meets you on Yonkers Avenue, Central Park Avenue, or Route 9."),
 ("Which highways can a car carrier use in Westchester?","Interstate 87, Interstate 95, and Interstate 287, plus the surface roads. The Saw Mill, the Sprain, the Bronx River, the Hutchinson, and the Cross County ban commercial vehicles. That is why the meeting spot sits near a Thruway exit."),
 ("How much does it cost to ship a car from Yonkers to Florida?","Plan on seven hundred seventy to one thousand ninety dollars for a sedan to Orlando. Miami adds a little. The trip covers about eleven hundred miles of Interstate 95. Fall southbound prices run above spring. SUVs and pickups add 10 to 25 percent."),
 ("Are the Thruway and bridge tolls added to my price?","No. The carrier pays the Thruway barrier, the Tappan Zee, and the Hudson crossings, then prices the trip. The number you approve already includes them."),
 ("Do you serve Bronxville, Tuckahoe, and Scarsdale?","Yes. The village streets ban trucks. The driver meets you on Central Park Avenue, at the Cross County Center, or at the village edge. The price is the same as a Yonkers pickup."),
 ("What happens if it snows or ices on my pickup day?","The driver waits on the flat until the hills are passable. A nor’easter can close the corridor for a day. Ice on the hillside streets lasts longer than the storm. We plan winter handoffs on the main roads from the start."),
 ("Can you ship a car for a commuter moving to Yonkers for the train?","Yes, every week. Households moving in for a Manhattan job often ship a car from Florida or California instead of driving. The handoff happens near the station on South Broadway or by the Thruway. An adult signs the form."),
 ("Can you ship a car for a Sarah Lawrence, Manhattan College, or Iona student?","Yes. Student cars arrive each August and leave each May. The campus streets are tight, so the driver meets you on a main road nearby. An adult signs for the car at pickup, and a parent can sign at the far end."),
 ("Can you ship a car that does not run from Yonkers?","Yes. A carrier with a winch takes a car that will not start, with the loading time priced in. The meeting spot has to be flat, which matters more here than anywhere. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Yonkers car shipping quote?","The pickup and delivery addresses, with the neighborhood and whether the street is on a hill. The year, make, and model. Whether it runs. Open or enclosed, and your dates. That is everything an accurate Yonkers quote needs."),
]
BODY.append(faq_section(FAQ,'Yonkers FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Yonkers?','Price the route on the form above in about two minutes. Tell us the neighborhood and your dates. We will name a flat meeting spot before the truck is dispatched.','+19147433643','(914) 743-3643','Get your free Yonkers quote'))

build({
 'slug':'auto-transport-yonkers-new-york',
 'title':'Car Shipping in Yonkers, NY — Auto Transport | Ship Guy',
 'meta':'Car shipping in Yonkers, NY on the Thruway, around the parkways that ban trucks. Flat meeting spots for the hills, Crestwood and Getty Square handoffs, Bronxville and Scarsdale pickups, the Florida snowbird lane, tolls built in. Local office on South Broadway. Free quote.',
 'h1':'Car Shipping in<br>Yonkers, <span class="accent">New York</span>',
 'lede':'Open, enclosed, and expedited auto transport across southern Westchester, planned around the parkways, the hills, and the season.',
 'tel':'+19147433643','disp':'(914) 743-3643','brand':'Yonkers','keyword':'car shipping in yonkers',
 'localterms':['yonkers','interstate 87','thruway','major deegan','tappan zee','saw mill','sprain','bronx river','cross county','hutchinson','interstate 95','interstate 287','central park avenue','yonkers avenue','tuckahoe road','route 9','south broadway','nepperhan','mclean','getty square','riverfront','nodine hill','park hill','ludlow','crestwood','colonial heights','lincoln park','cedar knolls','lawrence park','ridge hill','cross county center','bronxville','tuckahoe','eastchester','scarsdale','hastings','dobbs ferry','mount vernon','new rochelle','riverdale','metro-north','hudson line','harlem line','hospitals','valhalla','tarrytown','purchase','armonk','sarah lawrence','hills','ice','nor','florida','boca raton','palm beach','naples','philadelphia','hartford','boston','albany','washington'],
}, BODY, FAQ)
