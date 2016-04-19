from time import sleep
import camera
from trigger import Trigger
from led import Led
import save_name

video_length = 10
green_led_pin = 19
directory = "/home/nick/videos"
device = "L"

if __name__ == "__main__":
    trigger = Trigger()
    green_led = Led(green_led_pin)
    file_name = save_name.File_namer(directory, device)
    
    running = True
    
    while running:
        try:
            green_led.on()
            trigger.read_state()
            if trigger.input_state == False:
                green_led.off()
                camera.record_video(file_name.get_name(), video_length)           
        except KeyboardInterrupt:  
            green_led.cleanup()    
