import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Staten Island, New York','Car shipping in the borough of bridges, where every carrier arrives from New Jersey or over the Verrazzano',
 ['Car shipping in Staten Island is the easiest in the city, because the trucks come from New Jersey. Ship Guy is a licensed auto transport broker with an office on Willowbrook Road, next to the college.',
  'We book vetted carriers across the island, from the North Shore to Tottenville. We do not own the trucks.',
  'The Staten Island Expressway carries Interstate 278 from the Goethals Bridge to the Verrazzano. The West Shore Expressway carries Route 440 from the Outerbridge Crossing to the Bayonne Bridge. Hylan Boulevard, Richmond Avenue, and Victory Boulevard carry the island in between.',
  'This page covers the bridges and the tolls, the four shores and the hills, and the mall. It also covers the Florida lane, the city workers, the hospitals, the port, the storms, and the marathon.'],
 'Staten Island at a glance',
 ['Most pickups happen within 1 to 3 days. The New Jersey Turnpike sits ten minutes away, and every carrier on the East Coast runs it.',
  'Philadelphia, Boston, and Washington are same-day lanes. Albany and Buffalo take a day. Charlotte and Chicago take two, and Florida runs three.'],
 'Tell us the neighborhood. The North Shore hills and the narrow blocks on the East Shore need a meeting spot. The South Shore and the West Shore usually have a driveway or a wide street.'))

BODY.append(sec('The Roads','Interstate 278, Route 440, the Four Bridges, and the Tolls',
 prose(
  L('Staten Island is an island, and every carrier arrives over one of four bridges.'),
  P('The Goethals Bridge brings carriers in from the New Jersey Turnpike and Interstate 95. The Outerbridge Crossing brings them in from the Garden State Parkway and the shore. The Bayonne Bridge brings them in from Jersey City and the port. The Verrazzano brings them in from Brooklyn and the rest of the city.'),
  P('The three New Jersey bridges charge a toll coming onto the island and nothing leaving it. The Verrazzano charges in both directions. A carrier pays by transponder and by the axle, and the toll is built into the quote. A pickup that meets the truck on the New Jersey side can trim it.'),
  P('The Staten Island Expressway runs across the north of the island between the Goethals and the Verrazzano. It jams at both ends. The West Shore Expressway runs down the west side to the Outerbridge. The parkway on the South Shore bans trucks, so a carrier uses Hylan or Richmond Avenue instead.'),
  P('The carriers come off the Expressway at Richmond Avenue, Bradley Avenue, Victory Boulevard, and Hylan. The mall lot in New Springville and the lots along Richmond Avenue are the usual meeting spots. Our office sits on Willowbrook Road, between Victory Boulevard and the college.'),
 ), alt=True))

BODY.append(sec('The Four Shores','The North Shore, the East Shore, the South Shore, and the West Shore',
 prose(
  L('Staten Island is four shores and a ridge of hills, and the handoff depends on which one.'),
  P('The North Shore is the oldest part of the island. St. George, Tompkinsville, Stapleton, and New Brighton climb from the ferry on narrow one-way streets. The cars park on both curbs. The driver meets you on Bay Street, on Victory Boulevard, or at a lot by the ferry terminal.'),
  P('The hills in the middle of the island are the highest on the coast south of Maine. Todt Hill, Grymes Hill, Emerson Hill, and Lighthouse Hill have winding roads with no shoulders and low branches. A seventy-five-foot trailer stays on Richmond Road, Clove Road, or Victory Boulevard.'),
  P('The East Shore is flat and close to the water. South Beach, Midland Beach, New Dorp, and Oakwood have tight blocks and narrow streets. The ones nearest the water flood in a storm. The driver meets you on Hylan Boulevard or at a lot along Father Capodanno.'),
  P('The South Shore is the suburban end. Great Kills, Eltingville, Annadale, Huguenot, and Tottenville have driveways and wider streets. The truck usually reaches the curb or the end of the block. The West Shore is the mall, the park on the old landfill, the warehouses, and the port. Employers there can usually allow a handoff at the dock.'),
 )))

