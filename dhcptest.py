#!/usr/bin/python

# nick theone, 2018
# code is designed for testing dhcp behaviour
# this script generates dhcp discover package
# and sends it to some port, now u can set
# things up on the router to chech the behaviour

#import sys
from scapy.all import *

def MakePacket(srcMac, dstMac):

	print "Making packet..."

	eth = Ether(
		dst = dstMac, 
		src = srcMac, 
		type=0x800)

	ip = IP(
		src = '0.0.0.0', 
		dst = '255.255.255.255')

	udp = UDP(
		sport = 68, 
		dport = 67)

	boot = BOOTP(
		chaddr = dstMac, 
		ciaddr = '0.0.0.0', 
		xid = 0x01020304, 
		flags = 1)

	if int(raw_input('Use opt82? (1/0)')) == 1:

		print "Using 82!"
		option82 = "\x01\x01\x05\x02\x06\x11\x22\x34\x44\x55\x66"
		dhcp = DHCP(options=[
				('message-type', 'discover'),
				('relay_agent_Information', option82), 
				'end'])
	else:

		print "Not using 82!"
		dhcp = DHCP(options=[
				('message-type', 'discover'),
				'end'])

	pack = eth / ip / udp / boot / dhcp

	return pack


def main():

	print "Testing DHCP"

	routerIp = '10.10.10.101' 				# default router ip
	trustedsourceMac = raw_input('Enter trusted mac: ')
	defaultMac = '00:11:22:33:44:55'		# source mac of dhcp packets
											# if testing request packs should
											# be a) as trusted in router
											# settings b) as untrusted
	destMac = 'ff:ff:ff:ff:ff:ff'

	interface = raw_input('Enter the port: ')

	trustedPack = MakePacket(trustedsourceMac, destMac)
	untrustedPack = MakePacket(defaultMac, destMac)

	print "Packets ready"

	i = 0
	print "Sending trusted Pack: "
	while i < 6:

		print i
		i += 1
		sendp(trustedPack, iface = interface, verbose = False)
		time.sleep(10)					#sleep in seconds!

	i = 0
	print "Sending untrusted Pack: "
	while i < 6:

		print i
		i += 1
		sendp(untrustedPack, iface = interface, verbose = False)
		time.sleep(10)

main()