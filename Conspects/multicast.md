# Host Extensions for IP Multicasting

[RFC 1112](https://www.ietf.org/rfc/rfc1112.txt)

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