import tkinter as tk
from tkinter import *


class MainWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # define gui elements
        text_description = tk.Label(self,
                                    text="Select a Operation!",
                                    fg="black",
                                    font="Arial 12 bold")

        button_next = tk.Button(self,
                                text="Next",
                                width=25,
                                command=self.callback,
                                state=DISABLED)
        self.v = tk.IntVar()
        rb_resizeCrop = tk.Radiobutton(self,
                                       text="Resize & Crop",
                                       variable=self.v,
                                       value=1,
                                       font="Arial 12",
                                       command=lambda: self.activateButton(button_next))

        rb_layerFiltering = tk.Radiobutton(self,
                                           text="Layer Filtering",
                                           variable=self.v,
                                           value=2,
                                           font="Arial 12",
                                           command=lambda: self.activateButton(button_next))

        rb_removeBroken = tk.Radiobutton(self,
                                           text="Remove broken pictures",
                                           variable=self.v,
                                           value=3,
                                           font="Arial 12",
                                           command=lambda: self.activateButton(button_next))

        # pack gui elements
        text_description.pack(anchor=NW, pady=5)
        rb_resizeCrop.pack(anchor=NW, padx=3)
        rb_layerFiltering.pack(anchor=NW, padx=3)
        rb_removeBroken.pack(anchor=NW, padx=3)
        button_next.place(relx=0.99, rely=0.99, anchor=SE)

    def callback(self):
        if self.v.get() == 1:
            self.controller.show_frame("ResizeCropWindow")
        elif self.v.get() == 2:
            #ad if wiwndow exists
            self.controller.show_frame("LayerFilterWindow")
            pass
        elif self.v.get() == 3:
            self.controller.show_frame("RemoveBrokenWindow")
        else:
            pass


    def activateButton(self, button):
        button["state"] = "normal"