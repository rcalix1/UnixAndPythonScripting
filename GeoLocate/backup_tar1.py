import tarfile
import os
import subprocess
from datetime import datetime

str_datetime = str(  datetime.now()  )
str_datetime = str_datetime.replace(" ","_")

tar_file_name = "tmp_backup" + str_datetime + ".tar"

tar = tarfile.open(tar_file_name, "w")
selected_folder = "/tmp"
for root, dir, files in os.walk(selected_folder):
    for file in files:
        print(file) 
        fullpath = os.path.join(root, file)
        print(fullpath)
        tar.add(fullpath)

command = ["mv", tar_file_name, "/home/seed/Desktop"]
subprocess.call(command)


