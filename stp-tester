#! /bin/bash
if [[ ! -z $1 ]]; then
	device="$1"
else echo "error"
fi
echo "$1"
if [[ ! -z $2 ]]; then
	rootpc="$2"
else echo "error"
fi
echo "$2"
if [[ ! -z $3 ]]; then
	smac="$3"
else echo "error"
fi

dmac=01:80:C2:00:00:00  # destination MAC (default - 01:80:C2:00:00:00)
proto_id=0000           # Protocol Identifier (hex, 2 bytes)
proto_v_id=00           # Protocol Version Identifier (hex, 1 byte)
bpdutype=00             # BPDU type (hex, 1 byte)
flags=00                # flags value (hex, 1 byte)
rootid=0100002590ed20dF # Root Identifier (hex, 8 bytes)
brid=1000002590ed20d4   # Bridge Identifier (hex, 8 bytes)
portid=7002             # Port Identifier (hex, 2 bytes)
mage=0000               # Message Age (hex, 2 bytes)
maxage=1400             # Max Age (hex, 2 bytes)
hellotime=0200          # Hello Time (hex, 2 bytes)
fdelay=0f00             # Forward Delay (hex, 2 bytes)
 
echo "tester"|sudo -S  stp-bin -v -dev $device -dmac $dmac -smac $smac -protoid $proto_id -protovid $proto_v_id -bpdu $bpdutype -flags $flags -rootid $rootid -rootpc $rootpc -brid $brid -portid $portid -mage $mage -maxage $maxage -htime $hellotime -fdelay $fdelay
