import os
from flask import Flask, jsonify, render_template, request, g
import pickledb

app = Flask(__name__)
db = pickledb.load('example.db', False)
# db.set('france', 'paris')
# db.set('colombia', 'bogota')

ready = 'false'

stop_times = open("google_transit/stop_times.txt", "r+")
stops_info = open("google_transit/stops.txt", "r+")
for line in stop_times:
	print line
	ready = 'true'

@app.route('/')
def index():
	# return 'hello world'
	return ready

@app.route('/api')
def api():
	country = request.args.get('country', 0, type=str)
	print db.get(country)
	return db.get(country)


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
