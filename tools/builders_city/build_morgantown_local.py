import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("2–4 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Morgantown, West Virginia','Car shipping where Interstate 79 meets 68 on the hills, one campus fills the town each August, and Pittsburgh is an hour up the road',
 ['Car shipping in Morgantown runs on Interstate 79, with Interstate 68 leaving for Maryland south of town. Ship Guy is a licensed auto transport broker with an office at University Town Centre in Granville.',
  'We book vetted carriers across Morgantown, from the High Street blocks to Cheat Lake and the Mileground. Star City, Westover, Granville, Sabraton, and Fairmont ride the same trucks. Every truck belongs to a carrier. Ship Guy holds the license and the bond.',
  'Interstate 79 runs along the west side of the river, north to Pittsburgh and south to Charleston. Interstate 68 leaves it south of town and climbs east past Cheat Lake to Cumberland. Route 19 crosses the river at Westover. Route 705 carries the campus traffic past the hospital and the stadium. The Mileground, Beechurst Avenue, and Greenbag Road carry the rest.',
  'This page covers 79, 68, 705, the Mileground, downtown, the student hills, and the lake. It also covers the university, the two hospitals, the federal labs, and the gas fields. Football Saturdays, move-in week, the snow on the hills, and the Cheat are here too.'],
 'Morgantown at a glance',
 ['Most Morgantown pickups land within 2 to 4 days, and the Pittsburgh carriers often make it faster. The town sits an hour south of Pittsburgh on 79, and those trucks pass daily. The Charleston trucks come up 79, and the Baltimore trucks come over 68. The university keeps the pool fuller than the town’s size suggests.',
  'Pittsburgh and Charleston are a same-day haul. Columbus, Cleveland, Baltimore, Washington, Cincinnati, and Philadelphia take a day. Charlotte takes one to two, and Florida takes three.'],
 'Tell us the hill. Downtown, Sunnyside, South Park, and Wiles Hill meet the truck on Beechurst Avenue or at the Coliseum lots. Suncrest, Cheat Lake, Sabraton, Westover, and Star City usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 79, Interstate 68, Route 19, Route 119, Route 705, Route 7, Route 43, the Mileground, Beechurst Avenue, Monongahela Boulevard, Patteson Drive, University Avenue, and Greenbag Road',
 prose(
  L('Morgantown is a river town stacked up both banks. The interstates stay on the flat ground west and south of it. A carrier picks an exit and works the main roads, never the hills.'),
  P('Interstate 79 runs down the west side of the Monongahela. The exits are Star City, Westover, and Goshen Road. Pittsburgh is seventy-five miles north, and Fairmont and Clarksburg are south. Interstate 68 leaves 79 south of town and climbs east past Sabraton and Cheat Lake. It reaches Coopers Rock and the Maryland line. Baltimore and Washington ride it. Route 43 is the toll expressway from 68 north to Uniontown and Pittsburgh’s south side. Route 19 comes over the Westover Bridge and runs through town as Beechurst Avenue and Monongahela Boulevard. Route 119 is the Mileground to the east and Grafton Road to the south.'),
  P('Route 705 is Patteson Drive and Chestnut Ridge Road, the busiest two miles in town. It passes the hospital, the Coliseum, and the stadium and backs up every afternoon. University Avenue runs from the downtown campus through Sunnyside to Evansdale. High Street is downtown, one way and steep at the cross streets. Route 7 is Earl Core Road through Sabraton. Greenbag Road loops the south side past the old mall. Van Voorhis Road is the student apartment strip. The elevated cars of the campus transit run above the river road between the campuses.'),
  P('The carriers come off 79 at Star City or Westover. On 68 they use the Sabraton or Cheat Lake exits. They meet at the lots around our office at University Town Centre or the mall lots in Westover. The Suncrest shopping center on Patteson Drive works too. The Coliseum lots work outside game days. So do the old mall lots on Greenbag Road and the ballpark lot in Granville. Pittsburgh’s airport is an hour and a half north for a fly-and-ship. The small field on the Mileground flies commuter planes.'),
  P('Our office is at University Town Centre in Granville, across the river from campus, off exit 155.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, Sunnyside, Evansdale, Suncrest, South Park, Wiles Hill, Woodburn, Sabraton, Star City, Westover, Granville, Cheat Lake, the Mileground, Brookhaven, Fairmont, and Clarksburg',
 prose(
  L('Morgantown is a downtown on a slope, a student hill beside it, and neighborhoods on every ridge. The truck meets the hills at the bottom and the flat parts at the curb.'),
  P('Downtown is High Street, the courthouse, the bars, and one-way streets that climb hard to the east. The driver meets you on Beechurst Avenue or at the lots by the river. Sunnyside is the student hill between downtown and Evansdale, narrow streets of rentals with cars on both curbs. No trailer enters it. The handoff moves to Beechurst or the Coliseum lots. Evansdale is the towers, the stadium, the Coliseum, and the hospital along Patteson Drive. The handoff happens at the Coliseum lots. Suncrest north of Evansdale is postwar grids under big trees, and the curb works on most streets.'),
  P('South Park climbs above downtown with Victorian houses on winding streets. The driver meets you on Grand Street or at the bottom of the hill. Wiles Hill and Jerome Park are the same story on the north side. The handoff happens on University Avenue. Woodburn and First Ward east of downtown are older grids where the curb works on the wider streets. Sabraton along Deckers Creek is flat, and the curb works. Brookhaven on Greenbag Road is subdivisions, and the truck comes to the house.'),
  P('Star City and Westover across the river are flat river towns with grids, and the curb works. Granville is the shopping district, the ballpark, and new apartments, all built for trucks. Cheat Lake east on 68 is lake houses on steep winding roads and new subdivisions on the ridge. The handoff happens on Cheat Road or at the lots by the exit. The Mileground is the airport, the student complexes, and the strip. The complexes allow the curb at the entrance. Fairmont twenty miles south is a hill town with its own campus. Clarksburg and Bridgeport are flat enough that the curb works.'),
  P('Star City, Westover, Granville, Sabraton, Cheat Lake, and the Mileground ride the same trucks. They price the same as Morgantown. Fairmont and Uniontown do too. Clarksburg, Bridgeport, and Kingwood add a day.'),
 )))

ROUTES=[("Pittsburgh, PA","I-79 · ~75 mi","Same day","$150–$240"),("Charleston, WV","I-79 · ~155 mi","Same day","$210–$320"),
 ("Columbus, OH","I-79/I-70 · ~185 mi","1 day","$230–$350"),("Cleveland, OH","I-79/I-76 · ~205 mi","1 day","$240–$360"),
 ("Baltimore, MD","I-68/I-70 · ~210 mi","1 day","$240–$360"),("Washington, DC","I-68/I-70/I-270 · ~210 mi","1 day","$240–$360"),
 ("Cincinnati, OH","I-79/I-70/I-71 · ~290 mi","1 day","$280–$410"),("Philadelphia, PA","I-79/I-76 · ~370 mi","1 day","$320–$470"),
 ("Charlotte, NC","I-79/I-77 · ~390 mi","1–2 days","$360–$520"),("Orlando, FL","I-79/I-77/I-95 · ~900 mi","3 days","$660–$940")]
BODY.append(rate_table('Lanes &amp; Costs','Morgantown Car Shipping Lanes and Estimated Costs',
 'The lanes Monongalia County cars take most, with open-trailer estimates. Price your exact lane on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Morgantown, running sedan, open trailer. SUVs and pickups run 10 to 25 percent more, and enclosed runs above that. The week and the carriers on 79 that week fix the figure.',
 prose(
  P('Morgantown prices with Pittsburgh on most lanes, because the Pittsburgh trucks serve both. The Pittsburgh lane itself is among the lowest anywhere, an hour north on 79. Charleston rides 79 south. Columbus and Cleveland ride 79 and 70 through Washington, Pennsylvania. Baltimore and Washington ride 68 over the mountains. The Carolina lanes ride 79 and 77 through Charleston. The Florida lane fills in May when the graduates leave.'),
  P('Move-in week in August and a home Saturday are the busy weeks. The <a href="car-shipping-cost.html">cost guide</a> covers size, condition, and timing one at a time.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The University, the Two Hospitals, the Federal Labs, the Fingerprint Center in Clarksburg, the Gas Fields, the Town Centre, the Ballclub, and the Pittsburgh Commuters',
 prose(
  L('Morgantown relocates students, professors, residents, scientists, and gas crews. The university moves the most by far.'),
  P('West Virginia University enrolls more than twenty-three thousand students on the Morgantown campus. Residence hall move-in runs the middle three days of August, and the cars arrive with it. A parent books, and an adult signs at the Coliseum lots. The cars leave in May. Faculty and staff relocate on contract dates all year. The medical school and the two hospital systems bring residents each June and nurses every month. The handoff happens at the lots off Patteson Drive.'),
  P('The federal safety institute and the energy lab north of campus relocate scientists on program dates. The fingerprint center in Clarksburg, thirty-five miles south, relocates analysts on clearance timelines. The gas companies move crews in and out with the drilling schedule. The handoff happens at the lots on the Mileground. The stores at the Town Centre relocate managers. The summer-league ballclub in Granville brings players each June. When the employer covers the shipment, we write it up however it needs.'),
  P('The Guard’s readiness center rotates people on orders, and the veterans’ hospital in Clarksburg brings staff. Ship Guy is a private broker and not part of the Guard or the university. The <a href="military-car-shipping.html">military</a> page covers orders and the dates they set.'),
  P('Some newcomers keep a job in Pittsburgh and commute down 79. Retirees come to Cheat Lake from the Pittsburgh suburbs. The <a href="state-to-state-car-shipping.html">state-to-state</a> page explains the paperwork a state line adds.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Football Saturdays, Move-In Week, Graduation, Mountaineer Week, the Lake Summers, Coopers Rock in October, the Snow on the Hills, and the Cheat',
 prose(
  L('Morgantown runs on one calendar, the university’s. The weather problem is snow on streets that were steep to begin with.'),
  P('Football Saturdays bring sixty thousand people to the stadium. Patteson Drive and Monongahela Boulevard close from the morning on. The Coliseum lots are gone those days, and the handoff moves to the Town Centre or Westover. Move-in week in the middle of August fills Sunnyside and Evansdale. Graduation in May empties them. Mountaineer Week fills downtown in November, and homecoming fills it in October. Cheat Lake fills with boats every summer weekend. Coopers Rock fills 68 with leaf traffic each October. Give a home Saturday or a move-in date three weeks of notice.'),
  P('The February 2010 storms dropped close to two feet on the town in a week. The January 2016 blizzard dropped more than a foot and a half. Sandy came as snow in October 2012, most of a foot in town and more on the mountain. It closed 68 toward Cumberland. Two inches shuts Sunnyside and South Park. The carriers wait in Westover or Fairmont until the hills thaw. A winter pickup can slip two days. The long grade on 68 out to Cheat Lake ices first.'),
  P('The Cheat flooded in November 1985 and took out whole towns upstream. Deckers Creek climbs its banks in a wet spring and closes Route 7 for a day. Fog settles in the river valley on fall mornings. Summer brings an afternoon storm that passes in an hour.'),
 )+chips(["Downtown","High Street","Sunnyside","Evansdale","Suncrest","South Park","Wiles Hill","Jerome Park","Woodburn","First Ward","Greenmont","Sabraton","Brookhaven","Star City","Westover","Granville","Cheat Lake","The Mileground","Pierpont","Osage","Fairmont","Clarksburg","Bridgeport","Kingwood","Uniontown","Point Marion","Waynesburg"])
 +NOTE('Serving Morgantown, Monongalia County, and the north-central hills, Sunnyside rental or Cheat Lake ridge. Tell us the hill and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Morgantown?',
 prose(
  L('Open trailers carry most of north-central West Virginia’s cars, and the table above assumes one.'),
  P('Enclosed keeps the road brine, the coal dust, and the spring hail off the paint. The professors moving a car worth more than the move book it. So do the lake owners with a convertible. When snow is coming and only an open truck has room, you hear that first.'),
  P('A commuter car or a student’s hatchback rides open and arrives fine. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages set out the difference.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A figure, a lot off 79, and a signature when the car comes off the truck. Move-in week or the contract date picks the week.'),
  P('Approve the figure, and we hand the car to a carrier already running 79 that week. The lot and the window are set the same day. The driver photographs the car at pickup and writes its condition on the Bill of Lading. You initial it, and it is the reference at delivery.'),
 )+ULI([
  "Your things out of the cabin and the trunk",
  "A quarter tank of fuel or less",
  "Photos of every side and the odometer before the truck arrives",
  "A working key and a note on known faults",
  "Aftermarket alarms turned off",
  "In Sunnyside, in South Park, or on a game Saturday, expect the Coliseum lots or the Town Centre",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> page walks the steps, and the <a href="car-shipping-preparation.html">preparation</a> page covers the morning the truck comes.'))))

BODY.append(sec('Why Ship Guy','Why Morgantown Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already run 79 between Pittsburgh and Charleston every day. We know which Saturdays close Patteson Drive and which hills never take a trailer.'),
  P('Our FMCSA license and our $75,000 bond are on the federal register for anyone to check. The office is at University Town Centre in Granville.'),
  P('One person at Ship Guy carries the move from quote to delivery call. The <a href="services.html">services</a> page covers open, enclosed, and expedited one by one.'),
 )))

BODY.append(office('Morgantown','7839 University Town Centre Dr #323','Morgantown, WV 26501','+13046326352','(304) 632-6352','ET',
 '7839+University+Town+Centre+Dr+%23323,+Morgantown,+WV+26501','Visit Us','Find Ship Guy in Morgantown',
 'Our office is at University Town Centre in Granville, across the river from campus, off exit 155.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3792.3361771583895!2d-79.99475079999999!3d39.6435849!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x88357bdef37ea709%3A0xe8d7ac5c260e1594!2sShip%20Guy%20Auto%20Transport!5e1!3m2!1sen!2sus!4v1794237241123!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Morgantown to Pittsburgh or Baltimore?","Pittsburgh runs one hundred fifty to two hundred forty dollars for a sedan, an hour north on 79. It is among the lowest lanes anywhere. Baltimore and Washington run two hundred forty to three hundred sixty over 68. Charleston runs two hundred ten to three hundred twenty. An SUV or a pickup adds 10 to 25 percent."),
 ("Can you deliver on a WVU move-in date?","Yes. Residence hall move-in runs the middle three days of August, and the cars arrive with it. A parent books, and an adult signs at the Coliseum lots. Sunnyside and the campus streets are closed to a trailer that week. The window follows your date, and the cars go home in May."),
 ("What happens on a football Saturday?","Patteson Drive and Monongahela Boulevard close from the morning on, and sixty thousand people fill the stadium. The Coliseum lots are gone. The handoff moves to the Town Centre or Westover, and the figure does not change. Give a home Saturday three weeks of notice."),
 ("Can the carrier come to my street in Sunnyside or South Park?","No. Sunnyside is narrow streets with cars on both curbs. South Park is winding streets up a steep hill. The driver meets you on Beechurst Avenue, on Grand Street, or at the Coliseum lots. Suncrest, Cheat Lake, Sabraton, Westover, and Star City usually allow the curb."),
 ("Why does Morgantown take 2 to 4 days when Pittsburgh is an hour away?","Because the town is small, and a carrier fills the truck in Pittsburgh or Charleston first. The Pittsburgh trucks often make it faster. We tell you the window with the figure. The university weeks run tighter than the rest of the year."),
 ("Do you ship cars for the hospitals, the federal labs, or the fingerprint center?","Yes, in every season. The two hospital systems bring residents each June. The safety institute and the energy lab relocate scientists on program dates. The fingerprint center in Clarksburg relocates analysts on clearance timelines. When the employer covers the shipment, we write it up however it needs."),
 ("What happens if snow hits on my pickup day?","Two inches shuts the hills. The truck waits in Westover or Fairmont until they thaw, usually a day. The February 2010 storms and the January 2016 blizzard each closed the town for most of a week. We call as soon as the forecast turns. The pickup moves to the first clear morning, and the figure stays put."),
 ("Can you ship a car to or from Cheat Lake, Fairmont, or Clarksburg?","Yes. Star City, Westover, Granville, Sabraton, Cheat Lake, and the Mileground ride the same carriers. They price the same as Morgantown. Fairmont and Uniontown do too. Clarksburg, Bridgeport, and Kingwood add a day."),
 ("Can you ship a car that does not run from Morgantown?","Yes. The carrier brings a winch, and the figure includes the loading time. The Town Centre lots and the Westover mall lots are flat. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Morgantown car shipping quote?","Both addresses, with the hill or the neighborhood. The year, make, and model, and whether it runs. Open or enclosed, and the week around move-in or the contract date. With those, the Morgantown figure comes back the same day."),
]
BODY.append(faq_section(FAQ,'Morgantown FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Morgantown?','Two minutes on the form above puts a Morgantown figure on your lane. Tell us the hill and the week, and a carrier already on 79 takes it.','+13046326352','(304) 632-6352','Get your free Morgantown quote'))

build({
 'slug':'auto-transport-morgantown-west-virginia',
 'title':'Car Shipping in Morgantown, WV — Auto Transport | Ship Guy',
 'meta':'Car shipping in Morgantown, WV, where Interstate 79 meets 68. WVU move-in dates and football Saturdays, the two hospitals, the federal labs, the fingerprint center in Clarksburg, main-road handoffs for Sunnyside, South Park, and downtown, curbside pickups in Suncrest, Cheat Lake, Sabraton, Westover, and Star City, the Pittsburgh lane, and the snow on the hills. Local office at University Town Centre in Granville. Free quote.',
 'h1':'Car Shipping in<br>Morgantown, <span class="accent">West Virginia</span>',
 'lede':'Open, enclosed, and expedited auto transport across Morgantown, Monongalia County, and the north-central hills, planned around 79 and 68, the campus dates, the football Saturdays, the Pittsburgh lane, and the snow.',
 'tel':'+13046326352','disp':'(304) 632-6352','brand':'Morgantown','keyword':'car shipping in morgantown',
 'localterms':['morgantown','interstate 79','interstate 68','route 19','route 119','route 705','route 7','route 43','toll expressway','uniontown','the mileground','grafton road','beechurst avenue','monongahela boulevard','patteson drive','chestnut ridge road','university avenue','high street','earl core road','greenbag road','van voorhis','elevated cars','westover bridge','star city','westover','goshen road','sabraton','cheat lake','coopers rock','maryland line','cumberland','downtown','courthouse','one-way streets','sunnyside','student hill','rentals','evansdale','towers','stadium','coliseum','hospital','suncrest','south park','grand street','wiles hill','jerome park','woodburn','first ward','greenmont','deckers creek','brookhaven','granville','ballpark','town centre','old mall','pierpont','osage','fairmont','clarksburg','bridgeport','kingwood','point marion','waynesburg','west virginia university','twenty-three thousand','residence hall','move-in','middle three days of august','medical school','hospital systems','residents','federal safety institute','energy lab','fingerprint center','clearance','gas companies','drilling','summer-league','ballclub','guard','readiness center','veterans’ hospital','pittsburgh commuters','retirees','football saturdays','sixty thousand','graduation','mountaineer week','homecoming','boats','leaf traffic','february 2010','two feet','january 2016','foot and a half','sandy','october 2012','two inches','grade','cheat','november 1985','fog','river valley','fly-and-ship','airport','small field','suncrest shopping center','mall lots','pittsburgh','charleston','columbus','cleveland','baltimore','washington','cincinnati','philadelphia','charlotte','orlando','brine','coal dust','hail','convertible','bill of lading','fmcsa','winch'],
}, BODY, FAQ)
