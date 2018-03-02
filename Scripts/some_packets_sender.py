#!/usr/bin/python

from scapy.all import *

scrIp = '10.1.1.1'
dstIp = '255.255.255.255'

srcMac = '00:1b:21:a6:9c:fd'
dstMac = '00:11:22:33:44:55'

face = ''

ip = raw_input('Enter source ip or 0 (default %s): ' % scrIp)
if ip != 0:
	scrIp = ip

mac = raw_input('Enter source mac or 0 (default %s): ' % srcMac)
if mac != 0:
	srcMac = mac

face  = raw_input('Enter the interface: ')

eth = Ether(
		src = srcMac,
		dst = dstMac)
ip = IP(
		src = scrIp,
		dst = dstIp)

dot1q = Dot1Q(
		prio = 7)

pack = eth/ip/dot1q

while True:
	
	sendp(pack, iface = face, verbose = False)
	print "Sent!"
	time.sleep(3)
