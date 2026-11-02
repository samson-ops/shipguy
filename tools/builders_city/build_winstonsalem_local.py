import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Winston-Salem, North Carolina','Car shipping in the city of tobacco towers and a Moravian village, at the west end of the Triad',
 ['Car shipping in Winston-Salem runs on Interstate 40 along the south side and Highway 52 through the east. Ship Guy is a licensed auto transport broker with an office on West Fifth Street downtown.',
  'We book vetted carriers across Winston-Salem, from the West End to Konnoak Hills and out to Clemmons. The carriers own the trucks. Ship Guy holds the license and the bond.',
  'Interstate 40 runs along the south side past the mall to Greensboro and the mountains. Highway 52 is 74 now, north to Mount Airy and south to 85 at Lexington. The Salem Parkway is the old Business 40 through downtown, rebuilt in 2020. Silas Creek Parkway loops the west side, and University Parkway runs north to the campus and the fairgrounds.',
  'This page covers 40, 52, 421, the Parkway, Silas Creek, downtown, the West End, Ardmore, and Old Salem. It also covers the medical center, the universities, the research campus, the furniture market, and the ice storms.'],
 'Winston-Salem at a glance',
 ['Most pickups happen within 1 to 3 days. The 40 carriers pass between Raleigh and Asheville all day, and the 85 trucks turn north at Lexington. The Triad pool stages between the city and Greensboro.',
  'Charlotte, Raleigh, Greensboro, and Columbia ride a single day on the truck. Richmond takes a day. Washington, Atlanta, and Nashville take one to two, and New York and Florida take two.'],
 'Tell us the neighborhood. Old Salem, the West End, Washington Park, and downtown meet the truck on a main road. Ardmore, Sherwood Forest, Konnoak Hills, Clemmons, and the grids off Silas Creek usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 40, Highway 52 and Interstate 74, Highway 421, the Salem Parkway, Silas Creek Parkway, Stratford Road, and University Parkway',
 prose(
  L('Winston-Salem is a hilly old city with a rebuilt freeway through its middle. A carrier picks the loop road and meets you where the hills flatten.'),
  P('Interstate 40 runs along the south side past the mall and the hospital on Silas Creek. East it runs thirty miles to Greensboro and on to Raleigh. West it climbs to Statesville and 77, and 421 leaves it for the mountains at Boone. Highway 52 runs north and south through the east side of downtown. The 74 signs went up a few years ago. North it reaches Mount Airy and Virginia. South it reaches 85 at Lexington, the Charlotte road. The new beltway on the east side ties 52 to 40 and Business 40 without crossing town.'),
  P('The Salem Parkway is the old Business 40 through downtown. It closed for a year and a half and reopened in 2020 with new bridges. Highway 421 rides it east to Greensboro and west to Yadkinville. Silas Creek Parkway loops the west and south sides past the second hospital. Stratford Road is the mall strip from downtown to 40. University Parkway runs north from downtown to the university, the coliseum, and the fairgrounds. Peters Creek Parkway runs south, and Reynolda Road runs northwest through the estates.'),
  P('The carriers come off 40 at Stratford Road or Silas Creek, and off 52 at the Parkway. The mall lots on Stratford are the usual meeting spot. The big-box lots on Hanes Mall Boulevard work too. So do the coliseum lots on University Parkway outside a game and the fairgrounds lots outside the fair. The airport in Greensboro is twenty miles east for a fly-and-ship.'),
  P('Our office is in the tower on West Fifth Street downtown, two blocks from the convention center.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, Old Salem, the West End, Ardmore, Buena Vista, Reynolda, Washington Park, Waughtown, Konnoak Hills, Sherwood Forest, and Clemmons',
 prose(
  L('Winston-Salem is old streets on steep hills near downtown and long ranch subdivisions on the ridges around it. The truck meets the hills on a main road.'),
  P('Downtown runs along Fourth and Trade Streets between the Parkway and the tobacco towers, one-way streets and garages. The research campus in the old cigarette factories sits at the east end of it. The driver meets you at the garage entrances on Fifth Street or at the ballpark lots. Old Salem south of downtown is the Moravian village, brick sidewalks and narrow streets from the 1700s. A trailer does not enter. The handoff moves to Main Street at the south end or to the Parkway lots.'),
  P('The West End climbs the hill west of downtown, big old houses on streets that bend and drop. The driver meets you on Fourth Street or Northwest Boulevard. Ardmore between the West End and the medical center is bungalows on a grid. The curb usually works. Buena Vista and Reynolda to the northwest are estates on wide curving streets under old oaks. The curb works where the branches allow it. The handoff moves to Reynolda Road where they do not.'),
  P('Washington Park south of Old Salem is steep and narrow, and the handoff moves to Broad Street. Waughtown and the southeast grids around the second university are plain blocks where the curb works. Konnoak Hills and the south side off Peters Creek are postwar ranches on wide streets. Sherwood Forest, Westview, and the west side off Robinhood Road are the same. The truck reaches the curb. The north side off University Parkway and the retirement communities allow the curb nearly everywhere.'),
  P('Clemmons and Lewisville west on 40 ship with the same trucks and price the same as Winston-Salem. So do Kernersville, Walkertown, and Rural Hall. Greensboro and High Point are thirty minutes away and price with the city. Mount Airy and Lexington add thirty miles and nothing else.'),
 )))

