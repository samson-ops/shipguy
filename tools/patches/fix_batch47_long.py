"""Batch 47 long-sentence splits (>18 words), applied to the builders."""
D='/home/claude/tools/builders_city/'
def fix(fn, pairs):
    p=D+fn; s=open(p,encoding='utf-8').read()
    if pairs and all(s.count(o[0])==0 for o in pairs): print(fn,'already applied'); return
    for item in pairs:
        old,new=item[0],item[1]; k=item[2] if len(item)>2 else 1
        c=s.count(old); assert c==k, (fn, c, old[:70])
        s=s.replace(old,new)
    open(p,'w',encoding='utf-8').write(s); print(fn, len(pairs), 'fixes')

fix('build_rochestermn_local.py', [
('The 52 carriers come down from the Twin Cities daily, and the 90 carriers pass between Sioux Falls and Chicago.','The 52 carriers come down from the Twin Cities daily. The 90 carriers pass between Sioux Falls and Chicago.'),
('Highway 52 enters from the north past the old computer campus and runs as a freeway down the west side of downtown.','Highway 52 enters from the north past the old computer campus. It runs as a freeway down the west side of downtown.'),
('Rochester runs on the clinic calendar, and the weather problem is open prairie between the city and everywhere else.','Rochester runs on the clinic calendar. The weather problem is open prairie between the city and everywhere else.'),
('The July changeover brings a new class of residents and sends the old one home in the same week.','The July changeover brings a new class of residents and sends the old one home the same week.'),
('A blizzard closes 52 and 90 a few times each winter, because there is nothing to stop the wind.','A blizzard closes 52 and 90 a few times each winter. There is nothing to stop the wind.'),
('The August 2007 rain flooded the river towns east of the city and closed 14 near Winona for days.','The August 2007 rain flooded the river towns east of the city. It closed 14 near Winona for days.'),
('Residents and fellows arrive in late June for the July start, and that is the busiest week on our calendar.','Residents and fellows arrive in late June for the July start. That is the busiest week on our calendar.'),
('The blocks around the clinic have been under construction for a decade, and the lane closures move every month.','The blocks around the clinic have been under construction for a decade. The lane closures move every month.'),
('The handoff happens at the civic center lots or the mall at 52 and 14, and the driver never enters the work zone.','The handoff happens at the civic center lots or the mall at 52 and 14. The driver never enters the work zone.'),
])

fix('build_gulfport_local.py', [
('The 10 carriers pass between Jacksonville and Houston every day, and the 49 carriers link the coast to Jackson.','The 10 carriers pass between Jacksonville and Houston every day. The 49 carriers link the coast to Jackson.'),
('Long Beach and Pass Christian west on the beach ship with the same trucks and price the same as Gulfport.','Long Beach and Pass Christian ship with the same trucks and price the same as Gulfport.'),
('A report date at the base in June or the October car week lands in the busiest weeks of the year.','A June report date at the base or the October car week lands in the busiest weeks.'),
('Winter residents arrive in January from Canada and the Midwest and fill the parks and the condos until March.','Winter residents arrive in January from Canada and the Midwest. They fill the parks and the condos until March.'),
('The car week in early October brings thousands of classic cars to 90 from Pass Christian to Ocean Springs.','The car week in early October brings thousands of classic cars to 90 along the whole coast.'),
('Instructors and permanent party rotate on orders, and students on class cycles ship a car for a long course.','Instructors and permanent party rotate on orders. Students on class cycles ship a car for a long course.'),
('Thousands of classic cars fill 90 for a week in early October, and every enclosed trailer on the Gulf is booked for the event.','Thousands of classic cars fill 90 for a week in early October. Every enclosed trailer on the Gulf is booked for the event.'),
('The community college on Switzer Road takes cars in late August, and the campus on the beach in Long Beach follows the same week.','The community college on Switzer Road takes cars in late August. The campus on the beach in Long Beach follows the same week.'),
])

