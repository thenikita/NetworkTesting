# Ethernet OAM aka Connectivity Fault Manager

## Sources
[Cisco Article](https://www.cisco.com/c/en/us/td/docs/optical/15000r9_0/ethernet/454/guide/45490ethernetguide/45490a_eoamonmlmr.pdf)

[About OAM](http://blog.sbolshakov.ru/12-ethernet-oam/)


## Short Summary
OAM stands for Operation, Administration and Maintenance. *In case of lack of free money for capitalism's shit there won't be link to original document, cuz it's unreachable.* The document itself describes Fault Manager, so I tried to collect some information about it. (802.1ah - OAM, 802.1ag - CFM)


## Ethernet CFM
ECFM is an endtoend per-service-instance EOAM protocol. It includes proactive connectivity monitoring, fault verification and fault isolation  for large Ethernet metropolitan-area networks and WANs. 802.3ah OAM is a single-hop per-physical-wire protocol, unlike ECFM (but it's out of scope of this page).

## Concepts for understanding CFM

### Ethernet CFM Support on the ML-MR-10 Card
Ethernet CFM on the ...card provides:
* end-to-end service-level OAM technology
* Support for both distribution and access network environments with the outward facing MEPs enchacement
* Support for interoperability with CPP
* Support for QOS on CFM packets


### Customer Service Instance
A customer service instance is an Ethernet virtual connection which is edentified by a S-VLAN within an Ethernet island and is identified by a globally unique service ID. Can be point2point or multipoint2multipoint.


### Maintenance Domain
A maintenance domain is a management space for managing and administering a network. MD has a inique maintenance level in the range of 0 to 7 assigned by admin. Domains must not intersect, but may nest or touch.


### Maintenance Point
Maintenance point is a demarcation point on an interface that participates in CFM within a maintenance domain. MP on device ports act as filters for decline CFM frames from wrong domains. They drop lower-level and forward higher-level frames.
* Maintenance end points (MEPs) -- inward-facing points at the edge defining the boundary. Inward means that they communicate through the relay function side and not the wire side.
* Maintenance intermediate points (MIPs) -- internal to a domain and respond to CFM only when triggered by traceroute and loopback messages.


### CFM Messages
CFMM are standard ETher frames. Routers can support only limited CFM functions. Bridges that cannot interpret CFM messages forfard them as normal frames. **CFMs encapsulate in 802.1Q tag.**

Tree types of messages:
* Continuity check (possible errors below)
	* *MEP Up*
	* *MEP Down*
	* *Cross connect*
	* *Config error*
	* *Forwarding loop*
* Loopback: Reply, Messaqge
* Traceroute: R, M

## CFM Config guidlines
full ones at Cisco's Article p. 34-14