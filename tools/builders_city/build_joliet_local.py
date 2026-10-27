import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Joliet, Illinois','Car shipping at the crossing of Interstates 55 and 80, next to the busiest inland port in the country',
 ['Car shipping in Joliet starts where Interstate 80 crosses Interstate 55, a few miles from the intermodal yards. Ship Guy is a licensed auto transport broker with an office on Chicago Street downtown, beside the Rialto.',
  'We arrange vetted carriers across Will County, from Plainfield to New Lenox and down to Elwood. The trucks belong to the carriers.',
  'Interstate 80 crosses the south side of the city from Larkin Avenue to Briggs Street. Interstate 55 runs the west side. US 30 crosses the north. Route 53 is Chicago Street through downtown and the road south to the yards. Jefferson Street, Larkin, and Essington carry the rest.',
  'This page covers the interstates, the lift bridges, downtown, the Cathedral Area, both sides of town, and beyond. It also covers the intermodal, the refinery, the hospitals, the colleges, the race weekends, and the lanes.'],
 'Joliet at a glance',
 ['Most pickups happen within 1 to 3 days. Every cross-country carrier on 80 passes the city, and the Chicago trucks come down 55.',
  'Chicago is an hour. Indianapolis, St. Louis, Milwaukee, and Detroit are a same-day haul. Minneapolis and Nashville take a day. Denver and Dallas take two or three, and the coasts take three to five.'],
 'Tell us the side of the river. Downtown and the Cathedral Area need a meeting spot. The west side, Shorewood, and the subdivisions on Caton Farm usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 80, Interstate 55, Route 53, US 30, Jefferson Street, and the Lift Bridges',
 prose(
  L('Joliet carries more trucks than any city its size in the country. The car haulers ride with them.'),
  P('Interstate 80 crosses the south side of the city. The exits are Larkin, Center, Chicago Street, Richards, and Briggs. Every carrier between the coasts passes all of them. The state is rebuilding 80 through the city, river bridges included. The lane closures run for years. The carriers plan for them. Interstate 55 runs the west side from Shorewood to Bolingbrook, and the Chicago trucks use it.'),
  P('Route 53 is Chicago Street downtown. It runs south past the raceway to the intermodal yards in Elwood. Arsenal Road and Laraway Road feed the yards. The new Houbolt Road bridge links the yards to 80 and charges a toll. US 30 is Plainfield Road across the north side. US 52 is Jefferson Street from downtown west to 55. US 6 runs through downtown toward Channahon.'),
  P('Larkin Avenue and Essington Road run north and south on the west side. Black Road, Theodore Street, and Caton Farm Road cross it. Collins Street runs the east side past the old prison. Route 7 reaches Lockport and Crest Hill. Interstate 355 ends at 80 in New Lenox, and it is the only tollway in the county.'),
  P('Downtown, the bridges over the river lift for the barges. Jefferson, Cass, Jackson, and Ruby Streets all stop for ten minutes at a time. A carrier crossing downtown builds that in. The carriers come off 80 at Larkin and Chicago Street, and off 55 at Jefferson. The mall lot on Larkin, the stadium, and the casino by the interchange are the usual meeting spots.'),
  P('Our office is on Chicago Street downtown, beside the Rialto and two blocks from the train station.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the Cathedral Area, the West Side, the East Side, Shorewood, and the Intermodal Towns',
 prose(
  L('Joliet is a stone and steel town on a river. A grid sits on the bluffs, and subdivisions run west to Plainfield.'),
  P('Downtown sits between the river and the bluff. It is a grid around the theater, the station, and the ballpark. Chicago Street is narrow, and a trailer cannot stop on it. The driver meets you at the station lots, at the stadium, or at the casino on the river. The Cathedral Area up the hill to the west is a historic district. Big houses sit on narrow streets under old trees. The handoff moves to the college lot or to Jefferson.'),
  P('The west side along Larkin and Essington is the postwar half of the city. It has wide streets and the mall. The curb works on most blocks. The subdivisions off Caton Farm, Black Road, and Theodore have wider streets still. Cunningham, Forest Park, and the Upper Bluff above downtown are older grids with alleys. The handoff moves to the main road.'),
  P('The east side along Collins Street is the oldest part of town. It has the prison, the steel-mill grids, and narrow streets. The driver meets you on Collins or at a lot off 80 at Richards. Fairmont, Preston Heights, and Ingalls Park south of 80 are the same. Rockdale by the river and the Chicago Street yards are industrial, and a lot by the gate works.'),
  P('Shorewood and Crest Hill have wide streets and lots on every main road. Plainfield and Lockport price the same as Joliet, and so does New Lenox on the east. Elwood, Channahon, and Minooka to the south are the intermodal towns. The refinery and the yards sit at their edges. Romeoville and Bolingbrook up 55 price the same too.'),
 )))

