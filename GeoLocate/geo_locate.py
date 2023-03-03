

import socket
import dpkt
import pygeoip
from geoip import geolite2

db_dict = {}
db_dict["192.168.1.3"] = "Japan"

##############################################

gi = pygeoip.GeoIP('geo1.dat')

##############################################

def retGeoStr(the_ip):
    try:
        res = gi.country_name_by_addr('14.139.61.12')
        print(res)
    except:
        print("error")


##############################################



def printPcap(pcap):
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa( ip.src  )
            dst = socket.inet_ntoa( ip.dst  )

            retGeoStr(src)
            retGeoStr(dst)


        except:
            print("error")



###############################################

## function to collect packet

f = open('test1.pcap', 'rb')

pcap = dpkt.pcap.Reader(f)

printPcap(pcap)



