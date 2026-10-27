import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Albany, New York','Car shipping for the capital, where the Thruway, the Northway, and the Boston lane meet',
 ['Car shipping in Albany starts at the interchange where three of the busiest roads in the Northeast meet. Ship Guy is a licensed auto transport broker with an office on Washington Avenue near the Capitol.',
  'We book vetted carriers across the Capital District, from Colonie and Guilderland to Troy, Schenectady, and Clifton Park. We do not own the trucks.',
  'The Thruway carries Interstate 87 up from the city and Interstate 90 in from Buffalo. The Northway continues 87 to Saratoga and the Adirondacks. Free Interstate 90 runs east to the Massachusetts line and Boston.',
  'This page covers the interchange and the Northway, the state workforce, the medical center, and the neighborhoods. It also covers the chip plant in Malta, the Saratoga season, the winter, and the lanes.'],
 'Albany at a glance',
 ['Most pickups happen within 1 to 3 days. The Thruway and the Boston lane bring carriers through the interchange all day.',
  'New York City, Boston, Hartford, and Syracuse are same-day lanes. Buffalo, Philadelphia, and Washington take a day. Florida runs three.'],
 'Tell us the neighborhood. Center Square, Pine Hills, and downtown Troy need a meeting spot. Colonie, Clifton Park, and Delmar usually meet the truck at the curb.'))

