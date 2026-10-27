import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Virginia Beach, Virginia','Car shipping at the end of Interstate 64, in the biggest Navy town in the world',
 ['Car shipping in Virginia Beach runs off Interstate 264 across the city and Interstate 64 to the tunnels. Ship Guy is a licensed auto transport broker with an office on South Boulevard by Lynnhaven.',
  'We book vetted carriers across Hampton Roads, from the Oceanfront to Chesapeake and Norfolk and over to Hampton. The trucks belong to the carriers, and we hold the authority and the bond.',
  'Interstate 264 runs from Norfolk to the Oceanfront with exits at Lynnhaven, Independence, and Birdneck. Interstate 64 loops the west side to the Hampton Roads tunnel. Virginia Beach Boulevard is the old road, and Shore Drive runs the bay.',
  'This page covers 264, 64, the tunnels, the Oceanfront, the North End, Great Neck, Kempsville, Sandbridge, and Pungo. It also covers the bases, the shipyards, the port, the hospitals, the summer season, and the lanes.'],
 'Virginia Beach at a glance',
 ['Most pickups happen within 1 to 3 days. The Richmond carriers come down 64 every day, and the 95 trucks turn east at Petersburg.',
  'Richmond, Raleigh, Washington, and Baltimore are a same-day haul. Philadelphia, Charlotte, and New York take a day. Atlanta takes one to two. Florida takes two, and the West takes four.'],
 'Tell us the neighborhood and the base, if there is one. The Oceanfront, the North End, Chic’s Beach, and Sandbridge need a meeting spot. Kempsville, Great Neck, Red Mill, and the Chesapeake subdivisions usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 264, Interstate 64, the Tunnels, Virginia Beach Boulevard, Shore Drive, and the Bay Bridge-Tunnel',
 prose(
  L('Virginia Beach sits at the dead end of the interstate system. Every carrier crosses water to reach it.'),
  P('Interstate 264 is the expressway across the city from Norfolk to the Oceanfront. The exits at Lynnhaven Parkway, Independence Boulevard, and Birdneck Road serve most of the city. Interstate 64 loops the west side from Chesapeake to Norfolk. It crosses to the Peninsula through the Hampton Roads tunnel. The state is widening the tunnel crossing, and the work closes lanes at night.'),
  P('The tunnels set the schedule. The Hampton Roads tunnel and the Monitor-Merrimac tunnel back up every rush hour. The carriers plan a crossing for the middle of the morning. The Downtown and Midtown tunnels between Norfolk and Portsmouth charge a toll, and it rides inside the quote. The bay bridge-tunnel to the Eastern Shore charges a bigger one.'),
  P('Virginia Beach Boulevard is US 58, the old road from Norfolk to the beach. It is four lanes of retail the whole way. Independence Boulevard and Lynnhaven Parkway run north and south. Princess Anne Road runs to the south end, and General Booth Boulevard runs to Sandbridge. Shore Drive is US 60 along the bay to the cape. Atlantic Avenue is the resort strip, and a trailer stays off it.'),
  P('The carriers come off 264 at Lynnhaven and Independence. The mall lots at Lynnhaven and the convention center lots on 19th Street are the usual meeting spots. The shopping centers on Virginia Beach Boulevard work too. The amphitheater lots in Princess Anne work for the south end.'),
  P('Our office is on South Boulevard by Lynnhaven, a minute from the 264 exit at Lynnhaven Parkway.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','The Oceanfront, the North End, Great Neck, Bayside, Kempsville, Town Center, Red Mill, Sandbridge, Pungo, and Chesapeake',
 prose(
  L('Virginia Beach is a resort strip, a Navy town, and three hundred square miles of subdivisions. The handoff depends on which one you are in.'),
  P('The Oceanfront between Rudee Inlet and 40th Street is the hotel strip. Atlantic and Pacific are one-way, and the side streets are closed to a trailer from May through September. The driver meets you at the convention center lots on 19th Street or at the Birdneck exit. The North End above 40th Street is narrow beach lanes under the pines. The handoff moves to the lot at the cape or to Shore Drive.'),
  P('Great Neck and Alanton are big lots, old trees, and cul-de-sacs. The driver reaches most of the curbs. Bayside and Chic’s Beach along the bay are narrow beach streets. The handoff moves to Shore Drive. Thoroughgood and Lake Smith are the same. Town Center at Pembroke is towers on garages. The driver meets you at the mall or the Independence exit.'),
  P('Kempsville is the middle of the city, 1970s and 1980s subdivisions on wide streets. The curb works almost everywhere. Lynnhaven, Thalia, and Windsor Woods are the same. Red Mill, Princess Anne, and the subdivisions off General Booth are the newest. They have wide loops and open curbs. Sandbridge at the end of the road is one lane each way with no shoulders. The driver meets you on General Booth.'),
  P('Pungo and Blackwater are the farm country in the south, with narrow roads and the strawberry fields. The handoff happens at the Pungo crossroads. Chesapeake and Greenbrier across the line are wide subdivisions that allow the curb. Norfolk, Portsmouth, Suffolk, and the Peninsula ride the same carriers through the tunnels. All of them price the same as Virginia Beach.'),
 )))

