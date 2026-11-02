"""Batch 46 long-sentence splits (>18 words), applied to the builders."""
D='/home/claude/tools/builders_city/'
def fix(fn, pairs):
    p=D+fn; s=open(p,encoding='utf-8').read()
    if pairs and all(s.count(o[0])==0 for o in pairs): print(fn,'already applied'); return
    for item in pairs:
        old,new=item[0],item[1]; k=item[2] if len(item)>2 else 1
        c=s.count(old); assert c==k, (fn, c, old[:70])
        s=s.replace(old,new)
    open(p,'w',encoding='utf-8').write(s); print(fn, len(pairs), 'fixes')

fix('build_siouxfalls_local.py', [
('Car shipping in Sioux Falls rides Interstate 29 and Interstate 90, the two roads that cross at the northwest corner of the city.','Car shipping in Sioux Falls rides Interstate 29 and Interstate 90, which cross at the northwest corner of the city.'),
('We book vetted carriers across Sioux Falls and the Big Sioux valley, from the Cathedral district to Harrisburg and Brandon.','We book vetted carriers across Sioux Falls and the Big Sioux valley, from the Cathedral district to Harrisburg.'),
('It also covers the health systems, the card centers, the pork plant, the Guard wing, the colleges, the blizzards, and the lanes.','It also covers the health systems, the card centers, the plant, the Guard wing, the colleges, and the blizzards.'),
('The 29 carriers pass between Omaha and Fargo every day, and the 90 carriers cross between Chicago and the Northwest.','The 29 carriers pass between Omaha and Fargo every day. The 90 carriers cross between Chicago and the Northwest.'),
('It comes up from Sioux City along the west side of the city, crosses 90, and leaves north for Brookings, Watertown, and Fargo.','It comes up from Sioux City along the west side of the city and crosses 90. It leaves north for Brookings, Watertown, and Fargo.'),
('It runs along the north side from the Minnesota line past the airport and leaves west for Mitchell and the Black Hills.','It runs along the north side past the airport and leaves west for Mitchell and the Black Hills.'),
('Interstate 229 leaves 29 at the south end and loops east and north to 90, with exits for every part of the south and east sides.','Interstate 229 leaves 29 at the south end and loops east and north to 90. It has an exit for every part of the south and east sides.'),
('The bridges over the Big Sioux at 8th, 10th, and 26th tie the East Bank and the east side to downtown.','The bridges over the Big Sioux at 8th, 10th, and 26th tie the east side to downtown.'),
('The big-box lots on 41st and Louise, the arena lots on the north side outside event nights, and the fairgrounds lots on 12th outside fair week work too.','The big-box lots on 41st and Louise work too. So do the arena lots outside event nights and the fairgrounds lots outside fair week.'),
('The East Bank across the river is lofts, the old warehouses, and our office, on short blocks with little room.','The East Bank across the river is lofts, old warehouses, and our office on short blocks with little room.'),
('The Cathedral district on the hill west of downtown is the oldest neighborhood in the city, narrow streets under big trees around the cathedral.','The Cathedral district on the hill west of downtown is the oldest neighborhood in the city. The streets are narrow and the trees are big.'),
('The north end past the airport is the plant, the rail yards, and the newer blocks toward Benson Road.','The north end past the airport is the plant, the rail yards, and the newer blocks near Benson Road.'),
('The south side from 41st Street down to 85th is where the city grew, wide subdivisions on former farm fields.','The south side from 41st Street down to 85th is where the city grew, wide subdivisions on old farm fields.'),
('The west side along Louise and out toward Tea is the same, with the mall and the big-box strip in the middle.','The west side along Louise and out toward Tea is the same. The mall and the big-box strip sit in the middle.'),
('Harrisburg and Tea to the south, Brandon to the east, and Hartford to the west ship with the same trucks and price the same as Sioux Falls.','Harrisburg and Tea to the south, Brandon to the east, and Hartford to the west ship with the same trucks. All of them price the same as Sioux Falls.'),
('The week of dates you give and the trucks crossing on 29 and 90 that week set the real quote.','Your week of dates and the trucks crossing on 29 and 90 that week set the real quote.'),
('The card centers on the north and west sides relocate managers on start dates, and the banks downtown do the same.','The card centers on the north and west sides relocate managers on start dates. The banks downtown do the same.'),
('The pork plant on the north side moves managers on production dates, and the ag technology company does the same on project dates.','The pork plant on the north side moves managers on production dates. The ag technology company does the same on project dates.'),
('The two universities on 33rd and 22nd Streets take student cars in late August and send them home in May.','The two universities on 33rd and 22nd Streets take student cars in late August. They send them home in May.'),
('The same week the rally in the Black Hills sends thousands of motorcycles west on 90, and the truck stops fill up.','The same week the rally in the Black Hills sends thousands of motorcycles west on 90. The truck stops fill up.'),
('The pheasant opener on the third Saturday of October fills the hotels again, and the handoff moves to the morning.','The pheasant opener on the third Saturday of October fills the hotels again. The handoff moves to the morning.'),
('A blizzard on the open prairie closes 29 and 90 for a day at a time, and the state posts no travel until the plows catch up.','A blizzard on the open prairie closes 29 and 90 for a day at a time. The state posts no travel until the plows catch up.'),
('The April 2013 ice storm put two inches of ice on every tree in the city and left half of it dark for a week.','The April 2013 ice storm put two inches of ice on every tree in the city. Half of it stayed dark for a week.'),
('Three tornadoes crossed the city on a September night in 2019 and tore up 41st Street from the mall to the hospitals.','Three tornadoes crossed the city on a September night in 2019. They tore up 41st Street from the mall to the hospitals.'),
('The diversion channel keeps downtown dry, but the river parks and the low blocks on the east side flood.','The diversion channel keeps downtown dry. The river parks and the low blocks on the east side flood.'),
('We know which carriers cross on 29 and 90 each week and when the state will post no travel.','We know which carriers cross on 29 and 90 each week and when the state posts no travel.'),
('The blocks around 33rd and 22nd Streets are full that week, so the meeting point is the mall lots.','The blocks around 33rd and 22nd Streets are full that week. The meeting point is the mall lots.'),
('Brookings is an hour up 29 and prices a shade higher, with the handoff at a lot near campus.','Brookings is an hour up 29 and prices a shade higher. The handoff is at a lot near campus.'),
('The state posts no travel on both interstates in a blizzard, and a carrier waits in Omaha or Sioux City.','The state posts no travel on both interstates in a blizzard. A carrier waits in Omaha or Sioux City.'),
('The fair jams 12th Street for ten days, and the rally sends thousands of motorcycles west on 90 the same week.','The fair jams 12th Street for ten days. The rally sends thousands of motorcycles west on 90 the same week.'),
('Tell us the neighborhood and a week of dates, and we flag the next carrier crossing on 29 or 90.','Tell us the neighborhood and a week of dates, and we flag the next carrier through.'),
])
fix('build_siouxfalls_local.py', [
('Car shipping in Sioux Falls rides Interstate 29 and Interstate 90, which cross at the northwest corner of the city.','Car shipping in Sioux Falls rides Interstate 29 and Interstate 90, which cross at the edge of the city.'),
('Ship Guy is a licensed auto transport broker with an office on South Reid Street on the East Bank.','Ship Guy is a licensed auto transport broker with an office on South Reid Street downtown.'),
('It also covers the health systems, the card centers, the plant, the Guard wing, the colleges, and the blizzards.','It also covers the health systems, the card centers, the Guard wing, the colleges, and the blizzards.'),
('The East Bank across the river is lofts, old warehouses, and our office on short blocks with little room.','The East Bank across the river is lofts, old warehouses, and our office on short blocks.'),
('The north end past the airport is the plant, the rail yards, and the newer blocks near Benson Road.','The north end past the airport is the plant, the rail yards, and the newer blocks.'),
('The south side from 41st Street down to 85th is where the city grew, wide subdivisions on old farm fields.','The south side from 41st Street down to 85th is where the city grew. The subdivisions are wide.'),
('Harrisburg and Tea to the south, Brandon to the east, and Hartford to the west ship with the same trucks.','Harrisburg and Tea to the south and Brandon and Hartford on either side ship with the same trucks.'),
])
fix('build_siouxfalls_local.py', [
('Car shipping in Sioux Falls rides Interstate 29 and Interstate 90, which cross at the edge of the city.','Car shipping in Sioux Falls rides Interstate 29 and Interstate 90, which cross at the edge of town.'),
])

