import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('St. Louis, Missouri','Car shipping where four interstates meet the river, on both sides of it',
 ['Car shipping in St. Louis works because four interstates meet under the Arch. Ship Guy is a licensed auto transport broker with an office on Memorial Drive downtown.',
  'We book vetted carriers across the metro, from Chesterfield and St. Charles to the Metro East in Illinois. We do not own the trucks.',
  'Interstate 70, 64, 44, and 55 all reach downtown. Interstate 270 loops the Missouri side and 255 loops the Illinois side. The Poplar Street Bridge carries the heaviest truck traffic on the Mississippi.',
  'This page covers the interstates and the bridges, the brick neighborhoods, the suburbs, the hospitals, and the headquarters. It also covers the Illinois side, the air base, the river, and the lanes.'],
 'St. Louis at a glance',
 ['Most pickups happen within 1 to 3 days. Carriers crossing the country on 70, 44, 55, and 64 pass the city every day.',
  'Columbia and Springfield are same-day lanes. Kansas City, Chicago, Indianapolis, Memphis, Louisville, and Nashville take a day. Florida and Texas run two to three.'],
 'Tell us the neighborhood. Soulard, the Central West End, and the Hill need a meeting spot. Chesterfield, St. Peters, and South County usually meet the truck at the curb.'))

