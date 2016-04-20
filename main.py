from time import sleep
import camera
from trigger import Trigger
from led import Led
from filesystem_mount import nfs_mount
import save_name

video_length = 10
green_led_pin = 19
save_directory = "/mnt/nfsserver/videos"
device = "L"

pi_master = True
#the following mount only applies if pi_master is set false (if this is slavepi)
directory_to_mount = "192.168.0.3:/mnt/nfsserver"
mount_location = "/mnt/nfs"
if not pi_master:
    nfs_mount(directory_to_mount, mount_location)
    save_directory = "/mnt/nfs/videos"

if __name__ == "__main__":
        
    trigger = Trigger()
    green_led = Led(green_led_pin)
    file_name = save_name.File_namer(save_directory, device)
    
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
