D='/home/claude/tools/builders_city/'
def fix(fn, pairs):
    p=D+fn; s=open(p,encoding='utf-8').read()
    for item in pairs:
        old,new=item[0],item[1]; k=item[2] if len(item)>2 else 1
        c=s.count(old); assert c==k, (fn, c, old[:70])
        s=s.replace(old,new)
    open(p,'w',encoding='utf-8').write(s); print(fn, len(pairs), 'fixes')

fix('build_warwick_local.py', [
("Route 2 is Bald Hill Road, the retail strip, and Route 117 runs from the bay through Apponaug to the west.","Route 2 is Bald Hill Road, the retail strip. Route 117 runs from the bay through Apponaug to the west."),
("This page covers 95, 295, Route 2, Route 117, the airport, the villages on the bay, and the hills to the west.","This page covers 95, 295, Route 2, Route 117, the airport, the bay villages, and the hills to the west."),
("It carries the New York-to-Boston lane, and the exits for the airport, Route 37, Route 117, and Route 4 all fall inside Warwick.","It carries the New York-to-Boston lane. The exits for the airport, Route 37, Route 117, and Route 4 all fall inside Warwick."),
("Warwick is thirty villages on a bay, and the ones on the water are the ones a trailer skips.","Warwick is thirty villages on a bay. The ones on the water are the ones a trailer skips."),
("A seventy-five-foot trailer stays on West Shore Road, and the driver meets you there or at the beach lots.","A seventy-five-foot trailer stays on West Shore Road. The driver meets you there or at the beach lots."),
("Cowesett in the west is hills and big lots, and the driver reaches the driveway or meets you on Cowesett Avenue.","Cowesett in the west is hills and big lots. The driver reaches the driveway or meets you on Cowesett Avenue."),
("Potowomut across the river sits by the state park on the East Greenwich line, and the handoff happens on Ives Road.","Potowomut across the river sits by the state park on the East Greenwich line. The handoff happens on Ives Road."),
("The airport is the state’s front door, and its airlines, its contractors, and the car-rental lots hire year round.","The airport is the state’s front door. Its airlines, its contractors, and the car-rental lots hire year round."),
("The Pawtuxet runs along the north edge of the city, and the March 2010 flood put it over the mall.","The Pawtuxet runs along the north edge of the city. The March 2010 flood put it over the mall."),
("At pickup you and the driver walk around the car, and the Bill of Lading records every existing mark.","At pickup you and the driver walk around the car. The Bill of Lading records every existing mark."),
])

