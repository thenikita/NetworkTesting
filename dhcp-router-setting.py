#!/usr/bin/python

# nick theone 2018
#
# code is designed for setting up dchp profile
# on the net's router for overall and guard
# behaviour tests
#
# To use the script router already must have
# set telnet / ssh (later) acces!

from scapy.all import *
import telnetlib

targetIp = '10.10.10.101'
psw = ''
usr = ''
telnet = telnetlib.Telnet(targetIp, 23)
telnet.read_until(':')


def Write(str1, str2 = '#'):
	
	telnet.write(str1 + '\r')
	telnet.read_until(str2)
	
	return


# connectin as usr via telnet
def Connect(telnet):
	
	print "Connecting..."

	usr = raw_input('Enter login: ')
	psw = raw_input('Enter password: ')

	try:
		
		Write(usr, ':')
		Write(psw)
	
	except Exception as e:
		
		print "   Cannot log in as " + usr

	else:
		
		print "   Logged in!"


# functions sets vlan and ip to it to
# transit DHCP packets
def VlanSetup():

	Write('end')
	Write('configure')
	Write('vlan 101')
	Write('interface vlan 101')
	Write('ip address %s /24' % targetIp)


# function sets uo basic things for dhcp
# for some reason can't throw exception
def DhcpSetup():

	ip = '10.0.2.'
	mask = '255.255.255.0'

	Write('end')
	Write('configure')

	try:

		print "Generatin IP pool..."
		Write(
			'ip dhcp pool network Generated ' + 
			ip + '0 '+
			mask)

		Write('do show ip dhcp pool Generated')

	except Exception as e:

		print "   Pool generation failed!"

	else:

		print "   Pool generated!"


	try:

		print "Setting IP range..."
		Write(
			'address ' +
			'low ' + ip + '0 ' +
			'high ' + ip + '255')

	except Exception as e:

		print "   IP range wasn't set!"

	else:

		print "   IP range was set!"


	mode = raw_input('Enter mode (srv/rel): ')
	if mode == 'srv':
		
		print "Server mode setting..."

		port = 			raw_input('Enter routers testing port: ')
		vlan = 			raw_input("      VLAN: ")
		trustedMac = 	raw_input("      trusted mac: ")

		Write(
			'allow members port ' + port +
			' vlan ' + vlan +
			' devID ' + trustedMac +
			' low ' + ip + '0' +
			' high ' + ip + '255')

	elif mode == 'rel':
			
		print "Relay mode setting..."
		# this's not ready yet


def main():

	try:

		Connect(telnet)
		time.sleep(5)		#wait for load
	
	except Exception as e:
		
		print "Finally no way to connect..."

	else:

		print "Connect finished!"


	try:
	
		print "DHCP setup started..."
		DhcpSetup()

	except Exception as e:

		print "DHCP setup failed!"

	else:
	
		print "DHCP setup finished!"


	
	Write('CLIexit')
	telnet.close()
	print "Exited"

main()