fix('build_charlestonwv_local.py', [
('We book vetted carriers across the Kanawha Valley, from the East End to Kanawha City, Teays Valley, and the hollows.','We book vetted carriers across the Kanawha Valley, from the East End to Teays Valley and the hollows.'),
('This page covers 64, 77, 79, the Turnpike, Corridor G, the bridges, downtown, the hills, and the valley towns.','This page covers 64, 77, 79, the Turnpike, Corridor G, downtown, the hills, and the valley towns.'),
('It also covers the Capitol, the hospitals, the chemical plants, the Guard wing, the floods, the ice, and the lanes.','It also covers the Capitol, the hospitals, the chemical plants, the Guard wing, the floods, and the ice.'),
('South Hills, the East End lanes, the West Side, and the hollows meet the truck on a main road or in the valley.','South Hills, the East End lanes, the West Side, and the hollows meet the truck on a main road.'),
('It comes in from Huntington along the Kanawha, crosses the river on the Fort Hill Bridge, and joins 77 east of downtown.','It comes in from Huntington along the Kanawha and crosses the river on the Fort Hill Bridge. It joins 77 east of downtown.'),
('It comes down from Parkersburg, meets 79 and 64 at the junction north of downtown, and leaves south on the Turnpike for Princeton and Bluefield.','It comes down from Parkersburg and meets 79 and 64 at the junction north of downtown. It leaves south on the Turnpike for Princeton and Bluefield.'),
('The Turnpike charges by the axle at three plazas between Charleston and Princeton, and the tolls ride inside every quote.','The Turnpike charges by the axle at three plazas between Charleston and Princeton. The tolls ride inside every quote.'),
('The big-box lots on MacCorkle in Kanawha City, the Coliseum lots downtown outside event nights, and the mall lots in Teays Valley work too.','The big-box lots on MacCorkle in Kanawha City work too. So do the Coliseum lots outside event nights and the mall lots in Teays Valley.'),
('Downtown runs along Capitol Street and Kanawha Boulevard, brick blocks with angled parking and the Coliseum at the west end.','Downtown runs along Capitol Street and Kanawha Boulevard, brick blocks with angled parking. The Coliseum sits at the west end.'),
('The West Side across the Elk is older grids on narrow streets, and the driver meets you on Patrick Street.','The West Side across the Elk is older grids on narrow streets. The driver meets you on Patrick Street.'),
('Kanawha City across the river is the flat grid of the city, and the curb works on nearly every block.','Kanawha City across the river is the flat grid of the city. The curb works on nearly every block.'),
('South Charleston, Dunbar, Nitro, and St. Albans down the valley are old plant towns on flat grids where the curb usually works.','South Charleston, Dunbar, Nitro, and St. Albans down the valley are old plant towns on flat grids. The curb usually works.'),
('The legislature brings a crowd for sixty days from January, and a new governor brings an appointee class every fourth January.','The legislature brings a crowd for sixty days from January. A new governor brings an appointee class every fourth January.'),
('The university on the river takes student cars in late August, and the state university in Institute does the same.','The university on the river takes student cars in late August. The state university in Institute does the same.'),
('In June 2016 the Elk and the creeks rose in an afternoon and took Clendenin and Elkview with them.','In June 2016 the Elk and the creeks rose in an afternoon and took Clendenin with them.'),
('The Turnpike over the mountain closes for a day at a time, and the carriers wait in Charleston or Beckley.','The Turnpike over the mountain closes for a day at a time. The carriers wait in Charleston or Beckley.'),
('The June 2012 derecho put the valley in the dark for a week and dropped trees across every hill road.','The June 2012 derecho put the valley in the dark for a week. Trees came down on every hill road.'),
('An enclosed trailer keeps off the salt and cinders of a mountain winter and the grit of the Turnpike.','An enclosed trailer keeps off the salt and cinders of a mountain winter and the Turnpike grit.'),
('At pickup the driver circles the car with you and writes up its condition on the Bill of Lading.','At pickup the driver circles the car with you and writes its condition on the Bill of Lading.'),
('Charlotte runs two hundred eighty to four hundred ten, about two hundred ninety miles down 77 and the Turnpike.','Charlotte runs two hundred eighty to four hundred ten, about two hundred ninety miles down 77.'),
('The carriers pay by the axle at the three plazas between Charleston and Princeton, and the toll rides inside the quote.','The carriers pay by the axle at the three plazas between Charleston and Princeton. The toll rides inside the quote.'),
('South Hills is switchbacks a trailer cannot climb, and the East End lanes are too narrow to turn in.','South Hills is switchbacks a trailer cannot climb. The East End lanes are too narrow to turn in.'),
])
fix('build_charlestonwv_local.py', [
('South Hills, the East End lanes, the West Side, and the hollows meet the truck on a main road.','South Hills, the East End lanes, and the hollows meet the truck on a main road.'),
])

