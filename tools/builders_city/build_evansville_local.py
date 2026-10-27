import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Evansville, Indiana','Car shipping on the Ohio River bend, where Interstate 69 ends at the water and Interstate 64 passes to the north',
 ['Car shipping in Evansville runs between Interstate 64 to the north and the river to the south. Ship Guy is a licensed auto transport broker with an office in the Old Courthouse downtown.',
  'We book vetted carriers across the tri-state, from Newburgh to Mount Vernon and across the bridges to Henderson. We do not own the trucks.',
  'Interstate 69 comes down from Indianapolis and ends at the river until the new bridge opens. Interstate 64 crosses ten miles north on its way from St. Louis to Louisville. The Lloyd Expressway runs east and west through the city. US 41 crosses the Twin Bridges into Kentucky.',
  'This page covers the interstates, the Lloyd, downtown, the West Side, the East Side, and Newburgh. It also covers the hospitals, the Toyota plant, the campuses, the Fall Festival, the river, and the lanes.'],
 'Evansville at a glance',
 ['Most pickups happen within 1 to 3 days. Carriers running 64 between St. Louis and Louisville drop down US 41 or 69 for a load.',
  'Louisville, Nashville, St. Louis, and Indianapolis are all a same-day haul. Chicago, Cincinnati, and Memphis take a day. Atlanta and Dallas need two, and the coasts need three to five.'],
 'Tell us the side of the Lloyd. Downtown and the old West Side need a meeting spot. The East Side, Newburgh, and the north side usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 69, Interstate 64, the Lloyd Expressway, US 41, and Green River Road',
 prose(
  L('Evansville is the corner where Indiana, Kentucky, and Illinois meet, and the trucks arrive from all three.'),
  P('Interstate 64 runs east and west ten miles north of downtown. Every carrier between St. Louis and Louisville passes the US 41 and 69 exits. Interstate 69 comes down from Indianapolis and crosses 64. It runs the east side of the city to the river. The new Ohio River bridge will carry it into Kentucky when it opens.'),
  P('The Lloyd Expressway is State Road 62 and 66, the main road across the city. It runs from the West Side past downtown to the East Side and on to Newburgh. US 41 is the north-south strip through the middle. It crosses the Twin Bridges to Henderson. Highway 57 reaches the airport and the Toyota plant.'),
  P('Green River Road and Burkhardt Road carry the East Side. First Avenue and Diamond Avenue cross the north side. Morgan Avenue and Washington Avenue run east from downtown. Franklin Street runs the West Side. Riverside Drive follows the river past the casino. Oak Hill, Boonville-New Harmony Road, and Red Bank Road reach the county.'),
  P('The carriers come off 64 at US 41 and 69, and off the Lloyd at Green River Road. The mall lot on Green River and the arena lots are the usual meeting spots. No road in Vanderburgh County charges a toll. The new bridge will, once it opens.'),
  P('Our office is in the Old Courthouse downtown, two blocks from the Lloyd and the Civic Center.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the West Side, the East Side, the North Side, Newburgh, and Henderson',
 prose(
  L('Evansville is a river city with an old West Side and a growing East Side. Small towns sit in every direction.'),
  P('Downtown sits on the bend between the Lloyd and the river. It is a grid of one-way streets around the courthouse and the arena. A trailer cannot stop on Main Street. The driver meets you at the arena lots or on Riverside by the casino. Haynie’s Corner and the historic district on the south edge have narrow streets under old trees. The handoff moves to the Lloyd.'),
  P('The West Side across Pigeon Creek is the old German side, with Franklin Street at its heart. The streets are narrow and the houses close. The driver meets you on Franklin or at the shopping center on the Lloyd. Howell, Lamasco, and Jacobsville by the creek are the same. Garvin Park and the Diamond Avenue grids to the north allow the curb.'),
  P('The East Side along Green River and Burkhardt is the growth side. It has the mall, the hospital campus, and subdivisions out to 69. The truck reaches the curb. The north side along Oak Hill and First Avenue is postwar grids with wide streets. Darmstadt and McCutchanville by the airport are country lanes, and the driver meets you on Highway 57.'),
  P('Newburgh on the river east of town is a Warrick County suburb. It has a historic riverfront and wide new subdivisions. The driver meets you on the Lloyd or at a lot in town. Boonville and Chandler beyond it are small towns with lots on every main road. Henderson across the bridges and Mount Vernon downriver price the same as Evansville, and so does Newburgh.'),
 )))

