from scapy.all import *
import sys

dstMac = "00:11:11:11"

M1 = "00:10:11:11:11:11"

for i in range(0, 2):
	dstMacTemp = dstMac + ":" + format( i, '02x' ) + ":"
	for j in range(0, 3):
		dstMacTempTemp = dstMacTemp + format( j, '02x' )
		print( dstMacTempTemp )
		M2 = dstMacTempTemp
		sendp( Ether( src=M1, dst=M2 ) / ("*"*46), iface="eth1", count=1)
