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


db = pickledb.load('example.db', False)
i = 1
for key in data:
	# print 'key', key, i
	# i += 1
	# print 'data[key]', data[key]
	db.set(key, data[key])


@app.route('/')
def index():
	# load_data()
	return 'hello world. stations'

# Given station, returns all info about that station
@app.route('/api')
def api():
	id = request.args.get('id', 0, type=str)
	print 'request for id', id
	res = db.get(id)
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


	# return jsonify(result=results)
# stop_times = open("google_transit/stop_times.txt", "r+")
# stops_info = open("google_transit/stops.txt", "r+")
# # info = open("info.json", "w+")

# # arrivals = []
# for line in stop_times:
# 	t = line.split(",")
# 	time = t[1].split(":")
# 	time = str(time)
# 	# print 'time', time
# 	id = t[3]
# 	# print 'id', id
# 	# arrival = {'time' : time, 'id' : id}
# 	# arrivals.append(arrival)
# 	db.dcreate('stops')
# 	db.dadd(id, time)

# print 'done with arrivals'

# @app.route('/')
# def index():
# 	print db.get('D40S')
# 	return db.get('D40S')

# # ready = 'false'
# # arrivals = []
# # def load_data(callback):
# # 	global arrivals
# # 	print 'loading data'
# # 	data = open("google_transit/stop_times.txt", "r+")
# # 	for line in data:
# # 		t = line.split(",")
# # 		arrivals.append(t)
	
# # 	callback(arrivals)

# # @app.route('/')
# # def index():
# # 	def cb(arrivals):
# # 		print 'done loading file. ready'
# # 		# print arrivals[0: 100]
# # 		global ready
# # 		ready = 'true'
# # 		print 'ready', ready
		
# # 	# while(i )
# # 	# ready = 'false'
# # 	# req = request.args.get('ready', 0, type=str)
# # 	# 	if ready is 'false':
# # 	# 		return 'false'
# # 	print 'ready', ready
# # 	load_data(cb)

# # 	return render_template('index.html')

# # @app.route('/check_ready')
# # def check_ready():
# # 	global arrivals
# # 	req = request.args.get('ready', 0, type=str)
# # 	return jsonify(result=arrivals)

# # # @app.route('/')
# # # def index():
# # # 	return render_template('index.html')

# # @app.route('/get_arrivals')
# # def get_arrivals():
# # 	print 'callitime = data[1].split(":")
# # 	# 	print time
# # 		# hour = time[0]
# # 		# minute = time[1]ng get_arrivals'
	
# # 	currHour = request.args.get('hour', 0, type=str)
# # 	currMinute = request.args.get('minute', 0, type=str)

# # 	# currArrivals = {} # Dictionary {time, station}

# # 	# for line in arrivals:
# # 	# 	print line
# # 	# 	data = line.split(",")
# # 	# 	# print data
# # 	# 	
# # 	# 	if(currHour is hour or currMinute is minute):
# # 	# 		currArrivals.update({data[3]:(data[1])})

# # 	# return jsonify(result=currHour + currMinute)
# # 	return jsonify(result=arrivals)
	

# # # @app.route('/')
# # # def index():
# # # 	load_data()

# # # 	# print arrivals
# # # 	return render_template('index.html')

if __name__ == "__main__":
	app.run()
	# main()
