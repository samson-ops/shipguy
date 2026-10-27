import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Nampa, Idaho','Car shipping on the west side of the Treasure Valley, where Interstate 84 meets the Karcher interchange',
 ['Car shipping in Nampa starts along Interstate 84, which crosses the city with five exits in six miles. Ship Guy is a licensed auto transport broker with an office on East Franklin Road.',
  'We book vetted carriers across Canyon County, from Caldwell to Kuna and down to Lake Lowell. We do not own the trucks.',
  'Interstate 84 runs through the north side of the city from the Karcher interchange to the Garrity exit. Highway 55 is Karcher Road west to Marsing. Highway 45 is 12th Avenue, the road south to the river. Caldwell Boulevard, Garrity Boulevard, and Franklin carry the rest.',
  'This page covers the interstate, the Karcher side, downtown, the north side, the farm roads, and Caldwell. It also covers the warehouse, the plants, the campuses, the sugar campaign, the rodeo, and the lanes.'],
 'Nampa at a glance',
 ['Most pickups happen within 1 to 3 days. Interstate 84 brings the Portland carriers through the Karcher interchange before they reach Boise.',
  'Portland and Salt Lake City are a day away, and Spokane is the same. Seattle, Reno, and Sacramento need one to two. Las Vegas, Los Angeles, and Denver need two, and the Midwest needs three to four.'],
 'Tell us the side of the interstate. Downtown and the old blocks by the college need a meeting spot. The north side, the Karcher subdivisions, and South Nampa usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 84, Karcher Road, Garrity Boulevard, 12th Avenue, and Caldwell Boulevard',
 prose(
  L('Nampa is the first Treasure Valley city a westbound carrier reaches, and the interstate runs straight through it.'),
  P('Interstate 84 enters from Caldwell at the Karcher interchange and runs through the north side of the city. The exits at Karcher, Midland, Northside, Franklin, and Garrity are six miles apart end to end. Every carrier between Portland and Salt Lake City passes all five, and the Portland trucks reach Nampa first.'),
  P('Karcher Road is Highway 55 west of the interstate, the road to Marsing and the Owyhees. The Karcher interchange has the newest retail on the west side. Caldwell Boulevard is US 20 and 26, the old strip between the two cities. Garrity Boulevard runs from the interstate to the event center and the warehouses on the north side.'),
  P('12th Avenue is Highway 45, the road through downtown and south to the river. 11th Avenue and 3rd Street cross the old grid. Franklin Boulevard runs the north side past the campus. Midland Boulevard carries the west side. Greenhurst, Amity, Lake Lowell Avenue, and Happy Valley Road reach the farms and the subdivisions to the south.'),
  P('The carriers come off 84 at Karcher, Franklin, and Garrity. The lots at the event center, at Karcher, and along Garrity are the usual meeting spots. No road in Canyon County charges a toll.'),
  P('Our office sits on East Franklin Road by the event center, a minute from the Franklin exit.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the College Blocks, the North Side, Karcher, South Nampa, and Caldwell',
 prose(
  L('Nampa is a railroad town with a farm town around it, and both are filling in with subdivisions.'),
  P('Downtown is a tight grid of one-way streets around the old depot. A trailer cannot stop on 1st or 2nd Street. The driver meets you on 12th Avenue or at the library lot. The blocks around the college on Holly Street and Dewey Avenue are old grids with narrow streets. The campus lots work for a handoff.'),
  P('The north side along Garrity and Franklin has the event center, the warehouses, and the campus. There is room everywhere. The curb works on the postwar grids off Northside Boulevard. The Karcher side on the west has subdivisions from the last twenty years with wide streets. The truck reaches the curb.'),
  P('South Nampa along Greenhurst, Amity, and Lake Lowell Avenue is a mix of farms and subdivisions. The subdivisions allow the curb. The farms sit on long gravel drives, and the driver meets you on the paved county road. The lake and the refuge sit at the end of the road. A lakeside pickup meets the truck in town.'),
  P('Caldwell next door has an old downtown along Indian Creek and a college on the hill. The driver meets you on Cleveland Boulevard or at a lot off the interstate. Middleton, Marsing, and Melba are farm towns with lots on every main street. Caldwell prices the same as Nampa, and so does Kuna across the county line.'),
 )))

