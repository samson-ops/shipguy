import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Fort Wayne, Indiana','Car shipping where three rivers meet, with Interstate 69 on one side and the 469 loop around the rest',
 ['Car shipping in Fort Wayne runs off Interstate 69 and the 469 loop that wraps the east side. Ship Guy is a licensed auto transport broker with an office on Broadway at Electric Works.',
  'We arrange vetted carriers across Allen County, from Aboite to New Haven and up to Huntertown. The trucks belong to the carriers, not to us.',
  'Interstate 69 runs the west side of the city on its way from Indianapolis to the Michigan line. Interstate 469 loops the south and east. US 30 crosses toward Chicago and Ohio. Lima Road, Coldwater Road, Jefferson Boulevard, and Coliseum Boulevard carry the rest.',
  'This page covers the interstate, the loop, downtown, the north side, Aboite, and New Haven. It also covers the hospitals, the pickup plant, the campuses, the festivals, the rivers, and the lanes.'],
 'Fort Wayne at a glance',
 ['Most pickups happen within 1 to 3 days. Carriers running between Indianapolis and Detroit pass the city on 69, and the Chicago trucks use US 30.',
  'Indianapolis, Chicago, Detroit, and Columbus are all a same-day haul. Cincinnati, Cleveland, and Louisville take a day. The East Coast and the South need two to three, and the West needs four or five.'],
 'Tell us the side of town. Downtown and West Central need a meeting spot. Aboite, the north side, and New Haven usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 69, the 469 Loop, US 30, Lima Road, and Coliseum Boulevard',
 prose(
  L('Fort Wayne sits on the straightest highway between Indianapolis and Detroit. The carriers treat it as a stop.'),
  P('Interstate 69 runs north and south on the west side of the city. The exits at Illinois Road, Jefferson, US 30, Coldwater, Lima, and Dupont cover eight miles. Every carrier between Indianapolis and the Michigan plants passes all of them. The trucks for Chicago and Ohio split off at US 30.'),
  P('Interstate 469 is the loop around the south and east sides. It carries the through trucks past the airport, the pickup plant, and New Haven. US 24 runs east toward Toledo and west toward Logansport. US 27 and US 33 reach the south and the northwest. US 30 leaves the loop toward Van Wert and Chicago.'),
  P('Inside the loop, Lima Road is State Road 3 past the mall. Coldwater Road runs the retail strip. Jefferson Boulevard and Illinois Road carry the southwest. Coliseum Boulevard rings the north side from the university to the coliseum. Clinton Street, Lafayette Street, and Broadway run downtown to the rivers. The Fort to Port highway reaches Toledo on US 24.'),
  P('The carriers come off 69 at Coldwater, Illinois Road, and US 30. The lots at the mall, at Jefferson Pointe, and by the coliseum are the usual meeting spots. No road in Allen County charges a toll. The Ohio Turnpike starts an hour east.'),
  P('Our office is on Broadway at the Electric Works campus, the old GE plant just south of downtown.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, West Central, the North Side, Aboite, Waynedale, and New Haven',
 prose(
  L('Fort Wayne is an old river town with a ring of postwar suburbs and a fast-growing southwest.'),
  P('Downtown sits where the three rivers meet. It is a grid of one-way streets around the courthouse and the ballpark. A trailer cannot stop on Calhoun or Wayne Street. The driver meets you at the Parkview Field lots or at Headwaters Park. West Central next door is a historic district of narrow brick streets. The handoff moves to Broadway or to the Electric Works lots.'),
  P('The north side along Coldwater, Lima, and Dupont has the mall and the hospital campus. Its subdivisions date from every decade since 1950. The postwar grids off Coliseum allow the curb. Pine Valley, Cherry Hill, and the Dupont subdivisions have wide streets. Huntertown and Leo-Cedarville beyond them are small towns with lots on every main road.'),
  P('Aboite on the southwest is the growth side, with Jefferson Pointe and subdivisions out to Roanoke. The truck reaches the curb. Waynedale on the south side is an older grid off Bluffton Road. The handoff works at the shopping center. Southwood Park and the Old Mill neighborhoods have tight streets under old trees.'),
  P('New Haven on the east is its own city, with wide streets and the loop at its edge. The driver meets you on Lincoln Highway or at a lot off the loop. The southeast side along Anthony and McKinnie is an older grid. Georgetown, Maplecrest, and Stellhorn fill the northeast. New Haven prices the same as Fort Wayne, and so does Huntertown.'),
 )))

