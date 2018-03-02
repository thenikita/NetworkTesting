#!/usr/bin/python

# nick theone 2018
# 
# code designed for testing maximum amount of ip interfaces

import telnetlib

targetIp = '10.10.10.101'

startVlanId = 1000
endVlanId = 1011

startTargetIface = 2
endTargetIface = 6

# ip: ip1.ip2.ip3.0
ip1 = 10
ip2 = 1
ip3 = 1

print "Starting script"

telnet = telnetlib.Telnet(targetIp, 23)
telnet.read_until(':')
print "Read..."

def Write(str1, str2 = '#'):
	
	telnet.write(str1 + '\r')
	telnet.read_until(str2)
	
	return

Write('admin', ':')
Write('admin')
Write('configure')
Write('vlan %i-%i' % (startVlanId, endVlanId))
print "Vlan created..."

Write('interface range ethernet %i-%i' % (startTargetIface, endTargetIface))
Write('switchport trunk allowed vlan add %i-%i' % (startVlanId, endVlanId))
Write('exit')
print "Trunks are set..."

for i in range(startVlanId, endVlanId):
	print "Interface %i\r" % i
	Write('interface vlan %i' % i)
	Write('ip address 10.%i.%i.%i /24' % (ip1, ip2, ip3))
	Write('exit')
	ip3 += 1
	if ip3 > 255:
		ip2 += 1
		ip3 = 0
		print "First subnet used!"
	if ip2 > 255:
		ip2 = 0
		print "TOO MUCH POWER!!!"

print "Going to default..."
Write('end')
Write('configure')
Write('interface range ethernet %i-%i' % (startTargetIface, endTargetIface))
Write('switchport trunk allowed vlan remove %i-%i' % (startVlanId, endVlanId))
print "Trunks removed!"
Write('exit')
Write('no vlan %i-%i' % (startVlanId, endVlanId))
print "VLANs removed!"

telnet.close()