ROUTES=[("Portland, OR","I-84 · ~410 mi","1 day","$360–$520"),("Salt Lake City, UT","I-84 · ~360 mi","1 day","$330–$470"),
 ("Spokane, WA","US-95 · ~410 mi","1 day","$360–$520"),("Seattle, WA","I-84/I-90 · ~480 mi","1 day","$400–$570"),
 ("Reno, NV","US-95 · ~400 mi","1 day","$360–$520"),("Sacramento, CA","I-84/I-80 · ~540 mi","1–2 days","$440–$640"),
 ("Las Vegas, NV","I-84/US-93 · ~650 mi","2 days","$480–$690"),("Los Angeles, CA","US-95/I-15 · ~870 mi","2 days","$590–$840"),
 ("Denver, CO","I-84/I-80 · ~840 mi","2 days","$570–$810"),("Chicago, IL","I-84/I-80 · ~1,720 mi","3–4 days","$1,000–$1,400")]
BODY.append(rate_table('Lanes &amp; Costs','Nampa Car Shipping Lanes and Estimated Costs',
 'The lanes Canyon County cars take most, with estimated open-trailer ranges. Your exact route prices on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates, priced from Nampa, running sedan, open trailer. SUVs and pickups cost 10 to 25 percent more, enclosed more still. West Coast demand, the winter, and carrier availability on your dates decide the final figure.',
 prose(
  P('Nampa prices a few dollars under Boise on the Portland lane, because the westbound carriers reach it first. The Salt Lake lane runs the other way and prices a few dollars over. The lanes from California, Washington, and Oregon run full with transplants, and the return legs run lighter.'),
  P('Denver and the Midwest ride 84 and 80 through Wyoming. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Warehouse, the Cheese Plant, the Hospitals, the Campuses, and the Transplants',
 prose(
  L('Nampa relocates warehouse managers, plant engineers, nurses, students, and families priced out of Boise. Most arrive on a closing date.'),
  P('The warehouse by the Garrity exit is one of the biggest employers in the county. It brings in managers and technicians from every state. The cheese plant on the east side and the electronics plant relocate engineers on program schedules. The sugar company’s factory hires on the campaign calendar. We supply the paperwork a reimbursed move needs.'),
  P('The two hospitals bring in nurses all year and residents each June. The university on Holly Street brings cars in each August. The community college on the north side does the same. An adult signs for a student car at a campus lot. The mission aviation group at the airport relocates pilots and mechanics on their own calendar.'),
  P('West Coast households reach Nampa on closing dates in every month. Many pick it for the prices west of Boise. One car ships while the other is driven. When a closing slips, the delivery window slips with it, so an early heads-up helps. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
  P('The Air Force base east of the valley rotates families year round. Some settle in Nampa and Caldwell. The orders move one car, and we move the other. Ship Guy is a private broker and has no connection to the base. The <a href="military-car-shipping.html">military</a> page covers the timing.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Stampede, the Sugar Campaign, the Inversion, Snow, and Smoke',
 prose(
  L('Nampa runs on a rodeo week, a sugar beet season, and the same valley winter as Boise.'),
  P('The Stampede fills the event center and every hotel in the county for a week in July. The parade closes downtown, and Garrity gridlocks around the grounds each evening. A pickup near the event center moves to another day or to Karcher. The county fair in Caldwell does the same at the end of the month.'),
  P('The sugar campaign runs from October into February. Beet trucks fill the farm roads and the interstate exits, and the factory runs around the clock. A carrier loses time behind the beet trucks on the county roads. A farm pickup in those months meets the truck on the highway.'),
  P('December and January bring the inversion, weeks of cold fog that the carriers drive through. Snow glazes the overpasses and the county roads a few times a winter. The 2017 storm closed the valley for days. The carriers park on 84, and a winter pickup may lose a day.'),
  P('Fire smoke settles into the valley from July through September, and the interstate stays open. Summer heat passes one hundred degrees in July, and the loading hour moves to the morning. Spring wind across the open ground west of the city slows a tall trailer.'),
 )+chips(["Downtown","The Depot","12th Avenue","Holly Street","Dewey Avenue","College Blocks","North Side","Garrity","Franklin","Event Center","Northside","Midland","Karcher","Karcher Interchange","Sunnyridge","South Nampa","Greenhurst","Amity","Lake Lowell","Happy Valley","Can-Ada","Caldwell","Indian Creek","Middleton","Marsing","Melba","Kuna"])
 +NOTE('Serving Nampa, Caldwell, and all of Canyon County, farm road or subdivision. Tell us the side of the interstate and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Nampa?',
 prose(
  L('Most cars leave Canyon County on an open trailer, and the coast lanes are priced that way.'),
  P('A closed trailer shields a car from road salt, smoke, and curious eyes. Families bringing a restored car up from California tend to book one. The garages in the Karcher subdivisions book them for the shows.'),
  P('A commuter car or a farm truck goes open and arrives fine. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages lay out the trade.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff at the event center or a lot on Karcher, and a delivery. The closing date sets the week.'),
  P('Say yes to the price, and we book a carrier already crossing the valley on 84. The lot and the window come back to you that day. At pickup, the driver checks the car with you and writes it up on a Bill of Lading. Both signatures go on, and the sheet is compared at delivery.'),
 )+ULI([
  "Clear the cabin and the trunk of anything personal",
  "Keep the fuel around a quarter tank",
  "Photograph every side of the car before the handoff",
  "Hand the driver a working key and mention any mechanical problem",
  "Disarm any aftermarket alarm",
  "From a farm road, meet the truck on the paved county road or in town",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Nampa Drivers Choose Ship Guy',
 prose(
  L('We catch the Portland carriers at the first exit in the valley. We plan around the closing date, the beet trucks, and the winter.'),
  P('Ship Guy is an active FMCSA broker with a $75,000 surety bond behind it. The federal register carries both. Our office is on East Franklin Road by the event center.'),
  P('The coordinator who quotes the move answers the phone until it is delivered. Open, enclosed, and expedited transport are on the <a href="services.html">services</a> page.'),
 ), alt=True))

BODY.append(office('Nampa','5700 E Franklin Rd #499B','Nampa, ID 83687','+12086461142','(208) 646-1142','MT',
 '5700+E+Franklin+Rd+%23499B,+Nampa,+ID+83687','Visit Us','Find Ship Guy in Nampa',
 'Our office is on East Franklin Road by the event center, a minute from the Franklin exit.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4442.655050604058!2d-116.5085878!3d43.60565869999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x54ae4d7b62f87f75%3A0xe830ad385d96f2d0!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792170061628!5m2!1sen!2sus'))

FAQ=[
 ("Can you time delivery to my closing date in Nampa?","Yes. Closings drive most Nampa bookings. Families come from California, Washington, and Oregon and pick Nampa for the prices. We build the delivery window around the closing, and it moves when the closing does. Tell us as soon as the date changes."),
 ("How much does it cost to ship a car from Portland or California to Nampa?","Portland runs three hundred sixty to five hundred twenty dollars for a sedan. That is about four hundred ten miles up 84. Sacramento runs four hundred forty to six hundred forty, about five hundred forty miles on 80 and 84. Los Angeles comes in between five hundred ninety and eight hundred forty. Inbound trailers run full, which holds those prices down. An SUV or pickup adds 10 to 25 percent."),
 ("Can the carrier come to my street downtown or by the college?","Usually not. Downtown is a one-way grid around the depot, and the college blocks on Holly and Dewey are narrow. The driver meets you on 12th Avenue, at the library lot, or at a campus lot. The north side, the Karcher subdivisions, and South Nampa usually allow the curb."),
 ("Can you pick up on a farm south of town?","Yes, on the paved road. A seventy-five-foot trailer stays off the gravel drives. The driver meets you on the county road or in town. From October into February, the beet trucks slow the farm roads. A farm pickup in those months meets the truck on the highway."),
 ("Does the Stampede affect my pickup?","Near the event center, yes. The rodeo fills every hotel in the county for a week in July. Garrity gridlocks around the grounds each evening. We move a pickup near the grounds to another day or to Karcher. The rest of the city runs normally."),
 ("Do you ship cars for employees relocating to the warehouse or the plants?","Yes, all year. The warehouse, the cheese plant, and the electronics plant hire managers and engineers from every state. Many ship a second car behind the move. The handoff works at the event center or a lot on Garrity. We provide the paperwork a reimbursed move needs."),
 ("What happens if snow or the inversion hits on my pickup day?","Inversion fog slows the roads and closes none of them, so the trucks keep moving. Snow glazes the overpasses and the county roads, and the carriers park on 84 until the plows finish. A winter pickup can lose a day, and you get a call before it does."),
 ("Can you ship a car to or from Caldwell or Kuna?","Yes, and both price the same as Nampa. Caldwell rides the same carriers off the Karcher interchange, and Kuna rides them off Can-Ada Road. The lots off the interstate in Caldwell work for a handoff. Send the full address for a new subdivision in Kuna."),
 ("Can you ship a car that does not run from Nampa?","Yes. A winch truck is sent, and the quote already carries the extra loading time. The event center lots or a lot on Karcher give the driver level ground. Note whether it rolls, steers, and brakes."),
 ("What do you need for a Nampa car shipping quote?","Where the car starts and ends, with the side of the interstate or the farm road here. Year, make, and model, and whether it drives. Open or enclosed. Dates that fit the closing. That is a full Nampa request."),
]
BODY.append(faq_section(FAQ,'Nampa FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Nampa?','Two minutes on the form above prices your lane. Send the side of the interstate and your dates, and a carrier already on 84 takes it.','+12086461142','(208) 646-1142','Get your free Nampa quote'))

build({
 'slug':'auto-transport-nampa-idaho',
 'title':'Car Shipping in Nampa, ID — Auto Transport | Ship Guy',
 'meta':'Car shipping in Nampa, ID on the west side of the Treasure Valley, where Interstate 84 meets the Karcher interchange. Closing-date deliveries for transplants, warehouse and plant relocations, downtown and college-block meeting spots, farm-road pickups, Caldwell and Kuna, the Stampede and the sugar campaign. Local office on East Franklin Road. Free quote.',
 'h1':'Car Shipping in<br>Nampa, <span class="accent">Idaho</span>',
 'lede':'Open, enclosed, and expedited auto transport across Canyon County, planned around 84, the Karcher interchange, the closing date, and the beet trucks.',
 'tel':'+12086461142','disp':'(208) 646-1142','brand':'Nampa','keyword':'car shipping in nampa',
 'localterms':['nampa','interstate 84','karcher','highway 55','marsing','highway 45','12th avenue','caldwell boulevard','us 20','garrity','franklin','northside','midland','11th avenue','3rd street','greenhurst','amity','lake lowell','happy valley','can-ada','event center','downtown','depot','one-way','library','holly street','dewey avenue','college','north side','warehouses','karcher side','south nampa','farms','gravel','refuge','caldwell','indian creek','cleveland boulevard','middleton','melba','kuna','warehouse','cheese plant','electronics plant','sugar','campaign','beet trucks','hospitals','nurses','residents','university','community college','mission aviation','airport','air force base','orders','closing date','transplants','california','washington','oregon','stampede','rodeo','parade','county fair','inversion','snow','2017','smoke','spring wind','portland','salt lake city','spokane','seattle','reno','sacramento','las vegas','los angeles','denver','chicago'],
}, BODY, FAQ)
