import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Bellevue, Washington','Car shipping on the east side of the lake, between the floating bridges and the campuses',
 ['Car shipping in Bellevue runs on Interstate 405 and the two floating bridges to Seattle. Ship Guy is a licensed auto transport broker with an office on 116th Avenue Northeast, east of 405.',
  'We line up vetted carriers across Bellevue and the Eastside, from Medina to Issaquah and Redmond. The carriers own the trucks. Ship Guy holds the license and the bond.',
  'Interstate 405 runs north and south through the middle of the city, from Renton to Kirkland and Bothell. Interstate 90 crosses the south side at Factoria and rides the free bridge to Mercer Island and Seattle. Highway 520 crosses the north side and rides the tolled bridge. Bellevue Way, 148th Avenue, and Coal Creek Parkway carry the rest.',
  'This page covers 405, the bridges, the toll, downtown, the Gold Coast, the hills, and the Eastside suburbs. It also covers the software campuses, the towers, the hospital, the snow days, and the lanes.'],
 'Bellevue at a glance',
 ['Most pickups happen within 1 to 3 days. The Interstate 5 carriers reach the Eastside on 405 every day. The 90 carriers cross the mountains to Spokane.',
  'Portland and Vancouver are same-day runs. Spokane and Boise need a day. Missoula, Sacramento, and Salt Lake City need two, and California and Denver need three.'],
 'Tell us the neighborhood and whether the street climbs. Downtown, Medina, Bridle Trails, and Somerset meet the truck at a lot. Lake Hills, Crossroads, Factoria, Newcastle, Redmond, and Issaquah usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 405, Interstate 90, Highway 520, the Floating Bridges, Bellevue Way, 148th, Coal Creek Parkway, and the Toll',
 prose(
  L('Bellevue sits between two floating bridges and under one freeway. A carrier reaches the whole Eastside from 405 without crossing the lake.'),
  P('Interstate 405 is the Eastside freeway. It runs from Renton and the Boeing plant north through downtown Bellevue to Kirkland, Bothell, and Lynnwood. The express toll lanes north of the city cost money, and the regular lanes jam both rush hours. The carriers coming up Interstate 5 from Portland leave it at Renton or Tukwila and ride 405 in. The Spokane carriers come over the pass on 90.'),
  P('Interstate 90 crosses the south side of the city at Eastgate and Factoria. It rides the floating bridge to Mercer Island and Seattle for free. Highway 520 crosses the north side past the Spring District and rides the newer floating bridge. That bridge charges a toll in both directions, and the toll is inside every quote. A loaded trailer uses 90 unless the delivery is on the 520 side. Both bridges close for a weekend now and then for work. The driver knows it before you do.'),
  P('Bellevue Way runs from downtown south to the 90 interchange. 148th Avenue runs the east side from the 90 campus to Overlake and the software campus in Redmond. Coal Creek Parkway climbs from Factoria to Newcastle. The carriers meet you at the South Bellevue park-and-ride, the Eastgate lots, or the Factoria lots. The Crossroads lots on 156th and the big-box lots in Overlake work too.'),
  P('Our office is on 116th Avenue Northeast, east of 405, a few blocks from the hospital.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, Old Bellevue, the Gold Coast, Bridle Trails, Lake Hills, Crossroads, Factoria, Somerset, Newcastle, and the Eastside',
 prose(
  L('Bellevue is glass towers downtown, gated lanes along the lake, and hills with switchbacks. The truck meets most of it at a lot.'),
  P('Downtown is towers, garages, and one-way loading zones. A seventy-five-foot trailer has nowhere to stop. The driver meets you at the South Bellevue park-and-ride or on 116th by the hospital. Old Bellevue along Main Street is lower and tighter, with the same answer. Wilburton and Northtowne east of 405 are older blocks on wider streets, and the curb usually works.'),
  P('Medina, Clyde Hill, Hunts Point, and Yarrow Point along the lake are the Gold Coast. The lanes are narrow and run behind gates and hedges. The truck does not fit, and the gate code does not help. The driver meets you on 84th or at the park-and-ride. Enatai and Beaux Arts to the south are the same. Bridle Trails is acre lots on gravel lanes with horse trails for shoulders. The handoff moves to 140th or 148th.'),
  P('Lake Hills and Crossroads east of downtown are the postwar grids, wide streets with room for a trailer. Robinswood and Woodridge are the same. Factoria and Eastgate along 90 are apartments and office parks with big lots. Somerset, Cougar Mountain, and Lakemont climb the hills above them on switchbacks a trailer cannot take. The driver meets you at the bottom, in Factoria or at the Eastgate lots.'),
  P('The Eastside beyond the city line ships with the same trucks. Redmond, Kirkland, Issaquah, and Sammamish price the same as Bellevue. So do Newcastle, Renton, Mercer Island, Bothell, and Woodinville. Mercer Island and the Kirkland waterfront are tight, and the rest usually allows the curb.'),
 )))

