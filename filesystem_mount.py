from subprocess import *
import os

def nfs_mount(directory_to_mount, mount_location):
    "check if locaion is mounted, if not, mount it "
    if not os.path.ismount(mount_location):
        command = 'mount -t nfs ' + directory_to_mount + " " + mount_location + " -o noauto,x-systemd.automount"
        check_call(command, shell = True)
    
