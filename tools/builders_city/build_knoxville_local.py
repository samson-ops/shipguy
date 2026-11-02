import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Knoxville, Tennessee','Car shipping where Interstate 40 and 75 share the road through town, the university fills the Fort each August, and the Smokies set the fall traffic',
 ['Car shipping in Knoxville runs on Interstates 40 and 75, which share the road through the city. Ship Guy is a licensed auto transport broker with an office on Gay Street downtown.',
  'We book vetted carriers across Knoxville, from the Old City and the Fort to Farragut and Fountain City. Alcoa, Maryville, and Oak Ridge ride the same trucks. Every truck is a carrier’s own. The license and the bond are Ship Guy’s.',
  'Interstate 40 crosses the whole state and runs through downtown on the stretch rebuilt in 2009. Interstate 75 shares it from the west and leaves north for Lexington on the 640 bypass. Interstate 640 loops the north side, 275 spurs from downtown, and 140 runs south to the airport. Alcoa Highway, Kingston Pike, Broadway, and Chapman Highway carry the rest.',
  'This page covers 40, 75, 640, 140, Alcoa Highway, Kingston Pike, downtown, the Fort, and the hills. It also covers the university, the power authority, the laboratory in Oak Ridge, and the hospitals. The football Saturdays, the ice, and the gorge are here too.'],
 'Knoxville at a glance',
 ['Most Knoxville pickups land within 1 to 3 days. The city sits where the 40 and 75 carriers share the road. The trucks between Nashville, Atlanta, and the Ohio Valley pass through all day. The pool is deep, and the university keeps it moving.',
  'Chattanooga, Nashville, Lexington, Atlanta, and Asheville are a same-day haul. Charlotte, Cincinnati, and Louisville take a day. Memphis takes one to two, and Florida takes two.'],
 'Tell us the neighborhood. Downtown, the Fort, the Strip, Sequoyah Hills, and South Knoxville meet the truck on a main road. Bearden, West Hills, Farragut, Hardin Valley, Fountain City, and Halls usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 40, Interstate 75, Interstate 640, Interstate 275, Interstate 140, Alcoa Highway, Kingston Pike, Henley Street, Broadway, and Chapman Highway',
 prose(
  L('Knoxville is a river city on hills with two interstates braided through the middle of it. A carrier picks its exit and stays on the pikes.'),
  P('Interstate 40 comes in from Nashville and shares the road with 75 from the Loudon County line. It runs through downtown to the Smokies and the Pigeon River gorge. The downtown stretch was rebuilt in 2008 and 2009. The state closed it for fourteen months and sent every truck around 640. Interstate 75 leaves 40 at the split west of downtown and rides 640 around the north side. It heads north for Lexington. Interstate 275 spurs from downtown north to 640. Interstate 140 is the Pellissippi Parkway, from 40 on the west side south to the airport.'),
  P('Alcoa Highway runs from the campus over the river past the medical center to the airport and Maryville. Kingston Pike runs west from the campus through Bearden and West Hills to Farragut. Henley Street carries 441 through downtown and over the Henley Bridge to Chapman Highway and the Smokies. Broadway runs north through Fountain City. Cumberland Avenue is the Strip along the campus, and Neyland Drive runs the river past the stadium. The gorge on 40 at the North Carolina line has run with restrictions since the 2024 hurricane. The Charlotte and Asheville lanes plan around it.'),
  P('The carriers come off 40 at Papermill, Cedar Bluff, or Lovell Road and off 75 at Merchant Drive. They meet at the big-box lots on Kingston Pike or the lots at the mall in West Knoxville. The lots at the fairgrounds in East Knoxville work outside the fair. So do the lots along Alcoa Highway and the truck stops at Lovell Road and Strawberry Plains. The airport is twenty minutes south on Alcoa Highway for a fly-and-ship.'),
  P('Our office is in the 100 block of Gay Street downtown, at the Old City end.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the Old City, the Fort, Fourth and Gill, Sequoyah Hills, Bearden, West Hills, Farragut, Hardin Valley, Fountain City, South Knoxville, East Knoxville, Alcoa, Maryville, and Oak Ridge',
 prose(
  L('Knoxville is a brick downtown, a student hill beside it, old streets under oaks, and subdivisions running west. The truck meets the hills on a main road and the west side at the curb.'),
  P('Downtown is Gay Street, Market Square, and the towers of the power authority, one-way streets and the theaters. The driver meets you on Summit Hill Drive or at the lots by the civic coliseum. The Old City north of the tracks is brick warehouses turned bars and lofts on short blocks. The handoff happens on Jackson Avenue. The Fort between downtown and the campus is student rentals on a steep hill with cars everywhere. No trailer enters it. The handoff moves to the lots off Cumberland or the stadium lots.'),
  P('Fourth and Gill and Old North Knoxville are Victorian streets under big trees. The handoff happens on Broadway. Sequoyah Hills along the river is the old money, big houses on winding boulevards with low limbs. The driver meets you on Kingston Pike. Bearden and West Hills are postwar grids with wide streets, and the curb works. Farragut is cul-de-sacs with covenants, and the handoff moves to the entrance when a covenant bans trailers. Hardin Valley is new subdivisions on open ground, and the truck comes to the house.'),
  P('Fountain City, Halls, and Powell on the north side are wide grids and subdivisions. The curb works nearly everywhere. South Knoxville across the river is hills and hollows from Island Home to Vestal. The handoff happens on Chapman Highway. East Knoxville from Holston Hills to Burlington is older grids, and the curb works where the hills allow. Alcoa and Maryville are mill towns and subdivisions around the plants, and the truck reaches the curb. Oak Ridge is the laboratory’s planned grids, and the curb works on most streets.'),
  P('Alcoa, Maryville, Oak Ridge, Farragut, and Seymour ship with the same trucks and price the same as Knoxville. Lenoir City and Clinton do too. Sevierville adds an hour in October, and Gatlinburg adds the parkway and a figure.'),
 )))

