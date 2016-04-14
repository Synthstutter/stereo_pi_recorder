import picamera
from trigger import Trigger_pud
from time import sleep
from led import Led

cam = picamera.PiCamera()
led = Led()

def record_video(seconds):
    cam.start_recording('testvid.h264')
    recording = True
    while recording:
        for second in range(seconds/2-1):
            print "recording..."
            led.on()
            sleep(1)
            led.off()
            sleep(1)
        recording = False
    cam.stop_recording()
    print "end recording"
    


