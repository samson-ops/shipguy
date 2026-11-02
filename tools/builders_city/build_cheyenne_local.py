import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("3–6 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Cheyenne, Wyoming','Car shipping where 80 meets 25, an hour above Denver and a mile above the sea',
 ['Car shipping in Cheyenne rides Interstate 80 and Interstate 25, which cross on the west edge of town. Ship Guy is a licensed auto transport broker with an office on East 19th Street.',
  'We book vetted carriers across Cheyenne and Laramie County, from the Avenues to the base and the Ranchettes. The carriers own the trucks. Ship Guy holds the license and the bond.',
  'Interstate 80 runs along the south side of the city between Nebraska and the Summit toward Laramie. Interstate 25 runs the west side from Denver and Fort Collins north to Casper. Interstate 180 spurs into downtown. Lincolnway, Dell Range Boulevard, and Pershing carry the rest.',
  'This page covers 80, 25, the Summit, the wind closures, Lincolnway, downtown, the Avenues, and the north subdivisions. It also covers the base, the Capitol, the data centers, the railroad, Frontier Days, and the blizzards.'],
 'Cheyenne at a glance',
 ['Most pickups happen within 3 to 6 days. Wyoming is a pass-through market, and the 80 carriers add a Cheyenne stop when the load lines up. The Denver pool an hour south helps more than anywhere else in the state.',
  'Fort Collins and Denver are a day on the truck. Colorado Springs takes a day. Salt Lake City and Albuquerque take two. Omaha and Kansas City take two to three, and Chicago and Phoenix take three to four.'],
 'Tell us the neighborhood and whether the street is paved. The Avenues, downtown, the base housing, and the Ranchettes meet the truck at a lot or the gate. The north subdivisions, the east side, South Cheyenne, and Burns usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 80, Interstate 25, Interstate 180, the Summit, Lincolnway, Dell Range, Pershing, College Drive, and the Wind',
 prose(
  L('Cheyenne sits on the high plains where the two big roads cross. A carrier reaches every block from an exit, when the state lets it move.'),
  P('Interstate 80 is the New York-to-San Francisco road. It comes in from Nebraska past Pine Bluffs and runs the south side of the city. Then it climbs west to the Summit toward Laramie. The Summit at eight thousand six hundred feet closes dozens of times a winter. A carrier waits in Cheyenne until it opens. Interstate 25 is the Denver-to-Billings road. It comes up from Fort Collins along the west side and leaves north for Chugwater and Casper. The stretch to Wellington closes in blowing snow.'),
  P('The wind is the road problem the rest of the country does not have. The state closes 80 and 25 to light, high-profile vehicles when gusts pass sixty. A loaded car hauler counts. A closure usually lasts a day. Interstate 180 spurs from 80 into downtown with traffic lights on it. Lincolnway is US 30, the main street through downtown and east to the airport road. Dell Range Boulevard is the commercial strip on the north side. Pershing crosses the middle, and College Drive runs the south side past the college and the distribution centers.'),
  P('The carriers come off 80 at College Drive or 25 at Missile Drive. The mall lots on Dell Range are the usual meeting spot. The big-box lots on Dell Range and the college lots on a weekend work too. So do the depot lots outside the rodeo. The airport lots work for a fly-and-ship.'),
  P('Our office is on East 19th Street, a mile east of downtown and the Capitol.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the Capitol, the Avenues, South Cheyenne, the North Side, the East Side, the West and the Base, the Ranchettes, and the County',
 prose(
  L('Cheyenne is a railroad grid under a gold dome with new subdivisions spreading north. The truck reaches most of it.'),
  P('Downtown runs along Lincolnway and Capitol Avenue from the depot to the Capitol, brick blocks with angled parking. The driver meets you at the depot plaza lots or on Lincolnway. The Avenues east of the Capitol are the oldest neighborhood in the city, tree-lined streets of Victorian houses. The handoff moves to Pershing or the Capitol lots. South Cheyenne below the viaduct is older grids on plain streets, and the curb usually works.'),
  P('The north side from Pershing up Dell Range is where the city grew. Saddle Ridge, the Pointe, and the subdivisions off Yellowstone Road are wide and new. The driver reaches the house. The east side along Converse and out to the airport is the same. The streets outrun the carrier maps, so send the full address.'),
  P('The base on the west edge is gated. The housing beyond the gate is off limits to a carrier. The handoff happens at the gate or at a lot on Dell Range. The Ranchettes north of the city are horse lots on county roads, gravel and washboard. The truck meets you at the pavement.'),
  P('Burns and Pine Bluffs out 80 and Chugwater up 25 ship with the same trucks. They price the same as Cheyenne. Laramie over the Summit adds an hour and a closure risk. Fort Collins and Wellington in Colorado are forty minutes down 25 and ride the Denver pool. All of them meet the truck in town.'),
 )))

ROUTES=[("Fort Collins, CO","I-25 · ~45 mi","1 day","$150–$240"),("Denver, CO","I-25 · ~100 mi","1 day","$170–$280"),
 ("Colorado Springs, CO","I-25 · ~170 mi","1 day","$220–$340"),("Salt Lake City, UT","I-80 · ~440 mi","2 days","$400–$570"),
 ("Omaha, NE","I-80 · ~500 mi","2–3 days","$430–$620"),("Albuquerque, NM","I-25 · ~550 mi","2 days","$430–$620"),
 ("Kansas City, MO","I-80/I-29 · ~640 mi","3 days","$470–$680"),("Dallas, TX","I-25/US-287 · ~900 mi","3–4 days","$650–$900"),
 ("Chicago, IL","I-80 · ~970 mi","3 days","$680–$950"),("Phoenix, AZ","I-25/I-40 · ~1,000 mi","4 days","$700–$1,000")]
BODY.append(rate_table('Lanes &amp; Costs','Cheyenne Car Shipping Lanes and Estimated Costs',
 'The lanes southeast Wyoming cars run most, with estimated open-trailer ranges. Your own route gets a number on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Cheyenne, running sedan, open trailer. Add about 10 to 25 percent for an SUV or a pickup, and more for enclosed. The week of dates you give, the Summit, and the wind set the real quote.',
 prose(
  P('Cheyenne prices like a Denver suburb on the short lanes and a Wyoming town on the long ones. The Colorado lanes ride 25 south and fill every day with the Denver pool. The Salt Lake lane rides 80 over the Summit and across the whole state. The Omaha and Chicago lanes ride 80 east across Nebraska. The Arizona lane fills each October with the base retirees heading south.'),
  P('A July report date at the base or Frontier Days the same month lands in the busiest weeks. The <a href="car-shipping-cost.html">cost guide</a> explains what size, condition, and the date range do to the number.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Missile Wing, the Capitol, the Railroad, the Data Centers, the Hospital, the College, and the Retirees',
 prose(
  L('Cheyenne relocates airmen, state employees, railroaders, and technicians. The base moves more households than the rest of the city combined.'),
  P('The missile wing rotates airmen and officers on orders all year, with a summer peak. Housing is behind the gate, so the handoff happens outside it or on Dell Range. The government moves one vehicle on orders, and the family sends the second one with us. Ship Guy is a private broker and has nothing to do with the Air Force. The <a href="military-car-shipping.html">military</a> page explains how orders change the timing.'),
  P('State government fills the Capitol and the blocks around it. The agencies move staff in on start dates all year, and the legislature brings a crowd each winter. A new governor brings an appointee class every fourth January. The railroad keeps a crew base and the steam shop downtown and moves railroaders on bid dates. The data centers and the supercomputer in the business park move technicians on project dates. If the state or an employer is paying, the receipts for the package come from us.'),
  P('The hospital on East 23rd hires traveling nurses year round and brings residents each June. The distribution centers on the south side move managers on opening schedules. The college takes student cars in late August and sends them home in May. Mom or Dad books, and an adult signs at a lot. The university over the Summit in Laramie does the same. Its cars meet the truck in Cheyenne when the pass is closed.'),
  P('Retirees from the base stay for the taxes and leave for Arizona each October. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the paperwork for crossing a state line. Families priced out of Fort Collins buy in Cheyenne and ship one car up 25.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Frontier Days, the Session, the PCS Season, the Wind, the Summit, the Blizzards, the Hail, and the Altitude',
 prose(
  L('Cheyenne runs on a rodeo calendar and a base calendar. The weather problem is wind in every season and the Summit in winter.'),
  P('Frontier Days fills the city for ten days ending the last Sunday of July. Two hundred thousand people come, and the parades close Capitol Avenue four mornings. Every hotel within a hundred miles is full. A handoff anywhere in the city moves to the week before or the week after. The PCS season at the base runs June through August and fills the carriers with second cars. A July pickup is a three-week-ahead booking. The legislature fills the Capitol district each winter.'),
  P('The wind blows harder here than in any other city its size. The state closes 80 and 25 to high-profile vehicles when the gusts pass sixty. A loaded trailer waits. A closure usually lasts a day. The Summit on 80 closes dozens of times a winter for snow and ice. The Salt Lake car waits in Cheyenne. The stretch of 25 to Wellington closes in blowing snow, and the Denver car waits too. You hear it from us before the driver does.'),
  P('Winter brings sixty inches of snow and nights at twenty below. The March 2021 storm dropped thirty inches and shut the city for three days. A car from the south gets winter oil and a block heater before its first night here. An electric car should land with half a charge, since the cold and the altitude take a share. The truck meets you in a plowed lot, not a drifted street.'),
  P('Summer brings the hail. Cheyenne sits in hail alley, and a July storm dents a car in a parking lot in minutes. The August 1985 storm put the city under hail and water in an hour. An enclosed trailer avoids it, and an open one loads in the morning. The altitude takes a little power from every engine, and a carrier climbs the Summit slowly.'),
 )+chips(["Downtown","Lincolnway","Depot Plaza","Capitol","The Avenues","Rainsford","South Cheyenne","North Side","Dell Range","Saddle Ridge","The Pointe","Yellowstone Road","East Side","Converse","Sun Valley","Buffalo Ridge","Airport","West Edge","F.E. Warren","Missile Drive","Fox Farm","Ranchettes","Burns","Pine Bluffs","Chugwater","Laramie","Wellington","Fort Collins"])
 +NOTE('Serving Cheyenne and all of Laramie County, Avenues block or Ranchettes county road. Tell us the neighborhood and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Cheyenne?',
 prose(
  L('Almost every car in Cheyenne leaves on an open trailer, and the table above is priced that way.'),
  P('An enclosed trailer keeps off the hail, the gravel of the Summit, and the sand on 80. The collectors in the Avenues book one. So do the officers bringing a new car to the base. A car crossing the Summit in January often goes enclosed as well.'),
  P('A commuter car or a student car belongs on an open trailer. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages show where the line falls.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a meeting spot on Dell Range, and a signature at delivery. Your dates pick the truck.'),
  P('Say yes, and we line up a carrier on 80 or from the Denver pool that week. The moment one commits, the lot and the window are set. The driver goes around the car with you and notes each mark on the Bill of Lading. Your initials go on it, and delivery is held to it.'),
 )+ULI([
  "Clear the car of your belongings, trunk and glovebox too",
  "Gas gauge around a quarter",
  "Take your own photos of each side and the mileage that morning",
  "A key the driver can use, plus a heads-up on any quirks",
  "Add-on alarm switched off",
  "In the Avenues, downtown, at the base, or in the Ranchettes, plan on a lot or the gate",
 ])+prose(P('Every step is on the <a href="how-it-works.html">how it works</a> page, and the whole checklist is on the <a href="car-shipping-preparation.html">preparation</a> page.'))))

BODY.append(sec('Why Ship Guy','Why Cheyenne Drivers Choose Ship Guy',
 prose(
  L('We know which carriers cross on 80 each week and when the Summit or the wind shuts it.'),
  P('Anyone can find our FMCSA license and our $75,000 bond on the federal register. The office is on East 19th Street.'),
  P('A single coordinator carries the move from the quote to the delivery photo. Open, enclosed, and expedited are compared on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Cheyenne','1600 E 19th St #447','Cheyenne, WY 82001','+13048496570','(304) 849-6570','MT',
 '1600+E+19th+St+%23447,+Cheyenne,+WY+82001','Visit Us','Find Ship Guy in Cheyenne',
 'Our office is on East 19th Street, a mile east of downtown and the Capitol.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3708.854009698389!2d-104.79895839999999!3d41.142357499999996!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x876f3bc7cc12fdf3%3A0x37e16f34f87bc5fc!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793629038945!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Cheyenne to Denver or Salt Lake City?","Denver runs one hundred seventy to two hundred eighty dollars for a sedan. That is about a hundred miles down 25. Salt Lake City runs four hundred to five hundred seventy, about four hundred forty miles out 80. Fort Collins is forty-five miles and the lowest lane on the table. Add about 10 to 25 percent for an SUV or a pickup."),
 ("Why does a Cheyenne pickup take 3 to 6 days?","Because Wyoming is a pass-through market. The carriers cross on 80 between Salt Lake City and Nebraska. One adds a Cheyenne stop when the load lines up. The Denver pool an hour south shortens the wait more than anywhere else in the state. A week of dates puts the car on the next truck through."),
 ("Do you handle PCS moves for F.E. Warren?","Yes, with the peak in summer. Airmen and officers rotate through the missile wing on orders all year. Housing sits behind the gate, so the truck meets you outside it or on Dell Range. The government moves one vehicle, and the family sends the second one with us. Ship Guy is a private broker and has nothing to do with the Air Force."),
 ("What happens if the wind closes 80 or 25 on my pickup day?","The truck waits a day. The state closes both roads to high-profile vehicles when the gusts pass sixty. A loaded car hauler counts. The carrier sits in Cheyenne or Fort Collins until the closure lifts. We tell you before the driver does. A closure rarely lasts more than a day."),
 ("Can the carrier come to my street in the Avenues or the Ranchettes?","Usually not. The Avenues are tree-lined streets of old houses with no room to turn a trailer. The Ranchettes are gravel county roads. The driver meets you on Pershing, at the Capitol lots, or at the pavement. The north subdivisions, the east side, and South Cheyenne usually allow the curb."),
 ("Does Frontier Days affect my pickup?","Yes, for ten days in late July. Two hundred thousand people come and the parades close Capitol Avenue. Every hotel for a hundred miles is full. A handoff anywhere in the city moves to the week before or the week after. The rest of the year has room."),
 ("Can you ship a car to or from Laramie, Fort Collins, or Casper?","Yes. Fort Collins is forty minutes down 25 and rides the Denver pool, and the curb works. Laramie is an hour over the Summit. Its cars meet the truck in Cheyenne when the pass is closed. Casper is three hours up 25 and prices a shade higher. Send the full address for a county road."),
 ("Can you deliver on a Laramie County Community College move-in date?","Yes. The college takes cars in late August and sends them home in May. Mom or Dad books, and an adult signs at a lot. The college lots on College Drive are the meeting point. Give us a range around the date, because the first snow can come the same week."),
 ("Can you ship a car that does not run from Cheyenne?","Yes. A winch carrier and the loading time are built into the number from the start. A non-runner narrows which trucks can stop on 80, so give us room on the dates. The mall lots on Dell Range are level. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Cheyenne car shipping quote?","Both ends of the move, with the neighborhood and whether the road is paved. Year, make, and model. Running or not. Open or enclosed. The widest week of dates you can live with. Those five, and the Cheyenne number is back before the day ends."),
]
BODY.append(faq_section(FAQ,'Cheyenne FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Cheyenne?','Two minutes on the form above, and a Cheyenne number comes back. Give us the neighborhood and a week of dates, and we catch the next carrier through.','+13048496570','(304) 849-6570','Get your free Cheyenne quote'))

build({
 'slug':'auto-transport-cheyenne-wyoming',
 'title':'Car Shipping in Cheyenne, WY — Auto Transport | Ship Guy',
 'meta':'Car shipping in Cheyenne, WY, where Interstate 80 meets Interstate 25 an hour above Denver. Honest 3 to 6 day windows, F.E. Warren PCS moves outside the gate, the wind closures and the Summit, lot handoffs for the Avenues and downtown, curbside pickups in the north subdivisions, the east side, and South Cheyenne, Frontier Days, and the hail. Local office on East 19th Street. Free quote.',
 'h1':'Car Shipping in<br>Cheyenne, <span class="accent">Wyoming</span>',
 'lede':'Open, enclosed, and expedited auto transport across Cheyenne and Laramie County, planned around 80, 25, the Summit, the wind, the base calendar, Frontier Days, and the honest windows of a pass-through state.',
 'tel':'+13048496570','disp':'(304) 849-6570','brand':'Cheyenne','keyword':'car shipping in cheyenne',
 'localterms':['cheyenne','interstate 80','interstate 25','denver','east 19th street','laramie county','avenues','base','ranchettes','nebraska','summit','laramie','fort collins','casper','interstate 180','lincolnway','dell range','pershing','wind closures','downtown','north subdivisions','capitol','data centers','railroad','frontier days','blizzards','colorado springs','salt lake city','albuquerque','omaha','kansas city','chicago','phoenix','paved','gate','pavement','east side','south cheyenne','burns','pine bluffs','eight thousand six hundred feet','chugwater','wellington','high-profile','sixty','traffic lights','us 30','airport road','college drive','distribution centers','missile drive','mall','big-box','depot','rodeo','fly-and-ship','gold dome','capitol avenue','angled parking','victorian','viaduct','saddle ridge','pointe','yellowstone road','converse','horse lots','county roads','gravel','washboard','retirees','arizona','report date','missile wing','orders','summer peak','session','appointee','crew base','steam shop','bid dates','supercomputer','business park','hospital','east 23rd','traveling nurses','residents','college','late august','university','taxes','parades','two hundred thousand','pcs season','sixty inches','twenty below','march 2021','thirty inches','block heater','electric car','altitude','hail','august 1985','sand','bill of lading','fmcsa','rainsford','sun valley','buffalo ridge','west edge','fox farm','winch'],
}, BODY, FAQ)
