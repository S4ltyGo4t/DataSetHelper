import tkinter as tk  # python 3
from tkinter import font  as tkfont  # python 3
import math
from MainWindow import MainWindow
from ResizeCropWindow import ResizeCropWindow
from LayerFilterWindow import LayerFilterWindow
from RemoveBrokenWindow import RemoveBrokenWindow


# window in which later the frames loada in
class DataSetHelper(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Times', size=18, weight="bold", slant="italic")
        self.title = "DataSet Helper"
        self.geometry("%sx%s" % (math.ceil(self.winfo_screenwidth() / 4), math.ceil(self.winfo_screenheight() / 4)))
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainWindow, ResizeCropWindow, LayerFilterWindow, RemoveBrokenWindow):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainWindow")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = DataSetHelper()
    app.mainloop()
