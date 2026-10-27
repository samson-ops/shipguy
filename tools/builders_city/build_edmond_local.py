import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Edmond, Oklahoma','Car shipping for the north side, where Route 66 meets Interstate 35',
 ['Car shipping in Edmond is a suburban booking with a big-city carrier supply ten minutes away. Ship Guy is a licensed auto transport broker with an office on East Eleventh Street near downtown.',
  'We book vetted carriers across the north metro, from Deer Creek to Arcadia Lake and north to Waterloo. We do not own the trucks.',
  'Interstate 35 runs along the east side of the city. The Broadway Extension carries the commute south into Oklahoma City. The Kilpatrick Turnpike meets the interstate at the south edge. The Turner Turnpike to Tulsa begins a few miles below that.',
  'This page covers the interstate and the turnpikes, the gated additions, the university, and the commute. It also covers the hail, the ice, the festivals on Broadway, and the lanes.'],
 'Edmond at a glance',
 ['Most pickups happen within 1 to 3 days. The Interstate 35 and Interstate 44 lanes bring carriers past the city all day.',
  'Tulsa, Wichita, Dallas, and Fort Worth are same-day lanes. Kansas City, Little Rock, and Houston take a day. Denver runs two.'],
 'Tell us the addition and the gate. Many Edmond additions are gated or governed by an association, and the truck meets you at the entrance.'))

