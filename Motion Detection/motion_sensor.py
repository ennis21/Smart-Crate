from gpiozero import MotionSensor
import time

pir = MotionSensor(4)

while True:
    pir.wait_for_motion()
    print("Motion detected.")
    try:
        exec(open("camera.py").read())
    except SystemExit:
            pass
    time.sleep(75)
    