#!/usr/bin/python

from time import sleep
import picamera
import save_name
from trigger import Trigger
from led import Led
from filesystem_mount import nfs_mount, move_file_to_mount
import threading


video_length = 10
green_led_pin = 19
red_led_pin = 26
save_directory = "/mnt/nfsserver/videos"
device = "L"

def recording_led(red_led_pin):
    while running: 
        print "recording..."
        self.led_on()
        sleep(1)
        self.led_off()
        sleep(1)
        

pi_master = True
#the following mount only applies if pi_master is set false (if this is slavepi)
directory_to_mount = "192.168.0.3:/mnt/nfsserver"
mount_location = "/mnt/nfs"
if not pi_master:
    nfs_mount(directory_to_mount, mount_location)
    save_directory = "/home/nick/videos"
    mv_directory = "/mnt/nfs/videos"
    
if __name__ == "__main__":
    camera = picamera.PiCamera()
    # red_led_thread = threading.Thread(target =camera.recording_led)
    trigger = Trigger()
    green_led = Led(green_led_pin)
    red_led = Led(red_led_pin)
    file_name = save_name.File_namer(save_directory, device)
    running = True
    
    while running:
        try:
            red_led.led_off()
            green_led.led_on()
            trigger.read_state()
            if trigger.input_state == False:
                print "recording..." + file_name.get_name()
                green_led.led_off()
                red_led.led_on()
                camera.start_recording(file_name.get_name())
                # red_led_thread.start()
                sleep(1)
                trigger.input_state = True
                while camera.recording:
                    trigger.read_state()
                    if trigger.input_state == False:
                        camera.stop_recording()
                        print "stopped recording"
                sleep(0.5)
                if not pi_master:
                    move_file_to_mount(save_directory, mv_directory)
        except KeyboardInterrupt:  
            green_led.led_cleanup()  
