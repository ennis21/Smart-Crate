from picamera import PiCamera
import time
camera = PiCamera()
time.sleep(2)
camera.resolution = (1280, 720)
camera.vflip = True
camera.contrast = 10
file_name = "/home/pi/recording/detected_" + str(time.time()) + ".h264"
print("Recording started.")
camera.start_recording(file_name)
camera.wait_recording(20)
camera.stop_recording()
print("Recording saved.")
camera.close()
exit()
