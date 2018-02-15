#!/usr/bin/python

# nick theone, 2018
# code is designed for testing dhcp behaviour
# this script generates dhcp discover package
# and sends it to some port, now u can set
# things up on the router to chech the behaviour

#import sys
from scapy.all import *

#test
def main():
	print "Testing DHCP"

	routerIp = '10.10.10.101' 			# default router ip
	sourceMac = '00:11:22:33:44:55'		# defaul src mac
	interface = 'eth5'					# -/-

	eth = Ether(dst = 'ff:ff:ff:ff:ff:ff', src = sourceMac, type=0x800)
	ip = IP(src = '1.2.3.4', dst = '255.255.255.255')
	udp = UDP(sport = 68, dport = 67)
	boot = BOOTP(chaddr = 'ff:ff:ff:ff:ff:ff', ciaddr = '0.0.0.0', xid = 0x01020304, flags = 1)
	dhcp = DHCP(options=[('message-type', 'discover'), 'end'])
	pack = eth / ip / udp / boot / dhcp

	print "Packet ready"

	pack.show()

	while True:
		sendp(pack, iface = interface)
		time.sleep(10)

main()