fix('build_stpaul_local.py', [
("Car shipping in St. Paul runs on Interstate 94 and the 494 and 694 ring around the Twin Cities.","Car shipping in St. Paul runs on Interstate 94 and the ring around the Twin Cities."),
("We book vetted carriers across Saint Paul and the east metro, from Highland Park to the East Side and Roseville to Woodbury.","We book vetted carriers across Saint Paul and the east metro, from Highland Park to Roseville and Woodbury."),
("Interstate 35E runs north and south through downtown, and the south half is a parkway that bans heavy trucks.","Interstate 35E runs north and south through downtown. Its south half is a parkway that bans heavy trucks."),
("This page covers 94, 35E, the ring, the truck ban, downtown, Summit Hill, the East Side, the Midway, Highland, and the suburbs.","This page covers 94, 35E, the ring, the truck ban, downtown, Summit Hill, the Midway, Highland, and the suburbs."),
("It also covers the state workforce, the headquarters, the campuses, the State Fair, the snow emergencies, and the lanes.","It also covers the state workforce, the headquarters, the campuses, the fair, the snow emergencies, and the lanes."),
("The Chicago and Fargo carriers run 94 through the city every day, and the Iowa trucks come up 35.","The Chicago and Fargo carriers run 94 through the city every day. The Iowa trucks come up 35."),
("St. Paul sits on the east side of the metro, and a carrier reaches every suburb from the ring without touching the hills.","St. Paul sits on the east side of the metro. A carrier reaches every suburb from the ring without touching the hills."),
("Interstate 94 is the Chicago-to-Fargo road, and it runs from Minneapolis through the Midway and downtown to Hudson, Wisconsin.","Interstate 94 is the Chicago-to-Fargo road. It runs from Minneapolis through the Midway and downtown to Hudson, Wisconsin."),
("South of downtown it is a parkway with a 45 limit and a ban on trucks over four and a half tons.","South of downtown it is a parkway with a 45 limit. Trucks over four and a half tons are banned."),
("The Rosedale lots in Roseville, the Maplewood Mall lots on 694, and the Woodbury centers on 94 work too.","The Rosedale lots in Roseville and the Maplewood Mall lots on 694 work too. So do the Woodbury centers on 94."),
("The West Side across the river is a flat grid of small houses, and the handoff moves to Robert Street.","The West Side across the river is a flat grid of small houses. The handoff moves to Robert Street."),
("Highland Park has wider streets and the new neighborhood on the old Ford plant, and the curb usually works.","Highland Park has wider streets and the new neighborhood on the old Ford plant. The curb usually works."),
("The Midway along University Avenue is the soccer stadium, the rail line, and a mix of old blocks and big-box lots.","The Midway along University Avenue is the soccer stadium, the rail line, old blocks, and big-box lots."),
("The East Side, from Payne-Phalen to Dayton’s Bluff and Battle Creek, is a grid of older houses and the handoff moves to the shopping centers.","The East Side, from Payne-Phalen to Dayton’s Bluff and Battle Creek, is a grid of older houses. The handoff moves to the shopping centers."),
("The Arizona and Florida lanes fill each fall with snowbirds, and the price runs higher in October than in June.","The Arizona and Florida lanes fill each fall with snowbirds. The price runs higher in October than in June."),
("The water and hygiene company downtown, the insurer on Robert Street, and the tape and adhesives company in Maplewood relocate engineers and managers on offer dates.","The water and hygiene company downtown and the insurer on Robert Street relocate staff on offer dates. The tape and adhesives company in Maplewood moves engineers the same way."),
("The university on Summit, the colleges along Snelling and Grand, and the campus on Dayton’s Bluff all do it.","The university on Summit and the colleges along Snelling and Grand do it. So does the campus on Dayton’s Bluff."),
("The State Fair fills the fairgrounds for the twelve days ending on Labor Day, and two million people come.","The State Fair fills the fairgrounds for the twelve days ending on Labor Day. Two million people come."),
("The Winter Carnival fills downtown and Rice Park for ten days in late January, and the ice palace years close whole blocks.","The Winter Carnival fills downtown and Rice Park for ten days in late January. The ice palace years close whole blocks."),
("A snow emergency puts the plows on the night routes first and the day routes next, and a car on the wrong side gets towed.","A snow emergency puts the plows on the night routes first and the day routes next. A car on the wrong side gets towed."),
("At pickup the driver and you inspect the car together, and the Bill of Lading records every existing mark.","At pickup the driver and you inspect the car together. The Bill of Lading records every existing mark."),
("Summit Hill and Cathedral Hill are narrow Victorian blocks parked on both sides, and downtown is ramps and one-way streets.","Summit Hill and Cathedral Hill are narrow Victorian blocks parked on both sides. Downtown is ramps and one-way streets."),
("Because the south half of 35E is a parkway with a 45 limit and a ban on trucks over four and a half tons.","Because the south half of 35E is a parkway with a 45 limit. It bans trucks over four and a half tons."),
])

