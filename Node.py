from Graph import Graph
from Edge import Edge

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
        for i in self.edge_list:
            if i.travelmethod in travelmethod:
                destinations.append(i.destination)
        return destinations

    def add_edge(self, edge):
        self.edge_list.append(edge)
