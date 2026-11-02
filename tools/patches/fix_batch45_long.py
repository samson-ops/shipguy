"""Batch 45 long-sentence splits (>18 words), applied to the builders."""
D='/home/claude/tools/builders_city/'
def fix(fn, pairs):
    p=D+fn; s=open(p,encoding='utf-8').read()
    if pairs and all(s.count(o[0])==0 for o in pairs): print(fn,'already applied'); return
    for item in pairs:
        old,new=item[0],item[1]; k=item[2] if len(item)>2 else 1
        c=s.count(old); assert c==k, (fn, c, old[:70])
        s=s.replace(old,new)
    open(p,'w',encoding='utf-8').write(s); print(fn, len(pairs), 'fixes')

fix('build_bellevue_local.py', [
('The Interstate 5 carriers reach the Eastside on 405 every day, and the 90 carriers cross the mountains to Spokane.','The Interstate 5 carriers reach the Eastside on 405 every day. The 90 carriers cross the mountains to Spokane.'),
('Both bridges close for a weekend now and then for work, and the driver knows it before you do.','Both bridges close for a weekend now and then for work. The driver knows it before you do.'),
('The carriers meet you at the South Bellevue park-and-ride at Bellevue Way and 90, the Eastgate lots, or the Factoria lots.','The carriers meet you at the South Bellevue park-and-ride, the Eastgate lots, or the Factoria lots.'),
('Our office is on 116th Avenue Northeast, east of 405 and south of 520, a few blocks from the hospital.','Our office is on 116th Avenue Northeast, east of 405, a few blocks from the hospital.',2),
('Medina, Clyde Hill, Hunts Point, and Yarrow Point along the lake are the Gold Coast, narrow lanes behind gates and hedges.','Medina, Clyde Hill, Hunts Point, and Yarrow Point along the lake are the Gold Coast. The lanes are narrow and run behind gates and hedges.'),
('Redmond and the software campus, Kirkland along the lake, and Issaquah and Sammamish up the hill price the same as Bellevue.','Redmond, Kirkland, Issaquah, and Sammamish price the same as Bellevue.'),
('The wireless carrier headquartered in Factoria, the truck maker on 106th, and the utility relocate staff on offer dates.','The wireless carrier in Factoria, the truck maker on 106th, and the utility relocate staff on offer dates.'),
('The aerospace plant in Renton moves engineers on program dates, and the game studios in Bellevue and Redmond hire on project cycles.','The aerospace plant in Renton moves engineers on program dates. The game studios in Bellevue and Redmond hire on project cycles.'),
('The college on Landerholm Circle takes student cars each September, and the university across the lake does the same a week later.','The college on Landerholm Circle takes student cars each September. The university across the lake does the same a week later.'),
('The joint base south of Tacoma and the naval station in Everett send families to the Eastside on orders.','The joint base near Tacoma and the naval station in Everett send families to the Eastside on orders.'),
('The second one ships with us, and Ship Guy is a private broker with no connection to either base.','The second one ships with us. Ship Guy is a private broker with no connection to either base.'),
('Snowflake Lane closes a lane of Bellevue Way every evening from late November through Christmas Eve for the parade.','Snowflake Lane closes a lane of Bellevue Way every evening from late November through Christmas Eve.'),
('The 2006 storm put the Eastside in the dark for a week and dropped firs across every hill road.','The 2006 storm put the Eastside in the dark for a week and dropped firs on every hill road.'),
('The smoke in September 2020 sat over the lake for ten days and shifted nothing but the loading hour.','The smoke in September 2020 sat over the lake for ten days and shifted only the loading hour.'),
('The collectors in Medina and Hunts Point book one, and so do the engineers relocating a new electric car from California.','The collectors in Medina and Hunts Point book one. So do the engineers bringing a new electric car up from California.'),
('A loaded trailer takes 90 across the lake for free unless the pickup or delivery sits on the 520 side.','A loaded trailer takes 90 across the lake for free unless the address sits on the 520 side.'),
])
fix('build_bellevue_local.py', [
('The 2006 storm put the Eastside in the dark for a week and dropped firs on every hill road.','The 2006 storm put the Eastside in the dark for a week and dropped firs on the hill roads.'),
])
fix('build_bellevue_local.py', [
('The 2006 storm put the Eastside in the dark for a week and dropped firs on the hill roads.','The 2006 storm put the Eastside in the dark for a week. Firs came down on every hill road.'),
])