ROUTES=[("Philadelphia, PA","I-95 · ~85 mi","Same day","$170–$280"),("Boston, MA","I-95 · ~230 mi","Same day","$240–$360"),
 ("Washington, DC","I-95 · ~220 mi","Same day","$240–$360"),("Albany, NY","I-87 · ~160 mi","1 day","$210–$320"),
 ("Buffalo, NY","I-80/I-90 · ~400 mi","1 day","$380–$540"),("Charlotte, NC","I-95/I-85 · ~620 mi","2 days","$470–$680"),
 ("Chicago, IL","I-80 · ~790 mi","2 days","$560–$820"),("Orlando, FL","I-95 · ~1,070 mi","3 days","$760–$1,080"),
 ("Boca Raton, FL","I-95 · ~1,230 mi","3–4 days","$800–$1,140"),("Los Angeles, CA","I-80/I-40 · ~2,780 mi","7–9 days","$1,340–$1,790")]
BODY.append(rate_table('Lanes &amp; Costs','Staten Island Car Shipping Lanes and Estimated Costs',
 'Where Staten Island cars go, from the Turnpike to Florida, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a running sedan on an open trailer. An SUV or pickup adds about 10 to 25 percent, and enclosed adds more. The bridge tolls, the season, and the carriers free on your dates set the final number.',
 prose(
  P('Staten Island prices like New Jersey more than like the rest of the city. The carriers come from the Turnpike. Philadelphia and Washington ride 95 south, and Boston rides 95 north around the city.'),
  P('The Florida lane is the biggest one on the island. It runs full from October into December. The <a href="car-shipping-cost.html">cost guide</a> has the rest of the detail.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Florida Lane, the City Workers, the Hospitals, and the Port',
 prose(
  L('Staten Island relocates retirees, cops, firefighters, nurses, and port workers, and most of them head south.'),
  P('More Staten Island families leave for Florida, the Carolinas, and the Jersey Shore than anywhere else. Most ship a car ahead of the move. Retirees ship to Boca Raton, Tampa, Orlando, and Naples from October into December. The car comes back in spring. Our <a href="snowbird-car-shipping.html">snowbird</a> page has the planning tips.'),
  P('A large share of the city’s police officers and firefighters live on the island. Their retirements send cars south on a schedule of their own. Many keep a second home in the Poconos or at the Jersey Shore. We ship between the two every month.'),
  P('The hospital on the East Shore and the one on the North Shore bring in residents every summer. Most arrive from out of state with a car. The handoff happens on Hylan Boulevard or Castleton Avenue rather than in a hospital garage.'),
  P('The container port at Howland Hook and the warehouses along the West Shore hire managers on start dates. The college on Victory Boulevard and the college on Grymes Hill bring cars in each August. The campus lots take the handoff, and an adult signs for the car.'),
  P('Fort Hamilton sits at the Brooklyn end of the Verrazzano. The Coast Guard station sits under the Staten Island end. Families from both live on the island. The orders usually move one car, and the other one travels with us. See the <a href="military-car-shipping.html">military</a> page for PCS planning and the <a href="state-to-state-car-shipping.html">state-to-state</a> page for the interstate side.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Nor’easters, the Flood Zone, the Bridge Wind, and the Marathon',
 prose(
  L('Staten Island gets the ocean’s weather first, and the bridges feel it before the streets do.'),
  P('Nor’easters and the remnants of hurricanes push the water up the East Shore and the South Shore. Midland Beach, New Dorp Beach, and Oakwood Beach flooded badly in Sandy. The seawall is still being built. A pickup near the water waits for the tide to fall and moves to Hylan Boulevard.'),
  P('High wind closes the Verrazzano to empty trailers and tandem rigs. A loaded carrier crosses while an empty one waits. The New Jersey bridges post wind warnings on the same days. We watch the forecast and move a bridge crossing earlier or later in the day.'),
  P('Snow closes the Expressway for a morning a few times each winter. The hills ice before the rest of the island. A winter pickup can slide a day, and the handoff moves to a plowed lot. Summer heat moves the loading hour earlier. The beach traffic fills Father Capodanno on weekends.'),
  P('The marathon starts at Fort Wadsworth on the first Sunday of November. The Verrazzano closes to traffic that morning. The Tunnel to Towers run closes the Brooklyn end in September. We schedule bridge crossings around both, and the New Jersey bridges run normally.'),
 )+chips(["St. George","Tompkinsville","Stapleton","New Brighton","West Brighton","Port Richmond","Mariners Harbor","Willowbrook","Bulls Head","New Springville","Todt Hill","Grymes Hill","Emerson Hill","Dongan Hills","South Beach","Midland Beach","New Dorp","Oakwood","Great Kills","Eltingville","Annadale","Huguenot","Tottenville","Travis","Bloomfield","Howland Hook"])
 +NOTE('Serving every neighborhood on the island. Tell us the shore, the street, and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Staten Island?',
 prose(
  L('Most of what leaves the island rides open, and the Florida lane is priced that way.'),
  P('An enclosed trailer keeps the salt, the road grime, and attention off the car. The garages on Todt Hill and in Annadale book enclosed trailers. So does a car that spends the winter in Boca Raton.'),
  P('A commuter car rides open to Florida and arrives the way it left. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages lay out the trade-off.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff at the mall or on a wide road, and a delivery. The bridges decide the hour.'),
  P('Accept the price, and a carrier already running the Turnpike takes the booking. We set the spot with the bridges in mind. The driver walks the car with you and writes it up on a Bill of Lading. Both sign, and delivery is checked against it.'),
 )+ULI([
  "Clear everything personal out of the car",
  "A quarter tank of fuel is enough",
  "Photograph the car before pickup, salt and all",
  "Leave a working key and flag anything mechanical",
  "Shut the aftermarket alarm off",
  "On the North Shore hills, plan to meet the truck on Richmond Road or Clove Road",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages cover the rest.'))))

BODY.append(sec('Why Ship Guy','Why Staten Island Drivers Choose Ship Guy',
 prose(
  L('We work the bridges every day and plan around the tolls, the wind, and the Florida season.'),
  P('Ship Guy holds active brokerage authority with the FMCSA. A $75,000 surety bond backs every booking. Both are public record. Our office is on Willowbrook Road, next to the college.'),
  P('One coordinator handles the booking start to finish. Open, enclosed, and expedited transport are all available here, and the <a href="services.html">services</a> page lists them.'),
 ), alt=True))

BODY.append(office('Staten Island','651 Willowbrook Rd Ste 887','Staten Island, NY 10314','+19297232493','(929) 723-2493','ET',
 '651+Willowbrook+Rd+Ste+887,+Staten+Island,+NY+10314','Visit Us','Find Ship Guy in Staten Island',
 'Our office is on Willowbrook Road, between Victory Boulevard and the College of Staten Island.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3738.8580412271317!2d-74.1469173!3d40.6089646!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c24d3aaac7b64b%3A0xa886b5ad27d1afeb!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792079811034!5m2!1sen!2sus'))

FAQ=[
 ("Are the bridge tolls added to my Staten Island quote?","They are built in. The three New Jersey bridges charge coming onto the island and nothing leaving it. The Verrazzano charges both ways. The carrier pays by transponder and by the axle, and the quote includes it. Meeting the truck on the New Jersey side can trim the number."),
 ("How much does it cost to ship a car from Staten Island to Florida?","Orlando runs seven hundred sixty to ten hundred eighty dollars for a sedan. That is about ten hundred seventy miles down Interstate 95. Boca Raton and Fort Lauderdale run a little more, and Tampa is in between. October through December costs more than spring. SUVs and pickups add 10 to 25 percent."),
 ("Can the carrier come to my street on Staten Island?","On the South Shore, usually. Great Kills, Eltingville, Annadale, and Tottenville have driveways and wider streets. On the North Shore hills and the East Shore blocks, the driver meets you on Hylan Boulevard. The mall lot works for the whole middle of the island."),
 ("Is Staten Island priced like Brooklyn or like New Jersey?","Like New Jersey, which works in your favor. The carriers come off the Turnpike and over the Goethals or the Outerbridge. They never touch the rest of the city. A Brooklyn pickup adds the Verrazzano toll and the city traffic. Many Brooklyn customers meet the truck on this side for that reason."),
 ("What happens if high wind closes the Verrazzano on my pickup day?","A loaded carrier usually still crosses, because the wind ban covers empty trailers and tandem rigs. If the bridge closes to everything, the truck uses the Goethals and the Turnpike instead. The handoff moves earlier or later in the day, and we call before it does."),
 ("Does the marathon or a storm change the schedule?","The marathon closes the Verrazzano on the first Sunday of November, and the New Jersey bridges run normally. A nor’easter moves a pickup on the East Shore or the South Shore to Hylan Boulevard. It waits there until the water falls. We schedule around both and call the moment the plan changes."),
 ("Do you ship cars for retiring police officers and firefighters?","Yes, every month. Retirements send cars to Florida, the Carolinas, and the Jersey Shore. Many families ship the second car ahead of the move. We also run cars between the island and a second home in the Poconos or at the shore. Two to three weeks of notice keeps the Florida price steady in the fall."),
 ("Do you handle a PCS move to Fort Hamilton or the Coast Guard station?","Yes. Fort Hamilton sits at the Brooklyn end of the Verrazzano. The Coast Guard sector sits under the Staten Island end. The orders usually move one car, and the other one travels with us. Both gates stop the truck, so the handoff happens on Bay Street or at the Verrazzano lots. Ship Guy is a private broker with no connection to either."),
 ("Can you ship a car that does not run from Staten Island?","Yes. A carrier with a winch takes the job, and the slower loading is part of the price. The spot has to be flat, which usually means the mall lot or a wide South Shore street. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Staten Island car shipping quote?","Both addresses, with the shore and the street on this end. The year, make, and model. Whether it runs. Open or enclosed. Your dates, with the Florida season in mind. That is a complete Staten Island request."),
]
BODY.append(faq_section(FAQ,'Staten Island FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Staten Island?','The form above prices the trip in about two minutes. Tell us the shore and your dates, and a carrier already on the Turnpike takes it from there.','+19297232493','(929) 723-2493','Get your free Staten Island quote'))

build({
 'slug':'auto-transport-staten-island-new-york',
 'title':'Car Shipping in Staten Island, NY — Auto Transport | Ship Guy',
 'meta':'Car shipping in Staten Island, NY over the Goethals, the Outerbridge, and the Verrazzano. Bridge tolls built in, North Shore and East Shore meeting spots, South Shore driveways, the Florida retirement lane, hospital and port relocations, Fort Hamilton and Coast Guard moves, nor’easter and bridge-wind planning. Local office on Willowbrook Road. Free quote.',
 'h1':'Car Shipping in<br>Staten Island, <span class="accent">New York</span>',
 'lede':'Open, enclosed, and expedited auto transport across the island, planned around the bridges, the tolls, and the Florida season.',
 'tel':'+19297232493','disp':'(929) 723-2493','brand':'Staten Island','keyword':'car shipping in staten island',
 'localterms':['staten island','interstate 278','route 440','expressway','goethals','outerbridge','bayonne','verrazzano','turnpike','garden state parkway','tolls','transponder','hylan','richmond avenue','victory boulevard','richmond road','clove road','bay street','father capodanno','castleton','willowbrook','bradley avenue','north shore','st. george','tompkinsville','stapleton','new brighton','todt hill','grymes hill','emerson hill','lighthouse hill','east shore','south beach','midland beach','new dorp','oakwood','south shore','great kills','eltingville','annadale','huguenot','tottenville','west shore','mall','new springville','landfill','warehouses','port','howland hook','ferry','college','hospital','medical center','residents','police','firefighters','retirees','florida','boca raton','tampa','orlando','naples','carolinas','jersey shore','poconos','fort hamilton','coast guard','fort wadsworth','marathon','tunnel to towers','nor’easters','sandy','seawall','wind','snow','philadelphia','boston','washington','albany','buffalo','charlotte','chicago','los angeles'],
}, BODY, FAQ)
