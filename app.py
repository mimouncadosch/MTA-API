import os
from flask import Flask, jsonify, render_template, request, g
import pickledb

app = Flask(__name__)
stop_times = open("google_transit/stop_times.txt", "r+")
stops_info = open("google_transit/stops.txt", "r+")


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
	time = data[1]
	id = data[3]
	if id not in ids:
		ids.append(id)
	arrivals.setdefault(id,[]).append(time)
# print 'len(ids)', len(ids)


data = {}
for id in ids:
	data[id] = {'name' : stops[id]['name'], 'lat': stops[id]['lat'], 'lon': stops[id]['lon'], 'arrivals': arrivals[id]}


@app.route('/')
def index():
	return 'hello world. stations'

# Given station, returns all info about that station
@app.route('/api')
def api():
	id = request.args.get('id', 0, type=str)
	print 'request for id', id
	res = data[id]
	print 'res', res
	return jsonify(result=res)

# Given time, returns all stations where train stops at that time
@app.route('/times')
def times():
	hour = request.args.get('hour', 0, type=str)
	minute = request.args.get('minute', 0, type=str)
	print 'request for hour and min', hour, minute
	i = 0
	results = []
	for key in data:
		arrivals = data[key]['arrivals']
		for arrival in arrivals:
			a = arrival.split(":")
			if a[0] == hour and a[1] == minute:
				result = {'arrival': arrival, 'id': key, 'name': data[key]['name'], 'lat': data[key]['lat'], 'lon': data[key]['lon']}
				results.append(result)
	return jsonify(result=results)

if __name__ == "__main__":
	app.run()
