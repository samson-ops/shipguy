import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Chesapeake, Virginia','Car shipping across the biggest city in Hampton Roads, from Greenbrier to Great Bridge and the swamp to the state line',
 ['Car shipping in Chesapeake covers three hundred fifty square miles, and much of the south is swamp. Ship Guy is a licensed auto transport broker with an office on Belaire Avenue in Greenbrier.',
  'We book vetted carriers across the city, from Western Branch and Deep Creek to Great Bridge and Hickory. The carriers own the trucks. Ship Guy holds the authority and the bond.',
  'Interstate 64 crosses the city from Bowers Hill to the Virginia Beach line over the High Rise Bridge. Interstate 464 runs north to downtown Norfolk, and Interstate 664 runs the west edge to the Monitor-Merrimac tunnel. The Chesapeake Expressway runs south to the Outer Banks, and Battlefield Boulevard is the spine.',
  'This page covers 64, 464, 664, the High Rise, the Expressway, Greenbrier, Great Bridge, Western Branch, and Hickory. It also covers the Navy families, the headquarters, the hospital, the drawbridges, the storms, and the lanes.'],
 'Chesapeake at a glance',
 ['Most pickups happen within 1 to 3 days. Carriers serving Norfolk and Virginia Beach pass through the city on 64 and 464 every day.',
  'Richmond, Raleigh, Washington, and Baltimore are a same-day haul. Philadelphia, Charlotte, and New York take a day. Atlanta takes one to two, and Florida takes two.'],
 'Tell us the borough and whether a drawbridge sits between you and 64. Greenbrier, Great Bridge, Hickory, and Western Branch usually allow the curb. South Norfolk and the older blocks by the river meet the truck at a lot.'))