ROUTES=[("Louisville, KY","I-64 · ~120 mi","Same day","$170–$270"),("Nashville, TN","I-69/I-24 · ~155 mi","Same day","$190–$300"),
 ("St. Louis, MO","I-64 · ~170 mi","Same day","$200–$310"),("Indianapolis, IN","I-69 · ~175 mi","Same day","$200–$310"),
 ("Cincinnati, OH","I-64/I-71 · ~240 mi","1 day","$240–$360"),("Chicago, IL","I-69/I-65 · ~290 mi","1 day","$280–$410"),
 ("Memphis, TN","I-69/I-24/I-40 · ~330 mi","1 day","$310–$450"),("Atlanta, GA","I-24/I-75 · ~410 mi","1 day","$360–$520"),
 ("Dallas, TX","I-64/I-44 · ~720 mi","2 days","$530–$760"),("Orlando, FL","I-24/I-75 · ~880 mi","2–3 days","$620–$880")]
BODY.append(rate_table('Lanes &amp; Costs','Evansville Car Shipping Lanes and Estimated Costs',
 'The lanes tri-state cars take most, with estimated open-trailer ranges. Your exact route prices on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates out of Evansville, sedan that starts and drives, open trailer. An SUV or pickup costs 10 to 25 percent more, and an enclosed trailer costs more again. Fuel, the season, and the carriers free on your dates set the final figure.',
 prose(
  P('Evansville prices a little under Indianapolis on the Nashville and St. Louis lanes. The 64 carriers pass close by. The Louisville lane runs daily and prices the lowest of all. The Chicago lane rides 69 and 65 and runs lighter, which adds a day.'),
  P('Florida and Texas follow the snowbird calendar, higher in the fall and lower in the spring. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Hospitals, the Toyota Plant, the Campuses, the Plastics Company, and the Refineries',
 prose(
  L('Evansville relocates nurses, plant engineers, students, and chemists. Most arrive on a start date.'),
  P('Two hospital systems run the East Side campus and the downtown hospitals. They bring in nurses on contracts all year and residents each June. Physicians arrive with a closing date and a second car. We supply the paperwork a reimbursed move needs.'),
  P('The Toyota plant in Princeton builds SUVs and minivans a half hour north on US 41. It moves engineers and team leaders from Kentucky and Texas on program schedules. The plastics company downtown, the nutrition plant, and the aluminum mill in Newburgh relocate the same way. So do the chemical plants in Mount Vernon. The national moving company headquartered here moves its own people too.'),
  P('The university on Lincoln Avenue brings cars in each August. The state university on the West Side and the technical college do the same. A parent ships the car, and an adult signs at a campus lot. The casino on the river hires from every state and moves its managers on short notice.'),
  P('Fort Campbell sits two hours south on 24, and families on orders settle in Evansville and Newburgh. The orders cover one car, and the second comes with us. Ship Guy is a private broker with no connection to the post. The <a href="military-car-shipping.html">military</a> page covers the timing. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Fall Festival, the Air Show, the Frog Follies, the River, and the Tornadoes',
 prose(
  L('Evansville runs on a street festival in October, a river summer, and a river that rises every spring.'),
  P('The Fall Festival fills Franklin Street for the first full week of October. It is one of the largest street festivals in the country, and the West Side closes for it. A pickup west of Pigeon Creek that week moves to the Lloyd or to US 41. The parade on Saturday closes Franklin end to end.'),
  P('The air show over the river fills Riverside Drive and the downtown lots in late June. The hot rod show at the fairgrounds fills Boonville-New Harmony Road on a weekend in August. The ballpark on the north side and the arena downtown fill their lots on game nights. A handoff near any of them moves to the morning.'),
  P('The Ohio River rises every spring, and the 1937 flood put most of the city under water. The levee has held since. The river still closes Riverside Drive and the low roads in Newburgh in a wet March. A pickup on those streets moves to the Lloyd for a day.'),
  P('Tornadoes are the bigger worry. The November 2005 storm crossed the southeast side and Newburgh. The sirens sound a few times each spring. A pickup waits for the warning to lift. Ice is the winter problem, and the 2009 storm took the power out for a week. Snow is light, and the carriers rarely park. Summer heat and humidity move the loading hour to the morning.'),
 )+chips(["Downtown","Old Courthouse","Arena","Riverside","Haynie’s Corner","Historic District","West Side","Franklin Street","Howell","Lamasco","Jacobsville","Garvin Park","Diamond Avenue","North Side","First Avenue","Oak Hill","Darmstadt","McCutchanville","Airport","East Side","Green River Road","Burkhardt","Eastland","Lincoln Avenue","Washington Avenue","Newburgh","Chandler","Boonville","Mount Vernon","Henderson"])
 +NOTE('Serving Evansville, Newburgh, Henderson, and the whole tri-state, old street or new subdivision. Tell us the side of the Lloyd and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Evansville?',
 prose(
  L('Most cars leave the tri-state on an open trailer, and the lane prices assume one.'),
  P('A closed trailer keeps a car out of the salt, the gravel, and the weather. The hot rod crowd that fills the fairgrounds each August books one for the show cars. Families shipping a new SUV from the plant book one too.'),
  P('A daily driver or a work truck rides open and arrives in the same shape it left. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages compare the two.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A number, a meeting spot at the mall or the arena, and a car at the far end. Most moves fit inside a week.'),
  P('Once you accept the number, we place the car with a carrier already running 64 or 69. You get the lot and the window the same day. At pickup, the driver inspects the car with you and notes every mark on a Bill of Lading. You both sign it, and the same form settles the delivery.'),
 )+ULI([
  "Empty the car of anything that is not bolted in",
  "Leave about a quarter tank of fuel",
  "Take dated photos of every panel before the pickup",
  "Hand over one working key and list any mechanical issue",
  "Turn off any aftermarket alarm",
  "Downtown or on the old West Side, meet the truck at the arena lots or on the Lloyd",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Evansville Drivers Choose Ship Guy',
 prose(
  L('We catch the 64 carriers as they pass to the north. We plan around the Fall Festival, the river, and the tornado season.'),
  P('Ship Guy is an FMCSA-licensed broker backed by a $75,000 surety bond, and the federal register lists both. Our office is in the Old Courthouse downtown.'),
  P('The coordinator who prices the move stays with it until the car is signed for. Open, enclosed, and expedited transport are on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Evansville','201 NW 4th St Suite 425B','Evansville, IN 47708','+18129546362','(812) 954-6362','ET',
 '201+NW+4th+St+Suite+425B,+Evansville,+IN+47708','Visit Us','Find Ship Guy in Evansville',
 'Our office is in the Old Courthouse downtown, two blocks from the Lloyd Expressway and the Civic Center.',
 map_src=None))

FAQ=[
 ("How much does it cost to ship a car from Evansville to Louisville or Nashville?","Louisville runs one hundred seventy to two hundred seventy dollars for a sedan. That is about one hundred twenty miles on 64. Nashville runs one hundred ninety to three hundred, about one hundred fifty-five miles on 69 and 24. St. Louis and Indianapolis price about the same as Nashville. An SUV or pickup adds 10 to 25 percent. All four lanes run daily, so a pickup comes within a day or two."),
 ("Can the carrier come to my street downtown or on the West Side?","Usually not. Downtown is a one-way grid around the courthouse, and the West Side streets off Franklin are narrow. The driver meets you at the arena lots, on Riverside, or at the shopping center on the Lloyd. The East Side, the north side, and Newburgh usually allow the curb."),
 ("Do you ship cars for people relocating to the hospitals or the Toyota plant?","Yes, all year. The hospital systems bring in nurses, residents, and physicians every month. The plant in Princeton moves engineers and team leaders from Kentucky and Texas on program schedules. Many ship a second car behind the move. The handoff works at the East Side campus lots or a lot on US 41. We provide the paperwork a reimbursed move needs."),
 ("Does the Fall Festival affect my pickup?","On the West Side, yes. Franklin Street closes for the first full week of October. The parade closes it end to end on Saturday. We move a pickup west of Pigeon Creek that week to the Lloyd or to US 41. The rest of the tri-state runs normally."),
 ("Can you ship a car to or from Newburgh or Henderson?","Yes, and both price the same as Evansville. Newburgh rides the same carriers off the Lloyd, and Henderson rides them across the Twin Bridges. A lot in Newburgh or off 41 in Henderson works for a handoff. Send the full address for a new subdivision in either town."),
 ("Can you time delivery to a student move at the university?","Yes. The campus on Lincoln Avenue and the one on the West Side fill with cars each August. They empty in May. A parent usually books, and someone over eighteen meets the truck at a campus lot. The delivery window follows the move-in date, and it shifts if the date shifts."),
 ("What happens if a tornado warning or the river hits on my pickup day?","A tornado warning stops the loading until it lifts, and the sirens sound a few times each spring. The driver waits it out and finishes the same day in most cases. The river closes Riverside and the low roads in Newburgh in a wet March. A pickup on those streets moves to the Lloyd. An ice storm costs a day, and the call comes before it does."),
 ("Can you ship a car that does not run from Evansville?","Yes. We send a truck with a winch. The quote carries the extra loading time from the first number. The arena lots or the mall lot on Green River give the driver level pavement. Tell us whether the car rolls, steers, and brakes."),
 ("Will the new Ohio River bridge change my shipment?","Not until it opens, and not much after. Today the carriers cross into Kentucky on the Twin Bridges on US 41, which are free. The new 69 bridge will carry a toll, and the carriers will choose between the two. The price of a Kentucky lane may move a few dollars either way."),
 ("What do you need for an Evansville car shipping quote?","Both addresses, with the side of the Lloyd or the town here. Year, make, and model. Whether it runs under its own power. Open or enclosed. The week you have in mind. With those, the Evansville number comes back the same day."),
]
BODY.append(faq_section(FAQ,'Evansville FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Evansville?','Two minutes on the form above prices your lane. Send the side of the Lloyd and your dates, and a carrier already on 64 takes it.','+18129546362','(812) 954-6362','Get your free Evansville quote'))

build({
 'slug':'auto-transport-evansville-indiana',
 'title':'Car Shipping in Evansville, IN — Auto Transport | Ship Guy',
 'meta':'Car shipping in Evansville, IN on the Ohio River bend, between Interstate 64 and the Twin Bridges. Hospital and Toyota-plant relocations, downtown and West Side meeting spots, East Side and Newburgh curbside pickups, Fall Festival week, the river, and the tornado season. Local office in the Old Courthouse downtown. Free quote.',
 'h1':'Car Shipping in<br>Evansville, <span class="accent">Indiana</span>',
 'lede':'Open, enclosed, and expedited auto transport across the tri-state, planned around 64, 69, the Lloyd, the Fall Festival, and the river.',
 'tel':'+18129546362','disp':'(812) 954-6362','brand':'Evansville','keyword':'car shipping in evansville',
 'localterms':['evansville','interstate 69','interstate 64','lloyd expressway','state road 62','66','us 41','twin bridges','henderson','highway 57','green river road','burkhardt','first avenue','diamond avenue','morgan avenue','washington avenue','franklin street','riverside drive','oak hill','boonville-new harmony','red bank','new bridge','downtown','courthouse','old courthouse','civic center','arena','main street','casino','haynie’s corner','historic district','west side','pigeon creek','german','howell','lamasco','jacobsville','garvin park','east side','mall','hospital campus','north side','darmstadt','mccutchanville','airport','newburgh','warrick','boonville','chandler','mount vernon','tri-state','kentucky','illinois','hospitals','nurses','residents','toyota','princeton','plastics','nutrition plant','aluminum mill','chemical plants','moving company','university','lincoln avenue','state university','technical college','fort campbell','orders','fall festival','parade','air show','hot rod','fairgrounds','ballpark','1937 flood','levee','tornado','2005','ice','2009','humidity','louisville','nashville','st. louis','indianapolis','cincinnati','chicago','memphis','atlanta','dallas','orlando'],
}, BODY, FAQ)
