import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Dayton, Ohio','Car shipping at the crossroads of 70 and 75, on the Air Force calendar',
 ['Car shipping in Dayton runs on orders more than on any other calendar. Ship Guy is a licensed auto transport broker with an office on North Ludlow Street downtown.',
  'We book vetted carriers across the Miami Valley, from Huber Heights and Beavercreek to Kettering, Centerville, and Miamisburg. We do not own the trucks.',
  'Interstate 75 runs through downtown. Interstate 70 crosses it north of the city at one of the busiest interchanges in the country. Interstate 675 loops the east side past the base. Route 35 crosses the middle of the city.',
  'This page covers the crossroads, the base and the orders, and the neighborhoods from Oakwood to Huber Heights. It also covers the hospitals and the glass plant, the air show, the storm history, and the lanes.'],
 'Dayton at a glance',
 ['Most pickups happen within 1 to 3 days. Carriers on both interstates pass the city all day.',
  'Cincinnati, Columbus, Indianapolis, Lexington, and Louisville are same-day lanes. Detroit, Cleveland, and Chicago take a day. Florida runs two to three.'],
 'Tell us the neighborhood and the gate. The base housing is gated and Oakwood bans the truck. Kettering and Beavercreek usually meet it at the curb.'))

BODY.append(sec('The Crossroads','Interstate 75, 70, 675, and Route 35',
 prose(
  L('Dayton is where the Detroit-to-Florida lane crosses the Pittsburgh-to-Indianapolis lane, and the carriers never leave.'),
  P('Interstate 75 runs north to Toledo and Detroit and south to Cincinnati, Atlanta, and Florida. Interstate 70 runs east to Columbus and west to Indianapolis. The two cross in Vandalia north of the city, and the airport sits at the interchange.'),
  P('Interstate 675 leaves 75 south of the city. It loops through Kettering and Beavercreek to the base and back to 70. Route 35 crosses the city east to Xenia and west toward Eaton. Route 4 reaches Huber Heights and Springfield.'),
  P('None of the Dayton roads charges a toll. The rebuilt stretch of 75 through downtown moves well. The Vandalia interchange is the only place the carriers slow.'),
  P('Our office sits on North Ludlow Street downtown, a few blocks from the 75 ramps and Route 35.'),
 ), alt=True))

BODY.append(sec('The Base','Wright-Patterson, the Orders, and the Second Vehicle',
 prose(
  L('The largest Air Force base in the country sits on the east side of Dayton. It moves families every week of the year.'),
  P('The base houses the research labs, the materiel command, and the institute of technology. It rotates airmen, civilians, and contractors with a summer peak. Most families arrive from Texas, Virginia, Colorado, or Georgia with two cars. The orders pay to move one.'),
  P('The second vehicle rides with us. The gates are controlled. The driver meets you outside them in Fairborn, Riverside, or Huber Heights, or on Route 444. We plan the pickup around the report date.'),
  P('Ship Guy is a private broker with no connection to the base or any command. The <a href="military-car-shipping.html">military</a> page covers the timing of a PCS move in detail.'),
  P('The San Antonio, Colorado Springs, Washington, and Warner Robins lanes run out of Dayton every month. The same families rotate between the same bases.'),
 )))

ROUTES=[("Cincinnati, OH","I-75 · ~55 mi","Same day","$140–$230"),("Columbus, OH","I-70 · ~70 mi","Same day","$150–$250"),
 ("Indianapolis, IN","I-70 · ~115 mi","Same day","$170–$280"),("Lexington, KY","I-75 · ~140 mi","Same day","$190–$300"),
 ("Louisville, KY","I-75/I-71 · ~160 mi","Same day","$210–$320"),("Detroit, MI","I-75 · ~210 mi","Same day","$230–$350"),
 ("Chicago, IL","I-70/I-65 · ~290 mi","1 day","$280–$410"),("Washington, DC","I-70 · ~480 mi","1 day","$420–$600"),
 ("San Antonio, TX","I-70/I-44/I-35 · ~1,250 mi","3 days","$850–$1,200"),("Tampa, FL","I-75 · ~900 mi","2–3 days","$680–$970")]
