import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Lancaster, Pennsylvania','Car shipping where Route 30 skirts a brick city, the buggies share the two-lanes, and the October car meet in Hershey books every enclosed trailer',
 ['Car shipping in Lancaster runs on Route 30 and Route 283, the four-lanes to the interstates. Ship Guy is a licensed auto transport broker with an office on New Holland Avenue, northeast of downtown.',
  'We book vetted carriers across Lancaster, from the row houses downtown to the farms east of the city. Manheim Township, Millersville, Lititz, Ephrata, and Columbia ride the same trucks. Each truck belongs to its carrier. The license and the bond are Ship Guy’s.',
  'Route 30 loops the north side of the city as a freeway. East of there it carries the tourist strip to Ronks. Route 283 runs northwest to Harrisburg and the Turnpike. Route 222 runs north to Reading and south to Quarryville. Lititz Pike, Manheim Pike, Columbia Avenue, and the Old Philadelphia Pike carry the rest.',
  'This page covers 30, 283, 222, the pikes, downtown, the townships, and the farm country. It also covers the hospital, the colleges, the warehouses, the retirement villages, and the Hershey car meet. The buggies, the snow, and the Conestoga are here too.'],
 'Lancaster at a glance',
 ['Most Lancaster pickups land within 1 to 3 days. The city sits an hour from Philadelphia, Baltimore, and Harrisburg on roads carriers run daily. The Route 30 trucks pass the north side all day. The 283 trucks come down from the Turnpike.',
  'Harrisburg, Philadelphia, Baltimore, Washington, and New York are a same-day haul. Pittsburgh, Richmond, and Boston take a day. Charlotte takes one to two, and Florida takes three.'],
 'Tell us the street. Downtown, Cabbage Hill, and the Northwest meet the truck on Prince Street or at the ballpark lot. Manheim Township, East Hempfield, Millersville, and Lititz usually allow the curb. A farm lane means the main road.'))

