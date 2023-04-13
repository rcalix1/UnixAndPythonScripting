from scapy.all import *

a = IP()
a.dst = '8.8.8.8'
b = ICMP()
c = "Hello Google"

p = a/b/c



for i in range(1):
    send(p)
