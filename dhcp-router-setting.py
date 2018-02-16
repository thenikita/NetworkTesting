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


# function writes a command to the telnet
# console and reads the response
def Write(str1, str2 = '#'):
	
	telnet.write(str1 + '\r')
	telnet.read_until(str2)
	
	return


# function that resets settings before all
def ResetSettings():

	print "Resetting settings:D (not working)"
	Write('configure')
	Write('no ip dhcp pool network Generated')
	Write('no ip dhcp relay address')
	Write('no ip dhcp relay enable')
	Write('no ip dhcp information option')
	Write('end')


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

	ip = '10.10.10.'
	mask = '255.255.255.0'

	Write('end')
	Write('configure')

	try:

		print "Generatin IP pool..."
		Write(
			'ip dhcp pool network Generated ' + 
			ip + '0 '+
			mask)

	except Exception as e:

		print "   Pool generation failed!"

	else:

		print "   Pool generated!"


	try:

		print "Setting IP range..."
		
		Write(
			'address ' +
			'low ' + ip + '0 ' +
			'high ' + ip + '254')

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
			' high ' + ip + '254')

		Write('ip dhcp server')

	elif mode == 'rel':
			
		print "Relay mode setting..."
		
		Write('end')
		Write('configure')
		
		port = raw_input('The number of router port wheres DHCP server: ')
		Write(
			'interface ethernet %s' %
			port) 
		Write('ip dhcp snooping trust')

		Write('exit')
		serverIp = raw_input('Enter the DHCP servers IP: ')
		Write(
			'ip dhcp relay address %s' % 
			serverIp)
		Write('ip dhcp relay enable')
		Write('ip dhcp information option')


def main():

	try:

		Connect(telnet)
		time.sleep(5)		#wait for load
		ResetSettings()
	
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


	Write('end')
	Write('CLIexit')
	telnet.close()
	print "Exited"

main()