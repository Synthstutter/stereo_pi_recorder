import RPi.GPIO as GPIO
import time

class Trigger_pud():
    "for trigger pull down, attach one end to pin, the other to grond"

    def __init__(self, pin =18):
        self.pin = pin
        self.input_state = True
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def read_state(self):
        self.input_state = GPIO.input(self.pin)


# trigger = Trigger_pud()
# trigger.on_press(whatever_function)
