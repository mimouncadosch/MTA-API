import os
from flask import Flask, jsonify, render_template, request	

app = Flask(__name__)


@app.route('/load')
def load_data():
	print 'calling load_data'
	data = open("google_transit/stop_times_abbr.txt", "r+")
	arrivals = []
	for line in data:
		arrivals.append(line)

	return 'data loaded'


@app.route('/get_arrivals')
def get_arrivals():
	print 'calling get_arrivals'
	currHour = request.args.get('hour', 0, type=str)
	currMinute = request.args.get('minute', 0, type=str)

	return jsonify(result=currHour + currMinute)

@app.route('/')
def index():
	isLoaded = load_data()
	print isLoaded
	return 'I am ready'
	# return render_template('index.html')

if __name__ == "__main__":
	app.run()