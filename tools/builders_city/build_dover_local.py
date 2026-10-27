import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Dover, Delaware','Car shipping in a state capital with no interstate, where Route 1 and US 13 do the work',
 ['Car shipping in Dover starts on the DuPont Highway, the strip that carries every truck through town. Ship Guy is a licensed auto transport broker with an office on West Division Street downtown.',
  'We book vetted carriers across Kent County, from Smyrna to Harrington and out to the bay. We do not own the trucks.',
  'Route 1 is the toll road from the canal to the beaches. It passes the east side of the city. US 13 is the DuPont Highway, free and slower, and it runs straight through. Route 8 is Division Street, the road west to the Maryland line.',
  'This page covers the two highways, the base gates, downtown, the subdivisions, and the bayside towns. It also covers the state government, the air base, the plants, the university, the speedway, and the lanes.'],
 'Dover at a glance',
 ['Most pickups happen within 1 to 3 days along the highways. The farm roads and the bayside towns run 2 to 4. The corridor carriers leave 95 at the canal and come down Route 1 or US 13.',
  'Wilmington, Philadelphia, and Baltimore are same-day lanes. Washington is the same day too. New York and Norfolk take a day. Richmond takes one, and Florida takes three.'],
 'Tell us the neighborhood. Downtown, the Green, and the base need a meeting spot. Rodney Village, Fox Hall, and the newer subdivisions usually allow the curb.'))