fix('build_bloomington_local.py', [
('Car shipping in Bloomington runs on Interstate 494, the strip the whole south metro drives to reach the airport.','Car shipping in Bloomington runs on Interstate 494, the strip the south metro drives to reach the airport.'),
('We book vetted carriers across Bloomington and the south metro, from Normandale to the mall and across the river.','We book vetted carriers across Bloomington and the south metro, from Normandale to the mall and the river.'),
('It also covers the health plan, the mower maker, the airline crews, the parking ban, the holiday crush, and the lanes.','It also covers the headquarters, the airline crews, the parking ban, the holiday crush, and the lanes.'),
('The Chicago and Fargo carriers ride 494 around the metro every day, and the Iowa trucks come up 35W.','The Chicago and Fargo carriers ride 494 around the metro every day. The Iowa trucks come up 35W.'),
('It runs from the airport past the mall, the Penn and France hotels, and the Normandale towers to Eden Prairie.','It runs from the airport past the mall, the hotels, and the Normandale towers to Eden Prairie.'),
('The Southtown lots at Penn and 494, the Oxboro lots at Lyndale and 98th, and the big-box lots on American Boulevard work every day.','The Southtown lots at Penn and 494 and the Oxboro lots at Lyndale and 98th work every day. So do the big-box lots on American Boulevard.'),
('The bluffs along the river from Bloomington Ferry to Old Cedar are steep streets and dead ends above the refuge.','The bluffs from Bloomington Ferry to Old Cedar are steep streets and dead ends above the refuge.'),
('A move timed to the holiday rush at the mall or a January start date lands in a busy week.','A move timed to the holiday rush or a January start date lands in a busy week.'),
('Pilots, crews, and mechanics relocate on bid dates all year, and the handoff happens in Bloomington rather than at the terminal.','Pilots, crews, and mechanics relocate on bid dates all year. The handoff happens in Bloomington rather than at the terminal.'),
('Two Guard wings fly out of the airport, and the reserve units at Fort Snelling rotate staff on orders.','Two Guard wings fly out of the airport. The reserve units at Fort Snelling rotate staff on orders.'),
('The mall fills from Black Friday to New Year’s, and Cedar, Killebrew, and the 494 ramps crawl every weekend of December.','The mall fills from Black Friday to New Year’s. Cedar, Killebrew, and the 494 ramps crawl every weekend of December.'),
('The Summer Fete fills Normandale Lake Park on the third of July, and the fireworks close Normandale Boulevard for the night.','The Summer Fete fills Normandale Lake Park on the third of July. The fireworks close Normandale Boulevard for the night.'),
('The bottoms below the bluffs go under, and the crossings to Shakopee and Savage on 101 close for weeks.','The bottoms below the bluffs go under. The crossings to Shakopee and Savage on 101 close for weeks.'),
('The health plan, the mower maker, the filter maker, and the fab relocate staff on start dates all year.','The health plan, the mower maker, the filter maker, and the fab relocate staff all year.'),
('The city bans street parking after a snowfall until the plow has been through, and a car on the street gets towed.','The city bans street parking after a snowfall until the plow has been through. A car left out gets towed.'),
])

