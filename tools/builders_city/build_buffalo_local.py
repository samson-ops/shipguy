import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Buffalo, New York','Car shipping at the end of the Thruway, where the lake writes the schedule',
 ['Car shipping in Buffalo is planned around the Thruway and the lake. Ship Guy is a licensed auto transport broker with an office on Main Street downtown.',
  'We book vetted carriers across Erie and Niagara Counties, from the Southtowns to Niagara Falls. We do not own the trucks.',
  'Interstate 90 ends its run across the state here and turns south toward Erie and Cleveland. Interstate 190 carries the city to the Peace Bridge and the falls. Interstate 290 and the Kensington connect the suburbs and the airport.',
  'This page covers the Thruway and the border, the medical campus, the university, and the neighborhoods. It also covers the lake-effect winter, the Florida lane, the Bills calendar, and the lanes.'],
 'Buffalo at a glance',
 ['Most pickups happen within 1 to 3 days, longer in a lake-effect week. The Interstate 90 freight lane brings carriers through every day.',
  'Rochester, Cleveland, and Pittsburgh are same-day lanes. New York City and Boston take a day. Chicago runs one to two, and Florida runs three to four.'],
 'Tell us the neighborhood and the month. Elmwood and Allentown need a meeting spot. Amherst and Clarence allow the curb, and January adds a day.'))

