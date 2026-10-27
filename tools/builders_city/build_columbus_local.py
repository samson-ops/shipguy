import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Columbus, Ohio','Car shipping in the fastest-growing city in the Midwest, a day from half the country',
 ['Car shipping in Columbus is easy to book and hard to schedule in August. Ship Guy is a licensed auto transport broker with an office on South High Street downtown.',
  'We book vetted carriers across central Ohio, from Dublin and Westerville to Grove City, New Albany, and Delaware. We do not own the trucks.',
  'Interstate 70 and 71 cross downtown at the split. Interstate 270 loops the whole metro, and Route 315 carries the university traffic up the river. Six cities in three states sit within a few hours on those roads.',
  'This page covers the split and the Outerbelt, the university weeks, and the headquarters and the chip plant. It also covers the neighborhoods from German Village to Dublin, the fair and the stadium, and the lanes.'],
 'Columbus at a glance',
 ['Most pickups happen within 1 to 3 days. Carriers crossing the country on Interstate 70 pass the city all day.',
  'Cincinnati, Cleveland, Dayton, Indianapolis, Pittsburgh, Detroit, and Louisville are same-day lanes. Chicago, Nashville, and Washington take a day. Florida runs two to three.'],
 'Tell us the neighborhood and the week. German Village, the Short North, and Clintonville need a meeting spot. Dublin, Hilliard, and Westerville usually meet the truck at the curb.'))

BODY.append(sec('The Roads','The Split, the Outerbelt, 315, and 670',
 prose(
  L('Columbus sits on the one east-west interstate that crosses the whole country, and the carriers use it.'),
  P('Interstate 70 runs from Pittsburgh and Washington through the city to Indianapolis and beyond. Interstate 71 runs from Cleveland through downtown to Cincinnati and Louisville. The two share the split south of downtown, and the rebuild there slows the downtown ramps.'),
  P('Interstate 270 is the Outerbelt, fifty-five miles around the metro with an exit for every suburb. Interstate 670 carries the airport traffic through downtown. Route 315 runs up the Olentangy past the university to Worthington.'),
  P('Route 33 reaches Dublin and the plants in Marysville to the northwest and Lancaster to the southeast. Route 23 runs north to Delaware and south to Chillicothe. Route 161 reaches New Albany and the chip plant.'),
  P('High Street is the spine of the city for ten miles, and Broad Street crosses it downtown. None of the Columbus interstates charges a toll.'),
 ), alt=True))

BODY.append(sec('The University Weeks','Move-In, Move-Out, and Seven Saturdays',
 prose(
  L('The state university brings more cars to Columbus in one August week than most cities see all month.'),
  P('Move-in fills High Street, Lane Avenue, and Route 315 for a week in late August. The driver meets you on Olentangy River Road or by the Outerbelt, not near the dorms. The same thing happens in reverse in early May.'),
  P('Seven home football Saturdays each fall close the streets around the stadium. Route 315 and Interstate 71 fill for hours. We schedule campus-area pickups on another day of that week.'),
  P('The medical center on the campus brings in residents every June and July. Most arrive with a car from out of state. The handoff happens on Olentangy River Road rather than in a hospital garage. An adult signs for a student car.'),
 )))

ROUTES=[("Dayton, OH","I-70 · ~70 mi","Same day","$150–$250"),("Cincinnati, OH","I-71 · ~110 mi","Same day","$170–$280"),
 ("Cleveland, OH","I-71 · ~145 mi","Same day","$200–$320"),("Indianapolis, IN","I-70 · ~175 mi","Same day","$220–$340"),
 ("Pittsburgh, PA","I-70/I-79 · ~185 mi","Same day","$220–$340"),("Louisville, KY","I-71 · ~210 mi","Same day","$230–$350"),
 ("Nashville, TN","I-71/I-65 · ~380 mi","1 day","$340–$490"),("Charlotte, NC","US-23/I-77 · ~430 mi","1 day","$380–$540"),
 ("New York, NY","I-70/I-76 · ~535 mi","1–2 days","$450–$640"),("Orlando, FL","I-75 · ~940 mi","2–3 days","$700–$1,000")]