fix('build_greatfalls_local.py', [
('We arrange vetted carriers across Great Falls and the Golden Triangle, from the Lower North Side to Malmstrom and Vaughn.','We arrange vetted carriers across Great Falls and the Golden Triangle, from the North Side to Malmstrom and Vaughn.'),
('Interstate 15 passes the west side of the city on its way from Helena to Shelby and the border.','Interstate 15 passes the west side of the city between Helena and Shelby.'),
('It also covers the hospital, the refinery, the Guard wing, the fair, the wind, the canyon closures, and the lanes.','It also covers the hospital, the refinery, the Guard wing, the fair, the wind, and the canyon closures.'),
('Montana is a pass-through market, and a carrier on 15 or 90 adds a Great Falls stop when the load lines up.','Montana is a pass-through market. A carrier on 15 or 90 adds a Great Falls stop when the load lines up.'),
('The Lower North Side, downtown, and the base housing meet the truck at a lot or outside the gate.','The Lower North Side, downtown, and the base housing meet the truck at a lot or the gate.'),
('It comes up from Helena through Wolf Creek Canyon, passes the airport on Gore Hill, and leaves north for Conrad, Shelby, and the border.','It comes up from Helena through Wolf Creek Canyon and passes the airport on Gore Hill. It leaves north for Conrad, Shelby, and the border.'),
('Central Avenue runs through downtown, and the river bridges on Central, Ninth Street, and Fifteenth Street tie the West Side and Black Eagle to the rest.','Central Avenue runs through downtown. The river bridges on Central, Ninth Street, and Fifteenth Street tie the West Side and Black Eagle to the rest.'),
('Great Falls is a railroad and smelter town laid out in a grid, with the base on one edge and the river through the middle.','Great Falls is a railroad and smelter town laid out in a grid. The base sits on one edge and the river runs through the middle.'),
('Downtown runs along Central Avenue from the river to the tracks, brick blocks with angled parking and alleys behind.','Downtown runs along Central Avenue from the river to the tracks, brick blocks with angled parking.'),
('The West Side across the river climbs toward the airport, wide streets and postwar houses where the curb works.','The West Side across the river climbs toward the airport, wide streets where the curb works.'),
('The East Side from the fairgrounds out to Fifty-Seventh Street is the biggest grid in the city, ranch houses on wide streets.','The East Side from the fairgrounds out to Fifty-Seventh Street is the biggest grid in the city. Ranch houses sit on wide streets.'),
('The base housing beyond the gate is off limits to a carrier, and the handoff happens at the gate or on Tenth Avenue.','The base housing beyond the gate is off limits to a carrier. The handoff happens at the gate or on Tenth Avenue.'),
('Black Eagle across the river to the north is the old smelter town, small houses on a hillside grid.','Black Eagle across the river is the old smelter town, small houses on a hillside grid.'),
('Sand Coulee and Stockett down the coulee are old mining towns at the end of a county road, and the handoff is at the highway.','Sand Coulee and Stockett down the coulee are old mining towns at the end of a county road. The handoff is at the highway.'),
('Vaughn and Sun River to the west, Cascade and Ulm down 15, and Belt out 87 ship with the same trucks.','Vaughn and Sun River to the west and Cascade and Ulm down 15 ship with the same trucks. So does Belt out 87.'),
('Conrad, Shelby, and the Hi-Line towns run 5 to 10 days, because a carrier leaves 15 for them only with a full load.','Conrad, Shelby, and the Hi-Line towns run 5 to 10 days. A carrier leaves 15 for them only with a full load.'),
('On a pass-through corridor the week of dates you give and the trucks crossing that week set the real quote.','On a pass-through corridor your week of dates and the trucks crossing that week set the real quote.'),
('Great Falls prices like a stop on the 15 corridor with a detour from 90, because that is how the carriers see it.','Great Falls prices like a stop on 15 with a detour from 90, because that is how the carriers see it.'),
('The missile wing at the base on the east edge rotates airmen and officers on orders all year, with a summer peak.','The missile wing at the base rotates airmen and officers on orders all year, with a summer peak.'),
('The refinery by the river and the malt plant on the east side move engineers and managers on contract dates.','The refinery by the river and the malt plant move engineers and managers on contract dates.'),
('The ranches and the grain elevators move a few managers each season, and the handoff is at the highway.','The ranches and the grain elevators move a few managers each season. The handoff is at the highway.'),
('A Chinook in January can lift the temperature fifty degrees in a day, and a gust on Tenth Avenue can rock a loaded trailer.','A Chinook in January can lift the temperature fifty degrees in a day. A gust on Tenth Avenue can rock a loaded trailer.'),
('Wolf Creek Canyon on 15 closes for ice and rockslides a few times a season, and the carriers wait in Helena.','Wolf Creek Canyon on 15 closes for ice and rockslides a few times a season. The carriers wait in Helena.'),
('An enclosed trailer keeps off the gravel of the canyon, the summer hail, and the salt the state spreads on 15.','An enclosed trailer keeps off the gravel of the canyon, the summer hail, and the salt on 15.'),
('The collectors on the Lower North Side and the officers moving a new car to the base book one.','The collectors on the North Side and the officers moving a new car to the base book one.'),
('At pickup the driver goes around the car with you and logs every mark on the Bill of Lading.','At pickup the driver goes around the car with you and logs each mark on the Bill of Lading.'),
('We know which carriers come up 15 and over from 90 each week, and when the canyon is closed.','We know which carriers come up 15 and over from 90 each week, and when the canyon closes.'),
('The refinery and the malt plant move engineers on contract dates, and the Guard wing rotates crews on orders.','The refinery and the malt plant move engineers on contract dates. The Guard wing rotates crews on orders.'),
('A westbound car can also ride 200 over Rogers Pass when the pass is open and the canyon is not.','A westbound car can ride 200 over Rogers Pass when the pass is open and the canyon is not.'),
('The fair jams the fairgrounds blocks for ten days at the end of July, and a handoff there moves to the week after.','The fair jams the fairgrounds blocks for ten days at the end of July. A handoff there moves to the week after.'),
('Give us the neighborhood and a week of dates, and we catch the next carrier on 15 or over from 90.','Give us the neighborhood and a week of dates, and we catch the next carrier on 15 or 90.'),
])
fix('build_greatfalls_local.py', [
('We arrange vetted carriers across Great Falls and the Golden Triangle, from the North Side to Malmstrom and Vaughn.','We arrange vetted carriers across Great Falls and the Golden Triangle, from downtown to Malmstrom and Vaughn.'),
('The river bridges on Central, Ninth Street, and Fifteenth Street tie the West Side and Black Eagle to the rest.','The bridges on Central, Ninth Street, and Fifteenth Street tie the West Side and Black Eagle to the rest.'),
('Great Falls prices like a stop on 15 with a detour from 90, because that is how the carriers see it.','Great Falls prices like a stop on 15 with a detour from 90. That is how the carriers see it.'),
('At pickup the driver goes around the car with you and logs each mark on the Bill of Lading.','At pickup the driver walks around the car with you and logs each mark on the sheet.'),
('A westbound car can ride 200 over Rogers Pass when the pass is open and the canyon is not.','A westbound car can ride 200 over Rogers Pass when the canyon is shut and the pass is not.'),
('Give us the neighborhood and a week of dates, and we catch the next carrier on 15 or 90.','Give us the neighborhood and a week of dates, and we catch the next carrier through.'),
])
fix('build_greatfalls_local.py', [
('The bridges on Central, Ninth Street, and Fifteenth Street tie the West Side and Black Eagle to the rest.','The bridges on Central, Ninth Street, and Fifteenth Street tie the West Side and Black Eagle in.'),
('A westbound car can ride 200 over Rogers Pass when the canyon is shut and the pass is not.','A westbound car can ride 200 over Rogers Pass while the canyon is shut.'),
])

