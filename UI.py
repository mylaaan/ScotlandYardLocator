from tkinter import *
from PIL.Image import Resampling
from PIL import Image, ImageTk
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class UI:

    def __init__(self, locator):
        self.WINDOW_WIDTH = 1600
        self.WINDOW_HEIGHT = 900
        self.playboard = "scotlandyard_board_mid_high_res.png"
        self.locator = locator
        self.locator.build_graph()

        self.list = ["taxi", "bus", "underground", "black ticket"]

        self.x = []
        self.y = []


    def submit(self):
        if self.starting_entry.get() == "":
            self.results_box.delete("1.0", END)
            self.results_box.insert("2.0", "No starting point defined!")
        else:
            if self.results_box.get("1.0", END) == "No starting point defined!":
                temp_start = self.starting_entry.get()
                self.reset()
                self.starting_entry.insert(0, temp_start)

            locations = self.locator.show_options(int(self.starting_entry.get()), [str(self.list[self.radio_choice.get()])])
            self.x.clear()
            self.y.clear()
            for node in locations:
                temp_x = self.locator.node_list[node].x
                temp_y = self.locator.node_list[node].y
                if not (temp_x == 0 or temp_y == 0):
                    self.x.append(temp_x)
                    self.y.append(temp_y)
            self.results_box.insert(END, "\n\r >> " + str(locations))
            self.replot()


    def reset(self):
        self.results_box.delete("1.0", END)
        self.locator.old_possible_node_numbers.clear()
        self.locator.currently_possible_node_numbers.clear()
        self.starting_entry.delete(0, END)
        self.x.clear()
        self.y.clear()
        self.replot()


    def replot(self):
        self.axes.clear()
        self.axes.imshow(self.img)
        self.axes.scatter(self.x, self.y, c="red")
        self.axes.patch.set_facecolor('black')
        self.axes.axis("off")
        self.figure_canvas.draw()


    def create_window(self):
        window = Tk()
        window.geometry(str(self.WINDOW_WIDTH) + 'x' + str(self.WINDOW_HEIGHT))

        #########################################################################################################################
        #########################################################################################################################

        image_frame = Frame(bg="black", width=(int(self.WINDOW_HEIGHT * 1.285)), height=self.WINDOW_HEIGHT)

        self.img = plt.imread(self.playboard)
        self.figure = Figure(figsize=((int(self.WINDOW_HEIGHT * 1.285/250)), (self.WINDOW_HEIGHT/250)), dpi=300)
        self.figure_canvas = FigureCanvasTkAgg(self.figure, master=image_frame)
        self.axes = self.figure.add_subplot()
        self.figure.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
        self.axes.imshow(self.img)
        self.axes.scatter(self.x, self.y, c="red")
        self.axes.patch.set_facecolor('black')
        self.axes.axis("off")
        self.figure_canvas.get_tk_widget().pack(expand=True)  # side=LEFT, fill=BOTH, expand=True
        image_frame.pack(fill=BOTH, side=LEFT)

        # image_frame = Frame(bg="blue", width=(int(self.WINDOW_HEIGHT * 1.285)), height=self.WINDOW_HEIGHT)
        # image = Image.open("scotlandyard_board.png")
        # image = image.resize(((int(self.WINDOW_HEIGHT * 1.285)), self.WINDOW_HEIGHT), Resampling.LANCZOS)
        # board = ImageTk.PhotoImage(image)
        #
        # boardLabel = Label(master=image_frame, image=board, borderwidth=0)
        # boardLabel.image = board
        # boardLabel.place(x=0, y=0)

        image_frame.pack(fill=BOTH, side=LEFT)

        #########################################################################################################################
        #########################################################################################################################

        input_frame = Frame(master=window, height=10, bg="black")

        input_label = Label(master=input_frame, text="Starting position: ", bg="black", fg="white")
        input_label.grid(row=0, column=0, sticky="w")

        self.starting_entry = Entry(master=input_frame, fg="black", bg="white", width=3)
        self.starting_entry.grid(row=0, column=1, sticky="w")

        #########################################################################################################################

        #based on ["taxi", "bus", "underground", "black ticket"]
        self.radio_choice = IntVar()
        radio_taxi = Radiobutton(master=input_frame, text="Taxi", variable=self.radio_choice, value=0, fg="white", bg="black", selectcolor="grey")
        radio_bus = Radiobutton(master=input_frame, text="Bus", variable=self.radio_choice, value=1, fg="white", bg="black", selectcolor="grey")
        radio_underground = Radiobutton(master=input_frame, text="Underground", variable=self.radio_choice, value=2, fg="white", bg="black", selectcolor="grey")
        radio_black = Radiobutton(master=input_frame, text="Black ticket", variable=self.radio_choice, value=3, fg="white", bg="black", selectcolor="grey")
        radio_taxi.grid(row=1, column=0, sticky="w")
        radio_bus.grid(row=2, column=0, sticky="w")
        radio_underground.grid(row=3, column=0, sticky="w")
        radio_black.grid(row=4, column=0, sticky="w")

        #########################################################################################################################

        spacing1 = Label(master=input_frame, text=" ", bg="black", fg="black")
        spacing1.grid(row=5, column=0, rowspan=2)

        submit_button = Button(master=input_frame, text="Submit!", width=20, height=2, highlightbackground="white", highlightcolor="black", command=self.submit)
        submit_button.grid(row=7, column=0)
        reset_button = Button(master=input_frame, text="Reset", width=20, height=2, highlightbackground="white", highlightcolor="black", command=self.reset)
        reset_button.grid(row=7, column=3)

        spacing2 = Label(master=input_frame, text=" ", bg="black", fg="black")
        spacing2.grid(row=8, column=0, rowspan=2)

        #########################################################################################################################

        result_label = Label(master=input_frame, text="Results: ", bg="black", fg="white")
        result_label.grid(row=10, column=0)

        input_frame.pack(fill=X, side=TOP, anchor="n")

        #########################################################################################################################

        result_frame = Frame(master=window, bg="black")

        self.results_box = Text(master=result_frame, bg="white", fg="black")
        self.results_box.pack(anchor="w")

        result_frame.pack(fill=BOTH, side=TOP, expand=True)


        window.mainloop()

    #########################################################################################################################
    #########################################################################################################################
    #########################################################################################################################

    def text_based(self):
        scotland_yard_is_fun = True
        print("Type exit to reset and/or exit")
        print("#################################")
        while scotland_yard_is_fun:
            start_node = input("Starting point: ")
            if start_node == "exit":
                break

            start_node = int(start_node)
            on_the_run_in_the_dark = True
            while on_the_run_in_the_dark:
                travelmethod = input("taxi, bus, underground or black ticket? ")
                if travelmethod == "exit":
                    on_the_run_in_the_dark = False
                    break
                if travelmethod in ["taxi", "bus", "underground", "black ticket"]:
                    print(self.locator.show_options(start_node, [travelmethod]))
                else:
                    print("unknown travel option, try again!")