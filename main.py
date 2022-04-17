from Graph import Graph

scotland_yard_is_fun = True


while (scotland_yard_is_fun):
    locator = Graph()
    locator.build_graph()
    start_node = input("Starting point: ")
    #start_node = 1
    if start_node == "exit":
        break

    start_node = int(start_node)
    on_the_run_in_the_dark = True
    while on_the_run_in_the_dark:
        travelmethod = input("taxi, bus, underground or black ticket? ")
        #travelmethod = "taxi"
        if travelmethod == "exit":
            on_the_run_in_the_dark = False
            break
        if travelmethod in ["taxi", "bus", "underground", "black ticket"]:
            locator.show_options(start_node, [travelmethod])
        else:
            print("unknown travel option, try again!")

