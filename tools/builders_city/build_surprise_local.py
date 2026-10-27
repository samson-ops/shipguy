import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Surprise, Arizona','Car shipping in the Northwest Valley, where Grand Avenue meets the 303 on the road to Las Vegas',
 ['Car shipping in Surprise runs off Grand Avenue and the 303, the roads that opened the Northwest Valley. Ship Guy is a licensed auto transport broker with an office on Bell Road by the stadium.',
  'We arrange vetted carriers across the Northwest Valley, from Sun City West to Waddell and north to Wittmann. We own none of the trucks.',
  'US 60 is Grand Avenue, the diagonal from Phoenix through the city to Wickenburg and Las Vegas. Loop 303 crosses the west side from the 10 to Grand. Bell Road is the retail strip across the middle. Litchfield, Bullard, Reems, and Cotton run north and south between them.',
  'This page covers Grand, the 303, Bell Road, the original townsite, the Del Webb communities, and Marley Park. It also covers the base, the snowbirds, spring training, the haboobs, and the lanes.'],
 'Surprise at a glance',
 ['Most pickups happen within 1 to 3 days. The Las Vegas carriers pass the city on Grand. The 303 brings the California trucks up from the 10.',
  'Phoenix is thirty minutes. Las Vegas, Flagstaff, Tucson, and the California coast are a same-day haul. Salt Lake City takes a day. Denver takes two, and the Midwest takes three to four.'],
 'Tell us the side of Grand. The original townsite and the oldest grids need a meeting spot. The Del Webb communities, Marley Park, and the subdivisions west of Reems usually allow the curb.'))

