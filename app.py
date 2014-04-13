import os
from flask import Flask, jsonify, render_template, request	

app = Flask(__name__)

@app.route('/')
def index():
	stop = {'name' : '96', 'place': 'UWS'}
	stop['people'] = '200'
	return render_template('index.html', stop = stop)

@app.route('/files')
def read_file():
	# Create objects for each subway stop
	stops_file = open("google_transit/stops.txt", "r+") # Open file
	stops = [] # Array of stop objects

	for line in stops_file:
		t = line.split(",") # Read each line
		stop = {'id' : t[0], 'name' : t[2], 'lat': t[4], 'lon': t[5], 'arrivals': []}
		# print stop
		stops.append(stop) # Add subway stop to array of stops

	# Remove duplicates. Every station appears three times in file
	stops = remove_duplicates(stops)

	# For each subway stop, add the times where trains top there
	stop_times = open("google_transit/stop_times.txt", "r+")
	
	for line in stop_times:
		t = line.split(",")

		for stop in stops:
			if t[3] == stop['id']:	# Match stations by code
				print 't[3]', t[3]
				print stop['id']
				stop['arrivals'].append(t[1]) # Add arrival times to each station

	for item in stops:
		print item

	return 'hello world backend'

# In file given, each station appears three times. Take each station once only
def remove_duplicates(array):
	new_array = []
	length = len(array)
	for i in range(1, length, 3):
		new_array.append(array[i])
	return new_array


if __name__ == "__main__":
    app.run()