import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Metairie, Louisiana','Car shipping on the East Bank of Jefferson Parish, between Interstate 10 and the foot of the Causeway',
 ['Car shipping in Metairie runs off Interstate 10 and the Causeway interchange, the busiest crossing in the state. Ship Guy is a licensed auto transport broker with an office on North Causeway Boulevard.',
  'We book vetted carriers across the East Bank, from Old Metairie to Kenner and down to Harahan. We own none of the trucks.',
  'Interstate 10 runs the length of Metairie from the parish line to the airport in Kenner. The Causeway crosses the lake to Mandeville. Veterans Boulevard is the retail strip beside the interstate. Airline Drive runs the south side, and Clearview, Causeway, and Williams run north and south.',
  'This page covers 10, the Causeway, Veterans, Old Metairie, Bucktown, Kenner, and the river towns. It also covers the hospitals, the airport, the parades on Veterans, the pumps, the storms, and the lanes.'],
 'Metairie at a glance',
 ['Most pickups happen within 1 to 3 days. Metairie shares the New Orleans carrier pool. The trucks reach it first coming in from Baton Rouge and Houston.',
  'Baton Rouge is ninety minutes. Mobile, Jackson, and Houston are a same-day haul. Memphis, Atlanta, and Dallas take a day. Florida takes two, and Chicago and the East Coast take three to four.'],
 'Tell us the side of Veterans. Old Metairie and the streets off Metairie Road need a meeting spot. The grids north of Veterans, Kenner, and Harahan usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 10, the Causeway, Veterans Boulevard, Airline Drive, and Clearview Parkway',
 prose(
  L('Metairie is a grid of wide boulevards between the interstate and the lake. The trucks reach the curb on most of it.'),
  P('Interstate 10 crosses the whole of Metairie from the 17th Street Canal to the airport. The exits at Causeway, Clearview, Power, and Williams serve the East Bank. The Causeway interchange is the busiest in Louisiana. Every carrier between Houston and Florida passes it. Interstate 610 splits off at the parish line for the Orleans side.'),
  P('The Causeway runs twenty-four miles across the lake to Mandeville and Covington. The carriers cross it with the northbound toll built in. Wind and fog close it to high vehicles a few days a year. Veterans Boulevard runs beside the interstate as the retail strip, from the mall at Causeway to the airport. West Esplanade runs the lake side.'),
  P('Airline Drive is US 61, the old road on the south side. It runs past the stadium and the Saints facility to the airport and Baton Rouge. Metairie Road runs through the old town to the Orleans line. Clearview, Transcontinental, David, Power, and Williams cross the grid north and south. Jefferson Highway and the river road carry Harahan and River Ridge. The Huey P. Long Bridge crosses to the West Bank.'),
  P('The carriers come off 10 at Causeway and Clearview, and off Airline at the stadium. The mall on Veterans, the stadium on Airline, and the lakefront have the usual meeting lots. The Causeway toll is the only toll, and only northbound.'),
  P('Our office is on North Causeway Boulevard, minutes from Interstate 10 and the foot of the Causeway.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Old Metairie, the Veterans Grids, Bucktown and the Lakefront, Fat City, Elmwood, Kenner, and the River Towns',
 prose(
  L('Metairie is the suburb that New Orleans built on the high ground along the lake. The newer the street, the wider it runs.'),
  P('Old Metairie along Metairie Road is the oldest part, with big houses on narrow streets under live oaks. A trailer cannot get under the limbs. The driver meets you on Metairie Road or at the shopping center on Causeway. The streets between Metairie Road and the interstate are the same. The handoff moves to Causeway or Bonnabel.'),
  P('The grids north of Veterans to the lake are postwar subdivisions with wide streets and no trees overhead. The truck reaches the curb. Bucktown and the lakefront by the canal have the seafood houses and the boat launch. The lots by the lake work for a handoff. Fat City behind the mall is apartments and bars, and the handoff moves to the mall.'),
  P('The south side along Airline is the stadium, the practice facility, and older grids with wide streets. Elmwood to the west is the business park, the warehouses, and the studios, with room everywhere. Harahan and River Ridge along the river are quiet grids under big trees. The driver meets you on Jefferson Highway. Jefferson by the hospital is the same.'),
  P('Kenner to the west has the airport, the casino, and subdivisions from the last fifty years. The streets are wide, and the curb works. Across the lake, Mandeville, Covington, and Slidell are wide-street suburbs an hour away. The West Bank towns across the bridge price the same as Metairie, and so does the Orleans side.'),
 )))

