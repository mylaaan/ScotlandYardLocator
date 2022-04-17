
from Node import Node
from Edge import Edge

class Graph:

    def __init__(self):
        self.node_list = []
        self.currently_possible_node_numbers = []
        self.old_possible_node_numbers = []

    def build_graph(self):
        x = "hallo"





    def add_edge(self, departure, destination, travel_option, x_coordinate = 0, y_coordinate = 0):
        edge = Edge(travel_option, destination)
        if not self.node_list[departure]:
            node = Node(departure, x_coordinate, y_coordinate)
            self.node_list[departure] = node
        self.node_list[departure].add_edge(edge)


    def show_options(self, starting_point, travelmethod):
        self.old_possible_node_numbers.clear()
        self.old_possible_node_numbers = self.currently_possible_node_numbers
        self.currently_possible_node_numbers.clear()
        temp_destination_list = []
        for node_number in self.old_possible_node_numbers:
            if travelmethod == ["black ticket"]:
                temp_destination_list = self.node_list[node_number].destinations_with_travelmethod()
            else:
                temp_destination_list = self.node_list[node_number].destinations_with_travelmethod(travelmethod)
            for i in temp_destination_list:
                if not i in self.currently_possible_node_numbers:
                    self.currently_possible_node_numbers.append(i)

        print("possible locations:")
        print(self.currently_possible_node_numbers)


