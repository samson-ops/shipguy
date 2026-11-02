import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("2–4 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Santa Fe, New Mexico','Car shipping at seven thousand feet, in a capital laid out four centuries before the first truck',
 ['Car shipping in Santa Fe rides Interstate 25 and the Albuquerque carrier pool an hour down the hill. Ship Guy is a licensed auto transport broker with an office on East Palace Avenue by the Plaza.',
  'We book vetted carriers across Santa Fe and the north, from Canyon Road to Eldorado and Los Alamos. The carriers own the trucks. Ship Guy holds the license and the bond.',
  'Interstate 25 runs along the south edge of the city. It drops down La Bajada to Albuquerque and climbs northeast to Las Vegas, Raton, and Denver. US 84 and 285 cross the city as St. Francis Drive and leave north for Española and Taos. Cerrillos Road is the commercial strip, and Highway 599 loops the west side.',
  'This page covers 25, La Bajada, St. Francis, Cerrillos, the Plaza, the East Side, and the villages. It also covers the state, the lab, the hospitals, the opera, the markets, the snow, and the monsoon.'],
 'Santa Fe at a glance',
 ['Most pickups happen within 2 to 4 days. The carriers base in Albuquerque and come up 25 when a Santa Fe stop lines up. A few days of flexibility keeps the price down.',
  'Albuquerque and Las Cruces are same-day runs. El Paso, Colorado Springs, Denver, and Amarillo need a day. Phoenix and Oklahoma City need one to two, and Dallas and Los Angeles need two.'],
 'Tell us the neighborhood and whether the street is paved. The Plaza, the East Side, Canyon Road, and Tesuque meet the truck at a lot. Casa Solana, the Southside, Rancho Viejo, Eldorado, and Los Alamos usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 25, La Bajada, St. Francis Drive, Cerrillos Road, St. Michael’s, Old Pecos Trail, Highway 599, and Paseo de Peralta',
 prose(
  L('Santa Fe sits on a hill above the interstate. Every carrier arrives from the south and climbs to reach it.'),
  P('Interstate 25 is the Denver-to-El Paso road. From Albuquerque it climbs La Bajada, a long grade that ices in January. It passes the city on the south. It leaves northeast past Glorieta for Las Vegas and Raton Pass at the Colorado line. Both grades close in a storm, and a carrier waits them out. The exits that matter are Cerrillos Road, St. Francis Drive, and Old Pecos Trail.'),
  P('US 84 and 285 cross the city as St. Francis Drive, the one in-town road built for trucks. They leave north for Pojoaque, Española, the lab turnoff, and Taos. Cerrillos Road runs from downtown southwest to the interstate, five miles of shopping centers and hotels. St. Michael’s Drive crosses the middle. Paseo de Peralta loops the old city, and Highway 599 loops the new one on the west.'),
  P('The carriers come off 25 at Cerrillos Road. The mall lots at Cerrillos and Rodeo are the usual meeting spot. The outlet lots by the interstate and the big-box lots on Cerrillos work too. So do the Railyard lots at the edge of downtown. The community center lots on Rodeo Road work on a weekday.'),
  P('Our office is on East Palace Avenue, a block east of the Plaza.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','The Plaza, the East Side, Canyon Road, the South Capitol, Casa Solana, the Northwest, the Southside, Eldorado, Tesuque, and the Villages',
 prose(
  L('Santa Fe is adobe walls on lanes built for burros, with new subdivisions on the flats below. The truck meets the old city at the edge.'),
  P('The Plaza and the blocks around it are the oldest streets in the country still in use. They are narrow, one-way, and walled on both sides. A trailer does not enter. The driver meets you at the Railyard lots or on Paseo de Peralta. The East Side along Canyon Road and Acequia Madre is tighter still, galleries and houses behind adobe walls. The handoff moves to the same lots.'),
  P('The South Capitol around Don Gaspar is older houses on short blocks. The driver meets you on St. Francis. Casa Solana and Casa Alegre to the northwest are the postwar grids, wide enough for the curb. The Northwest beyond them is Tano Road and Las Campanas, ranchettes on dirt roads behind gates. The handoff moves to the pavement or to the 599 interchange. Tesuque in the valley to the north is narrow lanes along the creek. The truck waits on the highway.'),
  P('The Southside along Airport Road is where the city grew. Tierra Contenta, Rancho Viejo, and the subdivisions off Rodeo Road are wide and new, and the curb works. Agua Fria village between them keeps its old lanes. Eldorado fifteen miles southeast is cul-de-sacs on dirt roads under a homeowners association. The handoff is at the shopping center. Pecos and Glorieta over the pass meet the truck at the highway.'),
  P('Los Alamos on the hill, Española, and the pueblos along 285 ship with the same trucks. So do Cerrillos and Madrid down Highway 14 and Lamy at the train station. All of them price a shade above Santa Fe for the extra miles. Albuquerque prices a shade below it.'),
 )))

ROUTES=[("Albuquerque, NM","I-25 · ~60 mi","Same day","$150–$240"),("Las Cruces, NM","I-25 · ~285 mi","Same day","$260–$390"),
 ("Colorado Springs, CO","I-25 · ~320 mi","1 day","$280–$410"),("El Paso, TX","I-25/I-10 · ~325 mi","1 day","$280–$410"),
 ("Amarillo, TX","I-25/I-40 · ~350 mi","1 day","$300–$440"),("Denver, CO","I-25 · ~390 mi","1 day","$340–$490"),
 ("Phoenix, AZ","I-25/I-40/I-17 · ~480 mi","1–2 days","$400–$570"),("Oklahoma City, OK","I-25/I-40 · ~600 mi","1–2 days","$460–$660"),
 ("Dallas, TX","I-25/I-40/US-287 · ~700 mi","2 days","$500–$730"),("Los Angeles, CA","I-25/I-40 · ~860 mi","2 days","$600–$860")]
BODY.append(rate_table('Lanes &amp; Costs','Santa Fe Car Shipping Lanes and Estimated Costs',
 'The lanes northern New Mexico cars run most, with estimated open-trailer ranges. Price your own route on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Santa Fe for a running sedan on an open trailer. An SUV or a pickup adds roughly 10 to 25 percent, and enclosed adds more. The season, the grade, and the trucks free on your dates decide the real quote.',
 prose(
  P('Santa Fe prices a shade above Albuquerque on every lane. The carriers climb an hour to reach it. The Denver lane rides 25 north over Raton Pass. The Phoenix and Los Angeles lanes drop to Albuquerque and ride 40 west. The Texas lanes ride 40 east through Amarillo. The Colorado lanes fill each winter with the ski crowd, and the Arizona lane fills each October.'),
  P('A legislative start in January or the opera season in July lands in a busy week. The <a href="car-shipping-cost.html">cost guide</a> explains how size, condition, and timing shape the number.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The State, the Lab, the Hospitals, the Opera, the Galleries, the Colleges, and the Retirees',
 prose(
  L('Santa Fe relocates legislators, physicists, nurses, singers, and retirees. The state and the lab move the most.'),
  P('State government fills the Roundhouse and the office blocks around it. The agencies transfer staff on start dates all year, and the session brings a crowd each January. Every fourth January a new governor arrives with a class of appointees. When the state or an employer reimburses the move, the receipts come from us.'),
  P('The lab in Los Alamos hires physicists and engineers from across the country on project dates. Many of them live in Santa Fe and commute up 502. The lab relocates them with a package that usually covers one car. The second one rides a trailer with us. The hospital on St. Michael’s and the medical center on the Southside hire traveling nurses year round. Residents arrive each June.'),
  P('The opera brings singers, musicians, and crews in each June for a season that ends in August. The galleries move dealers and artists in on their own calendars. The college on Camino de Cruz Blanca takes student cars each September. The community college on the Southside and the arts institute do the same in August. A parent books from home, and an adult meets the truck at a lot to sign.'),
  P('Retirees arrive from Texas, California, and the East every month for the light and the altitude. They ship the car ahead of the moving truck. The base in Albuquerque sends airmen north on orders. Ship Guy is a private broker with no connection to it. The <a href="military-car-shipping.html">military</a> page covers the timing around orders, and the <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate paperwork.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Indian Market, Spanish Market, Fiesta, the Opera, the Session, the Snow, the Spring Wind, the Monsoon, and the Fires',
 prose(
  L('Santa Fe runs on a market calendar and an altitude calendar. The weather problem changes with the season.'),
  P('Indian Market closes the Plaza and the streets around it for the third weekend of August. A hundred thousand people come, and every hotel is full. Spanish Market does the same for the last weekend of July. Fiesta fills downtown in early September. The burning at Fort Marcy Park closes the north side for a night. The folk art market fills Museum Hill in July. A handoff near any of them moves to the week after.'),
  P('The opera season runs from late June to late August and fills the hotels on weekends. The legislative session fills the Roundhouse district from January into March. The farolito walk closes Canyon Road on Christmas Eve. The balloon fiesta in Albuquerque fills Santa Fe’s hotels for nine days in October. The 25 traffic doubles.'),
  P('Winter at seven thousand feet brings real snow from November through March. La Bajada ices, and Raton Pass closes for a day at a time. The carriers wait in Albuquerque until the grade is sanded. The city plows the main roads and leaves the lanes. A winter pickup can lose a day, and you hear it from us before the driver does. Spring brings the wind, dust across 25 from March into May.'),
  P('The monsoon arrives in July. Afternoon storms drop an inch in an hour, and the arroyos run across Cerrillos Road and Airport Road. The driver loads in the morning and watches the sky after noon. The fires come in June. In 2022 the Hermits Peak fire burned east of town for two months. The smoke sat on the city for weeks. A pickup in the smoke still happens, and a pickup in an evacuation zone waits.'),
 )+chips(["The Plaza","Downtown","Railyard","East Side","Canyon Road","Acequia Madre","South Capitol","Don Gaspar","Casa Solana","Casa Alegre","Bellamah","Tano Road","Las Campanas","Tesuque","Southside","Airport Road","Tierra Contenta","Rancho Viejo","Agua Fria","Eldorado","Glorieta","Pecos","Lamy","Cerrillos","Madrid","Pojoaque","Española","Los Alamos","White Rock","Taos"])
 +NOTE('Serving Santa Fe and the whole north, East Side lane or Rancho Viejo cul-de-sac. Tell us the neighborhood and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Santa Fe?',
 prose(
  L('Open trailers carry most of Santa Fe, and the table above is priced for one.'),
  P('An enclosed trailer keeps off the dust, the cinders on the grade, and the high-altitude sun. The collectors on the East Side and in Las Campanas book one. So do the retirees bringing a new car in from Texas or California. A car headed over Raton Pass in January often rides enclosed too.'),
  P('A commuter car or a student car is an open-trailer car. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages set the two side by side.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A number, a lot on Cerrillos Road, and a signature at delivery. The session or the market picks the week.'),
  P('Approve the price, and a carrier coming up from Albuquerque that week takes the car. The lot and the window are confirmed as soon as it commits. At pickup the driver walks the car with you and lists its condition on the Bill of Lading. You initial the sheet, and delivery is held to it.'),
 )+ULI([
  "Everything personal out of the car, trunk included",
  "Fuel near a quarter tank",
  "Your own photos of each side and the odometer that morning",
  "A working key, and a note about anything that sticks or leaks",
  "Any add-on alarm switched off",
  "At the Plaza, on the East Side, in Tesuque, or on a dirt road, plan on a lot",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> page covers the sequence, and the <a href="car-shipping-preparation.html">preparation</a> page covers the checklist.'))))

BODY.append(sec('Why Ship Guy','Why Santa Fe Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already come up 25 from Albuquerque. We know which lanes a trailer cannot enter.'),
  P('Our FMCSA license and our $75,000 bond are on the federal register for anyone to check. The office is on East Palace Avenue.'),
  P('One coordinator handles the move from the quote to the delivery photo. The <a href="services.html">services</a> page compares open, enclosed, and expedited.'),
 )))

BODY.append(office('Santa Fe','141 E Palace Ave #445','Santa Fe, NM 87501','+15054878959','(505) 487-8959','MT',
 '141+E+Palace+Ave+%23445,+Santa+Fe,+NM+87501','Visit Us','Find Ship Guy in Santa Fe',
 'Our office is on East Palace Avenue, a block east of the Plaza.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4949.466074056562!2d-105.9357945!3d35.6875605!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x871851dbd6d23d21%3A0x4b9c94b5e6bb5d2f!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793300315625!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Santa Fe to Denver or Phoenix?","Denver runs three hundred forty to four hundred ninety dollars for a sedan. That is about three hundred ninety miles up 25. Phoenix runs four hundred to five hundred seventy, about four hundred eighty miles out 40 and 17. Albuquerque is an hour away and costs the least. An SUV or a pickup adds roughly 10 to 25 percent."),
 ("Why does a Santa Fe pickup take 2 to 4 days?","Because the carriers base in Albuquerque and climb an hour to reach the city. One comes up 25 when a Santa Fe stop lines up with the rest of the load. A few days of flexibility gets the next truck. A single fixed date can wait for one."),
 ("Can the carrier come to my street near the Plaza or on Canyon Road?","No. The streets downtown and on the East Side are narrow, one-way, and walled. A trailer cannot enter them. The driver meets you at the Railyard lots or on Paseo de Peralta. Casa Solana, the Southside, Rancho Viejo, and Eldorado usually allow the curb."),
 ("Do you ship cars for the lab and the state?","Yes, every week. The lab hires physicists and engineers on project dates, and many of them live in Santa Fe. The package usually covers one car, and the second one rides a trailer with us. The agencies transfer staff all year, and a new governor brings an appointee class every fourth January. The receipts for a reimbursed move come from us."),
 ("Can you deliver on a St. John’s or Santa Fe Community College move-in date?","Yes. The college on the hill takes cars each September. The community college and the arts institute take them in August. A parent books from home, and an adult meets the truck at a lot to sign. The window follows the date."),
 ("Can you ship a car to or from Los Alamos, Española, or Eldorado?","Yes. Los Alamos is forty minutes up 502, and the handoff happens in town rather than past the gate. Española rides the same carriers off 285. Eldorado is dirt roads and cul-de-sacs, and the truck meets you at the shopping center. All three price a shade above Santa Fe."),
 ("What happens if La Bajada or Raton Pass closes on my pickup day?","The carrier waits in Albuquerque or Trinidad until the grade is sanded. A closure usually lasts hours, and the truck arrives a day late. We tell you before the driver does. A Denver car can also ride 40 to Amarillo and 287 north when Raton stays shut."),
 ("Does Indian Market or Fiesta affect my pickup?","Yes, downtown. Indian Market closes the Plaza for the third weekend of August, and Fiesta fills it in early September. The burning at Fort Marcy closes the north side for a night. A handoff anywhere inside Paseo de Peralta moves to the week after. The Southside runs normally."),
 ("Can you ship a car that does not run from Santa Fe?","Yes. We book a carrier with a winch, and the loading time is in the quote from the start. The mall lots at Cerrillos and Rodeo give the driver level ground. Let us know whether it rolls, steers, and brakes."),
 ("What do you need for a Santa Fe car shipping quote?","Pickup and delivery, with the neighborhood or the village and whether the road is paved. The year, make, and model. Whether it runs. Open or enclosed. The week you have in mind. Five answers, and a Santa Fe number is back the same day."),
]
BODY.append(faq_section(FAQ,'Santa Fe FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Santa Fe?','The form above takes two minutes and comes back with a Santa Fe number. Name the neighborhood and the week, and a carrier coming up 25 takes it.','+15054878959','(505) 487-8959','Get your free Santa Fe quote'))

build({
 'slug':'auto-transport-santa-fe-new-mexico',
 'title':'Car Shipping in Santa Fe, NM — Auto Transport | Ship Guy',
 'meta':'Car shipping in Santa Fe, NM, the capital at seven thousand feet an hour up Interstate 25 from Albuquerque. State and lab relocations, the opera and market calendars, lot handoffs for the Plaza, the East Side, and Canyon Road, curbside pickups in Casa Solana, the Southside, Rancho Viejo, and Eldorado, La Bajada and Raton Pass, the monsoon, and the fires. Local office on East Palace Avenue by the Plaza. Free quote.',
 'h1':'Car Shipping in<br>Santa Fe, <span class="accent">New Mexico</span>',
 'lede':'Open, enclosed, and expedited auto transport across Santa Fe and the north, planned around 25, La Bajada, the Albuquerque carrier pool, the market weekends, and the snow at seven thousand feet.',
 'tel':'+15054878959','disp':'(505) 487-8959','brand':'Santa Fe','keyword':'car shipping in santa fe',
 'localterms':['santa fe','seven thousand feet','capital','interstate 25','albuquerque','east palace avenue','plaza','east side','eldorado','los alamos','la bajada','las vegas','raton','denver','us 84','285','st. francis drive','española','taos','cerrillos road','highway 599','southside','villages','state','lab','hospitals','opera','markets','snow','monsoon','las cruces','el paso','colorado springs','amarillo','phoenix','oklahoma city','dallas','los angeles','paved','canyon road','tesuque','casa solana','rancho viejo','glorieta','raton pass','old pecos trail','pojoaque','shopping centers','hotels','st. michael','paseo de peralta','mall','rodeo','outlet','big-box','railyard','community center','adobe','burros','one-way','walled','galleries','acequia madre','south capitol','don gaspar','casa alegre','tano road','las campanas','ranchettes','dirt roads','gates','creek','airport road','tierra contenta','agua fria','homeowners association','pecos','pueblos','cerrillos','madrid','lamy','train station','ski','roundhouse','session','appointee','physicists','engineers','502','traveling nurses','residents','singers','crews','dealers','artists','camino de cruz blanca','arts institute','retirees','texas','california','light','altitude','base','airmen','indian market','spanish market','fiesta','fort marcy','folk art market','museum hill','farolito','balloon fiesta','sanded','plows','wind','dust','arroyos','inch in an hour','fires','2022','hermits peak','smoke','evacuation','cinders','bill of lading','fmcsa','trinidad','287','bellamah','white rock','winch'],
}, BODY, FAQ)