fix('build_santafe_local.py', [
('Ship Guy is a licensed auto transport broker with an office on East Palace Avenue, a block from the Plaza.','Ship Guy is a licensed auto transport broker with an office on East Palace Avenue by the Plaza.'),
('We book vetted carriers across Santa Fe and the north, from the East Side to Eldorado and Los Alamos.','We book vetted carriers across Santa Fe and the north, from Canyon Road to Eldorado and Los Alamos.'),
('US 84 and 285 run through the city as St. Francis Drive and leave north for Española and Taos.','US 84 and 285 cross the city as St. Francis Drive and leave north for Española and Taos.'),
('This page covers 25, La Bajada, St. Francis, Cerrillos, the Plaza, the East Side, the Southside, and the villages.','This page covers 25, La Bajada, St. Francis, Cerrillos, the Plaza, the East Side, and the villages.'),
('It also covers the state, the lab, the hospitals, the opera, the markets, the snow, the monsoon, and the lanes.','It also covers the state, the lab, the hospitals, the opera, the markets, the snow, and the monsoon.'),
('From Albuquerque it climbs La Bajada, a long grade that ices in January, and passes the city on the south.','From Albuquerque it climbs La Bajada, a long grade that ices in January. It passes the city on the south.'),
('US 84 and 285 run through the city as St. Francis Drive, the only road built for trucks inside the limits.','US 84 and 285 cross the city as St. Francis Drive, the one road inside the limits built for trucks.'),
('The outlet lots by the interstate, the big-box lots on Cerrillos, and the Railyard lots at the edge of downtown work too.','The outlet lots by the interstate and the big-box lots on Cerrillos work too. So do the Railyard lots at the edge of downtown.'),
('The East Side along Canyon Road and Acequia Madre is tighter still, galleries and old houses behind adobe walls.','The East Side along Canyon Road and Acequia Madre is tighter still, galleries and houses behind adobe walls.'),
('The South Capitol around Don Gaspar is older houses on short blocks, and the driver meets you on St. Francis.','The South Capitol around Don Gaspar is older houses on short blocks. The driver meets you on St. Francis.'),
('Tesuque in the valley to the north is narrow lanes along the creek, and the truck waits on the highway.','Tesuque in the valley to the north is narrow lanes along the creek. The truck waits on the highway.'),
('Eldorado fifteen miles southeast is cul-de-sacs on dirt roads under a homeowners association, and the handoff is at the shopping center.','Eldorado fifteen miles southeast is cul-de-sacs on dirt roads under a homeowners association. The handoff is at the shopping center.'),
('Los Alamos on the hill, Española in the valley, and the pueblos along 285 ship with the same trucks.','Los Alamos on the hill, Española, and the pueblos along 285 ship with the same trucks.'),
('Santa Fe prices a shade above Albuquerque on every lane, because the carriers climb an hour to reach it.','Santa Fe prices a shade above Albuquerque on every lane. The carriers climb an hour to reach it.'),
('The lab on the hill in Los Alamos hires physicists and engineers from across the country on project dates.','The lab in Los Alamos hires physicists and engineers from across the country on project dates.'),
('The hospital on St. Michael’s and the medical center on the Southside hire traveling nurses year round and bring residents each June.','The hospital on St. Michael’s and the medical center on the Southside hire traveling nurses year round. Residents arrive each June.'),
('The base in Albuquerque sends airmen north on orders, and Ship Guy is a private broker with no connection to it.','The base in Albuquerque sends airmen north on orders. Ship Guy is a private broker with no connection to it.'),
('Fiesta fills downtown in early September, and the burning at Fort Marcy Park closes the north side for a night.','Fiesta fills downtown in early September. The burning at Fort Marcy Park closes the north side for a night.'),
('The balloon fiesta in Albuquerque fills Santa Fe’s hotels for nine days in October, and the 25 traffic doubles.','The balloon fiesta in Albuquerque fills Santa Fe’s hotels for nine days in October. The 25 traffic doubles.'),
('In 2022 the Hermits Peak fire burned east of town for two months, and the smoke sat on the city for weeks.','In 2022 the Hermits Peak fire burned east of town for two months. The smoke sat on the city for weeks.'),
('An enclosed trailer keeps off the dust, the cinders on the grade, and the sun that cracks a dashboard at this altitude.','An enclosed trailer keeps off the dust, the cinders on the grade, and the high-altitude sun.'),
('Phoenix runs four hundred to five hundred seventy, about four hundred eighty miles by way of 40 and 17.','Phoenix runs four hundred to five hundred seventy, about four hundred eighty miles out 40 and 17.'),
('The college on the hill takes cars each September, and the community college and the arts institute take them in August.','The college on the hill takes cars each September. The community college and the arts institute take them in August.'),
])
fix('build_santafe_local.py', [
('US 84 and 285 cross the city as St. Francis Drive, the one road inside the limits built for trucks.','US 84 and 285 cross the city as St. Francis Drive, the one in-town road built for trucks.'),
])

