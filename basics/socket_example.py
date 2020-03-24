import socket
socket.setdefaulttimeout(2)
s = socket.socket()


ip_address = "1.1.1.1" #"localhost"
port = 22

try:
    s.connect((ip_address,port))
    ans = s.recv(1024)
    print ans
except Exception, e:
    print "error detected using ip_address", ip_address


#ans =s.recv(1024)

#print ans
