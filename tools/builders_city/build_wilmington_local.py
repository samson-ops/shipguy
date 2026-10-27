import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Wilmington, Delaware','Car shipping on the twenty miles of Interstate 95 that every East Coast carrier crosses',
 ['Car shipping in Wilmington starts on the viaduct, where Interstate 95 crosses the city between Baltimore and Philadelphia. Ship Guy is a licensed auto transport broker with an office on West 10th Street downtown.',
  'We book vetted carriers across New Castle County, from Claymont to Middletown and out to Hockessin. We do not own the trucks.',
  'Interstate 95 runs through the middle of the city on the viaduct. Interstate 495 swings around it along the river. Interstate 295 leaves for the Delaware Memorial Bridge and New Jersey. US 13, US 202, and Route 141 tie the suburbs to all three.',
  'This page covers the three interstates, the toll plaza, downtown, the rowhouse blocks, and the estate roads. It also covers the banks, the chemical companies, the hospitals, the port, the river, and the lanes.'],
 'Wilmington at a glance',
 ['Most pickups happen within 1 to 3 days. Interstate 95 carries the Boston-to-Florida carriers over the city all day.',
  'Philadelphia, Baltimore, and Washington are same-day lanes. New York is the same day too. Richmond and Boston take a day. Raleigh takes one, and Florida takes three.'],
 'Tell us the neighborhood. Trolley Square, Little Italy, and the rowhouse blocks need a meeting spot. Brandywine Hundred, Pike Creek, and Bear usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 95, 495, 295, the Viaduct, and the Toll Plaza',
 prose(
  L('Wilmington sits on the busiest twenty miles of the East Coast corridor. The trucks never stop.'),
  P('Interstate 95 crosses the city on a viaduct that was rebuilt from 2021 to 2023. The ramps at Delaware Avenue and Martin Luther King Boulevard are the way downtown. The toll plaza sits west of Newark at the Maryland line. Carriers pay it in both directions.'),
  P('Interstate 495 leaves 95 at the Pennsylvania line and runs down the river past the port. It rejoins 95 south of the city. Most through trucks take it, so the viaduct stays lighter. Interstate 295 branches off at the bottom for the Delaware Memorial Bridge and the New Jersey Turnpike.'),
  P('US 13 is DuPont Highway, the long strip south through New Castle to Dover. US 202 is Concord Pike, the strip north into Pennsylvania. Route 141 loops around the west side past the airport. Route 52 is Kennett Pike, the road into the estate country. Kirkwood Highway runs west to Newark.'),
  P('The carriers come off 95 at Exit 7 for downtown and at Exit 4 for Christiana. The lots at the Christiana Mall, along Concord Pike, and by the Riverfront are the usual meeting spots. Route 1 south of the canal charges a toll as well.'),
  P('Our office sits on West 10th Street downtown, a few blocks west of Rodney Square.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, Trolley Square, Little Italy, the Highlands, and the Suburbs',
 prose(
  L('Wilmington is a rowhouse city on two rivers, ringed by suburbs that were farms within living memory.'),
  P('Downtown is a grid of office towers between the Brandywine and the Christina. Market Street has the opera house and the bank lobbies. A trailer can stop on King Street or by the train station. The Riverfront along the Christina has wide lots, the ballpark, and the Chase Center. The handoff often happens there.'),
  P('Trolley Square, Little Italy, Forty Acres, and the Ninth Ward are rowhouse blocks with cars on both curbs. Union Street and Delaware Avenue are the meeting spots. The Highlands, Westover Hills, and the blocks by Rockford Park have winding streets under old trees. The driver stays on Pennsylvania Avenue.'),
  P('The East Side, Southbridge, Riverside, and Browntown are tight blocks south and east of downtown. The driver meets you on Fourth Street, on New Castle Avenue, or at the Riverfront. Brandywine Hundred and North Wilmington are postwar grids off Concord Pike and Marsh Road. The truck usually reaches the curb.'),
  P('Greenville, Centreville, and Hockessin are the estate country along Kennett Pike. The drives are long and the roads are narrow. The handoff happens at a shopping center on Route 52 or Route 41. Pike Creek, Newark, Bear, and Middletown are suburban grids where the curb usually works. New Castle has a colonial Main Street and open blocks beyond it.'),
 )))

