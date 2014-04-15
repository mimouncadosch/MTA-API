import os

stop_times = open("google_transit/stop_times	.txt", "r+")
stops_info = open("google_transit/stops.txt", "r+")
info = open("info.json", "w+")

# Create stops
stops = {}
for line in stops_info:
	# print line
	data = line.split(",")
	id = data[0]
	name = data[2]
	lat = data[4]
	lon = data[5]
	stop = {'name' : name, 'lat': lat, 'lon': lon}
	stops[id] = stop
	
# print type(stops)

# Create arrivals
ids = []
arrivals = {}
for line in stop_times:
	data = line.split(",")
	# print data
	time = data[1]
	# print time
	id = data[3]
	if id not in ids:
		ids.append(id)
	arrivals.setdefault(id,[]).append(time)

print 'len(ids)', len(ids)

data = {}
for id in ids:
	data[id] = {'name' : stops[id]['name'], 'lat': stops[id]['lat'], 'lon': stops[id]['lon'], 'arrivals': arrivals[id]}
	print data[id]


# Fill in stations. Initialize dictionary
# for line in stop_times:
# 	id = line.split(",")[3]
# 	# print id
# 	arrivals[id] = []
# 	# print arrivals[id]
# # print 'Initialized dictionary'

# for line in stop_times:
# 	t = line.split(",")
# 	time = t[1].split(":")
# 	id = t[3]
# 	print time
# 	print id

# 	arrivals[id].append(time)
	# print arrivals[id]
	

# print 'done with arrivals'
# print arrivals

# stops = []
# for line in stops_info:
# 	t = line.split(",")
# 	print t
# 	id = t[0]
# 	name = t[2]
# 	lat = t[4]
# 	lon = t[5]
	
# 	stop = {'id': id, 'name': name, 'lat': lat, 'lon': lon}
# 	stops.append(stop)
# print 'done with stops'


# data = {}
# for arrival in arrivals:
# 	for stop in stops:
# 		if stop['id'] == arrival['id']:
# 			print 'found match', stop['id'], arrival['id']
# 			data[stop['id']] = {'id': stop['id'], 'name': stop['name'], 'lat': stop['lat'], 'lon': stop['lon'], 'time':arrival['time']}
# 			print data

# # data = jsonify(data)
# info.write(data)

