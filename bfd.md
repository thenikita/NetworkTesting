# BFD
Original RFCs:
[RFC 5880](https://tools.ietf.org/html/rfc5880)
[RFC 5881](https://tools.ietf.org/html/rfc5881)
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