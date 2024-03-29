
class RIPPacket(object):
    def __init__(self, command, router_id, rip_entries):
        self.command = command
        self.version = 2
        self.router_id = router_id
        self.rip_entries = rip_entries

    def getCommand(self):
        return self.command

    def getVersion(self):
        return self.version

    def getRouterId(self):
        return self.router_id

    def getRIPEntries(self):
        return self.rip_entries