fix('build_billings_local.py', [
('Car shipping in Billings runs on Interstate 90 and 94, which meet at the east edge of the city.','Car shipping in Billings runs on Interstate 90 and 94, which meet at the east edge of town.'),
('Interstate 90 runs along the south side of the city with the Shiloh, King Avenue, 27th Street, and Lockwood exits.','Interstate 90 runs along the south side with the Shiloh, King Avenue, 27th Street, and Lockwood exits.'),
('Billings is the only Montana city where two interstates meet, and the Rims decide how a truck gets anywhere else.','Billings is the only Montana city where two interstates meet. The Rims decide how a truck gets anywhere else.'),
('West on 90 the road climbs to Bozeman in a hundred forty miles and Missoula in three hundred forty.','Bozeman is a hundred forty miles west on 90, and Missoula is three hundred forty.'),
('Billings is an old grid below the Rims, a boom of subdivisions to the west, and a second city on the plateau.','Billings is an old grid below the Rims and a boom of subdivisions to the west. The Heights is a second city on the plateau above.'),
('Downtown runs from the tracks north to the hospitals, towers and one-way streets around the tallest building in the state.','Downtown runs from the tracks north to the hospitals. It is towers and one-way streets around the tallest building in the state.'),
('The North Side between downtown and the Rims is the old neighborhood, narrow streets of brick houses around Pioneer Park.','The North Side between downtown and the Rims is the old neighborhood. The streets around Pioneer Park are narrow and lined with brick houses.'),
('The West End off Shiloh Road is the newest part of the city, and the subdivisions outrun the maps every year.','The West End off Shiloh Road is the newest part of the city. The subdivisions outrun the maps every year.'),
('The South Side across the tracks is the oldest grid, small houses on narrow streets near the beet plant and the refinery.','The South Side across the tracks is the oldest grid. It is small houses on narrow streets near the beet plant and the refinery.'),
('The beet plant on the south side runs a campaign from October into February and staffs up for it.','The beet plant on the south side runs its campaign from October into February and hires for it.'),
('Billings runs on a fair calendar and a hospital calendar, and the weather problem is a winter that arrives in October and leaves in May.','Billings runs on a fair calendar and a hospital calendar. The weather problem is a winter that arrives in October and leaves in May.'),
('Hunting season in October and November fills 90 and 94 with pickups and trailers, and the carriers slow down.','Hunting season in October and November fills 90 and 94 with pickups and trailers. The carriers slow down.'),
('The Father’s Day tornado in June 2010 tore the roof off the arena at MetraPark and crossed the Heights.','The Father’s Day tornado in June 2010 tore the roof off the arena at MetraPark. It crossed the Heights.'),
('The June 2022 flood on the Yellowstone shut the water plant for two days and cut the road to Red Lodge.','The June 2022 flood on the Yellowstone shut the water plant for two days. It cut the road to Red Lodge.'),
('An enclosed trailer keeps off the road salt, the gravel the state spreads on the pass, and the hail.','An enclosed trailer keeps off the road salt, the gravel the state spreads, and the hail.'),
('On the North Side, the South Side, or under the Rims, plan on a main road or a lot','On the North Side, the South Side, or under the Rims, plan on a lot'),
('The grids off Main Street from Alkali Creek to Lake Elmo are wide, and the curb works on most blocks.','The grids off Main Street from Alkali Creek to Lake Elmo are wide. The curb works on most blocks.'),
('The two hospitals bring residents each June and traveling nurses all year, and the handoff happens at the fairgrounds lots.','The two hospitals bring residents each June and traveling nurses all year. The handoff happens at the fairgrounds lots.'),
('The road to Red Lodge is two lanes, and a trailer meets you in town rather than up a ranch road.','The road to Red Lodge is two lanes. A trailer meets you in town rather than up a ranch road.'),
])

