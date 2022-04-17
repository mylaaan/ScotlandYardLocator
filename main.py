from Graph import Graph
from Node import Node
from Edge import Edge

scotland_yard_is_fun = True


while (scotland_yard_is_fun):
    locator = Graph()
    start_node = input("Starting point")
    if start_node == "exit":
        break

    on_the_run_in_the_dark = True
    while on_the_run_in_the_dark:
        travelmethod = input("taxi, bus, underground or black ticket?")
        if travelmethod == "exit":
            on_the_run_in_the_dark = False
            break
        if travelmethod in ["taxi, bus, underground or black ticket"]:
            locator.show_options(start_node, [travelmethod])
        else:
            print("unknown travel option, try again!")


