import os

stop_times = open("google_transit/stop_times.txt", "r+")
stops_info = open("google_transit/stops.txt", "r+")
info = open("info.json", "w+")

arrivals = []
for line in stop_times:
	t = line.split(",")
	time = t[1].split(":")
	id = t[3]
	arrival = {'time' : time, 'id' : id}
	arrivals.append(arrival)
print 'done with arrivals'

stops = []
for line in stops_info:
	t = line.split(",")
	print t
	id = t[0]
	name = t[2]
	lat = t[4]
	lon = t[5]
	
	stop = {'id': id, 'name': name, 'lat': lat, 'lon': lon}
	stops.append(stop)
print 'done with stops'


data = {}
for stop in stops:
	for arrival in arrivals:
		if stop['id'] == arrival['id']:
			print 'found match', stop['id'], arrival['id']
			data[stop['id']] = {'id': stop['id'], 'name': stop['name'], 'lat': stop['lat'], 'lon': stop['lon'], 'time':arrival['time']}
			print data

data = jsonify(data)
info.write(data)

