import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Overland Park, Kansas','Car shipping in the largest city in Johnson County, where the 435 loop crosses US 69 south of the state line',
 ['Car shipping in Overland Park runs off the 435 loop and the 69 freeway, which cross mid-city. Ship Guy is a licensed auto transport broker with an office in Corporate Woods off 110th Street.',
  'We book vetted carriers across Johnson County, from Leawood and Prairie Village down to the Blue Valley subdivisions. The carriers own the trucks.',
  'Interstate 435 is the metro loop, and it runs east and west across the city. Interstate 35 clips the northwest corner. US 69 is the north-south freeway, and Metcalf Avenue is the strip beside it. College Boulevard, 95th, 119th, and 135th Streets carry the rest.',
  'This page covers the loop, Metcalf, downtown, the north side, the corporate corridor, and Blue Valley. It also covers the hospitals, the engineering firms, the soccer complex, the ice storms, and the lanes.'],
 'Overland Park at a glance',
 ['Most pickups happen within 1 to 3 days. The metro shares one carrier pool across the state line. The 435 loop brings the trucks past the door.',
  'Topeka and Columbia are ninety minutes. Wichita, Omaha, Des Moines, and St. Louis are a same-day haul. Tulsa, Oklahoma City, and Chicago are a day out. Dallas and Denver run one to two days, and either coast runs three to five.'],
 'Tell us the side of 435. Downtown and the north side grids need a meeting spot. The Blue Valley subdivisions south of 119th usually allow the curb, gate code permitting.'))

