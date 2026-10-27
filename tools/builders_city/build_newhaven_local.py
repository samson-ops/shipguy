import sys; sys.path.insert(0,'/home/claude/tools')
from localpage import *

BODY=[]
BODY.append(stats([("50","States Served"),("100%","Insured Transport"),("1–3 Days","Typical Pickup"),("7 Days","Local Support")]))

BODY.append(intro_block('New Haven, Connecticut','Car shipping where Interstate 95 meets Interstate 91, on the university and hospital calendar',
 ['Car shipping in New Haven runs on two calendars, the university’s and the hospital’s, and two interstates. Ship Guy is a licensed auto transport broker with an office on Church Street facing the Green.',
  'We book vetted carriers across greater New Haven, from Hamden and West Haven to Branford and Milford. We do not own the trucks.',
  'Interstate 95 crosses the harbor on the Pearl Harbor Memorial Bridge and meets Interstate 91 by the water. Interstate 91 runs north through the city to Hartford. The Wilbur Cross Parkway bans commercial vehicles, so the carriers stay on 95, 91, and Route 1.',
  'This page covers the two interstates and the parkway, the Green and the neighborhoods, and the suburbs. It also covers the university, the hospital, the biotech labs, the port, the storms, and the lanes.'],
 'New Haven at a glance',
 ['Most pickups happen within 1 to 3 days. Two interstates bring carriers through the city from three directions all day.',
  'Hartford, Bridgeport, and Providence are same-day lanes. Manhattan and Boston are the same day too. Philadelphia and Albany take a day. Florida runs three.'],
 'Tell us the neighborhood. The Green, East Rock, Wooster Square, and the Hill need a meeting spot. Hamden, Westville, and the suburban grids often allow the curb.'))

BODY.append(sec('The Roads','Interstate 95, 91, Route 34, the Parkway, and the Harbor Bridge',
 prose(
  L('New Haven is the one shoreline city where a second interstate turns north. The carriers use both.'),
  P('Interstate 95 runs along the harbor and crosses it on the Pearl Harbor Memorial Bridge. Interstate 91 leaves 95 at the harbor and runs north through the city to Hartford and Springfield. The interchange between them is the busiest in the state, and it backs up in both rushes.'),
  P('Route 34 leaves the interchange for downtown and the hospital. The Wilbur Cross Parkway crosses the north of the city through the tunnel under West Rock. It bans commercial vehicles. A carrier uses Route 1, Whalley Avenue, or Dixwell Avenue instead.'),
  P('The carriers come off 95 at Long Wharf and Sargent Drive. On 91 they use Trumbull Street and State Street. The lots along Long Wharf, Sargent Drive, and Route 1 are the usual meeting spots. Union Station has a garage that works for an arriving student.'),
  P('Our office sits on Church Street facing the Green, a block from the courthouse.'),
 ), alt=True))

BODY.append(sec('The Neighborhoods','The Green, East Rock, Wooster Square, the Hill, Westville, and the Suburbs',
 prose(
  L('New Haven was laid out in nine squares before the automobile. The squares still decide where a truck can stop.'),
  P('Downtown and the Green sit inside the nine squares, with one-way streets and bus lanes. The university wraps three sides. East Rock and Wooster Square have narrow streets with cars on both curbs. The driver meets you on State Street, on Whalley Avenue, or at Long Wharf.'),
  P('The Hill holds the hospital and the medical school. Its streets are tight and often blocked by construction. Fair Haven and Newhallville are grids of three-family houses with alleys. A main road nearby is the usual spot.'),
  P('Westville, Beaver Hills, and Prospect Hill have wider streets under big trees. The truck often reaches the curb. Morris Cove sits by the airport and the water, and it floods in a storm. The driver meets you on Townsend Avenue or at the lot by the beach.'),
  P('Hamden, North Haven, West Haven, and Milford are suburban grids where the curb usually works. Branford and Guilford have narrow shoreline lanes, and the handoff happens on Route 1. The warehouses along 91 in North Haven have truck entrances of their own.'),
 )))

