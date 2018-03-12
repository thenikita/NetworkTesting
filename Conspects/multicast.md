# Host Extensions for IP Multicasting

[RFC 1112](https://www.ietf.org/rfc/rfc1112.txt)
[RFC 2236](https://tools.ietf.org/html/rfc2236)

## Short Summary
Multicast = transmission to multiple destinations.

## Levels of Conformance
**Level 0**: No support
**Level 1**: Support for sending and no receiving
**Level 2**: Full support

## Host Group Addresses
Class D: starting with **1110** 

TO

Class E: starting with **1111**

In dotted decimal notation, host group addresses range from **224.0.0.0** to **239.255.255.255**. The 224.0.0.0 is guaranteed not to ne assigned to any group and 224.0.0.1 is assigned to the permanent group of all IP hosts.

# IGMP
See more in igmp.md

## Short Sum
IGMP stands for Internet Group Management Protocol, it's used by IP hosts to report their host group membership to any neighbouring multicast routers. **Here it's specified as asymetric protocol from the point of view if a host.**

Like ICMP, IGMP is an integral opart of IP, required to be implemented by all hosts conforming L2 of IP multicast specification. Messages are encapsulated in IP datagrams with protocol numer of 2.

## Packet

(Size in bits)

* Version(4): **1** or 0 (obsolete)
* Type(4):
	* *0x11* = Membership query
	* *0x16* = Membership Report
	* *0x17* = Leave Group
	* *0x12* = v1 membership report
* Max Response Time(8): meaningful only in Query packets
* Checksum(16): 
* Group address(32): in a query is zeroed and ignored when received; in a request holds IP host group address

## Used for testing

Multicast ping with [omping](https://linux.die.net/man/8/omping) from the server.

.............. with [iperf](https://gist.github.com/jayjanssen/5697813).