ROUTES=[("Richmond, VA","I-64 · ~105 mi","Same day","$170–$280"),("Raleigh, NC","US-58/I-95 · ~200 mi","Same day","$230–$350"),
 ("Washington, DC","I-64/I-95 · ~210 mi","Same day","$230–$350"),("Baltimore, MD","I-64/I-95 · ~250 mi","Same day","$250–$380"),
 ("Philadelphia, PA","I-64/I-95 · ~290 mi","1 day","$270–$400"),("Charlotte, NC","US-58/I-85 · ~330 mi","1 day","$300–$440"),
 ("New York, NY","I-95 · ~380 mi","1 day","$350–$510"),("Atlanta, GA","I-85 · ~560 mi","1–2 days","$440–$630"),
 ("Jacksonville, FL","I-95 · ~600 mi","2 days","$450–$650"),("Orlando, FL","I-95 · ~740 mi","2 days","$520–$750")]
BODY.append(rate_table('Lanes &amp; Costs','Virginia Beach Car Shipping Lanes and Estimated Costs',
 'The lanes Hampton Roads cars run most, with estimated open-trailer ranges. Your own route is priced on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates priced from Virginia Beach for a sedan that runs, on an open trailer. An SUV or a pickup runs 10 to 25 percent more, and an enclosed trailer more again. Tunnel tolls are inside the number when a carrier pays them. The carriers free on your dates set the final figure.',
 prose(
  P('Virginia Beach prices with Norfolk on every lane, because the carriers reach both through the same tunnels. It runs a little over Richmond on the lanes north. The carrier has to cross the water first. The Florida lane fills with sailors on orders each summer and with retirees each fall. The Washington and Baltimore lanes ride 64 and 95 and run daily.'),
  P('A move on orders in June or July ships with the busiest weeks of the year. The price follows. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Navy, the Shipyards, the Port, the Hospitals, the Broadcaster, and the Chainsaw Plant',
 prose(
  L('Virginia Beach relocates sailors, shipbuilders, nurses, and contractors. The Navy moves more households through this city than anyone moves anywhere.'),
  P('The air station at Oceana sits in the middle of the city and flies the fighter squadrons. The amphibious base at Little Creek and the training base at Dam Neck sit on its edges. The naval station in Norfolk is the largest in the world. Sailors and families rotate all year, and the heaviest moves run from May through August. The orders cover one car, and families ship the second one with us. Housing on every base is gated, and the handoff happens outside the gate. Ship Guy is a private broker and not connected to the Navy or any installation. The <a href="military-car-shipping.html">military</a> page covers the timing.'),
  P('The shipbuilder in Newport News and the repair yards in Norfolk move engineers and welders on contract schedules. The defense contractors around the bases hire from every state. The port in Norfolk receives imported cars, and we move them domestically once customs releases them. If an employer or an agency reimburses the move, we produce the paperwork.'),
  P('The hospital system’s campuses bring in traveling nurses all year. The medical school in Norfolk sends residents each June. The broadcaster and the university on Centerville Turnpike move staff on their own calendars. The chainsaw maker’s plant on the west side relocates engineers on production schedules. The state university in Norfolk and the colleges here take cars in each August.'),
  P('Military retirees stay for the base privileges and ship a car in from the last duty station. Families from the Northeast buy in Red Mill and Chesapeake on closing dates. One car rides the trailer while the other is driven. The interstate side is on the <a href="state-to-state-car-shipping.html">state-to-state</a> page.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Summer Season, the Neptune Festival, the Air Show, the Marathon, the Nor’easters, and the Hurricanes',
 prose(
  L('Virginia Beach runs on a summer that fills the Oceanfront. The storm season comes from two directions.'),
  P('The resort strip fills from Memorial Day through Labor Day, and Atlantic Avenue crawls every weekend. A handoff at the Oceanfront in summer moves to the convention center lots in the morning. The marathon closes Atlantic and the boardwalk for a March weekend. The Neptune Festival closes the strip for the last weekend of September. The sand sculptures draw half a million people.'),
  P('The air show at Oceana fills the roads around the base for a September weekend. The patriotic festival fills the Oceanfront for a June weekend. The amphitheater in Princess Anne fills its lots on concert nights all summer. A handoff near any of them moves to the daytime or to the next morning.'),
  P('Hurricane season runs from June through November. Isabel in 2003 took the power out for two weeks. Matthew in 2016 dropped fourteen inches of rain and flooded Windsor Woods. When a storm turns toward the coast, the carriers pull back for a week. The nor’easters come from the other direction from October through March and flood the same streets. A pickup on the low ground moves inland until the water drops.'),
  P('Snow is rare, but the January 2018 storm dropped a foot and shut the tunnels for two days. The city has little equipment for it, and the carriers wait in Richmond until the roads clear. Summer brings ninety-five degrees and an afternoon storm most days. The tunnels close for a crash a few times a month, and a crossing can lose an hour.'),
 )+chips(["Oceanfront","Atlantic Avenue","Rudee Inlet","North End","Cape Henry","Shore Drive","Chic’s Beach","Bayside","Thoroughgood","Great Neck","Alanton","Lynnhaven","South Boulevard","Thalia","Windsor Woods","Kempsville","Town Center","Pembroke","Independence","Princess Anne","Red Mill","General Booth","Sandbridge","Pungo","Blackwater","Oceana","Little Creek","Dam Neck","Chesapeake","Greenbrier","Norfolk","Portsmouth","Suffolk","Hampton","Newport News"])
 +NOTE('Serving Virginia Beach and all of Hampton Roads, Oceanfront lane or Chesapeake subdivision. Tell us the neighborhood and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Virginia Beach?',
 prose(
  L('Most Hampton Roads cars leave on an open trailer, and the lane table above assumes one.'),
  P('An enclosed trailer keeps off the salt air, the sand, and the road grime. The collectors who fill the Oceanfront car shows book one. Sailors shipping a new car to the next duty station book one too.'),
  P('A commuter car or a sailor’s pickup rides open and arrives as it left. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages lay out the choice.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a lot at Lynnhaven or the convention center, and a signature at the far end. The report date or the closing picks the week.'),
  P('Give the price the nod, and the car is booked onto a carrier already working 64. The lot and the window come to you the same day. The driver and you check the car over before it loads. Anything already on it is noted on the Bill of Lading. Two signatures, and that form is the record at the other end.'),
 )+ULI([
  "Personal gear out of the cabin and the trunk",
  "A quarter tank of fuel is plenty",
  "Pictures of every side and the odometer before the truck arrives",
  "One working key for the driver, and a heads-up on any fault",
  "Aftermarket alarm switched off for the trip",
  "At the Oceanfront or a beach lane, meet the truck at the convention center or on Shore Drive",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Virginia Beach Drivers Choose Ship Guy',
 prose(
  L('We book the carriers already crossing the tunnels. We know the base calendar as well as the housing office does.'),
  P('Ship Guy’s brokerage authority and $75,000 surety bond are both registered with the FMCSA. Our office is on South Boulevard by Lynnhaven.'),
  P('The coordinator who quotes the move answers the phone until the car is delivered. The <a href="services.html">services</a> page covers open, enclosed, and expedited transport.'),
 )))

BODY.append(office('Virginia Beach','4560 South Blvd #733','Virginia Beach, VA 23452','+17579083865','(757) 908-3865','ET',
 '4560+South+Blvd+%23733,+Virginia+Beach,+VA+23452','Visit Us','Find Ship Guy in Virginia Beach',
 'Our office is on South Boulevard by Lynnhaven, a minute from the 264 exit at Lynnhaven Parkway.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4910.686984195432!2d-76.134175!3d36.8328505!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89ba95ef9fd190b5%3A0x72eb7f60ced7b7a5!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793103398110!5m2!1sen!2sus', alt=True))

FAQ=[
 ("Do you ship cars for sailors on orders to Oceana, Little Creek, or Norfolk?","Yes, every week, and most of all from May through August. The orders cover one car, and families ship the second one with us. Housing on every base is gated, so the driver meets you outside the gate or at Lynnhaven. Ship Guy is a private broker and not connected to the Navy or any installation. Send the report date, and the window is built around it."),
 ("How much does it cost to ship a car from Virginia Beach to Washington or Florida?","Washington runs two hundred thirty to three hundred fifty dollars for a sedan. That is about two hundred ten miles up 64 and 95. Orlando runs five hundred twenty to seven hundred fifty, about seven hundred forty miles down 95. Richmond is two hours and the lowest of the three. An SUV or a pickup runs 10 to 25 percent more."),
 ("Can the carrier come to my house at the Oceanfront or in the North End?","In summer, no. The side streets off Atlantic are closed to a trailer from May through September. The North End lanes are narrow under the pines. The driver meets you at the convention center lots on 19th Street or at the Birdneck exit. Kempsville, Great Neck, Red Mill, and the Chesapeake subdivisions usually allow the curb."),
 ("Do the tunnels affect my pickup or delivery?","Every day. The Hampton Roads and Monitor-Merrimac tunnels back up every rush hour. The carriers cross in the middle of the morning. A crash closes a tunnel a few times a month, and a crossing can lose an hour. The Downtown and Midtown tunnels charge a toll, and it rides inside the quote. We build a cushion into any window that crosses the water."),
 ("Can you ship a car to or from Norfolk, Chesapeake, or Newport News?","Yes, and all three price the same as Virginia Beach. Norfolk and Chesapeake ride the same carriers off 64 and 264. Newport News and Hampton ride them through the tunnel, and the shipyard has lots at every gate. Send the full address, because the new subdivisions in Chesapeake and Suffolk are not on every map."),
 ("Does the Neptune Festival or the summer season affect my pickup?","At the Oceanfront, yes. The strip crawls every summer weekend, and the festival closes it for the last weekend of September. We move an Oceanfront handoff those days to the convention center lots in the morning or to Lynnhaven. The rest of the city runs normally."),
 ("What happens if a hurricane or a nor’easter hits on my pickup day?","When a storm turns toward the coast, the carriers pull back for a week. The pickup is rebooked for the week after. You hear it from us first. A nor’easter floods the low streets for a day or two, and a pickup there moves inland. The tunnels close in high wind, and a crossing waits until they reopen."),
 ("Can you ship a car that does not run from Virginia Beach?","Yes. A carrier with a winch takes it, and the slower loading is priced in from the first quote. The Lynnhaven mall lots or the convention center lots give the driver level pavement. Say whether the car rolls, steers, and brakes."),
 ("Can you ship a car that arrived at the port of Norfolk?","Yes, once customs releases it. The ocean leg is an international process we do not arrange. From the terminal, we move the car domestically to any state. Send the release paperwork, and the pickup is booked for the day the terminal makes it available."),
 ("What do you need for a Virginia Beach car shipping quote?","Where the car is and where it goes, with the neighborhood or the base. Year, make, and model. Whether it runs. Open or enclosed. The week around the report date or the closing. That covers it, and the Virginia Beach number is back the same day."),
]
BODY.append(faq_section(FAQ,'Virginia Beach FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Virginia Beach?','Price the lane on the form above in two minutes. Tell us the neighborhood and the week, and a carrier already crossing the tunnels takes it.','+17579083865','(757) 908-3865','Get your free Virginia Beach quote'))

build({
 'slug':'auto-transport-virginia-beach-virginia',
 'title':'Car Shipping in Virginia Beach, VA — Auto Transport | Ship Guy',
 'meta':'Car shipping in Virginia Beach, VA, at the end of Interstate 64 in the biggest Navy town in the world. Orders to Oceana, Little Creek, and Norfolk, the tunnels and the tolls, convention-center handoffs for the Oceanfront, curbside pickups in Kempsville and Great Neck, Chesapeake and Newport News, the summer season, and the storms. Local office on South Boulevard by Lynnhaven. Free quote.',
 'h1':'Car Shipping in<br>Virginia Beach, <span class="accent">Virginia</span>',
 'lede':'Open, enclosed, and expedited auto transport across Hampton Roads, planned around 264, the tunnels, the base calendar, the summer strip, and the storms.',
 'tel':'+17579083865','disp':'(757) 908-3865','brand':'Virginia Beach','keyword':'car shipping in virginia beach',
 'localterms':['virginia beach','hampton roads','interstate 264','interstate 64','tunnels','south boulevard','lynnhaven','oceanfront','chesapeake','norfolk','hampton','independence','birdneck','virginia beach boulevard','shore drive','north end','great neck','kempsville','town center','sandbridge','pungo','bases','shipyards','port','hospitals','richmond','petersburg','raleigh','washington','baltimore','philadelphia','charlotte','new york','atlanta','florida','chic’s beach','red mill','dead end','hampton roads tunnel','monitor-merrimac','downtown','midtown','portsmouth','toll','bay bridge-tunnel','eastern shore','us 58','princess anne road','general booth','us 60','cape','atlantic avenue','resort strip','mall','convention center','19th street','amphitheater','rudee inlet','40th street','pacific','one-way','pines','alanton','cul-de-sacs','bayside','thoroughgood','lake smith','pembroke','towers','garages','thalia','windsor woods','strawberry','blackwater','greenbrier','suffolk','peninsula','jacksonville','orlando','sailors','shipbuilders','nurses','contractors','navy','oceana','fighter squadrons','little creek','amphibious','dam neck','naval station','orders','gated','newport news','repair yards','welders','defense contractors','customs','traveling nurses','medical school','residents','broadcaster','university','centerville turnpike','chainsaw','state university','colleges','military retirees','northeast','summer season','memorial day','labor day','marathon','boardwalk','neptune festival','sand sculptures','half a million','air show','patriotic festival','concert nights','hurricane season','isabel','matthew','fourteen inches','nor’easters','january 2018','foot','ninety-five degrees','car shows','bill of lading','fmcsa','surety bond','cape henry'],
}, BODY, FAQ)
