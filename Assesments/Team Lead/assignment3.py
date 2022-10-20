import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

while True:

	GPIO.output(2, True)
	time.sleep(60)
	GPIO.output(2, False)

	GPIO.output(3, True)
	time.sleep(5)
	GPIO.output(3, False)

	GPIO.output(4, True)
	time.sleep(10)
	GPIO.output(False)