import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('Fayetteville, North Carolina','Car shipping in the city beside the largest Army post in the country, on the busiest interstate on the coast',
 ['Car shipping in Fayetteville runs on Interstate 95 along the east side and through the Fort Bragg gates. Ship Guy is a licensed auto transport broker with an office on Hay Street downtown.',
  'We book vetted carriers across Fayetteville, from Haymount to Hope Mills and out to Spring Lake. The carriers own the trucks. Ship Guy holds the license and the bond.',
  'Interstate 95 runs along the east side with the 24, 53, and 301 exits. Interstate 295 is the new outer loop around the north and west. Bragg Boulevard and the All American Freeway run to the post. Raeford Road, Skibo Road, and Ramsey Street carry the rest of the city.',
  'This page covers 95, 295, Bragg Boulevard, Skibo, Raeford Road, downtown, Haymount, and the subdivisions. It also covers the post, the PCS season, the medical center, the universities, the river, and the hurricanes.'],
 'Fayetteville at a glance',
 ['Most pickups happen within 1 to 3 days. The 95 carriers pass between New York and Florida every hour. The Raleigh pool is an hour north. The post keeps a pool of its own.',
  'Raleigh, Wilmington, Charlotte, and Columbia ride a single day on the truck. Richmond takes a day. Washington, Atlanta, and Jacksonville take one to two, and New York and Orlando take two.'],
 'Tell us the neighborhood and whether the post is involved. Haymount, downtown, and the old mill villages meet the truck on a main road. The subdivisions off Cliffdale, Raeford Road, and Ramsey Street usually allow the curb.'))