fix('build_jackson_local.py', [
("Car shipping in Jackson works on the two interstates that cross south of downtown and the carriers they bring.","Car shipping in Jackson works on the two interstates that cross south of downtown."),
("This page covers 55, 20, 220, the Stack, Lakeland Drive, County Line Road, and the neighborhoods from Belhaven to Byram.","This page covers 55, 20, 220, the Stack, Lakeland Drive, County Line Road, and Belhaven to Byram."),
("It also covers the state workforce, the medical center, the assembly plant, the campuses, the fair, the tornadoes, and the lanes.","It also covers the state workforce, the medical center, the plant, the campuses, the fair, the tornadoes, and the lanes."),
("The plant in Canton keeps car haulers based in the metro, and the 55 and 20 traffic never stops.","The plant in Canton keeps car haulers based in the metro. The 55 and 20 traffic never stops."),
("Jackson is the crossroads of the state, and a carrier reaches every suburb from the interstates without crossing a pothole downtown.","Jackson is the crossroads of the state. A carrier reaches every suburb from the interstates without crossing a pothole downtown."),
("Interstate 55 runs north and south through the city, from Byram past downtown and the medical center to Ridgeland and Madison.","Interstate 55 runs north and south through the city. It runs from Byram past downtown and the medical center to Ridgeland and Madison."),
("Eastover and Woodland Hills are big houses on curving streets under the trees, and a trailer stays off them.","Eastover and Woodland Hills are big houses on curving streets under the trees. A trailer stays off them."),
("South Jackson along Terry Road and McDowell Road is postwar grids, and the curb works on most of them.","South Jackson along Terry Road and McDowell Road is postwar grids. The curb works on most of them."),
("Jackson prices among the best in the Deep South, because four interstates cross here and the plant keeps haulers based nearby.","Jackson prices among the best in the Deep South. Four interstates cross here, and the plant keeps haulers based nearby."),
("The state government is the largest employer in the city, and its agencies transfer staff on start dates all year.","The state government is the largest employer in the city. Its agencies transfer staff on start dates all year."),
("The assembly plant in Canton twenty miles north moves engineers in on launch schedules, and its suppliers along 55 do the same.","The assembly plant in Canton twenty miles north moves engineers in on launch schedules. Its suppliers along 55 do the same."),
("The state university in West Jackson, the college in Belhaven, the one on North State Street, and the college in Clinton all do it.","The state university in West Jackson and the college in Belhaven do it. So do the college on North State Street and the one in Clinton."),
("The State Fair fills the fairgrounds on High Street for twelve days in October, and the downtown streets around it close.","The State Fair fills the fairgrounds on High Street for twelve days in October. The downtown streets around it close."),
("The classic in the fall and the homecoming games fill the stadium on North State Street and the streets around it.","The classic in the fall and the homecoming games fill the stadium on North State Street. The streets around it fill too."),
("Warnings close the roads for an hour at a time from March through May, and a carrier parks until the cell passes.","Warnings close the roads for an hour at a time from March through May. A carrier parks until the cell passes."),
("The February 2021 storm iced the city for a week, shut the interstates, and left trucks stranded on 55.","The February 2021 storm iced the city for a week and shut the interstates. Trucks sat stranded on 55."),
("The Easter flood of 1979 put thousands of homes under water, and the August 2022 flood reached the same streets in Northeast Jackson.","The Easter flood of 1979 put thousands of homes under water. The August 2022 flood reached the same streets in Northeast Jackson."),
("The collectors in Eastover and Madison book one, and so do executives relocating a new car to the plant.","The collectors in Eastover and Madison book one. So do executives relocating a new car to the plant."),
("At pickup you and the driver go around the car together, and the Bill of Lading records every existing mark.","At pickup you and the driver go around the car together. The Bill of Lading records every existing mark."),
("Atlanta runs three hundred forty to four hundred ninety, about three hundred eighty miles east on the same road.","Atlanta runs three hundred forty to four hundred ninety, about three hundred eighty miles east."),
("Belhaven and the Fondren blocks are narrow streets under low oaks, and a seventy-five-foot trailer stays on the main roads.","Belhaven and the Fondren blocks are narrow streets under low oaks. A seventy-five-foot trailer stays on the main roads."),
("Campus streets are tight that week, so the handoff happens at the lots on Highway 80 or State Street.","Campus streets are tight that week. The handoff happens at the lots on Highway 80 or State Street."),
("Warnings close the roads from March through May, and the window moves to later the same day or the next morning.","Warnings close the roads from March through May. The window moves to later the same day or the next morning."),
("The fair fills High Street for twelve days in October, and the rodeo fills it for three weeks in February.","The fair fills High Street for twelve days in October. The rodeo fills it for three weeks in February."),
("Give us the side of town and the week, and a carrier already crossing at the Stack takes it.","Give us the side of town and the week. A carrier already crossing at the Stack takes it."),
])