BODY.append(sec('The Roads','Route 30, Route 283, Route 222, Route 501, Route 72, Route 23, Route 462, Lititz Pike, Manheim Pike, Columbia Avenue, and the Old Philadelphia Pike',
 prose(
  L('Lancaster has no interstate of its own, and the carriers never notice. Two four-lanes reach the Turnpike in thirty minutes either way.'),
  P('Route 30 is the Lincoln Highway. It runs as a freeway around the north of the city from Columbia to the Route 222 interchange. East of there it drops to a strip of outlets, motels, and buggy traffic through Ronks and Paradise. Route 283 leaves 30 at Rohrerstown and runs northwest past Mount Joy and Elizabethtown to Harrisburg. It meets the Turnpike at the Harrisburg East exit. Route 222 runs north through Ephrata to Reading and the Turnpike there. South of the city it runs to Willow Street and Quarryville.'),
  P('Lititz Pike is Route 501, north to Lititz. Manheim Pike is Route 72, out past the mall to Manheim. Fruitville Pike runs between them. Route 23 is New Holland Pike to the east and Marietta Avenue to the west. Route 462 is King Street, the old Lincoln Highway through Penn Square to Columbia. Columbia Avenue carries it west. Route 340 is the Old Philadelphia Pike through Bird-in-Hand and Intercourse, and Route 896 runs to Strasburg. Harrisburg Pike runs to the campus and the mall. The buggies use every one of them.'),
  P('The carriers come off 30 at Fruitville Pike, Lititz Pike, or Route 222. They meet at the outlet lots on 30 or the mall lots at Harrisburg Pike. The big-box lots on Lititz Pike work too. The ballpark lot on North Prince Street works outside game nights. So do the lots at the Rockvale outlets and the truck stops at the 283 exits. The airport in Lititz is small, and Harrisburg’s airport is thirty-five minutes up 283 for a fly-and-ship. The train station on McGovern Avenue runs to Philadelphia and New York all day.'),
  P('Our office sits on New Holland Avenue, northeast of downtown, minutes from Route 30 and the train station.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, Cabbage Hill, the Northwest, School Lane Hills, Manheim Township, East Hempfield, Millersville, Lititz, Ephrata, Columbia, Mount Joy, Elizabethtown, Strasburg, and the Farm Country',
 prose(
  L('Lancaster is a brick city of narrow streets ringed by postwar townships and then by farms. The truck meets the city on a main road and the townships at the curb. The farms mean the pike.'),
  P('Downtown is Penn Square, Central Market, and blocks of row houses on one-way streets. The alleys are tight, and the parking is permit. No trailer fits. The driver meets you on Prince Street, Queen Street, or at the ballpark lot. Cabbage Hill southwest of downtown is steep brick streets of row houses. The handoff moves to Manor Street or Columbia Avenue. The Northwest and Chestnut Hill are row houses under old trees near the college. The handoff happens on Harrisburg Avenue. The Southeast is the same brick grid, and the handoff happens on Duke Street or South Prince.'),
  P('School Lane Hills and Grandview Heights are big houses on curving streets with low limbs. The driver meets you on Marietta Avenue or Harrisburg Pike. Manheim Township is Neffsville, Grandview, and the subdivisions off Lititz Pike and Fruitville Pike. The streets are wide, and the curb works. East Hempfield is Rohrerstown, Landisville, and the developments off Route 283. The curb works there too. Lancaster Township and Millersville are postwar grids around the university. Student streets fill in August, and the handoff moves to the campus lots.'),
  P('Lititz is a tight borough center with a huge production campus on the edge. The handoff happens on Route 501. Ephrata, Columbia, Marietta, Mount Joy, and Elizabethtown are old boroughs with alleys and a main street. The driver meets you at a lot on the edge of town. Strasburg, Bird-in-Hand, Intercourse, and New Holland are villages among the farms. The farm lanes are gravel and a mile long, and the trailer stays on the pike. A buggy ahead of the truck sets the pace.'),
  P('Manheim Township, East Hempfield, Millersville, Lititz, and Ephrata ride the same trucks. They price the same as the city. Columbia, Mount Joy, Elizabethtown, and Strasburg do too. Quarryville and the southern end add a day for the farm roads. York across the river prices the same and ships the same day.'),
 )))

ROUTES=[("Harrisburg, PA","PA-283 · ~40 mi","Same day","$130–$210"),("Philadelphia, PA","US-30/US-202 · ~70 mi","Same day","$150–$240"),
 ("Baltimore, MD","US-222/I-83 · ~75 mi","Same day","$150–$240"),("Washington, DC","I-83/I-95 · ~125 mi","Same day","$180–$290"),
 ("New York, NY","US-222/I-78 · ~160 mi","Same day","$210–$320"),("Richmond, VA","I-83/I-95 · ~225 mi","1 day","$240–$360"),
 ("Pittsburgh, PA","Turnpike · ~245 mi","1 day","$250–$380"),("Boston, MA","I-78/I-84/I-90 · ~340 mi","1 day","$300–$440"),
 ("Charlotte, NC","I-83/I-81/I-77 · ~470 mi","1–2 days","$400–$580"),("Orlando, FL","I-95 · ~980 mi","3 days","$700–$1,000")]
BODY.append(rate_table('Lanes &amp; Costs','Lancaster Car Shipping Lanes and Estimated Costs',
 'The lanes Lancaster County cars travel most often, with open-trailer estimates. The form above prices your exact lane.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Lancaster, running sedan, open trailer. An SUV or a pickup adds 10 to 25 percent, and enclosed sits higher. The week you ship and the trucks on Route 30 that week set the figure.',
 prose(
  P('Lancaster sits inside a triangle of cheap lanes. Philadelphia, Baltimore, and Harrisburg are each an hour away. The carriers between them pass the county every day. New York rides 222 and 78 through Allentown. Washington rides 83 through York. The Turnpike carries Pittsburgh and Ohio. The Florida lane fills each fall with the snowbirds from the retirement villages.'),
  P('A late-August move-in at the colleges or the Hershey meet week means a busy week. The <a href="car-shipping-cost.html">cost guide</a> explains size, condition, and timing one at a time.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Hospital, the Colleges, the Flooring Headquarters, the Food Plants, the Warehouses on 283, the Production Campus in Lititz, the Retirement Villages, and the Guard at the Gap',
 prose(
  L('Lancaster relocates nurses, students, plant managers, warehouse staff, and retirees. The hospital and the colleges move the most.'),
  P('The hospital system downtown brings residents each June and nurses all year. The handoff happens on Duke Street or at the campus garages. Franklin and Marshall College fills the Northwest each late August. Millersville University fills its borough the same week. Elizabethtown College and Thaddeus Stevens follow. A parent books the car, and an adult signs at the campus lot. The cars go home in May.'),
  P('The flooring maker’s headquarters on the west side relocates managers on start dates. The food plants do too. The dairy in Conestoga, the pretzel bakeries, and the meat packers hire from across the state. The warehouses along Route 283 and the Turnpike relocate supervisors in spring and fall. The production campus in Lititz builds the stages for arena tours and moves crews between cities. The handoff happens at the lots nearest the plant. When the employer pays for the car, we write the paperwork their way.'),
  P('The retirement villages south of the city and in Elizabethtown bring retirees from New Jersey, Philadelphia, and Maryland. Some go to Florida each winter and ship the car both ways. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the paperwork a state line adds.'),
  P('Fort Indiantown Gap trains Guard units thirty miles north, and its full-time staff rotate on orders. The Navy’s supply base and the Army depot near Harrisburg relocate civilians on the same calendar. Ship Guy is a private broker and not part of the Guard. The <a href="military-car-shipping.html">military</a> page covers orders and the dates they set.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Market Days, First Friday, the Fall Tourist Traffic, the Ephrata Fair, the Hershey Car Meet, Move-In Week, the Blizzards, and the Conestoga',
 prose(
  L('Lancaster runs on a tourist calendar and a college calendar. The weather problem is a blizzard every few winters and a river that climbs its banks.'),
  P('Central Market opens Tuesday, Friday, and Saturday and fills the blocks around Penn Square. First Friday closes Gallery Row each month. The fall tourist traffic crawls along Route 30 and Route 340 every October weekend. The Ephrata Fair closes downtown Ephrata for a week in late September. The New Holland fair follows in October. The antique car meet in Hershey each October books every enclosed trailer in the region. The Carlisle shows run from April to October. Move-in week fills Millersville and the Northwest in late August. Give a meet week or a move-in date three weeks of notice.'),
  P('The January 2016 blizzard set the county record, nearly twenty-eight inches in a day. The twin storms of February 2010 did nearly as much. The state shuts the Turnpike and 83 to trucks in a storm. The carriers wait in Harrisburg or Philadelphia. A winter pickup can slip two days. Lee in September 2011 put the Conestoga over its banks and closed the low roads for days. Agnes in 1972 put Columbia and Marietta under the Susquehanna.'),
  P('A February 2016 tornado crossed the eastern county. Fog settles in the river valleys on fall mornings. A buggy on an icy two-lane sets the pace for the truck behind it. Summer brings heat and an afternoon storm that passes in an hour.'),
 )+chips(["Downtown","Penn Square","Gallery Row","Cabbage Hill","The Northwest","Chestnut Hill","Musser Park","The Southeast","School Lane Hills","Grandview Heights","Manheim Township","Neffsville","East Hempfield","Rohrerstown","Landisville","Lancaster Township","Millersville","Lititz","Ephrata","Columbia","Marietta","Mount Joy","Elizabethtown","Strasburg","Bird-in-Hand","Intercourse","New Holland","Leola","Willow Street","Quarryville","York"])
 +NOTE('Serving Lancaster, Lancaster County, and the river towns, brick row house or farm lane. Give us the street and tell us whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Lancaster?',
 prose(
  L('Open trailers carry most of the county’s cars, and the table above assumes one.'),
  P('Enclosed keeps the road brine, the barn dust, and the spring hail off the paint. The collectors headed to the Hershey meet book it. So do the retirees moving a car worth more than the move itself. When a storm is coming and only an open truck has room, you hear that first.'),
  P('A commuter car or a student’s hatchback rides open and arrives fine. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages lay out the difference.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A figure, a lot off Route 30, and a signature when the car comes down the ramp. Your move-in or your start date picks the week.'),
  P('Approve the figure, and we assign the car to a carrier already running 30 or 283 that week. You get the lot and the window the same day. At pickup the driver photographs the car and writes its condition on the Bill of Lading. You initial it, and it becomes the reference at delivery.'),
 )+ULI([
  "Your things out of the cabin and the trunk",
  "A quarter tank of fuel or less",
  "Photos of every side and the odometer the morning of pickup",
  "A working key and a note on anything that acts up",
  "Aftermarket alarms switched off",
  "Downtown, on Cabbage Hill, or on a farm lane, expect a lot on Route 30",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> page walks through the steps, and the <a href="car-shipping-preparation.html">preparation</a> page covers pickup morning.'))))

BODY.append(sec('Why Ship Guy','Why Lancaster Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already run Route 30 and 283 past the county every day. We know which October weekends jam the strip and which lanes take a trailer.'),
  P('Our FMCSA license and our $75,000 bond are public record on the federal register. The office is on New Holland Avenue.'),
  P('One person at Ship Guy handles your move from the first figure to the delivery call. The <a href="services.html">services</a> page describes open, enclosed, and expedited in turn.'),
 )))

BODY.append(office('Lancaster','800 New Holland Avenue Rear #547','Lancaster, PA 17601','+17173732385','(717) 373-2385','ET',
 '800+New+Holland+Avenue+Rear+%23547,+Lancaster,+PA+17601','Visit Us','Find Ship Guy in Lancaster',
 'Our office sits on New Holland Avenue, northeast of downtown, minutes from Route 30 and the train station.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3769.9046293875676!2d-76.28694589999999!3d40.0508703!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c625ed33789995%3A0x5d498208c31ad32e!2sShip%20Guy%20Auto%20Transport!5e1!3m2!1sen!2sus!4v1794237059016!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Lancaster to Philadelphia or Baltimore?","Either one runs one hundred fifty to two hundred forty dollars for a sedan. Each is about seventy-five miles away. Harrisburg is the lowest lane on the table, forty miles up Route 283. New York runs two hundred ten to three hundred twenty. An SUV or a pickup adds 10 to 25 percent."),
 ("Can the carrier come down a farm lane in the Amish country?","No. The lanes are gravel, a mile long, and built for a buggy. The trailer stays on the pike. The driver meets you where the lane meets Route 340 or 896. A buggy ahead of the truck sets the pace. The figure does not change."),
 ("Can the carrier reach my row house downtown or on Cabbage Hill?","No. The one-way streets and the alleys are too tight, and the parking is permit. The driver meets you on Prince Street, Queen Street, or Manor Street, or at the ballpark lot. Manheim Township, East Hempfield, and Millersville usually allow the curb."),
 ("Can you ship a car for a Franklin and Marshall or Millersville student?","Yes. The cars arrive in late August and leave in May. A parent books, and an adult signs at the campus lot. The Northwest and the Millersville streets are closed to a trailer that week. The window follows your move-in date."),
 ("What happens to a pickup during the fall tourist traffic?","Route 30 and Route 340 crawl every October weekend from Ronks to Intercourse. A carrier plans the eastern pickups for a weekday morning or moves the handoff to the outlet lots. The figure stays the same. Give an October weekend date three weeks of notice."),
 ("Can you ship a collector car to the Hershey meet in October?","Yes, and book early. The antique car meet in Hershey books every enclosed trailer in the region that week. The Carlisle shows from April to October do the same. An enclosed truck keeps the brine and the hail off the paint. We tell you when a week is already full."),
 ("What happens if a blizzard hits on my pickup day?","The truck waits in Harrisburg or Philadelphia until the roads reopen, usually a day. The January 2016 blizzard dropped nearly twenty-eight inches in a day and closed the county for two. We call as soon as the forecast turns. The pickup moves to the first clear morning, and the figure stays put."),
 ("Can you ship a car to or from Lititz, Ephrata, or Columbia?","Yes. Lititz, Ephrata, Manheim Township, East Hempfield, and Millersville ride the same carriers. They price the same as the city. Columbia, Mount Joy, Elizabethtown, and Strasburg do too. Quarryville and the southern end add a day for the farm roads. York across the river ships the same day."),
 ("Can you ship a car that does not run from Lancaster?","Yes. The carrier brings a winch, and the figure includes the loading time. The outlet lots on Route 30 and the mall lots at Harrisburg Pike are flat. Tell us if it rolls, steers, and brakes."),
 ("What do you need for a Lancaster car shipping quote?","Both addresses, down to the street. The year, make, and model, and whether it runs. Open or enclosed, and the week you need. With those, your Lancaster figure comes back the same day."),
]
BODY.append(faq_section(FAQ,'Lancaster FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Lancaster?','Two minutes on the form above puts a Lancaster figure on your lane. Give us the street and the week, and a carrier already on Route 30 takes it from there.','+17173732385','(717) 373-2385','Get your free Lancaster quote'))

build({
 'slug':'auto-transport-lancaster-pennsylvania',
 'title':'Car Shipping in Lancaster, PA — Auto Transport | Ship Guy',
 'meta':'Car shipping in Lancaster, PA, on Route 30, Route 283, and Route 222. Row houses downtown, farm lanes in the Amish country, the colleges, the hospital, the warehouses on 283, the retirement villages, the Hershey car meet, and the blizzards. Local office on New Holland Avenue. Free quote.',
 'h1':'Car Shipping in<br>Lancaster, <span class="accent">Pennsylvania</span>',
 'lede':'Open, enclosed, and expedited auto transport across Lancaster, Lancaster County, and the river towns, planned around Route 30, the buggies, the college dates, the tourist weekends, the Hershey meet, and the snow.',
 'tel':'+17173732385','disp':'(717) 373-2385','brand':'Lancaster','keyword':'car shipping in lancaster',
 'localterms':['lancaster','route 30','route 283','route 222','route 501','route 72','route 23','route 462','route 340','route 896','lincoln highway','lititz pike','manheim pike','fruitville pike','columbia avenue','old philadelphia pike','harrisburg pike','new holland pike','marietta avenue','king street','turnpike','rohrerstown','ronks','paradise','downtown','penn square','central market','gallery row','row houses','one-way streets','permit','prince street','queen street','ballpark','cabbage hill','manor street','the northwest','chestnut hill','musser park','harrisburg avenue','the southeast','duke street','school lane hills','grandview heights','low limbs','manheim township','neffsville','east hempfield','landisville','lancaster township','millersville','lititz','production campus','ephrata','columbia','marietta','mount joy','elizabethtown','strasburg','bird-in-hand','intercourse','new holland','leola','willow street','quarryville','york','farm lanes','gravel','buggy','buggies','pike','hospital system','franklin and marshall','millersville university','thaddeus stevens','flooring maker','dairy','conestoga','pretzel bakeries','meat packers','warehouses','arena tours','retirement villages','snowbirds','fort indiantown gap','guard','supply base','army depot','market days','first friday','tourist traffic','ephrata fair','new holland fair','hershey','car meet','antique car meet','enclosed trailer','carlisle shows','move-in','january 2016','twenty-eight inches','february 2010','lee','september 2011','agnes','1972','susquehanna','february 2016 tornado','fog','river valleys','outlet lots','mall lots','big-box lots','rockvale','truck stops','airport','fly-and-ship','train station','mcgovern avenue','new holland avenue','harrisburg','philadelphia','baltimore','washington','new york','richmond','pittsburgh','boston','charlotte','orlando','brine','barn dust','hail','bill of lading','fmcsa','winch'],
}, BODY, FAQ)
