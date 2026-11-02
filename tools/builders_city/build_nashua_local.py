import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Nashua, New Hampshire','Car shipping on the state line, where the Boston commute meets a city with no sales tax',
 ['Car shipping in Nashua runs on the Everett Turnpike, forty-five miles from Boston and twenty from Manchester. Ship Guy is a licensed auto transport broker with an office on Northeastern Boulevard in southwest Nashua.',
  'We book vetted carriers across Nashua, from French Hill to the South End and out to Hudson. The carriers own the trucks. Ship Guy holds the license and the bond.',
  'The Everett Turnpike is Route 3, the road south to Lowell and 495 and north to Manchester. Route 101A is Amherst Street, west to Milford. Route 111 crosses the city and the river to Hudson. Daniel Webster Highway is the strip along the state line. Main Street is the old road through the mills.',
  'This page covers the turnpike, 101A, 111, Daniel Webster Highway, downtown, French Hill, and the Tree Streets. It also covers the Boston commute, the tax migration, the defense campus, the colleges, and the nor’easters.'],
 'Nashua at a glance',
 ['Most pickups happen within 1 to 3 days. The Boston pool is forty-five minutes down the turnpike. The 495 carriers pass the state line all day. The Florida trucks load along the strip every week.',
  'Boston, Manchester, Worcester, and Providence ride a single day on the truck. Portland, Hartford, and Albany take a day. New York takes one, Philadelphia and Washington take one to two, and Florida takes three.'],
 'Tell us the neighborhood. French Hill, the Tree Streets, and downtown meet the truck on a main road. The North End, the Southwest subdivisions, and the grids off Broad Street usually allow the curb.'))

