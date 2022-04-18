from PIL.Image import Resampling
from Graph import Graph
from tkinter import *
from PIL import Image, ImageTk


WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1000


locator = Graph()
locator.build_graph()
list = ["taxi", "bus", "underground", "black ticket"]

def submit():
    if starting_entry.get() == "":
        results_label.delete("1.0", END)
        results_label.insert("2.0", "No starting point defined!")
    else:
        if results_label.get("1.0", END) == "No starting point defined!":
            temp_start = starting_entry.get()
            reset()
            starting_entry.insert(0, temp_start)
        locations = locator.show_options(int(starting_entry.get()), [str(list[radio_choice.get()])])
        # results_label["text"] += "\n\r >> " + str(locations)
        results_label.insert(END, "\n\r >> " + str(locations))

def reset():
    results_label.delete("1.0", END)
    locator.old_possible_node_numbers.clear()
    locator.currently_possible_node_numbers.clear()
    starting_entry.delete(0, END)




window = Tk()
window.geometry(str(WINDOW_WIDTH) + 'x' + str(WINDOW_HEIGHT))

image_frame = Frame(bg="blue", width=(int(WINDOW_HEIGHT*1.285)), height=WINDOW_HEIGHT)
image = Image.open("scotlandyard_board.png")
image = image.resize(((int(WINDOW_HEIGHT*1.285)), WINDOW_HEIGHT), Resampling.LANCZOS)
board = ImageTk.PhotoImage(image)

boardLabel = Label(master=image_frame, image=board, borderwidth=0)
boardLabel.image = board
boardLabel.place(x=0, y=0)

image_frame.pack(fill=BOTH, side=LEFT)

input_frame = Frame(master=window, height=10, bg="black")

input_label = Label(master=input_frame, text="Starting position: ", bg="black", fg="white")
input_label.grid(row=0, column=0, sticky="w")
starting_entry = Entry(master=input_frame, fg="black", bg="white", width=3)
starting_entry.grid(row=0, column=1, sticky="w")

#based on ["taxi", "bus", "underground", "black ticket"]
radio_choice = IntVar()
radio_taxi = Radiobutton(master=input_frame, text="Taxi", variable=radio_choice, value=0, fg="white", bg="black")
radio_bus = Radiobutton(master=input_frame, text="Bus", variable=radio_choice, value=1, fg="white", bg="black")
radio_underground = Radiobutton(master=input_frame, text="Underground", variable=radio_choice, value=2, fg="white", bg="black")
radio_black = Radiobutton(master=input_frame, text="Black ticket", variable=radio_choice, value=3, fg="white", bg="black")
radio_taxi.grid(row=1, column=0, sticky="w")
radio_bus.grid(row=2, column=0, sticky="w")
radio_underground.grid(row=3, column=0, sticky="w")
radio_black.grid(row=4, column=0, sticky="w")

spacing1 = Label(master=input_frame, text=" ", bg="black", fg="black")
spacing1.grid(row=5, column=0, rowspan=2)

submit_button = Button(master=input_frame, text="Submit!", width=20, height=2, highlightbackground="white", highlightcolor="black", command=submit)
submit_button.grid(row=7, column=0)
reset_button = Button(master=input_frame, text="Reset", width=20, height=2, highlightbackground="white", highlightcolor="black", command=reset)
reset_button.grid(row=7, column=3)

spacing2 = Label(master=input_frame, text=" ", bg="black", fg="black")
spacing2.grid(row=8, column=0, rowspan=2)

result_label = Label(master=input_frame, text="Results: ", bg="black", fg="white")
result_label.grid(row=10, column=0)

input_frame.pack(fill=X, side=TOP, anchor="n")

result_frame = Frame(master=window, bg="white")
results_label = Text(master=result_frame, bg="white", fg="black")
results_label.pack(anchor="w")
result_frame.pack(fill=BOTH, side=TOP, expand=True)

window.mainloop()



#########################################################################################################################


# scotland_yard_is_fun = True
# while scotland_yard_is_fun:
#     locator = Graph()
#     locator.build_graph()
#     start_node = input("Starting point: ")
# #   start_node = 1
#     if start_node == "exit":
#         break
#
#     start_node = int(start_node)
#     on_the_run_in_the_dark = True
#     while on_the_run_in_the_dark:
#         travelmethod = input("taxi, bus, underground or black ticket? ")
# #       travelmethod = "taxi"
#         if travelmethod == "exit":
#             on_the_run_in_the_dark = False
#             break
#         if travelmethod in ["taxi", "bus", "underground", "black ticket"]:
#             locator.show_options(start_node, [travelmethod])
#         else:
#             print("unknown travel option, try again!")
