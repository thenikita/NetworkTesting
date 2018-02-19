# OSPF

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
Takes place but seems nothing interesting now

> test shit
> some more of it