fix('build_omaha_local.py', [
("Car shipping in Omaha runs on the busiest truck road in the Plains and the river crossing beside it.","Car shipping in Omaha runs on the busiest truck road in the Plains and the river crossing."),
("We book vetted carriers across the metro, from the Old Market and Dundee to Millard, Elkhorn, Papillion, and Bellevue.","We book vetted carriers across the metro, from the Old Market and Dundee to Millard, Elkhorn, and Bellevue."),
("Interstate 80 runs the south side of the city from the river to Gretna, carrying everything between Chicago and Denver.","Interstate 80 runs the south side of the city from the river to Gretna. It carries everything between Chicago and Denver."),
("Interstate 480 crosses the river downtown, Interstate 680 loops the north and west, and Dodge Street is the spine.","Interstate 480 crosses the river downtown, and Interstate 680 loops the north and west. Dodge Street is the spine."),
("It also covers the headquarters, the base, the medical center, the railroad, the College World Series, the floods, and the lanes.","It also covers the headquarters, the base, the medical center, the College World Series, the floods, and the lanes."),
("Every carrier between Chicago and Denver passes the city on 80, and the Kansas City trucks come up 29.","Every carrier between Chicago and Denver passes the city on 80. The Kansas City trucks come up 29."),
("Omaha is where the Plains truck road meets the river road, and a carrier reaches every suburb from one of them.","Omaha is where the Plains truck road meets the river road. A carrier reaches every suburb from one of them."),
("Interstate 80 enters from Council Bluffs over the Missouri and runs the south side of the city past the stockyards site, Millard, and Gretna.","Interstate 80 enters from Council Bluffs over the Missouri. It runs the south side of the city past the stockyards site, Millard, and Gretna."),
("Interstate 29 runs the Iowa side of the river, and the Kansas City and Sioux Falls trucks ride it to the 80 interchange at the bluffs.","Interstate 29 runs the Iowa side of the river. The Kansas City and Sioux Falls trucks ride it to the 80 interchange at the bluffs."),
("Interstate 480 is the downtown spur, from 80 north past the Old Market and over the river to Council Bluffs.","Interstate 480 is the downtown spur. It runs from 80 north past the Old Market and over the river to Council Bluffs."),
("Dodge Street is US 6, the spine from downtown west to Elkhorn, elevated as the West Dodge expressway beyond 90th.","Dodge Street is US 6, the spine from downtown west to Elkhorn. Beyond 90th it is the elevated West Dodge expressway."),
("The mall lots at 144th and Center, the centers at 168th and Dodge, and the big-box lots in Council Bluffs at the 29 interchange work too.","The mall lots at 144th and Center and the centers at 168th and Dodge work too. So do the big-box lots in Council Bluffs at the 29 interchange."),
("Papillion, La Vista, Gretna, and Bellevue in Sarpy County are the fastest-growing part of the state, and the curb works almost everywhere.","Papillion, La Vista, Gretna, and Bellevue in Sarpy County are the fastest-growing part of the state. The curb works almost everywhere."),
("Omaha prices among the best in the Plains, because the 80 traffic never stops and the 29 trucks turn here.","Omaha prices among the best in the Plains. The 80 traffic never stops, and the 29 trucks turn here."),
("The insurer on Dodge, the railroad downtown, the builder, and the holding company run by the city’s most famous investor all relocate staff on offer dates.","The insurer on Dodge, the railroad downtown, and the builder relocate staff on offer dates. So does the holding company run by the city’s most famous investor."),
("The base in Bellevue is the headquarters of the strategic command, and it moves thousands of airmen and officers on orders every year.","The base in Bellevue is the headquarters of the strategic command. It moves thousands of airmen and officers on orders every year."),
("The College World Series fills the ballpark downtown for two weeks in June, and every hotel in the metro with it.","The College World Series fills the ballpark downtown for two weeks in June. Every hotel in the metro fills with it."),
("A storm closes 80 west of Lincoln for a day, and the carriers wait in Des Moines or Council Bluffs.","A storm closes 80 west of Lincoln for a day. The carriers wait in Des Moines or Council Bluffs."),
("The April 2024 storm tore through Elkhorn and Bennington, and warnings park the carriers for an hour at a time.","The April 2024 storm tore through Elkhorn and Bennington. Warnings park the carriers for an hour at a time."),
("The March 2019 flood closed 29 for months, put the base under water, and shut the river crossings for days.","The March 2019 flood closed 29 for months and put the base under water. The river crossings shut for days."),
("The collectors in Dundee and the west side book one, and so do the executives relocating a new car to the towers.","The collectors in Dundee and the west side book one. So do the executives relocating a new car to the towers."),
("The Old Market is brick streets and carriages, and Dundee is big houses on narrow streets under old trees.","The Old Market is brick streets and carriages. Dundee is big houses on narrow streets under old trees."),
("The insurer, the railroad, the builder, and the holding company relocate staff on offer dates from across the country.","The insurer, the railroad, the builder, and the holding company relocate staff from across the country."),
("Campus streets are tight that week, so the handoff happens at the lots on Dodge or by the ballpark.","Campus streets are tight that week. The handoff happens at the lots on Dodge or by the ballpark."),
("The ballpark fills for two weeks in June, the streets around it close, and every hotel in the metro fills.","The ballpark fills for two weeks in June, and the streets around it close. Every hotel in the metro fills."),
("A blizzard closes 80 west of Lincoln for a day, and a warning closes the roads for an hour.","A blizzard closes 80 west of Lincoln for a day. A warning closes the roads for an hour."),
])

