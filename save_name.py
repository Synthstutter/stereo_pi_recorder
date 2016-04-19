import os
from os.path import isfile, join
import time as t
 

class File_namer():
    def __init__(self, directory, device):
        self.file_name = ""
        self.video_directory = directory
        if not os.path.exists(self.video_directory):
            os.makedirs(self.video_directory)
        self.device = device
        
    def get_name(self):
        onlyfiles = [f for f in os.listdir(self.video_directory) if isfile(join(self.video_directory, f)) and f.split("-")[0] == t.strftime('%Y_%m_%d')]
        new_int = str(len(onlyfiles) + 1).zfill(2)
        self.file_name=(self.video_directory + t.strftime('/%Y_%m_%d-') + self.device.__str__() + "_" + new_int + ".h264")
        return self.file_name
    
# example_name = "2016_4_23-03_02.h264"
