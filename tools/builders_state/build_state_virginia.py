import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Support")]))

BODY.append(intro_block('Virginia','Virginia auto transport from the Beltway to the largest naval base in the world',
 ['Virginia auto transport runs on federal orders, Navy orders, and a corridor that never stops between Washington and the Carolinas.',
  'Ship Guy is a licensed auto transport broker. We book vetted carriers across Virginia, and we do not own the trucks.',
  'Interstate 95 runs from the Beltway through Fredericksburg and Richmond to North Carolina. Interstate 64 links Hampton Roads to Richmond and the mountains, Interstate 81 runs the Shenandoah Valley, and Interstate 66 and 495 carry Northern Virginia.',
  'This page covers the corridors and the tunnels, Northern Virginia and the federal workforce, Richmond, Hampton Roads and its bases, the valley and the campuses, the southwest, and the weather.'],
 'Virginia at a glance',
 ['Most pickups happen within 1 to 3 days in Northern Virginia, Richmond, Hampton Roads, and along Interstate 81, and within 2 to 4 days in the southwest mountains and the Northern Neck.',
  'Washington, Baltimore, Raleigh, and Norfolk are same-day lanes from one region or another. Philadelphia, Charlotte, and Pittsburgh take a day. Florida runs two to three.'],
 'Virginia has no city page yet, so this page carries the detail for Arlington, Alexandria, Fairfax, Richmond, Norfolk, Virginia Beach, Roanoke, Charlottesville, and the rest.'))

BODY.append(sec('The Corridors','Interstate 95, 64, 81, 66, and the Tunnels',
 prose(
  L('Every carrier on the East Coast corridor crosses Virginia, and the state adds two tunnels and a valley to the trip.'),
  P('Interstate 95 carries the Northeast-to-Florida lane through Fredericksburg, Richmond, and Petersburg. It backs up from Washington to Fredericksburg every afternoon, and carriers plan Northern Virginia stops for mornings.'),
  P('Interstate 64 runs from the Hampton Roads bridge-tunnels through Richmond and Charlottesville to the mountains and West Virginia. Interstate 81 carries the Shenandoah Valley from Winchester through Harrisonburg and Roanoke to Bristol, with more trucks per mile than almost any road in the East.'),
  P('Interstate 66 and the Beltway carry Northern Virginia, with tolled express lanes carriers avoid. The Hampton Roads and Monitor-Merrimac tunnels carry Norfolk traffic, and the bay bridge-tunnel charges a toll that is built into every quote.'),
  P('Towns on those roads schedule fast. The southwest mountains, the Northern Neck, and the Eastern Shore take an extra day or two.'),
 ), alt=True))

