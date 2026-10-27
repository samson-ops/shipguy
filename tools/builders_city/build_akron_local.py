import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Akron, Ohio','Car shipping in the rubber city, between the Turnpike and the Pittsburgh lane',
 ['Car shipping in Akron rides the same interstates the tire plants built their business on. Ship Guy is a licensed auto transport broker with an office on West Market Street in Fairlawn.',
  'We book vetted carriers across Summit County, from Cuyahoga Falls and Hudson to Green and the Portage Lakes. We do not own the trucks.',
  'Interstate 77 runs north to Cleveland and south to Canton. Interstate 76 runs east to Youngstown and the Pennsylvania Turnpike. The Ohio Turnpike passes north of the city, and Route 8 carries the north suburbs.',
  'This page covers the interchange and the Turnpike, the tire and polymer employers, and the neighborhoods. It also covers Canton and the enshrinement week, the winter, and the lanes.'],
 'Akron at a glance',
 ['Most pickups happen within 1 to 3 days. Carriers running between Cleveland and Pittsburgh pass the city every day.',
  'Cleveland, Canton, Youngstown, Pittsburgh, and Columbus are same-day lanes. Detroit, Buffalo, and Cincinnati take a day. Chicago runs one to two, and Florida runs three.'],
 'Tell us the neighborhood. Highland Square, North Hill, and downtown Hudson need a meeting spot. Fairlawn, Stow, and Green usually meet the truck at the curb.'))

BODY.append(sec('The Roads','Interstate 77, 76, the Central Interchange, and the Turnpike',
 prose(
  L('Akron sits forty minutes from Cleveland and under two hours from Pittsburgh. The carriers run both lanes daily.'),
  P('Interstate 77 runs from Cleveland through downtown to Canton and on to West Virginia. Interstate 76 crosses it at the Central Interchange and carries the Youngstown and Pittsburgh traffic. Route 8 runs north from the interchange through Cuyahoga Falls to Hudson and the Turnpike.'),
  P('The Ohio Turnpike passes north of the city with a toll by the mile. Interstate 271 reaches the east side of Cleveland. Interstate 76 west meets Interstate 71 toward Columbus, and Route 18 is Market Street through Fairlawn and Montrose.'),
  P('The Turnpike and the Pennsylvania Turnpike tolls are paid by the carrier and built into every quote. Interstate 77 and 76 charge nothing.'),
  P('Our office sits on West Market Street in Fairlawn, by the Montrose retail lots.'),
 ), alt=True))

BODY.append(sec('The Employers','Tires, Polymers, the Hospitals, and the Universities',
 prose(
  L('Akron ships on tire research, polymer labs, and two hospital systems, and the relocations follow the hiring.'),
  P('The tire headquarters on the east side and the research center downtown recruit engineers from across the country. The polymer companies around the university do the same. The utility headquarters downtown relocates staff on start dates.'),
  P('The two hospital systems and the children’s hospital bring in residents every June and July. The handoff happens on Market Street or Exchange Street rather than in a hospital garage.'),
  P('The university downtown and the one in Kent bring cars in each August. They send them home each May. The campus streets are tight, so the driver meets you at a lot nearby. An adult signs for a student car.'),
  P('If your employer reimburses the shipment, we send the documentation. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side of a move.'),
 )))

ROUTES=[("Cleveland, OH","I-77 · ~40 mi","Same day","$140–$220"),("Youngstown, OH","I-76 · ~50 mi","Same day","$140–$230"),
 ("Pittsburgh, PA","I-76 · ~110 mi","Same day","$170–$280"),("Columbus, OH","I-76/I-71 · ~125 mi","Same day","$180–$290"),
 ("Detroit, MI","I-80/I-75 · ~190 mi","Same day","$220–$340"),("Buffalo, NY","I-90 · ~200 mi","Same day","$230–$350"),
 ("Cincinnati, OH","I-71 · ~230 mi","1 day","$240–$360"),("Washington, DC","I-76/I-70 · ~340 mi","1 day","$320–$460"),
 ("Chicago, IL","I-80 · ~380 mi","1 day","$340–$480"),("Tampa, FL","I-77/I-95/I-4 · ~1,080 mi","3 days","$780–$1,100")]