BODY.append(rate_table('Lanes &amp; Costs','Dayton Car Shipping Lanes and Estimated Costs',
 'Where Dayton cars go most often, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a running sedan on an open trailer. Add roughly 10 to 25 percent for an SUV or pickup, more for enclosed. The season and the carriers available on your dates decide the final number.',
 prose(
  P('Cincinnati and Columbus are an hour away in opposite directions. Five more cities sit within a same-day run. Interstate 75 carries the Florida traffic straight south.'),
  P('The base lanes to Texas and Colorado run on Interstate 70 and 44. The summer rotation keeps them busy. The <a href="car-shipping-cost.html">cost guide</a> explains the rest of the number.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Oakwood, the Oregon District, Kettering, Beavercreek, and Huber Heights',
 prose(
  L('Dayton has a few neighborhoods built for carriages and many built for cars. The meeting spot follows that line.'),
  P('The Oregon District, South Park, and the historic blocks east of downtown are narrow and parked solid. Downtown runs on garages. The driver meets you on Main Street, on Keowee, or at a lot by the 75 ramps.'),
  P('Oakwood winds under old trees with no truck access, and the handoff happens on Far Hills Avenue. Dayton View and Belmont are tight near the river and open toward the suburbs.'),
  P('Kettering, Beavercreek, Centerville, Springboro, and Miamisburg are wide grids where the truck usually reaches the curb. Huber Heights, Fairborn, and Riverside sit by the base and schedule the same way.'),
  P('Vandalia, Englewood, and Tipp City sit on the interstates north of the city. Xenia, Springfield, and Troy are thirty minutes out and schedule in a day or two.'),
 ), alt=True))

BODY.append(sec('Who Else Moves Here','The Hospitals, the Universities, the Glass Plant, and the Engine Plant',
 prose(
  L('Outside the gate, Dayton ships on two hospital systems, two universities, and two plants that hire from everywhere.'),
  P('The two hospital systems bring in residents every June and July. The handoff happens on Brown Street or Far Hills rather than in a hospital garage. The university on Brown Street and the one in Fairborn bring cars in each August. They send them home each May.'),
  P('The glass plant in Moraine and the engine plant up Interstate 75 transfer engineers in on start dates. The software and health-insurance companies downtown and in Miamisburg do the same.'),
  P('If your employer reimburses the shipment, we send the documentation it asks for. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side of a move.'),
 )))

BODY.append(sec('The Weather &amp; the Calendar','Tornadoes, the Air Show, Hamvention, and the Winter',
 prose(
  L('Dayton’s weather problem arrives in spring, and its traffic problem arrives in a jet.'),
  P('The Miami Valley sits in a tornado corridor. The outbreak on Memorial Day a few years back closed Interstate 75 and tore through Trotwood and Beavercreek. When a warning is issued, the driver pulls off and waits. Spring pickups carry a cushion for that.'),
  P('The air show fills Vandalia and the 70 and 75 interchange for a weekend in June. The radio convention fills Xenia for a weekend in May. We schedule north-side and Xenia pickups around both.'),
  P('Winter brings ice more than deep snow. Interstate 75 closes for a day a few times a season. Road salt runs from November through March. Summer humidity is the easy season.'),
 )+chips(["Downtown","Oregon District","St. Anne's Hill","South Park","Dayton View","Belmont","Walnut Hills","Old North Dayton","Riverside","Huber Heights","Fairborn","Beavercreek","Kettering","Oakwood","Centerville","Washington Township","Springboro","Miamisburg","West Carrollton","Moraine","Vandalia","Englewood","Trotwood","Tipp City","Troy","Xenia","Springfield","Yellow Springs"])
 +NOTE('Serving Montgomery, Greene, Miami, and Warren Counties. Tell us the neighborhood, the gate, and the report date if there is one.'), alt=True))

BODY.append(sec('Your Options','Open or Enclosed in Dayton?',
 prose(
  L('Open is the default in Dayton, and the price on the 75 lanes assumes it.'),
  P('An enclosed trailer keeps salt, hail, and attention off the car. The garages in Oakwood and Centerville book enclosed trailers. So do the collector cars headed to the summer shows.'),
  P('A commuter car arrives fine on an open trailer. Our <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages lay out when the roof is worth paying for.'),
 )))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a loading outside the gate or near the interstate, and a delivery. The report date decides the week.'),
  P('Once the price is approved, a carrier already working 75 or 70 gets the booking. We name the spot. The driver inspects the car with you there and records it on a Bill of Lading. Both of you sign, and that record governs the delivery check.'),
 )+ULI([
  "Clear out personal belongings",
  "Leave about a quarter tank of fuel in it",
  "Photograph the vehicle before pickup, especially after a hail storm",
  "Hand over a working key and mention any mechanical issues",
  "Turn off any aftermarket alarm",
  "For base housing, plan to meet the truck outside the gate or at a lot on Route 444",
 ])+prose(P('Our <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages fill in the details.')), alt=True))

BODY.append(sec('Why Ship Guy','Why Dayton Drivers Choose Ship Guy',
 prose(
  L('We work both interstates every day and plan around the orders, the storms, and the air show.'),
  P('Our brokerage authority is active with the FMCSA, and the $75,000 surety bond behind it is on file. Our office is on North Ludlow Street downtown.'),
  P('The coordinator who quotes your move is the one who sees it delivered. Open, enclosed, and expedited transport are all on offer, and the <a href="services.html">services</a> page explains each.'),
 )))

