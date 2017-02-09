import os
from os.path import isfile, join
import time as t
 

class File_namer():
    def __init__(self, mv_directory, save_directory, device):
        #move directory used for checking which name to put next
        self.file_name = ""
        self.save_directory = save_directory
        self.mv_directory = mv_directory
        if not os.path.exists(self.save_directory):
            os.makedirs(self.save_directory)
        self.device = device
        
    def get_name(self):
        # onlyfiles = [f for f in os.listdir(self.mv_directory) if isfile(join(self.mv_directory, f)) and f.split("-")[0] == t.strftime('%Y_%m_%d') and f.split("-")[1][0] == self.device]
        # ints = [int(item.split("_")[3][:2]) for item in onlyfiles]
        # try:
        #     max_int = max(ints)
        # except:
        #     max_int = 0
        # new_int = str(max_int + 1).zfill(2)
        self.file_name= (self.save_directory + t.strftime('/%Y_%m_%d-%H:%M:S_') + self.device.__str__() + ".h264")
        return self.file_name

    
# example_name = "2016_4_23-08:53_L.h264"