fix('build_cheyenne_local.py', [
('Car shipping in Cheyenne rides Interstate 80 and Interstate 25, which cross on the west edge of the city.','Car shipping in Cheyenne rides Interstate 80 and Interstate 25, which cross on the west edge of town.'),
('It also covers the base, the Capitol, the data centers, the railroad, Frontier Days, the blizzards, and the lanes.','It also covers the base, the Capitol, the data centers, the railroad, Frontier Days, and the blizzards.'),
('The Avenues, downtown, the base housing, and the Ranchettes meet the truck at a lot, the gate, or the pavement.','The Avenues, downtown, the base housing, and the Ranchettes meet the truck at a lot or the gate.'),
('It comes in from Nebraska past Pine Bluffs, runs the south side of the city, and climbs west to the Summit between Cheyenne and Laramie.','It comes in from Nebraska past Pine Bluffs and runs the south side of the city. Then it climbs west to the Summit toward Laramie.'),
('The Summit at eight thousand six hundred feet closes dozens of times a winter for snow, ice, and wind.','The Summit at eight thousand six hundred feet closes dozens of times a winter.'),
('The state closes 80 and 25 to light, high-profile vehicles when gusts pass sixty, and a loaded car hauler counts.','The state closes 80 and 25 to light, high-profile vehicles when gusts pass sixty. A loaded car hauler counts.'),
('The big-box lots on Dell Range, the college lots on a weekend, and the depot lots downtown outside the rodeo work too.','The big-box lots on Dell Range and the college lots on a weekend work too. So do the depot lots outside the rodeo.'),
('Saddle Ridge, the Pointe, and the subdivisions off Yellowstone Road are wide and new, and the driver reaches the house.','Saddle Ridge, the Pointe, and the subdivisions off Yellowstone Road are wide and new. The driver reaches the house.'),
('The base on the west edge is gated, and the housing beyond the gate is off limits to a carrier.','The base on the west edge is gated. The housing beyond the gate is off limits to a carrier.'),
('Burns and Pine Bluffs out 80 and Chugwater up 25 ship with the same trucks and price the same as Cheyenne.','Burns and Pine Bluffs out 80 and Chugwater up 25 ship with the same trucks. They price the same as Cheyenne.'),
('A report date at the base in July or Frontier Days the same month lands in the busiest weeks of the year.','A report date at the base in July or Frontier Days the same month lands in the busiest weeks.'),
('The missile wing on the west edge rotates airmen and officers on orders all year, with a summer peak.','The missile wing rotates airmen and officers on orders all year, with a summer peak.'),
('The university over the Summit in Laramie does the same, and its cars meet the truck in Cheyenne when the pass is closed.','The university over the Summit in Laramie does the same. Its cars meet the truck in Cheyenne when the pass is closed.'),
('Two hundred thousand people come, the parades close Capitol Avenue four mornings, and every hotel within a hundred miles is full.','Two hundred thousand people come, and the parades close Capitol Avenue four mornings. Every hotel within a hundred miles is full.'),
('The state closes 80 and 25 to high-profile vehicles when the gusts pass sixty, and a loaded trailer waits.','The state closes 80 and 25 to high-profile vehicles when the gusts pass sixty. A loaded trailer waits.'),
('The Summit on 80 closes dozens of times a winter for snow and ice, and the Salt Lake car waits in Cheyenne.','The Summit on 80 closes dozens of times a winter for snow and ice. The Salt Lake car waits in Cheyenne.'),
('An enclosed trailer keeps off the hail, the gravel of the Summit, and the sand the state spreads on 80.','An enclosed trailer keeps off the hail, the gravel of the Summit, and the sand on 80.'),
('We know which carriers cross on 80 each week, when the Summit is shut, and when the wind has closed the road.','We know which carriers cross on 80 each week and when the Summit or the wind has closed the road.'),
('Salt Lake City runs four hundred to five hundred seventy, about four hundred forty miles across the state on 80.','Salt Lake City runs four hundred to five hundred seventy, about four hundred forty miles out 80.'),
('The carriers cross on 80 between Salt Lake City and Nebraska and add a Cheyenne stop when the load lines up.','The carriers cross on 80 between Salt Lake City and Nebraska. One adds a Cheyenne stop when the load lines up.'),
('The state closes both roads to high-profile vehicles when the gusts pass sixty, and a loaded car hauler counts.','The state closes both roads to high-profile vehicles when the gusts pass sixty. A loaded car hauler counts.'),
('Two hundred thousand people come, the parades close Capitol Avenue, and every hotel for a hundred miles is full.','Two hundred thousand people come and the parades close Capitol Avenue. Every hotel for a hundred miles is full.'),
('Laramie is an hour over the Summit, and its cars meet the truck in Cheyenne when the pass is closed.','Laramie is an hour over the Summit. Its cars meet the truck in Cheyenne when the pass is closed.'),
('Where the car is and where it goes, with the neighborhood or the town and whether the road is paved.','Where the car is and where it goes, with the neighborhood and whether the road is paved.'),
('Give us the neighborhood and a week of dates, and we catch the next carrier on 80 or up from Denver.','Give us the neighborhood and a week of dates, and we catch the next carrier on 80 or from Denver.'),
])
fix('build_cheyenne_local.py', [
('A report date at the base in July or Frontier Days the same month lands in the busiest weeks.','A July report date at the base or Frontier Days the same month lands in the busiest weeks.'),
('We know which carriers cross on 80 each week and when the Summit or the wind has closed the road.','We know which carriers cross on 80 each week and when the Summit or the wind shuts it.'),
('Give us the neighborhood and a week of dates, and we catch the next carrier on 80 or from Denver.','Give us the neighborhood and a week of dates, and we catch the next carrier through.'),
])

