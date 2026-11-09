import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Hampton, Virginia','Car shipping at the mouth of the harbor, where Interstate 64 dives under the water, the fighter wing rotates every summer, and a king tide floods the low streets',
 ['Car shipping in Hampton runs on Interstate 64, which crosses the city to the bridge-tunnel. Ship Guy is a licensed auto transport broker with an office at Peninsula Town Center in Coliseum Central.',
  'We book vetted carriers across Hampton, from Phoebus and Fox Hill to the subdivisions off Big Bethel Road. Newport News, Poquoson, York County, and the Norfolk side of the tunnel ride the same trucks. The trucks belong to the carriers. Ship Guy holds the license and the bond.',
  'Interstate 64 runs the middle of the city with exits at Mercury Boulevard, Armistead Avenue, and Settlers Landing. Interstate 664 leaves it at the west edge for the Monitor-Merrimac crossing to Suffolk. Mercury Boulevard is the retail spine. Settlers Landing Road, Pembroke Avenue, Fox Hill Road, and Kecoughtan Road carry the rest.',
  'This page covers 64, 664, the tunnel widening, Mercury Boulevard, downtown, and the old waterfront wards. It also covers the air base, the research center, the shipyard next door, the university, and the hospitals. The jazz festival, the regatta, the hurricanes, and the tides are here too.'],
 'Hampton at a glance',
 ['Most Hampton pickups land within 1 to 3 days. The city sits where every Peninsula truck lines up for the bridge-tunnel. The Richmond carriers come down 64, and the Carolina carriers come through Suffolk on 58 and 664. The base and the shipyard keep the pool full year round.',
  'Richmond, Washington, Raleigh, and Baltimore are a same-day haul. Philadelphia, Charlotte, and New York take a day. Atlanta takes one to two, and Florida takes two.'],
 'Tell us the neighborhood. Phoebus, downtown, Wythe, and the Fox Hill lanes meet the truck on Mercury Boulevard. Northampton, Farmington, Magruder, Bethel, and the York County subdivisions usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 64, Interstate 664, the Hampton Roads Bridge-Tunnel, Mercury Boulevard, Settlers Landing Road, Armistead Avenue, Magruder Boulevard, Pembroke Avenue, Fox Hill Road, Big Bethel Road, and Kecoughtan Road',
 prose(
  L('Hampton is a flat harbor city with one freeway through the middle and a tunnel at the end. A carrier times the tunnel and works the boulevards.'),
  P('Interstate 64 comes down the Peninsula from Richmond and Newport News and runs the length of the city. The exits at Mercury Boulevard, Armistead Avenue, Settlers Landing, and Mallory Street serve the city. Then it dives under the harbor to Norfolk in the Hampton Roads Bridge-Tunnel. The state is widening the crossing with twin new tunnels, and the work runs to 2027. Lane shifts and overnight closures come with it. Interstate 664 leaves 64 at the west edge and crosses to Suffolk on the Monitor-Merrimac. It carries no toll, and the carriers use it when the tunnel backs up.'),
  P('Mercury Boulevard is Route 258, the retail spine from the James River Bridge through Coliseum Central to Phoebus. Settlers Landing Road carries downtown and the university. Armistead Avenue and Magruder Boulevard run north to the air base and the research center. Pembroke Avenue runs east to Buckroe and the beach. Fox Hill Road runs out to the old fishing village. Big Bethel Road carries the north side, and Kecoughtan Road carries the old waterfront to Newport News. Mallory Street crosses to Phoebus on the bridge that opened in 2026. LaSalle Avenue and Victoria Boulevard cross the middle.'),
  P('The carriers come off 64 at Mercury Boulevard or Armistead and off 664 at Power Plant Parkway. They meet at the Coliseum lots outside events or the Town Center lots around our office. The big-box lots on Mercury work too. The lots at the Power Plant shopping center work too. So do the university lots in summer and the beach lots at Buckroe in winter. The airport is twenty minutes west in Newport News for a fly-and-ship.'),
  P('Our office is in the office building at Peninsula Town Center, off Mercury Boulevard and 64.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, Phoebus, Wythe, Fox Hill, Buckroe, Aberdeen Gardens, Northampton, Farmington, Magruder, Bethel, Riverdale, Fort Monroe, Poquoson, Tabb, and Newport News',
 prose(
  L('Hampton is an old waterfront city of fishing villages and a postwar city of subdivisions. The truck meets the waterfront wards on a boulevard and the subdivisions at the curb.'),
  P('Downtown is Queens Way, the waterfront, the museum, and short blocks of brick. The streets are narrow, and the handoff happens on Settlers Landing or at the Coliseum lots. Phoebus is the old town across Mill Creek, with Mellen Street’s storefronts and tight blocks behind them. The driver meets you on Mallory Street or Mercury Boulevard. Wythe along Kecoughtan Road is big old houses on narrow lanes under oaks. The handoff happens on Kecoughtan. Fox Hill is the fishing village, tidal lanes that flood on a high tide. The driver meets you on Fox Hill Road or Beach Road.'),
  P('Buckroe is the bay beach and the bungalow blocks behind it, tight and low. The handoff happens at the beach lots or on Pembroke Avenue. Aberdeen Gardens is the historic 1930s neighborhood, wide streets where the curb works. Northampton is postwar grids off Big Bethel, and the curb works. Farmington, Magruder, Michaels Woods, and Bethel are north-side subdivisions where the truck comes to the house. Riverdale and the Mercury corridor are apartments and strip centers. The complexes allow a trailer at the entrance.'),
  P('Fort Monroe is the old post at the tip, closed as a base in 2011. It is a national monument now, with houses on its streets. The driver meets you at the lots by the moat. Poquoson to the north is a fishing town on marsh roads that flood. The handoff happens on Wythe Creek Road. Tabb and Grafton in York County are subdivisions where the curb works. Newport News next door is covered on its own page, and the two cities share every truck.'),
  P('Newport News, Poquoson, Tabb, and Grafton ship with the same trucks and price the same as Hampton. Yorktown and Williamsburg do too. The Norfolk side adds the tunnel, and the figure already includes it.'),
 )))

