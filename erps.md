# ERPS
Original:
[ITU-T G.8032](https://www.itu.int/rec/T-REC-G.8032-201508-I)

## Short summary
ERPS stands for ethernet ring protection switching. The fundamentals of ring protection architecture:
* the principle if loop avoidance
* the utilization of learning, forwarding and filtering DB mechanisms

Multiple-ring system takes place if these principles are adhered to:
* R-APS channels are not shared across Ethernet ring interconnections
* on each ring port, each traffic channel and R-APS channel are controlled by the Ethernet ring protection control process of only one Ethernet ring
* each major ring or sub-ring must have its own RPL

## Terms

* Adapter information
* Characteristic information
* Link
* Tandem connection
* Trail

* Defect
* Failure
* Server signal fail = *SSF*
* Signal degrade = *SD*
* Signal fail = *SF*
* Trail signal fail = *TSF*

* Transfer time = *T_t*

* Adaptation
* Flow
* Layer network
* Network
* Port
* Transport
* transport entity

* Hold-off time
* Non-revertive (protection) operation
* Protected domain
* Protection
* Protection transport entity
* Revertive (protection) operation
* Signal
* Switch
* Switching time
* Wait-to-restore time
* Working transport entity

* ERP instance
* Ethernet ring
* Ethernet ring node
* Interconnection node
* Maintenance entity = *ME*
* Maintenance entity group = *MEG*
* Major ring
* MEG end point = *MEP*
* R-APS virtual channel
* ring MEL
* Ring protection link = *RPL*
* RPL neighbour node
* RPL owner node
* sub-ring
* Sub-ring link
* Wait to block timer

## Abbreviations

* **AI** -- adaptive information
* **APS** -- Automatic protection switching
* **BPR** -- Blocked port reference
* **CCM** -- continuity check message
* **TCM** -- tandem connection monitoring
* **NR** -- no request
* **FS** -- forced switch
* **MS** -- manual switch
* **ERP** -- ethernet ring protection
* **CI**
* **DNF**
* **E-LAN**
* **EPL**
* **ERP**
* **ETH** -- ethernet layer network
* **ETHDi**
* **ETY**
* **EVPL**
* **FDB**
* **FF** -- flow forwarding
* **FOP-PM**
* **FOP-TO**
* **FP**
* **FS**
* **GFP**
* **ID**
* **MAC**
* **MEG** **MEL** **MEP**
* **MI**
* **MPLS**
* **MS**
... and other ...

## Ring protection characteristics
### Monitoring methods and conditions
ERP may adopt any of the following methods:
* Inherent -- the fault conbdition status of each ring link connection is derived from the status of the underlying server layer trail
* Sub-layer -- each rin glink is monitored using TCM
* Test trail -- defects are detected using an extra test trail
### Ethernet traffic and bandwith

### Ethernet ring protection switching performance
Some numbers, if interested watch the original document.

## Ring protection conditions and commands
* *SF* -- when an SF condition is detected on a ring link and it's determined to be a stable failure
* *NR* -- the condition when no local protection switching requests are active
* *FS* -- this command forces a block on the ring port where the command is issued
* *MS* -- this command forces a block on the ring port where the command is issued in the absence of a failure or FS
* *Clear* -- used for:
	a. clearing an active local administrative command
	b. triggering reversion before the wait to restore or wait to block timer expires in the case of revertive operation
	c. thiggering reversion in the case of non-revertive operation

* *Lockout of protection* -- disables the protection group
* *Replace the RPL* -- moves the RPL by blocking a different ring link and unblocking the RPL permanently
* *Exercise signal* -- of the R-APS protocol

## Ring protection archtectures
### REvertive and Non-revertive Switching
In revertive operation traffic channel restored to the RPL while error condition is active. After defect is cleared, traffic channel reverts. In non-reversive operation traffic channel continues to use the RPl.

### Protection Switching Triggers
* SF is declared on one of the ring links and the detected SF condition currently has the highest priority
* the received R-APS message requests to switch and it has the highest priority
* initiated by operator control and has the highest priority

###Protection Switching Models on a Single Ethernet Link
Scheme pictures in teh doc.

### Traffic Channel Blocking