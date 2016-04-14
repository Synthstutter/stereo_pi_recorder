from time import sleep
import camera
from trigger import Trigger_pud
from led import Led

video_length = 10
green_led_pin = 19

if __name__ == "__main__":
    trigger = Trigger_pud()
    green_led = Led(green_led_pin)
 
    running = True
    
    while running:
        green_led.on()
        trigger.read_state()
        if trigger.input_state == False:
            green_led.off()
            camera.record_video(video_length)            