ROUTES=[("Portland, OR","I-405/I-5 · ~175 mi","Same day","$220–$340"),("Vancouver, WA","I-405/I-5 · ~165 mi","Same day","$210–$330"),
 ("Spokane, WA","I-90 · ~270 mi","1 day","$260–$390"),("Boise, ID","I-90/I-82/I-84 · ~490 mi","1 day","$430–$620"),
 ("Missoula, MT","I-90 · ~470 mi","1–2 days","$400–$570"),("Sacramento, CA","I-5 · ~750 mi","2 days","$560–$820"),
 ("San Francisco, CA","I-5 · ~810 mi","2 days","$600–$880"),("Salt Lake City, UT","I-90/I-84 · ~830 mi","2 days","$600–$880"),
 ("Los Angeles, CA","I-5 · ~1,135 mi","3 days","$800–$1,150"),("Phoenix, AZ","I-5/US-93 · ~1,420 mi","3–4 days","$900–$1,300")]
BODY.append(rate_table('Lanes &amp; Costs','Bellevue Car Shipping Lanes and Estimated Costs',
 'The lanes Eastside cars run most, with estimated open-trailer ranges. Price your own route on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Bellevue for a running sedan on an open trailer. An SUV or a pickup runs about 10 to 25 percent more, and enclosed more again. The 520 toll is inside the number when the route uses it. The week and the carriers free that week set the final figure.',
 prose(
  P('Bellevue prices with Seattle on every lane, because the same trucks serve both sides of the lake. The Portland lane rides 405 and 5 and fills every day. The Spokane lane rides 90 over the pass. The California lanes fill each fall with the Eastside’s transplants heading home, and the price follows. The Arizona lane fills with retirees in October.'),
  P('A September start date or a campus move-in lands in the busiest weeks of the year. What size, condition, and timing do to the number is in the <a href="car-shipping-cost.html">cost guide</a>.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Software Campuses, the Towers, the Wireless Carrier, the Hospital, the Base Families, and the Students',
 prose(
  L('Bellevue relocates more engineers per square mile than almost anywhere. The campuses and the towers move the most.'),
  P('The software company in Redmond relocates engineers from across the country on start dates all year. The online retailer is filling its new towers downtown the same way. The wireless carrier in Factoria, the truck maker on 106th, and the utility relocate staff on offer dates. The packages usually cover one car, and the second one rides a trailer with us. If an employer is reimbursing the move, we produce the paperwork it wants.'),
  P('The hospital on 116th hires traveling nurses year round and brings residents each June. The aerospace plant in Renton moves engineers on program dates. The game studios in Bellevue and Redmond hire on project cycles. The college on Landerholm Circle takes student cars each September. The university across the lake does the same a week later. A parent books by phone, and an adult meets the truck at a lot to sign.'),
  P('The joint base near Tacoma and the naval station in Everett send families to the Eastside on orders. Orders usually cover one vehicle. The second one ships with us. Ship Guy is a private broker with no connection to either base. How orders change the timing is explained on the <a href="military-car-shipping.html">military</a> page.'),
  P('Transplants arrive from California every month and ship the car behind the moving truck. Retirees leave for Arizona and Palm Springs in October and come back in April. The interstate paperwork is covered on the <a href="state-to-state-car-shipping.html">state-to-state</a> page.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Snowflake Lane, the Arts Fair, Move-In Week, the Bridge Closures, the Snow Days, the Windstorms, and the Smoke',
 prose(
  L('Bellevue runs on a tech calendar and a bridge calendar. The weather problem is the two days a year it snows on the hills.'),
  P('Snowflake Lane closes a lane of Bellevue Way every evening from late November through Christmas Eve. A downtown handoff in December moves to the morning. The arts fair fills downtown for a weekend in late July. The Strawberry Festival fills Crossroads for a weekend in June. Move-in at the college comes in late September, and the university across the lake follows a week later.'),
  P('The floating bridges close for a weekend a few times a year for maintenance and rail work. When 90 is closed, the trailers use 520 and the toll goes on the quote. When 520 is closed, they use 90. A handoff on the Seattle side of a closed bridge moves to the next week. The 405 express lanes and the Renton curve back up every weekday, and a morning pickup beats them.'),
  P('Rain falls from October to May and changes nothing. Snow falls two or three days a winter and changes everything on the hills. Somerset, Cougar Mountain, Lakemont, and Bridle Trails close to a trailer until the ice melts. The February 2019 storm dropped a foot and shut the Eastside for a week. A carrier waits in Renton or Tukwila until 405 clears. A snow-day pickup slides a day or two, and you hear it from us first.'),
  P('The windstorms come in November and December. The 2006 storm put the Eastside in the dark for a week. Firs came down on every hill road. The 520 bridge closes to traffic in high wind, and the driver crosses on 90. The smoke in September 2020 sat over the lake for ten days and shifted only the loading hour. The June 2021 heat reached one hundred eight degrees, and the carriers loaded at dawn.'),
 )+chips(["Downtown","Old Bellevue","Main Street","Spring District","Wilburton","Northtowne","Medina","Clyde Hill","Hunts Point","Yarrow Point","Enatai","Beaux Arts","Bridle Trails","Lake Hills","Crossroads","Robinswood","Woodridge","Factoria","Eastgate","Somerset","Cougar Mountain","Lakemont","Newport Hills","Newcastle","Mercer Island","Redmond","Overlake","Kirkland","Issaquah","Sammamish","Renton","Bothell","Woodinville"])
 +NOTE('Serving Bellevue and the whole Eastside, Gold Coast lane or Lake Hills cul-de-sac. Tell us the neighborhood and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Bellevue?',
 prose(
  L('Open trailers carry most of the Eastside, and the table above is priced for one.'),
  P('An enclosed trailer keeps off the road grime of seven wet months and the gravel on the pass. The collectors in Medina and Hunts Point book one. So do the engineers bringing a new electric car up from California. A car headed over the mountains in January often rides enclosed too.'),
  P('A commuter car or a student car does fine in the open and arrives clean enough. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages set the two side by side.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A number, a lot at South Bellevue or Factoria, and a signature at delivery. The start date picks the week.'),
  P('Approve the price, and a carrier already riding 405 that week takes the car. We confirm the lot and the window the same afternoon. At pickup the driver inspects the car with you and notes every mark on the Bill of Lading. You initial it, and the delivery inspection is checked against it.'),
 )+ULI([
  "Personal things out of the car, trunk and glovebox included",
  "Gas at about a quarter tank",
  "Your own photos of each side and the mileage that morning",
  "One key that works, and a note about any quirks",
  "Any aftermarket alarm off",
  "Downtown, in Medina, in Bridle Trails, or on the hills, plan on a lot",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> page lays out the sequence, and the <a href="car-shipping-preparation.html">preparation</a> page has the whole checklist.'))))

BODY.append(sec('Why Ship Guy','Why Bellevue Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already run 405 and 90 every day. We know which bridge is open and which hill is iced.'),
  P('Our FMCSA license and our $75,000 bond are a public record on the federal register. The office is on 116th Avenue Northeast.'),
  P('The coordinator who quotes the move is the one who answers the phone until delivery. The <a href="services.html">services</a> page compares open, enclosed, and expedited.'),
 )))

BODY.append(office('Bellevue','2265 116th Ave NE #741','Bellevue, WA 98004','+14253187183','(425) 318-7183','PT',
 '2265+116th+Ave+NE+%23741,+Bellevue,+WA+98004','Visit Us','Find Ship Guy in Bellevue',
 'Our office is on 116th Avenue Northeast, east of 405, a few blocks from the hospital.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4106.733351985049!2d-122.1872925!3d47.6298728!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x54906d3adec37907%3A0x710a3954b783fff9!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793300056220!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Bellevue to California or Spokane?","Los Angeles is eleven hundred thirty-five miles down 5 and runs eight hundred to eleven hundred fifty dollars. San Francisco is eight hundred ten miles and runs six hundred to eight hundred eighty. Spokane over the pass runs two hundred sixty to three hundred ninety. Portland costs the least of all. An SUV or a pickup runs 10 to 25 percent more."),
 ("Can the carrier come to my street in Medina or on Somerset?","No. Medina, Clyde Hill, and Hunts Point are narrow lanes behind gates and hedges. Somerset, Cougar Mountain, and Lakemont climb on switchbacks. The driver meets you at the South Bellevue park-and-ride, the Factoria lots, or on 84th. Lake Hills, Crossroads, Newcastle, Redmond, and Issaquah usually allow the curb."),
 ("Is the 520 bridge toll in my price?","Yes, when the route uses that bridge. A loaded trailer takes 90 across the lake for free unless the address sits on the 520 side. When it does, the toll rides inside the quote. There is no separate line for it, and nothing is added at delivery."),
 ("Do you ship cars for the software campuses and the towers?","Yes, every week. The company in Redmond and the retailer downtown relocate engineers on start dates all year. The wireless carrier, the truck maker, and the utility do the same on offer dates. The package usually covers one car, and the second one rides a trailer with us. Reimbursed by an employer? We produce the paperwork it wants."),
 ("Do you handle moves for the joint base and the naval station?","Yes. Both send families to the Eastside on orders, with a summer peak. Orders usually cover one vehicle, and the second one ships with us. The handoff happens at a lot in Bellevue rather than at a gate. Ship Guy is a private broker with no connection to either base."),
 ("Can you ship a car to or from Redmond, Kirkland, or Issaquah?","Yes, and all three price the same as Bellevue. Redmond rides the same carriers off 520 at 148th, and the curb works. Kirkland rides them off 405 at 85th, and the waterfront blocks meet the truck on a main road. Issaquah rides them off 90 at Front Street. Send the full address for a hillside."),
 ("What happens if it snows on my pickup day?","The hills close and the rest waits a day. Somerset, Cougar Mountain, Lakemont, and Bridle Trails are off limits to a trailer until the ice melts. A carrier waits in Renton or Tukwila until 405 is clear. A pickup in the flats moves to a plowed lot in Factoria or at South Bellevue. You hear it from us before the driver does."),
 ("Can you deliver on a Bellevue College or UW move-in date?","Yes. The college takes cars in late September, and the university across the lake follows a week later. A parent books by phone, and an adult meets the truck at a lot to sign. The handoff for the university happens on the Eastside and skips the bridge traffic. The window follows the date."),
 ("Can you ship a car that does not run from Bellevue?","Yes. We send a carrier with a winch, and the extra loading time is priced up front. The Eastgate lots or the Factoria lots give the driver level ground. Tell us whether it rolls, steers, and brakes, and whether it sits in a garage."),
 ("What do you need for a Bellevue car shipping quote?","Pickup and delivery addresses, with the neighborhood or the Eastside town. The year, make, and model. Whether it drives. Open or enclosed. The week you want. Five answers, and a Bellevue number is back the same day."),
]
BODY.append(faq_section(FAQ,'Bellevue FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Bellevue?','Two minutes on the form above gets your lane a Bellevue number. Name the neighborhood and the week, and a carrier already on 405 takes it.','+14253187183','(425) 318-7183','Get your free Bellevue quote'))

build({
 'slug':'auto-transport-bellevue-washington',
 'title':'Car Shipping in Bellevue, WA — Auto Transport | Ship Guy',
 'meta':'Car shipping in Bellevue, WA, on the Eastside between the two floating bridges and under 405. Software campus and tower relocations, the 520 toll inside the quote, lot handoffs for downtown, Medina, Bridle Trails, and the hills, curbside pickups in Lake Hills, Crossroads, Redmond, and Issaquah, the snow days, and the bridge closures. Local office on 116th Avenue Northeast. Free quote.',
 'h1':'Car Shipping in<br>Bellevue, <span class="accent">Washington</span>',
 'lede':'Open, enclosed, and expedited auto transport across the Eastside, planned around 405, the two bridges, the toll, the campus calendar, and the two days a year it snows on the hills.',
 'tel':'+14253187183','disp':'(425) 318-7183','brand':'Bellevue','keyword':'car shipping in bellevue',
 'localterms':['bellevue','interstate 405','floating bridges','seattle','116th avenue','eastside','medina','issaquah','redmond','renton','kirkland','bothell','interstate 90','factoria','mercer island','highway 520','toll','bellevue way','148th','coal creek parkway','downtown','gold coast','hills','software','towers','hospital','snow days','portland','vancouver','spokane','boise','missoula','sacramento','salt lake city','california','denver','bridle trails','somerset','lake hills','crossroads','newcastle','boeing','express toll lanes','rush hours','tukwila','eastgate','spring district','overlake','park-and-ride','old bellevue','main street','wilburton','northtowne','clyde hill','hunts point','yarrow point','gates','hedges','84th','enatai','beaux arts','horse trails','140th','robinswood','woodridge','office parks','cougar mountain','lakemont','switchbacks','sammamish','woodinville','waterfront','transplants','arizona','start dates','online retailer','wireless carrier','truck maker','106th','utility','traveling nurses','residents','aerospace','game studios','landerholm circle','university','joint base','tacoma','naval station','everett','palm springs','snowflake lane','arts fair','strawberry festival','maintenance','rail','february 2019','windstorms','2006','firs','smoke','september 2020','june 2021','one hundred eight','grime','gravel','electric car','bill of lading','fmcsa','85th','front street','winch','newport hills','glovebox'],
}, BODY, FAQ)
