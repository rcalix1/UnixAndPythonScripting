import pygeoip
import dpkt

#####################################################

gi = pygeoip.GeoIP('/opt/GeoIP/Geo.dat')

def retGeoLocation(ip):
    try:
        rec = gi.record_by_name(ip)
        city = rec['city']
        country = rec['country']
        answer = city + ", " + country
        return  answer
    except:
        return "unregistered"
    



#####################################################

def printPcap(pcap):
    for (elements) in pcap:
        try:
            ip = dpkt.ethernet.Ethernet(elements).data
            src = ip.src
            dst = ip.dst
            print ip.dst + " -> " + retGeoLocation(dst)
        except:
            print "error"


#####################################################

f = open("geodata.pcap")
pcap = dpkt.pcap.Reader(f)
printPcap(pcap)

#####################################################



