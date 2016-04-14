import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class Led():
    def __init__(self, pin = 26):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)

    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def off(self):
        GPIO.output(self.pin, GPIO.LOW)
