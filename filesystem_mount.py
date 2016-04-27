from subprocess import *
import os
import shutil

def nfs_mount(directory_to_mount, mount_location):
    "check if locaion is mounted, if not, mount it "
    if not os.path.ismount(mount_location):
        command = 'mount -t nfs ' + directory_to_mount + " " + mount_location + " -o noauto,x-systemd.automount"
        check_call(command, shell = True)
    

def move_file_to_mount(save_directory, mv_directory):
    onlyfiles = [f for f in os.listdir(save_directory) if os.path.isfile(os.path.join(save_directory, f))]
    for item in onlyfiles:
        shutil.move(save_directory + "/" + item, mv_directory + "/" + item)
    
