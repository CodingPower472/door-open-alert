
<<<<<<< Updated upstream
from flask import Flask, render_template, send_from_directory
#from gpiozero import Button
=======
from flask import Flask, render_template, request, redirect
#import gpiozero
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
	return render_template('index.html', sensors = sensors)
	
=======
	render_template('index.html', sensors = sensors)

>>>>>>> Stashed changes
@app.route('/js/<path:path>')
def js(path):
	return send_from_directory('js', path)

if __name__  == "__main__":
	app.run(debug=True)