fix('build_newark_local.py', [
("Car shipping in Newark starts at one of the busiest interchanges in the country and ends at a door in the Ironbound.","Car shipping in Newark starts at one of the busiest interchanges in the country and ends in the Ironbound."),
("We book vetted carriers across Essex County and the port towns, from the North Ward to Weequahic and the Oranges to Harrison.","We book vetted carriers across Essex County and the port towns, from the North Ward to Weequahic and the Oranges."),
("The Turnpike runs the east side past the airport and the port, and 78 crosses it on the way to the Holland Tunnel.","The Turnpike runs the east side past the airport and the port. Interstate 78 crosses it on the way to the Holland Tunnel."),
("This page covers the Turnpike, 78, 280, the Parkway, Route 21, downtown, the Ironbound, the North Ward, the wards, and the suburbs.","This page covers the Turnpike, 78, 280, Route 21, downtown, the Ironbound, the North Ward, the wards, and the suburbs."),
("It also covers the port, the airport, the headquarters, the campuses, the cherry blossoms, Sandy and Ida, and the lanes.","It also covers the port, the airport, the headquarters, the campuses, the cherry blossoms, the storms, and the lanes."),
("Every carrier on the 95 lane passes the city on the Turnpike, and the port keeps haulers based next door.","Every carrier on the 95 lane passes the city on the Turnpike. The port keeps haulers based next door."),
("Newark is where the Turnpike, 78, and 280 meet, and a carrier reaches every town in the county without a bridge.","Newark is where the Turnpike, 78, and 280 meet. A carrier reaches every town in the county without a bridge."),
("The Turnpike is Interstate 95, and it runs the east edge of the city past the airport and the port.","The Turnpike is Interstate 95. It runs the east edge of the city past the airport and the port."),
("Interstate 78 crosses the Turnpike beside the airport and runs east to the Holland Tunnel and west to Allentown.","Interstate 78 crosses the Turnpike beside the airport. It runs east to the Holland Tunnel and west to Allentown."),
("Interstate 280 runs from the Turnpike at Kearny over the Passaic and through downtown to the Oranges and 80.","Interstate 280 runs from the Turnpike at Kearny over the Passaic. It continues through downtown to the Oranges and 80."),
("The Garden State Parkway skirts the west side through Irvington and East Orange, but it bans trucks this far north.","The Garden State Parkway skirts the west side through Irvington and East Orange. It bans trucks this far north."),
("Newark is dense wards on a tight grid, and the truck meets nearly all of them at a lot.","Newark is dense wards on a tight grid. The truck meets nearly all of them at a lot."),
("The driver meets you at the lots on Raymond Boulevard by the river or at the Broad Street garages.","The driver meets you at the Raymond Boulevard lots by the river or at the Broad Street garages."),
("University Heights west of downtown is the campuses and the hospital, and the handoff happens at a campus lot.","University Heights west of downtown is the campuses and the hospital. The handoff happens at a campus lot."),
("The Ironbound east of the station is the Portuguese and Brazilian neighborhood, with Ferry Street and streets of row houses between the rail lines.","The Ironbound east of the station is the Portuguese and Brazilian neighborhood. Ferry Street and the row-house streets sit between the rail lines."),
("Harrison across the river is new apartment blocks around the soccer stadium, and the handoff happens at the stadium lots.","Harrison across the river is new apartment blocks around the soccer stadium. The handoff happens at the stadium lots."),
("The North Ward climbs toward Branch Brook Park, and Forest Hill above the park is big houses on wider streets.","The North Ward climbs toward Branch Brook Park. Forest Hill above the park is big houses on wider streets."),
("Roseville and Mount Pleasant below it are tighter, and the handoff moves to the park lots or Bloomfield Avenue.","Roseville and Mount Pleasant below it are tighter. The handoff moves to the park lots or Bloomfield Avenue."),
("The Oranges, Irvington, and Hillside are older grids with the same answer, and Montclair and Bloomfield have wider streets where the curb sometimes works.","The Oranges, Irvington, and Hillside are older grids with the same answer. Montclair and Bloomfield have wider streets where the curb sometimes works."),
("Newark prices among the best in the Northeast, because every carrier on the 95 lane passes the city and the port keeps more based here.","Newark prices among the best in the Northeast. Every carrier on the 95 lane passes the city, and the port keeps more based here."),
("The auto terminals at the port land hundreds of thousands of imported cars a year, and the dealers’ haulers carry them out.","The auto terminals at the port land hundreds of thousands of imported cars a year. The dealers’ haulers carry them out."),
("Give us the release date and the terminal, and the ocean leg is booked separately if you ever need one.","Give us the release date and the terminal. The ocean leg is booked separately if you ever need one."),
("The airport is a hub for one of the big airlines, and its crews and contractors relocate on bid dates all year.","The airport is a hub for one of the big airlines. Its crews and contractors relocate on bid dates all year."),
("The insurer on Broad Street, the utility beside it, the audiobook company at Washington Park, and the electronics company by the station relocate staff on offer dates.","The insurer on Broad Street and the utility beside it relocate staff on offer dates. So do the audiobook company at Washington Park and the electronics company by the station."),
("Families priced out of the city across the river buy in Forest Hill, the Oranges, and Montclair on closing dates.","Families priced out of the city across the river buy in Forest Hill, the Oranges, and Montclair."),
("Service members headed to the joint base in Burlington County ship through here too, and Ship Guy has no tie to it.","Service members headed to the joint base in Burlington County ship through here too. Ship Guy has no tie to it."),
("The cherry blossoms fill Branch Brook Park for two weeks in April, and the park roads close for the festival weekend.","The cherry blossoms fill Branch Brook Park for two weeks in April. The park roads close for the festival weekend."),
("The arena downtown fills the garages on hockey nights from October through April and on concert nights all year.","The arena downtown fills the garages on hockey nights from October through April. Concert nights do the same all year."),
("Sandy in 2012 put the surge over the port and the Ironbound and destroyed thousands of new cars on the docks.","Sandy in 2012 put the surge over the port and the Ironbound. Thousands of new cars on the docks were destroyed."),
("Carriers leave the port district before a landfall, and a pickup on the flats moves uphill until the water drops.","Carriers leave the port district before a landfall. A pickup on the flats moves uphill until the water drops."),
("The collectors in Forest Hill and Montclair book one, and so do the executives relocating a new car to the towers.","The collectors in Forest Hill and Montclair book one. So do the executives relocating a new car to the towers."),
("Tell us the release date and the terminal, and the ocean leg is booked separately if you need one.","Tell us the release date and the terminal. The ocean leg is booked separately if you need one."),
("A carrier that uses the Turnpike, 78, or a Hudson crossing pays by transponder, and the toll rides inside the quote.","A carrier that uses the Turnpike, 78, or a Hudson crossing pays by transponder. The toll rides inside the quote."),
])

