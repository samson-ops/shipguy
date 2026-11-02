import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("2–4 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Rio Rancho, New Mexico','Car shipping on the west mesa, where the chip plant, the two hospitals, and the Albuquerque pool across the river set the week',
 ['Car shipping in Rio Rancho runs on Highway 528 and the bridges, because the city has no interstate. Ship Guy is a licensed auto transport broker with an office on Quantum Road off Northern Boulevard.',
  'We book vetted carriers across Rio Rancho, from the older grids along 528 to Enchanted Hills and Cabezon. Corrales, Bernalillo, and Placitas ride the same trucks. Ship Guy holds the license and the bond. The carriers hold the keys to the trucks.',
  'Highway 528 runs from the Alameda bridge north through the city to Bernalillo and Interstate 25. Southern and Northern Boulevards cross the mesa east and west. Unser Boulevard runs north and south through the middle. Highway 550 runs from Bernalillo across the river and northwest toward Farmington.',
  'This page covers 528, the bridges, 25 at Bernalillo, Southern, Northern, Unser, the Estates, and the dirt roads. It also covers the chip plant, the hospitals, the base and the labs, balloon week, and the wind.'],
 'Rio Rancho at a glance',
 ['A Rio Rancho pickup usually takes 2 to 4 days. The city rides the Albuquerque pool. The 25 and 40 carriers that cross the Big I reach the mesa in half an hour. The Denver trucks come down 25 and stop at Bernalillo.',
  'Santa Fe is a same-day haul. El Paso and Amarillo take a day. Phoenix and Denver take one to two, and Oklahoma City, Las Vegas, and Dallas take two. Los Angeles and Houston take two to three.'],
 'Tell us the subdivision. Corrales, the Estates, Placitas, and the dirt roads meet the truck on pavement or at a 528 lot. The grids along 528, Enchanted Hills, Cabezon, Northern Meadows, and Loma Colorado usually allow the curb.'))