BODY.append(sec('The Roads','The Thruway, the Northway, Interstate 90 East, and 787',
 prose(
  L('Albany is the one place where the New York, Boston, and Montreal lanes all touch. The carriers never stop coming.'),
  P('The Thruway arrives from New York City as Interstate 87 and from Buffalo as Interstate 90. The two meet at the Albany interchange with a toll by the mile on both. From there, free Interstate 90 runs east past Rensselaer to the Berkshires and Boston.'),
  P('The Northway carries Interstate 87 north through Colonie and Clifton Park to Saratoga and the Canadian line. The Twin Bridges over the Mohawk carry all of it. Interstate 787 runs the riverfront from the Thruway through downtown to Troy and Cohoes.'),
  P('Interstate 88 heads southwest to Binghamton. Route 7 crosses to Troy and Schenectady. Central Avenue and Western Avenue are the surface roads carriers use across the city. Wolf Road is the retail strip by the airport.'),
  P('Carriers pay the Thruway and quote with it included. The Northway, 787, 88, and Interstate 90 east of the interchange cost nothing.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The State Workforce, the Medical Center, the Chip Plant, and the Campuses',
 prose(
  L('Albany relocates people on the legislative calendar, the residency calendar, and the hiring at the chip plant.'),
  P('State government is the largest employer in the region. The agencies at the plaza and on the Harriman campus hire on start dates all year. The session runs January through June, and the downtown garages fill while it sits.'),
  P('The medical center on New Scotland Avenue brings in residents every June and July. Most come from out of state with a car. The handoff happens on Madison Avenue or at a lot nearby rather than in a hospital garage.'),
  P('The chip plant in Malta hires engineers from across the country. The biotech plant in Rensselaer does the same. The university on Washington Avenue and the engineering school in Troy bring cars in each August. The colleges in Loudonville and Schenectady do the same. All of them send the cars home in May.'),
  P('If your employer reimburses the shipment, we send the documentation it asks for. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the longer relocation.'),
 )))

ROUTES=[("Hartford, CT","I-90/I-91 · ~110 mi","Same day","$190–$300"),("Syracuse, NY","I-90 · ~145 mi","Same day","$190–$300"),
 ("New York, NY","I-87 · ~150 mi","Same day","$220–$340"),("Boston, MA","I-90 · ~170 mi","Same day","$220–$340"),
 ("Philadelphia, PA","I-87/I-287/I-95 · ~240 mi","1 day","$250–$370"),("Buffalo, NY","I-90 · ~290 mi","1 day","$270–$400"),
 ("Washington, DC","I-87/I-95 · ~370 mi","1 day","$340–$490"),("Cleveland, OH","I-90 · ~470 mi","1 day","$420–$600"),
 ("Chicago, IL","I-90 · ~800 mi","2 days","$570–$830"),("Orlando, FL","I-87/I-95 · ~1,200 mi","3 days","$820–$1,150")]
BODY.append(rate_table('Lanes &amp; Costs','Albany Car Shipping Lanes and Estimated Costs',
 'The lanes that leave the Capital District most often, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a running sedan, open trailer, Thruway tolls included. An SUV or pickup adds about 10 to 25 percent, and enclosed adds more again. Winter weather and the carriers available on your dates set the final price.',
 prose(
  P('New York City and Boston are both under three hours away. Both price like local trips because the trucks never stop. Hartford and Syracuse run the same day too.'),
  P('The Florida lane leaves on the Thruway and joins Interstate 95 below the city. The <a href="car-shipping-cost.html">cost guide</a> explains the rest of the number.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Center Square, Pine Hills, Delmar, Colonie, Troy, and Schenectady',
 prose(
  L('Albany is brownstone blocks downtown and wide suburbs everywhere else, and the meeting spot follows the block.'),
  P('Center Square, the Mansion District, and the blocks around the Capitol are rowhouses with no driveways. Cars park on both curbs. The driver meets you on Washington Avenue, Madison Avenue, or a lot by the plaza. Our office sits on Washington Avenue a few blocks from the Capitol.'),
  P('Pine Hills, the student blocks, and Delaware Avenue are two-families with narrow driveways. The handoff happens on Western Avenue, Madison, or near the university lots.'),
  P('Colonie, Guilderland, Latham, and Clifton Park are wide grids where the truck usually reaches the curb. Delmar, Slingerlands, and Glenmont in Bethlehem are the same. The mall in Guilderland and the Wolf Road lots are the usual meeting spots.'),
  P('Troy and Schenectady have tight downtowns and hillside streets. The driver meets you on Hoosick Street, on Erie Boulevard, or by the river. Saratoga Springs runs on its own calendar from July through Labor Day.'),
 )))

BODY.append(sec('The Season &amp; the Weather','Saratoga Summer, Tulip Week, Nor’easters, and Ice',
 prose(
  L('Albany’s busiest road closures come from a racetrack and a flower festival. Its hardest days come from ice.'),
  P('The track in Saratoga runs from July through Labor Day, and the Northway crawls on race days. Clifton Park and Saratoga pickups move to the morning or to another day. The tulip festival fills Washington Park in May, and downtown pickups work around it.'),
  P('Nor’easters close the Thruway for a day a few times each winter. Ice is the bigger problem on the hills in Troy and the river valley. The carriers wait for the sand trucks, and a pickup can slide a day.'),
  P('Salt is on the roads from November through April, which is why collector cars go enclosed. Spring floods on the Mohawk close the low roads in Schenectady and Cohoes for a day or two.'),
 )+chips(["Downtown","Center Square","Mansion District","Pine Hills","Delaware Avenue","Whitehall","North Albany","South End","Buckingham Pond","Colonie","Latham","Loudonville","Guilderland","Delmar","Slingerlands","Glenmont","East Greenbush","Rensselaer","Troy","Cohoes","Watervliet","Schenectady","Niskayuna","Clifton Park","Malta","Ballston Spa","Saratoga Springs"])
 +NOTE('Serving Albany, Rensselaer, Schenectady, and Saratoga Counties. Tell us the neighborhood and whether the car runs.'), alt=True))

BODY.append(sec('Military','Watervliet, Stratton, and the Second Vehicle',
 prose(
  L('The Capital District moves families through an arsenal, an airlift wing, and the orders headed up the Northway.'),
  P('The arsenal in Watervliet and the airlift wing in Scotia rotate families on orders. Fort Drum is three hours north on the Thruway and Interstate 81. Many families stage a move through Albany.'),
  P('Orders usually pay to move one vehicle, so the second car rides with us. Housing is gated, and the driver meets you outside. Ship Guy is a private broker with no connection to any post. Our <a href="military-car-shipping.html">military</a> page covers the timing.'),
 )))

BODY.append(sec('Your Options','Open or Enclosed in Albany?',
 prose(
  L('Most Capital District cars ride open, and the Thruway lanes are built around it.'),
  P('An enclosed trailer keeps salt, grit, and attention off the car. The garages in Loudonville and Saratoga book enclosed trailers. The horse-country households ship their cars the same way.'),
  P('A commuter car is fine in the open. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain the difference.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a loading near the interchange, and a delivery. Ice decides the timing in winter.'),
  P('Once you approve the price, a carrier already running the Thruway takes the booking. At the meeting spot you and the driver walk around the car and fill in the form. Both sign. At delivery, the car is checked against that sheet.'),
 )+ULI([
  "Remove personal belongings",
  "Keep about a quarter tank of fuel",
  "Photograph the vehicle before pickup, especially after a salty winter",
  "Provide a working key and disclose mechanical issues",
  "Disable aftermarket alarms",
  "In Center Square or downtown Troy, plan to meet the truck on a main road",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages cover the rest.'))))

BODY.append(sec('Why Ship Guy','Why Albany Drivers Choose Ship Guy',
 prose(
  L('We work the Thruway interchange every day and plan around the session, the track, and the ice.'),
  P('Every booking is backed by active FMCSA brokerage authority and a $75,000 surety bond. Our office is on Washington Avenue near the Capitol.'),
  P('The same coordinator stays with your shipment from quote to delivery. Open, enclosed, and expedited transport are all available. The <a href="services.html">services</a> page covers the whole range.'),
 ), alt=True))

BODY.append(office('Albany','111 Washington Ave #259','Albany, NY 12210','+15189902826','(518) 990-2826','ET',
 '111+Washington+Ave+%23259,+Albany,+NY+12210','Visit Us','Find Ship Guy in Albany',
 'Our office is on Washington Avenue a few blocks from the Capitol, minutes from Interstate 787.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4963.075247735147!2d-73.7596911!3d42.655224600000004!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89de0b84d1412db1%3A0xb5ed5f3048ec7be7!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792023016714!5m2!1sen!2sus'))

FAQ=[
 ("How much does it cost to ship a car from Albany to New York City or Boston?","A sedan usually runs two hundred twenty to three hundred forty dollars to either one. Both sit under three hours away on roads carriers run all day. The downstate handoff happens at a meeting spot rather than a doorstep. Larger vehicles add 10 to 25 percent."),
 ("Are the Thruway tolls added to my price?","No. Thruway mileage is paid by the carrier and already counted in the price you approve. The Northway, 787, 88, and Interstate 90 east of the interchange charge nothing."),
 ("Can the carrier come to my house in Center Square or Pine Hills?","Rarely. The rowhouse blocks have no driveways and parking on both curbs, and the student streets are narrow. The driver meets you on Washington, Madison, or Western Avenue, or at a lot by the plaza. Colonie, Delmar, and Clifton Park usually allow curbside."),
 ("Do you ship cars for residents at the medical center?","Yes, every June and July. The medical center brings in residents from every state, most with a car and two weeks of notice. The handoff happens on Madison Avenue or at a lot nearby rather than in a hospital garage."),
 ("Does the Saratoga racing season affect pickups?","Up the Northway, yes. Race days fill the Northway and the streets around the track from July through Labor Day. We schedule Saratoga and Clifton Park pickups for the morning or for another day. Albany itself runs normally."),
 ("Can you ship a car for a UAlbany, RPI, Siena, or Union student?","Yes. Student cars arrive each August and leave each May. The campus streets are tight, so the driver meets you at a lot nearby. In Troy, that means Hoosick Street or by the river. An adult signs for the car at pickup."),
 ("Do you handle a move to Watervliet, Stratton, or Fort Drum from Albany?","Yes. Orders usually pay to move one vehicle, and the second one rides with us. Housing is gated, so the meeting spot sits outside it. Fort Drum is three hours north, and winter pickups there wait for the plows. Ship Guy is a private broker with no connection to any post."),
 ("What happens if a nor’easter or an ice storm hits on my pickup day?","The driver waits until the Thruway reopens and the sand trucks reach the hills. A pickup can slide a day. Ice on the Troy hills lasts longer than the storm. Winter handoffs there happen on the main roads from the start."),
 ("Can you ship a car that does not run from Albany?","Yes. The carrier brings a winch for a car that will not start. The slower loading is reflected in the quote. In winter, have it shoveled out and reachable. Let us know if it rolls, steers, and brakes."),
 ("What do you need for an Albany car shipping quote?","Where the car is and where it is going, with the neighborhood or town on the Albany end. Year, make, and model. Whether it runs and rolls. Open or enclosed, and the dates you can work with. That covers an Albany quote."),
]
BODY.append(faq_section(FAQ,'Albany FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Albany?','The form above prices the lane in about two minutes. Add the neighborhood and your dates, and we will pair you with a carrier already on the Thruway.','+15189902826','(518) 990-2826','Get your free Albany quote'))

build({
 'slug':'auto-transport-albany-new-york',
 'title':'Car Shipping in Albany, NY — Auto Transport | Ship Guy',
 'meta':'Car shipping in Albany, NY at the Thruway, Northway, and Boston-lane interchange. State workforce and medical center timing, Center Square and Troy handoffs, the Malta chip plant, Saratoga season, Fort Drum staging, tolls built in. Local office on Washington Avenue. Free quote.',
 'h1':'Car Shipping in<br>Albany, <span class="accent">New York</span>',
 'lede':'Open, enclosed, and expedited auto transport across the Capital District, planned around the interchange, the session, and the ice.',
 'tel':'+15189902826','disp':'(518) 990-2826','brand':'Albany','keyword':'car shipping in albany',
 'localterms':['albany','thruway','interstate 87','interstate 90','northway','interstate 787','interstate 88','route 7','central avenue','western avenue','wolf road','twin bridges','washington avenue','capitol','plaza','center square','mansion district','pine hills','delaware avenue','colonie','latham','loudonville','guilderland','delmar','slingerlands','glenmont','rensselaer','troy','cohoes','watervliet','schenectady','niskayuna','clifton park','malta','saratoga','state government','session','medical center','residents','chip plant','biotech','university','engineering school','arsenal','airlift wing','fort drum','tulip','track','race days','nor','ice','salt','mohawk','new york city','boston','hartford','syracuse','buffalo','philadelphia','washington','chicago','orlando'],
}, BODY, FAQ)
