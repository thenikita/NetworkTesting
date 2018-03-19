# thenikita 2018

# below code is designed to perform setting
# actions on some switch via telnet

import telnetlib


class TelnetController:

    switchIp = "10.0.0.231"         # the switch's ip address

    adminVlanIp = "10.0.0.199"      # the vlan's ip from which
                                    # controller is operating

    adminPort = "eth1"              # port with link to the switch

    switchPort = "eth1"

    def __init__(self):

        temp = \
            raw_input(
                "IP to connect (or default {0})"
                .format(self.switchIp))

        if temp != "":
            self.switchIp = temp


        temp = \
            raw_input(
                "From this vlan IP (or default {0})"
                .format(self.adminVlanIp))

        if temp != "":
            self.adminVlanIp = temp


        temp = \
            raw_input(
                "From port (or default {0})"
                .format(self.adminPort))

        if temp != "":
            self.adminPort = temp


        temp = \
            raw_input(
                "Enter the port on switch using telnet (def is {0})"
                .format(self.switchPort))

        if temp != "":
            self.switchPort = temp


        self.ShowController()

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


    def SetupStp(self, priority):

        self.Write("configure")

        self.Write("spanning-tree")

        self.Write("spanning-tree priority %s" % priority)


    def SetupGuard(self):

        pass


    def ShowController(self):

        print(
            "switch ip: {0}\n"
            "vlan ip:   {1}\n"
            "port:      {2}\n"
            .format(self.switchIp, self.adminVlanIp, self.adminPort))

        # TODO add info about connection destination


if __name__ == '__main__':

    controller = TelnetController()
    controller.Write("show version")
