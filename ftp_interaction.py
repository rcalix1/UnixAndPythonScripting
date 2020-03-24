from ftplib import FTP
import ftplib
import sys, os


ftp = FTP('205.215.117.240', user, password)
ftp.login()

#ftp.cwd(/home/)   ## change to this directory

#ftp.retrline('LIST') ##print directory listing

local_file = open('example_file.txt')

ftp.upload(local_file)

ftp.download("specific_file")

ftp.close()

