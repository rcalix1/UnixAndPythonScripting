from scapy.all import *


def my_packet(   my_ttl   ):
    a = IP()
    a.dst = '8.8.8.8'
    a.ttl = my_ttl
    b = ICMP()
    p = a/b
    return p


number_of_hops = 25


for i in range(1, number_of_hops):
    pkt = my_packet(  i   )
    ## pkt.show()
    send(pkt)



