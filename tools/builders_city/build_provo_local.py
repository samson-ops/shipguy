import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Provo, Utah','Car shipping for two campuses, a tech valley, and the missionaries coming home',
 ['Car shipping in Provo runs on a calendar unlike any other college town, because the students leave for two years and come back.',
  'Ship Guy is a licensed auto transport broker with an office on North University Avenue downtown. We book vetted carriers across Utah County, and we do not own the trucks.',
  'Interstate 15 runs along the west side of the city between Salt Lake City and the south valley, and University Avenue and University Parkway carry the campus and Orem to the interchanges. A carrier reaches any Provo address from the interstate in ten minutes.',
  'This page covers the interstate and the rebuild, the university calendar and the missionary cycle, Orem and the second campus, Silicon Slopes, the canyon and the lake towns, and the lanes out of Utah County.'],
 'Provo at a glance',
 ['Most pickups happen within 1 to 3 days, with Interstate 15 bringing carriers past the city all day.',
  'Salt Lake City and Ogden are same-day lanes. Las Vegas, Boise, and Denver take a day. Los Angeles, Phoenix, and Seattle take two, and Texas and the Midwest run three.'],
 'Tell us the semester date you are working toward. Provo\u2019s move-in comes in September and January, not August, and the busy weeks are not the ones other college towns use.'))

BODY.append(sec('Interstate 15','The Rebuild, the Interchanges, and University Avenue',
 prose(
  L('Interstate 15 through Provo and Orem has been under reconstruction for years, and it still carries every carrier through Utah County.'),
  P('The interchanges at University Avenue, Center Street, and University Parkway put a carrier within ten minutes of the campus, downtown, or the lake side. The current widening project moves lanes and closes ramps overnight, and carriers plan around it.'),
  P('University Avenue runs from the interstate through downtown to the campus and up Provo Canyon as US 189. University Parkway carries Orem, and State Street carries the whole valley north and south on the old highway.'),
  P('The numbered grid tells the driver exactly where an address sits, with Center Street and University Avenue at the origin. Streets are wide, and the truck usually reaches the curb outside the campus blocks.'),
  P('Our office is on North University Avenue downtown, between the campus and the Interstate 15 interchange.'),
 ), alt=True))

BODY.append(sec('The University','September, January, April, and the Two-Year Absence',
 prose(
  L('Brigham Young University runs on its own calendar, and Provo ships on it.'),
  P('Fall semester begins in early September, and winter semester begins in early January, so student cars arrive in the last week of August and the first week of January. They leave in late April, and a summer term keeps some of them through August.'),
  P('Thousands of students leave each year for missions that last eighteen months to two years, and thousands return. A returning missionary often needs a car shipped from home to Provo in the middle of a semester, and we run that lane year round.'),
  P('The streets around campus and the apartment complexes along 900 East and University Avenue are tight, so the driver meets you at a lot nearby. An adult signs for a student car, and a parent can sign at the far end.'),
  P('Home football Saturdays fill the stadium and the streets north of campus from midmorning, and we schedule the campus side for weekdays in the fall.'),
 )))

ROUTES=[("Salt Lake City, UT","I-15 · ~45 mi","Same day","$150–$240"),("Ogden, UT","I-15 · ~85 mi","Same day","$170–$280"),
 ("St. George, UT","I-15 · ~265 mi","1 day","$260–$390"),("Las Vegas, NV","I-15 · ~375 mi","1 day","$350–$500"),
 ("Boise, ID","I-15/I-84 · ~385 mi","1 day","$350–$500"),("Denver, CO","US-6/I-70 · ~545 mi","1–2 days","$430–$620"),
 ("Phoenix, AZ","I-15/US-89 · ~620 mi","2 days","$460–$680"),("Los Angeles, CA","I-15 · ~640 mi","2 days","$480–$700"),
 ("Seattle, WA","I-84/I-82 · ~880 mi","2–3 days","$620–$900"),("Dallas, TX","I-15/I-40 · ~1,200 mi","3 days","$820–$1,150")]
BODY.append(rate_table('Lanes &amp; Costs','Provo Car Shipping Lanes and Estimated Costs',
 'The lanes Utah County households and students ask about most, with estimated open-transport ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates, running sedan, open trailer. SUVs, pickups, and minivans run about 10 to 25 percent more, enclosed more still. Semester windows and carrier availability on your dates set the real quote.',
 prose(
  P('Provo sits forty-five miles closer to Las Vegas and Los Angeles than Salt Lake City does, which trims those lanes. Denver runs through Spanish Fork Canyon on US 6 and swings with the weather there.'),
  P('The Arizona and California lanes fill with students each semester. The <a href="car-shipping-cost.html">cost guide</a> explains the rest of the number.'),
 ), alt=True))