BODY.append(sec('The Roads','Interstate 64, Interstate 464, Interstate 664, the High Rise Bridge, the Chesapeake Expressway, and Battlefield Boulevard',
 prose(
  L('Chesapeake is where every Hampton Roads highway comes together, and the carriers stage here for the whole region.'),
  P('Interstate 64 enters at Bowers Hill on the west. It crosses the Southern Branch of the Elizabeth River on the High Rise Bridge. The state is widening the bridge and the interstate from Bowers Hill to Greenbrier through the decade. Lane shifts move every few months. East of the river, 64 runs past Greenbrier to the Virginia Beach line.'),
  P('Interstate 464 leaves 64 at Great Bridge Boulevard. It runs north past South Norfolk to downtown Norfolk and the tunnel. Interstate 664 runs the west edge from Bowers Hill through Western Branch to the Monitor-Merrimac tunnel. The Chesapeake Expressway is Route 168, a toll road from Great Bridge to the Outer Banks. The toll rides inside the quote.'),
  P('Battlefield Boulevard is the spine. It runs from South Norfolk through Greenbrier and Great Bridge to Hickory and the state line. Military Highway and Route 17 carry the west side through Deep Creek. The Great Bridge drawbridge over the Intracoastal Waterway opens on the hour. The Gilmerton drawbridge on Military Highway opens for ships. A carrier waits on one of them most days.'),
  P('The carriers come off 64 at Battlefield Boulevard and Greenbrier Parkway. The mall lots in Greenbrier are the usual meeting spot. The centers on Battlefield in Great Bridge and the lots at Chesapeake Square in Western Branch work too. The city park lots on Greenbrier Parkway work outside the Jubilee.'),
  P('Our office is on Belaire Avenue in Greenbrier, just off Battlefield Boulevard south of 64.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Greenbrier, Great Bridge, Hickory, Deep Creek, Western Branch, South Norfolk, Indian River, and the Swamp',
 prose(
  L('Chesapeake is seven boroughs of subdivisions with a national wildlife refuge filling the south. The truck reaches nearly every curb.'),
  P('Greenbrier at the 64 interchange is the mall, the office parks, and the hotel strip. The subdivisions sit behind them. The driver reaches most curbs. Great Bridge south of it is the historic center, the courthouse, and wide 1980s subdivisions along Cedar Road. The curb works. Hickory beyond it is newer and bigger, with long driveways and farm roads toward the state line. The handoff happens at the house or at a church lot on Battlefield.'),
  P('Deep Creek along Route 17 sits on the Dismal Swamp Canal. The lock and the old village sit by the drawbridge. The subdivisions off Shillelagh and Cedar allow the curb. Western Branch across the river by Portsmouth is wide postwar streets around Chesapeake Square. The driver reaches the house.'),
  P('South Norfolk is the oldest borough, a grid of narrow streets and porches along Poindexter and Chesapeake Avenue. A seventy-five-foot trailer does not stop there. The handoff moves to the Campostella Road lots or the 464 ramps. Indian River along the Virginia Beach line is tight postwar streets off Indian River Road. The handoff moves to the shopping centers.'),
  P('The Great Dismal Swamp fills the southwest, and nothing ships from inside it. The farms and acreage along Ballahack and Centerville roads meet the truck at the road. Portsmouth, Norfolk, Suffolk, and Virginia Beach surround the city, and all four price the same as Chesapeake. Moyock across the state line prices the same too.'),
 )))

ROUTES=[("Richmond, VA","I-64 · ~95 mi","Same day","$170–$280"),("Raleigh, NC","US-58/I-95 · ~190 mi","Same day","$230–$350"),
 ("Washington, DC","I-64/I-95 · ~200 mi","Same day","$230–$350"),("Baltimore, MD","I-64/I-95 · ~240 mi","Same day","$250–$380"),
 ("Philadelphia, PA","I-64/I-95 · ~280 mi","1 day","$270–$400"),("Charlotte, NC","US-58/I-85 · ~320 mi","1 day","$300–$440"),
 ("New York, NY","I-95 · ~370 mi","1 day","$350–$510"),("Atlanta, GA","I-85 · ~550 mi","1–2 days","$440–$630"),
 ("Jacksonville, FL","I-95 · ~590 mi","2 days","$450–$650"),("Orlando, FL","I-95 · ~730 mi","2 days","$520–$750")]
BODY.append(rate_table('Lanes &amp; Costs','Chesapeake Car Shipping Lanes and Estimated Costs',
 'The lanes Chesapeake cars run most, with estimated open-trailer ranges. Price your own route on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Chesapeake for a running sedan on an open trailer. SUVs and pickups cost about 10 to 25 percent more, enclosed more still. The Expressway toll is inside the number when a carrier uses 168. Your dates and the trucks free on them set the real quote.',
 prose(
  P('Chesapeake prices a shade under Virginia Beach on every lane, because the carriers reach it without the tunnels. Richmond is ninety minutes up 64, and every northern lane starts there. The Raleigh and Charlotte lanes ride 58 west to 95 and 85. The Florida lane fills with Navy families each summer and retirees each fall.'),
  P('A move timed to a PCS report date or a July closing ships with the busiest weeks. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Navy Families, the Headquarters on Battlefield, the Hospital, the Shipyards, and the Port',
 prose(
  L('Chesapeake relocates sailors, chiefs, logistics managers, and nurses. The Navy moves more households here than every employer combined.'),
  P('No big base sits inside the city, but the families from all of them live here. Sailors from the Norfolk piers, Oceana, Little Creek, and the shipyard buy in Great Bridge for the schools. Orders bring them in and out all year, with a hard summer peak. The Navy annex on the state line and the auxiliary field in Fentress sit inside the city. Housing at both is gated, and the handoff happens outside the gate.'),
  P('Orders often cover one vehicle, so the second one ships privately. Booking two to three weeks ahead from May through August is wise. Ship Guy is a private broker with no connection to the Navy. Our <a href="military-car-shipping.html">military car shipping</a> page has the PCS timing in detail.'),
  P('The discount retailer headquartered on Battlefield at Summit Pointe relocates buyers and managers on start dates all year. The hospital on Battlefield and the health system campuses in Greenbrier hire traveling nurses year round. The shipyards on the Southern Branch and the port in Norfolk move engineers and managers the same way. Reimbursed moves get their documentation from us.'),
  P('Retirees who finished a Navy career leave for Florida and the Carolinas each fall. Families priced out of Virginia Beach buy in Hickory on closing dates. One car rides the trailer while the other is driven. The <a href="state-to-state-car-shipping.html">state-to-state</a> page has the interstate side.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Jubilee, the Outer Banks Traffic, Fleet Week, the Nor’easters, the Hurricanes, and the Swamp Fires',
 prose(
  L('Chesapeake runs on a Navy calendar and a beach-traffic calendar. The storms come off the ocean and up the river.'),
  P('The Jubilee fills the city park on Greenbrier Parkway for a weekend in May, and the lots close. Fleet Week and the Harborfest in Norfolk fill 464 for a June weekend. The Great Bridge battle reenactment fills the historic site for a December weekend. A handoff near any of them moves to the next morning.'),
  P('The Outer Banks traffic owns the Expressway every summer weekend. Southbound jams Friday and Saturday morning, and northbound jams Sunday afternoon. The Great Bridge drawbridge adds to it on the hour. A carrier headed for Hickory or the state line crosses midweek or before seven. The rest of the city barely notices.'),
  P('Hurricane season runs June through November. Isabel in 2003 put the Southern Branch over its banks and took the power out for a week. Matthew in 2016 flooded the low streets along the Elizabeth River and the canal. Carriers leave the region days before a landfall, and pickups pause until the roads reopen. Nor’easters push the river up the same streets each fall. The swamp burns in a dry summer, and the smoke slows 64 for an afternoon.'),
  P('Snow comes a few times a winter and melts in a day. The January 2018 storm dropped a foot and kept the carriers in Richmond for two days. The bridges ice first. The carriers wait in Richmond until the roads clear. A winter pickup can lose a day. We tell you first.'),
 )+chips(["Greenbrier","Greenbrier Mall","Summit Pointe","Great Bridge","Cedar Road","Hickory","Battlefield Boulevard","Deep Creek","Dismal Swamp Canal","Western Branch","Chesapeake Square","Bowers Hill","South Norfolk","Poindexter Street","Campostella","Indian River","Oak Grove","Norfolk Highlands","Portlock","Fentress","Etheridge Manor","Las Gaviotas","Edinburgh","Centerville","Ballahack","Moyock","Portsmouth","Norfolk","Suffolk","Virginia Beach","Elizabeth City"])
 +NOTE('Serving all seven boroughs of Chesapeake, Greenbrier cul-de-sac or Hickory farm road. Tell us the borough and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Chesapeake?',
 prose(
  L('Almost every Chesapeake car rides an open trailer, and that is what the lane table prices.'),
  P('An enclosed trailer keeps off the salt air, the pollen, and the road grit. The collectors in Great Bridge and the officers relocating a new car book one. A car bound for a long storage during a deployment often rides enclosed too.'),
  P('A commuter car or a sailor’s pickup rides open without a worry. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages lay out the difference.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A number, a lot in Greenbrier or at the Chesapeake Square, and a signature at delivery. The report date or the closing picks the week.'),
  P('Approve the price, and we book a carrier already working 64 and 464. The spot and the window are set the same day. At pickup you and the driver go around the car together. Every existing mark is written on the Bill of Lading. You both sign it. The delivery inspection is checked against that sheet.'),
 )+ULI([
  "Personal items out of the cabin and the trunk",
  "About a quarter tank of fuel",
  "Each side and the odometer photographed before the truck arrives",
  "One working key for the driver, with any fault named",
  "Aftermarket alarm switched off",
  "In South Norfolk or Indian River, meet the truck at a shopping center",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Chesapeake Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already stage in Chesapeake for all of Hampton Roads. We know which drawbridge opens when.'),
  P('Our FMCSA license and $75,000 bond are public on the federal register. Our office is on Belaire Avenue in Greenbrier.'),
  P('A single coordinator handles the move from the first call to the last signature. The <a href="services.html">services</a> page explains open, enclosed, and expedited transport.'),
 )))

BODY.append(office('Chesapeake','555 Belaire Ave #555A','Chesapeake, VA 23320','+17576376136','(757) 637-6136','ET',
 '555+Belaire+Ave+%23555A,+Chesapeake,+VA+23320','Visit Us','Find Ship Guy in Chesapeake',
 'Our office is on Belaire Avenue in Greenbrier, just off Battlefield Boulevard south of 64.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3945.191866026209!2d-76.2402147!3d36.7680532!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89babd01d3a29379%3A0x3ef9c2f9c2727e93!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793287611563!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Chesapeake to Washington or Florida?","Washington runs two hundred thirty to three hundred fifty dollars for a sedan. That is about two hundred miles up 64 and 95. Orlando runs five hundred twenty to seven hundred fifty, about seven hundred thirty miles down 95. Richmond is ninety minutes up 64 and the lowest of the three. An SUV or a pickup adds 10 to 25 percent."),
 ("Can the carrier come to my street in Greenbrier or Great Bridge?","Usually, yes. Greenbrier, Great Bridge, Hickory, Western Branch, and Deep Creek are wide subdivisions, and the driver reaches most curbs. South Norfolk and Indian River are older grids with narrow streets. There the driver meets you at the Campostella Road lots or a shopping center."),
 ("Do you handle Navy PCS moves for Chesapeake families?","Yes, and the summer is the peak. Sailors from the Norfolk piers, Oceana, Little Creek, and the Portsmouth shipyard live across the city. Orders usually cover one vehicle, so the second one ships privately. Book two to three weeks ahead from May through August. Ship Guy is a private broker with no connection to the Navy."),
 ("Does the Outer Banks traffic affect my pickup?","On summer weekends, yes, if you live along the Expressway or in Hickory. Southbound jams Friday and Saturday morning, and northbound jams Sunday afternoon. The Great Bridge drawbridge adds to it on the hour. A carrier crosses midweek or before seven. Greenbrier and Western Branch never notice."),
 ("Can you ship a car to or from Suffolk, Portsmouth, or Moyock?","Yes, and all three price the same as Chesapeake. Suffolk rides the same carriers out 664 and Route 17. Portsmouth rides them across the Gilmerton drawbridge. Moyock rides them down the Expressway and across the state line. Send the full address for a farm road."),
 ("What happens if a hurricane is forecast for my pickup week?","Carriers leave the region days before a landfall, and pickups pause until the roads reopen. Isabel in 2003 and Matthew in 2016 flooded the low streets along the river. If you need the car out ahead of a storm, call the moment the track firms up. Afterward, a few days of patience lowers the price."),
 ("Is the Chesapeake Expressway toll in my price?","Yes. A carrier that takes 168 to Hickory or the state line pays the toll. It rides inside the quote. There is no separate line. Interstate 64, 464, 664, and Battlefield Boulevard carry no toll."),
 ("Do you ship cars for the headquarters and the hospital on Battlefield?","Yes. The discount retailer at Summit Pointe relocates buyers and managers on start dates all year. The hospital and the health system campuses hire traveling nurses year round. A second car usually comes along on a trailer. Reimbursed moves get their documentation from us."),
 ("Can you ship a car that does not run from Chesapeake?","Yes. A carrier with a winch is booked, and the loading time is built into the quote. The mall lots in Greenbrier or the Chesapeake Square lots give the driver level ground. Tell us whether the car rolls, steers, and brakes."),
 ("What do you need for a Chesapeake car shipping quote?","The two addresses, with the borough. Year, make, and model. Does it run. Open or enclosed. The week around the report date or the closing. Five answers, and the Chesapeake number comes back within the day."),
]
BODY.append(faq_section(FAQ,'Chesapeake FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Chesapeake?','The form above prices your lane in about two minutes. Give us the borough and the week, and a carrier already staging on 64 takes it.','+17576376136','(757) 637-6136','Get your free Chesapeake quote'))

build({
 'slug':'auto-transport-chesapeake-virginia',
 'title':'Car Shipping in Chesapeake, VA — Auto Transport | Ship Guy',
 'meta':'Car shipping in Chesapeake, VA, the biggest city in Hampton Roads, from Greenbrier to Great Bridge and Hickory. Navy PCS timing, headquarters and hospital relocations, curbside pickups across the boroughs, lot handoffs in South Norfolk, the High Rise Bridge work, the drawbridges, the Expressway toll, the Outer Banks traffic, and the hurricanes. Local office on Belaire Avenue in Greenbrier. Free quote.',
 'h1':'Car Shipping in<br>Chesapeake, <span class="accent">Virginia</span>',
 'lede':'Open, enclosed, and expedited auto transport across all seven boroughs, planned around 64, the High Rise, the drawbridges, the Navy calendar, and the storms.',
 'tel':'+17576376136','disp':'(757) 637-6136','brand':'Chesapeake','keyword':'car shipping in chesapeake',
 'localterms':['chesapeake','hampton roads','greenbrier','great bridge','swamp','state line','belaire avenue','western branch','deep creek','hickory','south norfolk','interstate 64','bowers hill','virginia beach','high rise bridge','interstate 464','norfolk','interstate 664','monitor-merrimac','chesapeake expressway','outer banks','battlefield boulevard','navy','headquarters','hospital','drawbridges','storms','richmond','raleigh','washington','baltimore','philadelphia','charlotte','new york','atlanta','florida','southern branch','elizabeth river','widening','lane shifts','great bridge boulevard','tunnel','monitor-merrimac tunnel','route 168','toll','military highway','route 17','intracoastal waterway','gilmerton','greenbrier parkway','mall','chesapeake square','city park','jubilee','boroughs','wildlife refuge','courthouse','cedar road','farm roads','church lot','canal','lock','shillelagh','portsmouth','poindexter','chesapeake avenue','campostella','indian river','great dismal swamp','ballahack','centerville','suffolk','moyock','pcs','closing','sailors','chiefs','logistics','nurses','oceana','little creek','shipyard','schools','annex','fentress','gated','discount retailer','summit pointe','health system','traveling nurses','port','retirees','carolinas','fleet week','harborfest','reenactment','december','isabel','2003','matthew','2016','landfall','nor','swamp fires','january 2018','foot','salt air','pollen','deployment','bill of lading','fmcsa','oak grove','norfolk highlands','portlock','etheridge manor','las gaviotas','edinburgh','elizabeth city'],
}, BODY, FAQ)