fix('build_norfolk_local.py', [
('Car shipping in Norfolk runs on Interstate 64 and 264 and through the tunnels that tie the city to everything else.','Car shipping in Norfolk runs on Interstate 64 and 264 and through the tunnels that tie the city together.'),
('We book vetted carriers across Norfolk, from Ghent to Ocean View and out to the base and Little Creek.','We book vetted carriers across Norfolk, from Ghent to Ocean View and out to the base gates.'),
('Interstate 64 comes in from Richmond through the Hampton Roads tunnel and loops the east side of the city.','Interstate 64 comes in from Richmond through the Hampton Roads tunnel and loops the east side.'),
('It also covers the Navy, the port, the hospitals, the two universities, the nor’easters, the tides, and the lanes.','It also covers the Navy, the port, the hospitals, the universities, the nor’easters, and the tides.'),
('It comes down the Peninsula, dives under the harbor in the Hampton Roads tunnel, and loops the east side of the city past the airport to Chesapeake.','It comes down the Peninsula and dives under the harbor in the Hampton Roads tunnel. Then it loops the east side past the airport to Chesapeake.'),
('The big-box lots on Military Highway, the stadium lots by the university outside game days, and the Ocean View lots on a weekday work too.','The big-box lots on Military Highway work too. So do the stadium lots outside game days and the Ocean View lots on a weekday.'),
('Wards Corner is the crossroads of the north side, and the grids around it from Titustown to Norview are wide enough for a trailer.','Wards Corner is the crossroads of the north side. The grids around it from Titustown to Norview are wide enough for a trailer.'),
('Ocean View along the bay is beach lanes from Willoughby Spit to East Ocean View, and the handoff moves to Ocean View Avenue.','Ocean View along the bay is beach lanes from Willoughby Spit to East Ocean View. The handoff moves to Ocean View Avenue.'),
('The base housing at the naval station and Little Creek is behind the gates, and the handoff happens outside them.','The base housing at the naval station and Little Creek is behind the gates. The handoff happens outside them.'),
('The naval station at the end of Hampton Boulevard is the largest in the world, and the amphibious base at Little Creek sits beside it.','The naval station at the end of Hampton Boulevard is the largest in the world. The amphibious base at Little Creek sits beside it.'),
('The port terminals on the river move managers on contract dates, and the ships’ cars clear customs at the terminal.','The port terminals on the river move managers on contract dates. The ships’ cars clear customs at the terminal.'),
('The hospital system headquartered in the city runs the trauma center in Ghent and the children’s hospital beside it.','The hospital system headquartered here runs the trauma center in Ghent and the children’s hospital beside it.'),
('The university on Hampton Boulevard takes student cars in late August, and the university on Brambleton does the same.','The university on Hampton Boulevard takes student cars in late August. The university on Brambleton does the same.'),
('The tide floods the Hague in Ghent, the Crosstown blocks by the hospital, and the Ocean View lanes on a sunny day a dozen times a year.','The tide floods the Hague in Ghent and the Ocean View lanes on a sunny day a dozen times a year.'),
('Isabel in 2003 is the benchmark, and Matthew in 2016 dropped fourteen inches of rain on the city in a night.','Isabel in 2003 is the benchmark. Matthew in 2016 dropped fourteen inches of rain on the city in a night.'),
('A pickup in an evacuation waits for the all-clear, and you hear it from us the moment a watch is posted.','A pickup in an evacuation waits for the all-clear. You hear it from us the moment a watch is posted.'),
('An enclosed trailer keeps off the salt air, the pollen, and the brine the state sprays before a snow.','An enclosed trailer keeps off the salt air, the pollen, and the brine sprayed before a snow.'),
('New York runs three hundred fifty to five hundred ten, about three hundred seventy miles up the same road.','New York runs three hundred fifty to five hundred ten, about three hundred seventy miles north.'),
])
fix('build_norfolk_local.py', [
('Car shipping in Norfolk runs on Interstate 64 and 264 and through the tunnels that tie the city together.','Car shipping in Norfolk runs on Interstate 64 and 264 and through the tunnels between them.'),
('The tide floods the Hague in Ghent and the Ocean View lanes on a sunny day a dozen times a year.','The tide floods the Hague in Ghent and the Ocean View lanes a dozen times a year.'),
])

