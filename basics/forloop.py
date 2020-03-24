f = open('/etc/passwd','r')

for line in f.readlines():
    print line


f.close()




