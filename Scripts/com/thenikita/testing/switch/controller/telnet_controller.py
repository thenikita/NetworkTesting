# thenikita 2018

# below code is designed to perform setting
# actions on some switch via telnet

import telnetlib
from random import randint


class TelnetController:

    switchIp = "10.0.0.231"         # the switch's ip address

    adminVlanIp = "10.0.0.199"      # the vlan's ip from which
                                    # controller is operating

    adminPort = "eth1"              # port with link to the switch

    switchPort = "eth1"

    costs = []

    def __init__(self):

        self.switchIp       = "10.0.0.231"
        self.adminVlanIp    = "10.0.0.199"
        self.adminPort      = "eth1"
        self.switchPort     = "eth1"


    def InitController(self):

        need = raw_input("Wanna init controller?(y/N)")

        if need == "y":

            aIp =   raw_input("Admin VLAN IP: ")
            aPort = raw_input("Admin (server) Port: ")
            sIp =   raw_input("Switch IP: ")
            sPort = raw_input("Switch port: ")

            self.SetAdminIp     (aIp)
            self.SetAdminPort   (aPort)
            self.SetSwitchIp    (sIp)
            self.SetSwitchPort  (sPort)


    def Connect(self):

        self.tnConnection = telnetlib.Telnet(self.switchIp, 23)

        self.tnConnection.read_until(':')

        print("Connected")


    def Close(self):

        self.Write('end')

        self.tnConnection.close()

        print("Exit")


    def Write(self, what, until = "#"):

        self.tnConnection.write(what + "\r")
        self.tnConnection.read_until(until)


    def Read(self):

        self.tnConnection.write("show version")
        print(self.tnConnection.read_some())


    def ResetSwitchSettings(self):

        pass


# All setups are going from root menu mode


    def SetupStp(self, priority, ports):

        self.Write("configure")

        self.Write("spanning-tree")

        self.Write("spanning-tree priority %s" % priority)

        self.SetupStpPortCosts(ports)


    def SetupStpPortCosts(self, ports):

        for i in ports:

            cost = randint(0, 200000000)
            self.costs.append(cost)

            self.Write("interface ethernet %i" % i)
            self.Write("spanning-tree cost %i" % cost)

        print(self.costs)


    def GetSwitchPort(self):         return int(self.switchPort[3])

    def GetSwitchIp(self):           return self.switchIp

    def GetAdminIp(self):            return self.adminVlanIp

    def GetAdminPort(self):          return self.adminPort

    def SetSwitchPort(self, sp):     self.switchPort  = sp

    def SetSwitchIp(self, si):       self.switchIp    = si

    def SetAdminPort(self, ap):      self.adminPort   = ap

    def SetAdminIp(self, ai):        self.adminVlanIp = ai


    def ShowController(self):

        print(
            "switch ip:             {0}\n"
            "switch port:           {1}\n"
            "admin vlan ip:         {2}\n"
            "admin server port:     {3}\n"
            .format(
                self.switchIp,
                self.switchPort,
                self.adminVlanIp,
                self.adminPort))

        # TODO add info about connection destination


if __name__ == '__main__':

    tnController = TelnetController()

    tnController.SetupStpPortCosts([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
