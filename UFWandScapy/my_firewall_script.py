
import os

print("enter ip address to block and press enter")
ip = input()
print("enter port number to block, and then press enter")
port = input()


def configure_firewall():
    os.system(  "ufw deny from " + ip)
    os.system(  "ufw deny " + port)
    os.system(  "ufw disable")
    os.system(  "ufw enable")
    os.system(  "ufw status verbose" )
   

configure_firewall()
