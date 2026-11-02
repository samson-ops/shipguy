import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("3–6 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Bismarck, North Dakota','Car shipping in the capital on the Missouri, where 94 crosses the river and the gates come down in a blizzard',
 ['Car shipping in Bismarck rides Interstate 94, the one road the cross-state carriers use between Fargo and Montana. Ship Guy is a licensed auto transport broker with an office on East Main Avenue downtown.',
  'We book vetted carriers across Bismarck and Mandan, from the Cathedral District to the north subdivisions. The carriers own the trucks. Ship Guy holds the license and the bond.',
  'Interstate 94 runs along the north side of the city and crosses the river to Mandan. US 83 is State Street, and it runs north to Minot and south to the Standing Rock country. The Expressway loops the south and east sides, and Main Avenue crosses the river on the Memorial Bridge.',
  'This page covers 94, 83, the Expressway, downtown, the Cathedral District, the north, and the river blocks. It also covers the Capitol, the hospitals, the energy companies, the plants, the gates, and the floods.'],
 'Bismarck at a glance',
 ['Most pickups happen within 3 to 6 days. North Dakota is a pass-through market. A carrier on 94 adds a Bismarck stop when the load lines up. A week of dates gets the next truck through.',
  'Minot and Fargo are a day on the truck. Minneapolis takes one to two. Billings, Sioux Falls, Great Falls, and Omaha take two. Denver and Chicago take three, and Seattle takes four.'],
 'Tell us the neighborhood and whether the street has been plowed. Downtown, the Cathedral District, and the river blocks meet the truck at a lot. Highland Acres, the north subdivisions, Lincoln, and Mandan usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 94, US 83, the Expressway, State Street, Main Avenue, Century Avenue, 43rd Avenue, and the Two Bridges',
 prose(
  L('Bismarck is a grid on the east bank with its capital on a hill. A carrier sees the whole city from the 94 and 83 interchange.'),
  P('Interstate 94 is the Minneapolis-to-Montana road. It enters from Jamestown and Fargo and runs along the north side past State Street. Then it crosses the river to Mandan. It leaves west for Dickinson, the Bakken turnoff, and Montana. The state drops the gates on 94 at the city limits in a blizzard. Nothing moves until they lift.'),
  P('US 83 is State Street, the main road north and south. It climbs past the Capitol to Century Avenue and 43rd and leaves for Washburn and Minot. South of the Expressway it heads for Linton and the Standing Rock country. The Bismarck Expressway loops the south and east sides from the river to 94. Main Avenue runs through downtown and crosses to Mandan on the Memorial Bridge. Washington Street and Century Avenue carry the rest.'),
  P('The carriers come off 94 at State Street or the Expressway. The mall lots on Century Avenue are the usual meeting spot. The big-box lots on State Street and the Capitol lots on a weekend work too. So do the fairgrounds lots in Mandan. The airport lots work for a fly-and-ship.'),
  P('Our office is on East Main Avenue downtown, two blocks east of the old depot.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the Cathedral District, the Capitol, Highland Acres, the North, Southport, the River Blocks, Lincoln, and Mandan',
 prose(
  L('Bismarck is an old railroad town by the river with a new city spreading north across the prairie. The truck reaches most of it.'),
  P('Downtown runs along Main Avenue and Fourth Street, brick blocks with angled parking. The old depot anchors the east end. The driver meets you at the lots by the Civic Center or on Main. The Cathedral District climbs from downtown toward the Capitol. The oldest houses in the city sit on narrow streets under elms. The handoff moves to State Street or the Capitol lots.'),
  P('The Capitol grounds and the tower sit on the hill, with state office blocks around them. Highland Acres to the west is a postwar grid where the curb works. The north from Century Avenue past 43rd is the new city, wide subdivisions on former wheat fields. The streets outrun the carrier maps, so send the full address. The curb works everywhere up there.'),
  P('Southport and the river blocks south of the Expressway sit on the Missouri flood plain. Fox Island and Riverwood went under in 2011, and the levees have grown since. The handoff moves up to the Expressway in a wet spring. Lincoln to the southeast and the airport blocks are wide and reachable. The university on the bluffs south of town meets the truck in its lots.'),
  P('Mandan across the river is its own city with the refinery, the rail yard, and Old Red Trail. The older blocks near the yard are tight, and the newer ones to the north are wide. Fort Lincoln down 1806 and the river towns ship with the same trucks. Washburn, Wilton, and the coal towns up 83 add an hour. All of them price the same as Bismarck.'),
 )))

ROUTES=[("Minot, ND","US-83 · ~110 mi","1 day","$200–$310"),("Fargo, ND","I-94 · ~195 mi","1 day","$220–$340"),
 ("Billings, MT","I-94 · ~410 mi","2 days","$380–$540"),("Minneapolis, MN","I-94 · ~430 mi","1–2 days","$400–$570"),
 ("Sioux Falls, SD","I-94/I-29 · ~440 mi","2 days","$400–$570"),("Great Falls, MT","I-94/MT-200 · ~580 mi","2 days","$450–$650"),
 ("Omaha, NE","I-94/I-29 · ~620 mi","2 days","$460–$660"),("Denver, CO","US-85/I-25 · ~700 mi","3 days","$520–$750"),
 ("Chicago, IL","I-94 · ~830 mi","3 days","$580–$830"),("Seattle, WA","I-94/I-90 · ~1,200 mi","4 days","$800–$1,150")]
BODY.append(rate_table('Lanes &amp; Costs','Bismarck Car Shipping Lanes and Estimated Costs',
 'The lanes central North Dakota cars run most, with estimated open-trailer ranges. Your own route gets a number on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Bismarck, running sedan, open trailer. Add about 10 to 25 percent for an SUV or a pickup, and more again for enclosed. Your week of dates and the trucks crossing 94 that week decide the real figure.',
 prose(
  P('Bismarck prices like a stop halfway across 94, because that is what the carriers see. The Fargo and Minneapolis lanes ride 94 east and fill every week. The Billings and Seattle lanes ride it west. The Denver lane drops down 85 through the Black Hills. The Arizona lane fills each October with the state’s snowbirds.'),
  P('A session start in January or the August move-in lands in a busy week. The <a href="car-shipping-cost.html">cost guide</a> walks through what size, condition, and the date range do to the number.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Capitol, the Hospitals, the Energy Companies, the Loader Plant, the Refinery, the Colleges, and the Guard',
 prose(
  L('Bismarck relocates state employees, nurses, engineers, and students. The Capitol and the hospitals move the most.'),
  P('State government fills the tower and the blocks around it. The agencies transfer staff on start dates all year. The legislature brings a crowd to town each odd January. Every fourth January a new governor brings in a class of appointees. When the state or an employer picks up the cost, we produce the receipts.'),
  P('The two hospitals, one on the north side and one by the Capitol, hire traveling nurses year round. Residents arrive each June. The utility holding company and the electric cooperative headquartered here move engineers on project dates. So do the coal plants and the mines an hour up 83. The loader plant on the north side moves managers on production dates. The refinery in Mandan does the same. The second car usually rides a trailer.'),
  P('The college on Schafer Street takes student cars in late August. The university on the bluffs does the same. Both send them home in May. The parent books it by phone, and an adult signs at the lot. The Guard headquarters at Fraine Barracks rotates staff on orders. The Air Force base in Minot sends families south the same way. Ship Guy is a private broker with no connection to either. The <a href="military-car-shipping.html">military</a> page explains the timing around orders.'),
  P('Oil workers ship pickups to and from the Bakken on the hiring cycle. Many of them live in Bismarck. Each October the retirees head for Arizona, and each April they come back. The paperwork for crossing state lines is on the <a href="state-to-state-car-shipping.html">state-to-state</a> page.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Session, the Powwow, the Street Fair, Move-In Week, the Blizzards, the Gates, the Ice Jams, and the River',
 prose(
  L('Bismarck runs on a legislative calendar and a river calendar. The gates on 94 decide whether a truck moves at all.'),
  P('The legislature meets from January into April in odd years, and the Capitol blocks fill with cars. The powwow at the tribal college fills the south side for a weekend in September. The street fair closes downtown for a weekend the same month. The marathon closes the river roads on a Saturday. Move-in week in late August fills the college blocks. Pheasant season in October fills every hotel in the state.'),
  P('Winter brings fifty inches of snow and wind chills of forty below. A blizzard on the open prairie closes 94 for a day at a time. The state drops the gates at the city limits. No carrier moves until the gates lift. The October 2019 storm dropped seventeen inches before the leaves were off the trees. A car on a street that has not been plowed gets stuck or towed. We tell you to use the driveway or a lot before the truck comes.'),
  P('Winter oil and a block heater go in before a car from the south spends a night here. An electric car wants half a charge on arrival, since the cold eats the rest. The handoff happens in a plowed lot, never on a drifted street. A winter pickup can lose a day or two, and you hear it from us first.'),
  P('The Missouri floods when the dam upstream releases in a wet spring. In 2011 it came over the levees and emptied Fox Island, Southport, and Riverwood for a month. In 2009 an ice jam backed the river into the same blocks until the state broke it up. A pickup on the river blocks moves up to the Expressway until the water drops. Summer brings hail and the odd tornado warning, which shift the loading hour and nothing more.'),
 )+chips(["Downtown","Main Avenue","Civic Center","Cathedral District","Capitol","Highland Acres","North Bismarck","Century Avenue","43rd Avenue","Hay Creek","Northridge","Southport","Fox Island","Riverwood","Lincoln","Airport","Schafer Street","University of Mary","Mandan","Old Red Trail","Fort Lincoln","Washburn","Wilton","Hazen","Beulah","Jamestown","Dickinson","Minot","Williston"])
 +NOTE('Serving Bismarck, Mandan, and the whole middle of the state, Cathedral District block or north cul-de-sac. Tell us the neighborhood and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Bismarck?',
 prose(
  L('Nearly every Bismarck car travels on an open trailer, and the table above is priced for one.'),
  P('An enclosed trailer keeps off six months of salt, sand, and gravel. The collectors in the Cathedral District book one. So do the executives bringing a new car to the energy headquarters. Snowbirds sending a car south before the first blizzard often choose enclosed as well.'),
  P('A commuter car or a student car needs nothing more than an open trailer. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain where the line falls.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A number, a lot on Century Avenue, and a signature at delivery. The week of dates decides which truck.'),
  P('Approve the price, and we watch for a carrier crossing on 94 that week. The lot and the window are confirmed once one commits. At pickup the driver inspects the car with you and writes its condition on the Bill of Lading. You sign the sheet, and delivery is judged against it.'),
 )+ULI([
  "Your belongings out of the car, trunk and console included",
  "Gas at about a quarter tank",
  "Photos of each side and the odometer, taken the morning of pickup",
  "A key the driver can use, and a note about anything that sticks",
  "Add-on alarm switched off",
  "Downtown, in the Cathedral District, or on the river blocks, plan on a lot",
 ])+prose(P('Read the <a href="how-it-works.html">how it works</a> page for the order of events and the <a href="car-shipping-preparation.html">preparation</a> page for the checklist.'))))

BODY.append(sec('Why Ship Guy','Why Bismarck Drivers Choose Ship Guy',
 prose(
  L('We know which carriers cross on 94 each week and when the gates are likely to come down.'),
  P('Anyone can find our FMCSA license and our $75,000 bond on the federal register. The office is on East Main Avenue downtown.'),
  P('The same coordinator answers from the quote to the delivery call. The <a href="services.html">services</a> page compares open, enclosed, and expedited.'),
 )))

BODY.append(office('Bismarck','630 E Main Ave #592','Bismarck, ND 58501','+17016994053','(701) 699-4053','CT',
 '630+E+Main+Ave+%23592,+Bismarck,+ND+58501','Visit Us','Find Ship Guy in Bismarck',
 'Our office is on East Main Avenue downtown, two blocks east of the old depot.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4171.075921205562!2d-100.7823747!3d46.8055938!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x52d7837058886db7%3A0xe5cc4638f178d01!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793300383277!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Bismarck to Minneapolis or Denver?","Minneapolis runs four hundred to five hundred seventy dollars for a sedan. That is about four hundred thirty miles down 94. Denver runs five hundred twenty to seven hundred fifty, about seven hundred miles down 85 and 25. Minot and Fargo are a day away and cost the least. Add about 10 to 25 percent for an SUV or a pickup."),
 ("Why does a Bismarck pickup take 3 to 6 days?","Because North Dakota is a pass-through market. The carriers cross on 94 between Minneapolis and Montana. One adds a Bismarck stop when the load lines up. A week of dates lets us put the car on the next one through. A single fixed date can sit and wait."),
 ("Can the carrier come to my street in the Cathedral District or north of 43rd?","North of 43rd, yes. The subdivisions up there are wide, and the curb works on every block. The Cathedral District, usually not. The streets are narrow and the elms hang low. The driver meets you on State Street or at the Capitol lots."),
 ("Do you ship cars for state employees and the hospitals?","Yes, every week. The agencies transfer staff on start dates all year, and the legislature brings a crowd each odd January. The hospitals bring residents each June and hire traveling nurses year round. If the state or an employer is reimbursing the move, we produce the receipts."),
 ("Can you deliver on a Bismarck State or University of Mary move-in date?","Yes. Both take cars in late August and send them home in May. The parent books it by phone, and an adult signs at the lot. The college blocks are full that week, so the meeting point is the mall lots on Century Avenue. Give us a range around the date."),
 ("Can you ship a car to or from Mandan, Minot, or Williston?","Yes. Mandan prices the same as Bismarck and rides the same trucks across the river. Minot is two hours up 83 and prices a shade higher. Williston and the Bakken take 4 to 8 days, and the handoff is in town. Send the full address for a new subdivision."),
 ("What happens if the gates come down on 94 on my pickup day?","Nothing moves until they lift. The state closes 94 at the city limits in a blizzard. A carrier waits in Fargo or Dickinson. A closure usually lasts a day, and the truck arrives a day or two late. We tell you before the driver does. Park in the driveway and leave the block heater plugged in."),
 ("What happens if the river floods?","The handoff moves up the hill. Fox Island, Southport, and Riverwood sit on the flood plain. The dam releases can put them under in a wet spring. A pickup on those blocks meets the truck on the Expressway until the water drops. The rest of the city sits well above the river."),
 ("Can you ship a car that does not run from Bismarck?","Yes. The quote covers a winch-equipped carrier and the loading time from the start. On 94 that means fewer trucks can take the stop, so give us room on the dates. The mall lots on Century Avenue are level. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Bismarck car shipping quote?","Where the car is and where it goes, with the neighborhood or the town. Year, make, and model. Running or not. Open or enclosed. The widest week of dates you can live with. Answer those, and the Bismarck number is in your inbox the same day."),
]
BODY.append(faq_section(FAQ,'Bismarck FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Bismarck?','Two minutes on the form above, and a Bismarck number is on its way. Tell us the neighborhood and a week of dates, and we flag the next carrier crossing on 94.','+17016994053','(701) 699-4053','Get your free Bismarck quote'))

build({
 'slug':'auto-transport-bismarck-north-dakota',
 'title':'Car Shipping in Bismarck, ND — Auto Transport | Ship Guy',
 'meta':'Car shipping in Bismarck, ND, the capital on the Missouri where Interstate 94 crosses the river. Honest 3 to 6 day windows, Capitol and hospital relocations, lot handoffs for downtown and the Cathedral District, curbside pickups in Highland Acres, the north subdivisions, Lincoln, and Mandan, the blizzard gates, and the river. Local office on East Main Avenue downtown. Free quote.',
 'h1':'Car Shipping in<br>Bismarck, <span class="accent">North Dakota</span>',
 'lede':'Open, enclosed, and expedited auto transport across Bismarck and Mandan, planned around 94, the Capitol calendar, the gates, the river, and the honest windows of a pass-through market.',
 'tel':'+17016994053','disp':'(701) 699-4053','brand':'Bismarck','keyword':'car shipping in bismarck',
 'localterms':['bismarck','capital','missouri','interstate 94','gates','blizzard','fargo','montana','east main avenue','downtown','mandan','cathedral district','north subdivisions','river','us 83','state street','minot','standing rock','expressway','main avenue','memorial bridge','bridges','capitol','hospitals','energy','loader plant','refinery','floods','pass-through','minneapolis','billings','sioux falls','great falls','omaha','denver','chicago','seattle','plowed','highland acres','lincoln','jamestown','airport','dickinson','bakken','century avenue','43rd avenue','washburn','coal plants','linton','washington street','mall','big-box','fairgrounds','fly-and-ship','fourth street','angled parking','depot','civic center','elms','tower','wheat fields','southport','fox island','riverwood','2011','levees','university','bluffs','rail yard','old red trail','fort lincoln','1806','wilton','snowbirds','black hills','session','legislature','odd january','appointee','traveling nurses','residents','utility holding company','electric cooperative','project dates','mines','production dates','schafer street','fraine barracks','air force base','oil workers','pickups','hiring cycle','retirees','arizona','powwow','tribal college','street fair','marathon','pheasant season','fifty inches','forty below','october 2019','seventeen inches','towed','block heater','electric car','dam','ice jam','2009','hail','tornado','salt','sand','gravel','bill of lading','fmcsa','hay creek','northridge','hazen','beulah','williston','winch','console'],
}, BODY, FAQ)