ROUTES=[("Chattanooga, TN","I-75 · ~110 mi","Same day","$150–$240"),("Asheville, NC","I-40 · ~115 mi","Same day","$170–$280"),
 ("Nashville, TN","I-40 · ~180 mi","Same day","$200–$310"),("Lexington, KY","I-75 · ~175 mi","Same day","$220–$340"),
 ("Atlanta, GA","I-75 · ~215 mi","Same day","$220–$340"),("Charlotte, NC","I-40/I-26/I-85 · ~240 mi","1 day","$280–$410"),
 ("Cincinnati, OH","I-75 · ~250 mi","1 day","$270–$400"),("Louisville, KY","I-75/I-64 · ~250 mi","1 day","$270–$400"),
 ("Memphis, TN","I-40 · ~390 mi","1–2 days","$360–$520"),("Orlando, FL","I-75 · ~640 mi","2 days","$500–$730")]
BODY.append(rate_table('Lanes &amp; Costs','Knoxville Car Shipping Lanes and Estimated Costs',
 'The lanes Knox County cars run most, with open-trailer estimates. Price your exact lane on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Knoxville, running sedan, open trailer. SUVs and pickups come in 10 to 25 percent higher, and enclosed sits above that. Your week and the carriers on 40 and 75 that week decide the figure.',
 prose(
  P('Knoxville prices below Nashville on the Carolina and Ohio Valley lanes and above it on the Texas lanes. The Atlanta and Chattanooga lanes ride 75 south and fill every day. The Lexington and Cincinnati lanes ride 75 north. The Nashville and Memphis lanes ride 40 west. The Carolina lanes ride 40 through the gorge or 81 and 26 around it. The detour adds an hour and a few dollars. The Florida lane fills with the retirees each fall.'),
  P('A mid-August move-in or a home Saturday means a busy week. The <a href="car-shipping-cost.html">cost guide</a> takes size, condition, and timing in turn.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The University, the Power Authority, the Laboratory in Oak Ridge, the Hospitals, the Plants in Maryville, the Truck-Stop Chain, the Guard’s Tankers, and the Retirees',
 prose(
  L('Knoxville relocates students, professors, engineers, scientists, nurses, and retirees. The university moves the most.'),
  P('The university on the hill takes close to forty thousand students, and the cars arrive in mid-August. A parent books, and an adult signs at the lots off Cumberland. The cars leave in May. The power authority’s twin towers downtown and its offices around the city relocate engineers on start dates. The packages usually pay for a car. The national laboratory and the weapons plant in Oak Ridge relocate scientists on program schedules and clearance timelines. The handoff happens at the lots in Oak Ridge.'),
  P('The hospital systems on Alcoa Highway, in the Fort, and in West Knoxville bring residents each June. Traveling nurses come all year. The auto-parts plant and the manufactured-home builder in Maryville hire from across the South. So does the aluminum mill in Alcoa. The truck-stop chain’s headquarters relocates staff from across the country. The handoff happens at the lots nearest the office. If the employer covers the shipment, we put it in writing however it needs.'),
  P('The Guard’s tanker wing at the airport rotates airmen on orders. The handoff happens at the airport lots. Ship Guy is a private broker and not part of the Guard or the laboratory. Orders and the dates they set are covered on the <a href="military-car-shipping.html">military</a> page.'),
  P('Retirees come to the lakes and the foothills from the Midwest and Florida. Some go back south for the winter. The <a href="state-to-state-car-shipping.html">state-to-state</a> page spells out the paperwork a state line adds.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Football Saturdays, Move-In Week, the Fall Traffic to the Smokies, the Fair, the Dogwood Festival, the Ice, the Floods, the Fog, and the Gorge',
 prose(
  L('Knoxville runs on a university calendar and a Smokies calendar. The weather problem is an ice storm every winter or two and a valley that floods in February.'),
  P('Football Saturdays bring a hundred thousand people to the stadium and close Neyland Drive from the morning on. The boats fill the river. Move-in week in mid-August fills the Fort and the Strip. The fall traffic to the Smokies runs Chapman Highway and 441 at a crawl every October weekend. The fair takes Chilhowee Park for ten days in September. The dogwood festival fills April, and the Gay Street festivals close downtown for a weekend each spring. Give a mid-August date or a home Saturday three weeks of notice.'),
  P('The February 2015 ice storms coated the city twice in a week and took the power for days. The January 2024 storm dropped nine inches and held the city below freezing for a week. Ice closes the hills, and the carriers wait in Nashville or Chattanooga until the salt trucks finish. February 2019 was the wettest February on record. The creeks and the river put the low roads under water for days.'),
  P('The 2016 fire burned Gatlinburg and killed fourteen people. The Smokies pickups moved to Sevierville for a month. The 2024 hurricane tore out the gorge on 40 at the state line. The Carolina lanes still plan around it. Fog settles in the valley on fall mornings, and a driver waits for it to lift. A tornado watch holds the truck at the lot until it passes.'),
  P('Summer brings heat and humidity in the valley. A driver loads in the morning, and the afternoon storms pass in an hour.'),
 )+chips(["Downtown","Gay Street","Market Square","The Old City","The Fort","Fourth and Gill","Old North Knoxville","Happy Holler","Sequoyah Hills","Bearden","West Hills","Cedar Bluff","Farragut","Hardin Valley","Karns","Fountain City","Halls","Powell","South Knoxville","Island Home","Holston Hills","Alcoa","Maryville","Oak Ridge","Seymour","Lenoir City","Clinton","Sevierville"])
 +NOTE('Serving Knoxville, Knox County, and the Tennessee Valley, Farragut cul-de-sac or Sequoyah Hills boulevard. Name the neighborhood and tell us whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Knoxville?',
 prose(
  L('Open trailers do most of East Tennessee’s work, and the table above assumes one.'),
  P('Enclosed keeps the pollen, the brine before an ice storm, and the spring hail off the paint. The collectors in Sequoyah Hills book it. So do the scientists moving a car worth more than the rest of the relocation. When ice is in the forecast and only an open truck has room, we tell you that first.'),
  P('A commuter car or a student’s sedan rides open and arrives fine. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages set out the difference.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A figure, a lot off 40, and a signature when the car comes off the truck. The move-in or the start date decides the week.'),
  P('Approve the figure, and we hand the car to a carrier already on 40 or 75 that week. The lot and the window are set the same day. The driver photographs the car at pickup and enters its condition on the Bill of Lading. You initial it there, and it is the reference at delivery.'),
 )+ULI([
  "Your belongings out of the cabin and the trunk",
  "Fuel at a quarter tank or less",
  "Photos of every side and the odometer before pickup",
  "A working key and a note on known faults",
  "Aftermarket alarms turned off",
  "In the Fort, in Sequoyah Hills, or on a game Saturday, expect a lot off 40",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> page walks the steps, and the <a href="car-shipping-preparation.html">preparation</a> page covers the morning the truck comes.'))))

BODY.append(sec('Why Ship Guy','Why Knoxville Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already run 40 and 75 through the city every day. We know which Saturdays close Neyland Drive and how the gorge changes a Carolina lane.'),
  P('Our FMCSA license and our $75,000 bond are a matter of public record on the federal register. The office is on Gay Street downtown.'),
  P('One person at Ship Guy carries the move from quote to delivery call. Open, enclosed, and expedited each get a section on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Knoxville','129 S Gay St #522','Knoxville, TN 37902','+18653904490','(865) 390-4490','ET',
 '129+S+Gay+St+%23522,+Knoxville,+TN+37902','Visit Us','Find Ship Guy in Knoxville',
 'Our office is in the 100 block of Gay Street downtown, at the Old City end.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3985.959260098557!2d-83.9204847!3d35.968209099999996!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x885c179580dc961d%3A0xef1259389993c7b1!2sShip%20Guy%20Auto%20Transport!5e1!3m2!1sen!2sus!4v1793631508567!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Knoxville to Atlanta or Nashville?","Atlanta runs two hundred twenty to three hundred forty dollars for a sedan. That is about two hundred fifteen miles down 75. Nashville runs two hundred to three hundred ten, about one hundred eighty miles west on 40. Chattanooga is the lowest lane on the table, two hours down 75. An SUV or a pickup runs 10 to 25 percent more."),
 ("Can you deliver on a University of Tennessee move-in date?","Yes. Cars arrive in mid-August and leave in May. A parent books, and an adult signs at the lot. The Fort and the Strip are closed to a trailer that week. The meeting point is the lots off Cumberland or the stadium lots. The window follows your date."),
 ("What happens on a football Saturday?","The south side of downtown closes. A hundred thousand people fill the stadium, and Neyland Drive and Cumberland close from the morning on. The boats fill the river. The handoff moves to the Kingston Pike lots or the mall, and the figure does not change. Give a home Saturday three weeks of notice."),
 ("Can the carrier come to my street in the Fort or Sequoyah Hills?","No. The Fort is a steep hill of student rentals with cars on both curbs. Sequoyah Hills is winding boulevards with low limbs. The driver meets you on Cumberland or Kingston Pike. Bearden, West Hills, Farragut, Hardin Valley, Fountain City, and Halls usually allow the curb. A Farragut covenant moves the handoff to the entrance."),
 ("Do you ship cars for the laboratory in Oak Ridge or the power authority?","Yes, in every season. The laboratory and the weapons plant relocate scientists on program schedules and clearance timelines. The power authority relocates engineers on start dates. The handoff happens at the lots in Oak Ridge or at a garage entrance downtown. If the employer covers the shipment, we put it in writing however it needs."),
 ("Is the gorge on Interstate 40 open for my Carolina shipment?","It has run with restrictions since the 2024 hurricane tore it out at the state line. A carrier headed to Asheville or Charlotte plans for it, and some ride 81 and 26 around it. The detour adds an hour and a few dollars. We tell you which way the truck is going."),
 ("What happens if an ice storm hits on my pickup day?","The truck waits in Nashville or Chattanooga until the salt trucks finish, usually a day. The February 2015 storms and the January 2024 snow each closed the hills for most of a week. We call the moment the forecast turns. The pickup moves to the first clear morning, and the figure stays where it was."),
 ("Can you ship a car to or from Maryville, Oak Ridge, or Gatlinburg?","Yes. Alcoa, Maryville, Oak Ridge, Farragut, and Seymour ride the same carriers and price the same as Knoxville. Lenoir City and Clinton do too. Sevierville adds an hour in October when the Smokies traffic fills 441. Gatlinburg adds the parkway and a figure. The handoff there happens on the parkway or in Sevierville."),
 ("Can you ship a car that does not run from Knoxville?","Yes. The carrier comes with a winch, and the figure includes the loading time. The lots off Kingston Pike and the mall lots in West Knoxville are flat. Tell us if it rolls, steers, and brakes."),
 ("What do you need for a Knoxville car shipping quote?","Both addresses, with the neighborhood. The year, make, and model, and whether it runs. Open or enclosed, and the week around the move-in or the start date. With those, the Knoxville figure comes back the same day."),
]
BODY.append(faq_section(FAQ,'Knoxville FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Knoxville?','Two minutes on the form above puts a Knoxville figure on your lane. Name the neighborhood and the week, and a carrier already on 40 takes it.','+18653904490','(865) 390-4490','Get your free Knoxville quote'))

build({
 'slug':'auto-transport-knoxville-tennessee',
 'title':'Car Shipping in Knoxville, TN — Auto Transport | Ship Guy',
 'meta':'Car shipping in Knoxville, TN, where Interstates 40 and 75 share the road. University of Tennessee move-in dates and football Saturdays, the power authority, the laboratory in Oak Ridge, hospital and plant hires, main-road handoffs for the Fort, Sequoyah Hills, and downtown, curbside pickups in Bearden, Farragut, Hardin Valley, and Fountain City, the ice, and the gorge. Local office on Gay Street downtown. Free quote.',
 'h1':'Car Shipping in<br>Knoxville, <span class="accent">Tennessee</span>',
 'lede':'Open, enclosed, and expedited auto transport across Knoxville, Knox County, and the Tennessee Valley, planned around 40 and 75, the campus dates, the football Saturdays, the Smokies traffic, the ice, and the gorge.',
 'tel':'+18653904490','disp':'(865) 390-4490','brand':'Knoxville','keyword':'car shipping in knoxville',
 'localterms':['knoxville','interstate 40','interstate 75','640','275','140','pellissippi','alcoa highway','kingston pike','henley','broadway','chapman highway','441','cumberland','the strip','neyland drive','summit hill','jackson avenue','gay street','market square','old city','100 block','theaters','civic coliseum','power authority','twin towers','downtown','the fort','student rentals','fourth and gill','old north knoxville','happy holler','sequoyah hills','boulevards','low limbs','bearden','west hills','cedar bluff','farragut','covenants','hardin valley','karns','fountain city','halls','powell','south knoxville','island home','vestal','east knoxville','holston hills','burlington','alcoa','maryville','oak ridge','seymour','lenoir city','clinton','sevierville','gatlinburg','smokies','parkway','river','hills','hollows','university','forty thousand','students','stadium','hundred thousand','boats','laboratory','weapons plant','scientists','clearance','hospital systems','medical center','residents','traveling nurses','auto-parts plant','manufactured-home builder','aluminum mill','truck-stop chain','headquarters','guard','tanker wing','airmen','orders','airport','retirees','lakes','foothills','midwest','florida','football saturdays','move-in','fall traffic','fair','chilhowee park','dogwood festival','festivals','february 2015','ice storms','january 2024','nine inches','salt trucks','february 2019','wettest february','creeks','2016 fire','fourteen people','2024 hurricane','gorge','pigeon river','state line','restrictions','fog','tornado watch','humidity','rebuilt','2009','fourteen months','papermill','lovell road','merchant drive','strawberry plains','mall','fairgrounds','fly-and-ship','chattanooga','asheville','nashville','lexington','atlanta','charlotte','cincinnati','louisville','memphis','orlando','81','26','pollen','brine','hail','bill of lading','fmcsa','winch'],
}, BODY, FAQ)
