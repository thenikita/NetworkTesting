# OSPF
[Original RFC 1247](https://tools.ietf.org/html/rfc1247)
For now document doesn't look so much systemized but in future edits this trouble should be fixed. Any requests are appreciated. Also, feel free to **contact me** if you found any bad info, typos etc. 

## Short Summary
OSPF is a link-state based routing protocol.  It is designed to be run internal to a single Autonomous System. Each OSPF router maintains an identical database describing the Autonomous System's topology. From this database, a routing table is calculated by constructing a shortest-path tree.
### Terms

**Basic:**
* *link/ interface*
* *metric*
* *cost*
* *autonomus system, AS* -- a group of routers exchanging via a common routing protocol.

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

## Main
### Supported Networks:
* P2P
* broadcast
* non-broadcast

### Getting Ready
Routers connects, resending hello messages, making adjacencies. After all information is set every router creates routing table with itself as the root.

External ruting info originates from another protocol e. g. EGP.

OSPF can calculate a separate set of routes for an IP type of service.

### Splitting an AS into Areas
Each area has its own SPF algorithm, so own topological DB and graph. This topology is invisible from the outside.

### Backbone
The bb consists of networks not contained in any area, their routers and routers that belongs to multiple areas. Some areas can be uncontigious with backbones physically, so there's need to make logical connection (virtual link). BB is responsible for distributing routing information between areas. BB's topology is invisible for all areas, but BB can see all the topologies.

### Routers' Classification
* *Internal* -- router inside the area, only backbone iface routers.
* *Area border* -- router attached to multiple areas.
* *Backbone* -- router with an iface to the backbone. Includes all multi-area routers.
* *AS boundary* -- exchanges routing info with routers from other autonomous systems.

### IP Subnetting Support
Takes place but seems nothing interesting now.

An area can be configured as a stab only if there's only one exit point for it OR when 'the choice of exit point need not be made on a per-external-destination basis' (WTF?).

### Routing Protocol Packets
OSPF runs directly over IP type 89. Large packets can be divided into smaller ones what's recommended. 

**OSPF packet types:**
* *Hello* = **1** = discover neighbours
* *Database description* = **2** = summarize DB contents
* *Link state request, LSR* = **3** = download DB
* *Link state update, LSU* = **4** = update DB
* *Link state acknowledge* = **5**

**LSA types:**
* (1) *Router links* -- originated by any router. describes the collected states of the router's interfaces to an area. Throughout a single area only.
* (2) *Network links* -- originated by DR for multi-access nets. contains the list of routers connected to a the network. single area only.
* (3, 4) *Summary link* -- originated by area borders for their associated area. edscribes a route to a distination outside the area. 3 describes routes to networks, 4 describes routes to AS boundary routers.
* (5) *AS external* -- oroginates by AS boundary routers to the AS. describes a rout ti a destination in another AS.

### Implementation Requiriments
Not very important thing for now but may be useful later...
* Timers
* IP multicast
* Lower-level protocol
* List manipulation primitives
* Tasking support

## Data Structures
### Protocol, Area, Interface, Neighbour
Big shit, too lazy to conspect it cuz it looks useless for now.

## Interface States
State types:

* **Down**
* **Loopback**
* **Waiting**
* **P2P**
* **DR Other**
* **Backup**
* **DR**

Events causing state changes:

* **Interface up** -- Down -> ...
* **Wait timer** -- ... -> DR
* **Backup seen** -- waiting -> ...
* **Neighbour change** -- (B)DR changes
* **Loop ind**, **Unloop Ind**
* **Interface Down**

Detailed event behaviour can find in referred RFC on p.48-50

## Brinbging up Adjacencies
**Hello Protocol** is responsible fir establishing and maintaining neighbour relationships. Sent periodically. In multi-access networks HP elects the Designated Router. Among other networks HP controls the adjacencies. After neighbours are found and DR is set it's time to bring up an adjacency. The first step in this direction is to sync DBs.

In OSPF only adjacent routers must be syncronised. Each router sends packs that describes it's DB. A neighbour can update his DB if find newer advertisement. This DB exchange is over when a router gets packet with 'M-bit off'.

## Designated Router
DR performs 2 main finctions:
* originates a network lonks advertisement on behalf of the network.
* becomes adjacent to all other routers on the network. After DBs are initially synced, the DB plays a central part in syncronisation process. A backup unit is the BDR which behaves after DR becomes dead.

### Electing the DR
RFC's p.51-52

## Neighbour States
State types:
* **Down**
* **Attempt**
* **Init** 
* **2-Way**
* **ExStart**
* **Exchange**
* **Loading**
* **Full**

Events causing state changes:
* **Hello received**
* **Start**
* **2-Way received**
* **Negotioation Done**
* **Exchange done**
* **BadLSReq**
* **Loading done**
* **AdjOK**
* **Seq Number Mismatch**
* **1-Way**
* **KillNbr**
* **Inactivity timer**
* **LLDown**

Detailed event behaviour can find in referred RFC on p.61-66

## Whether to become adjacement
An adjacement shouldbe established when:
* The underlying network is p2p
* The underlying network is virtual link
* The router itself or the neigbour is DR or BDR

## Packet Processing
**Sending**

Packets are sent between adjacencies only. Header contains fields:
* Version
* Packet type
* Packet length
* Router ID (sender)
* Are ID
* Checksum
* Autype & Authentification

Packets in multicast networks are send as multicast except for LSUs -- they're always unicast.

IP source must be set as sending interface's IP.

**Receiving**

Ti be accepted at IP level packet should have:
* correct IP checksum
* destination IP same as address of receiving port
* Protocol must be specified as OSPF
* The source IP address should be examined to make sure this isn't a multicast packet.
* Version of protocol == 2
* 16-bit checksum verified (excluding auth field) 
* verified area ID: recieving interface's area ID or backbone ID
* ALLDRouters packets accepts only if state of receiving interface is DR or backup
* auth type must match to area's AT

If everything OK, the pack will be accepted. Now it must be authenticated. Auth procedure may use auth key which pre-configured for area. If there's Hello packet it will be processed by the hello protocol.

## Routing table structure
There's a single table in eash router. The fields of the table are:
* *Destination type*:
	* Network
	* Area border router
	* AS boundary router
* Destination ID
* Address mask
* Optional capabilities
* TOS
* Area
* Path type
* Cost
* Type 2 cost
* Link state Origin
* Next hop
* Advertising router

## Routing table lookup
1. Select the set of matching entries.
2. Check if destination IP's in configured area address range.
3. Reduce set of entries by selecting more suitable path-type.
4. Select most specific (concrete) match from the entries.
5. Select entries which TOS matches to it from the packet.

## Events causing LSA origination
* The LS refresh timer firing.

If the content of advertisement is different:
* Interface's state changing
* DR changing
* Neighbour state changing to/from FULL

For area border routers only:
* An intra-route changing
* An inter-route changing
* New router attaching

For AS boundary routers only:
* External route gained with an external routing protocol.

## Building the list of link recoreds
Relevant Link IDs see in the RFC p.93-94
* If the attached network doesn't belong to area A, no links are added to advertisement, and the next interface should be examined.
* Else if the state of the interface is down no links are added.
* Else if the state of the iface is p2p, add links according to:
	* If the neighbouring router is fully adjacent, add type 1 (p2p) link or type 4 (virtual link) if this is rigth interface.
	* If this is not listed above, add type 3 (stub net) link.
* Else if the state is loopback, add type 3 link.
* Else if waiting, add type 3 link.
* If the router is fully adjacent to the DR or DR itself, add type 2 link. else, add link as if interface state were waiting.

## Link types
* Router
* Network
* Summary
* AS external links

## Flooding

## Aging LSDB

## Virtual links

## Calculation of the Routing Table
* The present RT is invalidating
* The intra-area routes are calculating
* The inter-area routes are calculating
* For virtual link entries next hop is calcilating
* Routes to external destinations are calculating

## Linked Scripts
None of them now.
