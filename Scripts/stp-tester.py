# STP tester

#from scapy import *
import keyboard as keyboard
from scapy.all import *
from scapy.layers.inet import *
from scapy.layers.all import *


TIMEOUT = 5
SRC_MAC = "00:00:bb:00:00:02"


def SniffForBPDU():

    print("Sniffing now...")

    bpdus = []

    while not keyboard.is_pressed("s"):

        sniffedPackets = sniff(timeout = TIMEOUT)

        bpdus += sniffedPackets.filter(lambda x: not x.haslayer(Ether))

        print('\nThere are totally {0} BPDUs:'.format(len(bpdus)))


    for pack in bpdus:

        print('From {0} to {1}'.format(pack.src, pack.dst))

    return bpdus



def AnalyseFoundBPDUs(bpdus):

    for pack in bpdus:

        if SRC_MAC == pack.src:

            pack[STP].show()

            ## here's the stp data analysis depending on what we want

            print("Found! ")

def main():

    bpdus = SniffForBPDU()

    AnalyseFoundBPDUs(bpdus)



if __name__ == "__main__":

    main()

