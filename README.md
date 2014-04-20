#NYC Subway Data

## This is a RESTful API for NYC subway data from the MTA (Metropolitan Transportation Authority)

### Subway station codes
The MTA uses a set of codes to refer to subway stations in New York. In order to use these codes for other requests in this API, make the request:

Sample Request  
`mtaapi.herokuapp.com/stations`

Sample response
```
{ 
"result": [
	    {
	      "id": "901N", 
	      "name": "Grand Central - 42 St"
	    }, 
	    {
	      "id": "902N", 
	      "name": "Times Sq - 42 St"
	    }, 
	    ...
	]
}
```

### Subway station data
Given a station code (see above), get name and coordinates of every station.

Parameters  
`id: the station id. Ex: 120S for 96th St.`

Sample Request  
`mtaapi.herokuapp.com/stop?id=120S`

Sample response
```
{
  "result": {
    "lat": "40.752769", 
    "lon": "-73.979189", 
    "name": "Grand Central - 42 St"
  }
}
```

### Arrival times

This endpoint provides all subway arrival times at a given station.

Parameters  
`id: the station id. Ex: 120S for 96th St.`

Sample Request  
`mtaapi.herokuapp.com/api?id=120S`

Sample response
```
{
  "result": {
    "arrivals": [
      "06:30:00", 
      "08:38:00", 
      "10:45:00", 
      "12:55:30", 
      ...
      "12:34:00", 
      "15:22:00", 
      "18:10:00", 
      "20:58:00"
    ], 
    "lat": "40.793919", 
    "lon": "-73.972323", 
    "name": "96 St"
  }
}
```

### Times

This endpoint provides all subway stations where a train is stopping at the time specified

Parameters  
`hour: the hour, from 00:59 to 23:59 (European format). Ex: 23 for 11pm, 09 for 9am`
`minute: the minutes, from 0 to 59`

Sample Request  
`mtaapi.herokuapp.com/times?hour=10&minute=25`

Sample response
```
All stations where a train arrives at 10:25am
	{
  "result": [
    {
      "arrival": "10:25:00", 
      "id": "D22N", 
      "lat": "40.718267", 
      "lon": "-73.993753", 
      "name": "Grand St"
    }, 
    ...
    {
      "arrival": "10:25:00", 
      "id": "H13S", 
      "lat": "40.585307", 
      "lon": "-73.820558", 
      "name": "Beach 98 St"
    }
  ]
}
```
