import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–2 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('West Valley City, Utah','Car shipping on the west side of the valley, where the trucks already are',
 ['Car shipping in West Valley City is the easiest booking in Utah, because the carriers are already parked here.',
  'Ship Guy is a licensed auto transport broker with an office on Redwood Road at 2700 South. We book vetted carriers across the west side of Salt Lake County, and we do not own the trucks.',
  'The 201 freeway runs along the north edge of the city, Interstate 215 runs the west belt, and Bangerter Highway and Redwood Road carry everything in between. The airport and the distribution centers along 5600 West keep hundreds of trucks based within ten minutes.',
  'This page covers the freeways and the grid, the trucking corridor that makes the city so quick, the diverse neighborhoods of Granger and Hunter, the mine, the airport, Magna and Kearns, and the lanes out of the valley.'],
 'West Valley City at a glance',
 ['Most pickups happen within 1 to 2 days, faster than anywhere else in Utah, because the carriers stage on the west side.',
  'Provo and Ogden are same-day lanes. Las Vegas, Boise, and Denver take a day. Los Angeles, Phoenix, and Seattle take two, and Texas and the Midwest run three.'],
 'Send the address as the grid reads it, with the South and West coordinates. A driver who knows 3500 South at 2700 West finds it without a map.'))

BODY.append(sec('The Freeways &amp; the Grid','The 201, Interstate 215, Bangerter, and Redwood Road',
 prose(
  L('West Valley City was laid out on the same grid as Salt Lake City, and the streets are wide enough for a trailer on almost every block.'),
  P('State Route 201 runs along the north edge of the city from Interstate 15 to Magna, and Interstate 215 runs the west belt from the airport to the south valley. Both put a carrier within minutes of any address.'),
  P('Bangerter Highway carries the west side north and south, and its intersections are being rebuilt one at a time into freeway-style interchanges. A carrier working Bangerter this year plans around the construction zones.'),
  P('Redwood Road and 3500 South are the main streets, and 5600 West reaches the industrial corridor. The numbered grid tells the driver exactly where an address sits, and the truck usually reaches the curb.'),
  P('Salt Lake City has its own page covering the downtown grid, the airport terminal, and the Wasatch canyons.'),
 ), alt=True))

BODY.append(sec('The Trucking Corridor','Why the West Side Ships Faster Than Anywhere in Utah',
 prose(
  L('The distribution centers and freight yards along the 201 and 5600 West are where Utah\u2019s car haulers park.'),
  P('The warehouses and package hubs west of the airport keep hundreds of trucks based within ten minutes of the city, and the car haulers running Interstate 80 and 15 stage on the same lots. A private pickup in West Valley City slots into traffic that already exists.'),
  P('That is why the city schedules in 1 to 2 days when the rest of the state takes 1 to 3. The open-pit copper mine at the west edge of the valley adds shift workers who ship pickups in and out on hiring cycles.'),
  P('The interstate leg of any move is on the <a href="state-to-state-car-shipping.html">state-to-state</a> page.'),
 )))

ROUTES=[("Provo, UT","I-15 · ~45 mi","Same day","$150–$240"),("Ogden, UT","I-15 · ~40 mi","Same day","$150–$240"),
 ("Boise, ID","I-84 · ~335 mi","1 day","$320–$460"),("Las Vegas, NV","I-15 · ~415 mi","1 day","$380–$540"),
 ("Denver, CO","I-80/I-70 · ~525 mi","1–2 days","$430–$620"),("Reno, NV","I-80 · ~515 mi","1–2 days","$430–$620"),
 ("Phoenix, AZ","I-15/US-93 · ~660 mi","2 days","$480–$700"),("Los Angeles, CA","I-15 · ~685 mi","2 days","$500–$730"),
 ("Portland, OR","I-84 · ~765 mi","2 days","$560–$820"),("Dallas, TX","I-15/I-40 · ~1,240 mi","3 days","$850–$1,200")]
