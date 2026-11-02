import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("3–6 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Missoula, Montana','Car shipping in the hub of five valleys, on the Seattle-to-Chicago road',
 ['Car shipping in Missoula rides Interstate 90, the one road every cross-country carrier in Montana uses. Ship Guy is a licensed auto transport broker with an office on Great Northern Loop off West Broadway.',
  'We arrange vetted carriers across Missoula and the valley, from the Rattlesnake to Lolo and Frenchtown. The carriers own the trucks. Ship Guy holds the license and the bond.',
  'Interstate 90 runs through the city from Lookout Pass on the Idaho line to Butte and Billings. US 93 comes up the Bitterroot from Hamilton and leaves north for the Flathead. US 12 climbs Lolo Pass into Idaho, and Highway 200 follows the Blackfoot toward Great Falls.',
  'This page covers 90, 93, the passes, Reserve Street, the university, the old neighborhoods, and the valley towns. It also covers the Forest Service, the hospitals, the smokejumpers, the inversions, the fires, and the lanes.'],
 'Missoula at a glance',
 ['Most pickups happen within 3 to 6 days. Montana is a pass-through market, and a carrier adds a Missoula stop when the load lines up. A wide date range is the biggest help you can give us.',
  'Spokane and Billings are a day on the truck. Seattle, Boise, and Salt Lake City take one to two. Portland takes two, Denver and Fargo two to three, and Phoenix three.'],
 'Tell us the neighborhood and the nearest highway. The Rattlesnake, the University District, and the Northside meet the truck at a lot on Reserve or Brooks. Target Range, Miller Creek, Lolo, and Frenchtown usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 90, US 93, US 12, Highway 200, Reserve Street, Brooks, Broadway, and the Passes',
 prose(
  L('Missoula sits where the Bitterroot and the Blackfoot meet the Clark Fork. Every road into the valley follows a river.'),
  P('Interstate 90 is the Seattle-to-Chicago road. It enters the valley from the west past Frenchtown and the airport and leaves east through Hellgate Canyon. Lookout Pass sits a hundred miles west on the Idaho line, with a chain-up area at the top. Homestake Pass sits east of Butte on the Continental Divide. Both close for a few hours in a bad storm, and a carrier waits them out. The exits that matter are Reserve Street, Orange Street, Van Buren, and East Missoula.'),
  P('US 93 comes up the Bitterroot from Hamilton and Lolo as a wide four-lane road. It crosses the city as Reserve Street and leaves north for Arlee, Polson, and the Flathead. US 12 climbs Lolo Pass into Idaho, a hundred miles of curves with no services. Most carriers avoid it. Highway 200 follows the Blackfoot from Bonner over Rogers Pass to Great Falls. Brooks Street runs diagonally from downtown to Reserve, and Broadway runs east and west along the river.'),
  P('The carriers come off 90 at Reserve Street. The big-box lots on North Reserve and the mall lots on Brooks are the usual meeting spots. The fairgrounds lots on South Avenue work outside fair week. The Southgate lots work most days, and the airport lots work for a fly-and-ship.'),
  P('Our office is on Great Northern Loop off West Broadway, west of Reserve Street and minutes from 90.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the Rattlesnake, the University District, the Slant Streets, the Northside, the South Hills, Miller Creek, Target Range, and the Valley Towns',
 prose(
  L('Missoula is an old railroad town with narrow streets near the river and new subdivisions climbing every hillside. The truck meets the old blocks at the edge.'),
  P('Downtown sits between the river and the tracks, with Higgins Avenue as the main street. The blocks are short, the alleys are tight, and the parking is angled. The driver meets you at the lots by the depot or on Broadway. The Northside and the Westside across the tracks are small houses on narrow streets. The handoff moves to the lots on North Reserve.'),
  P('The Rattlesnake runs up the creek north of downtown, a mile of old houses and then new ones. The streets narrow as they climb, and the upper valley has no turnaround for a trailer. The driver meets you at the lower end or on Broadway. The University District east of Higgins is tree-lined blocks packed with student cars. Move-in week fills every inch. The handoff moves to the Adams Center lots or Brooks Street.'),
  P('The Slant Streets run diagonally between Higgins and Brooks, old houses on blocks the grid never agreed with. The driver meets you on Brooks or South Avenue. Rose Park, Franklin to the Fort, and the blocks around the fairgrounds are the same. The South Hills and Pattee Canyon climb above them, steep streets with switchbacks. The handoff moves to the bottom of the hill.'),
  P('Miller Creek and Linda Vista to the south are wide new subdivisions where the curb works. Target Range, Orchard Homes, and the Mullan Road corridor to the west are the same. A flood plain sits under them. Grant Creek to the north is wide and reachable. Lolo, Florence, and Stevensville down the Bitterroot ship with the same trucks. So do Frenchtown and Huson to the west and Bonner and Clinton to the east. All of them price the same as Missoula.'),
 )))

ROUTES=[("Spokane, WA","I-90 · ~200 mi","1 day","$230–$350"),("Billings, MT","I-90 · ~340 mi","1 day","$320–$460"),
 ("Boise, ID","I-90/US-95 · ~550 mi","1–2 days","$450–$640"),("Seattle, WA","I-90 · ~480 mi","1–2 days","$400–$570"),
 ("Salt Lake City, UT","I-90/I-15 · ~520 mi","1–2 days","$450–$650"),("Portland, OR","I-90/I-84 · ~560 mi","2 days","$460–$660"),
 ("Denver, CO","I-90/I-25 · ~900 mi","2–3 days","$650–$920"),("Fargo, ND","I-90/I-94 · ~960 mi","2–3 days","$680–$960"),
 ("Phoenix, AZ","I-15/US-93 · ~1,200 mi","3 days","$900–$1,250"),("Chicago, IL","I-90 · ~1,550 mi","3–4 days","$1,000–$1,400")]
BODY.append(rate_table('Lanes &amp; Costs','Missoula Car Shipping Lanes and Estimated Costs',
 'The lanes western Montana cars run most, with estimated open-trailer ranges. Your own route gets a number on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Missoula for a running sedan on an open trailer. Plan on 10 to 25 percent more for an SUV or a pickup, and more for enclosed. On a pass-through corridor the date range and the trucks crossing that week set the real quote.',
 prose(
  P('Missoula prices like a stop on the Seattle-to-Chicago road, because that is what it is. The Spokane and Seattle lanes ride 90 west and fill every week. The Salt Lake lane rides 90 east to Butte and 15 south. The Denver lane rides 90 to Billings and 25 south. The Arizona lane fills each October with the valley’s snowbirds.'),
  P('A move-in week in August or a Griz home Saturday lands in the busiest days of the year. The <a href="car-shipping-cost.html">cost guide</a> explains how size, condition, and the date range change the number.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The University, the Forest Service, the Hospitals, the Smokejumpers, and the Snowbirds',
 prose(
  L('Missoula relocates professors, rangers, nurses, firefighters, and students. The university and the Forest Service move the most.'),
  P('The university on the river is the largest employer in the city. Faculty arrive on contract dates over the summer, and researchers arrive on grant dates all year. The campus takes student cars in late August and sends them home in May. A parent sets the booking up by phone, and an adult meets the truck to sign. Campus streets are packed that week, so the meeting point is the Adams Center lots or Brooks Street.'),
  P('The Forest Service runs its Northern Region from Fort Missoula and its fire lab out by the airport. Rangers and scientists transfer in on federal start dates. The smokejumper base at the airport hires each spring. The two hospitals, downtown on Broadway and south on Fort Missoula Road, hire traveling nurses year round. Residents arrive each June. If an employer is paying for the move, the paperwork comes from us.'),
  P('The railroad, the trucking companies, and the timber mills moved managers here for a century. Remote workers who found the valley in 2020 ship a car in from Seattle or the Bay Area. Retirees leave for Arizona each October and come back in April. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate paperwork.'),
  P('Malmstrom in Great Falls sends airmen through the valley on orders. The Guard trains at Fort Harrison in Helena. Ship Guy is a private broker with no connection to either. The timing around orders is explained on the <a href="military-car-shipping.html">military</a> page.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Griz Saturdays, Move-In Week, the Fair, the Marathon, the Inversions, the Fires, and the Spring Runoff',
 prose(
  L('Missoula runs on a football calendar and a fire calendar. The weather closes a pass more often than it closes the city.'),
  P('Griz home games fill the stadium by the river on fall Saturdays. Game traffic fills Arthur Avenue, Van Buren, and the Madison Street bridge for hours. A handoff near campus moves to Friday or Sunday. The Cat-Griz game every other November is the worst of them. Move-in week in late August fills the University District. The fairgrounds fill for the Western Montana Fair the same month. The marathon closes Higgins and the downtown bridges on a Sunday in late June.'),
  P('Winter brings forty inches of snow and the inversions. Cold air pools in the valley for days, and the fog freezes on every windshield. The streets are plowed, but Lookout Pass and Homestake Pass close for hours in a storm. The carriers wait them out in Spokane or Butte rather than chain up. A winter pickup can lose a day, and you hear it from us before the driver does.'),
  P('August brings the fires. In 2017 the Lolo Peak fire closed US 12 and sent part of Lolo out of town. The smoke sat in the valley for a month. A fire closure on 90 is rare and short. A fire closure on 93 or 12 reroutes a carrier by a day. The driver meets you where the smoke allows and the road is open.'),
  P('The rivers rise with the snowmelt in May. In 2018 the Clark Fork rose higher than it had in decades. Orchard Homes, Tower Street, and the low blocks of the Rattlesnake flooded for weeks. A pickup on the flood plain moves up to Reserve Street until the water drops. Summer hail dents a car in a parking lot, and an enclosed trailer avoids it.'),
 )+chips(["Downtown","Higgins Avenue","Hip Strip","Rattlesnake","Lower Rattlesnake","University District","Slant Streets","Rose Park","Franklin to the Fort","Northside","Westside","South Hills","Pattee Canyon","Farviews","Miller Creek","Linda Vista","Target Range","Orchard Homes","Mullan Road","Grant Creek","East Missoula","Bonner","Milltown","Clinton","Lolo","Florence","Stevensville","Frenchtown","Huson","Hamilton","Seeley Lake"])
 +NOTE('Serving Missoula and the whole valley, Rattlesnake block or Bitterroot cul-de-sac. Tell us the neighborhood and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Missoula?',
 prose(
  L('Nearly every valley car rides an open trailer, and the lane table above is priced that way.'),
  P('An enclosed trailer keeps off the gravel of the passes and the de-icer the state sprays on 90. The collectors in the Rattlesnake and the retirees sending a new car to Arizona book one. A car coming in from Seattle ahead of the first snow often rides enclosed too.'),
  P('A commuter car or a student car rides open without a second look. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages lay the two side by side.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A number, a lot on Reserve Street, and a signature at delivery. The date range picks the truck.'),
  P('Approve the price, and we watch for a carrier crossing on 90 that week. The lot and the window are confirmed as soon as one commits. At pickup the driver walks the car with you and writes every mark on the Bill of Lading. You sign it, and the delivery inspection is checked against it.'),
 )+ULI([
  "Everything that is yours out of the car, trunk included",
  "Fuel at a quarter tank, no more",
  "Your own photos of each side and the mileage before the truck comes",
  "A key that works, and a word about anything that sticks",
  "Aftermarket alarm switched off",
  "In the Rattlesnake, the University District, or downtown, plan on a lot",
 ])+prose(P('The order of events is on the <a href="how-it-works.html">how it works</a> page. The full checklist is on the <a href="car-shipping-preparation.html">preparation</a> page.'))))

BODY.append(sec('Why Ship Guy','Why Missoula Drivers Choose Ship Guy',
 prose(
  L('We know which carriers cross on 90 each week and which passes they will not chain up for.'),
  P('Our FMCSA license and our $75,000 bond are on the federal register, where anyone can check them. The office is on Great Northern Loop off West Broadway.'),
  P('One coordinator takes the move from the first call to the delivery photo. The <a href="services.html">services</a> page compares open, enclosed, and expedited.'),
 )))

BODY.append(office('Missoula','2829 Great Northern Loop #951','Missoula, MT 59808','+14067976768','(406) 797-6768','MT',
 '2829+Great+Northern+Loop+%23951,+Missoula,+MT+59808','Visit Us','Find Ship Guy in Missoula',
 'Our office is on Great Northern Loop off West Broadway, west of Reserve Street and minutes from 90.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4164.9888356722895!2d-114.0330711!3d46.884047699999996!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x535dcf48c85f6d89%3A0x4a467f587b166248!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793293166690!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Missoula to Seattle or Phoenix?","Seattle runs four hundred to five hundred seventy dollars for a sedan. That is about four hundred eighty miles west on 90. Phoenix runs nine hundred to twelve hundred fifty, about twelve hundred miles down 15. Spokane is two hundred miles and the lowest lane of all. An SUV or a pickup adds 10 to 25 percent."),
 ("Why does a Missoula pickup take 3 to 6 days?","Because Montana is a pass-through market. The carriers cross on 90 between Seattle and the Midwest. One adds a Missoula stop when the load lines up. A date range of a week gets the next truck through. A single fixed date can wait for one."),
 ("Can the carrier come to my street in the Rattlesnake or the University District?","Usually not. The Rattlesnake narrows as it climbs, and the upper valley has nowhere to turn a trailer. The University District is packed with student cars. The driver meets you on Broadway, at the Adams Center lots, or on Brooks Street. Miller Creek, Target Range, Lolo, and Frenchtown usually allow the curb."),
 ("Do you ship cars for the university and the Forest Service?","Yes, every month. Faculty arrive on contract dates over the summer, and rangers transfer on federal start dates. The hospitals hire traveling nurses year round and bring residents each June. If an employer is paying for the move, the paperwork comes from us."),
 ("Can you deliver on the University of Montana move-in date?","Yes. The campus takes student cars in late August and sends them home in May. A parent sets the booking up by phone, and an adult meets the truck to sign. Campus streets are packed that week, so the meeting point is the Adams Center lots. The window moves with the date, so give us a range."),
 ("Can you ship a car to or from Lolo, Hamilton, or the Flathead?","Yes. Lolo, Florence, and Stevensville price the same as Missoula and ride the same trucks. Hamilton adds an hour down 93 and a day of waiting. Kalispell, Whitefish, and Polson take 5 to 10 days. A carrier leaves 90 only for a full load. The handoff up there is in town or on the highway."),
 ("What happens if Lookout Pass or Homestake Pass closes on my pickup day?","The carrier waits it out in Spokane or Butte rather than chain up. A pass closure usually lasts hours, not days, and the truck arrives a day late. We tell you before the driver does. A Salt Lake car rides 15 south from Butte and never touches Homestake."),
 ("Does Griz football or move-in week affect my pickup?","Yes, near campus. Home Saturdays fill Arthur Avenue, Van Buren, and the Madison Street bridge with game traffic. Move-in week in late August fills the University District. A handoff in that corner of the city moves to a weekday or to Brooks Street. The rest of the valley barely notices."),
 ("Can you ship a car that does not run from Missoula?","Yes. A carrier with a winch takes it, and the loading time is in the number from the start. On a pass-through road that also narrows which trucks can stop. The Southgate lots or the lots on North Reserve give the driver level ground. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Missoula car shipping quote?","The two addresses, with the neighborhood or the valley town. The year, make, and model. Whether it runs. Open or enclosed. The widest date range you can live with. Those five answers get a Missoula number back the same day."),
]
BODY.append(faq_section(FAQ,'Missoula FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Missoula?','The form above takes two minutes, and a Missoula number comes back with it. Give us the neighborhood and a date range, and we catch the next carrier crossing on 90.','+14067976768','(406) 797-6768','Get your free Missoula quote'))

build({
 'slug':'auto-transport-missoula-montana',
 'title':'Car Shipping in Missoula, MT — Auto Transport | Ship Guy',
 'meta':'Car shipping in Missoula, MT, the valley on Interstate 90 where the Seattle-to-Chicago carriers cross. Honest 3 to 6 day windows, University of Montana move-in timing, Forest Service and hospital relocations, lot handoffs for the Rattlesnake and the University District, curbside pickups in Miller Creek, Target Range, Lolo, and Frenchtown, the passes, the inversions, and the fire season. Local office on Great Northern Loop off West Broadway. Free quote.',
 'h1':'Car Shipping in<br>Missoula, <span class="accent">Montana</span>',
 'lede':'Open, enclosed, and expedited auto transport across the Missoula valley, planned around 90, the passes, the Griz calendar, the fire season, and the honest windows of a pass-through market.',
 'tel':'+14067976768','disp':'(406) 797-6768','brand':'Missoula','keyword':'car shipping in missoula',
 'localterms':['missoula','interstate 90','great northern loop','west broadway','rattlesnake','lolo','frenchtown','lookout pass','butte','billings','us 93','bitterroot','hamilton','flathead','us 12','lolo pass','highway 200','blackfoot','great falls','reserve street','university','forest service','hospitals','smokejumpers','griz','inversions','fires','pass-through','spokane','seattle','boise','salt lake city','denver','portland','fargo','phoenix','northside','brooks','target range','miller creek','clark fork','hellgate canyon','airport','chain-up','homestake pass','continental divide','orange street','van buren','east missoula','arlee','polson','rogers pass','bonner','higgins','depot','westside','adams center','slant streets','rose park','franklin to the fort','fairgrounds','south hills','pattee canyon','linda vista','orchard homes','mullan road','grant creek','florence','stevensville','huson','clinton','southgate','fly-and-ship','contract dates','grant dates','late august','fort missoula','fire lab','rangers','traveling nurses','residents','railroad','timber','madison street','remote workers','snowbirds','arizona','malmstrom','fort harrison','helena','cat-griz','western montana fair','marathon','forty inches','fog','chain up','lolo peak','2017','smoke','snowmelt','2018','tower street','hail','de-icer','bill of lading','fmcsa','hip strip','farviews','milltown','seeley lake','kalispell','whitefish','arthur avenue','winch','date range'],
}, BODY, FAQ)