fix('build_bismarck_local.py', [
('We book vetted carriers across Bismarck and Mandan, from the Cathedral District to the north subdivisions and across the river.','We book vetted carriers across Bismarck and Mandan, from the Cathedral District to the north subdivisions.'),
('Interstate 94 runs along the north side of the city and crosses the river to Mandan on the Grant Marsh Bridge.','Interstate 94 runs along the north side of the city and crosses the river to Mandan.'),
('This page covers 94, 83, the Expressway, the bridges, downtown, the Cathedral District, the north, and the river blocks.','This page covers 94, 83, the Expressway, downtown, the Cathedral District, the north, and the river blocks.'),
('It also covers the Capitol, the hospitals, the energy companies, the loader plant, the refinery, the gates, the floods, and the lanes.','It also covers the Capitol, the hospitals, the energy companies, the plants, the gates, and the floods.'),
('North Dakota is a pass-through market, and a carrier on 94 adds a Bismarck stop when the load lines up.','North Dakota is a pass-through market. A carrier on 94 adds a Bismarck stop when the load lines up.'),
('It enters from Jamestown and Fargo, runs along the north side past the airport exit and State Street, and crosses the river to Mandan.','It enters from Jamestown and Fargo and runs along the north side past State Street. Then it crosses the river to Mandan.'),
('The state drops the gates on 94 at the city limits in a blizzard, and nothing moves until they lift.','The state drops the gates on 94 at the city limits in a blizzard. Nothing moves until they lift.'),
('It climbs past the Capitol to Century Avenue and 43rd Avenue and leaves for Washburn, the coal plants, and Minot.','It climbs past the Capitol to Century Avenue and 43rd and leaves for Washburn and Minot.'),
('The big-box lots on State Street, the Capitol lots on a weekend, and the fairgrounds lots in Mandan work too.','The big-box lots on State Street and the Capitol lots on a weekend work too. So do the fairgrounds lots in Mandan.'),
('Downtown runs along Main Avenue and Fourth Street, brick blocks with angled parking and the old depot at the east end.','Downtown runs along Main Avenue and Fourth Street, brick blocks with angled parking. The old depot anchors the east end.'),
('The Cathedral District climbs from downtown toward the Capitol, the oldest houses in the city on narrow streets under elms.','The Cathedral District climbs from downtown toward the Capitol. The oldest houses in the city sit on narrow streets under elms.'),
('The agencies transfer staff on start dates all year, and the legislature brings a crowd to town each odd January.','The agencies transfer staff on start dates all year. The legislature brings a crowd to town each odd January.'),
('The two hospitals, one on the north side and one by the Capitol, hire traveling nurses year round and bring residents each June.','The two hospitals, one on the north side and one by the Capitol, hire traveling nurses year round. Residents arrive each June.'),
('The college on Schafer Street takes student cars in late August, and the university on the bluffs does the same.','The college on Schafer Street takes student cars in late August. The university on the bluffs does the same.'),
('The Guard headquarters at Fraine Barracks rotates staff on orders, and the Air Force base in Minot sends families south on orders.','The Guard headquarters at Fraine Barracks rotates staff on orders. The Air Force base in Minot sends families south the same way.'),
('Oil workers ship pickups to and from the Bakken on the hiring cycle, and Bismarck is where many of them live.','Oil workers ship pickups to and from the Bakken on the hiring cycle. Many of them live in Bismarck.'),
('The street fair closes downtown for a weekend the same month, and the marathon closes the river roads on a Saturday.','The street fair closes downtown for a weekend the same month. The marathon closes the river roads on a Saturday.'),
('A blizzard on the open prairie closes 94 for a day at a time, and the state drops the gates at the city limits.','A blizzard on the open prairie closes 94 for a day at a time. The state drops the gates at the city limits.'),
('The collectors in the Cathedral District and the executives relocating a new car to the energy headquarters book one.','The collectors in the Cathedral District and the executives bringing a new car to the energy headquarters book one.'),
('At pickup the driver inspects the car with you and writes up its condition on the Bill of Lading.','At pickup the driver inspects the car with you and writes its condition on the Bill of Lading.'),
('The carriers cross on 94 between Minneapolis and Montana, and one adds a Bismarck stop when the load lines up.','The carriers cross on 94 between Minneapolis and Montana. One adds a Bismarck stop when the load lines up.'),
('The state closes 94 at the city limits in a blizzard, and a carrier waits in Fargo or Dickinson.','The state closes 94 at the city limits in a blizzard. A carrier waits in Fargo or Dickinson.'),
('Fox Island, Southport, and Riverwood sit on the flood plain, and the dam releases can put them under in a wet spring.','Fox Island, Southport, and Riverwood sit on the flood plain. The dam releases can put them under in a wet spring.'),
])
fix('build_bismarck_local.py', [
('The collectors in the Cathedral District and the executives bringing a new car to the energy headquarters book one.','The collectors in the Cathedral District book one. So do the executives bringing a new car to the energy headquarters.'),
])

