import RPi.GPIO as GPIO #Initialize input and output pins of the PIR sensors 
import time
GPIO.setup(PIR_PIN, GPIO.IN)


PIR_PIN = 7


print("PIR Module Test (CTRL+C) to exit")
time.sleep(2)
print("Ready")

while True:
               if GPIO.input(PIR_PIN):
                print("Motion Dectected!")
                time.sleep(1)


#Write script to trigger the camera 