BODY.append(rate_table('Lanes &amp; Costs','Columbus Car Shipping Lanes and Estimated Costs',
 'Where Columbus cars go most often, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a running sedan on an open trailer. Add roughly 10 to 25 percent for an SUV or pickup, more for enclosed. Move-in week, the season, and carrier availability on your dates decide the final number.',
 prose(
  P('Dayton and Cincinnati are the quick lanes. The Ohio triangle on Interstate 71 prices like a local trip. Interstate 70 carries Pittsburgh and Indianapolis the same day in either direction.'),
  P('The Florida lane joins Interstate 75 at Cincinnati and swings with the fall migration. The <a href="car-shipping-cost.html">cost guide</a> explains the rest of the number.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Headquarters, the Chip Plant, the Banks, and the State',
 prose(
  L('Columbus adds people faster than any city in the Midwest. Most of them arrive with a car and a start date.'),
  P('The insurance and banking headquarters downtown transfer staff in on start dates. The retail headquarters on the east side does the same. The bank operations center at Polaris and the health-care logistics company in Dublin do the same.'),
  P('The chip plant rising in New Albany draws engineers from Arizona, Oregon, and Texas. The data centers around it and the auto plants in Marysville add more. If your employer reimburses the shipment, we send the documentation it asks for.'),
  P('State government hires on its own calendar, and the agencies downtown relocate people all year. The defense supply center on the east side and the air wing at Rickenbacker rotate families on orders. The second vehicle usually rides with us, and the <a href="military-car-shipping.html">military</a> page covers the planning.'),
  P('The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side of a relocation.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','German Village, the Short North, Clintonville, Bexley, and the Suburbs',
 prose(
  L('Columbus is brick streets inside the Outerbelt and wide subdivisions outside it. The meeting spot follows that line.'),
  P('German Village and the Brewery District run on brick streets a trailer cannot turn on. The Short North, Victorian Village, and Italian Village are the same with bars on every corner. The driver meets you on Front Street, on Parsons Avenue, or at a lot by the split. Our office sits on South High Street at the edge of it.'),
  P('Clintonville, the University District, and Grandview have narrow streets with cars on both curbs. Upper Arlington and Bexley wind through old trees with no truck access. The handoff happens on High Street, Broad Street, or Olentangy River Road.'),
  P('Dublin, Hilliard, Westerville, Gahanna, Grove City, and Reynoldsburg are wide grids where the truck usually reaches the curb. New Albany, Powell, and Lewis Center are new construction. Some streets are not on a carrier’s map yet. Send the full address.'),
  P('Delaware, Lancaster, and Newark sit thirty minutes out on the state routes. They schedule in a day or two.'),
 )))

BODY.append(sec('The Calendar &amp; the Weather','The State Fair, the Arnold, the Memorial, and the Winter',
 prose(
  L('Columbus fills for a fair, a fitness expo, and a golf tournament. The carriers plan around all three.'),
  P('The state fair fills the fairgrounds on Seventeenth Avenue for twelve days around the start of August. The Interstate 71 ramps crawl. The fitness expo takes over downtown for a weekend in early March. The golf tournament fills Dublin in early June.'),
  P('We schedule the affected neighborhoods around those dates. The marathon closes downtown and the north side on a Sunday in October.'),
  P('Winter brings ice and a few heavy snows. Interstate 70 closes for a day a few times a season. Spring brings storms and the occasional tornado warning, and the driver pulls off until it passes. Summer is the easy season outside of move-in week.'),
 )+chips(["Downtown","German Village","Brewery District","Short North","Victorian Village","Italian Village","Olde Towne East","Franklinton","Clintonville","University District","Grandview Heights","Upper Arlington","Bexley","Worthington","Westerville","Dublin","Hilliard","Gahanna","New Albany","Powell","Lewis Center","Polaris","Easton","Reynoldsburg","Pickerington","Grove City","Canal Winchester","Delaware","Lancaster","Marysville"])
 +NOTE('Serving Franklin, Delaware, Union, Licking, and Fairfield Counties. Tell us the neighborhood and the week, especially in August.'), alt=True))

BODY.append(sec('Your Options','Open or Enclosed in Columbus?',
 prose(
  L('Nine out of ten Columbus cars ride open, and the 70 and 71 lanes are priced for it.'),
  P('An enclosed trailer keeps salt, grit, and attention off the car. The garages in Upper Arlington, Bexley, and New Albany book enclosed trailers. So do the collector cars headed to the auctions.'),
  P('The car you commute in does not need a roof for the trip. Compare the two on the <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages.'),
 )))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a loading near the Outerbelt, and a delivery. The calendar decides the week.'),
  P('When you approve the price, we assign a carrier already working 70 or 71 and name the spot. You and the driver fill in a Bill of Lading there and both sign it. The car is inspected against that sheet at delivery.'),
 )+ULI([
  "Remove personal belongings",
  "Keep about a quarter tank of fuel",
  "Photograph the vehicle before pickup, especially after a salty winter",
  "Provide a working key and disclose mechanical issues",
  "Disable aftermarket alarms",
  "During move-in week or on a game Saturday, plan to meet the truck away from the campus",
 ])+prose(P('Everything else is on the <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages.')), alt=True))

BODY.append(sec('Why Ship Guy','Why Columbus Drivers Choose Ship Guy',
 prose(
  L('We work 70 and 71 every day and plan around the campus, the fair, and the growth.'),
  P('Our brokerage authority is active with the FMCSA and our $75,000 surety bond is filed. Our office is on South High Street downtown.'),
  P('One coordinator sees your shipment through from the quote to the delivery signature. Open, enclosed, and expedited transport are all available, and the <a href="services.html">services</a> page lists each.'),
 )))

BODY.append(office('Columbus','338 S High St #968','Columbus, OH 43215','+13802621289','(380) 262-1289','ET',
 '338+S+High+St+%23968,+Columbus,+OH+43215','Visit Us','Find Ship Guy in Columbus',
 'Our office is on South High Street downtown, between the Statehouse and German Village.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3775.1896274531737!2d-82.9989331!3d39.95522309999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x88388f7013a7d93d%3A0xde6fd3b395e47620!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792064678441!5m2!1sen!2sus'))

FAQ=[
 ("Can you ship a car for an Ohio State student?","Yes. Student cars arrive in late August and leave in early May. Move-in week fills High Street, Lane Avenue, and Route 315. The driver meets you at a lot on Olentangy River Road or near the Outerbelt. An adult signs for the car at pickup."),
 ("Does a home football Saturday affect my pickup?","Yes, if it falls on one. The streets around the stadium close, and Route 315 and Interstate 71 fill for hours. We schedule campus-area pickups on another day of that week. The suburbs run normally."),
 ("How much does it cost to ship a car from Columbus to Florida?","Plan on seven hundred to one thousand dollars for a sedan to Orlando or Tampa. The run is about nine hundred forty miles down Interstate 71 and 75. Fall southbound prices run above spring. SUVs and pickups add 10 to 25 percent."),
 ("Can the carrier come to my house in German Village or Clintonville?","Rarely. German Village runs on brick streets a trailer cannot turn on, and Clintonville parks solid on both curbs. The driver meets you on Front Street, Parsons Avenue, High Street, or at a lot by the split. Dublin, Hilliard, and Westerville usually allow curbside."),
 ("Do you handle relocations to the chip plant or the headquarters?","Yes, every week. The chip plant in New Albany, the data centers, and the downtown headquarters all hire on start dates. We plan the pickup around your first day. If your employer reimburses the shipment, we send the paperwork."),
 ("Do you handle a move to Rickenbacker or the defense supply center?","Yes. Both rotate families on orders, and the second vehicle usually rides with us. The base is gated, so the handoff happens outside it. Ship Guy is a private broker with no connection to either one."),
 ("Does the state fair affect pickups?","Near the fairgrounds, yes. Seventeenth Avenue and the Interstate 71 ramps crawl for twelve days in late July and early August. We schedule north-side pickups around it. The rest of the metro runs normally."),
 ("Can you pick up in New Albany, Powell, or a brand-new subdivision?","Yes. Some streets out there are not on a carrier’s map yet. Send the full address and the nearest main road, and the driver meets you on the pavement. Most of those streets are wide enough for the curb."),
 ("Can you ship a car that does not run from Columbus?","Yes. A winch-equipped truck takes it, and the longer loading is built into the price. In winter, have the car cleared and reachable. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Columbus car shipping quote?","The two addresses, with the Columbus neighborhood. The year, make, and model. Whether it runs and rolls. Open or enclosed, and the dates you can work with, especially in August. A Columbus quote needs nothing else."),
]
BODY.append(faq_section(FAQ,'Columbus FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Columbus?','The form above prices the lane in about two minutes. Add the neighborhood and your dates. We will pair you with a carrier already on 70 or 71.','+13802621289','(380) 262-1289','Get your free Columbus quote'))

build({
 'slug':'auto-transport-columbus-ohio',
 'title':'Car Shipping in Columbus, OH — Auto Transport | Ship Guy',
 'meta':'Car shipping in Columbus, OH on Interstate 70 and 71. Ohio State move-in and game-day planning, German Village and Clintonville handoffs, chip plant and headquarters relocations, Rickenbacker moves, state fair timing, the Florida lane. Local office on South High Street. Free quote.',
 'h1':'Car Shipping in<br>Columbus, <span class="accent">Ohio</span>',
 'lede':'Open, enclosed, and expedited auto transport across central Ohio, planned around the split, the campus, and the growth.',
 'tel':'+13802621289','disp':'(380) 262-1289','brand':'Columbus','keyword':'car shipping in columbus',
 'localterms':['columbus','interstate 70','interstate 71','interstate 270','outerbelt','interstate 670','route 315','olentangy','route 33','route 23','route 161','high street','broad street','the split','downtown','german village','brewery district','short north','victorian village','italian village','franklinton','clintonville','university district','grandview','upper arlington','bexley','worthington','westerville','dublin','hilliard','gahanna','new albany','powell','lewis center','polaris','easton','reynoldsburg','grove city','delaware','lancaster','marysville','state university','move-in','football','stadium','medical center','residents','insurance','banking','retail','chip plant','data centers','state government','defense supply','rickenbacker','state fair','fairgrounds','fitness expo','golf','marathon','ice','tornado','dayton','cincinnati','cleveland','indianapolis','pittsburgh','louisville','nashville','charlotte','new york','orlando'],
}, BODY, FAQ)
