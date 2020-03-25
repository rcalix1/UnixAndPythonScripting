import os
import re ## python regular expression module

path = '/home/seed/Desktop/2020springITS372/fileSystem/'

## get the data

for filename in os.listdir(path):
    pathname = os.path.join(path, filename)
    if os.path.isfile(pathname):
        f = open(pathname, 'r')
        print pathname
        for line in f.readlines():
            print line
            ## now that yo have the contents of each file
            ## use the re module to search a specific pattern 


        f.close()

print re.findall("[Ll]en","len is the Length")
