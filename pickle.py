import pickledb
import os
from flask import Flask, jsonify, render_template, request, g

app = Flask(__name__)
db = pickledb.load('example.db', False) 
db.set('key', 'value')
db.set('mom', 'sara')
db.set('sister', 'nicole')

@app.route('/')
def index():
	return db.get('sister')

	
if __name__ == "__main__":
	app.run()

