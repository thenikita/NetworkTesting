# OSPF

## Short Summary
### Terms
Basic:
* * link/ interface *
* * metric *
* * cost *
* * autonomus system *
OSPF: basic:
* * router ID, RID *
* * area *
* * link-state advertisement, LSA * -- data unit which includes state description of router/net
* * link state database, LSDB * -- base with all LSAs
OSPF: neighbours:
* * neighbour *
* * adjacency *
* * hello protocol *
* * neighbours database *
OSPF: packets:
* * hello *
* * DBD * -- describes LSDB
* * LSR * -- requests full LSA which are currently not in local LSDB
* * LSU * -- sends full LSA info
* * LSAck * -- acknowledge of succesful packet transfer