BODY.append(sec('Northern Virginia','Arlington, Fairfax, Loudoun, and the Federal Calendar',
 prose(
  L('More Virginians live inside the Beltway\u2019s orbit than anywhere else in the state, and they move on the federal calendar.'),
  P('The Pentagon, the agencies, and the defense contractors along the Dulles corridor relocate employees from across the country on start dates. The data centers in Loudoun County add engineers on project schedules.'),
  P('Arlington and Alexandria have narrow streets, rowhouses, and towers with garages, and the driver meets you on a main road or at a lot near Interstate 395. Fairfax, Loudoun, and Prince William are wide subdivisions, many with gates, so send the community name.'),
  P('Fort Belvoir, the joint base at Myer and Henderson Hall, and the Marine base at Quantico rotate families year round with a summer peak. Housing is gated, so the driver meets you outside it.'),
  P('If your employer or agency reimburses the shipment, we provide the documentation. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
 )))

ROUTES=[("Washington, DC (from Arlington)","I-395 · ~10 mi","Same day","$150–$230"),("Norfolk, VA (from Richmond)","I-64 · ~95 mi","Same day","$170–$280"),
 ("Baltimore, MD (from Fairfax)","I-495/I-95 · ~60 mi","Same day","$150–$240"),("Raleigh, NC (from Richmond)","I-95 · ~170 mi","Same day","$220–$340"),
 ("Philadelphia, PA (from Richmond)","I-95 · ~250 mi","1 day","$250–$380"),("Charlotte, NC (from Richmond)","I-85 · ~290 mi","1 day","$270–$400"),
 ("Pittsburgh, PA (from Winchester)","I-81/I-70 · ~240 mi","1 day","$250–$380"),("Nashville, TN (from Roanoke)","I-81/I-40 · ~430 mi","1 day","$380–$540"),
 ("Atlanta, GA (from Richmond)","I-85 · ~530 mi","1–2 days","$430–$620"),("Orlando, FL (from Norfolk)","I-95 · ~740 mi","2 days","$520–$750")]
BODY.append(rate_table('Lanes &amp; Costs','Virginia Car Shipping Lanes and Estimated Costs',
 'Common lanes out of Northern Virginia, Richmond, Hampton Roads, and the valley, with estimated open-transport ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a running sedan on an open trailer, priced from the nearer region. SUVs and pickups add about 10 to 25 percent, enclosed more. Tunnel and bridge tolls are included, and season plus carrier availability on your dates set the real quote.',
 prose(
  P('Washington, Baltimore, and Raleigh are among the cheapest lanes anywhere, because the corridor never stops. Interstate 81 makes Pittsburgh and Nashville steady from the valley.'),
  P('The Florida lane swings with the fall migration from Northern Virginia and Hampton Roads. The <a href="car-shipping-cost.html">cost guide</a> explains the other variables.'),
 ), alt=True))

BODY.append(sec('Hampton Roads','Norfolk, the Navy, the Shipyards, and the Tunnels',
 prose(
  L('Hampton Roads moves more military households than anywhere in the country, and every one of them crosses a bridge or a tunnel.'),
  P('Naval Station Norfolk is the largest naval base in the world, and the air station at Oceana, the amphibious base at Little Creek, and the shipyard in Portsmouth sit beside it. Langley Air Force Base and Fort Eustis share a joint base across the water.'),
  P('Sailors and families rotate year round, with the heaviest moves from May through August. Many ship a second vehicle through us, since orders may cover only one, and housing is gated at each installation.'),
  P('The shipbuilder in Newport News relocates engineers on program schedules, and the port receives imported cars that clear customs before we ship them domestically. The tunnels back up every rush hour, and carriers plan crossings for mid-morning.'),
  P('Virginia Beach, Chesapeake, and Suffolk are wide suburbs where the truck reaches the curb. Ship Guy is a private broker with no military affiliation, and our <a href="military-car-shipping.html">military</a> page covers PCS timing.'),
 )))

BODY.append(sec('Richmond','The Capital, the Medical Center, and Fort Gregg-Adams',
 prose(
  L('Richmond sits where Interstate 95 and 64 cross, and carriers stage there for the whole state.'),
  P('State government, the medical center, and the corporate headquarters relocate people on start dates, and the university sends cars in each August. The Fan and Church Hill have narrow streets and rowhouses, so the driver meets you on a main road.'),
  P('Fort Gregg-Adams at Petersburg trains logistics soldiers on class cycles year round. Housing is gated, so the driver meets you outside it.'),
  P('Henrico, Chesterfield, and the suburbs are wide grids where the truck reaches the curb. Fredericksburg to the north fills with commuters and Quantico families.'),
 ), alt=True))

BODY.append(sec('The Valley &amp; the Campuses','Charlottesville, Blacksburg, Harrisonburg, and Roanoke',
 prose(
  L('West of Richmond, Virginia ships on campuses and a valley full of trucks.'),
  P('Charlottesville sends cars in each August and home each May, and its downtown and the streets near the university are tight. Blacksburg sits in the mountains off Interstate 81, and home football Saturdays fill the roads for hours.'),
  P('Harrisonburg, Lexington, and Radford add waves on the same calendar. Campus handoffs happen at a lot nearby, and an adult signs for a student car.'),
  P('Roanoke is the hub of the southwest, on Interstate 81 with the hospitals and the rail yards. Winchester ships on the Washington commute, and the Shenandoah Valley towns sit right on the corridor.'),
  P('Bristol, the coalfields, and the far southwest sit on winding two-lane roads and take an extra day or two.'),
 )))

BODY.append(sec('Weather &amp; the Corners','Mountain Snow, Coastal Storms, and the Northern Neck',
 prose(
  L('Virginia weather runs from mountain snow to coastal flooding, with the corridor in between.'),
  P('Snow and ice close Interstate 81 and the mountain passes a few times each winter, and fog settles into the valley on fall mornings. Carriers wait for the plows and the sun.'),
  P('Hurricanes and nor\u2019easters flood Hampton Roads and the Eastern Shore, and carriers leave the coast days before a landfall. After a storm, the tunnels reopen before the neighborhoods dry out.'),
  P('The Northern Neck, the Middle Peninsula, and the Eastern Shore sit on two-lane roads between rivers, and the driver meets you on the US highway. Summer heat and Beltway traffic change only the loading hour.'),
 )+chips(["Arlington","Alexandria","Fairfax","Reston","Ashburn","Leesburg","Manassas","Woodbridge","Fredericksburg","Richmond","Henrico","Chesterfield","Petersburg","Williamsburg","Newport News","Hampton","Norfolk","Virginia Beach","Chesapeake","Suffolk","Charlottesville","Harrisonburg","Winchester","Roanoke","Blacksburg","Bristol"])
 +NOTE('Serving all ninety-five Virginia counties and the independent cities. For a gated community, a base, or a peninsula address, tell us the town and we will name the meeting spot.'), alt=True))

BODY.append(sec('Your Options','Open or Enclosed in Virginia?',
 prose(
  L('Open transport is the everyday choice, and the corridor and the base moves run on it.'),
  P('Enclosed transport keeps a car covered against road salt, coastal air, and attention. McLean, Great Falls, and the horse country keep enclosed carriers busy with collector cars.'),
  P('A commuter car rides open without trouble. Our <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages compare the two.'),
 )))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff on the corridor, and a delivery, with the tunnels and the gates already planned.'),
  P('Once the price is approved, a carrier on Interstate 95, 64, or 81 takes the booking. The driver records the car\u2019s condition on a Bill of Lading, and you sign it before loading. That record is what delivery is checked against.'),
 )+ULI([
  "Remove personal belongings",
  "Keep about a quarter tank of fuel",
  "Photograph the vehicle before pickup",
  "Provide a working key and disclose mechanical issues",
  "Turn off aftermarket alarms",
  "For a base or a gated community, plan to meet the truck at the gate or a nearby lot",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> guides go step by step.')), alt=True))

BODY.append(sec('Why Ship Guy','Why Virginia Drivers Choose Ship Guy',
 prose(
  L('We know the tunnel hours, the base gates, and which afternoon Interstate 95 stops moving.'),
  P('Ship Guy holds active FMCSA brokerage authority and a $75,000 surety bond, both verifiable in federal records.'),
  P('One coordinator carries the shipment from quote to delivery and can arrange open, enclosed, or expedited transport. The <a href="services.html">services</a> page lists everything we offer.'),
 )))

FAQ=[
 ("Can you handle a PCS move to Norfolk, Oceana, Langley, or Quantico?","Yes, Hampton Roads and Northern Virginia move more military households than anywhere in the country, and every installation is a steady lane for us. Many ship a second vehicle through us, since orders may cover only one. Housing is gated, so the driver meets you outside it. Summer is the peak, so allow two to three weeks. Ship Guy has no military affiliation."),
 ("How much does it cost to ship a car from Virginia to Florida?","Orlando from Norfolk usually runs five hundred twenty to seven hundred fifty dollars for a sedan, about seven hundred forty miles down Interstate 95. From Northern Virginia, add about a hundred fifty miles. Fall snowbird demand lifts the price from October through December. Larger vehicles add 10 to 25 percent."),
 ("Can the carrier come to my house in Arlington or Alexandria?","Usually not the narrow streets or the towers. The driver meets you on a main road or at a lot near Interstate 395 or the Beltway. It is a few minutes from home. Fairfax, Loudoun, and Prince William subdivisions often allow curbside, but many have gates, so send the community name."),
 ("Do the tunnels and bridges affect Hampton Roads shipments?","Yes, in timing. The Hampton Roads and Monitor-Merrimac tunnels back up every rush hour, so carriers plan crossings for mid-morning. The bay bridge-tunnel charges a toll that is built into every quote, and a strong wind closes it to high-profile vehicles."),
 ("Do you handle federal and contractor relocations in Northern Virginia?","Yes, the agencies, the Pentagon, and the contractors along the Dulles corridor are a large part of our Virginia work, along with the Loudoun data centers. We plan the pickup around your start date. If your employer or agency reimburses the shipment, we provide the documentation."),
 ("Can you ship a car for a UVA, Virginia Tech, or JMU student?","Yes, student cars move each August and again in May. The streets near the Charlottesville campus are tight, and Blacksburg's game-day Saturdays fill the mountain roads, so we schedule around both. The handoff happens at a lot near campus, and an adult signs for the car."),
 ("Why is Interstate 81 such a busy lane?","Because it carries more trucks per mile than almost any road in the East, running the Shenandoah Valley from Winchester to Bristol. Roanoke, Harrisonburg, and the valley towns sit right on it, and Pittsburgh, Nashville, and Charlotte are all a day away."),
 ("Does winter close the routes across Virginia?","In the mountains, a few times each winter. Snow and ice close Interstate 81 and the passes for a day, and fog settles into the valley on fall mornings. The corridor and the coast run normally most of the winter, with nor'easters closing them a few times a season."),
 ("Can you ship a car that does not run?","Yes, non-running cars ship from every part of Virginia. A winch-equipped carrier loads it, and the extra time carries a fee. Tell us whether it can roll, steer, and brake."),
 ("What do you need for a Virginia car shipping quote?","Both addresses, with the community name for a gated address or the base for a PCS move. The year, make, and model. Whether it runs and rolls. Open or enclosed, and a date range. That is a complete Virginia quote request."),
]
BODY.append(faq_section(FAQ,'Virginia FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book auto transport in Virginia?','A quote takes about two minutes. Then tell us your town and dates, and we will plan around the tunnels, the gates, and the corridor.','+18664992815','(866) 499-2815','Get your free Virginia quote'))

build_state({
 'slug':'virginia-auto-transport',
 'title':'Virginia Auto Transport &amp; Car Shipping | Ship Guy',
 'meta':'Virginia auto transport from the Beltway to Hampton Roads. Federal and contractor relocations, Norfolk, Oceana, Langley, and Quantico moves, Richmond and the valley, UVA and Virginia Tech timing, tunnel hours, tolls built in. Free quote.',
 'h1':'Virginia<br>Auto <span class="accent">Transport</span>',
 'lede':'Open, enclosed, and expedited car shipping across Virginia, planned around the corridor, the bases, and the tunnels.',
 'brand':'Virginia','keyword':'virginia auto transport','abbr':'VA',
 'localterms':['virginia','interstate 95','interstate 64','interstate 81','interstate 66','interstate 495','interstate 395','interstate 85','beltway','tunnel','bridge-tunnel','arlington','alexandria','fairfax','loudoun','ashburn','dulles','pentagon','fort belvoir','quantico','fredericksburg','richmond','fan','petersburg','fort gregg-adams','hampton roads','norfolk','naval station','oceana','little creek','portsmouth','langley','fort eustis','newport news','shipbuilder','virginia beach','chesapeake','charlottesville','uva','blacksburg','virginia tech','harrisonburg','jmu','roanoke','winchester','shenandoah','bristol','northern neck','eastern shore','nor','hurricane','florida'],
}, BODY, FAQ)