ROUTES=[("Chicago, IL","I-55 · ~45 mi","Same day","$120–$200"),("Milwaukee, WI","I-55/I-94 · ~130 mi","Same day","$170–$270"),
 ("Indianapolis, IN","I-80/I-65 · ~190 mi","Same day","$210–$320"),("St. Louis, MO","I-55 · ~255 mi","1 day","$250–$370"),
 ("Detroit, MI","I-80/I-94 · ~290 mi","1 day","$280–$410"),("Minneapolis, MN","I-39/I-90 · ~400 mi","1 day","$350–$500"),
 ("Nashville, TN","I-57/I-24 · ~460 mi","1 day","$390–$560"),("Dallas, TX","I-55/I-44 · ~900 mi","2–3 days","$630–$890"),
 ("Denver, CO","I-80/I-76 · ~950 mi","2–3 days","$650–$930"),("Orlando, FL","I-65/I-75 · ~1,160 mi","3 days","$770–$1,090")]
BODY.append(rate_table('Lanes &amp; Costs','Joliet Car Shipping Lanes and Estimated Costs',
 'The lanes Will County cars take most, with estimated open-trailer ranges. Your exact route prices on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates leaving Joliet, sedan that starts, open trailer. Add 10 to 25 percent for an SUV or a pickup, and more for an enclosed trailer. The Houbolt bridge and 355 tolls are included when a carrier uses them. Fuel, the season, and the carriers free on your dates set the final price.',
 prose(
  P('Joliet prices under Chicago on the cross-country lanes. The carriers are already on 80 and lose no time reaching the city. The Denver, Iowa, and East Coast lanes price lowest of all for that reason. The Chicago lane runs daily in both directions.'),
  P('Florida and Texas follow the snowbird calendar, higher in the fall and lower in the spring. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Intermodal, the Refinery, the Hospitals, the Colleges, and the County',
 prose(
  L('Joliet relocates warehouse managers, refinery engineers, nurses, and students. The intermodal moves more people than anyone.'),
  P('The intermodal yards in Elwood and Joliet handle more containers than any inland port in the country. The warehouses around them stretch for miles and bring in managers, technicians, and drivers from every state. The refinery in Channahon relocates engineers and operators on turnaround schedules. We supply the paperwork a reimbursed move needs.'),
  P('The hospital on the near west side and the one in New Lenox bring in nurses all year. Residents arrive each June. The junior college on Houbolt Road is the oldest public community college in the country. It brings cars in each August. The university in the Cathedral Area and the university in Romeoville do the same. An adult signs for a student car at a campus lot.'),
  P('The county government downtown and the courts move attorneys and staff in every month. The casinos hire managers on short notice. The quarries and the steel shops along the river move operators from the mills in Indiana. Families priced out of the inner suburbs buy in Plainfield and Shorewood. Many ship a second car behind the move.'),
  P('Great Lakes sits two hours north, and families on orders settle across Will County. The orders cover one car, and the second one comes with us. Ship Guy is a private broker with no connection to the base. The <a href="military-car-shipping.html">military</a> page covers the timing. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Race Weekends, the Ballpark, the Haunted Prison, the River, and the Tornado of 1990',
 prose(
  L('Joliet runs on a drag strip, a ballpark, a haunted prison, and a river that lifts its bridges.'),
  P('The drag strip at the raceway fills Route 53 on race weekends from spring through fall. The traffic backs onto the interstate. A pickup south of the city on a race weekend moves to the morning. Memorial Day fills Route 53 at the national cemetery in Elwood the same way.'),
  P('The ballpark downtown fills the station lots on game nights from May through September. The theater fills Chicago Street on show nights. The old prison on Collins Street runs a haunted house every night in October. The east side gridlocks after dark. The holiday parade closes downtown on a Friday night in November. A handoff near any of them moves to the daytime.'),
  P('The river floods downtown. The April 2013 storm put Bluff Street and the lots by the casino under water. The lift bridges stayed up for days. A pickup on the low streets moves up the hill for a day. The bluffs and the west side never notice.'),
  P('The 1990 Plainfield tornado crossed Crest Hill and the north side of Joliet. The sirens sound a few times each spring. A pickup waits for the warning to lift. Winter brings thirty inches of snow, and 80 closes a few times a season. The 2011 blizzard stranded the trucks on 80 overnight. The carriers park at the truck stops by the interchange until the plows finish. A winter pickup can lose a day. Summer derechos take the trees down every few years.'),
 )+chips(["Downtown","Chicago Street","Rialto","Union Station","Ballpark","Bluff Street","Cathedral Area","Upper Bluff","Cunningham","Forest Park","West Side","Larkin","Essington","Black Road","Theodore","Caton Farm","Rock Run","East Side","Collins Street","Fairmont","Preston Heights","Ingalls Park","Rockdale","Crest Hill","Shorewood","Plainfield","Lockport","Romeoville","New Lenox","Elwood","Channahon","Minooka","Manhattan"])
 +NOTE('Serving Joliet, Shorewood, Plainfield, and all of Will County, bluff street or subdivision. Tell us the side of the river and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Joliet?',
 prose(
  L('Most cars leave Will County on an open trailer, and the lane prices assume one.'),
  P('A closed trailer keeps a car away from the salt and the gravel. It also stops the stone chips that fly on 80 behind the container trucks. The racers who run the drag strip book one for the trip home. Families shipping a new car to a student book one too.'),
  P('A commuter car or a work truck goes open and arrives fine. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages lay out the difference.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A number, a meeting spot at the mall or the station, and a signature at the far end. Most moves close inside a week.'),
  P('Confirm the number, and we hand the car to a carrier already rolling on 80 or 55. The lot and the pickup window reach you that day. At the handoff, the driver inspects the car and lists every mark on a Bill of Lading. You both sign it, and the same sheet closes the delivery.'),
 )+ULI([
  "Remove everything personal from the cabin, the trunk, and the console",
  "Leave the tank at about a quarter",
  "Photograph each panel and the odometer before the truck arrives",
  "Hand the driver one working key and describe any fault",
  "Shut off any aftermarket alarm",
  "Downtown or in the Cathedral Area, meet the truck at the station lots or on Jefferson",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Joliet Drivers Choose Ship Guy',
 prose(
  L('We put your car on the carriers already crossing the country on 80. We plan around the bridge lifts, the race weekends, and the winter.'),
  P('Ship Guy holds FMCSA brokerage authority and a $75,000 surety bond, and the federal register lists both. Our office is on Chicago Street downtown, beside the Rialto.'),
  P('The coordinator who quotes the move answers for it until the car is signed for. Open, enclosed, and expedited transport are on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Joliet','116 N Chicago St #788','Joliet, IL 60432','+18158531975','(815) 853-1975','CT',
 '116+N+Chicago+St+%23788,+Joliet,+IL+60432','Visit Us','Find Ship Guy in Joliet',
 'Our office is on Chicago Street downtown, beside the Rialto Square Theatre and two blocks from Union Station.',
 map_src=None, alt=True))

FAQ=[
 ("How much does it cost to ship a car from Joliet to Chicago or Indianapolis?","Chicago runs one hundred twenty to two hundred dollars for a sedan, about forty-five miles up 55. Indianapolis runs two hundred ten to three hundred twenty, about one hundred ninety miles on 80 and 65. St. Louis comes in between two hundred fifty and three hundred seventy. An SUV or pickup adds 10 to 25 percent. All three lanes run daily, so a pickup comes within a day or two."),
 ("Can the carrier come to my street downtown or in the Cathedral Area?","Usually not. Chicago Street is narrow, and the Cathedral Area has big trees over narrow streets. The driver meets you at the station lots, at the stadium, or at the college lot. The west side, Shorewood, and the subdivisions off Caton Farm usually allow the curb."),
 ("Do you ship cars for people relocating to the intermodal or the refinery?","Yes, all year. The warehouses around the yards in Elwood and Joliet bring in managers, technicians, and drivers from every state. The refinery in Channahon moves engineers on turnaround schedules. Many ship a second car behind the move. The handoff works at a lot off 80 or on Route 53. We provide the paperwork a reimbursed move needs."),
 ("Does the construction on Interstate 80 affect my pickup?","A little. The state is rebuilding 80 through the city, bridges included, and the lane closures run for years. The carriers plan around them and come off at Larkin or Chicago Street. A pickup near the river bridges may move to a lot on the west side. The price does not change."),
 ("Do the lift bridges downtown delay the truck?","Sometimes. The bridges on Jefferson, Cass, Jackson, and Ruby lift for the barges. Traffic stops for about ten minutes. A carrier crossing downtown builds that into the window. A handoff at the station lots sits on the east bank. The truck coming off 80 never crosses a bridge."),
 ("Can you ship a car to or from Plainfield, Shorewood, or New Lenox?","Yes, and all three price the same as Joliet. Plainfield and Shorewood ride the same carriers off 55. New Lenox rides them off 80 at 355. A lot on Route 59, on Route 30, or off the interchange works for a handoff. Send the full address for a new subdivision."),
 ("What happens if a blizzard or a tornado warning hits on my pickup day?","Snow closes 80 a few times a winter. The carriers wait at the truck stops by the interchange for the plows. A winter pickup can slip a day, and the call comes first. A tornado warning stops the loading until it lifts, and the sirens sound a few times each spring. The river floods the low streets downtown after a big storm. A pickup there moves up the hill."),
 ("Can you ship a car that does not run from Joliet?","Yes. We send a winch-equipped carrier, and the loading time is priced into the quote from the start. The mall lot on Larkin or the stadium lot gives the driver flat pavement. Tell us whether the car rolls, steers, and brakes."),
 ("Can you ship a race car to or from the drag strip?","Yes. Racers run the strip at the raceway on Route 53 from spring through fall. Most book an enclosed trailer. A car that does not drive on the street goes on a winch carrier. We pick up at the pits or at the shop. Book before the race weekend, and the car leaves the week after."),
 ("What do you need for a Joliet car shipping quote?","The pickup and delivery addresses, with the side of the river or the town here. Year, make, and model. Whether it drives. Open or enclosed. The week you want it gone. With those five things, the Joliet number comes back the same day."),
]
BODY.append(faq_section(FAQ,'Joliet FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Joliet?','Two minutes on the form above prices your lane. Send the side of the river and your dates, and a carrier already on 80 takes it.','+18158531975','(815) 853-1975','Get your free Joliet quote'))

build({
 'slug':'auto-transport-joliet-illinois',
 'title':'Car Shipping in Joliet, IL — Auto Transport | Ship Guy',
 'meta':'Car shipping in Joliet, IL, where Interstate 80 crosses Interstate 55 beside the busiest inland port in the country. Intermodal and refinery relocations, downtown and Cathedral Area meeting spots, west side and Shorewood curbside pickups, the lift bridges, the 80 rebuild, race weekends, the river, and the winter. Local office on Chicago Street beside the Rialto. Free quote.',
 'h1':'Car Shipping in<br>Joliet, <span class="accent">Illinois</span>',
 'lede':'Open, enclosed, and expedited auto transport across Will County, planned around 80, 55, the lift bridges, the race weekends, and the winter.',
 'tel':'+18158531975','disp':'(815) 853-1975','brand':'Joliet','keyword':'car shipping in joliet',
 'localterms':['joliet','interstate 80','interstate 55','interstate 355','tollway','route 53','chicago street','us 30','plainfield road','us 52','jefferson street','us 6','route 7','larkin','essington','black road','theodore','caton farm','collins street','richards','briggs','houbolt','arsenal road','laraway','lift bridges','cass','jackson','ruby','barges','rebuild','construction','downtown','rialto','theater','station','union station','ballpark','stadium','bluff street','casino','interchange','cathedral area','historic','college','upper bluff','cunningham','forest park','west side','mall','rock run','east side','prison','steel','fairmont','preston heights','ingalls park','rockdale','shorewood','crest hill','plainfield','lockport','new lenox','elwood','channahon','minooka','romeoville','bolingbrook','intermodal','yards','containers','inland port','warehouses','refinery','turnaround','hospital','nurses','residents','junior college','university','county','courts','casinos','quarries','great lakes','orders','raceway','drag strip','race weekends','memorial day','national cemetery','haunted','october','holiday parade','2013','flood','1990','tornado','sirens','snow','2011 blizzard','truck stops','derechos','chicago','milwaukee','indianapolis','st. louis','detroit','minneapolis','nashville','dallas','denver','orlando','iowa'],
}, BODY, FAQ)