BODY.append(sec('The Thruway &amp; the Border','Interstate 90, 190, 290, and the Peace Bridge',
 prose(
  L('Buffalo is where the Thruway ends and the Great Lakes freight lane begins.'),
  P('Interstate 90 arrives from Rochester and Albany as the Thruway, with a toll by the mile. South of the city it continues to Erie, Cleveland, and Chicago. Every carrier moving between New England and the Midwest passes the toll barrier at Williamsville.'),
  P('Interstate 190 runs from the Thruway through downtown, across Grand Island, and up to Niagara Falls. Interstate 290 crosses the north suburbs, and the Kensington Expressway carries the airport traffic. Route 5 runs the lakeshore south to Hamburg.'),
  P('The Peace Bridge carries trucks to Fort Erie and the Queen Elizabeth Way. Our carriers do not cross into Canada. A car coming from Ontario clears customs on the Buffalo side. The handoff happens near the bridge plaza.'),
  P('The Thruway toll is paid by the carrier and built into every quote. Interstate 190 and 290 carry no toll beyond the Grand Island bridges.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Elmwood, Allentown, North Buffalo, the Southtowns, and Amherst',
 prose(
  L('Buffalo was built for streetcars, and the streets that made it charming were not made for a trailer.'),
  P('Elmwood Village, Allentown, and the Delaware District have narrow streets and old elms overhead. Cars park on both sides. The driver meets you on Delaware Avenue, Elmwood near the park, or a lot off the Scajaquada.'),
  P('North Buffalo, Parkside, and the Hertel strip are tighter still. South Buffalo and Kaisertown are blocks of doubles with alley garages. The handoff happens on Seneca Street, Abbott Road, or a main road nearby. Downtown runs on garages, and our office sits on Main Street in the middle of it.'),
  P('Amherst, Williamsville, Clarence, and Lancaster are wide suburban grids where the truck usually reaches the curb. Cheektowaga and Depew near the airport are the same. Orchard Park, Hamburg, and East Aurora are open except in a lake-effect week.'),
  P('Tonawanda, Kenmore, and Grand Island sit along Interstate 190 and schedule easily. Niagara Falls is twenty minutes north, and Lockport sits on the canal to the northeast.'),
 )))

ROUTES=[("Rochester, NY","I-90 · ~75 mi","Same day","$160–$260"),("Syracuse, NY","I-90 · ~150 mi","Same day","$190–$300"),
 ("Cleveland, OH","I-90 · ~190 mi","Same day","$210–$330"),("Pittsburgh, PA","I-90/I-79 · ~215 mi","Same day","$230–$350"),
 ("Detroit, MI","I-90/I-75 · ~360 mi","1 day","$340–$480"),("Washington, DC","I-90/I-79/I-70 · ~380 mi","1 day","$370–$530"),
 ("New York, NY","I-90/I-87 · ~400 mi","1 day","$390–$550"),("Boston, MA","I-90 · ~450 mi","1 day","$420–$600"),
 ("Chicago, IL","I-90 · ~540 mi","1–2 days","$450–$640"),("Fort Myers, FL","I-79/I-77/I-95 · ~1,350 mi","3–4 days","$900–$1,300")]
BODY.append(rate_table('Lanes &amp; Costs','Buffalo Car Shipping Lanes and Estimated Costs',
 'The lanes Buffalo households and employers ask about most, with estimated open-transport ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates, running sedan, open trailer. SUVs and pickups add roughly 10 to 25 percent, and enclosed adds more. Thruway tolls are included. Lake-effect weeks and carrier availability on your dates set the real quote.',
 prose(
  P('Rochester, Cleveland, and Pittsburgh are the quick lanes, all within four hours on roads carriers run every day. Chicago rides Interstate 90 straight across Ohio and Indiana.'),
  P('Detroit is closer through Ontario, but carriers go around the lake through Cleveland and Toledo instead. The <a href="car-shipping-cost.html">cost guide</a> explains the rest of the number.'),
 ), alt=True))

BODY.append(sec('The Lake-Effect Winter','Snow Bands, Driving Bans, and the Thruway Closures',
 prose(
  L('Buffalo gets its snow in bands. One side of the city can be buried while the other side sees sun.'),
  P('Lake-effect season runs from November into March. The bands set up off Lake Erie and bury the Southtowns, Orchard Park, Hamburg, and South Buffalo. The Northtowns often stay clear. A single storm can drop several feet in two days.'),
  P('When a band sets up, the state closes the Thruway to trucks and the city issues driving bans. Carriers wait it out at the truck stops in Pembroke or Dunkirk. A pickup can slide a day or two. We call the moment the forecast changes the plan.'),
  P('Road salt runs from November through April, and collector-car owners ride enclosed for that reason. A car arriving from a warm state needs a strong battery and winter oil.'),
  P('Spring brings ice jams on the creeks. Wind closes the Grand Island bridges now and then. Summer is the easy season.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Medical Campus, the University, the Plants, and the Bills',
 prose(
  L('Buffalo ships on residency match day, the university calendar, the auto plants, and a football schedule.'),
  P('The medical campus downtown brings in residents, fellows, and research staff every June and July. The handoff happens on Main Street or Ellicott Street rather than in a hospital garage. Most of those cars come from out of state.'),
  P('The university moves tens of thousands of students through the Amherst campus, the South Campus, and downtown. August and May are the peaks. The driver meets you at a lot on Millersport or Main Street. An adult signs for a student car.'),
  P('The engine plant in Tonawanda and the stamping plant in Hamburg transfer engineers on production cycles. The solar plant in South Buffalo does the same. The bank headquarters downtown relocates staff on start dates. If your employer reimburses the shipment, we send the documentation.'),
  P('Home games in Orchard Park fill Route 20 and the Southtowns roads for hours. We schedule Southtowns pickups on other days of the week. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the longer relocation.'),
 )))

BODY.append(sec('The Florida Lane','Fort Myers, Naples, and the Snowbird Season',
 prose(
  L('Buffalo empties toward the Gulf coast of Florida every fall, and the cars go by trailer.'),
  P('Amherst, Williamsville, and the Southtowns ship their cars to Fort Myers, Naples, and Sarasota between October and December. The cars come home in April, May, and June. Interstate 79 and 77 carry the trip south through the mountains.'),
  P('Two to three weeks of notice keeps the price steady in season. Northbound in spring is the cheaper direction. Our <a href="snowbird-car-shipping.html">snowbird</a> page has the planning tips.'),
  P('Myrtle Beach and the Carolinas take a smaller wave on the same roads.'),
 )+chips(["Downtown","Canalside","Elmwood Village","Allentown","Delaware District","North Buffalo","Parkside","Hertel","University Heights","West Side","South Buffalo","Kaisertown","Larkinville","Amherst","Williamsville","Clarence","Cheektowaga","Depew","Lancaster","Tonawanda","Kenmore","Grand Island","West Seneca","Orchard Park","Hamburg","East Aurora","Lackawanna","Niagara Falls","Lockport"])
 +NOTE('Serving Erie and Niagara Counties. Tell us the neighborhood, the month, and whether the car runs.'), alt=True))

BODY.append(sec('Your Options','Open or Enclosed in Buffalo?',
 prose(
  L('Open transport carries most of Buffalo, and the Interstate 90 lanes run on it.'),
  P('Enclosed transport keeps a car covered against road salt, slush, and lake grit. The collector garages in the Delaware District and East Aurora book enclosed trailers. A car wintering in Naples often does too.'),
  P('A commuter car rides open without trouble. Our <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages lay out each option.'),
 )))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a loading near the Thruway, and a delivery. In winter, the lake has a vote on the timing.'),
  P('Once you approve the price, a carrier already running Interstate 90 takes the booking. The driver notes the car’s condition on a Bill of Lading at the meeting spot. You sign it, and you compare the car to it at delivery.'),
 )+ULI([
  "Remove personal belongings",
  "Keep about a quarter tank of fuel",
  "Photograph the vehicle before pickup, especially after a salty winter",
  "Provide a working key and disclose mechanical issues",
  "Disable aftermarket alarms",
  "In Elmwood, Allentown, or North Buffalo, plan to meet the truck on Delaware or at a lot",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> guides take it step by step.')), alt=True))

BODY.append(sec('Why Ship Guy','Why Buffalo Drivers Choose Ship Guy',
 prose(
  L('We work the Interstate 90 lane every day and plan around the bands, the border, and the Bills.'),
  P('Active FMCSA brokerage authority and a $75,000 surety bond stand behind every booking we make. Our office is on Main Street downtown.'),
  P('One coordinator carries your shipment from quote to delivery and can book open, enclosed, or expedited transport. The <a href="services.html">services</a> page shows the full lineup.'),
 )))

BODY.append(office('Buffalo','424 Main St #497','Buffalo, NY 14202','+17164665036','(716) 466-5036','ET',
 '424+Main+St+%23497,+Buffalo,+NY+14202','Visit Us','Find Ship Guy in Buffalo',
 'Our office is on Main Street downtown, steps from the Metro Rail and minutes from Interstate 190.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4944.646331386509!2d-78.8749125!3d42.8856402!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89d313efa4a5a69b%3A0x1f06578fef8aceb!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792023112932!5m2!1sen!2sus'))

FAQ=[
 ("Does lake-effect snow delay a Buffalo pickup?","Sometimes by a day or two. When a band sets up over the Southtowns, the state closes the Thruway to trucks. The city issues driving bans. Carriers wait at the truck stops until the roads open. We tell you the moment the forecast shifts the plan."),
 ("How much does it cost to ship a car from Buffalo to Florida?","Nine hundred to thirteen hundred dollars for a sedan to Fort Myers, and a bit less to Orlando. The route runs about thirteen hundred miles down Interstate 79, 77, and 95. November southbound costs more than July. SUVs and pickups add 10 to 25 percent."),
 ("Is the Thruway toll added to my price?","No. The carrier pays the Thruway by the mile and prices the trip accordingly. The toll is folded into the number you approve. Interstate 190 and 290 carry no toll beyond the Grand Island bridges."),
 ("Can you ship a car across the Peace Bridge from Canada?","Our carriers stay on the American side. You or your customs broker clear the car at the Peace Bridge. The handoff happens near the bridge plaza in Buffalo. From there we ship it anywhere in the country."),
 ("Can the carrier come to my house in Elmwood Village or Allentown?","Rarely. The streets are narrow, cars park on both sides, and the elms hang low. The driver meets you on Delaware Avenue, on Elmwood near the park, or at a lot nearby. Amherst, Clarence, and Cheektowaga usually allow curbside."),
 ("Do you ship cars for residents at the medical campus?","Yes, every June and July. The hospitals and the research buildings downtown bring in residents and fellows from every state. The handoff happens on Main Street or Ellicott Street rather than in a hospital garage. Most arrive with two weeks of notice, and we plan around the start date."),
 ("Does a Bills home game affect my pickup?","In the Southtowns, yes. Route 20 and the roads around Orchard Park fill for hours on game days. We schedule Orchard Park, Hamburg, and West Seneca pickups on other days of that week. The rest of the metro runs normally."),
 ("Can you ship a car for a UB or Buffalo State student?","Yes. Student cars arrive each August and leave each May. The driver meets you at a lot on Millersport Highway or Main Street rather than on campus. An adult signs for the car at pickup, and a winter arrival needs a strong battery."),
 ("Can you ship a car that does not run from Buffalo?","Yes. A carrier with a winch takes a car that will not start. The extra loading time is part of the price. In winter, dig the car out before the truck arrives. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Buffalo car shipping quote?","Both addresses, with the neighborhood on the Buffalo end. The year, make, and model. Whether it runs and rolls. Open or enclosed, and the dates, with the month in mind. That is a complete Buffalo quote request."),
]
BODY.append(faq_section(FAQ,'Buffalo FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Buffalo?','The form above takes about two minutes. Tell us the neighborhood and your dates. We will match you with a carrier already on the Thruway.','+17164665036','(716) 466-5036','Get your free Buffalo quote'))

build({
 'slug':'auto-transport-buffalo-new-york',
 'title':'Car Shipping in Buffalo, NY — Auto Transport | Ship Guy',
 'meta':'Car shipping in Buffalo, NY on the Interstate 90 freight lane. Lake-effect planning, Elmwood and Allentown handoffs, the medical campus and UB calendar, the Peace Bridge, the Fort Myers snowbird lane, Thruway tolls built in. Local office on Main Street downtown. Free quote.',
 'h1':'Car Shipping in<br>Buffalo, <span class="accent">New York</span>',
 'lede':'Open, enclosed, and expedited auto transport across Erie and Niagara Counties, planned around the Thruway, the lake, and the season.',
 'tel':'+17164665036','disp':'(716) 466-5036','brand':'Buffalo','keyword':'car shipping in buffalo',
 'localterms':['buffalo','interstate 90','thruway','interstate 190','interstate 290','kensington','scajaquada','route 5','peace bridge','grand island','niagara falls','williamsville','elmwood','allentown','delaware','north buffalo','parkside','hertel','south buffalo','kaisertown','downtown','main street','amherst','clarence','lancaster','cheektowaga','depew','orchard park','hamburg','east aurora','tonawanda','kenmore','lockport','lake-effect','southtowns','driving ban','salt','medical campus','residents','university','students','engine plant','stamping plant','solar','bank','bills','fort myers','naples','snowbird','rochester','cleveland','pittsburgh','chicago','detroit'],
}, BODY, FAQ)