ROUTES=[("Richmond, VA","I-64 · ~75 mi","Same day","$150–$240"),("Washington, DC","I-64/I-95 · ~180 mi","Same day","$220–$340"),
 ("Raleigh, NC","US-58/I-95 · ~185 mi","Same day","$230–$350"),("Baltimore, MD","I-64/I-95 · ~220 mi","Same day","$240–$360"),
 ("Philadelphia, PA","I-64/I-95 · ~265 mi","1 day","$260–$390"),("Charlotte, NC","US-58/I-85 · ~315 mi","1 day","$300–$440"),
 ("New York, NY","I-95 · ~355 mi","1 day","$340–$490"),("Atlanta, GA","I-85 · ~555 mi","1–2 days","$440–$630"),
 ("Jacksonville, FL","I-95 · ~600 mi","2 days","$450–$650"),("Orlando, FL","I-95 · ~745 mi","2 days","$520–$750")]
BODY.append(rate_table('Lanes &amp; Costs','Hampton Car Shipping Lanes and Estimated Costs',
 'The lanes Peninsula cars ship most, with open-trailer estimates. The form above prices your exact lane.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Hampton, running sedan, open trailer. An SUV or a pickup runs 10 to 25 percent above, and enclosed runs higher. The week and the carriers on 64 that week set the figure.',
 prose(
  P('Hampton prices with Newport News on every lane, because the same trucks serve both. Richmond is an hour up 64, and the carriers run it daily. Washington and Baltimore ride 64 and 95 north. Raleigh and Charlotte ride 58 west through Suffolk and then 95 or 85. The Florida lane fills in October with the retirees and in June with the orders. Norfolk and Virginia Beach sit across the tunnel and price the same.'),
  P('A summer rotation at the base or a jazz festival weekend makes for a busy week. The <a href="car-shipping-cost.html">cost guide</a> covers size, condition, and timing in turn.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Fighter Wing at Langley, the Research Center, the Shipyard Next Door, the University, the Hospitals, the Veterans’ Hospital, the Watermen, and the Retirees',
 prose(
  L('Hampton relocates airmen, engineers, shipbuilders, students, nurses, and retirees. The base and the research center move the most.'),
  P('Joint Base Langley-Eustis sits on the north side of the city. Its fighter wing rotates airmen year round with a summer peak. Families ship a second car on orders every week. The handoff happens at a lot outside the gate. The research center beside the base relocates engineers and scientists on program dates. The shipbuilder next door in Newport News relocates engineers on program schedules. Many of them live in Hampton. The defense contractors along Magruder Boulevard follow the same calendar. When the employer or the agency covers the shipment, we write it up however it needs.'),
  P('Hampton University fills its waterfront campus each August and empties it in May. The community college follows. A parent books, and an adult signs at the campus lot. The hospital on Coliseum Drive brings nurses all year. The veterans’ hospital on Emancipation Drive brings staff on federal schedules. The watermen of Fox Hill and Poquoson stay put. Retirees come to the bay from the Northeast and go south each winter. The <a href="state-to-state-car-shipping.html">state-to-state</a> page explains the paperwork a state line adds.'),
  P('Fort Monroe closed as a post in 2011. The naval station across the harbor rotates sailors on the same summer calendar. Ship Guy is a private broker and not part of the Air Force or the Navy. The <a href="military-car-shipping.html">military</a> page covers orders and the dates they set.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Jazz Festival, the Pirate Festival, the Regatta, the Speedway, Homecoming, the Tunnel Closures, the Hurricanes, the Nor’easters, the Snow, and the Tides',
 prose(
  L('Hampton runs on a base calendar and a harbor calendar. The weather problem is a hurricane every decade, a nor’easter every winter, and a flooding tide.'),
  P('The jazz festival fills the Coliseum for a weekend each June, and the lots go with it. The pirate festival fills downtown and the waterfront the same month. The hydroplane regatta fills Mill Creek and the Fort Monroe shore each August. The speedway runs Saturday nights from April to October. The university’s homecoming fills Settlers Landing each October. The tunnel work closes lanes overnight and shuts the crossing a few nights a year. Give a festival weekend or a rotation week three weeks of notice.'),
  P('Isabel in September 2003 pushed the surge over Fox Hill, Buckroe, Phoebus, and downtown. Trees were down for weeks, and the tunnel closed. Irene in 2011 and Matthew in 2016 flooded the same streets with rain. A nor’easter does it again a few times each winter. Before a landfall the carriers move inland, and the Peninsula pickups wait until the tunnel reopens.'),
  P('The January 2018 storm dropped a foot of snow, and the January 2022 storms did it twice. The side streets stay white for days. A king tide alone floods the low lanes in Fox Hill and Buckroe. A strong wind closes the bridge-tunnel to high-profile vehicles, and a loaded carrier waits. Fog settles on the harbor on fall mornings, and summer brings heat and a storm most afternoons.'),
 )+chips(["Downtown","Queens Way","Phoebus","Mellen Street","Wythe","Fox Hill","Buckroe","Aberdeen Gardens","Northampton","Farmington","Magruder","Michaels Woods","Bethel","Riverdale","Coliseum Central","Fort Monroe","Langley","Poquoson","Tabb","Grafton","Yorktown","Williamsburg","Newport News"])
 +NOTE('Serving Hampton, the lower Peninsula, and York County, Fox Hill lane or Magruder cul-de-sac. Name the neighborhood and tell us whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Hampton?',
 prose(
  L('Open trailers carry most of the Peninsula’s cars, and the table above prices one.'),
  P('Enclosed keeps the salt air, the brine, and the pollen off the paint. The officers moving a car worth more than the orders cover book it. So do the engineers at the research center with a restored car. When a storm is coming and only an open truck has room, we say so first.'),
  P('A commuter car or a student’s sedan rides open and arrives fine. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain the difference.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A figure, a lot off Mercury Boulevard, and a signature when the car comes off the truck. The orders or the program date set the week.'),
  P('Approve the figure, and we hand the car to a carrier already running 64 that week. The lot and the window are set the same day. The driver photographs the car at pickup and writes its condition on the Bill of Lading. You initial it, and it is the reference at delivery.'),
 )+ULI([
  "Your belongings out of the cabin and the trunk",
  "Fuel at a quarter tank or less",
  "Photos of every side and the odometer before the truck arrives",
  "A working key and a note on anything that acts up",
  "Aftermarket alarms turned off",
  "In Phoebus, in Wythe, or on a Fox Hill lane, expect the Coliseum lots or Mercury Boulevard",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> page walks the steps, and the <a href="car-shipping-preparation.html">preparation</a> page covers pickup morning.'))))

BODY.append(sec('Why Ship Guy','Why Hampton Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already run 64 to the tunnel every day. We know which nights the crossing closes and which lanes flood on a tide.'),
  P('Our FMCSA license and our $75,000 bond are a matter of public record on the federal register. The office is at Peninsula Town Center.'),
  P('One person at Ship Guy carries your move from the quote to the delivery call. The <a href="services.html">services</a> page covers open, enclosed, and expedited one by one.'),
 )))

BODY.append(office('Hampton','4410 E Claiborne Square Suite 594','Hampton, VA 23666','+17575519799','(757) 551-9799','ET',
 '4410+E+Claiborne+Square+Suite+594,+Hampton,+VA+23666','Visit Us','Find Ship Guy in Hampton',
 'Our office is in the office building at Peninsula Town Center, off Mercury Boulevard and 64.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3930.8495032672313!2d-76.3935662!3d37.045907899999996!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89ba838a9fce6ba7%3A0x74469e16cf0626d!2sShip%20Guy%20Auto%20Transport!5e1!3m2!1sen!2sus!4v1794237444228!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Hampton to Richmond or Florida?","Richmond runs one hundred fifty to two hundred forty dollars for a sedan, an hour up 64. Orlando runs five hundred twenty to seven hundred fifty and takes two days. Washington runs two hundred twenty to three hundred forty. An SUV or a pickup adds 10 to 25 percent."),
 ("Do you ship cars for Langley families on orders?","Yes, every week, with a summer peak. The fighter wing rotates airmen year round, and families ship a second car when the orders cover one. The handoff happens at a lot outside the gate on Armistead or at the Town Center. Ship Guy is a private broker and not part of the Air Force."),
 ("Does the tunnel widening affect my shipment?","In timing. The work runs to 2027 with lane shifts and overnight closures. The crossing shuts a few nights a year. A carrier crossing to Norfolk plans for mid-morning or uses the Monitor-Merrimac on 664. The figure does not change."),
 ("Can the carrier come to my street in Phoebus, Wythe, or Fox Hill?","Usually not. Phoebus is tight blocks behind Mellen Street, and Wythe is narrow lanes under oaks. The Fox Hill lanes flood on a high tide. The driver meets you on Mercury Boulevard, Kecoughtan Road, or at the Coliseum lots. Northampton, Farmington, Magruder, Bethel, and the York County subdivisions usually allow the curb."),
 ("Can you deliver a car for a Hampton University student?","Yes. Cars arrive in August and leave in May. A parent books, and an adult signs at the campus lot off Settlers Landing. Homecoming weekend in October closes the streets around the campus. The handoff moves to the Coliseum lots that weekend."),
 ("What happens if a hurricane or a nor’easter is coming?","The carriers move inland before a landfall, and the Peninsula pickups wait until the tunnel reopens. Isabel in 2003 put Fox Hill, Buckroe, and downtown under the surge. A nor’easter floods the same streets a few times each winter. We call when the forecast turns, and the figure stays where it was."),
 ("Do you ship cars for the research center or the shipyard?","Yes. The research center relocates engineers and scientists on program dates. The shipbuilder next door relocates engineers on program schedules. The contractors along Magruder Boulevard follow the same calendar. When the employer or the agency pays, we write it up however it needs."),
 ("Can you ship a car to or from Poquoson, Yorktown, or Fort Monroe?","Yes. Newport News, Poquoson, Tabb, and Grafton ride the same carriers and price the same as Hampton. Yorktown and Williamsburg do too. Fort Monroe takes a handoff at the lots by the moat. Poquoson takes one on Wythe Creek Road."),
 ("Can you ship a car that does not run from Hampton?","Yes. The carrier brings a winch, and the figure includes the loading time. The Coliseum lots and the Town Center lots are flat. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Hampton car shipping quote?","Both addresses, with the neighborhood or the gate. The year, make, and model, and whether it runs. Open or enclosed, and the week around the orders or the program date. With those, the Hampton figure comes back the same day."),
]
BODY.append(faq_section(FAQ,'Hampton FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Hampton?','Two minutes on the form above puts a Hampton figure on your lane. Name the neighborhood and the week, and a carrier already on 64 takes it.','+17575519799','(757) 551-9799','Get your free Hampton quote'))

build({
 'slug':'auto-transport-hampton-virginia',
 'title':'Car Shipping in Hampton, VA — Auto Transport | Ship Guy',
 'meta':'Car shipping in Hampton, VA, where Interstate 64 meets the bridge-tunnel. Langley orders and the research center, the shipyard next door, Hampton University move-in dates, boulevard handoffs for Phoebus, Wythe, and Fox Hill, curbside pickups in Northampton, Farmington, Magruder, and York County, the tunnel widening, the hurricanes, and the tides. Local office at Peninsula Town Center. Free quote.',
 'h1':'Car Shipping in<br>Hampton, <span class="accent">Virginia</span>',
 'lede':'Open, enclosed, and expedited auto transport across Hampton, the lower Peninsula, and York County, planned around 64, the tunnel, the orders, the festivals, the storms, and the tides.',
 'tel':'+17575519799','disp':'(757) 551-9799','brand':'Hampton','keyword':'car shipping in hampton',
 'localterms':['hampton','interstate 64','interstate 664','bridge-tunnel','monitor-merrimac','twin new tunnels','2027','mercury boulevard','route 258','settlers landing','armistead avenue','magruder boulevard','pembroke avenue','fox hill road','big bethel road','kecoughtan road','mallory street','lasalle avenue','victoria boulevard','power plant parkway','james river bridge','coliseum central','coliseum lots','town center','peninsula town center','downtown','queens way','waterfront','museum','phoebus','mill creek','mellen street','wythe','oaks','fox hill','fishing village','high tide','beach road','buckroe','bay beach','bungalow','aberdeen gardens','1930s','northampton','farmington','magruder','michaels woods','bethel','riverdale','fort monroe','2011','national monument','moat','poquoson','wythe creek road','tabb','grafton','york county','yorktown','williamsburg','newport news','joint base langley-eustis','fighter wing','airmen','orders','research center','shipbuilder','defense contractors','hampton university','community college','hospital','coliseum drive','veterans’ hospital','emancipation drive','watermen','retirees','naval station','jazz festival','pirate festival','hydroplane','regatta','speedway','homecoming','overnight closures','isabel','september 2003','surge','irene','matthew','nor’easter','january 2018','foot of snow','january 2022','king tide','high-profile','fog','richmond','washington','raleigh','baltimore','philadelphia','charlotte','new york','atlanta','jacksonville','orlando','norfolk','virginia beach','suffolk','58','fly-and-ship','airport','salt air','brine','pollen','restored car','bill of lading','fmcsa','winch'],
}, BODY, FAQ)