BODY.append(sec('The Roads','Interstate 35, the Broadway Extension, and the Turnpikes',
 prose(
  L('Edmond sits on the busiest north-south lane in the state, and the carriers are already here.'),
  P('Interstate 35 runs the east side of the city. The exits are Second Street, Fifteenth, Thirty-Third, Covell, and Waterloo. North it reaches Wichita and Kansas City. South it crosses Oklahoma City to Norman and Dallas.'),
  P('The Broadway Extension is Highway 77, the commuter road from downtown Edmond into the city. The Kilpatrick Turnpike meets Interstate 35 at the south edge and loops the west side to the airport.'),
  P('The Turner Turnpike to Tulsa starts at the Interstate 44 junction a few miles south. Interstate 40 is fifteen minutes beyond that. Every lane out of Edmond starts on one of those roads.'),
  P('Second Street is Route 66 through town. It runs east past Arcadia Lake to the round barn. Covell, Danforth, and Fifteenth are the east-west section lines the carriers use across the city.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Gated Additions, Downtown Broadway, Deer Creek, and the Lake',
 prose(
  L('Edmond was built in additions with gates, greens, and three-car garages. The trailer has to be invited in.'),
  P('Oak Tree, Rose Creek, Fairfax, and the golf-course additions are gated. The driver meets you at the gate or in the clubhouse lot. A loaded trailer cannot turn on the lanes inside.'),
  P('Coffee Creek, Twin Bridges, and the additions along Covell and Danforth are open but governed by associations. Most allow a truck at the curb for a few minutes. We check the rule before the driver arrives.'),
  P('Downtown along Broadway runs on angled parking and the festival calendar. The university campus east of downtown is tight on move-in days. The handoff happens on Second Street, Boulevard, or a lot near the rail line.'),
  P('Deer Creek on the west side is new construction. Some streets are not on a carrier’s map yet. Send the full address and the nearest section line. The lake side along Interstate 35 is wide and easy.'),
  P('Our office is on East Eleventh Street a few blocks from Broadway, between downtown and the university.'),
 )))

ROUTES=[("Tulsa, OK","I-35/Turner Tpk · ~95 mi","Same day","$170–$280"),("Wichita, KS","I-35 · ~145 mi","Same day","$190–$300"),
 ("Fort Worth, TX","I-35 · ~215 mi","Same day","$230–$350"),("Dallas, TX","I-35 · ~220 mi","Same day","$230–$350"),
 ("Amarillo, TX","I-40 · ~270 mi","1 day","$250–$380"),("Kansas City, MO","I-35 · ~335 mi","1 day","$310–$450"),
 ("Little Rock, AR","I-40 · ~355 mi","1 day","$320–$460"),("Houston, TX","I-35/I-45 · ~465 mi","1 day","$400–$570"),
 ("St. Louis, MO","Turner Tpk/I-44 · ~490 mi","1–2 days","$420–$600"),("Denver, CO","I-40/US-287 · ~660 mi","2 days","$500–$730")]
BODY.append(rate_table('Lanes &amp; Costs','Edmond Car Shipping Lanes and Estimated Costs',
 'The lanes Edmond households ask about most, with estimated open-transport ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates, running sedan, open trailer. SUVs and pickups add roughly 10 to 25 percent, and enclosed adds more. Turnpike tolls are included. Spring weather and carrier availability on your dates set the real quote.',
 prose(
  P('Tulsa is the quickest lane. It sits an hour and a half up the Turner Turnpike from the south edge of town. Wichita is the next one north. Dallas and Fort Worth are the busy lanes south.'),
  P('Phoenix, Los Angeles, Chicago, and Florida run three to four days and price by the season. The <a href="car-shipping-cost.html">cost guide</a> explains the rest of the number.'),
 ), alt=True))

BODY.append(sec('The Commute &amp; the Employers','Downtown Towers, the Tech Campus, Tinker, and the Hospitals',
 prose(
  L('Edmond households work across the metro, and the relocations arrive on corporate calendars.'),
  P('The energy and banking towers downtown transfer executives on start dates. The software campus on Memorial Road does the same with engineers. Many of them land in Edmond for the schools. Many ship a car from Texas, Colorado, or the coasts.'),
  P('If your employer reimburses the shipment, we send the documentation it asks for. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the longer relocation.'),
  P('Tinker Air Force Base is twenty-five minutes southeast on Interstate 35. Officers and contractors fill the north-side additions. The move order covers one car, so the second one rides with us. The handoff happens outside the gate. Our <a href="military-car-shipping.html">military</a> page covers the planning.'),
  P('The two hospital campuses on Interstate 35 and Second Street bring in physicians on start dates. The university downtown and the Christian university on Memorial Road add student cars each August and May.'),
 )))

BODY.append(sec('Hail, Ice, and the Festivals','The Weather and the Broadway Closures',
 prose(
  L('Edmond’s weather problem is hail, and its traffic problem is a parade.'),
  P('The storm months run from April into June. The north side has taken hail the size of baseballs more than once. A car waiting outside on a storm day is the risk. We shift the window when hail is in the forecast. Enclosed transport keeps a collector car covered.'),
  P('A tornado warning parks the driver on the shoulder until it clears. Ice storms bring down the big oaks and the power lines a few times a decade. Interstate 35 closes for a day, and carriers wait for the plows and the line crews.'),
  P('The Fourth of July parade closes Broadway and the downtown blocks for the morning. The fireworks fill the campus that night. The monthly street festival closes Broadway on Saturday evenings from spring through fall. The arts festival fills the market in May.'),
  P('We schedule downtown pickups around those dates. The additions north of Danforth and the lake side run normally through all of it.'),
 )+chips(["Downtown Edmond","Broadway","University District","Oak Tree","Rose Creek","Fairfax","Coffee Creek","Twin Bridges","Huntwick","Kelly Lakes","Cheyenne Ridge","Deer Creek","Spring Creek","Hafer Park","Mitch Park","Arcadia Lake","Arcadia","Memorial Road","Quail Creek","The Village","Guthrie","Luther","Jones","Piedmont"])
 +NOTE('Serving Oklahoma and Logan Counties. Tell us the addition, the gate code if there is one, and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Edmond?',
 prose(
  L('Open transport carries most of Edmond, and the Interstate 35 lanes run on it every day.'),
  P('Enclosed transport keeps a car covered against hail, road grit, and the spring storms. The three-car garages on the north side hold a lot of collector cars and new luxury cars. Most of them ride enclosed.'),
  P('A commuter car rides open without trouble. Our <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages lay out each option.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a loading at the gate or on a section line, and a delivery. The hail forecast decides the timing.'),
  P('Once you approve the price, a carrier already running Interstate 35 takes the booking. At the gate, the driver marks up the car’s condition on a Bill of Lading. You sign it. Compare the car to that form at delivery before you sign again.'),
 )+ULI([
  "Remove personal belongings",
  "Keep about a quarter tank of fuel",
  "Photograph the vehicle before pickup, especially after a hail storm",
  "Provide a working key and disclose mechanical issues",
  "Disable aftermarket alarms",
  "For a gated addition, plan to meet the truck at the entrance or the clubhouse lot",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> guides take it step by step.'))))

BODY.append(sec('Why Ship Guy','Why Edmond Drivers Choose Ship Guy',
 prose(
  L('We work the Interstate 35 lane every day and plan around the gates, the hail, and the parade.'),
  P('Active FMCSA brokerage authority and a $75,000 surety bond stand behind every booking we make. Our office is on East Eleventh Street.'),
  P('One coordinator carries your shipment from quote to delivery and can book open, enclosed, or expedited transport. The <a href="services.html">services</a> page shows the full lineup.'),
 ), alt=True))

BODY.append(office('Edmond','2 E 11th St #522','Edmond, OK 73034','+14057809279','(405) 780-9279','CT',
 '2+E+11th+St+%23522,+Edmond,+OK+73034','Visit Us','Find Ship Guy in Edmond',
 'Our office is on East Eleventh Street a few blocks from Broadway, between downtown and the university.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5484.225882956063!2d-97.48236659999999!3d35.6423659!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x87b21fccf5d22a95%3A0x6d5e68a491d764f8!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792022849124!5m2!1sen!2sus'))

FAQ=[
 ("Can the carrier come inside my gated addition in Edmond?","Usually not. Oak Tree, Rose Creek, Fairfax, and the golf-course additions have lanes a loaded trailer cannot turn on. The driver meets you at the gate or in the clubhouse lot. Tell us the gate code or the guard arrangement when you book."),
 ("How much does it cost to ship a car from Edmond to Dallas or Fort Worth?","A sedan usually runs two hundred thirty to three hundred fifty dollars to either city. That is about two hundred twenty miles down Interstate 35. Houston runs four hundred to five hundred seventy. Larger vehicles add 10 to 25 percent."),
 ("Is the Turner Turnpike toll added to my price?","No. The carrier pays the Turner and Kilpatrick turnpikes and prices the trip accordingly. The toll is folded into the number you approve. Interstate 35 to Wichita and Dallas carries no toll."),
 ("What happens if hail is forecast on my pickup day?","We shift the window. A car waiting outside on a hail day is the real risk in Edmond. The north side has taken baseball-sized hail more than once. If a storm is already overhead, the driver pulls off and waits."),
 ("Do you handle a PCS move to Tinker from Edmond?","Yes. Many Tinker officers and contractors live in the north-side additions. The move order covers one car, and the second one rides with us. The base is gated, so the meeting spot sits outside it. Ship Guy is a private broker with no connection to the base."),
 ("Does the Fourth of July parade or the Saturday festival affect pickups?","Downtown, yes. The parade closes Broadway for the morning of the Fourth. The monthly festival closes Broadway on Saturday evenings from spring through fall. We schedule downtown pickups around those dates, and the rest of the city runs normally."),
 ("Can you ship a car for a UCO student?","Yes. Student cars arrive each August and leave each May. The campus streets east of downtown are tight on move-in days. The driver meets you on Second Street or a lot nearby. An adult signs for the car at pickup."),
 ("Can you pick up in Deer Creek or a brand-new addition?","Yes. Some streets in Deer Creek and the newest additions north of Covell are not on a carrier’s map. Send the full address and the nearest section line. The driver meets you on the paved road."),
 ("Can you ship a car that does not run from Edmond?","Yes. A winch-equipped carrier handles a car that will not start. The extra loading time is built into the quote. Tell us whether it rolls, steers, and brakes so we send the right truck."),
 ("What do you need for an Edmond car shipping quote?","Both addresses, with the addition and the gate on the Edmond end. The year, make, and model. Whether it runs and rolls. Open or enclosed, and the dates you can give us. That is a complete Edmond quote request."),
]
BODY.append(faq_section(FAQ,'Edmond FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Edmond?','Price the route on the form above in about two minutes. Tell us the addition and your dates. We will match you with a carrier already on Interstate 35.','+14057809279','(405) 780-9279','Get your free Edmond quote'))

build({
 'slug':'auto-transport-edmond-oklahoma',
 'title':'Car Shipping in Edmond, OK — Auto Transport | Ship Guy',
 'meta':'Car shipping in Edmond, OK on the Interstate 35 lane. Gated-addition handoffs, Broadway Extension and Turner Turnpike routing, UCO timing, Tinker families, hail and ice planning. Local office on East Eleventh Street. Free quote.',
 'h1':'Car Shipping in<br>Edmond, <span class="accent">Oklahoma</span>',
 'lede':'Open, enclosed, and expedited auto transport across the north metro, planned around the gates, the hail, and the commute.',
 'tel':'+14057809279','disp':'(405) 780-9279','brand':'Edmond','keyword':'car shipping in edmond',
 'localterms':['edmond','interstate 35','broadway extension','highway 77','kilpatrick','turner turnpike','interstate 44','interstate 40','second street','route 66','covell','danforth','fifteenth','waterloo','arcadia lake','round barn','oak tree','rose creek','fairfax','coffee creek','twin bridges','gated','association','three-car','downtown','broadway','university','deer creek','memorial road','energy','banking','software','tinker','hospital','christian university','hail','ice','tornado','parade','fourth of july','festival','arts festival','tulsa','wichita','dallas','fort worth','kansas city','denver'],
}, BODY, FAQ)
