import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import os
from PIL import Image


class RemoveBrokenWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.source_directory = StringVar()

        # define gui elements
        text_description = tk.Label(self,
                                    text="Remove broken pictures",
                                    fg="black",
                                    font="Arial 12 bold")

        button_next = tk.Button(self,
                                text="Remove",
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

        # place gui elements
        text_description.grid(row=0, column=0)
        label_source.grid(row=1, column=0)
        dir_box_source.grid(row=2, column=0)
        button_browser_source.grid(row=2, column=1)

        button_next.place(relx=0.99, rely=0.99, anchor=SE)
        button_prev.place(rely=0.99, anchor=SW)

    def callback(self, directory):
        filename = tk.filedialog.askdirectory()
        directory.set(filename)

    def execute(self):
        # check if all parameters are set, give information if some ware wrong
        if self.checkFields():
            # debug info remove if it works
            print("Source directory: " + self.source_directory.get())
            try:
                # try something
                self.removePictures(self.source_directory.get())
                print("Succesfully executed!")
            except:
                print("Something went wrong!")
                pass

    def checkFields(self):
        if self.source_directory.get() == "":
            print(self.source_directory.get())
            messagebox.showinfo("Notification", "Please select a source and destination directory.")
            return False
        return True

    def removePictures(self, _path):
        path = os.path.normpath(_path)
        # counters for images
        # store images to later remove them
        files_to_remove = []

        for dir in os.listdir(path):
            file_path = os.path.join(path, dir)
            if os.stat(file_path).st_size == 0:
                files_to_remove.append(dir)

            #     with Image.open(file_path) as img:
            #         #store broken pictures in to the remove list
            #         if (img.size() == 0):
            #             pictures_to_remove.append(dir)
            # except:
            #     #if some picture cant be open, remote it as well
            #     pictures_to_remove.append(dir)
            #     pass
        if len(files_to_remove) > 0:
            # remove all pictures stored in the list
            print("Removing %i pictures!" % len(files_to_remove))
            for picture in files_to_remove:
                os.remove(os.path.join(path, picture))

    def mainWindow(self):
        self.controller.show_frame("MainWindow")
