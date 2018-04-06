import routing_row


class RoutingTable(object):

    def __init__(self, data):
        self.routing_id = data["router-id"]
        self.input_ports = data["input-ports"]
        self.output_ports = data["outputs"]
        self.table = []
        self.populateTable()
        print(self.table)
    def populateTable(self):
        self_entry = routing_row.RoutingRow(0, 0, 0, self.routing_id, 0)
        self.table.append(self_entry)
        output_list = self.output_ports.split(', ')

        for i in output_list:
            values = i.split('-')
            nextHopPort = values[0]
            linkCost = values[1]
            destId = values[2]
            learnedFrom = 0  # As it was learned from ConfigFile

            row = routing_row.RoutingRow(nextHopPort, destId, linkCost, destId, learnedFrom)
            self.table.append(row)

    def getRoutingTable(self):
        return self.table

