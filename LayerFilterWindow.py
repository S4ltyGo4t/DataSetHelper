import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import os
from PIL import Image


class LayerFilterWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.source_directory = StringVar()
        self.layerType = IntVar()

        # define gui elements
        text_description = tk.Label(self,
                                    text="Layer Filtering",
                                    fg="black",
                                    font="Arial 12 bold")

        button_next = tk.Button(self,
                                text="Filter Layer",
                                width=25,
                                command=self.execute)

        button_prev = tk.Button(self,
                                text="Zurück",
                                width=25,
                                command=self.mainWindow)

        label_source = tk.Label(self, text="Source Directory")
        dir_box_source = tk.Entry(self, textvariable=self.source_directory, state=DISABLED, text=self.source_directory,
                                  width=40)
        button_browser_source = tk.Button(self, text="Browse", command=lambda: self.callback(self.source_directory))

        # preselect middle
        self.layerType.set(0)
        label_cropType = tk.Label(self, text="Keep pictures with")

        rb_3_Layer = tk.Radiobutton(self,
                                    text="3 Layer (RGB)",
                                    variable=self.layerType,
                                    value=3)

        rb_1_Layer = tk.Radiobutton(self,
                                    text="1 Layer (B&W)",
                                    variable=self.layerType,
                                    value=1)

        # place gui elements
        text_description.grid(row=0, column=0)
        label_source.grid(row=1, column=0)
        dir_box_source.grid(row=2, column=0)
        button_browser_source.grid(row=2, column=1)

        label_cropType.grid(row=7, column=0)
        rb_3_Layer.grid(row=8, column=0)
        rb_1_Layer.grid(row=9, column=0)

        button_next.place(relx=0.99, rely=0.99, anchor=SE)
        button_prev.place(rely=0.99, anchor=SW)

    def callback(self, directory):
        filename = tk.filedialog.askdirectory()
        directory.set(filename)
        # self.dir_box["text"] = directory

    def execute(self):
        # check if all parameters are set, give information if some ware wrong
        if self.checkFields():
            # debug info remove if it works
            print("Source directory: " + self.source_directory.get())
            print("Layer type: %i" % self.layerType.get())
            try:
                # try something
                self.removeLayers(self.source_directory.get(), self.layerType.get())
                print("Succesfully executed!")
            except:
                print("Something went wrong!")
                pass

    def checkFields(self):

        if self.source_directory.get() == "":
            print(self.source_directory.get())
            messagebox.showinfo("Notification", "Please select a source and destination directory.")
            return False
        elif self.layerType.get() != 3 and self.layerType.get() != 1:
            print(self.layerType.get())
            messagebox.showinfo("Notification", "Please select a layer category you want to remove!")
            return False
        return True

    def removeLayers(self, _path, layercount):
        path = os.path.normpath(_path)
        # counters for images
        layer_3 = 0
        layer_1 = 0
        # store images to later remove them
        pictures_to_remove = []

        for dir in os.listdir(path):
            pic_path = os.path.join(path, dir)
            try:
                with Image.open(pic_path) as img:
                    # count all pictures with 1 layer and if 3 layer should be removed, store them in the remove list
                    if (img.layers == 3):
                        layer_3 = layer_3 + 1
                        if layercount == 3:
                            pictures_to_remove.append(dir)
                    # count all pictures with 1 layer and if 1 layer should be removed, store them in the remove list
                    elif (img.layers == 1):
                        layer_1 = layer_1 + 1
                        if layercount == 1:
                            pictures_to_remove.append(dir)
            except:
                pass
        if len(pictures_to_remove) > 0:
            # remove all pictures stored in the list
            print("Removing %i pictures!" % len(pictures_to_remove))
            for picture in pictures_to_remove:
                os.remove(os.path.join(path, picture))

    def mainWindow(self):
        self.controller.show_frame("MainWindow")