fix('build_bethlehem_local.py', [
('Car shipping in Bethlehem runs on Interstate 78 and Route 22, the two roads that bracket the city north and south.','Car shipping in Bethlehem runs on Interstate 78 and Route 22, which bracket the city north and south.'),
('This page covers 78, 22, 378, 412, 33, the bridges, downtown, the South Side, the Moravian district, and the valley towns.','This page covers 78, 22, 378, 412, 33, downtown, the South Side, the Moravian district, and the valley towns.'),
('It also covers the universities, the hospital, the device maker, the casino, the warehouses, Musikfest, the ice, and the lanes.','It also covers the universities, the hospital, the device maker, the casino, the warehouses, Musikfest, and the ice.'),
('The New York-to-Harrisburg carriers pass the city on 78 every day, and the Philadelphia trucks come up 476 and 309.','The New York-to-Harrisburg carriers pass the city on 78 every day. The Philadelphia trucks come up 476 and 309.'),
('It runs along the south edge of the city past Hellertown and leaves east for the Delaware and the Turnpike.','It runs along the south edge of the city past Hellertown and leaves east for the Delaware.'),
('The New York carriers ride it every day, and the Philadelphia carriers come up 476 and 309 to meet it.','The New York carriers ride it every day. The Philadelphia carriers come up 476 and 309 to meet it.'),
('Route 378 comes down from 22 through West Bethlehem, crosses the river on the Hill-to-Hill Bridge, and climbs the South Side to 78.','Route 378 comes down from 22 through West Bethlehem and crosses the river on the Hill-to-Hill Bridge. Then it climbs the South Side to 78.'),
('The big-box lots on Route 33 in Bethlehem Township, the mall lots on Route 22, and the stadium lots on the hill outside game days work too.','The big-box lots on Route 33 and the mall lots on Route 22 work too. So do the stadium lots on the hill outside game days.'),
('The Moravian district along Main and Church Streets is the oldest part of the city, stone buildings on streets laid out in 1741.','The Moravian district along Main and Church Streets is the oldest part of the city. The stone buildings sit on streets laid out in 1741.'),
('Center City along Broad Street is brick storefronts and angled parking, and the handoff happens on the same lots.','Center City along Broad Street is brick storefronts and angled parking. The handoff happens on the same lots.'),
('The South Side across the Fahy Bridge is the steel neighborhood, rowhouses on narrow one-way streets from Third Street to the hill.','The South Side across the Fahy Bridge is the steel neighborhood. Rowhouses line narrow one-way streets from Third Street to the hill.'),
('Bethlehem Township to the east along Freemansburg Avenue and Route 33 is wide subdivisions and big-box lots, and the driver reaches the house.','Bethlehem Township to the east along Freemansburg Avenue is wide subdivisions and big-box lots. The driver reaches the house.'),
('Nazareth up 33, Easton down 22, and Allentown next door ship with the same trucks and price the same as Bethlehem.','Nazareth up 33, Easton down 22, and Allentown next door ship with the same trucks. All of them price the same as Bethlehem.'),
('The university on the north side does the same, and the community college in the township follows a week later.','The university on the north side does the same. The community college in the township follows a week later.'),
('The campus hill is closed to a trailer in move-in week, so the meeting point is the stadium lots.','The campus hill is closed to a trailer in move-in week. The meeting point is the stadium lots.'),
('Commuters to New York and Philadelphia buy in the valley for the prices and ship one car behind the moving truck.','Commuters to New York and Philadelphia buy in the valley for the prices. They ship one car behind the moving truck.'),
('The Guard post at Indiantown Gap sends a few families east on orders, and Ship Guy is a private broker with no connection to it.','The Guard post at Indiantown Gap sends a few families east on orders. Ship Guy is a private broker with no connection to it.'),
('Families moving over the mountain to Hellertown or out to the township ship one car and drive the other.','Families moving over the mountain to Hellertown ship one car and drive the other.'),
('Christkindlmarkt fills the plant site from Thanksgiving to Christmas, and the Christmas City lights fill Main Street every December weekend.','Christkindlmarkt fills the plant site from Thanksgiving to Christmas. The Christmas City lights fill Main Street every December weekend.'),
('The rivalry game in November fills the stadium on the hill every other year and the roads to Easton the other years.','The rivalry game in November fills the stadium on the hill every other year. The other years it fills the roads to Easton.'),
('The campus hill, the Wyandotte hill on 378, and Fountain Hill close to a trailer until the ice melts.','The campus hill, the Wyandotte hill on 378, and Fountain Hill close to a trailer until it melts.'),
('A pickup in the district or along the creek waits for the water to drop and moves to Broad Street.','A pickup in the district or along the creek waits for the water to drop. The handoff moves to Broad Street.'),
('The Moravian district is colonial streets a trailer cannot enter, and the South Side is rowhouses on narrow one-way streets.','The Moravian district is colonial streets a trailer cannot enter. The South Side is rowhouses on narrow one-way streets.'),
('The driver meets you at the Broad Street lots, on Third or Fourth Street, or at the casino lots.','The driver meets you at the Broad Street lots, on Third Street, or at the casino lots.'),
('The university on the hill takes cars in late August, and the university on the north side does the same.','The university on the hill takes cars in late August. The university on the north side does the same.'),
('Allentown rides the same carriers off 22 and 78, and its row-house blocks meet the truck on a main road.','Allentown rides the same carriers off 22 and 78. Its row-house blocks meet the truck on a main road.'),
('The hills stay closed to a trailer until the ice melts, and the handoff moves to a lot on the flats.','The hills stay closed to a trailer until the ice melts. The handoff moves to a lot on the flats.'),
('The creek runs through the Moravian district and floods in a hurricane’s remnants, as it did with Ida in 2021.','The creek runs through the Moravian district and floods in a hurricane’s remnants. Ida did it in 2021.'),
])
fix('build_bethlehem_local.py', [
('This page covers 78, 22, 378, 412, 33, downtown, the South Side, the Moravian district, and the valley towns.','This page covers 78, 22, 378, 412, downtown, the South Side, the Moravian district, and the valley towns.'),
("'turnpike',",""),
])
fix('build_norfolk_local.py', [
("The family sends the second one with us, and Ship Guy is a private broker with no tie to the Navy.","The family sends the second one with us. Ship Guy is a private broker with no tie to the Navy."),
("'governor',",""),
])
