from UI import UI
from Graph import Graph

locator = Graph()
ui = UI(locator)

# for a GUI
ui.create_window()

# for text-based in terminal
#ui.text_based()