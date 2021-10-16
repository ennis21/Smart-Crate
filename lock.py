import RPi.GPIO as GPIO

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
#This sets up the GPIO 23 pin as an output pin
GPIO.setup(23, GPIO.OUT)

while (True):

    GPIO.output(23, 1)
    sleep(8)
    GPIO.output(23, 0)
    sleep(1)