BODY.append(sec('Orem &amp; the Second Campus','Utah Valley University, Vineyard, and the Lake Side',
 prose(
  L('The largest university in the state by enrollment is not the famous one, and it sits ten minutes north in Orem.'),
  P('Utah Valley University is a commuter campus with tens of thousands of students, and its calendar runs a week or two off the Provo one. Its lots are wide, and the handoff happens at the edge of campus off University Parkway.'),
  P('Vineyard on the lake side was a steel mill twenty years ago and is one of the fastest-growing cities in the country now. Its subdivisions add streets every month, so send the community name.'),
  P('Orem itself is a wide grid where the truck reaches the curb, and Lindon and Pleasant Grove to the north are the same.'),
 )))

BODY.append(sec('Silicon Slopes','The Headquarters in Provo, Lehi, and the Commute',
 prose(
  L('Utah County ships on the tech companies as much as on the campuses now.'),
  P('The software, security, and direct-sales companies headquartered in Provo and Orem, and the larger cluster fifteen minutes north in Lehi, relocate engineers from across the country on start dates. Corporate packages usually cover a vehicle, and we provide the documentation.'),
  P('Many newcomers buy in Vineyard, Saratoga Springs, or Eagle Mountain across the lake and commute on the interstate. We plan the pickup around the first day, and the <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
  P('Families here are large, and a minivan or full-size SUV costs 10 to 25 percent more to ship than a sedan. We quote the real size up front.'),
 ), alt=True))

BODY.append(sec('The Canyon &amp; the South Valley','Provo Canyon, Sundance, Spanish Fork, and the Airport',
 prose(
  L('Two canyons leave Provo, and only one of them is friendly to a trailer.'),
  P('Provo Canyon on US 189 runs to Heber and the Wasatch Back, and a carrier can use it in good weather. The road to Sundance climbs off it on switchbacks no trailer takes, so resort deliveries hand off at the mouth of the canyon.'),
  P('Spanish Fork Canyon on US 6 carries the Denver lane and closes in snow and wind more often than any road in the county. Carriers wait it out in Spanish Fork or Price.'),
  P('Springville, Spanish Fork, Payson, and the south valley are wide grids with new subdivisions, and Santaquin marks the end of the Front. The regional airport on the lake side flies to a growing list of cities, and a driver meets you at a lot near the terminal.'),
 )+chips(["Downtown","Campus","Joaquin","Grandview","Riverbottoms","Edgemont","Indian Hills","Provo Bay","Orem","Vineyard","Lindon","Pleasant Grove","American Fork","Lehi","Saratoga Springs","Eagle Mountain","Springville","Mapleton","Spanish Fork","Payson","Santaquin","Sundance"])
 +NOTE('Serving all of Utah County from Lehi to Santaquin. Tell us the semester date, the community name, and the vehicle size.')))

BODY.append(sec('Weather','Snow, the Inversion, and the Canyon Wind',
 prose(
  L('Utah County winter is snow in the canyons and cold trapped in the valley, and the canyons decide the lanes.'),
  P('Spanish Fork Canyon closes to high-profile vehicles in wind and snow, and Provo Canyon closes in a storm. Inside the valley, the plows keep the interstate open, and a pickup rarely moves more than a day.'),
  P('The inversion settles over Utah Lake and the valley for weeks each winter and changes nothing for a carrier. Summer heat passes a hundred degrees in July, and drivers load early.'),
  P('We tell you the moment the forecast changes the plan.'),
 ), alt=True))

BODY.append(sec('Your Options','Open or Enclosed in Provo?',
 prose(
  L('Open transport is the everyday choice, and the semester lanes run on it.'),
  P('Enclosed transport keeps a car covered against road salt, canyon grit, and the sun. The east-bench estates and the Sundance homes keep enclosed carriers busy with collector cars.'),
  P('A student car rides open without concern. Our <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages lay out the choice.'),
 )))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff at the curb or a lot near campus, and a delivery, with the semester setting the window.'),
  P('Once the price is approved, a carrier running Interstate 15 takes the booking. The driver lists the car\u2019s condition on a Bill of Lading, and you sign it before loading. That list is your comparison at delivery.'),
 )+ULI([
  "Remove personal belongings",
  "Keep about a quarter tank of fuel",
  "Photograph the vehicle before pickup",
  "Provide a working key and disclose mechanical issues",
  "Turn off aftermarket alarms",
  "Include the community name, the semester date, and the vehicle size",
 ])+prose(P('Our <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> guides cover each step.')), alt=True))

BODY.append(sec('Why Ship Guy','Why Provo Drivers Choose Ship Guy',
 prose(
  L('We know the semester dates, the mission cycle, and which canyon closes in the wind.'),
  P('Active FMCSA brokerage authority and a $75,000 surety bond back everything we book, and our office is on North University Avenue.'),
  P('One coordinator handles the shipment from quote to delivery and can set up open, enclosed, or expedited transport. The <a href="services.html">services</a> page lists each option.'),
 )))