ROUTES=[("Hartford, CT","I-91 · ~40 mi","Same day","$120–$200"),("Bridgeport, CT","I-95 · ~20 mi","Same day","$100–$170"),
 ("Providence, RI","I-95 · ~100 mi","Same day","$180–$290"),("Manhattan, NY","I-95 · ~80 mi","Same day","$170–$280"),
 ("Boston, MA","I-91/I-90 · ~140 mi","Same day","$210–$330"),("Philadelphia, PA","I-95 · ~170 mi","1 day","$220–$340"),
 ("Washington, DC","I-95 · ~300 mi","1 day","$280–$410"),("Charlotte, NC","I-95/I-85 · ~700 mi","2 days","$510–$730"),
 ("Orlando, FL","I-95 · ~1,160 mi","3 days","$790–$1,110"),("Miami, FL","I-95 · ~1,350 mi","3–4 days","$830–$1,180")]
BODY.append(rate_table('Lanes &amp; Costs','New Haven Car Shipping Lanes and Estimated Costs',
 'The lanes New Haven students, residents, and families price most, with estimated open-trailer ranges. Price your exact route above.',
 ['Route','Corridor · distance','Est. transit','Est. open rate*'],ROUTES,
 '*2026 estimates for a sedan that runs, open trailer. SUVs and pickups add 10 to 25 percent or so, and enclosed adds more. Move-in season, the storms, and the carriers free on your dates decide the final number.',
 prose(
  P('New Haven prices a little under the Gold Coast. Two interstates bring trucks through it instead of one. Hartford and Boston ride 91 north, and Manhattan and Philadelphia ride 95 south.'),
  P('The lanes to Boston, Washington, and the Bay Area fill each June and August with residents and students. The <a href="car-shipping-cost.html">cost guide</a> lays out how the number is built.'),
 ), alt=True))

BODY.append(sec('Who Moves Here','The University, the Hospital, the Labs, and the Port',
 prose(
  L('New Haven relocates people on the semester, the residency match, the grant cycle, and the Florida season.'),
  P('The university brings cars in each late August and sends them home each May. The graduate schools run on their own calendars. The streets around the colleges are closed or tight on move-in day. The driver meets you at Long Wharf, on State Street, or at the Union Station garage. An adult signs for a student car.'),
  P('The hospital is the largest in the state, and it brings in residents and fellows every late June. Most arrive from out of state with a car. Sargent Drive or Long Wharf is the handoff, never the hospital garage.'),
  P('The biotech labs downtown and in Science Park hire scientists from every state. They arrive on grant cycles and start dates. The port and the warehouses along 91 in North Haven hire on start dates all year. We supply the records an employer needs to reimburse the move.'),
  P('The two universities in Hamden and West Haven add their own move-in weeks each August. The veterans hospital in West Haven brings in staff on start dates. Retirees along the shoreline leave for Florida each fall, and our <a href="snowbird-car-shipping.html">snowbird</a> page covers the timing.'),
  P('The Coast Guard academy sits an hour east in New London. The submarine base sits across the river from it. The <a href="military-car-shipping.html">military</a> page covers a PCS move. The <a href="state-to-state-car-shipping.html">state-to-state</a> page covers the interstate side.'),
 ), alt=True))

BODY.append(sec('The Calendar &amp; the Weather','Move-In, Commencement, Nor’easters, and the Long Wharf Tide',
 prose(
  L('New Haven closes its streets for students twice a year. It loses Long Wharf to the tide a few times more.'),
  P('Move-in in late August and commencement in May fill downtown and close the streets around the colleges. Hotel and garage traffic backs up to 95. We move a downtown pickup to another day for both. A lot at Long Wharf works the rest of the week.'),
  P('Nor’easters close 95 and 91 for a morning a few times each winter. The carriers wait for the plows. A storm surge floods Long Wharf and Morris Cove. Interstate 95 itself has gone under at Long Wharf. A pickup there waits for the tide to fall.'),
  P('The arts festival fills the Green for two weeks each June. The cherry blossom festival fills Wooster Square for a weekend in April. The St. Patrick’s parade closes downtown in March. We schedule around all three.'),
  P('Interstate 95 and the 91 interchange back up from six to ten and from three to seven. A New Haven pickup happens between the rushes. Summer heat moves the loading hour earlier.'),
 )+chips(["Downtown","The Green","East Rock","Wooster Square","The Hill","Dwight","Fair Haven","Newhallville","Dixwell","Westville","Beaver Hills","Prospect Hill","Morris Cove","Long Wharf","Sargent Drive","Whalley Avenue","Hamden","North Haven","West Haven","East Haven","Branford","Guilford","Milford","Orange","Woodbridge"])
 +NOTE('Serving New Haven and the whole shoreline county. Tell us the neighborhood, the week, and whether the car runs.')))

