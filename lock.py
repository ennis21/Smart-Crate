import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT) #lock
GPIO.setup(24, GPIO.OUT) #LED

while (True):

    GPIO.output(23, 1)
    GPIO.output(24, 1)
    sleep(8)
    GPIO.output(23, 0)
    sleep(4)
    GPIO.output(24,0)
    sleep(1)