fix('build_eugene_local.py', [
('Car shipping in Eugene rides Interstate 5, the Seattle-to-California road that runs along the east edge of the city.','Car shipping in Eugene rides Interstate 5, the Seattle-to-California road along the east edge of the city.'),
('Interstate 5 runs from Portland and Salem past the east side of the city to Roseburg, Medford, and the Siskiyou Summit.','Interstate 5 runs from Portland and Salem past the east side of the city to Medford and the Siskiyou.'),
('It also covers the university, the hospital, the timber companies, the track meets, the ice storm, the fires, and the lanes.','It also covers the university, the hospital, the mills, the track meets, the ice storm, and the fires.'),
('The Seattle-to-California carriers pass the city on 5 every day, and a car near the interstate rides a truck already making the trip.','The Seattle-to-California carriers pass the city on 5 every day. A car near the interstate rides a truck already making the trip.'),
('It comes down from Portland and Salem past Coburg, passes Springfield and the east side of Eugene, and leaves south for Cottage Grove and Roseburg.','It comes down from Portland and Salem past Coburg and passes the east side of Eugene. It leaves south for Cottage Grove and Roseburg.'),
('The Siskiyou Summit at the California line is two hundred miles down and closes for snow and chains a few times a winter.','The Siskiyou Summit at the California line is two hundred miles down. It closes for snow and chains a few times a winter.'),
('Highway 126 runs west through Veneta to Florence and the coast, and east up the McKenzie to Blue River and the passes.','Highway 126 runs west through Veneta to Florence and the coast. It runs east up the McKenzie to Blue River and the passes.'),
('The Gateway lots in Springfield, the big-box lots on West 11th, and the stadium lots outside the football calendar work too.','The Gateway lots in Springfield and the big-box lots on West 11th work too. So do the stadium lots outside the football calendar.'),
('Downtown runs along the one-way couplets of 6th and 7th and 11th and 13th, with the Park Blocks and the market at the center.','Downtown runs along the one-way couplets of 6th and 7th and 11th and 13th. The Park Blocks and the market sit at the center.'),
('The campus and Fairmount east of downtown are tree-lined blocks packed with student cars from late September to June.','The campus and Fairmount east of downtown are tree-lined blocks packed with student cars most of the year.'),
('South Eugene and College Hill climb from the campus toward Spencer Butte on streets that narrow as they rise.','South Eugene and College Hill climb toward Spencer Butte on streets that narrow as they rise.'),
('Cal Young and Harlow north of the river are postwar grids and newer subdivisions, wide enough for a trailer.','Cal Young and Harlow north of the river are postwar grids and newer subdivisions. A trailer fits.'),
('River Road and Santa Clara to the northwest are old farm roads with wide lots, and the driver reaches the house.','River Road and Santa Clara to the northwest are old farm roads with wide lots. The driver reaches the house.'),
('Eugene prices like Portland with a hundred miles taken off the California side and added to the Seattle side.','Eugene prices like Portland with a hundred miles moved from the California side to the Seattle side.'),
('The running shoe company that started here keeps designers and coaches moving in and out on the track calendar.','The running shoe company born here moves designers and coaches in and out on the track calendar.'),
('The health plan in Springfield and the regional retailer headquartered on the west side relocate staff on offer dates.','The health plan in Springfield and the retailer headquartered on the west side relocate staff on offer dates.'),
('Transplants arrive from California every month for the rain and the trails, and they ship the car behind the moving truck.','Transplants arrive from California every month for the rain and the trails. They ship the car behind the moving truck.'),
('The track meets at Hayward Field fill the campus blocks in late May and June, and the national championships and the trials fill every hotel in the valley.','The track meets at Hayward Field fill the campus blocks in late May and June. The national championships and the trials fill every hotel in the valley.'),
('Half an inch of ice brought down firs and oaks across the city, and the power stayed off for days.','Half an inch of ice brought down firs and oaks across the city. The power stayed off for days.'),
('The Siskiyou closes for chains a few times a winter, and the California car waits a day in Medford.','The Siskiyou closes for chains a few times a winter. The California car waits a day in Medford.'),
('The collectors in the south hills and the coaches relocating a new car on the track calendar book one.','The collectors in the south hills book one. So do the coaches bringing a new car in on the track calendar.'),
('The January 2024 storm brought down firs across the city, and the carriers waited in Salem until the streets were clear.','The January 2024 storm brought down firs across the city. The carriers waited in Salem until the streets were clear.'),
])
fix('build_eugene_local.py', [
('Interstate 5 runs from Portland and Salem past the east side of the city to Medford and the Siskiyou.','Interstate 5 runs from Portland past the east side of the city to Medford and the Siskiyou.'),
])

