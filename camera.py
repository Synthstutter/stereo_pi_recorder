from picamera import PiCamera
from trigger import Trigger
from time import sleep
from led import Led

# cam = picamera.PiCamera()
# led = Led()

class Camera(PiCamera, Led):
    def __init__(self):
        self.led_pin = 26
    # def timed_record_video(self, name, seconds):
    #     self.PiCamera.start_recording(name)
    #     while self.PiCamera.recording:
    #         for second in range(seconds/2-1):
    #             try:
    #                 self.recording_led()
    #             except KeyboardInterrupt:  
    #                 self.cleanup()     
    #         self.PiCamera.recording = False
    #     self.PiCamera.stop_recording()

    def recording_led(self):
        while self.recording: 
            print "recording..."
            self.led_on()
            sleep(1)
            self.led_off()
            sleep(1)
