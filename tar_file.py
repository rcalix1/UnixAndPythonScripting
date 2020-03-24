import tarfile

tar  = tarfile.open("temp.tar", "w")

import os

for root, dir, files in os.walk("/etc"):
    for file in files:
        fullpath = os.path.join(root, file)
        tar.add(fullpath)


tar.close()