fix('build_charleston_local.py', [
('Car shipping in Charleston runs on Interstate 26, the Mark Clark loop, and the bridges that tie the peninsula to everything else.','Car shipping in Charleston runs on Interstate 26, the Mark Clark loop, and the bridges off the peninsula.'),
('It also covers the joint base, the port, the aircraft plant, the medical university, the colleges, the hurricanes, the king tides, and the lanes.','It also covers the joint base, the port, the plants, the medical university, the colleges, the hurricanes, and the king tides.'),
('The 95 carriers come over on 26 from Columbia and up 17 from Savannah every day, and the port keeps more based in North Charleston.','The 95 carriers come over on 26 from Columbia and up 17 from Savannah every day. The port keeps more based in North Charleston.'),
('It comes down from Columbia and the Upstate through Summerville, Ladson, and North Charleston and ends at the Crosstown on the peninsula.','It comes down from Columbia through Summerville, Ladson, and North Charleston. It ends at the Crosstown on the peninsula.'),
('It runs from Savannah Highway in West Ashley over the Ashley, past the airport and the aircraft plant, over the Cooper on the Don Holt Bridge, and across Daniel Island to Mount Pleasant.','It runs from Savannah Highway in West Ashley over the Ashley and past the airport. Then it crosses the Cooper on the Don Holt Bridge and Daniel Island to Mount Pleasant.'),
('US 17 is Savannah Highway in West Ashley, the Crosstown across the peninsula, and the Ravenel Bridge to Mount Pleasant.','US 17 is Savannah Highway in West Ashley, the Crosstown on the peninsula, and the Ravenel Bridge.'),
('The carriers come off 26 at Montague or Ashley Phosphate and off 526 at Savannah Highway or Long Point.','The carriers come off 26 at Montague or Ashley Phosphate and off 526 at Savannah Highway.'),
('The outlet lots at 26 and Montague, the Towne Centre lots in Mount Pleasant, and the big-box lots on Rivers Avenue work too.','The outlet lots at 26 and Montague and the Towne Centre lots in Mount Pleasant work too. So do the big-box lots on Rivers Avenue.'),
('Our office is on Gardner Road in West Ashley, by the mall on Sam Rittenberg Boulevard and minutes from 526 and 26.','Our office is on Gardner Road in West Ashley, by the mall on Sam Rittenberg Boulevard.',2),
('West Ashley across the Ashley River is the biggest suburb, from Avondale and Byrnes Downs to Shadowmoss and Carolina Bay.','West Ashley across the river is the biggest suburb, from Avondale and Byrnes Downs to Shadowmoss and Carolina Bay.'),
('Folly Beach at the end of the road is narrow and sandy, and the handoff moves to the Folly Road lots.','Folly Beach at the end of the road is narrow and sandy. The handoff moves to the Folly Road lots.'),
('Kiawah and Seabrook sit behind gates at the end of Bohicket, and the handoff is at the gate or in town.','Kiawah and Seabrook sit behind gates at the end of Bohicket. The handoff is at the gate or in town.'),
('Mount Pleasant across the Cooper is wide and new in Park West, Carolina Park, and Dunes West, where the curb works.','Mount Pleasant across the Cooper is wide and new in Park West, Carolina Park, and Dunes West. The curb works.'),
('The Old Village and the new urbanist blocks of I’On are tight, and the driver meets you on Coleman Boulevard.','The Old Village and the new urbanist blocks of I’On are tight. The driver meets you on Coleman Boulevard.'),
('Sullivan’s Island and the Isle of Palms are beach lanes over the Ben Sawyer swing bridge and the connector.','Sullivan’s Island and the Isle of Palms are beach lanes over the swing bridge and the connector.'),
('North Charleston is Park Circle’s roundabouts, the airport, the plants, and the old Navy base, wide enough almost everywhere.','North Charleston is Park Circle’s roundabouts, the airport, the plants, and the old Navy base. It is wide almost everywhere.'),
('The 95 carriers come over on 26 and 17 every day, and the port keeps a pool of them based in North Charleston.','The 95 carriers come over on 26 and 17 every day. The port keeps a pool of them based in North Charleston.'),
('A PCS report date in July, the August move-in, or a hurricane week lands in the busiest days of the year.','A report date in July, the August move-in, or a hurricane week lands in the busiest days.'),
('The joint base combines the airlift wing at the airport and the weapons station in Goose Creek, with the nuclear school on it.','The joint base combines the airlift wing at the airport and the weapons station in Goose Creek. The nuclear school sits on the station.'),
('The port lands imported cars by the thousand and ships the state’s own cars out by the thousand more.','The port lands imported cars by the thousand and ships the state’s own cars out the same way.'),
('Retirees arrive from the Northeast and the Midwest every month for Mount Pleasant, Daniel Island, and the Summerville subdivisions.','Retirees arrive from the Northeast and the Midwest every month for Mount Pleasant, Daniel Island, and Summerville.'),
('The lights at the county park on James Island jam Riverland Drive every evening from November to New Year’s.','The lights at the county park on James Island jam Riverland Drive every evening through December.'),
('Matthew in 2016, Irma in 2017, and Idalia in 2023 flooded the peninsula and the low blocks of West Ashley.','Matthew in 2016, Irma in 2017, and Idalia in 2023 flooded the peninsula and low West Ashley.'),
('The king tides flood the Crosstown, Lockwood, and the Market on a sunny day a dozen times a year.','The king tides flood the Crosstown, Lockwood, and the Market on sunny days a dozen times a year.'),
('An enclosed trailer keeps off the salt air, the pollen, and the storm debris on 26 after a blow.','An enclosed trailer keeps off the salt air, the pollen, and the debris on 26 after a blow.'),
('A parent books it from home, and an adult meets the truck at a lot off 26 to sign.','A parent books it from home, and an adult meets the truck at a lot to sign.'),
('Kiawah sits behind a gate at the end of Bohicket, and the handoff is at the gate or in town.','Kiawah sits behind a gate at the end of Bohicket. The handoff is at the gate or in town.'),
])
fix('build_charleston_local.py', [
('It also covers the joint base, the port, the plants, the medical university, the colleges, the hurricanes, and the king tides.','It also covers the joint base, the port, the plants, the colleges, the hurricanes, and the king tides.'),
('West Ashley across the river is the biggest suburb, from Avondale and Byrnes Downs to Shadowmoss and Carolina Bay.','West Ashley across the river is the biggest suburb, from Avondale and Byrnes Downs out to Carolina Bay.'),
])

# after the overlap pass
fix('build_bellevue_local.py', [
('Los Angeles is about eleven hundred thirty-five miles down 5 and runs eight hundred to eleven hundred fifty dollars for a sedan.','Los Angeles is eleven hundred thirty-five miles down 5 and runs eight hundred to eleven hundred fifty dollars.'),
])
fix('build_bloomington_local.py', [
('At pickup the driver and you go over the car together, and every mark goes on the Bill of Lading.','At pickup the driver and you go over the car together. Every mark goes on the Bill of Lading.'),
])
fix('build_greatfalls_local.py', [
('The week you can give us and the trucks on 15 and 90 that week set the real quote.','Your week of dates and the trucks on 15 and 90 that week set the real quote.'),
])
