# IGMV v2
More in [multicast.md](./multicast.md)

## Summary
IGMP is used by IP hosts to report their multicast group membership to any immediately-neighbouring routers.
IGMPv2 allows group membership termination to be quickly reported to the routing protocol.

## Packet
* **Type** *1 octet*: 0x11 = query, 0x16 = v2 membership report, 0x17 = leave, 0x12 = v1 membership report
* **MAX response time** *1 octet*: meaningful only in query messages, in 1/10 second.
* **Checksum** *2 octets*:
* **Group address** *4 octets*:

It also may have additional fields in future...

## Possible Host States
* non-member
* delaying member
* idle member