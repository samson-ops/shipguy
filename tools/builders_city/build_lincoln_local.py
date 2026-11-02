import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Lincoln, Nebraska','Car shipping in the capital, where seven Saturdays a year the stadium becomes the third-largest city in the state',
 ['Car shipping in Lincoln runs along Interstate 80 on the north edge and down Highway 2 southeast. Ship Guy is a licensed auto transport broker with an office on Plantation Drive in south Lincoln.',
  'We book vetted carriers across Lincoln, from the Near South to the Highlands and out to Waverly. The carriers own the trucks. Ship Guy holds the license and the bond.',
  'Interstate 80 runs along the north edge with exits from the 77 bypass to 56th Street and Waverly. Interstate 180 drops into downtown. Highway 2 is the Kansas City road through the south side. Highway 77 is the west bypass, and the new South Beltway ties the two together. O Street and Cornhusker Highway carry the rest.',
  'This page covers 80, 180, Highway 2, 77, O Street, downtown, the Near South, and the subdivisions. It also covers the Capitol, the university, the game days, the hospitals, the insurance offices, and the winter.'],
 'Lincoln at a glance',
 ['Most pickups happen within 1 to 3 days. Nearly every carrier crossing the country rides 80 past the city. The Omaha pool is an hour east. The Kansas City trucks come up Highway 2.',
  'Omaha, Kansas City, and Des Moines ride a single day on the truck. Sioux Falls and Wichita take a day. Denver, Minneapolis, and Chicago take one to two, and Dallas takes two.'],
 'Tell us the neighborhood. The Near South, the Haymarket, and the campus blocks meet the truck on a main road. The south subdivisions, the Highlands, Eastridge, and the grids off O Street usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 80, Interstate 180, Highway 2, Highway 77, Highway 6, O Street, Cornhusker Highway, and the South Beltway',
 prose(
  L('Lincoln is a grid on a creek with the busiest road in the country along its north edge. A carrier picks its exit by the side of town.'),
  P('Interstate 80 runs along the north edge of the city. The 77 exit serves the west side and the airport. 27th Street serves the north, and 56th Street serves the northeast. Waverly is the last exit before the Omaha pool. Interstate 180 leaves 80 and runs straight into downtown as 9th and 10th Streets. The road west to Grand Island and Denver is the same interstate, and it closes in a blizzard. The state shuts the gates, and the trucks wait in town.'),
  P('Highway 2 is the Nebraska Parkway, the strip across the south side from 14th Street to 84th. Beyond that it runs southeast to Nebraska City and the Kansas City road. Highway 77 is the west bypass, south to Beatrice and north to the interstate. The South Beltway ties 77 to Highway 2 around the bottom of the city. O Street runs the whole width of town. Cornhusker Highway is the northeast road to Waverly, and Capitol Parkway cuts the diagonal into downtown.'),
  P('The carriers come off 80 at 27th Street or the 77 exit. They come off Highway 2 at 27th or 70th. The big-box lots on North 27th are the usual meeting spot. The lots along Highway 2 work too. So do the arena lots in the Haymarket outside the games and the fairgrounds lots at 84th. The airport cell lot works for a fly-and-ship.'),
  P('Our office is on Plantation Drive in south Lincoln, just off Highway 2 near 27th Street.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the Haymarket, the Near South, Country Club, Havelock, University Place, Belmont, the Highlands, Air Park, Eastridge, and the South',
 prose(
  L('Lincoln is a tight old grid around the Capitol and wide new subdivisions on every edge. The truck meets the old grid on a main road.'),
  P('Downtown runs from the Capitol north to the campus, office blocks and one-way streets. The Haymarket at the west end is brick warehouses, the arena, and the tracks. The driver meets you at the arena lots or on 9th Street. The Near South below the Capitol is the oldest neighborhood. It is big houses on narrow streets with tree lawns and alley garages. A trailer does not enter. The handoff moves to 27th Street or Capitol Parkway. The campus blocks north of downtown are the same, and the lots on Vine Street take the handoff.'),
  P('Country Club and the Sheridan Boulevard streets south of there are winding and wooded. The handoff moves to Van Dorn or 33rd. Havelock on the northeast side is the old railroad town around the car shops. It is a plain grid where the curb works. University Place, Bethany, and the grids out to 70th are the same. Belmont and the north grids off 27th are wide, and the truck reaches the curb.'),
  P('The Highlands and Fallbrook on the northwest side by the interstate are the newest subdivisions. The streets are wide. Air Park by the airport is the old base housing, wide streets on a flat grid. Eastridge, Meadowlane, Piedmont, and Wedgewood east of 48th are postwar grids where the curb works. Indian Village, College View, and Irvingdale south of the Capitol are plain blocks with a few narrow ones.'),
  P('The south side from Pine Lake Road to Yankee Hill is the fastest-growing part of the city. Wilderness Hills, Southern Hills, Village Gardens, and Edenton allow the curb nearly everywhere. The cul-de-sacs are the only problem. Waverly, Hickman, and Roca ship with the same trucks and price the same as Lincoln. Crete and Seward add thirty miles. Omaha is an hour east and prices with the city.'),
 )))