ROUTES=[("Indianapolis, IN","I-69 · ~125 mi","Same day","$170–$270"),("Chicago, IL","US-30/I-65 · ~160 mi","Same day","$190–$300"),
 ("Detroit, MI","I-69/I-94 · ~160 mi","Same day","$190–$300"),("Columbus, OH","US-33 · ~165 mi","Same day","$200–$310"),
 ("Cincinnati, OH","US-27/I-75 · ~180 mi","Same day","$210–$320"),("Cleveland, OH","US-30/I-71 · ~230 mi","1 day","$240–$360"),
 ("Louisville, KY","I-69/I-65 · ~240 mi","1 day","$240–$360"),("Nashville, TN","I-69/I-65 · ~420 mi","1 day","$370–$530"),
 ("Dallas, TX","I-69/I-44 · ~1,020 mi","2–3 days","$700–$990"),("Orlando, FL","I-75 · ~1,090 mi","3 days","$750–$1,050")]
BODY.append(rate_table('Lanes &amp; Costs','Fort Wayne Car Shipping Lanes and Estimated Costs',
 'The lanes Allen County cars take most, with estimated open-trailer ranges. Your exact route prices on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Fort Wayne for a running sedan on an open trailer. Add 10 to 25 percent for an SUV or a pickup, and more for an enclosed trailer. The week, the direction, and the carriers free on your dates move the final price.',
 prose(
  P('Fort Wayne prices in line with Indianapolis on the Chicago and Detroit lanes. Carriers come through from both and pick up a second car here. The Ohio lanes run full with plant traffic in both directions, which keeps them steady.'),
  P('Florida and Texas ride the snowbird calendar, higher in the fall and lower in the spring. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Hospitals, the Pickup Plant, the Campuses, the Insurer, and the Music Retailer',
 prose(
  L('Fort Wayne relocates nurses, plant engineers, students, and actuaries. The hospital systems move more people than anyone.'),
  P('Two hospital systems run a dozen campuses across the county. The Dupont Road campus and the downtown hospital bring in nurses on contracts all year. Residents arrive each June. Surgeons and administrators arrive with a closing date and a second car. We supply the paperwork a reimbursed move needs.'),
  P('The pickup plant on the south side of the loop builds full-size trucks around the clock. It moves engineers and supervisors from Michigan and Texas on program schedules. The steel company, the defense plant, and the pump maker relocate the same way. The insurer downtown moves actuaries and analysts in every month.'),
  P('The university on Coliseum Boulevard brings cars in each August. The two private colleges and the technical college do the same. A parent ships the car, and an adult signs at a campus lot. The music retailer on US 30 hires from every state and moves its people on short notice.'),
  P('The fighter wing at the airport rotates airmen on orders. The orders cover one car, and the second one comes with us. Ship Guy is a private broker with no connection to the wing. The <a href="military-car-shipping.html">military</a> page covers the timing. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Three Rivers Week, the Ballpark, Johnny Appleseed, the Rivers, and the Snow',
 prose(
  L('Fort Wayne runs on a festival week in July, a ballpark summer, and a winter that closes 69.'),
  P('Three Rivers Festival fills downtown and Headwaters Park for nine days in July. The parade closes Wayne Street, and the fireworks fill every lot by the rivers. A downtown pickup that week moves to Electric Works or to a lot off Coliseum. The Johnny Appleseed Festival does the same thing to the north side in September.'),
  P('The ballpark downtown fills the lots around Jefferson on game nights from April through September. The coliseum does the same on hockey nights and concert nights. The outlet sale at the Memorial Coliseum in April draws shoppers from every state. A handoff near either moves to the morning.'),
  P('The three rivers flood. The 1982 flood put the near north side under water, and the levees have held since. Spy Run and Lakeside still see the rivers rise in a wet March. A pickup on those streets moves to higher ground for a day.'),
  P('Snow comes off the lake in the northeast corner of the state. Interstate 69 closes a few times each winter. The 1978 blizzard shut the city for a week. Ice is the bigger problem on the overpasses. The carriers park in Angola or Marion until the plows finish. A winter pickup can lose a day. Summer brings thunderstorms and a tornado watch most Junes.'),
 )+chips(["Downtown","Parkview Field","Headwaters Park","West Central","Electric Works","Broadway","Spy Run","Lakeside","Bloomingdale","North Side","Coldwater","Lima Road","Glenbrook","Dupont","Pine Valley","Cherry Hill","Huntertown","Leo-Cedarville","Coliseum","Northcrest","Georgetown","Maplecrest","Stellhorn","Southwest","Aboite","Jefferson Pointe","Roanoke","Southwood Park","Waynedale","Southeast","New Haven","Woodburn"])
 +NOTE('Serving Fort Wayne, New Haven, and all of Allen County, river town or subdivision. Tell us the side of the loop and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Fort Wayne?',
 prose(
  L('Most cars leave Allen County on an open trailer, and the lane prices assume one.'),
  P('A closed trailer keeps a car away from salt, stone chips, and weather. Collectors heading to the auction in Auburn book one in May and September. Families shipping a new car from the plant book one too.'),
  P('A commuter car or a work truck goes open and arrives fine. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages lay out the difference.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A quote, a handoff at the mall or off the loop, and a delivery at the far end. The whole thing takes a week.'),
  P('Approve the quote, and we match the car with a carrier already running 69 or US 30. The meeting lot and the pickup window reach you the same day. The driver walks the car with you at pickup and records its condition on a Bill of Lading. You both sign, and the delivery check uses the same sheet.'),
 )+ULI([
  "Take everything personal out of the cabin and the trunk",
  "Run the tank down to about a quarter",
  "Photograph each side and the odometer before the truck arrives",
  "Give the driver one working key and say what the car does wrong",
  "Switch off any aftermarket alarm",
  "In West Central or downtown, meet the truck on Broadway or at a lot",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Fort Wayne Drivers Choose Ship Guy',
 prose(
  L('We book the carriers already passing on 69 and US 30. We plan around the festival week, the ballpark, and the winter.'),
  P('Ship Guy carries active FMCSA brokerage authority and a $75,000 surety bond, both listed in the federal register. Our office sits on Broadway at Electric Works, south of downtown.'),
  P('One coordinator takes the move from the quote to the signed delivery sheet. Open, enclosed, and expedited transport are on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Fort Wayne','1690 Broadway #1055A','Fort Wayne, IN 46802','+12603002248','(260) 300-2248','ET',
 '1690+Broadway+%231055A,+Fort+Wayne,+IN+46802','Visit Us','Find Ship Guy in Fort Wayne',
 'Our office is on Broadway at the Electric Works campus, a few blocks south of downtown.',
 map_src=None, alt=True))

FAQ=[
 ("How much does it cost to ship a car from Fort Wayne to Indianapolis or Chicago?","Indianapolis runs one hundred seventy to two hundred seventy dollars for a sedan. That is about one hundred twenty-five miles down 69. Chicago runs one hundred ninety to three hundred, about one hundred sixty miles on US 30 and 65. Detroit and Columbus price about the same as Chicago. An SUV or pickup adds 10 to 25 percent. Both lanes run daily, so a pickup comes within a day or two."),
 ("Can the carrier come to my street downtown or in West Central?","Usually not. Downtown is a one-way grid around the courthouse, and West Central has narrow brick streets. The driver meets you on Broadway, at the Electric Works lots, or at Headwaters Park. Aboite, the north side, and New Haven usually allow the curb."),
 ("Do you ship cars for people relocating to the hospitals or the pickup plant?","Yes, all year. The hospital systems bring in nurses, residents, and surgeons every month. The pickup plant moves engineers and supervisors from Michigan and Texas on program schedules. Many ship a second car behind the move. The handoff works at the Dupont campus lots or a lot off the loop. We provide the paperwork a reimbursed move needs."),
 ("Does Three Rivers Festival affect my pickup?","Downtown, yes. The festival fills Headwaters Park and the lots by the rivers for nine days in July. The parade closes Wayne Street. We move a downtown pickup that week to Electric Works or to a lot off Coliseum. The rest of the county runs normally."),
 ("Can you ship a car to or from New Haven or Huntertown?","Yes, and both price the same as Fort Wayne. New Haven rides the same carriers off the loop, and Huntertown rides them off Lima Road. A lot off the loop or on Lincoln Highway works for a handoff. Send the full address for a new subdivision in either town."),
 ("Can you time delivery to a student move at the university?","Yes. The campuses on Coliseum Boulevard and downtown bring cars in each August and send them home in May. A parent books the move, and an adult signs for the car at a campus lot. We set the delivery window on the move-in date and move it when the date moves."),
 ("What happens if snow or ice hits on my pickup day?","Ice on the overpasses stops the trucks before snow does. The carriers park in Angola or Marion until the salt trucks finish, and 69 reopens within hours. A winter pickup can slip a day, and the call comes before it does. The rivers rise in March, and a pickup in Spy Run or Lakeside moves to higher ground."),
 ("Can you ship a car that does not run from Fort Wayne?","Yes. We send a carrier with a winch, and the quote includes the loading time from the start. The lots at the mall or by the coliseum give the driver flat ground to work on. Tell us whether the car rolls, steers, and brakes."),
 ("Can you ship a car bought at the Auburn auction?","Yes. Auburn sits twenty minutes north on 69. The auctions in May and September draw buyers from every state. Most book an enclosed trailer for the trip home. We pick up at the auction grounds or at the shipper the auction uses. Book before the sale, and the car leaves the week it is bought."),
 ("What do you need for a Fort Wayne car shipping quote?","The pickup address and the delivery address, with the side of the loop or the neighborhood here. Year, make, and model. Whether it starts and drives. Open or enclosed. The week you want it to go. That gives us enough for a firm Fort Wayne number."),
]
BODY.append(faq_section(FAQ,'Fort Wayne FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Fort Wayne?','Two minutes on the form above prices your lane. Send the side of the loop and your dates, and a carrier already on 69 takes it.','+12603002248','(260) 300-2248','Get your free Fort Wayne quote'))

build({
 'slug':'auto-transport-fort-wayne-indiana',
 'title':'Car Shipping in Fort Wayne, IN — Auto Transport | Ship Guy',
 'meta':'Car shipping in Fort Wayne, IN, where Interstate 69 meets the 469 loop. Hospital and pickup-plant relocations, downtown and West Central meeting spots, Aboite and New Haven curbside pickups, Three Rivers Festival week, the Auburn auctions, and the winter on 69. Local office on Broadway at Electric Works. Free quote.',
 'h1':'Car Shipping in<br>Fort Wayne, <span class="accent">Indiana</span>',
 'lede':'Open, enclosed, and expedited auto transport across Allen County, planned around 69, the 469 loop, the festival week, and the winter.',
 'tel':'+12603002248','disp':'(260) 300-2248','brand':'Fort Wayne','keyword':'car shipping in fort wayne',
 'localterms':['fort wayne','interstate 69','469','loop','us 30','us 24','us 27','us 33','lima road','state road 3','coldwater','dupont','jefferson boulevard','illinois road','coliseum boulevard','clinton','lafayette','broadway','fort to port','calhoun','wayne street','courthouse','parkview field','ballpark','headwaters park','west central','electric works','ge plant','three rivers','spy run','lakeside','bloomingdale','north side','mall','glenbrook','pine valley','cherry hill','huntertown','leo-cedarville','aboite','jefferson pointe','roanoke','waynedale','bluffton road','southwood park','old mill','new haven','lincoln highway','anthony','mckinnie','georgetown','maplecrest','stellhorn','hospital','nurses','residents','pickup plant','trucks','steel','defense','pump','insurer','actuaries','university','colleges','music retailer','fighter wing','airport','orders','three rivers festival','johnny appleseed','parade','coliseum','outlet sale','1982 flood','levees','snow','1978 blizzard','ice','angola','marion','tornado','auburn','auction','indianapolis','chicago','detroit','columbus','cincinnati','cleveland','louisville','nashville','dallas','orlando','michigan','texas','ohio','toledo'],
}, BODY, FAQ)
