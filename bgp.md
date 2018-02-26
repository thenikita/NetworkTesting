# BGP
[Original RFC](https://tools.ietf.org/html/rfc4271)

## Short Summary
BGP stands for Border Gateway Protocol -- inter-autonomous system routing protocol. The primary function of BGP is to exchange network reachability information with other BGP systems. BGP-4 provides a set of mechanisms for supporting Classless Inter-Domain Routing (CIDR).

## Commonly Used Terms
**Adj-RIB-In** contains unprocessed routing information that has been advertised to the local BGP speaker by its peers.

**Adk-RIB-out** contains the routes for advertisement to specific peers by means of the local speaker's update messages.

**Autonomous System** -- a set of routers under a single technical administration, using an interior gateway protocol and common metrics to determine intra-routing. Also there's a defenition in the OSPF documentation.

**BGP Identifier** -- 4-octet unsigned integer that indicates the sender of BGP messages.

**BGP Speaker** -- a router that implements BGP.

**EBGP** -- external BGP.

**External peer** -- per that is in a different AS.

**Feasible route** -- an advertised route that is available for use to recepient.

**IBGP** -- Internal BGP.

**Internal peer**

**IGP** -- Interior gateway protocol -- a routing protocol used to exchange routing data within a single AS.

**Loc-RIB** -- contains the routes that have been selected by the local BGP speaker's decision process.

**NLRI** -- network layer reachability information.

**Route**

**RIB** -- routing information base.

**Unfeaseble route**

## Routing Information Base
Consists of 3 parts:
1. Adj-RIB-in
2. Loc-RIB
3. Adj-RIB-out

## Message Format
Header:
* Marker = 16 octets
* Length = 2 octets
* Type = 1 octet

### Messages
**Open message**

First message after opening connection.

* Version
* My autonomous system
* Hold time
* BGP identifier
* Optional params length
* Optional parameters

**Update message**

Used to transfer routing information.

* Withdraw routes length
* Withdraw routes
* Total path attribute length
* Path attributes

**Keepalive message**

KA messages are exchanged often enough to prevent timer expiration.

Consists of only the message header and has a length of 19 octets.

**Notification message**

Sends when an error condition is detected.

In addition to header it has
* Error code
* Error subcode
* Date

## Path Attributes

* ORIGIN
* AS_PATH
* NEXT_HOP
* MULTI\_EXIT_DISC
* LOCAL_PREF
* ATOMIC_AGGREGATE
* AGGREGATOR

## Error Handling
If error detected, a notification message sent with relevant error code etc.

**Message Header**
**Open message**
**Update message**
**Notification message**
**Hold timer expired**
**Finite state machine**
**Cease**
**BGP Connection collision**

## BGP Finite State Machine
Doesn't seem to be useful now.

## Update Message Handling
Same here.

## BGP Timers
Same here.