fix('build_lincoln_local.py', [
('Car shipping in Lincoln runs along Interstate 80 on the north edge of the city and down Highway 2 to the southeast.','Car shipping in Lincoln runs along Interstate 80 on the north edge and down Highway 2 southeast.'),
('Nearly every carrier crossing the country rides 80 past the city, and the Omaha pool is an hour east.','Nearly every carrier crossing the country rides 80 past the city. The Omaha pool is an hour east.'),
('The 77 exit serves the west side and the airport, 27th Street serves the north, and 56th Street serves the northeast.','The 77 exit serves the west side and the airport. 27th Street serves the north, and 56th Street serves the northeast.'),
('The carriers come off 80 at 27th Street or the 77 exit, and off Highway 2 at 27th or 70th.','The carriers come off 80 at 27th Street or the 77 exit. They come off Highway 2 at 27th or 70th.'),
('So do the arena lots in the Haymarket outside the games and the fairgrounds lots at 84th and Havelock.','So do the arena lots in the Haymarket outside the games and the fairgrounds lots at 84th.'),
('The Near South below the Capitol is the oldest neighborhood, big houses on narrow streets with tree lawns and alley garages.','The Near South below the Capitol is the oldest neighborhood. It is big houses on narrow streets with tree lawns and alley garages.'),
('Country Club and the Sheridan Boulevard streets south of there are winding and wooded, and the handoff moves to Van Dorn or 33rd.','Country Club and the Sheridan Boulevard streets south of there are winding and wooded. The handoff moves to Van Dorn or 33rd.'),
('Havelock on the northeast side is the old railroad town around the car shops, a plain grid where the curb works.','Havelock on the northeast side is the old railroad town around the car shops. It is a plain grid where the curb works.'),
('The Highlands and Fallbrook on the northwest side by the interstate are the newest subdivisions, wide streets and cul-de-sacs.','The Highlands and Fallbrook on the northwest side by the interstate are the newest subdivisions. The streets are wide.'),
('Wilderness Hills, Southern Hills, Village Gardens, and Edenton allow the curb nearly everywhere, and the cul-de-sacs are the only problem.','Wilderness Hills, Southern Hills, Village Gardens, and Edenton allow the curb nearly everywhere. The cul-de-sacs are the only problem.'),
('The Denver and Chicago lanes ride 80 and fill every day, because every carrier crossing the country is on it.','The Denver and Chicago lanes ride 80 and fill every day. Every carrier crossing the country is on it.'),
('State government fills the Capitol and the office blocks around it, and the agencies move staff in on start dates all year.','State government fills the Capitol and the office blocks around it. The agencies move staff in on start dates all year.'),
('The Guard’s refueling wing at the airport rotates airmen on orders, and the jet completion hangars beside it bring technicians on contract.','The Guard’s refueling wing at the airport rotates airmen on orders. The jet completion hangars beside it bring technicians on contract.'),
('Seven Saturdays from late August to November fill the stadium, and every home game has sold out since 1962.','Seven Saturdays from late August to November fill the stadium. Every home game has sold out since 1962.'),
('The October 1997 storm dropped a foot of wet snow on the trees and put the city in the dark for a week.','The October 1997 storm dropped a foot of wet snow on the trees. It put the city in the dark for a week.'),
('A tornado watch holds the truck at the truck stop until it lifts, and we call before it does.','A tornado watch holds the truck at the truck stop until it lifts. We call before it does.'),
('In the Near South, the Haymarket, or on the campus blocks, plan on a main road or a lot','In the Near South, the Haymarket, or on the campus blocks, plan on a lot'),
('Seven Saturdays a year the stadium fills, 80 backs up from Omaha, and the streets around the campus close.','Seven Saturdays a year the stadium fills and 80 backs up from Omaha. The streets around the campus close.'),
('The Near South is narrow streets with tree lawns and alley garages, and Country Club is winding and wooded.','The Near South is narrow streets with tree lawns and alley garages. Country Club is winding and wooded.'),
])

