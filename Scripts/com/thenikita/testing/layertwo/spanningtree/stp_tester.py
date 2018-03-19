# STP tester

# from scapy import *
import keyboard as keyboard
from scapy.all import *
from scapy.layers.inet import *
from com.thenikita.testing.switch.controller.telnet_controller import *

TIMEOUT = 1
SRC_MAC = "00:00:bb:00:00:02"
ASSUMING_ROOT_MAC = "00:00:bb:00:00:02"

_rootlist = []
_countlist = []
_packlist = []

_modes = [ "normal",
           "twoswitches",
           "guard",
           "all"]

_testmode = ""

_freeports = [ "eth1",
               "eth2",
               "eth3",
               "eth4",
               "eth5",
               "eth6",
               "eth7",
               "eth8",
               "eth9",
               "eth10",
               "eth11",
               "eth12",
               "eth13",
               "eth14",
               "eth15"]


def SniffForBPDU():

    print("[Sniffing]")

    bpdus = []

    while not keyboard.is_pressed("s"):

        sniffedPackets = sniff(timeout = TIMEOUT)

        bpdus += sniffedPackets.filter(lambda x: not x.haslayer(Ether))

        print(
            '    There are totally {0} BPDUs:'
            .format(len(bpdus)))

    return bpdus



def AnalyseFoundBPDUs(bpdus):

    print "[Analysing]"

    bpdus = PickBPDUsBySource(bpdus)

    FindRoot(bpdus)


def PickBPDUsBySource(bpdus):

    print "....[Picking]"
    temp = []

    for pack in bpdus:

        if (SRC_MAC != pack.src) & (pack.haslayer(STP)):

            temp += pack

    return temp


def FindRoot(bpdus):

    print("....[Rooting]")

    if len(bpdus) == 0:

        print "      Cannot resolve root. There are no packs from src."

    else:

        for pack in bpdus:

            i = FindExistedRoot(_rootlist, pack[STP].rootmac)

            if i == -1:

                _packlist.append(pack)
                _rootlist.append(pack[STP].rootmac)
                _countlist.append(1)

            else:

                _packlist[i] = pack
                _countlist[i] += 1

        for j in range(0, len(_rootlist)):

            print(
                "        ROOT: {0} x {1} times"
                .format(_rootlist[j], _countlist[j]))


def FindExistedRoot(rootlist, target):

    for i in range(0, len(rootlist)):

        if target == rootlist[i]:

            return i

    return -1


def CreateSniffReport():
    pass


def mainNormal():

    print "Initial sniffing:"

    bpdus = SniffForBPDU()

    AnalyseFoundBPDUs(bpdus)


def mainTwoSwitches():

    switchOne = TelnetController()
    switchTwo = TelnetController()

    portsOne = _freeports
    portsTwo = _freeports

    ConnectControllers(switchOne, switchTwo)

    portsOne.remove(switchOne.GetSwitchPort())
    portsTwo.remove(switchTwo.GetSwitchPort())

    # TODO fix removing ports above

    DefineAvailablePorts(portsOne, portsTwo)


def ConnectControllers(switchOne, switchTwo):

    print("Connecting to switches")

    try:

        switchOne.InitController()
        switchTwo.InitController()

        switchOne.ShowController()
        switchTwo.ShowController()

        print("Connected")

    except Exception as exc:

        print(exc)


def DefineAvailablePorts(portsOne, portsTwo):

    need = raw_input("Need to delete additional ports? (y/N)")

    if need == "y":

        pass

    # TODO add removing ports from available


def mainGuard():

    pass


if __name__ == "__main__":

    _testmode = raw_input(
            "Enter the mode ({0}): "
            .format(_modes))

    if (_testmode == "normal") | (_testmode == "1"):

        mainNormal()

    if (_testmode == "twoswitches") | (_testmode == "2"):

        mainTwoSwitches()

    if (_testmode == "guard") | (_testmode == "3"):

        mainGuard()

    if (_testmode == "all") | (_testmode == "4"):

        mainNormal()
        mainTwoSwitches()
        mainGuard()