ROUTES=[("Philadelphia, PA","I-95 · ~30 mi","Same day","$150–$240"),("Baltimore, MD","I-95 · ~70 mi","Same day","$150–$240"),
 ("Washington, DC","I-95 · ~110 mi","Same day","$170–$280"),("New York, NY","I-95/NJ Tpke · ~125 mi","Same day","$170–$280"),
 ("Richmond, VA","I-95 · ~220 mi","1 day","$230–$350"),("Pittsburgh, PA","I-76 · ~330 mi","1 day","$290–$420"),
 ("Boston, MA","I-95 · ~320 mi","1 day","$290–$420"),("Raleigh, NC","I-95 · ~380 mi","1 day","$340–$490"),
 ("Chicago, IL","I-76/I-80 · ~760 mi","2 days","$550–$800"),("Orlando, FL","I-95 · ~960 mi","3 days","$700–$980")]
BODY.append(rate_table('Lanes &amp; Costs','Wilmington Car Shipping Lanes and Estimated Costs',
 'The corridor lanes that leave Wilmington most, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a running sedan on an open trailer, priced from downtown Wilmington. An SUV or pickup adds roughly 10 to 25 percent, and enclosed adds more. The tolls are in the figure. The season and the carriers free on your dates set the final price.',
 prose(
  P('Philadelphia, Baltimore, Washington, and New York are some of the lowest prices in the country. The corridor never empties, so a Wilmington car usually shares a trailer that was passing anyway.'),
  P('The Florida lane climbs in the fall, when the retirees leave. The <a href="car-shipping-cost.html">cost guide</a> explains vehicle size, condition, and the rest of the math.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Banks, the Chemical Companies, the Hospitals, the Port, and the Courts',
 prose(
  L('Wilmington relocates bankers, chemists, lawyers, and residents, and most of them arrive on a start date.'),
  P('The credit card banks are the biggest private employers in the state. Their towers downtown and their campuses in Christiana bring in analysts from every state. The start dates cluster in January and in the summer. A second car usually rides a truck.'),
  P('The chemical companies that built the city still relocate scientists and engineers. The research campuses along the Brandywine and on Concord Pike hire on program schedules. The pharmaceutical companies in North Wilmington do the same. We supply the paperwork a reimbursed move needs.'),
  P('The Court of Chancery and the law firms around Rodney Square bring in attorneys each fall. The hospitals bring in residents each June. The children’s hospital in Rockland and the big hospital campus in Stanton add nurses and fellows every summer. The university in Newark brings cars in each August.'),
  P('The port at the mouth of the Christina handles more fruit than any other on the coast. It brings in logistics managers. The refinery down the river in Delaware City rotates contractors on turnaround schedules. The interstate half of a move is explained on the <a href="state-to-state-car-shipping.html">state-to-state</a> page.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Nor’easters, the Brandywine, the Grand Prix, and the Italian Festival',
 prose(
  L('Wilmington gets corridor weather. Snow from the northeast, floods from the south, and heat in between.'),
  P('Nor’easters close 95 a few times each winter. The viaduct and the bridge over the Susquehanna ice first. The carriers hold in Maryland or Pennsylvania until the plows and the salt finish. A winter pickup can slide a day.'),
  P('The Christina and the Brandywine flood after a tropical storm. Ida in 2021 put the blocks along the Brandywine under water. A pickup near either river moves up the hill until the water drops. Summer heat moves the loading hour to early morning.'),
  P('The Grand Prix closes downtown for a weekend each May for bike races. The jazz festival fills Rodney Square in June. The Italian festival closes Union Street and Little Italy for a week in June. The steeplechase at Winterthur fills Kennett Pike on a Sunday in May. We move a pickup in those blocks to another day.'),
  P('Move-in at the university fills Newark for a weekend in late August. The ballpark fills the Riverfront lots on summer game nights. Neither one stops a pickup, but both move the meeting spot a few blocks.'),
 )+chips(["Downtown","Market Street","Rodney Square","Riverfront","Trolley Square","Little Italy","Forty Acres","Ninth Ward","The Highlands","Westover Hills","Rockford Park","East Side","Southbridge","Riverside","Browntown","Brandywine Hundred","North Wilmington","Claymont","Talleyville","Greenville","Centreville","Hockessin","Pike Creek","Elsmere","Newport","Stanton","Christiana","New Castle","Newark","Bear","Middletown"])
 +NOTE('Serving Wilmington and all of New Castle County, from the Pennsylvania line to the canal. Tell us the neighborhood and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Wilmington?',
 prose(
  L('Open is the corridor standard, and the short lanes to Philadelphia and Baltimore are priced for it.'),
  P('An enclosed trailer keeps the road salt, the slush, and the eyes off a car. The garages in Greenville and the Highlands book them for collector cars. So does a car headed to a show or to a winter house in Florida.'),
  P('A commuter car rides open without a second thought. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages set the two side by side.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff at the Riverfront or the Christiana lots, and a delivery. The corridor sets the pace.'),
  P('Approve the price, and a carrier already crossing the state takes the booking. We confirm the spot and the window the same day. The driver walks around the car with you and records its condition on a Bill of Lading. You both sign it, and the same sheet comes out at delivery.'),
 )+ULI([
  "Clear your belongings out of the car",
  "Run the tank down to about a quarter",
  "Photograph the car before the handoff, salt and all",
  "Hand over a working key and mention any mechanical issue",
  "Disable any aftermarket alarm",
  "On a rowhouse block, pick a wide street or a lot where the truck can stop",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Wilmington Drivers Choose Ship Guy',
 prose(
  L('We book the trucks that already cross the state every day. We plan around the viaduct, the tolls, and the snow.'),
  P('Ship Guy’s FMCSA brokerage authority is active, and a $75,000 surety bond stands behind it. Both can be checked in the federal register. Our office is on West 10th Street downtown.'),
  P('One coordinator stays with your shipment from the first quote to the signature at delivery. Open, enclosed, and expedited transport are all available, and the <a href="services.html">services</a> page lays them out.'),
 ), alt=True))

BODY.append(office('Wilmington','221 W 10th St #373','Wilmington, DE 19801','+13022404170','(302) 240-4170','ET',
 '221+W+10th+St+%23373,+Wilmington,+DE+19801','Visit Us','Find Ship Guy in Wilmington',
 'Our office is on West 10th Street downtown, a few blocks from Rodney Square and the 95 ramps.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4717.36779028364!2d-75.5494051!3d39.746679!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c6fd65d5add7eb%3A0x5216dac5c213be8c!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792153856730!5m2!1sen!2sus'))

FAQ=[
 ("Why is car shipping from Wilmington priced so low?","Because the city sits on the busiest twenty miles of the East Coast corridor. Every carrier between Boston and Florida crosses it on 95 or 495. A Wilmington car fills a space on a trailer that was passing anyway. Philadelphia and Baltimore usually run one hundred fifty to two hundred forty dollars for a sedan."),
 ("How much does it cost to ship a car from Wilmington to Florida or New York?","Orlando runs seven hundred to nine hundred eighty dollars for a sedan. That is about nine hundred sixty miles down 95. New York runs one hundred seventy to two hundred eighty. That is about one hundred twenty-five miles up 95 and the Turnpike. Fall retiree demand lifts the Florida price from October through December. SUVs and pickups add 10 to 25 percent."),
 ("Can the carrier come onto my street in Trolley Square or Little Italy?","Usually not. Those blocks are narrow, and cars park on both curbs. A seventy-five-foot rig has nowhere to stop. The driver meets you on Delaware Avenue, on Union Street, or at a lot on the Riverfront. Brandywine Hundred, Pike Creek, and Bear usually allow the curb."),
 ("Do you ship cars for bank employees relocating to Wilmington?","Yes, all year, with peaks in January and summer. The card banks bring in analysts and managers from every state on start dates. Many ship a second car behind the move. We provide the paperwork for a reimbursed move. The handoff works at the Riverfront or the Christiana lots."),
 ("Are the Delaware tolls added to my Wilmington quote?","No, they are already in it. Carriers pay the plaza on 95 at the Maryland line and the Route 1 plazas down south. The price you approve is the whole price. Some carriers headed south use US 13 instead, and it carries no toll."),
 ("What happens if a nor’easter hits on my pickup day?","The carriers wait it out in Maryland or Pennsylvania. The viaduct and the Susquehanna bridge ice before the rest of 95. Nothing moves a loaded trailer on ice. A winter pickup can slide a day, and we call before it does."),
 ("Can you ship a car for a University of Delaware student?","Yes. Cars move in each August and out each May, and both windows fill early. Campus streets in Newark are packed during move-in. The handoff happens at a lot off Route 896 near the 95 interchange. An adult signs for the car at pickup."),
 ("Can you pick up in Greenville or Hockessin?","Yes, at the nearest shopping center. The estate roads along Kennett Pike are narrow, and the drives are long. The driver meets you at a lot on Route 52 or Route 41. Enclosed carriers work that country often, since many of those garages hold collector cars."),
 ("Can you ship a car that does not run from Wilmington?","Yes. We send a carrier with a winch, and the extra loading time is priced in. Choose a flat, open spot, which usually means a Riverfront lot or the Christiana Mall. Tell us whether the car rolls, steers, and brakes."),
 ("What do you need for a Wilmington car shipping quote?","Both addresses, with the neighborhood on this end. The year, make, and model. Whether the car runs and rolls. Open or enclosed, and the dates you can work with. That is everything a Wilmington quote needs."),
]
BODY.append(faq_section(FAQ,'Wilmington FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Wilmington?','The form above prices your lane in about two minutes. Give us the neighborhood and your dates, and a truck already on the corridor does the rest.','+13022404170','(302) 240-4170','Get your free Wilmington quote'))

build({
 'slug':'auto-transport-wilmington-delaware',
 'title':'Car Shipping in Wilmington, DE — Auto Transport | Ship Guy',
 'meta':'Car shipping in Wilmington, DE on the Interstate 95 corridor between Philadelphia and Baltimore. Rowhouse-block meeting spots, Riverfront and Christiana handoffs, bank and chemical-company relocations, hospital residents, the Delaware tolls, nor’easter and Brandywine flood planning. Local office on West 10th Street downtown. Free quote.',
 'h1':'Car Shipping in<br>Wilmington, <span class="accent">Delaware</span>',
 'lede':'Open, enclosed, and expedited auto transport across New Castle County, planned around 95, the viaduct, the tolls, and the snow.',
 'tel':'+13022404170','disp':'(302) 240-4170','brand':'Wilmington','keyword':'car shipping in wilmington',
 'localterms':['wilmington','interstate 95','interstate 495','interstate 295','viaduct','toll plaza','delaware memorial bridge','us 13','dupont highway','us 202','concord pike','route 141','route 52','kennett pike','kirkwood highway','route 1','christiana','riverfront','rodney square','market street','king street','train station','chase center','ballpark','trolley square','little italy','forty acres','ninth ward','highlands','westover hills','rockford park','pennsylvania avenue','east side','southbridge','riverside','browntown','brandywine hundred','north wilmington','marsh road','greenville','centreville','hockessin','pike creek','newark','bear','middletown','new castle','claymont','banks','chemical','brandywine','pharmaceutical','court of chancery','law firms','hospitals','residents','rockland','stanton','university','port','fruit','refinery','delaware city','nor’easters','susquehanna','ida','2021','grand prix','jazz festival','italian festival','union street','steeplechase','winterthur','move-in','philadelphia','baltimore','washington','new york','richmond','boston','raleigh','pittsburgh','chicago','orlando','florida'],
}, BODY, FAQ)