BODY.append(rate_table('Lanes &amp; Costs','West Valley City Car Shipping Lanes and Estimated Costs',
 'The lanes west-side households ask about most, with estimated open-transport ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates, running sedan, open trailer. SUVs, pickups, and minivans run about 10 to 25 percent more, enclosed more still. Canyon closures and carrier availability on your dates set the real quote.',
 prose(
  P('Las Vegas, Boise, and Denver are the cheapest long lanes, because the carriers staging on the west side run them daily. California runs full in both directions.'),
  P('A lane that crosses Parleys Canyon in winter swings with the chain law. The <a href="car-shipping-cost.html">cost guide</a> explains the rest of the number.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Granger, Hunter, and the Most Diverse City in Utah',
 prose(
  L('West Valley City is the second-largest city in the state and the most diverse, and it moves on family calendars.'),
  P('Granger on the east side and Hunter on the west side are wide grids of ranch houses and newer subdivisions, and the truck reaches the curb on nearly every street. Families here are large, and the vehicles are too.'),
  P('A minivan or a full-size SUV costs 10 to 25 percent more than a sedan to ship, because a carrier is priced by the space and weight it carries. We quote the real size up front.'),
  P('The Pacific Islander, Latino, and refugee communities here move on family and church calendars, and many households ship a car to or from relatives in California, Nevada, and Arizona. The lanes to all three run daily.'),
  P('Our office is on Redwood Road at 2700 South, minutes from the 201 freeway and the airport.'),
 )))

BODY.append(sec('The Airport, the Arena, and the Mine','Fly-and-Ship, Event Nights, and Copperton',
 prose(
  L('The airport is ten minutes north, and that changes how people move here.'),
  P('The new terminal at Salt Lake City International sits just across the 201 from the city. A carrier meets you at a lot near the terminal, and the car is on the truck the day you land.'),
  P('The arena on Decker Lake Drive fills the 3500 South corridor on hockey nights and concert nights. We schedule pickups near it for other evenings.'),
  P('The copper mine in the Oquirrh Mountains at the west edge of the valley is one of the largest in the world. Its workers and contractors ship trucks in and out on hiring cycles, and Copperton and Magna share the West Valley carrier pool.'),
  P('If your employer reimburses the shipment, we provide the documentation.'),
 ), alt=True))

BODY.append(sec('The West Side Towns','Magna, Kearns, Taylorsville, and the Lake',
 prose(
  L('The cities around West Valley share its grid, its freeways, and its carrier pool.'),
  P('Magna at the end of the 201 and Kearns to the south are wide and easy, and Taylorsville along Redwood Road is the same. The truck reaches the curb in all three.'),
  P('The Great Salt Lake lies west of the city, and its shoreline dust blows across the west side on windy days. Lake-effect snow adds to the winter totals here more than on the east side.'),
  P('The inversion settles over the whole valley for weeks each winter, and it changes nothing for a carrier. Interstate 80 across the salt flats closes in a ground blizzard a few times a season.'),
 )+chips(["Granger","Hunter","Valley Fair","Decker Lake","Chesterfield","Redwood Road","3500 South","5600 West","Magna","Copperton","Kearns","Taylorsville","Murray","Midvale","West Jordan","South Salt Lake"])
 +NOTE('Serving the whole west side of Salt Lake County. Send the address as the grid reads it, and tell us if the vehicle is a minivan or a full-size SUV.')))

BODY.append(sec('Your Options','Open or Enclosed in West Valley City?',
 prose(
  L('Open transport is the everyday choice on the west side, and the staged carriers run it.'),
  P('Enclosed transport keeps a car covered against road salt, lake dust, and canyon grit. It costs more and benefits from flexible dates, since fewer enclosed carriers stage here.'),
  P('A family vehicle rides open without concern. Our <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages set out the difference.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a loading at the curb, and a delivery, with the canyon deciding the timing in winter.'),
  P('Once the price is approved, a carrier staging on the west side takes the booking. The driver records the car\u2019s condition on a Bill of Lading, and you sign it before the car loads. That record is your reference at delivery.'),
 )+ULI([
  "Remove personal belongings",
  "Keep about a quarter tank of fuel",
  "Photograph the vehicle before pickup",
  "Provide a working key and disclose mechanical issues",
  "Turn off aftermarket alarms",
  "Tell us the vehicle size and any gate code",
 ])+prose(P('Our <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> guides cover each step.'))))

BODY.append(sec('Why Ship Guy','Why West Valley City Drivers Choose Ship Guy',
 prose(
  L('We use the carriers already staged on the west side and quote the real price for a family-size vehicle.'),
  P('Every Ship Guy booking is backed by active FMCSA brokerage authority and a $75,000 surety bond, and our office is on Redwood Road.'),
  P('One coordinator handles the shipment from quote to delivery and can arrange open, enclosed, or expedited transport. The <a href="services.html">services</a> page shows everything we offer.'),
 ), alt=True))

BODY.append(office('West Valley City','2708 S Redwood Rd #588','West Valley City, UT 84119','+13853044070','(385) 304-4070','MT',
 '2708+S+Redwood+Rd+%23588,+West+Valley+City,+UT+84119','Visit Us','Find Ship Guy in West Valley City',
 'Our office is on Redwood Road at 2700 South, minutes from the 201 freeway and the airport.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3733.065024921236!2d-111.93937059999999!3d40.712398!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x87528b7901ae101d%3A0x6a0fccf6bcbdbc49!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1790274987990!5m2!1sen!2sus'))

FAQ=[
 ("Why is West Valley City faster to schedule than the rest of Utah?","Because the car haulers running Interstate 80 and 15 stage on the freight lots along the 201 and 5600 West, ten minutes from any address in the city. A private pickup slots into traffic that already exists. Most West Valley pickups happen within 1 to 2 days."),
 ("How much does it cost to ship a minivan or a large SUV from West Valley City?","About 10 to 25 percent more than a sedan on every lane, because a carrier is priced by the space and weight it carries. Las Vegas runs three hundred eighty to five hundred forty for a sedan, so a minivan lands a little above that. We quote the real size up front, so tell us the model."),
 ("Can the carrier come to my house in Granger or Hunter?","Almost always. West Valley City sits on the same wide grid as Salt Lake City, and the truck reaches the curb on nearly every street. Send the address as the grid reads it, with the South and West coordinates, and add a gate code if your subdivision has one."),
 ("Can you meet me at the airport?","Yes, the new terminal sits just across the 201 from the city. The driver meets you at a lot near the terminal, and the car is on the truck the day you land. Tell us the flight time when you book."),
 ("Is Bangerter Highway construction a problem for pickups?","Only for timing. The intersections are being rebuilt one at a time into freeway-style interchanges, and a carrier working Bangerter this year plans around the closures. The 201, Interstate 215, and Redwood Road carry the rest of the city normally."),
 ("How much does it cost to ship a car from West Valley City to Los Angeles?","Usually five hundred to seven hundred thirty dollars for a sedan riding open. Interstate 15 runs the whole way, about six hundred eighty-five miles. The lane runs full in both directions, which keeps it competitive. Larger vehicles and enclosed add to it."),
 ("Do you serve Magna, Kearns, and Taylorsville?","Yes, the whole west side of Salt Lake County ships through this office. Magna, Kearns, and Taylorsville share the grid, the freeways, and the carrier pool, and the truck reaches the curb in all three. Copperton and the mine workforce are covered as well."),
 ("Does the inversion or winter weather delay shipping here?","The inversion changes nothing for a carrier. Lake-effect snow adds to the west side\\u2019s winter totals, and Interstate 80 across the salt flats closes in a ground blizzard a few times a season. A lane that crosses Parleys Canyon waits out a chain-law closure."),
 ("Can you ship a car that does not run from West Valley City?","Yes, non-running cars ship out of the west side every week. A winch-equipped carrier loads it, and the extra loading time is priced into the quote. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a West Valley City car shipping quote?","The pickup and delivery addresses, with the grid coordinates. The year, make, and model, and whether it is a minivan or a full-size SUV. Whether it runs and rolls. Open or enclosed, and your dates. That is everything an accurate West Valley City quote needs."),
]
BODY.append(faq_section(FAQ,'West Valley City FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in West Valley City?','A quote takes about two minutes on the form above. Then send us the grid address and your dates, and we will pull a carrier off the lot down the street.','+13853044070','(385) 304-4070','Get your free West Valley City quote'))

build({
 'slug':'auto-transport-west-valley-city-utah',
 'title':'Car Shipping in West Valley City, UT — Auto Transport | Ship Guy',
 'meta':'Car shipping in West Valley City, UT with carriers already staged on the west side. The 201, Interstate 215, and Bangerter routing, grid addresses, real pricing for minivans and SUVs, airport meetups, Magna, Kearns, and Taylorsville. Local office on Redwood Road. Free quote.',
 'h1':'Car Shipping in<br>West Valley City, <span class="accent">Utah</span>',
 'lede':'Open, enclosed, and expedited auto transport across the west side of Salt Lake County, from the lots where the carriers already park.',
 'tel':'+13853044070','disp':'(385) 304-4070','brand':'West Valley City','keyword':'car shipping in west valley city',
 'localterms':['west valley city','west valley','west side','salt lake county','201','interstate 215','interstate 80','bangerter','redwood road','3500 south','5600 west','grid','coordinates','airport','terminal','distribution','freight','trucking','stage','granger','hunter','valley fair','decker lake','arena','copper','mine','oquirrh','copperton','magna','kearns','taylorsville','minivan','suv','family','pacific islander','latino','great salt lake','lake-effect','dust','inversion','salt flats','parleys','chain law'],
}, BODY, FAQ)