BODY.append(rate_table('Lanes &amp; Costs','Akron Car Shipping Lanes and Estimated Costs',
 'The lanes that leave Akron most often, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a running sedan, open trailer, Turnpike tolls included. An SUV or pickup adds about 10 to 25 percent, and enclosed adds more again. Winter weather and the carriers available on your dates set the final price.',
 prose(
  P('Cleveland and Youngstown are local trips more than lanes, and Pittsburgh is under two hours on Interstate 76. Columbus rides Interstate 71 the same day.'),
  P('The Florida lane runs Interstate 77 down through the mountains to Charlotte and joins Interstate 95 there. The <a href="car-shipping-cost.html">cost guide</a> explains the rest of the number.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Highland Square, North Hill, Fairlawn, Hudson, and the Portage Lakes',
 prose(
  L('Akron is dense inside the expressways and open outside them, and the meeting spot follows that line.'),
  P('Highland Square, North Hill, and the blocks around the university have narrow streets with cars on both curbs. Downtown runs on garages. The driver meets you on Market Street, on Exchange, or at a lot near the Central Interchange.'),
  P('Firestone Park, Goodyear Heights, Kenmore, and Ellet are flatter blocks of bungalows with alley garages. The handoff happens on a main road nearby.'),
  P('Fairlawn, Copley, Bath, Stow, Tallmadge, and Green are wide suburban grids where the truck usually reaches the curb. Bath and the horse-farm roads wind, and the driver meets you on Cleveland-Massillon Road.'),
  P('Hudson has a tight historic downtown, and the handoff happens at a plaza on Route 91. The Portage Lakes sit on narrow lake roads south of the city. The carrier meets you on Manchester Road. Cuyahoga Falls and Barberton are open outside their downtowns.'),
 )))

BODY.append(sec('Canton &amp; the Calendar','Enshrinement Week, the Derby, the Marathon, and the Golf',
 prose(
  L('Akron and Canton share a carrier pool and a calendar of weeks when the roads fill.'),
  P('Enshrinement week fills Canton for the first week of August, and Interstate 77 south of the city crawls. The parade and the game close the streets around the hall. We schedule Canton and Green pickups before or after it.'),
  P('The soap box derby fills Derby Downs in July. The senior golf tournament fills the roads around the country club the same month. The marathon closes downtown on a Saturday in September.'),
  P('Winter is the bigger factor. Akron sits at the edge of the snow belt. Hudson, Stow, and the east side take the heavier bands. Interstate 77 and the Turnpike close to trucks a few times a season. A pickup can slide a day.'),
  P('Road salt runs from November through April. Spring brings the occasional tornado warning, and the driver pulls off until it passes.'),
 )+chips(["Downtown","Highland Square","West Akron","Wallhaven","North Hill","Firestone Park","Goodyear Heights","Kenmore","Ellet","Merriman Valley","Fairlawn","Montrose","Copley","Bath","Richfield","Cuyahoga Falls","Stow","Hudson","Tallmadge","Mogadore","Green","Norton","Barberton","Wadsworth","Portage Lakes","Kent","Canton","Massillon","Medina"])
 +NOTE('Serving Summit, Portage, Medina, and Stark Counties. Tell us the neighborhood, the month, and whether the car runs.'), alt=True))

BODY.append(sec('Your Options','Open or Enclosed in Akron?',
 prose(
  L('Akron ships open far more often than enclosed, and the 77 and 76 lanes reflect that.'),
  P('An enclosed trailer keeps salt, slush, and attention off the car. The garages in Bath, Hudson, and West Akron book enclosed trailers. A car headed to Florida for the winter often does too.'),
  P('A daily driver rides open and arrives fine. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages weigh the two choices.'),
 )))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a loading near the interchange, and a delivery. Winter has a say in the timing.'),
  P('Approve the price and we assign a carrier already running 77 or 76, then tell you the spot. At the spot, you and the driver walk the car together and fill in the Bill of Lading. Both sign. The delivery inspection goes line by line against it.'),
 )+ULI([
  "Remove personal belongings",
  "Keep about a quarter tank of fuel",
  "Take photos of the car before pickup, especially after a salty winter",
  "Leave a working key and tell us about any mechanical issues",
  "Switch off any aftermarket alarm",
  "In Highland Square, North Hill, or downtown Hudson, plan to meet the truck on a main road",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through the rest.')), alt=True))

BODY.append(sec('Why Ship Guy','Why Akron Drivers Choose Ship Guy',
 prose(
  L('We run the Cleveland and Pittsburgh lanes daily and plan around the snow belt and enshrinement week.'),
  P('Our FMCSA brokerage authority and $75,000 surety bond are both current and on the federal register. Our office is on West Market Street in Fairlawn.'),
  P('You deal with one coordinator the whole way, from the quote to the signature at delivery. Open, enclosed, and expedited transport are all available. The <a href="services.html">services</a> page describes each one.'),
 )))

BODY.append(office('Akron','3200 W Market St #780','Akron, OH 44333','+13306323174','(330) 632-3174','ET',
 '3200+W+Market+St+%23780,+Akron,+OH+44333','Visit Us','Find Ship Guy in Akron',
 'Our office is on West Market Street in Fairlawn, by the Montrose retail lots.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3709.471658122049!2d-81.6179738!3d41.1314348!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8830d10deadee50b%3A0x29bf10aef3c94e64!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792064661900!5m2!1sen!2sus'))

FAQ=[
 ("Is Akron priced the same as Cleveland?","Close to it. The two cities share a carrier pool and sit forty minutes apart on Interstate 77. A Fairlawn or Stow pickup prices like a Cleveland suburb. Canton and the Portage Lakes add a little for the extra miles."),
 ("Are the Turnpike tolls added to my price?","No. The carrier pays both turnpikes by the mile and prices the trip with them inside. Interstate 77 and 76 charge nothing. The number you approve is the number you pay."),
 ("How much does it cost to ship a car from Akron to Florida?","Count on seven hundred eighty to eleven hundred dollars for a sedan to Tampa. Orlando runs about the same, and Fort Myers adds a little. The route runs about eleven hundred miles down Interstate 77 and 95. November southbound costs more than spring. SUVs and pickups add 10 to 25 percent."),
 ("Can the carrier come to my house in Highland Square or North Hill?","Rarely. The streets are narrow and cars line both curbs. The driver meets you on Market Street, on Exchange, or at a lot near the Central Interchange. Fairlawn, Stow, Green, and Copley usually allow a curbside pickup."),
 ("Does enshrinement week affect pickups?","South of the city, yes. Interstate 77 toward Canton crawls for the first week of August. The streets around the hall close for the parade and the game. We schedule Canton and Green pickups before or after it."),
 ("Do you ship cars for residents at the Akron hospitals?","Yes, every June and July. The two hospital systems and the children’s hospital bring in residents from every state, most with a car. The handoff happens on Market Street or Exchange Street rather than in a hospital garage."),
 ("Can you ship a car for a University of Akron or Kent State student?","Yes. Student cars come in each August and go home each May. The campus streets are tight, so the driver meets you at a lot nearby. In Kent, that means Route 59 or the plaza by the campus. An adult signs for the car at pickup."),
 ("Does the snow belt reach Akron?","The edge of it. Hudson, Stow, and the east side take the heavier bands, and the west side sees less. Interstate 77 and the Turnpike close to trucks a few times a season. A winter pickup can slide a day. We call the moment the forecast changes the plan."),
 ("Can you ship a car that does not run from Akron?","Yes. We book a carrier with a winch, and the loading time goes into the price. In winter, dig it out before the truck arrives. Let us know whether it rolls, steers, and brakes."),
 ("What do you need for an Akron car shipping quote?","Both addresses, with the Akron neighborhood. Year, make, and model. Whether it runs. Open or enclosed. Your dates, with the month in mind. That is the whole Akron quote request."),
]
BODY.append(faq_section(FAQ,'Akron FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Akron?','Two minutes on the form above gets you a price. Tell us the neighborhood and your dates. We will pair you with a carrier already on Interstate 77.','+13306323174','(330) 632-3174','Get your free Akron quote'))

build({
 'slug':'auto-transport-akron-ohio',
 'title':'Car Shipping in Akron, OH — Auto Transport | Ship Guy',
 'meta':'Car shipping in Akron, OH on Interstate 77 and 76. Cleveland and Pittsburgh same-day lanes, Highland Square and Hudson handoffs, tire and polymer relocations, hospital and campus timing, enshrinement week, snow-belt planning, Turnpike tolls built in. Local office on West Market Street. Free quote.',
 'h1':'Car Shipping in<br>Akron, <span class="accent">Ohio</span>',
 'lede':'Open, enclosed, and expedited auto transport across Summit County, planned around the interchange, the snow belt, and the calendar.',
 'tel':'+13306323174','disp':'(330) 632-3174','brand':'Akron','keyword':'car shipping in akron',
 'localterms':['akron','interstate 77','interstate 76','central interchange','turnpike','route 8','interstate 271','route 18','market street','exchange','fairlawn','montrose','downtown','highland square','west akron','wallhaven','north hill','firestone park','goodyear heights','kenmore','ellet','merriman valley','copley','bath','cuyahoga falls','stow','hudson','tallmadge','green','barberton','portage lakes','kent','canton','massillon','tire','polymer','utility','hospital','children','residents','university','enshrinement','derby','golf','marathon','snow belt','salt','tornado','cleveland','youngstown','pittsburgh','columbus','detroit','buffalo','cincinnati','washington','chicago','tampa'],
}, BODY, FAQ)
