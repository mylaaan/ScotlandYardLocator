from Node import Node
from Edge import Edge


class Graph:


    def __init__(self):
        self.node_list = []
        self.currently_possible_node_numbers = []
        self.old_possible_node_numbers = []

    def add_edge(self, departure, destination, travel_option, x_coordinate=0, y_coordinate=0):
        edge = Edge(travel_option, destination)
        if len(self.node_list) <= departure:
            node = Node(departure, x_coordinate, y_coordinate)
            self.node_list.insert(departure, node)
        self.node_list[departure].add_edge(edge)

    def show_options(self, starting_point, travelmethod):
        if not self.old_possible_node_numbers:
            self.old_possible_node_numbers.append(starting_point)
        else:
            self.old_possible_node_numbers.clear()
            self.old_possible_node_numbers.extend(self.currently_possible_node_numbers)
            self.currently_possible_node_numbers.clear()
        for node_number in self.old_possible_node_numbers:
            if travelmethod == ["black ticket"]:
                self.currently_possible_node_numbers.extend(self.node_list[node_number].destinations_with_travelmethod())
            else:
                self.currently_possible_node_numbers.extend(self.node_list[node_number].destinations_with_travelmethod(travelmethod))

        self.currently_possible_node_numbers = list(dict.fromkeys(self.currently_possible_node_numbers))
        return self.currently_possible_node_numbers


    def build_graph(self):
        boat = ["boat"]
        taxi = ["taxi"]
        bus = ["bus"]
        underground = ["underground"]
        taxi_bus = ["taxi", "bus"]
        bus_underground = ["bus", "underground"]
        self.add_edge(0, 0, taxi)
        self.add_edge(1, 8, taxi_bus)
        self.add_edge(1, 9, taxi)
        self.add_edge(1, 46, bus_underground)
        self.add_edge(2, 10, taxi)
        self.add_edge(2, 20, taxi)
        self.add_edge(3, 4, taxi)
        self.add_edge(3, 11, taxi_bus)
        self.add_edge(4, 3, taxi)
        self.add_edge(4, 13, taxi)
        self.add_edge(5, 15, taxi)
        self.add_edge(5, 16, taxi)
        self.add_edge(6, 7, taxi)
        self.add_edge(6, 7, taxi)
        self.add_edge(6, 29, taxi)
        self.add_edge(7, 6, taxi)
        self.add_edge(7, 17, taxi)
        self.add_edge(7, 42, bus)
        self.add_edge(8, 1, taxi, 452, 411)
        self.add_edge(8, 18, taxi)
        self.add_edge(8, 19, taxi)
        self.add_edge(9, 1, taxi, 796, 405)
        self.add_edge(9, 19, taxi)
        self.add_edge(9, 20, taxi)
        self.add_edge(10, 2, taxi)
        self.add_edge(10, 11, taxi)
        self.add_edge(10, 21, taxi)
        self.add_edge(10, 34, taxi)
        self.add_edge(11, 3, taxi)
        self.add_edge(11, 10, taxi)
        self.add_edge(11, 22, taxi)
        self.add_edge(12, 3, taxi)
        self.add_edge(12, 23, taxi)
        self.add_edge(12, 23, taxi)
        self.add_edge(13, 4, taxi)
        self.add_edge(13, 14, bus_underground)
        self.add_edge(13, 23, taxi_bus)
        self.add_edge(13, 24, taxi)
        self.add_edge(13, 46, underground)
        self.add_edge(13, 52, bus)
        self.add_edge(13, 52, bus)
        self.add_edge(13, 67, underground)
        self.add_edge(13, 89, underground)
        self.add_edge(14, 13, bus_underground)
        self.add_edge(14, 15, taxi_bus)
        self.add_edge(14, 25, taxi)
        self.add_edge(15, 5, taxi)
        self.add_edge(15, 14, taxi_bus)
        self.add_edge(15, 16, taxi)
        self.add_edge(15, 26, taxi)
        self.add_edge(15, 28, taxi)
        self.add_edge(15, 29, bus)
        self.add_edge(15, 41, bus)
        self.add_edge(16, 5, taxi)
        self.add_edge(16, 15, taxi)
        self.add_edge(16, 28, taxi)
        self.add_edge(16, 29, taxi)
        self.add_edge(17, 7, taxi)
        self.add_edge(17, 29, taxi)
        self.add_edge(17, 30, taxi)
        self.add_edge(18, 8, taxi, 268, 582)
        self.add_edge(18, 31, taxi)
        self.add_edge(18, 43, taxi)
        self.add_edge(19, 8, taxi, 586, 602)
        self.add_edge(19, 9, taxi)
        self.add_edge(19, 32, taxi)
        self.add_edge(20, 2, taxi, 981, 485)
        self.add_edge(20, 9, taxi)
        self.add_edge(20, 33, taxi)
        self.add_edge(21, 10, taxi)
        self.add_edge(21, 33, taxi)
        self.add_edge(22, 3, bus)
        self.add_edge(22, 11, taxi)
        self.add_edge(22, 23, taxi_bus)
        self.add_edge(22, 34, bus)
        self.add_edge(22, 35, bus)
        self.add_edge(22, 65, bus)
        self.add_edge(23, 3, bus)
        self.add_edge(23, 12, taxi)
        self.add_edge(23, 13, bus)
        self.add_edge(23, 22, taxi_bus)
        self.add_edge(23, 37, taxi)
        self.add_edge(23, 67, bus)
        self.add_edge(24, 13, taxi)
        self.add_edge(24, 37, taxi)
        self.add_edge(24, 38, taxi)
        self.add_edge(25, 14, taxi)
        self.add_edge(25, 38, taxi)
        self.add_edge(25, 39, taxi)
        self.add_edge(26, 15, taxi)
        self.add_edge(26, 27, taxi)
        self.add_edge(26, 39, taxi)
        self.add_edge(27, 26, taxi)
        self.add_edge(27, 28, taxi)
        self.add_edge(27, 40, taxi)
        self.add_edge(28, 15, taxi)
        self.add_edge(28, 26, taxi)
        self.add_edge(28, 27, taxi)
        self.add_edge(28, 41, taxi)
        self.add_edge(29, 6, taxi)
        self.add_edge(29, 15, bus)
        self.add_edge(29, 16, taxi)
        self.add_edge(29, 17, taxi)
        self.add_edge(29, 41, bus)
        self.add_edge(29, 42, bus)
        self.add_edge(29, 55, bus)
        self.add_edge(30, 17, taxi)
        self.add_edge(30, 42, taxi)
        self.add_edge(31, 18, taxi)
        self.add_edge(31, 43, taxi)
        self.add_edge(31, 44, taxi)
        self.add_edge(32, 19, taxi)
        self.add_edge(32, 33, taxi)
        self.add_edge(32, 44, taxi)
        self.add_edge(32, 45, taxi)
        self.add_edge(33, 20, taxi)
        self.add_edge(33, 21, taxi)
        self.add_edge(33, 32, taxi)
        self.add_edge(33, 46, taxi)
        self.add_edge(34, 10, taxi)
        self.add_edge(34, 22, taxi_bus)
        self.add_edge(34, 46, bus)
        self.add_edge(34, 47, taxi)
        self.add_edge(34, 48, taxi)
        self.add_edge(34, 63, bus)
        self.add_edge(35, 22, taxi)
        self.add_edge(35, 36, taxi)
        self.add_edge(35, 48, taxi)
        self.add_edge(35, 65, taxi)
        self.add_edge(36, 35, taxi)
        self.add_edge(36, 37, taxi)
        self.add_edge(36, 49, taxi)
        self.add_edge(37, 23, taxi)
        self.add_edge(37, 24, taxi)
        self.add_edge(37, 36, taxi)
        self.add_edge(37, 50, taxi)
        self.add_edge(38, 24, taxi)
        self.add_edge(38, 25, taxi)
        self.add_edge(38, 50, taxi)
        self.add_edge(38, 51, taxi)
        self.add_edge(39, 25, taxi)
        self.add_edge(39, 26, taxi)
        self.add_edge(39, 51, taxi)
        self.add_edge(39, 52, taxi)
        self.add_edge(40, 27, taxi)
        self.add_edge(40, 41, taxi)
        self.add_edge(40, 52, taxi)
        self.add_edge(40, 53, taxi)
        self.add_edge(41, 15, bus)
        self.add_edge(41, 28, taxi)
        self.add_edge(41, 29, taxi_bus)
        self.add_edge(41, 40, taxi)
        self.add_edge(41, 52, bus)
        self.add_edge(41, 87, bus)
        self.add_edge(42, 7, bus)
        self.add_edge(42, 29, taxi_bus)
        self.add_edge(42, 30, taxi)
        self.add_edge(42, 56, taxi)
        self.add_edge(43, 18, taxi)
        self.add_edge(43, 31, taxi)
        self.add_edge(43, 57, taxi)
        self.add_edge(44, 31, taxi)
        self.add_edge(44, 32, taxi)
        self.add_edge(44, 58, taxi)
        self.add_edge(45, 32, taxi)
        self.add_edge(45, 46, taxi)
        self.add_edge(45, 58, taxi)
        self.add_edge(45, 59, taxi)
        self.add_edge(45, 60, taxi)
        self.add_edge(46, 1, bus_underground)
        self.add_edge(46, 13, underground)
        self.add_edge(46, 33, taxi)
        self.add_edge(46, 34, bus)
        self.add_edge(46, 45, taxi)
        self.add_edge(46, 58, bus)
        self.add_edge(46, 74, underground)
        self.add_edge(46, 78, bus)
        self.add_edge(46, 79, underground)
        self.add_edge(47, 34, taxi)
        self.add_edge(47, 46, taxi)
        self.add_edge(47, 62, taxi)
        self.add_edge(48, 34, taxi)
        self.add_edge(48, 35, taxi)
        self.add_edge(48, 62, taxi)
        self.add_edge(48, 63, taxi)
        self.add_edge(49, 36, taxi)
        self.add_edge(49, 50, taxi)
        self.add_edge(49, 66, taxi)
        self.add_edge(50, 37, taxi)
        self.add_edge(50, 38, taxi)
        self.add_edge(50, 49, taxi)
        self.add_edge(51, 38, taxi)
        self.add_edge(51, 39, taxi)
        self.add_edge(51, 52, taxi)
        self.add_edge(51, 67, taxi)
        self.add_edge(51, 68, taxi)
        self.add_edge(52, 13, bus)
        self.add_edge(52, 39, taxi)
        self.add_edge(52, 40, taxi)
        self.add_edge(52, 41, bus)
        self.add_edge(52, 52, taxi)
        self.add_edge(52, 67, bus)
        self.add_edge(52, 69, taxi)
        self.add_edge(52, 86, bus)
        self.add_edge(53, 40, taxi)
        self.add_edge(53, 54, taxi)
        self.add_edge(53, 69, taxi)
        self.add_edge(54, 41, taxi)
        self.add_edge(54, 53, taxi)
        self.add_edge(54, 55, taxi)
        self.add_edge(54, 70, taxi)
        self.add_edge(55, 29, bus)
        self.add_edge(55, 54, taxi)
        self.add_edge(55, 71, taxi)
        self.add_edge(55, 89, bus)
        self.add_edge(56, 42, taxi)
        self.add_edge(56, 91, taxi)
        self.add_edge(57, 43, taxi)
        self.add_edge(57, 58, taxi)
        self.add_edge(57, 73, taxi)
        self.add_edge(58, 1, bus)
        self.add_edge(58, 44, taxi)
        self.add_edge(58, 45, taxi)
        self.add_edge(58, 46, bus)
        self.add_edge(58, 57, taxi)
        self.add_edge(58, 59, taxi)
        self.add_edge(58, 74, bus)
        self.add_edge(58, 77, bus)
        self.add_edge(59, 45, taxi)
        self.add_edge(59, 58, taxi)
        self.add_edge(59, 75, taxi)
        self.add_edge(59, 76, taxi)
        self.add_edge(60, 45, taxi)
        self.add_edge(60, 61, taxi)
        self.add_edge(60, 76, taxi)
        self.add_edge(61, 46, taxi)
        self.add_edge(61, 60, taxi)
        self.add_edge(61, 62, taxi)
        self.add_edge(61, 76, taxi)
        self.add_edge(61, 78, taxi)
        self.add_edge(62, 47, taxi)
        self.add_edge(62, 48, taxi)
        self.add_edge(62, 61, taxi)
        self.add_edge(62, 79, taxi)
        self.add_edge(63, 34, bus)
        self.add_edge(63, 48, taxi)
        self.add_edge(63, 64, taxi)
        self.add_edge(63, 79, taxi_bus)
        self.add_edge(63, 80, taxi)
        self.add_edge(63, 100, bus)
        self.add_edge(64, 63, taxi)
        self.add_edge(64, 65, taxi)
        self.add_edge(64, 81, taxi)
        self.add_edge(65, 22, bus)
        self.add_edge(65, 35, taxi)
        self.add_edge(65, 63, bus)
        self.add_edge(65, 64, taxi)
        self.add_edge(65, 82, taxi_bus)
        self.add_edge(66, 49, taxi)
        self.add_edge(66, 65, taxi)
        self.add_edge(66, 67, taxi)
        self.add_edge(66, 82, taxi)
        self.add_edge(67, 13, underground)
        self.add_edge(67, 23, bus)
        self.add_edge(67, 51, taxi)
        self.add_edge(67, 52, bus)
        self.add_edge(67, 65, bus)
        self.add_edge(67, 66, taxi)
        self.add_edge(67, 68, taxi)
        self.add_edge(67, 79, underground)
        self.add_edge(67, 82, bus)
        self.add_edge(67, 84, taxi)
        self.add_edge(67, 89, underground)
        self.add_edge(67, 102, bus)
        self.add_edge(67, 111, underground)
        self.add_edge(68, 51, taxi)
        self.add_edge(68, 67, taxi)
        self.add_edge(68, 69, taxi)
        self.add_edge(68, 85, taxi)
        self.add_edge(69, 52, taxi)
        self.add_edge(69, 53, taxi)
        self.add_edge(69, 68, taxi)
        self.add_edge(69, 86, taxi)
        self.add_edge(70, 54, taxi)
        self.add_edge(70, 71, taxi)
        self.add_edge(70, 87, taxi)
        self.add_edge(71, 55, taxi)
        self.add_edge(71, 70, taxi)
        self.add_edge(71, 72, taxi)
        self.add_edge(71, 89, taxi)
        self.add_edge(72, 42, bus)
        self.add_edge(72, 71, taxi)
        self.add_edge(72, 90, taxi)
        self.add_edge(72, 91, taxi)
        self.add_edge(72, 105, bus)
        self.add_edge(72, 107, bus)
        self.add_edge(73, 57, taxi)
        self.add_edge(73, 74, taxi)
        self.add_edge(73, 92, taxi)
        self.add_edge(74, 46, underground)
        self.add_edge(74, 58, taxi_bus)
        self.add_edge(74, 73, taxi)
        self.add_edge(74, 75, taxi)
        self.add_edge(74, 92, taxi)
        self.add_edge(74, 94, bus)
        self.add_edge(75, 58, taxi)
        self.add_edge(75, 59, taxi)
        self.add_edge(75, 74, taxi)
        self.add_edge(75, 94, taxi)
        self.add_edge(76, 59, taxi)
        self.add_edge(76, 60, taxi)
        self.add_edge(76, 61, taxi)
        self.add_edge(76, 77, taxi)
        self.add_edge(77, 58, bus)
        self.add_edge(77, 76, taxi)
        self.add_edge(77, 78, taxi_bus)
        self.add_edge(77, 94, bus)
        self.add_edge(77, 95, taxi)
        self.add_edge(77, 96, taxi)
        self.add_edge(77, 124, bus)
        self.add_edge(78, 46, bus)
        self.add_edge(78, 61, taxi)
        self.add_edge(78, 77, taxi_bus)
        self.add_edge(78, 79, bus)
        self.add_edge(78, 79, taxi)
        self.add_edge(78, 97, taxi)
        self.add_edge(79, 46, underground)
        self.add_edge(79, 62, taxi)
        self.add_edge(79, 63, taxi_bus)
        self.add_edge(79, 78, taxi_bus)
        self.add_edge(79, 98, taxi)
        self.add_edge(79, 111, underground)
        self.add_edge(80, 63, taxi)
        self.add_edge(80, 99, taxi)
        self.add_edge(80, 100, taxi)
        self.add_edge(81, 64, taxi)
        self.add_edge(81, 82, taxi)
        self.add_edge(81, 100, taxi)
        self.add_edge(82, 65, taxi_bus)
        self.add_edge(82, 66, taxi)
        self.add_edge(82, 67, bus)
        self.add_edge(82, 81, taxi)
        self.add_edge(82, 100, bus)
        self.add_edge(82, 101, taxi)
        self.add_edge(83, 101, taxi)
        self.add_edge(83, 102, taxi)
        self.add_edge(84, 67, taxi)
        self.add_edge(84, 85, taxi)
        self.add_edge(85, 68, taxi)
        self.add_edge(85, 84, taxi)
        self.add_edge(85, 103, taxi)
        self.add_edge(86, 52, bus)
        self.add_edge(86, 69, taxi)
        self.add_edge(86, 87, bus)
        self.add_edge(86, 102, bus)
        self.add_edge(86, 103, taxi)
        self.add_edge(86, 104, taxi)
        self.add_edge(86, 116, bus)
        self.add_edge(87, 41, bus)
        self.add_edge(87, 70, taxi)
        self.add_edge(87, 86, bus)
        self.add_edge(87, 88, taxi)
        self.add_edge(87, 105, bus)
        self.add_edge(88, 87, taxi)
        self.add_edge(88, 89, taxi)
        self.add_edge(88, 117, taxi)
        self.add_edge(89, 13, underground)
        self.add_edge(89, 55, bus)
        self.add_edge(89, 67, underground)
        self.add_edge(89, 71, taxi)
        self.add_edge(89, 105, taxi_bus)
        self.add_edge(89, 128, underground)
        self.add_edge(90, 72, taxi)
        self.add_edge(90, 91, taxi)
        self.add_edge(90, 105, taxi)
        self.add_edge(91, 56, taxi)
        self.add_edge(91, 72, taxi)
        self.add_edge(91, 90, taxi)
        self.add_edge(91, 105, taxi)
        self.add_edge(91, 107, taxi)
        self.add_edge(92, 73, taxi)
        self.add_edge(92, 74, taxi)
        self.add_edge(92, 93, taxi)
        self.add_edge(93, 79, underground)
        self.add_edge(93, 92, taxi)
        self.add_edge(93, 94, taxi_bus)
        self.add_edge(94, 74, bus)
        self.add_edge(94, 75, taxi)
        self.add_edge(94, 93, taxi_bus)
        self.add_edge(94, 95, taxi)
        self.add_edge(95, 77, taxi)
        self.add_edge(95, 94, taxi)
        self.add_edge(95, 122, taxi)
        self.add_edge(96, 77, taxi)
        self.add_edge(96, 97, taxi)
        self.add_edge(96, 109, taxi)
        self.add_edge(97, 78, taxi)
        self.add_edge(97, 96, taxi)
        self.add_edge(97, 98, taxi)
        self.add_edge(97, 109, taxi)
        self.add_edge(98, 79, taxi)
        self.add_edge(98, 97, taxi)
        self.add_edge(98, 99, taxi)
        self.add_edge(98, 110, taxi)
        self.add_edge(99, 80, taxi)
        self.add_edge(99, 98, taxi)
        self.add_edge(99, 110, taxi)
        self.add_edge(99, 112, taxi)
        self.add_edge(100, 63, bus)
        self.add_edge(100, 80, taxi)
        self.add_edge(100, 81, taxi)
        self.add_edge(100, 82, bus)
        self.add_edge(100, 111, bus)
        self.add_edge(100, 112, taxi)
        self.add_edge(100, 113, taxi)
        self.add_edge(101, 82, taxi)
        self.add_edge(101, 83, taxi)
        self.add_edge(101, 100, taxi)
        self.add_edge(101, 114, taxi)
        self.add_edge(102, 67, bus)
        self.add_edge(102, 83, taxi)
        self.add_edge(102, 86, bus)
        self.add_edge(102, 103, taxi)
        self.add_edge(102, 115, taxi)
        self.add_edge(102, 127, bus)
        self.add_edge(103, 85, taxi)
        self.add_edge(103, 86, taxi)
        self.add_edge(103, 102, taxi)
        self.add_edge(104, 86, taxi)
        self.add_edge(104, 116, taxi)
        self.add_edge(105, 72, bus)
        self.add_edge(105, 87, bus)
        self.add_edge(105, 89, taxi_bus)
        self.add_edge(105, 90, taxi)
        self.add_edge(105, 91, taxi)
        self.add_edge(105, 106, taxi)
        self.add_edge(105, 106, taxi)
        self.add_edge(105, 107, bus)
        self.add_edge(105, 108, taxi_bus)
        self.add_edge(106, 105, taxi)
        self.add_edge(106, 107, taxi)
        self.add_edge(107, 72, bus)
        self.add_edge(107, 91, taxi)
        self.add_edge(107, 105, bus)
        self.add_edge(107, 106, taxi)
        self.add_edge(107, 119, taxi)
        self.add_edge(107, 161, bus)
        self.add_edge(108, 105, taxi_bus)
        self.add_edge(108, 117, taxi)
        self.add_edge(108, 119, taxi)
        self.add_edge(108, 135, bus)
        self.add_edge(108, 135, bus)
        self.add_edge(109, 96, taxi)
        self.add_edge(109, 97, taxi)
        self.add_edge(109, 110, taxi)
        self.add_edge(109, 124, taxi)
        self.add_edge(110, 98, taxi)
        self.add_edge(110, 99, taxi)
        self.add_edge(110, 109, taxi)
        self.add_edge(110, 111, taxi)
        self.add_edge(111, 67, underground)
        self.add_edge(111, 79, underground)
        self.add_edge(111, 110, taxi)
        self.add_edge(111, 112, taxi)
        self.add_edge(111, 112, taxi)
        self.add_edge(111, 124, taxi_bus)
        self.add_edge(111, 153, underground)
        self.add_edge(111, 163, underground)
        self.add_edge(112, 99, taxi)
        self.add_edge(112, 100, taxi)
        self.add_edge(112, 111, taxi)
        self.add_edge(112, 125, taxi)
        self.add_edge(113, 100, taxi)
        self.add_edge(113, 114, taxi)
        self.add_edge(113, 125, taxi)
        self.add_edge(114, 101, taxi)
        self.add_edge(114, 113, taxi)
        self.add_edge(114, 115, taxi)
        self.add_edge(114, 126, taxi)
        self.add_edge(114, 131, taxi)
        self.add_edge(114, 132, taxi)
        self.add_edge(115, 102, taxi)
        self.add_edge(115, 114, taxi)
        self.add_edge(115, 126, taxi)
        self.add_edge(115, 127, taxi)
        self.add_edge(116, 86, bus)
        self.add_edge(116, 104, taxi)
        self.add_edge(116, 108, bus)
        self.add_edge(116, 117, taxi)
        self.add_edge(116, 118, taxi)
        self.add_edge(116, 127, taxi_bus)
        self.add_edge(116, 142, bus)
        self.add_edge(117, 88, taxi)
        self.add_edge(117, 108, taxi)
        self.add_edge(117, 116, taxi)
        self.add_edge(117, 129, taxi)
        self.add_edge(118, 116, taxi)
        self.add_edge(118, 129, taxi)
        self.add_edge(118, 134, taxi)
        self.add_edge(118, 142, taxi)
        self.add_edge(119, 107, taxi)
        self.add_edge(119, 108, taxi)
        self.add_edge(119, 136, taxi)
        self.add_edge(120, 121, taxi)
        self.add_edge(120, 144, taxi)
        self.add_edge(121, 120, taxi)
        self.add_edge(121, 122, taxi)
        self.add_edge(121, 145, taxi)
        self.add_edge(122, 121, taxi)
        self.add_edge(122, 123, taxi_bus)
        self.add_edge(122, 144, bus)
        self.add_edge(122, 146, taxi)
        self.add_edge(123, 122, taxi_bus)
        self.add_edge(123, 124, taxi_bus)
        self.add_edge(123, 137, taxi)
        self.add_edge(123, 144, bus)
        self.add_edge(123, 149, taxi)
        self.add_edge(123, 165, bus)
        self.add_edge(124, 77, bus)
        self.add_edge(124, 109, taxi)
        self.add_edge(124, 123, taxi_bus)
        self.add_edge(124, 130, taxi)
        self.add_edge(124, 138, taxi)
        self.add_edge(124, 153, bus)
        self.add_edge(125, 112, taxi)
        self.add_edge(125, 113, taxi)
        self.add_edge(125, 131, taxi)
        self.add_edge(126, 114, taxi)
        self.add_edge(126, 115, taxi)
        self.add_edge(126, 127, taxi)
        self.add_edge(126, 140, taxi)
        self.add_edge(127, 102, bus)
        self.add_edge(127, 115, taxi)
        self.add_edge(127, 116, taxi_bus)
        self.add_edge(127, 126, taxi)
        self.add_edge(127, 133, taxi_bus)
        self.add_edge(127, 134, taxi)
        self.add_edge(128, 89, underground)
        self.add_edge(128, 135, bus)
        self.add_edge(128, 140, underground)
        self.add_edge(128, 142, taxi_bus)
        self.add_edge(128, 143, taxi)
        self.add_edge(128, 160, taxi)
        self.add_edge(128, 161, bus)
        self.add_edge(128, 172, taxi)
        self.add_edge(128, 185, underground)
        self.add_edge(128, 187, bus)
        self.add_edge(128, 188, taxi)
        self.add_edge(128, 199, bus)
        self.add_edge(129, 117, taxi)
        self.add_edge(129, 118, taxi)
        self.add_edge(129, 135, taxi)
        self.add_edge(129, 142, taxi)
        self.add_edge(129, 143, taxi)
        self.add_edge(130, 124, taxi)
        self.add_edge(130, 131, taxi)
        self.add_edge(130, 139, taxi)
        self.add_edge(131, 114, taxi)
        self.add_edge(131, 125, taxi)
        self.add_edge(131, 130, taxi)
        self.add_edge(132, 114, taxi)
        self.add_edge(132, 140, taxi)
        self.add_edge(133, 127, taxi_bus)
        self.add_edge(133, 140, taxi_bus)
        self.add_edge(133, 141, taxi)
        self.add_edge(133, 157, bus)
        self.add_edge(134, 118, taxi)
        self.add_edge(134, 127, taxi)
        self.add_edge(134, 141, taxi)
        self.add_edge(134, 142, taxi)
        self.add_edge(135, 108, bus)
        self.add_edge(135, 128, bus)
        self.add_edge(135, 129, taxi)
        self.add_edge(135, 136, taxi)
        self.add_edge(135, 143, taxi)
        self.add_edge(135, 161, taxi_bus)
        self.add_edge(136, 119, taxi)
        self.add_edge(136, 135, taxi)
        self.add_edge(136, 162, taxi)
        self.add_edge(137, 123, taxi)
        self.add_edge(137, 147, taxi)
        self.add_edge(138, 124, taxi)
        self.add_edge(138, 150, taxi)
        self.add_edge(138, 152, taxi)
        self.add_edge(138, 152, taxi)
        self.add_edge(139, 130, taxi)
        self.add_edge(139, 140, taxi)
        self.add_edge(139, 153, taxi)
        self.add_edge(139, 154, taxi)
        self.add_edge(140, 82, bus)
        self.add_edge(140, 89, underground)
        self.add_edge(140, 126, taxi)
        self.add_edge(140, 128, underground)
        self.add_edge(140, 133, taxi_bus)
        self.add_edge(140, 139, taxi)
        self.add_edge(140, 153, underground)
        self.add_edge(140, 154, taxi_bus)
        self.add_edge(140, 156, taxi_bus)
        self.add_edge(141, 133, taxi)
        self.add_edge(141, 134, taxi)
        self.add_edge(141, 142, taxi)
        self.add_edge(142, 116, bus)
        self.add_edge(142, 118, taxi)
        self.add_edge(142, 128, taxi_bus)
        self.add_edge(142, 129, taxi)
        self.add_edge(142, 134, taxi)
        self.add_edge(142, 141, taxi)
        self.add_edge(142, 143, taxi)
        self.add_edge(142, 157, bus)
        self.add_edge(142, 158, taxi)
        self.add_edge(143, 128, taxi)
        self.add_edge(143, 129, taxi)
        self.add_edge(143, 135, taxi)
        self.add_edge(143, 142, taxi)
        self.add_edge(143, 160, taxi)
        self.add_edge(144, 120, taxi)
        self.add_edge(144, 122, bus)
        self.add_edge(144, 123, bus)
        self.add_edge(144, 145, taxi)
        self.add_edge(144, 163, bus)
        self.add_edge(144, 177, taxi)
        self.add_edge(145, 121, taxi)
        self.add_edge(145, 144, taxi)
        self.add_edge(145, 146, taxi)
        self.add_edge(146, 122, taxi)
        self.add_edge(146, 145, taxi)
        self.add_edge(146, 147, taxi)
        self.add_edge(146, 163, taxi)
        self.add_edge(147, 137, taxi)
        self.add_edge(147, 146, taxi)
        self.add_edge(147, 164, taxi)
        self.add_edge(148, 123, taxi)
        self.add_edge(148, 149, taxi)
        self.add_edge(148, 164, taxi)
        self.add_edge(149, 123, taxi)
        self.add_edge(149, 148, taxi)
        self.add_edge(149, 150, taxi)
        self.add_edge(149, 165, taxi)
        self.add_edge(150, 138, taxi)
        self.add_edge(150, 149, taxi)
        self.add_edge(150, 151, taxi)
        self.add_edge(151, 150, taxi)
        self.add_edge(151, 152, taxi)
        self.add_edge(151, 165, taxi)
        self.add_edge(151, 166, taxi)
        self.add_edge(152, 138, taxi)
        self.add_edge(152, 151, taxi)
        self.add_edge(152, 151, taxi)
        self.add_edge(152, 153, taxi)
        self.add_edge(153, 111, underground)
        self.add_edge(153, 124, bus)
        self.add_edge(153, 139, taxi)
        self.add_edge(153, 140, underground)
        self.add_edge(153, 152, taxi)
        self.add_edge(153, 154, taxi_bus)
        self.add_edge(153, 163, underground)
        self.add_edge(153, 166, taxi)
        self.add_edge(153, 167, taxi)
        self.add_edge(153, 180, bus)
        self.add_edge(153, 184, bus)
        self.add_edge(153, 185, underground)
        self.add_edge(154, 139, taxi)
        self.add_edge(154, 140, taxi_bus)
        self.add_edge(154, 153, taxi_bus)
        self.add_edge(154, 155, taxi)
        self.add_edge(154, 156, bus)
        self.add_edge(155, 154, taxi)
        self.add_edge(155, 156, taxi)
        self.add_edge(155, 167, taxi)
        self.add_edge(155, 168, taxi)
        self.add_edge(156, 140, taxi_bus)
        self.add_edge(156, 154, bus)
        self.add_edge(156, 155, taxi)
        self.add_edge(156, 157, taxi_bus)
        self.add_edge(156, 169, taxi)
        self.add_edge(156, 184, bus)
        self.add_edge(157, 133, bus)
        self.add_edge(157, 142, bus)
        self.add_edge(157, 156, taxi_bus)
        self.add_edge(157, 158, taxi)
        self.add_edge(157, 170, taxi)
        self.add_edge(157, 185, bus)
        self.add_edge(158, 141, taxi)
        self.add_edge(158, 142, taxi)
        self.add_edge(158, 157, taxi)
        self.add_edge(158, 159, taxi)
        self.add_edge(159, 158, taxi)
        self.add_edge(159, 170, taxi)
        self.add_edge(159, 172, taxi)
        self.add_edge(159, 186, taxi)
        self.add_edge(159, 198, taxi)
        self.add_edge(160, 128, taxi)
        self.add_edge(160, 143, taxi)
        self.add_edge(160, 161, taxi)
        self.add_edge(160, 173, taxi)
        self.add_edge(161, 107, bus)
        self.add_edge(161, 128, bus)
        self.add_edge(161, 135, taxi_bus)
        self.add_edge(161, 160, taxi)
        self.add_edge(161, 174, taxi)
        self.add_edge(161, 199, bus)
        self.add_edge(162, 136, taxi)
        self.add_edge(162, 175, taxi)
        self.add_edge(163, 111, underground)
        self.add_edge(163, 144, bus)
        self.add_edge(163, 146, taxi)
        self.add_edge(163, 153, underground)
        self.add_edge(163, 176, bus)
        self.add_edge(163, 177, taxi)
        self.add_edge(163, 191, bus)
        self.add_edge(164, 147, taxi)
        self.add_edge(164, 148, taxi)
        self.add_edge(164, 178, taxi)
        self.add_edge(164, 179, taxi)
        self.add_edge(165, 123, bus)
        self.add_edge(165, 149, taxi)
        self.add_edge(165, 151, taxi)
        self.add_edge(165, 179, taxi)
        self.add_edge(165, 180, taxi_bus)
        self.add_edge(165, 191, bus)
        self.add_edge(166, 151, taxi)
        self.add_edge(166, 153, taxi)
        self.add_edge(166, 181, taxi)
        self.add_edge(166, 183, taxi)
        self.add_edge(167, 153, taxi)
        self.add_edge(167, 155, taxi)
        self.add_edge(167, 168, taxi)
        self.add_edge(167, 183, taxi)
        self.add_edge(168, 155, taxi)
        self.add_edge(168, 167, taxi)
        self.add_edge(168, 184, taxi)
        self.add_edge(169, 156, taxi)
        self.add_edge(169, 184, taxi)
        self.add_edge(170, 157, taxi)
        self.add_edge(170, 159, taxi)
        self.add_edge(170, 185, taxi)
        self.add_edge(171, 173, taxi)
        self.add_edge(171, 175, taxi)
        self.add_edge(171, 199, taxi)
        self.add_edge(171, 199, taxi)
        self.add_edge(172, 128, taxi)
        self.add_edge(172, 159, taxi)
        self.add_edge(172, 187, taxi)
        self.add_edge(173, 160, taxi)
        self.add_edge(173, 171, taxi)
        self.add_edge(173, 174, taxi)
        self.add_edge(173, 188, taxi)
        self.add_edge(174, 161, taxi)
        self.add_edge(174, 173, taxi)
        self.add_edge(174, 175, taxi)
        self.add_edge(175, 162, taxi)
        self.add_edge(175, 171, taxi)
        self.add_edge(175, 174, taxi)
        self.add_edge(176, 163, bus)
        self.add_edge(176, 177, taxi)
        self.add_edge(176, 189, taxi)
        self.add_edge(176, 190, bus)
        self.add_edge(177, 144, taxi)
        self.add_edge(177, 163, taxi)
        self.add_edge(177, 176, taxi)
        self.add_edge(178, 164, taxi)
        self.add_edge(178, 189, taxi)
        self.add_edge(178, 191, taxi)
        self.add_edge(179, 164, taxi)
        self.add_edge(179, 165, taxi)
        self.add_edge(179, 191, taxi)
        self.add_edge(180, 153, bus)
        self.add_edge(180, 165, taxi_bus)
        self.add_edge(180, 181, taxi)
        self.add_edge(180, 184, bus)
        self.add_edge(180, 190, bus)
        self.add_edge(180, 193, taxi)
        self.add_edge(181, 166, taxi)
        self.add_edge(181, 180, taxi)
        self.add_edge(181, 182, taxi)
        self.add_edge(181, 193, taxi)
        self.add_edge(182, 181, taxi)
        self.add_edge(182, 183, taxi)
        self.add_edge(182, 195, taxi)
        self.add_edge(183, 166, taxi)
        self.add_edge(183, 167, taxi)
        self.add_edge(183, 182, taxi)
        self.add_edge(183, 196, taxi)
        self.add_edge(184, 153, bus)
        self.add_edge(184, 156, bus)
        self.add_edge(184, 168, taxi)
        self.add_edge(184, 169, taxi)
        self.add_edge(184, 180, bus)
        self.add_edge(184, 185, taxi_bus)
        self.add_edge(184, 196, taxi)
        self.add_edge(184, 197, taxi)
        self.add_edge(185, 128, underground)
        self.add_edge(185, 153, underground)
        self.add_edge(185, 157, bus)
        self.add_edge(185, 170, taxi)
        self.add_edge(185, 184, taxi_bus)
        self.add_edge(185, 186, taxi)
        self.add_edge(185, 187, bus)
        self.add_edge(186, 159, taxi)
        self.add_edge(186, 185, taxi)
        self.add_edge(186, 198, taxi)
        self.add_edge(187, 128, bus)
        self.add_edge(187, 172, taxi)
        self.add_edge(187, 185, bus)
        self.add_edge(187, 188, taxi)
        self.add_edge(187, 198, taxi)
        self.add_edge(188, 128, taxi)
        self.add_edge(188, 173, taxi)
        self.add_edge(188, 187, taxi)
        self.add_edge(188, 199, taxi)
        self.add_edge(189, 176, taxi)
        self.add_edge(189, 178, taxi)
        self.add_edge(189, 190, taxi)
        self.add_edge(190, 176, bus)
        self.add_edge(190, 180, bus)
        self.add_edge(190, 189, taxi)
        self.add_edge(190, 191, taxi_bus)
        self.add_edge(190, 192, taxi)
        self.add_edge(191, 163, bus)
        self.add_edge(191, 165, bus)
        self.add_edge(191, 178, taxi)
        self.add_edge(191, 179, taxi)
        self.add_edge(191, 190, taxi_bus)
        self.add_edge(191, 192, taxi)
        self.add_edge(192, 190, taxi)
        self.add_edge(192, 191, taxi)
        self.add_edge(192, 194, taxi)
        self.add_edge(193, 180, taxi)
        self.add_edge(193, 181, taxi)
        self.add_edge(193, 194, taxi)
        self.add_edge(194, 192, taxi)
        self.add_edge(194, 193, taxi)
        self.add_edge(194, 195, taxi)
        self.add_edge(195, 182, taxi)
        self.add_edge(195, 194, taxi)
        self.add_edge(195, 197, taxi)
        self.add_edge(196, 183, taxi)
        self.add_edge(196, 184, taxi)
        self.add_edge(196, 197, taxi)
        self.add_edge(197, 184, taxi)
        self.add_edge(197, 195, taxi)
        self.add_edge(197, 196, taxi)
        self.add_edge(198, 159, taxi)
        self.add_edge(198, 186, taxi)
        self.add_edge(198, 187, taxi)
        self.add_edge(198, 199, taxi)
        self.add_edge(199, 128, bus)
        self.add_edge(199, 161, bus)
        self.add_edge(199, 171, taxi)
        self.add_edge(199, 188, taxi)
        self.add_edge(199, 198, taxi)

        self.add_edge(108, 115, boat)
        self.add_edge(115, 108, boat)
        self.add_edge(115, 157, boat)
        self.add_edge(157, 115, boat)
        self.add_edge(157, 194, boat)
        self.add_edge(194, 157, boat)

