BODY.append(sec('Your Options','Open or Enclosed in New Haven?',
 prose(
  L('Open trailers carry most of what leaves New Haven. The student and resident lanes are priced for them.'),
  P('An enclosed trailer keeps the salt, the grime, and attention off the car. The garages in Prospect Hill, Woodbridge, and Guilford book enclosed trailers. So does a collector car headed to Florida for the winter.'),
  P('A student car or a resident’s car rides open without trouble. The <a href="open-car-transport.html">open</a> and <a href="enclosed-auto-transport.html">enclosed</a> pages explain what the roof is for.'),
 ), alt=True))

BODY.append(sec('The Basics','How It Works and How to Prepare',
 prose(
  L('A price, a handoff at Long Wharf or on a wide avenue, and a delivery. The semester decides the week.'),
  P('Accept the price, and a carrier already running 95 or 91 takes the booking. We set the spot the same day. The driver and you walk the car together and note its condition on a Bill of Lading. You both sign, and delivery is inspected against it.'),
 )+ULI([
  "Empty the car of personal belongings",
  "Fuel to about a quarter tank",
  "Photograph the car before pickup, especially after a salt storm",
  "Hand over a working key and flag anything mechanical",
  "Turn the aftermarket alarm off if there is one",
  "On move-in day, plan to meet the truck at Long Wharf rather than near the colleges",
 ])+prose(P('The <a href="how-it-works.html">how it works</a> and <a href="car-shipping-preparation.html">preparation</a> pages have the rest in order.'))))

BODY.append(sec('Why Ship Guy','Why New Haven Drivers Choose Ship Guy',
 prose(
  L('We work 95 and 91 every day and plan around the semester, the tide, and the storms.'),
  P('Ship Guy is an active, FMCSA-licensed broker with a $75,000 surety bond on file. Both are public record. Our office is on Church Street facing the Green.'),
  P('Your coordinator stays the same from the first call to the delivery signature. Open, enclosed, and expedited transport are all on the table, and the <a href="services.html">services</a> page covers each one.'),
 ), alt=True))