ROUTES=[("Baton Rouge, LA","I-10 · ~75 mi","Same day","$160–$260"),("Mobile, AL","I-10 · ~150 mi","Same day","$220–$340"),
 ("Jackson, MS","I-55 · ~180 mi","1 day","$220–$340"),("Houston, TX","I-10 · ~345 mi","1 day","$320–$470"),
 ("Memphis, TN","I-55 · ~390 mi","1 day","$350–$510"),("Atlanta, GA","I-10/I-65/I-85 · ~475 mi","1–2 days","$400–$580"),
 ("Dallas, TX","I-49/I-20 · ~505 mi","1–2 days","$430–$620"),("Orlando, FL","I-10/I-75 · ~645 mi","2 days","$470–$680"),
 ("Chicago, IL","I-55 · ~920 mi","3 days","$650–$900"),("New York, NY","I-59/I-81 · ~1,305 mi","3–4 days","$820–$1,150")]
BODY.append(rate_table('Lanes &amp; Costs','Metairie Car Shipping Lanes and Estimated Costs',
 'The lanes East Bank cars take most, with estimated open-trailer ranges. Your exact route prices on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates priced from Metairie, open trailer, sedan that runs. SUVs and pickups land 10 to 25 percent higher, enclosed higher again. Storm season and the carriers free on your dates settle the real figure.',
 prose(
  P('Metairie prices with New Orleans on every lane. A carrier coming in on 10 reaches it before the city. The Houston and Baton Rouge lanes run daily. The Florida lanes rise in the fall with the snowbirds and ease in the spring. The Chicago and New York lanes ride 55 and 59 and run lighter.'),
  P('A storm in the Gulf clears the coast of carriers for a week. Every price moves with it. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Hospitals, the Airport, the Office Towers, the Film Studios, and the Transplants',
 prose(
  L('Metairie relocates nurses, airline staff, lawyers, and film crews. The hospital system moves more people than anyone.'),
  P('The hospital system headquartered on Jefferson Highway is the largest employer in the region. The hospital on Houma Boulevard sits in the middle of Metairie. Between them they hire nurses on contracts all year and take residents each June. Physicians come with a closing date and a second car. The paperwork for a reimbursed move comes from us.'),
  P('The airport in Kenner moves airline and ground staff in on short notice. The office towers at Causeway and the lake hold the energy-services firms, the law firms, and the insurers. They relocate staff in every month. The studios in Elmwood bring in crews for a production and send them home when it wraps.'),
  P('The football team trains on Airline Drive, and the front office relocates staff on the league calendar. The parish schools and the Catholic schools draw families from the Orleans side and from Houston. One car ships while the other is driven. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
  P('The naval air station across the river in Belle Chasse rotates sailors and families on orders. Many settle on the East Bank. Orders cover one car, and the family’s other car comes with us. Ship Guy is a private broker with no tie to the station. The <a href="military-car-shipping.html">military</a> page explains the timing.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The Parades on Veterans, Family Gras, Saints Camp, the Pumps, and the Hurricanes',
 prose(
  L('Metairie runs on a parade route, a training camp, and a drainage system that decides the day.'),
  P('The Metairie parades roll on Veterans Boulevard on the weekends before Mardi Gras, from Clearview to Severn. The boulevard closes from the afternoon, and the mall lots fill with ladders and chairs. A pickup along Veterans on a parade day moves to Airline or to the morning. Family Gras fills the mall lot the weekend before. The Orleans parades pull the carriers off the parish line the same days.'),
  P('Training camp on Airline fills the practice facility lots for three weeks in August. The Fourth of July fills the lakefront and the park on Downs Boulevard. The seafood festival fills Bucktown on an October weekend. A handoff near any of them moves to the daytime or to another lot.'),
  P('The pumps decide the street. Metairie sits below sea level. A summer downpour floods the low streets for an hour until the pumps catch up. The driver waits it out. In 2005 the pumps sat unmanned, and the east side of Metairie flooded from rain. The Orleans side flooded from the canal. The pumps are staffed through every storm now.'),
  P('Hurricane season runs from June through November. Zeta crossed Metairie in October 2020, and Ida took the power down for ten days in 2021. When a storm enters the Gulf, the carriers pull back from the coast days ahead. Contraflow on 10 stops everything else. We rebook the week after. Wind and fog close the Causeway to high vehicles a few days a year. Summer heat moves the loading hour to the morning.'),
 )+chips(["Old Metairie","Metairie Road","Bonnabel","Causeway","Lakeside","Fat City","Veterans","Clearview","Transcontinental","David Drive","Power Boulevard","West Esplanade","Bucktown","Lakefront","Severn","Airline Drive","Stadium","Saints Facility","Elmwood","Harahan","River Ridge","Jefferson","Ochsner","Kenner","Williams","Airport","Laketown","Rivertown","Mandeville","Covington","Slidell","West Bank"])
 +NOTE('Serving Metairie, Kenner, and the East Bank of Jefferson Parish, oak street or open grid. Tell us the side of Veterans and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Metairie?',
 prose(
  L('Open trailers move most East Bank cars, and the lane table is priced for one.'),
  P('An enclosed trailer keeps the rain, the grime, and the salt air off a car. The garages in Old Metairie book one for the collector cars. Families sending a car to a student in Texas or Florida book one too.'),
  P('The carpool SUV and the commuter car go open and arrive the way they left. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages put the two side by side.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A number, a handoff at the mall or the stadium, and a signature at delivery. The closing date or the storm calendar sets the week.'),
  P('Say yes to the number, and the car goes to a carrier already working 10. The meeting lot and the window follow within hours. At the handoff the driver and you walk around the car. The Bill of Lading records every mark already on it. Two signatures, and the same sheet settles the delivery.'),
 )+ULI([
  "Clear the cabin and the trunk of anything personal",
  "Run the tank down to about a quarter",
  "Photograph the car on all four sides, plus the mileage",
  "Pass the driver one working key and point out any fault",
  "Kill any aftermarket alarm before the handoff",
  "In Old Metairie, meet the truck on Metairie Road or at the shopping center on Causeway",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Metairie Drivers Choose Ship Guy',
 prose(
  L('We catch the carriers on 10 before they reach the city. We plan around the parades, the pumps, and the storm calendar.'),
  P('Ship Guy carries FMCSA brokerage authority and a $75,000 surety bond, both on the federal register. The office is on North Causeway Boulevard.'),
  P('The coordinator who prices the move keeps it until the delivery sheet is signed. Open, enclosed, and expedited transport are on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Metairie','2121 N Causeway Blvd #554A','Metairie, LA 70001','+15045141757','(504) 514-1757','CT',
 '2121+N+Causeway+Blvd+%23554A,+Metairie,+LA+70001','Visit Us','Find Ship Guy in Metairie',
 'Our office is on North Causeway Boulevard, minutes from Interstate 10 and the foot of the Causeway.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5313.840262018561!2d-90.1548384!3d29.991757399999997!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8620b19e53e2dbd5%3A0xb6927c557b317489!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793025016464!5m2!1sen!2sus'))

FAQ=[
 ("How much does it cost to ship a car from Metairie to Houston or Baton Rouge?","Houston runs three hundred twenty to four hundred seventy dollars for a sedan. That is about three hundred forty-five miles down 10. Baton Rouge runs one hundred sixty to two hundred sixty, about seventy-five miles the same way. Mobile and Jackson price between the two. An SUV or pickup adds 10 to 25 percent. Metairie prices with New Orleans on every lane."),
 ("Can the carrier come to my street in Old Metairie?","Usually not. Metairie Road and the streets around it run under live oaks. A trailer cannot get under the limbs. The driver meets you on Metairie Road, at the shopping center on Causeway, or on Bonnabel. The grids north of Veterans, Kenner, and Harahan usually allow the curb."),
 ("Do the Mardi Gras parades on Veterans affect my pickup?","Yes, on the parade weekends. Veterans closes from Clearview to Severn from the afternoon, and the mall lots fill with ladders by noon. We move a pickup along Veterans on a parade day to Airline or to the morning. The Orleans parades pull the carriers off the parish line the same days. The rest of the year, Veterans is the easiest street in the parish."),
 ("Do you ship cars for people relocating to the hospitals or the airport?","Yes, all year. The hospital system on Jefferson Highway and the hospital on Houma Boulevard hire nurses and physicians every month. The airport moves airline staff in on short notice. Many ship a second car behind the move. The handoff works at the mall lot or the stadium lot. We provide the paperwork a reimbursed move needs."),
 ("Can you ship a car to or from Kenner, Harahan, or across the lake?","Yes, and all of them price the same as Metairie. Kenner rides the same carriers off 10 at Williams. The handoff works at the airport or the casino lot. Harahan and River Ridge ride them off Jefferson Highway. Mandeville and Covington ride them across the Causeway with the toll built in. Send the full address for a new subdivision on the Northshore."),
 ("What happens if a hurricane is in the Gulf on my pickup day?","Three days out from landfall the carriers are gone from the coast, and contraflow turns 10 one way. Your pickup moves to the week after the storm. A car already on a trailer keeps going inland. On an ordinary summer afternoon, a downpour floods the low streets until the pumps catch up. The driver simply waits the hour. We call at every change."),
 ("Does the carrier use the Causeway?","Going north, yes. A carrier bound for Mandeville or Covington crosses the Causeway and pays the northbound toll. It rides inside the quote. Wind and fog close the bridge to high vehicles a few days a year. On those days the carrier goes around by 10 and 12. The price does not change either way."),
 ("Can you ship a car that does not run from Metairie?","Yes. We dispatch a carrier with a winch, and the loading time is inside the quote from the start. The mall lot on Veterans or the stadium lot gives the driver somewhere flat to winch from. Say whether the wheels turn, the steering works, and the brakes hold."),
 ("Do you ship cars for sailors at the naval air station?","Yes. The station in Belle Chasse rotates sailors and families on orders, and many settle in Metairie and Kenner. The orders pay for one car, and we move the other. Ship Guy is a private broker with no connection to the station. Send the report date, and we build the window around it."),
 ("What do you need for a Metairie car shipping quote?","Pickup and delivery addresses, with the side of Veterans or the town. Year, make, model. Whether it drives. Open or enclosed. The week you want it gone. With those five, the Metairie quote comes back within the day."),
]
BODY.append(faq_section(FAQ,'Metairie FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Metairie?','Two minutes on the form above prices your lane. Send the side of Veterans and your dates, and a carrier already on 10 takes it.','+15045141757','(504) 514-1757','Get your free Metairie quote'))

build({
 'slug':'auto-transport-metairie-louisiana',
 'title':'Car Shipping in Metairie, LA — Auto Transport | Ship Guy',
 'meta':'Car shipping in Metairie, LA on the East Bank of Jefferson Parish, between Interstate 10 and the Causeway. Hospital and airport relocations, Old Metairie meeting spots, Veterans-grid and Kenner curbside pickups, the parades on Veterans, the Causeway and its toll, the pumps, and hurricane season. Local office on North Causeway Boulevard. Free quote.',
 'h1':'Car Shipping in<br>Metairie, <span class="accent">Louisiana</span>',
 'lede':'Open, enclosed, and expedited auto transport across the East Bank, planned around 10, the Causeway, the parades, the pumps, and the storm calendar.',
 'tel':'+15045141757','disp':'(504) 514-1757','brand':'Metairie','keyword':'car shipping in metairie',
 'localterms':['metairie','east bank','jefferson parish','interstate 10','causeway','interchange','interstate 610','17th street canal','veterans','mall','west esplanade','airline drive','us 61','metairie road','clearview','transcontinental','david','power','williams','jefferson highway','river road','huey p. long','west bank','old metairie','live oaks','bonnabel','grids','bucktown','lakefront','boat launch','fat city','stadium','practice facility','saints','elmwood','warehouses','studios','harahan','river ridge','jefferson','hospital','kenner','airport','casino','mandeville','covington','slidell','northshore','orleans','hospital system','houma boulevard','nurses','residents','office towers','law firms','energy-services','film','crews','football team','schools','transplants','naval air station','belle chasse','orders','parades','mardi gras','ladders','family gras','training camp','fourth of july','seafood festival','pumps','sea level','2005','zeta','2020','ida','2021','contraflow','wind','fog','toll','baton rouge','mobile','jackson','houston','memphis','atlanta','dallas','orlando','chicago','new york','florida'],
}, BODY, FAQ)