BODY.append(sec('The Roads','Interstate 95, Interstate 295, Business 95, Bragg Boulevard, the All American Freeway, Raeford Road, Skibo Road, Ramsey Street, and the Gates',
 prose(
  L('Fayetteville is a city between an interstate and an Army post, and the post is bigger. A carrier picks its exit and never gets near a gate without a reason.'),
  P('Interstate 95 runs along the east side of the city, the New York-to-Florida road. More car haulers ride it than any road in the state. The 24, 53, and 301 exits serve the city. The 295 exit north of town serves the loop. Interstate 295 is the outer loop, around the north side past the post to Raeford Road. Business 95 is Eastern Boulevard, the old road through the east side. Highway 24 is Bragg Boulevard, the strip from downtown to the post. The All American Freeway runs from Owen Drive to the main gates.'),
  P('Raeford Road is 401, the long strip southwest to Hope Mills and Raeford. Skibo Road crosses it at the mall and carries every big-box store in the county. Ramsey Street is 401 north past the tire plant and the university to Spring Lake. Morganton Road and Cliffdale Road serve the west side subdivisions. Hay Street runs through downtown to the Market House. Person Street crosses the river east. The Cape Fear runs along the east edge and sets the flood line.'),
  P('The carriers come off 95 at 24 or 301 and off 295 at Raeford Road. The mall lots on Skibo are the usual meeting spot. The big-box lots on Raeford Road work too. So do the stadium lots downtown outside a game and the shopping center lots on Ramsey Street. The airport off 301 south works for a fly-and-ship.'),
  P('Our office is on Hay Street downtown, a block from the Market House.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','Downtown, Haymount, Massey Hill, Westover, Cliffdale, Jack Britt, Hope Mills, Bonnie Doone, Yadkin Road, Cottonade, Spring Lake, and the Post',
 prose(
  L('Fayetteville is an old town on the river and a hill of old money above it. The subdivisions spread west toward the post. The truck meets the old streets on a main road.'),
  P('Downtown runs along Hay Street from the river to Haymount. It is brick storefronts, the stadium, and the Market House in the middle of the road. The driver meets you at the stadium lots or on Person Street. Haymount on the hill west of downtown is the oldest neighborhood. It is big houses on narrow streets under old oaks. A trailer does not enter. The handoff moves to Bragg Boulevard or Raeford Road. Massey Hill south of downtown is the old mill village, small houses on short streets. The handoff moves to Southern Avenue.'),
  P('Westover and the blocks around the mall are postwar grids where the curb works. Cliffdale and the west side off Morganton Road are subdivisions from the seventies on, wide streets and cul-de-sacs. Jack Britt and the southwest off Raeford Road are the newest, and the streets outrun the maps. Send the full address. Hope Mills below them is a town of its own with the same streets. The truck reaches the curb.'),
  P('Bonnie Doone and the Yadkin Road blocks beside the post are where the soldiers live off post. They are apartments and small houses along the Korean restaurants. The handoff happens on Yadkin Road or at the gates. Cottonade and the north side off Ramsey Street are plain subdivisions, and the curb usually works. Spring Lake at the north end is the post’s town, and the gates there take the handoff too. On-post housing is behind the gates, and the truck meets you outside them.'),
  P('Spring Lake, Hope Mills, and Raeford ship with the same trucks and price the same as Fayetteville. So do Dunn and Lumberton up and down 95. Southern Pines and Pinehurst are forty miles west and add a few hours. Raleigh is an hour north and prices with the city.'),
 )))

ROUTES=[("Raleigh, NC","I-95/US-401 · ~65 mi","Same day","$140–$230"),("Wilmington, NC","NC-87/I-40 · ~95 mi","Same day","$150–$240"),
 ("Charlotte, NC","US-74/I-485 · ~135 mi","Same day","$190–$300"),("Columbia, SC","US-401/I-20 · ~150 mi","Same day","$200–$310"),
 ("Richmond, VA","I-95 · ~200 mi","Same day","$230–$350"),("Washington, DC","I-95 · ~310 mi","1 day","$280–$410"),
 ("Atlanta, GA","US-74/I-85 · ~390 mi","1 day","$320–$460"),("Jacksonville, FL","I-95 · ~400 mi","1 day","$340–$490"),
 ("Orlando, FL","I-95 · ~530 mi","1–2 days","$420–$600"),("New York, NY","I-95 · ~540 mi","1–2 days","$420–$600")]
BODY.append(rate_table('Lanes &amp; Costs','Fayetteville Car Shipping Lanes and Estimated Costs',
 'The lanes Cumberland County cars run most, with estimated open-trailer ranges. Price your own route on the form above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates from Fayetteville for a sedan that runs, open trailer. Plan on 10 to 25 percent more for an SUV or a pickup, and more again for enclosed. The week you offer and the carriers passing on 95 that week set the final figure.',
 prose(
  P('Fayetteville prices like a stop on the busiest car-hauling road in the country, which is what it is. The Florida and New York lanes ride 95 and fill in both directions every day. The Raleigh lane rides 95 and 401 and fills with the commuters. The Charlotte lane rides 74 west. The Texas and Washington lanes fill with orders in the summer. The price rises with the PCS season.'),
  P('A July report date at the post or the August move-in lands in the busiest weeks. The <a href="car-shipping-cost.html">cost guide</a> explains what size, condition, and timing do to the figure.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The Post, the Airfield, the Medical Center, the Veterans Hospital, the Universities, the Tire Plant, the Warehouses, and the Retirees',
 prose(
  L('Fayetteville relocates soldiers, airmen, nurses, professors, and veterans. The post moves more households than the rest of the county combined.'),
  P('Fort Bragg west of the city is the largest Army post in the country. It is home to the airborne corps and the special operations command. It deploys and returns whole divisions. Families rotate on orders every week of the year, with a summer peak. Post housing is gated, so the handoff happens outside the gate or at the mall. Orders cover one car, and the second one usually rides with us. The airfield beside the post rotates airmen the same way. Ship Guy is a private broker with no tie to the post. The <a href="military-car-shipping.html">military</a> page explains how orders set the timing.'),
  P('The medical center on Owen Drive is the largest employer in the county after the post. It brings residents each June and hires traveling nurses year round. The veterans hospital on Ramsey Street does the same, and half the city has a connection to it. The tire plant on Ramsey Street moves engineers between plants. The warehouses in Hope Mills and along 95 move managers on opening dates. If an employer reimburses the shipment, the paperwork comes from us.'),
  P('The state university on Murchison Road takes student cars in mid-August. The university on Ramsey Street and the community college follow in late August. A parent sets it up, and an adult signs at the handoff. The cars head home in May.'),
  P('Military retirees stay for the post, the hospital, and the commissary. The county has more of them than almost any in the country. Some leave for Florida each November and come back in April. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the paperwork for crossing a state line.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','The PCS Season, the Homecomings, All American Week, the Dogwood Festival, Move-In Week, the Fair, the Hurricanes, the River, the Ice, and the Tornadoes',
 prose(
  L('Fayetteville runs on an Army calendar. The weather problem is a river that rises for a week after a hurricane.'),
  P('The PCS season runs from May through August and fills every carrier on 95 with second cars. The homecomings at the airfield fill the post for a day at a time. The families book around them. All American Week fills the post in May. The dogwood festival closes downtown for a weekend in April. Move-in week in mid and late August fills the blocks around both campuses. The county fair fills the fairgrounds in September. Book three weeks ahead for a July date.'),
  P('The storms run June through November. Florence in 2018 is the benchmark. The Cape Fear crested above sixty feet and closed the Person Street bridge. The east side flooded for a week. Matthew in 2016 flooded the creeks across the city and closed 95 at Lumberton for days. A hurricane watch holds the truck in Raleigh until the all-clear. The river keeps the east side closed after the sky clears. We call the moment a watch goes up.'),
  P('Ice comes once or twice a winter. The February 2014 storm iced 95 for a day, and the carriers waited in Raleigh and Florence. The April 2011 tornado crossed Yadkin Road and the west side subdivisions and took roofs for miles. A tornado watch holds the truck at the truck stop until it lifts.'),
  P('Summer is hot and humid with a storm most afternoons, which only moves the loading hour. April pollen turns every car yellow for three weeks.'),
 )+chips(["Downtown","Hay Street","The Market House","Haymount","Massey Hill","Westover","Skibo Road","Cross Creek Mall","Cliffdale","Morganton Road","Jack Britt","Raeford Road","Hope Mills","Bonnie Doone","Yadkin Road","Bragg Boulevard","Cottonade","Ramsey Street","Spring Lake","Fort Bragg","Pope Field","Eastover","Gray's Creek","Raeford","Dunn","Lumberton","Southern Pines","Pinehurst","Sanford","Lillington"])
 +NOTE('Serving Fayetteville and the whole of Cumberland County, Haymount hill or Jack Britt cul-de-sac. Tell us the neighborhood and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in Fayetteville?',
 prose(
  L('Open trailers carry most of the Sandhills, and the table above is priced for one.'),
  P('Enclosed keeps the pollen, the post’s sand, and the pre-storm brine off the paint. Haymount collectors book it, and officers back from a tour overseas do too. Ahead of a hurricane, the car rides the first truck with room, and we are honest about that.'),
  P('Open is the right call for a commuter car or a student’s car. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages lay out the difference.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A figure, then a lot on Skibo Road, then a signature at the other end. Orders or the move-in date set the week.'),
  P('Approve the figure, and the car goes to a carrier already rolling down 95 that week. The lot and the window are agreed that afternoon. At pickup the driver shoots each panel and fills in the Bill of Lading. You initial it, and both ends work from that sheet.'),
 )+ULI([
  "Nothing personal left in the cabin or the trunk",
  "About a quarter tank of fuel",
  "Pictures of every side and the odometer before the truck arrives",
  "One working key and a note about anything that does not work",
  "Any aftermarket alarm disarmed",
  "In Haymount, downtown, or behind a gate, the handoff is on a main road",
 ])+prose(P('The steps are on <a href="how-it-works.html">how it works</a>, and the day-of list is on <a href="car-shipping-preparation.html">preparation</a>.'))))

BODY.append(sec('Why Ship Guy','Why Fayetteville Drivers Choose Ship Guy',
 prose(
  L('We book the carriers that already pass on 95 every hour. We know how orders set a week and which gate a driver can reach.'),
  P('Our FMCSA license and our $75,000 bond are a public record on the federal register. The office is on Hay Street downtown.'),
  P('The coordinator who picks up your first call stays on until the delivery call. The <a href="services.html">services</a> page compares open, enclosed, and expedited.'),
 )))

BODY.append(office('Fayetteville','109 Hay St #457','Fayetteville, NC 28301','+19109965586','(910) 996-5586','ET',
 '109+Hay+St+%23457,+Fayetteville,+NC+28301','Visit Us','Find Ship Guy in Fayetteville',
 'Our office is on Hay Street downtown, a block from the Market House.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4031.673668602404!2d-78.87897799999999!3d35.052588400000005!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89ab130a56a19565%3A0xba5e8d67752ce448!2sShip%20Guy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1793630977430!5m2!1sen!2sus', alt=True))

FAQ=[
 ("How much does it cost to ship a car from Fayetteville to Florida or New York?","Orlando runs four hundred twenty to six hundred dollars for a sedan. That is about five hundred thirty miles down 95. New York runs the same, about five hundred forty miles north. Raleigh is the lowest lane on the table, an hour up the interstate. SUVs and pickups run 10 to 25 percent more."),
 ("Do you ship cars for soldiers on orders to Fort Bragg?","Yes, fifty-two weeks a year. Orders pay for one car, and the family ships the second one with us. Post housing is gated, so the driver meets you outside the gate or at the mall on Skibo. The summer peak means a July date needs three weeks of notice. Ship Guy is a private broker, and the post is not involved in the booking."),
 ("Can you ship a car while a soldier is deployed?","Yes. A spouse or a parent books, and whoever holds the keys signs at the handoff. We need a copy of the registration and a note from the owner naming the signer. The homecoming date sets the delivery week, and we work around it."),
 ("Can the carrier come to my street in Haymount or downtown?","No. Haymount is narrow streets under old oaks on a hill. Downtown has the Market House in the middle of the road. The driver meets you on Bragg Boulevard, Raeford Road, or at the stadium lots. Westover, Cliffdale, Jack Britt, Hope Mills, and the subdivisions off Ramsey Street usually allow the curb."),
 ("Can you deliver on a Fayetteville State or Methodist move-in date?","Yes. The state university takes cars in mid-August, and the university on Ramsey Street follows in late August. Mom or Dad books, and an adult signs at the lot. The campus blocks are full those weeks, so the mall on Skibo is the meeting point. The date sets the window."),
 ("Do you ship cars for the medical center and the veterans hospital?","Yes, in every season. Both take residents in June and traveling nurses all year. The handoff is on Owen Drive or Ramsey Street. The tire plant moves engineers between plants the same way. If the employer pays you back, the paperwork comes from us."),
 ("Can you ship a car to or from Spring Lake, Hope Mills, or Southern Pines?","Yes. Spring Lake, Hope Mills, and Raeford ride the same carriers and price the same as Fayetteville. Dunn and Lumberton on 95 do too. Southern Pines and Pinehurst are forty miles west and add a few hours on the day."),
 ("What happens if a hurricane hits on my pickup day?","Under a watch the truck stays in Raleigh until the all-clear. The river keeps rising for days after the storm passes. The east side stays shut after the sky clears. We call as soon as the watch posts. The first clear day after the roads reopen is the new pickup day, and the figure stays put."),
 ("Can you ship a car that does not run from Fayetteville?","Yes. The carrier brings a winch, and the loading time is already in the figure. The mall lots on Skibo and the big-box lots on Raeford Road are flat. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a Fayetteville car shipping quote?","Where it starts and ends, with the neighborhood and the post if it is involved. What it is and whether it runs. Open or enclosed, and the week around the report date. With those, the Fayetteville figure is back the same day."),
]
BODY.append(faq_section(FAQ,'Fayetteville FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in Fayetteville?','Two minutes on the form above gets your lane a Fayetteville figure. Name the neighborhood and the week, and a carrier already passing on 95 takes it.','+19109965586','(910) 996-5586','Get your free Fayetteville quote'))

build({
 'slug':'auto-transport-fayetteville-north-carolina',
 'title':'Car Shipping in Fayetteville, NC — Auto Transport | Ship Guy',
 'meta':'Car shipping in Fayetteville, NC, beside Fort Bragg on Interstate 95. Army PCS moves outside the gates, deployment handoffs, medical center and campus relocations, main-road handoffs for Haymount and downtown, curbside pickups in Cliffdale, Jack Britt, and Hope Mills, the river after a hurricane, and the ice. Local office on Hay Street downtown. Free quote.',
 'h1':'Car Shipping in<br>Fayetteville, <span class="accent">North Carolina</span>',
 'lede':'Open, enclosed, and expedited auto transport across Fayetteville and Cumberland County, planned around 95, the post, the PCS season, the campus dates, and hurricane season.',
 'tel':'+19109965586','disp':'(910) 996-5586','brand':'Fayetteville','keyword':'car shipping in fayetteville',
 'localterms':['fayetteville','army post','interstate 95','295','outer loop','business 95','eastern boulevard','bragg boulevard','all american freeway','raeford road','skibo road','ramsey street','morganton road','cliffdale','hay street','person street','market house','cape fear','owen drive','yadkin road','downtown','haymount','massey hill','westover','jack britt','hope mills','bonnie doone','cottonade','spring lake','fort bragg','airfield','eastover','raeford','dunn','lumberton','southern pines','pinehurst','raleigh','wilmington','charlotte','columbia','richmond','washington','atlanta','jacksonville','orlando','new york','florida','texas','mall','stadium','airport','gates','soldiers','airmen','nurses','professors','veterans','airborne','special operations','divisions','orders','pcs season','medical center','residents','traveling nurses','veterans hospital','tire plant','warehouses','state university','murchison road','community college','student','retirees','commissary','homecomings','all american week','dogwood festival','move-in','county fair','fairgrounds','florence','2018','sixty feet','matthew','2016','creeks','february 2014','ice','april 2011','tornado','pollen','sand','brine','bill of lading','fmcsa','winch','oaks','mill village','southern avenue','korean restaurants','sandhills','deployed','registration','car haulers'],
}, BODY, FAQ)
