class Node:

    def __init__(self, number, x, y):
        self.number = number
        self.edge_list = []
        self.x = x
        self.y = y

    def give_node_string(self):
        return "n" + self.number

    def destinations_with_travelmethod(self, travelmethod = ["taxi", "bus", "underground", "boat"]):
        destinations = []
        for edge in self.edge_list:
            for method in travelmethod:
                if method in edge.travelmethod:

                    destinations.append(edge.destination)
        return destinations

    def add_edge(self, edge):
        self.edge_list.append(edge)

    def __str__(self):
        return str(self.edge_list)