ROUTES=[("Charlotte, NC","US-52/I-85 · ~80 mi","Same day","$150–$240"),("Raleigh, NC","I-40 · ~105 mi","Same day","$150–$240"),
 ("Columbia, SC","US-52/I-85/I-77 · ~190 mi","Same day","$220–$340"),("Richmond, VA","US-52/US-58/I-85 · ~220 mi","Same day","$240–$360"),
 ("Washington, DC","I-85/I-95 · ~330 mi","1 day","$300–$440"),("Atlanta, GA","I-85 · ~330 mi","1 day","$300–$440"),
 ("Nashville, TN","I-40 · ~440 mi","1 day","$390–$560"),("New York, NY","I-85/I-95 · ~520 mi","1–2 days","$450–$650"),
 ("Orlando, FL","I-77/I-95 · ~600 mi","2 days","$460–$660"),("Chicago, IL","I-77/I-65 · ~760 mi","2 days","$550–$800")]
BODY.append(rate_table('Lanes &amp; Costs','Winston-Salem Car Shipping Lanes and Estimated Costs',
 'The lanes Forsyth County cars run most, with estimated open-trailer ranges. Price your own route on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Winston-Salem, sedan that runs, open trailer. Expect an SUV or a pickup to run 10 to 25 percent higher, and enclosed higher still. The week you choose and the carriers free on 40 that week set the final figure.',
 prose(
  P('Winston-Salem prices with Greensboro on every lane, because the same trucks serve the whole Triad. The Charlotte lane rides 52 to 85 and fills every day. The Raleigh lane rides 40 and fills the same way. The Atlanta and Washington lanes ride 85 in both directions. The Florida lane rides 77 to 95 and fills each fall with the retirees and the students.'),
  P('A July start at the medical center or the late August move-in lands in the busiest weeks. The <a href="car-shipping-cost.html">cost guide</a> explains what size, condition, and timing do to the figure.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Medical Center, the Second Hospital, the Research Campus, the Tobacco Company, the Apparel Company, the Universities, the Warehouses, and the Retirees',
 prose(
  L('Winston-Salem relocates physicians, researchers, professors, students, and retirees. The medical center moves more households than anyone else in the county.'),
  P('The medical center on the hill southwest of downtown is the largest employer in the county. It brings residents each June for a July start and hires traveling nurses year round. The medical school on the research campus brings faculty on contract dates. The second hospital on Silas Creek does the same. The handoff for all of them happens at the mall lots or on Stratford Road. If the hospital or an employer pays for the move, the documentation comes from our office.'),
  P('The research campus in the old cigarette factories is labs and startups. It moves scientists on grant cycles. The tobacco company keeps its headquarters downtown and its plant north of the city. It moves managers between the two. The apparel company on Hanes Mill Road relocates designers and managers the same way. The banks that moved their headquarters to Charlotte left thousands of jobs behind, and those offices still hire. The warehouses along 40 toward the airport in Greensboro move managers on opening dates.'),
  P('The university on the north side takes student cars in late August. The arts conservatory by Old Salem follows. The state university on the east side does the same in mid-August. The women’s college in Old Salem and the community college on Silas Creek add more. A parent books it, and an adult signs at the lot. The cars go home in May. The <a href="state-to-state-car-shipping.html">state-to-state</a> page explains the paperwork for a state line.'),
  P('Retirees fill the communities on the north side and the condos downtown. Many of them came from the Northeast. Some leave for Florida each November and come back in April.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Fair, the Furniture Market, Move-In Week, the Film Festival, the Theatre Festival, Football Saturdays, the Festival of Lights, the Ice Storms, and the Snow',
 prose(
  L('Winston-Salem runs on a hospital calendar and a campus calendar. The weather problem is ice that arrives twice a winter and stays a day.'),
  P('The fair fills the fairgrounds on the north side for ten days in early October. It takes University Parkway with it. The furniture market in High Point fills every Triad hotel for a week each April and October. The carriers stage farther out. Move-in week in late August fills the blocks around the university. The film festival takes downtown for a week in April. The theatre festival takes it for a week every other August. Football Saturdays fill the stadium and the coliseum lots from September to November. Book three weeks ahead for a late August date.'),
  P('Ice comes once or twice a winter, and the hills make it worse here than in Greensboro. The December 2002 ice storm put the city in the dark for a week. It dropped trees on every street in Buena Vista. The December 2018 storm dropped a foot of snow and closed 40 for a day. The February 2014 storm did the same. The carriers wait in Greensboro or Statesville until the roads clear. A storm pushes a pickup to the next clear morning at the same figure.'),
  P('The festival of lights at Tanglewood backs up 40 at Clemmons on the weekends from November into January. A Clemmons handoff moves to a weekday that month. Hurricane remnants bring a day of rain and wind a few times a decade. Hugo in 1989 took trees across the city on its way through.'),
  P('Summer brings heat, humidity, and an afternoon storm most weeks. The storm shifts the loading hour and nothing else. The pollen in April coats every car yellow for three weeks.'),
 )+chips(["Downtown","Fourth Street","Trade Street","The Research Campus","Old Salem","The West End","Ardmore","Buena Vista","Reynolda","Washington Park","Waughtown","Konnoak Hills","Sherwood Forest","Westview","Robinhood Road","Stratford Road","Hanes Mall","Silas Creek","University Parkway","The Fairgrounds","Oldtown","Ogburn Station","Clemmons","Lewisville","Pfafftown","Rural Hall","Walkertown","Kernersville","Lexington","Mount Airy"])
 +NOTE('Serving Winston-Salem and the whole of Forsyth County, West End hill or Clemmons cul-de-sac. Tell us the neighborhood and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Winston-Salem?',
 prose(
  L('Open trailers carry most of the Triad, and the table above is priced for one.'),
  P('An enclosed trailer keeps off the pollen, the brine, and the sap under the oaks. The collectors in Buena Vista book one. So do the physicians bringing a car worth more than the rest of the move. Ahead of an ice storm, the car takes whatever truck has a spot. We tell you that first.'),
  P('A daily driver or a student’s car is fine on an open trailer. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages set them side by side.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A figure, a lot on Stratford Road, and a signature when the car arrives. The start date or the move-in sets the week.'),
  P('Approve the figure, and we book a carrier already running 40 that week. The lot and the window are set the same afternoon. At pickup the driver photographs every panel and writes the condition on the Bill of Lading. You initial that sheet, and it is the record at delivery.'),
 )+ULI([
  "Everything personal out of the cabin and the trunk",
  "Fuel down to a quarter tank",
  "Photograph each side and the odometer before the truck comes",
  "One good key, and a note about any known faults",
  "Any add-on alarm turned off",
  "In Old Salem, the West End, or Washington Park, expect a main road",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> page covers the sequence, and the <a href="car-shipping-preparation.html">preparation</a> page covers pickup day.'))))

BODY.append(sec('Why Ship Guy','Why Winston-Salem Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already run 40 every day. We know which weeks the furniture market takes every truck in the Triad.'),
  P('Our FMCSA license and our $75,000 bond are a public record on the federal register. The office is on West Fifth Street downtown.'),
  P('Your coordinator answers from the first call until the delivery signature. Open, enclosed, and expedited are compared on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Winston-Salem','500 W 5th St #562','Winston-Salem, NC 27101','+13364446889','(336) 444-6889','ET',
 '500+W+5th+St+%23562,+Winston-Salem,+NC+27101','Visit Us','Find Ship Guy in Winston-Salem',
 'Our office is in the tower on West Fifth Street downtown, two blocks from the convention center.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3979.3443867910364!2d-80.2493458!3d36.0990293!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8853af8d85d21e25%3A0x7d601e34adb687ba!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793630957845!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Winston-Salem to Charlotte or New York?","Charlotte runs one hundred fifty to two hundred forty dollars for a sedan. That is about eighty miles down 52 and 85 and the lowest lane on the table with Raleigh. New York runs four hundred fifty to six hundred fifty, about five hundred twenty miles up 95. An SUV or a pickup runs 10 to 25 percent higher."),
 ("Can the carrier come to my street in the West End or Old Salem?","No. The West End is steep streets that bend and drop. Old Salem is narrow streets from the 1700s. The driver meets you on Fourth Street, Northwest Boulevard, or Main Street at the south end. Ardmore, Konnoak Hills, Sherwood Forest, Clemmons, and the grids off Silas Creek usually allow the curb."),
 ("Do you ship cars for the medical center and the research campus?","Yes, every week of the year. The medical center brings residents each June for a July start and traveling nurses all year. The research campus moves scientists on grant cycles. The handoff happens at the mall lots or on Stratford Road. When the employer reimburses the move, we send the paperwork it wants."),
 ("Can you deliver on a Wake Forest or Winston-Salem State move-in date?","Yes. The state university takes cars in mid-August, and the university on the north side follows in late August. The arts conservatory and the community college run the same weeks. Mom or Dad books, and an adult signs at a lot. The campus blocks are packed that week, so we meet at the coliseum lots. Your date sets the window."),
 ("Does the furniture market affect my pickup?","Yes, for a week each April and October. The market in High Point fills every hotel in the Triad, and the carriers stage farther out. A pickup that week schedules a day or two later than usual. The fair in early October takes the fairgrounds lots and University Parkway the same month."),
 ("Can you ship a car to or from Greensboro, Clemmons, or Mount Airy?","Yes. Clemmons, Lewisville, and Kernersville ride the same carriers and price the same as Winston-Salem. Greensboro and High Point are thirty minutes away and price with the city. Mount Airy and Lexington add thirty miles and a few hours on the day."),
 ("What happens if an ice storm hits on my pickup day?","The truck holds in Greensboro or Statesville until the roads clear, usually a day. The hills here ice before the flat land to the east. A call goes out as soon as the forecast turns. We move the pickup to the first clear morning, and the figure holds."),
 ("Is the Salem Parkway open now?","Yes. The old Business 40 through downtown closed in late 2018 and reopened in early 2020 with new bridges. Carriers use it to cross downtown again. The Stratford Road and Silas Creek exits on 40 still take most of the handoffs."),
 ("Can you ship a car that does not run from Winston-Salem?","Yes. A carrier with a winch takes it, and the loading time is built into the quote. The mall lots on Stratford and the big-box lots on Hanes Mall Boulevard are flat. Let us know if it rolls, steers, and brakes."),
 ("What do you need for a Winston-Salem car shipping quote?","The two addresses with the neighborhood, the year, make, and model, and whether it runs. Then open or enclosed and the week around the start date. Send those, and the Winston-Salem figure is back the same day."),
]
BODY.append(faq_section(FAQ,'Winston-Salem FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Winston-Salem?','Two minutes on the form above gets your lane a Winston-Salem figure. Name the neighborhood and the week, and a carrier already running 40 takes it.','+13364446889','(336) 444-6889','Get your free Winston-Salem quote'))

build({
 'slug':'auto-transport-winston-salem-north-carolina',
 'title':'Car Shipping in Winston-Salem, NC — Auto Transport | Ship Guy',
 'meta':'Car shipping in Winston-Salem, NC, at the west end of the Triad. Medical center and research campus relocations, university move-in, the furniture market weeks, main-road handoffs for the West End and Old Salem, curbside pickups in Ardmore, Konnoak Hills, and Clemmons, and the ice storms. Local office on West Fifth Street downtown. Free quote.',
 'h1':'Car Shipping in<br>Winston-Salem, <span class="accent">North Carolina</span>',
 'lede':'Open, enclosed, and expedited auto transport across Winston-Salem and Forsyth County, planned around 40, 52, the hospital calendar, the campus dates, the market weeks, and the ice.',
 'tel':'+13364446889','disp':'(336) 444-6889','brand':'Winston-Salem','keyword':'car shipping in winston-salem',
 'localterms':['winston-salem','tobacco','moravian','triad','interstate 40','highway 52','74','421','salem parkway','business 40','silas creek','stratford road','university parkway','peters creek','reynolda road','hanes mall','fifth street','fourth street','trade street','convention center','downtown','research campus','cigarette factories','old salem','west end','ardmore','buena vista','reynolda','washington park','waughtown','konnoak hills','sherwood forest','westview','robinhood road','oldtown','clemmons','lewisville','kernersville','walkertown','rural hall','greensboro','high point','mount airy','lexington','statesville','boone','charlotte','raleigh','columbia','richmond','washington','atlanta','nashville','new york','orlando','chicago','florida','medical center','residents','traveling nurses','medical school','faculty','second hospital','scientists','grant cycles','tobacco company','headquarters','plant','apparel company','hanes mill road','banks','warehouses','airport','university','arts conservatory','state university','women','community college','students','move-in','retirees','retirement communities','fair','fairgrounds','furniture market','film festival','theatre festival','football saturdays','coliseum','festival of lights','tanglewood','ice storm','december 2002','december 2018','february 2014','hugo','1989','pollen','brine','sap','oaks','bill of lading','fmcsa','winch','ballpark','beltway','northwest boulevard','main street','broad street','garages','1700s','brick sidewalks','hills'],
}, BODY, FAQ)