ROUTES=[("Omaha, NE","I-80 · ~55 mi","Same day","$140–$230"),("Kansas City, MO","NE-2/I-29 · ~200 mi","Same day","$210–$330"),
 ("Des Moines, IA","I-80 · ~190 mi","Same day","$220–$340"),("Sioux Falls, SD","I-80/I-29 · ~240 mi","1 day","$250–$380"),
 ("Wichita, KS","US-77/I-135 · ~270 mi","1 day","$280–$410"),("Minneapolis, MN","I-29/I-90/I-35 · ~430 mi","1–2 days","$360–$520"),
 ("St. Louis, MO","I-29/I-70 · ~430 mi","1–2 days","$400–$570"),("Denver, CO","I-80/I-76 · ~490 mi","1–2 days","$400–$570"),
 ("Chicago, IL","I-80 · ~520 mi","1–2 days","$430–$620"),("Dallas, TX","I-35 · ~640 mi","2 days","$460–$670")]
BODY.append(rate_table('Lanes &amp; Costs','Lincoln Car Shipping Lanes and Estimated Costs',
 'The lanes Lancaster County cars run most, with estimated open-trailer ranges. Price your own route on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Lincoln, sedan that runs, open trailer. An SUV or a pickup costs 10 to 25 percent more, and enclosed more still. The week you pick and the carriers passing on 80 that week set the final figure.',
 prose(
  P('Lincoln prices with Omaha on every lane, plus or minus fifty miles. The Denver and Chicago lanes ride 80 and fill every day. Every carrier crossing the country is on it. The Kansas City lane rides Highway 2 to 29. The Texas lane rides 29 and 35 through Kansas City. The Arizona and Texas lanes fill each October with the retirees, and the price rises with them.'),
  P('A move-in date in August or a game Saturday means a busy week. The <a href="car-shipping-cost.html">cost guide</a> explains how size, condition, and timing move the figure.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The State, the University, the Two Hospital Systems, the Insurance Offices, the Plant, the Railroad Shops, the Guard Wing, and the Retirees',
 prose(
  L('Lincoln relocates state employees, professors, nurses, actuaries, and students. The state and the university move the most.'),
  P('State government fills the Capitol and the office blocks around it. The agencies move staff in on start dates all year. The legislature brings senators and staff to town from January into April or June. The university brings faculty on contract dates and twenty-five thousand students in the third week of August. The campus blocks are full that week, and the handoff happens at the lots on Vine Street. The cars leave in May. A parent books it, and an adult signs at the lot.'),
  P('The two hospital systems bring residents each June and hire traveling nurses year round. The insurance companies on O Street and in the Haymarket relocate actuaries and managers on start dates. The sports video company in the Haymarket hires engineers the same way. The plant on Northwest 27th builds personal watercraft and rail cars and moves engineers between plants. The railroad’s car shops in Havelock move crews on bid cycles. When an employer covers the move, the documentation comes from our office.'),
  P('The Guard’s refueling wing at the airport rotates airmen on orders. The jet completion hangars beside it bring technicians on contract. The prison on 14th Street relocates staff the same way. Ship Guy is a private broker with no tie to the Guard. The <a href="military-car-shipping.html">military</a> page explains how orders set the timing.'),
  P('The second college on the northeast side and the third in College View take cars in late August. Retirees head for Arizona and Texas each October and return in April. The <a href="state-to-state-car-shipping.html">state-to-state</a> page explains what a state line adds.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Game Days, Move-In Week, the Marathon, the Fair, the Session, the Tournaments, the Blizzards, the Ice, and the Tornadoes',
 prose(
  L('Lincoln runs on a football calendar and a legislative one. The weather problem is an interstate the state closes when the plains blow shut.'),
  P('Seven Saturdays from late August to November fill the stadium. Every home game has sold out since 1962. Interstate 80 fills from Omaha by nine in the morning, and the streets around the stadium close. We schedule pickups around the games. Move-in week in the third week of August fills the campus blocks. The marathon closes downtown and Sheridan Boulevard on the first Sunday in May. The county fair fills the fairgrounds at 84th and Havelock in late July. The state tournaments fill the arena and the Devaney Center in March. Book three weeks ahead for an August date.'),
  P('Blizzards shut 80 west of the city several times each winter. The state closes the gates, and the trucks wait in town until the plows finish. The Christmas 2009 blizzard closed the interstate for two days. The October 1997 storm dropped a foot of wet snow on the trees. It put the city in the dark for a week. An ice storm shifts a handoff to the afternoon. A carrier does not load a car at twenty below.'),
  P('The April 2024 tornado crossed 80 at Waverly and flattened a plant on the northeast side. The December 2021 windstorm took roofs and power lines across the city. A tornado watch holds the truck at the truck stop until it lifts. We call before it does. A wet spring puts Salt Creek over the low crossings on the west side for a morning.'),
  P('Summer brings heat, humidity, and hail. No carrier loads under a hail warning. They clear by evening, and the day runs a few hours late.'),
 )+chips(["Downtown","The Haymarket","The Capitol","The Near South","Country Club","Sheridan Boulevard","Woods Park","Irvingdale","Indian Village","College View","Havelock","University Place","Bethany","Belmont","The Highlands","Fallbrook","Air Park","West A","Capitol Beach","Eastridge","Meadowlane","Piedmont","Wedgewood","Edenton","Wilderness Hills","Southern Hills","Pine Lake","Yankee Hill","Waverly","Hickman"])
 +NOTE('Serving Lincoln and the whole of Lancaster County, Near South block or Pine Lake cul-de-sac. Tell us the neighborhood and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Lincoln?',
 prose(
  L('Open trailers carry most of eastern Nebraska, and the table above is priced for one.'),
  P('An enclosed trailer keeps off the salt, the pre-storm brine, and the hail. The collectors in Country Club book one. So do the alumni moving a car that matters more than the rest of the load. A car leaving ahead of a blizzard rides whatever truck has a spot, and we tell you so.'),
  P('A daily driver or a student’s car rides an open trailer just fine. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages compare the two.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A figure, a lot on North 27th, and a signature at the other end. The move-in or the start date sets the week.'),
  P('Approve the figure, and we put the car on a carrier already passing on 80 that week. Lot and window are fixed the same afternoon. The driver photographs the car at pickup and lists its condition on the Bill of Lading. You initial it there, and it is the record at delivery.'),
 )+ULI([
  "Clear the cabin and the trunk of anything personal",
  "Run the tank down to a quarter",
  "Take a photo of each side and of the odometer before the truck comes",
  "One working key, and a note on any known faults",
  "Aftermarket alarm switched off",
  "In the Near South, the Haymarket, or on the campus blocks, expect a main road",
 ])+prose(P('See the <a href="how-it-works.html">how it works</a> page for the order of events and the <a href="car-shipping-preparation.html">preparation</a> page for pickup day.'))))

BODY.append(sec('Why Ship Guy','Why Lincoln Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already pass on 80 every day. We know which Saturdays to stay away from the stadium.'),
  P('Our FMCSA license and our $75,000 bond are a public record on the federal register. The office is on Plantation Drive in south Lincoln.'),
  P('The coordinator who quotes your move answers until the car is delivered. The <a href="services.html">services</a> page compares open, enclosed, and expedited side by side.'),
 )))

BODY.append(office('Lincoln','3400 Plantation Dr Ste 445','Lincoln, NE 68516','+14028148622','(402) 814-8622','CT',
 '3400+Plantation+Dr+Ste+445,+Lincoln,+NE+68516','Visit Us','Find Ship Guy in Lincoln',
 'Our office is on Plantation Drive in south Lincoln, just off Highway 2 near 27th Street.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3730.787845461989!2d-96.6699964!3d40.7529973!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x879695440b9b15a3%3A0x10f452c7f189e6e1!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793629931425!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Lincoln to Denver or Chicago?","Denver runs four hundred to five hundred seventy dollars for a sedan. That is about four hundred ninety miles west on 80 and 76. Chicago runs four hundred thirty to six hundred twenty, about five hundred twenty miles east on 80. Omaha is an hour away and the lowest lane on the table. An SUV or a pickup runs 10 to 25 percent higher."),
 ("Will a Husker game day affect my pickup?","Yes. Seven Saturdays a year the stadium fills and 80 backs up from Omaha. The streets around the campus close. We do not schedule a Lincoln pickup on a home Saturday. The Friday before and the Sunday after run normally, and the rest of the city is unaffected."),
 ("Can the carrier come to my street in the Near South or Country Club?","No. The Near South is narrow streets with tree lawns and alley garages. Country Club is winding and wooded. The driver meets you on 27th Street, Capitol Parkway, or Van Dorn. Eastridge, Havelock, the Highlands, Air Park, and the south subdivisions usually allow the curb."),
 ("Can you deliver on a University of Nebraska move-in date?","Yes. The university takes cars in the third week of August and sends them home in May. Mom or Dad books, and an adult signs at a lot. The campus blocks are packed that week, so we meet at the lots on Vine Street. Your date sets the window."),
 ("Do you ship cars for state employees and the hospitals?","Yes, every week of the year. The agencies move staff in on start dates, and the session brings senators and staff each January. The two hospital systems bring residents each June and hire traveling nurses in every season. When the employer reimburses the move, we supply the paperwork. The handoff happens at the lots on North 27th or along Highway 2."),
 ("Can you ship a car to or from Omaha, Waverly, or Crete?","Yes. Waverly, Hickman, and Roca ride the same carriers and price the same as Lincoln. Omaha is an hour east and prices with the city on every lane. Crete and Seward add thirty miles on two-lane roads and a few hours on the day."),
 ("What happens if a blizzard closes 80 on my pickup day?","The truck holds in town until the state opens the gates, usually a day. You get a call the moment the gates close. We reschedule for the first clear morning, and the figure does not move. Give a January date a flexible week."),
 ("Do you handle moves for the Guard wing at the airport?","Yes. The refueling wing rotates airmen on orders, and the jet completion hangars beside it bring technicians on contract. The handoff happens at the lots on Northwest 12th or at the airport. Ship Guy is a private broker and has no tie to the Guard."),
 ("Can you ship a car that does not run from Lincoln?","Yes. We send a winch-equipped carrier and quote the loading time with the rest. The big-box lots on North 27th and along Highway 2 are flat. Let us know whether it rolls, steers, and brakes."),
 ("What do you need for a Lincoln car shipping quote?","The two addresses with the neighborhood. The year, make, and model, and whether it runs. Open or enclosed, and the week around the move-in or the start date. Send those, and the Lincoln figure is back the same day."),
]
BODY.append(faq_section(FAQ,'Lincoln FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Lincoln?','Two minutes on the form above gets your lane a Lincoln figure. Name the neighborhood and the week, and a carrier already passing on 80 takes it.','+14028148622','(402) 814-8622','Get your free Lincoln quote'))

build({
 'slug':'auto-transport-lincoln-nebraska',
 'title':'Car Shipping in Lincoln, NE — Auto Transport | Ship Guy',
 'meta':'Car shipping in Lincoln, NE, the capital on Interstate 80. Game-day scheduling, university move-in, state and hospital relocations, Guard moves at the airport, main-road handoffs for the Near South and Country Club, curbside pickups in the south subdivisions and the Highlands, and the blizzards on 80. Local office on Plantation Drive. Free quote.',
 'h1':'Car Shipping in<br>Lincoln, <span class="accent">Nebraska</span>',
 'lede':'Open, enclosed, and expedited auto transport across Lincoln and Lancaster County, planned around 80, Highway 2, the game days, the campus calendar, and the winter.',
 'tel':'+14028148622','disp':'(402) 814-8622','brand':'Lincoln','keyword':'car shipping in lincoln',
 'localterms':['lincoln','capital','stadium','interstate 80','interstate 180','highway 2','highway 77','cornhusker highway','o street','south beltway','capitol parkway','27th street','56th street','waverly','plantation drive','downtown','haymarket','arena','capitol','near south','country club','sheridan boulevard','havelock','university place','bethany','belmont','highlands','fallbrook','air park','eastridge','meadowlane','piedmont','wedgewood','indian village','college view','irvingdale','pine lake','yankee hill','wilderness hills','southern hills','village gardens','edenton','hickman','roca','crete','seward','beatrice','omaha','kansas city','des moines','sioux falls','wichita','minneapolis','st. louis','denver','chicago','dallas','arizona','texas','retirees','state employees','professors','nurses','actuaries','students','legislature','senators','session','university','faculty','vine street','hospital systems','residents','traveling nurses','insurance','sports video','personal watercraft','rail cars','car shops','bid cycles','refueling wing','airmen','jet completion','technicians','prison','game days','move-in','marathon','county fair','fairgrounds','tournaments','devaney','blizzard','gates','christmas 2009','october 1997','april 2024','tornado','december 2021','windstorm','salt creek','hail','salt','brine','bill of lading','fmcsa','winch','9th street','vine','van dorn','airport','truck stop','1962'],
}, BODY, FAQ)