BODY.append(sec('The Roads','Route 1, US 13, Route 8, and the Toll Plaza South of Town',
 prose(
  L('Dover is one of the few state capitals with no interstate. The carriers reach it on two highways and a toll.'),
  P('Route 1 leaves Interstate 95 at Christiana and crosses the canal on the Roth Bridge. It runs down the east side of Dover past the air base. The toll plaza sits just south of town, and the Biddles Corner plaza sits north of Smyrna. Carriers pay both or take US 13.'),
  P('US 13 is the DuPont Highway. It crosses the whole state toll-free and turns into the retail strip through Dover. The mall, the car dealers, and the hotels line it. Most carriers that pick up in Dover come down 13, because the strip has room to stop.'),
  P('Route 8 is Division Street. It runs west through farm country to the Maryland line at Marydel. East, it reaches Little Creek and the bay. Route 10 runs from Camden to the base. US 113 splits off 13 south of town for Milford and the beaches. Route 9 follows the bay through Leipsic and Little Creek.'),
  P('The carriers come off Route 1 at Division Street for downtown and at Route 10 for the base. The lots along the DuPont Highway, at the mall, and by the speedway are the usual meeting spots. Our office sits on West Division Street downtown, a few blocks north of the Green.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the Green, the Base, the Subdivisions, and the Bayside Towns',
 prose(
  L('Dover is a colonial green, a government complex, a retail strip, and a ring of subdivisions. Each parks differently.'),
  P('The Green and the blocks around Legislative Hall are the oldest streets in the state. They are narrow, brick, and full of state cars from January to June. A trailer cannot stop there. The driver meets you on Loockerman Street, at a lot off State Street, or on the DuPont Highway.'),
  P('The air base fills the southeast corner of the city. Its housing sits behind the gates, and the truck stops at the gate. The handoff happens at a lot outside the main gate on Route 1 or in town. Airmen know the drill, and the drivers know the gate.'),
  P('Rodney Village, Capitol Park, Mayfair, and Fox Hall are postwar grids and cul-de-sacs around the city. The truck usually reaches the curb. The newer subdivisions off Route 8 and down Route 10 in Camden have wide streets. The answer is the same. The university campus on the north side has big lots off 13.'),
  P('Smyrna, Camden, Wyoming, Magnolia, Frederica, and Harrington are the county towns. Each has a grid downtown and farms beyond it. Leipsic, Little Creek, Bowers Beach, and Kitts Hummock sit on the bay down long marsh roads. The driver meets a bayside pickup on Route 9 or Route 1. The Amish farms west of town share their roads with buggies. The truck stays on Route 8.'),
 )))

ROUTES=[("Wilmington, DE","Route 1/US-13 · ~50 mi","Same day","$130–$220"),("Philadelphia, PA","Route 1/I-95 · ~80 mi","Same day","$150–$250"),
 ("Baltimore, MD","US-301/US-50 · ~100 mi","Same day","$160–$270"),("Washington, DC","US-301/US-50 · ~100 mi","Same day","$170–$280"),
 ("New York, NY","Route 1/NJ Tpke · ~170 mi","Same day","$190–$300"),("Norfolk, VA","US-13/CBBT · ~170 mi","1 day","$200–$320"),
 ("Richmond, VA","US-301/I-95 · ~200 mi","1 day","$220–$340"),("Raleigh, NC","US-301/I-95 · ~330 mi","1 day","$310–$450"),
 ("Chicago, IL","I-76/I-80 · ~800 mi","2 days","$570–$830"),("Orlando, FL","I-95 · ~950 mi","3 days","$700–$990")]
BODY.append(rate_table('Lanes &amp; Costs','Dover Car Shipping Lanes and Estimated Costs',
 'The lanes that leave Kent County most, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a sedan that runs, on an open trailer, priced from Dover. Add about 10 to 25 percent for an SUV or pickup, and more for enclosed. The Route 1 tolls are in the figure. The base calendar and the carriers free on your dates set the final price.',
 prose(
  P('Dover prices a little above Wilmington on every lane, because the carrier leaves the corridor to reach it. The fifty miles down Route 1 or 13 add a day to some pickups and a few dollars.'),
  P('The base keeps the Texas, California, and Carolina lanes busy every summer. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Air Base, the State, the University, the Plants, and the Speedway',
 prose(
  L('Dover relocates airmen, state employees, students, and plant engineers, and the base calendar runs the year.'),
  P('Dover Air Force Base flies the biggest cargo planes in the fleet, and it moves families all year. Aircrews, loadmasters, and maintainers rotate through with their families, and the peak is summer. Orders cover one car, and the second one comes with us. The truck stops at the gate, so the handoff happens on Route 1 or in town.'),
  P('Ship Guy is a private broker with no connection to the base. The <a href="military-car-shipping.html">military</a> page explains the timing around a report date.'),
  P('The state is the biggest employer in town, and the agencies hire on their own calendar. The session runs January through June, and the staff arrive before it. The university on the north side brings cars in each August and out each May. The campus lots off 13 work for the handoff, and an adult signs for a student car.'),
  P('The plants along the highway make wipes, desserts, and household goods. They relocate engineers on program schedules. The hospital downtown brings in nurses and residents every summer. The casino and the speedway hire on the race calendar. We provide the paperwork a reimbursed move needs, and the <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Race Weekend, the Session, Nor’easters, and the Bay',
 prose(
  L('Dover has three calendars. The base, the legislature, and the speedway each fill the town in turn.'),
  P('Race weekend at the Monster Mile fills every hotel in the county. Route 1 and 13 jam for three days. A pickup in Dover moves to another day. The state fair in Harrington does the same for ten days in late July.'),
  P('The legislative session runs from January to the end of June. Downtown parking disappears on session days, and the Green fills with state cars. Dover Days closes the Green for a weekend in early May. We move a downtown pickup to the DuPont Highway for each.'),
  P('Nor’easters push the bay into Bowers Beach, Kitts Hummock, and Leipsic a few times each year. Sandy in 2012 flooded the bayside towns. A bayside pickup moves to Route 1 until the tide drops. Snow is lighter here than in Wilmington, but an ice storm still holds a trailer for a day.'),
  P('Summer brings humidity, thunderstorms, and beach traffic on Route 1 from Memorial Day through Labor Day. The carriers come down 13 instead on summer Fridays. The loading hour moves to early morning in July and August.'),
 )+chips(["Downtown","The Green","Loockerman Street","Legislative Hall","DuPont Highway","Rodney Village","Capitol Park","Mayfair","Fox Hall","Kent Acres","Woodbrook","Dover AFB","Camden","Wyoming","Cheswold","Smyrna","Clayton","Magnolia","Frederica","Felton","Harrington","Milford","Marydel","Hartly","Little Creek","Leipsic","Bowers Beach","Kitts Hummock"])
 +NOTE('Serving Dover and every town in Kent County, highway, farm road, or bayside. Tell us the neighborhood, the gate, and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Dover?',
 prose(
  L('Open is how Kent County ships, and the base lanes are priced for it.'),
  P('An enclosed trailer keeps the salt air, the road grit, and attention off a car. Airmen with a restored car book enclosed for a long move. So do the collectors who show at the speedway car shows.'),
  P('A daily driver or a work truck goes open without a problem. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain what each one buys you.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff on the DuPont Highway or outside the gate, and a delivery. The base calendar sets the week.'),
  P('Approve the price, and a carrier coming down from the corridor takes the booking. We name the spot and the window the same day. The driver inspects the car with you and writes its condition on a Bill of Lading. Both of you sign, and the same form comes out when the car arrives.'),
 )+ULI([
  "Empty the car of personal items",
  "Leave about a quarter tank of fuel",
  "Photograph the car before the handoff",
  "Provide a working key and disclose any mechanical issue",
  "Turn off any aftermarket alarm",
  "On base, plan to meet the truck outside the gate on Route 1",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages walk through the rest.'))))

BODY.append(sec('Why Ship Guy','Why Dover Drivers Choose Ship Guy',
 prose(
  L('We bring the corridor carriers down Route 1 and 13. We plan around the gate, the session, and the race.'),
  P('Ship Guy’s brokerage authority with the FMCSA is active, backed by a $75,000 surety bond. Both are on file in the federal register. Our office is on West Division Street downtown.'),
  P('One coordinator owns your shipment from the first quote to the last signature. You can book open, enclosed, or expedited transport, and the <a href="services.html">services</a> page describes each.'),
 ), alt=True))

BODY.append(office('Dover','223 W Division St #523','Dover, DE 19901','+13022468730','(302) 246-8730','ET',
 '223+W+Division+St+%23523,+Dover,+DE+19901','Visit Us','Find Ship Guy in Dover',
 'Our office is on West Division Street downtown, a few blocks north of the Green.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4757.215462700998!2d-75.529364!3d39.161080999999996!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c77b1c278818a1%3A0x8c6e2bdf06bdf832!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792153867791!5m2!1sen!2sus'))

FAQ=[
 ("Do you handle a PCS move to Dover Air Force Base?","Yes, every week of the year, with the peak in summer. Orders cover one car, and the second one comes with us. The gate stops the truck, so we meet you at a lot on Route 1 or in town. We schedule around your report date. Ship Guy is a private broker with no connection to the base."),
 ("How much does it cost to ship a car from Dover to Wilmington or Baltimore?","Wilmington runs one hundred thirty to two hundred twenty dollars for a sedan. That is about fifty miles up Route 1 or 13. Baltimore runs one hundred sixty to two hundred seventy, about one hundred miles over the Bay Bridge. SUVs and pickups add 10 to 25 percent."),
 ("Why does Dover cost a little more than Wilmington?","Because no interstate reaches it. The carrier leaves 95 at the canal and drives fifty miles down Route 1 or 13. That adds a day to some pickups and a few dollars to the price. The base keeps enough trucks coming that the difference stays small."),
 ("Are the Route 1 tolls added to my Dover quote?","No. The plaza south of Dover and the one at Biddles Corner are already in the price. Many carriers skip them and take the DuPont Highway, which carries no toll. Either way, the figure you approve is the whole figure."),
 ("Does race weekend or the legislative session affect my pickup?","Both do. Race weekend fills every hotel in the county and jams both highways for three days. A Dover pickup moves to another day. During the session, from January to June, downtown parking vanishes. We move a downtown handoff to the DuPont Highway."),
 ("Can the carrier come to my street near the Green or on the base?","Not on either one. The streets around the Green are narrow and brick, and the base housing sits behind a gate. The driver meets you on Loockerman Street, at a lot off State Street, or on the DuPont Highway. Rodney Village, Fox Hall, and the newer subdivisions are a different story, and the curb usually works."),
 ("Can you ship a car for a Delaware State University student?","Yes. Cars arrive each August and leave each May, and both windows book up early. The campus lots off the DuPont Highway work for the handoff. A parent or another adult signs at pickup."),
 ("Can you pick up on a farm west of town or in a bayside town?","Yes, on the paved road. A seventy-five-foot trailer stays on Route 8, Route 9, or Route 1. It does not go down a gravel drive or a marsh road. The driver meets you there or in the nearest town. Count on 2 to 4 days for those instead of 1 to 3."),
 ("Can you ship a car that does not run from Dover?","Yes. The carrier arrives with a winch, and the quote already covers the slower loading. Pick a flat, open spot, which in Dover usually means a lot on the DuPont Highway. Let us know if it rolls, steers, and brakes."),
 ("What do you need for a Dover car shipping quote?","Where the car is and where it goes, with the gate or the neighborhood on this end. Year, make, and model. Running or not. Open or enclosed. A date range, with the report date or race weekend in mind. That is all a Dover quote takes."),
]
BODY.append(faq_section(FAQ,'Dover FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Dover?','The form above prices your lane in about two minutes. Tell us the gate or the neighborhood and your dates. A carrier coming down Route 1 handles the rest.','+13022468730','(302) 246-8730','Get your free Dover quote'))

build({
 'slug':'auto-transport-dover-delaware',
 'title':'Car Shipping in Dover, DE — Auto Transport | Ship Guy',
 'meta':'Car shipping in Dover, DE, the capital with no interstate. Air base second cars and gate handoffs, the Green and Loockerman Street meeting spots, subdivision curbside, state and university relocations, race weekend and session planning, bayside flooding. Local office on West Division Street downtown. Free quote.',
 'h1':'Car Shipping in<br>Dover, <span class="accent">Delaware</span>',
 'lede':'Open, enclosed, and expedited auto transport across Kent County, planned around Route 1, the DuPont Highway, the gate, and the race.',
 'tel':'+13022468730','disp':'(302) 246-8730','brand':'Dover','keyword':'car shipping in dover',
 'localterms':['dover','route 1','us 13','dupont highway','route 8','division street','route 10','us 113','route 9','toll plaza','biddles corner','roth bridge','canal','interstate 95','christiana','the green','legislative hall','loockerman street','state street','air base','gate','rodney village','capitol park','mayfair','fox hall','camden','wyoming','smyrna','magnolia','frederica','harrington','milford','marydel','leipsic','little creek','bowers beach','kitts hummock','amish','buggies','cargo planes','aircrews','orders','report date','state government','session','university','campus','plants','wipes','hospital','residents','casino','speedway','monster mile','race weekend','state fair','dover days','nor’easters','sandy','2012','ice storm','beach traffic','memorial day','labor day','wilmington','philadelphia','baltimore','washington','new york','norfolk','richmond','raleigh','chicago','orlando','florida','texas','california','carolina'],
}, BODY, FAQ)
