# STALE BUILDER — the live Milwaukee page received a sentence-splitting pass after this file was recovered from the
# transcript, so a rebuild would regress that wording. Patch city/auto-transport-milwaukee-wisconsin/index.html directly;
# do not run this file against the site (a dry run to SG_OUT_DIR is fine for reference).
import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Milwaukee, Wisconsin','Car shipping on the lake, ninety miles from the busiest carrier hub in the Midwest',
 ['Car shipping in Milwaukee benefits from a fact of geography, because the city sits an hour and a half from Chicago on the road every Midwest carrier runs.',
  'Ship Guy is a licensed auto transport broker with an office on East Wisconsin Avenue downtown. We book vetted carriers across the metro from <a href="/city/auto-transport-kenosha-wisconsin/">Kenosha</a> to Port Washington. We do not own any of the trucks.',
  'Interstate 94 runs from the Illinois line through downtown to <a href="/city/auto-transport-madison-wisconsin/">Madison</a>. Interstate 43 runs the lakeshore to <a href="/city/auto-transport-green-bay-wisconsin/">Green Bay</a>. Interstate 41 carries the west side to the Fox Valley. The rebuilt interchanges and the one still under construction decide the route across town.',
  'This page covers the interstates and the interchanges, the neighborhoods from the East Side to Bay View, the suburbs, the employers and the medical college, the festival summer, the snowbird winter, and the lanes in every direction.'],
 'Milwaukee at a glance',
 ['Most pickups happen within 1 to 3 days, with the Chicago-to-Minneapolis lane bringing carriers through the city all day.',
  'Chicago and Madison are same-day lanes. Minneapolis, Indianapolis, and Detroit take a day. Nashville and Kansas City take one to two, and Florida and Arizona run three to four.'],
 'Tell us the neighborhood. The East Side, the Third Ward, and the old South Side bungalow blocks need a meeting spot, and the suburbs usually do not.'))