BODY.append(office('Provo','86 N University Ave Ste 487','Provo, UT 84601','+13853508211','(385) 350-8211','MT',
 '86+N+University+Ave+Ste+487,+Provo,+UT+84601','Visit Us','Find Ship Guy in Provo',
 'Our office is on North University Avenue downtown, between the campus and the Interstate 15 interchange.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3759.7028851148757!2d-111.6581236!3d40.2349652!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x874d973766b6af87%3A0xf0e2f0ced4967b!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1790275334452!5m2!1sen!2sus'))

FAQ=[
 ("When should I book a car for a BYU student?","In August for the September start and in December for the January start, since Provo runs on a September and January calendar rather than an August one. Cars head home in late April. The streets around campus are tight, so the driver meets you at a lot nearby. An adult signs for the car."),
 ("Can you ship a car to a missionary who just returned?","Yes, and it is one of our steadiest Provo lanes. Returning missionaries often transfer in mid-semester and need a car sent from home, and we run that lane year round. Give us the arrival date, and we plan the delivery around it."),
 ("How much does it cost to ship a car from Provo to Los Angeles or Las Vegas?","Los Angeles usually runs four hundred eighty to seven hundred dollars for a sedan, about six hundred forty miles down Interstate 15. Las Vegas runs three hundred fifty to five hundred. Provo sits forty-five miles closer to both than Salt Lake City does. Larger vehicles add 10 to 25 percent."),
 ("Do you serve Orem and Utah Valley University?","Yes, Orem is ten minutes north and ships through this office. The university calendar runs a week or two off the Provo one, and its lots are wide, so the handoff happens at the edge of campus off University Parkway. Orem streets usually allow curbside."),
 ("Do you handle relocations to the tech companies in Provo and Lehi?","Yes, the companies headquartered in Provo and Orem and the cluster in Lehi relocate engineers from across the country on start dates. Corporate packages usually cover a vehicle, and we provide the documentation. Many newcomers buy across the lake in Vineyard or Saratoga Springs, so send the community name."),
 ("Can you deliver to Sundance or up Provo Canyon?","To the mouth of the canyon or Heber, yes. Provo Canyon on US 189 is fine for a carrier in good weather, but the road to Sundance climbs on switchbacks no trailer takes. The driver meets you at a lot at the canyon mouth, and the last leg is a short drive."),
 ("Does the Interstate 15 construction affect pickups in Provo?","Only for timing. The widening project moves lanes and closes ramps overnight, and carriers plan around it. The interchanges at University Avenue, Center Street, and University Parkway still put a truck within ten minutes of any address."),
 ("Why does the Denver lane from Provo swing with the weather?","Because it runs through Spanish Fork Canyon on US 6, which closes to high-profile vehicles in wind and snow more often than any road in the county. Carriers wait it out in Spanish Fork or Price, and a winter Denver pickup can slide a day."),
 ("Can you ship a car that does not run from Provo?","Yes, non-running cars ship out of Utah County regularly. A winch-equipped carrier loads it, and the extra loading time carries a fee. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Provo car shipping quote?","The pickup and delivery addresses, with the community name. The year, make, and model, and whether it is a minivan or a full-size SUV. Whether it runs and rolls. Open or enclosed, and the semester date you are working toward. That is everything an accurate Provo quote needs."),
]
BODY.append(faq_section(FAQ,'Provo FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Provo?','A quote takes about two minutes on the form above. Then tell us the semester date and your neighborhood, and we will plan the pickup around the calendar.','+13853508211','(385) 350-8211','Get your free Provo quote'))

build({
 'slug':'auto-transport-provo-utah',
 'title':'Car Shipping in Provo, UT — Auto Transport | Ship Guy',
 'meta':'Car shipping in Provo, UT on the September and January semester calendar. BYU and UVU timing, the returning-missionary lane, Silicon Slopes relocations, Vineyard new construction, Provo Canyon and Sundance handoffs, Spanish Fork Canyon closures. Local office on University Avenue. Free quote.',
 'h1':'Car Shipping in<br>Provo, <span class="accent">Utah</span>',
 'lede':'Open, enclosed, and expedited auto transport across Utah County, planned around the semester, the mission cycle, and the canyons.',
 'tel':'+13853508211','disp':'(385) 350-8211','brand':'Provo','keyword':'car shipping in provo',
 'localterms':['provo','utah county','interstate 15','university avenue','university parkway','center street','state street','us 189','us 6','interchange','construction','grid','byu','brigham young','semester','september','january','april','missionary','mission','stadium','900 east','orem','utah valley university','uvu','vineyard','lindon','pleasant grove','silicon slopes','lehi','headquarters','saratoga springs','eagle mountain','minivan','suv','family','provo canyon','sundance','heber','spanish fork canyon','springville','spanish fork','payson','santaquin','airport','utah lake','inversion','wind'],
}, BODY, FAQ)
