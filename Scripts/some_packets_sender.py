#!/usr/bin/python

from scapy.all import *

scrIp = '10.10.10.2'
dstIp = '10.10.10.4'

srcMac = '00:11:22:33:44:56'
dstMac = '00:11:22:33:44:55'

face = ''


ip = raw_input('Enter source ip (default %s): ' % scrIp)
if ip != '':
	scrIp = ip

mac = raw_input('Enter source mac (default %s): ' % srcMac)
if mac != '':
	srcMac = mac

ip = raw_input('Enter destination ip (default %s): ' % dstIp)
if ip != '':
	dstIp = ip

mac = raw_input('Enter destination mac (default %s): ' % dstMac)
if mac != '':
	dstMac = mac

face  = raw_input('Enter the interface: ')


eth = Ether(
		src = srcMac,
		dst = dstMac,
		type = 0x8100)

ip = IP(
		src = scrIp,
		dst = dstIp)

''' optional '''
dotq = Dot1Q(
		prio = 7,
		vlan = 101)
''' optional '''

pack = eth/dotq/ip/ICMP()

dotq = Dot1Q(
		prio = 2,
		vlan = 101)

pack2 = eth/dotq/ip/ICMP()

pack.display()
pack2.display()

i = 0;

while True:
	
	i += 1;
	sendp(pack, iface = face, verbose = False)
	sendp(pack2, iface = face, verbose = False)
	print "sent"
	time.sleep(3)