BODY.append(sec('The Interstates','Interstate 94, 43, 41, 794, and the Interchanges',
 prose(
  L('Milwaukee\u2019s freeways were rebuilt one interchange at a time, and the last one is still under construction.'),
  P('Interstate 94 arrives from Chicago through Kenosha and Racine, passes the airport, and crosses the Marquette Interchange downtown before heading west past the ballpark to Madison. The stretch between the Marquette and the Zoo Interchange is being rebuilt now, and carriers plan around the lane closures.'),
  P('Interstate 43 runs the lakeshore north through Glendale and Mequon to Green Bay, and south to Beloit. Interstate 41 carries the west side north through Menomonee Falls to Fond du Lac and the Fox Valley, and Interstate 894 bypasses downtown to the south.'),
  P('Interstate 794 crosses the Hoan Bridge from downtown to the port and Bay View, and the bridge closes to high-profile vehicles in a strong lake wind. A loaded trailer takes the surface route through Walker\u2019s Point instead.'),
  P('Every carrier between Chicago and Minneapolis passes the city, which keeps Milwaukee pricing among the best in the upper Midwest.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','The East Side, the Third Ward, Bay View, and the Bungalow Blocks',
 prose(
  L('Milwaukee was built dense, and a seventy-five-foot trailer respects that.'),
  P('The East Side, Brady Street, and Riverwest have narrow streets, alleys, and parked cars on both sides. The Third Ward and the downtown towers run on garages. The driver meets you on Prospect Avenue, Farwell, or a lot near the lakefront.'),
  P('The old South Side and the North Side are blocks of bungalows and duplexes with alley garages, and the driver meets you on National Avenue, Lincoln, or a main road nearby. Bay View is the same near the lake and easier toward the airport.'),
  P('Wauwatosa, Brookfield, Mequon, Franklin, and Oak Creek are wide, and the truck usually reaches the curb. Send the subdivision name where there is one.'),
  P('Our office is on East Wisconsin Avenue downtown, a few blocks from the lakefront and the Marquette Interchange.'),
 )))

ROUTES=[("Chicago, IL","I-94 · ~90 mi","Same day","$170–$280"),("Madison, WI","I-94 · ~80 mi","Same day","$170–$280"),
 ("Green Bay, WI","I-43 · ~115 mi","Same day","$180–$290"),("Indianapolis, IN","I-94/I-65 · ~280 mi","1 day","$260–$390"),
 ("Minneapolis, MN","I-94 · ~340 mi","1 day","$320–$460"),("Detroit, MI","I-94 · ~375 mi","1 day","$340–$490"),
 ("St. Louis, MO","I-94/I-55 · ~375 mi","1 day","$340–$490"),("Nashville, TN","I-65 · ~560 mi","1–2 days","$450–$650"),
 ("Denver, CO","I-90/I-80 · ~1,030 mi","3 days","$700–$1,000"),("Orlando, FL","I-65/I-75 · ~1,300 mi","3–4 days","$850–$1,200")]
BODY.append(rate_table('Lanes &amp; Costs','Milwaukee Car Shipping Lanes and Estimated Costs',
 'The lanes Milwaukee households ask about most, with estimated open-transport ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates, running sedan, open trailer. SUVs and pickups run about 10 to 25 percent more, enclosed more still. Winter and the snowbird season swing the long lanes, and carrier availability on your dates sets the real quote.',
 prose(
  P('Chicago is the cheapest lane out of Milwaukee and one of the cheapest in the country, ninety miles down a road carriers run all day. Madison, Minneapolis, and Indianapolis follow on the same corridors.'),
  P('The Florida and Arizona lanes fill each fall with snowbirds. The <a href="car-shipping-cost.html">cost guide</a> explains the rest of the number.'),
 ), alt=True))

BODY.append(sec('The Employers &amp; the Medical College','Corporate Moves, June Residents, and the Universities',
 prose(
  L('Milwaukee ships on insurance, automation, and medicine as much as on the breweries it is known for.'),
  P('The insurance and financial headquarters downtown, the automation and controls companies on the north side, and the motorcycle maker relocate employees on start dates all year. If your employer reimburses the shipment, we provide the documentation.'),
  P('The medical college and the hospital campus in Wauwatosa move residents and fellows every June, and most arrive with a car and two weeks of notice. The campus garages do not admit a trailer, so the handoff happens on Watertown Plank Road.'),
  P('Marquette downtown, the state university on the East Side, and the engineering school bring cars in each August and send them home each May. Campus streets are tight, so the driver meets you at a lot nearby, and an adult signs for a student car.'),
  P('The interstate leg of a relocation is on the <a href="state-to-state-car-shipping.html">state-to-state</a> page.'),
 )))

BODY.append(sec('The Festival Summer','Summerfest, the State Fair, Game Days, and the Lakefront',
 prose(
  L('Milwaukee spends its summer on the lakefront, and the lakefront roads fill for weeks at a time.'),
  P('Summerfest runs for eleven days around the start of July and closes the lakefront grounds and the streets around them. The state fair fills West Allis for eleven days in August, and the ethnic festivals fill the same lakefront grounds most weekends between.'),
  P('Brewers home games fill the ballpark interchange on Interstate 94, and Bucks games fill the arena district downtown. We schedule the East Side and downtown around the festival dates and the west side around the ballpark.'),
  P('The lake ferry to Michigan runs from the port each summer and carries cars, but not carriers. A car headed across the lake by ferry hands off at the terminal, and the rest of the year the lane runs around through Chicago.'),
 ), alt=True))

BODY.append(sec('The Snowbird Winter','Florida, Arizona, and the Lake-Effect Snow',
 prose(
  L('Milwaukee empties toward Florida and Arizona every fall, and the cars go by trailer.'),
  P('Retirees from Whitefish Bay, Brookfield, and the North Shore ship cars south from October through December and home from March through May. Two to three weeks of notice keeps the price steady, and our <a href="snowbird-car-shipping.html">snowbird</a> page has the planning tips.'),
  P('Lake-effect snow piles onto the East Side and the North Shore, and blizzards close Interstate 94 for a day at a time from December through March. Carriers wait for the plows, and a car arriving from a warm state needs winter oil and a strong battery.'),
  P('Road salt runs all winter, and collector-car owners often choose enclosed transport for the trip. Spring brings flooding along the rivers and construction on every interstate.'),
 )+chips(["Downtown","Third Ward","East Side","Brady Street","Riverwest","Bay View","Walker's Point","South Side","North Side","Wauwatosa","West Allis","Brookfield","Waukesha","Glendale","Whitefish Bay","Shorewood","Mequon","Cedarburg","Franklin","Oak Creek","Cudahy","Menomonee Falls","Germantown","Racine","Kenosha","Port Washington"])
 +NOTE('Serving Milwaukee, Waukesha, Ozaukee, Washington, Racine, and Kenosha Counties. Tell us the neighborhood and the vehicle size.')))

BODY.append(sec('Your Options','Open or Enclosed in Milwaukee?',
 prose(
  L('Open transport is the everyday choice, and the Interstate 94 lanes run on it.'),
  P('Enclosed transport keeps a car covered against road salt, slush, and lake grit. The North Shore and Lake Drive keep enclosed carriers busy with collector cars, and the motorcycle rallies add to it.'),
  P('A commuter car rides open without trouble. Our <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages describe each choice.'),
 )))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a loading on the corridor, and a delivery, with the winter and the festivals deciding the timing.'),
  P('Once the price is approved, a carrier running Interstate 94 takes the booking. The driver marks the car\u2019s condition on a Bill of Lading, and you sign it before loading. That form is your checklist at delivery.'),
 )+ULI([
  "Remove personal belongings",
  "Keep about a quarter tank of fuel",
  "Photograph the vehicle before pickup, especially after a salty winter",
  "Provide a working key and disclose mechanical issues",
  "Disable aftermarket alarms",
  "For a dense neighborhood or a downtown tower, plan to meet the truck on a main road",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> guides go step by step.')), alt=True))

BODY.append(sec('Why Ship Guy','Why Milwaukee Drivers Choose Ship Guy',
 prose(
  L('We use the lane between Chicago and Minneapolis and plan around the interchanges, the festivals, and the snow.'),
  P('Active FMCSA brokerage authority and a $75,000 surety bond stand behind every booking we make, and our office is on East Wisconsin Avenue.'),
  P('One coordinator carries the shipment from quote to delivery and can book open, enclosed, or expedited transport. The <a href="services.html">services</a> page shows the full lineup.'),
 )))

BODY.append(office('Milwaukee','411 E Wisconsin Ave #548','Milwaukee, WI 53202','+14144859612','(414) 485-9612','CT',
 '411+E+Wisconsin+Ave+%23548,+Milwaukee,+WI+53202','Visit Us','Find Ship Guy in Milwaukee',
 'Our office is on East Wisconsin Avenue downtown, a few blocks from the lakefront and the Marquette Interchange.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3599.607982997958!2d-87.90585829999999!3d43.0385255!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8805196340349981%3A0x8f3819da0a035ebe!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1790275127836!5m2!1sen!2sus'))

FAQ=[
 ("Why is Milwaukee to Chicago so cheap?","Because the two cities sit ninety miles apart on Interstate 94, and every carrier crossing the upper Midwest runs that stretch. It usually costs one hundred seventy to two hundred eighty dollars for a sedan, one of the cheapest lanes in the country. Madison is nearly as easy."),
 ("Can the carrier come to my house on the East Side or in Bay View?","Rarely on the dense blocks. The East Side, Brady Street, and Riverwest have narrow streets with parked cars on both sides, and Bay View near the lake is the same. The driver meets you on Prospect, Farwell, or a main road nearby. The suburbs usually allow curbside."),
 ("How much does it cost to ship a car from Milwaukee to Florida or Arizona?","Orlando usually runs eight hundred fifty to twelve hundred dollars for a sedan, about thirteen hundred miles on Interstate 65 and 75. Phoenix runs nine hundred fifty to thirteen hundred fifty. Season matters more than distance, and a southbound car in November costs more than in July. Larger vehicles add 10 to 25 percent."),
 ("Does Summerfest or the state fair affect pickups?","For the lakefront and West Allis, yes. Summerfest closes the lakefront grounds and the streets around them for eleven days around the start of July, and the fair fills West Allis for eleven days in August. We schedule those areas around the dates, and the rest of the metro runs normally."),
 ("Do you handle moves for residents at the medical college?","Yes, the medical college and the hospital campus in Wauwatosa move residents and fellows every June, and most arrive with a car and two weeks of notice. We plan the pickup around the start date. The campus garages do not admit a trailer, so the handoff happens on Watertown Plank Road."),
 ("Is the Interstate 94 construction a problem?","Only for timing. The stretch between the Marquette and Zoo Interchanges is being rebuilt, and carriers plan around the lane closures. Interstate 894 and 43 carry the traffic around it. The Hoan Bridge closes to high-profile vehicles in a strong lake wind, and a loaded trailer takes the surface route."),
 ("Can you ship a car across the lake on the ferry?","We deliver to the ferry terminal at the port, and the car boards the ferry as a passenger vehicle with you or a driver. Carriers do not ride the ferry. Outside the summer season, the Michigan lane runs around through Chicago, and Detroit is a day away on Interstate 94."),
 ("Can you ship a car for a Marquette or UWM student?","Yes, student cars move each August and again in May. Campus streets downtown and on the East Side are tight, so the driver meets you at a lot nearby. An adult signs for the car, and a parent can sign at the far end. Winter arrivals need a strong battery."),
 ("Can you ship a car that does not run from Milwaukee?","Yes, non-running cars ship out of Milwaukee every week. A winch-equipped carrier loads it, and the extra loading time is billed. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Milwaukee car shipping quote?","The pickup and delivery addresses, with the neighborhood. The year, make, and model. Whether it runs and rolls. Open or enclosed, and your dates. That is everything an accurate Milwaukee quote needs."),
]
BODY.append(faq_section(FAQ,'Milwaukee FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Milwaukee?','A quote takes about two minutes on the form above. Then tell us the neighborhood and your dates, and we will match you with a carrier already on the corridor.','+14144859612','(414) 485-9612','Get your free Milwaukee quote'))

build({
 'slug':'auto-transport-milwaukee-wisconsin',
 'title':'Car Shipping in Milwaukee, WI — Auto Transport | Ship Guy',
 'meta':'Car shipping in Milwaukee, WI on the Chicago-to-Minneapolis lane. East Side and Bay View handoffs, the Marquette and Zoo Interchange rebuild, medical college residents, Summerfest and fair timing, the Florida and Arizona snowbird lane, lake-effect winter. Local office on East Wisconsin Avenue. Free quote.',
 'h1':'Car Shipping in<br>Milwaukee, <span class="accent">Wisconsin</span>',
 'lede':'Open, enclosed, and expedited auto transport across the Milwaukee metro, planned around the interchanges, the lakefront, and the winter.',
 'tel':'+14144859612','disp':'(414) 485-9612','brand':'Milwaukee','keyword':'car shipping in milwaukee',
 'localterms':['milwaukee','interstate 94','interstate 43','interstate 41','interstate 794','interstate 894','marquette interchange','zoo interchange','hoan bridge','lakefront','lake michigan','east side','brady street','riverwest','third ward','bay view','walker','south side','north side','bungalow','wauwatosa','west allis','brookfield','waukesha','mequon','whitefish bay','shorewood','franklin','oak creek','menomonee falls','racine','kenosha','insurance','automation','motorcycle','medical college','residents','marquette','uwm','summerfest','state fair','brewers','bucks','ferry','snowbird','lake-effect','salt','chicago'],
}, BODY, FAQ)