BODY.append(sec('The Roads','Grand Avenue, Loop 303, Bell Road, Litchfield Road, and the Railroad Crossings',
 prose(
  L('Surprise is the last city on the Las Vegas road before the desert. The carriers pass it in both directions all day.'),
  P('US 60 is Grand Avenue, the diagonal that runs from downtown Phoenix through Glendale and Surprise to Wickenburg. North of Wickenburg it becomes the Las Vegas road on US 93. The railroad runs beside it the whole way. The crossings at Bell, Greenway, and Waddell stop traffic for the trains. Every carrier between the Valley and Las Vegas uses Grand.'),
  P('Loop 303 crosses the west side of the city from the 10 at Goodyear to Grand. The exits at Waddell, Cactus, Peoria, Bell, Greenway, and Happy Valley serve the city. The California carriers come up the 303 from the 10. The Flagstaff trucks take it to the 17. Loop 101 sits five miles east at the Peoria line.'),
  P('Bell Road is the retail strip across the middle of the city, from Sun City to the 303. The bridge carries it over Grand at the busiest corner in the Northwest Valley. Greenway, Waddell, Cactus, and Peoria cross the city east and west. Litchfield, Dysart, Bullard, Reems, Cotton, and Perryville run north and south. Sun Valley Parkway runs south to Buckeye around the mountains.'),
  P('The carriers come off Grand at Bell and off the 303 at Bell and Waddell. The stadium on Bell, the shopping centers by the 303, and the civic center have the meeting lots. No road in the Valley charges a toll.'),
  P('Our office is on Bell Road by the stadium and the civic center, a minute from Bullard Avenue.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','The Original Townsite, Sun City Grand and Sun City West, Marley Park, the Bell Road Grids, West of Reems, and the Towns Around',
 prose(
  L('Surprise was a few blocks on Grand Avenue until the builders arrived. Now it runs for ten miles in every direction.'),
  P('The original townsite sits in the triangle at Grand and Bell. It is a few blocks of small lots and narrow streets. The driver meets you on Bell or at the stadium lots. The oldest subdivisions along Dysart and the El Mirage line have narrow streets too. The handoff moves to the main road. Everything built after 1990 has wide streets.'),
  P('Sun City Grand north of Bell and Sun City West beyond it are the Del Webb communities. They are age-restricted and built around the golf courses. The streets are wide, and the golf carts have their own lanes. The truck reaches the curb on most of them. Some gated sections wait for the handoff at the gate. Arizona Traditions and Sun Village run the same way.'),
  P('Marley Park and the grids off Bullard and Reems are the family subdivisions from the last twenty-five years. The streets are wide, with alleys behind. The truck reaches the curb. The communities along the 303 at Prasada and Asante are the newest. The streets are not on every map yet. Send the full address.'),
  P('West of Reems toward the White Tanks, the subdivisions give way to ranches and the regional park. The driver meets you on Waddell or Olive. Waddell and Wittmann are the country towns, and El Mirage and Youngtown to the east are older grids. Luke sits ten minutes south. All of them price the same as Surprise, and so do Peoria and Glendale.'),
 )))

ROUTES=[("Phoenix, AZ","US-60 · ~25 mi","Same day","$120–$200"),("Tucson, AZ","Loop 303/I-10 · ~140 mi","Same day","$170–$280"),
 ("Flagstaff, AZ","Loop 303/I-17 · ~150 mi","1 day","$170–$280"),("Las Vegas, NV","US-60/US-93 · ~260 mi","1 day","$250–$370"),
 ("San Diego, CA","Loop 303/I-10/I-8 · ~340 mi","1 day","$330–$470"),("Los Angeles, CA","Loop 303/I-10 · ~355 mi","1 day","$340–$490"),
 ("Salt Lake City, UT","US-93/I-15 · ~630 mi","2 days","$480–$690"),("Denver, CO","I-17/I-40/I-25 · ~840 mi","2 days","$560–$800"),
 ("Seattle, WA","Loop 303/I-10/I-5 · ~1,400 mi","3 days","$950–$1,350"),("Minneapolis, MN","I-40/I-35 · ~1,720 mi","3–4 days","$1,000–$1,450")]
BODY.append(rate_table('Lanes &amp; Costs','Surprise Car Shipping Lanes and Estimated Costs',
 'The lanes Northwest Valley cars take most, with estimated open-trailer ranges. Your exact route prices on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates out of Surprise, sedan in running order, open trailer. SUVs and pickups run 10 to 25 percent higher, and an enclosed trailer higher still. The snowbird months run higher inbound in the fall and outbound in the spring. The trucks free on your dates settle the final price.',
 prose(
  P('Surprise prices with Phoenix on the California and eastern lanes. The Las Vegas lane prices under the rest of the Valley. The carriers pass the door on Grand and pick the car up on the way out. The Salt Lake lane rides the same road north. The Midwest and Canadian-border lanes fill with snowbird cars each October and April.'),
  P('From October through April, book two to three weeks ahead, because the inbound snowbird cars take the space. The <a href="car-shipping-cost.html">cost guide</a> covers vehicle size, condition, and the rest.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Snowbirds, the Base, the Hospitals, the Schools, and the Transplants',
 prose(
  L('Surprise relocates retirees, airmen, nurses, and families priced out of the East Valley. The snowbirds move more cars than anyone.'),
  P('The Del Webb communities fill from October through April with retirees from the Midwest, the Northwest, and Canada. Most ship a car down in the fall and home in the spring. The Canadians keep a car here year round. It ships to a US address when they sell or move. The fall trucks fill by September, and the spring trucks fill by March.'),
  P('The base south of the city trains fighter pilots on class cycles. It rotates airmen on orders all year. Many families settle in Marley Park and the grids off Bullard. The orders cover one car, and we move the other. Base housing sits behind a gate, so the handoff happens outside it. Ship Guy is a private broker with no tie to the base. The timing around a report date is on the <a href="military-car-shipping.html">military</a> page.'),
  P('The hospital in Sun City West and the new hospitals along the 303 bring in nurses all year. Physicians arrive with a closing date and a second car. The school district is the largest employer in the city and moves teachers in each July. The spring-training teams move staff in each January. We supply the paperwork a reimbursed move needs.'),
  P('Families from California and the East Valley buy west of Reems on closing dates in every month. One car ships while the other is driven. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Spring Training, the Snowbird Turnover, the Fourth at the Stadium, the Haboobs, and the Heat',
 prose(
  L('Surprise runs on a spring-training month, two snowbird turnovers, and a summer that empties the Del Webb streets.'),
  P('Spring training brings the Royals and the Rangers to the stadium on Bell from February into March. The lots fill by ten, and Bell backs up from Bullard to Grand. A pickup near the stadium on a game day moves to the morning or to the 303 side. The Fourth of July fills the recreation campus for the fireworks. The festival in October does the same.'),
  P('The snowbird turnover is the other calendar. The communities fill in October and November, and the carriers run full coming in. They empty in March and April, and the carriers run full going out. A car moving against that tide rides cheaper and sooner. A car moving with it needs two to three weeks of notice.'),
  P('The heat is the weather. Summer passes one hundred ten degrees for weeks. The Northwest Valley runs hotter than the center of town. The loading hour moves to dawn from June through September. Half the Del Webb streets sit empty all summer. A summer pickup there is the easiest in the Valley.'),
  P('The monsoon runs July into September. A haboob rolls in from the southwest and closes Grand and the 303 for an hour. The driver waits it out. A flash flood closes the Agua Fria crossings at Olive and Northern and the washes west of Reems. The 2014 storm flooded the West Valley for a day. Winter is the easy season, and the frost never reaches the roads.'),
 )+chips(["Original Townsite","Grand Avenue","Bell Road","Stadium","Civic Center","Dysart","Litchfield","Sun City Grand","Sun City West","Arizona Traditions","Sun Village","Marley Park","Bullard","Greenway","Reems","Cotton","Prasada","Asante","Sierra Montana","Rancho Gabriela","Surprise Farms","Greer Ranch","Mountain Vista","Waddell","White Tanks","Wittmann","El Mirage","Youngtown","Luke","Peoria","Glendale","Wickenburg"])
 +NOTE('Serving Surprise, Sun City West, and the whole Northwest Valley, golf-cart street or ranch road. Tell us the side of Grand and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Surprise?',
 prose(
  L('Nine cars in ten leave the Northwest Valley on an open trailer. The table above is priced that way.'),
  P('An enclosed trailer shuts out the sun, the dust, and the gravel. Snowbirds with a new car book one for the trip down each fall. The collectors in Sun City Grand book one for the show in Scottsdale each January.'),
  P('A golf-cart-town sedan or a ranch truck rides open and arrives fine, dust and all. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain the trade-off.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A number, a handoff at the stadium lot or by the 303, and a car at delivery. The snowbird calendar sets the week.'),
  P('Say yes to the number, and we pair the car with a carrier already running Grand. The lot and the window come back within hours. The driver walks the car with you and records every existing mark on the Bill of Lading. Both of you sign, and the sheet settles the delivery.'),
 )+ULI([
  "Empty the car of anything personal, trunk included",
  "Leave about a quarter tank of fuel",
  "Take dated photos of every panel and the mileage",
  "Hand the driver one working key and describe any fault",
  "Turn off any aftermarket alarm",
  "In a gated section, the handoff waits at the gate, so send the code ahead",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages go through each step.'))))

BODY.append(sec('Why Ship Guy','Why Surprise Drivers Choose Ship Guy',
 prose(
  L('We catch the Las Vegas carriers on Grand and the California carriers on the 303. We plan around the snowbird tide, the base calendar, and the heat.'),
  P('Ship Guy carries FMCSA brokerage authority and a $75,000 surety bond, both on the federal register. Our office is on Bell Road by the stadium.'),
  P('The coordinator who prices the move stays with it until the car is signed for. Open, enclosed, and expedited transport are on the <a href="services.html">services</a> page.'),
 )))

BODY.append(office('Surprise','15331 W Bell Rd #558','Surprise, AZ 85374','+19284595190','(928) 459-5190','MST',
 '15331+W+Bell+Rd+%23558,+Surprise,+AZ+85374','Visit Us','Find Ship Guy in Surprise',
 'Our office is on Bell Road by the stadium and the civic center, a minute from Bullard Avenue.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5108.065980677788!2d-112.3903701!3d33.6375497!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x872b45611c593def%3A0x895d0f4a1e401252!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793025129811!5m2!1sen!2sus', alt=True))

FAQ=[
 ("Can you ship a snowbird’s car down to Surprise in the fall and home in the spring?","Yes, and it is the move we make most. Cars come from the Midwest, the Northwest, and the border states each October and go home each April. Book two to three weeks ahead, because the carriers run full with the tide. A car moving against the tide rides cheaper and sooner. The driver meets you at the curb in Sun City Grand or at the gate."),
 ("How much does it cost to ship a car from Surprise to Las Vegas or Los Angeles?","Las Vegas runs two hundred fifty to three hundred seventy dollars for a sedan. That is about two hundred sixty miles up Grand and 93. Los Angeles runs three hundred forty to four hundred ninety, about three hundred fifty-five miles down the 10. Surprise prices under the rest of the Valley on the Las Vegas lane, since the carriers pass by. Count on 10 to 25 percent more for an SUV or a pickup."),
 ("Can the carrier come to my street in Sun City Grand or Marley Park?","Usually, yes. Both have wide streets, and the truck reaches the curb on most of them. Some sections of the Del Webb communities sit behind a gate. The handoff waits at the gate or the clubhouse lot. The original townsite and the oldest grids along Dysart are narrow. The driver meets you on Bell or at the stadium lots."),
 ("Do you ship cars for airmen at Luke who live in Surprise?","Yes, all year. Airmen and families arrive on orders on class cycles. They settle in Marley Park and the grids off Bullard. The orders cover one car, and we move the other. Housing on the base is gated. The driver meets you outside the gate or at a lot on Bell. Ship Guy is a private broker with no link to the base. Give us the report date, and the window is built around it."),
 ("Does spring training affect my pickup?","Near the stadium, yes. The Royals and the Rangers play on Bell from February into March, and the lots fill by ten. Bell backs up from Bullard to Grand on a game day. We move a pickup near the stadium to the morning or to the 303 side. The rest of the city runs normally."),
 ("Can you ship a car to or from Sun City West, El Mirage, or Wickenburg?","Yes, and all three price the same as Surprise. Sun City West rides the same carriers off Grand, and the curb works on most streets. El Mirage rides them off Dysart and Grand. Wickenburg rides them off Grand on the way to Las Vegas, and the driver meets you in town. Send the full address for a new subdivision along the 303."),
 ("What happens if a haboob or a flash flood hits on my pickup day?","A dust storm closes Grand and the 303 for an hour, and the driver waits it out. A flash flood shuts the Agua Fria crossings and the washes west of Reems. The pickup waits for the next morning. From June through September the loading happens at dawn. We call before any of it changes your window."),
 ("Can you ship a car that does not run from Surprise?","Yes. A carrier with a winch is sent, and the loading time is in the quote from the start. The stadium lot on Bell or a shopping center by the 303 gives the driver level ground. Tell us whether the car rolls, steers, and brakes."),
 ("Do you ship cars for Canadians who winter in Surprise?","Yes, within the United States. Many Canadians keep a car in Sun City Grand or Sun City West year round. When they sell the house or move, the car ships to a US address or a dealer. We do not cross the border, and the <a href=\"/car-shipping-cost\">cost guide</a> covers the rest. Tell us where the car needs to land, and we price the lane."),
 ("What do you need for a Surprise car shipping quote?","Both addresses, with the side of Grand and any gate code here. Year, make, and model. Whether it runs. Open or enclosed. The week around the snowbird turnover or the report date. Those five answers are the whole request, and the Surprise number is back within the day."),
]
BODY.append(faq_section(FAQ,'Surprise FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Surprise?','The form above prices the lane in two minutes. Tell us the side of Grand and the week. The next carrier on the Las Vegas road takes it.','+19284595190','(928) 459-5190','Get your free Surprise quote'))

build({
 'slug':'auto-transport-surprise-arizona',
 'title':'Car Shipping in Surprise, AZ — Auto Transport | Ship Guy',
 'meta':'Car shipping in Surprise, AZ in the Northwest Valley, where Grand Avenue meets the 303 on the road to Las Vegas. Snowbird moves to Sun City Grand and Sun City West, Luke families, Marley Park curbside pickups, gated-section handoffs, spring training on Bell Road, the haboobs, and the heat. Local office on Bell Road by the stadium. Free quote.',
 'h1':'Car Shipping in<br>Surprise, <span class="accent">Arizona</span>',
 'lede':'Open, enclosed, and expedited auto transport across the Northwest Valley, planned around Grand, the 303, the snowbird tide, and the heat.',
 'tel':'+19284595190','disp':'(928) 459-5190','brand':'Surprise','keyword':'car shipping in surprise',
 'localterms':['surprise','northwest valley','grand avenue','us 60','wickenburg','las vegas','us 93','railroad','crossings','loop 303','goodyear','happy valley','loop 101','bell road','bridge','greenway','waddell','cactus','peoria','litchfield','dysart','bullard','reems','cotton','perryville','sun valley parkway','original townsite','sun city grand','sun city west','del webb','age-restricted','golf','golf carts','gated','arizona traditions','sun village','marley park','prasada','asante','white tanks','ranches','wittmann','el mirage','youngtown','luke','base','glendale','stadium','civic center','recreation campus','snowbirds','retirees','midwest','northwest','canada','canadians','airmen','orders','class cycles','hospital','nurses','school district','teachers','spring training','royals','rangers','transplants','california','closing date','fourth of july','festival','turnover','heat','one hundred ten','monsoon','haboob','dust storm','flash flood','agua fria','olive','northern','2014','phoenix','tucson','flagstaff','san diego','los angeles','salt lake city','denver','seattle','minneapolis','scottsdale'],
}, BODY, FAQ)