BODY.append(sec('The Interstates','70, 64, 44, 55, the Loops, and the Bridges',
 prose(
  L('St. Louis is the only city where Interstate 70, 44, 55, and 64 all come together. The carriers never leave.'),
  P('Interstate 70 runs west to Kansas City and Denver and east over the Stan Musial bridge to Indianapolis. Interstate 44 ends downtown after running up from Tulsa and Springfield. Interstate 55 follows the river south to Memphis and north through Illinois to Chicago.'),
  P('Interstate 64 is the central corridor from downtown through the Central West End and Clayton to Chesterfield. Interstate 270 loops the Missouri side from South County to St. Charles. Interstate 255 closes the loop through Illinois, and 170 cuts through Clayton to the airport.'),
  P('The Poplar Street Bridge carries 55 and 64 across the Mississippi. It sees more trucks than any crossing in the region. The Chain of Rocks and Jefferson Barracks bridges carry the loops. No bridge in the metro charges a toll.'),
  P('Our office sits on Memorial Drive downtown, beside the Arch grounds and the interstate ramps.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Soulard, the Central West End, the Hill, Clayton, and the Suburbs',
 prose(
  L('St. Louis was built in brick before the automobile. The brick blocks are the ones that need planning.'),
  P('Soulard, Lafayette Square, Benton Park, and the Hill have narrow streets with cars on both curbs. Tower Grove, Shaw, and the Central West End are the same under old trees. The driver meets you on Gravois, Kingshighway, or at a lot by the interstate.'),
  P('Downtown and Clayton run on garages and towers. The handoff happens on the riverfront, on Forsyth, or at a lot off 170. University City and the Loop meet the truck on Delmar.'),
  P('Kirkwood, Webster Groves, and Ladue wind under old trees with no room for a trailer. The driver meets you on Manchester Road, Lindbergh, or Clayton Road. Chesterfield, Ballwin, Creve Coeur, and Maryland Heights are wide grids where the truck reaches the curb.'),
  P('St. Charles, St. Peters, O’Fallon, and Wentzville sit across the Missouri River on 70 and schedule easily. South County, Arnold, and Fenton do the same on 55 and 44. The new subdivisions in St. Charles County outrun carrier maps, so send the full address.'),
 )))

ROUTES=[("Columbia, MO","I-70 · ~125 mi","Same day","$180–$290"),("Springfield, MO","I-44 · ~215 mi","Same day","$230–$350"),
 ("Indianapolis, IN","I-70 · ~245 mi","1 day","$250–$370"),("Kansas City, MO","I-70 · ~250 mi","1 day","$250–$370"),
 ("Louisville, KY","I-64 · ~260 mi","1 day","$260–$390"),("Memphis, TN","I-55 · ~285 mi","1 day","$270–$400"),
 ("Chicago, IL","I-55 · ~300 mi","1 day","$290–$420"),("Nashville, TN","I-64/I-24 · ~310 mi","1 day","$290–$430"),
 ("Dallas, TX","I-44/US-75 · ~630 mi","1–2 days","$480–$690"),("Orlando, FL","I-64/I-24/I-75 · ~1,000 mi","3 days","$750–$1,050")]
BODY.append(rate_table('Lanes &amp; Costs','St. Louis Car Shipping Lanes and Estimated Costs',
 'The routes St. Louis households and employers book most, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates, sedan that runs, open trailer. SUVs and pickups cost about 10 to 25 percent more, enclosed more than that. The season and which carriers are free on your dates set the final figure.',
 prose(
  P('Seven cities sit within five hours of the Arch. Those lanes price about as low as any in the country. Chicago and Memphis ride Interstate 55 in opposite directions all day.'),
  P('The Florida lane leaves on 64 and joins Interstate 75 in Tennessee. It swings with the fall migration. The <a href="car-shipping-cost.html">cost guide</a> explains the rest of the number.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Hospitals, the Universities, the Headquarters, and the Plants',
 prose(
  L('St. Louis relocates people on the medical calendar first, and on corporate and plant calendars after that.'),
  P('The hospital complex in the Central West End is one of the largest in the country. It brings in residents and fellows every June and July. Most arrive from out of state with a car. The handoff happens on Kingshighway or Forest Park Avenue rather than in a hospital garage.'),
  P('The university in Clayton and the one in Midtown bring cars in each August. They send them home each May. The campus streets are narrow, so the handoff happens at a lot a few blocks away. An adult signs for a student car.'),
  P('The defense aircraft plant by the airport and the rental-car headquarters in Clayton transfer staff on start dates. The brokerage in Des Peres does too. The crop-science campus in Creve Coeur does the same. So does the new intelligence agency campus on the north side. The van plant in Wentzville keeps carriers based in St. Charles County.'),
  P('Employers that reimburse the shipment get whatever documentation they ask for. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side of a move.'),
 )))

BODY.append(sec('The Illinois Side &amp; the Base','The Metro East, Scott Air Force Base, and the Second Vehicle',
 prose(
  L('A third of the metro lives in Illinois. The carriers treat both sides of the river as one city.'),
  P('Belleville, Edwardsville, Collinsville, O’Fallon, and Granite City share the St. Louis carrier pool and the same pricing. The handoff happens on Route 159, on Interstate 55 and 70, or at a lot near 255.'),
  P('The air base east of Belleville houses the mobility and transportation commands. It rotates airmen, civilians, and contractors with a summer peak. Most arrive with two cars and orders that pay for one. The second vehicle rides with us.'),
  P('The gates are controlled, so the handoff happens in Shiloh, O’Fallon, or Mascoutah. The report date sets the schedule. Ship Guy is a private broker with no connection to the base. The <a href="military-car-shipping.html">military</a> page covers a PCS move in detail.'),
 ), alt=True))

BODY.append(sec('The River &amp; the Weather','Floods, Tornadoes, Ice, and Game Days',
 prose(
  L('St. Louis sits between two rivers in the middle of a tornado corridor. The carriers plan for both.'),
  P('Tornado watches run from March into June. The city has taken direct hits on both sides of the river. A warning parks the driver until it passes, and a spring pickup can slide a day. Hail does more damage to a parked car than wind. We shift the window when it is forecast.'),
  P('The Mississippi and the Missouri rise in wet springs. The riverfront roads downtown go under a few times a decade. So do the bottoms in Chesterfield Valley and St. Charles. We move the handoff uphill when the river is up.'),
  P('Ice closes 70, 44, and 64 for a day a few times each winter. Summer heat moves the loading hour earlier. Baseball and hockey downtown fill the 64 and 44 ramps for hours. We schedule downtown pickups around game nights.'),
 )+chips(["Downtown","Soulard","Lafayette Square","Benton Park","Tower Grove","Shaw","The Hill","Central West End","Forest Park","Dogtown","Carondelet","Dutchtown","Clayton","University City","Kirkwood","Webster Groves","Ladue","Frontenac","Creve Coeur","Maryland Heights","Chesterfield","Ballwin","Florissant","Hazelwood","South County","Arnold","Fenton","St. Charles","St. Peters","O'Fallon","Wentzville","Belleville","Edwardsville","Collinsville","Granite City"])
 +NOTE('Serving St. Louis City and County, St. Charles and Jefferson Counties, and the Metro East. Tell us the neighborhood and which side of the river.')))

BODY.append(sec('Your Options','Open or Enclosed in St. Louis?',
 prose(
  L('Four out of five St. Louis cars go open, and the interstate lanes are quoted that way.'),
  P('An enclosed trailer keeps salt, hail, and attention off the car. The garages in Ladue, Frontenac, and Clayton book enclosed trailers. So do the collector cars headed to the auctions.'),
  P('The car you commute in rides open without a problem. Our <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain what the roof buys you.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a loading on a main road, and a delivery. The brick blocks and the river decide the spot.'),
  P('Say yes to the price and a carrier already on one of the four interstates takes the job. We name the spot. The driver looks the car over with you there and notes everything on a Bill of Lading. You both sign it.'),
 )+ULI([
  "Empty the car of personal items",
  "Leave the tank about a quarter full",
  "Shoot photos of every panel before pickup, especially after hail",
  "Supply a working key and flag any mechanical issue",
  "Turn aftermarket alarms off",
  "On a brick block in Soulard or the Hill, plan to meet the truck on a main road",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages carry the step-by-step.'))))

BODY.append(sec('Why Ship Guy','Why St. Louis Drivers Choose Ship Guy',
 prose(
  L('We work all four interstates every day and plan around the river, the storms, and the medical calendar.'),
  P('Ship Guy holds FMCSA brokerage authority and a $75,000 surety bond. Both are a matter of public record. Our office is on Memorial Drive downtown.'),
  P('From the first quote to the delivery signature, one coordinator handles everything. Open, enclosed, and expedited transport are all available, and the <a href="services.html">services</a> page covers each.'),
 ), alt=True))

BODY.append(office('St. Louis','1 Memorial Dr #878A','St. Louis, MO 63102','+13146617719','(314) 661-7719','CT',
 '1+Memorial+Dr+%23878A,+St.+Louis,+MO+63102','Visit Us','Find Ship Guy in St. Louis',
 'Our office is on Memorial Drive downtown, beside the Arch grounds and the ramps for all four interstates.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3847.626326346466!2d-90.1880626!3d38.6244003!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x87d8b3e7838f7f49%3A0xe20ab3dc527837d9!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792076163917!5m2!1sen!2sus'))

FAQ=[
 ("Can the carrier come to my house in Soulard, the Hill, or the Central West End?","Rarely. The brick streets are narrow and cars line both curbs. The driver meets you on Gravois, Kingshighway, or at a lot by the interstate. Chesterfield, St. Peters, South County, and the Metro East usually allow a curbside pickup."),
 ("Do you pick up on the Illinois side?","Yes. Belleville, Edwardsville, Collinsville, O’Fallon, and Granite City share the St. Louis carrier pool and the same pricing. The handoff happens on Route 159 or near Interstate 55, 70, or 255."),
 ("How much does it cost to ship a car from St. Louis to Florida?","Figure seven hundred fifty to one thousand fifty dollars for a sedan to Orlando. Tampa runs about the same. The route is about a thousand miles on 64, 24, and 75. Fall southbound costs more than spring. SUVs and pickups add 10 to 25 percent."),
 ("Do you handle a PCS move to Scott Air Force Base?","Yes, every week. The orders cover one vehicle, and we carry the second. The gates are controlled, so you meet the driver in Shiloh, O’Fallon, or Mascoutah. The report date sets the schedule. Ship Guy is a private broker with no connection to the base."),
 ("Do you ship cars for residents at the medical center?","Yes, every June and July. Residents and fellows arrive at the Central West End complex from every state. Most come with a car. The handoff happens on Kingshighway or Forest Park Avenue rather than in a hospital garage."),
 ("Can you ship a car for a WashU or SLU student?","Yes. The cars come in each August and head home each May. Campus streets are narrow, so the handoff happens at a lot a few blocks away. An adult signs at pickup, and a parent can sign at the far end."),
 ("What happens if a tornado warning is issued during my pickup?","The driver gets off the road and waits out the warning. The pickup can lose a few hours or a day. Tornado watches run March into June on both sides of the river. Spring bookings carry a cushion for it."),
 ("Does a Cardinals or Blues game affect my pickup?","Downtown, yes. The 64 and 44 ramps fill for hours before and after a game. We schedule downtown and Soulard pickups around game nights. The suburbs run normally."),
 ("Can you ship a car that does not run from St. Louis?","Yes. We assign a carrier with a winch, and the longer loading is figured into the price. The spot has to be flat and wide, which usually means a lot by the interstate. Tell us if it rolls, steers, and brakes."),
 ("What do you need for a St. Louis car shipping quote?","Where it is and where it is going, with the neighborhood and the side of the river. Year, make, and model. Does it run. Open or enclosed. Your dates. That is a complete St. Louis request."),
]
BODY.append(faq_section(FAQ,'St. Louis FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in St. Louis?','Price the trip on the form above, then tell us the neighborhood and your dates. A carrier already passing the Arch takes it from there.','+13146617719','(314) 661-7719','Get your free St. Louis quote'))

build({
 'slug':'auto-transport-st-louis-missouri',
 'title':'Car Shipping in St. Louis, MO — Auto Transport | Ship Guy',
 'meta':'Car shipping in St. Louis, MO where Interstate 70, 44, 55, and 64 meet. Brick-block handoffs in Soulard and the Hill, Metro East pickups, Scott Air Force Base moves, hospital and university timing, river floods and storm season, the Florida lane. Local office on Memorial Drive. Free quote.',
 'h1':'Car Shipping in<br>St. Louis, <span class="accent">Missouri</span>',
 'lede':'Open, enclosed, and expedited auto transport on both sides of the river, planned around the interstates, the brick blocks, and the storms.',
 'tel':'+13146617719','disp':'(314) 661-7719','brand':'St. Louis','keyword':'car shipping in st. louis',
 'localterms':['st. louis','interstate 70','interstate 64','interstate 44','interstate 55','interstate 270','interstate 255','170','poplar street','stan musial','chain of rocks','jefferson barracks','memorial drive','arch','downtown','soulard','lafayette square','benton park','tower grove','shaw','the hill','central west end','forest park','clayton','university city','delmar','kirkwood','webster groves','ladue','frontenac','creve coeur','maryland heights','chesterfield','ballwin','florissant','south county','arnold','fenton','st. charles','st. peters','wentzville','belleville','edwardsville','collinsville','granite city','metro east','air base','scott','hospital','residents','university','defense aircraft','rental-car','brokerage','crop-science','intelligence agency','van plant','tornado','hail','flood','ice','cardinals','blues','columbia','springfield','kansas city','chicago','indianapolis','memphis','louisville','nashville','dallas','orlando'],
}, BODY, FAQ)