fix('build_lascruces_local.py', [
("Car shipping in Las Cruces runs on the two interstates that meet on the west side of town and the El Paso carrier pool.","Car shipping in Las Cruces runs on the two interstates that meet west of town and the El Paso carrier pool."),
("We book vetted carriers across Doña Ana County, from Mesilla and the valley farms to the East Mesa, Picacho Hills, and the border towns.","We book vetted carriers across Doña Ana County, from Mesilla and the valley to the East Mesa and the border towns."),
("US 70 climbs over the pass to the missile range and Alamogordo, and Lohman Avenue is the spine of the east side.","US 70 climbs over the pass to the missile range and Alamogordo. Lohman Avenue is the spine of the east side."),
("This page covers 10, 25, the pass, the checkpoints, downtown, Mesilla, the valley, the East Mesa, and the border towns.","This page covers 10, 25, the pass, the checkpoints, downtown, Mesilla, the East Mesa, and the border towns."),
("It also covers the university, the missile range, the hospitals, the pecans and the chile, the spring wind, and the lanes.","It also covers the university, the missile range, the hospitals, the farms, the spring wind, and the lanes."),
("Las Cruces is the last big town before the desert in three directions, and the carriers plan their fuel around it.","Las Cruces is the last big town before the desert in three directions. The carriers plan their fuel around it."),
("The two share the rebuilt interchange on the west side, and the carriers come off it onto Avenida de Mesilla or Valley Drive.","The two share the rebuilt interchange on the west side. The carriers come off it onto Avenida de Mesilla or Valley Drive."),
("US 70 leaves the east side as Bataan Memorial Highway and climbs San Augustin Pass through the Organ Mountains.","US 70 leaves the east side as Bataan Memorial Highway. It climbs San Augustin Pass through the Organ Mountains."),
("The 10 checkpoint sits west of the city, the 25 checkpoint sits north of it, and the 70 checkpoint sits on the pass.","The 10 checkpoint sits west of the city and the 25 checkpoint north of it. The 70 checkpoint sits on the pass."),
("The big-box lots at Lohman and Walton, the centers on the East Mesa, and the arena lots on the campus work too.","The big-box lots at Lohman and Walton and the centers on the East Mesa work too. So do the arena lots on the campus."),
("The East Mesa from Lohman up to the mountains is the newest half of the city, subdivisions on wide streets.","The East Mesa from Lohman up to the mountains is the newest half of the city. It is subdivisions on wide streets."),
("Picacho Hills across the river sits on the golf course with big lots, and the driver reaches the driveway.","Picacho Hills across the river sits on the golf course with big lots. The driver reaches the driveway."),
("The valley south along Highway 28 is pecan orchards, chile fields, and dairies, and the handoff happens on the highway.","The valley south along Highway 28 is pecan orchards, chile fields, and dairies. The handoff happens on the highway."),
("Doña Ana, Radium Springs, and Hatch sit up the valley on 25, and the chile town prices the same as the city.","Doña Ana, Radium Springs, and Hatch sit up the valley on 25. The chile town prices the same as the city."),
("Las Cruces prices with El Paso on every lane, because the carriers are the same trucks forty minutes south.","Las Cruces prices with El Paso on every lane. The carriers are the same trucks forty minutes south."),
("The university is the state’s land-grant campus, and it takes cars each August and sends them home each May.","The university is the state’s land-grant campus. It takes cars each August and sends them home each May."),
("The missile range over the pass is the largest employer in the county, with soldiers, civilians, and contractors by the thousand.","The missile range over the pass is the largest employer in the county. It holds soldiers, civilians, and contractors by the thousand."),
("Retirees arrive from the Midwest and the coasts for the sun and the prices, and they ship the car ahead of the moving truck.","Retirees arrive from the Midwest and the coasts for the sun and the prices. They ship the car ahead of the moving truck."),
("The chile harvest fills Hatch for the festival on Labor Day weekend, and 25 backs up at the exit.","The chile harvest fills Hatch for the festival on Labor Day weekend. The 25 exit backs up."),
("The day of the dead fills the Mesilla plaza in early November, and the arts fair fills the park the same week.","The day of the dead fills the Mesilla plaza in early November. The arts fair fills the park the same week."),
("The pileups near Deming and Lordsburg have killed people, and the state shuts the road when the visibility drops.","The pileups near Deming and Lordsburg have killed people. The state shuts the road when the visibility drops."),
("The monsoon runs from July through September, and an afternoon storm floods the arroyos and the underpasses in an hour.","The monsoon runs from July through September. An afternoon storm floods the arroyos and the underpasses in an hour."),
("At pickup the driver and you inspect the car together, and the Bill of Lading records every existing mark.","At pickup the driver and you inspect the car together. The Bill of Lading records every existing mark."),
("The range over the pass rotates soldiers on orders all year, and Fort Bliss families live across the county.","The range over the pass rotates soldiers on orders all year. Fort Bliss families live across the county."),
("The spring wind closes 10 west of town a few afternoons each year, and the pileups near Deming are the reason.","The spring wind closes 10 west of town a few afternoons each year. The pileups near Deming are the reason."),
])