BODY.append(sec('The Roads','Interstate 435, US 69, Metcalf Avenue, College Boulevard, and 135th Street',
 prose(
  L('Overland Park sits inside the metro loop. Every carrier working Kansas City crosses it on the way around.'),
  P('Interstate 435 crosses the city east and west between the state line and 35. The exits at Metcalf, Nall, Antioch, Quivira, and 69 cover six miles. Interstate 35 runs along the northwest edge past Lenexa toward Olathe. The carriers between Dallas and Des Moines use it. Interstate 70 and the Turnpike sit twenty minutes north.'),
  P('US 69 is the freeway through the middle of the city, from 435 south to the county line. Metcalf Avenue runs beside it as the old strip, from downtown to Blue Valley. Antioch, Nall, Lamar, Quivira, Switzer, and Pflumm run north and south through the grid. State Line Road is the east edge.'),
  P('College Boulevard is the office corridor from the state line to the community college. 95th Street carries the mall. 119th and 135th Streets are the retail strips through Blue Valley. 151st, 159th, and 179th reach the newest subdivisions at the south end. Shawnee Mission Parkway and 75th Street cross the north side.'),
  P('The carriers come off 435 at Metcalf and 69, and off 69 at 119th and 135th. The mall on 95th, the convention center on College, and the soccer complex have the usual meeting lots. No road in Johnson County charges a toll. The Turnpike starts at Kansas City on the way to Topeka.'),
  P('Our office is in Corporate Woods off 110th Street, a minute from the 435 and 69 interchange.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the North Side, the Corporate Corridor, Blue Valley, and the Cities Next Door',
 prose(
  L('Overland Park grew south one mile at a time. The streets get wider the farther south you go.'),
  P('Downtown is the old grid around 80th and Santa Fe. It has the clock tower, the farmers market, and the shops. The streets are narrow and the market closes them on Saturdays. The driver meets you at the lots off Metcalf or at the shopping center on 75th. The north side grids between 75th and 95th are postwar blocks with mature trees. The curb works on most of them, and a lot on Metcalf works for the rest.'),
  P('The corporate corridor along College Boulevard and 110th is office parks, hotels, and the convention center. There is room everywhere. The subdivisions between 95th and 119th have wide streets, and the truck reaches the curb. The mall at 95th and Quivira fills on weekends.'),
  P('Blue Valley south of 119th is the growth side, with subdivisions out to 179th and beyond. The streets are wide, and the curb works. Some of the newest developments are gated, and the handoff waits at the gate. Carriers reach these streets faster than the maps update them. Send the full address and the gate code.'),
  P('Leawood east of the city has its own gated streets and the shops on 135th. Prairie Village, Mission, and Merriam to the north are older grids with narrow streets. Lenexa and Shawnee to the west have the warehouses and wide roads. Olathe to the southwest has its own page. All of them price the same as Overland Park, and so does the Missouri side across State Line.'),
 )))

ROUTES=[("Topeka, KS","K-10/I-70 · ~65 mi","Same day","$140–$230"),("Columbia, MO","I-70 · ~130 mi","Same day","$180–$290"),
 ("Wichita, KS","I-35 · ~185 mi","Same day","$220–$340"),("Omaha, NE","I-29 · ~190 mi","Same day","$230–$350"),
 ("St. Louis, MO","I-70 · ~250 mi","1 day","$250–$370"),("Tulsa, OK","US-69/I-44 · ~250 mi","1 day","$250–$380"),
 ("Chicago, IL","I-35/I-80 · ~510 mi","1–2 days","$420–$600"),("Dallas, TX","I-35 · ~530 mi","1–2 days","$430–$620"),
 ("Denver, CO","I-70 · ~600 mi","1–2 days","$450–$650"),("Phoenix, AZ","I-35/I-40 · ~1,240 mi","3–4 days","$880–$1,200")]
BODY.append(rate_table('Lanes &amp; Costs','Overland Park Car Shipping Lanes and Estimated Costs',
 'The lanes Johnson County cars take most, with estimated open-trailer ranges. Your exact route prices on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Overland Park for a sedan that runs, on an open trailer. Add 10 to 25 percent for an SUV or a pickup, and more for enclosed. Turnpike tolls are included when a carrier uses it. Fuel, the week, and the carriers free on your dates settle the final price.',
 prose(
  P('Overland Park prices with Kansas City on every lane. The metro shares one carrier pool across the state line. The Dallas and Denver lanes run full in both directions and price the lowest per mile. The Chicago lane rides 35 and 80 and runs lighter.'),
  P('Phoenix and Florida follow the snowbird calendar, higher in the fall and lower in the spring. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Hospitals, the Engineering Firms, the Corporate Corridor, the Schools, and the Transplants',
 prose(
  L('Overland Park relocates engineers, physicians, corporate staff, and families chasing the schools. Most arrive on a closing date.'),
  P('Three hospitals sit inside the city, on Quivira, on Nall, and in Blue Valley. They bring in nurses on contracts all year and physicians with a closing date and a second car. The children’s hospital campus and the clinics do the same. We supply the paperwork a reimbursed move needs.'),
  P('The engineering firm on Lamar and the companies along College Boulevard move engineers and analysts in every month. The old wireless campus at 119th and Nall is filling with new tenants. They relocate staff the same way. The salt company and the data-center firm move people on their own calendars.'),
  P('The Blue Valley schools draw families from both coasts, and the closing date drives the move. One car ships while the other is driven. The community college on Quivira brings cars in each August, and a parent ships the car. An adult signs at a campus lot. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
  P('Fort Leavenworth sits forty minutes north. Officers at the staff college settle in Overland Park and Leawood each summer. Orders pay for one car, and the family’s second car rides with us. Ship Guy is a private broker and has no connection to the post. The <a href="military-car-shipping.html">military</a> page explains the timing.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Fourth at Corporate Woods, the Soccer Complex, Chiefs Sundays, the Ice, and the Sirens',
 prose(
  L('Overland Park runs on a fireworks night, a soccer complex that fills every weekend, and an icy winter.'),
  P('The Fourth of July fireworks at Corporate Woods fill 110th and College and every lot around them. A pickup in the corridor that evening moves to the morning. The jazz festival in June and the fall festival downtown in September close streets for a weekend. The farmers market closes downtown every Saturday morning from spring through fall.'),
  P('The soccer complex at 135th and Switzer hosts tournaments most weekends from March through November. The lots fill by eight, and 135th backs up. A handoff near it moves to a weekday. Chiefs Sundays jam 435 eastbound toward the stadium, and the carriers plan around the kickoff.'),
  P('Ice is the winter problem. The 2002 ice storm took down half the trees in the metro and the power for a week. The carriers parked on 435 for two days. Snow adds up to twenty inches in a normal year. The 2011 blizzard shut 35 for a day. The carriers sit at the truck stops by the Turnpike while the plows work. A pickup that week can lose a day.'),
  P('The sirens sound a few times each spring. The 2019 tornado crossed the county line at Linwood and Bonner Springs. The 2003 storms hit the Kansas side of the metro. A pickup waits for the warning to lift. Indian Creek floods the trail and the low roads off 103rd in a big summer storm. Summer heat passes one hundred degrees in July, and the loading hour moves to the morning.'),
 )+chips(["Downtown","Santa Fe","Clock Tower","Farmers Market","North Side","75th Street","Shawnee Mission Parkway","Metcalf","Antioch","Nall","Lamar","Quivira","95th Street","Oak Park","College Boulevard","Corporate Woods","Convention Center","Indian Creek","119th Street","Aspiria","Blue Valley","135th Street","Prairiefire","Soccer Complex","Deanna Rose","151st","159th","179th","Arboretum","Leawood","Prairie Village","Mission","Merriam","Lenexa","Shawnee","State Line"])
 +NOTE('Serving Overland Park, Leawood, Lenexa, and all of Johnson County, old grid or gated subdivision. Tell us the side of 435 and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Overland Park?',
 prose(
  L('Open trailers carry most of the cars that leave Johnson County. The lane table is priced for one.'),
  P('An enclosed trailer keeps the salt, the gravel, and the hail off. The garages in Leawood and Blue Valley book one for the collector cars. Executives relocating a new car to the corridor book one too.'),
  P('The family SUV and the commuter car go open and arrive exactly as they left. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages lay the two side by side.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a meeting spot at the mall or in the corridor, and a signed sheet at delivery. The closing date sets the week.'),
  P('Once you approve the price, we assign a carrier that is already circling the loop. The meeting lot and the pickup window follow within hours. You and the driver go over the car together at pickup. Every existing mark goes on the Bill of Lading. Two signatures close it, and the same form is checked at delivery.'),
 )+ULI([
  "Take everything personal out of the cabin and the trunk",
  "Leave the fuel near a quarter tank",
  "Photograph each side of the car and the odometer before the handoff",
  "Give the driver one working key and name any mechanical fault",
  "Disarm any aftermarket alarm",
  "In a gated subdivision, meet the truck at the gate or send the code ahead",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Overland Park Drivers Choose Ship Guy',
 prose(
  L('We load the carriers already circling the metro on 435. We plan around the closing date, the soccer weekends, and the ice.'),
  P('Ship Guy is an active FMCSA broker with a $75,000 surety bond on file. The federal register lists both. Our office is in Corporate Woods off 110th Street.'),
  P('The coordinator who prices the move is the one who answers the phone until the car is delivered. Open, enclosed, and expedited transport are on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Overland Park','5440 W 110th St Ste 458A','Overland Park, KS 66211','+19135657461','(913) 565-7461','CT',
 '5440+W+110th+St+Ste+458A,+Overland+Park,+KS+66211','Visit Us','Find Ship Guy in Overland Park',
 'Our office is in Corporate Woods off 110th Street, a minute from the 435 and 69 interchange.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4772.791270393336!2d-94.6468972!3d38.9301761!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x87c0eb0a8e0d0bb7%3A0xb7ef62033405a12!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793024860581!5m2!1sen!2sus'))

FAQ=[
 ("Can you time delivery to my closing date in Overland Park?","Yes. Closings drive most Overland Park bookings. Families come from both coasts for the schools and buy in Blue Valley or Leawood. The delivery window is pinned to the closing date, and when the closing slides, so does the window. One call with the new date is all it takes."),
 ("How much does it cost to ship a car from Overland Park to Dallas or Denver?","Dallas runs four hundred thirty to six hundred twenty dollars for a sedan. That is about five hundred thirty miles down 35. Denver runs four hundred fifty to six hundred fifty, about six hundred miles out 70. Both lanes run full in both directions, which keeps them steady. An SUV or pickup adds 10 to 25 percent."),
 ("Can the carrier come to my street in a gated subdivision?","Up to the gate, yes. Many of the newest streets south of 135th sit behind a gate. A seventy-five-foot trailer cannot turn inside. The driver meets you at the gate or at the clubhouse lot. Send the gate code ahead if the guard needs it. The older subdivisions between 95th and 135th allow the curb."),
 ("Do you ship cars for people relocating to the hospitals or the corporate corridor?","Yes, all year. The three hospitals bring in nurses, residents, and physicians every month. The engineering firm, the companies on College Boulevard, and the old wireless campus move staff from every state. Many ship a second car behind the move. The handoff works at the convention center lots or a lot off 435. We provide the paperwork a reimbursed move needs."),
 ("Does the soccer complex or a Chiefs game affect my pickup?","Near 135th and Switzer on a tournament weekend, yes. The lots fill by eight and 135th backs up. We move a handoff there to a weekday. Chiefs Sundays jam 435 eastbound toward the stadium, and the carriers plan the loop around kickoff. The rest of the county runs normally."),
 ("Can you ship a car to or from Leawood, Lenexa, or Prairie Village?","Yes, and all three price the same as Overland Park. Leawood rides the same carriers off 435 at State Line and 135th. Lenexa rides them off 35 and 435, and Prairie Village rides them off Shawnee Mission Parkway. A lot on the main road works for a handoff. Send the full address and any gate code."),
 ("What happens if an ice storm or a tornado warning hits on my pickup day?","Ice, more than snow, is what parks the trucks here. When it glazes 435, the carriers hold by the Turnpike until the salt trucks have been through. Expect a day of delay at most, with a call from us ahead of it. Under a tornado warning the loading pauses until the all-clear. The sirens are a spring ritual, and the driver usually finishes the same afternoon."),
 ("Can you ship a car that does not run from Overland Park?","Yes. We send a carrier with a winch. The loading time is in the quote from the first number. The mall lot on 95th or the convention center lots give the driver level pavement. Tell us whether the car rolls, steers, and brakes."),
 ("Do you ship cars for officers at Fort Leavenworth who live in Overland Park?","Yes, every summer. The staff college moves its officers together each June and July. Many families settle in Overland Park and Leawood. The orders cover one car, and we move the second. Ship Guy is a private broker with no connection to the post. Send the report date, and we build the window around it."),
 ("What do you need for an Overland Park car shipping quote?","Both addresses, with the side of 435 and any gate code here. Year, make, and model. Whether it drives. Open or enclosed. The week around the closing. With those, the Overland Park number comes back the same day."),
]
BODY.append(faq_section(FAQ,'Overland Park FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Overland Park?','Two minutes on the form above prices your lane. Send the side of 435 and your dates, and a carrier already on the loop takes it.','+19135657461','(913) 565-7461','Get your free Overland Park quote'))

build({
 'slug':'auto-transport-overland-park-kansas',
 'title':'Car Shipping in Overland Park, KS — Auto Transport | Ship Guy',
 'meta':'Car shipping in Overland Park, KS, where the 435 loop crosses US 69 in Johnson County. Closing-date deliveries for Blue Valley families, hospital and corporate-corridor relocations, gated-subdivision handoffs, Leawood and Lenexa, the soccer complex, Chiefs Sundays, and the ice storms. Local office in Corporate Woods. Free quote.',
 'h1':'Car Shipping in<br>Overland Park, <span class="accent">Kansas</span>',
 'lede':'Open, enclosed, and expedited auto transport across Johnson County, planned around 435, 69, the closing date, the gates, and the ice.',
 'tel':'+19135657461','disp':'(913) 565-7461','brand':'Overland Park','keyword':'car shipping in overland park',
 'localterms':['overland park','johnson county','interstate 435','loop','interstate 35','us 69','metcalf','antioch','nall','lamar','quivira','switzer','pflumm','state line','college boulevard','95th','119th','135th','151st','159th','179th','shawnee mission parkway','75th','turnpike','downtown','santa fe','clock tower','farmers market','north side','corporate corridor','corporate woods','convention center','mall','blue valley','gated','gate code','leawood','prairie village','mission','merriam','lenexa','shawnee','olathe','missouri side','hospitals','nurses','physicians','children’s hospital','engineering firm','wireless campus','salt company','data-center','schools','community college','closing date','fort leavenworth','staff college','orders','fourth of july','fireworks','jazz festival','fall festival','soccer complex','tournaments','chiefs','stadium','ice storm','2002','snow','2011 blizzard','sirens','2019','linwood','2003','indian creek','heat','topeka','columbia','wichita','omaha','st. louis','tulsa','chicago','dallas','denver','phoenix','des moines','oklahoma city'],
}, BODY, FAQ)
