from flask import Flask, render_template, send_from_directory
from gpiozero import Button, LED
import os, time

app = Flask(__name__)

dir = os.getcwd()

global sensors
sensors = []

led = LED(17)
button = Button(2, hold_time=10)
button1 = Button(27)

def alertwebsite():
	print("Alerting the enemy")

def wasttime():
	print("wasting time")
	led.on()
	time.sleep(60)
	led.off()


def setupgpio():
	button.when_held = wasttime
	button1.when_pressed = alertwebsite


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
	setupgpio()
	app.run(debug=True)