BODY.append(sec('The Roads','The Everett Turnpike, Route 101A, Route 111, Route 130, Daniel Webster Highway, Main Street, and the Bridges',
 prose(
  L('Nashua is a mill town on two rivers with a turnpike through the middle. A carrier picks its exit and never crosses downtown.'),
  P('The Everett Turnpike is Route 3. It runs the length of the city from the state line to Merrimack. The Spit Brook exit serves the South End and the strip. The Hollis Street exits serve the west side and downtown, and the Amherst Street exits serve the northwest. South of the line it runs to Lowell and 495. From there 93 and 95 are twenty minutes away. North it runs to Manchester and the airport. The toll north of the city rides inside the quote.'),
  P('Route 101A is Amherst Street, the road west through the big-box strip to Milford. Route 111 is Hollis Street on the west side. It crosses the river on the Taylor Falls Bridge to Hudson. Route 130 is Broad Street through the northwest. Daniel Webster Highway runs along the Merrimack from the mall at the state line to the South End. Main Street is the old road through the mills and downtown, two lanes and slow. Three bridges cross the Merrimack to Hudson, and all three back up at five.'),
  P('The carriers come off the turnpike at Spit Brook or Amherst Street. The mall lots at the state line are the usual meeting spot. The big-box lots on Amherst Street work too. So do the lots along Daniel Webster Highway and the stadium lot on Amherst Street outside a game. The airport in Manchester is fifteen miles up the turnpike for a fly-and-ship.'),
  P('Our office is on Northeastern Boulevard in southwest Nashua, between Exits 4 and 5 of the Everett Turnpike.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, the Millyard, French Hill, the Tree Streets, Crown Hill, the North End, the South End, the Southwest, the Northwest, and Hudson',
 prose(
  L('Nashua is dense mill-town streets near the river and postwar subdivisions on every edge. The truck meets the old streets on a main road.'),
  P('Downtown runs along Main Street from the river bridge north to the library. It is brick blocks and the old mills along the canal. The lofts in the Millyard have tight lots and no room for a trailer. The driver meets you at the Main Street lots or on Hollis Street. French Hill northeast of downtown is triple-deckers on narrow streets climbing from the river. A trailer does not enter. The handoff moves to Canal Street or Bridge Street.'),
  P('The Tree Streets west of Main are the same density on a flat grid. The driver meets you on Kinsley or Hollis Street. Crown Hill east of Main and south of the river is older houses on short blocks. Some allow the curb. The North End along Concord Street is big houses on wide lots around the park. The curb works on most of it, and the oaks are the only problem.'),
  P('The South End off Spit Brook Road is condo complexes and the defense campus. The complexes have one entrance, and the handoff happens at the gate or on Daniel Webster Highway. The Southwest off Hollis Street and Main Dunstable Road is subdivisions from the sixties on, wide and quiet. The truck reaches the curb. The Northwest off Amherst and Broad Streets is the same. The airport sits at the edge of it.'),
  P('Hudson across the river ships with the same trucks and prices the same as Nashua. So do Merrimack, Hollis, Amherst, and Litchfield. Milford and Pelham add a few miles and nothing else. Lowell and Tyngsborough across the line price with the city too.'),
 )))

ROUTES=[("Manchester, NH","US-3 · ~20 mi","Same day","$120–$200"),("Boston, MA","US-3/I-95 · ~45 mi","Same day","$150–$240"),
 ("Worcester, MA","US-3/I-495/I-290 · ~55 mi","Same day","$150–$240"),("Providence, RI","I-495/I-95 · ~85 mi","Same day","$170–$280"),
 ("Hartford, CT","I-495/I-90/I-84 · ~120 mi","Same day","$190–$300"),("Portland, ME","I-93/I-95 · ~120 mi","Same day","$200–$310"),
 ("New York, NY","I-495/I-84/I-684 · ~230 mi","1 day","$280–$410"),("Philadelphia, PA","I-84/I-287/I-95 · ~320 mi","1 day","$330–$480"),
 ("Washington, DC","I-84/I-81/I-95 · ~470 mi","1–2 days","$400–$570"),("Orlando, FL","I-95 · ~1,350 mi","3 days","$820–$1,160")]
BODY.append(rate_table('Lanes &amp; Costs','Nashua Car Shipping Lanes and Estimated Costs',
 'The lanes southern New Hampshire cars run most, with estimated open-trailer ranges. Price your own route on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Nashua, sedan that runs, on an open trailer. An SUV or a pickup runs 10 to 25 percent higher, and enclosed higher still. The turnpike toll rides inside the figure where the route uses it. The week and the carriers free on 495 that week set the final figure.',
 prose(
  P('Nashua prices like the top of the Boston pool, which is what it is. The Boston lane rides the turnpike and 3 and fills in both directions every day. The Connecticut and New York lanes ride 495 to 90 and 84. The Florida lane rides 95 the whole way and fills each October with the snowbirds. The Maine lane rides 101 and 95 up the Seacoast.'),
  P('A move-in date in late August or the first week of September lands in the busiest days. What size, condition, and timing do to the figure is in the <a href="car-shipping-cost.html">cost guide</a>.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Tax Migrants, the Boston Commuters, the Defense Campus, the Two Hospitals, the Tech Parks, the Colleges, and the Snowbirds',
 prose(
  L('Nashua relocates engineers, nurses, commuters, and retirees. The households moving north from Massachusetts move the most.'),
  P('No sales tax and no income tax on wages pull households over the line every month. Most ship one car and drive the other, and the Boston lane runs full both ways. The commuters work in Burlington, Waltham, and along 128 and drive the turnpike and 3 every morning. The mall at the state line was built so the stores sit on the New Hampshire side. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the paperwork for crossing a state line.'),
  P('The defense electronics campus on Spit Brook Road is the largest employer in the city. It brings engineers on contract starts all year and moves them between sites. The tech parks at the turnpike exits hire the same way. The two hospitals, one downtown and one on Kinsley Street, bring residents each June. Both hire traveling nurses year round. When an employer covers the move, we write up whatever it asks for.'),
  P('The university at the south end of Main Street takes student cars in late August. The community college on Amherst Street does the same, and the universities in Manchester and Durham follow. A parent books, and an adult meets the driver at a lot to sign. The cars go home in May.'),
  P('Retirees leave for Florida in October and November and come back in April. The Villages, Naples, and Sarasota are the usual addresses. The lane is the busiest long lane out of the city.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Holiday Stroll, the Fourth, Move-In Week, the Boston Moving Day, the Snowbirds, Mud Season, the Nor’easters, the Ice, and the Floods',
 prose(
  L('Nashua runs on a Boston calendar and a snowbird calendar. The weather problem is a winter that arrives in December and leaves in April.'),
  P('The holiday stroll closes Main Street on the Saturday after Thanksgiving. The Fourth fills the stadium on Amherst Street. Move-in week in late August fills the blocks around the university. The first of September is Boston’s moving day. Every carrier in New England is in the city that week. The snowbirds leave in October and November and fill the Florida trucks. Book three weeks ahead for a date in the last week of August.'),
  P('The nor’easters run from December into March. The February 2013 storm dropped two feet and stopped the turnpike for a day. March 2018 brought three in two weeks. The December 2008 ice storm put half the state in the dark for a week. The carriers waited in Lowell until the roads cleared. A storm shifts a pickup to the first clear morning, and the price does not change. Mud season in March and April posts the dirt roads in Hollis and Amherst. A trailer meets you on the pavement.'),
  P('The rivers flood in a wet spring. The May 2006 storm put the Nashua River over its banks downtown. The low roads closed for days. The April 2007 storm did it again. A handoff near the river moves to the strip for a day.'),
  P('Summer brings humidity and an afternoon storm a few times a week. The storm shifts the loading hour and nothing else. The leaf traffic in October fills 93 and 3 on the weekends. A Friday handoff moves to the morning.'),
 )+chips(["Downtown","Main Street","The Millyard","Railroad Square","Library Hill","French Hill","The Tree Streets","Crown Hill","The North End","Greeley Park","Concord Street","The South End","Spit Brook Road","Daniel Webster Highway","The Mall","The Southwest","Main Dunstable Road","Hollis Street","The Northwest","Amherst Street","Broad Street","The Airport","Hudson","Merrimack","Hollis","Amherst","Litchfield","Milford","Pelham","Tyngsborough"])
 +NOTE('Serving Nashua and the whole of southern New Hampshire, French Hill block or Southwest cul-de-sac. Tell us the neighborhood and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Nashua?',
 prose(
  L('Open trailers carry most of southern New Hampshire, and the table above is priced for one.'),
  P('An enclosed trailer keeps off the road salt, the brine, and the sand the plows leave behind. The collectors in the North End book one. So do the snowbirds sending a car worth more than the rest of the move. A car leaving ahead of a nor’easter rides whatever truck has room, and we say that plainly.'),
  P('A commuter car or a student’s car is fine in the open. Compare the two on the <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A figure, a lot at the mall, and a signature at the far end. The closing date or the move-in sets the week.'),
  P('Approve the figure, and a carrier already passing on 495 that week gets the car. We fix the lot and the window the same afternoon. The driver photographs the car at pickup and records its condition on the Bill of Lading. Your initials go on it, and delivery is checked against it.'),
 )+ULI([
  "Everything personal out of the cabin and the trunk",
  "Fuel down to a quarter tank",
  "Photograph each side and the odometer before the truck comes",
  "One good key, and a note about any known faults",
  "Any add-on alarm turned off",
  "In French Hill, the Tree Streets, or the Millyard, expect a main road",
 ])+prose(P('The order of events is on the <a href="how-it-works.html">how it works</a> page. The pickup list is on the <a href="car-shipping-preparation.html">preparation</a> page.'))))

BODY.append(sec('Why Ship Guy','Why Nashua Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already run the turnpike and 495 every day. We know which week Boston moves and takes every truck with it.'),
  P('Our FMCSA license and our $75,000 bond are a public record on the federal register. The office is on Northeastern Boulevard in southwest Nashua.'),
  P('One coordinator stays with your move from the quote to the delivery signature. The <a href="services.html">services</a> page lays out open, enclosed, and expedited.'),
 )))

BODY.append(office('Nashua','74 Northeastern Blvd #774','Nashua, NH 03062','+18023088118','(802) 308-8118','ET',
 '74+Northeastern+Blvd+%23774,+Nashua,+NH+03062','Visit Us','Find Ship Guy in Nashua',
 'Our office is on Northeastern Boulevard in southwest Nashua, between Exits 4 and 5 of the Everett Turnpike.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3617.3562387597326!2d-71.48466379999999!3d42.7351245!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89e3b7fe41319ed5%3A0x2496a45253ec6c69!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793630042105!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Nashua to Florida or New York?","Orlando runs eight hundred twenty to eleven hundred sixty dollars for a sedan. That is about thirteen hundred fifty miles down 95. New York runs two hundred eighty to four hundred ten, about two hundred thirty miles. Boston is forty-five miles away and the lowest lane on the table after Manchester. An SUV or a pickup runs 10 to 25 percent higher."),
 ("Is the turnpike toll in my price?","Yes, when the route uses it. Carriers pay the toll north of the city and the Massachusetts tolls on 90 and price accordingly. There is no separate line at delivery. Route 3 south to Lowell and 495 carries no toll."),
 ("Can the carrier come to my street in French Hill or the Tree Streets?","No. Both are dense streets of triple-deckers with cars on both curbs, and a trailer does not enter. The driver meets you on Canal Street, Kinsley Street, or Hollis Street. The North End, the Southwest subdivisions, and the grids off Broad Street usually allow the curb."),
 ("Why do so many people ship cars into Nashua from Massachusetts?","Because households move over the line for the taxes every month. Most ship one car while driving the other. The Boston lane runs full in both directions, which keeps it the lowest-cost lane out of the state. The mall at the state line and the turnpike exits are the usual meeting spots."),
 ("Can you deliver on a Rivier or Nashua Community College move-in date?","Yes. The university takes cars in late August, and the community college follows the same week. Mom or Dad books, and an adult signs at a lot. The first of September is Boston’s moving day, so a date that week wants three weeks of notice."),
 ("Do you ship cars for the defense campus and the hospitals?","Yes, every week of the year. The campus on Spit Brook Road brings engineers on contract starts and moves them between sites. The handoff happens on Daniel Webster Highway. The two hospitals bring residents each June and traveling nurses in every season. When the employer reimburses the move, the documentation comes from us."),
 ("Can you ship a car to or from Hudson, Manchester, or Lowell?","Yes. Hudson, Merrimack, and Hollis ride the same carriers and price the same as Nashua. Manchester is twenty miles up the turnpike and prices with the city. Lowell and Tyngsborough across the line do too. Milford and Pelham add a few miles and nothing else."),
 ("What happens if a nor’easter hits on my pickup day?","The truck holds in Lowell or Manchester until the plows finish, usually a day. We call as soon as the forecast turns. The pickup goes to the next clear morning, and the figure stays put. Give a February date a flexible week."),
 ("Can you ship a car that does not run from Nashua?","Yes. We send a carrier with a winch and price the loading time into the quote. The mall lots and the big-box lots on Amherst Street are flat. Tell us if it rolls, steers, and brakes."),
 ("What do you need for a Nashua car shipping quote?","Both addresses with the neighborhood. The year, make, and model, and whether it runs. Open or enclosed, and the week around the move-in or the closing. With those, the Nashua figure comes back the same day."),
]
BODY.append(faq_section(FAQ,'Nashua FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Nashua?','Two minutes on the form above gets your lane a Nashua figure. Name the neighborhood and the week, and a carrier already passing on 495 takes it.','+18023088118','(802) 308-8118','Get your free Nashua quote'))

build({
 'slug':'auto-transport-nashua-new-hampshire',
 'title':'Car Shipping in Nashua, NH — Auto Transport | Ship Guy',
 'meta':'Car shipping in Nashua, NH, on the state line forty-five miles from Boston. Tax-migration moves from Massachusetts, the snowbird lane to Florida, defense campus and hospital relocations, main-road handoffs for French Hill and the Tree Streets, curbside pickups in the North End and the Southwest, and the nor’easters. Local office on Northeastern Boulevard. Free quote.',
 'h1':'Car Shipping in<br>Nashua, <span class="accent">New Hampshire</span>',
 'lede':'Open, enclosed, and expedited auto transport across Nashua and southern New Hampshire, planned around the turnpike, 495, the Boston commute, the campus calendar, and the winter.',
 'tel':'+18023088118','disp':'(802) 308-8118','brand':'Nashua','keyword':'car shipping in nashua',
 'localterms':['nashua','state line','boston','sales tax','everett turnpike','route 3','manchester','lowell','495','101a','amherst street','111','hollis street','130','broad street','daniel webster highway','main street','spit brook','northeastern boulevard','exits 4 and 5','downtown','millyard','french hill','tree streets','crown hill','north end','concord street','south end','southwest','northwest','main dunstable','hudson','merrimack','hollis','amherst','litchfield','milford','pelham','tyngsborough','taylor falls bridge','three bridges','mall','airport','stadium','worcester','providence','hartford','portland','albany','new york','philadelphia','washington','florida','orlando','villages','naples','sarasota','snowbirds','tax migrants','commuters','burlington','waltham','128','defense electronics','contract starts','tech parks','hospitals','kinsley','residents','traveling nurses','university','community college','durham','student','move-in','holiday stroll','fourth','moving day','first of september','mud season','posts','nor’easters','february 2013','march 2018','december 2008','ice storm','may 2006','april 2007','floods','nashua river','leaf traffic','road salt','brine','sand','bill of lading','fmcsa','winch','toll','canal street','bridge street','triple-deckers','lofts','engineers','retirees'],
}, BODY, FAQ)