BODY.append(office('New Haven','157 Church St #558','New Haven, CT 06510','+14752705918','(475) 270-5918','ET',
 '157+Church+St+%23558,+New+Haven,+CT+06510','Visit Us','Find Ship Guy in New Haven',
 'Our office is on Church Street facing the Green, a block from the courthouse.',
 map_src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4608.798406288398!2d-72.9248612!3d41.307018299999996!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89e7d9e1966b0631%3A0x80e35577a2881e21!2sShipGuy%20Auto%20Transports!5e1!3m2!1sen!2sus!4v1792153220906!5m2!1sen!2sus'))

FAQ=[
 ("Can you ship a car for a Yale student?","Yes, every August and May. The streets around the colleges are closed or tight on move-in day. The driver meets you at Long Wharf, on State Street, or at the Union Station garage. An adult signs for the car at pickup, and a parent can sign at the far end. Two to three weeks of notice keeps the price steady in late August."),
 ("How much does it cost to ship a car from New Haven to Boston or Florida?","Boston runs two hundred ten to three hundred thirty dollars for a sedan. That is about one hundred forty miles up 91 and the Pike. Orlando runs seven hundred ninety to eleven hundred ten, about eleven hundred sixty miles down 95. Fall southbound costs more than spring. SUVs and pickups add 10 to 25 percent."),
 ("Do you ship cars for residents at Yale New Haven Hospital?","Yes, every late June. Residents and fellows arrive from every state, and most bring a car. The handoff happens on Sargent Drive or at Long Wharf, not in the hospital garage. We plan the pickup around the report date."),
 ("Can the carrier come into East Rock, Wooster Square, or the Hill?","Usually not. The streets are narrow and parked on both curbs. The Hill has construction most of the year. The driver meets you on State Street, on Whalley Avenue, or at Long Wharf. Westville, Hamden, and the suburbs often allow the curb."),
 ("What happens if a nor’easter or a storm surge hits on my pickup day?","The carriers wait for the plows on 95 and 91. Long Wharf and Morris Cove wait for the tide to fall. The highway itself has flooded at Long Wharf. A winter pickup can lose a day, and we call ahead."),
 ("Is New Haven priced like Hartford or like the Gold Coast?","A little under both. Two interstates bring trucks through the city, and the student and resident lanes keep them full. Hartford runs one hundred twenty to two hundred dollars for a sedan. Bridgeport runs one hundred to one hundred seventy."),
 ("Do you handle relocations to the biotech labs or the warehouses?","Yes, on start dates all year. The labs downtown and in Science Park hire scientists from every state. The warehouses along 91 in North Haven hire managers the same way. Many employers allow a handoff in the lot. We provide the records for a reimbursed move."),
 ("Can you ship a car for a Quinnipiac or University of New Haven student?","Yes. The cars come in each August and leave each May. The campus lots in Hamden and West Haven work for the handoff, and Whalley Avenue is the backup. An adult signs for the car at pickup."),
 ("Can you ship a car that does not run from New Haven?","Yes. A winch truck handles it, and the longer loading is built into the price. The spot has to be flat and open, which usually means Long Wharf. Tell us whether it rolls, steers, and brakes."),
 ("What do you need for a New Haven car shipping quote?","Both addresses, with the neighborhood on this end. The year, make, and model, and whether it runs and rolls. Open or enclosed. Your dates, with move-in week or the report date in mind. That is everything a New Haven quote needs."),
]
BODY.append(faq_section(FAQ,'New Haven FAQ','Frequently Asked Questions'))
BODY.append(cta('Ready to book car shipping in New Haven?','About two minutes on the form above gets you a price. Tell us the neighborhood and your dates. A carrier already on 95 or 91 takes it from there.','+14752705918','(475) 270-5918','Get your free New Haven quote'))

build({
 'slug':'auto-transport-new-haven-connecticut',
 'title':'Car Shipping in New Haven, CT — Auto Transport | Ship Guy',
 'meta':'Car shipping in New Haven, CT where Interstate 95 meets 91. Yale move-in and commencement timing, hospital residents, Long Wharf and State Street meeting spots, East Rock and Wooster Square blocks, biotech and warehouse relocations, nor’easter and Long Wharf tide planning. Local office on Church Street at the Green. Free quote.',
 'h1':'Car Shipping in<br>New Haven, <span class="accent">Connecticut</span>',
 'lede':'Open, enclosed, and expedited auto transport across greater New Haven, planned around the two interstates, the semester, and the tide.',
 'tel':'+14752705918','disp':'(475) 270-5918','brand':'New Haven','keyword':'car shipping in new haven',
 'localterms':['new haven','interstate 95','interstate 91','route 34','wilbur cross','parkway','west rock','pearl harbor memorial bridge','harbor','long wharf','sargent drive','state street','trumbull street','whalley avenue','dixwell avenue','townsend avenue','route 1','union station','church street','the green','nine squares','downtown','east rock','wooster square','the hill','dwight','fair haven','newhallville','westville','beaver hills','prospect hill','morris cove','airport','hamden','north haven','west haven','east haven','branford','guilford','milford','orange','woodbridge','university','colleges','graduate schools','move-in','commencement','hospital','residents','fellows','medical school','biotech','science park','port','warehouses','veterans hospital','coast guard','submarine base','new london','snowbird','nor’easters','storm surge','tide','arts festival','cherry blossom','parade','hartford','bridgeport','providence','manhattan','boston','philadelphia','washington','charlotte','orlando','miami','albany'],
}, BODY, FAQ)
