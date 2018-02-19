# OSPF
[Original RFC 1247](ttps://tools.ietf.org/html/rfc1247#section-3.5)
For now document doesn't look so much systemized but in future edits this trouble should be fixed. Any requests are appreciated. Also, feel free to **contact me** if you found any bad info, typos etc. 

## Short Summary
OSPF is a link-state based routing protocol.  It is designed to be run internal to a single Autonomous System. Each OSPF router maintains an identical database describing the Autonomous System's topology. From this database, a routing table is calculated by constructing a shortest-path tree.
### Terms

**Basic:**
* *link/ interface*
* *metric*
* *cost*
* *autonomus system, AS*

**OSPF: basic:**
* *router ID, RID*
* *area*
* *link-state advertisement, LSA* -- data unit which includes state description of router/net
* *link state database, LSDB* -- base with all LSAs

**OSPF: neighbours:**
* *neighbour*
* *adjacency*
* *hello protocol*
* *neighbours database*

**OSPF: packets:**
* *hello*
* *DBD* -- describes LSDB
* *LSR* -- requests full LSA which are currently not in local LSDB
* *LSU* -- sends full LSA info
* *LSAck* -- acknowledge of succesful packet transfer

## The subject
### OSPF supports networks:
* P2P
* broadcast
* non-broadcast

### Getting ready
Routers connects, resending hello messages, making adjacencies. After all information is set every router creates routing table with itself as the root.

External ruting info originates from another protocol e. g. EGP.

OSPF can calculate a separate set of routes for an IP type of service.

### Splitting an AS into Areas
Each area has its own SPF algorithm, so own topological DB and graph. This topology is invisible from the outside.

### Backbone
The bb consists of networks not contained in any area, their routers and routers that belongs to multiple areas. Some areas can be uncontigious with backbones physically, so there's need to make logical connection (virtual link). BB is responsible for distributing routing information between areas. BB's topology is invisible for all areas, but BB can see all the topologies.

### Routers' classification
* *Internal*
* *Area border*
* *Backbone*
* *AS boundary*

### IP subnetting support
Takes place but seems nothing interesting now.

An area can be configured as a stab only if there's only one exit point for it OR when 'the choice of exit point need not be made on a per-external-destination basis' (WTF?).

### Routing protocol packets
OSPF runs directly over IP type 89. Large packets can be divided into smaller ones what's recommended. 

**OSPF packet types:**
* *Hello* = **1** = discover neighbours
* *Database description* = **2** = summarize DB contents
* *Link state request, LSR* = **3** = download DB
* *Link state update, LSU* = **4** = update DB
* *Link state acknowledge* = **5**

**LSA types:**
1. (1) *Router links* -- originated by any router. describes the collected states of the router's interfaces to an area. Throughout a single area only.
1. (2) *Network links* -- originated by DR for multi-access nets. contains the list of routers connected to a the network. single area only.
1. (3, 4) *Summary link* -- originated by area borders for their associated area. edscribes a route to a distination outside the area. 3 describes routes to networks, 4 describes routes to AS boundary routers.
1. (5) *AS external* -- oroginates by AS boundary routers to the AS. describes a rout ti a destination in another AS.

### Implementation requiriments
Not very important thing for now but may be useful later...
* Timers
* IP multicast
* Lower-level protocol
* List manipulation primitives
* Tasking support

## Data structures
### Protocol, Area
Big shit, too lazy to conspect it cuz it looks useless for now.

## Brinbging up adjacencies
**Hello Protocol** is responsible fir establishing and maintaining neighbour relationships. Sent periodically. In multi-access networks HP elects the Designated Router. Among other networks HP controls the adjacencies. After neighbours are found and DR is set it's time to bring up an adjacency. The first step in this direction is to sync DBs.

## Linked scripts
None of them now.