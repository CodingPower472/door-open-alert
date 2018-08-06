
from flask import Flask, render_template, send_from_directory
#from gpiozero import Button
import os

app = Flask(__name__)

dir = os.getcwd()

global sensors
sensors = []

@app.route('/', methods=['GET', 'POST'])
def main():
	global sensors
	sensors = [{
		"title": "Sensor 1",
		"closed": True
	}, {
		"title": "Sensor 2",
		"closed": False
	}]
	return render_template('index.html', sensors = sensors)
	
@app.route('/js/<path:path>')
def js(path):
	return send_from_directory('js', path)

if __name__  == "__main__":
	app.run(debug=True)