fix('build_nashua_local.py', [
('Daniel Webster Highway is the strip along the state line, and Main Street is the old road through the mills.','Daniel Webster Highway is the strip along the state line. Main Street is the old road through the mills.'),
('This page covers the turnpike, 101A, 111, Daniel Webster Highway, downtown, French Hill, the Tree Streets, the North End, and the South End.','This page covers the turnpike, 101A, 111, Daniel Webster Highway, downtown, French Hill, and the Tree Streets.'),
('It also covers the Boston commute, the tax migration, the defense campus, the hospitals, the colleges, and the nor’easters.','It also covers the Boston commute, the tax migration, the defense campus, the colleges, and the nor’easters.'),
('The Boston pool is forty-five minutes down the turnpike, and the 495 carriers pass the state line all day.','The Boston pool is forty-five minutes down the turnpike. The 495 carriers pass the state line all day.'),
('The Everett Turnpike is Route 3, and it runs the length of the city from the state line to Merrimack.','The Everett Turnpike is Route 3. It runs the length of the city from the state line to Merrimack.'),
('South of the line it runs to Lowell and 495, and 495 reaches 93 and 95 in twenty minutes.','South of the line it runs to Lowell and 495. From there 93 and 95 are twenty minutes away.'),
('Route 111 is Hollis Street on the west side and crosses the river on the Taylor Falls Bridge to Hudson.','Route 111 is Hollis Street on the west side. It crosses the river on the Taylor Falls Bridge to Hudson.'),
('Downtown runs along Main Street from the river bridge north to the library, brick blocks and the old mills along the canal.','Downtown runs along Main Street from the river bridge north to the library. It is brick blocks and the old mills along the canal.'),
('The Tree Streets west of Main are the same density on a flat grid, and the driver meets you on Kinsley or Hollis Street.','The Tree Streets west of Main are the same density on a flat grid. The driver meets you on Kinsley or Hollis Street.'),
('Crown Hill east of Main and south of the river is older houses on short blocks, and some allow the curb.','Crown Hill east of Main and south of the river is older houses on short blocks. Some allow the curb.'),
('The Northwest off Amherst and Broad Streets is the same, and the airport sits at the edge of it.','The Northwest off Amherst and Broad Streets is the same. The airport sits at the edge of it.'),
('A move-in date in late August or the first week of September lands in the busiest days of the year.','A move-in date in late August or the first week of September lands in the busiest days.'),
('The two hospitals, one downtown and one on Kinsley Street, bring residents each June and traveling nurses year round.','The two hospitals, one downtown and one on Kinsley Street, bring residents each June. Both hire traveling nurses year round.'),
('The first of September is Boston’s moving day, and every carrier in New England is in the city that week.','The first of September is Boston’s moving day. Every carrier in New England is in the city that week.'),
('The December 2008 ice storm put half the state in the dark for a week, and the carriers waited in Lowell until the roads cleared.','The December 2008 ice storm put half the state in the dark for a week. The carriers waited in Lowell until the roads cleared.'),
('Mud season in March and April posts the dirt roads in Hollis and Amherst, and a trailer meets you on the pavement.','Mud season in March and April posts the dirt roads in Hollis and Amherst. A trailer meets you on the pavement.'),
('The May 2006 storm put the Nashua River over its banks downtown and closed the low roads for days.','The May 2006 storm put the Nashua River over its banks downtown. The low roads closed for days.'),
('The leaf traffic in October fills 93 and 3 on the weekends, and a Friday handoff moves to the morning.','The leaf traffic in October fills 93 and 3 on the weekends. A Friday handoff moves to the morning.'),
('An enclosed trailer keeps off the road salt, the brine sprayed before a storm, and the sand the plows leave behind.','An enclosed trailer keeps off the road salt, the brine, and the sand the plows leave behind.'),
('Because households move over the line for the taxes every month, and most ship one car while driving the other.','Because households move over the line for the taxes every month. Most ship one car while driving the other.'),
('The campus on Spit Brook Road brings engineers on contract starts and moves them between sites, and the handoff happens on Daniel Webster Highway.','The campus on Spit Brook Road brings engineers on contract starts and moves them between sites. The handoff happens on Daniel Webster Highway.'),
])

