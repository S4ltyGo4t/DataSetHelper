import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import re
import os
from resizeandcrop import resize_and_crop


class ResizeCropWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.source_directory = StringVar()
        # make it from sourcepath/..
        self.destination_directory = StringVar()
        self.cropChoise = StringVar()
        self.shapeChoise = StringVar()

        # define gui elements
        text_description = tk.Label(self,
                                    text="Resize & Crop",
                                    fg="black",
                                    font="Arial 12 bold")

        button_next = tk.Button(self,
                                text="Resize",
                                width=25,
                                command=self.execute)

        button_prev = tk.Button(self,
                                text="Zurück",
                                width=25,
                                command=self.mainWindow)

        label_source = tk.Label(self, text="Source Directory")
        dir_box_source = tk.Entry(self, textvariable=self.source_directory, state=DISABLED, text=self.source_directory,
                                  width=40)
        # TODO Change Search Root
        button_browser_source = tk.Button(self, text="Browse", command=lambda: self.callback(self.source_directory))

        label_destination = tk.Label(self, text="Destination Directory")
        dir_box_destination = tk.Entry(self, textvariable=self.destination_directory, state=DISABLED,
                                       text=self.destination_directory, width=40)
        # TODO Change Search Root
        button_browser_destination = tk.Button(self, text="Browse",
                                               command=lambda: self.callback(self.destination_directory))

        label_shapeLabel = tk.Label(self, text="Label")
        label_shape = tk.Label(self, text="[width]x[height]")
        dir_box_shape = tk.Entry(self, textvariable=self.shapeChoise, text=self.shapeChoise, width=9)

        # preselect middle
        self.cropChoise.set(2)
        label_cropType = tk.Label(self, text="Crop type")
        rb_middle = tk.Radiobutton(self,
                                   text="middle",
                                   variable=self.cropChoise,
                                   value="middle")
        rb_top = tk.Radiobutton(self,
                                text="top",
                                variable=self.cropChoise,
                                value="top")
        rb_bottom = tk.Radiobutton(self,
                                   text="bottom",
                                   variable=self.cropChoise,
                                   value="bottom")

        # place gui elements
        text_description.grid(row=0, column=0)

        label_shapeLabel.grid(row=2, column=3)
        label_shape.grid(row=3, column=3)

        label_source.grid(row=1, column=0)
        dir_box_source.grid(row=2, column=0)
        button_browser_source.grid(row=2, column=1)
        dir_box_shape.grid(row=4, column=3)

        label_destination.grid(row=4, column=0)
        dir_box_destination.grid(row=5, column=0)
        button_browser_destination.grid(row=5, column=1)

        label_cropType.grid(row=7, column=0)
        rb_top.grid(row=8, column=0)
        rb_middle.grid(row=9, column=0)
        rb_bottom.grid(row=10, column=0)

        button_next.place(relx=0.99, rely=0.99, anchor=SE)
        button_prev.place(rely=0.99, anchor=SW)

    def callback(self, directory):
        filename = tk.filedialog.askdirectory()
        directory.set(filename)
        # self.dir_box["text"] = directory

    def execute(self):
        # check if all parameters are set, give information if some ware wrong
        if self.checkFields():
            # run resize and crop
            # TODO implement resize and crop
            # parse shape
            pattern_Width = re.compile("^\d+[^x]")
            pattern_Height = re.compile("\d+$")
            match_Width = pattern_Width.search(self.shapeChoise.get()).group()
            match_Height = pattern_Height.search(self.shapeChoise.get()).group()

            #debug info remove if it works
            print("Width: " + match_Width + " Height: "+match_Height)
            print("Source directory: " + self.source_directory.get())
            print("Destination directory: " + self.destination_directory.get())
            print("Crop type: " + self.cropChoise.get())

            source_path = os.path.normpath(self.source_directory.get())
            destination_path = os.path.normpath(self.destination_directory.get())
            for pic in os.listdir(source_path):
                try:
                    resize_and_crop(os.path.join(source_path, pic),
                                    os.path.join(destination_path, pic),
                                    (int(match_Width), int(match_Height)),
                                    crop_type=self.cropChoise.get())
                except:
                    pass
            print("Succesfully executed!")

    # checks if paths are set and shape is in shape []x[]
    def checkFields(self):
        pattern = re.compile("^\d+x\d+$")

        if (self.source_directory.get() == "") or (self.destination_directory.get() == ""):
            messagebox.showinfo("Notification", "Please select a source and destination directory.")
            return False
        elif not pattern.match(self.shapeChoise.get()):
            messagebox.showinfo("Notification", "Please make sure the shape looks like: [weight]x[height]")
            return False
        return True

    def mainWindow(self):
        self.controller.show_frame("MainWindow")

