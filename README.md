#Totalcorner API Client

Unofficial API Client for totalcorner.com API.



## **Install**

`pip install totalcorner`

or

`python setup.py install`



## **Usage**



`import totalcorner`

`tapi = totalcorner.TotalCornerAPI("apikeyabcdefg")`



*Today*


`tapi.today(type="upcoming", columns="events,odds,asian,cornerLine,cornerLineHalf,goalLine,goalLineHalf,asianCorner,attacks,dangerousAttacks,shotOn,shotOff,possession", page=1)`

*Schedule*

`tapi.schedule(date="20190501", columns="events,odds,asian,cornerLine,cornerLineHalf,goalLine,goalLineHalf,asianCorner,attacks,dangerousAttacks,shotOn,shotOff,possession", page=1)`

*Matchview*

`tapi.matchview(matchid="82537483",columns="events,odds,asian,cornerLine,cornerLineHalf,goalLine,goalLineHalf,asianCorner,attacks,dangerousAttacks,shotOn,shotOff,possession")`

*Odds*

`tapi.odds(matchid="82537483", columns="asianList,goalList,cornerList,oddsList,asianHalfList,goalHalfList,cornerHalfList,oddsHalfList")`

*League Table*
`tapi.leaguetable(leagueid="1", type='table')`

*League Schedule*

`tapi.leagueschedule(leagueid="1", page=None, columns='events,odds,asian,cornerLine,cornerLineHalf,goalLine,goalLineHalf,"asianCorner,attacks,dangerousAttacks,shotOn,shotOff,possession')`