BODY.append(sec('The Roads','Highway 528, Southern Boulevard, Northern Boulevard, Unser Boulevard, Highway 550, the River Bridges, Interstate 25 at Bernalillo, and Corrales Road',
 prose(
  L('Rio Rancho is a grid on a mesa above the Rio Grande, with four bridges to the metro. A carrier comes off 25 at Bernalillo or crosses a bridge and stays on the boulevards.'),
  P('Highway 528 is the spine, from the Alameda bridge north past the plant to Bernalillo. Interstate 25 passes Bernalillo five miles east of the city. The 550 exit is the one a carrier uses. The Alameda, Paseo del Norte, and Montaño bridges carry the city into Albuquerque. The 550 bridge at Bernalillo carries it north. Corrales Road is two lanes through the village under the cottonwoods, and a trailer does not use it.'),
  P('Southern Boulevard runs the length of the city past the city center and the events center. Northern Boulevard runs parallel a mile north. Unser Boulevard runs north and south through the middle past the two hospitals and the college campuses. Westside Boulevard and Idalia Road carry the south and the north. Paseo del Volcan runs along the west edge toward 550 and will reach Interstate 40 someday. Beyond the pavement, the Estates are miles of platted dirt roads with no water or power.'),
  P('The carriers come across the Alameda bridge or down 528 from Bernalillo. They meet at the big-box lots on 528 or the lots at the events center. The lots at the city center on Unser work outside an event. So do the lots at the casino on 550 and the truck stops on 25 at Bernalillo. The Albuquerque airport is forty minutes away for a fly-and-ship.'),
  P('Our office is on Quantum Road off Northern Boulevard, a few blocks west of 528.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','The Grids Along 528, Rivers Edge, Chamisa Hills, Vista Hills, Loma Colorado, Enchanted Hills, Northern Meadows, Cabezon, Mariposa, the Estates, Corrales, Bernalillo, and Placitas',
 prose(
  L('Rio Rancho is older grids near the river, new subdivisions up the mesa, and platted desert beyond. The truck reaches the curb wherever the street is paved.'),
  P('The older grids along 528, from Rivers Edge to Chamisa Hills, are seventies ranch houses on wide streets. The curb works. Vista Hills and Loma Colorado in the middle are the same with bigger lots. Enchanted Hills in the north by 550 is newer subdivisions with cul-de-sacs. The truck comes to the house. Northern Meadows and Cabezon on the west side are the newest, and the carrier maps lag their streets. Send the full address.'),
  P('Mariposa in the far northwest is a master-planned community on its own road. The handoff happens at the entrance. The Estates beyond the pavement are platted lots on dirt roads with no turnaround. The handoff moves to the nearest paved road or the 528 lots. The city center on Unser is apartments, the campuses, and the arena. The handoff happens in the lots.'),
  P('Corrales across the line is a village of horse properties and dirt lanes under the cottonwoods. The handoff happens on 528 or at the village lots. Bernalillo is an old plaza town on the river with narrow streets, and the handoff happens on 550. Placitas across 25 is hillside houses on dirt roads with gates. The handoff happens at the bottom of the hill.'),
  P('Corrales, Bernalillo, and Albuquerque’s west side ship with the same trucks and price the same as Rio Rancho. Placitas adds a few dollars for the hill. Santa Fe is an hour up 25 and prices with the metro.'),
 )))

ROUTES=[("Santa Fe, NM","I-25 · ~50 mi","Same day","$150–$240"),("El Paso, TX","I-25/I-10 · ~280 mi","1 day","$250–$380"),
 ("Amarillo, TX","I-40 · ~300 mi","1 day","$270–$400"),("Phoenix, AZ","I-40/I-17 · ~430 mi","1–2 days","$380–$540"),
 ("Denver, CO","I-25 · ~440 mi","1–2 days","$400–$560"),("Oklahoma City, OK","I-40 · ~555 mi","2 days","$440–$630"),
 ("Las Vegas, NV","I-40/US-93 · ~590 mi","2 days","$460–$670"),("Dallas, TX","I-40/US-287 · ~660 mi","2 days","$470–$680"),
 ("Los Angeles, CA","I-40 · ~810 mi","2–3 days","$560–$820"),("Houston, TX","I-40/US-287/I-45 · ~860 mi","2–3 days","$620–$880")]
BODY.append(rate_table('Lanes &amp; Costs','Rio Rancho Car Shipping Lanes and Estimated Costs',
 'The lanes Sandoval County cars run most, with an open-trailer range for each. Your own lane prices above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Rio Rancho for a sedan that runs on an open trailer. Figure 10 to 25 percent more for an SUV or a pickup, and more for an enclosed trailer. The week and the carriers on 25 and 40 that week set the real figure.',
 prose(
  P('Rio Rancho prices with Albuquerque on every lane, because the same pool serves the whole metro. The Denver lane rides 25 north from Bernalillo and fills every day. The Phoenix and Los Angeles lanes ride 40 west. The Texas lanes ride 40 east and 25 south. The California lane fills with the transplants and the retirees each fall, and the price rises with them.'),
  P('A start date at the chip plant or a balloon-week pickup in October means a busy week. The <a href="car-shipping-cost.html">cost guide</a> spells out what size, condition, and timing do to the figure.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Chip Plant, the Two Hospitals, the Base and the Labs Across the River, the Offices on Unser, the Campuses, the Pueblos, and the Retirees',
 prose(
  L('Rio Rancho relocates engineers, technicians, nurses, airmen, scientists, and retirees. The chip plant moves the most.'),
  P('The chip plant on the mesa edge employs thousands and is building out again. It relocates engineers and technicians from Arizona, Oregon, and overseas on start dates. The packages usually pay for a car, and the handoff happens at the 528 lots or the house. The call centers and the offices along Unser move staff the same way. When the plant or the lab pays you back, we document it the way they ask.'),
  P('The two hospitals on Unser bring residents each June and hire traveling nurses all year. The base and the national laboratory across the river in Albuquerque employ thousands of Rio Rancho families. They relocate airmen, engineers, and scientists on orders and clearance timelines. The handoff for the base happens outside the gate on the Albuquerque side. Ship Guy is a private company, unconnected to the Air Force or the labs. The <a href="military-car-shipping.html">military</a> page lays out what a set of orders does to the schedule.'),
  P('The two college campuses at the city center take students in late August, and most of them commute. The pueblos along the river and the casino on 550 hire on their own calendar. Retirees come from California, Texas, and the Midwest for the dry air and the tax rates. Some go back for the summer. Crossing into another state adds paperwork, and the <a href="state-to-state-car-shipping.html">state-to-state</a> page walks through it.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Balloon Week, the Fourth, the State Fair, the Harvest Festival, the Spring Wind, the Monsoon, the Arroyos, the Snow, and the Smoke',
 prose(
  L('Rio Rancho runs on an Albuquerque calendar and a plant calendar. The weather problem is a spring wind that stops high trailers and a monsoon that fills the arroyos.'),
  P('Balloon week takes the first nine days of October. The dawn traffic to the launch field clogs Alameda, 528, and 25 from before sunrise. The carriers meet on the mesa after nine those mornings. The Fourth fills the events center lots with the barbecue festival. The state fair in September and the harvest festival in Corrales take the weekends around them. Give a balloon-week date three weeks of notice.'),
  P('The wind blows from March into May. The gusts on the mesa pass sixty miles an hour with the dust behind them. A carrier does not load in it, and the handoff waits for a calm morning. The monsoon runs from July into September. An afternoon storm fills the arroyos and floods Southern Boulevard at the low spots. A driver loads in the morning and waits out a warning. The December 2006 storm dropped more than a foot on the mesa. The February 2011 freeze shut the gas off across the state for days.'),
  P('Smoke from the mountain fires settles on the valley in June some years. The carriers keep moving through it. Summer heat holds the mesa in the upper nineties for weeks, and the figure holds with it.'),
  P('Snow comes a few mornings each winter and melts by noon. A trailer waits for the bridges to clear, usually an hour.'),
 )+chips(["Rivers Edge","Chamisa Hills","Vista Hills","Loma Colorado","Panorama Heights","The City Center","Enchanted Hills","Northern Meadows","Cabezon","Mariposa","The Estates","Corrales","Bernalillo","Placitas","Algodones","Paradise Hills","Ventana Ranch","Taylor Ranch"])
 +NOTE('Serving Rio Rancho, Corrales, Bernalillo, and the west mesa, Enchanted Hills curb or Estates dirt road. Tell us the subdivision and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Rio Rancho?',
 prose(
  L('Rio Rancho ships open nearly every time, and the table above is figured for an open trailer.'),
  P('Enclosed keeps the spring dust, the sun, and the hail of a monsoon storm off the paint. The collectors in Corrales book it. So do the engineers moving a car from overseas worth more than the rest of the container. When a windstorm is coming and only an open truck has room, we say so first.'),
  P('A commuter car or an engineer’s crossover is fine in the open. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages put the two side by side.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A figure first, then a lot on 528, then a signature at the far end. The start date or the move sets the week.'),
  P('Say yes to the figure, and a carrier already running 25 or 40 that week gets the car. The lot and the window get settled that afternoon. The driver photographs the car at pickup and records its condition on the Bill of Lading. You initial it, and delivery works from that sheet.'),
 )+ULI([
  "Cabin and trunk emptied of your things",
  "Fuel down to a quarter tank or less",
  "Each side and the odometer in your own photos",
  "A good key and a note about anything that does not work",
  "Add-on alarms disabled",
  "In the Estates, in Corrales, or on a dirt road, expect a lot on 528",
 ])+prose(P('For the steps, read <a href="how-it-works.html">how it works</a>. For pickup day, read <a href="car-shipping-preparation.html">preparation</a>.'))))

BODY.append(sec('Why Ship Guy','Why Rio Rancho Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already work the Albuquerque pool every day. We know which subdivisions the maps have not reached and which mornings the wind cancels.'),
  P('Our FMCSA license and $75,000 bond are listed on the federal register. The office is on Quantum Road.'),
  P('One coordinator stays on your move from the quote to the delivery call. For open, enclosed, and expedited, see the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Rio Rancho','661 Quantum Rd NE #325','Rio Rancho, NM 87124','+15054075664','(505) 407-5664','MT',
 '661+Quantum+Rd+NE+%23325,+Rio+Rancho,+NM+87124','Visit Us','Find Ship Guy in Rio Rancho',
 'Our office is on Quantum Road off Northern Boulevard, a few blocks west of 528.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4020.9209254605944!2d-106.6341961!3d35.269813899999995!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x872271c46157797d%3A0x7e1dd7f4bfc97027!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793631646776!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Rio Rancho to Denver or Phoenix?","Denver runs four hundred to five hundred sixty dollars for a sedan. That is about four hundred forty miles up 25 from Bernalillo. Phoenix runs three hundred eighty to five hundred forty, about four hundred thirty miles out 40. Santa Fe is the lowest lane on the table, an hour up 25. For an SUV or a pickup, figure 10 to 25 percent more."),
 ("Do you work with relocation packages at the chip plant?","Yes, every month. The plant relocates engineers and technicians from Arizona, Oregon, and overseas on start dates. The packages usually pay for a car. We plan the pickup around the first day at the plant. The handoff happens at the 528 lots or the house. When the plant pays you back, we document it the way it asks."),
 ("Why does a Rio Rancho pickup take 2 to 4 days?","Because the mesa rides the Albuquerque pool. A car waits for the next carrier crossing the Big I with room. Denver and Phoenix trucks come most often. A windstorm or a monsoon afternoon pushes the window a day, and we tell you when it does."),
 ("Can the carrier come to my street in Rio Rancho?","On the paved streets, yes. The grids along 528, Enchanted Hills, Cabezon, Northern Meadows, and Loma Colorado have wide streets. The truck reaches the curb. Send the full address, because the newest streets are not on the carrier maps. The Estates, Corrales, and Placitas are dirt roads. The handoff moves to the nearest paved road or the 528 lots."),
 ("What happens if the spring wind or a monsoon storm hits on my pickup day?","The truck waits for a calm morning. A carrier does not load in a sixty-mile-an-hour gust with dust behind it. A monsoon storm fills the arroyos and floods the low spots on Southern for an hour. We call the moment the forecast turns. The pickup moves to the next workable morning at the same figure."),
 ("Do you ship cars for the base and the labs across the river?","Yes, in every season. The base and the national laboratory in Albuquerque relocate airmen, engineers, and scientists on orders and clearance timelines. The handoff for the base happens outside the gate on the Albuquerque side. The labs ship from the house or the 528 lots. Ship Guy is a private company with no tie to the Air Force or the labs."),
 ("Can you ship a car to or from Corrales, Bernalillo, or Placitas?","Yes. Corrales, Bernalillo, and Albuquerque’s west side ride the same carriers and price the same as Rio Rancho. Corrales meets the truck on 528 or at the village lots. The lanes are dirt under the cottonwoods. Bernalillo meets it on 550. Placitas adds a few dollars for the hill and meets the truck at the bottom of it."),
 ("Does balloon week affect my pickup?","For nine mornings in October. The dawn traffic to the launch field clogs Alameda, 528, and 25 from before sunrise. The carriers meet on the mesa after nine. The afternoons run normally. Give a balloon-week date three weeks of notice, and the figure does not change."),
 ("Can you ship a car that does not run from Rio Rancho?","Yes. A winch truck handles it, and the loading time is priced in. The big-box lots on 528 and the events center lots are flat. The only question is whether it rolls, steers, and brakes."),
 ("What do you need for a Rio Rancho car shipping quote?","Start and end, with the subdivision. Year, make, and model, and whether it runs. Open or enclosed, and the week around the start date or the move. That is enough for a Rio Rancho figure the same afternoon."),
]
BODY.append(faq_section(FAQ,'Rio Rancho FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Rio Rancho?','Two minutes on the form above returns a Rio Rancho figure for your lane. Give the subdivision and the week, and a carrier already running 25 takes the car.','+15054075664','(505) 407-5664','Get your free Rio Rancho quote'))

build({
 'slug':'auto-transport-rio-rancho-new-mexico',
 'title':'Car Shipping in Rio Rancho, NM — Auto Transport | Ship Guy',
 'meta':'Car shipping in Rio Rancho, NM, on the west mesa above Albuquerque. Chip-plant relocation packages, the two hospitals on Unser, the base and the labs across the river, curbside pickups in the grids along 528, Enchanted Hills, Cabezon, and Northern Meadows, paved-road handoffs for the Estates, Corrales, and Placitas, balloon week, the spring wind, and the monsoon. Local office on Quantum Road. Free quote.',
 'h1':'Car Shipping in<br>Rio Rancho, <span class="accent">New Mexico</span>',
 'lede':'Open, enclosed, and expedited auto transport across Rio Rancho, Corrales, Bernalillo, and the west mesa, planned around 528, the bridges, the plant’s start dates, balloon week, the wind, and the monsoon.',
 'tel':'+15054075664','disp':'(505) 407-5664','brand':'Rio Rancho','keyword':'car shipping in rio rancho',
 'localterms':['rio rancho','west mesa','highway 528','alameda','paseo del norte','montaño','bridges','rio grande','interstate 25','bernalillo','highway 550','farmington','southern boulevard','northern boulevard','unser','westside boulevard','idalia','paseo del volcan','interstate 40','corrales road','cottonwoods','quantum road','big i','the estates','platted','dirt roads','rivers edge','chamisa hills','vista hills','loma colorado','panorama heights','city center','events center','arena','enchanted hills','northern meadows','cabezon','mariposa','entrance','corrales','horse properties','village','plaza','placitas','algodones','paradise hills','ventana ranch','taylor ranch','west side','chip plant','mesa edge','building out','engineers','technicians','arizona','oregon','overseas','packages','call centers','two hospitals','residents','traveling nurses','base','national laboratory','airmen','scientists','clearance','college campuses','students','commute','pueblos','casino','retirees','california','texas','midwest','dry air','tax rates','balloon week','nine days','launch field','dawn','the fourth','barbecue festival','state fair','harvest festival','spring wind','sixty miles an hour','dust','monsoon','arroyos','low spots','december 2006','more than a foot','february 2011','freeze','gas','smoke','mountain fires','upper nineties','snow','truck stops','airport','fly-and-ship','santa fe','el paso','amarillo','phoenix','denver','oklahoma city','las vegas','dallas','los angeles','houston','hail','bill of lading','fmcsa','winch'],
}, BODY, FAQ)