# ---- residual pass
fix('build_warwick_local.py', [
("This page covers 95, 295, Route 2, Route 117, the airport, the bay villages, and the hills to the west.","This page covers 95, 295, Route 2, Route 117, the airport, the bay villages, and the western hills."),
])
fix('build_stpaul_local.py', [
("This page covers 94, 35E, the ring, the truck ban, downtown, Summit Hill, the Midway, Highland, and the suburbs.","This page covers 94, 35E, the ring, the truck ban, downtown, Summit Hill, the Midway, and the suburbs."),
])
fix('build_jackson_local.py', [
("It also covers the state workforce, the medical center, the plant, the campuses, the fair, the tornadoes, and the lanes.","It also covers the state workforce, the medical center, the plant, the campuses, the tornadoes, and the lanes."),
])
fix('build_omaha_local.py', [
("It also covers the headquarters, the base, the medical center, the College World Series, the floods, and the lanes.","It also covers the headquarters, the base, the medical center, the World Series, the floods, and the lanes."),
])
fix('build_newark_local.py', [
("Car shipping in Newark starts at one of the busiest interchanges in the country and ends in the Ironbound.","Car shipping in Newark starts at one of the busiest interchanges in the country."),
("We book vetted carriers across Essex County and the port towns, from the North Ward to Weequahic and the Oranges.","We book vetted carriers across Essex County and the port towns, from the North Ward to the Oranges."),
("This page covers the Turnpike, 78, 280, Route 21, downtown, the Ironbound, the North Ward, the wards, and the suburbs.","This page covers the Turnpike, 78, 280, Route 21, downtown, the Ironbound, the wards, and the suburbs."),
("It also covers the port, the airport, the headquarters, the campuses, the cherry blossoms, the storms, and the lanes.","It also covers the port, the airport, the headquarters, the campuses, the blossoms, the storms, and the lanes."),
("'ferry street','row houses'","'ferry street','row-house'"),
])
fix('build_lascruces_local.py', [
("Car shipping in Las Cruces runs on the two interstates that meet west of town and the El Paso carrier pool.","Car shipping in Las Cruces runs on the two interstates that meet west of town."),
("We book vetted carriers across Doña Ana County, from Mesilla and the valley to the East Mesa and the border towns.","We book vetted carriers across Doña Ana County, from Mesilla to the East Mesa and the border towns."),
("'pecans','chile'","'pecan','chile'"),
])
