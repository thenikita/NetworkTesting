# BFD
Original RFCs:
[RFC 5880](https://tools.ietf.org/html/rfc5880) |
[RFC 5881](https://tools.ietf.org/html/rfc5881) |
[RFC 5882](https://tools.ietf.org/html/rfc5882)

## Short Summary
BFD stands for Bidirectional Forwarding Detection. The goal of BFD is to provide low-overhead, short-duration detection of failures in the path between adjacent forwarding engines. An additional goal is to provide a single mechanism that can be used for liveness detection over any media, at any protocol layer, with a wide range of detection times and overhead, to avoid proliferation of different methods.

## Functioning
There're two functioning modes:
* Asynchronous
* Demand

## BFD Control Packet
**Generic**
* Version
* Diagnostic
* State
* Poll
* Final
* Control Plane Independent
* Auth Present
* Demand
* Multipoint
* Detect Mult
* Lenght
* My Discriminator
* Your Discriminator
* Desired Min TX Interval
* Required Min RX Interval
* REquired Min Echo RX Enterval
* Auth type
* Auth len

**Simple Password Auth Section**

If auth present bit is set in the header, and auth type is 1, the auth section has the format:

* Auth type = *1 octet*
* Auth len = *1 octet*
* Auth key ID = *1 octet*
* Password = *1 octet*

**Keyed MD5 and Meticulous Keyed MD5 Ayth Section**

* Auth type = *1 octet*
* Auth len = *1 octet*
* Auth key ID = *1 octet*
* Reserved *1 octet*
* Sequence number = *4 octets*
* Auth key = *4 octets*

**Keyed SHA1 and Meticulous SHA1 Auth Section**
Same as fot MD5 sum

## BFD Echo Packet Format
These packets are encapsulated to the environment so should look at concrete application douments.

## Elements of procedure
It's important to enforce only requirements specified below (RFC5880 section 6) to prevent unexpected disoperability.

A system can take either an active or passive role is session initialization, so it will or will not initiate BFD resending. At least one system must take active role. Session begins with slow periodic transmission of BFD control packets to achieve bidirectional communication.

Once session is up, a system can chose to start the Echo function //or something else what isn't clear in doc (RFC 5880 p.15). If Echo is inactive, the transmission rate can be increased. Also, system may signal that it has entered Demand mode.

If Demand mode isn't active and there're no control packets in calculated Detection time, the session is declared down. If sufficient Echo packets are lost, the session is declared down as well. If Demand mode is active and no appropriate Control packets are received in responce to a Poll sequence, the session is declared down.

If the session goes down, the transmission of Echo packets ceases and Control packets' transmission  rate goes slow.

A session can be kept down by using AdminDown state.

## IANA Considerations

**Diagnostic codes**

Value | Code name

	0. No diagnostic
	1. Control detection time expired
	2. Echo function failed
	3. Neighbour signaled session down
	4. Forwarding plane failed
	5. Path down
	6. Concatenated path down
	7. Administratively down
	8. Reverse concatenated path down
	9. and higher to 31 are unassigned


**Auth types**

Value | Code name

	0. Reserved
	1. Simple password
	2. Keyed MD5
	3. Meticulous Keyed MD5
	4. Keyed SHA1
	5. Meticulous Keyed SHA1
	6. and higher to 255 are unassigned
 
# For multihop paths 
The part below describes the content of the RFC 5881.

This protocol is called unusable for over-internet transmission because of its simpleness.

There issues for BFD using multihop path:
	1. Security and spoofing
	2. Demultiplexing multiple BFD sessions between the same pair of systems
	3. Echo function mustn't be used over multiple hops

At the document some kind of solutions are presented, not so long to read there.

There is a **IANA consideration** that port 4784 has been assigned for use with BFD MHop Control.

# Generic Application of BFD

The part below describes the content of RFC 5882.

All the info is pretty concrete, no idea if need it later.

At least it's used for OSPF Virtual links' failure detection.

Also, it's used with BGP for faster triggering topology changes.