BODY.append(office('Dayton','131 N Ludlow St #981','Dayton, OH 45402','+19378065751','(937) 806-5751','ET',
 '131+N+Ludlow+St+%23981,+Dayton,+OH+45402','Visit Us','Find Ship Guy in Dayton',
 'Our office is on North Ludlow Street downtown, a few blocks from the Interstate 75 ramps.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3785.8524307599896!2d-84.1944436!3d39.7616663!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8840818a019d9bdf%3A0x842dfd243fc65531!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792064646166!5m2!1sen!2sus'))

FAQ=[
 ("Do you handle a PCS move to or from Wright-Patterson?","Yes, every week. Orders usually pay to move one vehicle, and the second one rides with us. The gates are controlled. The driver meets you in Fairborn, Riverside, or Huber Heights, or on Route 444. We plan around the report date. Ship Guy is a private broker with no connection to the base."),
 ("How much does it cost to ship a car from Dayton to San Antonio or Colorado Springs?","San Antonio usually runs eight hundred fifty to twelve hundred dollars for a sedan. That is about twelve hundred fifty miles on Interstate 70, 44, and 35. Colorado Springs runs about the same. Summer rotation season pushes both up. SUVs and pickups add 10 to 25 percent."),
 ("How much does it cost to ship a car from Dayton to Florida?","Six hundred eighty to nine hundred seventy dollars for a sedan to Tampa is typical. Orlando runs about the same. The route is about nine hundred miles straight down Interstate 75. Fall southbound costs more than spring."),
 ("Can the carrier come to my house in Oakwood or the Oregon District?","No. Oakwood bans trucks on its winding streets, and the Oregon District parks solid on both curbs. The driver meets you on Far Hills Avenue, Main Street, or at a lot by the 75 ramps. Kettering, Beavercreek, and Centerville usually allow curbside."),
 ("What happens if a tornado warning is issued during my pickup?","The driver pulls off and waits for the all-clear. The pickup can slide a few hours or a day. The Miami Valley sits in a tornado corridor, and spring bookings carry a cushion for it."),
 ("Does the air show affect pickups?","On the north side, yes. Vandalia and the 70 and 75 interchange fill for the June weekend, and the airport roads close. We schedule north-side pickups around it. The rest of the metro runs normally."),
 ("Do you ship cars for residents at the Dayton hospitals?","Yes, every June and July. Both hospital systems bring in residents from every state, most with a car. The handoff happens on Brown Street or Far Hills rather than in a hospital garage."),
 ("Can you ship a car for a University of Dayton or Wright State student?","Yes. Student cars come in each August and go home each May. The streets around Brown Street are tight, so the driver meets you at a lot nearby. In Fairborn, the handoff happens on Colonel Glenn Highway. An adult signs for the car at pickup."),
 ("Can you ship a car that does not run from Dayton?","Yes. The carrier we send brings a winch, and the slower loading is part of the quote. Tell us whether it rolls, steers, and brakes, since that decides the equipment."),
 ("What do you need for a Dayton car shipping quote?","The two addresses, with the Dayton neighborhood or the gate. The year, make, and model. Whether it runs and rolls. Open or enclosed, and the dates you can work with, plus the report date if there is one. A Dayton quote needs nothing else."),
]
BODY.append(faq_section(FAQ,'Dayton FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Dayton?','Run the form above and you have a price in about two minutes. Add the neighborhood and your dates, and a carrier already on 75 or 70 takes it from there.','+19378065751','(937) 806-5751','Get your free Dayton quote'))

build({
 'slug':'auto-transport-dayton-ohio',
 'title':'Car Shipping in Dayton, OH — Auto Transport | Ship Guy',
 'meta':'Car shipping in Dayton, OH at the Interstate 70 and 75 crossroads. Wright-Patterson PCS moves and the second vehicle, Oakwood and Oregon District handoffs, hospital and university timing, tornado-season planning, air show week, the Florida lane. Local office on North Ludlow Street. Free quote.',
 'h1':'Car Shipping in<br>Dayton, <span class="accent">Ohio</span>',
 'lede':'Open, enclosed, and expedited auto transport across the Miami Valley, planned around the base, the crossroads, and the storms.',
 'tel':'+19378065751','disp':'(937) 806-5751','brand':'Dayton','keyword':'car shipping in dayton',
 'localterms':['dayton','interstate 75','interstate 70','interstate 675','route 35','route 4','route 444','vandalia','airport','ludlow','main street','keowee','downtown','oregon district','south park','dayton view','belmont','oakwood','far hills','kettering','beavercreek','centerville','springboro','miamisburg','moraine','huber heights','fairborn','riverside','englewood','trotwood','tipp city','troy','xenia','springfield','wright-patterson','base','orders','gate','report date','research labs','materiel','second vehicle','san antonio','colorado springs','warner robins','hospital','residents','university','brown street','glass plant','engine plant','software','health-insurance','tornado','air show','radio convention','ice','salt','cincinnati','columbus','indianapolis','lexington','louisville','detroit','chicago','washington','tampa'],
}, BODY, FAQ)