fix('build_winstonsalem_local.py', [
('This page covers 40, 52, 421, the Parkway, Silas Creek, downtown, the West End, Ardmore, Buena Vista, and Old Salem.','This page covers 40, 52, 421, the Parkway, Silas Creek, downtown, the West End, Ardmore, and Old Salem.'),
('It also covers the medical center, the universities, the research campus, the fair, the furniture market, and the ice storms.','It also covers the medical center, the universities, the research campus, the furniture market, and the ice storms.'),
('Interstate 40 runs along the south side of the city past the mall and the hospital on Silas Creek.','Interstate 40 runs along the south side past the mall and the hospital on Silas Creek.'),
('Highway 52 runs north and south through the east side of downtown, and the 74 signs went up a few years ago.','Highway 52 runs north and south through the east side of downtown. The 74 signs went up a few years ago.'),
('The Salem Parkway is the old Business 40 through downtown, closed for a year and a half and reopened in 2020 with new bridges.','The Salem Parkway is the old Business 40 through downtown. It closed for a year and a half and reopened in 2020 with new bridges.'),
('Our office is in the tower on West Fifth Street downtown, a few blocks from Fourth Street and the convention center.','Our office is in the tower on West Fifth Street downtown, two blocks from the convention center.',2),
('Ardmore between the West End and the medical center is bungalows on a grid, and the curb usually works.','Ardmore between the West End and the medical center is bungalows on a grid. The curb usually works.'),
('The curb works where the branches allow it, and the handoff moves to Reynolda Road where they do not.','The curb works where the branches allow it. The handoff moves to Reynolda Road where they do not.'),
('Sherwood Forest, Westview, and the west side off Robinhood Road are the same, and the truck reaches the curb.','Sherwood Forest, Westview, and the west side off Robinhood Road are the same. The truck reaches the curb.'),
('A July start at the medical center or the late August move-in lands in the busiest weeks of the year.','A July start at the medical center or the late August move-in lands in the busiest weeks.'),
('The research campus in the old cigarette factories fills with labs and startups and moves scientists on grant cycles.','The research campus in the old cigarette factories is labs and startups. It moves scientists on grant cycles.'),
('The tobacco company keeps its headquarters downtown and its plant north of the city, and it moves managers between the two.','The tobacco company keeps its headquarters downtown and its plant north of the city. It moves managers between the two.'),
('The university on the north side takes student cars in late August, and the arts conservatory by Old Salem follows.','The university on the north side takes student cars in late August. The arts conservatory by Old Salem follows.'),
('Retirees fill the communities on the north side and the condos downtown, and many of them came from the Northeast.','Retirees fill the communities on the north side and the condos downtown. Many of them came from the Northeast.'),
('Winston-Salem runs on a hospital calendar and a campus calendar, and the weather problem is ice that arrives twice a winter and stays a day.','Winston-Salem runs on a hospital calendar and a campus calendar. The weather problem is ice that arrives twice a winter and stays a day.'),
('The fair fills the fairgrounds on the north side for ten days in early October and takes University Parkway with it.','The fair fills the fairgrounds on the north side for ten days in early October. It takes University Parkway with it.'),
('The furniture market in High Point fills every hotel in the Triad for a week each April and October, and the carriers stage farther out.','The furniture market in High Point fills every Triad hotel for a week each April and October. The carriers stage farther out.'),
('The December 2002 ice storm put the city in the dark for a week and dropped trees on every street in Buena Vista.','The December 2002 ice storm put the city in the dark for a week. It dropped trees on every street in Buena Vista.'),
('An enclosed trailer keeps off the pollen, the brine sprayed before an ice storm, and the sap under the oaks.','An enclosed trailer keeps off the pollen, the brine, and the sap under the oaks.'),
('New York runs four hundred fifty to six hundred fifty, about five hundred twenty miles up 85 and 95.','New York runs four hundred fifty to six hundred fifty, about five hundred twenty miles up 95.'),
('The West End is steep streets that bend and drop, and Old Salem is narrow streets from the 1700s.','The West End is steep streets that bend and drop. Old Salem is narrow streets from the 1700s.'),
('Carriers use it to cross downtown again, and the Stratford Road and Silas Creek exits on 40 still take most of the handoffs.','Carriers use it to cross downtown again. The Stratford Road and Silas Creek exits on 40 still take most of the handoffs.'),
])
